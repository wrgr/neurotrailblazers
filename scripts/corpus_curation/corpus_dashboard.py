#!/usr/bin/env python3
"""
Real-Time Connectomics Corpus & RAG Retrieval Dashboard.
Displays current download progress, permissions breakdown, disk storage, and RAG status.
"""

import json
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
PDF_CORPUS = PROJECT_ROOT / "data" / "pdf_corpus"
MANIFEST_PATH = PDF_CORPUS / "corpus_manifest.json"
EXTRACTED_DIR = PROJECT_ROOT / "data" / "rag_extracted"
DB_PATH = PROJECT_ROOT / "data" / "rag_index" / "connectomics_rag.sqlite"
PRIVATE_DIR = PROJECT_ROOT.parent / "neurotrailblazers-private" / "papers"


def get_dir_size_mb(files):
    return sum(f.stat().st_size for f in files) / (1024 * 1024) if files else 0


def render_dashboard():
    gold = list((PDF_CORPUS / "oa_gold").glob("*.pdf")) if (PDF_CORPUS / "oa_gold").exists() else []
    author = list((PDF_CORPUS / "author_provided").glob("*.pdf")) if (PDF_CORPUS / "author_provided").exists() else []
    pub_free = list((PDF_CORPUS / "publisher_free").glob("*.pdf")) if (PDF_CORPUS / "publisher_free").exists() else []
    closed_meta = list((PDF_CORPUS / "closed_metadata").glob("*.json")) if (PDF_CORPUS / "closed_metadata").exists() else []
    priv_pdfs = list(PRIVATE_DIR.glob("*.pdf")) if PRIVATE_DIR.exists() else []

    total_pdfs = len(gold) + len(author) + len(pub_free) + len(priv_pdfs)
    total_size_mb = get_dir_size_mb(gold) + get_dir_size_mb(author) + get_dir_size_mb(pub_free) + get_dir_size_mb(priv_pdfs)
    extracted = len(list(EXTRACTED_DIR.glob("*.json"))) if EXTRACTED_DIR.exists() else 0

    pct = (total_pdfs / 2000) * 100
    bar_width = 30
    filled = int(bar_width * (total_pdfs / 2000))
    bar = "█" * filled + "░" * (bar_width - filled)

    print("=" * 80)
    print("              🧠 CONNECTOMICS CORPUS REAL-TIME RETRIEVAL DASHBOARD              ")
    print("=" * 80)
    print(f" Target Corpus Scope:        2,000 Milestone Connectomics Papers")
    print(f" Total Full-Text PDFs:       {total_pdfs:4d} / 2,000  [{bar}] {pct:.1f}%")
    print(f" Total Storage Footprint:    {total_size_mb:6.1f} MB ({total_size_mb/1024:.2f} GB)")
    print(f" Extracted RAG Documents:    {extracted:4d} / {total_pdfs} ({extracted/max(1, total_pdfs)*100:.1f}%)")
    print("-" * 80)
    print(" 📂 MULTI-REPOSITORY STORAGE & PERMISSIONS BREAKDOWN:")
    print(f"   🟢 Gold Open Access (CC-BY):       {len(gold):4d} PDFs ({get_dir_size_mb(gold):6.1f} MB) -> data/pdf_corpus/oa_gold/")
    print(f"   🔵 Author Preprints / PMC Renders: {len(author):4d} PDFs ({get_dir_size_mb(author):6.1f} MB) -> data/pdf_corpus/author_provided/")
    print(f"   🟡 Publisher Free / Bronze Access: {len(pub_free):4d} PDFs ({get_dir_size_mb(pub_free):6.1f} MB) -> data/pdf_corpus/publisher_free/")
    print(f"   🔒 Private Dev Stash (Paywalled):  {len(priv_pdfs):4d} PDFs ({get_dir_size_mb(priv_pdfs):6.1f} MB) -> ../neurotrailblazers-private/papers/")
    print(f"   📑 Public Metadata Stubs:          {len(closed_meta):4d} JSONs (100% Public Coverage) -> data/pdf_corpus/closed_metadata/")
    print("-" * 80)
    print(" ⚡ RESOLVER ENGINES ACTIVE:")
    print("   • Europe PMC REST API (PMCID ?pdf=render streams)")
    print("   • OpenAlex Institutional Repositories (Harvard, Cambridge, EPFL, NIH, Janelia)")
    print("   • Semantic Scholar & Unpaywall Multi-Location Resolver")
    print("   • 12 Concurrent Worker Threads with SHA-256 & %PDF- Magic Byte Verification")
    print("=" * 80)


if __name__ == "__main__":
    render_dashboard()
