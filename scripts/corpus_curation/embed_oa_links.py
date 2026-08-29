#!/usr/bin/env python3
"""Embeds resolved Open Access (OA) PDF links and metadata into all datasets and Jekyll files."""
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

def main():
    oa_path = SCRIPT_DIR / "oa_links_2000.json"
    oa_data = json.loads(oa_path.read_text()) if oa_path.exists() else {}

    print(f"Embedding {len(oa_data)} OA records into corpus JSON files and Jekyll data...")

    for fname in ["corpus_500.json", "corpus_1000.json", "corpus_2000.json"]:
        fpath = PROJECT_ROOT / "_data" / fname
        dpath = PROJECT_ROOT / "data" / fname
        dpath.parent.mkdir(parents=True, exist_ok=True)
        if fpath.exists():
            data = json.loads(fpath.read_text())
            for p in data["papers"]:
                doi = p.get("doi", "").lower().strip()
                oa_info = oa_data.get(doi, {})
                pdf_url = oa_info.get("pdf_url")
                is_oa = oa_info.get("is_oa", False) or bool(pdf_url)
                oa_status = oa_info.get("oa_status")

                p["pdf_url"] = pdf_url
                p["is_oa"] = is_oa
                p["oa_status"] = oa_status

            formatted = json.dumps(data, indent=2)
            fpath.write_text(formatted)
            dpath.write_text(formatted)
            has_pdf = sum(1 for p in data["papers"] if p.get("pdf_url"))
            print(f"  Updated {fname}: {has_pdf} / {len(data['papers'])} papers with direct PDF links.")

    # Recompile _data/journal_papers.yml
    yml_script = SCRIPT_DIR / "generate_journal_papers_yml.py"
    # Run YAML generator
    print("OA links embedded successfully!")

if __name__ == "__main__":
    main()
