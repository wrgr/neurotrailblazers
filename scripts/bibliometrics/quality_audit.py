#!/usr/bin/env python3
"""
Quality Audit: Preprint/Published Duplicate Detection & Author Name Deduplication
for the connectomics paper corpus.
"""

import json
import re
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

BASE = Path("/home/user/neurotrailblazers/scripts/bibliometrics/output")

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
with open(BASE / "paper_rankings.json") as f:
    rankings = json.load(f)

with open(BASE / "reading_list.json") as f:
    reading_list = json.load(f)

with open(BASE / "graphs" / "citation_graph.json") as f:
    graph = json.load(f)

# Build lookup structures
reading_list_ids = {p["openalex_id"] for p in reading_list}
rank_by_id = {p["openalex_id"]: i + 1 for i, p in enumerate(rankings)}
paper_by_id = {p["openalex_id"]: p for p in rankings}

# Also index graph nodes for journal info (rankings don't have journal)
graph_node_by_id = {n["id"]: n for n in graph["nodes"]}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def normalize_title(t):
    """Lowercase, strip punctuation, collapse whitespace, remove leading articles."""
    t = t.lower()
    t = unicodedata.normalize("NFKD", t)
    t = re.sub(r"[^\w\s]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    # Strip leading articles
    for prefix in ("a ", "an ", "the "):
        if t.startswith(prefix):
            t = t[len(prefix):]
    return t

def title_similarity(t1, t2):
    return SequenceMatcher(None, t1, t2).ratio()

def is_preprint_doi(doi):
    if not doi:
        return False
    return "10.1101/" in doi or "arxiv" in doi.lower()

def get_journal(paper):
    """Get journal from graph node if available."""
    node = graph_node_by_id.get(paper["openalex_id"])
    if node and node.get("journal"):
        return node["journal"]
    # Check reading list
    for rl in reading_list:
        if rl["openalex_id"] == paper["openalex_id"]:
            return rl.get("journal", "")
    return ""

def extract_last_name(full_name):
    """Extract probable last name from author string."""
    parts = full_name.strip().split()
    if not parts:
        return ""
    return parts[-1]

def extract_first_parts(full_name):
    """Extract first/middle name parts."""
    parts = full_name.strip().split()
    if len(parts) <= 1:
        return []
    return parts[:-1]

def normalize_name(name):
    """Normalize unicode in name."""
    return unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")

# ---------------------------------------------------------------------------
# 1. PREPRINT / PUBLISHED DUPLICATE DETECTION
# ---------------------------------------------------------------------------
print("=" * 80)
print("QUALITY AUDIT REPORT")
print("=" * 80)
print()
print("=" * 80)
print("SECTION 1: PREPRINT / PUBLISHED DUPLICATE DETECTION")
print("=" * 80)
print()

# Pre-compute normalized titles
norm_titles = []
for i, p in enumerate(rankings):
    nt = normalize_title(p["title"])
    first_author = p["authors"][0] if p["authors"] else ""
    last_name = extract_last_name(first_author)
    doi = p.get("doi", "") or ""
    is_preprint = is_preprint_doi(doi)
    journal = get_journal(p)
    journal_is_preprint = bool(
        journal and any(x in journal.lower() for x in ("biorxiv", "arxiv", "medrxiv", "preprint"))
    )
    norm_titles.append({
        "idx": i,
        "norm_title": nt,
        "first_author_last": last_name.lower(),
        "is_preprint_doi": is_preprint,
        "is_preprint_journal": journal_is_preprint,
        "journal": journal,
    })

# Group by first-author last name to reduce O(n^2) comparisons
by_author = defaultdict(list)
for nt in norm_titles:
    if nt["first_author_last"]:
        by_author[nt["first_author_last"]].append(nt)

# Also do a broader pass: group by first 5 words of normalized title
by_title_prefix = defaultdict(list)
for nt in norm_titles:
    words = nt["norm_title"].split()[:5]
    key = " ".join(words)
    by_title_prefix[key].append(nt)

# Find candidate pairs
duplicate_pairs = []
seen_pairs = set()

def check_pair(i, j):
    """Check if papers i,j are suspected duplicates."""
    if i >= j:
        return None
    key = (i, j)
    if key in seen_pairs:
        return None
    seen_pairs.add(key)

    pi = rankings[i]
    pj = rankings[j]
    ni = norm_titles[i]
    nj = norm_titles[j]

    sim = title_similarity(ni["norm_title"], nj["norm_title"])
    if sim < 0.80:
        return None

    # Year must be close
    if abs(pi["year"] - pj["year"]) > 2:
        return None

    # High similarity alone is sufficient
    if sim >= 0.90:
        return (i, j, sim, "high_title_similarity")

    # Medium similarity + same first author
    if sim >= 0.85 and ni["first_author_last"] == nj["first_author_last"]:
        return (i, j, sim, "title_sim+same_first_author")

    # Medium similarity + one is preprint
    if sim >= 0.82 and (ni["is_preprint_doi"] or nj["is_preprint_doi"] or
                         ni["is_preprint_journal"] or nj["is_preprint_journal"]):
        return (i, j, sim, "title_sim+preprint_signal")

    return None

# Search within author groups
for author, entries in by_author.items():
    if len(entries) < 2:
        continue
    for a in range(len(entries)):
        for b in range(a + 1, len(entries)):
            result = check_pair(entries[a]["idx"], entries[b]["idx"])
            if result:
                duplicate_pairs.append(result)

# Search within title-prefix groups
for prefix, entries in by_title_prefix.items():
    if len(entries) < 2:
        continue
    for a in range(len(entries)):
        for b in range(a + 1, len(entries)):
            result = check_pair(entries[a]["idx"], entries[b]["idx"])
            if result:
                duplicate_pairs.append(result)

# Sort by similarity descending
duplicate_pairs.sort(key=lambda x: -x[2])

print(f"Found {len(duplicate_pairs)} suspected preprint/published duplicate pairs")
print()

total_split_citations = 0
merges_into_top500 = []

for pair_num, (i, j, sim, reason) in enumerate(duplicate_pairs, 1):
    pi = rankings[i]
    pj = rankings[j]
    rank_i = rank_by_id[pi["openalex_id"]]
    rank_j = rank_by_id[pj["openalex_id"]]
    in_top500_i = pi["openalex_id"] in reading_list_ids
    in_top500_j = pj["openalex_id"] in reading_list_ids
    combined_citations = pi["total_citations"] + pj["total_citations"]
    combined_score = pi["composite_score"] + pj["composite_score"]

    # Determine which is likely the preprint
    doi_i = pi.get("doi", "") or ""
    doi_j = pj.get("doi", "") or ""
    journal_i = get_journal(pi)
    journal_j = get_journal(pj)

    preprint_label = ""
    if is_preprint_doi(doi_i) and not is_preprint_doi(doi_j):
        preprint_label = f"  [Paper A is likely PREPRINT, Paper B is PUBLISHED]"
    elif is_preprint_doi(doi_j) and not is_preprint_doi(doi_i):
        preprint_label = f"  [Paper B is likely PREPRINT, Paper A is PUBLISHED]"

    print(f"--- Duplicate Pair #{pair_num} (similarity: {sim:.3f}, reason: {reason}) ---")
    if preprint_label:
        print(preprint_label)
    print(f"  Paper A [Rank #{rank_i}]{'  ** IN TOP 500 **' if in_top500_i else ''}:")
    print(f"    Title: {pi['title']}")
    print(f"    Year: {pi['year']}  |  DOI: {doi_i}  |  Journal: {journal_i}")
    print(f"    Citations: {pi['total_citations']}  |  Composite: {pi['composite_score']:.4f}")
    print(f"  Paper B [Rank #{rank_j}]{'  ** IN TOP 500 **' if in_top500_j else ''}:")
    print(f"    Title: {pj['title']}")
    print(f"    Year: {pj['year']}  |  DOI: {doi_j}  |  Journal: {journal_j}")
    print(f"    Citations: {pj['total_citations']}  |  Composite: {pj['composite_score']:.4f}")
    print(f"  COMBINED citations: {combined_citations}  |  COMBINED composite: {combined_score:.4f}")

    # Check if either is outside top 500 but combined would push it in
    if not in_top500_i and not in_top500_j:
        # Check if combined score would beat rank 500
        score_500 = rankings[499]["composite_score"] if len(rankings) >= 500 else 0
        if combined_score > score_500:
            merges_into_top500.append((i, j, combined_score, combined_citations))
            print(f"  ** MERGE WOULD ENTER TOP 500 (threshold: {score_500:.4f}) **")
    elif in_top500_i != in_top500_j:
        print(f"  ** SPLIT: One version in top 500, one outside **")

    total_split_citations += min(pi["total_citations"], pj["total_citations"])
    print()

if not duplicate_pairs:
    print("No suspected duplicates found in the top 2000 papers.")
    print()

# ---------------------------------------------------------------------------
# 2. AUTHOR NAME VARIANT DETECTION
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("SECTION 2: AUTHOR NAME VARIANT DETECTION (Top 500 papers)")
print("=" * 80)
print()

# Extract all authors from reading list
author_papers = defaultdict(list)  # author_name -> list of paper titles
for p in reading_list:
    for author in p.get("authors", []):
        author_papers[author].append({
            "title": p["title"],
            "year": p["year"],
            "openalex_id": p["openalex_id"],
        })

all_authors = list(author_papers.keys())
print(f"Total unique author name strings in top 500: {len(all_authors)}")

# Group by last name
by_last = defaultdict(list)
for name in all_authors:
    last = extract_last_name(name)
    if last:
        by_last[last.lower()].append(name)

# Also group by normalized (ASCII) last name to catch unicode variants
by_last_ascii = defaultdict(list)
for name in all_authors:
    last = extract_last_name(name)
    if last:
        key = normalize_name(last).lower()
        by_last_ascii[key].append(name)

# Find suspected name variants
name_variant_groups = []

def first_name_similar(name_a, name_b):
    """Check if two names with the same last name are likely the same person."""
    parts_a = extract_first_parts(name_a)
    parts_b = extract_first_parts(name_b)
    if not parts_a or not parts_b:
        return False, ""

    first_a = parts_a[0]
    first_b = parts_b[0]

    # One is initial of the other
    if len(first_a) <= 2 and first_b.lower().startswith(first_a.rstrip(".").lower()):
        return True, "initial_match"
    if len(first_b) <= 2 and first_a.lower().startswith(first_b.rstrip(".").lower()):
        return True, "initial_match"

    # Nickname / short form (e.g., Jeff vs Jeffrey)
    if first_a.lower().startswith(first_b.lower()[:3]) or first_b.lower().startswith(first_a.lower()[:3]):
        if len(first_a) >= 3 and len(first_b) >= 3:
            sim = SequenceMatcher(None, first_a.lower(), first_b.lower()).ratio()
            if sim >= 0.6:
                return True, f"name_similarity({sim:.2f})"

    # Exact match but different middle name/initial
    if first_a.lower() == first_b.lower() and parts_a != parts_b:
        return True, "same_first_diff_middle"

    # Unicode normalization difference
    if normalize_name(name_a).lower() == normalize_name(name_b).lower() and name_a != name_b:
        return True, "unicode_variant"

    # Full fuzzy match
    norm_a = normalize_name(" ".join(parts_a)).lower()
    norm_b = normalize_name(" ".join(parts_b)).lower()
    if norm_a != norm_b:
        sim = SequenceMatcher(None, norm_a, norm_b).ratio()
        if sim >= 0.75 and len(norm_a) > 2 and len(norm_b) > 2:
            return True, f"fuzzy_first({sim:.2f})"

    return False, ""

# Check within each last-name group (using ASCII-normalized grouping)
checked_groups = set()
for last_key, names in by_last_ascii.items():
    if len(names) < 2:
        continue
    # Find variant clusters
    variants_found = []
    for a_idx in range(len(names)):
        for b_idx in range(a_idx + 1, len(names)):
            is_sim, reason = first_name_similar(names[a_idx], names[b_idx])
            if is_sim:
                variants_found.append((names[a_idx], names[b_idx], reason))

    if variants_found:
        # Merge into connected groups
        groups = {}
        for na, nb, reason in variants_found:
            ga = groups.get(na, {na})
            gb = groups.get(nb, {nb})
            merged = ga | gb
            for n in merged:
                groups[n] = merged
        unique_groups = []
        seen = set()
        for g in groups.values():
            key = frozenset(g)
            if key not in seen:
                seen.add(key)
                unique_groups.append(g)
        for group in unique_groups:
            total_papers = sum(len(author_papers[n]) for n in group)
            name_variant_groups.append({
                "names": sorted(group),
                "last_name": last_key,
                "total_papers": total_papers,
                "paper_counts": {n: len(author_papers[n]) for n in sorted(group)},
            })

# Sort by total papers descending (most impactful first)
name_variant_groups.sort(key=lambda x: -x["total_papers"])

print(f"Found {len(name_variant_groups)} suspected author name variant groups")
print()

# Show prolific authors (5+ papers) with variants
prolific_variants = [g for g in name_variant_groups if g["total_papers"] >= 5]
print(f"Prolific authors (5+ papers) with name variants: {len(prolific_variants)}")
print()

for gnum, group in enumerate(prolific_variants, 1):
    print(f"--- Author Variant Group #{gnum} (last name: {group['last_name']}) ---")
    for name in group["names"]:
        count = group["paper_counts"][name]
        print(f"  \"{name}\" ({count} paper{'s' if count != 1 else ''})")
    print(f"  Total papers across variants: {group['total_papers']}")
    # List some affected papers
    all_group_papers = []
    for name in group["names"]:
        for pp in author_papers[name]:
            all_group_papers.append((name, pp))
    if len(all_group_papers) <= 10:
        for name, pp in all_group_papers:
            print(f"    - [{pp['year']}] \"{pp['title']}\" (as: {name})")
    else:
        for name, pp in all_group_papers[:8]:
            print(f"    - [{pp['year']}] \"{pp['title']}\" (as: {name})")
        print(f"    ... and {len(all_group_papers) - 8} more papers")
    print()

# Show all remaining variant groups (fewer papers)
other_variants = [g for g in name_variant_groups if g["total_papers"] < 5]
if other_variants:
    print(f"\nOther name variant groups ({len(other_variants)} groups with <5 papers):")
    for group in other_variants[:30]:
        names_str = " | ".join(f'"{n}" ({group["paper_counts"][n]}p)' for n in group["names"])
        print(f"  [{group['last_name']}] {names_str}")
    if len(other_variants) > 30:
        print(f"  ... and {len(other_variants) - 30} more groups")

# ---------------------------------------------------------------------------
# 3. IMPACT ASSESSMENT
# ---------------------------------------------------------------------------
print()
print()
print("=" * 80)
print("SECTION 3: IMPACT ASSESSMENT")
print("=" * 80)
print()

print("--- Citation Splitting Impact ---")
print(f"Total duplicate pairs found: {len(duplicate_pairs)}")
print(f"Estimated citations 'lost' to splitting (sum of lesser count): {total_split_citations}")
print()

if duplicate_pairs:
    # For each pair, estimate composite score impact
    print("Per-pair impact on composite scores:")
    score_500 = rankings[499]["composite_score"] if len(rankings) >= 500 else 0
    print(f"(Current rank #500 composite score threshold: {score_500:.4f})")
    print()

    for pair_num, (i, j, sim, reason) in enumerate(duplicate_pairs, 1):
        pi = rankings[i]
        pj = rankings[j]
        rank_i = rank_by_id[pi["openalex_id"]]
        rank_j = rank_by_id[pj["openalex_id"]]
        better = pi if pi["composite_score"] >= pj["composite_score"] else pj
        worse = pj if pi["composite_score"] >= pj["composite_score"] else pi
        rank_better = rank_by_id[better["openalex_id"]]
        rank_worse = rank_by_id[worse["openalex_id"]]

        combined_score = pi["composite_score"] + pj["composite_score"]
        combined_citations = pi["total_citations"] + pj["total_citations"]
        combined_pagerank = pi["pagerank"] + pj["pagerank"]

        # Estimate new rank (how many papers have score > combined)
        new_rank = sum(1 for p in rankings if p["composite_score"] > combined_score) + 1

        print(f"  Pair #{pair_num}: \"{better['title'][:70]}...\"")
        print(f"    Current best rank: #{rank_better} (score {better['composite_score']:.4f})")
        print(f"    Other version rank: #{rank_worse} (score {worse['composite_score']:.4f})")
        print(f"    If merged -> score ~{combined_score:.4f}, est. rank #{new_rank}")
        print(f"    Citations: {better['total_citations']} + {worse['total_citations']} = {combined_citations}")
        print(f"    Rank improvement: #{rank_better} -> #{new_rank} ({rank_better - new_rank} positions)")
        if rank_better > 500 and new_rank <= 500:
            print(f"    ** WOULD ENTER TOP 500 **")
        elif rank_better <= 500 and new_rank < rank_better:
            print(f"    ** Would improve position within top 500 **")
        print()

print()
print("--- Author Name Variant Impact ---")
print(f"Total variant groups found: {len(name_variant_groups)}")
print(f"Prolific authors affected (5+ papers): {len(prolific_variants)}")
total_affected_papers = sum(g["total_papers"] for g in name_variant_groups)
print(f"Total papers potentially affected by name variants: {total_affected_papers}")
print()
print("These name variants could affect:")
print("  - Co-authorship network community detection (same author split into multiple nodes)")
print("  - Author productivity metrics (publication counts fragmented)")
print("  - Collaboration pattern analysis (connections attributed to different 'people')")
print()

# Summary
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"  Preprint/published duplicate pairs: {len(duplicate_pairs)}")
print(f"  Author name variant groups: {len(name_variant_groups)}")
print(f"  Prolific authors with variants: {len(prolific_variants)}")
if merges_into_top500:
    print(f"  Merges that would enter top 500: {len(merges_into_top500)}")
print(f"  Estimated split citations: {total_split_citations}")
print()
