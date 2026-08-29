#!/usr/bin/env python3
"""
Check PubMed Central availability for papers using NIH ID conversion service.
Much faster than Unpaywall - uses batch API.
"""

import json
import requests
import time
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class PMCChecker:
    def __init__(self):
        self.pmc_base = "https://www.ncbi.nlm.nih.gov/pmc/articles"
        self.stats = defaultdict(int)

    def load_papers(self):
        """Load papers from the existing index."""
        json_file = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output/connectomics_papers_pdf_index.json')
        with open(json_file) as f:
            data = json.load(f)
        return data['papers']

    def check_pmc_batch(self, dois, batch_size=200):
        """Check PMC availability using NIH ID conversion service (batch mode)."""
        results = {}

        for i in range(0, len(dois), batch_size):
            batch = dois[i:i+batch_size]
            doi_str = ','.join(batch)

            try:
                time.sleep(0.1)  # Small delay between batches
                response = requests.get(
                    'https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/',
                    params={
                        'tool': 'connectomics-rag',
                        'email': 'connectomics@neurotrailblazers.org',
                        'ids': doi_str,
                        'format': 'json'
                    },
                    timeout=10
                )

                if response.status_code == 200:
                    data = response.json()
                    for record in data.get('records', []):
                        doi = record.get('doi')
                        pmcid = record.get('pmcid')

                        if doi and pmcid:
                            pdf_url = f"{self.pmc_base}/{pmcid}/pdf/{pmcid}.pdf"
                            results[doi] = {
                                'pmcid': pmcid,
                                'pdf_url': pdf_url,
                                'source': 'pmc'
                            }
                            self.stats['pmc_found'] += 1
                        elif doi:
                            self.stats['doi_not_in_pmc'] += 1

                if (i + batch_size) % 1000 == 0:
                    logger.info(f"Processed {min(i + batch_size, len(dois))}/{len(dois)} DOIs")

            except Exception as e:
                logger.warning(f"Error processing batch: {e}")
                self.stats['api_errors'] += 1

        return results

    def update_index(self, papers, pmc_results):
        """Update papers with PMC URLs."""
        updated = 0

        for paper in papers:
            doi = paper.get('doi')
            if doi in pmc_results:
                pmc_info = pmc_results[doi]
                paper['pdf_sources'].append({
                    'source': 'pmc',
                    'url': pmc_info['pdf_url']
                })
                paper['is_paywalled'] = False
                paper['oa_status'] = 'pmc'
                updated += 1

        return updated

    def save_updated_index(self, papers):
        """Save updated index."""
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        json_file = output_dir / 'connectomics_papers_pdf_index.json'

        with open(json_file, 'w') as f:
            json.dump({
                'metadata': {
                    'generated': datetime.now().isoformat(),
                    'total_papers': len(papers),
                    'stats': dict(self.stats)
                },
                'papers': papers
            }, f, indent=2)

        logger.info(f"Updated JSON: {json_file}")

    def run(self):
        """Run the PMC checker."""
        logger.info("="*60)
        logger.info("PubMed Central Availability Checker")
        logger.info("="*60)

        papers = self.load_papers()
        logger.info(f"Loaded {len(papers)} papers")

        # Extract DOIs
        dois = [p['doi'] for p in papers if p['doi']]
        logger.info(f"Checking {len(dois)} papers with DOIs against PMC...")

        # Check PMC
        pmc_results = self.check_pmc_batch(dois)
        logger.info(f"Found {len(pmc_results)} papers in PMC")

        # Update index
        updated = self.update_index(papers, pmc_results)
        logger.info(f"Updated {updated} papers with PMC URLs")

        # Save
        self.save_updated_index(papers)

        # Stats
        logger.info("\n" + "="*60)
        logger.info("RESULTS")
        logger.info("="*60)
        for key, val in sorted(self.stats.items()):
            logger.info(f"  {key}: {val}")

        # Count totals
        oa_count = sum(1 for p in papers if p['is_paywalled'] is False)
        logger.info(f"\nTotal Open Access: {oa_count} ({100*oa_count//len(papers)}%)")

if __name__ == '__main__':
    checker = PMCChecker()
    checker.run()
