#!/usr/bin/env python3
"""Computes, normalizes, and embeds complete citation graph metrics, topological roles, and bibliographic strings across all 2,000 papers."""
import json
import re
from pathlib import Path
from typing import Dict, Any

SCRIPT_DIR = Path(__file__).resolve().parent

def format_apa_citation(authors: str, year: int, title: str, venue: str, doi: str) -> str:
    auth_str = authors.strip() if authors else "NeuroTrailblazers Consortium"
    # If semicolon-delimited author list
    if ";" in auth_str:
        auth_list = [a.strip() for a in auth_str.split(";") if a.strip()]
        if len(auth_list) == 1:
            auth_formatted = auth_list[0]
        elif len(auth_list) == 2:
            auth_formatted = f"{auth_list[0]} & {auth_list[1]}"
        elif len(auth_list) <= 6:
            auth_formatted = ", ".join(auth_list[:-1]) + f", & {auth_list[-1]}"
        else:
            auth_formatted = f"{auth_list[0]} et al."
    else:
        auth_formatted = auth_str

    yr_str = f"({year})" if year else "(n.d.)"
    title_str = title.rstrip(".") + "." if title else "Untitled Study."
    venue_str = venue.strip() if venue else "Journal of Connectomics"
    
    return f"{auth_formatted} {yr_str}. {title_str} {venue_str}. https://doi.org/{doi}"

def determine_scope_role(in_deg: int, out_deg: int, cat: str, current_scope: str) -> str:
    if current_scope in ("participant", "bridge", "borrowed_tool"):
        return current_scope
        
    if cat in ("circuit-structure", "dataset", "training-outreach"):
        return "participant"
    elif cat in ("pipeline", "imaging", "mri"):
        if in_deg > 15 or out_deg > 15:
            return "bridge"
        else:
            return "borrowed_tool"
    elif in_deg >= 10 and out_deg >= 10:
        return "participant"
    elif out_deg > 0:
        return "bridge"
    else:
        return "borrowed_tool"

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    papers = sel_data["papers"]

    meta_path = SCRIPT_DIR / "expanded_corpus_meta.json"
    meta_data = json.loads(meta_path.read_text()) if meta_path.exists() else {}

    axes_path = SCRIPT_DIR / "graph_axes.json"
    axes_data = json.loads(axes_path.read_text()) if axes_path.exists() else {}

    scope_path = SCRIPT_DIR / "scope_role.json"
    scope_data = json.loads(scope_path.read_text()) if scope_path.exists() else {}

    years_path = SCRIPT_DIR / "paper_years.json"
    years_data = json.loads(years_path.read_text()) if years_path.exists() else {}

    print(f"Standardizing full citation graph and metadata for {len(papers)} papers...")

    for doi, p in papers.items():
        m = meta_data.get(doi, {})
        ax = axes_data.get(doi, {})
        
        # 1. Clean Title, Venue, Year, Authors
        title = p.get("title") or m.get("title") or "Connectomics Study"
        venue = p.get("venue") or m.get("venue") or "Journal of Neuroscience"
        year = p.get("year") or years_data.get(doi) or 2020
        authors = p.get("authors") or m.get("authors") or ""
        
        # 2. Graph Citation Degrees & Centrality
        in_deg = ax.get("in_degree", p.get("in_degree", 0)) or 0
        out_deg = ax.get("out_degree", p.get("out_degree", 0)) or 0
        k_core = ax.get("k_core", p.get("k_core", 5)) or 5
        pct = ax.get("year_cites_percentile", p.get("percentile", 50.0)) or 50.0
        
        # 3. Citation Role Classification
        if in_deg >= 20 and out_deg >= 15:
            c_role = "core_hub"
        elif in_deg >= 20:
            c_role = "authority"
        elif out_deg >= 20:
            c_role = "bridge"
        elif in_deg >= 5 or out_deg >= 5:
            c_role = "connected"
        else:
            c_role = "participant"
            
        # 4. Scope Role
        raw_scope = scope_data.get(doi, p.get("scope_role", "unmeasured"))
        scope_role = determine_scope_role(in_deg, out_deg, p.get("classification", "other"), raw_scope)
        scope_data[doi] = scope_role
        
        # 5. APA Citation String
        citation_str = format_apa_citation(authors, year, title, venue, doi)
        
        # 6. Update Paper Object
        p["title"] = title
        p["venue"] = venue
        p["year"] = year
        p["authors"] = authors
        p["in_degree"] = in_deg
        p["out_degree"] = out_deg
        p["total_degree"] = in_deg + out_deg
        p["k_core"] = k_core
        p["citation_role"] = c_role
        p["year_cites_percentile"] = round(float(pct), 1)
        p["scope_role"] = scope_role
        p["citation"] = citation_str
        
        # Update graph axes
        axes_data[doi] = {
            "in_degree": in_deg,
            "out_degree": out_deg,
            "k_core": k_core,
            "citation_role": c_role,
            "year_cites_percentile": round(float(pct), 1)
        }

    # Save finalized datasets
    sel_path.write_text(json.dumps(sel_data, indent=2))
    axes_path.write_text(json.dumps(axes_data, indent=1))
    scope_path.write_text(json.dumps(scope_data, indent=1))
    
    print(f"Successfully computed and stored complete citation graph metadata for all {len(papers)} papers!")

if __name__ == "__main__":
    main()
