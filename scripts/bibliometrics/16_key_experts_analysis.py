#!/usr/bin/env python3
"""
Identify key experts and their important work.

Combines:
1. Top authors by paper count
2. Their highest-scoring papers (composite_score)
3. Paper roles (landmark, foundational, infrastructure, etc.)
4. Strategic seed list enrichment opportunities
"""
import json
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path("output")


def main():
    print("Loading data...")
    with open(OUTPUT_DIR / "corpus_final.json") as f:
        corpus = json.load(f)
    with open(OUTPUT_DIR / "paper_rankings_all.json") as f:
        rankings = {p['openalex_id']: p for p in json.load(f)}
    with open(OUTPUT_DIR / "author_rankings.json") as f:
        author_rankings = json.load(f)
    with open(OUTPUT_DIR / "paper_role_analysis.json") as f:
        roles = {p['openalex_id']: p for p in json.load(f)}

    # Build corpus lookup
    corpus_by_id = {p['openalex_id']: p for p in corpus}

    # Key experts: Top 50 authors
    key_authors = author_rankings[:50]

    print(f"\nAnalyzing top {len(key_authors)} experts...\n")

    expert_analysis = []

    for author in key_authors:
        author_name = author['name']
        paper_count = author.get('paper_count', 0)
        co_author_count = author.get('co_author_count', 0)

        # Find all papers by this author
        author_papers = []
        for paper in corpus:
            paper_authors = [a.get('name', '') for a in paper.get('authors', [])]
            if author_name in paper_authors:
                pid = paper['openalex_id']
                ranking = rankings.get(pid, {})
                role = roles.get(pid, {})

                author_papers.append({
                    'openalex_id': pid,
                    'title': paper.get('title', ''),
                    'year': paper.get('year', 0),
                    'citations': paper.get('cited_by_count', 0),
                    'composite_score': ranking.get('composite_score', 0),
                    'role': role.get('inferred_role', 'unknown'),
                    'in_degree': role.get('in_degree', 0),
                    'out_degree': role.get('out_degree', 0),
                })

        # Sort by composite score
        author_papers.sort(key=lambda p: p['composite_score'], reverse=True)

        # Categorize papers by role
        role_summary = defaultdict(int)
        for p in author_papers:
            role_summary[p['role']] += 1

        # Top papers
        top_papers = author_papers[:10]

        # Identify important papers (>0.5 composite score OR landmark role)
        important_papers = [
            p for p in author_papers
            if p['composite_score'] > 0.5 or
            p['role'].startswith('landmark') or
            p['role'] == 'foundational'
        ]

        # Review/synthesis papers
        synthesis_papers = [
            p for p in author_papers
            if p['role'] in ['synthesis_integration', 'methods_infrastructure']
        ]

        expert_analysis.append({
            'rank': author.get('rank', 0),
            'name': author_name,
            'paper_count': paper_count,
            'co_author_count': co_author_count,
            'collaborative_reach': author.get('composite_score', 0),
            'total_papers': len(author_papers),
            'role_distribution': dict(role_summary),
            'important_papers_count': len(important_papers),
            'synthesis_papers_count': len(synthesis_papers),
            'top_papers': [
                {
                    'title': p['title'][:80],
                    'year': p['year'],
                    'role': p['role'],
                    'score': round(p['composite_score'], 4),
                    'citations': p['citations'],
                }
                for p in top_papers
            ],
            'important_papers': [
                {
                    'title': p['title'][:80],
                    'year': p['year'],
                    'role': p['role'],
                    'score': round(p['composite_score'], 4),
                    'citations': p['citations'],
                }
                for p in sorted(important_papers, key=lambda x: -x['composite_score'])[:5]
            ],
        })

    # Save analysis
    with open(OUTPUT_DIR / "key_experts_analysis.json", "w") as f:
        json.dump(expert_analysis, f, indent=2)

    print("✓ Saved: key_experts_analysis.json\n")

    # Print summary
    print("=" * 80)
    print("KEY EXPERTS AND THEIR IMPORTANT WORK")
    print("=" * 80)

    for expert in expert_analysis[:10]:
        print(f"\n#{expert['rank']} {expert['name']}")
        print(f"  Papers: {expert['total_papers']} total, {expert['important_papers_count']} important")
        print(f"  Roles distribution: {expert['role_distribution']}")
        print(f"  Top papers:")
        for p in expert['important_papers'][:3]:
            print(f"    • {p['title']} ({p['year']}, {p['role']})")

    print("\n" + "=" * 80)
    print("STRATEGIC ENRICHMENT OPPORTUNITIES")
    print("=" * 80)
    print("\nKey experts with synthesis/infrastructure papers (potential reviews):")
    synthesis_experts = [
        e for e in expert_analysis if e['synthesis_papers_count'] > 0
    ]
    for expert in synthesis_experts[:15]:
        print(f"  {expert['name']:30s} ({expert['synthesis_papers_count']} synthesis/infrastructure papers)")

    print("\nKey experts with important landmark papers:")
    for expert in expert_analysis[:10]:
        important = expert['important_papers_count']
        if important > 0:
            print(f"  {expert['name']:30s} ({important} important papers: landmarks/foundational)")


if __name__ == "__main__":
    main()
