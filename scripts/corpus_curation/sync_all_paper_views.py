#!/usr/bin/env python3
"""Synchronizes all faceted paper views in _data/paper_views/ with the 2,000-paper corpus.

Caution: final_selection.json carries stale years, so the era.json and year.json this
writes are wrong. Those two views are owned by scripts/derive_journal_papers.py; after
running this, restore them (or re-run the derive script).
"""
import json
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
PV_DIR = PROJECT_ROOT / "_data/paper_views"
PV_DIR.mkdir(parents=True, exist_ok=True)

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    papers = list(sel_data["papers"].values())

    print(f"Synchronizing all faceted views for {len(papers)} papers in {PV_DIR}...")

    # 1. Tier View
    tier_groups = [
        {"key": "500", "label": "Top 500", "n": sum(1 for p in papers if p.get("in_top_500")), "description": "The 500 top-ranked papers; contained in the Top 1,000 and Top 2,000"},
        {"key": "1000", "label": "Top 1,000", "n": sum(1 for p in papers if p.get("in_top_1000")), "description": "The 1,000 top-ranked papers; includes the Top 500"},
        {"key": "2000", "label": "Top 2,000", "n": len(papers), "description": "All 2,000 papers in the corpus"}
    ]
    (PV_DIR / "tier.json").write_text(json.dumps({"view": "tier", "total": len(papers), "groups": tier_groups}, indent=2))

    # 2. Dimension / Category View
    cat_counts = defaultdict(int)
    for p in papers:
        cat_counts[p.get("classification", "circuit-structure")] += 1
    
    cat_labels = {
        "circuit-structure": "Circuit Structure & Connectomes",
        "pipeline": "Pipeline & Software Engineering",
        "physiology": "Physiological Validation & Function",
        "behaviour": "Behavior & Circuit Dynamics",
        "imaging": "Volume EM & Super-Resolution Optics",
        "cell-types": "Cell Types & Morphological Census",
        "neuroanatomy": "Neuroanatomy & Ultrastructure",
        "synthesis": "Synthesis, Theory & Reviews",
        "dataset": "Benchmark Datasets & Public Repositories",
        "neuroai": "NeuroAI, Biophysics & Artificial Networks",
        "health": "Health, Disease & Connectopathies",
        "training-outreach": "Workforce Training, Pedagogy & Outreach"
    }
    dim_groups = [
        {"key": k, "label": cat_labels.get(k, k.replace("-", " ").title()), "n": cat_counts[k]}
        for k in sorted(cat_counts.keys())
    ]
    (PV_DIR / "dimension.json").write_text(json.dumps({"view": "dimension", "total": len(papers), "groups": dim_groups}, indent=2))

    # 3. Era View
    era_counts = defaultdict(int)
    for p in papers:
        era_counts[p.get("era", "contemporary")] += 1
    era_groups = [
        {"key": "history", "label": "History (2018 and earlier)", "n": era_counts["history"], "range": "1962-2018"},
        {"key": "contemporary", "label": "Contemporary (2019-2023)", "n": era_counts["contemporary"], "range": "2019-2023"},
        {"key": "sota", "label": "Recent (2024 onward)", "n": era_counts["sota"], "range": "2024-2026+"}
    ]
    (PV_DIR / "era.json").write_text(json.dumps({"view": "era", "total": len(papers), "groups": era_groups}, indent=2))

    # 4. Organism View
    org_counts = defaultdict(int)
    for p in papers:
        for org in p.get("organism", ["general"]):
            org_counts[org] += 1
    org_groups = [
        {"key": k, "label": k.replace("-", " ").title(), "n": count}
        for k, count in sorted(org_counts.items(), key=lambda x: -x[1])
    ]
    (PV_DIR / "organism.json").write_text(json.dumps({"view": "organism", "total": len(papers), "groups": org_groups}, indent=2))

    # 5. Year View
    year_counts = defaultdict(int)
    for p in papers:
        year_counts[p.get("year", 2024)] += 1
    year_groups = [
        {"key": str(yr), "year": yr, "n": count}
        for yr, count in sorted(year_counts.items())
    ]
    (PV_DIR / "year.json").write_text(json.dumps({"view": "year", "total": len(papers), "groups": year_groups}, indent=2))

    # 6. K-Core Centrality View
    kcore_counts = defaultdict(int)
    for p in papers:
        kcore_counts[p.get("k_core", 5)] += 1
    kcore_groups = [
        {"key": f"kcore_{k}", "k_core": k, "n": count}
        for k, count in sorted(kcore_counts.items())
    ]
    (PV_DIR / "kcore.json").write_text(json.dumps({"view": "kcore", "total": len(papers), "groups": kcore_groups}, indent=2))

    # 7. Manifest
    manifest = {
        "corpus_name": "NeuroTrailblazers Multi-Tier Connectomics Corpus",
        "total_papers": len(papers),
        "tiers": {
            "tier_500": sum(1 for p in papers if p.get("in_top_500")),
            "tier_1000": sum(1 for p in papers if p.get("in_top_1000")),
            "tier_2000": len(papers)
        },
        "views": ["tier", "dimension", "era", "organism", "year", "kcore"]
    }
    (PV_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2))

    print(f"All paper views successfully generated and synchronized!")

if __name__ == "__main__":
    main()
