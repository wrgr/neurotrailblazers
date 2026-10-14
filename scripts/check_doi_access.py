#!/usr/bin/env python3
"""
Try to access the 1667 papers without direct links.
Check if DOI links are accessible or redirect to free versions.
"""

import json
import requests
from pathlib import Path
from collections import defaultdict
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class DOIChecker:
    def __init__(self, workers=10):
        self.workers = workers
        self.stats = defaultdict(int)
        self.found_papers = []

    def load_papers(self):
        """Load papers without direct links."""
        json_file = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output/connectomics_papers_pdf_index.json')
        with open(json_file) as f:
            data = json.load(f)

        papers = data['papers']
        no_link_papers = [p for p in papers if not p['pdf_sources'] and p['doi']]
        return no_link_papers

    def check_doi_url(self, paper):
        """Try to access DOI and follow redirects to find PDF."""
        doi = paper['doi']

        try:
            # Try direct DOI resolution with Accept: application/pdf header
            headers = {
                'Accept': 'application/pdf',
                'User-Agent': 'Mozilla/5.0 (compatible; connectomics-rag)'
            }

            response = requests.head(
                f'https://doi.org/{doi}',
                headers=headers,
                timeout=5,
                allow_redirects=True
            )

            # Check if it redirected to a PDF or HTML page
            if response.status_code == 200:
                content_type = response.headers.get('content-type', '')
                final_url = response.url

                # Try to get PDF if it's HTML
                if 'text/html' in content_type:
                    # Try common patterns for full text links
                    try:
                        r = requests.get(final_url, timeout=5)
                        if r.status_code == 200:
                            html = r.text
                            # Look for PDF links in the page
                            if '.pdf' in html.lower() or 'pdf' in html.lower():
                                return {
                                    'doi': doi,
                                    'status': 'html_with_pdf_link',
                                    'url': final_url,
                                    'title': paper['title']
                                }
                    except:
                        pass

                elif 'application/pdf' in content_type:
                    return {
                        'doi': doi,
                        'status': 'direct_pdf',
                        'url': final_url,
                        'title': paper['title']
                    }

                return {
                    'doi': doi,
                    'status': 'accessible_html',
                    'url': final_url,
                    'title': paper['title']
                }

            elif response.status_code == 403 or response.status_code == 401:
                return {
                    'doi': doi,
                    'status': 'forbidden',
                    'title': paper['title']
                }

            elif response.status_code == 404:
                return {
                    'doi': doi,
                    'status': 'not_found',
                    'title': paper['title']
                }

            else:
                return {
                    'doi': doi,
                    'status': f'http_{response.status_code}',
                    'title': paper['title']
                }

        except requests.Timeout:
            self.stats['timeout'] += 1
        except Exception as e:
            self.stats['error'] += 1

        return None

    def check_papers_parallel(self, papers):
        """Check papers in parallel."""
        logger.info(f"Checking {len(papers)} papers without direct links...")

        results = defaultdict(list)
        completed = 0

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {executor.submit(self.check_doi_url, p): p['doi'] for p in papers}

            for future in as_completed(futures):
                completed += 1
                if completed % 100 == 0:
                    logger.info(f"Progress: {completed}/{len(papers)}")

                result = future.result()
                if result:
                    status = result['status']
                    results[status].append(result)
                    self.stats[status] += 1

        return results

    def run(self):
        """Run the checker."""
        logger.info("="*70)
        logger.info("DOI Accessibility Checker")
        logger.info("="*70)

        papers = self.load_papers()
        logger.info(f"Loaded {len(papers)} papers without direct links but with DOIs")

        # Check DOIs
        results = self.check_papers_parallel(papers)

        # Report
        logger.info("\n" + "="*70)
        logger.info("RESULTS")
        logger.info("="*70)

        for status in sorted(results.keys(), key=lambda x: len(results[x]), reverse=True):
            count = len(results[status])
            logger.info(f"\n{status}: {count} papers")

        # Show direct PDFs found
        if results.get('direct_pdf'):
            logger.info(f"\n🎉 Found {len(results['direct_pdf'])} papers with direct PDF access!")
            for paper in results['direct_pdf'][:5]:
                logger.info(f"  - {paper['title'][:60]}...")
                logger.info(f"    URL: {paper['url']}")

        # Show accessible HTML
        if results.get('accessible_html'):
            logger.info(f"\n📄 Found {len(results['accessible_html'])} papers with accessible HTML pages")

        # Show HTML with PDF links
        if results.get('html_with_pdf_link'):
            logger.info(f"\n🔗 Found {len(results['html_with_pdf_link'])} papers with PDF links on HTML page")

        # Save results to file
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        output_file = output_dir / 'doi_accessibility_check.json'

        with open(output_file, 'w') as f:
            json.dump({
                'timestamp': str(time.time()),
                'total_checked': sum(len(v) for v in results.values()),
                'results': {k: v for k, v in results.items()}
            }, f, indent=2)

        logger.info(f"\nSaved detailed results to: {output_file}")

if __name__ == '__main__':
    checker = DOIChecker(workers=15)
    checker.run()
