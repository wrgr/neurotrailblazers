#!/usr/bin/env python3
"""
Step 4: Validate data-driven results against expert-curated list.

Compares the pipeline's discoveries with:
  - 150 expert seed papers (from _data/expert_seed_papers/)
  - 102 journal papers (from _data/journal_papers.yml)
  - 55 expert researchers (from expert_seed_list.json)

Outputs: output/validation_report.json, output/validation_report.md

Usage:
  python 04_validate.py
"""
import json
import re
from collections import defaultdict
from pathlib import Path

from config import SEED_PAPERS_DIR, JOURNAL_PAPERS_YML, OUTPUT_DIR


def load_expert_papers():
    """
    Load all expert-curated papers from seed JSONs.
    Returns list of dicts with at least: doi, title, seed_expert, dimensions.
    """
    papers = []
    for expert_dir in SEED_PAPERS_DIR.iterdir():
        if not expert_dir.is_dir():
            continue
        for json_file in expert_dir.glob("*.json"):
            with open(json_file) as f:
                paper = json.load(f)
            if paper.get("doi"):
                papers.append(paper)
    return papers


def load_journal_papers():
    """
    Load papers from journal_papers.yml.
    Returns list of dicts with doi field.
    """
    # Simple YAML parsing for DOIs (avoid pyyaml dependency if not installed)
    papers = []
    path = JOURNAL_PAPERS_YML
    if not path.exists():
        return papers

    current = {}
    with open(path) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("- id:"):
                if current.get("doi"):
                    papers.append(current)
                current = {"id": line.split(":", 1)[1].strip()}
            elif line.strip().startswith("doi:"):
                doi_val = line.split(":", 1)[1].strip().strip('"').strip("'")
                if doi_val and doi_val != "null":
                    current["doi"] = doi_val.lower().replace("https://doi.org/", "")
            elif line.strip().startswith("title:"):
                current["title"] = line.split(":", 1)[1].strip().strip('"')
            elif line.strip().startswith("dimension:"):
                current["dimension"] = line.split(":", 1)[1].strip().strip('"')
    if current.get("doi"):
        papers.append(current)

    return papers


def load_expert_list():
    """Load expert researcher list."""
    path = SEED_PAPERS_DIR / "expert_seed_list.json"
    with open(path) as f:
        data = json.load(f)
    return data.get("experts", []) + data.get("additional_contributors", [])


def load_data_driven_corpus():
    """Load the data-driven merged corpus."""
    path = OUTPUT_DIR / "corpus_merged.json"
    with open(path) as f:
        return json.load(f)


def load_provenance_corpora():
    """Load individual corpora for triangulation."""
    corpora = {}
    for name in ["corpus_a", "corpus_b", "corpus_c"]:
        path = OUTPUT_DIR / f"{name}.json"
        if path.exists():
            with open(path) as f:
                corpora[name] = json.load(f)
    return corpora


def normalize_doi(doi):
    """Normalize DOI for comparison."""
    if not doi:
        return None
    return doi.strip().lower().replace("https://doi.org/", "").replace("http://doi.org/", "")


def compute_triangulation(corpora):
    """
    Compute Jaccard overlap between corpora A, B, C.
    """
    sets = {}
    for name, papers in corpora.items():
        dois = {normalize_doi(p.get("doi")) for p in papers if p.get("doi")}
        dois.discard(None)
        sets[name] = dois

    results = {}
    names = list(sets.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            intersection = sets[a] & sets[b]
            union = sets[a] | sets[b]
            jaccard = len(intersection) / len(union) if union else 0
            results[f"jaccard_{a}_vs_{b}"] = {
                "jaccard": round(jaccard, 4),
                "intersection_size": len(intersection),
                "union_size": len(union),
                "a_size": len(sets[a]),
                "b_size": len(sets[b]),
            }

    # All-three overlap
    if len(sets) == 3:
        all_sets = list(sets.values())
        core = all_sets[0] & all_sets[1] & all_sets[2]
        results["core_all_three"] = {
            "size": len(core),
            "note": "Papers found by all three independent methods",
        }

    return results


def compute_expert_validation(expert_papers, journal_papers, data_driven):
    """
    Compare expert-curated papers with data-driven corpus.
    """
    expert_dois = set()
    for p in expert_papers:
        doi = normalize_doi(p.get("doi"))
        if doi:
            expert_dois.add(doi)
    for p in journal_papers:
        doi = normalize_doi(p.get("doi"))
        if doi:
            expert_dois.add(doi)

    dd_dois = set()
    for p in data_driven:
        doi = normalize_doi(p.get("doi"))
        if doi:
            dd_dois.add(doi)

    found = expert_dois & dd_dois
    missed = expert_dois - dd_dois
    novel = dd_dois - expert_dois

    recall = len(found) / len(expert_dois) if expert_dois else 0

    # Find titles for missed papers
    missed_papers = []
    for p in expert_papers + journal_papers:
        doi = normalize_doi(p.get("doi"))
        if doi in missed:
            missed_papers.append({
                "doi": doi,
                "title": p.get("title", ""),
                "seed_expert": p.get("seed_expert", ""),
            })

    return {
        "expert_total": len(expert_dois),
        "data_driven_total": len(dd_dois),
        "found_in_both": len(found),
        "recall": round(recall, 4),
        "missed_by_data_driven": len(missed),
        "novel_in_data_driven": len(novel),
        "missed_papers": missed_papers[:50],  # cap for readability
    }


def check_expert_authors(expert_list, data_driven):
    """
    Check if all 55 experts appear as authors in the data-driven corpus.
    """
    # Build set of author names in data-driven corpus (lowered for fuzzy match)
    dd_author_names = set()
    for paper in data_driven:
        for author in paper.get("authors", []):
            name = (author.get("name") or "").lower()
            if name:
                dd_author_names.add(name)

    results = []
    for expert in expert_list:
        name = expert.get("name", "")
        name_lower = name.lower()
        # Try exact match and last-name match
        found = name_lower in dd_author_names
        if not found:
            # Try last name match
            last_name = name.split()[-1].lower() if name else ""
            found = any(last_name in n for n in dd_author_names)

        results.append({
            "name": name,
            "found": found,
            "affiliation": expert.get("affiliation", ""),
        })

    found_count = sum(1 for r in results if r["found"])
    return {
        "total_experts": len(results),
        "found_in_corpus": found_count,
        "recall": round(found_count / len(results), 4) if results else 0,
        "missing_experts": [r for r in results if not r["found"]],
    }


def generate_markdown_report(triangulation, validation, author_check):
    """Generate human-readable markdown report."""
    lines = ["# Validation Report\n"]
    lines.append("## Triangulation (Corpus Overlap)\n")
    for key, val in triangulation.items():
        if key.startswith("jaccard"):
            lines.append(f"- **{key}**: Jaccard = {val['jaccard']:.4f} "
                        f"(intersection: {val['intersection_size']}, "
                        f"union: {val['union_size']})")
    if "core_all_three" in triangulation:
        lines.append(f"- **Core (all 3 corpora)**: {triangulation['core_all_three']['size']} papers\n")

    lines.append("\n## Expert Paper Validation\n")
    lines.append(f"- Expert papers: {validation['expert_total']}")
    lines.append(f"- Data-driven papers: {validation['data_driven_total']}")
    lines.append(f"- **Recall**: {validation['recall']:.1%} "
                f"({validation['found_in_both']}/{validation['expert_total']})")
    lines.append(f"- Missed by data-driven: {validation['missed_by_data_driven']}")
    lines.append(f"- Novel discoveries: {validation['novel_in_data_driven']}\n")

    if validation.get("missed_papers"):
        lines.append("### Missed Papers (sample)\n")
        for p in validation["missed_papers"][:20]:
            lines.append(f"- {p['title'][:80]} (expert: {p['seed_expert']})")

    lines.append(f"\n## Expert Author Validation\n")
    lines.append(f"- Experts checked: {author_check['total_experts']}")
    lines.append(f"- **Found in corpus**: {author_check['found_in_corpus']} "
                f"({author_check['recall']:.1%})")

    if author_check.get("missing_experts"):
        lines.append("\n### Missing Experts\n")
        for e in author_check["missing_experts"]:
            lines.append(f"- {e['name']} ({e['affiliation']})")

    return "\n".join(lines)


def main():
    print("Loading data...")
    expert_papers = load_expert_papers()
    journal_papers = load_journal_papers()
    expert_list = load_expert_list()
    data_driven = load_data_driven_corpus()
    corpora = load_provenance_corpora()

    print(f"  Expert papers: {len(expert_papers)}")
    print(f"  Journal papers: {len(journal_papers)}")
    print(f"  Experts: {len(expert_list)}")
    print(f"  Data-driven corpus: {len(data_driven)}")

    # Triangulation
    print("\n--- Triangulation ---")
    triangulation = compute_triangulation(corpora)
    for key, val in triangulation.items():
        if isinstance(val, dict) and "jaccard" in val:
            print(f"  {key}: {val['jaccard']:.4f}")

    # Expert validation
    print("\n--- Expert Paper Validation ---")
    validation = compute_expert_validation(expert_papers, journal_papers, data_driven)
    print(f"  Recall: {validation['recall']:.1%}")
    print(f"  Missed: {validation['missed_by_data_driven']}")
    print(f"  Novel: {validation['novel_in_data_driven']}")

    # Expert author check
    print("\n--- Expert Author Check ---")
    author_check = check_expert_authors(expert_list, data_driven)
    print(f"  Found: {author_check['found_in_corpus']}/{author_check['total_experts']}")

    # Save results
    report = {
        "triangulation": triangulation,
        "expert_validation": validation,
        "author_check": author_check,
    }
    report_path = OUTPUT_DIR / "validation_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n  Saved to {report_path}")

    # Markdown report
    md = generate_markdown_report(triangulation, validation, author_check)
    md_path = OUTPUT_DIR / "validation_report.md"
    with open(md_path, "w") as f:
        f.write(md)
    print(f"  Saved to {md_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
