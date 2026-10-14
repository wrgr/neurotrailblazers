#!/usr/bin/env python3
"""
Complete Helmstaedter citation expansion.

For each of 179 reference papers:
1. Get all papers that cite it (in-citations)
2. Get all papers it cites (out-citations)
3. Build comprehensive citation neighborhood
4. Compare to PRIMARY corpus

Input: 179-reference JSON from Helmstaedter 2026 review
Output: Complete expanded citation network
"""

import json
import requests
from pathlib import Path
from collections import defaultdict
import time

class HelmstaedterCompleteExpansion:
    def __init__(self, references_json, output_dir="scripts/bibliometrics/output"):
        self.references_json = Path(references_json)
        self.output_dir = Path(output_dir)
        self.openalex_base = "https://api.openalex.org"
        self.references = []
        self.citing_papers = {}  # Papers that cite our references
        self.cited_papers = {}   # Papers cited by our references

    def load_references(self):
        """Load the 179-reference JSON."""
        print("="*80)
        print("HELMSTAEDTER COMPLETE CITATION EXPANSION")
        print("="*80)

        print(f"\nLoading references from: {self.references_json}")

        with open(self.references_json) as f:
            data = json.load(f)

        # Handle both list and dict formats
        if isinstance(data, list):
            self.references = data
        elif isinstance(data, dict) and 'references' in data:
            self.references = data['references']
        else:
            self.references = data if isinstance(data, list) else [data]

        print(f"✓ Loaded {len(self.references)} references")
        return self

    def expand_all_references(self):
        """For each reference, get citing and cited papers."""
        print(f"\n[EXPANSION] Processing {len(self.references)} references...\n")

        success_count = 0
        fail_count = 0

        for i, ref in enumerate(self.references, 1):
            doi = ref.get('doi', '').strip()

            if not doi or doi == 'N/A':
                continue

            if i % 20 == 0:
                print(f"  [{i}/{len(self.references)}] Citing: {len(self.citing_papers)}, Cited: {len(self.cited_papers)}")

            # Get papers that cite this reference
            citing = self._get_citing_papers(doi)

            # Get papers cited by this reference
            cited = self._get_cited_papers(doi)

            if citing or cited:
                success_count += 1
            else:
                fail_count += 1

            time.sleep(0.1)  # Rate limiting

        print(f"\n✓ Expansion complete")
        print(f"  Successfully expanded: {success_count} references")
        print(f"  Failed/skipped: {fail_count} references")
        print(f"  Total citing papers: {len(self.citing_papers)}")
        print(f"  Total cited papers: {len(self.cited_papers)}")

        return self

    def _get_citing_papers(self, doi):
        """Get papers that cite this DOI."""
        try:
            url = f"{self.openalex_base}/works?filter=cites_doi:{doi}&per_page=100"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                return []

            data = response.json()
            papers = []

            for result in data.get('results', []):
                work_id = result.get('id')
                if work_id:
                    self.citing_papers[work_id] = {
                        'doi': result.get('doi'),
                        'title': result.get('title'),
                        'year': result.get('publication_year'),
                        'cited_by': result.get('cited_by_count', 0)
                    }
                    papers.append(work_id)

            return papers

        except Exception as e:
            return []

    def _get_cited_papers(self, doi):
        """Get papers cited by this DOI."""
        try:
            # Query OpenAlex for the paper itself
            url = f"{self.openalex_base}/works?filter=doi:{doi}"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                return []

            data = response.json()
            results = data.get('results', [])

            if not results:
                return []

            work = results[0]
            referenced_works = work.get('referenced_works', [])

            papers = []
            for ref_id in referenced_works[:200]:  # Limit to first 200
                if ref_id not in self.cited_papers:
                    self.cited_papers[ref_id] = {
                        'type': 'cited_by_reference'
                    }
                papers.append(ref_id)

            return papers

        except Exception as e:
            return []

    def get_combined_set(self):
        """Get complete set of all papers (references + citing + cited)."""
        # Start with the reference DOIs
        reference_dois = set()
        for ref in self.references:
            doi = ref.get('doi', '').strip()
            if doi and doi != 'N/A':
                reference_dois.add(doi)

        combined_set = reference_dois.copy()

        # Add all citing papers
        combined_set.update(self.citing_papers.keys())

        # Add all cited papers
        combined_set.update(self.cited_papers.keys())

        print(f"\n[COMBINED SET]")
        print(f"  Reference papers: {len(reference_dois)}")
        print(f"  Citing papers: {len(self.citing_papers)}")
        print(f"  Cited papers: {len(self.cited_papers)}")
        print(f"  Total combined: {len(combined_set)}")

        return combined_set, reference_dois

    def save_results(self, combined_set, reference_dois):
        """Save expansion results."""
        # Save citing papers
        citing_file = self.output_dir / 'helmstaedter_citing_papers.json'
        with open(citing_file, 'w') as f:
            json.dump({
                'metadata': {
                    'papers_that_cite_helmstaedter_references': len(self.citing_papers),
                    'generated': '2026-04-01'
                },
                'papers': list(self.citing_papers.values())
            }, f, indent=2)
        print(f"\n✓ Saved: {citing_file}")

        # Save cited papers
        cited_file = self.output_dir / 'helmstaedter_cited_papers.json'
        with open(cited_file, 'w') as f:
            json.dump({
                'metadata': {
                    'papers_cited_by_helmstaedter_references': len(self.cited_papers),
                    'generated': '2026-04-01'
                },
                'papers': list(self.cited_papers.values())
            }, f, indent=2)
        print(f"✓ Saved: {cited_file}")

        # Save combined set
        combined_file = self.output_dir / 'helmstaedter_complete_expansion.json'
        with open(combined_file, 'w') as f:
            json.dump({
                'metadata': {
                    'helmstaedter_references': len(reference_dois),
                    'citing_helmstaedter': len(self.citing_papers),
                    'cited_by_helmstaedter': len(self.cited_papers),
                    'total_combined': len(combined_set),
                    'generated': '2026-04-01'
                },
                'combined_set_size': len(combined_set)
            }, f, indent=2)
        print(f"✓ Saved: {combined_file}")

    def run(self):
        """Execute full expansion."""
        self.load_references()
        self.expand_all_references()
        combined_set, reference_dois = self.get_combined_set()
        self.save_results(combined_set, reference_dois)

        print("\n" + "="*80)
        print("EXPANSION COMPLETE - READY FOR K-CORE ANALYSIS")
        print("="*80)

if __name__ == '__main__':
    expander = HelmstaedterCompleteExpansion('data/helmstaedter_references_complete.json')
    expander.run()
