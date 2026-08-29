#!/usr/bin/env python3
"""
Anchor-based discovery: Extract ALL authors from landmark papers,
harvest ALL their papers from OpenAlex.

Landmark papers (Nature Method of Year 2025):
- FlyWire papers (Dorkenwald, Schlegel, etc.)
- MICrONS paper (Collman, Seung, Tolias, etc.)

Output: Complete bibliography of all authors in these landmark collaborations
"""

import json
import requests
from pathlib import Path
from collections import defaultdict
import time

class AnchorAuthorExpansion:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.openalex_base = "https://api.openalex.org"

        # Known landmark paper DOIs
        self.landmark_dois = [
            '10.1038/s41586-024-07558-x',  # FlyWire main - Dorkenwald
            '10.1038/s41592-025-02906-w',  # FlyWire Method of Year
            '10.1038/s41586-025-08790-w',  # MICrONS - Collman
        ]

    def get_paper_authors_from_openalex(self, doi):
        """Fetch complete author list from OpenAlex for a landmark paper."""
        print(f"\n  Fetching authors for {doi}...")

        try:
            # Query OpenAlex by DOI
            url = f"{self.openalex_base}/works?filter=doi:{doi}"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                print(f"    ✗ Not found in OpenAlex")
                return []

            data = response.json()
            if not data.get('results'):
                print(f"    ✗ No results")
                return []

            paper = data['results'][0]
            authors = paper.get('authorships', [])

            author_list = []
            for auth in authors:
                author_obj = auth.get('author', {})
                if author_obj:
                    author_list.append({
                        'name': author_obj.get('display_name'),
                        'openalex_id': author_obj.get('id'),
                        'orcid': author_obj.get('orcid')
                    })

            print(f"    ✓ Found {len(author_list)} authors")
            return author_list

        except Exception as e:
            print(f"    ✗ Error: {e}")
            return []

    def harvest_author_papers(self, openalex_author_id, author_name, per_page=200):
        """Get ALL papers by an author from OpenAlex."""
        papers = []
        page = 1
        max_pages = 50  # Safety limit

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
                time.sleep(0.1)  # Rate limiting

        except Exception as e:
            print(f"    ✗ Error harvesting {author_name}: {e}")

        return papers

    def run_discovery(self):
        """Execute anchor-based discovery."""
        print("="*80)
        print("ANCHOR-BASED DISCOVERY: FlyWire + MICrONS")
        print("="*80)

        all_authors = {}  # author_id -> {name, papers_count}
        all_papers = defaultdict(lambda: {'count': 0, 'authors': set()})

        # Phase 1: Extract authors from landmark papers
        print("\n[PHASE 1] Extracting authors from landmark papers...")

        landmark_authors = []
        for doi in self.landmark_dois:
            authors = self.get_paper_authors_from_openalex(doi)
            landmark_authors.extend(authors)

        unique_authors = {}
        for author in landmark_authors:
            author_id = author['openalex_id']
            if author_id not in unique_authors:
                unique_authors[author_id] = author

        print(f"\n✓ Total unique authors from landmarks: {len(unique_authors)}")

        # Phase 2: Harvest all papers by these authors
        print("\n[PHASE 2] Harvesting ALL papers by landmark authors...")
        print(f"This may take a minute... requesting papers for {len(unique_authors)} authors\n")

        author_paper_counts = {}

        for i, (author_id, author_info) in enumerate(unique_authors.items(), 1):
            author_name = author_info.get('name', 'Unknown')

            if i % 10 == 0:
                print(f"  [{i}/{len(unique_authors)}] {author_name}")

            papers = self.harvest_author_papers(author_id, author_name)
            author_paper_counts[author_name] = len(papers)

            # Track papers
            for paper in papers:
                doi = paper.get('doi', 'unknown')
                all_papers[doi]['count'] += 1
                all_papers[doi]['title'] = paper.get('title')
                all_papers[doi]['year'] = paper.get('year')
                all_papers[doi]['cited_by_count'] = paper.get('cited_by_count', 0)
                all_papers[doi]['authors'].add(author_name)

        print(f"\n✓ Harvesting complete")

        return {
            'unique_authors': unique_authors,
            'author_paper_counts': author_paper_counts,
            'all_papers': all_papers
        }

    def save_results(self, results):
        """Save discovery results."""
        unique_authors = results['unique_authors']
        author_paper_counts = results['author_paper_counts']
        all_papers = results['all_papers']

        # Convert papers dict to list for JSON
        papers_list = []
        for doi, data in all_papers.items():
            papers_list.append({
                'doi': doi,
                'title': data['title'],
                'year': data['year'],
                'cited_by_count': data['cited_by_count'],
                'by_authors_count': data['count'],
                'authors_in_corpus': list(data['authors'])
            })

        # Sort by citation count
        papers_list.sort(key=lambda x: -x['cited_by_count'])

        # Save author list
        authors_file = self.output_dir / 'anchor_discovery_authors.json'
        with open(authors_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'FlyWire + MICrONS landmark papers',
                    'total_unique_authors': len(unique_authors),
                    'generated': '2026-04-01'
                },
                'authors': list(unique_authors.values())
            }, f, indent=2)
        print(f"✓ Saved: {authors_file} ({len(unique_authors)} authors)")

        # Save all papers
        papers_file = self.output_dir / 'anchor_discovery_papers.json'
        with open(papers_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'ALL papers by landmark authors',
                    'total_papers': len(papers_list),
                    'total_author_instances': sum(p['by_authors_count'] for p in papers_list),
                    'generated': '2026-04-01'
                },
                'papers': papers_list
            }, f, indent=2)
        print(f"✓ Saved: {papers_file} ({len(papers_list)} unique papers)")

        # Save summary report
        report_file = self.output_dir / 'anchor_discovery_report.md'
        with open(report_file, 'w') as f:
            f.write(self.generate_report(unique_authors, author_paper_counts, papers_list))
        print(f"✓ Saved: {report_file}")

    def generate_report(self, authors, author_counts, papers_list):
        """Generate discovery report."""
        lines = []

        lines.append("# Anchor-Based Discovery Report\n")
        lines.append("**Landmark Papers:** FlyWire + MICrONS (Nature Method of Year 2025)\n")

        lines.append(f"\n## Summary\n")
        lines.append(f"**Total unique landmark authors:** {len(authors)}")
        lines.append(f"**Total unique papers harvested:** {len(papers_list)}")
        lines.append(f"**Total papers across all instances:** {sum(author_counts.values())}\n")

        # Top authors by paper count
        lines.append(f"\n## Top Authors by Publication Count\n")
        sorted_authors = sorted(author_counts.items(), key=lambda x: -x[1])

        for i, (name, count) in enumerate(sorted_authors[:30], 1):
            lines.append(f"{i}. **{name}**: {count} papers")

        # Top papers by citation count
        lines.append(f"\n## Top Papers by Citation Count\n")

        for i, paper in enumerate(papers_list[:30], 1):
            authors_str = ', '.join(paper['authors_in_corpus'][:2])
            if len(paper['authors_in_corpus']) > 2:
                authors_str += f", +{len(paper['authors_in_corpus'])-2} more"

            lines.append(f"\n{i}. **{paper['title'][:80]}...**")
            lines.append(f"   - Year: {paper['year']}")
            lines.append(f"   - Citations: {paper['cited_by_count']}")
            lines.append(f"   - By authors: {authors_str}")

        return "\n".join(lines)

if __name__ == '__main__':
    discovery = AnchorAuthorExpansion()
    results = discovery.run_discovery()
    discovery.save_results(results)

    print("\n" + "="*80)
    print("DISCOVERY COMPLETE")
    print("="*80)

    # Show top results
    sorted_authors = sorted(results['author_paper_counts'].items(), key=lambda x: -x[1])
    print("\nTop 15 authors by paper count:")
    for i, (name, count) in enumerate(sorted_authors[:15], 1):
        print(f"  {i}. {name}: {count} papers")
