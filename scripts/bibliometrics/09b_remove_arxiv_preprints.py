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

    # Filter corpus
    corpus_filtered = [p for i, p in enumerate(corpus) if i not in arxiv_to_remove]

    print(f"\nResults:")
    print(f"  Original: {len(corpus)}")
    print(f"  Removed:  {len(arxiv_to_remove)} arXiv preprints")
    print(f"  Final:    {len(corpus_filtered)}")

    # Save
    with open(OUTPUT_DIR / "corpus_final.json", "w") as f:
        json.dump(corpus_filtered, f, indent=2)

    # Log removals
    with open(OUTPUT_DIR / "arxiv_removal_log.json", "w") as f:
        removed_papers = [corpus[i] for i in arxiv_to_remove]
        json.dump([
            {
                'doi': p.get('doi'),
                'year': p.get('year'),
                'title': p.get('title')[:100],
                'type': p.get('type')
            }
            for p in removed_papers
        ], f, indent=2)


if __name__ == "__main__":
    main()
