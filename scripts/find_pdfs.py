#!/usr/bin/env python3
"""
Find PDF links and open-access status for connectomics papers.
Works with 7500+ paper corpus from paper_rankings_all.json.
Outputs to JSON, CSV, and SQLite database for efficient querying.
"""

import json
import sqlite3
import csv
from pathlib import Path
import requests
import time
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import logging
from collections import defaultdict

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PDFFinder:
    def __init__(self):
        self.results = []
        self.api_delay = 0.2  # seconds between API calls (rate limiting)
        self.pmc_base = "https://www.ncbi.nlm.nih.gov/pmc/articles"
        self.biorxiv_base = "https://www.biorxiv.org/content"
        self.medrxiv_base = "https://www.medrxiv.org/content"
        self.stats = defaultdict(int)

    def load_papers(self) -> List[Dict]:
        """Load full connectomics corpus from paper_rankings_all.json."""
        papers = []
        corpus_file = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output/paper_rankings_all.json')

        if corpus_file.exists():
            with open(corpus_file) as f:
                papers = json.load(f)
            logger.info(f"Loaded {len(papers)} papers from corpus")
            with_doi = sum(1 for p in papers if p.get('doi'))
            logger.info(f"Papers with DOI: {with_doi}")
        else:
            logger.error(f"Corpus file not found: {corpus_file}")

        return papers

    def get_unpaywall_status(self, doi: str) -> Optional[Dict]:
        """Query Unpaywall API for open-access status (free, rate-limited)."""
        if not doi:
            return None

        try:
            time.sleep(self.api_delay)
            response = requests.get(
                f'https://api.unpaywall.org/v2/{doi}?email=connectomics@neurotrailblazers.org',
                timeout=5
            )

            if response.status_code == 200:
                data = response.json()
                return {
                    'is_oa': data.get('is_oa', False),
                    'oa_status': data.get('oa_status'),
                    'best_oa_url': data.get('best_oa_location', {}).get('url'),
                    'host_type': data.get('best_oa_location', {}).get('host_type')
                }
        except Exception as e:
            logger.debug(f"Unpaywall error for {doi}: {e}")

        return None

    def check_pmc(self, doi: str) -> Optional[str]:
        """Check if paper is available on PubMed Central."""
        if not doi:
            return None

        try:
            time.sleep(self.api_delay)
            response = requests.get(
                'https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/',
                params={
                    'tool': 'connectomics-rag',
                    'email': 'connectomics@neurotrailblazers.org',
                    'ids': doi,
                    'format': 'json'
                },
                timeout=5
            )

            if response.status_code == 200:
                data = response.json()
                for record in data.get('records', []):
                    if record.get('pmcid'):
                        pmcid = record['pmcid']
                        return f"{self.pmc_base}/{pmcid}/pdf/{pmcid}.pdf"
        except Exception as e:
            logger.debug(f"PMC check error for {doi}: {e}")

        return None

    def check_preprint_servers(self, doi: str) -> Optional[Tuple[str, str]]:
        """Check bioRxiv/medRxiv for preprints."""
        if not doi:
            return None

        try:
            # bioRxiv/medRxiv DOIs start with 10.1101
            if doi.startswith('10.1101'):
                doi_suffix = doi.split('10.1101/')[-1]
                pdf_url = f"{self.biorxiv_base}/10.1101/{doi_suffix}.full.pdf"
                return (pdf_url, 'biorxiv')
        except Exception as e:
            logger.debug(f"Preprint check error for {doi}: {e}")

        return None

    def process_papers(self, papers: List[Dict]) -> None:
        """Process all papers and find PDF links."""
        logger.info(f"Processing {len(papers)} papers for PDF availability...")

        for i, paper in enumerate(papers, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(papers)} ({100*i//len(papers)}%)")

            doi = paper.get('doi')
            result = {
                'doi': doi,
                'openalex_id': paper.get('openalex_id'),
                'title': paper.get('title'),
                'year': paper.get('year'),
                'authors': paper.get('authors', [])[:3],  # First 3 authors
                'pdf_links': {},
                'oa_status': None,
                'is_paywalled': None,  # True=paywalled, False=OA, None=unknown
                'notes': []
            }

            # Check preprint servers first (always open)
            if doi:
                preprint = self.check_preprint_servers(doi)
                if preprint:
                    result['pdf_links']['preprint'] = preprint[0]
                    result['is_paywalled'] = False
                    result['oa_status'] = 'preprint'
                    self.stats['preprint_found'] += 1

            # Check PubMed Central
            if doi and result['is_paywalled'] is None:
                pmc_pdf = self.check_pmc(doi)
                if pmc_pdf:
                    result['pdf_links']['pmc'] = pmc_pdf
                    result['is_paywalled'] = False
                    result['oa_status'] = 'pmc'
                    self.stats['pmc_found'] += 1

            # Check Unpaywall
            if doi:
                oa_data = self.get_unpaywall_status(doi)
                if oa_data:
                    result['oa_status'] = oa_data.get('oa_status')
                    if oa_data.get('best_oa_url'):
                        result['pdf_links']['unpaywall'] = oa_data['best_oa_url']
                        result['is_paywalled'] = False
                        self.stats['unpaywall_found'] += 1
                    if oa_data.get('is_oa') and result['is_paywalled'] is None:
                        result['is_paywalled'] = False
                    elif not oa_data.get('is_oa') and result['is_paywalled'] is None:
                        result['is_paywalled'] = True

            # Default classification
            if result['is_paywalled'] is None:
                result['is_paywalled'] = None  # Keep as unknown

            self.results.append(result)
            self.stats['total_processed'] += 1

        logger.info(f"Processing complete!")

    def save_json(self) -> Path:
        """Save results as JSON."""
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        output_dir.mkdir(parents=True, exist_ok=True)

        json_file = output_dir / 'connectomics_papers_pdf_index.json'
        with open(json_file, 'w') as f:
            json.dump({
                'metadata': {
                    'generated': datetime.now().isoformat(),
                    'total_papers': len(self.results),
                    'stats': dict(self.stats)
                },
                'papers': self.results
            }, f, indent=2)

        logger.info(f"Saved JSON to {json_file}")
        return json_file

    def save_csv(self) -> Path:
        """Save results as CSV for spreadsheet import."""
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        output_dir.mkdir(parents=True, exist_ok=True)

        csv_file = output_dir / 'connectomics_papers_pdf_index.csv'
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'doi', 'title', 'year', 'authors',
                'is_paywalled', 'oa_status',
                'preprint_link', 'pmc_link', 'unpaywall_link'
            ])
            writer.writeheader()

            for paper in self.results:
                writer.writerow({
                    'doi': paper['doi'],
                    'title': paper['title'],
                    'year': paper['year'],
                    'authors': '; '.join(paper.get('authors', [])[:3]),
                    'is_paywalled': paper['is_paywalled'],
                    'oa_status': paper['oa_status'],
                    'preprint_link': paper['pdf_links'].get('preprint', ''),
                    'pmc_link': paper['pdf_links'].get('pmc', ''),
                    'unpaywall_link': paper['pdf_links'].get('unpaywall', '')
                })

        logger.info(f"Saved CSV to {csv_file}")
        return csv_file

    def save_sqlite(self) -> Path:
        """Save results as SQLite database for efficient querying."""
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        output_dir.mkdir(parents=True, exist_ok=True)

        db_file = output_dir / 'connectomics_papers_pdf.db'

        # Remove existing database
        if db_file.exists():
            db_file.unlink()

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create tables
        cursor.execute('''
            CREATE TABLE papers (
                id INTEGER PRIMARY KEY,
                doi TEXT UNIQUE,
                openalex_id TEXT,
                title TEXT,
                year INTEGER,
                is_paywalled BOOLEAN,
                oa_status TEXT,
                first_author TEXT,
                created_at TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE pdf_links (
                id INTEGER PRIMARY KEY,
                paper_doi TEXT,
                source TEXT,
                url TEXT,
                FOREIGN KEY(paper_doi) REFERENCES papers(doi)
            )
        ''')

        cursor.execute('''
            CREATE INDEX idx_paywalled ON papers(is_paywalled);
        ''')

        cursor.execute('''
            CREATE INDEX idx_oa_status ON papers(oa_status);
        ''')

        cursor.execute('''
            CREATE INDEX idx_year ON papers(year);
        ''')

        # Insert data
        for paper in self.results:
            cursor.execute('''
                INSERT INTO papers (doi, openalex_id, title, year, is_paywalled, oa_status, first_author, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                paper['doi'],
                paper['openalex_id'],
                paper['title'],
                paper['year'],
                paper['is_paywalled'],
                paper['oa_status'],
                paper['authors'][0] if paper['authors'] else None,
                datetime.now().isoformat()
            ))

            # Insert PDF links
            for source, url in paper['pdf_links'].items():
                cursor.execute('''
                    INSERT INTO pdf_links (paper_doi, source, url)
                    VALUES (?, ?, ?)
                ''', (paper['doi'], source, url))

        conn.commit()
        conn.close()

        logger.info(f"Saved SQLite database to {db_file}")
        return db_file

    def save_markdown_summary(self) -> Path:
        """Save human-readable markdown summary."""
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        output_dir.mkdir(parents=True, exist_ok=True)

        md_file = output_dir / 'connectomics_papers_pdf_summary.md'
        with open(md_file, 'w') as f:
            f.write('# Connectomics Papers PDF Availability Index\n\n')
            f.write(f'**Generated:** {datetime.now().isoformat()}\n\n')

            # Statistics
            oa_count = sum(1 for p in self.results if p['is_paywalled'] is False)
            paywalled = sum(1 for p in self.results if p['is_paywalled'] is True)
            unknown = sum(1 for p in self.results if p['is_paywalled'] is None)

            f.write('## Summary Statistics\n\n')
            f.write('| Category | Count | Percentage |\n')
            f.write('|----------|-------|------------|\n')
            f.write(f'| Open Access (Direct Link) | {oa_count} | {100*oa_count//len(self.results)}% |\n')
            f.write(f'| Behind Paywall | {paywalled} | {100*paywalled//len(self.results)}% |\n')
            f.write(f'| Unknown Status | {unknown} | {100*unknown//len(self.results)}% |\n')
            f.write(f'| **Total** | **{len(self.results)}** | **100%** |\n\n')

            # OA Breakdown
            f.write('## Open Access Breakdown\n\n')
            oa_sources = defaultdict(int)
            for p in self.results:
                if p['oa_status']:
                    oa_sources[p['oa_status']] += 1

            for source, count in sorted(oa_sources.items(), key=lambda x: x[1], reverse=True):
                f.write(f'- **{source}**: {count} papers\n')

            f.write('\n## Top Papers (by citations)\n\n')
            f.write('| Title | Year | DOI | Paywall |\n')
            f.write('|-------|------|-----|---------|\n')

            for i, paper in enumerate(self.results[:50], 1):
                if len(paper['title']) > 80:
                    title = paper['title'][:77] + '...'
                else:
                    title = paper['title']
                paywall_status = 'OA' if paper['is_paywalled'] is False else 'Paywalled' if paper['is_paywalled'] else '?'
                f.write(f'| {title} | {paper["year"]} | `{paper["doi"]}` | {paywall_status} |\n')

            f.write('\n## How to Use\n\n')
            f.write('- **JSON format** (`connectomics_papers_pdf_index.json`): For programmatic access\n')
            f.write('- **CSV format** (`connectomics_papers_pdf_index.csv`): For spreadsheet import\n')
            f.write('- **SQLite database** (`connectomics_papers_pdf.db`): For efficient queries\n\n')

            f.write('### Example SQLite Queries\n\n')
            f.write('```sql\n')
            f.write('-- Find all open-access papers\n')
            f.write('SELECT title, year, oa_status FROM papers WHERE is_paywalled = 0;\n\n')
            f.write('-- Count papers by OA status\n')
            f.write('SELECT oa_status, COUNT(*) FROM papers GROUP BY oa_status;\n\n')
            f.write('-- Find papers from specific year\n')
            f.write('SELECT title, oa_status FROM papers WHERE year = 2020;\n')
            f.write('```\n')

        logger.info(f"Saved summary to {md_file}")
        return md_file

def main():
    finder = PDFFinder()

    logger.info("=" * 60)
    logger.info("Connectomics Papers PDF Availability Indexer")
    logger.info("=" * 60)

    papers = finder.load_papers()
    if not papers:
        logger.error("No papers loaded!")
        return

    finder.process_papers(papers)

    logger.info("\nGenerating outputs...")
    finder.save_json()
    finder.save_csv()
    finder.save_sqlite()
    finder.save_markdown_summary()

    logger.info("\n" + "=" * 60)
    logger.info("Statistics:")
    logger.info("=" * 60)
    for key, value in sorted(finder.stats.items()):
        logger.info(f"  {key}: {value}")

    logger.info("\nDone!")

if __name__ == '__main__':
    main()
