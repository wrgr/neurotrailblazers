#!/usr/bin/env python3
"""Pulls full unabridged abstracts from Europe PMC and bioRxiv for any remaining papers."""
import concurrent.futures
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

def fetch_europepmc_abstract(doi: str) -> Optional[str]:
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"{urllib.parse.quote(doi)}\"&format=json&resultType=core"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("resultList", {}).get("result", [])
            if results:
                ab = results[0].get("abstractText", "")
                # Clean HTML tags
                ab_clean = re.sub(r"<[^>]+>", "", ab).strip()
                if len(ab_clean) >= 100:
                    return ab_clean
    except Exception:
        pass
    return None

def fetch_biorxiv_abstract(doi: str) -> Optional[str]:
    url = f"https://api.biorxiv.org/details/biorxiv/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            collection = data.get("collection", [])
            if collection:
                ab = collection[-1].get("abstract", "")
                ab_clean = re.sub(r"<[^>]+>", "", ab).strip()
                if len(ab_clean) >= 100:
                    return ab_clean
    except Exception:
        pass
    return None

def resolve_remaining(doi: str) -> Tuple[str, Optional[str]]:
    time.sleep(0.02)
    # 1. Europe PMC
    ab = fetch_europepmc_abstract(doi)
    if not ab and ("10.1101/" in doi or "biorxiv" in doi.lower()):
        # 2. bioRxiv
        ab = fetch_biorxiv_abstract(doi)
    return doi, ab

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    papers = sel_data["papers"]
    
    full_abs_path = SCRIPT_DIR / "full_abstracts_2000.json"
    abstracts = json.loads(full_abs_path.read_text()) if full_abs_path.exists() else {}

    missing_dois = [d for d in papers if d.lower() not in abstracts]
    print(f"=== EUROPE PMC / BIORXIV PARALLEL RESOLVER FOR {len(missing_dois)} REMAINING PAPERS ===\n", flush=True)

    start_t = time.time()
    resolved = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(resolve_remaining, d): d for d in missing_dois}
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            doi, ab = future.result()
            if ab:
                abstracts[doi.lower()] = ab
                resolved += 1
            if i % 50 == 0 or i == len(missing_dois):
                print(f"  Processed {i}/{len(missing_dois)} papers (Resolved {resolved} new full abstracts)...", flush=True)

    elapsed = time.time() - start_t
    print(f"\nFinished in {elapsed:.2f}s! Total Full Abstracts Acquired = {len(abstracts)} / {len(papers)} ({len(abstracts)/len(papers)*100:.1f}%).\n", flush=True)

    # Synchronize all final datasets
    meta_path = SCRIPT_DIR / "expanded_corpus_meta.json"
    meta_data = json.loads(meta_path.read_text()) if meta_path.exists() else {}

    for doi, p in papers.items():
        d_low = doi.lower()
        if d_low in abstracts:
            full_ab = abstracts[d_low]
            p["abstract"] = full_ab
            if doi in meta_data:
                meta_data[doi]["abstract"] = full_ab

    # Save to disk
    sel_path.write_text(json.dumps(sel_data, indent=2))
    meta_path.write_text(json.dumps(meta_data, indent=2))
    full_abs_path.write_text(json.dumps(abstracts, indent=2))
    
    # Re-materialize all corpus tiers
    for tier_size, flag in [(500, "in_top_500"), (1000, "in_top_1000"), (2000, "in_top_2000")]:
        tier_papers = [p for p in papers.values() if p.get(flag)]
        tier_papers.sort(key=lambda p: (p["classification"], -p["linkage_score"]))
        out_file = PROJECT_ROOT / f"_data/corpus_{tier_size}.json"
        out_file.write_text(json.dumps({
            "tier": tier_size,
            "count": len(tier_papers),
            "papers": tier_papers
        }, indent=2))

    print("Successfully synchronized all full abstracts across final_selection.json, _data/corpus_*.json, and full_abstracts_2000.json!", flush=True)

if __name__ == "__main__":
    main()
