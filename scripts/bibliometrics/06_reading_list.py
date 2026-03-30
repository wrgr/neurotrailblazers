#!/usr/bin/env python3
"""
Step 6: Generate a structured reading list with prerequisite ordering.

Algorithm:
  1. Take top-N papers by composite score (default 150)
  2. Filter to connectomics-relevant communities (exclude corpus noise)
  3. Build citation subgraph among these papers
  4. Topological sort → prerequisites always precede the papers that cite them
  5. Group into phases: Foundations → Methods → Datasets → Frontiers
  6. Output reading_list.json + reading_list.md

Usage:
  python 06_reading_list.py
  python 06_reading_list.py --top 200
"""
import argparse
import json
from collections import defaultdict, deque
from pathlib import Path

from config import OUTPUT_DIR

# Communities identified as corpus noise (non-connectomics)
NOISE_COMMUNITY_LABELS = {
    "geology", "seismology", "chromatography", "mass spectrometry",
    "apoptosis", "autophagy", "biochemistry",
}

# Role reading order: reviews orient you, then foundations, methods, datasets, biology
ROLE_ORDER = {"review": 0, "methods": 1, "dataset": 2, "biology": 3}


def load_data():
    def load(f): 
        with open(OUTPUT_DIR / f) as fh: 
            return json.load(fh)
    return (
        load("paper_rankings.json"),
        load("communities.json"),
        load("corpus_merged.json"),
    )


def label_community(community):
    """Return a human-readable label and whether it's noise."""
    top = [c["name"].lower() for c in community.get("top_concepts", [])[:3]]
    authors = [a["name"] for a in community.get("top_authors", [])[:2]]
    is_noise = any(noise in " ".join(top) for noise in NOISE_COMMUNITY_LABELS)
    label = " / ".join(c["name"] for c in community.get("top_concepts", [])[:2])
    return label, authors, is_noise


def build_community_map(communities):
    """Map each paper openalex_id → community_id."""
    paper_to_community = {}
    community_info = {}
    for c in communities:
        cid = c["community_id"]
        label, authors, is_noise = label_community(c)
        community_info[cid] = {
            "label": label,
            "top_authors": authors,
            "size": c["size"],
            "year_range": c["year_range"],
            "is_noise": is_noise,
        }
        for pid in c.get("members", []):
            paper_to_community[pid] = cid
    return paper_to_community, community_info


def topological_sort(papers, corpus_lookup):
    """
    Kahn's algorithm topological sort on internal citation edges.
    Papers that cite nothing internal come first (true foundations).
    Among papers with the same topo-depth, sort by year then role.
    """
    ids = {p["openalex_id"] for p in papers}
    in_edges = defaultdict(set)   # paper → set of internal papers it cites
    out_edges = defaultdict(set)  # paper → set of internal papers that cite it

    for p in papers:
        pid = p["openalex_id"]
        corpus_paper = corpus_lookup.get(pid, {})
        for ref in corpus_paper.get("referenced_works", []):
            if ref in ids:
                in_edges[pid].add(ref)
                out_edges[ref].add(pid)

    # Kahn's BFS
    queue = deque(sorted(
        [p["openalex_id"] for p in papers if not in_edges[p["openalex_id"]]],
        key=lambda pid: (
            next((p["year"] or 9999 for p in papers if p["openalex_id"] == pid), 9999),
            next((ROLE_ORDER.get(p.get("role", "methods"), 1) for p in papers if p["openalex_id"] == pid), 1),
        )
    ))

    paper_lookup = {p["openalex_id"]: p for p in papers}
    order = []
    visited = set()

    while queue:
        pid = queue.popleft()
        if pid in visited:
            continue
        visited.add(pid)
        order.append(pid)
        # Enqueue successors whose all prerequisites are satisfied
        ready = sorted(
            [s for s in out_edges[pid] if s not in visited and in_edges[s] <= visited],
            key=lambda s: (
                paper_lookup.get(s, {}).get("year") or 9999,
                ROLE_ORDER.get(paper_lookup.get(s, {}).get("role", "methods"), 1),
            )
        )
        queue.extend(ready)

    # Append anything not reached (disconnected nodes)
    for p in sorted(papers, key=lambda x: (x.get("year") or 9999)):
        if p["openalex_id"] not in visited:
            order.append(p["openalex_id"])

    return order


def assign_phase(paper, position, total):
    """Assign a reading phase based on role, year, and position."""
    role = paper.get("role", "methods")
    year = paper.get("year") or 2000
    frac = position / max(total, 1)

    if role == "review":
        return "0_orientation"
    if year < 2010 or frac < 0.20:
        return "1_foundations"
    if role == "dataset" or (role == "methods" and year < 2018):
        return "2_core_methods"
    if role == "dataset" and year >= 2018:
        return "3_landmark_datasets"
    if frac > 0.75:
        return "4_frontiers"
    return "2_core_methods"


PHASE_NAMES = {
    "0_orientation":       "Phase 0 — Orientation (read first: reviews & field overviews)",
    "1_foundations":       "Phase 1 — Foundations (seminal papers, pre-2010)",
    "2_core_methods":      "Phase 2 — Core Methods & Tools",
    "3_landmark_datasets": "Phase 3 — Landmark Datasets",
    "4_frontiers":         "Phase 4 — Frontiers (recent, builds on all prior phases)",
}


def generate_markdown(reading_list, community_info):
    lines = ["# Connectomics Reading List\n",
             "> Generated by bibliometric pipeline. Order respects citation prerequisites.\n"]

    current_phase = None
    current_community = None

    for i, entry in enumerate(reading_list, 1):
        phase = entry["phase"]
        comm_label = entry["community_label"]

        if phase != current_phase:
            current_phase = phase
            current_community = None
            lines.append(f"\n## {PHASE_NAMES.get(phase, phase)}\n")

        if comm_label != current_community:
            current_community = comm_label
            lines.append(f"\n### {comm_label}\n")

        doi = entry.get("doi", "")
        doi_link = f"https://doi.org/{doi}" if doi else ""
        authors_str = ", ".join(entry.get("authors", [])[:3])
        if len(entry.get("authors", [])) > 3:
            authors_str += " et al."

        lines.append(
            f"{i}. **{entry['title']}**  \n"
            f"   {authors_str} ({entry.get('year', '?')})  \n"
            f"   *{entry.get('role','').title()}* | "
            f"Citations: {entry.get('total_citations', 0):,} | "
            f"Score: {entry.get('composite_score', 0):.3f}  \n"
            + (f"   [{doi_link}]({doi_link})  \n" if doi_link else "")
        )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=150)
    args = parser.parse_args()

    print("Loading data...")
    rankings, communities, corpus = load_data()
    corpus_lookup = {p["openalex_id"]: p for p in corpus}

    paper_to_community, community_info = build_community_map(communities)

    # Filter to top-N and non-noise communities
    candidates = []
    for p in rankings[:args.top * 2]:  # oversample, then filter
        pid = p["openalex_id"]
        cid = paper_to_community.get(pid)
        if cid is not None and community_info[cid]["is_noise"]:
            continue
        candidates.append(p)
        if len(candidates) >= args.top:
            break

    print(f"  {len(candidates)} papers after noise filter (from top {args.top * 2})")

    # Topological sort
    print("  Topological sort...")
    order = topological_sort(candidates, corpus_lookup)

    # Build reading list entries
    paper_lookup = {p["openalex_id"]: p for p in candidates}
    reading_list = []
    for pos, pid in enumerate(order):
        p = paper_lookup.get(pid)
        if not p:
            continue
        cid = paper_to_community.get(pid, -1)
        cinfo = community_info.get(cid, {})
        phase = assign_phase(p, pos, len(order))
        reading_list.append({
            **p,
            "reading_order": pos + 1,
            "phase": phase,
            "community_id": cid,
            "community_label": cinfo.get("label", "Other"),
        })

    # Sort within phases: by year, then role
    reading_list.sort(key=lambda x: (
        x["phase"],
        x["community_label"],
        x.get("year") or 9999,
        ROLE_ORDER.get(x.get("role", "methods"), 1),
    ))
    for i, entry in enumerate(reading_list, 1):
        entry["reading_order"] = i

    # Save JSON
    out_path = OUTPUT_DIR / "reading_list.json"
    with open(out_path, "w") as f:
        json.dump(reading_list, f, indent=2)
    print(f"  Saved {len(reading_list)} papers → {out_path}")

    # Save markdown
    md = generate_markdown(reading_list, community_info)
    md_path = OUTPUT_DIR / "reading_list.md"
    with open(md_path, "w") as f:
        f.write(md)
    print(f"  Saved → {md_path}")

    # Print summary
    phases = {}
    for e in reading_list:
        phases.setdefault(e["phase"], []).append(e)
    print()
    for phase_key in sorted(phases):
        entries = phases[phase_key]
        print(f"  {PHASE_NAMES.get(phase_key, phase_key)}")
        print(f"    {len(entries)} papers")
        for e in entries[:3]:
            print(f"    → [{e.get('year')}] {(e.get('title') or '')[:65]}...")
        print()


if __name__ == "__main__":
    main()
