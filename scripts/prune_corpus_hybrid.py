#!/usr/bin/env python3
"""
Hybrid Corpus Pruning Strategy

Remove:
1. Isolates (no in/out citations)
2. Leaves that BOTH:
   - Cite nothing in the corpus (0 citations TO corpus)
   - Have low total citations (<10)

Keep:
- All papers that cite connectomics work
- High-citation leaves (even if not cited back)
- Core integrated papers
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class HybridCorpusPruner:
    def __init__(self):
        self.pruning_log = {
            'timestamp': datetime.now().isoformat(),
            'removed': defaultdict(list),
            'statistics': {}
        }

    def load_graph(self):
        """Load citation graph."""
        with open('scripts/bibliometrics/output/graphs/citation_graph_deduplicated.json') as f:
            return json.load(f)

    def load_rankings(self):
        """Load paper rankings."""
        with open('scripts/bibliometrics/output/paper_rankings_all.json') as f:
            return json.load(f)

    def build_adjacency(self, graph_data):
        """Build adjacency information with corpus-specific citations."""
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
        cites_in_corpus = defaultdict(int)  # How many corpus papers does this cite?

        all_nodes = {n['id'] for n in graph_data['nodes']}

        for edge in graph_data['edges']:
            source = edge['source']
            target = edge['target']
            out_degree[source] += 1
            in_degree[target] += 1

            # Check if citation is to something in corpus
            if target in all_nodes:
                cites_in_corpus[source] += 1

        return doi_to_node, node_to_doi, in_degree, out_degree, cites_in_corpus, all_nodes

    def prune_hybrid(self, graph_data, rankings):
        """
        Hybrid pruning:
        - Remove isolates (no in/out)
        - Remove leaves that BOTH cite nothing in corpus AND have <10 total citations
        """
        doi_to_node, node_to_doi, in_degree, out_degree, cites_in_corpus, all_nodes = \
            self.build_adjacency(graph_data)
        ranking_map = {p['doi']: p for p in rankings}

        nodes_to_keep = set(all_nodes)

        # Identify isolates
        isolates = []
        for node_id in all_nodes:
            if in_degree[node_id] == 0 and out_degree[node_id] == 0:
                isolates.append(node_id)

        # Identify peripheral leaves
        peripheral_leaves = []
        for node_id in all_nodes:
            in_d = in_degree[node_id]
            cites_in = cites_in_corpus[node_id]
            out_d = out_degree[node_id]

            # Leaf that cites nothing in corpus AND has low total citations
            if in_d == 0 and out_d > 0 and cites_in == 0:
                # Check total citations
                doi = node_to_doi.get(node_id)
                if doi in ranking_map:
                    paper = ranking_map[doi]
                    total_citations = paper.get('total_citations', 0)
                    if total_citations < 10:
                        peripheral_leaves.append(node_id)

        # Remove nodes
        nodes_to_remove = set(isolates) | set(peripheral_leaves)
        nodes_to_keep -= nodes_to_remove

        # Log removals
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

        for node_id in peripheral_leaves:
            doi = node_to_doi.get(node_id)
            if doi in ranking_map:
                paper = ranking_map[doi]
                self.pruning_log['removed']['peripheral_leaves'].append({
                    'doi': doi,
                    'title': paper.get('title'),
                    'citations': paper.get('total_citations'),
                    'year': paper.get('year'),
                    'reason': 'Leaf with 0 citations to corpus and <10 total'
                })

        # Filter graph and rankings
        pruned_nodes = [n for n in graph_data['nodes'] if n['id'] in nodes_to_keep]
        pruned_edges = [e for e in graph_data['edges']
                       if e['source'] in nodes_to_keep and e['target'] in nodes_to_keep]
        pruned_rankings = [p for p in rankings
                          if doi_to_node.get(p.get('doi')) in nodes_to_keep]

        # Statistics
        self.pruning_log['statistics'] = {
            'original_nodes': len(graph_data['nodes']),
            'original_edges': len(graph_data['edges']),
            'original_papers': len(rankings),
            'pruned_nodes': len(pruned_nodes),
            'pruned_edges': len(pruned_edges),
            'pruned_papers': len(pruned_rankings),
            'isolates_removed': len(isolates),
            'peripheral_leaves_removed': len(peripheral_leaves),
            'total_removed': len(isolates) + len(peripheral_leaves)
        }

        return pruned_nodes, pruned_edges, pruned_rankings

    def save_results(self, pruned_nodes, pruned_edges, pruned_rankings):
        """Save pruned corpus."""
        output_dir = Path('scripts/bibliometrics/output')

        # Graph
        pruned_graph = {
            'directed': True,
            'multigraph': False,
            'graph': {},
            'nodes': pruned_nodes,
            'edges': pruned_edges
        }
        with open(output_dir / 'citation_graph_pruned_hybrid.json', 'w') as f:
            json.dump(pruned_graph, f)

        # Rankings
        with open(output_dir / 'paper_rankings_pruned_hybrid.json', 'w') as f:
            json.dump(pruned_rankings, f)

        # Report
        with open(output_dir / 'pruning_report_hybrid.json', 'w') as f:
            json.dump(self.pruning_log, f, indent=2)

        # Markdown report
        with open(output_dir / 'pruning_report_hybrid.md', 'w') as f:
            f.write('# Hybrid Corpus Pruning Report\n\n')
            f.write(f'Generated: {self.pruning_log["timestamp"]}\n\n')

            stats = self.pruning_log['statistics']
            f.write('## Summary\n\n')
            f.write(f'- Original papers: {stats["original_papers"]}\n')
            f.write(f'- Pruned papers: {stats["pruned_papers"]} ({100*stats["pruned_papers"]//stats["original_papers"]}%)\n')
            f.write(f'- Papers removed: {stats["total_removed"]}\n\n')

            f.write(f'- Original nodes: {stats["original_nodes"]}\n')
            f.write(f'- Pruned nodes: {stats["pruned_nodes"]} ({100*stats["pruned_nodes"]//stats["original_nodes"]}%)\n\n')

            f.write(f'- Original edges: {stats["original_edges"]}\n')
            f.write(f'- Pruned edges: {stats["pruned_edges"]} ({100*stats["pruned_edges"]//stats["original_edges"]}%)\n\n')

            f.write('## Removal Criteria\n\n')
            f.write(f'✓ Isolates (no in/out citations): {stats["isolates_removed"]}\n')
            f.write(f'✓ Peripheral leaves (0 citations TO corpus AND <10 total): {stats["peripheral_leaves_removed"]}\n\n')

            f.write('## Removed Papers (sample)\n\n')
            f.write('### Isolates\n\n')
            for paper in self.pruning_log['removed']['isolates'][:5]:
                f.write(f"- {paper['title'][:70]}...\n")
                f.write(f"  {paper['citations']} citations | {paper['year']}\n\n")

            f.write('### Peripheral Leaves\n\n')
            for paper in self.pruning_log['removed']['peripheral_leaves'][:5]:
                f.write(f"- {paper['title'][:70]}...\n")
                f.write(f"  {paper['citations']} citations | {paper['year']}\n\n")

        print(f"Saved: citation_graph_pruned_hybrid.json")
        print(f"Saved: paper_rankings_pruned_hybrid.json")
        print(f"Saved: pruning_report_hybrid.json/.md")

    def run(self):
        """Run hybrid pruning."""
        print("="*80)
        print("HYBRID CORPUS PRUNING")
        print("="*80)

        graph_data = self.load_graph()
        rankings = self.load_rankings()

        print(f"\nLoaded:")
        print(f"  Graph: {len(graph_data['nodes'])} nodes, {len(graph_data['edges'])} edges")
        print(f"  Rankings: {len(rankings)} papers")

        pruned_nodes, pruned_edges, pruned_rankings = self.prune_hybrid(graph_data, rankings)
        self.save_results(pruned_nodes, pruned_edges, pruned_rankings)

        stats = self.pruning_log['statistics']
        print(f"\n" + "="*80)
        print("RESULTS")
        print("="*80)
        print(f"\nPapers: {stats['original_papers']} → {stats['pruned_papers']} ({100*stats['pruned_papers']//stats['original_papers']}%)")
        print(f"Nodes:  {stats['original_nodes']} → {stats['pruned_nodes']} ({100*stats['pruned_nodes']//stats['original_nodes']}%)")
        print(f"Edges:  {stats['original_edges']} → {stats['pruned_edges']} ({100*stats['pruned_edges']//stats['original_edges']}%)")
        print(f"\nRemoved:")
        print(f"  {stats['isolates_removed']:4d} isolates")
        print(f"  {stats['peripheral_leaves_removed']:4d} peripheral leaves (0→corpus, <10 citations)")
        print(f"  {stats['total_removed']:4d} total")

        print(f"\n✅ Kept:")
        print(f"  - All papers that cite connectomics work")
        print(f"  - All well-cited leaves (even if not cited back)")
        print(f"  - All integrated papers (cited AND cite)")

if __name__ == '__main__':
    pruner = HybridCorpusPruner()
    pruner.run()
