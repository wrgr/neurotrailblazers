#!/usr/bin/env python3
"""Comprehensive verification and audit of final_selection.json across tiers, categories, eras, and organisms."""
import json
from collections import defaultdict, Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

def main():
    sel_file = SCRIPT_DIR / "final_selection.json"
    data = json.loads(sel_file.read_text())
    papers = data["papers"]
    meta = data["metadata"]

    print(f"=== COMPREHENSIVE AUDIT OF FINAL SELECTION ({len(papers)} PAPERS) ===\n")
    print(f"Tier 500 Count:  {meta['tier_500_count']}")
    print(f"Tier 1000 Count: {meta['tier_1000_count']}")
    print(f"Tier 2000 Count: {meta['tier_2000_count']}\n")

    # Audit by Tier
    for tier_size, flag in [(500, "in_top_500"), (1000, "in_top_1000"), (2000, "in_top_2000")]:
        tier_papers = [p for p in papers.values() if p.get(flag)]
        print(f"--- TIER {tier_size} (N = {len(tier_papers)}) ---")
        
        cat_counts = Counter(p["classification"] for p in tier_papers)
        era_counts = Counter(p["era"] for p in tier_papers)
        org_counts = Counter(org for p in tier_papers for org in p.get("organism", ["none"]))
        
        print("  Category Distribution:")
        for cat, cnt in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
            pct = (cnt / len(tier_papers)) * 100
            print(f"    {cat:22s}: {cnt:4d} papers ({pct:5.1f}%)")
            
        print("  Era Distribution:")
        for era, cnt in sorted(era_counts.items(), key=lambda x: x[1], reverse=True):
            pct = (cnt / len(tier_papers)) * 100
            print(f"    {era:22s}: {cnt:4d} papers ({pct:5.1f}%)")
            
        print("  Top Organisms:")
        for org, cnt in org_counts.most_common(6):
            print(f"    {org:22s}: {cnt:4d} papers")
        print()

    # Generate txt report
    report_path = SCRIPT_DIR / "audit_final_selection.txt"
    report_lines = []
    report_lines.append(f"FINAL CORPUS SELECTION AUDIT REPORT (Total Selected: {len(papers)})\n")
    report_lines.append("=" * 80 + "\n")
    
    for cat in sorted(meta["category_shares"].keys()):
        c_papers = [p for p in papers.values() if p["classification"] == cat]
        report_lines.append(f"\nCATEGORY: {cat.upper()} (Total in 2000: {len(c_papers)})")
        report_lines.append("-" * 60)
        for p in sorted(c_papers, key=lambda x: (x.get("in_top_500", False), x["linkage_score"]), reverse=True)[:15]:
            t_flag = "TOP 500 " if p.get("in_top_500") else ("TOP 1000" if p.get("in_top_1000") else "TOP 2000")
            report_lines.append(f"[{t_flag} | {p['year']} | In:{p['in_degree']:3d} | Out:{p['out_degree']:2d}] {p['doi']:25s} | {p['title'][:60]}")
            
    report_path.write_text("\n".join(report_lines))
    print(f"Audit report saved to {report_path}")

if __name__ == "__main__":
    main()
