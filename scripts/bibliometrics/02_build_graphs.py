#!/usr/bin/env python3
"""
Step 2: Build multi-layer graphs from the merged corpus.

Constructs four graphs:
  1. Citation graph (directed)
  2. Co-citation graph (undirected, weighted)
  3. Bibliographic coupling graph (undirected, weighted)
  4. Co-authorship graph (undirected, weighted)

Input:  output/corpus_merged.json
Output: output/graphs/{citation,cocitation,coupling,coauthorship}_graph.json

Usage:
  python 02_build_graphs.py
"""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

import networkx as nx
from networkx.readwrite import json_graph

from config import OUTPUT_DIR, MIN_COCITATION_WEIGHT, MIN_COUPLING_WEIGHT


def load_corpus():
    """Load merged corpus from output/corpus_merged.json."""
    path = OUTPUT_DIR / "corpus_merged.json"
    with open(path) as f:
        return json.load(f)


def build_citation_graph(corpus):
    """
    Build directed citation graph.
    Nodes: papers (by openalex_id). Edges: A→B if A cites B.
    Only includes edges where both endpoints are in the corpus.
    """
    corpus_ids = {p["openalex_id"] for p in corpus}
    G = nx.DiGraph()

    for paper in corpus:
        pid = paper["openalex_id"]
        G.add_node(pid, **{
            "title": paper.get("title", ""),
            "year": paper.get("year"),
            "cited_by_count": paper.get("cited_by_count", 0),
            "doi": paper.get("doi", ""),
            "journal": paper.get("journal", ""),
            "type": paper.get("type", ""),
        })

    for paper in corpus:
        pid = paper["openalex_id"]
        for ref_id in paper.get("referenced_works", []):
            if ref_id in corpus_ids:
                G.add_edge(pid, ref_id)

    print(f"  Citation graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G


def build_cocitation_graph(corpus, citation_graph):
    """
    Build undirected co-citation graph.
    Edge weight(A,B) = number of corpus papers that cite both A and B.
    Only creates edges where weight >= MIN_COCITATION_WEIGHT.
    """
    # For each paper, get what it cites (successors in citation graph)
    cocite_counts = Counter()
    for paper_id in citation_graph.nodes():
        refs = list(citation_graph.successors(paper_id))
        for a, b in combinations(sorted(refs), 2):
            cocite_counts[(a, b)] += 1

    G = nx.Graph()
    for (a, b), weight in cocite_counts.items():
        if weight >= MIN_COCITATION_WEIGHT:
            G.add_edge(a, b, weight=weight)

    # Copy node attributes from citation graph
    for node in G.nodes():
        if node in citation_graph.nodes:
            G.nodes[node].update(citation_graph.nodes[node])

    print(f"  Co-citation graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G


def build_coupling_graph(corpus):
    """
    Build bibliographic coupling graph.
    Edge weight(A,B) = number of shared references between A and B.
    Only creates edges where weight >= MIN_COUPLING_WEIGHT.
    """
    # Build reference sets
    ref_sets = {}
    for paper in corpus:
        pid = paper["openalex_id"]
        refs = set(paper.get("referenced_works", []))
        if refs:
            ref_sets[pid] = refs

    G = nx.Graph()
    paper_ids = list(ref_sets.keys())
    for i in range(len(paper_ids)):
        for j in range(i + 1, len(paper_ids)):
            a, b = paper_ids[i], paper_ids[j]
            shared = len(ref_sets[a] & ref_sets[b])
            if shared >= MIN_COUPLING_WEIGHT:
                G.add_edge(a, b, weight=shared)

    print(f"  Coupling graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G


def build_coauthorship_graph(corpus):
    """
    Build undirected co-authorship graph.
    Nodes: authors (by OpenAlex author ID). Edge weight = co-authored papers.
    """
    G = nx.Graph()
    for paper in corpus:
        author_ids = [
            a["id"] for a in paper.get("authors", [])
            if a.get("id")
        ]
        # Add nodes with name attribute
        for a in paper.get("authors", []):
            aid = a.get("id")
            if aid:
                if aid not in G:
                    G.add_node(aid, name=a.get("name", ""), papers=[])
                G.nodes[aid]["papers"].append(paper.get("openalex_id", ""))

        # Add edges for all author pairs
        for a1, a2 in combinations(author_ids, 2):
            if G.has_edge(a1, a2):
                G[a1][a2]["weight"] += 1
            else:
                G.add_edge(a1, a2, weight=1)

    print(f"  Co-authorship graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G


def save_graph(graph, filename):
    """Save graph in D3 node-link JSON format."""
    graphs_dir = OUTPUT_DIR / "graphs"
    graphs_dir.mkdir(parents=True, exist_ok=True)
    path = graphs_dir / filename

    # Manual conversion to ensure edges are included (node_link_data has bugs)
    nodes_list = []
    for node_id, attrs in graph.nodes(data=True):
        node = {"id": node_id}
        node.update(attrs)
        nodes_list.append(node)

    links_list = []
    for source, target, attrs in graph.edges(data=True):
        link = {"source": source, "target": target}
        link.update(attrs)
        links_list.append(link)

    data = {
        "directed": graph.is_directed(),
        "multigraph": graph.is_multigraph(),
        "nodes": nodes_list,
        "links": links_list
    }

    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  Saved to {path}")


def main():
    print("Loading corpus...")
    corpus = load_corpus()
    print(f"  {len(corpus)} papers")

    print("\nBuilding citation graph...")
    cg = build_citation_graph(corpus)
    save_graph(cg, "citation_graph.json")

    print("\nBuilding co-citation graph...")
    cocg = build_cocitation_graph(corpus, cg)
    save_graph(cocg, "cocitation_graph.json")

    print("\nBuilding bibliographic coupling graph...")
    # Note: coupling graph is O(n^2) — may be slow for large corpora.
    # For >3000 papers, consider sampling or approximate methods.
    if len(corpus) > 3000:
        print("  WARNING: >3000 papers, coupling graph may be slow. Consider sampling.")
    cpg = build_coupling_graph(corpus)
    save_graph(cpg, "coupling_graph.json")

    print("\nBuilding co-authorship graph...")
    cag = build_coauthorship_graph(corpus)
    save_graph(cag, "coauthorship_graph.json")

    print("\nDone.")


if __name__ == "__main__":
    main()
