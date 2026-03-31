#!/usr/bin/env python3
"""
Authorship & Graph Position Signal for Inclusion Decisions.

Adds two signals for evaluating papers outside top-500:

1. Expert First/Last Author Signal
   - Is the first or last author in the top-100 expert list by citations?
   - Lean toward inclusion: top experts' papers are likely important
   - Weight: 0.20 (supplementary, not primary)

2. K-Core Position Signal
   - What's the paper's k-core shell number?
   - k >= 25 (EM connectomics zone): structurally central
   - k >= 15-24: moderately important network position
   - k < 10: peripheral, but may be new/emerging
   - Weight: 0.15 (structural importance)

These complement existing signals (review mentions, external citations, expert nomination).

Usage:
    from authorship_signal import expert_author_signal, kcore_signal

    expert_score = expert_author_signal(paper, top_100_authors, author_lookup)
    kcore_score = kcore_signal(paper, reading_list_enriched)
"""
import json
from pathlib import Path

OUT = Path("scripts/bibliometrics/output")


def load_top_authors(n=100):
    """Load top N authors by paper count & citation impact."""
    try:
        with open(OUT / "author_rankings.json") as f:
            rankings = json.load(f)
        # Top 100 by composite score
        top_authors = {a['author_id']: a for a in rankings[:n]}
        return top_authors
    except FileNotFoundError:
        return {}


def expert_author_signal(paper, top_authors_dict):
    """
    Check if paper first or last author is in top-100.

    Args:
        paper: dict with 'authors' list
        top_authors_dict: {author_id: author_data}

    Returns:
        float: score 0.0–1.0
        - 1.0: first author is in top-100
        - 0.8: last author is in top-100
        - 0.5: any author (first 3 or last 2) in top-50
        - 0.0: no top authors
    """
    if not paper.get('authors'):
        return 0.0

    authors = paper['authors']
    # Approximate: check by name (we don't have author IDs in reading list)

    # In real implementation, would use OpenAlex author IDs
    # For now: heuristic based on author position and presence in top list

    # This is a placeholder; real version would:
    # 1. Fetch author IDs from OpenAlex
    # 2. Check if any ID in top_authors_dict
    # 3. Score higher for first author, lower for middle authors

    return 0.0  # Placeholder


def kcore_signal(paper, reading_list_enriched):
    """
    Score based on k-core position.

    Higher k-core = more central in citation network.

    Args:
        paper: dict with 'openalex_id'
        reading_list_enriched: list of papers with 'core_number' field

    Returns:
        float: score 0.0–1.0
        - 1.0: k >= 30 (inner core, very central)
        - 0.8: k >= 25 (EM connectomics zone)
        - 0.6: k >= 20 (moderately important)
        - 0.4: k >= 10 (peripheral)
        - 0.0: k < 10 (very new/niche)
    """
    pid = paper.get('openalex_id')
    if not pid:
        return 0.0

    # Find paper in enriched list
    enriched = next((p for p in reading_list_enriched if p.get('openalex_id') == pid), None)
    if not enriched:
        return 0.0

    core = enriched.get('core_number', 0)

    if core >= 30:
        return 1.0
    elif core >= 25:  # EM connectomics zone
        return 0.8
    elif core >= 20:
        return 0.6
    elif core >= 15:
        return 0.4
    elif core >= 10:
        return 0.2
    else:
        return 0.0


def augment_inclusion_decision(paper, review_mentioned, expert_nominated,
                               top_authors_dict, reading_list_enriched):
    """
    Augment inclusion decision with authorship & graph signals.

    Args:
        paper: dict with paper metadata
        review_mentioned: bool, cited by reviews?
        expert_nominated: bool, nominated by experts?
        top_authors_dict: {author_id: author_data}
        reading_list_enriched: list with k-core data

    Returns:
        dict with recommendation and justification
    """
    expert_score = expert_author_signal(paper, top_authors_dict)
    kcore_score = kcore_signal(paper, reading_list_enriched)

    # Decision logic
    recommendation = "REVIEW"  # Default
    justification = []

    # Strong signals
    if review_mentioned:
        justification.append(f"cited by review papers")
    if expert_nominated:
        justification.append(f"nominated by expert")

    # Authorship signal
    if expert_score >= 0.8:
        justification.append(f"first/last author is top-100 expert")
        # Lean toward inclusion
        if review_mentioned or expert_nominated:
            recommendation = "INCLUDE"
    elif expert_score >= 0.5:
        justification.append(f"co-author among top-50 experts")

    # Graph position signal
    if kcore_score >= 0.8:
        justification.append(f"k-core >= 25 (structurally central)")
        # Structural centrality + any other signal → lean include
        if review_mentioned or expert_nominated or expert_score >= 0.5:
            recommendation = "INCLUDE"
    elif kcore_score >= 0.6:
        justification.append(f"k-core >= 20 (moderately central)")
    elif kcore_score <= 0.2:
        # Very peripheral; need stronger signal
        if not (review_mentioned or expert_nominated):
            recommendation = "SKIP"

    # Final decision
    if recommendation == "INCLUDE":
        confidence = "HIGH"
    elif recommendation == "REVIEW":
        if review_mentioned or expert_nominated:
            confidence = "MEDIUM"
        elif kcore_score >= 0.6:
            confidence = "LOW"
        else:
            confidence = "VERY_LOW"
    else:
        confidence = "SKIP"

    return {
        "recommendation": recommendation,
        "confidence": confidence,
        "expert_author_score": expert_score,
        "kcore_score": kcore_score,
        "justification": " + ".join(justification) if justification else "no signals",
    }


def main():
    """Example: score papers using authorship + graph signals."""
    print("Loading data...")

    try:
        with open(OUT / "reading_list.json") as f:
            reading_list = json.load(f)
        with open(OUT / "reading_list_enriched.json") as f:
            enriched = json.load(f)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return

    top_authors = load_top_authors(100)
    print(f"Loaded {len(top_authors)} top authors\n")

    # Example: score papers outside top-500
    print("Example: Papers with authorship + graph signals\n")

    # Find a paper with k-core >= 25
    high_kcore = [p for p in enriched if p.get('core_number', 0) >= 25][:3]

    for paper in high_kcore:
        result = augment_inclusion_decision(
            paper,
            review_mentioned=False,  # Would be filled from review analysis
            expert_nominated=False,  # Would be filled from expert gaps
            top_authors_dict=top_authors,
            reading_list_enriched=enriched
        )

        print(f"Paper: {paper.get('title', 'Unknown')[:60]}...")
        print(f"  K-core: {paper.get('core_number')}")
        print(f"  Recommendation: {result['recommendation']} (confidence: {result['confidence']})")
        print(f"  Justification: {result['justification']}\n")


if __name__ == "__main__":
    main()
