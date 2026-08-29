#!/usr/bin/env python3
"""Exports verified final_selection.json into site views (_data/paper_views/) and YAML staging."""
import json
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
VIEWS_DIR = PROJECT_ROOT / "_data/paper_views"
VIEWS_DIR.mkdir(parents=True, exist_ok=True)

def main():
    sel_file = SCRIPT_DIR / "final_selection.json"
    data = json.loads(sel_file.read_text())
    papers = data["papers"]
    meta = data["metadata"]

    print(f"Exporting {len(papers)} curated papers to site views in {VIEWS_DIR}...")

    # 1. Tier View (_data/paper_views/tier.json)
    tier_groups = [
        {"name": "500", "title": "Top 500 Core Flagships", "count": meta["tier_500_count"], "dois": [d for d, p in papers.items() if p.get("in_top_500")]},
        {"name": "1000", "title": "Top 1,000 Landmark Corpus", "count": meta["tier_1000_count"], "dois": [d for d, p in papers.items() if p.get("in_top_1000")]},
        {"name": "2000", "title": "Top 2,000 Comprehensive Corpus", "count": meta["tier_2000_count"], "dois": list(papers.keys())}
    ]
    (VIEWS_DIR / "tier.json").write_text(json.dumps({"view": "tier", "groups": tier_groups}, indent=2))

    # 2. Dimension (Category) View (_data/paper_views/dimension.json)
    by_dim = defaultdict(list)
    for d, p in papers.items():
        by_dim[p["classification"]].append(d)
    
    dim_groups = []
    for dim_name, d_list in sorted(by_dim.items(), key=lambda x: len(x[1]), reverse=True):
        dim_groups.append({
            "name": dim_name,
            "title": dim_name.replace("-", " ").title(),
            "count": len(d_list),
            "dois": d_list
        })
    (VIEWS_DIR / "dimension.json").write_text(json.dumps({"view": "dimension", "groups": dim_groups}, indent=2))

    # 3. Era View (_data/paper_views/era.json)
    by_era = defaultdict(list)
    for d, p in papers.items():
        by_era[p["era"]].append(d)
    
    era_labels = {
        "history": "History (<=2018)",
        "contemporary": "Contemporary (2019-2023)",
        "sota": "SOTA (2024-2026+)"
    }
    era_groups = []
    for era_key in ["history", "contemporary", "sota"]:
        d_list = by_era.get(era_key, [])
        era_groups.append({
            "name": era_key,
            "title": era_labels[era_key],
            "count": len(d_list),
            "dois": d_list
        })
    (VIEWS_DIR / "era.json").write_text(json.dumps({"view": "era", "groups": era_groups}, indent=2))

    # 4. Organism View (_data/paper_views/organism.json)
    by_org = defaultdict(list)
    for d, p in papers.items():
        for org in p.get("organism", ["none"]):
            by_org[org].append(d)
            
    org_groups = []
    for org_name, d_list in sorted(by_org.items(), key=lambda x: len(x[1]), reverse=True):
        org_groups.append({
            "name": org_name,
            "title": org_name.title() if org_name != "none" else "Theory & Methods (General)",
            "count": len(d_list),
            "dois": d_list
        })
    (VIEWS_DIR / "organism.json").write_text(json.dumps({"view": "organism", "groups": org_groups}, indent=2))

    # 5. Manifest (_data/paper_views/manifest.json)
    manifest = {
        "total_corpus_size": len(papers),
        "tiers": {
            "tier_500": meta["tier_500_count"],
            "tier_1000": meta["tier_1000_count"],
            "tier_2000": meta["tier_2000_count"]
        },
        "category_counts": {g["name"]: g["count"] for g in dim_groups},
        "era_counts": {g["name"]: g["count"] for g in era_groups},
        "views_available": ["tier", "dimension", "era", "organism"]
    }
    (VIEWS_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2))

    print(f"Successfully generated all paper views in {VIEWS_DIR}!")

if __name__ == "__main__":
    main()
