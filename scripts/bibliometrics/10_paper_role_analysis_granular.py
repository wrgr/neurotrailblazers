#!/usr/bin/env python3
"""
Analyze paper importance with granular role categories.

Philosophy: Better to have false positives (over-classify importance) than false negatives.
- Lower thresholds: 10 for each direction (not 20/15)
- More granular categories: Divide niche/specialized into meaningful buckets
- Capture emerging methods and papers that may not yet have heavy citation footprint
"""
import json
from pathlib import Path
from collections import defaultdict
import statistics

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

    # Calculate statistics for reference
    out_degrees = [d for d in out_degree.values() if d > 0]
    in_degrees = [d for d in in_degree.values() if d > 0]

    print(f"\nOut-degree statistics:")
    print(f"  Mean: {statistics.mean(out_degrees):.1f}")
    print(f"  Median: {statistics.median(out_degrees):.1f}")
    print(f"  Top 5% threshold: {sorted(out_degrees, reverse=True)[len(out_degrees)//20]}")

    print(f"\nIn-degree statistics:")
    print(f"  Mean: {statistics.mean(in_degrees):.1f}")
    print(f"  Median: {statistics.median(in_degrees):.1f}")

    # Create paper profiles for ALL papers
    profiles = []

    for pid, rank in rankings.items():
        corpus_p = corpus.get(pid, {})
        k = kcore.get(pid, {}).get('k_core', 0)

        in_deg = in_degree.get(pid, 0)
        out_deg = out_degree.get(pid, 0)

        # In/Out ratio characterizes role
        ratio = in_deg / max(out_deg, 1)

        # GRANULAR ROLE CLASSIFICATION
        # Philosophy: Better false positives than false negatives
        # Thresholds: 10 for each direction (not 20/15 or 50)

        if in_deg > 500 and 'connectom' in corpus_p.get('title', '').lower():
            role = 'landmark_connectome'
        elif in_deg > 300:
            role = 'landmark_influential'
        elif in_deg > 100:
            role = 'foundational'
        elif in_deg > 50:
            role = 'well_cited'
        elif out_deg >= 50:
            role = 'methods_infrastructure'
        elif out_deg >= 30:
            role = 'synthesis_integration'
        elif out_deg >= 10 and in_deg >= 10:
            role = 'balanced_contribution'
        elif out_deg >= 10:
            role = 'methodological_focus'
        elif in_deg >= 10:
            role = 'cited_technical'
        elif out_deg > 0 or in_deg > 0:
            role = 'active_contributor'
        else:
            role = 'orphaned_paper'

        profiles.append({
            'openalex_id': pid,
            'title': corpus_p.get('title', 'Unknown')[:100],
            'year': corpus_p.get('year', 0),
            'type': corpus_p.get('type', 'unknown'),
            'citations': corpus_p.get('cited_by_count', 0),

            # Network position
            'in_degree': in_deg,
            'out_degree': out_deg,
            'in_out_ratio': round(ratio, 2),

            # Role indicators
            'is_landmark': in_deg > 100,
            'is_methodological': out_deg >= 10,
            'is_cited': in_deg >= 10,
            'is_infrastructure': out_deg >= 50,

            # Network metrics
            'pagerank': rank.get('pagerank', 0),
            'betweenness': rank.get('betweenness', 0),
            'composite_score': rank.get('composite_score', 0),
            'k_core': k,

            # Inferred role (granular categories)
            'inferred_role': role
        })

    # Sort by composite importance
    profiles.sort(key=lambda p: p['composite_score'], reverse=True)

    # Save
    with open(OUTPUT_DIR / "paper_role_analysis.json", "w") as f:
        json.dump(profiles, f, indent=2)

    print(f"\n✓ Saved: paper_role_analysis.json ({len(profiles)} papers)\n")

    # Statistics
    role_counts = defaultdict(int)
    for p in profiles:
        role_counts[p['inferred_role']] += 1

    print("Paper roles distribution (granular thresholds, lower bounds):")
    print(f"  Thresholds: 10+ in-degree OR 10+ out-degree captures active research")
    print()
    for role, count in sorted(role_counts.items(), key=lambda x: -x[1]):
        pct = 100 * count / len(profiles)
        print(f"  {role:25s}: {count:5d} papers ({pct:5.1f}%)")

    # Top papers by in/out degree
    print("\nTop 10 by IN-DEGREE (highly cited/influential):")
    for p in sorted(profiles, key=lambda x: -x['in_degree'])[:10]:
        print(f"  In:{p['in_degree']:4d} Out:{p['out_degree']:3d} | Role:{p['inferred_role']:20s} | {p['title'][:45]}...")

    print("\nTop 10 by OUT-DEGREE (methods/infrastructure/synthesis):")
    for p in sorted(profiles, key=lambda x: -x['out_degree'])[:10]:
        print(f"  In:{p['in_degree']:4d} Out:{p['out_degree']:3d} | Role:{p['inferred_role']:20s} | {p['title'][:45]}...")

    print("\nPapers with (In≥10 AND Out≥10) — balanced contributions:")
    balanced = [p for p in profiles if p['in_degree'] >= 10 and p['out_degree'] >= 10]
    print(f"  Count: {len(balanced)}")
    for p in sorted(balanced, key=lambda x: -x['composite_score'])[:10]:
        print(f"  In:{p['in_degree']:4d} Out:{p['out_degree']:3d} | {p['title'][:55]}...")


if __name__ == "__main__":
    main()
