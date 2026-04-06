#!/usr/bin/env python3
"""
Build citation lineage data for ancestry visualization.

Loads papers from one of three sources (in priority order):
1. Pre-built lineage_data.json from connectome-kb (copy directly)
2. corpus_canonical.json from connectome-kb (filter tier=="included", recompute)
3. Legacy corpus_kcore_25.json (backward compatibility)

Output: assets/analysis/lineage_data.json
"""
import json
import shutil
from pathlib import Path
from collections import defaultdict, deque

from config import KB_OUTPUTS_PATH, OUTPUT_DIR, ASSETS_DIR


def load_corpus():
    """
    Load core papers with citation data.

    Returns dict of {openalex_id: paper}, or None if pre-built lineage
    was copied directly from KB (no recompute needed).
    """
    # Tier 1: KB already built lineage_data.json — copy and skip recompute
    kb_lineage = KB_OUTPUTS_PATH / "lineage_data.json"
    if kb_lineage.exists():
        ASSETS_DIR.mkdir(parents=True, exist_ok=True)
        out = ASSETS_DIR / "lineage_data.json"
        shutil.copy(kb_lineage, out)
        print(f"  Copied pre-built lineage from KB: {kb_lineage}")
        return None

    # Tier 2: KB corpus_canonical.json — load and filter by tier
    kb_corpus = KB_OUTPUTS_PATH / "corpus_canonical.json"
    if kb_corpus.exists():
        with open(kb_corpus) as f:
            all_papers = json.load(f)
        papers = [p for p in all_papers if p.get("tier") == "included"]
        print(f"  Loaded {len(papers)} included papers from KB corpus_canonical.json")
        return {p["openalex_id"]: p for p in papers}

    # Tier 3: Legacy fallback
    legacy = OUTPUT_DIR / "corpus_kcore_25.json"
    with open(legacy) as f:
        papers = json.load(f)
    print(f"  Loaded {len(papers)} papers from legacy corpus_kcore_25.json")
    return {p['openalex_id']: p for p in papers}

def build_citation_graph(papers):
    """Build directed citation graph (paper -> papers it cites)."""
    # Map openalex_id to paper index for faster lookup
    id_to_paper = {pid: p for pid, p in papers.items()}

    # Build adjacency lists
    graph = defaultdict(list)  # source -> [targets]
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for paper_id, paper in papers.items():
        for cited_id in paper.get('referenced_works', []):
            # Only include citations within the core corpus
            if cited_id in id_to_paper:
                graph[paper_id].append(cited_id)
                out_degree[paper_id] += 1
                in_degree[cited_id] += 1

    # Set defaults for papers with no edges
    for paper_id in papers:
        if paper_id not in in_degree:
            in_degree[paper_id] = 0
        if paper_id not in out_degree:
            out_degree[paper_id] = 0

    return graph, in_degree, out_degree

def compute_generations(papers, graph, in_degree, out_degree):
    """
    Compute generation/level for each paper based on citation distance.

    Generation = max distance to any leaf node (paper with no outgoing citations).
    - Generation 0: Papers that don't cite anyone in the corpus
    - Generation 1: Papers that cite generation 0 papers
    - etc.
    """
    generations = {}

    # BFS from papers with in_degree=0 (foundational papers)
    # Actually, we want generation based on how deep in citation hierarchy
    # Generation 0 = foundational (high in_degree, low out_degree)
    # Generation N = cites generation N-1 papers

    # Better approach: reverse topological sort
    # Find papers with out_degree=0 (no citations), mark as generation 0
    # Then mark papers that cite them as generation 1, etc.

    queue = deque()
    visited = set()

    # Start with papers that have no outgoing citations (leaves)
    for paper_id, out_deg in out_degree.items():
        if out_deg == 0:
            generations[paper_id] = 0
            queue.append(paper_id)
            visited.add(paper_id)

    # BFS backward through citations
    # For each paper we've processed, mark papers that cite it
    # as generation = current generation + 1
    reverse_graph = defaultdict(list)
    for source, targets in graph.items():
        for target in targets:
            reverse_graph[target].append(source)

    while queue:
        current_id = queue.popleft()
        current_gen = generations[current_id]

        # Find papers that cite this one
        for citing_paper in reverse_graph[current_id]:
            if citing_paper not in visited:
                generations[citing_paper] = current_gen + 1
                queue.append(citing_paper)
                visited.add(citing_paper)

    # Handle any remaining papers (shouldn't happen in connected component)
    for paper_id in papers:
        if paper_id not in generations:
            generations[paper_id] = 0

    return generations

def build_lineage_data(papers, graph, in_degree, out_degree, generations):
    """Build node and link data for D3 visualization."""

    nodes = []
    node_index = {}

    # Sort papers by generation (bottom = foundational, top = recent)
    sorted_papers = sorted(papers.items(),
                          key=lambda x: (generations[x[0]], -x[1]['year']))

    for idx, (paper_id, paper) in enumerate(sorted_papers):
        node_index[paper_id] = idx
        gen = generations[paper_id]

        nodes.append({
            'id': idx,
            'title': paper['title'],
            'year': paper['year'],
            'cited_by_count': paper['cited_by_count'],
            'doi': paper.get('doi'),
            'authors': [a['name'] for a in paper.get('authors', [])[:3]],
            'in_degree': in_degree[paper_id],
            'out_degree': out_degree[paper_id],
            'generation': gen,
            'openalex_id': paper_id,
        })

    # Build links
    links = []
    for source_id, targets in graph.items():
        source_idx = node_index[source_id]
        for target_id in targets:
            target_idx = node_index[target_id]
            links.append({
                'source': source_idx,
                'target': target_idx,
                'strength': in_degree[target_id],  # Importance of cited paper
            })

    return nodes, links, node_index

def main():
    print("Loading corpus...")
    papers = load_corpus()

    # If load_corpus returned None, lineage was already copied from KB
    if papers is None:
        print("Done (used pre-built KB lineage).")
        return

    print(f"  {len(papers)} papers loaded")

    print("Building citation graph...")
    graph, in_degree, out_degree = build_citation_graph(papers)
    total_links = sum(len(v) for v in graph.values())
    print(f"  {total_links} citation links within corpus")

    print("Computing generations...")
    generations = compute_generations(papers, graph, in_degree, out_degree)
    gen_counts = defaultdict(int)
    for gen in generations.values():
        gen_counts[gen] += 1
    print(f"  Generation distribution: {dict(sorted(gen_counts.items()))}")

    print("Building visualization data...")
    nodes, links, node_index = build_lineage_data(papers, graph, in_degree, out_degree, generations)

    data = {
        'nodes': nodes,
        'links': links,
        'metadata': {
            'total_papers': len(nodes),
            'total_citations': len(links),
            'generation_count': max(generations.values()) + 1 if generations else 0,
            'year_range': [
                min(p['year'] for p in papers.values()),
                max(p['year'] for p in papers.values()),
            ],
        }
    }

    # Save to assets directory for use in visualization
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = ASSETS_DIR / "lineage_data.json"
    print(f"\nSaving to {output_path}...")
    with open(output_path, 'w') as f:
        json.dump(data, f)
    print(f"  {len(nodes)} nodes, {len(links)} links")
    print(f"  File size: {output_path.stat().st_size / 1024 / 1024:.1f} MB")

if __name__ == '__main__':
    main()
