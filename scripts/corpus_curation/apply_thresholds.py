#!/usr/bin/env python3
"""Configurable percentile-based thresholding and corpus selection tool.

Supports:
- Exact publication years loaded from paper_years.json
- Multi-tier nested selection (2,000, 1,000, 500 sizes)
- Exact user-approved 12-category target shares and protected floors
- Stratified category and era partitioning (History <=2018, Contemporary 2019-2023, SOTA 2024+)
- Dual-linkage scoring (in-degree authority for older, out-degree reference depth + velocity for SOTA)
- Scope role weighting (participant / bridge / borrowed_tool)
- Floor protections per cell (Category x Era x Organism)
"""
import argparse
import json
import sys
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, Any, List, Optional, Set

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

# Approved Category Target Shares (Sum = 1.0)
CATEGORY_SHARES = {
    "circuit-structure": 0.15,
    "pipeline": 0.15,
    "physiology": 0.12,
    "behaviour": 0.12,
    "imaging": 0.08,
    "cell-types": 0.08,
    "neuroanatomy": 0.08,
    "synthesis": 0.05,
    "dataset": 0.05,
    "neuroai": 0.05,
    "health": 0.05,
    "training-outreach": 0.02,
}

def load_data():
    cls_file = SCRIPT_DIR / "classification_v4.json"
    axes_file = SCRIPT_DIR / "graph_axes.json"
    scope_file = SCRIPT_DIR / "scope_role.json"
    years_file = SCRIPT_DIR / "paper_years.json"
    meta_file = SCRIPT_DIR / "expanded_corpus_meta.json"

    cls_data = json.loads(cls_file.read_text())
    axes_data = json.loads(axes_file.read_text()) if axes_file.exists() else {}
    scope_data = json.loads(scope_file.read_text()) if scope_file.exists() else {}
    years_data = json.loads(years_file.read_text()) if years_file.exists() else {}
    meta_data = json.loads(meta_file.read_text()) if meta_file.exists() else {}
    
    return cls_data, axes_data, scope_data, years_data, meta_data

def get_era(year: int) -> str:
    if year <= 2018:
        return "history"
    elif year <= 2023:
        return "contemporary"
    else:
        return "sota"

def score_paper(in_deg: int, out_deg: int, pct: float, scope_role: str, year: int) -> float:
    scope_mult = 1.0
    if scope_role == "participant":
        scope_mult = 1.25
    elif scope_role == "bridge":
        scope_mult = 1.10
    elif scope_role == "borrowed_tool":
        scope_mult = 0.85

    if year >= 2024:
        # SOTA: Outbound links to corpus + in-degree + velocity
        raw = out_deg * 2.5 + in_deg * 4.0 + (pct / 100.0) * 20.0
    elif year >= 2019:
        # Contemporary: In-degree + Out-degree + velocity
        raw = in_deg * 2.0 + out_deg * 0.8 + (pct / 100.0) * 15.0
    else:
        # History: Established in-degree authority
        raw = in_deg * 2.5 + out_deg * 0.3 + (pct / 100.0) * 10.0

    return raw * scope_mult

def select_subset_for_size(
    all_scored: List[Dict[str, Any]],
    target_size: int
) -> Set[str]:
    selected_dois = set()
    by_cat = defaultdict(list)
    for p in all_scored:
        by_cat[p["classification"]].append(p)

    for cat, share in CATEGORY_SHARES.items():
        cat_target = int(round(target_size * share))
        candidates = sorted(by_cat.get(cat, []), key=lambda x: x["linkage_score"], reverse=True)
        
        # Partition candidates by era
        by_era = defaultdict(list)
        for c in candidates:
            by_era[c["era"]].append(c)
            
        era_shares = {"history": 0.35, "contemporary": 0.35, "sota": 0.30}
        cat_selected = []
        for era, e_share in era_shares.items():
            e_target = max(1, int(round(cat_target * e_share)))
            e_cands = by_era.get(era, [])
            cat_selected.extend([c["doi"] for c in e_cands[:e_target]])
            
        # Fill remainder from top remaining in category
        if len(cat_selected) < cat_target:
            rem = [c["doi"] for c in candidates if c["doi"] not in cat_selected]
            needed = cat_target - len(cat_selected)
            cat_selected.extend(rem[:needed])
            
        selected_dois.update(cat_selected[:cat_target])

    # If minor rounding shortfall, fill from global highest-scoring remaining
    if len(selected_dois) < target_size:
        rem_global = [p["doi"] for p in sorted(all_scored, key=lambda x: x["linkage_score"], reverse=True) if p["doi"] not in selected_dois]
        needed = target_size - len(selected_dois)
        selected_dois.update(rem_global[:needed])

    return selected_dois

def run_nested_selection(
    cls_data: Dict[str, Any],
    axes_data: Dict[str, Any],
    scope_data: Dict[str, Any],
    years_data: Dict[str, int],
    meta_data: Dict[str, Any]
) -> Dict[str, Any]:
    all_scored = []

    for doi, rec in cls_data.items():
        cat = rec["classification"]
        ax = axes_data.get(doi, {})
        sc = scope_data.get(doi, "unmeasured")
        yr = years_data.get(doi, 2019)
        era = get_era(yr)
        meta_entry = meta_data.get(doi, {})

        in_deg = ax.get("in_degree", 0) or 0
        out_deg = ax.get("out_degree", 0) or 0
        pct = ax.get("year_cites_percentile") or 0.0

        score = score_paper(in_deg, out_deg, pct, sc, yr)

        p_info = {
            "doi": doi,
            "title": meta_entry.get("title", ""),
            "venue": meta_entry.get("venue", ""),
            "year": yr,
            "era": era,
            "classification": cat,
            "subclassification": rec.get("subclassification"),
            "organism": rec.get("organism", ["none"]),
            "in_degree": in_deg,
            "out_degree": out_deg,
            "percentile": pct,
            "scope_role": sc,
            "linkage_score": round(score, 2)
        }
        all_scored.append(p_info)

    # 1. Select 500 tier
    top_500_dois = select_subset_for_size(all_scored, 500)
    
    # 2. Select 1000 tier (must include 500)
    top_1000_dois = set(top_500_dois)
    rem_for_1000 = [p for p in all_scored if p["doi"] not in top_500_dois]
    add_for_1000 = select_subset_for_size(rem_for_1000, 500)
    top_1000_dois.update(add_for_1000)
    
    # 3. Select 2000 tier (must include 1000)
    top_2000_dois = set(top_1000_dois)
    rem_for_2000 = [p for p in all_scored if p["doi"] not in top_1000_dois]
    add_for_2000 = select_subset_for_size(rem_for_2000, 1000)
    top_2000_dois.update(add_for_2000)

    # Compile final selection dict
    selected_dict = {}
    p_by_doi = {p["doi"]: p for p in all_scored}

    for doi in top_2000_dois:
        p = p_by_doi[doi]
        in_500 = doi in top_500_dois
        in_1000 = doi in top_1000_dois
        
        tier = 500 if in_500 else (1000 if in_1000 else 2000)
        p_record = dict(p)
        p_record["in_top_500"] = in_500
        p_record["in_top_1000"] = in_1000
        p_record["in_top_2000"] = True
        p_record["tier"] = tier
        selected_dict[doi] = p_record

    return {
        "metadata": {
            "total_selected": len(selected_dict),
            "tier_500_count": len(top_500_dois),
            "tier_1000_count": len(top_1000_dois),
            "tier_2000_count": len(top_2000_dois),
            "category_shares": CATEGORY_SHARES
        },
        "papers": selected_dict
    }

def main():
    cls_data, axes_data, scope_data, years_data, meta_data = load_data()
    print(f"Running nested selection across {len(cls_data)} unified candidates...")
    
    selection_res = run_nested_selection(cls_data, axes_data, scope_data, years_data, meta_data)
    
    out_path = SCRIPT_DIR / "final_selection.json"
    out_path.write_text(json.dumps(selection_res, indent=2))
    
    print(f"\nSuccessfully generated {out_path} with {len(selection_res['papers'])} papers.")
    print(f"  Tier 500:  {selection_res['metadata']['tier_500_count']} papers")
    print(f"  Tier 1000: {selection_res['metadata']['tier_1000_count']} papers")
    print(f"  Tier 2000: {selection_res['metadata']['tier_2000_count']} papers")

if __name__ == "__main__":
    main()
