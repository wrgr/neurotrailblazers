#!/usr/bin/env python3
"""
Step 11: Extend metrics to ALL papers in corpus.

Problem: paper_rankings.json only has ~2,000 papers
Solution: Compute metrics for all 7,504 papers using available data

For papers without full metrics, use:
- In-degree / Out-degree (from citation graph)
- K-core value
- Citation count
- Create composite score from these

Output: paper_rankings_all.json (7,504 papers)
"""
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

OUTPUT_DIR = Path("output")

CURRENT_YEAR = datetime.now().year


def normalize(values):
    """Min-max normalize values to [0, 1]."""
    if not values:
        return {}
    vals = [v for v in values.values() if v is not None and v >= 0]
    if not vals:
        return {k: 0 for k in values}
    min_val = min(vals)
    max_val = max(vals)
    if min_val == max_val:
        return {k: 0.5 if v is not None else 0 for k, v in values.items()}
    return {
        k: (v - min_val) / (max_val - min_val) if v is not None and v >= 0 else 0
        for k, v in values.items()
    }


def main():
    print("Loading data...")

    # Load corpus
    with open(OUTPUT_DIR / "corpus_final.json") as f:
        corpus = {p['openalex_id']: p for p in json.load(f)}

    # Load existing rankings
    with open(OUTPUT_DIR / "paper_rankings.json") as f:
        existing_rankings = {p['openalex_id']: p for p in json.load(f)}

    # Load graph for in/out degree
    with open(OUTPUT_DIR / "graphs" / "citation_graph.json") as f:
        graph = json.load(f)

    # Compute in/out degree
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    for edge in graph.get("links", []):
        source = edge.get('source')
        target = edge.get('target')
        out_degree[source] += 1
        in_degree[target] += 1

    # Load k-core
    with open(OUTPUT_DIR / "kcore_tiers_annotated.json") as f:
        kcore_data = json.load(f)

    # Load paper role analysis for in/out ratio
    with open(OUTPUT_DIR / "paper_role_analysis.json") as f:
        role_analysis = {p['openalex_id']: p for p in json.load(f)}

    print(f"Extending metrics to all {len(corpus)} papers...\n")

    # Build complete rankings
    all_rankings = []

    # Normalize metrics across corpus
    citations_norm = normalize({
        pid: corpus[pid].get('cited_by_count', 0) for pid in corpus
    })
    in_degree_norm = normalize(dict(in_degree))
    out_degree_norm = normalize(dict(out_degree))
    kcore_norm = normalize({pid: kcore_data.get(pid, {}).get('k_core', 0) for pid in corpus})

    for pid, paper in corpus.items():
        # Start with existing ranking if available
        if pid in existing_rankings:
            ranking = existing_rankings[pid].copy()
            ranking['source'] = 'computed'
        else:
            # Create new ranking from available metrics
            ranking = {
                'openalex_id': pid,
                'doi': paper.get('doi', ''),
                'title': paper.get('title', ''),
                'year': paper.get('year', 0),
                'role': 'unknown',
                'authors': [a.get('name', '') for a in paper.get('authors', [])[:6]],
                'total_citations': paper.get('cited_by_count', 0),
                'citations_per_year': (
                    paper.get('cited_by_count', 0) / max(CURRENT_YEAR - (paper.get('year') or CURRENT_YEAR), 1)
                ),
                'source': 'derived'
            }

            # Compute metrics from components
            in_deg = in_degree.get(pid, 0)
            out_deg = out_degree.get(pid, 0)
            k = kcore_data.get(pid, {}).get('k_core', 0)
            cites = paper.get('cited_by_count', 0)

            # Use in-degree as proxy for PageRank (correlation is high)
            ranking['pagerank'] = in_degree_norm.get(pid, 0)
            ranking['hits_hub'] = out_degree_norm.get(pid, 0)  # Out-degree proxy for hub
            ranking['hits_authority'] = in_degree_norm.get(pid, 0)  # In-degree proxy for authority
            ranking['betweenness'] = 0.1 * (in_degree_norm.get(pid, 0) + out_degree_norm.get(pid, 0)) / 2
            ranking['in_degree'] = in_deg
            ranking['out_degree'] = out_deg
            ranking['in_degree_norm'] = in_degree_norm.get(pid, 0)
            ranking['out_degree_norm'] = out_degree_norm.get(pid, 0)

            # Composite score: weighted average of available metrics
            # Weight: citations (0.3) + in-degree (0.4) + out-degree (0.15) + k-core (0.15)
            ranking['composite_score'] = (
                0.30 * citations_norm.get(pid, 0) +
                0.40 * in_degree_norm.get(pid, 0) +
                0.15 * out_degree_norm.get(pid, 0) +
                0.15 * kcore_norm.get(pid, 0)
            )

            ranking['k_core'] = k

        # Add role info if available
        if pid in role_analysis:
            role_info = role_analysis[pid]
            ranking['inferred_role'] = role_info.get('inferred_role', 'unknown')
            if 'in_degree' not in ranking:
                ranking['in_degree'] = role_info.get('in_degree', 0)
            if 'out_degree' not in ranking:
                ranking['out_degree'] = role_info.get('out_degree', 0)
            if 'in_out_ratio' not in ranking:
                ranking['in_out_ratio'] = role_info.get('in_out_ratio', 0)

        # Round floats
        for key in ['pagerank', 'hits_hub', 'hits_authority', 'betweenness', 'composite_score']:
            if key in ranking:
                ranking[key] = round(ranking[key], 6)

        all_rankings.append(ranking)

    # Sort by composite score
    all_rankings.sort(key=lambda x: x.get('composite_score', 0), reverse=True)

    # Add rank position
    for i, r in enumerate(all_rankings, 1):
        r['rank'] = i

    # Save
    with open(OUTPUT_DIR / "paper_rankings_all.json", "w") as f:
        json.dump(all_rankings, f, indent=2)

    print(f"✓ Saved paper_rankings_all.json ({len(all_rankings)} papers)\n")

    # Statistics
    computed = sum(1 for r in all_rankings if r.get('source') == 'computed')
    derived = sum(1 for r in all_rankings if r.get('source') == 'derived')

    print(f"Metrics coverage:")
    print(f"  Original paper_rankings.json: {computed} papers")
    print(f"  Extended with derived metrics: {derived} papers")
    print(f"  Total: {len(all_rankings)} papers\n")

    # Sample output
    print("Top 10 papers (all metrics):")
    for r in all_rankings[:10]:
        in_deg = r.get('in_degree', 0)
        out_deg = r.get('out_degree', 0)
        print(f"  {r['rank']:4d}. {r['title'][:60]}... (In:{in_deg} Out:{out_deg} Score:{r['composite_score']:.3f})")


if __name__ == "__main__":
    main()
