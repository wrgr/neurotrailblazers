#!/usr/bin/env python3
"""
Connectomics Corpus PDF Retrieval & Rights-Classification Engine.
Downloads, verifies, indexes, and categorizes papers from the 2,000-paper corpus
into strict licensing tiers (OA Gold, Author-Provided Green, Publisher Free, Closed Metadata).
"""

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
from typing import Dict, Any, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
CORPUS_JSON = PROJECT_ROOT / "data" / "corpus_2000.json"
TARGET_DIR = PROJECT_ROOT / "data" / "pdf_corpus"

DIR_OA_GOLD = TARGET_DIR / "oa_gold"
DIR_AUTHOR_PROVIDED = TARGET_DIR / "author_provided"
DIR_PUBLISHER_FREE = TARGET_DIR / "publisher_free"
DIR_CLOSED_META = TARGET_DIR / "closed_metadata"

MANIFEST_PATH = TARGET_DIR / "corpus_manifest.json"
CSV_INDEX_PATH = TARGET_DIR / "corpus_index.csv"

# Bypass SSL verify issues if any mirror has self-signed/expired cert
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/pdf,application/octet-stream,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}


def sanitize_filename(doi: str) -> str:
    """Converts a DOI to a filesystem-safe filename."""
    clean = re.sub(r'[/\\:*?"<>|]', '_', doi.strip().lower())
    if not clean.endswith('.pdf'):
        clean += '.pdf'
    return clean


def classify_rights(paper: Dict[str, Any]) -> str:
    """
    Classifies paper redistribution rights:
    - OA_GOLD: Explicit open licenses (PLOS, eLife, Nature Comms, BioMed Central)
    - AUTHOR_PROVIDED: Author manuscripts, preprints, PMC Green OA (bioRxiv, arXiv, PMC)
    - PUBLISHER_FREE: Bronze / Hybrid free-to-read on publisher portal without explicit open redistribution license
    - CLOSED_PUBLISHER: Subscription / Paywalled literature
    """
    oa_status = (paper.get("oa_status") or "").lower()
    pdf_url = (paper.get("pdf_url") or "").lower()
    doi = (paper.get("doi") or "").lower()

    if oa_status in ["gold", "diamond"]:
        return "OA_GOLD"
    
    if "biorxiv" in pdf_url or "arxiv" in pdf_url or "pmc" in pdf_url or "europepmc" in pdf_url or oa_status == "green":
        return "AUTHOR_PROVIDED"
    
    if oa_status in ["bronze", "hybrid"]:
        return "PUBLISHER_FREE"
    
    if not paper.get("pdf_url") or oa_status in ["closed", ""]:
        return "CLOSED_PUBLISHER"
    
    return "PUBLISHER_FREE"


def is_valid_pdf_data(data: bytes) -> bool:
    """Verifies that bytes begin with the standard PDF magic signature (%PDF-)."""
    return len(data) >= 1000 and data.startswith(b"%PDF-")


def download_single_paper(paper: Dict[str, Any], existing_manifest: Dict[str, Any]) -> Dict[str, Any]:
    doi = paper.get("doi") or paper.get("id")
    norm_doi = doi.strip().lower()
    rights = classify_rights(paper)
    filename = sanitize_filename(norm_doi)

    # Determine target subfolder
    if rights == "OA_GOLD":
        target_dir = DIR_OA_GOLD
    elif rights == "AUTHOR_PROVIDED":
        target_dir = DIR_AUTHOR_PROVIDED
    elif rights == "PUBLISHER_FREE":
        target_dir = DIR_PUBLISHER_FREE
    else:
        target_dir = DIR_CLOSED_META

    target_file = target_dir / filename
    meta_stub_file = DIR_CLOSED_META / (filename.replace(".pdf", ".json"))

    record = {
        "id": paper.get("id"),
        "doi": norm_doi,
        "title": paper.get("title"),
        "authors": paper.get("authors") or (paper.get("authors_short") if isinstance(paper.get("authors_short"), str) else ""),
        "year": paper.get("year"),
        "journal": paper.get("journal"),
        "dimension": paper.get("dimension"),
        "tier": paper.get("tier", 2000),
        "rights_category": rights,
        "pdf_url": paper.get("pdf_url"),
        "landing_url": paper.get("landing_url") or f"https://doi.org/{norm_doi}",
        "filename": filename if rights != "CLOSED_PUBLISHER" else None,
        "relative_path": str(target_file.relative_to(PROJECT_ROOT)) if rights != "CLOSED_PUBLISHER" else None,
        "pdf_status": "PENDING",
        "file_size_bytes": 0,
        "sha256": None,
        "error": None
    }

    # If closed, save metadata stub and return
    if rights == "CLOSED_PUBLISHER" or not paper.get("pdf_url"):
        record["pdf_status"] = "CLOSED_METADATA_ONLY"
        with open(meta_stub_file, "w", encoding="utf-8") as mf:
            json.dump(record, mf, indent=2)
        return record

    # Check if already downloaded and valid
    if target_file.exists() and target_file.stat().st_size > 1000:
        try:
            with open(target_file, "rb") as tf:
                head = tf.read(1024)
                if head.startswith(b"%PDF-"):
                    tf.seek(0)
                    h = hashlib.sha256(tf.read()).hexdigest()
                    record["pdf_status"] = "DOWNLOADED"
                    record["file_size_bytes"] = target_file.stat().st_size
                    record["sha256"] = h
                    return record
        except Exception:
            pass

    # Download from pdf_url
    pdf_url = paper["pdf_url"]
    candidate_urls = [pdf_url]
    
    # Add fallback mirrors if available (e.g. Europe PMC if DOI starts with PMC)
    if "ncbi.nlm.nih.gov/pmc/articles/" in pdf_url:
        pmc_id = re.search(r'PMC\d+', pdf_url)
        if pmc_id:
            candidate_urls.append(f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmc_id.group(0)}&blobtype=pdf")

    success = False
    for url in candidate_urls:
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20, context=SSL_CTX) as resp:
                content = resp.read()
                if is_valid_pdf_data(content):
                    with open(target_file, "wb") as out_f:
                        out_f.write(content)
                    
                    record["pdf_status"] = "DOWNLOADED"
                    record["file_size_bytes"] = len(content)
                    record["sha256"] = hashlib.sha256(content).hexdigest()
                    success = True
                    break
                else:
                    record["error"] = f"Invalid PDF signature (received {content[:50]!r})"
        except Exception as e:
            record["error"] = str(e)
            time.sleep(0.3)

    if not success:
        record["pdf_status"] = "FAILED"
        if target_file.exists():
            try: target_file.unlink()
            except Exception: pass

    return record


def main():
    print("=" * 70)
    print("NeuroTrailblazers Connectomics Corpus PDF Retrieval Engine")
    print("=" * 70)

    for d in [DIR_OA_GOLD, DIR_AUTHOR_PROVIDED, DIR_PUBLISHER_FREE, DIR_CLOSED_META]:
        d.mkdir(parents=True, exist_ok=True)

    if not CORPUS_JSON.exists():
        print(f"Error: {CORPUS_JSON} not found!")
        sys.exit(1)

    with open(CORPUS_JSON, "r", encoding="utf-8") as f:
        corpus_data = json.load(f)

    papers = corpus_data.get("papers", [])
    print(f"Loaded {len(papers)} papers from corpus_2000.json.")

    existing_manifest = {}
    if MANIFEST_PATH.exists():
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as mf:
                existing_manifest = json.load(mf)
            print(f"Loaded {len(existing_manifest)} existing records from manifest.")
        except Exception:
            existing_manifest = {}

    results = {}
    total = len(papers)
    completed = 0
    downloaded_count = 0
    closed_count = 0
    failed_count = 0

    print(f"\nStarting parallel retrieval across {total} papers (10 workers)...")
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_paper = {
            executor.submit(download_single_paper, p, existing_manifest): p
            for p in papers
        }

        for fut in as_completed(future_to_paper):
            completed += 1
            rec = fut.result()
            results[rec["doi"]] = rec

            if rec["pdf_status"] == "DOWNLOADED":
                downloaded_count += 1
            elif rec["pdf_status"] == "CLOSED_METADATA_ONLY":
                closed_count += 1
            else:
                failed_count += 1

            if completed % 100 == 0 or completed == total:
                elapsed = time.time() - start_time
                print(f"  [{completed}/{total} - {completed/total*100:.1f}%] Downloaded: {downloaded_count} | Closed/Meta: {closed_count} | Failed: {failed_count} | ({elapsed:.1f}s)")

    # Write Master Manifest
    with open(MANIFEST_PATH, "w", encoding="utf-8") as mf:
        json.dump(results, mf, indent=2)
    print(f"\nSaved master manifest to: {MANIFEST_PATH}")

    # Write CSV Index
    fieldnames = [
        "doi", "rights_category", "pdf_status", "title", "authors", "year",
        "journal", "dimension", "tier", "file_size_bytes", "sha256", "relative_path", "pdf_url", "landing_url"
    ]
    with open(CSV_INDEX_PATH, "w", encoding="utf-8", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        for rec in sorted(results.values(), key=lambda r: (r.get("rights_category") or "", r.get("doi") or "")):
            row = {k: rec.get(k) for k in fieldnames}
            writer.writerow(row)
    print(f"Saved master CSV index to: {CSV_INDEX_PATH}")

    # Generate Summary Audit
    oa_gold_files = list(DIR_OA_GOLD.glob("*.pdf"))
    author_files = list(DIR_AUTHOR_PROVIDED.glob("*.pdf"))
    pub_free_files = list(DIR_PUBLISHER_FREE.glob("*.pdf"))
    closed_stubs = list(DIR_CLOSED_META.glob("*.json"))

    print("\n" + "=" * 70)
    print("CORPUS RETRIEVAL & RIGHTS CLASSIFICATION SUMMARY")
    print("=" * 70)
    print(f"Total Papers Processed:               {total}")
    print(f"  ├── Gold Open Access PDFs (OA_GOLD):          {len(oa_gold_files)}")
    print(f"  ├── Author Preprints / PMC (AUTHOR_PROVIDED): {len(author_files)}")
    print(f"  ├── Publisher Free / Bronze (PUBLISHER_FREE): {len(pub_free_files)}")
    print(f"  ├── Closed Metadata Stubs (CLOSED_PUBLISHER): {len(closed_stubs)}")
    print(f"  └── Total Local PDFs Downloaded:              {len(oa_gold_files) + len(author_files) + len(pub_free_files)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
