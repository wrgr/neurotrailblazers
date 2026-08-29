#!/usr/bin/env python3
"""Compiles and replaces _data/journal_papers.yml with the curated 2,000-paper multi-tiered corpus."""
import json
import re
from pathlib import Path
from typing import Dict, Any, List

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
OUTPUT_YML = PROJECT_ROOT / "_data/journal_papers.yml"

def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    return s[:40]

def make_paper_id(p: Dict[str, Any]) -> str:
    authors = p.get("authors", "author")
    first_author = authors.split(";")[0].split("&")[0].strip().split(",")[-1].strip().split()[-1].lower() if authors else "author"
    first_author = re.sub(r"[^\w]", "", first_author)
    year = p.get("year", 2024)
    doi = p.get("doi", "").lower()
    clean_d = re.sub(r"[^\w]", "-", doi)[-12:]
    return f"{first_author}-{year}-{clean_d}"

def escape_yaml_str(s: str) -> str:
    if not s: return "''"
    s = s.replace("\n", " ").replace("\r", " ").strip()
    # Escape quotes
    escaped = s.replace("'", "''")
    return f"'{escaped}'"

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    papers_dict = sel_data["papers"]

    # Load complete 2,000 corpus with rich OCAR cards & 3-tier summaries
    c2000_path = PROJECT_ROOT / "_data/corpus_2000.json"
    c2000_dict = {}
    if c2000_path.exists():
        c2000_papers = json.loads(c2000_path.read_text()).get("papers", [])
        for cp in c2000_papers:
            c2000_dict[cp["doi"].lower()] = cp

    # Load directed citation edges
    edges_path = SCRIPT_DIR / "corpus_citation_edges.json"
    adj_out = {}
    if edges_path.exists():
        adj_out = json.loads(edges_path.read_text()).get("adj_out", {})

    print(f"Compiling _data/journal_papers.yml from {len(papers_dict)} curated papers...")

    lines = []
    lines.append("# Journal paper corpus: NeuroTrailblazers Curated Multi-Tier Corpus (2,000 papers).")
    lines.append("# Generated automatically from verified 12-category stratified graph selection.")
    lines.append("# Supports: Top 500 Flagships, Top 1,000 Landmark Collection, Top 2,000 Full Network.")
    lines.append("papers:")

    # Sort papers by tier (500 first, then 1000, then 2000), then category, then linkage score
    sorted_papers = sorted(
        papers_dict.values(),
        key=lambda x: (x.get("tier", 2000), x.get("classification", ""), -x.get("linkage_score", 0))
    )

    for p in sorted_papers:
        doi = p.get("doi", "").lower()
        c2000_p = c2000_dict.get(doi, {})

        p_id = make_paper_id(p)
        title = p.get("title", "")
        authors = p.get("authors", "")
        year = p.get("year", 2024)
        journal = p.get("venue", "Journal of Connectomics")
        cat = p.get("classification", "circuit-structure")
        era = p.get("era", "contemporary")
        tier = p.get("tier", 2000)
        in_top_500 = p.get("in_top_500", False)
        in_top_1000 = p.get("in_top_1000", False)
        in_top_2000 = True

        in_deg = p.get("in_degree", 0)
        out_deg = p.get("out_degree", 0)
        k_core = p.get("k_core", 5)
        c_role = p.get("citation_role", "participant")
        scope_role = p.get("scope_role", "participant")
        citation = p.get("citation", "")
        abstract = p.get("abstract", "")

        # OCAR and Summaries (from c2000_p)
        ocar = c2000_p.get("ocar")
        summaries = c2000_p.get("summaries")
        prompts = c2000_p.get("discussion_prompts")
        annot_status = c2000_p.get("source_flag", "generated_from_unabridged_abstract")
        plain_summary = summaries.get("intermediate", abstract[:200] + "...") if summaries else abstract[:200] + "..."

        lines.append(f"- id: {p_id}")
        lines.append(f"  uuid: {doi}")
        lines.append(f"  work_id: work_{abs(hash(doi)) % 10000000000:010d}")
        lines.append(f"  title: {escape_yaml_str(title)}")
        lines.append(f"  authors: {escape_yaml_str(authors)}")
        lines.append(f"  year: {year}")
        lines.append(f"  journal: {escape_yaml_str(journal)}")
        lines.append(f"  doi: {doi}")
        lines.append(f"  dimension: {cat}")
        lines.append(f"  reading_phase: {'1_foundations' if year <= 2018 else ('2_contemporary' if year <= 2023 else '3_sota')}")
        lines.append(f"  role: {cat}")
        lines.append(f"  inclusion_role: {era}")
        lines.append(f"  tier: {tier}")
        lines.append(f"  in_top_500: {'true' if in_top_500 else 'false'}")
        lines.append(f"  in_top_1000: {'true' if in_top_1000 else 'false'}")
        lines.append(f"  in_top_2000: true")
        lines.append(f"  k_core: {k_core}")
        lines.append(f"  in_degree: {in_deg}")
        lines.append(f"  out_degree: {out_deg}")
        lines.append(f"  citation_role: {c_role}")
        lines.append(f"  scope_role: {scope_role}")
        lines.append(f"  citation: {escape_yaml_str(citation)}")
        lines.append(f"  landing_url: https://doi.org/{doi}")
        pdf_url = c2000_p.get("pdf_url")
        if pdf_url:
            lines.append(f"  pdf_url: {escape_yaml_str(pdf_url)}")
            lines.append("  is_oa: true")
            if c2000_p.get("oa_status"):
                lines.append(f"  oa_status: {escape_yaml_str(c2000_p.get('oa_status'))}")
        else:
            lines.append("  is_oa: false")

        # Cites list (papers cited by this paper)
        p_cites = adj_out.get(doi, [])
        lines.append("  cites:")
        for c_doi in p_cites:
            lines.append(f"  - {c_doi}")

        # Tags
        orgs = p.get("organism", ["general"])
        lines.append("  tags:")
        for org in orgs:
            lines.append(f"  - {org}")
        lines.append(f"  - {cat}")
        lines.append(f"  - tier_{tier}")

        # OCAR (if present)
        if ocar:
            lines.append("  ocar:")
            lines.append(f"    opportunity: {escape_yaml_str(ocar.get('opportunity', ''))}")
            lines.append(f"    challenge: {escape_yaml_str(ocar.get('challenge', ''))}")
            lines.append(f"    action: {escape_yaml_str(ocar.get('action', ''))}")
            lines.append(f"    resolution: {escape_yaml_str(ocar.get('resolution', ''))}")
            lines.append(f"    future_work: {escape_yaml_str(ocar.get('future_work', ''))}")

        # Summaries
        lines.append(f"  plain_language_summary: {escape_yaml_str(plain_summary)}")
        if summaries:
            lines.append("  summaries:")
            lines.append(f"    beginner: {escape_yaml_str(summaries.get('beginner', plain_summary))}")
            lines.append(f"    intermediate: {escape_yaml_str(summaries.get('intermediate', abstract))}")
            lines.append(f"    advanced: {escape_yaml_str(summaries.get('advanced', abstract))}")
        else:
            lines.append("  summaries:")
            lines.append(f"    beginner: {escape_yaml_str(plain_summary)}")
            lines.append(f"    intermediate: {escape_yaml_str(abstract)}")
            lines.append(f"    advanced: {escape_yaml_str(abstract)}")

        # Discussion prompts
        if prompts:
            lines.append("  discussion_prompts:")
            for pr in prompts:
                lines.append(f"  - {escape_yaml_str(pr)}")

    OUTPUT_YML.write_text("\n".join(lines) + "\n")
    print(f"Successfully generated {OUTPUT_YML} ({len(sorted_papers)} papers, {OUTPUT_YML.stat().st_size} bytes).")

if __name__ == "__main__":
    main()
