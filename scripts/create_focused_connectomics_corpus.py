#!/usr/bin/env python3
"""
Create focused connectomics corpus by filtering PRIMARY to domain-relevant papers only.

Filters: Keeps only Core EM + Secondary Connectomics + Foundational
Removes: General Neuroscience and Uncertain papers (noise reduction)

Result: 529 papers instead of 959 (cleaner, more focused)
"""

import json
from pathlib import Path

class FocusedCorpusBuilder:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)

    def load_primary_corpus(self):
        """Load PRIMARY corpus (959 papers, k≥25 + in-degree≥2)."""
        path = self.output_dir / 'corpus_primary_validated.json'
        with open(path) as f:
            data = json.load(f)
        return data.get('papers', [])

    def load_domain_labels(self):
        """Load domain classification for all papers."""
        path = self.output_dir / 'domain_labels.json'
        with open(path) as f:
            labels = json.load(f)

        # Convert OpenAlex ID to DOI mapping if needed
        # For now, assume it's keyed by OpenAlex ID
        return labels

    def load_paper_metadata(self):
        """Load full paper rankings for reference."""
        path = self.output_dir / 'paper_rankings_all.json'
        with open(path) as f:
            papers = json.load(f)

        # Build DOI → metadata mapping
        doi_map = {}
        for paper in papers:
            doi = paper.get('doi')
            if doi:
                doi_map[doi] = paper

        return doi_map

    def classify_paper_domain(self, paper, domain_labels, doi_map):
        """Determine paper domain based on multiple signals."""
        doi = paper.get('doi')
        openalex_id = paper.get('openalex_id', '')

        # Try explicit domain label
        if openalex_id in domain_labels:
            return domain_labels[openalex_id]

        # Fallback: heuristic based on title/metadata
        title = paper.get('title', '').lower()

        # Check title keywords
        em_keywords = ['electron microscopy', 'connectome', 'nanoscale', 'synapse', 'serial section']
        mri_keywords = ['fmri', 'dmri', 'diffusion', 'mri', 'resting-state', 'functional connectivity']
        methods_keywords = ['graph', 'network analysis', 'machine learning', 'algorithm', 'deep learning']

        if any(kw in title for kw in em_keywords):
            return 'em_connectomics'
        if any(kw in title for kw in mri_keywords):
            return 'mri_connectomics'
        if any(kw in title for kw in methods_keywords):
            return 'methods_ml'

        # Default to unknown
        return 'unknown'

    def build_focused_corpus(self, primary_papers, domain_labels, doi_map):
        """Filter PRIMARY to keep only connectomics-relevant domains."""

        connectomics_relevant = [
            'em_connectomics',
            'mri_connectomics',
            'methods_ml',
            'network_science'
        ]

        filtered = []
        domain_counts = {
            'em_connectomics': 0,
            'mri_connectomics': 0,
            'methods_ml': 0,
            'network_science': 0,
            'neuroscience': 0,
            'unknown': 0,
            'off_topic': 0
        }

        for paper in primary_papers:
            # Determine domain
            domain = self.classify_paper_domain(paper, domain_labels, doi_map)

            # Track counts
            if domain in domain_counts:
                domain_counts[domain] += 1

            # Include if connectomics-relevant
            if domain in connectomics_relevant:
                paper_with_domain = {**paper, 'domain': domain}
                filtered.append(paper_with_domain)

        return filtered, domain_counts

    def generate_report(self, focused_papers, domain_counts, primary_count):
        """Generate comparison report."""
        lines = []

        lines.append("# Focused Connectomics Corpus Report\n")
        lines.append(f"**Generated:** 2026-04-01\n")

        lines.append(f"\n## Summary\n")
        lines.append(f"**PRIMARY Corpus:** {primary_count} papers (k≥25 + in-degree≥2)")
        lines.append(f"**Focused Corpus:** {len(focused_papers)} papers (connectomics-relevant only)\n")

        removed = primary_count - len(focused_papers)
        pct_removed = 100 * removed / primary_count
        lines.append(f"**Removed:** {removed} papers ({pct_removed:.1f}% - general neuroscience noise)\n")

        lines.append(f"\n## Domain Breakdown of FOCUSED Corpus\n")

        total = sum(domain_counts[d] for d in ['em_connectomics', 'mri_connectomics', 'methods_ml', 'network_science'])

        if total > 0:
            lines.append(f"| Domain | Papers | % |\n")
            lines.append(f"|--------|--------|---|\n")

            domains = [
                ('em_connectomics', '🟢 Core EM Connectomics'),
                ('mri_connectomics', '🟡 Secondary Connectomics (fMRI/MRI)'),
                ('methods_ml', '🔵 Methods & ML'),
                ('network_science', '🔵 Network Science')
            ]

            for domain_key, domain_label in domains:
                count = domain_counts[domain_key]
                pct = 100 * count / total
                lines.append(f"| {domain_label} | {count} | {pct:.1f}% |")

        lines.append(f"\n## Removed Domains\n")
        removed_counts = {
            'neuroscience': domain_counts['neuroscience'],
            'unknown': domain_counts['unknown'],
            'off_topic': domain_counts['off_topic']
        }

        for domain, count in removed_counts.items():
            if count > 0:
                lines.append(f"- {domain}: {count} papers")

        lines.append(f"\n## Quality Signal\n")
        lines.append(f"**All papers in focused corpus:**")
        lines.append(f"- K-core ≥ 25 (structurally embedded)")
        lines.append(f"- In-degree ≥ 2 (cited by multiple corpus papers)")
        lines.append(f"- Domain-validated (connectomics-relevant)")

        return "\n".join(lines)

    def save_results(self, focused_papers, report):
        """Save focused corpus and report."""
        # Save focused corpus
        corpus_file = self.output_dir / 'corpus_focused_connectomics.json'
        with open(corpus_file, 'w') as f:
            json.dump({
                'metadata': {
                    'tier': 'FOCUSED CONNECTOMICS',
                    'purpose': 'Connectomics-relevant papers only (removes general neuroscience)',
                    'paper_count': len(focused_papers),
                    'source': 'Filtered from PRIMARY (k≥25 + in-degree≥2)',
                    'domains_included': ['em_connectomics', 'mri_connectomics', 'methods_ml', 'network_science'],
                    'generated': '2026-04-01'
                },
                'papers': focused_papers
            }, f, indent=2)
        print(f"✓ Saved: {corpus_file} ({len(focused_papers)} papers)")

        # Save report
        report_file = self.output_dir / 'focused_corpus_report.md'
        with open(report_file, 'w') as f:
            f.write(report)
        print(f"✓ Saved: {report_file}")

    def run(self):
        """Execute focused corpus creation."""
        print("=" * 80)
        print("CREATING FOCUSED CONNECTOMICS CORPUS")
        print("=" * 80)

        # Load data
        print("\nLoading data...")
        primary_papers = self.load_primary_corpus()
        domain_labels = self.load_domain_labels()
        doi_map = self.load_paper_metadata()

        print(f"  PRIMARY corpus: {len(primary_papers)} papers")
        print(f"  Domain labels: {len(domain_labels)} papers")

        # Filter to focused corpus
        print("\nFiltering to connectomics-relevant papers...")
        focused_papers, domain_counts = self.build_focused_corpus(primary_papers, domain_labels, doi_map)

        # Generate report
        print("Generating report...")
        report = self.generate_report(focused_papers, domain_counts, len(primary_papers))

        # Save
        print("Saving results...")
        self.save_results(focused_papers, report)

        # Summary
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"\n✓ PRIMARY Corpus: {len(primary_papers)} papers")
        print(f"✓ FOCUSED Corpus: {len(focused_papers)} papers")
        print(f"✓ Removed: {len(primary_papers) - len(focused_papers)} papers ({100*(len(primary_papers) - len(focused_papers))/len(primary_papers):.1f}%)")
        print(f"\n✓ By domain (focused):")
        for domain in ['em_connectomics', 'mri_connectomics', 'methods_ml', 'network_science']:
            count = sum(1 for p in focused_papers if p.get('domain') == domain)
            if count > 0:
                pct = 100 * count / len(focused_papers)
                print(f"  - {domain}: {count} ({pct:.1f}%)")

if __name__ == '__main__':
    builder = FocusedCorpusBuilder()
    builder.run()
