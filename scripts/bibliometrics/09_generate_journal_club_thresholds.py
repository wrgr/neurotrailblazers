#!/usr/bin/env python3
"""
Generate journal club papers at different importance thresholds.

Takes journal_club_revised.json and filters by role_weighted_score to create
papers at different selectivity levels.
"""
import json
from pathlib import Path

OUTPUT_DIR = Path("output")

THRESHOLDS = {
    10: ("Inclusive", 0.10),
    15: ("Moderate", 0.15),
    20: ("Core", 0.20),
    30: ("Strict", 0.30),
}


def main():
    print("Loading journal club papers...")
    with open(OUTPUT_DIR / "journal_club_revised.json") as f:
        all_papers = json.load(f)

    print(f"Total papers: {len(all_papers)}")

    # Sort by role_weighted_score descending
    all_papers.sort(key=lambda p: p.get('role_weighted_score', 0), reverse=True)

    for threshold_num, (label, score_threshold) in THRESHOLDS.items():
        # Filter papers by threshold
        filtered = [
            p for p in all_papers
            if p.get('role_weighted_score', 0) >= score_threshold
        ]

        # Assign tiers
        for p in filtered:
            score = p.get('role_weighted_score', 0)
            if score >= 0.40:
                p['tier'] = 'Platinum'
            elif score >= 0.30:
                p['tier'] = 'Gold'
            elif score >= 0.20:
                p['tier'] = 'Silver'
            else:
                p['tier'] = 'Bronze'

        # Save JSON
        json_path = OUTPUT_DIR / f"journal_club_threshold_{threshold_num}.json"
        with open(json_path, "w") as f:
            json.dump(filtered, f, indent=2)

        # Count by tier
        tier_counts = {}
        for p in filtered:
            tier = p.get('tier', 'Bronze')
            tier_counts[tier] = tier_counts.get(tier, 0) + 1

        print(f"\n✓ Threshold {threshold_num} ({label}, ≥{score_threshold}):")
        print(f"  Total: {len(filtered)} papers")
        for tier in ['Platinum', 'Gold', 'Silver', 'Bronze']:
            count = tier_counts.get(tier, 0)
            if count > 0:
                print(f"  - {tier}: {count}")


if __name__ == "__main__":
    main()
