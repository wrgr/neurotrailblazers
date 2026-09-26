"""Before/after quality indicators for a synthetic proofreading triage kit.

Used by the Module 06 and Module 07 kits on neurotrailblazers.org. All data are
synthetic teaching data written by scripts/generate_kit_materials.rb; nothing here
is a measurement of a real segmentation.

The script plays the part of re-measuring against a proofread reference region:
it reads the kit's ground-truth file, applies the effect of every item you list as
fixed, and prints the indicators before and after. Python 3, standard library only.

    python3 qc_metrics.py                    # baseline
    python3 qc_metrics.py --fixed E03,E11    # after fixing E03 and E11
    python3 qc_metrics.py --fixed-file my_fixes.txt   # one ID per line
"""

import argparse
import csv
import hashlib
import json
import platform
from pathlib import Path


def load(kit_dir):
    kit = json.loads((kit_dir / "kit.json").read_text(encoding="utf-8"))
    with open(kit_dir / kit["report_file"], newline="", encoding="utf-8") as fh:
        report = {row[kit["id_column"]]: row for row in csv.DictReader(fh)}
    with open(kit_dir / kit["ground_truth_file"], newline="", encoding="utf-8") as fh:
        truth = {row["id"]: row for row in csv.DictReader(fh)}
    return kit, report, truth


def indicators(kit, truth, fixed):
    a = kit["analysis"]
    fp = fn = false_recip = hidden_recip = error_sites = outliers = misassigned = 0
    for item_id, row in truth.items():
        if item_id in fixed:
            continue
        fp += int(row["false_edges"])
        fn += int(row["missed_edges"])
        false_recip += int(row["false_reciprocal"])
        hidden_recip += int(row["hidden_reciprocal"])
        outliers += int(row["size_outlier"])
        misassigned += int(row["misassigned_synapses"])
        if row["true_type"] != "not_error" and row["on_analysis_cell"] == "1":
            error_sites += 1
    tp = a["true_edges"] - fn
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / a["true_edges"]
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    runs = a["analysis_cells"] + a["unflagged_error_sites"] + error_sites
    out = {
        "edge_precision": round(precision, 3),
        "edge_recall": round(recall, 3),
        "edge_f1": round(f1, 3),
        "false_edges": fp,
        "missed_edges": fn,
        "run_length_proxy_um": round(a["analysis_path_um"] / runs, 1),
        "flagged_error_sites_on_analysis_cells": error_sites,
    }
    if a["true_reciprocal_pairs"]:
        out["reciprocal_pairs_counted"] = a["true_reciprocal_pairs"] - hidden_recip + false_recip
        out["of_which_spurious"] = false_recip
        out["real_pairs_hidden_by_splits"] = hidden_recip
    if any(int(r["size_outlier"]) for r in truth.values()):
        out["analysis_objects_outside_size_range"] = outliers
    if any(int(r["misassigned_synapses"]) for r in truth.values()):
        out["synapses_on_wrong_neuron"] = misassigned
    return out


def main():
    parser = argparse.ArgumentParser(description="Before/after indicators for a synthetic triage kit.")
    parser.add_argument("--kit", default=str(Path(__file__).resolve().parent),
                        help="kit directory (default: the directory holding this script)")
    parser.add_argument("--fixed", default="", help="comma-separated IDs you corrected")
    parser.add_argument("--fixed-file", help="file with one corrected ID per line")
    args = parser.parse_args()

    kit_dir = Path(args.kit)
    kit, report, truth = load(kit_dir)
    ids = [i.strip() for i in args.fixed.split(",") if i.strip()]
    if args.fixed_file:
        ids += [ln.strip() for ln in Path(args.fixed_file).read_text(encoding="utf-8").splitlines() if ln.strip()]
    unknown = sorted(set(ids) - set(report))
    if unknown:
        parser.error("not in %s: %s" % (kit["report_file"], ", ".join(unknown)))
    fixed = set(ids)

    wasted = sorted(i for i in fixed if truth[i]["true_type"] == "not_error")
    result = {
        "dataset": kit["dataset"],
        "version": kit["version"],
        "analysis": kit["analysis"]["description"],
        "fixed": sorted(fixed),
        "fix_budget": kit["fix_budget"],
        "over_budget": len(fixed) > kit["fix_budget"],
        "fixes_spent_on_non_errors": wasted,
        "before": indicators(kit, truth, set()),
        "after": indicators(kit, truth, fixed),
        "python_version": platform.python_version(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limitation": kit["limitation"],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
