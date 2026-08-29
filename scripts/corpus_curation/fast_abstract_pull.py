#!/usr/bin/env python3
"""High-speed dual-authenticated abstract extractor using OpenAlex API Key + Semantic Scholar API Key + PubMed."""
import concurrent.futures
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

OPENALEX_API_KEY = os.environ.get("OPENALEX_API_KEY", "ZkzbbRa1YqEiHetWMeS8pp")
S2_API_KEY = os.environ.get("S2_API_KEY", "s2k-j7ugxHdmg19KzcNVbJBMIVc56ZFyN01awklHX6Q8")

def fetch_openalex_batch(dois: List[str]) -> Dict[str, str]:
    if not dois: return {}
    doi_filter = "|".join([f"https://doi.org/{d}" for d in dois])
    url = f"https://api.openalex.org/works?filter=doi:{urllib.parse.quote(doi_filter)}&select=doi,abstract_inverted_index&per_page=50&api_key={OPENALEX_API_KEY}"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    res = {}
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for item in data.get("results", []):
                full_doi = item.get("doi", "")
                if full_doi:
                    clean_doi = full_doi.replace("https://doi.org/", "").strip().lower()
                    inv = item.get("abstract_inverted_index")
                    if inv:
                        words = []
                        for word, pos_list in inv.items():
                            for pos in pos_list:
                                words.append((pos, word))
                        words.sort()
                        full_abs = " ".join([w[1] for w in words])
                        if len(full_abs) >= 150:
                            res[clean_doi] = full_abs
    except Exception:
        pass
    return res

def fetch_s2_single(doi: str) -> Optional[str]:
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{urllib.parse.quote(doi)}?fields=abstract"
    req = urllib.request.Request(url, headers={
        "x-api-key": S2_API_KEY,
        "User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"
    })
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            ab = data.get("abstract")
            if ab and len(ab.strip()) >= 150:
                return ab.strip()
    except Exception:
        pass
    return None

def fetch_pubmed_single(doi: str) -> Optional[str]:
    esearch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(doi)}[doi]&retmode=json"
    req = urllib.request.Request(esearch_url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            id_list = data.get("esearchresult", {}).get("idlist", [])
            if id_list:
                pmid = id_list[0]
                efetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
                req_ef = urllib.request.Request(efetch_url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
                with urllib.request.urlopen(req_ef, timeout=6) as ef_resp:
                    xml_root = ET.fromstring(ef_resp.read())
                    abs_nodes = xml_root.findall(".//AbstractText")
                    if abs_nodes:
                        abs_text = " ".join(["".join(node.itertext()).strip() for node in abs_nodes])
                        if len(abs_text.strip()) >= 150:
                            return abs_text.strip()
    except Exception:
        pass
    return None

def fetch_crossref_single(doi: str) -> Optional[str]:
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            msg = data.get("message", {})
            abstract = msg.get("abstract", "")
            abstract = re.sub(r"<[^>]+>", "", abstract).strip()
            if len(abstract) >= 150:
                return abstract
    except Exception:
        pass
    return None

def resolve_fallback(doi: str) -> Tuple[str, Optional[str]]:
    time.sleep(0.05) # Polite rate limit
    # 1. Try S2 API
    ab = fetch_s2_single(doi)
    if not ab:
        # 2. Try PubMed
        ab = fetch_pubmed_single(doi)
    if not ab:
        # 3. Try Crossref
        ab = fetch_crossref_single(doi)
    return doi, ab

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    papers = sel_data["papers"]
    dois = list(papers.keys())

    print(f"=== HIGH-SPEED DUAL-AUTHENTICATED EXTRACTION ({len(dois)} PAPERS) ===\n", flush=True)
    
    abstracts = {}
    
    # 1. OpenAlex Batch Extraction (10 workers in parallel)
    batch_size = 50
    batches = [dois[i:i + batch_size] for i in range(0, len(dois), batch_size)]
    print(f"Phase 1: Querying OpenAlex in {len(batches)} batches across 10 threads...", flush=True)
    
    start_t = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_openalex_batch, b): b for b in batches}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            abstracts.update(res)

    elapsed_oa = time.time() - start_t
    print(f"Phase 1 Complete in {elapsed_oa:.2f}s: Retrieved {len(abstracts)} / {len(dois)} abstracts ({len(abstracts)/len(dois)*100:.1f}%).\n", flush=True)

    # 2. Semantic Scholar + PubMed Fallback Extraction
    missing_dois = [d for d in dois if d.lower() not in abstracts]
    print(f"Phase 2: Querying Semantic Scholar + PubMed for {len(missing_dois)} remaining papers across 10 threads...", flush=True)

    start_t = time.time()
    resolved_s2 = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(resolve_fallback, d): d for d in missing_dois}
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            doi, ab = future.result()
            if ab:
                abstracts[doi.lower()] = ab
                resolved_s2 += 1
            if i % 100 == 0 or i == len(missing_dois):
                print(f"  Processed {i}/{len(missing_dois)} fallbacks (Found {resolved_s2} additional full abstracts)...", flush=True)

    elapsed_s2 = time.time() - start_t
    print(f"Phase 2 Complete in {elapsed_s2:.2f}s: Total Full Abstracts Acquired = {len(abstracts)} / {len(dois)} ({len(abstracts)/len(dois)*100:.1f}%).\n", flush=True)

    # 3. Synchronize All Datasets
    meta_path = SCRIPT_DIR / "expanded_corpus_meta.json"
    meta_data = json.loads(meta_path.read_text()) if meta_path.exists() else {}

    for doi, p in papers.items():
        d_low = doi.lower()
        if d_low in abstracts:
            full_ab = abstracts[d_low]
            p["abstract"] = full_ab
            if doi in meta_data:
                meta_data[doi]["abstract"] = full_ab
        else:
            if not p.get("abstract") and doi in meta_data:
                p["abstract"] = meta_data[doi].get("abstract", "")

    # Save to disk
    sel_path.write_text(json.dumps(sel_data, indent=2))
    meta_path.write_text(json.dumps(meta_data, indent=2))
    (SCRIPT_DIR / "full_abstracts_2000.json").write_text(json.dumps(abstracts, indent=2))
    
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

    print(f"Successfully updated final_selection.json, _data/corpus_*.json, and full_abstracts_2000.json with unabridged multi-paragraph abstracts!", flush=True)

if __name__ == "__main__":
    main()
