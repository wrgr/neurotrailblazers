#!/usr/bin/env python3
"""
Step 8: Generate OCAR structured summaries for each reading-list paper.

OCAR fields (matching _data/journal_papers.yml schema):
  opportunity  — the gap or problem the paper addresses
  challenge    — what made it hard / why it wasn't obvious
  action       — what the authors specifically did
  resolution   — what they found / demonstrated / released
  future_work  — open questions the paper leaves behind

Also generates:
  summaries.beginner / .intermediate / .advanced
  tags (OpenAlex concepts → connectomics tag vocabulary)
  discussion_prompts (3 questions for journal club)

Input:   output/reading_list.json  (from 06_reading_list.py)
Cache:   output/ocar_cache/        (one JSON per paper — resumable)
Output:  output/ocar_entries.json  (all OCAR records)
         output/ocar_entries.yaml  (drop-in for _data/journal_papers.yml)

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  python 08_generate_ocar.py
  python 08_generate_ocar.py --limit 50      # first 50 papers only
  python 08_generate_ocar.py --from-paper 51 # resume from paper 51
"""
import argparse
import json
import os
import re
import time
from pathlib import Path

import anthropic

from config import OUTPUT_DIR, CACHE_DIR

MODEL = "claude-sonnet-4-6"
OCAR_CACHE = OUTPUT_DIR / "ocar_cache"
OCAR_CACHE.mkdir(parents=True, exist_ok=True)

# ── Prompt ────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are a neuroscience expert writing structured paper summaries for the NeuroTrailblazers \
educational platform. Your audience ranges from motivated undergraduates to active researchers \
in connectomics, electron microscopy, and neural circuit analysis.

Respond ONLY with valid JSON — no markdown fences, no explanation outside the JSON object.
"""

def build_user_prompt(paper):
    abstract = (paper.get("abstract") or "").strip()
    concepts = ", ".join(paper.get("concepts", [])[:8])
    authors = ", ".join(paper.get("authors", [])[:5])
    if len(paper.get("authors", [])) > 5:
        authors += " et al."

    return f"""\
Generate a structured OCAR summary for this paper.

PAPER:
  Title:   {paper.get("title", "")}
  Authors: {authors}
  Year:    {paper.get("year", "")}
  Journal: {paper.get("journal", "")}
  DOI:     {paper.get("doi", "")}
  Role:    {paper.get("role", "")}  (methods | dataset | biology | review)
  Concepts (OpenAlex): {concepts}
  Abstract: {abstract if abstract else "[not available — infer from title, journal, and concepts]"}

Return a JSON object with EXACTLY these keys:
{{
  "ocar": {{
    "opportunity": "1-2 sentences: what gap or unmet need motivated this work",
    "challenge":   "1-2 sentences: what made this problem hard / non-obvious",
    "action":      "2-3 sentences: what the authors specifically did (methods, datasets, approach)",
    "resolution":  "2-3 sentences: key findings, what was demonstrated or released",
    "future_work": "1-2 sentences: open questions or limitations the paper leaves behind"
  }},
  "summaries": {{
    "beginner":     "2-3 sentences for a curious undergrad with intro biology",
    "intermediate": "3-4 sentences for a grad student with neuroscience background",
    "advanced":     "3-4 sentences for a researcher — include methodological nuance and caveats"
  }},
  "discussion_prompts": [
    "question 1 suitable for journal club (specific to this paper)",
    "question 2",
    "question 3"
  ],
  "dimension": "pick ONE: connectomics | image-acquisition | segmentation | proofreading | graph-analysis | neuroanatomy | cell-types | infrastructure | neuroai | methods-general | review",
  "tags": ["up to 6 tags from the paper's content, format: category:term, e.g. imaging:fib-sem, species:drosophila, tool:catmaid"]
}}
"""


# ── Abstract reconstruction ───────────────────────────────────────────

def get_abstract_from_cache(openalex_id):
    safe_id = openalex_id.replace("https://openalex.org/", "")
    cache_path = CACHE_DIR / "works" / f"{safe_id}.json"
    if not cache_path.exists():
        return ""
    try:
        with open(cache_path) as f:
            work = json.load(f)
        aii = work.get("abstract_inverted_index") or {}
        if not aii:
            return ""
        max_pos = max(pos for positions in aii.values() for pos in positions)
        words = [""] * (max_pos + 1)
        for word, positions in aii.items():
            for pos in positions:
                if 0 <= pos <= max_pos:
                    words[pos] = word
        return " ".join(w for w in words if w)
    except Exception:
        return ""


# ── OCAR generation ───────────────────────────────────────────────────

def generate_ocar(client, paper):
    """Call Claude to generate OCAR for one paper. Returns parsed dict."""
    prompt = build_user_prompt(paper)
    response = client.messages.create(
        model=MODEL,
        max_tokens=1200,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.content[0].text.strip()
    # Strip markdown fences if model adds them despite instructions
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def ocar_cache_path(openalex_id):
    safe = openalex_id.replace("https://openalex.org/", "")
    return OCAR_CACHE / f"{safe}.json"


def load_cached_ocar(openalex_id):
    p = ocar_cache_path(openalex_id)
    if p.exists():
        with open(p) as f:
            return json.load(f)
    return None


def save_cached_ocar(openalex_id, data):
    with open(ocar_cache_path(openalex_id), "w") as f:
        json.dump(data, f, indent=2)


# ── YAML serialiser (no pyyaml dependency) ────────────────────────────

def _yaml_str(s, indent=0):
    """Emit a YAML block scalar for multi-sentence strings."""
    s = (s or "").replace('"', "'")
    if "\n" in s or len(s) > 80:
        pad = " " * (indent + 2)
        lines = "\n".join(pad + line for line in s.splitlines())
        return f"|\n{lines}"
    return f'"{s}"'


def entry_to_yaml(entry):
    """Convert one reading-list + ocar entry to YAML text."""
    ocar = entry.get("ocar", {})
    summaries = entry.get("summaries", {})
    prompts = entry.get("discussion_prompts", [])
    tags = entry.get("tags", [])
    doi = entry.get("doi", "")
    authors_list = entry.get("authors", [])
    authors_str = ", ".join(a.split()[-1] for a in authors_list[:3])
    if len(authors_list) > 3:
        authors_str += " et al."
    slug = re.sub(r"[^a-z0-9]+", "-", (entry.get("title") or "").lower())[:60].strip("-")

    lines = [
        f"- id: {slug}",
        f"  title: {_yaml_str(entry.get('title',''))}",
        f"  authors: {_yaml_str(authors_str)}",
        f"  year: {entry.get('year','')}",
        f"  journal: {_yaml_str(entry.get('journal',''))}",
        f"  doi: {doi or 'null'}",
        f"  dimension: {entry.get('dimension','connectomics')}",
        f"  reading_phase: {entry.get('phase','')}",
        f"  composite_score: {entry.get('composite_score',0)}",
        f"  role: {entry.get('role','')}",
        "  tags:",
    ]
    for tag in tags:
        lines.append(f"  - {tag}")

    lines.append("  ocar:")
    for field in ["opportunity", "challenge", "action", "resolution", "future_work"]:
        val = ocar.get(field, "")
        lines.append(f"    {field}: {_yaml_str(val, indent=4)}")

    lines.append("  summaries:")
    for level in ["beginner", "intermediate", "advanced"]:
        val = summaries.get(level, "")
        lines.append(f"    {level}: {_yaml_str(val, indent=6)}")

    if prompts:
        lines.append("  discussion_prompts:")
        for p in prompts:
            lines.append(f"  - {_yaml_str(p)}")

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None,
                        help="Max papers to process (default: all)")
    parser.add_argument("--from-paper", type=int, default=1,
                        help="Start from reading_order N (for resuming)")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: set ANTHROPIC_API_KEY environment variable")
        return

    client = anthropic.Anthropic(api_key=api_key)

    print("Loading reading list...")
    with open(OUTPUT_DIR / "reading_list.json") as f:
        reading_list = json.load(f)

    # Filter to requested range
    papers = [p for p in reading_list if p.get("reading_order", 0) >= args.from_paper]
    if args.limit:
        papers = papers[:args.limit]

    print(f"Processing {len(papers)} papers (reading order "
          f"{papers[0].get('reading_order')} – {papers[-1].get('reading_order')})")

    results = []
    errors = []

    for i, paper in enumerate(papers, 1):
        pid = paper["openalex_id"]
        order = paper.get("reading_order", i)

        # Check cache
        cached = load_cached_ocar(pid)
        if cached:
            results.append({**paper, **cached})
            print(f"  [{order:3}/{len(reading_list)}] (cached) {paper.get('title','')[:55]}...")
            continue

        # Ensure abstract is populated
        if not paper.get("abstract"):
            paper["abstract"] = get_abstract_from_cache(pid)

        print(f"  [{order:3}/{len(reading_list)}] Generating... {paper.get('title','')[:55]}...")

        for attempt in range(3):
            try:
                ocar_data = generate_ocar(client, paper)
                entry = {
                    **paper,
                    "ocar":               ocar_data.get("ocar", {}),
                    "summaries":          ocar_data.get("summaries", {}),
                    "discussion_prompts": ocar_data.get("discussion_prompts", []),
                    "dimension":          ocar_data.get("dimension", "connectomics"),
                    "tags":               ocar_data.get("tags", []),
                }
                save_cached_ocar(pid, {
                    "ocar":               entry["ocar"],
                    "summaries":          entry["summaries"],
                    "discussion_prompts": entry["discussion_prompts"],
                    "dimension":          entry["dimension"],
                    "tags":               entry["tags"],
                })
                results.append(entry)
                break
            except json.JSONDecodeError as e:
                print(f"    JSON parse error (attempt {attempt+1}): {e}")
                time.sleep(2 ** attempt)
            except anthropic.RateLimitError:
                wait = 30 * (attempt + 1)
                print(f"    Rate limit, waiting {wait}s...")
                time.sleep(wait)
            except Exception as e:
                print(f"    Error (attempt {attempt+1}): {e}")
                time.sleep(2 ** attempt)
        else:
            print(f"    FAILED after 3 attempts, skipping.")
            errors.append(paper.get("title", pid))

        # Small politeness pause
        time.sleep(0.3)

    # Save combined JSON
    out_json = OUTPUT_DIR / "ocar_entries.json"
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved {len(results)} entries → {out_json}")

    # Save YAML
    out_yaml = OUTPUT_DIR / "ocar_entries.yaml"
    yaml_lines = [
        "# Auto-generated OCAR entries for EM connectomics reading list",
        "# Produced by 08_generate_ocar.py using claude-sonnet-4-6",
        "# Fields match _data/journal_papers.yml schema",
        "papers:",
    ]
    for entry in results:
        yaml_lines.append(entry_to_yaml(entry))
    with open(out_yaml, "w") as f:
        f.write("\n".join(yaml_lines))
    print(f"Saved YAML → {out_yaml}")

    if errors:
        print(f"\nFailed ({len(errors)}):")
        for t in errors:
            print(f"  - {t[:70]}")

    print("\nDone.")


if __name__ == "__main__":
    main()
