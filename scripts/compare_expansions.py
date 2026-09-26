#!/usr/bin/env python3
"""
Quick comparison: Citation neighborhood expansion vs PRIMARY corpus
"""

import json
from pathlib import Path

class ExpansionComparison:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)

    def load_expansion(self):
        """Load citation neighborhood expansion."""
        path = self.output_dir / "helmstaedter_citation_expansion.json"
        with open(path) as f:
            data = json.load(f)

        # Extract DOI set from reference papers
        dois = set()
        for paper in data['reference_papers']:
            doi = paper.get('doi')
            if doi:
                dois.add(doi)

        return dois, data['metadata']['total_expanded']

    def load_primary(self):
        """Load PRIMARY corpus."""
        path = self.output_dir / "corpus_primary_validated.json"
        with open(path) as f:
            data = json.load(f)

        papers = data.get('papers', [])
        dois = set(p.get('doi') for p in papers if p.get('doi'))

        return dois

    def load_citation_graph_dois(self):
        """Get all DOIs in citation graph."""
        path = self.output_dir / "graphs" / "citation_graph_deduplicated.json"
        with open(path) as f:
            data = json.load(f)

        dois = set()
        for node in data['nodes']:
            doi = node.get('doi')
            if doi:
                dois.add(doi)

        return dois

    def run(self):
        """Execute comparison."""
        print("="*80)
        print("EXPANSION COMPARISON")
        print("="*80)

        # Load data
        print("\n[LOADING]")
        expansion_dois, total_expanded = self.load_expansion()
        primary_dois = self.load_primary()
        citation_graph_dois = self.load_citation_graph_dois()

        print(f"  Expansion reference papers: {len(expansion_dois)}")
        print(f"  Expansion total papers: {total_expanded}")
        print(f"  PRIMARY corpus: {len(primary_dois)}")
        print(f"  Citation graph DOIs: {len(citation_graph_dois)}")

        # Analysis
        print("\n[ANALYSIS]")

        # Expansion vs PRIMARY
        overlap = expansion_dois & primary_dois
        only_expansion = expansion_dois - primary_dois
        only_primary = primary_dois - expansion_dois

        print(f"\nExpansion reference papers vs PRIMARY:")
        print(f"  Overlap: {len(overlap)}")
        print(f"  Only in expansion: {len(only_expansion)}")
        print(f"  Only in PRIMARY: {len(only_primary)}")

        # Expansion in citation graph
        expansion_in_graph = expansion_dois & citation_graph_dois
        expansion_not_in_graph = expansion_dois - citation_graph_dois

        print(f"\nExpansion reference papers in citation graph:")
        print(f"  In graph: {len(expansion_in_graph)} ({100*len(expansion_in_graph)/len(expansion_dois):.0f}%)")
        print(f"  NOT in graph: {len(expansion_not_in_graph)} ({100*len(expansion_not_in_graph)/len(expansion_dois):.0f}%)")

        # Key insight
        print(f"\n[KEY INSIGHT]")
        print(f"\nThe 5,802-paper citation expansion is based on {len(expansion_dois)} reference papers.")
        print(f"Of these, only {len(expansion_in_graph)} are in our 7,925-paper citation graph.")
        print(f"\nThis means:")
        print(f"  - {len(expansion_in_graph)} reference papers can be analyzed with k-core")
        print(f"  - {len(expansion_not_in_graph)} reference papers are outside current graph")
        print(f"\nTo properly analyze the 5,802-paper expansion:")
        print(f"  Option A: Rebuild citation graph from 5,802-paper subset")
        print(f"  Option B: Use only the {len(expansion_in_graph)} papers in current graph")

        # Report
        self.generate_report(expansion_dois, primary_dois, expansion_in_graph, expansion_not_in_graph, total_expanded)

    def generate_report(self, expansion_dois, primary_dois, in_graph, not_in_graph, total_expanded):
        """Generate report."""
        report = f"""# Citation Neighborhood vs PRIMARY Corpus

## Overview
- **Citation neighborhood reference papers:** {len(expansion_dois)}
- **Total papers in expansion:** {total_expanded}
- **PRIMARY corpus:** {len(primary_dois)}

## Key Finding
Only {len(in_graph)} of {len(expansion_dois)} reference papers are in our 7,925-paper citation graph.

This creates a fundamental constraint:
- We can compute k-core only on papers in the existing graph
- Most of the 5,802-paper expansion is outside the graph
- Full analysis requires rebuilding the citation graph

## Papers in Graph vs Not in Graph
- In graph: {len(in_graph)} ({100*len(in_graph)/len(expansion_dois):.0f}%)
- NOT in graph: {len(not_in_graph)} ({100*len(not_in_graph)/len(expansion_dois):.0f}%)

## Recommendation
The citation neighborhood expansion strategy is sound, but:

1. **For focused analysis**: Use the {len(in_graph)} papers already in citation graph
   - Can apply k-core filtering immediately
   - Compare to PRIMARY (959)
   - See overlap and gaps

2. **For comprehensive analysis**: Rebuild citation graph from 5,802 papers
   - Takes longer but captures full expansion
   - Can then apply k-core filtering properly
   - More accurate k-core values

Which approach serves your needs better?
"""

        output_file = self.output_dir / "expansion_comparison_report.md"
        with open(output_file, 'w') as f:
            f.write(report)

        print(f"\n✓ Report saved: {output_file}")

if __name__ == '__main__':
    comp = ExpansionComparison()
    comp.run()
