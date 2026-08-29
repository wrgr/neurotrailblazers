#!/usr/bin/env python3
"""
Incremental Section-Aware Text Extraction Tool for Connectomics RAG.
Extracts clean, structured text and academic sections (Abstract, Methods, Results, Discussion)
from PDF manuscripts and saves per-paper JSON representations incrementally.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DEFAULT_PDF_ROOT = PROJECT_ROOT / "data" / "pdf_corpus"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data" / "rag_extracted"
MANIFEST_PATH = PROJECT_ROOT / "data" / "pdf_corpus" / "corpus_manifest.json"


def sanitize_filename(doi: str) -> str:
    return re.sub(r'[/\\:*?"<>|]', '_', doi.strip().lower())


def extract_raw_text_from_pdf(pdf_path: Path) -> str:
    """Extracts raw text stream using pypdf or fallback text regex."""
    text_chunks = []
    try:
        import pypdf
        reader = pypdf.PdfReader(str(pdf_path))
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text_chunks.append(t)
        return "\n\n".join(text_chunks)
    except Exception:
        pass

    # Fallback: PyMuPDF / fitz if available
    try:
        import fitz
        doc = fitz.open(str(pdf_path))
        for page in doc:
            text_chunks.append(page.get_text())
        return "\n\n".join(text_chunks)
    except Exception:
        pass

    # Basic binary stream text extractor fallback for clean strings
    try:
        raw_bytes = pdf_path.read_bytes()
        ascii_matches = re.findall(rb'[\x20-\x7E\s]{6,}', raw_bytes)
        return "\n".join([m.decode('utf-8', errors='ignore') for m in ascii_matches if len(m) > 10])
    except Exception:
        return ""


def detect_methodological_traits(full_text: str, sections: Dict[str, str], metadata: Dict[str, Any]) -> Dict[str, Any]:
    """Detects segmentation algorithms, imaging modalities, and validation metrics from full text."""
    corpus_text = (full_text + " " + json.dumps(sections) + " " + json.dumps(metadata)).lower()
    
    # 1. Segmentation Approaches
    seg_approaches = []
    if re.search(r'\b(flood[\s\-]filling|ffn)\b', corpus_text):
        seg_approaches.append("Flood-Filling Networks (FFN)")
    if re.search(r'\b(3d\s+u[\s\-]net|unet|u[\s\-]net)\b', corpus_text):
        seg_approaches.append("3D U-Net / CNN Affinity")
    if re.search(r'\b(watershed|seeded\s+watershed)\b', corpus_text):
        seg_approaches.append("Watershed / Supervoxel Agglomeration")
    if re.search(r'\b(random\s+forest|ilastik)\b', corpus_text):
        seg_approaches.append("Random Forest (Ilastik/Weka)")
    if re.search(r'\b(vision\s+transformer|vit|transformer[\s\-]based\s+segmentation)\b', corpus_text):
        seg_approaches.append("Vision Transformer (ViT)")
    if re.search(r'\b(manual\s+skeleton|manual\s+tracing|catmaid|knossos)\b', corpus_text):
        seg_approaches.append("Manual Skeletonization / Tracing")
    if re.search(r'\b(pypchunkedgraph|cave|neuprint)\b', corpus_text):
        seg_approaches.append("Graph-Based Proofreading (CAVE/PyChunkedGraph)")
    if not seg_approaches:
        seg_approaches.append("General Dense Volume Segmentation")

    # 2. Imaging Modalities
    modalities = []
    if re.search(r'\b(fib[\s\-]sem|focused\s+ion\s+beam)\b', corpus_text):
        modalities.append("FIB-SEM")
    if re.search(r'\b(sstem|serial[\s\-]section\s+tem|tem\s+grid)\b', corpus_text):
        modalities.append("Serial-Section TEM (ssTEM)")
    if re.search(r'\b(sbf[\s\-]sem|serial\s+block[\s\-]face)\b', corpus_text):
        modalities.append("SBF-SEM")
    if re.search(r'\b(multibeam|multi[\s\-]beam\s+sem|msem)\b', corpus_text):
        modalities.append("Multi-Beam SEM")
    if re.search(r'\b(atum[\s\-]sem|automated\s+tape)\b', corpus_text):
        modalities.append("ATUM-SEM")
    if re.search(r'\b(synchrotron|x[\s\-]ray\s+nano|nano[\s\-]ct)\b', corpus_text):
        modalities.append("Synchrotron X-ray Nano-CT")

    # 3. Error Metrics & Quality Standards
    metrics = []
    if re.search(r'\b(expected\s+run\s+length|erl)\b', corpus_text):
        metrics.append("Expected Run Length (ERL)")
    if re.search(r'\b(variation\s+of\s+information|vi_split|vi_merge|\bvi\b)\b', corpus_text):
        metrics.append("Variation of Information (VI)")
    if re.search(r'\b(rand\s+error|rand\s+index|adapted\s+rand)\b', corpus_text):
        metrics.append("Rand Error / Rand Index")
    if re.search(r'\b(precision|recall|f1[\s\-]score|f1\s+boundary)\b', corpus_text):
        metrics.append("Boundary F1 / Precision-Recall")

    return {
        "segmentation_approaches": seg_approaches,
        "imaging_modalities": modalities,
        "validation_metrics": metrics
    }


def segment_academic_sections(full_text: str, metadata: Dict[str, Any]) -> Dict[str, str]:
    """Partitions paper text into discrete academic sections."""
    sections = {
        "abstract": metadata.get("abstract") or "",
        "opportunity_intro": "",
        "methods_protocol": "",
        "results_findings": "",
        "discussion_horizons": ""
    }

    if not full_text:
        if metadata.get("ocar"):
            sections["opportunity_intro"] = metadata["ocar"].get("opportunity", "")
            sections["methods_protocol"] = metadata["ocar"].get("action", "")
            sections["results_findings"] = metadata["ocar"].get("resolution", "")
            sections["discussion_horizons"] = metadata["ocar"].get("future_work", "")
        return sections

    # Common section header regexes
    sec_patterns = [
        ("abstract", r"(?i)\babstract\b"),
        ("opportunity_intro", r"(?i)\b(introduction|background)\b"),
        ("methods_protocol", r"(?i)\b(materials\s+and\s+methods|methods|experimental\s+procedures|computational\s+methods)\b"),
        ("results_findings", r"(?i)\b(results|findings|circuit\s+reconstruction)\b"),
        ("discussion_horizons", r"(?i)\b(discussion|conclusion|future\s+directions)\b")
    ]

    lines = full_text.splitlines()
    current_sec = "opportunity_intro"
    sec_buffers = {k: [] for k in sections.keys()}

    for line in lines:
        sline = line.strip()
        if len(sline) < 60 and len(sline) > 3:
            matched = False
            for sec_key, pat in sec_patterns:
                if re.match(pat, sline):
                    current_sec = sec_key
                    matched = True
                    break
            if matched:
                continue

        sec_buffers[current_sec].append(line)

    for k in sections.keys():
        extracted = "\n".join(sec_buffers[k]).strip()
        if len(extracted) > 50:
            sections[k] = extracted
        elif metadata.get("ocar") and k in ["opportunity_intro", "methods_protocol", "results_findings", "discussion_horizons"]:
            ocar_map = {
                "opportunity_intro": "opportunity",
                "methods_protocol": "action",
                "results_findings": "resolution",
                "discussion_horizons": "future_work"
            }
            sections[k] = metadata["ocar"].get(ocar_map[k], "")

    return sections


def main():
    parser = argparse.ArgumentParser(description="Incremental connectomics full-text extractor")
    parser.add_argument("--pdf-dir", type=str, default=str(DEFAULT_PDF_ROOT), help="Base directory containing PDFs")
    parser.add_argument("--output-dir", type=str, default=str(DEFAULT_OUTPUT_DIR), help="Output directory for extracted JSONs")
    parser.add_argument("--sample", type=int, default=None, help="Process only first N PDFs for testing")
    parser.add_argument("--force", action="store_true", help="Re-extract even if already extracted")
    args = parser.parse_args()

    pdf_root = Path(args.pdf_dir)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Incremental Connectomics Full-Text Extraction Engine")
    print(f"Reading from: {pdf_root}")
    print(f"Saving to:   {out_dir}")
    print("=" * 70)

    manifest = {}
    if MANIFEST_PATH.exists():
        manifest = json.loads(MANIFEST_PATH.read_text())

    pdf_files = list(pdf_root.rglob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files in corpus directories.")

    if args.sample:
        pdf_files = pdf_files[:args.sample]
        print(f"Running sample of {len(pdf_files)} files.")

    processed = 0
    skipped = 0
    start_time = time.time()

    for pdf_p in pdf_files:
        doi_slug = pdf_p.stem
        out_json = out_dir / f"{doi_slug}.json"

        # Check incremental cache
        if out_json.exists() and not args.force:
            skipped += 1
            continue

        raw_text = extract_raw_text_from_pdf(pdf_p)
        file_sha = hashlib.sha256(pdf_p.read_bytes()).hexdigest()
        
        # Match metadata from manifest
        norm_doi = doi_slug.replace("_", "/")
        meta = manifest.get(norm_doi, {})

        sections = segment_academic_sections(raw_text, meta)

        methods_traits = detect_methodological_traits(raw_text, sections, meta)

        doc_record = {
            "doi": meta.get("doi", norm_doi),
            "title": meta.get("title", ""),
            "authors": meta.get("authors", ""),
            "year": meta.get("year", ""),
            "journal": meta.get("journal", ""),
            "dimension": meta.get("dimension", ""),
            "organism": meta.get("organism", []),
            "tier": meta.get("tier", 2000),
            "license_type": meta.get("license_type", ""),
            "redistribution_permitted": meta.get("redistribution_permitted", False),
            "storage_location": meta.get("storage_location", "PUBLIC_REPO"),
            "sha256": file_sha,
            "raw_text_length": len(raw_text),
            "full_text": raw_text,
            "sections": sections,
            "methodology": methods_traits
        }

        out_json.write_text(json.dumps(doc_record, indent=2))
        processed += 1

    print("\n" + "=" * 70)
    print("INCREMENTAL EXTRACTION SUMMARY")
    print(f"Newly Processed: {processed}")
    print(f"Skipped (Cached): {skipped}")
    print(f"Total Extracted Files in {out_dir}: {len(list(out_dir.glob('*.json')))}")
    print(f"Elapsed Time: {time.time() - start_time:.2f}s")
    print("=" * 70)


if __name__ == "__main__":
    main()
