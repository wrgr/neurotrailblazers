#!/usr/bin/env python3
"""
Step 10: Analyze paper importance through in/out degree for ALL papers.

Uses paper_rankings_all.json to ensure complete coverage.
"""
import json
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path("output")


def load_graph_edges():
    """Load edges from citation graph."""
    with open(OUTPUT_DIR / "graphs" / "citation_graph.json") as f:
        graph = json.load(f)
    return graph.get("links", [])


def load_rankings_all():
    """Load paper rankings for ALL papers."""
    with open(OUTPUT_DIR / "paper_rankings_all.json") as f:
        return {p['openalex_id']: p for p in json.load(f)}


def load_kcore():
    """Load k-core data."""
    with open(OUTPUT_DIR / "kcore_tiers_annotated.json") as f:
        return json.load(f)


def load_corpus():
    """Load corpus."""
    with open(OUTPUT_DIR / "corpus_final.json") as f:
        return {p['openalex_id']: p for p in json.load(f)}


def main():
    print("Loading data...")
    edges = load_graph_edges()
    rankings = load_rankings_all()
    kcore = load_kcore()
    corpus = load_corpus()

    # Compute in/out degree
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for edge in edges:
        source = edge.get('source')
        target = edge.get('target')
        out_degree[source] += 1
        in_degree[target] += 1

    print(f"Computed in/out degree for {len(in_degree)} papers")

    # Create paper profiles for ALL papers
    profiles = []

    for pid, rank in rankings.items():
        corpus_p = corpus.get(pid, {})
        k = kcore.get(pid, {}).get('k_core', 0)

        in_deg = in_degree.get(pid, 0)
        out_deg = out_degree.get(pid, 0)

        # In/Out ratio characterizes role
        ratio = in_deg / max(out_deg, 1)  # Avoid division by zero

        profiles.append({
            'openalex_id': pid,
            'title': corpus_p.get('title', 'Unknown')[:100],
            'year': corpus_p.get('year', 0),
            'type': corpus_p.get('type', 'unknown'),
            'citations': corpus_p.get('cited_by_count', 0),

            # Network position
            'in_degree': in_deg,           # How many papers cite this
            'out_degree': out_deg,          # How many papers this cites
            'in_out_ratio': round(ratio, 2),

            # Role indicators
            'is_foundational': ratio > 2,   # High citations relative to references
            'is_methodological': ratio < 0.5,  # Cites many, cited less
            'is_synthesis': 1000 <= in_deg <= 5000,  # Moderately cited, broad impact
            'is_landmark': in_deg > 500,    # Highly cited

            # Network metrics
            'pagerank': rank.get('pagerank', 0),
            'betweenness': rank.get('betweenness', 0),
            'composite_score': rank.get('composite_score', 0),
            'k_core': k,

            # Inferred role
            'inferred_role': (
                'landmark_dataset' if in_deg > 500 and 'connectom' in corpus_p.get('title', '').lower()
                else 'foundational' if ratio > 2 and in_deg > 100
                else 'methodological' if ratio < 0.5 and out_deg > 50
                else 'synthesis_review' if ratio > 1 and out_deg > 30
                else 'applied_biology' if ratio > 1 and in_deg > 50
                else 'emerging'
            )
        })

    # Sort by composite importance (PageRank as proxy for overall)
    profiles.sort(key=lambda p: p['composite_score'], reverse=True)

    # Save
    with open(OUTPUT_DIR / "paper_role_analysis.json", "w") as f:
        json.dump(profiles, f, indent=2)

    print(f"✓ Saved: paper_role_analysis.json ({len(profiles)} papers)\n")

    # Statistics
    role_counts = defaultdict(int)
    for p in profiles:
        role_counts[p['inferred_role']] += 1

    print("Paper roles distribution:")
    for role, count in sorted(role_counts.items(), key=lambda x: -x[1]):
        print(f"  {role:20s}: {count:4d} papers")

    # Top papers by in/out degree
    print("\nTop 10 by IN-DEGREE (foundational/cited):")
    for p in sorted(profiles, key=lambda x: -x['in_degree'])[:10]:
        print(f"  In:{p['in_degree']:4d} Out:{p['out_degree']:3d} | {p['year']} | {p['title'][:60]}...")

    print("\nTop 10 by OUT-DEGREE (synthesizing/methodological):")
    for p in sorted(profiles, key=lambda x: -x['out_degree'])[:10]:
        print(f"  In:{p['in_degree']:4d} Out:{p['out_degree']:3d} | {p['year']} | {p['title'][:60]}...")

    print("\nHighest IN/OUT RATIO (foundational vs methods):")
    for p in sorted(profiles, key=lambda x: -x['in_out_ratio'])[:10]:
        print(f"  Ratio:{p['in_out_ratio']:5.2f} | In:{p['in_degree']:4d} Out:{p['out_degree']:3d} | {p['title'][:60]}...")


if __name__ == "__main__":
    main()
