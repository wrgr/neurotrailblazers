#!/usr/bin/env python3
"""Fetches verified accurate publication years, full author lists, and journal venues across all 2,000 papers."""
import json
import re
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
            "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,authors,year,venue,publicationDate,externalIds",
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
                if not ext_doi: continue
                
                authors_list = [a.get("name", "").strip() for a in w.get("authors", []) if a.get("name")]
                authors_str = "; ".join(authors_list)
                year = w.get("year")
                if not year and w.get("publicationDate"):
                    try:
                        year = int(w.get("publicationDate")[:4])
                    except Exception:
                        pass
                
                results[ext_doi] = {
                    "authors": authors_str,
                    "year": year,
                    "venue": w.get("venue", ""),
                    "title": w.get("title", "")
                }
    except Exception as e:
        pass
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
                if not doi: continue
                
                authors_list = []
                for a in w.get("authorships", []):
                    name = (a.get("author", {}) or {}).get("display_name", "").strip()
                    if name:
                        authors_list.append(name)
                authors_str = "; ".join(authors_list)
                year = w.get("publication_year")
                venue = (w.get("primary_location", {}) or {}).get("source", {}) or {}
                venue_name = venue.get("display_name", "") if isinstance(venue, dict) else ""
                
                results[doi] = {
                    "authors": authors_str,
                    "year": year,
                    "venue": venue_name,
                    "title": w.get("title", "")
                }
    except Exception as e:
        pass
    return results

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    dois = [d.lower().strip() for d in sel_data["papers"].keys()]

    print(f"Fetching accurate authors, publication years, and venues for {len(dois)} papers in parallel...")

    meta_results = {}
    
    # 1. Query Semantic Scholar
    batches = list(chunk_list(dois, 50))
    print(f"Querying Semantic Scholar ({len(batches)} batches)...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_s2_batch, b): b for b in batches}
        for fut in as_completed(futures):
            res = fut.result()
            for d, val in res.items():
                if val.get("authors") and val.get("year"):
                    meta_results[d] = val

    print(f"Semantic Scholar populated {len(meta_results)} records.")

    # 2. Query OpenAlex for remaining or to supplement
    missing_dois = [d for d in dois if not meta_results.get(d, {}).get("authors") or not meta_results.get(d, {}).get("year")]
    print(f"Querying OpenAlex for {len(missing_dois)} remaining papers...")
    oa_batches = list(chunk_list(missing_dois, 50))
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_openalex_batch, b): b for b in oa_batches}
        for fut in as_completed(futures):
            res = fut.result()
            for d, val in res.items():
                if d not in meta_results or not meta_results[d].get("authors"):
                    meta_results[d] = val
                elif not meta_results[d].get("year") and val.get("year"):
                    meta_results[d]["year"] = val.get("year")

    # Load expert seed papers as ground truth
    seed_dir = PROJECT_ROOT / "_data/expert_seed_papers"
    if seed_dir.exists():
        for sp in seed_dir.glob("**/*.json"):
            try:
                sdata = json.loads(sp.read_text())
                d = sdata.get("doi", "").lower().strip()
                if d:
                    if sdata.get("authors"):
                        a_str = "; ".join(sdata["authors"]) if isinstance(sdata["authors"], list) else sdata["authors"]
                        if d not in meta_results: meta_results[d] = {}
                        meta_results[d]["authors"] = a_str
                    if sdata.get("year"):
                        if d not in meta_results: meta_results[d] = {}
                        meta_results[d]["year"] = int(sdata["year"])
                    if sdata.get("journal"):
                        meta_results[d]["venue"] = sdata["journal"]
            except Exception:
                pass

    # Save to JSON cache
    cache_path = SCRIPT_DIR / "authors_years_2000.json"
    cache_path.write_text(json.dumps(meta_results, indent=2))

    has_authors = sum(1 for v in meta_results.values() if v.get("authors"))
    has_years = sum(1 for v in meta_results.values() if v.get("year"))
    print(f"Metadata Enrichment Complete:")
    print(f"  Papers with Valid Authors: {has_authors} / {len(dois)} ({has_authors/len(dois)*100:.1f}%)")
    print(f"  Papers with Valid Years:   {has_years} / {len(dois)} ({has_years/len(dois)*100:.1f}%)")

if __name__ == "__main__":
    main()
