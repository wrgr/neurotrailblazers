#!/usr/bin/env python3
"""Merge the visible-core export (flat yml + rich collection.json) into a single
_data/journal_papers.yml for NeuroTrailblazers.

Source: connectomics-survey/source_artifact/neurotrailblazers_visible_core/
  - ntb_export/journal_papers.yml  (flat, clear field names, no PDF binaries)
  - collection.json                (adds graph/streams/related/pdf/era/why)

The flat yml already has everything the existing journal-club card needs
(ocar, summaries, discussion_prompts, tags, dimension, reading_phase, role).
We enrich each record with the extra fields from collection.json so the site
can build k-core/organism/dataset/method/era views and a citation graph.
"""
import json
import shutil
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_YML = REPO_ROOT / "_data" / "journal_papers.yml"
VIEWS_DIR = REPO_ROOT / "_data" / "paper_views"


def load_flat(src_dir):
    with open(src_dir / "ntb_export" / "journal_papers.yml") as f:
        return yaml.safe_load(f)


def load_collection(src_dir):
    with open(src_dir / "collection.json") as f:
        recs = json.load(f)
    return {r["uuid"]: r for r in recs}


def clean_list(x):
    return [v for v in (x or []) if v]


def backfill_journal(rec):
    """27 records shipped with an empty journal field (mostly preprints /
    conference abstracts). The card renders <em>{{ p.journal }}</em> and the
    site's own validator refuses blank journals, so fill these in from the
    DOI prefix / landing URL rather than leaving them empty."""
    if (rec.get("journal") or "").strip():
        return
    doi = (rec.get("doi") or "").lower()
    landing = (rec.get("landing_url") or "").lower()
    if doi.startswith("10.1101/") :
        rec["journal"] = "bioRxiv"
    elif "arxiv.org" in landing:
        rec["journal"] = "arXiv"
    elif doi.startswith("10.20944/preprints"):
        rec["journal"] = "Preprints.org"
    elif doi.startswith("10.3389/conf.fninf"):
        rec["journal"] = "Frontiers in Neuroinformatics (Conference Abstract)"
    elif doi.startswith("10.9729/am."):
        rec["journal"] = "Applied Microscopy"
    elif doi.startswith("10.1080/10618600"):
        rec["journal"] = "Journal of Computational and Graphical Statistics"
    elif doi.startswith("10.1007/978-981-10-9020-2"):
        rec["journal"] = "Springer (book chapter)"
    elif doi.startswith("10.1103/"):
        rec["journal"] = "Physical Review family (APS)"
    else:
        rec["journal"] = "Preprint"


def merge(flat, coll_by_uuid):
    out = []
    missing_related = 0
    for p in flat:
        c = coll_by_uuid.get(p["uuid"])
        rec = dict(p)  # keep all flat fields (id, uuid, title, authors, year,
        # journal, doi, dimension, reading_phase, role, inclusion_role,
        # k_core, in_degree, out_degree, annotation_status, tags, ocar,
        # plain_language_summary, summaries, discussion_prompts, pdf_status,
        # pdf_url, work_id)

        if c:
            rec["landing_url"] = c.get("landing_url")
            rec["era"] = c.get("era")
            rec["why"] = c.get("why")
            graph = c.get("graph") or {}
            rec["citation_role"] = graph.get("citation_role")
            rec["link_strength"] = graph.get("link_strength")
            rec["year_cites_percentile"] = graph.get("year_cites_percentile")
            streams = c.get("streams") or {}
            rec["streams"] = {
                "axis": streams.get("axis") or None,
                "stages": clean_list(streams.get("stages")),
                "datasets": clean_list(streams.get("datasets")),
                "organism": clean_list(streams.get("organism")),
                "method": clean_list(streams.get("method")),
                "training_outreach": bool(streams.get("training_outreach")),
                "health_translation": bool(streams.get("health_translation")),
                "biological_application": bool(streams.get("biological_application")),
                "bridge": bool(streams.get("bridge")),
                "field_synthesis": bool(streams.get("field_synthesis")),
            }
            related = c.get("related") or {}
            rec["related"] = {
                "cites": clean_list(related.get("cites")),
                "cited_by": clean_list(related.get("cited_by")),
            }
        else:
            missing_related += 1
            rec["related"] = {"cites": [], "cited_by": []}
            rec["streams"] = {}

        backfill_journal(rec)
        out.append(rec)

    print(f"merged {len(out)} records; {missing_related} had no collection.json match", file=sys.stderr)
    return out


def year_key(rec):
    y = rec.get("year")
    return y if isinstance(y, int) else -1


def resolve_related(records):
    """Turn related.cites/.cited_by from bare uuid strings into {id, title,
    year} objects so Jekyll templates don't need an O(n) `where` lookup per
    related link per card (O(n^2) across ~1074 cards at build time)."""
    by_uuid = {r["uuid"]: r for r in records}
    for r in records:
        rel = r.get("related") or {}
        for key in ("cites", "cited_by"):
            resolved = []
            for uuid in rel.get(key, []):
                target = by_uuid.get(uuid)
                if target:
                    resolved.append({"id": target["id"], "title": target["title"], "year": target.get("year")})
            rel[key] = resolved
        r["related"] = rel


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <path-to-connectomics-survey-checkout>/source_artifact/neurotrailblazers_visible_core",
              file=sys.stderr)
        sys.exit(1)
    src_dir = Path(sys.argv[1])
    flat = load_flat(src_dir)
    coll = load_collection(src_dir)
    merged = merge(flat, coll)
    resolve_related(merged)
    merged.sort(key=lambda r: (-year_key(r), r.get("id", "")))

    with open(OUT_YML, "w") as f:
        f.write("# Journal paper corpus: NeuroTrailblazers visible core.\n")
        f.write("#\n")
        f.write("# Generated from connectomics-survey's visible-core export\n")
        f.write("# (source_artifact/neurotrailblazers_visible_core/). One collection\n")
        f.write("# (1,074 papers), multiple views. Do not split this into a second\n")
        f.write("# corpus alongside hand-authored teaching pages -- those pages are\n")
        f.write("# curated deep-dives into a subset of this same collection.\n")
        f.write("#\n")
        f.write("# Regenerate with: python3 scripts/sync_journal_papers.py "
                "<connectomics-survey-checkout>/source_artifact/neurotrailblazers_visible_core\n")
        yaml.safe_dump({"papers": merged}, f, sort_keys=False, allow_unicode=True, width=100000)

    print(f"wrote {len(merged)} papers to {OUT_YML}")

    VIEWS_DIR.mkdir(parents=True, exist_ok=True)
    n_views = 0
    for view_file in sorted((src_dir / "views").glob("*.json")):
        shutil.copyfile(view_file, VIEWS_DIR / view_file.name)
        n_views += 1
    print(f"copied {n_views} view files to {VIEWS_DIR}")


if __name__ == "__main__":
    main()
