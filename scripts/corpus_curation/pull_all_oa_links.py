#!/usr/bin/env python3
"""Batch pulls Open Access (OA) PDF URLs, licenses, and landing links across all 2,000 papers."""
import json
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, Any, List

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

OPENALEX_KEY = "ZkzbbRa1YqEiHetWMeS8pp"
S2_KEY = "s2k-j7ugxHdmg19KzcNVbJBMIVc56ZFyN01awklHX6Q8"

def chunk_list(lst: List[Any], chunk_size: int):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def fetch_s2_batch(batch_dois: List[str]) -> Dict[str, Dict[str, Any]]:
    results = {}
    try:
        payload = json.dumps({"ids": [f"DOI:{d}" for d in batch_dois]}).encode("utf-8")
        req = urllib.request.Request(
            "https://api.semanticscholar.org/graph/v1/paper/batch?fields=openAccessPdf,url,isOpenAccess,externalIds",
            data=payload,
            headers={
                "x-api-key": S2_KEY,
                "Content-Type": "application/json",
                "User-Agent": "NeuroTrailblazers/1.0"
            }
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for w in data:
                if not w: continue
                ext_doi = (w.get("externalIds", {}).get("DOI") or "").strip().lower()
                oa_pdf = w.get("openAccessPdf") or {}
                pdf_url = oa_pdf.get("url") if isinstance(oa_pdf, dict) else None
                status = oa_pdf.get("status") if isinstance(oa_pdf, dict) else None
                is_oa = w.get("isOpenAccess", False) or bool(pdf_url)
                
                if ext_doi:
                    results[ext_doi] = {
                        "pdf_url": pdf_url,
                        "is_oa": is_oa,
                        "oa_status": status,
                        "source": "s2"
                    }
    except Exception as e:
        print(f"  [S2 batch error]: {e}")
    return results

def fetch_openalex_batch(batch_dois: List[str]) -> Dict[str, Dict[str, Any]]:
    results = {}
    try:
        oa_filter = "|".join([f"https://doi.org/{d}" for d in batch_dois])
        url = f"https://api.openalex.org/works?filter=doi:{urllib.parse.quote(oa_filter)}&api_key={OPENALEX_KEY}&per_page=50"
        req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for w in data.get("results", []):
                doi = (w.get("doi") or "").replace("https://doi.org/", "").strip().lower()
                best_oa = w.get("best_oa_location") or {}
                oa_info = w.get("open_access") or {}
                
                pdf_url = best_oa.get("pdf_url") or oa_info.get("oa_url")
                is_oa = oa_info.get("is_oa", False) or bool(pdf_url)
                oa_status = oa_info.get("oa_status")
                
                if doi:
                    results[doi] = {
                        "pdf_url": pdf_url,
                        "is_oa": is_oa,
                        "oa_status": oa_status,
                        "landing_url": best_oa.get("landing_page_url") or f"https://doi.org/{doi}",
                        "source": "openalex"
                    }
    except Exception as e:
        print(f"  [OpenAlex batch error]: {e}")
    return results

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    dois = [d.lower().strip() for d in sel_data["papers"].keys()]

    print(f"Starting comprehensive OA pass across all {len(dois)} papers in parallel...")

    oa_results = {}
    
    # 1. Query Semantic Scholar Batch API (50 per batch)
    batches = list(chunk_list(dois, 50))
    print(f"Querying Semantic Scholar ({len(batches)} batches)...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_s2_batch, b): b for b in batches}
        for fut in as_completed(futures):
            res = fut.result()
            for d, val in res.items():
                if d not in oa_results or not oa_results[d].get("pdf_url"):
                    oa_results[d] = val

    print(f"Semantic Scholar identified {len(oa_results)} works; {sum(1 for v in oa_results.values() if v.get('pdf_url'))} direct PDF links.")

    # 2. Query OpenAlex Batch API to find additional / missing OA PDFs
    missing_pdf_dois = [d for d in dois if not oa_results.get(d, {}).get("pdf_url")]
    print(f"Querying OpenAlex for {len(missing_pdf_dois)} remaining papers...")
    oa_batches = list(chunk_list(missing_pdf_dois, 50))
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_openalex_batch, b): b for b in oa_batches}
        for fut in as_completed(futures):
            res = fut.result()
            for d, val in res.items():
                if val.get("pdf_url"):
                    oa_results[d] = val
                elif d not in oa_results:
                    oa_results[d] = val

    # Save to JSON
    out_oa_path = SCRIPT_DIR / "oa_links_2000.json"
    out_oa_path.write_text(json.dumps(oa_results, indent=2))
    
    total_oa = sum(1 for v in oa_results.values() if v.get("is_oa"))
    total_pdf = sum(1 for v in oa_results.values() if v.get("pdf_url"))
    
    print(f"OA Pass Complete!")
    print(f"  Total Open Access Papers: {total_oa} / {len(dois)} ({total_oa/len(dois)*100:.1f}%)")
    print(f"  Direct PDF Download URLs: {total_pdf} / {len(dois)} ({total_pdf/len(dois)*100:.1f}%)")

if __name__ == "__main__":
    main()
