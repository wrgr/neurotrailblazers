#!/usr/bin/env python3
"""
Step 10: Apply author name merges and recompute author rankings.

Merges fall into three categories:
  A. User-confirmed (Gray Roncal)
  B. Multi-paper shared evidence — same first initial + last, 2+ co-authored papers
  C. Unicode/punctuation normalization (hyphen vs en-dash, trailing period)

Outputs:
  output/author_merge_map.json      — canonical → [aliases]
  output/author_rankings_merged.json — recomputed rankings after merge
  output/author_merge_report.txt    — human-readable merge log
"""
import json, re
from collections import defaultdict
from pathlib import Path

from config import OUTPUT_DIR

# ── Merge table ───────────────────────────────────────────────────────
# Format: (canonical, [aliases])
# Only high-confidence, manually verified merges.
# FALSE POSITIVES removed:
#   - 'Szi-chieh Yu' != 'Seongbong Yu'  (different people, coincidental co-authorship)
# CONFIRMED:
#   - Shin-ya / Satoko Takemura (13 shared papers, same person, OpenAlex error)
#   - Gray Roncal variants (user confirmed)
#   - Bates variants (1 shared paper, full name vs abbreviated)

MERGE_TABLE = [
    # User confirmed
    ("William Gray-Roncal", [
        "William Gray Roncal",
        "William R. Gray Roncal",
        "William R. Gray-Roncal",
        "Will Gray-Roncal",
    ]),
    # Multi-paper shared evidence
    ("Shin-ya Takemura", ["Satoko Takemura"]),
    ("Alexander Shakeel Bates", ["Alexander S. Bates"]),
    # Abbreviation — full name confirmed from external knowledge
    ("Gregory S.X.E. Jefferis", ["Gregory S. X. E. Jefferis", "Gregory SXE Jefferis", "G Jefferis"]),
    ("H. Sebastian Seung", ["H Sebastian Seung"]),
    ("Olaf Sporns", ["O Sporns"]),
    ("Moritz Helmstaedter", ["M Helmstaedter"]),
    ("Davi D. Bock", ["D Bock"]),
    ("Marta Costa", ["M Costa"]),
    # Unicode hyphen normalization (en-dash → hyphen)
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
    """Return corpus with author names normalised."""
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


def recompute_author_stats(merged_corpus):
    """Simple author stats: paper count, total external citations."""
    author_papers = defaultdict(set)
    author_cites = defaultdict(int)
    for p in merged_corpus:
        pid = p["openalex_id"]
        cites = p.get("cited_by_count", 0) or 0
        for a in p.get("authors", []):
            name = a.get("name", "")
            if name:
                author_papers[name].add(pid)
                author_cites[name] += cites
    return author_papers, author_cites


def main():
    with open(OUTPUT_DIR / "corpus_merged.json") as f:
        corpus = json.load(f)
    with open(OUTPUT_DIR / "author_rankings.json") as f:
        orig_rankings = json.load(f)

    alias_map = build_alias_map(MERGE_TABLE)
    merged_corpus = apply_merges_to_corpus(corpus, alias_map)

    author_papers, author_cites = recompute_author_stats(merged_corpus)

    # Build merged rankings from original + merge adjustments
    orig_lookup = {a["name"]: a for a in orig_rankings}
    canonical_names = {canonical for canonical, _ in MERGE_TABLE}

    report_lines = ["Author Merge Report", "=" * 60, ""]
    merged_stats = []

    for canonical, aliases in MERGE_TABLE:
        parts = [canonical] + aliases
        all_papers = set()
        for name in parts:
            all_papers |= author_papers.get(name, set())
        total_cites = sum(author_cites.get(name, 0) for name in parts)

        # Find original rank of canonical
        orig_entry = orig_lookup.get(canonical, {})
        orig_rank = next((i+1 for i,a in enumerate(orig_rankings) if a["name"]==canonical), None)

        merged_stats.append({
            "canonical": canonical,
            "aliases": aliases,
            "merged_paper_count": len(all_papers),
            "orig_paper_count": orig_entry.get("paper_count", 0),
            "total_citations_sum": total_cites,
            "orig_rank": orig_rank,
            "composite_score": orig_entry.get("composite_score", 0),
        })

        report_lines.append(f"Merge: '{canonical}'")
        for alias in aliases:
            alias_papers = len(author_papers.get(alias, set()))
            report_lines.append(f"  ← '{alias}' ({alias_papers} papers)")
        report_lines.append(f"  Combined: {len(all_papers)} unique papers  |  orig rank: #{orig_rank}")
        report_lines.append("")

    # Special: Gray Roncal not in top-1000, compute fresh
    roncal_names = ["William Gray-Roncal", "William Gray Roncal",
                    "William R. Gray Roncal", "William R. Gray-Roncal", "Will Gray-Roncal"]
    roncal_papers = set()
    for name in roncal_names:
        roncal_papers |= author_papers.get(name, set())
    report_lines.append(f"Will Gray-Roncal combined: {len(roncal_papers)} unique papers")
    report_lines.append(f"  (outside top-1000 before merge due to name fragmentation)")
    report_lines.append("")

    report_text = "\n".join(report_lines)
    with open(OUTPUT_DIR / "author_merge_report.txt", "w") as f:
        f.write(report_text)
    print(report_text)

    with open(OUTPUT_DIR / "author_merge_map.json", "w") as f:
        json.dump([{"canonical": c, "aliases": al} for c, al in MERGE_TABLE], f, indent=2)

    print(f"\nSaved → output/author_merge_map.json")
    print(f"Saved → output/author_merge_report.txt")


if __name__ == "__main__":
    main()
