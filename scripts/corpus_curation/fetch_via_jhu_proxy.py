#!/usr/bin/env python3
"""
Johns Hopkins University (JHU) EZProxy Batch Manuscript Fetcher.
Allows downloading paywalled literature via JHU Sheridan Libraries EZProxy
using an authenticated session cookie (JHED SSO) or JHU IP authentication.
Saves retrieved PDFs directly into ../neurotrailblazers-private/papers/
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

# JHU EZProxy Endpoints
JHU_PROXY_PREFIX = "https://proxy1.library.jhu.edu/login?url="

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE


def sanitize_filename(doi: str) -> str:
    clean = re.sub(r'[/\\:*?"<>|]', '_', doi.strip().lower())
    if not clean.endswith('.pdf'):
        clean += '.pdf'
    return clean


def is_valid_pdf(data: bytes) -> bool:
    return len(data) >= 1000 and data.startswith(b"%PDF-")


def build_jhu_urls(doi: str) -> List[str]:
    """Generates direct publisher URLs routed through JHU EZProxy."""
    doi_clean = doi.strip()
    candidates = []

    # 1. Direct DOI through proxy
    candidates.append(f"{JHU_PROXY_PREFIX}https://doi.org/{urllib.parse.quote(doi_clean)}")

    # 2. Nature / Springer through JHU Proxy
    if "10.1038/" in doi_clean or "10.1007/" in doi_clean or "10.1186/" in doi_clean:
        candidates.append(f"{JHU_PROXY_PREFIX}https://link.springer.com/content/pdf/{doi_clean}.pdf")
        candidates.append(f"{JHU_PROXY_PREFIX}https://www.nature.com/articles/{doi_clean.split('/')[-1]}.pdf")

    # 3. ScienceDirect / Cell Press / Neuron through JHU Proxy
    if "10.1016/" in doi_clean:
        candidates.append(f"{JHU_PROXY_PREFIX}https://www.sciencedirect.com/science/article/pii/{doi_clean.split('/')[-1]}/pdfft?isDTMRedir=true&download=true")

    # 4. Science / AAAS through JHU Proxy
    if "10.1126/" in doi_clean:
        candidates.append(f"{JHU_PROXY_PREFIX}https://www.science.org/doi/pdf/{doi_clean}")

    # 5. Wiley through JHU Proxy
    if "10.1002/" in doi_clean or "10.1111/" in doi_clean:
        candidates.append(f"{JHU_PROXY_PREFIX}https://onlinelibrary.wiley.com/doi/pdfdirect/{doi_clean}")

    # 6. PNAS through JHU Proxy
    if "10.1073/" in doi_clean:
        candidates.append(f"{JHU_PROXY_PREFIX}https://www.pnas.org/doi/pdf/{doi_clean}")

    # 7. Oxford Academic through JHU Proxy
    if "10.1093/" in doi_clean:
        candidates.append(f"{JHU_PROXY_PREFIX}https://academic.oup.com/doi/pdf/{doi_clean}")

    return candidates


def download_via_jhu(doi: str, dest_file: Path, cookie_str: Optional[str] = None) -> Tuple[bool, Optional[str], Optional[int], Optional[str]]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/pdf,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    if cookie_str:
        headers["Cookie"] = cookie_str.strip()

    urls = build_jhu_urls(doi)
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as resp:
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
    parser = argparse.ArgumentParser(description="JHU EZProxy Batch Paywalled Manuscript Fetcher")
    parser.add_argument("--cookie", type=str, default=None,
                        help="JHU EZProxy cookie string (e.g. ezproxy=...; JSESSIONID=...)")
    parser.add_argument("--cookie-file", type=str, default=None,
                        help="Path to file containing JHU cookie string")
    parser.add_argument("--max-workers", type=int, default=8, help="Concurrent worker threads")
    args = parser.parse_args()

    cookie_val = args.cookie or os.environ.get("JHU_EZPROXY_COOKIE")
    if args.cookie_file and Path(args.cookie_file).exists():
        cookie_val = Path(args.cookie_file).read_text().strip()

    print("=" * 80)
    print("      🏛️ JOHNS HOPKINS UNIVERSITY (JHU) BATCH MANUSCRIPT RETRIEVER      ")
    print("=" * 80)
    print(f" Proxy Endpoint:       {JHU_PROXY_PREFIX}")
    print(f" Target Private Stash: {PRIVATE_REPO_DIR}")
    print(f" Session Cookie:       {'[LOADED]' if cookie_val else '[NONE - Direct IP Mode]'}")
    print("=" * 80)

    if not MANIFEST_PATH.exists():
        print(f"Error: {MANIFEST_PATH} not found!")
        sys.exit(1)

    manifest = json.loads(MANIFEST_PATH.read_text())
    unresolved = [rec for rec in manifest.values() if rec.get("pdf_status") != "DOWNLOADED"]
    print(f"Loaded {len(unresolved)} unresolved papers to fetch.\n")

    if not unresolved:
        print("All papers already downloaded! Nothing to do.")
        return

    PRIVATE_REPO_DIR.mkdir(parents=True, exist_ok=True)
    success_count = 0

    def process_paper(rec):
        doi = rec["doi"]
        clean_doi = sanitize_filename(doi)
        dest_file = PRIVATE_REPO_DIR / clean_doi

        if dest_file.exists() and dest_file.stat().st_size > 1000:
            rec["pdf_status"] = "DOWNLOADED"
            rec["relative_path"] = str(dest_file)
            return rec, True

        ok, sha, size, used_u = download_via_jhu(doi, dest_file, cookie_val)
        if ok:
            rec["pdf_status"] = "DOWNLOADED"
            rec["sha256"] = sha
            rec["file_size_bytes"] = size
            rec["storage_location"] = "PRIVATE_DEV_REPO"
            rec["license_type"] = "All-Rights-Reserved-Paywalled"
            rec["terms_of_use_notice"] = "JHU Institutional Subscription / Paywalled; local research & RAG indexing only."
            rec["relative_path"] = str(dest_file)
            rec["downloaded_source_url"] = used_u
            rec["source_origin"] = "jhu_ezproxy"
            return rec, True
        return rec, False

    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = {executor.submit(process_paper, rec): rec for rec in unresolved}
        for fut in as_completed(futures):
            rec, ok = fut.result()
            manifest[rec["doi"]] = rec
            if ok:
                success_count += 1
                print(f" ✅ [{success_count:3d}] Downloaded: {sanitize_filename(rec['doi'])} ({rec.get('file_size_bytes', 0)/1024/1024:.1f} MB)")

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
    print("\n" + "=" * 80)
    print(f" JHU Retrieval Complete: {success_count} / {len(unresolved)} papers downloaded.")
    print("=" * 80)


if __name__ == "__main__":
    main()
