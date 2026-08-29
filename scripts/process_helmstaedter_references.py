#!/usr/bin/env python3
"""
Process Helmstaedter complete reference JSON.
Extract all DOIs, analyze distribution, prepare for OpenAlex expansion.
"""

import json
from pathlib import Path
from collections import Counter, defaultdict

class HelmstaedterReferenceProcessor:
    def __init__(self, input_file, output_dir="scripts/bibliometrics/output"):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.references = []

    def load_and_process(self):
        """Load JSON and extract all DOIs."""
        print("="*80)
        print("HELMSTAEDTER REFERENCE PROCESSING")
        print("="*80)

        # Load reference JSON
        print(f"\nLoading: {self.input_file}")
        with open(self.input_file) as f:
            data = json.load(f)

        if isinstance(data, list):
            self.references = data
        elif isinstance(data, dict) and 'references' in data:
            self.references = data['references']
        else:
            self.references = data

        print(f"✓ Loaded {len(self.references)} references")

        return self

    def extract_dois(self):
        """Extract all DOIs from references."""
        dois = []
        missing_dois = []

        for i, ref in enumerate(self.references, 1):
            doi = ref.get('doi', '').strip()

            if doi and doi != 'N/A' and doi != '':
                dois.append(doi)
            else:
                missing_dois.append({
                    'index': i,
                    'title': ref.get('title', 'Unknown')[:50],
                    'authors': ref.get('authors', 'Unknown')
                })

        print(f"\nDOI Extraction:")
        print(f"  Total references: {len(self.references)}")
        print(f"  With DOI: {len(dois)}")
        print(f"  Missing DOI: {len(missing_dois)}")
        print(f"  Coverage: {100*len(dois)/len(self.references):.1f}%")

        if missing_dois:
            print(f"\n  References without DOI:")
            for m in missing_dois[:5]:
                print(f"    - {m['authors']}")
            if len(missing_dois) > 5:
                print(f"    ... and {len(missing_dois)-5} more")

        return dois, missing_dois

    def analyze_distribution(self, dois):
        """Analyze DOI distribution by journal and year."""
        journals = Counter(ref.get('journal', 'Unknown') for ref in self.references)
        years = Counter(ref.get('year', 'Unknown') for ref in self.references)
        types = Counter(ref.get('type', 'Unknown') for ref in self.references)

        print(f"\nJournal Distribution (top 10):")
        for journal, count in journals.most_common(10):
            print(f"  {journal}: {count}")

        print(f"\nYear Distribution (top 10):")
        for year, count in sorted(years.most_common(10), key=lambda x: -x[1]):
            print(f"  {year}: {count}")

        print(f"\nReference Type Distribution:")
        for ref_type, count in types.most_common():
            print(f"  {ref_type}: {count}")

        return journals, years, types

    def save_results(self, dois, missing_dois):
        """Save DOI list for OpenAlex processing."""
        # DOI list only
        doi_list = [{'doi': doi} for doi in dois]

        doi_file = self.output_dir / 'helmstaedter_dois_all.json'
        with open(doi_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'Helmstaedter 2026 Nature Reviews Neuroscience - Complete Reference List',
                    'total_references': len(self.references),
                    'total_dois': len(dois),
                    'coverage': f"{100*len(dois)/len(self.references):.1f}%",
                    'generated': '2026-04-01'
                },
                'dois': doi_list
            }, f, indent=2)

        print(f"\n✓ Saved: {doi_file}")

        # Missing DOIs for review
        if missing_dois:
            missing_file = self.output_dir / 'helmstaedter_references_missing_doi.json'
            with open(missing_file, 'w') as f:
                json.dump({
                    'metadata': {
                        'count': len(missing_dois),
                        'note': 'References without DOI - may need manual lookup'
                    },
                    'references': missing_dois
                }, f, indent=2)

            print(f"✓ Saved: {missing_file}")

        return doi_file

    def run(self):
        """Execute full processing."""
        self.load_and_process()
        dois, missing_dois = self.extract_dois()
        self.analyze_distribution(dois)
        self.save_results(dois, missing_dois)

        print("\n" + "="*80)
        print("NEXT STEPS")
        print("="*80)
        print(f"\n✓ Ready to process {len(dois)} DOIs with OpenAlex")
        print("  - Batch lookup all DOIs")
        print("  - Build complete citation neighborhood")
        print("  - Compare to PRIMARY corpus (959 papers)")
        print("  - Compute k-core on expanded set")

if __name__ == '__main__':
    processor = HelmstaedterReferenceProcessor('data/helmstaedter_references_complete.json')
    processor.run()
