#!/usr/bin/env python3
"""
Corpus Pruning Pipeline

After deduplication, merging, and graph construction:
1. Remove isolated nodes (no citations in/out)
2. Remove leaf nodes with no inbound citations (not cited by corpus)
3. Keep papers connected to the corpus core
4. Document what was removed and why

Input: citation_graph_deduplicated.json, paper_rankings_all.json
Output: cleaned corpus with pruning report
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class CorpusPruner:
    def __init__(self):
        self.pruning_log = {
            'timestamp': datetime.now().isoformat(),
            'removed': defaultdict(list),
            'statistics': {}
        }

    def load_graph(self):
        """Load citation graph."""
        with open('scripts/bibliometrics/output/graphs/citation_graph_deduplicated.json') as f:
            graph_data = json.load(f)
        return graph_data

    def load_rankings(self):
        """Load paper rankings."""
        with open('scripts/bibliometrics/output/paper_rankings_all.json') as f:
            return json.load(f)

    def build_adjacency(self, graph_data):
        """Build adjacency information."""
        doi_to_node = {}
        node_to_doi = {}
        for node in graph_data['nodes']:
            node_id = node['id']
            doi = node.get('doi')
            if doi:
                doi_to_node[doi] = node_id
                node_to_doi[node_id] = doi

        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for edge in graph_data['edges']:
            source = edge['source']
            target = edge['target']
            out_degree[source] += 1
            in_degree[target] += 1

        return doi_to_node, node_to_doi, in_degree, out_degree

    def identify_isolates(self, graph_data, in_degree, out_degree):
        """Identify papers with no citations (in or out)."""
        all_nodes = {n['id'] for n in graph_data['nodes']}
        isolates = []

        for node_id in all_nodes:
            if in_degree[node_id] == 0 and out_degree[node_id] == 0:
                isolates.append(node_id)

        return isolates

    def identify_unconnected_leaves(self, graph_data, in_degree, out_degree):
        """Identify leaf nodes NOT cited by any other paper in corpus.

        These are papers that may cite work but are not cited by anything.
        Useful for identifying newer/peripheral papers.
        """
        all_nodes = {n['id'] for n in graph_data['nodes']}
        leaves = []

        for node_id in all_nodes:
            if in_degree[node_id] == 0 and out_degree[node_id] > 0:
                leaves.append(node_id)

        return leaves

    def prune(self, graph_data, rankings, prune_isolates=True, prune_leaves=False):
        """
        Prune corpus.

        Args:
            prune_isolates: Remove papers with no citations (in or out)
            prune_leaves: Remove papers with no inbound citations
        """
        doi_to_node, node_to_doi, in_degree, out_degree = self.build_adjacency(graph_data)
        ranking_map = {p['doi']: p for p in rankings}

        all_nodes = {n['id'] for n in graph_data['nodes']}
        nodes_to_keep = set(all_nodes)

        # Identify nodes to remove
        isolates = self.identify_isolates(graph_data, in_degree, out_degree)
        leaves = self.identify_unconnected_leaves(graph_data, in_degree, out_degree)

        if prune_isolates:
            nodes_to_keep -= set(isolates)
            for node_id in isolates:
                doi = node_to_doi.get(node_id)
                if doi in ranking_map:
                    paper = ranking_map[doi]
                    self.pruning_log['removed']['isolates'].append({
                        'doi': doi,
                        'title': paper.get('title'),
                        'citations': paper.get('total_citations'),
                        'year': paper.get('year')
                    })

        if prune_leaves:
            nodes_to_keep -= set(leaves)
            for node_id in leaves:
                doi = node_to_doi.get(node_id)
                if doi in ranking_map:
                    paper = ranking_map[doi]
                    self.pruning_log['removed']['unconnected_leaves'].append({
                        'doi': doi,
                        'title': paper.get('title'),
                        'citations': paper.get('total_citations'),
                        'year': paper.get('year')
                    })

        # Filter graph
        pruned_nodes = [n for n in graph_data['nodes'] if n['id'] in nodes_to_keep]
        pruned_edges = [e for e in graph_data['edges']
                       if e['source'] in nodes_to_keep and e['target'] in nodes_to_keep]

        # Prune rankings
        pruned_rankings = [p for p in rankings if doi_to_node.get(p.get('doi')) in nodes_to_keep]

        # Log statistics
        self.pruning_log['statistics'] = {
            'original_nodes': len(graph_data['nodes']),
            'original_edges': len(graph_data['edges']),
            'original_papers': len(rankings),
            'pruned_nodes': len(pruned_nodes),
            'pruned_edges': len(pruned_edges),
            'pruned_papers': len(pruned_rankings),
            'isolates_removed': len(isolates) if prune_isolates else 0,
            'leaves_removed': len(leaves) if prune_leaves else 0,
            'total_removed': len(isolates) + (len(leaves) if prune_leaves else 0)
        }

        return pruned_nodes, pruned_edges, pruned_rankings

    def save_pruned_corpus(self, pruned_nodes, pruned_edges, pruned_rankings,
                          prune_isolates=True, prune_leaves=False):
        """Save pruned corpus."""
        output_dir = Path('scripts/bibliometrics/output')

        # Save graph
        pruned_graph = {
            'directed': True,
            'multigraph': False,
            'graph': {},
            'nodes': pruned_nodes,
            'edges': pruned_edges
        }

        graph_file = output_dir / 'citation_graph_pruned.json'
        with open(graph_file, 'w') as f:
            json.dump(pruned_graph, f)
        print(f"Saved pruned graph: {graph_file}")

        # Save rankings
        rankings_file = output_dir / 'paper_rankings_pruned.json'
        with open(rankings_file, 'w') as f:
            json.dump(pruned_rankings, f)
        print(f"Saved pruned rankings: {rankings_file}")

        # Save pruning log
        log_file = output_dir / 'pruning_report.json'
        with open(log_file, 'w') as f:
            json.dump(self.pruning_log, f, indent=2)
        print(f"Saved pruning report: {log_file}")

        # Save human-readable report
        report_file = output_dir / 'pruning_report.md'
        with open(report_file, 'w') as f:
            f.write('# Corpus Pruning Report\n\n')
            f.write(f'Generated: {self.pruning_log["timestamp"]}\n\n')

            stats = self.pruning_log['statistics']
            f.write('## Summary\n\n')
            f.write(f'- Original nodes: {stats["original_nodes"]}\n')
            f.write(f'- Pruned nodes: {stats["pruned_nodes"]} ({100*stats["pruned_nodes"]//stats["original_nodes"]}%)\n')
            f.write(f'- Nodes removed: {stats["total_removed"]}\n\n')

            f.write(f'- Original edges: {stats["original_edges"]}\n')
            f.write(f'- Pruned edges: {stats["pruned_edges"]} ({100*stats["pruned_edges"]//stats["original_edges"]}%)\n\n')

            f.write(f'- Original papers: {stats["original_papers"]}\n')
            f.write(f'- Pruned papers: {stats["pruned_papers"]} ({100*stats["pruned_papers"]//stats["original_papers"]}%)\n\n')

            f.write('## Removal Criteria\n\n')
            if prune_isolates:
                f.write(f'✓ Isolated nodes (no in/out citations): {stats["isolates_removed"]} papers\n')
            if prune_leaves:
                f.write(f'✓ Unconnected leaves (no inbound citations): {stats["leaves_removed"]} papers\n')

            if self.pruning_log['removed'].get('isolates'):
                f.write('\n## Removed Isolates (sample)\n\n')
                for paper in self.pruning_log['removed']['isolates'][:10]:
                    f.write(f"- {paper['title'][:70]}...\n")
                    f.write(f"  {paper['citations']} citations | {paper['year']}\n\n")

            if self.pruning_log['removed'].get('unconnected_leaves'):
                f.write('\n## Removed Leaves (sample)\n\n')
                for paper in self.pruning_log['removed']['unconnected_leaves'][:10]:
                    f.write(f"- {paper['title'][:70]}...\n")
                    f.write(f"  {paper['citations']} citations | {paper['year']}\n\n")

        print(f"Saved pruning report: {report_file}")

    def run(self, prune_isolates=True, prune_leaves=False):
        """Run the pruning pipeline."""
        print("="*80)
        print("CORPUS PRUNING PIPELINE")
        print("="*80)

        graph_data = self.load_graph()
        rankings = self.load_rankings()

        print(f"\nLoaded:")
        print(f"  Graph: {len(graph_data['nodes'])} nodes, {len(graph_data['edges'])} edges")
        print(f"  Rankings: {len(rankings)} papers")

        pruned_nodes, pruned_edges, pruned_rankings = self.prune(
            graph_data, rankings,
            prune_isolates=prune_isolates,
            prune_leaves=prune_leaves
        )

        self.save_pruned_corpus(pruned_nodes, pruned_edges, pruned_rankings,
                               prune_isolates=prune_isolates,
                               prune_leaves=prune_leaves)

        stats = self.pruning_log['statistics']
        print(f"\n" + "="*80)
        print("RESULTS")
        print("="*80)
        print(f"\nGraph:")
        print(f"  {stats['original_nodes']:5d} nodes → {stats['pruned_nodes']:5d} nodes ({100*stats['pruned_nodes']//stats['original_nodes']}%)")
        print(f"  {stats['original_edges']:5d} edges → {stats['pruned_edges']:5d} edges ({100*stats['pruned_edges']//stats['original_edges']}%)")
        print(f"\nPapers:")
        print(f"  {stats['original_papers']:5d} papers → {stats['pruned_papers']:5d} papers ({100*stats['pruned_papers']//stats['original_papers']}%)")
        print(f"\nRemoved:")
        if stats['isolates_removed'] > 0:
            print(f"  {stats['isolates_removed']:5d} isolates (no in/out citations)")
        if stats['leaves_removed'] > 0:
            print(f"  {stats['leaves_removed']:5d} leaves (no inbound citations)")

if __name__ == '__main__':
    pruner = CorpusPruner()

    # Run with both filters
    pruner.run(prune_isolates=True, prune_leaves=False)
