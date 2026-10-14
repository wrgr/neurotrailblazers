#!/usr/bin/env python3
"""
Parse Helmstaedter 2026 review references with DOIs.

Format: Author(s). Title. Journal Year. DOI

This script:
1. Parses reference text
2. Extracts DOI
3. Structures as JSON
4. Prepares for OpenAlex lookup
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Optional

class HelmstaedterReferenceParser:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)

    def parse_references_from_text(self, text: str) -> List[Dict]:
        """
        Parse reference list from formatted text.

        Expected format:
        Authors. Title. Journal Year. DOI
        - PubMed - PMC - DOI

        Example:
        Zador, A. M. A critique of pure learning... Nat. Commun. 10, 3770 (2019). - PubMed - DOI
        """
        references = []

        # Split by lines starting with author names (capitalized)
        # More robust: look for patterns with DOI

        # DOI pattern: 10.xxxx/xxxxx
        doi_pattern = r'10\.\d{4,}/[^\s)]+'

        lines = text.strip().split('\n')

        current_ref = []

        for line in lines:
            line = line.strip()

            if not line:
                continue

            # Check if this is a new reference (starts with author, or contains DOI)
            doi_match = re.search(doi_pattern, line)

            if doi_match:
                # This line contains a DOI
                doi = doi_match.group(0)

                # Join accumulated lines as the reference
                full_text = ' '.join(current_ref) + ' ' + line if current_ref else line

                # Try to extract author and title
                author, title = self._extract_author_title(full_text)

                references.append({
                    'doi': doi,
                    'full_text': full_text,
                    'author': author,
                    'title': title
                })

                current_ref = []
            else:
                # Accumulate lines
                current_ref.append(line)

        return references

    def _extract_author_title(self, text: str) -> tuple:
        """Extract first author name and approximate title from reference text."""
        # Try to find author (before first period)
        parts = text.split('.')

        if len(parts) >= 2:
            author = parts[0].strip()
            title = parts[1].strip() if len(parts) > 1 else ''
        else:
            author = text[:50]
            title = ''

        return author, title

    def parse_structured_references(self, references_list: List[str]) -> List[Dict]:
        """
        Parse a list of pre-formatted references.

        Input format: List of "Author. Title. Journal Year. DOI" strings
        """
        references = []

        doi_pattern = r'10\.\d{4,}/[^\s)]+'

        for ref_text in references_list:
            if not ref_text.strip():
                continue

            # Find DOI
            doi_match = re.search(doi_pattern, ref_text)

            if doi_match:
                doi = doi_match.group(0)

                # Extract author (before first period)
                author_match = re.match(r'^([^.]+)\.', ref_text)
                author = author_match.group(1) if author_match else 'Unknown'

                references.append({
                    'doi': doi,
                    'author': author.strip(),
                    'full_text': ref_text.strip()
                })

        return references

    def save_references(self, references: List[Dict], filename: str = 'helmstaedter_references_parsed.json'):
        """Save parsed references to JSON."""
        output_file = self.output_dir / filename

        with open(output_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'Helmstaedter 2026 Nature Reviews Neuroscience',
                    'total_references': len(references),
                    'with_doi': sum(1 for r in references if r.get('doi')),
                    'generated': '2026-04-01'
                },
                'references': references
            }, f, indent=2)

        print(f"✓ Saved: {output_file}")
        print(f"  Total: {len(references)}")
        print(f"  With DOI: {sum(1 for r in references if r.get('doi'))}")

        return output_file

    def run_from_raw_text(self, text: str):
        """Parse from raw text and save."""
        print("Parsing references from raw text...")
        references = self.parse_references_from_text(text)
        return self.save_references(references, 'helmstaedter_references_raw.json')

    def run_from_list(self, references_list: List[str]):
        """Parse from pre-formatted list and save."""
        print(f"Parsing {len(references_list)} references...")
        references = self.parse_structured_references(references_list)
        return self.save_references(references, 'helmstaedter_references_parsed.json')


# Pre-formatted references from Helmstaedter 2026 review
HELMSTAEDTER_REFERENCES = [
    "Zador, A. M. A critique of pure learning and what artificial neural networks can learn from animal brains. Nat. Commun. 10, 3770 (2019). - PubMed - PMC - DOI",
    "Roy, D. S. et al. Brain-wide mapping reveals that engrams for a single memory are distributed across multiple brain regions. Nat. Commun. 13, 1799 (2022). - PubMed - PMC - DOI",
    "Denk, W. & Horstmann, H. Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure. PLoS Biol. 2, e329 (2004). - PubMed - PMC - DOI",
    "Lichtman, J. W. & Denk, W. The big and the small: challenges of imaging the brain's circuits. Science 334, 618–623 (2011). - PubMed - DOI",
    "Helmstaedter, M., Briggman, K. L. & Denk, W. 3D structural imaging of the brain with photons and electrons. Curr. Opin. Neurobiol. 18, 633–641 (2008). - PubMed - DOI",
    "Briggman, K. L. & Denk, W. Towards neural circuit reconstruction with volume electron microscopy techniques. Curr. Opin. Neurobiol. 16, 562–570 (2006). - PubMed - DOI",
    "Sporns, O., Tononi, G. & Kotter, R. The human connectome: a structural description of the human brain. PLoS Comput. Biol. 1, e42 (2005). - PubMed - PMC - DOI",
    "Sievers, M. et al. Connectomic reconstruction of a cortical column. Preprint at bioRxiv https://doi.org/10.1101/2024.03.22.586254 (2024).",
    "MICrONS Consortium. Functional connectomics spanning multiple areas of mouse visual cortex. Nature 640, 435–447 (2025). - DOI",
    "Loomba, S. et al. Connectomic comparison of mouse and human cortex. Science 377, eabo0924 (2022). - PubMed - DOI",
    "Shapson-Coe, A. et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. Science 384, eadk4858 (2024). - PubMed - PMC - DOI",
    "Winding, M. et al. The connectome of an insect brain. Science 379, eadd9330 (2023). - PubMed - PMC - DOI",
    "Zheng, Z. et al. A complete electron microscopy volume of the brain of adult Drosophila melanogaster. Cell 174, 730–743.e722 (2018). - PubMed - PMC - DOI",
    "Dorkenwald, S. et al. Neuronal wiring diagram of an adult brain. Nature 634, 124–138 (2024). - PubMed - PMC - DOI",
    "Schlegel, P. et al. Whole-brain annotation and multi-connectome cell typing of Drosophila. Nature 634, 139–152 (2024). - PubMed - PMC - DOI",
    "Schmidt, M., Motta, A., Sievers, M. & Helmstaedter, M. RoboEM: automated 3D flight tracing for synaptic-resolution connectomics. Nat. Methods 21, 908–913 (2024). - PubMed - PMC - DOI",
    "Celii, B. et al. NEURD offers automated proofreading and feature extraction for connectomics. Nature 640, 487–496 (2025). - PubMed - PMC - DOI",
    "Treidel, L. A. et al. Insect flight: state of the field and future directions. Integr. Comp. Biol. 64, 533–555 (2024). - PubMed - DOI",
    "Furutachi, S., Franklin, A. D., Aldea, A. M., Mrsic-Flogel, T. D. & Hofer, S. B. Cooperative thalamocortical circuit mechanism for sensory prediction errors. Nature 633, 398–406 (2024). - PubMed - PMC - DOI",
    "Chen, S. et al. Brain-wide neural activity underlying memory-guided movement. Cell 187, 676–691.e616 (2024). - PubMed - PMC - DOI",
    "Li, N., Daie, K., Svoboda, K. & Druckmann, S. Robust neuronal dynamics in premotor cortex during motor planning. Nature 532, 459–464 (2016). - PubMed - PMC - DOI",
    "Findling, C. et al. Brain-wide representations of prior information in mouse decision-making. Nature 645, 192–200 (2025). - PubMed - PMC - DOI",
    "Fournier, J., Muller, C. M., Schneider, I. & Laurent, G. Spatial information in a non-retinotopic visual cortex. Neuron 97, 164–180.e167 (2018). - PubMed - DOI",
    "Montardy, Q. et al. Mapping the neural circuitry of predator fear in the nonhuman primate. Brain Struct. Funct. 226, 195–205 (2021). - PubMed - DOI",
    "Briggman, K. L., Helmstaedter, M. & Denk, W. Wiring specificity in the direction-selectivity circuit of the retina. Nature 471, 183–188 (2011). - PubMed - DOI",
    "Kim, J. S. et al. Space-time wiring specificity supports direction selectivity in the retina. Nature 509, 331–336 (2014). - PubMed - PMC - DOI",
    "Ding, H., Smith, R. G., Poleg-Polsky, A., Diamond, J. S. & Briggman, K. L. Species-specific wiring for direction selectivity in the mammalian retina. Nature 535, 105–110 (2016). - PubMed - PMC - DOI",
    "Takemura, S. Y. et al. A visual motion detection circuit suggested by Drosophila connectomics. Nature 500, 175–181 (2013). - PubMed - PMC - DOI",
    "Takemura, S. Y. et al. The comprehensive connectome of a neural substrate for 'ON' motion detection in Drosophila. eLife 6, e24394 (2017). - PubMed - PMC - DOI",
    "Borst, A. & Helmstaedter, M. Common circuit design in fly and mammalian motion vision. Nat. Neurosci. 18, 1067–1076 (2015). - PubMed - DOI",
    "Zador, A. et al. Catalyzing next-generation artificial intelligence through neuroAI. Nat. Commun. 14, 1597 (2023). - PubMed - PMC - DOI",
    "Helmstaedter, M. The mutual inspirations of machine learning and neuroscience. Neuron 86, 25–28 (2015). - PubMed - DOI",
    "Hassabis, D., Kumaran, D., Summerfield, C. & Botvinick, M. Neuroscience-inspired artificial intelligence. Neuron 95, 245–258 (2017). - PubMed - DOI",
    "Abbott, L. F. et al. The mind of a mouse. Cell 182, 1372–1376 (2020). - PubMed - DOI",
    "Herculano-Houzel, S. The human brain in numbers: a linearly scaled-up primate brain. Front. Hum. Neurosci. 3, 31 (2009). - PubMed - PMC - DOI",
    "Bakken, T. E. et al. Comparative cellular analysis of motor cortex in human, marmoset and mouse. Nature 598, 111–119 (2021). - PubMed - PMC - DOI",
    "Berg, J. et al. Human neocortical expansion involves glutamatergic neuron diversification. Nature 598, 151–158 (2021). - PubMed - PMC - DOI",
    "Lefort, S., Tomm, C., Floyd Sarria, J. C. & Petersen, C. C. The excitatory neuronal network of the C2 barrel column in mouse primary somatosensory cortex. Neuron 61, 301–316 (2009). - PubMed - DOI",
    "Meyer, H. S. et al. Cellular organization of cortical barrel columns is whisker-specific. Proc. Natl Acad. Sci. USA 110, 19113–19118 (2013). - PubMed - PMC - DOI",
    "Helmstaedter, M. Cellular-resolution connectomics: challenges of dense neural circuit reconstruction. Nat. Methods 10, 501–507 (2013). - PubMed - DOI",
    "Buhmann, J. et al. Automatic detection of synaptic partners in a whole-brain Drosophila electron microscopy data set. Nat. Methods 18, 771–774 (2021). - PubMed - PMC - DOI",
    "Helmstaedter, M. et al. Connectomic reconstruction of the inner plexiform layer in the mouse retina. Nature 500, 168–174 (2013). - PubMed - DOI",
    "Gupta, A., Wang, Y. & Markram, H. Organizing principles for a diversity of GABAergic interneurons and synapses in the neocortex. Science 287, 273–278 (2000). - PubMed - DOI",
    "Holler, S., Kostinger, G., Martin, K. A. C., Schuhknecht, G. F. P. & Stratford, K. J. Structure and function of a neocortical synapse. Nature 591, 111–116 (2021). - PubMed - DOI",
    "Schmidt, H. et al. Axonal synapse sorting in medial entorhinal cortex. Nature 549, 469–475 (2017). - PubMed - DOI",
    "Kornfeld, J. et al. EM connectomics reveals axonal target variation in a sequence-generating network. eLife 6, e24364 (2017). - PubMed - PMC - DOI",
    "Briggman, K. L. & Bock, D. D. Volume electron microscopy for neuronal circuit reconstruction. Curr. Opin. Neurobiol. 22, 154–161 (2012). - PubMed - DOI",
    "van Harreveld, A., Crowell, J. & Malhotra, S. K. A study of extracellular space in central nervous tissue by freeze-substitution. J. Cell Biol. 25, 117–137 (1965). - PMC - DOI",
    "Fraenkel-Conrat, H., Brandon, B. A. & Olcott, H. S. The reaction of formaldehyde with proteins; participation of indole groups; gramicidin. J. Biol. Chem. 168, 99–118 (1947). - PubMed - DOI",
    # ... More references continue (truncated for space)
]

if __name__ == '__main__':
    parser = HelmstaedterReferenceParser()

    print("="*80)
    print("HELMSTAEDTER REFERENCE PARSER")
    print("="*80)

    # Parse the pre-formatted list
    parser.run_from_list(HELMSTAEDTER_REFERENCES)

    print("\n✓ References parsed and saved")
