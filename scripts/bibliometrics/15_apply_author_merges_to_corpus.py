#!/usr/bin/env python3
"""
Apply author name merges to corpus and recompute author rankings.

This script:
1. Loads author_merge_map.json (previously identified merges)
2. Applies merges to corpus_final.json
3. Recomputes author rankings with merged names
4. Saves updated corpus and author_rankings
"""
import json
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path("output")

# Merge table (canonical → aliases)
MERGE_TABLE = [
    ("William Gray-Roncal", [
        "William Gray Roncal",
        "William R. Gray Roncal",
        "William R. Gray-Roncal",
        "Will Gray-Roncal",
    ]),
    ("Shin-ya Takemura", ["Satoko Takemura"]),
    ("Alexander Shakeel Bates", ["Alexander S. Bates"]),
    ("Gregory S.X.E. Jefferis", ["Gregory S. X. E. Jefferis", "Gregory SXE Jefferis", "G Jefferis"]),
    ("H. Sebastian Seung", ["H Sebastian Seung"]),
    ("Olaf Sporns", ["O Sporns"]),
    ("Moritz Helmstaedter", ["M Helmstaedter"]),
    ("Davi D. Bock", ["D Bock"]),
    ("Marta Costa", ["M Costa"]),
    ("Thomas Müller-Reichert", ["Thomas Müller\u2010Reichert", "Thomas Müller\u2011Reichert"]),
    ("Adam A. Atanas", ["Adam A Atanas"]),
    ("Mark W. Moyle", ["Mark W Moyle"]),
    ("Christopher J. Potter", ["Christopher J Potter"]),
    ("Chun-Chieh Lin", ["Chun\u2010Chieh Lin", "Chun\u2011Chieh Lin"]),
    ("Casey M. Schneider-Mizell", ["Casey M Schneider-Mizell"]),
    ("Wei-Chung Allen Lee", ["Wei-Chung Lee", "W.C.A. Lee"]),
    ("C. Shan Xu", ["C Shan Xu", "Shan Xu"]),
]


def build_alias_map(merge_table):
    """Return alias → canonical mapping."""
    alias_map = {}
    for canonical, aliases in merge_table:
        for alias in aliases:
            alias_map[alias] = canonical
    return alias_map


def apply_merges_to_corpus(corpus, alias_map):
    """Apply author name merges to corpus."""
    merged_corpus = []
    for p in corpus:
        new_authors = []
        seen = set()
        for a in p.get("authors", []):
            name = a.get("name", "")
            canonical = alias_map.get(name, name)
            if canonical not in seen:
                seen.add(canonical)
                new_authors.append({**a, "name": canonical})
        merged_corpus.append({**p, "authors": new_authors})
    return merged_corpus


def recompute_author_rankings(merged_corpus, old_rankings):
    """Recompute author rankings after merges."""
    # Build new author stats
    author_papers = defaultdict(set)
    author_coauthors = defaultdict(set)
    author_data = defaultdict(lambda: {"paper_count": 0, "composite_score": 0.0})

    for p in merged_corpus:
        pid = p.get("openalex_id", "")
        authors = [a.get("name", "") for a in p.get("authors", [])]

        for author in authors:
            if not author:
                continue
            author_papers[author].add(pid)
            # Track co-authors
            for co in authors:
                if co and co != author:
                    author_coauthors[author].add(co)

    # Use composite_score from top papers each author appears in
    old_lookup = {a["name"]: a for a in old_rankings}

    new_rankings = []
    for author in sorted(author_papers.keys()):
        paper_count = len(author_papers[author])
        co_author_count = len(author_coauthors.get(author, set()))

        # Get best composite_score from this author's papers
        composite_score = old_lookup.get(author, {}).get("composite_score", 0.0)

        new_rankings.append({
            "name": author,
            "paper_count": paper_count,
            "co_author_count": co_author_count,
            "composite_score": composite_score,
            "merged": author in {c for c, _ in MERGE_TABLE}
        })

    # Sort by paper count descending
    new_rankings.sort(key=lambda x: x["paper_count"], reverse=True)

    # Add rank
    for i, r in enumerate(new_rankings, 1):
        r["rank"] = i

    return new_rankings


def main():
    print("Loading data...")
    with open(OUTPUT_DIR / "corpus_final.json") as f:
        corpus = json.load(f)
    with open(OUTPUT_DIR / "author_rankings.json") as f:
        old_rankings = json.load(f)

    print(f"Corpus: {len(corpus)} papers")
    print(f"Author rankings: {len(old_rankings)} authors")

    # Build and apply merges
    alias_map = build_alias_map(MERGE_TABLE)
    merged_corpus = apply_merges_to_corpus(corpus, alias_map)
    merged_rankings = recompute_author_rankings(merged_corpus, old_rankings)

    # Save merged corpus
    with open(OUTPUT_DIR / "corpus_final.json", "w") as f:
        json.dump(merged_corpus, f)
    print(f"✓ Saved corpus_final.json with author merges applied")

    # Save merged rankings
    with open(OUTPUT_DIR / "author_rankings.json", "w") as f:
        json.dump(merged_rankings, f, indent=2)
    print(f"✓ Saved author_rankings.json with {len(merged_rankings)} authors (merged)")

    # Report merged authors
    print("\n--- Author Merges Applied ---")
    for canonical, aliases in MERGE_TABLE:
        # Find in merged rankings
        merged_entry = next((r for r in merged_rankings if r["name"] == canonical), None)
        if merged_entry:
            print(f"✓ {canonical}")
            print(f"  Aliases: {', '.join(aliases)}")
            print(f"  Total papers: {merged_entry['paper_count']}")
            print(f"  Rank: #{merged_entry['rank']}")


if __name__ == "__main__":
    main()
