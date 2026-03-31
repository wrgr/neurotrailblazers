#!/usr/bin/env python3
"""
Analyze paper importance through in/out degree with data-driven thresholds.

Key improvements:
1. Calculate methodological threshold from out-degree distribution (top 5%)
2. Classify papers by role with meaningful categories
3. Cover ALL papers in corpus
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

    # Calculate data-driven thresholds
    out_degrees = [d for d in out_degree.values() if d > 0]
    out_degrees_sorted = sorted(out_degrees, reverse=True)

    # Top 5% by out-degree (methodology/infrastructure papers)
    percentile_95 = out_degrees_sorted[max(0, len(out_degrees_sorted) // 20)]

    print(f"\nOut-degree statistics:")
    print(f"  Mean: {statistics.mean(out_degrees):.1f}")
    print(f"  Median: {statistics.median(out_degrees):.1f}")
    print(f"  Top 5% threshold: {percentile_95} references")

    in_degrees = [d for d in in_degree.values() if d > 0]
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

        # Determine role based on network position
        if in_deg > 500 and 'connectom' in corpus_p.get('title', '').lower():
            role = 'landmark_dataset'
        elif in_deg > 200:
            role = 'foundational'
        elif out_deg >= percentile_95:
            role = 'methodological_infrastructure'
        elif out_deg > 30 and in_deg > 50:
            role = 'synthesis_review'
        elif in_deg > 50:
            role = 'applied_biology'
        elif in_deg > 20 or out_deg > 15:
            role = 'specialized_research'
        else:
            role = 'niche_contribution'

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
            'is_foundational': in_deg > 200,
            'is_methodological': out_deg >= percentile_95,
            'is_synthesis': out_deg > 30 and in_deg > 50,
            'is_landmark': in_deg > 500,

            # Network metrics
            'pagerank': rank.get('pagerank', 0),
            'betweenness': rank.get('betweenness', 0),
            'composite_score': rank.get('composite_score', 0),
            'k_core': k,

            # Inferred role (meaningful categories)
            'inferred_role': role,
            'role_definition': {
                'landmark_dataset': 'Signature connectomics dataset (>500 citations)',
                'foundational': 'Foundational work (>200 citations)',
                'methodological_infrastructure': f'Methods/infrastructure paper (top 5% by out-degree, ≥{percentile_95} refs)',
                'synthesis_review': 'Synthesis/review paper (>30 refs, >50 citations)',
                'applied_biology': 'Applied biology research (>50 citations)',
                'specialized_research': 'Specialized research (>20 in OR >15 out)',
                'niche_contribution': 'Niche contribution (<20 citations, <15 references)'
            }.get(role, role)
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

    print("Paper roles distribution (data-driven thresholds):")
    print(f"  Methodological threshold: ≥{percentile_95} references (top 5%)")
    print()
    for role, count in sorted(role_counts.items(), key=lambda x: -x[1]):
        pct = 100 * count / len(profiles)
        print(f"  {role:25s}: {count:5d} papers ({pct:5.1f}%)")

    # Top papers by in/out degree
    print("\nTop 10 by IN-DEGREE (foundational/cited):")
    for p in sorted(profiles, key=lambda x: -x['in_degree'])[:10]:
        print(f"  In:{p['in_degree']:4d} Out:{p['out_degree']:3d} | {p['year']} | {p['title'][:50]}...")

    print("\nTop 10 by OUT-DEGREE (methodological/infrastructure):")
    for p in sorted(profiles, key=lambda x: -x['out_degree'])[:10]:
        print(f"  In:{p['in_degree']:4d} Out:{p['out_degree']:3d} | {p['year']} | {p['title'][:50]}...")


if __name__ == "__main__":
    main()
