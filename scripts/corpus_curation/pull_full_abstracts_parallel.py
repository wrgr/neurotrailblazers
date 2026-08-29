#!/usr/bin/env python3
"""Pulls full, unabridged multi-paragraph abstracts in parallel for all 2,000 selected papers.

Combines:
1. Fast OpenAlex Batch API (50 DOIs per request)
2. Parallel PubMed E-Utilities XML fetch for paywalled biomedical journals
3. Parallel Semantic Scholar & Crossref fallback
"""
import concurrent.futures
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

def fetch_openalex_batch(dois: List[str]) -> Dict[str, str]:
    if not dois: return {}
    doi_filter = "|".join([f"https://doi.org/{d}" for d in dois])
    url = f"https://api.openalex.org/works?filter=doi:{urllib.parse.quote(doi_filter)}&select=doi,abstract_inverted_index&per_page=50"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    res = {}
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
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

def fetch_pubmed_single(doi: str) -> Optional[str]:
    esearch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(doi)}[doi]&retmode=json"
    req = urllib.request.Request(esearch_url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            id_list = data.get("esearchresult", {}).get("idlist", [])
            if id_list:
                pmid = id_list[0]
                time.sleep(0.35)
                efetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
                req_ef = urllib.request.Request(efetch_url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
                with urllib.request.urlopen(req_ef, timeout=8) as ef_resp:
                    xml_root = ET.fromstring(ef_resp.read())
                    abs_nodes = xml_root.findall(".//AbstractText")
                    if abs_nodes:
                        abs_text = " ".join(["".join(node.itertext()).strip() for node in abs_nodes])
                        if len(abs_text.strip()) >= 150:
                            return abs_text.strip()
    except Exception:
        pass
    return None

def fetch_semanticscholar_single(doi: str) -> Optional[str]:
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{urllib.parse.quote(doi)}?fields=abstract"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("abstract") and len(data["abstract"]) >= 150:
                return data["abstract"].strip()
    except Exception:
        pass
    return None

def fetch_crossref_single(doi: str) -> Optional[str]:
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0 (mailto:curation@neurotrailblazers.org)"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            msg = data.get("message", {})
            abstract = msg.get("abstract", "")
            abstract = re.sub(r"<[^>]+>", "", abstract).strip()
            if len(abstract) >= 150:
                return abstract
    except Exception:
        pass
    return None

def fallback_resolver(doi: str) -> Tuple[str, Optional[str]]:
    # Try PubMed first
    ab = fetch_pubmed_single(doi)
    if not ab:
        # Try Semantic Scholar
        ab = fetch_semanticscholar_single(doi)
    if not ab:
        # Try Crossref
        ab = fetch_crossref_single(doi)
    return doi, ab

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    papers = sel_data["papers"]
    dois = list(papers.keys())

    print(f"=== PULLING FULL ABSTRACTS IN PARALLEL FOR {len(dois)} PAPERS ===\n")
    
    abstracts = {}
    
    # 1. OpenAlex Batch Resolution (batches of 50 in parallel)
    batch_size = 50
    batches = [dois[i:i + batch_size] for i in range(0, len(dois), batch_size)]
    print(f"Phase 1: Querying OpenAlex in {len(batches)} batches across 5 threads...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_openalex_batch, b): b for b in batches}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            abstracts.update(res)

    print(f"Phase 1 Complete: OpenAlex returned full abstracts for {len(abstracts)} / {len(dois)} papers ({len(abstracts)/len(dois)*100:.1f}%).\n")

    # 2. Targeted Parallel Fallback (PubMed + Semantic Scholar + Crossref)
    missing_dois = [d for d in dois if d.lower() not in abstracts]
    print(f"Phase 2: Querying PubMed / Semantic Scholar / Crossref for {len(missing_dois)} remaining papers...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(fallback_resolver, d): d for d in missing_dois}
        resolved_fb = 0
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            doi, ab = future.result()
            if ab:
                abstracts[doi.lower()] = ab
                resolved_fb += 1
            if i % 100 == 0 or i == len(missing_dois):
                print(f"  Processed {i}/{len(missing_dois)} fallbacks (Found {resolved_fb} full abstracts so far)...")

    print(f"\nPhase 2 Complete: Total Full Abstracts Acquired = {len(abstracts)} / {len(dois)} ({len(abstracts)/len(dois)*100:.1f}%).\n")

    # 3. Update Datasets
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
            # Preserve existing excerpt if full abstract not found
            if not p.get("abstract") and doi in meta_data:
                p["abstract"] = meta_data[doi].get("abstract", "")

    # Save enriched files
    sel_path.write_text(json.dumps(sel_data, indent=2))
    meta_path.write_text(json.dumps(meta_data, indent=2))
    (SCRIPT_DIR / "full_abstracts_2000.json").write_text(json.dumps(abstracts, indent=2))
    
    # Re-materialize corpus tiers with full abstracts
    for tier_size, flag in [(500, "in_top_500"), (1000, "in_top_1000"), (2000, "in_top_2000")]:
        tier_papers = [p for p in papers.values() if p.get(flag)]
        tier_papers.sort(key=lambda p: (p["classification"], -p["linkage_score"]))
        out_file = PROJECT_ROOT / f"_data/corpus_{tier_size}.json"
        out_file.write_text(json.dumps({
            "tier": tier_size,
            "count": len(tier_papers),
            "papers": tier_papers
        }, indent=2))

    print(f"Successfully updated final_selection.json, _data/corpus_*.json, and full_abstracts_2000.json!")

if __name__ == "__main__":
    main()
