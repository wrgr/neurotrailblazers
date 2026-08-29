#!/usr/bin/env python3
"""
Apply k-core filtering (k≥25 + in-degree≥2) to Helmstaedter citation expansion.

Input: 5,802-paper expanded set from Helmstaedter reference citations
Output: Filtered corpus with k≥25 + in-degree≥2
Compare: vs PRIMARY corpus (959 papers)
"""

import json
import networkx as nx
from pathlib import Path
from collections import defaultdict

class HelmstaedterKcoreFilter:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)

    def load_citation_graph(self):
        """Load the full citation graph."""
        print("\n[LOADING] Citation graph...")

        path = self.output_dir / "graphs" / "citation_graph_deduplicated.json"
        with open(path) as f:
            data = json.load(f)

        print(f"  Graph: {len(data['nodes'])} nodes, {len(data['edges'])} edges")

        # Build DOI -> ID mapping
        doi_to_id = {}
        for node in data['nodes']:
            doi = node.get('doi')
            node_id = node.get('id')
            if doi and node_id:
                doi_to_id[doi] = node_id

        print(f"  DOI mapping: {len(doi_to_id)} papers with DOI")

        return data, doi_to_id

    def load_expanded_set(self):
        """Load the 5,802-paper expanded set."""
        print("[LOADING] Helmstaedter expanded set...")

        path = self.output_dir / "helmstaedter_citation_expansion.json"
        with open(path) as f:
            data = json.load(f)

        return data

    def build_subgraph(self, graph_data, expanded_dois, doi_to_id):
        """Build a citation subgraph with only papers in expanded set."""
        print(f"\n[BUILDING] Citation subgraph for {len(expanded_dois)} papers...")

        # Convert DOIs to OpenAlex IDs
        expanded_ids = set()
        for doi in expanded_dois:
            if doi in doi_to_id:
                expanded_ids.add(doi_to_id[doi])

        print(f"  Mapped {len(expanded_ids)}/{len(expanded_dois)} DOIs to OpenAlex IDs")

        # Create directed graph
        G = nx.DiGraph()

        # Add nodes
        for node_id in expanded_ids:
            G.add_node(node_id)

        # Add edges (only if both source and target are in expanded set)
        edges_count = 0
        for edge in graph_data['edges']:
            source = edge['source']
            target = edge['target']

            if source in expanded_ids and target in expanded_ids:
                G.add_edge(source, target)
                edges_count += 1

        print(f"✓ Subgraph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
        return G, expanded_ids

    def compute_kcore(self, G):
        """Compute k-core on the graph."""
        print("\n[COMPUTING] K-core decomposition...")

        # Convert to undirected for k-core
        G_undirected = G.to_undirected()

        # Remove self-loops
        G_undirected.remove_edges_from(nx.selfloop_edges(G_undirected))

        # Compute k-core
        kcore = nx.core_number(G_undirected)

        print(f"✓ K-core computed: {len(kcore)} papers")

        # Distribution
        from collections import Counter
        kcore_dist = Counter(kcore.values())

        print("\nK-core distribution:")
        for k in sorted(kcore_dist.keys(), reverse=True)[:15]:
            print(f"  k={k}: {kcore_dist[k]} papers")

        return kcore

    def apply_filters(self, G, kcore, k_threshold=25, indegree_threshold=2):
        """Apply k≥25 + in-degree≥2 filtering."""
        print(f"\n[FILTERING] Applying k≥{k_threshold} + in-degree≥{indegree_threshold}...")

        filtered = []

        for doi, k_value in kcore.items():
            if k_value >= k_threshold:
                # Check in-degree requirement
                in_degree = G.in_degree(doi)

                if in_degree >= indegree_threshold:
                    filtered.append(doi)

        print(f"✓ Filtered: {len(filtered)} papers")
        print(f"  Percentage of subgraph: {100*len(filtered)/G.number_of_nodes():.1f}%")

        return filtered

    def load_primary_corpus(self):
        """Load PRIMARY corpus for comparison."""
        print("\n[LOADING] PRIMARY corpus...")

        path = self.output_dir / "corpus_primary_validated.json"
        with open(path) as f:
            data = json.load(f)

        papers = data.get('papers', [])
        dois = set(p.get('doi') for p in papers if p.get('doi'))

        print(f"  PRIMARY: {len(dois)} papers")
        return dois

    def compare(self, helmstaedter_filtered, primary_dois):
        """Compare the two corpora."""
        print("\n[COMPARING] Helmstaedter vs PRIMARY...\n")

        helmstaedter_set = set(helmstaedter_filtered)

        # Set operations
        overlap = helmstaedter_set & primary_dois
        only_helmstaedter = helmstaedter_set - primary_dois
        only_primary = primary_dois - helmstaedter_set

        print(f"Helmstaedter (k≥25 + in-deg≥2): {len(helmstaedter_set)}")
        print(f"PRIMARY (k≥25 + in-deg≥2):      {len(primary_dois)}")
        print(f"\nOverlap:          {len(overlap)} ({100*len(overlap)/len(primary_dois):.1f}% of PRIMARY)")
        print(f"Only Helmstaedter: {len(only_helmstaedter)} (new papers)")
        print(f"Only PRIMARY:      {len(only_primary)} (missed by expansion)")

        return {
            'helmstaedter_dois': helmstaedter_set,
            'overlap': overlap,
            'only_helmstaedter': only_helmstaedter,
            'only_primary': only_primary
        }

    def save_results(self, helmstaedter_dois, comparison, kcore):
        """Save results."""
        # Save filtered corpus
        output_file = self.output_dir / "corpus_helmstaedter_citation.json"
        with open(output_file, 'w') as f:
            json.dump({
                'metadata': {
                    'strategy': 'Citation neighborhood expansion + k≥25 + in-degree≥2',
                    'source_papers': 5802,
                    'filtered_papers': len(helmstaedter_dois),
                    'kcore_threshold': 25,
                    'indegree_threshold': 2,
                    'generated': '2026-04-01'
                },
                'papers': [{'doi': doi, 'k_core': kcore.get(doi, 0)} for doi in helmstaedter_dois]
            }, f, indent=2)

        print(f"\n✓ Saved: {output_file}")

        # Save comparison
        report_file = self.output_dir / "helmstaedter_vs_primary_report.md"
        with open(report_file, 'w') as f:
            f.write("# Helmstaedter Citation Expansion vs PRIMARY Corpus\n\n")
            f.write("## Strategy\n")
            f.write("1. Start with 30 papers cited in Helmstaedter 2026 review\n")
            f.write("2. Expand: +3,913 papers citing references + 1,987 papers cited by references\n")
            f.write("3. Total: 5,802 papers in citation neighborhood\n")
            f.write("4. Filter: k≥25 + in-degree≥2\n\n")

            f.write("## Results\n")
            f.write(f"- **Helmstaedter corpus:** {len(comparison['helmstaedter_dois'])} papers\n")
            f.write(f"- **PRIMARY corpus:** {len(comparison['overlap']) + len(comparison['only_primary'])} papers\n")
            f.write(f"- **Overlap:** {len(comparison['overlap'])} papers\n")
            f.write(f"- **New papers found by expansion:** {len(comparison['only_helmstaedter'])}\n")
            f.write(f"- **Papers PRIMARY has that expansion missed:** {len(comparison['only_primary'])}\n")

        print(f"✓ Saved: {report_file}")

    def run(self):
        """Execute."""
        print("="*80)
        print("HELMSTAEDTER CITATION EXPANSION K-CORE FILTERING")
        print("="*80)

        # Load data
        graph_data, doi_to_id = self.load_citation_graph()
        expanded_data = self.load_expanded_set()

        # Extract DOIs from expanded set
        expanded_dois = set()
        for paper in expanded_data['reference_papers']:
            doi = paper.get('doi')
            if doi:
                expanded_dois.add(doi)

        # Build subgraph
        G, expanded_ids = self.build_subgraph(graph_data, expanded_dois, doi_to_id)

        # Compute k-core
        kcore = self.compute_kcore(G)

        # Apply filters
        helmstaedter_filtered = self.apply_filters(G, kcore)

        # Load PRIMARY for comparison
        primary_dois = self.load_primary_corpus()

        # Compare
        comparison = self.compare(helmstaedter_filtered, primary_dois)

        # Save
        self.save_results(set(helmstaedter_filtered), comparison, kcore)

        return comparison

if __name__ == '__main__':
    processor = HelmstaedterKcoreFilter()
    comparison = processor.run()

    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
