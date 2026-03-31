#!/usr/bin/env python3
"""
Analyze career arcs of key experts.

Shows:
1. Publication trajectory (papers per year)
2. Citation impact over time
3. Collaboration evolution
4. Role transitions (methodological → applied, etc.)
"""
import json
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path("output")


def main():
    print("Loading data...")
    with open(OUTPUT_DIR / "corpus_final.json") as f:
        corpus = json.load(f)
    with open(OUTPUT_DIR / "key_experts_analysis.json") as f:
        experts = json.load(f)
    with open(OUTPUT_DIR / "paper_role_analysis.json") as f:
        roles_by_id = {p['openalex_id']: p for p in json.load(f)}

    # Build corpus lookup
    corpus_by_id = {p['openalex_id']: p for p in corpus}

    # Select key experts for detailed career analysis
    career_experts = experts[:15]  # Top 15

    print(f"Analyzing career arcs for {len(career_experts)} experts...\n")

    career_arcs = []

    for expert in career_experts:
        name = expert['name']
        papers = []

        # Find all papers by this expert
        for paper in corpus:
            paper_authors = [a.get('name', '') for a in paper.get('authors', [])]
            if name in paper_authors:
                pid = paper['openalex_id']
                role = roles_by_id.get(pid, {})

                papers.append({
                    'year': paper.get('year', 0),
                    'title': paper.get('title', ''),
                    'citations': paper.get('cited_by_count', 0),
                    'role': role.get('inferred_role', 'unknown'),
                    'authors_count': len(paper_authors),
                })

        if not papers:
            continue

        # Sort by year
        papers.sort(key=lambda p: p['year'])

        # Build year-by-year trajectory
        timeline = defaultdict(lambda: {
            'paper_count': 0,
            'total_citations': 0,
            'avg_citations': 0,
            'collaborators': 0,
            'roles': defaultdict(int)
        })

        for p in papers:
            year = p['year']
            if year < 1970 or year > 2026:  # Filter invalid years
                continue

            timeline[year]['paper_count'] += 1
            timeline[year]['total_citations'] += p['citations']
            timeline[year]['collaborators'] += p['authors_count']
            timeline[year]['roles'][p['role']] += 1

        # Calculate averages
        for year in timeline:
            count = timeline[year]['paper_count']
            timeline[year]['avg_citations'] = timeline[year]['total_citations'] / count

        # Convert to sorted list
        timeline_list = [
            {
                'year': year,
                'papers': timeline[year]['paper_count'],
                'total_citations': timeline[year]['total_citations'],
                'avg_citations_per_paper': round(timeline[year]['avg_citations'], 1),
                'avg_collaborators_per_paper': round(timeline[year]['collaborators'] / timeline[year]['paper_count'], 1),
                'roles': dict(timeline[year]['roles']),
            }
            for year in sorted(timeline.keys())
        ]

        # Identify career phases
        early_years = [t for t in timeline_list if t['year'] < 2005]
        mid_years = [t for t in timeline_list if 2005 <= t['year'] < 2015]
        recent_years = [t for t in timeline_list if t['year'] >= 2015]

        career_arc = {
            'rank': expert['rank'],
            'name': name,
            'total_papers': len(papers),
            'total_citations': sum(p['citations'] for p in papers),
            'first_year': papers[0]['year'] if papers else 0,
            'last_year': papers[-1]['year'] if papers else 0,
            'career_span_years': (papers[-1]['year'] if papers else 0) - (papers[0]['year'] if papers else 0),
            'timeline': timeline_list,
            'career_phases': {
                'early': {
                    'years': f"{early_years[0]['year']}-{early_years[-1]['year']}" if early_years else "N/A",
                    'papers': sum(t['papers'] for t in early_years),
                    'avg_citations': round(sum(t['total_citations'] for t in early_years) / max(1, sum(t['papers'] for t in early_years)), 1)
                } if early_years else None,
                'mid': {
                    'years': f"{mid_years[0]['year']}-{mid_years[-1]['year']}" if mid_years else "N/A",
                    'papers': sum(t['papers'] for t in mid_years),
                    'avg_citations': round(sum(t['total_citations'] for t in mid_years) / max(1, sum(t['papers'] for t in mid_years)), 1)
                } if mid_years else None,
                'recent': {
                    'years': f"{recent_years[0]['year']}-{recent_years[-1]['year']}" if recent_years else "N/A",
                    'papers': sum(t['papers'] for t in recent_years),
                    'avg_citations': round(sum(t['total_citations'] for t in recent_years) / max(1, sum(t['papers'] for t in recent_years)), 1)
                } if recent_years else None,
            },
            'top_papers': [
                {
                    'title': p['title'][:70],
                    'year': p['year'],
                    'citations': p['citations'],
                    'role': p['role']
                }
                for p in sorted(papers, key=lambda x: -x['citations'])[:5]
            ]
        }

        career_arcs.append(career_arc)

    # Save career arcs
    with open(OUTPUT_DIR / "career_arcs.json", "w") as f:
        json.dump(career_arcs, f, indent=2)

    print(f"✓ Saved career_arcs.json\n")

    # Print summaries
    print("=" * 80)
    print("CAREER ARC ANALYSIS — TOP EXPERTS")
    print("=" * 80)

    for arc in career_arcs[:10]:
        print(f"\n#{arc['rank']} {arc['name']}")
        print(f"  Papers: {arc['total_papers']} total")
        print(f"  Career span: {arc['first_year']}-{arc['last_year']} ({arc['career_span_years']} years)")
        print(f"  Total citations: {arc['total_citations']}")

        if arc['career_phases']['early']:
            print(f"  • Early ({arc['career_phases']['early']['years']}): "
                  f"{arc['career_phases']['early']['papers']} papers, "
                  f"{arc['career_phases']['early']['avg_citations']:.0f} cites/paper")
        if arc['career_phases']['mid']:
            print(f"  • Mid ({arc['career_phases']['mid']['years']}): "
                  f"{arc['career_phases']['mid']['papers']} papers, "
                  f"{arc['career_phases']['mid']['avg_citations']:.0f} cites/paper")
        if arc['career_phases']['recent']:
            print(f"  • Recent ({arc['career_phases']['recent']['years']}): "
                  f"{arc['career_phases']['recent']['papers']} papers, "
                  f"{arc['career_phases']['recent']['avg_citations']:.0f} cites/paper")

        print(f"  Top papers:")
        for p in arc['top_papers'][:3]:
            print(f"    - {p['title']} ({p['year']}, {p['citations']} cites)")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
