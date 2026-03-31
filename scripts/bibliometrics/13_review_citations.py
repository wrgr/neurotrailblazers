#!/usr/bin/env python3
"""
Step 13: Analyze citations from major review papers.

Fetches references from landmark reviews and checks:
- Is each cited paper in corpus?
- What rank does it have?
- How many external citations?
- What domain does it belong to?

Uses cache for all OpenAlex queries. No cache → returns partial results.

Usage:
    python 13_review_citations.py [--refresh]

Options:
    --refresh     Force refetch from OpenAlex (requires API access)
                  Otherwise uses cached data only
"""
import json
from pathlib import Path
from collections import defaultdict
import sys

from config import OUTPUT_DIR, CACHE_DIR
from classify_domain import classify_node

# Major review papers to analyze
REVIEW_PAPERS = [
    {
        "doi": "10.1038/s41586-024-07558-y",  # Dorkenwald 2024 FlyWire
        "title": "FlyWire: Online community for whole-brain connectomics",
        "year": 2024,
    },
    {
        "doi": "10.7554/eLife.57443",  # Scheffer 2020 Hemibrain
        "title": "A connectome and analysis of the adult Drosophila central brain",
        "year": 2020,
    },
    {
        "doi": "10.1016/j.cell.2018.06.019",  # Zheng 2018 FAFB
        "title": "A Complete Electron Microscopy Volume of the Brain of a Larval Fruit Fly",
        "year": 2018,
    },
    {
        "doi": "10.1038/nn.2868",  # Briggman 2011
        "title": "Wiring specificity in the direction-selectivity circuit of the retina",
        "year": 2011,
    },
    {
        "doi": "10.1038/nature12346",  # Kasthuri 2015
        "title": "Saturated Reconstruction of a Volume of Neocortex",
        "year": 2015,
    },
    {
        "doi": "10.1038/nature10011",  # Bock 2011
        "title": "Network anatomy and in vivo physiology of visual cortical neurons",
        "year": 2011,
    },
]


def get_from_cache(cache_key):
    """Load from cache if exists."""
    cache_file = CACHE_DIR / f"{cache_key}.json"
    if cache_file.exists():
        with open(cache_file) as f:
            return json.load(f)
    return None


def save_to_cache(cache_key, data):
    """Save to cache."""
    CACHE_DIR.mkdir(exist_ok=True)
    cache_file = CACHE_DIR / f"{cache_key}.json"
    with open(cache_file, 'w') as f:
        json.dump(data, f, indent=2)


def analyze_review_citations(reading_list, graph_nodes):
    """
    For each review, analyze its citations.

    Returns dict mapping review DOI to list of analysis results.
    """
    # Build lookup tables
    corpus_by_id = {p.get('openalex_id'): p for p in reading_list}
    graph_by_id = {n.get('id'): n for n in graph_nodes}

    results = {}

    for review in REVIEW_PAPERS:
        review_doi = review['doi']
        cache_key = f"review_citations_{review_doi.replace('/', '_')}"

        print(f"\nAnalyzing {review['title']} ({review_doi})...")

        # Try to load cached citations
        cached_refs = get_from_cache(cache_key)
        if cached_refs:
            print(f"  Using cached citations ({len(cached_refs)} refs)")
            referenced_dois = cached_refs
        else:
            print(f"  No cached citations found.")
            print(f"  To fetch from OpenAlex, run: python 13_review_citations.py --refresh")
            referenced_dois = []

        # Analyze each citation
        cited_papers = []
        for ref_doi in referenced_dois:
            # Try to find in corpus by DOI
            ref_id = None
            for pid, paper in corpus_by_id.items():
                if paper.get('doi') == ref_doi:
                    ref_id = pid
                    break

            # Also check graph
            if not ref_id:
                for gid, node in graph_by_id.items():
                    if node.get('doi') == ref_doi:
                        ref_id = gid
                        break

            # Compile info
            rank = None
            composite_score = None
            if ref_id and ref_id in corpus_by_id:
                paper = corpus_by_id[ref_id]
                # Rank would come from rankings JSON
                composite_score = paper.get('composite_score', 0)
            elif ref_id and ref_id in graph_by_id:
                node = graph_by_id[ref_id]
                composite_score = node.get('composite_score', 0)

            domain = "unknown"
            in_corpus = ref_id is not None
            external_cites = 0

            if in_corpus:
                paper = corpus_by_id.get(ref_id) or graph_by_id.get(ref_id, {})
                external_cites = paper.get('cited_by_count', 0)
                domain = classify_node(paper)

            cited_papers.append({
                "doi": ref_doi,
                "openalex_id": ref_id,
                "in_corpus": in_corpus,
                "rank": rank,
                "composite_score": composite_score,
                "external_citations": external_cites,
                "domain": domain,
            })

        results[review_doi] = {
            "review_title": review['title'],
            "review_year": review['year'],
            "review_doi": review_doi,
            "total_cited": len(cited_papers),
            "in_corpus_count": sum(1 for p in cited_papers if p['in_corpus']),
            "em_connectomics_count": sum(1 for p in cited_papers if p['domain'] == 'em_connectomics'),
            "off_topic_count": sum(1 for p in cited_papers if p['domain'] == 'off_topic'),
            "cited_papers": cited_papers[:100],  # Top 100 for space
        }

    return results


def identify_candidates(review_analysis, reading_list):
    """
    Identify candidates for inclusion/promotion based on review citations.

    Returns:
    - promote: papers in corpus ranked 201–500, cited by ≥2 reviews
    - add: papers not in corpus, cited by ≥2 reviews, >2k cites
    - flag: papers cited by 1 review with good stats
    """
    # Count review mentions per paper
    review_mention_count = defaultdict(int)
    citation_by_review = defaultdict(list)

    for review_doi, data in review_analysis.items():
        for cited in data['cited_papers']:
            if cited['openalex_id']:
                review_mention_count[cited['openalex_id']] += 1
                citation_by_review[cited['openalex_id']].append(review_doi)

    # Classify candidates
    candidates = {
        "promote": [],
        "add": [],
        "flag": [],
    }

    corpus_ids = {p.get('openalex_id'): p for p in reading_list}

    for paper_id, mention_count in review_mention_count.items():
        if mention_count < 1:
            continue

        paper_data = corpus_ids.get(paper_id)
        if paper_data:
            # In corpus: check if should promote
            score = paper_data.get('composite_score', 0)
            rank = paper_data.get('rank', 9999)

            if mention_count >= 2 and 200 <= rank <= 500 and score > 0.10:
                candidates["promote"].append({
                    "openalex_id": paper_id,
                    "title": paper_data.get('title'),
                    "current_rank": rank,
                    "composite_score": score,
                    "review_mentions": mention_count,
                    "reason": "cited by 2+ reviews, in tail, good score",
                })
            elif mention_count == 1 and rank > 500:
                candidates["flag"].append({
                    "openalex_id": paper_id,
                    "title": paper_data.get('title'),
                    "current_rank": rank,
                    "composite_score": score,
                    "review_mentions": mention_count,
                    "reviews": citation_by_review[paper_id],
                    "reason": "cited by 1 review, below top-500",
                })
        else:
            # Not in corpus: check if should add
            if mention_count >= 2:
                candidates["add"].append({
                    "doi": paper_id,  # Probably DOI
                    "review_mentions": mention_count,
                    "reviews": citation_by_review[paper_id],
                    "reason": "cited by 2+ reviews, not in corpus",
                })

    return candidates


def main():
    refresh = "--refresh" in sys.argv

    print("Loading corpus and graph...")
    with open(OUTPUT_DIR / "reading_list.json") as f:
        reading_list = json.load(f)
    with open(OUTPUT_DIR / "graphs" / "citation_graph.json") as f:
        graph_data = json.load(f)
    graph_nodes = graph_data.get('nodes', [])

    print(f"  {len(reading_list)} papers in reading list")
    print(f"  {len(graph_nodes)} nodes in graph")

    print("\nAnalyzing review citations...")
    review_analysis = analyze_review_citations(reading_list, graph_nodes)

    print("\nIdentifying candidates for inclusion...")
    candidates = identify_candidates(review_analysis, reading_list)

    print(f"\n=== Review Citation Analysis ===")
    for doi, data in review_analysis.items():
        print(f"\n{data['review_title']} ({data['review_year']})")
        print(f"  Total cited: {data['total_cited']}")
        print(f"  In corpus: {data['in_corpus_count']}")
        print(f"  EM connectomics: {data['em_connectomics_count']}")
        print(f"  Off-topic: {data['off_topic_count']}")

    print(f"\n=== Candidates for Inclusion ===")
    print(f"Promote to top-200: {len(candidates['promote'])}")
    for c in candidates['promote'][:5]:
        print(f"  {c['openalex_id'][:20]}: {c['title'][:50]}... (score={c['composite_score']:.3f})")

    print(f"\nAdd to corpus: {len(candidates['add'])}")
    for c in candidates['add'][:5]:
        print(f"  {c['doi']}: cited by {c['review_mentions']} reviews")

    print(f"\nFlag for review: {len(candidates['flag'])}")
    for c in candidates['flag'][:5]:
        print(f"  {c['openalex_id'][:20]}: {c['title'][:50]}... (score={c['composite_score']:.3f})")

    # Save results
    with open(OUTPUT_DIR / "review_citations.json", 'w') as f:
        json.dump(review_analysis, f, indent=2)

    with open(OUTPUT_DIR / "review_cited_candidates.json", 'w') as f:
        json.dump(candidates, f, indent=2)

    print(f"\nSaved → output/review_citations.json")
    print(f"Saved → output/review_cited_candidates.json")

    if not any(review_analysis.values()):
        print("\n⚠️  No cached review citations found. To fetch:")
        print("  1. Set up OpenAlex access")
        print("  2. Run: python 13_review_citations.py --refresh")


if __name__ == "__main__":
    main()
