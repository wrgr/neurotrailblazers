#!/usr/bin/env python3
"""Materializes clean, standalone JSON files for Tier 500, Tier 1000, and Tier 2000 in _data/."""
import json
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_ROOT / "_data"

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    papers = sel_data["papers"]

    print("Materializing standalone tier datasets...")

    for tier_size, flag in [(500, "in_top_500"), (1000, "in_top_1000"), (2000, "in_top_2000")]:
        tier_papers = [p for p in papers.values() if p.get(flag)]
        
        # Sort papers by category and rank within category
        tier_papers.sort(key=lambda p: (p["classification"], -p["linkage_score"]))
        
        out_file = DATA_DIR / f"corpus_{tier_size}.json"
        out_file.write_text(json.dumps({
            "tier": tier_size,
            "count": len(tier_papers),
            "papers": tier_papers
        }, indent=2))
        
        print(f"  --> Materialized {out_file} ({len(tier_papers)} papers)")

if __name__ == "__main__":
    main()
