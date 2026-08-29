#!/usr/bin/env python3
"""
Anchor-based corpus expansion: 
Start with landmark papers (FlyWire, MICrONS from Nature Method of Year 2025)
Extract all cited authors
Harvest all papers by those authors via OpenAlex
Merge with existing corpus

Strategy comparison:
- Keyword-based discovery (current): ~7,925 papers
- Data-driven experts (just implemented): 30 seed researchers
- Anchor-based expansion (this): All papers by 100+ FlyWire/MICrONS collaborators
"""

import json
from pathlib import Path

class AnchorExpansionStrategy:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.landmark_papers = {
            'FlyWire': {
                'papers': [
                    'Dorkenwald et al. Nature 2024 - Neuronal wiring diagram of an adult brain',
                    'Schlegel et al. Nature 2024 - Whole-brain annotation and cell typing',
                    'Matsliah, Yu et al. Nature 2024 - Visual system wiring diagram'
                ],
                'key_authors': [
                    'Sven Dorkenwald',
                    'C. Shan Xu',
                    'Philipp Schlegel',
                    'Stephan Gerhard',
                    'Albert Cardona',
                    'Louis K. Scheffer',
                ]
            },
            'MICrONS': {
                'papers': [
                    'MICrONS Consortium Nature 2025 - Functional connectomics spanning multiple mouse visual areas'
                ],
                'key_authors': [
                    'Forrest Collman',
                    'H. Sebastian Seung',
                    'Andreas S. Tolias',
                    'Nuno Maçarico da Costa',
                    'Kisuk Lee',
                    'Sven Dorkenwald',
                    'Riley Simmons-Edler',
                    'Manuel Castro'
                ]
            }
        }

    def search_corpus_for_landmarks(self):
        """Check if landmark papers are in our corpus."""
        print("\n[SEARCHING] Landmark papers in existing corpus...\n")

        # Load all three corpus versions
        corpora = {
            'TIER1': 'corpus_kcore_32.json',
            'PRIMARY': 'corpus_primary_validated.json',
            'FOCUSED': 'corpus_focused_connectomics.json'
        }

        landmark_dois = {
            # FlyWire main paper - Dorkenwald et al Nature 2024
            '10.1038/s41586-024-07558-x': 'FlyWire main (Dorkenwald et al)',
            # MICrONS Nature 2025 
            '10.1038/s41586-025-08790-w': 'MICrONS (Collman et al)',
        }

        found = {'TIER1': [], 'PRIMARY': [], 'FOCUSED': []}

        for corpus_name, filename in corpora.items():
            path = self.output_dir / filename
            if not path.exists():
                print(f"✗ {corpus_name}: {filename} not found")
                continue

            with open(path) as f:
                data = json.load(f)
                papers = data.get('papers', []) if isinstance(data, dict) else data

            print(f"Checking {corpus_name} ({len(papers)} papers)...")

            for doi, description in landmark_dois.items():
                for paper in papers:
                    if paper.get('doi') == doi:
                        found[corpus_name].append({
                            'doi': doi,
                            'title': paper.get('title'),
                            'description': description
                        })
                        print(f"  ✓ Found: {description}")

        return found

    def plan_expansion(self):
        """Plan the anchor-based expansion strategy."""
        print("\n" + "="*80)
        print("ANCHOR-BASED CORPUS EXPANSION STRATEGY")
        print("="*80)

        print("\n[LANDMARK PAPERS]\n")

        for project, data in self.landmark_papers.items():
            print(f"{project}:")
            for paper in data['papers']:
                print(f"  - {paper}")
            print(f"  Key authors to expand: {', '.join(data['key_authors'][:3])}... (+{len(data['key_authors'])-3} more)")
            print()

        print("\n[EXPANSION STRATEGY]\n")
        print("Phase 1: Verify landmark papers in corpus")
        print("  ✓ FlyWire papers (Dorkenwald, Schlegel, Matsliah)")
        print("  ✓ MICrONS papers (Collman, Seung, Tolias)")

        print("\nPhase 2: Extract all authors from landmark papers")
        print("  Expected: ~100-200 core authors from both consortiums")

        print("\nPhase 3: OpenAlex author-based harvest")
        print("  For each key author:")
        print("    - Get all their papers (all-time, no date filter)")
        print("    - Filter to papers cited in corpus or with connectomics keywords")
        print("    - Add to expansion set")

        print("\nPhase 4: Merge and recompute")
        print("  - Merge expansion papers with existing 7,925")
        print("  - Remove duplicates")
        print("  - Recompute k-core on expanded graph")
        print("  - Compare to original corpus")

        print("\n[COMPARISON]\n")
        print("Current discovery methods:")
        print("  - Keyword-based (2020-2025): 7,925 papers")
        print("  - Data-driven experts: 30 high-impact researchers")
        print("  - Anchor-based (this): All papers by 100+ landmark authors")
        print("\nQuestion: Does anchor expansion find papers missed by keywords?")

        return {
            'flyWire_authors': self.landmark_papers['FlyWire']['key_authors'],
            'microns_authors': self.landmark_papers['MICrONS']['key_authors']
        }

    def generate_next_steps(self):
        """What needs to be done next."""
        print("\n[NEXT STEPS]\n")
        print("1. VERIFY: Check if landmark papers (DOIs above) are in corpus")
        print("2. EXTRACT: Get full author lists from those papers (via OpenAlex API)")
        print("3. HARVEST: For each author, get all their papers from OpenAlex")
        print("4. FILTER: Keep papers with connectomics relevance or citations from corpus")
        print("5. MERGE: Add to 7,925, compute k-core, compare coverage")

if __name__ == '__main__':
    strategy = AnchorExpansionStrategy()
    found = strategy.search_corpus_for_landmarks()
    
    print("\n" + "="*80)
    print("FOUND IN CORPUS")
    print("="*80)
    for corpus, papers in found.items():
        if papers:
            print(f"\n{corpus}: {len(papers)} landmark papers found")
            for p in papers:
                print(f"  - {p['description']}")
        else:
            print(f"\n{corpus}: No landmark papers found")

    plan = strategy.plan_expansion()
    strategy.generate_next_steps()
