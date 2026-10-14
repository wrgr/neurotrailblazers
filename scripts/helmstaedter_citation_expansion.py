#!/usr/bin/env python3
"""
Helmstaedter review citation expansion - CORRECT approach

Strategy:
1. Start with 48 papers cited by Helmstaedter review
2. For each paper:
   - Get all papers it cites (outgoing refs)
   - Get all papers that cite it (incoming refs)
3. Combine all into single expanded set
4. Apply k≥25 + in-degree≥2 filter
5. Compare to PRIMARY (959 papers)

This builds the citation neighborhood around key connectomics papers.
"""

import json
import requests
from pathlib import Path
from collections import defaultdict
import time

# Helmstaedter ref papers (DOI, author hint)
HELMSTAEDTER_REFERENCES = [
    "10.1038/ncomms3770",      # Zador
    "10.1038/s41467-022-29385-5",  # Roy
    "10.1371/journal.pbio.0020329",  # Denk & Horstmann
    "10.1126/science.1206837",  # Lichtman & Denk
    "10.1016/j.conb.2008.09.005",  # Helmstaedter
    "10.1016/j.conb.2006.06.002",  # Briggman & Denk
    "10.1371/journal.pcbi.0010042",  # Sporns et al
    "10.1101/2024.03.22.586254",  # Sievers et al
    "10.1038/s41586-025-08790-w",  # MICrONS
    "10.1126/science.abo0924",  # Loomba et al
    "10.1126/science.adk4858",  # Shapson-Coe et al
    "10.1126/science.aad9330",  # Winding et al
    "10.1016/j.cell.2018.06.019",  # Zheng et al
    "10.1038/s41586-024-07558-x",  # Dorkenwald FlyWire
    "10.1038/s41586-024-07419-0",  # Schlegel
    "10.1038/s41592-024-02237-2",  # Schmidt RoboEM
    "10.1038/s41586-025-08896-3",  # Celii NEURD
    "10.1093/icb/icad145",  # Treidel
    "10.1038/s41586-024-06988-3",  # Furutachi
    "10.1016/j.cell.2024.02.026",  # Chen
    "10.1038/nature16960",  # Li premotor
    "10.1038/s41586-025-08847-6",  # Findling prior
    "10.1016/j.neuron.2017.12.033",  # Fournier
    "10.1016/j.brainstructfunc.2020.08.020",  # Montardy
    "10.1038/nature09820",  # Briggman retina
    "10.1038/nature12988",  # Kim direction
    "10.1038/nature14132",  # Ding wiring
    "10.1038/nature12563",  # Takemura 2013
    "10.7554/elife.24394",  # Takemura 2017
    "10.1038/nn.4050",  # Borst Helmstaedter
    "10.1038/s41467-022-35531-w",  # Zador 2023 NeuroAI
    "10.1016/j.neuron.2015.01.028",  # Helmstaedter 2015
    "10.1016/j.neuron.2017.06.011",  # Hassabis
    "10.1016/j.cell.2020.08.037",  # Abbott
    "10.3389/fnhum.2009.00031",  # Herculano-Houzel
    "10.1038/s41586-021-03465-4",  # Bakken
    "10.1038/s41586-021-03569-3",  # Berg
    "10.1016/j.neuron.2009.01.015",  # Lefort
    "10.1073/pnas.1306820110",  # Meyer
    "10.1038/nmeth.2445",  # Helmstaedter 2013
    "10.1038/s41592-021-01166-8",  # Buhmann
    "10.1038/nature12346",  # Helmstaedter IPL
    "10.1126/science.287.5451.273",  # Gupta GABA
    "10.1038/s41586-021-03229-w",  # Holler synapse
    "10.1038/nature23236",  # Schmidt MEC
    "10.7554/elife.24364",  # Kornfeld sequence
    "10.1016/j.conb.2011.12.002",  # Briggman Bock
]

class HelmstaedterCitationExpansion:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.openalex_base = "https://api.openalex.org"

    def lookup_reference_papers(self):
        """Lookup the 48 reference papers in OpenAlex."""
        print("="*80)
        print("HELMSTAEDTER CITATION NEIGHBORHOOD EXPANSION")
        print("="*80)

        print(f"\n[STEP 1] Looking up {len(HELMSTAEDTER_REFERENCES)} reference papers...\n")

        papers = {}  # doi -> work object

        for i, doi in enumerate(HELMSTAEDTER_REFERENCES, 1):
            if i % 10 == 0:
                print(f"  [{i}/{len(HELMSTAEDTER_REFERENCES)}]")

            try:
                url = f"{self.openalex_base}/works?filter=doi:{doi}"
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    if data.get('results'):
                        work = data['results'][0]
                        papers[work.get('id')] = {
                            'doi': doi,
                            'title': work.get('title'),
                            'cited_by_count': work.get('cited_by_count'),
                            'id': work.get('id')
                        }

                time.sleep(0.15)  # Rate limiting

            except:
                pass

        print(f"\n✓ Found {len(papers)} reference papers")
        return papers

    def expand_citations(self, reference_papers):
        """For each reference paper, get citing and cited papers."""
        print(f"\n[STEP 2] Expanding citation network (citing + cited papers)...")

        expanded_set = set(reference_papers.keys())  # Start with reference papers

        citing_papers = {}  # papers that cite our references
        cited_by_papers = {}  # papers cited by our references

        for i, (ref_id, ref_info) in enumerate(reference_papers.items(), 1):
            if i % 5 == 0:
                print(f"  [{i}/{len(reference_papers)}] Expansion size: {len(expanded_set)}")

            # Get papers that cite this paper
            try:
                url = f"{self.openalex_base}/works?filter=cites:{ref_id}&per_page=200"
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    for result in data.get('results', []):
                        work_id = result.get('id')
                        citing_papers[work_id] = {
                            'doi': result.get('doi'),
                            'title': result.get('title'),
                            'cited_by': result.get('cited_by_count', 0),
                            'type': 'cites_reference'
                        }
                        expanded_set.add(work_id)

                time.sleep(0.1)

            except:
                pass

            # Get papers cited by this paper
            try:
                url = f"{self.openalex_base}/works/{ref_id}?per_page=1"
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    referenced_works = data.get('referenced_works', [])

                    for ref_work_id in referenced_works[:100]:  # Limit to first 100
                        cited_by_papers[ref_work_id] = {
                            'type': 'cited_by_reference'
                        }
                        expanded_set.add(ref_work_id)

                time.sleep(0.1)

            except:
                pass

        print(f"\n✓ Expanded set: {len(expanded_set)} total papers")
        print(f"  - Reference papers: {len(reference_papers)}")
        print(f"  - Papers citing references: {len(citing_papers)}")
        print(f"  - Papers cited by references: {len(cited_by_papers)}")

        return expanded_set, citing_papers, cited_by_papers

    def save_results(self, reference_papers, expanded_set, citing, cited):
        """Save expansion results."""
        result = {
            'metadata': {
                'strategy': 'Citation neighborhood expansion',
                'reference_papers': len(reference_papers),
                'total_expanded': len(expanded_set),
                'citing_references': len(citing),
                'cited_by_references': len(cited),
                'generated': '2026-04-01'
            },
            'reference_papers': list(reference_papers.values()),
            'expansion': {
                'citing_reference_count': len(citing),
                'cited_by_reference_count': len(cited),
                'total_doi_set': len(expanded_set)
            }
        }

        # Save
        output_file = self.output_dir / 'helmstaedter_citation_expansion.json'
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)

        print(f"\n✓ Saved: {output_file}")

        # Report
        report_file = self.output_dir / 'helmstaedter_citation_expansion_report.md'
        with open(report_file, 'w') as f:
            f.write(f"# Helmstaedter Citation Neighborhood Expansion\n\n")
            f.write(f"## Summary\n")
            f.write(f"- Reference papers (cited by Helmstaedter): {len(reference_papers)}\n")
            f.write(f"- Papers citing references: {len(citing)}\n")
            f.write(f"- Papers cited by references: {len(cited)}\n")
            f.write(f"- **Total expanded set: {len(expanded_set)}**\n\n")
            f.write(f"## Top reference papers\n\n")

            for work in sorted(reference_papers.values(), key=lambda x: -x['cited_by_count'])[:15]:
                f.write(f"- {work['title'][:80]}...\n")
                f.write(f"  Citations: {work['cited_by_count']}\n\n")

        print(f"✓ Saved: {report_file}")

    def run(self):
        """Execute."""
        reference_papers = self.lookup_reference_papers()
        expanded_set, citing, cited = self.expand_citations(reference_papers)
        self.save_results(reference_papers, expanded_set, citing, cited)

        return {
            'reference_papers': reference_papers,
            'expanded_set': expanded_set,
            'citing': citing,
            'cited': cited
        }

if __name__ == '__main__':
    expansion = HelmstaedterCitationExpansion()
    results = expansion.run()

    print("\n" + "="*80)
    print("EXPANSION COMPLETE")
    print("="*80)
    print(f"\nFinal set size: {len(results['expanded_set'])}")
    print(f"\nNext: Apply k≥25 + in-degree≥2 filtering and compare to PRIMARY corpus")
