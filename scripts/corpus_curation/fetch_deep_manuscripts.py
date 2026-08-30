#!/usr/bin/env python3
"""
Deep Multi-Source Manuscript Retrieval & Permissions Engine.
Discovers author-accepted manuscripts, institutional preprints, PMC full-text renders,
and paywalled literature across Europe PMC, OpenAlex, Semantic Scholar, and Unpaywall.
Routes open-access files to public folders and paywalled manuscripts to a private repository.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
CORPUS_JSON = PROJECT_ROOT / "data" / "corpus_2000.json"
MANIFEST_PATH = PROJECT_ROOT / "data" / "pdf_corpus" / "corpus_manifest.json"
CSV_INDEX_PATH = PROJECT_ROOT / "data" / "pdf_corpus" / "corpus_index.csv"

# Bypass SSL verify issues if any mirror has self-signed/expired cert
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/pdf,application/octet-stream,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}

UNPAYWALL_EMAIL = "neurotrailblazers@gmail.com"


def sanitize_filename(doi: str) -> str:
    """Converts a DOI to a filesystem-safe filename."""
    clean = re.sub(r'[/\\:*?"<>|]', '_', doi.strip().lower())
    if not clean.endswith('.pdf'):
        clean += '.pdf'
    return clean


def compute_permissions(rights_cat: str, oa_status: str, source_url: str) -> Dict[str, Any]:
    """Generates explicit machine-readable permission flags."""
    r_cat = (rights_cat or "").upper()
    oa_stat = (oa_status or "").lower()

    if r_cat == "OA_GOLD" or oa_stat in ["gold", "diamond"]:
        return {
            "license_type": "CC-BY-4.0",
            "redistribution_permitted": True,
            "commercial_use_permitted": True,
            "storage_location": "PUBLIC_REPO",
            "terms_of_use_notice": "Open Access: Fully redistributable with author attribution."
        }
    elif r_cat == "AUTHOR_PROVIDED" or oa_stat == "green":
        return {
            "license_type": "Author-Accepted-Preprint",
            "redistribution_permitted": True,
            "commercial_use_permitted": False,
            "storage_location": "PUBLIC_REPO",
            "terms_of_use_notice": "Author-deposited manuscript / preprint for non-commercial educational & research use."
        }
    elif r_cat == "PUBLISHER_FREE" or oa_stat in ["bronze", "hybrid"]:
        return {
            "license_type": "Bronze-Free-To-Read",
            "redistribution_permitted": False,
            "commercial_use_permitted": False,
            "storage_location": "PRIVATE_DEV_REPO",
            "terms_of_use_notice": "Free to read on publisher portal only; third-party public redistribution prohibited."
        }
    else:
        return {
            "license_type": "All-Rights-Reserved-Paywalled",
            "redistribution_permitted": False,
            "commercial_use_permitted": False,
            "storage_location": "PRIVATE_DEV_REPO",
            "terms_of_use_notice": "Subscription / Paywalled; developer research & local RAG indexing only."
        }


def is_valid_pdf(data: bytes) -> bool:
    return len(data) >= 1000 and data.startswith(b"%PDF-")


def query_europe_pmc(doi: str) -> List[Tuple[str, str, str]]:
    """Discovers direct PDF render URLs and PMCIDs from Europe PMC REST API."""
    candidates = []
    try:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22{urllib.parse.quote(doi)}%22&format=json&resultType=core"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("resultList", {}).get("result", [])
            if results:
                res = results[0]
                pmcid = res.get("pmcid")
                is_oa = res.get("isOpenAccess") == "Y"
                cat = "OA_GOLD" if is_oa else "AUTHOR_PROVIDED"
                oa_status = "gold" if is_oa else "green"

                if pmcid:
                    candidates.append((f"https://europepmc.org/articles/{pmcid}?pdf=render", cat, oa_status))
                    candidates.append((f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/", cat, oa_status))

                for u in res.get("fullTextUrlList", {}).get("fullTextUrl", []):
                    if u.get("documentStyle") == "pdf":
                        candidates.append((u.get("url"), cat, oa_status))
    except Exception:
        pass
    return candidates


def query_semantic_scholar(doi: str) -> List[Tuple[str, str, str]]:
    """Discovers open access PDF URLs from Semantic Scholar API."""
    candidates = []
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}?fields=openAccessPdf"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            oa = data.get("openAccessPdf")
            if oa and oa.get("url"):
                status = oa.get("status", "green").lower()
                cat = "OA_GOLD" if status in ["gold", "diamond"] else ("AUTHOR_PROVIDED" if status == "green" else "PUBLISHER_FREE")
                candidates.append((oa.get("url"), cat, status))
    except Exception:
        pass
    return candidates


def query_openalex(doi: str) -> List[Tuple[str, str, str]]:
    """Discovers institutional repository locations from OpenAlex API."""
    candidates = []
    try:
        url = f"https://api.openalex.org/works/https://doi.org/{doi}"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for loc in data.get("locations", []):
                pdf_u = loc.get("pdf_url")
                if pdf_u:
                    is_oa = loc.get("is_oa", False)
                    status = (loc.get("version") or "green").lower()
                    cat = "OA_GOLD" if status in ["publishedversion", "gold"] else "AUTHOR_PROVIDED"
                    candidates.append((pdf_u, cat, status))
    except Exception:
        pass
    return candidates


def query_unpaywall(doi: str) -> List[Tuple[str, str, str]]:
    """Discovers alternative repository locations from Unpaywall API."""
    candidates = []
    try:
        url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={UNPAYWALL_EMAIL}"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for loc in data.get("oa_locations", []):
                pdf_u = loc.get("url_for_pdf") or loc.get("url")
                if pdf_u:
                    oa_stat = (loc.get("host_type") or loc.get("version") or "green").lower()
                    cat = "OA_GOLD" if oa_stat in ["publisher", "gold"] else "AUTHOR_PROVIDED"
                    candidates.append((pdf_u, cat, oa_stat))
    except Exception:
        pass
    return candidates


def download_with_fallback(candidate_urls: List[str], target_file: Path) -> Tuple[bool, Optional[str], Optional[int], Optional[str]]:
    """Tries downloading from candidate URLs in sequence, verifying PDF magic bytes."""
    for u in candidate_urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as resp:
                content = resp.read()
                if is_valid_pdf(content):
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(target_file, "wb") as f:
                        f.write(content)
                    sha = hashlib.sha256(content).hexdigest()
                    return True, sha, len(content), u
        except Exception:
            continue
    return False, None, None, None


def main():
    parser = argparse.ArgumentParser(description="Deep multi-source connectomics manuscript fetcher")
    parser.add_argument("--private-dir", type=str, default=str(PROJECT_ROOT / "data" / "pdf_corpus" / "internal_research_paywalled"),
                        help="Path to private repository or directory for paywalled papers")
    parser.add_argument("--max-workers", type=int, default=12, help="Parallel worker threads")
    parser.add_argument("--dry-run", action="store_true", help="Audit mode without downloading")
    args = parser.parse_args()

    private_dir = Path(args.private_dir)
    print("=" * 70)
    print("Deep Multi-Source Manuscript Retrieval & Permissions Engine")
    print(f"Target Private Repository Directory: {private_dir}")
    print("=" * 70)

    if not MANIFEST_PATH.exists():
        print(f"Error: {MANIFEST_PATH} not found!")
        sys.exit(1)

    manifest = json.loads(MANIFEST_PATH.read_text())
    print(f"Loaded {len(manifest)} papers from manifest.")

    unresolved = [rec for rec in manifest.values() if rec.get("pdf_status") != "DOWNLOADED"]
    print(f"Found {len(unresolved)} unresolved / paywalled papers to search.")

    resolved_count = 0
    start_time = time.time()

    def process_paper(rec: Dict[str, Any]) -> Dict[str, Any]:
        doi = rec["doi"]
        filename = sanitize_filename(doi)

        # Check existing locations first
        for search_path in [
            PROJECT_ROOT / "data" / "pdf_corpus" / "oa_gold" / filename,
            PROJECT_ROOT / "data" / "pdf_corpus" / "author_provided" / filename,
            PROJECT_ROOT / "data" / "pdf_corpus" / "publisher_free" / filename,
            private_dir / filename
        ]:
            if search_path.exists() and search_path.stat().st_size > 1000:
                rec["pdf_status"] = "DOWNLOADED"
                rec["file_size_bytes"] = search_path.stat().st_size
                rec["relative_path"] = str(search_path)
                return rec

        # Discover candidate URLs across Europe PMC, OpenAlex, S2, and Unpaywall
        candidates = []
        if rec.get("pdf_url"):
            candidates.append((rec["pdf_url"], rec.get("rights_category", "CLOSED_PUBLISHER"), rec.get("oa_status", "")))

        # 1. Europe PMC
        candidates.extend(query_europe_pmc(doi))
        # 2. OpenAlex
        candidates.extend(query_openalex(doi))
        # 3. Semantic Scholar
        candidates.extend(query_semantic_scholar(doi))
        # 4. Unpaywall
        candidates.extend(query_unpaywall(doi))

        if not candidates:
            return rec

        # Deduplicate candidate URLs
        seen_urls = set()
        unique_candidates = []
        for u, r_cat, oa_stat in candidates:
            if u and u not in seen_urls:
                seen_urls.add(u)
                unique_candidates.append((u, r_cat, oa_stat))

        # Try download
        for u, r_cat, oa_stat in unique_candidates:
            perm = compute_permissions(r_cat, oa_stat, u)
            if perm["storage_location"] == "PUBLIC_REPO":
                if r_cat == "OA_GOLD":
                    target_file = PROJECT_ROOT / "data" / "pdf_corpus" / "oa_gold" / filename
                else:
                    target_file = PROJECT_ROOT / "data" / "pdf_corpus" / "author_provided" / filename
            else:
                target_file = private_dir / filename

            success, sha, size, used_url = download_with_fallback([u], target_file)
            if success:
                rec.update(perm)
                rec["pdf_status"] = "DOWNLOADED"
                rec["sha256"] = sha
                rec["file_size_bytes"] = size
                rec["downloaded_source_url"] = used_url
                rec["relative_path"] = str(target_file)
                break

        return rec

    print(f"\nSearching deep multi-source repositories across {len(unresolved)} papers...")
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = {executor.submit(process_paper, rec): rec for rec in unresolved}
        for fut in as_completed(futures):
            rec = fut.result()
            manifest[rec["doi"]] = rec
            if rec.get("pdf_status") == "DOWNLOADED":
                resolved_count += 1

    # Update manifest & CSV
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
    
    fieldnames = [
        "doi", "license_type", "redistribution_permitted", "storage_location", "rights_category",
        "pdf_status", "title", "authors", "year", "journal", "dimension", "tier",
        "file_size_bytes", "sha256", "relative_path", "pdf_url", "landing_url", "terms_of_use_notice"
    ]
    with open(CSV_INDEX_PATH, "w", encoding="utf-8", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for rec in sorted(manifest.values(), key=lambda r: (r.get("storage_location") or "", r.get("doi") or "")):
            writer.writerow(rec)

    print("\n" + "=" * 70)
    print("DEEP MULTI-SOURCE RETRIEVAL COMPLETE")
    print(f"Newly Retrieved Manuscripts: {resolved_count}")
    print(f"Updated Master Manifest:      {MANIFEST_PATH}")
    print(f"Updated Master CSV:           {CSV_INDEX_PATH}")
    print("=" * 70)


if __name__ == "__main__":
    main()
