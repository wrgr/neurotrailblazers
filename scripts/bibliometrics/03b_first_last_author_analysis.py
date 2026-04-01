#!/usr/bin/env python3
"""
Step 3b: First/Last Author Analysis

Generates separate metrics and rankings counting only papers where an author
is first or last author (excluding middle authors).

This analysis highlights authors who are driving new research directions
(first authors) or providing senior leadership (last authors).

Input:  output/corpus_merged.json (with author_positions metadata)
Output: output/first_author_rankings.json, last_author_rankings.json,
        first_last_author_distribution.json

Usage:
  python 03b_first_last_author_analysis.py
"""
import json
from collections import defaultdict
from pathlib import Path

from config import OUTPUT_DIR


def load_corpus():
    path = OUTPUT_DIR / "corpus_merged.json"
    with open(path) as f:
        return json.load(f)


def analyze_first_authors(corpus):
    """
    Analyze papers where author is first author.
    Returns ranking dict keyed by author ID.
    """
    metrics = defaultdict(lambda: {
        "name": "",
        "paper_count": 0,
        "papers": [],
        "years": [],
        "journals": set(),
    })

    for paper in corpus:
        positions = paper.get("author_positions", [])
        if not positions:
            continue

        # Find first author
        first_pos = positions[0]
        author_id = first_pos.get("id")
        if not author_id:
            continue

        author_name = first_pos.get("name", "")
        if author_name:
            metrics[author_id]["name"] = author_name

        metrics[author_id]["papers"].append({
            "openalex_id": paper.get("openalex_id"),
            "title": paper.get("title", "")[:100],
            "year": paper.get("year"),
            "cited_by": paper.get("cited_by_count", 0),
        })
        metrics[author_id]["years"].append(paper.get("year") or 2025)
        if paper.get("journal"):
            metrics[author_id]["journals"].add(paper.get("journal"))

    # Compute derived metrics
    results = []
    for aid, m in metrics.items():
        m["paper_count"] = len(m["papers"])
        m["total_citations"] = sum(p.get("cited_by", 0) for p in m["papers"])
        m["avg_citations"] = m["total_citations"] / max(m["paper_count"], 1)
        m["year_range"] = f"{min(m['years']) or 0}-{max(m['years']) or 2025}" if m["years"] else "N/A"
        m["journal_diversity"] = len(m["journals"])
        m["journals"] = list(m["journals"])[:5]  # Top 5 journals
        m["papers"] = m["papers"][:10]  # Top 10 papers by appearance

        results.append({
            "author_id": aid,
            "name": m.get("name", ""),
            "first_author_papers": m["paper_count"],
            "total_citations": m["total_citations"],
            "avg_citations_per_paper": round(m["avg_citations"], 1),
            "year_range": m["year_range"],
            "journals": m["journals"],
            "sample_papers": m["papers"][:5],
        })

    results.sort(key=lambda x: x["total_citations"], reverse=True)
    return results


def analyze_last_authors(corpus):
    """
    Analyze papers where author is last author.
    Returns ranking dict keyed by author ID.
    """
    metrics = defaultdict(lambda: {
        "name": "",
        "paper_count": 0,
        "papers": [],
        "years": [],
        "journals": set(),
    })

    for paper in corpus:
        positions = paper.get("author_positions", [])
        if not positions:
            continue

        # Find last author
        last_pos = positions[-1]
        author_id = last_pos.get("id")
        if not author_id:
            continue

        author_name = last_pos.get("name", "")
        if author_name:
            metrics[author_id]["name"] = author_name

        metrics[author_id]["papers"].append({
            "openalex_id": paper.get("openalex_id"),
            "title": paper.get("title", "")[:100],
            "year": paper.get("year"),
            "cited_by": paper.get("cited_by_count", 0),
        })
        metrics[author_id]["years"].append(paper.get("year") or 2025)
        if paper.get("journal"):
            metrics[author_id]["journals"].add(paper.get("journal"))

    # Compute derived metrics
    results = []
    for aid, m in metrics.items():
        m["paper_count"] = len(m["papers"])
        m["total_citations"] = sum(p.get("cited_by", 0) for p in m["papers"])
        m["avg_citations"] = m["total_citations"] / max(m["paper_count"], 1)
        m["year_range"] = f"{min(m['years']) or 0}-{max(m['years']) or 2025}" if m["years"] else "N/A"
        m["journal_diversity"] = len(m["journals"])
        m["journals"] = list(m["journals"])[:5]

        results.append({
            "author_id": aid,
            "name": m.get("name", ""),
            "last_author_papers": m["paper_count"],
            "total_citations": m["total_citations"],
            "avg_citations_per_paper": round(m["avg_citations"], 1),
            "year_range": m["year_range"],
            "journals": m["journals"],
            "sample_papers": m["papers"][:5],
        })

    results.sort(key=lambda x: x["total_citations"], reverse=True)
    return results


def analyze_first_and_last(corpus):
    """
    Analyze papers where author is BOTH first and last author (likely single-author or very small teams).
    These authors drive complete research directions.
    """
    metrics = defaultdict(lambda: {
        "name": "",
        "paper_count": 0,
        "papers": [],
    })

    for paper in corpus:
        positions = paper.get("author_positions", [])
        if not positions or len(positions) < 2:
            continue

        first_id = positions[0].get("id")
        last_id = positions[-1].get("id")

        # Check for first and last (or overlap)
        if first_id and first_id == last_id:
            # Single author paper
            metrics[first_id]["name"] = positions[0].get("name", "")
            metrics[first_id]["papers"].append(paper.get("openalex_id"))
            metrics[first_id]["paper_count"] += 1

    results = []
    for aid, m in metrics.items():
        results.append({
            "author_id": aid,
            "name": m.get("name", ""),
            "single_author_papers": m["paper_count"],
        })

    results.sort(key=lambda x: x["single_author_papers"], reverse=True)
    return results


def save_json(data, filename):
    path = OUTPUT_DIR / filename
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  Saved to {path}")


def main():
    print("Loading corpus...")
    corpus = load_corpus()
    print(f"  {len(corpus)} papers")

    print("\n--- First Author Analysis ---")
    first_authors = analyze_first_authors(corpus)
    save_json(first_authors[:500], "first_author_rankings.json")
    print(f"  Top 5 first authors:")
    for a in first_authors[:5]:
        print(f"    [{a['total_citations']} citations] {a['name']} "
              f"({a['first_author_papers']} first-author papers)")

    print("\n--- Last Author Analysis ---")
    last_authors = analyze_last_authors(corpus)
    save_json(last_authors[:500], "last_author_rankings.json")
    print(f"  Top 5 last authors:")
    for a in last_authors[:5]:
        print(f"    [{a['total_citations']} citations] {a['name']} "
              f"({a['last_author_papers']} last-author papers)")

    print("\n--- First & Last Author Analysis (Single Author Papers) ---")
    first_last = analyze_first_and_last(corpus)
    save_json(first_last[:500], "single_author_rankings.json")
    print(f"  Top 5 single-author contributors:")
    for a in first_last[:5]:
        print(f"    {a['name']} ({a['single_author_papers']} papers)")

    # Summary distribution
    distribution = {
        "total_papers": len(corpus),
        "papers_with_position_data": sum(1 for p in corpus if p.get("author_positions")),
        "first_author_count": len(first_authors),
        "last_author_count": len(last_authors),
        "single_author_papers": sum(a["single_author_papers"] for a in first_last),
        "top_first_authors": first_authors[:10],
        "top_last_authors": last_authors[:10],
    }
    save_json(distribution, "first_last_author_distribution.json")

    print("\nDone.")


if __name__ == "__main__":
    main()
