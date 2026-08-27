#!/usr/bin/env python3
"""Apply the adjudicated corpus fixes to _data/journal_papers.yml.

Fixes 17 confirmed preprint/published duplicate-version pairs and 2 confirmed
`dimension` mis-tags, found by an audit on 2026-08-27 (see scripts/corpus_issues.json
for the full report, sent upstream to connectomics-survey). These are stopgap fixes
on top of the current export -- a full from-scratch re-query is planned separately
(see /root/.claude/plans/concept-explorer-is-very-quirky-lemon.md, Part 1B) and will
eventually replace this file's provenance entirely.

Merge rule for each pair: canonical id = the published version's DOI. The preprint's
DOI is retained on the canonical record as `alt_dois` so old references still resolve.
`related.cites` / `related.cited_by` are UNIONED across both records, never summed --
several corpus papers cite both versions of a paper and would be double-counted by a
naive sum. `in_degree` / `out_degree` are recomputed from the merged, deduplicated edge
list (still a subset of the true graph -- see STRUCT-001 in corpus_issues.json -- but
now at least internally consistent). `k_core` takes the max of the two source records
pending a real whole-graph recompute.

Every other record's `related.cites` / `related.cited_by` is scrubbed so no edge still
points at a removed duplicate id -- those are repointed onto the surviving canonical id.

Idempotent: running this twice is a no-op the second time, because the duplicate DOIs
this script looks for no longer exist in the corpus after the first run.

Usage:
    python3 scripts/apply_duplicate_merges.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PATH = ROOT / "_data" / "journal_papers.yml"

# (canonical_doi, duplicate_doi, label) -- see "Dedup technique -- validation evidence"
# in the plan doc for the author-overlap + OCAR-read adjudication behind each pair.
MERGES = [
    ("10.7554/elife.57443", "10.1101/2020.01.21.911859", "Hemibrain"),
    ("10.1038/s41592-018-0049-4", "work_3de0825b6d9efa49", "Flood-filling networks"),
    ("10.7554/elife.62576", "10.1101/2020.08.29.273276", "Mushroom body connectome"),
    ("10.1038/s41586-021-03284-x", "10.1101/2020.05.24.112870", "C. elegans multiscale brain map"),
    ("10.7554/elife.53350", "10.1101/006353", "natverse"),
    ("10.1038/s41586-024-07780-8", "10.1101/2023.01.23.525290", "Inhibitory specificity"),
    ("10.1038/s41586-024-07939-3", "10.1101/2023.03.11.532232", "Connectome-constrained networks"),
    ("10.1038/s41593-020-0607-9", "10.1101/649731", "Recurrent architecture insect brain"),
    ("10.1038/s41586-025-08925-z", "10.1101/2024.06.04.596633", "Comparative connectomics DN/AN"),
    ("10.1038/s41586-024-07763-9", "10.1101/2023.05.02.539144", "Drosophila computational brain model"),
    ("10.7554/elife.40247", "10.1101/368878", "Feeding connectome"),
    ("10.1038/s41467-024-50411-z", "10.21203/rs.3.rs-3121892/v1", "Multiplexed volumetric CLEM"),
    ("10.1109/tmi.2024.3400276", "10.48550/arxiv.2302.00545", "WASPSYN"),
    ("10.1093/gigascience/giaa147", "10.1101/615161", "Scalable reproducible framework"),
    ("10.1016/j.isci.2021.103601", "10.1101/2021.04.02.438164", "ScaleSF LM/EM"),
    ("10.1016/j.cub.2023.12.003", "10.1101/2023.10.04.560846", "Zebrafish telencephalon"),
    ("10.1038/s41467-026-72152-x", "10.1101/2024.12.17.628844", "Antennal grooming"),
]

# (doi, field, expected_current_value, new_value, label)
FIELD_FIXES = [
    ("work_ac9f66d6d45899c4", "dimension", "image-acquisition", "segmentation",
     "Lee 2015 boundary-detection convnets"),
    ("10.1038/s41586-021-03284-x", "dimension", "image-acquisition", "connectomics",
     "Brittin 2021 C. elegans multiscale brain map"),
]

HEADER = """# Journal paper corpus: NeuroTrailblazers visible core.
#
# Generated from connectomics-survey's visible-core export
# (source_artifact/neurotrailblazers_visible_core/). One collection
# (1,074 papers originally; 17 preprint/published duplicate pairs merged
# and 2 dimension mis-tags corrected 2026-08-27, see scripts/corpus_issues.json),
# multiple views. Do not split this into a second corpus alongside
# hand-authored teaching pages -- those pages are curated deep-dives into
# a subset of this same collection.
#
# Regenerate with: python3 scripts/sync_journal_papers.py <connectomics-survey-checkout>/source_artifact/neurotrailblazers_visible_core
# NOTE: regenerating will REVERT the 2026-08-27 duplicate merges and field
# fixes -- re-apply scripts/apply_duplicate_merges.py after any regeneration
# until upstream fixes these bugs (see scripts/corpus_issues.json).
"""


def union_edges(list_a, list_b, self_ids):
    seen = {}
    for edge in (list_a or []) + (list_b or []):
        eid = edge.get("id")
        if eid is None or eid in self_ids:
            continue  # drop self-references between the two merged records
        if eid not in seen:
            seen[eid] = edge
    return list(seen.values())


def apply_merges(data):
    by_uuid = {p["uuid"]: p for p in data["papers"]}
    removed_ids = set()
    merge_log = []
    skipped = 0

    for canon_doi, dup_doi, label in MERGES:
        canon = by_uuid.get(canon_doi)
        dup = by_uuid.get(dup_doi)
        if dup is None:
            # Already merged in a prior run (idempotent no-op), or not present.
            skipped += 1
            continue
        if canon is None:
            print(f"ERROR: canonical record missing for {label}: {canon_doi}", file=sys.stderr)
            sys.exit(1)

        canon_related = canon.get("related") or {"cites": [], "cited_by": []}
        dup_related = dup.get("related") or {"cites": [], "cited_by": []}
        self_ids = {canon["id"], dup["id"]}

        merged_cites = union_edges(canon_related.get("cites"), dup_related.get("cites"), self_ids)
        merged_cited_by = union_edges(canon_related.get("cited_by"), dup_related.get("cited_by"), self_ids)

        before_in = len(canon_related.get("cited_by") or [])
        canon["related"] = {"cites": merged_cites, "cited_by": merged_cited_by}
        canon["out_degree"] = len(merged_cites)
        canon["in_degree"] = len(merged_cited_by)
        canon["k_core"] = max(canon.get("k_core") or 0, dup.get("k_core") or 0)

        alt = canon.get("alt_dois") or []
        if dup_doi not in alt:
            alt.append(dup_doi)
        canon["alt_dois"] = alt

        removed_ids.add(dup["id"])
        merge_log.append((label, before_in, canon["in_degree"]))

    if skipped == len(MERGES):
        print("All merges already applied (idempotent no-op).", file=sys.stderr)
        return

    # Repoint every other record's edges away from removed duplicate ids.
    dup_to_canon_id = {}
    for canon_doi, dup_doi, _label in MERGES:
        c, d = by_uuid.get(canon_doi), by_uuid.get(dup_doi)
        if c and d and d["id"] in removed_ids:
            dup_to_canon_id[d["id"]] = c["id"]

    id_to_title_year = {p["id"]: (p["title"], p.get("year")) for p in data["papers"]}

    for p in data["papers"]:
        if p["id"] in removed_ids:
            continue
        related = p.get("related") or {}
        for key in ("cites", "cited_by"):
            edges = related.get(key) or []
            seen, new_edges = set(), []
            for edge in edges:
                eid = edge.get("id")
                if eid in dup_to_canon_id:
                    eid = dup_to_canon_id[eid]
                    title, year = id_to_title_year.get(eid, (edge.get("title"), edge.get("year")))
                    edge = {"id": eid, "title": title, "year": year}
                if eid == p["id"] or eid in seen:
                    continue
                seen.add(eid)
                new_edges.append(edge)
            related[key] = new_edges
        p["related"] = related

    before_count = len(data["papers"])
    data["papers"] = [p for p in data["papers"] if p["id"] not in removed_ids]
    print(f"Merged {len(merge_log)} pairs. Papers: {before_count} -> {len(data['papers'])}", file=sys.stderr)
    for label, before_in, after_in in merge_log:
        print(f"  {label}: in_degree {before_in} -> {after_in}", file=sys.stderr)


def apply_field_fixes(data):
    by_uuid = {p["uuid"]: p for p in data["papers"]}
    for doi, field, old, new, label in FIELD_FIXES:
        p = by_uuid.get(doi)
        if p is None:
            print(f"WARNING: record not found for field fix: {label} ({doi})", file=sys.stderr)
            continue
        if p[field] == new:
            continue  # already applied
        if p[field] != old:
            print(f"WARNING: {label}: expected {field}={old!r}, found {p[field]!r} -- skipping", file=sys.stderr)
            continue
        p[field] = new
        print(f"Fixed {label}: {field} {old!r} -> {new!r}", file=sys.stderr)


def main():
    with open(PATH) as f:
        data = yaml.safe_load(f)

    apply_merges(data)
    apply_field_fixes(data)

    with open(PATH, "w") as f:
        f.write(HEADER)
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=100000)

    print(f"Wrote {PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
