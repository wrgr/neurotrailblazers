#!/usr/bin/env python3
"""
Exhaustive Multi-Engine Retrieval for Remaining Unresolved Papers.
Applies:
1. NCBI PubMed Central (E-utilities) ID resolver for NIH public-access papers
2. Direct bioRxiv/medRxiv preprint full-text streams
3. Europe PMC Core REST API
4. Semantic Scholar & OpenAlex multi-location resolvers
5. Title-matched local connectome-kb ingestion
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
MANIFEST_PATH = PROJECT_ROOT / "data" / "pdf_corpus" / "corpus_manifest.json"
CSV_INDEX_PATH = PROJECT_ROOT / "data" / "pdf_corpus" / "corpus_index.csv"
PRIVATE_REPO_DIR = PROJECT_ROOT.parent / "neurotrailblazers-private" / "papers"

CKB_ROOT = Path("/Users/wgray13/projects/connectome-kb")
CKB_CORPUS_JSON = CKB_ROOT / "outputs" / "website" / "corpus_canonical.json"
CKB_PDF_CACHE = CKB_ROOT / "outputs" / "raw" / "pdf_cache"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 (mailto:neurotrailblazers@gmail.com)",
    "Accept": "application/pdf,application/octet-stream,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}


def sanitize_filename(doi: str) -> str:
    clean = re.sub(r'[/\\:*?"<>|]', '_', doi.strip().lower())
    if not clean.endswith('.pdf'):
        clean += '.pdf'
    return clean


def clean_title(t: str) -> str:
    t = re.sub(r'<[^>]+>', '', t or '')
    return re.sub(r'[^a-z0-9]', '', t.lower())


def is_valid_pdf(data: bytes) -> bool:
    return len(data) >= 1000 and data.startswith(b"%PDF-")


def compute_permissions(rights_cat: str, oa_status: str, source_url: str = "") -> Dict[str, Any]:
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
    elif r_cat == "AUTHOR_PROVIDED" or oa_stat == "green" or "biorxiv" in source_url or "arxiv" in source_url or "pmc" in source_url:
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


def resolve_ncbi_pmc(doi: str) -> List[Tuple[str, str, str]]:
    """Resolves DOIs to PMCIDs using NCBI E-utilities API."""
    candidates = []
    try:
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term={urllib.parse.quote(doi)}&retmode=json"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode())
            id_list = data.get("esearchresult", {}).get("idlist", [])
            for pmcid in id_list:
                candidates.append((f"https://europepmc.org/articles/PMC{pmcid}?pdf=render", "AUTHOR_PROVIDED", "green"))
                candidates.append((f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmcid}/pdf/", "AUTHOR_PROVIDED", "green"))
    except Exception:
        pass
    return candidates


def resolve_biorxiv(doi: str) -> List[Tuple[str, str, str]]:
    """Generates direct biorxiv / medrxiv PDF URLs."""
    candidates = []
    if "10.1101/" in doi:
        suffix = doi.split("10.1101/")[-1].strip()
        candidates.append((f"https://www.biorxiv.org/content/10.1101/{suffix}.full.pdf", "AUTHOR_PROVIDED", "green"))
        candidates.append((f"https://www.medrxiv.org/content/10.1101/{suffix}.full.pdf", "AUTHOR_PROVIDED", "green"))
    return candidates


def resolve_europe_pmc(doi: str) -> List[Tuple[str, str, str]]:
    candidates = []
    try:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22{urllib.parse.quote(doi)}%22&format=json&resultType=core"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode())
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


def resolve_semantic_scholar(doi: str) -> List[Tuple[str, str, str]]:
    candidates = []
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{doi}?fields=openAccessPdf"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode())
            oa = data.get("openAccessPdf")
            if oa and oa.get("url"):
                status = oa.get("status", "green").lower()
                cat = "OA_GOLD" if status in ["gold", "diamond"] else "AUTHOR_PROVIDED"
                candidates.append((oa.get("url"), cat, status))
    except Exception:
        pass
    return candidates


def resolve_openalex(doi: str) -> List[Tuple[str, str, str]]:
    candidates = []
    try:
        url = f"https://api.openalex.org/works/https://doi.org/{doi}"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode())
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


def download_with_fallback(candidate_urls: List[str], target_file: Path) -> Tuple[bool, Optional[str], Optional[int], Optional[str]]:
    for u in candidate_urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=12, context=SSL_CTX) as resp:
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
    print("=" * 80)
    print("      🚀 EXHAUSTIVE MULTI-ENGINE RETRIEVAL FOR REMAINING PAPERS         ")
    print("=" * 80)

    manifest = json.loads(MANIFEST_PATH.read_text())
    unresolved = [rec for rec in manifest.values() if rec.get("pdf_status") != "DOWNLOADED"]
    print(f"Loaded master manifest: {len(manifest)} total papers.")
    print(f"Targeting all {len(unresolved)} remaining unresolved papers with exhaustive discovery...\n")

    # Step 1: Check title-based matches in local connectome-kb
    title_matches_imported = 0
    if CKB_CORPUS_JSON.exists() and CKB_PDF_CACHE.exists():
        ckb_data = json.loads(CKB_CORPUS_JSON.read_text())
        ckb_by_title = {}
        for rec in ckb_data:
            cid = rec.get("canonical_paper_id")
            t = clean_title(rec.get("title", ""))
            if t and cid:
                src_f = CKB_PDF_CACHE / f"{cid}.pdf"
                if src_f.exists() and src_f.stat().st_size > 1000:
                    ckb_by_title[t[:35]] = (rec, src_f)

        for rec in unresolved:
            doi = rec["doi"]
            clean_doi = sanitize_filename(doi)
            t = clean_title(rec.get("title", ""))
            if t[:35] in ckb_by_title:
                ckb_rec, src_f = ckb_by_title[t[:35]]
                perm = compute_permissions(rec.get("rights_category", "CLOSED_PUBLISHER"), rec.get("oa_status", ""))
                dest = (PROJECT_ROOT / "data" / "pdf_corpus" / "oa_gold" / clean_doi) if perm["storage_location"] == "PUBLIC_REPO" and rec.get("rights_category") == "OA_GOLD" else ((PROJECT_ROOT / "data" / "pdf_corpus" / "author_provided" / clean_doi) if perm["storage_location"] == "PUBLIC_REPO" else (PRIVATE_REPO_DIR / clean_doi))
                
                dest.parent.mkdir(parents=True, exist_ok=True)
                with open(src_f, "rb") as sf:
                    content = sf.read()
                    if is_valid_pdf(content):
                        with open(dest, "wb") as df:
                            df.write(content)
                        rec.update(perm)
                        rec["pdf_status"] = "DOWNLOADED"
                        rec["sha256"] = hashlib.sha256(content).hexdigest()
                        rec["file_size_bytes"] = len(content)
                        rec["relative_path"] = str(dest)
                        rec["source_origin"] = f"connectome_kb_title_match:{ckb_rec.get('canonical_paper_id')}"
                        title_matches_imported += 1
                        print(f" ✅ [Local Title Match] Imported: {clean_doi} -> {dest.parent.name}/")

    print(f"\nImported {title_matches_imported} local title-matched papers from cache.")
    unresolved = [rec for rec in manifest.values() if rec.get("pdf_status") != "DOWNLOADED"]
    print(f"Proceeding to online multi-engine retrieval across remaining {len(unresolved)} papers...\n")

    online_resolved_count = 0

    def process_paper(rec: Dict[str, Any]) -> Dict[str, Any]:
        doi = rec["doi"]
        clean_doi = sanitize_filename(doi)

        candidates = []
        if rec.get("pdf_url"):
            candidates.append((rec["pdf_url"], rec.get("rights_category", "CLOSED_PUBLISHER"), rec.get("oa_status", "")))

        # 1. NCBI E-utilities (PMC)
        candidates.extend(resolve_ncbi_pmc(doi))
        # 2. bioRxiv/medRxiv
        candidates.extend(resolve_biorxiv(doi))
        # 3. Europe PMC
        candidates.extend(resolve_europe_pmc(doi))
        # 4. OpenAlex
        candidates.extend(resolve_openalex(doi))
        # 5. Semantic Scholar
        candidates.extend(resolve_semantic_scholar(doi))

        if not candidates:
            return rec

        seen_urls = set()
        unique = []
        for u, r_cat, oa_stat in candidates:
            if u and u not in seen_urls:
                seen_urls.add(u)
                unique.append((u, r_cat, oa_stat))

        for u, r_cat, oa_stat in unique:
            perm = compute_permissions(r_cat, oa_stat, u)
            if perm["storage_location"] == "PUBLIC_REPO":
                dest_file = (PROJECT_ROOT / "data" / "pdf_corpus" / "oa_gold" / clean_doi) if r_cat == "OA_GOLD" else (PROJECT_ROOT / "data" / "pdf_corpus" / "author_provided" / clean_doi)
            else:
                dest_file = PRIVATE_REPO_DIR / clean_doi

            ok, sha, size, used_u = download_with_fallback([u], dest_file)
            if ok:
                rec.update(perm)
                rec["pdf_status"] = "DOWNLOADED"
                rec["sha256"] = sha
                rec["file_size_bytes"] = size
                rec["relative_path"] = str(dest_file)
                rec["downloaded_source_url"] = used_u
                break
        return rec

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(process_paper, rec): rec for rec in unresolved}
        for fut in as_completed(futures):
            rec = fut.result()
            manifest[rec["doi"]] = rec
            if rec.get("pdf_status") == "DOWNLOADED":
                online_resolved_count += 1
                print(f" 🌐 [Online Resolved] {sanitize_filename(rec['doi'])} ({rec.get('file_size_bytes', 0)/1024/1024:.1f} MB) -> {rec.get('storage_location')}")

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

    print("\n" + "=" * 80)
    print("                 EXHAUSTIVE DISCOVERY RUN COMPLETE                      ")
    print("=" * 80)
    print(f" Newly Discovered Online: {online_resolved_count}")
    print(f" Newly Imported Local:    {title_matches_imported}")
    print(f" Total Downloaded Corpus: {sum(1 for r in manifest.values() if r.get('pdf_status') == 'DOWNLOADED')} / 2,000")
    print("=" * 80)


if __name__ == "__main__":
    main()
