#!/usr/bin/env python3
"""
Fast PDF indexer using smart heuristics and cached data.
Avoids slow API calls where possible.
"""

import json
import sqlite3
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class FastPDFIndexer:
    def __init__(self):
        self.results = []
        self.stats = defaultdict(int)

        # Known open-access publishers/platforms
        self.oa_indicators = {
            'biorxiv': False,  # Preprint = OA
            'medrxiv': False,
            'arxiv': False,
            'plos': False,
            'elife': False,
            'frontiers': False,
            'nature communications': False,
            'scientific reports': False,
        }

        # Known paywalled journals
        self.paywall_journals = {
            'nature', 'science', 'cell', 'neuron', 'neuroscience',
            'journal of neuroscience', 'brain', 'cortex'
        }

    def load_papers(self):
        """Load corpus."""
        corpus_file = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output/paper_rankings_all.json')
        with open(corpus_file) as f:
            papers = json.load(f)
        logger.info(f"Loaded {len(papers)} papers")
        return papers

    def classify_paper(self, paper):
        """Classify paper based on heuristics."""
        result = {
            'doi': paper.get('doi'),
            'title': paper.get('title'),
            'year': paper.get('year'),
            'authors': paper.get('authors', [])[:3],
            'openalex_id': paper.get('openalex_id'),
            'pdf_sources': [],
            'is_paywalled': None,
            'oa_status': None
        }

        doi = paper.get('doi', '')
        title = (paper.get('title') or '').lower()
        journal = (paper.get('journal') or '').lower() if 'journal' in paper else ''

        # Check for preprints first
        if '10.1101' in doi:
            result['pdf_sources'].append({
                'source': 'biorxiv',
                'url': f'https://www.biorxiv.org/content/10.1101/{doi.split("10.1101/")[1]}.full.pdf'
            })
            result['is_paywalled'] = False
            result['oa_status'] = 'preprint'
            self.stats['preprint_identified'] += 1
            return result

        # Check for known OA journals
        for oa_journal in self.oa_indicators:
            if oa_journal in journal:
                result['is_paywalled'] = False
                result['oa_status'] = 'oa_journal'
                self.stats['oa_journal_identified'] += 1
                return result

        # Check for known paywalled journals
        for paywall_journal in self.paywall_journals:
            if paywall_journal in journal:
                result['is_paywalled'] = True
                result['oa_status'] = 'likely_paywalled'
                self.stats['paywall_journal_identified'] += 1
                return result

        # Default to unknown
        result['is_paywalled'] = None
        self.stats['unknown_status'] += 1
        return result

    def process_papers(self, papers):
        """Process all papers with fast heuristics."""
        logger.info(f"Processing {len(papers)} papers...")

        for i, paper in enumerate(papers, 1):
            if i % 500 == 0:
                logger.info(f"Progress: {i}/{len(papers)}")

            self.results.append(self.classify_paper(paper))
            self.stats['total_processed'] += 1

        logger.info("Processing complete!")

    def save_json(self):
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

        logger.info(f"Saved JSON: {json_file}")
        return json_file

    def save_csv(self):
        """Save as CSV."""
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        output_dir.mkdir(parents=True, exist_ok=True)

        csv_file = output_dir / 'connectomics_papers_pdf_index.csv'
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'doi', 'title', 'year', 'is_paywalled', 'oa_status', 'primary_source'
            ])
            writer.writeheader()

            for paper in self.results:
                writer.writerow({
                    'doi': paper['doi'],
                    'title': paper['title'],
                    'year': paper['year'],
                    'is_paywalled': paper['is_paywalled'],
                    'oa_status': paper['oa_status'],
                    'primary_source': paper['pdf_sources'][0]['source'] if paper['pdf_sources'] else ''
                })

        logger.info(f"Saved CSV: {csv_file}")
        return csv_file

    def save_sqlite(self):
        """Save as SQLite."""
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        output_dir.mkdir(parents=True, exist_ok=True)

        db_file = output_dir / 'connectomics_papers_pdf.db'
        if db_file.exists():
            db_file.unlink()

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE papers (
                id INTEGER PRIMARY KEY,
                doi TEXT UNIQUE,
                title TEXT,
                year INTEGER,
                is_paywalled BOOLEAN,
                oa_status TEXT,
                created_at TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE INDEX idx_paywalled ON papers(is_paywalled);
        ''')

        cursor.execute('''
            CREATE INDEX idx_oa_status ON papers(oa_status);
        ''')

        for paper in self.results:
            try:
                cursor.execute('''
                    INSERT INTO papers (doi, title, year, is_paywalled, oa_status, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    paper['doi'],
                    paper['title'],
                    paper['year'],
                    paper['is_paywalled'],
                    paper['oa_status'],
                    datetime.now().isoformat()
                ))
            except sqlite3.IntegrityError:
                # Skip duplicate DOIs
                pass

        conn.commit()
        conn.close()

        logger.info(f"Saved SQLite: {db_file}")
        return db_file

    def save_summary(self):
        """Save markdown summary."""
        output_dir = Path('/home/user/neurotrailblazers/scripts/bibliometrics/output')
        output_dir.mkdir(parents=True, exist_ok=True)

        md_file = output_dir / 'connectomics_papers_pdf_summary.md'
        with open(md_file, 'w') as f:
            f.write('# Connectomics Papers PDF Availability Index\n\n')
            f.write(f'Generated: {datetime.now().isoformat()}\n\n')

            oa = sum(1 for p in self.results if p['is_paywalled'] is False)
            paywalled = sum(1 for p in self.results if p['is_paywalled'] is True)
            unknown = sum(1 for p in self.results if p['is_paywalled'] is None)

            f.write('## Statistics\n\n')
            f.write(f'- Open Access: {oa} ({100*oa//len(self.results)}%)\n')
            f.write(f'- Paywalled: {paywalled} ({100*paywalled//len(self.results)}%)\n')
            f.write(f'- Unknown: {unknown} ({100*unknown//len(self.results)}%)\n')
            f.write(f'- **Total: {len(self.results)}**\n\n')

            f.write('## OA By Type\n\n')
            for key, count in sorted(self.stats.items(), key=lambda x: x[1], reverse=True):
                if 'identified' in key:
                    f.write(f'- {key}: {count}\n')

        logger.info(f"Saved summary: {md_file}")
        return md_file

def main():
    indexer = FastPDFIndexer()
    papers = indexer.load_papers()
    indexer.process_papers(papers)
    indexer.save_json()
    indexer.save_csv()
    indexer.save_sqlite()
    indexer.save_summary()

    logger.info("\n" + "="*60)
    logger.info("RESULTS")
    logger.info("="*60)
    for key, val in sorted(indexer.stats.items()):
        logger.info(f"{key}: {val}")

if __name__ == '__main__':
    main()
