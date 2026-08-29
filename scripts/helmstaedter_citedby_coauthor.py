#!/usr/bin/env python3
"""
Alternative approach: Instead of extracting references FROM the review,
extract papers that CITE the review + all Helmstaedter co-author network.

This gives us:
1. Papers citing the review (will cite the key connectomics work it discusses)
2. All Helmstaedter collaborators' papers
3. Co-authors' collaborators (expanding the network)
"""

import json
import requests
from pathlib import Path
from collections import defaultdict
import time

class HelmstaedterCitedByExpansion:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.openalex_base = "https://api.openalex.org"
        self.review_doi = "10.1038/s41583-025-00998-z"

    def get_review(self):
        """Fetch the Helmstaedter review."""
        print("="*80)
        print("HELMSTAEDTER REVIEW: CITED-BY + COAUTHOR EXPANSION")
        print("="*80)

        print(f"\n[STEP 1] Fetching review: {self.review_doi}")

        try:
            url = f"{self.openalex_base}/works?filter=doi:{self.review_doi}"
            response = requests.get(url, timeout=10)

            data = response.json()
            if not data.get('results'):
                print("✗ Review not found")
                return None

            review = data['results'][0]
            print(f"✓ Found: {review.get('title')[:80]}...")
            print(f"  Citations: {review.get('cited_by_count')}")

            return review

        except Exception as e:
            print(f"✗ Error: {e}")
            return None

    def get_citing_papers(self, review_id):
        """Get papers that cite the Helmstaedter review."""
        print(f"\n[STEP 2] Fetching papers that cite this review...")

        citing_papers = []

        try:
            url = f"{self.openalex_base}/works?filter=cites:{review_id}&per_page=200"

            page = 1
            while page <= 10:
                response = requests.get(url + f"&page={page}", timeout=10)

                if response.status_code != 200:
                    break

                data = response.json()
                results = data.get('results', [])

                if not results:
                    break

                citing_papers.extend(results)
                page += 1
                time.sleep(0.1)

        except Exception as e:
            print(f"✗ Error: {e}")

        print(f"✓ Found {len(citing_papers)} papers citing this review")
        return citing_papers

    def extract_authors_from_papers(self, papers, label=""):
        """Extract unique authors."""
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
                            'papers_in_set': 0
                        }

                    unique_authors[author_id]['papers_in_set'] += 1

        print(f"✓ {label}: {len(unique_authors)} unique authors")
        return unique_authors

    def harvest_papers_by_authors(self, authors_dict, label=""):
        """Harvest ALL papers by a set of authors."""
        all_papers = defaultdict(lambda: {'count': 0, 'authors': set(), 'year': 0, 'cited_by': 0})
        author_counts = {}

        print(f"\n[STEP 3.{label}] Harvesting papers by {len(authors_dict)} authors...")

        for i, (author_id, author_info) in enumerate(authors_dict.items(), 1):
            author_name = author_info['name']

            if i % 50 == 0:
                print(f"  [{i}/{len(authors_dict)}]")

            papers = []
            page = 1
            while page <= 50:
                try:
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
                    break

            author_counts[author_name] = len(papers)

            for paper in papers:
                doi = paper.get('doi', f"unknown_{i}")
                all_papers[doi]['count'] += 1
                all_papers[doi]['title'] = paper.get('title', 'Unknown')
                all_papers[doi]['year'] = paper.get('publication_year', 0)
                all_papers[doi]['cited_by'] = paper.get('cited_by_count', 0)
                all_papers[doi]['authors'].add(author_name)

        print(f"  ✓ Harvested papers")
        return all_papers, author_counts

    def run(self):
        """Execute expanded discovery."""
        # Get review
        review = self.get_review()
        if not review:
            return None

        review_id = review.get('id', '')

        # Get citing papers
        citing_papers = self.get_citing_papers(review_id)

        # Extract authors from citing papers
        citing_authors = self.extract_authors_from_papers(citing_papers, "Citing papers")

        # Harvest papers by citing authors
        citing_all_papers, citing_counts = self.harvest_papers_by_authors(citing_authors, "A")

        # Try to find Helmstaedter's own papers + collaborators
        print(f"\n[STEP 4] Finding Helmstaedter's collaborators...")

        try:
            # Search for Helmstaedter directly
            url = f"{self.openalex_base}/authors?search=Moritz%20Helmstaedter"
            response = requests.get(url, timeout=10)

            helmstaedter_authors = {}
            if response.status_code == 200:
                data = response.json()
                if data.get('results'):
                    helmstaedter_obj = data['results'][0]
                    helmstaedter_id = helmstaedter_obj.get('id')
                    print(f"✓ Found Helmstaedter: {helmstaedter_id}")

                    # Get his papers
                    papers = []
                    page = 1
                    while page <= 20:
                        url = f"{self.openalex_base}/works?filter=author.id:{helmstaedter_id}&per_page=200&page={page}"
                        r = requests.get(url, timeout=10)

                        if r.status_code != 200:
                            break

                        d = r.json()
                        results = d.get('results', [])

                        if not results:
                            break

                        papers.extend(results)
                        page += 1
                        time.sleep(0.1)

                    # Extract his co-authors
                    coauthor_set = set()
                    for paper in papers:
                        authorships = paper.get('authorships', [])
                        for auth in authorships:
                            author_obj = auth.get('author', {})
                            if author_obj.get('id'):
                                coauthor_set.add(author_obj['id'])

                    # Build author dict
                    for coauthor_id in coauthor_set:
                        helmstaedter_authors[coauthor_id] = {
                            'name': f'Helmstaedter collaborator {len(helmstaedter_authors)}',
                            'openalex_id': coauthor_id,
                            'papers_in_set': 1
                        }

                    print(f"✓ Found {len(helmstaedter_authors)} Helmstaedter collaborators")

                    # Harvest their papers
                    coauthor_papers, coauthor_counts = self.harvest_papers_by_authors(helmstaedter_authors, "B")

                    # Merge
                    for doi, data in coauthor_papers.items():
                        citing_all_papers[doi]['count'] += data['count']
                        citing_all_papers[doi]['title'] = data['title']
                        citing_all_papers[doi]['year'] = data['year']
                        citing_all_papers[doi]['cited_by'] = data['cited_by']
                        citing_all_papers[doi]['authors'].update(data['authors'])

        except Exception as e:
            print(f"⚠ Could not fetch Helmstaedter collaborators: {e}")

        return {
            'review': review,
            'citing_papers': citing_papers,
            'citing_authors': citing_authors,
            'citing_counts': citing_counts,
            'all_papers': citing_all_papers
        }

    def save_results(self, results):
        """Save results."""
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

        # Save
        papers_file = self.output_dir / 'helmstaedter_expansion_papers.json'
        with open(papers_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'Papers citing Helmstaedter review + Helmstaedter collaborators',
                    'total_papers': len(papers_list),
                    'generated': '2026-04-01'
                },
                'papers': papers_list
            }, f, indent=2)

        print(f"\n✓ Saved: {papers_file}")

        # Report
        report_file = self.output_dir / 'helmstaedter_expansion_report.md'
        with open(report_file, 'w') as f:
            f.write(f"# Helmstaedter Review Expansion\n\n")
            f.write(f"**Papers found:** {len(papers_list)}\n")
            f.write(f"**Authors cited:** {len(results['citing_authors'])}\n\n")
            f.write(f"## Top papers by citation\n\n")

            for i, paper in enumerate(papers_list[:30], 1):
                f.write(f"{i}. {paper['title'][:100]}...\n")
                f.write(f"   - Citations: {paper['cited_by_count']}, Year: {paper['year']}\n\n")

        print(f"✓ Saved: {report_file}")

if __name__ == '__main__':
    discovery = HelmstaedterCitedByExpansion()
    results = discovery.run()

    if results:
        discovery.save_results(results)

        print("\n" + "="*80)
        print("EXPANSION COMPLETE")
        print("="*80)

        all_papers = results['all_papers']
        print(f"\nTotal papers found: {len(all_papers)}")
        print(f"Total authors in citing papers: {len(results['citing_authors'])}")
