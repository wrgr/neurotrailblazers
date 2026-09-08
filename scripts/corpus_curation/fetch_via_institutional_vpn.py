#!/usr/bin/env python3
"""
Institutional VPN & Proxy Batch Manuscript Fetcher.
Designed for downloading the remaining 632 paywalled papers using university network access
(Campus VPN, EZProxy, or on-campus IP connection).
Downloads full-text PDFs directly into ../neurotrailblazers-private/papers/
with strict naming and SHA-256 validation.
"""

import argparse
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

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/pdf,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def sanitize_filename(doi: str) -> str:
    clean = re.sub(r'[/\\:*?"<>|]', '_', doi.strip().lower())
    if not clean.endswith('.pdf'):
        clean += '.pdf'
    return clean


def is_valid_pdf(data: bytes) -> bool:
    return len(data) >= 1000 and data.startswith(b"%PDF-")


def build_publisher_candidate_urls(doi: str, ezproxy_prefix: Optional[str] = None) -> List[str]:
    """Constructs direct publisher landing & PDF download links."""
    candidates = []
    doi_clean = doi.strip()

    # Direct DOI resolution
    doi_url = f"https://doi.org/{urllib.parse.quote(doi_clean)}"
    if ezproxy_prefix:
        doi_url = f"{ezproxy_prefix.rstrip('/')}/{doi_url}"
    candidates.append(doi_url)

    # Springer / Nature
    if "10.1038/" in doi_clean or "10.1007/" in doi_clean or "10.1186/" in doi_clean:
        candidates.append(f"https://link.springer.com/content/pdf/{doi_clean}.pdf")
        candidates.append(f"https://www.nature.com/articles/{doi_clean.split('/')[-1]}.pdf")

    # Elsevier / ScienceDirect / Cell Press / Neuron
    if "10.1016/" in doi_clean:
        candidates.append(f"https://www.sciencedirect.com/science/article/pii/{doi_clean.split('/')[-1]}/pdfft?isDTMRedir=true&download=true")

    # Wiley Online Library
    if "10.1002/" in doi_clean or "10.1111/" in doi_clean:
        candidates.append(f"https://onlinelibrary.wiley.com/doi/pdfdirect/{doi_clean}")

    # Science / AAAS
    if "10.1126/" in doi_clean:
        candidates.append(f"https://www.science.org/doi/pdf/{doi_clean}")

    # PNAS
    if "10.1073/" in doi_clean:
        candidates.append(f"https://www.pnas.org/doi/pdf/{doi_clean}")

    # Oxford University Press
    if "10.1093/" in doi_clean:
        candidates.append(f"https://academic.oup.com/doi/pdf/{doi_clean}")

    # Apply EZProxy prefix if specified
    if ezproxy_prefix:
        prefixed = []
        for u in candidates:
            if not u.startswith(ezproxy_prefix):
                prefixed.append(f"{ezproxy_prefix.rstrip('/')}/{u}")
            else:
                prefixed.append(u)
        return prefixed

    return candidates


def download_paper(doi: str, dest_file: Path, ezproxy_prefix: Optional[str] = None) -> Tuple[bool, Optional[str], Optional[int], Optional[str]]:
    candidate_urls = build_publisher_candidate_urls(doi, ezproxy_prefix)
    for u in candidate_urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=12, context=SSL_CTX) as resp:
                content = resp.read()
                if is_valid_pdf(content):
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(dest_file, "wb") as f:
                        f.write(content)
                    sha = hashlib.sha256(content).hexdigest()
                    return True, sha, len(content), u
        except Exception:
            continue
    return False, None, None, None


def main():
    parser = argparse.ArgumentParser(description="Batch paywalled paper fetcher via institutional VPN or Proxy")
    parser.add_argument("--ezproxy-prefix", type=str, default=None,
                        help="Optional EZProxy prefix (e.g. https://proxy.library.jhu.edu/login?url=)")
    parser.add_argument("--max-workers", type=int, default=8, help="Concurrent worker threads")
    args = parser.parse_args()

    print("=" * 80)
    print("      🏛️ INSTITUTIONAL NETWORK BATCH MANUSCRIPT RETRIEVAL ENGINE        ")
    print("=" * 80)
    print(f" Target Private Stash: {PRIVATE_REPO_DIR}")
    if args.ezproxy_prefix:
        print(f" EZProxy Prefix:       {args.ezproxy_prefix}")
    else:
        print(" Mode:                 Direct Campus VPN / Institutional IP Space")
    print("=" * 80)

    if not MANIFEST_PATH.exists():
        print(f"Error: {MANIFEST_PATH} not found!")
        sys.exit(1)

    manifest = json.loads(MANIFEST_PATH.read_text())
    unresolved = [rec for rec in manifest.values() if rec.get("pdf_status") != "DOWNLOADED"]
    print(f"Found {len(unresolved)} unresolved papers to fetch via institutional access.\n")

    if not unresolved:
        print("All 2,000 papers in the corpus are already downloaded! Nothing to do.")
        return

    PRIVATE_REPO_DIR.mkdir(parents=True, exist_ok=True)
    success_count = 0

    def process_rec(rec):
        doi = rec["doi"]
        clean_doi = sanitize_filename(doi)
        dest_file = PRIVATE_REPO_DIR / clean_doi

        if dest_file.exists() and dest_file.stat().st_size > 1000:
            rec["pdf_status"] = "DOWNLOADED"
            rec["relative_path"] = str(dest_file)
            return rec, True

        ok, sha, size, used_u = download_paper(doi, dest_file, args.ezproxy_prefix)
        if ok:
            rec["pdf_status"] = "DOWNLOADED"
            rec["sha256"] = sha
            rec["file_size_bytes"] = size
            rec["storage_location"] = "PRIVATE_DEV_REPO"
            rec["license_type"] = "All-Rights-Reserved-Paywalled"
            rec["terms_of_use_notice"] = "Institutional access / paywalled; local research & RAG indexing only."
            rec["relative_path"] = str(dest_file)
            rec["downloaded_source_url"] = used_u
            return rec, True
        return rec, False

    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = {executor.submit(process_rec, rec): rec for rec in unresolved}
        for fut in as_completed(futures):
            rec, ok = fut.result()
            manifest[rec["doi"]] = rec
            if ok:
                success_count += 1
                print(f" ✅ [{success_count:3d}] Downloaded: {sanitize_filename(rec['doi'])} ({rec.get('file_size_bytes', 0)/1024/1024:.1f} MB)")

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
    print("\n" + "=" * 80)
    print(f" Institutional Fetch Complete: {success_count} / {len(unresolved)} papers downloaded.")
    print("=" * 80)


if __name__ == "__main__":
    main()
