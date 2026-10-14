#!/usr/bin/env python3
"""
Anchor-based discovery from Helmstaedter 2026 review:
"Synaptic-resolution connectomics: towards large brains and connectomic screening"

Strategy:
1. Get the review paper from OpenAlex (DOI: 10.1038/s41583-025-00998-z)
2. Extract ALL authors it cites/references
3. Harvest ALL papers by those authors
4. Keep separate from existing 7,925-paper corpus
"""

import json
import requests
from pathlib import Path
from collections import defaultdict
import time

class HelmstaedterReviewExpansion:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.openalex_base = "https://api.openalex.org"
        self.review_doi = "10.1038/s41583-025-00998-z"

    def get_review_and_references(self):
        """Fetch the review paper and extract all referenced authors."""
        print("="*80)
        print("HELMSTAEDTER REVIEW EXPANSION (Nature Rev Neuroscience 2026)")
        print("="*80)

        print(f"\n[STEP 1] Fetching review paper: {self.review_doi}")

        try:
            url = f"{self.openalex_base}/works?filter=doi:{self.review_doi}"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                print(f"✗ Paper not found in OpenAlex")
                return None

            data = response.json()
            if not data.get('results'):
                print(f"✗ No results")
                return None

            review = data['results'][0]
            print(f"✓ Found review by {review.get('display_name', 'Unknown')}")
            print(f"  Title: {review.get('title')[:80]}...")
            print(f"  Citation count: {review.get('cited_by_count')}")

            return review

        except Exception as e:
            print(f"✗ Error: {e}")
            return None

    def get_cited_references(self, review_work_id):
        """Get all papers cited by the review."""
        print(f"\n[STEP 2] Extracting all cited references...")

        cited_works = []

        try:
            # OpenAlex tracks cited_by relationships - get works that cite THIS review
            # Also get the works THIS review cites through relationships
            url = f"{self.openalex_base}/works?filter=referenced_works:{review_work_id}&per_page=200"

            page = 1
            while page <= 10:  # Max 2000 references
                response = requests.get(url + f"&page={page}", timeout=10)

                if response.status_code != 200:
                    break

                data = response.json()
                results = data.get('results', [])

                if not results:
                    break

                cited_works.extend(results)
                page += 1
                time.sleep(0.1)

        except Exception as e:
            print(f"✗ Error fetching references: {e}")

        print(f"✓ Found {len(cited_works)} referenced papers")
        return cited_works

    def extract_authors_from_papers(self, papers):
        """Extract unique authors from a set of papers."""
        print(f"\n[STEP 3] Extracting all unique authors from cited papers...")

        unique_authors = {}

        for i, paper in enumerate(papers):
            if i % 100 == 0 and i > 0:
                print(f"  Processed {i}/{len(papers)} papers...")

            authorships = paper.get('authorships', [])

            for auth in authorships:
                author_obj = auth.get('author', {})
                if author_obj and author_obj.get('id'):
                    author_id = author_obj['id']

                    if author_id not in unique_authors:
                        unique_authors[author_id] = {
                            'name': author_obj.get('display_name', 'Unknown'),
                            'openalex_id': author_id,
                            'orcid': author_obj.get('orcid'),
                            'papers_in_review': 0
                        }

                    unique_authors[author_id]['papers_in_review'] += 1

        print(f"✓ Found {len(unique_authors)} unique authors")
        return unique_authors

    def harvest_author_papers(self, openalex_author_id, author_name, per_page=200):
        """Get ALL papers by an author."""
        papers = []
        page = 1
        max_pages = 50

        try:
            while page <= max_pages:
                url = f"{self.openalex_base}/works?filter=author.id:{openalex_author_id}&per_page={per_page}&page={page}"
                response = requests.get(url, timeout=10)

                if response.status_code != 200:
                    break

                data = response.json()
                results = data.get('results', [])

                if not results:
                    break

                for result in results:
                    papers.append({
                        'doi': result.get('doi', 'N/A'),
                        'title': result.get('title', 'Unknown'),
                        'year': result.get('publication_year'),
                        'cited_by_count': result.get('cited_by_count', 0),
                        'openalex_id': result.get('id')
                    })

                page += 1
                time.sleep(0.05)

        except Exception as e:
            pass

        return papers

    def run_discovery(self):
        """Execute full discovery."""
        # Step 1: Get review
        review = self.get_review_and_references()
        if not review:
            return None

        # Step 2: Get referenced papers
        review_work_id = review.get('id', '')
        cited_papers = self.get_cited_references(review_work_id)

        # Step 3: Extract all unique authors
        all_authors = self.extract_authors_from_papers(cited_papers)

        print(f"\n[STEP 4] Harvesting ALL papers by {len(all_authors)} authors...")
        print(f"(This may take 2-3 minutes...)\n")

        all_papers = defaultdict(lambda: {'count': 0, 'authors': set(), 'year': 0, 'cited_by': 0})
        author_paper_counts = {}

        for i, (author_id, author_info) in enumerate(all_authors.items(), 1):
            author_name = author_info.get('name', 'Unknown')

            if i % 50 == 0:
                print(f"  [{i}/{len(all_authors)}] {author_name}")

            papers = self.harvest_author_papers(author_id, author_name)
            author_paper_counts[author_name] = len(papers)

            for paper in papers:
                doi = paper.get('doi', f"unknown_{i}")
                all_papers[doi]['count'] += 1
                all_papers[doi]['title'] = paper.get('title')
                all_papers[doi]['year'] = paper.get('year', 0)
                all_papers[doi]['cited_by'] = paper.get('cited_by_count', 0)
                all_papers[doi]['authors'].add(author_name)

        print(f"\n✓ Harvesting complete")

        return {
            'review': review,
            'cited_papers': cited_papers,
            'unique_authors': all_authors,
            'author_paper_counts': author_paper_counts,
            'all_papers': all_papers
        }

    def save_results(self, results):
        """Save discovery results."""
        unique_authors = results['unique_authors']
        author_counts = results['author_paper_counts']
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
                'authors_in_helmstaedter': list(data['authors'])
            })

        papers_list.sort(key=lambda x: -x['cited_by_count'])

        # Save authors
        authors_file = self.output_dir / 'helmstaedter_review_authors.json'
        with open(authors_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'Helmstaedter 2026 review (Nature Rev Neuroscience)',
                    'total_unique_authors': len(unique_authors),
                    'review_doi': '10.1038/s41583-025-00998-z',
                    'generated': '2026-04-01'
                },
                'authors': list(unique_authors.values())
            }, f, indent=2)
        print(f"✓ Saved: {authors_file}")

        # Save papers
        papers_file = self.output_dir / 'helmstaedter_review_papers.json'
        with open(papers_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'ALL papers by authors cited in Helmstaedter 2026 review',
                    'total_papers': len(papers_list),
                    'total_author_instances': sum(p['by_authors_count'] for p in papers_list),
                    'generated': '2026-04-01'
                },
                'papers': papers_list
            }, f, indent=2)
        print(f"✓ Saved: {papers_file} ({len(papers_list)} papers)")

        # Save report
        report_file = self.output_dir / 'helmstaedter_review_report.md'
        with open(report_file, 'w') as f:
            f.write(self.generate_report(unique_authors, author_counts, papers_list))
        print(f"✓ Saved: {report_file}")

    def generate_report(self, authors, author_counts, papers_list):
        """Generate report."""
        lines = []

        lines.append("# Helmstaedter Review Expansion Report\n")
        lines.append("**Review:** 'Synaptic-resolution connectomics: towards large brains and connectomic screening'\n")
        lines.append("**Author:** Moritz Helmstaedter | **Journal:** Nature Reviews Neuroscience | **Date:** Feb 2026\n")
        lines.append("**DOI:** 10.1038/s41583-025-00998-z\n")

        lines.append(f"\n## Summary\n")
        lines.append(f"**Total authors in review:** {len(authors)}")
        lines.append(f"**Total papers harvested:** {len(papers_list)}")
        lines.append(f"**Total paper-author instances:** {sum(author_counts.values())}\n")

        lines.append(f"\n## Top Authors by Paper Count\n")
        sorted_authors = sorted(author_counts.items(), key=lambda x: -x[1])

        for i, (name, count) in enumerate(sorted_authors[:30], 1):
            lines.append(f"{i}. {name}: {count} papers")

        lines.append(f"\n## Top Papers by Citation Count\n")

        for i, paper in enumerate(papers_list[:30], 1):
            lines.append(f"\n{i}. **{paper['title'][:80]}**")
            lines.append(f"   - Year: {paper['year']}")
            lines.append(f"   - Citations: {paper['cited_by_count']}")
            if paper['authors_in_helmstaedter']:
                authors_str = ', '.join(list(paper['authors_in_helmstaedter'])[:2])
                lines.append(f"   - Authors: {authors_str}")

        return "\n".join(lines)

if __name__ == '__main__':
    discovery = HelmstaedterReviewExpansion()
    results = discovery.run_discovery()

    if results:
        discovery.save_results(results)

        print("\n" + "="*80)
        print("DISCOVERY COMPLETE")
        print("="*80)

        sorted_authors = sorted(results['author_paper_counts'].items(), key=lambda x: -x[1])
        print(f"\nTotal authors found: {len(sorted_authors)}")
        print("\nTop 15 most prolific:")
        for i, (name, count) in enumerate(sorted_authors[:15], 1):
            print(f"  {i}. {name}: {count} papers")
