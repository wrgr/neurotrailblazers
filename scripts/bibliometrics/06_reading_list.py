#!/usr/bin/env python3
"""
Step 6: Generate a structured reading list with prerequisite ordering.

Algorithm:
  1. Load ALL ranked papers
  2. Hard-filter: keep only papers where title/abstract/concepts contain
     nanoscale connectomics terms  →  removes off-topic high-citation papers
     (BLAST, Benjamini-Hochberg, carbon nanotubes, etc.)
  3. Take top-N survivors by composite score
  4. Topological sort on internal citation subgraph (prerequisites first)
  5. Assign reading phases: Orientation → Foundations → Methods → Datasets → Frontiers
  6. Output reading_list.json + reading_list.md

Why the nanoscale pre-filter is necessary:
  The corpus was built by citation chasing from EM connectomics seeds.
  Connectomics papers cite general methods (Fiji, U-Net, BLAST) heavily,
  so those papers accumulate high in-degree and PageRank in our graph.
  They are useful tools but not connectomics reading material.

Usage:
  python 06_reading_list.py
  python 06_reading_list.py --top 500
"""
import argparse
import json
import re
from collections import defaultdict, deque
from pathlib import Path

from config import OUTPUT_DIR, NANOSCALE_KEEP_TERMS, TECHNIQUE_FAMILIES, CACHE_DIR

# ── Connectomics relevance filter ────────────────────────────────────
# A paper passes if title OR abstract OR ≥1 concept matches any term.
# Using a broader set than NANOSCALE_KEEP_TERMS to catch review papers
# that use field-level language.
CONNECTOMICS_TERMS = [
    # Core scope
    "connectom", "connectomics",
    "electron microscopy", "electron micrograph",
    "synapse", "synaptic", "synapses",
    "nanoscale", "ultrastructure",
    "neural circuit", "neural wiring",
    # Volume EM techniques
    "serial section", "serial block", "sbem", "fib-sem", "fibsem",
    "focused ion beam", "atum", "gridtape", "multibeam", "multi-beam",
    "volume em", "volume electron",
    # Non-EM nanoscale
    "expansion microscopy", "exm",
    "mapseq", "barseq", "bricseg", "barcod",
    "array tomography",
    "nanotomography", "nano-ct",
    # Reconstruction & tools
    "neuron segmentation", "neuronal segmentation",
    "synapse detection",
    "flood-filling", "flood filling",
    "proofreading", "reconstruction of",
    "catmaid", "webknossos", "flywire", "hemibrain",
    "microns", "neuprint", "bossdb",
    # Datasets
    "drosophila connectome", "c. elegans connectome",
    "whole-brain connectome", "dense reconstruction",
    "fafb", "h01",
    # Graph theory applied to connectomes
    "connectome graph", "wiring diagram",
    "neuronal graph", "brain graph",
]

NOISE_COMMUNITY_LABELS = {
    "geology", "seismology", "chromatography", "mass spectrometry",
    "apoptosis", "autophagy", "biochemistry",
}

ROLE_ORDER = {"review": 0, "methods": 1, "dataset": 2, "biology": 3}


def load_data():
    def load(f):
        with open(OUTPUT_DIR / f) as fh:
            return json.load(fh)
    return load("paper_rankings.json"), load("communities.json"), load("corpus_merged.json")


def reconstruct_abstract(openalex_id):
    """Reconstruct abstract text from OpenAlex inverted index in cache."""
    safe_id = openalex_id.replace("https://openalex.org/", "")
    cache_path = CACHE_DIR / "works" / f"{safe_id}.json"
    if not cache_path.exists():
        return ""
    try:
        with open(cache_path) as f:
            work = json.load(f)
        aii = work.get("abstract_inverted_index") or {}
        if not aii:
            return ""
        max_pos = max(pos for positions in aii.values() for pos in positions)
        words = [""] * (max_pos + 1)
        for word, positions in aii.items():
            for pos in positions:
                if 0 <= pos <= max_pos:
                    words[pos] = word
        return " ".join(w for w in words if w)
    except Exception:
        return ""


def is_connectomics_relevant(paper, abstract=""):
    """
    Return True if the paper is relevant to nanoscale connectomics.
    Checks title, abstract, and OpenAlex concepts.
    """
    title = (paper.get("title") or "").lower()
    abstract_lower = abstract.lower()
    concept_text = " ".join(
        c.get("name", "").lower() for c in paper.get("concepts", [])
    )
    combined = f"{title} {abstract_lower} {concept_text}"
    return any(term in combined for term in CONNECTOMICS_TERMS)


def build_community_map(communities):
    paper_to_community = {}
    community_info = {}
    for c in communities:
        cid = c["community_id"]
        top_labels = [x["name"].lower() for x in c.get("top_concepts", [])[:3]]
        is_noise = any(n in " ".join(top_labels) for n in NOISE_COMMUNITY_LABELS)
        label = " / ".join(x["name"] for x in c.get("top_concepts", [])[:2])
        community_info[cid] = {
            "label": label,
            "top_authors": [a["name"] for a in c.get("top_authors", [])[:2]],
            "size": c["size"],
            "year_range": c["year_range"],
            "is_noise": is_noise,
        }
        for pid in c.get("members", []):
            paper_to_community[pid] = cid
    return paper_to_community, community_info


def topological_sort(papers, corpus_lookup):
    """Kahn's algorithm: prerequisites before papers that cite them."""
    ids = {p["openalex_id"] for p in papers}
    in_edges = defaultdict(set)
    out_edges = defaultdict(set)

    for p in papers:
        pid = p["openalex_id"]
        for ref in corpus_lookup.get(pid, {}).get("referenced_works", []):
            if ref in ids:
                in_edges[pid].add(ref)
                out_edges[ref].add(pid)

    def sort_key(pid):
        p = next((x for x in papers if x["openalex_id"] == pid), {})
        return (p.get("year") or 9999, ROLE_ORDER.get(p.get("role", "methods"), 1))

    queue = deque(sorted(
        [p["openalex_id"] for p in papers if not in_edges[p["openalex_id"]]],
        key=sort_key
    ))
    paper_lookup = {p["openalex_id"]: p for p in papers}
    order, visited = [], set()

    while queue:
        pid = queue.popleft()
        if pid in visited:
            continue
        visited.add(pid)
        order.append(pid)
        ready = sorted(
            [s for s in out_edges[pid] if s not in visited and in_edges[s] <= visited],
            key=sort_key
        )
        queue.extend(ready)

    for p in sorted(papers, key=lambda x: (x.get("year") or 9999)):
        if p["openalex_id"] not in visited:
            order.append(p["openalex_id"])

    return order


def assign_phase(paper, year):
    role = paper.get("role", "methods")
    if role == "review":
        return "0_orientation"
    if year < 2010:
        return "1_foundations"
    if role == "dataset":
        return "3_landmark_datasets"
    if year >= 2021:
        return "4_frontiers"
    return "2_core_methods"


PHASE_NAMES = {
    "0_orientation":       "Phase 0 — Orientation  (reviews; read first)",
    "1_foundations":       "Phase 1 — Foundations  (seminal pre-2010 work)",
    "2_core_methods":      "Phase 2 — Core Methods & Tools  (2010–2020)",
    "3_landmark_datasets": "Phase 3 — Landmark Datasets",
    "4_frontiers":         "Phase 4 — Frontiers  (2021–present)",
}


def generate_markdown(reading_list):
    lines = [
        "# EM Connectomics Reading List\n",
        "> **How to use**: Read phases in order. Within each phase, follow the numbered order — "
        "citation prerequisites are resolved so each paper appears after the papers it builds on.\n",
        "> **Scoring**: composite = 0.35×PageRank + 0.25×citations + 0.20×betweenness + 0.20×recent_PageRank\n",
        f"> **Coverage**: {len(reading_list)} papers across {len(set(e['phase'] for e in reading_list))} phases\n",
    ]

    current_phase = None
    current_community = None

    for entry in reading_list:
        phase = entry["phase"]
        comm = entry["community_label"]

        if phase != current_phase:
            current_phase = phase
            current_community = None
            lines.append(f"\n---\n\n## {PHASE_NAMES.get(phase, phase)}\n")

        if comm != current_community:
            current_community = comm
            top_authors = ", ".join(entry.get("community_top_authors", []))
            lines.append(f"\n### {comm}  _{top_authors}_\n")

        doi = entry.get("doi", "")
        authors = entry.get("authors", [])
        authors_str = ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else "")
        role_badge = f"`{entry.get('role','').upper()}`"
        score = entry.get("composite_score", 0)

        lines.append(
            f"**{entry['reading_order']}. {entry.get('title','').rstrip('.')}**  \n"
            f"{authors_str} · {entry.get('year','?')} · *{entry.get('journal','')}*  \n"
            f"{role_badge} · citations: {entry.get('total_citations',0):,} · "
            f"score: {score:.3f}"
            + (f" · [doi](https://doi.org/{doi})" if doi else "") + "  \n\n"
        )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=500,
                        help="Target number of connectomics-relevant papers")
    args = parser.parse_args()

    print("Loading data...")
    rankings, communities, corpus = load_data()
    corpus_lookup = {p["openalex_id"]: p for p in corpus}

    paper_to_community, community_info = build_community_map(communities)

    # ── Step 1: connectomics relevance pre-filter ──────────────────
    print(f"\nFiltering {len(rankings)} ranked papers for connectomics relevance...")
    passed, filtered_out = [], []
    for p in rankings:
        pid = p["openalex_id"]
        abstract = reconstruct_abstract(pid)
        # Merge concepts from corpus record
        corpus_p = corpus_lookup.get(pid, {})
        p["concepts"] = corpus_p.get("concepts", [])
        p["abstract"] = abstract

        cid = paper_to_community.get(pid)
        community_is_noise = cid is not None and community_info[cid]["is_noise"]

        if community_is_noise:
            filtered_out.append(("noise_community", p.get("title", "")))
        elif not is_connectomics_relevant(p, abstract):
            filtered_out.append(("off_topic", p.get("title", "")))
        else:
            passed.append(p)

    noise_count = sum(1 for reason, _ in filtered_out if reason == "noise_community")
    offtopic_count = sum(1 for reason, _ in filtered_out if reason == "off_topic")
    print(f"  Passed:   {len(passed)}")
    print(f"  Filtered: {len(filtered_out)} total")
    print(f"    → noise communities: {noise_count}")
    print(f"    → off-topic (no connectomics terms): {offtopic_count}")
    print(f"  Sample filtered-out papers:")
    for reason, title in filtered_out[:8]:
        print(f"    [{reason}] {title[:70]}")

    # Take top-N survivors (already sorted by composite_score from rankings)
    candidates = passed[:args.top]
    print(f"\nTop {len(candidates)} connectomics papers selected")

    # ── Step 2: topological sort ────────────────────────────────────
    print("Topological sort (resolving citation prerequisites)...")
    order = topological_sort(candidates, corpus_lookup)

    # ── Step 3: assemble reading list ───────────────────────────────
    paper_lookup = {p["openalex_id"]: p for p in candidates}
    reading_list = []

    for pos, pid in enumerate(order):
        p = paper_lookup.get(pid)
        if not p:
            continue
        year = p.get("year") or 2000
        cid = paper_to_community.get(pid, -1)
        cinfo = community_info.get(cid, {})
        phase = assign_phase(p, year)

        reading_list.append({
            "openalex_id": pid,
            "doi": p.get("doi", ""),
            "title": p.get("title", ""),
            "authors": [a.get("name", "") for a in corpus_lookup.get(pid, {}).get("authors", [])[:6]],
            "year": year,
            "journal": p.get("journal", ""),
            "role": p.get("role", ""),
            "total_citations": p.get("total_citations", 0),
            "composite_score": round(p.get("composite_score", 0), 4),
            "pagerank": round(p.get("pagerank", 0), 6),
            "betweenness": round(p.get("betweenness", 0), 6),
            "abstract": p.get("abstract", ""),
            "concepts": [c.get("name", "") for c in p.get("concepts", [])[:8]],
            "phase": phase,
            "community_id": cid,
            "community_label": cinfo.get("label", "Other"),
            "community_top_authors": cinfo.get("top_authors", []),
        })

    # Sort within phases: community → year → role
    reading_list.sort(key=lambda x: (
        x["phase"],
        x["community_label"],
        x.get("year") or 9999,
        ROLE_ORDER.get(x.get("role", "methods"), 1),
    ))
    for i, entry in enumerate(reading_list, 1):
        entry["reading_order"] = i

    # ── Step 4: save outputs ────────────────────────────────────────
    out_path = OUTPUT_DIR / "reading_list.json"
    with open(out_path, "w") as f:
        json.dump(reading_list, f, indent=2)
    print(f"\nSaved {len(reading_list)} papers → {out_path}")

    md = generate_markdown(reading_list)
    md_path = OUTPUT_DIR / "reading_list.md"
    with open(md_path, "w") as f:
        f.write(md)
    print(f"Saved → {md_path}")

    # ── Summary ─────────────────────────────────────────────────────
    phases = defaultdict(list)
    for e in reading_list:
        phases[e["phase"]].append(e)

    print()
    for key in sorted(phases):
        entries = phases[key]
        comms = len(set(e["community_label"] for e in entries))
        print(f"  {PHASE_NAMES[key]}")
        print(f"    {len(entries)} papers · {comms} communities")
        for e in entries[:4]:
            print(f"    → [{e['year']}] {e['title'][:65]}...")
        print()


if __name__ == "__main__":
    main()
