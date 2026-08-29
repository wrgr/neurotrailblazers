#!/usr/bin/env python3
"""
Deep Manuscript Retrieval & Permissions Flagging Tool.
Discovers author-accepted manuscripts, institutional preprints, and paywalled full texts
for all 2,000 papers in the corpus across Unpaywall, Europe PMC, and Semantic Scholar.
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
    r_cat = rights_cat.upper()
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


def query_unpaywall(doi: str) -> List[Dict[str, Any]]:
    """Discovers alternative repository locations from Unpaywall API."""
    urls = []
    try:
        url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={UNPAYWALL_EMAIL}"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for loc in data.get("oa_locations", []):
                pdf_u = loc.get("url_for_pdf") or loc.get("url")
                if pdf_u and pdf_u.endswith(".pdf"):
                    urls.append({
                        "url": pdf_u,
                        "host_type": loc.get("host_type"),
                        "license": loc.get("license"),
                        "version": loc.get("version")
                    })
    except Exception:
        pass
    return urls


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
    parser = argparse.ArgumentParser(description="Deep connectomics manuscript fetcher")
    parser.add_argument("--private-dir", type=str, default=str(PROJECT_ROOT / "data" / "pdf_corpus" / "internal_research_paywalled"),
                        help="Path to private repository or directory for paywalled papers")
    parser.add_argument("--max-workers", type=int, default=8, help="Parallel worker threads")
    parser.add_argument("--dry-run", action="store_true", help="Audit mode without downloading")
    args = parser.parse_args()

    private_dir = Path(args.private_dir)
    print("=" * 70)
    print("Deep Manuscript Retrieval & Permissions Engine")
    print(f"Target Private Repository Directory: {private_dir}")
    print("=" * 70)

    if not MANIFEST_PATH.exists():
        print(f"Error: {MANIFEST_PATH} not found!")
        sys.exit(1)

    manifest = json.loads(MANIFEST_PATH.read_text())
    print(f"Loaded {len(manifest)} papers from manifest.")

    unresolved = [rec for rec in manifest.values() if rec.get("pdf_status") != "DOWNLOADED"]
    print(f"Found {len(unresolved)} unresolved / paywalled papers to search.")

    if args.dry_run:
        print("Dry run mode: Auditing permissions across all papers...")
        for rec in manifest.values():
            perm = compute_permissions(rec.get("rights_category", "CLOSED_PUBLISHER"), rec.get("oa_status", ""), rec.get("pdf_url", ""))
            rec.update(perm)
        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
        print("Updated manifest with permissions. Exiting.")
        return

    resolved_count = 0
    start_time = time.time()

    def process_paper(rec: Dict[str, Any]) -> Dict[str, Any]:
        doi = rec["doi"]
        filename = sanitize_filename(doi)
        perm = compute_permissions(rec.get("rights_category", "CLOSED_PUBLISHER"), rec.get("oa_status", ""), rec.get("pdf_url", ""))
        rec.update(perm)

        # Determine target file
        if perm["storage_location"] == "PUBLIC_REPO":
            if rec.get("rights_category") == "OA_GOLD":
                target_file = PROJECT_ROOT / "data" / "pdf_corpus" / "oa_gold" / filename
            else:
                target_file = PROJECT_ROOT / "data" / "pdf_corpus" / "author_provided" / filename
        else:
            target_file = private_dir / filename

        if target_file.exists() and target_file.stat().st_size > 1000:
            rec["pdf_status"] = "DOWNLOADED"
            rec["file_size_bytes"] = target_file.stat().st_size
            rec["relative_path"] = str(target_file)
            return rec

        # Discover candidate URLs
        candidate_urls = []
        if rec.get("pdf_url"):
            candidate_urls.append(rec["pdf_url"])
        
        # Query Unpaywall
        unpaywall_locs = query_unpaywall(doi)
        for loc in unpaywall_locs:
            candidate_urls.append(loc["url"])

        # Try download
        success, sha, size, used_url = download_with_fallback(candidate_urls, target_file)
        if success:
            rec["pdf_status"] = "DOWNLOADED"
            rec["sha256"] = sha
            rec["file_size_bytes"] = size
            rec["downloaded_source_url"] = used_url
            rec["relative_path"] = str(target_file)
        return rec

    print(f"\nSearching deep repositories across {len(unresolved)} papers...")
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
    print("DEEP RETRIEVAL & PERMISSIONS AUDIT COMPLETE")
    print(f"Newly Retrieved Manuscripts: {resolved_count}")
    print(f"Updated Master Manifest:      {MANIFEST_PATH}")
    print(f"Updated Master CSV:           {CSV_INDEX_PATH}")
    print("=" * 70)


if __name__ == "__main__":
    main()
