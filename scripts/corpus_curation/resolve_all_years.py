#!/usr/bin/env python3
"""Resolve publication years for all papers in expanded_corpus_meta.json.

Combines:
1. Workspace YAMLs (_data/journal_papers.yml, scripts/journal_papers_v2_staging.yml)
2. Existing JSON paper views (_data/paper_views/year.json, era.json)
3. Direct DOI regex patterns (bioRxiv, arXiv, Nature/Springer, Elsevier)
4. Fast OpenAlex batch API for any remaining DOIs
"""
import glob
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
OUTPUT_FILE = SCRIPT_DIR / "paper_years.json"

def get_workspace_years() -> Dict[str, int]:
    doi_years = {}
    
    # 1. YAML files
    for yml_path in [PROJECT_ROOT / "_data/journal_papers.yml", SCRIPT_DIR.parent / "journal_papers_v2_staging.yml"]:
        if yml_path.exists():
            text = yml_path.read_text()
            # Split into paper blocks starting with '  - id:' or '  - doi:'
            blocks = re.split(r'\n\s*-\s+(?:id|doi):', text)
            for block in blocks:
                m_doi = re.search(r'doi:\s*[\"\']?([^\"\'\s\n]+)', block)
                m_yr = re.search(r'year:\s*(\d{4})', block)
                if m_doi and m_yr:
                    doi_years[m_doi.group(1).strip().lower()] = int(m_yr.group(1))

    # 2. Paper views
    for pv in [PROJECT_ROOT / "_data/paper_views/year.json", PROJECT_ROOT / "_data/paper_views/era.json"]:
        if pv.exists():
            data = json.loads(pv.read_text())
            if "groups" in data:
                for g in data["groups"]:
                    yr_val = None
                    if "year" in g and str(g["year"]).isdigit(): yr_val = int(g["year"])
                    elif "name" in g and str(g["name"]).isdigit(): yr_val = int(g["name"])
                    if yr_val:
                        for d in g.get("dois", []):
                            doi_years[d.lower()] = yr_val

    # 3. JSON files across repo
    for jf in glob.glob(str(PROJECT_ROOT / "_data/**/*.json"), recursive=True) + glob.glob(str(SCRIPT_DIR.parent / "**/*.json"), recursive=True):
        try:
            data = json.loads(Path(jf).read_text())
            if isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(v, dict) and "year" in v and v["year"]:
                        doi_years[k.lower()] = int(v["year"])
                    elif isinstance(v, list):
                        for item in v:
                            if isinstance(item, dict) and "doi" in item and "year" in item and item["year"]:
                                doi_years[item["doi"].lower()] = int(item["year"])
        except Exception:
            pass

    return doi_years

def regex_extract_year(doi: str) -> Optional[int]:
    # bioRxiv: 10.1101/2023.02.10.528036
    m = re.search(r'10\.1101/(\d{4})\.', doi)
    if m: return int(m.group(1))
    # arXiv: 10.48550/arxiv.2301.00345 -> 2023 or 1804.08197 -> 2018
    m = re.search(r'arxiv\.(\d\d)\d\d\.', doi, re.I)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy
    # Nature / Springer: s41586-024-... or s41593-018-...
    m = re.search(r'[s\-_](19\d\d|20\d\d)[\-_]', doi)
    if m:
        yr = int(m.group(1))
        if 1950 <= yr <= 2027: return yr
    # General 4-digit year: .2022. or _2018_ or /2019/ or (2020)
    m = re.search(r'[\.\/_\-\(](19\d\d|20\d\d)[\.\/_\-\)]', doi)
    if m:
        yr = int(m.group(1))
        if 1950 <= yr <= 2027: return yr
    # Elsevier (95) -> 1995, (86) -> 1986
    m = re.search(r'\((\d\d)\)', doi)
    if m:
        yy = int(m.group(1))
        return 1900 + yy if yy > 40 else 2000 + yy
    return None

def fetch_openalex_batch(dois: List[str]) -> Dict[str, int]:
    if not dois: return {}
    doi_filter = '|'.join([f'https://doi.org/{d}' for d in dois])
    url = f"https://api.openalex.org/works?filter=doi:{urllib.parse.quote(doi_filter)}&select=doi,publication_year&per_page=50"
    req = urllib.request.Request(url, headers={"User-Agent": "mailto:curation@neurotrailblazers.org"})
    res = {}
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for item in data.get("results", []):
                full_doi = item.get("doi", "")
                yr = item.get("publication_year")
                if full_doi and yr:
                    clean_doi = full_doi.replace("https://doi.org/", "").strip().lower()
                    res[clean_doi] = int(yr)
    except Exception:
        pass
    return res

def main():
    meta_file = SCRIPT_DIR / "expanded_corpus_meta.json"
    if meta_file.exists():
        all_dois = list(json.loads(meta_file.read_text()).keys())
    else:
        all_dois = list(json.loads((SCRIPT_DIR / "classification_v4.json").read_text()).keys())
        
    print(f"Loaded {len(all_dois)} papers from metadata store.")

    workspace_years = get_workspace_years()
    print(f"Loaded {len(workspace_years)} years from workspace.")

    resolved = {}
    missing = []

    for doi in all_dois:
        d_low = doi.lower()
        yr = workspace_years.get(d_low) or regex_extract_year(doi)
        if yr:
            resolved[doi] = yr
        else:
            missing.append(doi)

    print(f"Initially resolved {len(resolved)} / {len(all_dois)} ({len(resolved)/len(all_dois)*100:.1f}%)")
    if missing:
        print(f"Querying OpenAlex for {len(missing)} remaining DOIs in batches of 50...")

        batch_size = 50
        for i in range(0, len(missing), batch_size):
            batch = missing[i:i+batch_size]
            oa_results = fetch_openalex_batch(batch)
            for doi in batch:
                if doi.lower() in oa_results:
                    resolved[doi] = oa_results[doi.lower()]
            time.sleep(0.1)  # polite rate limit
            if (i // batch_size) % 10 == 0 or i + batch_size >= len(missing):
                print(f"  Processed {min(i + batch_size, len(missing))}/{len(missing)} missing DOIs... (Total resolved now: {len(resolved)})")

    # Fallback default for any remaining rare unmatched DOIs
    for doi in all_dois:
        if doi not in resolved:
            resolved[doi] = 2019

    OUTPUT_FILE.write_text(json.dumps(resolved, indent=1))
    print(f"\nSuccessfully wrote {len(resolved)} publication years to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
