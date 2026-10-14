#!/usr/bin/env python3
"""
Helmstaedter review reference expansion:

1. Parse reference list (provided by user)
2. Extract DOIs and lookup in OpenAlex
3. Get all authors from cited papers
4. Harvest all papers by those authors
5. Apply k≥25 + in-degree≥2 filtering
6. Compare to existing PRIMARY corpus
"""

import json
import requests
from pathlib import Path
from collections import defaultdict
import time

# Reference list from Helmstaedter 2026 review (parsed from user input)
HELMSTAEDTER_REFERENCES = [
    ("10.1038/ncomms3770", "Zador"),  # Critique of pure learning
    ("10.1038/s41467-022-29385-5", "Roy"),  # Brain-wide mapping engrams
    ("10.1371/journal.pbio.0020329", "Denk & Horstmann"),  # Serial block-face SEM
    ("10.1126/science.1206837", "Lichtman & Denk"),  # Big and small challenges
    ("10.1016/j.conb.2008.09.005", "Helmstaedter"),  # 3D structural imaging
    ("10.1016/j.conb.2006.06.002", "Briggman & Denk"),  # Volume EM reconstruction
    ("10.1371/journal.pcbi.0010042", "Sporns et al"),  # Human connectome
    ("10.1101/2024.03.22.586254", "Sievers et al"),  # Cortical column reconstruction
    ("10.1038/s41586-025-08790-w", "MICrONS"),  # Mouse visual cortex
    ("10.1126/science.abo0924", "Loomba et al"),  # Mouse vs human cortex
    ("10.1126/science.adk4858", "Shapson-Coe et al"),  # Human cortex nanoscale
    ("10.1126/science.aad9330", "Winding et al"),  # Insect brain connectome
    ("10.1016/j.cell.2018.06.019", "Zheng et al"),  # Drosophila connectome
    ("10.1038/s41586-024-07558-x", "Dorkenwald et al"),  # FlyWire wiring diagram
    ("10.1038/s41586-024-07419-0", "Schlegel et al"),  # Drosophila annotation
    ("10.1038/s41592-024-02237-2", "Schmidt et al"),  # RoboEM
    ("10.1038/s41586-025-08896-3", "Celii et al"),  # NEURD proofreading
    ("10.1093/icb/icad145", "Treidel et al"),  # Insect flight
    ("10.1038/s41586-024-06988-3", "Furutachi et al"),  # Thalamocortical prediction
    ("10.1016/j.cell.2024.02.026", "Chen et al"),  # Neural activity memory
    ("10.1038/nature16960", "Li et al"),  # Premotor cortex prediction
    ("10.1038/s41586-025-08847-6", "Findling et al"),  # Prior information
    ("10.1016/j.neuron.2017.12.033", "Fournier et al"),  # Visual cortex
    ("10.1016/j.brainstructfunc.2020.08.020", "Montardy et al"),  # Predator fear
    ("10.1038/nature09820", "Briggman et al"),  # Retinal direction selectivity
    ("10.1038/nature12988", "Kim et al"),  # Direction selectivity retina
    ("10.1038/nature14132", "Ding et al"),  # Mammalian retina wiring
    ("10.1038/nature12563", "Takemura et al 2013"),  # Motion detection Drosophila
    ("10.7554/elife.24394", "Takemura et al 2017"),  # ON motion detection
    ("10.1038/nn.4050", "Borst & Helmstaedter"),  # Motion vision fly mammal
    ("10.1038/s41467-022-35531-w", "Zador et al 2023"),  # NeuroAI
    ("10.1016/j.neuron.2015.01.028", "Helmstaedter 2015"),  # Machine learning neuro
    ("10.1016/j.neuron.2017.06.011", "Hassabis et al"),  # Neuro-inspired AI
    ("10.1016/j.cell.2020.08.037", "Abbott et al"),  # Mind of a mouse
    ("10.3389/fnhum.2009.00031", "Herculano-Houzel"),  # Human brain numbers
    ("10.1038/s41586-021-03465-4", "Bakken et al"),  # Comparative motor cortex
    ("10.1038/s41586-021-03569-3", "Berg et al"),  # Human neocortex expansion
    ("10.1016/j.neuron.2009.01.015", "Lefort et al"),  # Barrel column organization
    ("10.1073/pnas.1306820110", "Meyer et al"),  # Whisker-specific organization
    ("10.1038/nmeth.2445", "Helmstaedter 2013"),  # Cellular connectomics
    ("10.1038/s41592-021-01166-8", "Buhmann et al"),  # Synaptic partner detection
    ("10.1038/nature12346", "Helmstaedter IPL"),  # Inner plexiform layer
    ("10.1126/science.287.5451.273", "Gupta et al"),  # GABA interneurons
    ("10.1038/s41586-021-03229-w", "Holler et al"),  # Neocortical synapse
    ("10.1038/nature23236", "Schmidt et al MEC"),  # Entorhinal cortex
    ("10.7554/elife.24364", "Kornfeld et al"),  # Sequence generation
    ("10.1016/j.conb.2011.12.002", "Briggman & Bock"),  # Volume EM review
]

class HelmstaedterRefsExpansion:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.openalex_base = "https://api.openalex.org"

    def lookup_papers_by_doi(self, dois_list):
        """Look up papers by DOI in OpenAlex."""
        print("="*80)
        print("HELMSTAEDTER REFERENCES EXPANSION")
        print("="*80)

        print(f"\n[STEP 1] Looking up {len(dois_list)} references in OpenAlex...\n")

        papers = []
        found = 0

        for i, (doi, author_hint) in enumerate(dois_list, 1):
            if i % 10 == 0:
                print(f"  [{i}/{len(dois_list)}] Found {found} so far...")

            try:
                url = f"{self.openalex_base}/works?filter=doi:{doi}"
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    if data.get('results'):
                        paper = data['results'][0]
                        papers.append(paper)
                        found += 1

                time.sleep(0.1)  # Rate limiting

            except Exception as e:
                pass

        print(f"\n✓ Found {found}/{len(dois_list)} papers in OpenAlex")
        return papers

    def extract_unique_authors(self, papers):
        """Extract all unique authors from papers."""
        print(f"\n[STEP 2] Extracting unique authors...")

        unique_authors = {}

        for paper in papers:
            authorships = paper.get('authorships', [])

            for auth in authorships:
                author_obj = auth.get('author', {})
                if author_obj and author_obj.get('id'):
                    author_id = author_obj['id']

                    if author_id not in unique_authors:
                        unique_authors[author_id] = {
                            'name': author_obj.get('display_name', 'Unknown'),
                            'openalex_id': author_id,
                            'papers_in_helmstaedter': 0
                        }

                    unique_authors[author_id]['papers_in_helmstaedter'] += 1

        print(f"✓ Found {len(unique_authors)} unique authors")
        return unique_authors

    def harvest_all_papers(self, authors):
        """Harvest all papers by these authors."""
        print(f"\n[STEP 3] Harvesting ALL papers by {len(authors)} authors...")
        print(f"(This will take a few minutes...)\n")

        all_papers = defaultdict(lambda: {
            'title': '',
            'year': 0,
            'cited_by': 0,
            'authors': set(),
            'count': 0
        })

        author_counts = {}

        for i, (author_id, author_info) in enumerate(authors.items(), 1):
            author_name = author_info['name']

            if i % 50 == 0:
                print(f"  [{i}/{len(authors)}]")

            papers = []
            page = 1

            try:
                while page <= 50:  # Max 10k papers per author
                    url = f"{self.openalex_base}/works?filter=author.id:{author_id}&per_page=200&page={page}"
                    response = requests.get(url, timeout=10)

                    if response.status_code != 200:
                        break

                    data = response.json()
                    results = data.get('results', [])

                    if not results:
                        break

                    papers.extend(results)
                    page += 1
                    time.sleep(0.05)

            except:
                pass

            author_counts[author_name] = len(papers)

            for paper in papers:
                doi = paper.get('doi', f"unknown_{i}")
                all_papers[doi]['title'] = paper.get('title', 'Unknown')
                all_papers[doi]['year'] = paper.get('publication_year', 0)
                all_papers[doi]['cited_by'] = paper.get('cited_by_count', 0)
                all_papers[doi]['authors'].add(author_name)
                all_papers[doi]['count'] += 1

        print(f"\n✓ Harvesting complete")
        return all_papers, author_counts

    def run(self):
        """Execute."""
        dois = [d for d, _ in HELMSTAEDTER_REFERENCES]

        papers = self.lookup_papers_by_doi(HELMSTAEDTER_REFERENCES)
        authors = self.extract_unique_authors(papers)
        all_papers, author_counts = self.harvest_all_papers(authors)

        return {
            'helmstaedter_refs': papers,
            'unique_authors': authors,
            'all_papers': all_papers,
            'author_counts': author_counts
        }

    def save_results(self, results):
        """Save."""
        all_papers = results['all_papers']

        # Convert to list
        papers_list = []
        for doi, data in all_papers.items():
            papers_list.append({
                'doi': doi,
                'title': data['title'],
                'year': data['year'],
                'cited_by_count': data['cited_by'],
                'by_authors_count': data['count'],
                'authors': list(data['authors'])
            })

        papers_list.sort(key=lambda x: -x['cited_by_count'])

        # Save papers
        papers_file = self.output_dir / 'helmstaedter_refs_papers.json'
        with open(papers_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'All papers by authors cited in Helmstaedter 2026 review',
                    'total_papers': len(papers_list),
                    'total_authors': len(results['unique_authors']),
                    'generated': '2026-04-01'
                },
                'papers': papers_list
            }, f, indent=2)

        print(f"\n✓ Saved: {papers_file}")
        print(f"  Total papers: {len(papers_list)}")
        print(f"  Total authors: {len(results['unique_authors'])}")

if __name__ == '__main__':
    discovery = HelmstaedterRefsExpansion()
    results = discovery.run()
    discovery.save_results(results)

    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)

    print(f"\nHelmstaedter reference papers cited: {len(results['helmstaedter_refs'])}")
    print(f"Unique authors: {len(results['unique_authors'])}")
    print(f"Total papers harvested: {len(results['all_papers'])}")

    top_authors = sorted(results['author_counts'].items(), key=lambda x: -x[1])
    print(f"\nTop 10 authors by paper count:")
    for i, (name, count) in enumerate(top_authors[:10], 1):
        print(f"  {i}. {name}: {count} papers")
