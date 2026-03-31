#!/usr/bin/env python3
"""
Compare two journal club selection approaches:
1. Full metrics: PageRank + HITS + betweenness + k-core
2. Simple metrics: Citations + k-core only

Generates ranked paper lists for both approaches, focusing on connectomics communities.
"""
import json
import math
from pathlib import Path
from collections import defaultdict

OUT = Path("output")


def load_json(name):
    with open(OUT / name) as f:
        return json.load(f)


def normalize(values):
    """Min-max normalize values to [0, 1]."""
    if not values:
        return {}
    min_val = min(values.values())
    max_val = max(values.values())
    if min_val == max_val:
        return {k: 0.5 for k in values}
    return {k: (v - min_val) / (max_val - min_val) for k, v in values.items()}


def main():
    print("Loading data...")
    rankings = load_json("paper_rankings.json")
    kcore = load_json("kcore_tiers_annotated.json")
    communities = load_json("communities.json")
    corpus = load_json("corpus_merged.json")

    # Build lookup tables
    rankings_by_id = {r["openalex_id"]: r for r in rankings}
    corpus_by_id = {p["openalex_id"]: p for p in corpus}

    # Identify connectomics communities
    connectomics_communities = set()
    for c in communities:
        top_labels = [x["name"].lower() for x in c.get("top_concepts", [])[:3]]
        is_noise = any(x in " ".join(top_labels) for x in
                      ["geology", "seismology", "chromatography", "mass spectrometry"])
        if not is_noise:
            connectomics_communities.add(c["community_id"])

    print(f"Connectomics communities: {len(connectomics_communities)}")

    # Build data for all papers in connectomics communities
    papers = []
    for pid, k_core_data in kcore.items():
        corpus_p = corpus_by_id.get(pid, {})
        rank_p = rankings_by_id.get(pid, {})

        # Get community assignment
        cid = None
        for c in communities:
            if pid in c.get("members", []):
                cid = c["community_id"]
                break

        if cid not in connectomics_communities:
            continue

        papers.append({
            "openalex_id": pid,
            "title": corpus_p.get("title", "Unknown"),
            "year": corpus_p.get("year", 0),
            "doi": corpus_p.get("doi", ""),
            "citations": corpus_p.get("cited_by_count", 0),
            "kcore": k_core_data.get("k_core", 0),
            "pagerank": rank_p.get("pagerank", 0),
            "hits_hub": rank_p.get("hits_hub", 0),
            "hits_authority": rank_p.get("hits_authority", 0),
            "betweenness": rank_p.get("betweenness", 0),
            "composite_score": rank_p.get("composite_score", 0),
            "community_id": cid,
        })

    print(f"Papers in connectomics communities: {len(papers)}")

    # ── APPROACH A: Full metrics (PageRank + HITS + betweenness) ──────────
    print("\n" + "="*70)
    print("APPROACH A: Full Metrics (PageRank + HITS + Betweenness + K-Core)")
    print("="*70)

    # For papers with composite_score, use it. Otherwise compute from components.
    approach_a_scores = {}
    for p in papers:
        pid = p["openalex_id"]
        if p["composite_score"] > 0:
            # Already have composite score
            approach_a_scores[pid] = p["composite_score"]
        elif p["pagerank"] > 0 or p["hits_hub"] > 0:
            # Compute from components if available
            # Weights: 0.35 PageRank, 0.25 HITS hub, 0.20 HITS authority, 0.20 betweenness
            score = (0.35 * p["pagerank"] +
                    0.25 * p["hits_hub"] +
                    0.20 * p["hits_authority"] +
                    0.20 * max(p["betweenness"], 0))
            approach_a_scores[pid] = score
        else:
            approach_a_scores[pid] = 0

    # Normalize metrics
    normalized_composite = normalize(approach_a_scores)
    normalized_kcore = normalize({p["openalex_id"]: p["kcore"] for p in papers})

    # Combine: 60% composite score + 40% k-core
    approach_a_results = []
    for p in papers:
        pid = p["openalex_id"]
        score = 0.6 * normalized_composite.get(pid, 0) + 0.4 * normalized_kcore.get(pid, 0)
        approach_a_results.append({
            **p,
            "composite_component": normalized_composite.get(pid, 0),
            "kcore_component": normalized_kcore.get(pid, 0),
            "combined_score": round(score, 4),
        })

    approach_a_results.sort(key=lambda x: x["combined_score"], reverse=True)

    # ── APPROACH B: Simple metrics (Citations + K-Core) ────────────────────
    print("\nAPPROACH B: Simple Metrics (Citations + K-Core only)")
    print("="*70)

    normalized_citations = normalize({p["openalex_id"]: p["citations"] for p in papers})

    approach_b_results = []
    for p in papers:
        pid = p["openalex_id"]
        score = 0.6 * normalized_citations.get(pid, 0) + 0.4 * normalized_kcore.get(pid, 0)
        approach_b_results.append({
            **p,
            "citations_component": normalized_citations.get(pid, 0),
            "kcore_component": normalized_kcore.get(pid, 0),
            "combined_score": round(score, 4),
        })

    approach_b_results.sort(key=lambda x: x["combined_score"], reverse=True)

    # Save both approaches
    with open(OUT / "journal_club_approach_a_full_metrics.json", "w") as f:
        json.dump(approach_a_results, f, indent=2)

    with open(OUT / "journal_club_approach_b_citations_kcore.json", "w") as f:
        json.dump(approach_b_results, f, indent=2)

    print(f"\nSaved: journal_club_approach_a_full_metrics.json ({len(approach_a_results)} papers)")
    print(f"Saved: journal_club_approach_b_citations_kcore.json ({len(approach_b_results)} papers)")

    # Compare top selections at different thresholds
    print("\n" + "="*70)
    print("COMPARISON AT DIFFERENT THRESHOLDS")
    print("="*70)

    thresholds = [0.50, 0.40, 0.30, 0.20]
    for threshold in thresholds:
        count_a = sum(1 for p in approach_a_results if p["combined_score"] >= threshold)
        count_b = sum(1 for p in approach_b_results if p["combined_score"] >= threshold)
        print(f"\nThreshold ≥ {threshold}:")
        print(f"  Approach A (full metrics): {count_a} papers")
        print(f"  Approach B (citations+kcore): {count_b} papers")

    # Show top 10 in each approach for comparison
    print("\n" + "="*70)
    print("TOP 10 PAPERS BY EACH APPROACH")
    print("="*70)

    print("\nAPPROACH A - Full Metrics:")
    for i, p in enumerate(approach_a_results[:10], 1):
        print(f"{i}. [{p['combined_score']:.3f}] {p['title'][:70]}... (y:{p['year']} k:{p['kcore']})")

    print("\nAPPROACH B - Citations + K-Core:")
    for i, p in enumerate(approach_b_results[:10], 1):
        print(f"{i}. [{p['combined_score']:.3f}] {p['title'][:70]}... (y:{p['year']} k:{p['kcore']})")

    # Compare overlap
    top_50_a = {p["openalex_id"] for p in approach_a_results[:50]}
    top_50_b = {p["openalex_id"] for p in approach_b_results[:50]}
    overlap = len(top_50_a & top_50_b)

    print(f"\n" + "="*70)
    print(f"Top 50 overlap: {overlap}/50 papers ({100*overlap/50:.1f}%)")
    print(f"Approach A only: {len(top_50_a - top_50_b)}")
    print(f"Approach B only: {len(top_50_b - top_50_a)}")

    # Community distribution in top selections
    def community_stats(results, name, threshold=0.40):
        selected = [p for p in results if p["combined_score"] >= threshold]
        comm_dist = defaultdict(int)
        for p in selected:
            comm_dist[p["community_id"]] += 1

        print(f"\n{name} (≥{threshold}):")
        print(f"  Total: {len(selected)} papers")
        print(f"  Communities: {len(comm_dist)}")
        for cid in sorted(comm_dist.keys(), key=lambda x: comm_dist[x], reverse=True):
            print(f"    Community {cid}: {comm_dist[cid]} papers")

    print("\n" + "="*70)
    print("COMMUNITY DISTRIBUTION")
    print("="*70)
    community_stats(approach_a_results, "Approach A")
    community_stats(approach_b_results, "Approach B")


if __name__ == "__main__":
    main()
