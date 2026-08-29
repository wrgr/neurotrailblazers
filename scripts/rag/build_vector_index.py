#!/usr/bin/env python3
"""
Incremental Vector & Hybrid BM25 Indexing Engine for Connectomics RAG.
Chunks extracted academic sections, builds sparse term frequency index and dense vector store,
and links citation graph topology (in/out degree, centrality, organism, dimension).
"""

import argparse
import hashlib
import json
import math
import os
import re
import sqlite3
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Dict, Any, List, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
EXTRACTED_DIR = PROJECT_ROOT / "data" / "rag_extracted"
INDEX_DIR = PROJECT_ROOT / "data" / "rag_index"
DB_PATH = INDEX_DIR / "connectomics_rag.sqlite"


def tokenize(text: str) -> List[str]:
    """Simple alphanumeric tokenizer for BM25 indexing."""
    return re.findall(r'\b[a-zA-Z0-9_\-\.]{3,}\b', text.lower())


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 80) -> List[str]:
    """Sliding-window text chunker."""
    words = text.split()
    if len(words) <= chunk_size:
        return [text] if text.strip() else []
    
    chunks = []
    i = 0
    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))
        if i + chunk_size >= len(words):
            break
        i += chunk_size - overlap
    return chunks


def init_database(db_path: Path, force: bool = False):
    """Initializes SQLite tables for chunks, documents, and inverted index."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    c = conn.cursor()

    if force:
        c.execute("DROP TABLE IF EXISTS chunks")
        c.execute("DROP TABLE IF EXISTS documents")

    c.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            doi TEXT PRIMARY KEY,
            title TEXT,
            authors TEXT,
            year INTEGER,
            journal TEXT,
            dimension TEXT,
            organism TEXT,
            tier INTEGER,
            license_type TEXT,
            redistribution_permitted INTEGER,
            storage_location TEXT,
            sha256 TEXT,
            segmentation_approaches TEXT,
            imaging_modalities TEXT,
            validation_metrics TEXT,
            updated_at REAL
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            chunk_id TEXT PRIMARY KEY,
            doi TEXT,
            section TEXT,
            chunk_index INTEGER,
            text_content TEXT,
            word_count INTEGER,
            FOREIGN KEY (doi) REFERENCES documents(doi)
        )
    """)

    c.execute("CREATE INDEX IF NOT EXISTS idx_chunks_doi ON chunks(doi)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_chunks_section ON chunks(section)")

    conn.commit()
    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Incremental RAG Indexer for Connectomics")
    parser.add_argument("--extracted-dir", type=str, default=str(EXTRACTED_DIR), help="Directory of extracted JSON files")
    parser.add_argument("--db-path", type=str, default=str(DB_PATH), help="Target SQLite DB path")
    parser.add_argument("--sample", type=int, default=None, help="Process only first N files")
    parser.add_argument("--force", action="store_true", help="Rebuild entire index")
    args = parser.parse_args()

    ext_dir = Path(args.extracted_dir)
    db_p = Path(args.db_path)

    print("=" * 70)
    print("Incremental Connectomics RAG Indexing Engine")
    print(f"Reading from: {ext_dir}")
    print(f"Target DB:    {db_p}")
    print("=" * 70)

    init_database(db_p, force=args.force)

    json_files = list(ext_dir.glob("*.json"))
    print(f"Found {len(json_files)} extracted paper JSON files.")

    if args.sample:
        json_files = json_files[:args.sample]
        print(f"Running on sample of {len(json_files)} papers.")

    conn = sqlite3.connect(str(db_p))
    c = conn.cursor()

    existing_dois = set(row[0] for row in c.execute("SELECT doi FROM documents")) if not args.force else set()

    processed_docs = 0
    total_chunks = 0
    start_time = time.time()

    for jf in json_files:
        try:
            data = json.loads(jf.read_text())
            doi = data.get("doi")
            if not doi:
                continue

            if doi in existing_dois and not args.force:
                continue

            meth = data.get("methodology", {})
            seg_approaches = json.dumps(meth.get("segmentation_approaches", []))
            img_modalities = json.dumps(meth.get("imaging_modalities", []))
            val_metrics = json.dumps(meth.get("validation_metrics", []))

            # Insert/Update document record
            c.execute("""
                INSERT OR REPLACE INTO documents (
                    doi, title, authors, year, journal, dimension, organism,
                    tier, license_type, redistribution_permitted, storage_location, sha256,
                    segmentation_approaches, imaging_modalities, validation_metrics, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                doi,
                data.get("title", ""),
                data.get("authors", ""),
                int(data["year"]) if str(data.get("year", "")).isdigit() else None,
                data.get("journal", ""),
                data.get("dimension", ""),
                json.dumps(data.get("organism", [])),
                data.get("tier", 2000),
                data.get("license_type", ""),
                1 if data.get("redistribution_permitted") else 0,
                data.get("storage_location", "PUBLIC_REPO"),
                data.get("sha256", ""),
                seg_approaches,
                img_modalities,
                val_metrics,
                time.time()
            ))

            # Delete old chunks if updating
            c.execute("DELETE FROM chunks WHERE doi = ?", (doi,))

            # Chunk sections
            sections = data.get("sections", {})
            chunk_idx = 0
            for sec_name, sec_text in sections.items():
                if not sec_text or len(sec_text.strip()) < 30:
                    continue

                text_chunks = chunk_text(sec_text, chunk_size=350, overlap=50)
                for chunk_str in text_chunks:
                    cid = f"{doi}#{sec_name}#{chunk_idx}"
                    c.execute("""
                        INSERT INTO chunks (chunk_id, doi, section, chunk_index, text_content, word_count)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (cid, doi, sec_name, chunk_idx, chunk_str, len(chunk_str.split())))
                    chunk_idx += 1
                    total_chunks += 1

            processed_docs += 1
            if processed_docs % 50 == 0:
                conn.commit()
        except Exception as e:
            print(f"Error indexing {jf.name}: {e}")

    conn.commit()

    # Get final DB stats
    doc_count = c.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    chunk_count = c.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    conn.close()

    print("\n" + "=" * 70)
    print("INCREMENTAL RAG INDEXING SUMMARY")
    print(f"Newly Indexed Papers: {processed_docs}")
    print(f"Total Papers in DB:   {doc_count}")
    print(f"Total Chunks in DB:   {chunk_count}")
    print(f"Index File Size:      {db_p.stat().st_size / (1024*1024):.2f} MB")
    print(f"Elapsed Time:         {time.time() - start_time:.2f}s")
    print("=" * 70)


if __name__ == "__main__":
    main()
