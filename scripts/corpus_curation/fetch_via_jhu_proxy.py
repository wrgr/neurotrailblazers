#!/usr/bin/env python3
"""
Johns Hopkins University (JHU) EZProxy Direct Batch Manuscript Fetcher.
Uses JHU Sheridan Libraries EZProxy session token with domain rewriting
to authenticate and download paywalled literature into ../neurotrailblazers-private/papers/.
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

PROXY_HOST = "proxy1.library.jhu.edu"

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


def to_jhu_proxy_url(original_url: str) -> str:
    """Rewrites a standard hostname into a JHU EZProxy subdomain."""
    parsed = urllib.parse.urlparse(original_url)
    host = parsed.netloc
    proxied_host = f"{host.replace('.', '-')}.{PROXY_HOST}"
    return urllib.parse.urlunparse((parsed.scheme, proxied_host, parsed.path, parsed.params, parsed.query, parsed.fragment))


def build_jhu_proxied_urls(doi: str) -> List[str]:
    doi_clean = doi.strip()
    urls = []

    # 1. Nature Publishing Group
    if "10.1038/" in doi_clean:
        suffix = doi_clean.split("10.1038/")[-1]
        urls.append(f"https://www-nature-com.{PROXY_HOST}/articles/{suffix}.pdf")
        urls.append(f"https://link-springer-com.{PROXY_HOST}/content/pdf/{doi_clean}.pdf")

    # 2. SpringerLink
    if "10.1007/" in doi_clean or "10.1186/" in doi_clean:
        urls.append(f"https://link-springer-com.{PROXY_HOST}/content/pdf/{doi_clean}.pdf")

    # 3. Science / AAAS
    if "10.1126/" in doi_clean:
        urls.append(f"https://www-science-org.{PROXY_HOST}/doi/pdf/{doi_clean}")

    # 4. Elsevier / ScienceDirect / Cell Press / Neuron
    if "10.1016/" in doi_clean:
        urls.append(f"https://www-sciencedirect-com.{PROXY_HOST}/science/article/pii/{doi_clean.split('/')[-1]}/pdfft?isDTMRedir=true&download=true")
        urls.append(f"https://www-sciencedirect-com.{PROXY_HOST}/science/article/pii/{doi_clean.split('/')[-1]}")
        urls.append(f"https://www-cell-com.{PROXY_HOST}/action/showPdf?pii={doi_clean.split('/')[-1]}")

    # 5. Wiley Online Library / JCN
    if "10.1002/" in doi_clean or "10.1111/" in doi_clean:
        urls.append(f"https://onlinelibrary-wiley-com.{PROXY_HOST}/doi/pdfdirect/{doi_clean}")
        urls.append(f"https://onlinelibrary-wiley-com.{PROXY_HOST}/doi/pdf/{doi_clean}")

    # 6. PNAS
    if "10.1073/" in doi_clean:
        urls.append(f"https://www-pnas-org.{PROXY_HOST}/doi/pdf/{doi_clean}")

    # 7. Oxford Academic / Cerebral Cortex
    if "10.1093/" in doi_clean:
        urls.append(f"https://academic-oup-com.{PROXY_HOST}/doi/pdf/{doi_clean}")

    # 8. Annual Reviews
    if "10.1146/" in doi_clean:
        urls.append(f"https://www-annualreviews-org.{PROXY_HOST}/doi/pdf/{doi_clean}")

    # 9. Royal Society
    if "10.1098/" in doi_clean:
        urls.append(f"https://royalsocietypublishing-org.{PROXY_HOST}/doi/pdf/{doi_clean}")

    # 10. J. Neuroscience / eLife / Frontiers
    if "10.1523/" in doi_clean:
        urls.append(f"https://www-jneurosci-org.{PROXY_HOST}/content/jneuro/{doi_clean.split('10.1523/')[-1]}.full.pdf")

    # 11. General DOI EZProxy login resolver
    urls.append(f"https://{PROXY_HOST}/login?url=https://doi.org/{urllib.parse.quote(doi_clean)}")

    return urls


def download_via_jhu_token(doi: str, dest_file: Path, token: str) -> Tuple[bool, Optional[str], Optional[int], Optional[str]]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/pdf,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": f"ezproxy={token.strip()}; EZPROXY_SESSION={token.strip()}; session={token.strip()}"
    }

    candidate_urls = build_jhu_proxied_urls(doi)
    for u in candidate_urls:
        try:
            req = urllib.request.Request(u, headers=headers)
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
    parser = argparse.ArgumentParser(description="JHU EZProxy Direct Batch Paywalled Manuscript Fetcher")
    parser.add_argument("--token", type=str, default=None, help="JHU EZProxy session token")
    parser.add_argument("--cookie-file", type=str, default="jhu_cookie.txt", help="Path to cookie/token file")
    parser.add_argument("--max-workers", type=int, default=10, help="Concurrent worker threads")
    args = parser.parse_args()

    token_val = args.token or os.environ.get("JHU_EZPROXY_TOKEN")
    cookie_p = PROJECT_ROOT / args.cookie_file if not Path(args.cookie_file).is_absolute() else Path(args.cookie_file)
    if not token_val and cookie_p.exists():
        token_val = cookie_p.read_text().strip()

    if not token_val:
        print("Error: No JHU EZProxy session token provided via --token, --cookie-file, or JHU_EZPROXY_TOKEN!")
        sys.exit(1)

    print("=" * 80)
    print("      🏛️ JOHNS HOPKINS UNIVERSITY (JHU) DIRECT BATCH MANUSCRIPT RETRIEVER      ")
    print("=" * 80)
    print(f" Target Private Stash: {PRIVATE_REPO_DIR}")
    print(f" JHU Session Token:    {token_val[:6]}...{token_val[-4:]} [AUTHENTICATED]")
    print(f" Parallel Workers:     {args.max_workers}")
    print("=" * 80)

    if not MANIFEST_PATH.exists():
        print(f"Error: {MANIFEST_PATH} not found!")
        sys.exit(1)

    manifest = json.loads(MANIFEST_PATH.read_text())
    unresolved = [rec for rec in manifest.values() if rec.get("pdf_status") != "DOWNLOADED"]
    print(f"Found {len(unresolved)} unresolved papers to fetch via JHU Sheridan Libraries.\n")

    if not unresolved:
        print("All 2,000 papers in the corpus are already downloaded! Nothing to do.")
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

        ok, sha, size, used_u = download_via_jhu_token(doi, dest_file, token_val)
        if ok:
            rec["pdf_status"] = "DOWNLOADED"
            rec["sha256"] = sha
            rec["file_size_bytes"] = size
            rec["storage_location"] = "PRIVATE_DEV_REPO"
            rec["license_type"] = "All-Rights-Reserved-Paywalled"
            rec["terms_of_use_notice"] = "JHU Institutional Access / Paywalled; developer research & local RAG indexing only."
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
                print(f" ✅ [{success_count:3d}] Downloaded via JHU: {sanitize_filename(rec['doi'])} ({rec.get('file_size_bytes', 0)/1024/1024:.1f} MB)")

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
    print("                     JHU RETRIEVAL RUN COMPLETE                         ")
    print("=" * 80)
    print(f" Newly Downloaded Papers:  {success_count} / {len(unresolved)}")
    print(f" Total Downloaded Corpus:  {sum(1 for r in manifest.values() if r.get('pdf_status') == 'DOWNLOADED')} / 2,000")
    print(f" Private Stash Directory:  {PRIVATE_REPO_DIR}")
    print("=" * 80)


if __name__ == "__main__":
    main()
