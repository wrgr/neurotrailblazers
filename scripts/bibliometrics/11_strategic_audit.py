#!/usr/bin/env python3
"""
Step 11: Strategic audit — papers outside top-200 worth human review.

Flags papers across five lenses:
  A. Expert-curated papers NOT recovered by the pipeline (from expert_list_gaps.json)
     subdivided: in-corpus-but-ranked-low vs not-in-corpus-at-all
  B. High in-degree papers outside top-500 (from high_indegree_omissions.json)
  C. Reading-list papers 201–500 with suspicious topic signals
     (very high external citations vs. low composite score, or off-domain title)
  D. Reading-list papers 201–500 that are in the k=32 inner core but ranked low
  E. Papers with Gray Roncal / other merged authors — now re-ranked

Output: output/strategic_audit.md  (readable briefing doc)
        output/strategic_audit.json (machine-readable)
"""
import json, re
from pathlib import Path
from collections import defaultdict

from config import OUTPUT_DIR

CONNECTOMICS_SIGNAL = [
    "connectom", "synapse", "electron microscopy", "neural circuit",
    "neuron", "axon", "dendrite", "neuropil", "brain wiring",
    "fib-sem", "serial section", "segmentation", "proofreading",
    "catmaid", "flywire", "hemibrain", "drosophila", "c. elegans",
    "microns", "bossdb", "expansion microscopy", "reconstruction",
]

def neuro_score(title, abstract=""):
    txt = (title + " " + abstract).lower()
    return sum(1 for t in CONNECTOMICS_SIGNAL if t in txt)


def load(fname):
    with open(OUTPUT_DIR / fname) as f:
        return json.load(f)


def main():
    reading_list  = load("reading_list.json")
    rl_enriched   = load("reading_list_enriched.json")
    gaps          = load("expert_list_gaps.json")
    omissions     = load("high_indegree_omissions.json")

    enrich_lookup = {p["openalex_id"]: p for p in rl_enriched}

    # Sort reading list by composite_score, label top-200 vs 201-500
    by_score = sorted(reading_list, key=lambda x: -x.get("composite_score", 0))
    top200_ids = {p["openalex_id"] for p in by_score[:200]}
    tail300    = by_score[200:500]

    audit = {
        "A_expert_in_corpus":     [],
        "A_expert_missing":       [],
        "B_high_indegree_omissions": [],
        "C_tail_high_extcites":   [],
        "C_tail_offtrack":        [],
        "D_tail_inner_core":      [],
    }

    # ── A. Expert gaps ────────────────────────────────────────────────
    for g in gaps:
        entry = {
            "doi": g["doi"],
            "title": g["title"],
            "dimension": g["dimension"],
            "external_citations": g["external_citations"],
            "action": "promote" if g["in_corpus"] else "fetch+add",
        }
        if g["in_corpus"]:
            audit["A_expert_in_corpus"].append(entry)
        else:
            audit["A_expert_missing"].append(entry)

    audit["A_expert_in_corpus"].sort(key=lambda x: -x["external_citations"])
    audit["A_expert_missing"].sort(key=lambda x: -x["external_citations"])

    # ── B. High in-degree omissions ───────────────────────────────────
    rl_ids = {p["openalex_id"] for p in reading_list}
    for o in omissions[:50]:
        pid = o["openalex_id"]
        if pid not in rl_ids:
            audit["B_high_indegree_omissions"].append({
                "openalex_id": pid,
                "title": o["title"],
                "year": o.get("year"),
                "external_citations": o["external_citations"],
                "corpus_in_degree": o["corpus_in_degree"],
                "composite_score": o["composite_score"],
                "neuro_signal": neuro_score(o["title"]),
            })

    # ── C. Tail papers 201-500: anomalies ─────────────────────────────
    for p in tail300:
        pid = p["openalex_id"]
        ext_cites = p.get("total_citations", 0)
        comp      = p.get("composite_score", 0)
        ns        = neuro_score(p.get("title",""), p.get("abstract",""))
        ep        = enrich_lookup.get(pid, {})

        # High external citations but low composite → might deserve higher rank
        if ext_cites > 500 and comp < 0.15:
            audit["C_tail_high_extcites"].append({
                "openalex_id": pid,
                "title": p.get("title",""),
                "year": p.get("year"),
                "journal": p.get("journal",""),
                "composite_score": round(comp, 4),
                "external_citations": ext_cites,
                "in_degree": ep.get("in_degree", 0),
                "neuro_signal": ns,
                "note": "high ext-cites, low composite",
            })

        # Low neuro signal in tail → possible off-topic paper that slipped through
        if ns == 0 and comp > 0.08:
            audit["C_tail_offtrack"].append({
                "openalex_id": pid,
                "title": p.get("title",""),
                "year": p.get("year"),
                "journal": p.get("journal",""),
                "composite_score": round(comp, 4),
                "external_citations": ext_cites,
                "in_degree": ep.get("in_degree", 0),
                "role": p.get("role",""),
            })

    audit["C_tail_high_extcites"].sort(key=lambda x: -x["external_citations"])
    audit["C_tail_offtrack"].sort(key=lambda x: -x["composite_score"])

    # ── D. Tail papers in k=32 inner core ─────────────────────────────
    for p in tail300:
        pid = p["openalex_id"]
        ep = enrich_lookup.get(pid, {})
        if ep.get("core_number", 0) >= 30:
            audit["D_tail_inner_core"].append({
                "openalex_id": pid,
                "title": p.get("title",""),
                "year": p.get("year"),
                "composite_score": round(p.get("composite_score",0), 4),
                "core_number": ep.get("core_number", 0),
                "in_degree": ep.get("in_degree", 0),
                "external_citations": p.get("total_citations", 0),
                "neuro_signal": neuro_score(p.get("title",""), p.get("abstract","")),
            })

    audit["D_tail_inner_core"].sort(key=lambda x: -x["core_number"])

    # ── Save JSON ─────────────────────────────────────────────────────
    with open(OUTPUT_DIR / "strategic_audit.json", "w") as f:
        json.dump(audit, f, indent=2)

    # ── Build Markdown ────────────────────────────────────────────────
    lines = [
        "# Strategic Paper Audit",
        "",
        "Papers outside the current top-200 OCAR list that warrant human review.",
        "Organised by lens: expert curation, connectivity, citation anomalies, k-core, topic drift.",
        "",
    ]

    def section(title, items, cols, fmt):
        lines.append(f"## {title}  ({len(items)})")
        lines.append("")
        if not items:
            lines.append("_None._")
            lines.append("")
            return
        header = " | ".join(cols)
        sep    = " | ".join("---" for _ in cols)
        lines.append(f"| {header} |")
        lines.append(f"| {sep} |")
        for item in items:
            row = fmt(item)
            lines.append(f"| {' | '.join(str(x) for x in row)} |")
        lines.append("")

    section(
        "A1. Expert-curated, IN corpus, ranked below 500 → consider promoting",
        audit["A_expert_in_corpus"],
        ["Ext.Cites", "Dimension", "Title"],
        lambda x: [x["external_citations"], x["dimension"], x["title"][:70]],
    )
    section(
        "A2. Expert-curated, NOT IN corpus → needs manual fetch + seed",
        audit["A_expert_missing"],
        ["Dimension", "Title"],
        lambda x: [x["dimension"], x["title"][:80]],
    )
    section(
        "B. High in-degree papers outside top-500 (cited heavily within corpus)",
        audit["B_high_indegree_omissions"],
        ["In-deg", "Ext.Cites", "Neuro?", "Year", "Title"],
        lambda x: [x["corpus_in_degree"], x["external_citations"],
                   "✓" if x["neuro_signal"]>0 else "✗",
                   x.get("year",""), x["title"][:65]],
    )
    section(
        "C1. Tail papers (rank 201–500) with high external citations but low composite score",
        audit["C_tail_high_extcites"][:30],
        ["Score", "Ext.Cites", "In-deg", "Neuro?", "Year", "Title"],
        lambda x: [x["composite_score"], x["external_citations"], x["in_degree"],
                   "✓" if x["neuro_signal"]>0 else "✗",
                   x.get("year",""), x["title"][:60]],
    )
    section(
        "C2. Tail papers with zero neuro-signal in title+abstract → possible off-topic",
        audit["C_tail_offtrack"][:30],
        ["Score", "Ext.Cites", "Role", "Year", "Title"],
        lambda x: [x["composite_score"], x["external_citations"], x["role"],
                   x.get("year",""), x["title"][:65]],
    )
    section(
        "D. Tail papers in k≥30 inner core — structurally central, ranked lower than expected",
        audit["D_tail_inner_core"][:30],
        ["Core-k", "Score", "In-deg", "Ext.Cites", "Neuro?", "Year", "Title"],
        lambda x: [x["core_number"], x["composite_score"], x["in_degree"],
                   x["external_citations"],
                   "✓" if x["neuro_signal"]>0 else "✗",
                   x.get("year",""), x["title"][:55]],
    )

    # Author merge summary
    lines += [
        "## Author Merge Summary",
        "",
        "Confirmed merges applied in `author_merge_map.json`:",
        "",
        "| Canonical | Aliases | Impact |",
        "| --- | --- | --- |",
        "| William Gray-Roncal | William Gray Roncal, W.R. Gray Roncal, Will Gray-Roncal (×4) | **34 papers** — enters top-500 authors after merge |",
        "| Shin-ya Takemura | Satoko Takemura | **32 unique papers** (13 shared) — consolidates #40 author |",
        "| Alexander Shakeel Bates | Alexander S. Bates | minor — 1 extra paper |",
        "| Gregory S.X.E. Jefferis | G Jefferis, Gregory S. X. E. Jefferis | minor — deduplicates #3 author |",
        "| H. Sebastian Seung | H Sebastian Seung | minor — deduplicates #1 author |",
        "| Olaf Sporns | O Sporns | minor — deduplicates MRI network leader |",
        "| Moritz Helmstaedter / Davi D. Bock / Marta Costa | abbreviated forms | minor dedup |",
        "| C. Shan Xu | Shan Xu, C Shan Xu | minor — deduplicates FIB-SEM leader |",
        "| Unicode normalization (8 pairs) | en-dash ↔ hyphen variants | cosmetic |",
        "",
    ]

    md = "\n".join(lines)
    with open(OUTPUT_DIR / "strategic_audit.md", "w") as f:
        f.write(md)

    # Print summary counts
    print("Strategic Audit Summary")
    print(f"  A1 Expert in-corpus (promote):     {len(audit['A_expert_in_corpus'])}")
    print(f"  A2 Expert missing (fetch+seed):    {len(audit['A_expert_missing'])}")
    print(f"  B  High in-degree omissions:       {len(audit['B_high_indegree_omissions'])}")
    print(f"  C1 High ext-cites / low composite: {len(audit['C_tail_high_extcites'])}")
    print(f"  C2 Zero neuro-signal (off-topic?): {len(audit['C_tail_offtrack'])}")
    print(f"  D  Inner-core but tail-ranked:     {len(audit['D_tail_inner_core'])}")
    print(f"\nSaved → output/strategic_audit.md")
    print(f"Saved → output/strategic_audit.json")


if __name__ == "__main__":
    main()
