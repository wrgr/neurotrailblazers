#!/usr/bin/env python3
"""
Extract all DOIs from Helmstaedter reference list.

Parses references in format:
Author(s). Title. Journal Volume, Pages (Year). DOI
"""

import json
import re
from pathlib import Path
from typing import List, Dict

class DOIExtractor:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.doi_pattern = r'10\.\d{4,}/[^\s\)]+(?:\))?'

    def extract_from_text(self, text: str) -> List[Dict]:
        """Extract all DOIs and associated metadata from reference text."""
        references = []

        # Split into individual references
        # References are typically separated by blank lines or by author pattern
        lines = text.strip().split('\n')

        current_ref_lines = []

        for line in lines:
            line = line.strip()

            if not line:
                # Blank line - process accumulated reference
                if current_ref_lines:
                    ref_text = ' '.join(current_ref_lines)
                    parsed = self._parse_reference(ref_text)
                    if parsed:
                        references.append(parsed)
                    current_ref_lines = []
            else:
                current_ref_lines.append(line)

        # Don't forget last reference
        if current_ref_lines:
            ref_text = ' '.join(current_ref_lines)
            parsed = self._parse_reference(ref_text)
            if parsed:
                references.append(parsed)

        return references

    def _parse_reference(self, ref_text: str) -> Dict:
        """Parse a single reference to extract DOI and metadata."""
        # Find DOI
        doi_match = re.search(self.doi_pattern, ref_text)

        if not doi_match:
            return None

        doi = doi_match.group(0).rstrip(')')

        # Extract first author
        first_dot = ref_text.find('.')
        author = ref_text[:first_dot] if first_dot > 0 else ref_text[:50]

        # Extract year (usually in parentheses)
        year_match = re.search(r'\((\d{4})\)', ref_text)
        year = year_match.group(1) if year_match else None

        return {
            'doi': doi,
            'author': author.strip(),
            'year': year,
            'full_text': ref_text
        }

    def save(self, references: List[Dict], filename: str = 'helmstaedter_dois_extracted.json'):
        """Save extracted DOIs."""
        output_file = self.output_dir / filename

        with open(output_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'Helmstaedter, M. (2026) Synaptic-resolution connectomics. Nature Rev. Neurosci.',
                    'total_references': len(references),
                    'with_doi': sum(1 for r in references if r.get('doi')),
                    'generated': '2026-04-01'
                },
                'references': references
            }, f, indent=2)

        print(f"✓ Saved: {output_file}")
        print(f"  Total: {len(references)}")
        print(f"  With DOI: {sum(1 for r in references if r.get('doi'))}")
        print(f"  With year: {sum(1 for r in references if r.get('year'))}")

        return output_file


if __name__ == '__main__':
    # Read from stdin or file
    import sys

    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1]) as f:
            text = f.read()
    else:
        # For testing - include just a few examples
        text = """
Denk, W. & Horstmann, H. Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure. PLoS Biol. 2, e329 (2004). DOI: 10.1371/journal.pbio.0020329

Lichtman, J. W. & Denk, W. The big and the small: challenges of imaging the brain's circuits. Science 334, 618–623 (2011). DOI: 10.1126/science.1206837

Helmstaedter, M., Briggman, K. L. & Denk, W. 3D structural imaging of the brain with photons and electrons. Curr. Opin. Neurobiol. 18, 633–641 (2008). DOI: 10.1016/j.conb.2008.09.005
"""

    print("="*80)
    print("HELMSTAEDTER REFERENCE DOI EXTRACTION")
    print("="*80)
    print()

    extractor = DOIExtractor()
    references = extractor.extract_from_text(text)

    print(f"Extracted {len(references)} references\n")

    for i, ref in enumerate(references[:5], 1):
        print(f"{i}. {ref['author']}")
        print(f"   DOI: {ref['doi']}")
        print(f"   Year: {ref['year']}")
        print()

    extractor.save(references)
