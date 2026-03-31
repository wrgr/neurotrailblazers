#!/usr/bin/env python3
"""
Step 9: Deduplicate preprint/journal versions of same papers.

Identifies papers that are:
1. ArXiv preprints with matching journal articles
2. Conference papers with matching arXiv preprints
3. Multiple versions of the same work

Strategy:
- Keep published journal version (highest authority)
- Remove arXiv if journal exists
- Remove conference preprint if journal exists
- Merge citations counts where applicable

Input:  output/corpus_merged.json
Output: output/corpus_deduplicated.json, output/dedup_log.json
"""
import json
from pathlib import Path
from collections import defaultdict
import difflib

OUTPUT_DIR = Path("output")


def load_corpus():
    with open(OUTPUT_DIR / "corpus_merged.json") as f:
        return json.load(f)


def similarity(s1, s2):
    """Compute string similarity (0-1)."""
    return difflib.SequenceMatcher(None, s1.lower(), s2.lower()).ratio()


def find_duplicates(corpus):
    """
    Find potential duplicate papers using multiple strategies.
    Returns: list of duplicate groups
    """
    duplicates = []

    # Strategy 1: Group by normalized title
    title_groups = defaultdict(list)
    for i, paper in enumerate(corpus):
        # Normalize title: lowercase, remove special chars, trim
        title = paper.get('title', '').lower().strip()
        title_norm = ''.join(c for c in title if c.isalnum() or c.isspace())
        title_norm = ' '.join(title_norm.split())  # Remove extra spaces
        if title_norm:
            title_groups[title_norm].append(i)

    # Find groups with same title (potential duplicates)
    for title_norm, indices in title_groups.items():
        if len(indices) > 1:
            group = [corpus[i] for i in indices]
            duplicates.append(group)

    # Strategy 2: Similar titles by same authors in adjacent years
    for i, paper1 in enumerate(corpus):
        if i % 100 == 0:
            print(f"  Comparing paper {i}/{len(corpus)}...")

        authors1 = set(a.get('id', '') for a in paper1.get('authors', []))
        year1 = paper1.get('year', 0)

        for j in range(i + 1, min(i + 50, len(corpus))):  # Only check nearby papers
            paper2 = corpus[j]
            authors2 = set(a.get('id', '') for a in paper2.get('authors', []))
            year2 = paper2.get('year', 0)

            # Same/overlapping authors within 2 years
            overlap = len(authors1 & authors2)
            if overlap >= 3 and abs(year1 - year2) <= 2:
                # Check title similarity
                title_sim = similarity(paper1.get('title', ''), paper2.get('title', ''))
                if title_sim > 0.7:
                    # Likely duplicates
                    type1 = paper1.get('type', '').lower()
                    type2 = paper2.get('type', '').lower()
                    # Only flag if one is preprint or conference
                    if any(t in [type1, type2] for t in ['preprint', 'conference']):
                        duplicates.append([paper1, paper2])

    return duplicates


def choose_canonical(group):
    """
    Choose the canonical version of a paper group.
    Priority: journal article > conference > preprint
    If same type: prefer higher citation count or more recent
    """
    type_priority = {
        'article': 0,
        'journal-article': 0,
        'conference': 1,
        'posted-content': 1,
        'preprint': 2,
    }

    def sort_key(p):
        ptype = p.get('type', '').lower()
        priority = type_priority.get(ptype, 10)
        citations = -p.get('cited_by_count', 0)  # Higher cites better
        year = -p.get('year', 0)  # More recent better
        return (priority, citations, year)

    return sorted(group, key=sort_key)[0]


def merge_papers(canonical, duplicates):
    """
    Merge duplicate papers into canonical version.
    Keeps canonical but aggregates citation information.
    """
    total_citations = canonical.get('cited_by_count', 0)
    for dup in duplicates:
        total_citations += dup.get('cited_by_count', 0)

    # Use the maximum (they should cite the same work)
    canonical['cited_by_count'] = max(
        canonical.get('cited_by_count', 0),
        max(d.get('cited_by_count', 0) for d in duplicates)
    )

    # Note merged versions
    canonical['merged_versions'] = [
        {
            'doi': dup.get('doi'),
            'year': dup.get('year'),
            'type': dup.get('type'),
            'citations': dup.get('cited_by_count')
        }
        for dup in duplicates
    ]

    return canonical


def main():
    print("Loading corpus...")
    corpus = load_corpus()
    print(f"  {len(corpus)} papers\n")

    print("Finding duplicate papers...")
    dup_groups = find_duplicates(corpus)
    print(f"  Found {len(dup_groups)} potential duplicate groups\n")

    # Process duplicates
    papers_to_remove = set()
    dedup_log = []

    for group in dup_groups:
        if len(group) < 2:
            continue

        canonical = choose_canonical(group)
        duplicates = [p for p in group if p != canonical]

        # Record in log
        dedup_log.append({
            'canonical': {
                'doi': canonical.get('doi'),
                'year': canonical.get('year'),
                'title': canonical.get('title')[:80],
                'type': canonical.get('type'),
                'citations': canonical.get('cited_by_count')
            },
            'removed': [
                {
                    'doi': d.get('doi'),
                    'year': d.get('year'),
                    'type': d.get('type'),
                    'citations': d.get('cited_by_count')
                }
                for d in duplicates
            ]
        })

        # Mark for removal
        for dup in duplicates:
            papers_to_remove.add(dup.get('openalex_id'))

        # Merge into canonical
        merge_papers(canonical, duplicates)

    # Filter corpus
    print(f"Removing {len(papers_to_remove)} duplicate papers...")
    corpus_dedup = [p for p in corpus if p.get('openalex_id') not in papers_to_remove]

    # Save
    with open(OUTPUT_DIR / "corpus_deduplicated.json", "w") as f:
        json.dump(corpus_dedup, f, indent=2)

    with open(OUTPUT_DIR / "dedup_log.json", "w") as f:
        json.dump(dedup_log, f, indent=2)

    print(f"\nDeduplication complete:")
    print(f"  Original: {len(corpus)} papers")
    print(f"  After:    {len(corpus_dedup)} papers")
    print(f"  Removed:  {len(papers_to_remove)} duplicates")
    print(f"  Saved dedup log: dedup_log.json")


if __name__ == "__main__":
    main()
