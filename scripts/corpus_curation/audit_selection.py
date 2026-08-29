#!/usr/bin/env python3
"""Audit selection results and report diagnostic summaries."""
import json
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SELECTION_FILE = SCRIPT_DIR / "final_selection.json"
AUDIT_FILE = SCRIPT_DIR / "audit_final_selection.txt"

def main():
    if not SELECTION_FILE.exists():
        print(f"Error: {SELECTION_FILE} does not exist. Run apply_thresholds.py first.")
        return

    data = json.loads(SELECTION_FILE.read_text())
    selected = data.get("selected_dois", {})
    summary = data.get("summary", {})

    lines = []
    lines.append("=" * 70)
    lines.append("       NEUROTRAILBLAZERS CORPUS CURATION: SELECTION AUDIT")
    lines.append("=" * 70)
    lines.append(f"Total Selected Papers: {len(selected)}")
    lines.append("")

    lines.append("--- CATEGORY SELECTION BREAKDOWN ---")
    lines.append(f"{'Category':22s} | {'Selected':8s} | {'Total':8s} | {'Retained %':10s} | {'Mean in_deg':11s}")
    lines.append("-" * 70)
    for cat, stats in sorted(summary.items(), key=lambda x: x[1]["selected_count"], reverse=True):
        lines.append(
            f"{cat:22s} | {stats['selected_count']:8d} | {stats['total_candidates']:8d} | "
            f"{stats['retention_rate']*100:9.1f}% | {stats['mean_in_degree']:11.1f}"
        )

    # Organism breakdown
    org_counts = Counter()
    for p in selected.values():
        for o in p.get("organism", []):
            org_counts[o] += 1

    lines.append("")
    lines.append("--- ORGANISM BREAKDOWN (SELECTED) ---")
    for o, c in org_counts.most_common():
        lines.append(f"  {o:15s}: {c:5d} ({c/len(selected)*100:4.1f}%)")

    # Scope role breakdown
    scope_counts = Counter(p.get("scope_role", "unmeasured") for p in selected.values())
    lines.append("")
    lines.append("--- SCOPE ROLE BREAKDOWN (SELECTED) ---")
    for s, c in scope_counts.most_common():
        lines.append(f"  {s:15s}: {c:5d} ({c/len(selected)*100:4.1f}%)")

    # Top cited papers in key categories
    lines.append("")
    lines.append("--- TOP PAPERS BY IN-DEGREE (KEY CATEGORIES) ---")
    by_cat = {}
    for p in selected.values():
        cat = p["classification"]
        if cat not in by_cat:
            by_cat[cat] = []
        by_cat[cat].append(p)

    for cat in ["dataset", "circuit-structure", "pipeline", "imaging", "neuroai"]:
        papers = sorted(by_cat.get(cat, []), key=lambda x: x["in_degree"], reverse=True)[:5]
        lines.append(f"\n[{cat.upper()}] Top 5:")
        for p in papers:
            lines.append(f"  - DOI: {p['doi']:30s} | in_deg: {p['in_degree']:4d} | %ile: {p['percentile']:4.1f} | org: {p['organism']}")

    audit_text = "\n".join(lines)
    AUDIT_FILE.write_text(audit_text)
    print(audit_text)
    print(f"\nWrote audit report to {AUDIT_FILE}")

if __name__ == "__main__":
    main()
