#!/usr/bin/env python3
"""
Analyze synthesis/review papers from key experts.

Extracts references and identifies missing papers with justification.
Framework: Only add papers cited by 2+ expert reviews, with confidence >0.5
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
    with open(OUTPUT_DIR / "graphs" / "citation_graph.json") as f:
        citation_graph = json.load(f)

    # Build DOI/title lookup for corpus
    corpus_by_doi = {}
    corpus_by_title_lower = {}
    corpus_ids = set()

    for paper in corpus:
        pid = paper['openalex_id']
        corpus_ids.add(pid)
        if paper.get('doi'):
            corpus_by_doi[paper['doi'].lower()] = pid
        title_lower = paper.get('title', '').lower()
        if title_lower:
            corpus_by_title_lower[title_lower] = pid

    # Key synthesis experts and their synthesis papers
    SYNTHESIS_EXPERTS = {
        'Olaf Sporns': 26,
        'Danielle S. Bassett': 29,
        'Edward T. Bullmore': 19,
    }

    # Find their synthesis papers
    synthesis_paper_list = []
    for expert in experts:
        if expert['name'] in SYNTHESIS_EXPERTS:
            synthesis_paper_list.extend(expert['important_papers'])

    print(f"\nKey synthesis experts: {list(SYNTHESIS_EXPERTS.keys())}")
    print(f"Total synthesis papers to analyze: {len(synthesis_paper_list)}")

    # Get outgoing edges from these papers (what they cite)
    synthesis_citations = defaultdict(int)  # cited_paper_id → count
    synthesis_by_expert = defaultdict(list)

    edges = citation_graph.get('links', [])

    # Build lookup: title → node ID in graph
    nodes = {n['id']: n for n in citation_graph.get('nodes', [])}

    print("\nExtracting references from synthesis papers...")
    for edge in edges:
        source_id = edge.get('source')
        target_id = edge.get('target')

        # Check if source is one of our synthesis papers
        source_node = nodes.get(source_id, {})
        if source_node.get('title', '').lower() in corpus_by_title_lower:
            synthesis_citations[target_id] += 1

    print(f"Found {len(synthesis_citations)} papers cited by synthesis papers\n")

    # Identify missing papers (cited by synthesis experts but not in corpus)
    missing_candidates = []
    for paper_id, citation_count in synthesis_citations.items():
        if paper_id not in corpus_ids:
            node = nodes.get(paper_id, {})
            missing_candidates.append({
                'openalex_id': paper_id,
                'title': node.get('title', 'Unknown'),
                'year': node.get('year', 0),
                'cited_by_synthesis_papers': citation_count,
                'confidence': min(1.0, citation_count / 3.0)  # 3 synthesis experts = 1.0 confidence
            })

    # Sort by citation count
    missing_candidates.sort(key=lambda x: -x['cited_by_synthesis_papers'])

    # Filter: only those cited by 2+ synthesis papers, confidence >0.5
    enrichment_candidates = [
        p for p in missing_candidates
        if p['cited_by_synthesis_papers'] >= 2 and p['confidence'] > 0.5
    ]

    print("=" * 80)
    print("ENRICHMENT CANDIDATES (Cited by 2+ synthesis papers, confidence >0.5)")
    print("=" * 80)
    print(f"\nTotal candidates: {len(enrichment_candidates)}\n")

    enrichment_flagged = []
    for candidate in enrichment_candidates[:50]:  # Top 50
        judgement = {
            'openalex_id': candidate['openalex_id'],
            'title': candidate['title'][:80],
            'year': candidate['year'],
            'cited_by_synthesis_papers': candidate['cited_by_synthesis_papers'],
            'confidence': round(candidate['confidence'], 3),
            'justification': f"Referenced by {candidate['cited_by_synthesis_papers']} expert synthesis papers",
            'action': 'FLAGGED_FOR_REVIEW',
            'decision': None  # To be filled in by manual review
        }
        enrichment_flagged.append(judgement)
        print(f"✓ {candidate['title'][:70]}")
        print(f"  Year: {candidate['year']}, Cited by: {candidate['cited_by_synthesis_papers']} reviews")
        print(f"  Confidence: {candidate['confidence']:.3f}\n")

    # Save flagged candidates
    with open(OUTPUT_DIR / "enrichment_candidates_flagged.json", "w") as f:
        json.dump(enrichment_flagged, f, indent=2)

    print("=" * 80)
    print(f"✓ Saved enrichment_candidates_flagged.json ({len(enrichment_flagged)} papers)")
    print("=" * 80)

    # Summary
    print(f"\n\nSUMMARY")
    print(f"{'='*80}")
    print(f"Synthesis papers analyzed: {len(synthesis_citations)} cited by experts")
    print(f"Missing from corpus: {len(missing_candidates)}")
    print(f"High-confidence candidates (2+ reviews, conf>0.5): {len(enrichment_candidates)}")
    print(f"\nNext step: Manual review of flagged candidates")
    print(f"             Decide on inclusion based on relevance to connectomics")


if __name__ == "__main__":
    main()
