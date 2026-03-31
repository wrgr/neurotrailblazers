#!/usr/bin/env python3
"""
Step 13b: Compile inclusion decisions for corpus expansion.

Combines signals from:
- review_cited_candidates.json (from 13_review_citations.py)
- expert_list_gaps.json (from 09_graph_analysis.py)
- duplicate_merge_log.json (from 12_apply_duplicate_merges.py)

Produces a decision log with inclusion criteria for each paper.

Usage:
    python 13_inclusion_decisions.py
"""
import json
from pathlib import Path
from collections import defaultdict

from config import OUTPUT_DIR


def load_json(name):
    """Load a JSON file from OUTPUT_DIR."""
    path = OUTPUT_DIR / name
    if not path.exists():
        print(f"Warning: {name} not found")
        return {}
    with open(path) as f:
        return json.load(f)


def main():
    print("Loading analysis files...")

    # Load previous analyses
    review_candidates = load_json("review_cited_candidates.json")
    expert_gaps = load_json("expert_list_gaps.json")
    reading_list = load_json("reading_list.json")

    # Compile decisions
    decisions = {
        "promote_from_tail": [],
        "add_missing_expert": [],
        "add_from_reviews": [],
        "flag_ambiguous": [],
        "summary": {},
    }

    # ── Decision 1: Promote from tail (rank 201–500) ──────────────────────
    # Criteria: expert-nominated + in_corpus + external_cites > 500 + em_connectomics

    expert_in_corpus = expert_gaps.get('A_expert_in_corpus', [])
    for paper in expert_in_corpus:
        if paper.get('external_citations', 0) > 500:
            decisions["promote_from_tail"].append({
                "doi": paper.get('doi'),
                "title": paper.get('title'),
                "dimension": paper.get('dimension'),
                "external_citations": paper.get('external_citations'),
                "criteria": "expert_nominated + in_corpus + external_cites > 500",
                "justification": f"{paper.get('external_citations')} external citations; "
                                f"expert identified this as important; "
                                f"low composite score likely due to specialized niche",
            })

    # ── Decision 2: Add missing expert papers ───────────────────────────────
    # Papers nominated by experts but not in OpenAlex

    expert_missing = expert_gaps.get('A_expert_missing', [])
    for paper in expert_missing:
        decisions["add_missing_expert"].append({
            "doi": paper.get('doi'),
            "title": paper.get('title'),
            "dimension": paper.get('dimension'),
            "external_citations": paper.get('external_citations'),
            "criteria": "expert_nominated + not_in_openAlex",
            "justification": f"Expert identified as important; "
                            f"{paper.get('external_citations')} external citations",
            "action": "Add DOI to EXTRA_SEED_DOIS in config.py and re-run harvest",
        })

    # ── Decision 3: Add papers cited by multiple reviews ────────────────────
    # Criteria: cited by 2+ reviews + (not in corpus OR high composite score)

    if review_candidates:
        for paper in review_candidates.get("add", []):
            decisions["add_from_reviews"].append({
                "doi": paper.get('doi'),
                "review_mentions": paper.get('review_mentions'),
                "criteria": "cited_by_2plus_reviews + not_in_corpus",
                "justification": f"Cited by {paper.get('review_mentions')} major reviews; "
                                f"likely important but not captured by automated corpus",
                "action": "Add DOI to EXTRA_SEED_DOIS",
                "reviews": paper.get('reviews'),
            })

        # ── Decision 4: Flag ambiguous cases ─────────────────────────────────
        # Cited by 1 review, but has good metrics

        for paper in review_candidates.get("flag", []):
            decisions["flag_ambiguous"].append({
                "openalex_id": paper.get('openalex_id'),
                "title": paper.get('title'),
                "composite_score": paper.get('composite_score'),
                "review_mentions": paper.get('review_mentions'),
                "criteria": "cited_by_1_review + composite_score > 0.15",
                "justification": f"Cited by review {paper.get('reviews', [None])[0]}; "
                                f"score={paper.get('composite_score'):.3f} (above threshold); "
                                f"likely niche but important",
                "decision_needed": "manual review — is this infrastructure/tool paper worth adding?",
            })

    # Compute summary statistics
    total_promote = len(decisions["promote_from_tail"])
    total_add_expert = len(decisions["add_missing_expert"])
    total_add_review = len(decisions["add_from_reviews"])
    total_flag = len(decisions["flag_ambiguous"])

    decisions["summary"] = {
        "promote_from_tail_count": total_promote,
        "add_missing_expert_count": total_add_expert,
        "add_from_reviews_count": total_add_review,
        "flag_ambiguous_count": total_flag,
        "total_new_papers": total_promote + total_add_expert + total_add_review,
        "human_review_required": total_flag,
    }

    # Save decisions
    with open(OUTPUT_DIR / "inclusion_decisions.json", 'w') as f:
        json.dump(decisions, f, indent=2)

    # Print summary
    print(f"\n=== Inclusion Decision Summary ===")
    print(f"Promote to top-200: {total_promote}")
    print(f"Add from expert list: {total_add_expert}")
    print(f"Add from review cites: {total_add_review}")
    print(f"Flag for human review: {total_flag}")
    print(f"\nTotal new papers: {total_promote + total_add_expert + total_add_review}")
    print(f"Requiring human review: {total_flag}")

    if total_promote > 0:
        print(f"\nPromote candidates (top 3):")
        for p in decisions["promote_from_tail"][:3]:
            print(f"  • {p['title'][:60]}... ({p['dimension']})")

    if total_add_expert > 0:
        print(f"\nMissing expert papers (top 3):")
        for p in decisions["add_missing_expert"][:3]:
            print(f"  • {p['title'][:60]}... ({p['doi']})")

    if total_add_review > 0:
        print(f"\nReview-cited papers to add (top 3):")
        for p in decisions["add_from_reviews"][:3]:
            print(f"  • {p['doi']}")

    print(f"\nSaved → output/inclusion_decisions.json")


if __name__ == "__main__":
    main()
