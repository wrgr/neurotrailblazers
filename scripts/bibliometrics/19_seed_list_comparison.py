#!/usr/bin/env python3
"""
Compare seed list (journal_club_final_strict.json) against current corpus.

Identifies:
1. Papers in seed list already in corpus
2. Papers missing from corpus
3. Papers in corpus not in seed list
4. Enrichment opportunities by key experts
"""
import json
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path("output")


def main():
    print("Loading data...")

    # Load seed list
    with open(OUTPUT_DIR / "journal_club_final_strict.json") as f:
        seed_list = json.load(f)

    # Load corpus
    with open(OUTPUT_DIR / "corpus_final.json") as f:
        corpus = json.load(f)

    # Load key experts
    with open(OUTPUT_DIR / "key_experts_analysis.json") as f:
        experts = json.load(f)

    # Load paper role analysis
    with open(OUTPUT_DIR / "paper_role_analysis.json") as f:
        roles_by_id = {p['openalex_id']: p for p in json.load(f)}

    # Build corpus lookups
    corpus_by_title_lower = {}
    corpus_by_doi_lower = {}
    corpus_ids = set()

    for paper in corpus:
        pid = paper['openalex_id']
        corpus_ids.add(pid)

        title_lower = paper.get('title', '').lower()
        if title_lower:
            corpus_by_title_lower[title_lower] = pid

        doi = paper.get('doi', '')
        if doi:
            corpus_by_doi_lower[doi.lower()] = pid

    print(f"Corpus: {len(corpus)} papers")
    print(f"Seed list: {len(seed_list)} papers\n")

    # Analyze seed list
    seed_in_corpus = []
    seed_missing = []

    for paper in seed_list:
        title_lower = paper.get('title', '').lower()
        doi = paper.get('doi', '').lower() if paper.get('doi') else ''

        # Try to find in corpus
        found = False
        corpus_id = None

        # Try by DOI first (most reliable)
        if doi and doi in corpus_by_doi_lower:
            corpus_id = corpus_by_doi_lower[doi]
            found = True
        # Try by title
        elif title_lower and title_lower in corpus_by_title_lower:
            corpus_id = corpus_by_title_lower[title_lower]
            found = True

        if found:
            seed_in_corpus.append({
                'title': paper.get('title', '')[:80],
                'year': paper.get('year', 0),
                'tier': paper.get('tier', 'unknown'),
                'openalex_id': corpus_id,
            })
        else:
            seed_missing.append({
                'title': paper.get('title', '')[:80],
                'year': paper.get('year', 0),
                'tier': paper.get('tier', 'unknown'),
                'doi': paper.get('doi', ''),
            })

    print("=" * 80)
    print("SEED LIST COMPARISON")
    print("=" * 80)
    print(f"\nIn corpus: {len(seed_in_corpus)} / {len(seed_list)} papers ({100*len(seed_in_corpus)/len(seed_list):.1f}%)")
    print(f"Missing: {len(seed_missing)} papers\n")

    if seed_missing:
        print("Missing from corpus (should be added):")
        for p in seed_missing:
            print(f"  • {p['title']} ({p['year']})")
            if p['doi']:
                print(f"    DOI: {p['doi']}")
    else:
        print("✓ All seed list papers are in corpus!")

    # Analyze seed list in corpus
    print(f"\n\nSeed list papers in corpus by tier:")
    tier_counts = defaultdict(int)
    for p in seed_in_corpus:
        tier_counts[p['tier']] += 1

    for tier in ['platinum', 'gold', 'silver', 'bronze']:
        count = tier_counts.get(tier, 0)
        print(f"  {tier:10s}: {count:3d} papers")

    # Check which seed papers are authored by key experts
    print(f"\n\nKey expert representation in seed list:")
    expert_papers = defaultdict(list)

    for seed_paper in seed_in_corpus:
        corpus_paper = next((p for p in corpus if p['openalex_id'] == seed_paper['openalex_id']), None)
        if corpus_paper:
            authors = [a.get('name', '') for a in corpus_paper.get('authors', [])]

            for expert in experts[:20]:  # Top 20 experts
                if expert['name'] in authors:
                    expert_papers[expert['name']].append(seed_paper['title'])

    for expert_name in sorted(expert_papers.keys(), key=lambda x: -len(expert_papers[x])):
        count = len(expert_papers[expert_name])
        print(f"  {expert_name:30s}: {count} papers")

    # Flagged decisions
    enrichment_log = {
        'comparison_date': '2026-03-31',
        'seed_list': 'journal_club_final_strict.json',
        'corpus_size': len(corpus),
        'seed_in_corpus': len(seed_in_corpus),
        'seed_missing': len(seed_missing),
        'coverage': f"{100*len(seed_in_corpus)/len(seed_list):.1f}%",
        'missing_papers': [
            {
                'title': p['title'],
                'year': p['year'],
                'tier': p['tier'],
                'doi': p.get('doi', ''),
                'action': 'ADD_TO_CORPUS',
                'confidence': 1.0,
                'justification': 'In user seed list (journal_club_final_strict)',
                'decision': 'PENDING'
            }
            for p in seed_missing
        ]
    }

    # Save log
    with open(OUTPUT_DIR / "seed_list_comparison.json", "w") as f:
        json.dump(enrichment_log, f, indent=2)

    print(f"\n✓ Saved seed_list_comparison.json")

    # Summary
    print(f"\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Seed list coverage: {len(seed_in_corpus)}/{len(seed_list)} papers in corpus")
    if len(seed_missing) > 0:
        print(f"\n⚠ {len(seed_missing)} papers to add from seed list")
        print("  These should be added with confidence=1.0 (high priority)")
    else:
        print(f"\n✓ Excellent: All seed list papers already in corpus!")
        print("  No enrichment needed from seed list.")


if __name__ == "__main__":
    main()
