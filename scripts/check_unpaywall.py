#!/usr/bin/env python3
"""
Check Unpaywall for all papers without direct links.
Unpaywall aggregates from institutional repos, author archives, etc.
"""

import json
import requests
import time
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class UnpaywallChecker:
    def __init__(self, workers=5):
        self.workers = workers
        self.stats = defaultdict(int)

    def load_papers(self):
        """Load papers from the existing index."""
        json_file = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output/connectomics_papers_pdf_index.json')
        with open(json_file) as f:
            data = json.load(f)
        return data['papers']

    def check_unpaywall(self, doi):
        """Check single DOI on Unpaywall."""
        if not doi:
            return None

        try:
            response = requests.get(
                f'https://api.unpaywall.org/v2/{doi}?email=connectomics@neurotrailblazers.org',
                timeout=5
            )

            if response.status_code == 200:
                data = response.json()
                if data.get('is_oa') and data.get('best_oa_location'):
                    location = data['best_oa_location']
                    return {
                        'doi': doi,
                        'is_oa': True,
                        'oa_status': data.get('oa_status'),
                        'host_type': location.get('host_type'),
                        'pdf_url': location.get('url'),
                        'source': location.get('endpoint')
                    }
                elif data.get('is_oa'):
                    return {
                        'doi': doi,
                        'is_oa': True,
                        'oa_status': data.get('oa_status'),
                        'note': 'OA but no direct PDF URL'
                    }
        except Exception as e:
            logger.debug(f"Unpaywall error for {doi}: {e}")

        return None

    def check_papers_parallel(self, papers):
        """Check papers in parallel."""
        # Filter papers that don't already have links
        papers_to_check = [p for p in papers if not p['pdf_sources']]
        dois = [p['doi'] for p in papers_to_check if p['doi']]

        logger.info(f"Checking {len(dois)} papers without links on Unpaywall...")

        results = {}
        completed = 0

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {executor.submit(self.check_unpaywall, doi): doi for doi in dois}

            for future in as_completed(futures):
                completed += 1
                if completed % 100 == 0:
                    logger.info(f"Progress: {completed}/{len(dois)}")

                result = future.result()
                if result:
                    results[result['doi']] = result
                    self.stats['unpaywall_found'] += 1

        return results

    def update_papers(self, papers, unpaywall_results):
        """Update papers with Unpaywall results."""
        updated = 0

        for paper in papers:
            doi = paper.get('doi')
            if doi in unpaywall_results:
                result = unpaywall_results[doi]
                if result.get('pdf_url'):
                    paper['pdf_sources'].append({
                        'source': f"unpaywall-{result.get('host_type', 'unknown')}",
                        'url': result['pdf_url']
                    })
                    paper['is_paywalled'] = False
                    paper['oa_status'] = result.get('oa_status', 'unpaywall')
                    updated += 1
                elif result.get('is_oa'):
                    # OA but no direct link - still record it
                    paper['is_paywalled'] = False
                    paper['oa_status'] = result.get('oa_status', 'unpaywall-no-link')

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
        """Run the checker."""
        logger.info("="*60)
        logger.info("Unpaywall Availability Checker")
        logger.info("="*60)

        papers = self.load_papers()
        logger.info(f"Loaded {len(papers)} papers")

        # Check Unpaywall
        unpaywall_results = self.check_papers_parallel(papers)
        logger.info(f"Found {len(unpaywall_results)} papers on Unpaywall")

        # Update
        updated = self.update_papers(papers, unpaywall_results)
        logger.info(f"Updated {updated} papers with Unpaywall links")

        # Save
        self.save_updated_index(papers)

        # Stats
        with_links = sum(1 for p in papers if p['pdf_sources'])
        without_links = len(papers) - with_links

        logger.info("\n" + "="*60)
        logger.info("RESULTS")
        logger.info("="*60)
        logger.info(f"Papers with PDF links: {with_links} ({100*with_links//len(papers)}%)")
        logger.info(f"Papers without links: {without_links} ({100*without_links//len(papers)}%)")
        logger.info(f"Unpaywall found: {self.stats['unpaywall_found']}")

if __name__ == '__main__':
    checker = UnpaywallChecker(workers=8)
    checker.run()
