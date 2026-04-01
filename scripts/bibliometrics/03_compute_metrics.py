#!/usr/bin/env python3
"""
Step 3: Compute centrality metrics, role classification, and community detection.

Input:  output/graphs/*.json, output/corpus_merged.json
Output: output/citation_baseline.json, paper_rankings.json,
        author_rankings.json, communities.json

Usage:
  python 03_compute_metrics.py
"""
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import networkx as nx
from networkx.readwrite import json_graph

from config import OUTPUT_DIR


CURRENT_YEAR = datetime.now().year


def load_graph(filename):
    """Load a graph from D3 node-link JSON."""
    path = OUTPUT_DIR / "graphs" / filename
    with open(path) as f:
        data = json.load(f)

    # Handle both "links" (D3 format) and "edges" (NetworkX format)
    if "links" in data and "edges" not in data:
        data["edges"] = data.pop("links")

    return json_graph.node_link_graph(data)


def load_corpus():
    path = OUTPUT_DIR / "corpus_merged.json"
    with open(path) as f:
        return json.load(f)


# ── Paper Role Classification ─────────────────────────────────────────

METHODS_KEYWORDS = {"algorithm", "segmentation", "software", "pipeline",
                    "framework", "detection", "network architecture",
                    "deep learning", "machine learning", "tool"}

DATASET_PATTERNS = [
    r"connectome", r"dataset", r"atlas", r"reconstruction of",
    r"whole.brain", r"dense reconstruction", r"release",
]

BIOLOGY_KEYWORDS = {"neuron", "synapse", "circuit", "wiring", "cell type",
                    "interneuron", "projection", "behavior", "modulation",
                    "sensory", "motor", "olfactory", "visual"}


def classify_paper_role(paper):
    """
    Classify paper as 'methods', 'dataset', 'biology', or 'review'.
    Uses OpenAlex concepts and title patterns.
    """
    title = (paper.get("title") or "").lower()
    paper_type = (paper.get("type") or "").lower()
    concept_names = {c.get("name", "").lower() for c in paper.get("concepts", [])}

    if paper_type == "review" or "review" in title or "survey" in title:
        return "review"

    methods_score = len(concept_names & METHODS_KEYWORDS)
    dataset_score = sum(1 for p in DATASET_PATTERNS if re.search(p, title))
    biology_score = len(concept_names & BIOLOGY_KEYWORDS)

    if dataset_score >= 2:
        return "dataset"
    if methods_score > biology_score:
        return "methods"
    if biology_score > 0:
        return "biology"
    return "methods"  # default


# ── Tier 0: Citation Baseline ─────────────────────────────────────────

def compute_citation_baseline(corpus):
    """
    Pure citation-count ranking. No graph analysis needed.
    Returns sorted list of papers with total_citations and citations_per_year.
    """
    results = []
    for paper in corpus:
        year = paper.get("year") or CURRENT_YEAR
        age = max(1, CURRENT_YEAR - year + 1)
        citations = paper.get("cited_by_count", 0)
        results.append({
            "openalex_id": paper["openalex_id"],
            "doi": paper.get("doi", ""),
            "title": paper.get("title", ""),
            "year": year,
            "total_citations": citations,
            "citations_per_year": round(citations / age, 1),
            "role": classify_paper_role(paper),
            "authors": [a.get("name", "") for a in paper.get("authors", [])[:5]],
        })
    results.sort(key=lambda x: x["total_citations"], reverse=True)
    return results


# ── Tier 1: Graph Metrics ────────────────────────────────────────────

def compute_paper_graph_metrics(citation_graph):
    """
    Compute graph-derived metrics for papers.
    Returns dict keyed by openalex_id.
    """
    metrics = {}

    print("  Computing PageRank...")
    pagerank = nx.pagerank(citation_graph, alpha=0.85)

    print("  Computing HITS...")
    try:
        hubs, authorities = nx.hits(citation_graph, max_iter=200)
    except nx.PowerIterationFailedConvergence:
        hubs = {n: 0 for n in citation_graph}
        authorities = {n: 0 for n in citation_graph}

    print("  Computing betweenness (may be slow for large graphs)...")
    if citation_graph.number_of_nodes() > 2000:
        # Approximate betweenness for large graphs
        betweenness = nx.betweenness_centrality(citation_graph, k=500)
    else:
        betweenness = nx.betweenness_centrality(citation_graph)

    # Recent PageRank (2020+ subgraph)
    print("  Computing recent PageRank (2020+ subgraph)...")
    recent_nodes = [
        n for n in citation_graph.nodes()
        if (citation_graph.nodes[n].get("year") or 0) >= 2020
    ]
    recent_subgraph = citation_graph.subgraph(recent_nodes)
    if recent_subgraph.number_of_nodes() > 10:
        recent_pagerank = nx.pagerank(recent_subgraph, alpha=0.85)
    else:
        recent_pagerank = {}

    for node in citation_graph.nodes():
        metrics[node] = {
            "pagerank": pagerank.get(node, 0),
            "hits_hub": hubs.get(node, 0),
            "hits_authority": authorities.get(node, 0),
            "betweenness": betweenness.get(node, 0),
            "in_degree": citation_graph.in_degree(node),
            "out_degree": citation_graph.out_degree(node),
            "recent_pagerank": recent_pagerank.get(node, 0),
        }

    return metrics


def get_author_position_weight(position, alpha=2.0):
    """
    Get weight multiplier for author based on position.

    Args:
        position: "first", "last", "middle", or "only"
        alpha: weight multiplier for first/last authors (default 2.0)

    Returns:
        Weight multiplier (float)
    """
    if position in ("first", "last"):
        return alpha
    elif position == "only":
        return 1.0  # Single author, normal weight
    else:  # "middle"
        return 1.0


def compute_author_metrics(coauthorship_graph, corpus, paper_metrics):
    """
    Compute author-level metrics from co-authorship graph and paper metrics.
    Returns dict keyed by author OpenAlex ID.
    """
    metrics = {}

    print("  Computing co-authorship centrality...")
    if coauthorship_graph.number_of_nodes() > 0:
        degree = dict(coauthorship_graph.degree(weight="weight"))
        # Approximate betweenness for large graphs (same cap as citation graph)
        if coauthorship_graph.number_of_nodes() > 2000:
            betweenness = nx.betweenness_centrality(
                coauthorship_graph, weight="weight", k=500
            )
        else:
            betweenness = nx.betweenness_centrality(coauthorship_graph, weight="weight")
        try:
            eigenvector = nx.eigenvector_centrality(
                coauthorship_graph, weight="weight", max_iter=500
            )
        except (nx.PowerIterationFailedConvergence, nx.NetworkXError):
            eigenvector = {n: 0 for n in coauthorship_graph}
    else:
        degree = betweenness = eigenvector = {}

    # Build author → papers mapping from corpus
    author_papers = defaultdict(list)
    for paper in corpus:
        for author in paper.get("authors", []):
            aid = author.get("id")
            if aid:
                author_papers[aid].append(paper)

    for aid in coauthorship_graph.nodes():
        papers = author_papers.get(aid, [])
        recent_papers = [p for p in papers if (p.get("year") or 0) >= 2022]

        # Sum of paper PageRanks
        total_pagerank = sum(
            paper_metrics.get(p["openalex_id"], {}).get("pagerank", 0)
            for p in papers
        )

        metrics[aid] = {
            "name": coauthorship_graph.nodes[aid].get("name", ""),
            "weighted_degree": degree.get(aid, 0),
            "betweenness": betweenness.get(aid, 0),
            "eigenvector": eigenvector.get(aid, 0),
            "paper_count": len(papers),
            "recent_paper_count": len(recent_papers),
            "total_pagerank": total_pagerank,
        }

    return metrics


def compute_author_metrics_weighted(coauthorship_graph, corpus, paper_metrics,
                                   first_author_weight=2.0, last_author_weight=2.0):
    """
    Compute weighted author metrics where first/last authors get higher contribution credit.

    Args:
        coauthorship_graph: co-authorship network
        corpus: list of papers with author_positions metadata
        paper_metrics: dict of paper metrics by openalex_id
        first_author_weight: multiplier for first authors (default 2.0)
        last_author_weight: multiplier for last authors (default 2.0)

    Returns:
        Dict of author metrics with weighted contributions
    """
    metrics = {}

    print("  Computing weighted co-authorship centrality...")
    if coauthorship_graph.number_of_nodes() > 0:
        degree = dict(coauthorship_graph.degree(weight="weight"))
        if coauthorship_graph.number_of_nodes() > 2000:
            betweenness = nx.betweenness_centrality(
                coauthorship_graph, weight="weight", k=500
            )
        else:
            betweenness = nx.betweenness_centrality(coauthorship_graph, weight="weight")
        try:
            eigenvector = nx.eigenvector_centrality(
                coauthorship_graph, weight="weight", max_iter=500
            )
        except (nx.PowerIterationFailedConvergence, nx.NetworkXError):
            eigenvector = {n: 0 for n in coauthorship_graph}
    else:
        degree = betweenness = eigenvector = {}

    # Build author → papers mapping with position data
    author_papers = defaultdict(list)
    for paper in corpus:
        positions = {ap["id"]: ap["position"] for ap in paper.get("author_positions", [])}
        for author in paper.get("authors", []):
            aid = author.get("id")
            if aid:
                position = positions.get(aid, "middle")
                author_papers[aid].append((paper, position))

    for aid in coauthorship_graph.nodes():
        papers_with_pos = author_papers.get(aid, [])

        # Count papers by position
        first_author_papers = [p for p, pos in papers_with_pos if pos == "first"]
        last_author_papers = [p for p, pos in papers_with_pos if pos == "last"]
        middle_author_papers = [p for p, pos in papers_with_pos if pos == "middle"]
        only_author_papers = [p for p, pos in papers_with_pos if pos == "only"]

        # Recent papers (by position)
        recent_papers_all = [p for p, pos in papers_with_pos if (p.get("year") or 0) >= 2022]

        # Weighted PageRank contribution
        total_pagerank_weighted = 0.0
        for paper, position in papers_with_pos:
            paper_pr = paper_metrics.get(paper["openalex_id"], {}).get("pagerank", 0)
            if position == "first":
                weight = first_author_weight
            elif position == "last":
                weight = last_author_weight
            else:
                weight = 1.0

            # Distribute paper's PageRank by weight
            num_authors = len(paper.get("authors", []))
            if num_authors > 0:
                # Each author gets their weighted share of the paper's PageRank
                total_weight = sum(
                    (first_author_weight if pos == "first" else
                     last_author_weight if pos == "last" else 1.0)
                    for pos in paper.get("author_positions", [{}])
                )
                if total_weight == 0:
                    total_weight = 1.0
                share = (weight / total_weight) * paper_pr
                total_pagerank_weighted += share

        metrics[aid] = {
            "name": coauthorship_graph.nodes[aid].get("name", ""),
            "weighted_degree": degree.get(aid, 0),
            "betweenness": betweenness.get(aid, 0),
            "eigenvector": eigenvector.get(aid, 0),
            "paper_count": len(papers_with_pos),
            "first_author_count": len(first_author_papers),
            "last_author_count": len(last_author_papers),
            "middle_author_count": len(middle_author_papers),
            "only_author_count": len(only_author_papers),
            "recent_paper_count": len(recent_papers_all),
            "total_pagerank_weighted": total_pagerank_weighted,
        }

    return metrics


# ── Community Detection ──────────────────────────────────────────────

def detect_communities(graph, corpus_lookup):
    """
    Run Louvain community detection and label clusters.
    Returns list of community dicts with members, top concepts, top authors.
    """
    if graph.number_of_nodes() == 0:
        return []

    # Convert to undirected for Louvain if needed
    if graph.is_directed():
        G = graph.to_undirected()
    else:
        G = graph

    print("  Running Louvain community detection...")
    communities = nx.community.louvain_communities(G, seed=42)

    results = []
    for i, members in enumerate(communities):
        if len(members) < 3:
            continue

        # Get top concepts for this community
        concept_counts = defaultdict(int)
        author_pageranks = defaultdict(float)
        years = []

        for node_id in members:
            paper = corpus_lookup.get(node_id)
            if paper:
                for c in paper.get("concepts", []):
                    concept_counts[c.get("name", "")] += 1
                years.append(paper.get("year") or 0)
                for a in paper.get("authors", []):
                    author_pageranks[a.get("name", "")] += 1

        top_concepts = sorted(concept_counts.items(), key=lambda x: -x[1])[:5]
        top_authors = sorted(author_pageranks.items(), key=lambda x: -x[1])[:5]

        results.append({
            "community_id": i,
            "size": len(members),
            "members": list(members)[:50],  # cap for readability
            "top_concepts": [{"name": n, "count": c} for n, c in top_concepts],
            "top_authors": [{"name": n, "score": s} for n, s in top_authors],
            "year_range": [min(years) if years else None, max(years) if years else None],
            "label": top_concepts[0][0] if top_concepts else "unlabeled",
        })

    results.sort(key=lambda x: -x["size"])
    print(f"  Found {len(results)} communities (>= 3 members)")
    return results


# ── Ranking ──────────────────────────────────────────────────────────

def rank_papers(corpus, paper_metrics):
    """
    Composite paper ranking: normalized PageRank + betweenness + citations.
    Returns sorted list, both global and per-role.
    """
    results = []
    for paper in corpus:
        pid = paper["openalex_id"]
        gm = paper_metrics.get(pid, {})
        year = paper.get("year") or CURRENT_YEAR
        age = max(1, CURRENT_YEAR - year + 1)
        citations = paper.get("cited_by_count", 0)

        results.append({
            "openalex_id": pid,
            "doi": paper.get("doi", ""),
            "title": paper.get("title", ""),
            "year": year,
            "role": classify_paper_role(paper),
            "authors": [a.get("name", "") for a in paper.get("authors", [])[:5]],
            "total_citations": citations,
            "citations_per_year": round(citations / age, 1),
            **gm,
        })

    # Composite score (simple weighted sum of normalized metrics)
    if results:
        max_pr = max(r.get("pagerank", 0) for r in results) or 1
        max_bt = max(r.get("betweenness", 0) for r in results) or 1
        max_ct = max(r.get("total_citations", 0) for r in results) or 1

        for r in results:
            r["composite_score"] = (
                0.35 * (r.get("pagerank", 0) / max_pr) +
                0.20 * (r.get("betweenness", 0) / max_bt) +
                0.25 * (r.get("total_citations", 0) / max_ct) +
                0.20 * (r.get("recent_pagerank", 0) / max_pr)
            )

    results.sort(key=lambda x: x.get("composite_score", 0), reverse=True)
    return results


def rank_authors(author_metrics):
    """Composite author ranking."""
    results = list(author_metrics.values())

    if results:
        max_pr = max(r.get("total_pagerank", 0) for r in results) or 1
        max_bt = max(r.get("betweenness", 0) for r in results) or 1
        max_deg = max(r.get("weighted_degree", 0) for r in results) or 1

        for r in results:
            r["composite_score"] = (
                0.35 * (r.get("total_pagerank", 0) / max_pr) +
                0.25 * (r.get("betweenness", 0) / max_bt) +
                0.20 * (r.get("weighted_degree", 0) / max_deg) +
                0.20 * (r.get("recent_paper_count", 0) / max(r.get("paper_count", 1), 1))
            )

    results.sort(key=lambda x: x.get("composite_score", 0), reverse=True)
    return results


def rank_authors_weighted(author_metrics, first_weight=2.0, last_weight=2.0):
    """Composite author ranking with position-weighted contributions."""
    results = list(author_metrics.values())

    if results:
        max_pr_w = max(r.get("total_pagerank_weighted", 0) for r in results) or 1
        max_bt = max(r.get("betweenness", 0) for r in results) or 1
        max_deg = max(r.get("weighted_degree", 0) for r in results) or 1

        for r in results:
            # Higher weight for first/last authorship
            first_last_ratio = (
                (r.get("first_author_count", 0) + r.get("last_author_count", 0)) /
                max(r.get("paper_count", 1), 1)
            ) if r.get("paper_count", 0) > 0 else 0

            r["composite_score_weighted"] = (
                0.40 * (r.get("total_pagerank_weighted", 0) / max_pr_w) +  # Higher weight on PageRank
                0.20 * (r.get("betweenness", 0) / max_bt) +
                0.15 * (r.get("weighted_degree", 0) / max_deg) +
                0.15 * (r.get("recent_paper_count", 0) / max(r.get("paper_count", 1), 1)) +
                0.10 * first_last_ratio  # Bonus for being first/last author
            )

    results.sort(key=lambda x: x.get("composite_score_weighted", 0), reverse=True)
    return results


def save_json(data, filename):
    path = OUTPUT_DIR / filename
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  Saved to {path}")


def main():
    print("Loading data...")
    corpus = load_corpus()
    corpus_lookup = {p["openalex_id"]: p for p in corpus}
    citation_graph = load_graph("citation_graph.json")
    coauthorship_graph = load_graph("coauthorship_graph.json")

    print(f"\nCorpus: {len(corpus)} papers")
    print(f"Citation graph: {citation_graph.number_of_nodes()} nodes")
    print(f"Co-authorship graph: {coauthorship_graph.number_of_nodes()} nodes")

    # Tier 0: Citation baseline
    print("\n--- Citation Baseline ---")
    baseline = compute_citation_baseline(corpus)
    save_json(baseline[:200], "citation_baseline.json")
    print(f"  Top 5 by citations:")
    for p in baseline[:5]:
        print(f"    [{p['total_citations']}] {p['title'][:70]}...")

    # Tier 1: Graph metrics
    print("\n--- Paper Graph Metrics ---")
    paper_metrics = compute_paper_graph_metrics(citation_graph)

    print("\n--- Author Metrics ---")
    author_metrics = compute_author_metrics(coauthorship_graph, corpus, paper_metrics)

    # Community detection
    print("\n--- Community Detection ---")
    communities = detect_communities(citation_graph, corpus_lookup)
    save_json(communities, "communities.json")

    # Rankings
    print("\n--- Paper Rankings ---")
    paper_rankings = rank_papers(corpus, paper_metrics)
    save_json(paper_rankings[:2000], "paper_rankings.json")
    print(f"  Top 5 by composite score:")
    for p in paper_rankings[:5]:
        print(f"    [{p['composite_score']:.3f}] {p['title'][:70]}...")

    print("\n--- Author Rankings ---")
    author_rankings = rank_authors(author_metrics)
    save_json(author_rankings[:1000], "author_rankings.json")
    print(f"  Top 5 authors:")
    for a in author_rankings[:5]:
        print(f"    [{a['composite_score']:.3f}] {a['name']} ({a['paper_count']} papers)")

    # Weighted author rankings (position-based)
    print("\n--- Weighted Author Rankings (position-weighted, alpha=2.0) ---")
    author_metrics_weighted = compute_author_metrics_weighted(
        coauthorship_graph, corpus, paper_metrics,
        first_author_weight=2.0, last_author_weight=2.0
    )
    author_rankings_weighted = rank_authors_weighted(author_metrics_weighted, first_weight=2.0, last_weight=2.0)
    save_json(author_rankings_weighted[:1000], "author_rankings_weighted.json")
    print(f"  Top 5 authors (weighted):")
    for a in author_rankings_weighted[:5]:
        print(f"    [{a['composite_score_weighted']:.3f}] {a['name']} "
              f"({a['paper_count']} papers: {a.get('first_author_count', 0)} first, "
              f"{a.get('last_author_count', 0)} last, {a.get('middle_author_count', 0)} middle)")

    # Corpus stats
    print("\n--- Corpus Stats ---")
    role_counts = defaultdict(int)
    year_counts = defaultdict(int)
    for p in corpus:
        role_counts[classify_paper_role(p)] += 1
        year_counts[p.get("year") or 0] += 1

    stats = {
        "total_papers": len(corpus),
        "total_authors": coauthorship_graph.number_of_nodes(),
        "role_distribution": dict(role_counts),
        "year_distribution": dict(sorted(year_counts.items())),
        "communities": len(communities),
    }
    save_json(stats, "corpus_stats.json")

    print("\nDone.")


if __name__ == "__main__":
    main()
