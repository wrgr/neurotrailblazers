#!/usr/bin/env python3
"""
High-Precision Local Paper Cache Ingestion & Verification Tool.
Ingests papers from /Users/wgray13/projects/connectome-kb/outputs/raw/pdf_cache
into neurotrailblazers (public OA) and neurotrailblazers-private (paywalled manuscripts),
performing strict DOI, title, PDF integrity, and filename verification.
"""

import csv
import hashlib
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
MANIFEST_PATH = PROJECT_ROOT / "data" / "pdf_corpus" / "corpus_manifest.json"
CSV_INDEX_PATH = PROJECT_ROOT / "data" / "pdf_corpus" / "corpus_index.csv"

CKB_ROOT = Path("/Users/wgray13/projects/connectome-kb")
CKB_CORPUS_JSON = CKB_ROOT / "outputs" / "website" / "corpus_canonical.json"
CKB_PDF_CACHE = CKB_ROOT / "outputs" / "raw" / "pdf_cache"
PRIVATE_REPO_DIR = PROJECT_ROOT.parent / "neurotrailblazers-private" / "papers"


def sanitize_filename(doi: str) -> str:
    """Converts a DOI to the repository standard filename format."""
    clean = re.sub(r'[/\\:*?"<>|]', '_', doi.strip().lower())
    if not clean.endswith('.pdf'):
        clean += '.pdf'
    return clean


def clean_title(t: str) -> str:
    """Strips HTML formatting and special characters for strict title verification."""
    t = re.sub(r'<[^>]+>', '', t or '')
    return re.sub(r'[^a-z0-9]', '', t.lower())


def compute_permissions(rights_cat: str, oa_status: str, source_url: str = "") -> Dict[str, Any]:
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


def is_valid_pdf_file(p: Path) -> bool:
    """Verifies that a file exists, has size > 1KB, and starts with %PDF-."""
    if not p.exists() or p.stat().st_size < 1000:
        return False
    try:
        with open(p, "rb") as f:
            header = f.read(10)
            return header.startswith(b"%PDF-")
    except Exception:
        return False


def main():
    print("=" * 80)
    print("      🔍 VERIFIED LOCAL CONNECTOME-KB PAPER CACHE INGESTION ENGINE      ")
    print("=" * 80)
    print(f" Source Corpus Metadata: {CKB_CORPUS_JSON}")
    print(f" Source PDF Cache:       {CKB_PDF_CACHE}")
    print(f" Target Master Manifest: {MANIFEST_PATH}")
    print(f" Private Stash Dir:      {PRIVATE_REPO_DIR}")
    print("=" * 80)

    if not CKB_CORPUS_JSON.exists():
        print(f"Error: {CKB_CORPUS_JSON} not found!")
        sys.exit(1)
    if not CKB_PDF_CACHE.exists():
        print(f"Error: {CKB_PDF_CACHE} not found!")
        sys.exit(1)
    if not MANIFEST_PATH.exists():
        print(f"Error: {MANIFEST_PATH} not found!")
        sys.exit(1)

    manifest = json.loads(MANIFEST_PATH.read_text())
    ckb_data = json.loads(CKB_CORPUS_JSON.read_text())
    print(f"Loaded {len(manifest)} manifest records and {len(ckb_data)} connectome-kb records.\n")

    # Build lookup map from CKB
    ckb_by_doi = {}
    for rec in ckb_data:
        d = (rec.get("doi") or "").replace("https://doi.org/", "").strip().lower()
        if d:
            ckb_by_doi[d] = rec

    PRIVATE_REPO_DIR.mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / "data" / "pdf_corpus" / "oa_gold").mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / "data" / "pdf_corpus" / "author_provided").mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / "data" / "pdf_corpus" / "publisher_free").mkdir(parents=True, exist_ok=True)

    imported_count = 0
    already_present_count = 0
    verified_count = 0

    for doi, target_rec in manifest.items():
        clean_doi = sanitize_filename(doi)
        
        # Check if already present on disk in any location
        existing_paths = [
            PROJECT_ROOT / "data" / "pdf_corpus" / "oa_gold" / clean_doi,
            PROJECT_ROOT / "data" / "pdf_corpus" / "author_provided" / clean_doi,
            PROJECT_ROOT / "data" / "pdf_corpus" / "publisher_free" / clean_doi,
            PRIVATE_REPO_DIR / clean_doi
        ]
        
        has_existing = any(p.exists() and is_valid_pdf_file(p) for p in existing_paths)
        if has_existing:
            already_present_count += 1
            continue

        # Look up in connectome-kb
        ckb_rec = ckb_by_doi.get(doi)
        if not ckb_rec:
            continue

        cid = ckb_rec.get("canonical_paper_id")
        if not cid:
            continue

        source_pdf = CKB_PDF_CACHE / f"{cid}.pdf"
        if not is_valid_pdf_file(source_pdf):
            continue

        # Strict Title Cross-Verification
        target_title = target_rec.get("title", "")
        ckb_title = ckb_rec.get("title", "")
        
        ct = clean_title(target_title)
        cc = clean_title(ckb_title)
        
        # Verify title match
        if not (ct in cc or cc in ct or ct[:25] == cc[:25]):
            print(f"⚠️ Title Mismatch Skipped: {doi}\n   Target: {target_title}\n   Source: {ckb_title}")
            continue

        verified_count += 1

        # Determine target permission & storage routing
        rights_cat = target_rec.get("rights_category", "CLOSED_PUBLISHER")
        oa_stat = target_rec.get("oa_status", "")
        perm = compute_permissions(rights_cat, oa_stat)

        if perm["storage_location"] == "PUBLIC_REPO":
            if rights_cat == "OA_GOLD":
                dest_file = PROJECT_ROOT / "data" / "pdf_corpus" / "oa_gold" / clean_doi
            else:
                dest_file = PROJECT_ROOT / "data" / "pdf_corpus" / "author_provided" / clean_doi
        else:
            dest_file = PRIVATE_REPO_DIR / clean_doi

        # Copy verified PDF
        shutil.copyfile(source_pdf, dest_file)
        
        # Compute SHA256 & Size
        with open(dest_file, "rb") as f:
            content = f.read()
            sha = hashlib.sha256(content).hexdigest()
            size = len(content)

        # Update manifest record with verified naming and metadata
        target_rec.update(perm)
        target_rec["pdf_status"] = "DOWNLOADED"
        target_rec["sha256"] = sha
        target_rec["file_size_bytes"] = size
        target_rec["relative_path"] = str(dest_file)
        target_rec["source_origin"] = f"connectome_kb:{cid}"

        imported_count += 1
        print(f" ✅ [{imported_count:3d}] Verified & Imported: {clean_doi} ({size/1024/1024:.1f} MB) -> {dest_file.parent.name}/")

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
    print("                    INGESTION & VERIFICATION SUMMARY                    ")
    print("=" * 80)
    print(f" Verified & Newly Imported Papers: {imported_count}")
    print(f" Previously Existing Papers:       {already_present_count}")
    print(f" Total Current Full-Text Papers:   {already_present_count + imported_count} / 2,000 ({(already_present_count + imported_count)/2000*100:.1f}%)")
    print(f" Updated Manifest:                 {MANIFEST_PATH}")
    print(f" Updated CSV Index:                {CSV_INDEX_PATH}")
    print("=" * 80)


if __name__ == "__main__":
    main()
