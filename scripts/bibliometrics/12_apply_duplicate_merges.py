#!/usr/bin/env python3
"""
Step 12: Apply duplicate merge decisions.

Reads TSV decisions from `12_dedup_review.py` output and consolidates duplicates.
Transfers citation edges, co-authorship, and metadata to canonical papers.

Usage:
    python 12_apply_duplicate_merges.py

Input:
    output/duplicate_review.tsv  (with 'decision' column filled: ACCEPT/REJECT/NULL)
    output/corpus_deduplicated.json  (or corpus_merged.json if no dedup yet)
    output/graphs/citation_graph.json

Output:
    output/corpus_deduplicated.json
    output/graphs/citation_graph_deduplicated.json
    output/duplicate_merge_log.json
"""
import json
from pathlib import Path
from collections import defaultdict
import networkx as nx
from networkx.readwrite import json_graph

from config import OUTPUT_DIR

# Would be run after user fills in TSV decisions
# For now: skeleton with comments on how to apply merges

def load_tsv_decisions(path):
    """Load merge decisions from TSV. Expects columns:
    paper1_id, paper2_id, confidence, signal_breakdown, decision, notes
    """
    decisions = []
    with open(path) as f:
        lines = f.readlines()

    header = lines[0].strip().split('\t')
    decision_col = header.index('decision') if 'decision' in header else -1

    for line in lines[1:]:
        parts = line.strip().split('\t')
        if decision_col >= 0 and len(parts) > decision_col:
            decision = parts[decision_col].strip()
            if decision == 'ACCEPT':
                decisions.append({
                    'paper1_id': parts[0],
                    'paper2_id': parts[1],
                    'confidence': float(parts[2]) if parts[2] else 0,
                })
    return decisions


def apply_merges(corpus, graph, merge_decisions):
    """
    Apply accepted merge decisions.

    For each merge:
    1. Choose canonical (usually published version over preprint)
    2. Transfer all citations edges to canonical
    3. Consolidate author lists
    4. Sum citation counts
    5. Remove duplicate node from graph
    """
    # Build ID-to-canonical mapping
    canonical_map = {}  # duplicate_id -> canonical_id
    merge_log = {
        'total_merges': len(merge_decisions),
        'papers_removed': 0,
        'citations_consolidated': 0,
        'affected_papers': [],
    }

    for decision in merge_decisions:
        p1_id = decision['paper1_id']
        p2_id = decision['paper2_id']

        # Simple heuristic: if one is bioRxiv/arXiv, other is canonical
        p1_data = next((p for p in corpus if p.get('openalex_id') == p1_id), {})
        p2_data = next((p for p in corpus if p.get('openalex_id') == p2_id), {})

        p1_is_preprint = 'arxiv' in p1_data.get('doi', '').lower() or \
                         'biorxiv' in p1_data.get('journal', '').lower()
        p2_is_preprint = 'arxiv' in p2_data.get('doi', '').lower() or \
                         'biorxiv' in p2_data.get('journal', '').lower()

        if p1_is_preprint and not p2_is_preprint:
            canonical_id, dup_id = p2_id, p1_id
        elif p2_is_preprint and not p1_is_preprint:
            canonical_id, dup_id = p1_id, p2_id
        else:
            # Both preprints or both published: use older year as canonical
            y1 = p1_data.get('year', 9999)
            y2 = p2_data.get('year', 9999)
            canonical_id = p1_id if y1 <= y2 else p2_id
            dup_id = p2_id if y1 <= y2 else p1_id

        canonical_map[dup_id] = canonical_id
        merge_log['affected_papers'].append({
            'canonical_id': canonical_id,
            'duplicate_id': dup_id,
            'reason': 'preprint-published' if (p1_is_preprint or p2_is_preprint) else 'corrupted_record',
        })

    # Update corpus: merge duplicate entries into canonical
    corpus_dedup = []
    seen_ids = set()

    for paper in corpus:
        pid = paper.get('openalex_id')
        canonical = canonical_map.get(pid, pid)

        if canonical in seen_ids:
            # Duplicate of already-added paper; skip
            continue
        seen_ids.add(canonical)

        if canonical != pid:
            # This is a duplicate; consolidate into canonical entry
            canonical_paper = next((p for p in corpus if p.get('openalex_id') == canonical), None)
            if canonical_paper:
                # Merge metadata: prefer non-empty fields from canonical, fall back to dup
                merged = dict(canonical_paper)
                for key in ['abstract', 'concepts']:
                    if not merged.get(key) and paper.get(key):
                        merged[key] = paper[key]
                # Increment citation count
                merged['cited_by_count'] = merged.get('cited_by_count', 0) + paper.get('cited_by_count', 0)
                # Keep original ID as canonical
                corpus_dedup.append(merged)
                merge_log['citations_consolidated'] += paper.get('cited_by_count', 0)
        else:
            # Not a duplicate; include as-is
            corpus_dedup.append(paper)

    merge_log['papers_removed'] = len(corpus) - len(corpus_dedup)

    # Update graph: redirect edges and remove duplicate nodes
    if isinstance(graph, nx.DiGraph):
        # Citation graph
        edges_to_add = []
        nodes_to_remove = []

        for dup_id, canonical_id in canonical_map.items():
            dup_node = next((n for n in graph.nodes(data=True) if n[1].get('id') == dup_id), None)
            canonical_node = next((n for n in graph.nodes(data=True) if n[1].get('id') == canonical_id), None)

            if dup_node and canonical_node:
                dup_key = dup_node[0]
                canonical_key = canonical_node[0]

                # Redirect incoming edges
                for pred in list(graph.predecessors(dup_key)):
                    if pred != canonical_key and graph.has_edge(pred, canonical_key):
                        graph[pred][canonical_key]['weight'] = graph[pred][canonical_key].get('weight', 1) + \
                                                                 graph[pred][dup_key].get('weight', 1)
                    else:
                        edges_to_add.append((pred, canonical_key, graph[pred][dup_key]))

                # Redirect outgoing edges
                for succ in list(graph.successors(dup_key)):
                    if succ != canonical_key and graph.has_edge(canonical_key, succ):
                        graph[canonical_key][succ]['weight'] = graph[canonical_key][succ].get('weight', 1) + \
                                                                 graph[dup_key][succ].get('weight', 1)
                    else:
                        edges_to_add.append((canonical_key, succ, graph[dup_key][succ]))

                nodes_to_remove.append(dup_key)

        # Add consolidated edges and remove duplicate nodes
        for src, tgt, data in edges_to_add:
            if not graph.has_edge(src, tgt):
                graph.add_edge(src, tgt, **data)

        for node in nodes_to_remove:
            graph.remove_node(node)

    return corpus_dedup, graph, merge_log


def main():
    # Check if decisions TSV exists and has been filled in
    decisions_path = OUTPUT_DIR / "duplicate_review.tsv"
    if not decisions_path.exists():
        print("ERROR: Run 12_dedup_review.py first to generate duplicate_review.tsv")
        return

    print("Loading decisions from duplicate_review.tsv...")
    decisions = load_tsv_decisions(decisions_path)
    print(f"  Found {len(decisions)} ACCEPT decisions")

    print("Loading corpus...")
    with open(OUTPUT_DIR / "corpus_merged.json") as f:
        corpus = json.load(f)
    print(f"  {len(corpus)} papers before dedup")

    print("Loading citation graph...")
    with open(OUTPUT_DIR / "graphs" / "citation_graph.json") as f:
        graph_data = json.load(f)
    graph = json_graph.node_link_graph(graph_data, directed=True)
    print(f"  {len(graph)} nodes, {len(graph.edges())} edges before dedup")

    print("\nApplying merge decisions...")
    corpus_dedup, graph_dedup, merge_log = apply_merges(corpus, graph, decisions)

    print(f"\nMerge results:")
    print(f"  Papers removed: {merge_log['papers_removed']}")
    print(f"  Citations consolidated: {merge_log['citations_consolidated']}")
    print(f"  Corpus size: {len(corpus)} → {len(corpus_dedup)}")
    print(f"  Graph size: {len(graph)} → {len(graph_dedup)} nodes")

    # Save deduplicated outputs
    print("\nSaving deduplicated corpus and graph...")
    with open(OUTPUT_DIR / "corpus_deduplicated.json", 'w') as f:
        json.dump(corpus_dedup, f, indent=2)

    graph_data_dedup = json_graph.node_link_data(graph_dedup)
    with open(OUTPUT_DIR / "graphs" / "citation_graph_deduplicated.json", 'w') as f:
        json.dump(graph_data_dedup, f, indent=2)

    with open(OUTPUT_DIR / "duplicate_merge_log.json", 'w') as f:
        json.dump(merge_log, f, indent=2)

    print(f"Saved → output/corpus_deduplicated.json")
    print(f"Saved → output/graphs/citation_graph_deduplicated.json")
    print(f"Saved → output/duplicate_merge_log.json")


if __name__ == "__main__":
    main()
