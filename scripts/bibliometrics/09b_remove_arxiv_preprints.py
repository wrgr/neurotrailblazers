#!/usr/bin/env python3
"""
Remove arXiv preprints when published versions exist.

Priority for keeping:
1. Journal articles
2. Conference papers
3. ArXiv preprints (remove these if published version exists)

For papers with matching DOI/OpenAlex ID patterns, keep the published version.
"""
import json
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path("output")


def main():
    # Load deduplicated corpus
    with open(OUTPUT_DIR / "corpus_deduplicated.json") as f:
        corpus = json.load(f)

    print(f"Starting with {len(corpus)} papers")

    # Group by OpenAlex ID to find versions
    openalex_groups = defaultdict(list)
    for i, paper in enumerate(corpus):
        oa_id = paper.get('openalex_id', '')
        if oa_id:
            openalex_groups[oa_id].append(i)

    # Find arXiv papers that have published counterparts
    arxiv_to_remove = set()

    # Strategy 1: Remove arXiv if same OpenAlex ID exists in published form
    for oa_id, indices in openalex_groups.items():
        if len(indices) > 1:
            papers = [corpus[i] for i in indices]
            arxiv_papers = [p for p in papers if p.get('type', '').lower() in ['preprint', 'posted-content']]
            published = [p for p in papers if p.get('type', '').lower() in ['article', 'journal-article', 'conference']]

            if arxiv_papers and published:
                # Remove arXiv versions
                for arxiv in arxiv_papers:
                    arxiv_to_remove.add(corpus.index(arxiv))

    # Strategy 2: Explicitly match known duplicates by DOI patterns
    # ArXiv DOIs start with 10.48550/arxiv
    # Look for matching conference/journal papers

    arxiv_papers = {}
    for i, paper in enumerate(corpus):
        doi = paper.get('doi', '')
        if 'arxiv' in doi.lower():
            arxiv_papers[i] = paper

    # For each arXiv paper, look for published version with similar metadata
    for arxiv_idx, arxiv_paper in arxiv_papers.items():
        arxiv_title = arxiv_paper.get('title', '').lower()
        arxiv_authors = set(a.get('id', '') for a in arxiv_paper.get('authors', []))
        arxiv_year = arxiv_paper.get('year', 0)

        for i, candidate in enumerate(corpus):
            if i == arxiv_idx:
                continue

            ctype = candidate.get('type', '').lower()
            if ctype in ['preprint', 'posted-content']:
                continue  # Only match against published

            candidate_title = candidate.get('title', '').lower()
            candidate_authors = set(a.get('id', '') for a in candidate.get('authors', []))
            candidate_year = candidate.get('year', 0)

            # Check if likely same paper
            if arxiv_title in candidate_title or candidate_title in arxiv_title:
                # Check author overlap (at least 50% overlap)
                overlap = len(arxiv_authors & candidate_authors)
                min_authors = min(len(arxiv_authors), len(candidate_authors))
                if min_authors > 0 and overlap / min_authors >= 0.5:
                    # Check year (within 1 year)
                    if abs(arxiv_year - candidate_year) <= 1:
                        # Mark arXiv for removal
                        arxiv_to_remove.add(arxiv_idx)
                        print(f"  Removing arXiv: {arxiv_paper.get('title')[:60]}...")
                        print(f"    Keeping: {candidate.get('type')} {candidate_year}")
                        break

    # Merge citations from removed arXiv into published versions
    # Create a mapping of removed arXiv indices to their published versions
    arxiv_merges = {}

    # For papers marked to remove, find their corresponding published version and merge citations
    for arxiv_idx in arxiv_to_remove:
        arxiv_paper = corpus[arxiv_idx]
        arxiv_title = arxiv_paper.get('title', '').lower()
        arxiv_authors = set(a.get('id', '') for a in arxiv_paper.get('authors', []))
        arxiv_year = arxiv_paper.get('year', 0)

        # Find the published version
        for i, candidate in enumerate(corpus):
            if i == arxiv_idx or i in arxiv_to_remove:
                continue

            ctype = candidate.get('type', '').lower()
            if ctype in ['preprint', 'posted-content']:
                continue

            candidate_title = candidate.get('title', '').lower()
            candidate_authors = set(a.get('id', '') for a in candidate.get('authors', []))
            candidate_year = candidate.get('year', 0)

            if arxiv_title in candidate_title or candidate_title in arxiv_title:
                overlap = len(arxiv_authors & candidate_authors)
                min_authors = min(len(arxiv_authors), len(candidate_authors))
                if min_authors > 0 and overlap / min_authors >= 0.5:
                    if abs(arxiv_year - candidate_year) <= 1:
                        # Merge: add arXiv citations to published version
                        arxiv_merges[arxiv_idx] = {
                            'published_idx': i,
                            'arxiv_cites': arxiv_paper.get('cited_by_count', 0)
                        }
                        # Add to the published version
                        if 'merged_versions' not in candidate:
                            candidate['merged_versions'] = []
                        candidate['merged_versions'].append({
                            'doi': arxiv_paper.get('doi'),
                            'year': arxiv_year,
                            'type': 'preprint',
                            'citations': arxiv_paper.get('cited_by_count', 0)
                        })
                        candidate['cited_by_count'] = candidate.get('cited_by_count', 0) + arxiv_paper.get('cited_by_count', 0)
                        break

    # Filter corpus (remove arXiv versions)
    corpus_filtered = [p for i, p in enumerate(corpus) if i not in arxiv_to_remove]

    print(f"\nResults:")
    print(f"  Original: {len(corpus)}")
    print(f"  Merged:   {len(arxiv_to_remove)} arXiv preprints into published versions")
    print(f"  Final:    {len(corpus_filtered)}")

    # Log merges
    merge_log = []
    for arxiv_idx, merge_info in arxiv_merges.items():
        arxiv_paper = corpus[arxiv_idx]
        published_idx = merge_info['published_idx']
        published_paper = corpus[published_idx]

        merge_log.append({
            'removed_arxiv': {
                'doi': arxiv_paper.get('doi'),
                'year': arxiv_paper.get('year'),
                'title': arxiv_paper.get('title')[:100],
                'citations': arxiv_paper.get('cited_by_count')
            },
            'merged_into': {
                'doi': published_paper.get('doi'),
                'year': published_paper.get('year'),
                'type': published_paper.get('type'),
                'new_total_citations': published_paper.get('cited_by_count')
            }
        })

    with open(OUTPUT_DIR / "arxiv_merge_log.json", "w") as f:
        json.dump(merge_log, f, indent=2)

    # Save
    with open(OUTPUT_DIR / "corpus_final.json", "w") as f:
        json.dump(corpus_filtered, f, indent=2)


if __name__ == "__main__":
    main()
