#!/usr/bin/env python3
"""Re-derive the bibliographic fields of _data/journal_papers.yml from
_data/corpus_2000.json.

Why this exists
---------------
`scripts/corpus_curation/generate_journal_papers_yml.py` compiled the 2,000-paper
file from `final_selection.json`, whose author strings were empty, whose years
disagreed with the corpus on 818 records, whose venue names were truncated at 40
characters, and whose `citation` field was a self-attribution template
("NeuroTrailblazers Consortium (YEAR). Title"). `corpus_2000.json` -- the file the
OCAR cards and summaries were generated from -- carries full authors, the
correct year, the full venue and an abstract on 2,000/2,000 records. This
script joins the two on DOI and rewrites only the fields that were wrong.

What it changes, per record
---------------------------
  authors         <- corpus `authors` ("; "-separated full names; graph.md
                     splits on ';' for node labels, the card renders it as-is)
  year            <- corpus `year`
  journal         <- corpus `venue` (full name, not truncated)
  inclusion_role  <- era recomputed from the corrected year (history <= 2018,
                     contemporary 2019-2023, sota >= 2024). The generator
                     derived it from the wrong year; the era facet and the
                     card's era chip read it.
  reading_phase   <- same thresholds (1_foundations / 2_contemporary / 3_sota)
  citation        <- "Surname et al. (YEAR). Title. Journal. https://doi.org/DOI"
                     ("Surname & Surname" for two authors, "Surname" for one)
  abstract        <- corpus `abstract` (new field, inserted before
                     `plain_language_summary`)

Everything else -- id, uuid, title, tier, graph metrics, cites, tags, ocar,
summaries, discussion_prompts, pdf_url, ... -- is copied through byte-for-byte.
Record order is preserved.

How it writes
-------------
The file is generated one scalar per line (see the generator's
`escape_yaml_str`), so this edits lines in place rather than round-tripping
through a YAML emitter; a PyYAML dump would restyle all 97,000 lines and hide
the real change in review. After writing to a temporary file the result is
parsed and compared record-by-record against the original: every untouched
key must be equal, the only new key must be `abstract`, and ids must appear in
the same order. On any mismatch nothing is written.

It also rebuilds the two facet views that depend on year:
_data/paper_views/era.json and _data/paper_views/year.json.

Usage:
    python3 scripts/derive_journal_papers.py            # rewrite in place
    python3 scripts/derive_journal_papers.py --dry-run  # report only
"""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
import tempfile
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "journal_papers.yml"
CORPUS = ROOT / "_data" / "corpus_2000.json"
VIEWS = ROOT / "_data" / "paper_views"

# Fields this script owns. Everything else must survive unchanged.
REWRITTEN = {"authors", "year", "journal", "inclusion_role", "reading_phase", "citation"}
ADDED = {"abstract"}

RECORD_RE = re.compile(r"^- id: ")
KEY_RE = re.compile(r"^  ([a-z_0-9]+):")


# ---------------------------------------------------------------------------
# Scalars, in the generator's style
# ---------------------------------------------------------------------------
def quote(s: str) -> str:
    """Single-quoted flow scalar, one line -- identical to the generator's
    escape_yaml_str so unchanged values would re-emit byte-for-byte."""
    if not s:
        return "''"
    s = s.replace("\n", " ").replace("\r", " ").strip()
    return "'" + s.replace("'", "''") + "'"


def clean_abstract(text: str) -> str:
    """Normalise a corpus abstract for publication.

    Four corpus abstracts contain newlines. One is a real four-paragraph
    abstract; the others are scraped bioRxiv HTML -- a lone "Abstract" heading,
    whitespace-only lines, and inline-italic words split onto their own lines.
    A blank line, or a line ending a sentence followed by a line starting one,
    is a paragraph break; other consecutive lines are fragments of one
    paragraph and are re-joined (no space before punctuation).
    """
    lines = [l.strip() for l in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    if lines and lines[0].lower() == "abstract":
        lines = lines[1:]
    paragraphs, cur = [], ""
    for line in lines:
        if not line:
            if cur:
                paragraphs.append(cur)
            cur = ""
        elif not cur:
            cur = line
        elif line[0] in ",.;:)]":
            cur += line
        elif cur[-1] in ".?!" and re.match(r"[A-Z0-9]", line) and len(line.split()) > 3:
            paragraphs.append(cur)  # sentence ended, a new sentence starts: paragraph break
            cur = line
        else:
            cur += " " + line
    if cur:
        paragraphs.append(cur)
    return "\n\n".join(paragraphs)


def scalar_lines(key: str, value: str, indent: str = "  ") -> list[str]:
    """Emit `key: value`. Multi-paragraph text becomes a `|-` block so the
    paragraph breaks survive; single-paragraph text is single-quoted."""
    value = value.replace("\r\n", "\n").replace("\r", "\n").strip()
    if "\n" not in value:
        return [f"{indent}{key}: {quote(value)}"]
    out = [f"{indent}{key}: |-"]
    for line in value.split("\n"):
        out.append(f"{indent}  {line.rstrip()}" if line.strip() else "")
    return out


# ---------------------------------------------------------------------------
# Names
# ---------------------------------------------------------------------------
GROUP_RE = re.compile(
    r"\b(consortium|collaboration|group|team|project|initiative|network|committee|alliance)\b",
    re.IGNORECASE,
)
SUFFIXES = {"jr", "sr", "ii", "iii", "iv"}
PARTICLES = {
    "van", "von", "de", "der", "den", "del", "della", "di", "da", "dos", "das",
    "du", "la", "le", "las", "los", "ter", "ten", "el", "al", "bin", "ibn", "y",
    "af", "av", "zu", "op", "'t",
}


def split_authors(authors: str) -> list[str]:
    return [a.strip() for a in authors.split(";") if a.strip()]


def surname(name: str) -> str:
    """Best-effort family name for a citation.

    Handles "Jesse Gray", "Daniel J. White", "JG White", "Denk W" (surname then
    initials), "Martijn P. van den Heuvel", "John Smith Jr", and leaves group
    authors ("MICrONS Consortium") whole.
    """
    name = name.strip()
    if GROUP_RE.search(name):
        return name
    toks = name.replace(",", " ").split()
    if not toks:
        return name
    while len(toks) > 1 and toks[-1].lower().rstrip(".") in SUFFIXES:
        toks.pop()
    # "Denk W", "Lee WCA": trailing run of bare capitals is initials.
    if len(toks) > 1 and re.fullmatch(r"[A-Z]{1,3}", toks[-1]):
        toks.pop()
        while len(toks) > 1 and re.fullmatch(r"[A-Z]{1,3}", toks[-1]):
            toks.pop()
        return " ".join(toks)
    i = len(toks) - 1
    while i > 0 and toks[i - 1].lower() in PARTICLES:
        i -= 1
    return " ".join(toks[i:])


def author_label(authors: str) -> str:
    names = split_authors(authors)
    if not names:
        return ""
    if len(names) == 1:
        return surname(names[0])
    if len(names) == 2:
        return f"{surname(names[0])} & {surname(names[1])}"
    return f"{surname(names[0])} et al."


def end_stop(text: str) -> str:
    text = text.strip()
    return text if text[-1:] in ".?!" else text + "."


def build_citation(authors: str, year: int, title: str, journal: str, doi: str) -> str:
    parts = [f"{author_label(authors)} ({year}).", end_stop(title)]
    if journal.strip():
        parts.append(end_stop(journal))
    if doi:
        parts.append(f"https://doi.org/{doi}")
    return " ".join(parts)


# ---------------------------------------------------------------------------
# Era
# ---------------------------------------------------------------------------
def era_for(year: int) -> str:
    if year <= 2018:
        return "history"
    if year <= 2023:
        return "contemporary"
    return "sota"


PHASE = {"history": "1_foundations", "contemporary": "2_contemporary", "sota": "3_sota"}


# ---------------------------------------------------------------------------
# Join
# ---------------------------------------------------------------------------
def norm_title(t: str) -> str:
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())


def load_corpus():
    papers = json.loads(CORPUS.read_text(encoding="utf-8"))["papers"]
    by_doi = {}
    by_title = {}
    for p in papers:
        doi = (p.get("doi") or "").strip().lower()
        if doi:
            by_doi[doi] = p
        by_title.setdefault(norm_title(p.get("title", "")), p)
    return papers, by_doi, by_title


# ---------------------------------------------------------------------------
# Rewrite
# ---------------------------------------------------------------------------
def rewrite_record(lines: list[str], rec: dict, cp: dict) -> list[str]:
    """Return the record's lines with the owned fields replaced."""
    year = int(cp["year"])
    era = era_for(year)
    new_values = {
        "authors": quote(cp["authors"]),
        "year": str(year),
        "journal": quote(cp["venue"]),
        "inclusion_role": era,
        "reading_phase": PHASE[era],
        "citation": quote(build_citation(cp["authors"], year, rec["title"], cp["venue"], rec.get("doi") or cp["doi"])),
    }
    abstract_lines = scalar_lines("abstract", clean_abstract(cp["abstract"]))

    out = []
    seen = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = KEY_RE.match(line)
        key = m.group(1) if m else None
        if key in new_values:
            out.append(f"  {key}: {new_values[key]}")
            seen.add(key)
            i += 1
            continue
        if key == "abstract":
            # Re-run: drop the previous abstract (and its block body, if any).
            i += 1
            while i < len(lines) and (lines[i].startswith("    ") or lines[i] == ""):
                i += 1
            continue
        if key == "plain_language_summary":
            out.extend(abstract_lines)
            seen.add("abstract")
        out.append(line)
        i += 1

    missing = (set(new_values) | {"abstract"}) - seen
    if missing:
        raise RuntimeError(f"{rec['id']}: could not place field(s) {sorted(missing)}")
    return out


def split_records(text: str):
    """Yield (header_lines, [record_lines, ...])."""
    lines = text.split("\n")
    header = []
    records = []
    cur = None
    for line in lines:
        if RECORD_RE.match(line):
            cur = [line]
            records.append(cur)
        elif cur is None:
            header.append(line)
        else:
            cur.append(line)
    # The file ends with "\n", so the last record carries one trailing "".
    if records and records[-1] and records[-1][-1] == "":
        records[-1].pop()
        trailer = [""]
    else:
        trailer = []
    return header, records, trailer


def verify(old_recs: list[dict], new_recs: list[dict], matches: dict) -> list[str]:
    problems = []
    if len(old_recs) != len(new_recs):
        problems.append(f"record count changed: {len(old_recs)} -> {len(new_recs)}")
        return problems
    for o, n in zip(old_recs, new_recs):
        cp = matches.get(o["id"])
        if cp is not None:
            if n.get("abstract") != clean_abstract(cp["abstract"]):
                problems.append(f"{o['id']}: abstract did not round-trip")
            if n.get("authors") != cp["authors"].strip() or int(n.get("year")) != int(cp["year"]) \
                    or n.get("journal") != cp["venue"].strip():
                problems.append(f"{o['id']}: authors/year/journal did not round-trip")
        if o["id"] != n["id"]:
            problems.append(f"order changed at {o['id']} / {n['id']}")
            break
        extra = set(n) - set(o)
        lost = set(o) - set(n)
        if extra - ADDED or lost:
            problems.append(f"{o['id']}: keys added {sorted(extra - ADDED)} lost {sorted(lost)}")
        for k in o:
            if k in REWRITTEN or k in ADDED:
                continue
            if o[k] != n.get(k):
                problems.append(f"{o['id']}: field {k} changed")
        if list(k for k in o if k not in ADDED) != list(k for k in n if k not in ADDED):
            problems.append(f"{o['id']}: key order changed")
        if len(problems) > 20:
            problems.append("...")
            break
    return problems


def write_views(recs: list[dict]) -> None:
    total = len(recs)
    era_counts = Counter(r["inclusion_role"] for r in recs)
    era_groups = [
        {"key": "history", "label": "History & Classics (≤2018)", "n": era_counts["history"], "range": "1962-2018"},
        {"key": "contemporary", "label": "Contemporary Surge (2019-2023)", "n": era_counts["contemporary"], "range": "2019-2023"},
        {"key": "sota", "label": "State of the Art (2024-2026+)", "n": era_counts["sota"], "range": "2024-2026+"},
    ]
    years = sorted(recs, key=lambda r: r["year"])
    era_groups[0]["range"] = f"{years[0]['year']}-2018"
    (VIEWS / "era.json").write_text(
        json.dumps({"view": "era", "total": total, "groups": era_groups}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    year_counts = Counter(int(r["year"]) for r in recs)
    year_groups = [{"key": str(y), "year": y, "n": n} for y, n in sorted(year_counts.items())]
    (VIEWS / "year.json").write_text(
        json.dumps({"view": "year", "total": total, "groups": year_groups}, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dry-run", action="store_true", help="report the join and the changes; write nothing")
    args = ap.parse_args()

    text = DATA.read_text(encoding="utf-8")
    old_recs = yaml.safe_load(text)["papers"]
    _, by_doi, by_title = load_corpus()
    header, records, trailer = split_records(text)
    if len(records) != len(old_recs):
        print(f"line split found {len(records)} records, YAML parse found {len(old_recs)}; refusing", file=sys.stderr)
        return 2

    stats = Counter()
    changes = Counter()
    unmatched = []
    matches = {}
    out_lines = list(header)
    for rec, rec_lines in zip(old_recs, records):
        doi = (rec.get("doi") or "").strip().lower()
        cp = by_doi.get(doi) if doi else None
        if cp is not None:
            stats["matched_by_doi"] += 1
        else:
            cp = by_title.get(norm_title(rec.get("title", "")))
            if cp is not None:
                stats["matched_by_title"] += 1
        if cp is None:
            stats["unmatched"] += 1
            unmatched.append(rec["id"])
            out_lines.extend(rec_lines)
            continue
        matches[rec["id"]] = cp
        if int(cp["year"]) != int(rec["year"]):
            changes["year"] += 1
        if cp["venue"].strip() != rec.get("journal"):
            changes["journal"] += 1
        if cp["authors"].strip() != rec.get("authors"):
            changes["authors"] += 1
        if era_for(int(cp["year"])) != rec.get("inclusion_role"):
            changes["inclusion_role"] += 1
        if "abstract" not in rec:
            changes["abstract_added"] += 1
        out_lines.extend(rewrite_record(rec_lines, rec, cp))
    out_lines.extend(trailer)
    new_text = "\n".join(out_lines)

    new_recs = yaml.safe_load(new_text)["papers"]
    problems = verify(old_recs, new_recs, matches)

    print(f"join: {stats['matched_by_doi']} by DOI, {stats['matched_by_title']} by title, "
          f"{stats['unmatched']} unmatched (left untouched)")
    if unmatched:
        print("  unmatched ids: " + ", ".join(unmatched[:10]) + (" ..." if len(unmatched) > 10 else ""))
    print("changes: " + ", ".join(f"{k}={v}" for k, v in sorted(changes.items())))
    if problems:
        print("round-trip verification FAILED; nothing written:", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        return 1
    print(f"round-trip verification OK: {len(new_recs)} records, only "
          f"{sorted(REWRITTEN)} rewritten and {sorted(ADDED)} added")

    if args.dry_run:
        print("dry run; nothing written")
        return 0
    if new_text == text:
        print("no changes")
        return 0

    fd, tmp = tempfile.mkstemp(prefix="journal_papers.", suffix=".yml", dir=str(DATA.parent))
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(new_text)
    os.chmod(tmp, stat.S_IMODE(DATA.stat().st_mode))  # mkstemp gives 0600
    os.replace(tmp, DATA)
    write_views(new_recs)
    print(f"wrote {DATA.relative_to(ROOT)} ({len(new_text.encode('utf-8'))} bytes) and "
          f"paper_views/era.json, paper_views/year.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
