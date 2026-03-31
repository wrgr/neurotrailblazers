#!/usr/bin/env python3
"""
Step 12b: Auto-review high-confidence duplicate & author dedup decisions.

Reads TSV outputs from 12_dedup_review.py and automatically accepts/flags
decisions based on confidence thresholds. This avoids manual TSV review
for high-confidence matches while preserving transparency.

Usage:
    python 12_auto_review.py [--auto-threshold 0.70] [--confidence-level high|medium|conservative]

Options:
    --auto-threshold N         Accept merges with confidence >= N
                              Default: 0.70 (requires further TSV review)
                              Recommended: 0.80 (high confidence, skip TSV)

    --confidence-level LEVEL   Preset thresholds:
                              'conservative': only auto-accept >= 0.85 (safest)
                              'medium':       auto-accept >= 0.75
                              'high':         auto-accept >= 0.70 (original)

Output:
    output/duplicate_auto_decisions.json   — ACCEPT/REJECT/REVIEW decisions
    output/author_auto_decisions.json      — ACCEPT/REJECT/REVIEW decisions
    output/auto_review_log.json           — detailed log of all decisions
    output/duplicate_review_flagged.tsv   — only the REVIEW cases (human TSV)
    output/author_review_flagged.tsv      — only the REVIEW cases (human TSV)
"""
import json
from pathlib import Path
import sys

OUT = Path("scripts/bibliometrics/output")


def parse_args():
    """Parse command-line arguments."""
    args = {
        'auto_threshold': 0.70,
        'duplicate_threshold': 0.70,
        'author_threshold': 0.70,
    }

    for i, arg in enumerate(sys.argv[1:]):
        if arg == '--auto-threshold' and i + 1 < len(sys.argv) - 1:
            args['auto_threshold'] = float(sys.argv[i + 2])
        elif arg == '--confidence-level':
            level = sys.argv[i + 2] if i + 1 < len(sys.argv) - 1 else 'medium'
            if level == 'conservative':
                args['duplicate_threshold'] = 0.85
                args['author_threshold'] = 0.85
            elif level == 'medium':
                args['duplicate_threshold'] = 0.75
                args['author_threshold'] = 0.75
            elif level == 'high':
                args['duplicate_threshold'] = 0.70
                args['author_threshold'] = 0.70

    return args


def load_tsv(path):
    """Load TSV file (tab-separated, first line is header)."""
    if not path.exists():
        return []

    rows = []
    with open(path) as f:
        lines = f.readlines()

    if not lines:
        return []

    header = lines[0].strip().split('\t')
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.strip().split('\t')
        row = {}
        for i, col in enumerate(header):
            row[col] = parts[i] if i < len(parts) else ""
        rows.append(row)

    return rows, header


def auto_review_duplicates(tsv_path, threshold_accept, threshold_review):
    """
    Auto-review duplicate pairs based on confidence score.

    Returns:
    - accept_list: papers to merge (confidence >= threshold_accept)
    - flagged_rows: pairs for human review (threshold_review <= confidence < threshold_accept)
    - rejected_list: papers to skip (confidence < threshold_review)
    """
    rows, header = load_tsv(tsv_path)
    if not rows:
        return [], [], []

    accept = []
    flagged = [header]  # Keep header for TSV
    rejected = []
    log = []

    for row in rows:
        try:
            conf = float(row.get('confidence', 0))
        except ValueError:
            continue

        paper1 = row.get('paper1_id', '').split()[0]
        paper2 = row.get('paper2_id', '').split()[0]
        existing_decision = row.get('decision', '').strip()

        # Skip if already decided
        if existing_decision and existing_decision.upper() not in ('', 'ACCEPT', 'REJECT'):
            if existing_decision.upper() == 'ACCEPT':
                accept.append({
                    'paper1_id': paper1,
                    'paper2_id': paper2,
                    'confidence': conf,
                    'reason': 'user-decided',
                })
            continue

        # Auto-decision based on confidence
        if conf >= threshold_accept:
            accept.append({
                'paper1_id': paper1,
                'paper2_id': paper2,
                'confidence': conf,
                'reason': f'auto_accepted >= {threshold_accept}',
            })
            log.append({
                'pair': [paper1, paper2],
                'confidence': conf,
                'decision': 'AUTO_ACCEPT',
                'justification': f'confidence {conf:.4f} >= threshold {threshold_accept}',
            })

        elif conf >= threshold_review:
            # Flag for human review
            flagged.append(row)
            log.append({
                'pair': [paper1, paper2],
                'confidence': conf,
                'decision': 'FLAGGED',
                'justification': f'confidence {conf:.4f} between {threshold_review} and {threshold_accept}',
            })

        else:
            rejected.append({
                'paper1_id': paper1,
                'paper2_id': paper2,
                'confidence': conf,
                'reason': f'confidence {conf:.4f} < {threshold_review}',
            })
            log.append({
                'pair': [paper1, paper2],
                'confidence': conf,
                'decision': 'REJECTED',
                'justification': f'confidence {conf:.4f} < review threshold {threshold_review}',
            })

    return accept, flagged, rejected, log


def auto_review_authors(tsv_path, threshold_accept, threshold_review):
    """Similar to auto_review_duplicates but for author names."""
    rows, header = load_tsv(tsv_path)
    if not rows:
        return [], [], []

    accept = []
    flagged = [header]
    rejected = []
    log = []

    for row in rows:
        try:
            conf = float(row.get('confidence', 0))
        except ValueError:
            continue

        name_a = row.get('name_a', '')
        name_b = row.get('name_b', '')
        existing_decision = row.get('decision', '').strip()

        if existing_decision and existing_decision.upper() not in ('', 'ACCEPT', 'REJECT'):
            if existing_decision.upper() == 'ACCEPT':
                accept.append({
                    'name_a': name_a,
                    'name_b': name_b,
                    'confidence': conf,
                    'reason': 'user-decided',
                })
            continue

        if conf >= threshold_accept:
            accept.append({
                'name_a': name_a,
                'name_b': name_b,
                'confidence': conf,
                'reason': f'auto_accepted >= {threshold_accept}',
            })
            log.append({
                'pair': [name_a, name_b],
                'confidence': conf,
                'decision': 'AUTO_ACCEPT',
                'justification': f'confidence {conf:.4f} >= threshold {threshold_accept}',
            })

        elif conf >= threshold_review:
            flagged.append(row)
            log.append({
                'pair': [name_a, name_b],
                'confidence': conf,
                'decision': 'FLAGGED',
                'justification': f'confidence {conf:.4f} between {threshold_review} and {threshold_accept}',
            })

        else:
            rejected.append({
                'name_a': name_a,
                'name_b': name_b,
                'confidence': conf,
                'reason': f'confidence {conf:.4f} < {threshold_review}',
            })
            log.append({
                'pair': [name_a, name_b],
                'confidence': conf,
                'decision': 'REJECTED',
                'justification': f'confidence {conf:.4f} < {threshold_review}',
            })

    return accept, flagged, rejected, log


def main():
    args = parse_args()

    print(f"\n{'='*70}")
    print(f"AUTO-REVIEW: High-Confidence Duplicate & Author Decisions")
    print(f"{'='*70}")
    print(f"\nThresholds:")
    print(f"  Duplicate AUTO_ACCEPT:  >= {args['duplicate_threshold']}")
    print(f"  Duplicate REVIEW FLAG:  >= 0.40")
    print(f"  Author AUTO_ACCEPT:     >= {args['author_threshold']}")
    print(f"  Author REVIEW FLAG:     >= 0.35\n")

    # Process duplicates
    print("Processing duplicates...")
    dup_accept, dup_flagged, dup_rejected, dup_log = auto_review_duplicates(
        OUT / "duplicate_review.tsv",
        threshold_accept=args['duplicate_threshold'],
        threshold_review=0.40
    )

    # Process authors
    print("Processing author name variants...")
    auth_accept, auth_flagged, auth_rejected, auth_log = auto_review_authors(
        OUT / "author_dedup_review.tsv",
        threshold_accept=args['author_threshold'],
        threshold_review=0.35
    )

    # Save decisions
    decisions = {
        "duplicates": {
            "auto_accept_count": len(dup_accept),
            "flagged_for_review_count": len(dup_flagged) - 1,  # Exclude header
            "rejected_count": len(dup_rejected),
            "threshold": args['duplicate_threshold'],
        },
        "authors": {
            "auto_accept_count": len(auth_accept),
            "flagged_for_review_count": len(auth_flagged) - 1,
            "rejected_count": len(auth_rejected),
            "threshold": args['author_threshold'],
        },
    }

    with open(OUT / "duplicate_auto_decisions.json", 'w') as f:
        json.dump({"auto_accept": dup_accept, "log": dup_log}, f, indent=2)

    with open(OUT / "author_auto_decisions.json", 'w') as f:
        json.dump({"auto_accept": auth_accept, "log": auth_log}, f, indent=2)

    with open(OUT / "auto_review_log.json", 'w') as f:
        json.dump(decisions, f, indent=2)

    # Save flagged cases to TSV for human review
    if len(dup_flagged) > 1:
        with open(OUT / "duplicate_review_flagged.tsv", 'w') as f:
            for row in dup_flagged:
                if isinstance(row, list):  # Header
                    f.write("\t".join(row) + "\n")
                else:
                    f.write("\t".join(str(row.get(col, "")) for col in dup_flagged[0]) + "\n")

    if len(auth_flagged) > 1:
        with open(OUT / "author_review_flagged.tsv", 'w') as f:
            for row in auth_flagged:
                if isinstance(row, list):
                    f.write("\t".join(row) + "\n")
                else:
                    f.write("\t".join(str(row.get(col, "")) for col in auth_flagged[0]) + "\n")

    # Print summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}\n")

    print(f"Duplicates:")
    print(f"  ✓ AUTO_ACCEPT ({len(dup_accept)} pairs) → applied automatically")
    print(f"  ? FLAGGED ({len(dup_flagged) - 1} pairs) → saved to duplicate_review_flagged.tsv")
    print(f"  ✗ REJECTED ({len(dup_rejected)} pairs) → not merged\n")

    print(f"Author Name Variants:")
    print(f"  ✓ AUTO_ACCEPT ({len(auth_accept)} pairs) → apply with 10_apply_merges.py")
    print(f"  ? FLAGGED ({len(auth_flagged) - 1} pairs) → saved to author_review_flagged.tsv")
    print(f"  ✗ REJECTED ({len(auth_rejected)} pairs) → not merged\n")

    print("Output files:")
    print(f"  • auto_review_log.json")
    print(f"  • duplicate_auto_decisions.json")
    print(f"  • author_auto_decisions.json")
    if len(dup_flagged) > 1:
        print(f"  • duplicate_review_flagged.tsv (requires human review)")
    if len(auth_flagged) > 1:
        print(f"  • author_review_flagged.tsv (requires human review)")

    print(f"\nNext steps:")
    if len(dup_flagged) > 1:
        print(f"  1. Review duplicate_review_flagged.tsv (manually decide on {len(dup_flagged) - 1} pairs)")
    if len(auth_flagged) > 1:
        print(f"  2. Review author_review_flagged.tsv (manually decide on {len(auth_flagged) - 1} pairs)")
    print(f"  3. Run: python 12_apply_duplicate_merges.py (to apply auto-accepted decisions)")
    print(f"  4. Run: python 10_apply_merges.py (to apply author merges)")
    print(f"  5. Run: python 03_compute_metrics.py (re-rank corpus)")


if __name__ == "__main__":
    main()
