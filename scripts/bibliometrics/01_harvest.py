#!/usr/bin/env python3
"""
Step 1: Harvest connectomics papers from OpenAlex.

Three independent corpus construction paths:
  A) Auto-seed from OpenAlex → 1-hop citation expansion (adaptive to 2-hop)
  B) Keyword/concept search
  C) Dataset-anchored (papers citing landmark datasets)

Outputs: output/corpus_a.json, corpus_b.json, corpus_c.json, corpus_merged.json

Usage:
  python 01_harvest.py                # Run all three paths
  python 01_harvest.py --corpus a     # Just corpus A
  python 01_harvest.py --corpus b     # Just corpus B
  python 01_harvest.py --corpus c     # Just corpus C
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import re

from config import (
    AUTO_SEED_QUERIES, EXTRA_SEED_DOIS, KEYWORD_QUERIES,
    KEYWORD_MIN_CITATIONS, KEYWORD_MIN_YEAR, KEYWORD_MAX_RESULTS_PER_QUERY,
    DATASET_ANCHOR_DOIS, DATASET_MAX_CITERS,
    EXPANSION_MIN_SEED_CONNECTIONS, EXPANSION_MAX_CITED_BY,
    EXPANSION_MARGINAL_GAIN_THRESHOLD, MAX_CORPUS_SIZE,
    TECHNIQUE_MIN_PAPERS, OUTPUT_DIR,
    MACRO_EXCLUSION_TERMS, NANOSCALE_KEEP_TERMS,
)
from openalex_client import OpenAlexClient


def normalize_work(work):
    """
    Extract a normalized paper record from an OpenAlex work object.

    Returns dict with: openalex_id, doi, title, authors, year,
    cited_by_count, concepts, referenced_works, type, journal
    """
    if not work:
        return None
    authors = []
    for authorship in work.get("authorships", []):
        author = authorship.get("author", {})
        authors.append({
            "id": author.get("id", ""),
            "name": author.get("display_name", ""),
        })
    concepts = [
        {"id": c.get("id", ""), "name": c.get("display_name", ""),
         "score": c.get("score", 0)}
        for c in work.get("concepts", [])
    ]
    source = work.get("primary_location", {}).get("source") or {}
    return {
        "openalex_id": work.get("id", ""),
        "doi": (work.get("doi") or "").replace("https://doi.org/", ""),
        "title": work.get("title", ""),
        "authors": authors,
        "year": work.get("publication_year"),
        "cited_by_count": work.get("cited_by_count", 0),
        "concepts": concepts,
        "referenced_works": work.get("referenced_works", []),
        "type": work.get("type", ""),
        "journal": source.get("display_name", ""),
    }


# ── Macro-Connectomics Exclusion Filter ───────────────────────────────

def _text_matches_any(text, terms):
    """Check if lowered text contains any of the terms."""
    text = text.lower()
    return any(t in text for t in terms)


def filter_macro_connectomics(papers):
    """
    Remove macro-connectomics papers (dMRI, fMRI, resting-state, tractography)
    UNLESS they also contain nanoscale indicators (EM, synapse, graph theory).

    Returns (kept, removed_count).
    """
    kept = []
    removed = 0
    for paper in papers:
        title = (paper.get("title") or "").lower()
        abstract = (paper.get("abstract") or "").lower()
        text = f"{title} {abstract}"

        has_macro = _text_matches_any(text, MACRO_EXCLUSION_TERMS)
        has_nano = _text_matches_any(text, NANOSCALE_KEEP_TERMS)

        if has_macro and not has_nano:
            removed += 1
        else:
            kept.append(paper)

    if removed:
        print(f"  Filtered {removed} macro-connectomics papers (dMRI/fMRI)")
    return kept, removed


# ── Corpus A: Auto-Seed + Citation Expansion ─────────────────────────

def build_auto_seed(client):
    """
    Build seed set from OpenAlex using queries in config.AUTO_SEED_QUERIES.
    Returns list of normalized work dicts.
    """
    seen_ids = set()
    seeds = []

    for search_type, query, top_n in AUTO_SEED_QUERIES:
        print(f"  Auto-seed query: {search_type} '{query}' (top {top_n})")
        if search_type == "concept":
            works = client.search_works_by_concept(query, max_results=top_n)
        elif search_type == "title":
            works = client.search_works_by_title(query, max_results=top_n)
        else:
            works = client.search_works(query, max_results=top_n)

        for w in works:
            oa_id = w.get("id", "")
            if oa_id and oa_id not in seen_ids:
                seen_ids.add(oa_id)
                norm = normalize_work(w)
                if norm:
                    seeds.append(norm)

    # Add any manually specified DOIs
    for doi in EXTRA_SEED_DOIS:
        w = client.get_work_by_doi(doi)
        if w and w.get("id") not in seen_ids:
            seen_ids.add(w["id"])
            norm = normalize_work(w)
            if norm:
                seeds.append(norm)

    print(f"  Auto-seed: {len(seeds)} papers")
    return seeds


def expand_citations(client, seeds, max_hops=2):
    """
    Citation chasing from seed papers.

    For each seed: fetch forward citations + backward references.
    Keep papers connected to >= EXPANSION_MIN_SEED_CONNECTIONS seeds.
    Adaptive: expand to hop 2 only if marginal gain threshold met.

    Returns list of normalized work dicts (includes seeds).
    """
    corpus = {w["openalex_id"]: w for w in seeds}
    seed_ids = set(corpus.keys())

    # Track how many seeds connect to each discovered paper
    connection_count = Counter()

    for hop in range(1, max_hops + 1):
        print(f"\n  Hop {hop}: expanding from {len(corpus)} papers...")
        new_papers = {}
        source_ids = seed_ids if hop == 1 else set(new_papers.keys())

        for i, sid in enumerate(source_ids):
            if i % 50 == 0:
                print(f"    Processing {i}/{len(source_ids)}...")

            work = corpus.get(sid) or {}
            oa_id = sid.replace("https://openalex.org/", "")

            # Backward: referenced_works (already in the work object)
            for ref_id in work.get("referenced_works", []):
                connection_count[ref_id] += 1

            # Forward: papers citing this one
            citers = client.get_cited_by(oa_id, max_results=EXPANSION_MAX_CITED_BY)
            for citer in citers:
                citer_id = citer.get("id", "")
                if citer_id:
                    connection_count[citer_id] += 1

        # Add papers meeting connection threshold
        before_count = len(corpus)
        candidates = [
            oa_id for oa_id, count in connection_count.items()
            if count >= EXPANSION_MIN_SEED_CONNECTIONS
            and oa_id not in corpus
        ]
        print(f"    {len(candidates)} candidates meet threshold...")

        for oa_id in candidates:
            if len(corpus) >= MAX_CORPUS_SIZE:
                print(f"    Hit corpus size cap ({MAX_CORPUS_SIZE})")
                break
            w = client.get_work(oa_id)
            norm = normalize_work(w)
            if norm:
                norm["hop_distance"] = hop
                norm["seed_connections"] = connection_count[oa_id]
                corpus[norm["openalex_id"]] = norm

        after_count = len(corpus)
        gain = (after_count - before_count) / max(before_count, 1)
        print(f"    Hop {hop}: {before_count} → {after_count} "
              f"(+{after_count - before_count}, gain={gain:.2%})")

        if gain < EXPANSION_MARGINAL_GAIN_THRESHOLD:
            print(f"    Marginal gain below threshold, stopping expansion.")
            break

    return list(corpus.values())


def build_corpus_a(client):
    """Build Corpus A: auto-seed + citation expansion."""
    print("\n=== Corpus A: Auto-Seed + Citation Expansion ===")
    seeds = build_auto_seed(client)
    seeds, _ = filter_macro_connectomics(seeds)
    expanded = expand_citations(client, seeds)
    expanded, _ = filter_macro_connectomics(expanded)
    return expanded


# ── Corpus B: Keyword Search ─────────────────────────────────────────

def build_corpus_b(client):
    """Build Corpus B: keyword/concept search, independent of seeds."""
    print("\n=== Corpus B: Keyword Search ===")
    seen_ids = set()
    corpus = []
    filters = {
        "publication_year": f">{KEYWORD_MIN_YEAR}",
        "cited_by_count": f">{KEYWORD_MIN_CITATIONS}",
    }

    for query in KEYWORD_QUERIES:
        print(f"  Searching: {query}")
        works = client.search_works(
            query, filters=filters,
            max_results=KEYWORD_MAX_RESULTS_PER_QUERY
        )
        for w in works:
            oa_id = w.get("id", "")
            if oa_id and oa_id not in seen_ids:
                seen_ids.add(oa_id)
                norm = normalize_work(w)
                if norm:
                    corpus.append(norm)

    print(f"  Corpus B (pre-filter): {len(corpus)} papers")
    corpus, _ = filter_macro_connectomics(corpus)
    print(f"  Corpus B (post-filter): {len(corpus)} papers")
    return corpus


# ── Corpus C: Dataset-Anchored ───────────────────────────────────────

def build_corpus_c(client):
    """Build Corpus C: papers citing landmark dataset releases."""
    print("\n=== Corpus C: Dataset-Anchored ===")
    seen_ids = set()
    corpus = []

    for doi in DATASET_ANCHOR_DOIS:
        print(f"  Dataset: {doi}")
        work = client.get_work_by_doi(doi)
        if not work:
            print(f"    Not found in OpenAlex, skipping")
            continue

        oa_id = work.get("id", "")
        # Add the dataset paper itself
        if oa_id and oa_id not in seen_ids:
            seen_ids.add(oa_id)
            norm = normalize_work(work)
            if norm:
                norm["is_dataset_anchor"] = True
                corpus.append(norm)

        # Fetch papers citing this dataset
        citers = client.get_cited_by(oa_id, max_results=DATASET_MAX_CITERS)
        print(f"    {len(citers)} citing papers")
        for citer in citers:
            cid = citer.get("id", "")
            if cid and cid not in seen_ids:
                seen_ids.add(cid)
                norm = normalize_work(citer)
                if norm:
                    corpus.append(norm)

    print(f"  Corpus C (pre-filter): {len(corpus)} papers")
    corpus, _ = filter_macro_connectomics(corpus)
    print(f"  Corpus C (post-filter): {len(corpus)} papers")
    return corpus


# ── Merge ─────────────────────────────────────────────────────────────

def merge_corpora(corpus_a, corpus_b, corpus_c):
    """
    Merge three corpora into one, deduplicating by OpenAlex ID.
    Tags each paper with provenance (which corpus/corpora it appeared in).
    """
    merged = {}
    for paper in corpus_a:
        pid = paper["openalex_id"]
        if pid not in merged:
            paper["provenance"] = {"a": True, "b": False, "c": False}
            merged[pid] = paper
        else:
            merged[pid]["provenance"]["a"] = True

    for paper in corpus_b:
        pid = paper["openalex_id"]
        if pid not in merged:
            paper["provenance"] = {"a": False, "b": True, "c": False}
            merged[pid] = paper
        else:
            merged[pid]["provenance"]["b"] = True

    for paper in corpus_c:
        pid = paper["openalex_id"]
        if pid not in merged:
            paper["provenance"] = {"a": False, "b": False, "c": True}
            merged[pid] = paper
        else:
            merged[pid]["provenance"]["c"] = True

    result = list(merged.values())
    # Stats
    a_only = sum(1 for p in result if p["provenance"]["a"] and not p["provenance"]["b"] and not p["provenance"]["c"])
    b_only = sum(1 for p in result if p["provenance"]["b"] and not p["provenance"]["a"] and not p["provenance"]["c"])
    c_only = sum(1 for p in result if p["provenance"]["c"] and not p["provenance"]["a"] and not p["provenance"]["b"])
    all_three = sum(1 for p in result if p["provenance"]["a"] and p["provenance"]["b"] and p["provenance"]["c"])
    print(f"\n=== Merged Corpus ===")
    print(f"  Total: {len(result)}")
    print(f"  A only: {a_only}, B only: {b_only}, C only: {c_only}")
    print(f"  In all three: {all_three}")
    return result


def save_corpus(corpus, filename):
    """Save corpus to JSON."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    with open(path, "w") as f:
        json.dump(corpus, f, indent=2)
    print(f"  Saved {len(corpus)} papers to {path}")


def main():
    parser = argparse.ArgumentParser(description="Harvest connectomics papers from OpenAlex")
    parser.add_argument("--corpus", choices=["a", "b", "c"], default=None,
                        help="Build only one corpus (default: all three)")
    args = parser.parse_args()

    client = OpenAlexClient()

    corpus_a = corpus_b = corpus_c = []

    if args.corpus in (None, "a"):
        corpus_a = build_corpus_a(client)
        save_corpus(corpus_a, "corpus_a.json")

    if args.corpus in (None, "b"):
        corpus_b = build_corpus_b(client)
        save_corpus(corpus_b, "corpus_b.json")

    if args.corpus in (None, "c"):
        corpus_c = build_corpus_c(client)
        save_corpus(corpus_c, "corpus_c.json")

    if args.corpus is None:
        merged = merge_corpora(corpus_a, corpus_b, corpus_c)
        save_corpus(merged, "corpus_merged.json")


if __name__ == "__main__":
    main()
