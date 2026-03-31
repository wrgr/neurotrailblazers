#!/usr/bin/env python3
"""
Multi-signal duplicate detection for the connectomics paper corpus.

Combines five independent signals into a single confidence score:
  1. Title similarity       (fuzzy string match)
  2. DOI pattern            (bioRxiv/arXiv prefix detection)
  3. Citation neighborhood  (Jaccard similarity of in/out edges)
  4. Author overlap         (shared first/last author)
  5. Mutual non-citation    (true duplicates rarely cite each other)

Outputs:
  - duplicate_review.tsv  — ranked pairs for human review
  - duplicate_review.md   — formatted markdown report

Run:  python3 scripts/bibliometrics/12_dedup_review.py
"""
import json, re, sys
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

OUT = Path("scripts/bibliometrics/output")

# ── Load data ────────────────────────────────────────────────────────────

print("Loading citation graph...")
with open(OUT / "graphs/citation_graph.json") as f:
    graph = json.load(f)

nodes = {n["id"]: n for n in graph["nodes"]}
edges = graph["edges"]

print("Loading paper rankings...")
with open(OUT / "paper_rankings.json") as f:
    rankings = json.load(f)

rank_by_id = {r["openalex_id"]: i + 1 for i, r in enumerate(rankings)}
id_to_ranking = {r["openalex_id"]: r for r in rankings}

print("Loading reading list...")
with open(OUT / "reading_list.json") as f:
    reading_list = json.load(f)
top500_ids = {p["openalex_id"] for p in reading_list}

# ── Build adjacency ─────────────────────────────────────────────────────

cites = defaultdict(set)
cited_by = defaultdict(set)
for e in edges:
    cites[e["source"]].add(e["target"])
    cited_by[e["target"]].add(e["source"])

# ── Helpers ──────────────────────────────────────────────────────────────

def normalize_title(t):
    return re.sub(r"[^a-z0-9\s]", "", (t or "").lower()).strip()

def jaccard(a, b):
    if not a and not b:
        return 0.0
    union = a | b
    return len(a & b) / len(union) if union else 0.0

def is_preprint_doi(doi):
    if not doi:
        return False
    return "10.1101/" in doi or "arxiv" in doi.lower()

def is_preprint_journal(journal):
    if not journal:
        return False
    return any(x in journal.lower() for x in ("biorxiv", "arxiv", "medrxiv", "preprint"))

def extract_last_name(name):
    parts = (name or "").split()
    return parts[-1].lower() if parts else ""

def author_overlap(a_id, b_id):
    """Check if two papers share first or last author."""
    ra = id_to_ranking.get(a_id)
    rb = id_to_ranking.get(b_id)
    if not ra or not rb:
        return 0.0
    aa = ra.get("authors", [])
    ab = rb.get("authors", [])
    if not aa or not ab:
        return 0.0
    # Check first author last name
    first_a = extract_last_name(aa[0])
    first_b = extract_last_name(ab[0])
    if first_a == first_b and first_a:
        return 1.0
    # Check last author
    last_a = extract_last_name(aa[-1])
    last_b = extract_last_name(ab[-1])
    if last_a == last_b and last_a:
        return 0.5
    return 0.0

# ── Signal computation ───────────────────────────────────────────────────

def compute_signals(a_id, b_id):
    """Compute all five dedup signals for a pair of papers."""
    na = nodes.get(a_id, {})
    nb = nodes.get(b_id, {})

    # 1. Title similarity
    title_sim = SequenceMatcher(
        None, normalize_title(na.get("title", "")),
        normalize_title(nb.get("title", ""))
    ).ratio()

    # 2. Preprint signal (either or both has preprint DOI/journal)
    doi_a, doi_b = na.get("doi", ""), nb.get("doi", "")
    journal_a, journal_b = na.get("journal", ""), nb.get("journal", "")
    preprint_a = is_preprint_doi(doi_a) or is_preprint_journal(journal_a)
    preprint_b = is_preprint_doi(doi_b) or is_preprint_journal(journal_b)
    # One preprint + one published is the classic pattern
    preprint_signal = 1.0 if (preprint_a != preprint_b) else (0.5 if (preprint_a and preprint_b) else 0.0)

    # 3. Citation neighborhood Jaccard
    out_j = jaccard(cites.get(a_id, set()), cites.get(b_id, set()))
    in_j = jaccard(cited_by.get(a_id, set()), cited_by.get(b_id, set()))
    citation_sim = 0.5 * out_j + 0.5 * in_j

    # 4. Author overlap
    auth_overlap = author_overlap(a_id, b_id)

    # 5. Mutual non-citation (do they cite each other? unlikely for duplicates)
    mutual_cite = (b_id in cites.get(a_id, set())) or (a_id in cites.get(b_id, set()))
    non_cite_signal = 0.0 if mutual_cite else 1.0

    return {
        "title_sim": title_sim,
        "preprint_signal": preprint_signal,
        "citation_sim": citation_sim,
        "out_jaccard": out_j,
        "in_jaccard": in_j,
        "author_overlap": auth_overlap,
        "non_cite": non_cite_signal,
        "mutual_cite": mutual_cite,
    }

def composite_confidence(signals):
    """
    Weighted confidence score.
    Weights chosen so that:
      - Title alone (1.0) → ~0.35 (needs corroboration)
      - Title + preprint → ~0.55 (likely but review)
      - Title + citation overlap → ~0.65 (strong)
      - Title + preprint + citations + author → ~0.90 (near-certain)
      - Low title but high citations + author → ~0.50 (title-changed, flag for review)
    """
    return (
        0.35 * signals["title_sim"]
        + 0.10 * signals["preprint_signal"]
        + 0.25 * signals["citation_sim"]
        + 0.15 * signals["author_overlap"]
        + 0.15 * signals["non_cite"]
    )

# ── Candidate pair generation ────────────────────────────────────────────

print("Generating candidate pairs...")

# Strategy 1: Title prefix groups (catches same/similar titles)
title_prefix_groups = defaultdict(list)
for nid, n in nodes.items():
    nt = normalize_title(n.get("title", ""))
    if len(nt) >= 20:
        title_prefix_groups[nt[:25]].append(nid)

# Strategy 2: First-author + year groups (catches title changes)
author_year_groups = defaultdict(list)
for nid in nodes:
    r = id_to_ranking.get(nid)
    if r and r.get("authors"):
        last = extract_last_name(r["authors"][0])
        year = nodes[nid].get("year", 0) or 0
        if last and year:
            # Group by author + year window
            for y in range(year - 1, year + 2):
                author_year_groups[(last, y)].append(nid)

# Strategy 3: bioRxiv papers matched against same-year published papers
# (already covered by Strategy 2 if first author matches)

# Deduplicate candidate pairs
candidate_pairs = set()

def add_candidates(groups, max_group_size=50):
    for key, group in groups.items():
        if len(group) < 2 or len(group) > max_group_size:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                if a > b:
                    a, b = b, a
                candidate_pairs.add((a, b))

add_candidates(title_prefix_groups)
add_candidates(author_year_groups)

print(f"  {len(candidate_pairs)} candidate pairs to evaluate")

# ── Evaluate all candidates ──────────────────────────────────────────────

print("Computing signals for each pair...")
results = []

for a_id, b_id in candidate_pairs:
    na = nodes.get(a_id, {})
    nb = nodes.get(b_id, {})

    # Quick year filter
    ya = na.get("year", 0) or 0
    yb = nb.get("year", 0) or 0
    if abs(ya - yb) > 3:
        continue

    signals = compute_signals(a_id, b_id)
    confidence = composite_confidence(signals)

    if confidence < 0.30:
        continue

    # Determine category
    if confidence >= 0.70:
        category = "AUTO_MERGE"
    elif confidence >= 0.50:
        category = "LIKELY_DUP"
    elif confidence >= 0.40:
        category = "REVIEW"
    else:
        category = "LOW"

    # Determine which is preprint
    doi_a = na.get("doi", "") or ""
    doi_b = nb.get("doi", "") or ""
    preprint_label = ""
    if is_preprint_doi(doi_a) and not is_preprint_doi(doi_b):
        preprint_label = "A=preprint"
    elif is_preprint_doi(doi_b) and not is_preprint_doi(doi_a):
        preprint_label = "B=preprint"
    elif doi_a != doi_b:
        preprint_label = "diff_DOIs"

    rank_a = rank_by_id.get(a_id, 9999)
    rank_b = rank_by_id.get(b_id, 9999)
    in_500_a = a_id in top500_ids
    in_500_b = b_id in top500_ids

    results.append({
        "a_id": a_id, "b_id": b_id,
        "title_a": na.get("title", ""), "title_b": nb.get("title", ""),
        "year_a": ya, "year_b": yb,
        "doi_a": doi_a, "doi_b": doi_b,
        "cites_a": na.get("cited_by_count", 0), "cites_b": nb.get("cited_by_count", 0),
        "rank_a": rank_a, "rank_b": rank_b,
        "in_500_a": in_500_a, "in_500_b": in_500_b,
        "journal_a": na.get("journal", ""), "journal_b": nb.get("journal", ""),
        "preprint_label": preprint_label,
        "confidence": confidence,
        "category": category,
        **signals,
    })

results.sort(key=lambda x: -x["confidence"])

# ── Summary stats ────────────────────────────────────────────────────────

auto_merge = [r for r in results if r["category"] == "AUTO_MERGE"]
likely_dup = [r for r in results if r["category"] == "LIKELY_DUP"]
review = [r for r in results if r["category"] == "REVIEW"]
low = [r for r in results if r["category"] == "LOW"]

both_in_500 = [r for r in results if r["in_500_a"] and r["in_500_b"] and r["confidence"] >= 0.50]
would_enter = []
score_500 = rankings[499]["composite_score"] if len(rankings) >= 500 else 0

for r in results:
    if r["confidence"] < 0.50:
        continue
    ra = id_to_ranking.get(r["a_id"])
    rb = id_to_ranking.get(r["b_id"])
    if not ra or not rb:
        continue
    combined_score = ra["composite_score"] + rb["composite_score"]
    best_rank = min(r["rank_a"], r["rank_b"])
    if best_rank > 500 and combined_score >= score_500:
        would_enter.append({**r, "combined_score": combined_score, "best_rank": best_rank})

print()
print(f"=== DEDUP SUMMARY ===")
print(f"  AUTO_MERGE (conf ≥ 0.70):  {len(auto_merge)}")
print(f"  LIKELY_DUP (conf ≥ 0.50):  {len(likely_dup)}")
print(f"  REVIEW     (conf ≥ 0.40):  {len(review)}")
print(f"  LOW        (conf ≥ 0.30):  {len(low)}")
print(f"  Total pairs:               {len(results)}")
print()
print(f"  Both versions in top 500:  {len(both_in_500)}")
print(f"  Would enter top 500:       {len(would_enter)}")

# ── Write TSV for human review ───────────────────────────────────────────

tsv_path = OUT / "duplicate_review.tsv"
with open(tsv_path, "w") as f:
    headers = [
        "category", "confidence", "title_sim", "citation_sim", "out_jaccard",
        "in_jaccard", "author_overlap", "preprint_signal", "mutual_cite",
        "preprint_label", "rank_a", "rank_b", "in_500_a", "in_500_b",
        "cites_a", "cites_b", "year_a", "year_b",
        "title_a", "title_b", "doi_a", "doi_b",
        "journal_a", "journal_b", "decision",
    ]
    f.write("\t".join(headers) + "\n")
    for r in results:
        row = [
            r["category"],
            f"{r['confidence']:.3f}",
            f"{r['title_sim']:.3f}",
            f"{r['citation_sim']:.3f}",
            f"{r['out_jaccard']:.3f}",
            f"{r['in_jaccard']:.3f}",
            f"{r['author_overlap']:.1f}",
            f"{r['preprint_signal']:.1f}",
            str(r["mutual_cite"]),
            r["preprint_label"],
            str(r["rank_a"]),
            str(r["rank_b"]),
            str(r["in_500_a"]),
            str(r["in_500_b"]),
            str(r["cites_a"]),
            str(r["cites_b"]),
            str(r["year_a"]),
            str(r["year_b"]),
            r["title_a"],
            r["title_b"],
            r["doi_a"],
            r["doi_b"],
            r["journal_a"],
            r["journal_b"],
            "",  # human decision column (blank)
        ]
        f.write("\t".join(row) + "\n")

print(f"\n  Wrote {tsv_path}  ({len(results)} pairs)")

# ── Write markdown report ────────────────────────────────────────────────

md_path = OUT / "duplicate_review.md"
with open(md_path, "w") as f:
    f.write("# Duplicate Review Report\n\n")
    f.write("Multi-signal duplicate detection using five independent signals:\n")
    f.write("title similarity, DOI pattern, citation neighborhood Jaccard,\n")
    f.write("author overlap, and mutual non-citation.\n\n")
    f.write("**Decision column**: mark each pair as `merge`, `keep_both`, or `investigate`.\n\n")

    f.write(f"## Summary\n\n")
    f.write(f"| Category | Count | Action |\n")
    f.write(f"| --- | --- | --- |\n")
    f.write(f"| AUTO_MERGE (conf ≥ 0.70) | {len(auto_merge)} | Merge unless flagged |\n")
    f.write(f"| LIKELY_DUP (conf ≥ 0.50) | {len(likely_dup)} | Review, likely merge |\n")
    f.write(f"| REVIEW (conf ≥ 0.40) | {len(review)} | Human judgment needed |\n")
    f.write(f"| LOW (conf ≥ 0.30) | {len(low)} | Probably not duplicates |\n")
    f.write(f"\n")
    f.write(f"Both versions in top 500 (wasting slots): **{len(both_in_500)}**\n")
    f.write(f"Would enter top 500 if merged: **{len(would_enter)}**\n\n")

    f.write("## Signal Weights\n\n")
    f.write("| Signal | Weight | What it catches |\n")
    f.write("| --- | --- | --- |\n")
    f.write("| Title similarity | 0.35 | Same or near-same titles |\n")
    f.write("| Citation neighborhood | 0.25 | Shared references + citers (catches title changes) |\n")
    f.write("| Author overlap | 0.15 | Same first/last author |\n")
    f.write("| Mutual non-citation | 0.15 | True dupes don't cite each other |\n")
    f.write("| Preprint DOI pattern | 0.10 | bioRxiv/arXiv DOI prefix |\n\n")

    f.write("## Confidence Interpretation\n\n")
    f.write("- **≥ 0.90**: Near-certain duplicate (high title + citations + author + preprint)\n")
    f.write("- **0.70–0.89**: Very likely duplicate, auto-merge unless flagged\n")
    f.write("- **0.50–0.69**: Likely duplicate, needs quick human check\n")
    f.write("- **0.40–0.49**: Possible duplicate, needs investigation\n")
    f.write("- **0.30–0.39**: Unlikely duplicate, included for completeness\n\n")

    # AUTO_MERGE section
    f.write(f"## AUTO_MERGE ({len(auto_merge)} pairs)\n\n")
    for i, r in enumerate(auto_merge, 1):
        label = f" `{r['preprint_label']}`" if r["preprint_label"] else ""
        in500 = ""
        if r["in_500_a"] and r["in_500_b"]:
            in500 = " **⚠ BOTH IN TOP 500**"
        elif r["in_500_a"] or r["in_500_b"]:
            in500 = " (one in top 500)"
        f.write(f"**{i}.** conf={r['confidence']:.3f} title={r['title_sim']:.2f} cit={r['citation_sim']:.2f} auth={r['author_overlap']:.1f}{label}{in500}\n")
        f.write(f"- A #{r['rank_a']}: [{r['year_a']}] {r['title_a'][:90]}  ({r['cites_a']} cites)\n")
        f.write(f"- B #{r['rank_b']}: [{r['year_b']}] {r['title_b'][:90]}  ({r['cites_b']} cites)\n")
        f.write(f"- Decision: ___________\n\n")

    # LIKELY_DUP section
    f.write(f"## LIKELY_DUP ({len(likely_dup)} pairs)\n\n")
    for i, r in enumerate(likely_dup, 1):
        label = f" `{r['preprint_label']}`" if r["preprint_label"] else ""
        f.write(f"**{i}.** conf={r['confidence']:.3f} title={r['title_sim']:.2f} cit={r['citation_sim']:.2f} auth={r['author_overlap']:.1f}{label}\n")
        f.write(f"- A #{r['rank_a']}: [{r['year_a']}] {r['title_a'][:90]}  ({r['cites_a']} cites)\n")
        f.write(f"- B #{r['rank_b']}: [{r['year_b']}] {r['title_b'][:90]}  ({r['cites_b']} cites)\n")
        f.write(f"- Decision: ___________\n\n")

    # REVIEW section
    f.write(f"## REVIEW ({len(review)} pairs)\n\n")
    for i, r in enumerate(review, 1):
        label = f" `{r['preprint_label']}`" if r["preprint_label"] else ""
        f.write(f"**{i}.** conf={r['confidence']:.3f} title={r['title_sim']:.2f} cit={r['citation_sim']:.2f} auth={r['author_overlap']:.1f}{label}\n")
        f.write(f"- A #{r['rank_a']}: [{r['year_a']}] {r['title_a'][:90]}  ({r['cites_a']} cites)\n")
        f.write(f"- B #{r['rank_b']}: [{r['year_b']}] {r['title_b'][:90]}  ({r['cites_b']} cites)\n")
        f.write(f"- Decision: ___________\n\n")

    # Would-enter-top-500 section
    if would_enter:
        f.write(f"## Papers That Would Enter Top 500 If Merged ({len(would_enter)})\n\n")
        for r in would_enter:
            f.write(f"- #{r['best_rank']} → ~#{int(500 * score_500 / r['combined_score'])} | ")
            f.write(f"**{r['title_a'][:70]}** ({r['cites_a']}+{r['cites_b']} cites)\n")
        f.write("\n")

print(f"  Wrote {md_path}")
print("\nDone.")
