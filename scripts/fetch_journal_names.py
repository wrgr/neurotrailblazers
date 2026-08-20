#!/usr/bin/env python3
"""Resolve the `journal` field in _data/journal_papers.yml from Crossref.

Every one of the 200 records shipped with `journal: ''`, and
_includes/cards/journal-paper-card.html renders `<em>{{ p.journal }}</em>` — so
every card on a *journal* club page displayed an empty journal. 198 records
carry a real DOI, which makes this recoverable rather than a guessing exercise.

Design constraints, in order of importance:

1. **Never invent a journal.** If Crossref has no container-title, the field
   stays empty and the record is reported. A blank is honest; a plausible
   guess is not.
2. **Never reformat the file.** The YAML holds block scalars and hand-tuned
   structure, and a PyYAML round-trip would rewrite all 3,000-odd lines and
   make a real change invisible in review. Only `journal:` lines are touched,
   in place.
3. **Refuse to write a truncated file.** An indentation bug in the upstream
   generator once nested 199 of the 200 papers inside the first record's
   discussion_prompts, and the site rendered "1 papers" for some time. A floor
   on the record count is asserted before and after.

Keyed by DOI, never by id: nine ids appeared twice in this file before
dedupe_journal_papers.py ran, so an id-keyed lookup assigned one record's
journal from the other record's DOI.

Usage:
    python3 scripts/fetch_journal_names.py --fetch    # query Crossref, cache to disk
    python3 scripts/fetch_journal_names.py --apply    # write cached names into the YAML
    python3 scripts/fetch_journal_names.py            # both
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "journal_papers.yml"
CACHE = ROOT / "scripts" / ".crossref-journals.json"
# A floor, not an exact count: 8 duplicate records were merged out (see
# dedupe_journal_papers.py). The floor still catches the failure that matters --
# a generator bug once collapsed the file to a single record.
MIN_PAPERS = 190

# Crossref asks for a contact address so they can reach you about a misbehaving
# script; it also puts the request in their faster pool.
MAILTO = "willgray@gmail.com"
BATCH = 20
USER_AGENT = f"neurotrailblazers-journal-backfill (mailto:{MAILTO})"

# Crossref returns publisher imprints in inconsistent forms. These are the only
# normalisations applied, and each is a pure display fix rather than a change of
# fact.
CLEANUPS = [
    (re.compile(r"\s+"), " "),
    (re.compile(r"^The\s+(?=Journal|Lancet)"), "The "),
]


def load_records() -> list[dict]:
    """Minimal parse: we only need id/doi pairs, so avoid a YAML dependency."""
    records: list[dict] = []
    current: dict | None = None
    for line in DATA.read_text(encoding="utf-8").splitlines():
        if line.startswith("- id: "):
            if current:
                records.append(current)
            current = {"id": line[len("- id: "):].strip()}
        elif current is not None and line.startswith("  doi: "):
            current["doi"] = line[len("  doi: "):].strip().strip("'\"")
        elif current is not None and line.startswith("  title: "):
            current.setdefault("title", line[len("  title: "):].strip().strip("'\""))
    if current:
        records.append(current)
    return records


def normalise(name: str) -> str:
    for pattern, repl in CLEANUPS:
        name = pattern.sub(repl, name)
    return name.strip()


def crossref_batch(dois: list[str]) -> dict[str, str]:
    """Resolve a batch of DOIs to container titles. Missing DOIs are simply absent."""
    filt = ",".join(f"doi:{d}" for d in dois)
    url = (
        "https://api.crossref.org/works?"
        + urllib.parse.urlencode(
            {"filter": filt, "rows": len(dois),
             "select": "DOI,container-title,publisher,type", "mailto": MAILTO}
        )
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.load(resp)

    out: dict[str, str] = {}
    for item in payload.get("message", {}).get("items", []):
        doi = str(item.get("DOI", "")).lower()
        titles = [t for t in item.get("container-title", []) if t and t.strip()]
        if titles:
            out[doi] = normalise(titles[0])
        elif item.get("type") in {"book", "monograph", "edited-book"} and item.get("publisher"):
            # For a book the publisher is the honest analogue of a journal name.
            out[doi] = normalise(item["publisher"])
    return out


def fetch(records: list[dict]) -> dict[str, str]:
    dois = [r["doi"].lower() for r in records if r.get("doi")]
    resolved: dict[str, str] = {}
    for i in range(0, len(dois), BATCH):
        chunk = dois[i:i + BATCH]
        try:
            resolved.update(crossref_batch(chunk))
        except Exception as exc:  # noqa: BLE001 - report and continue; partial data is fine
            print(f"  batch {i // BATCH + 1}: {exc}", file=sys.stderr)
        print(f"  resolved {len(resolved)}/{len(dois)}", file=sys.stderr)
        time.sleep(0.4)
    CACHE.write_text(json.dumps(resolved, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return resolved


def split_records(text: str) -> tuple[str, list[str]]:
    """Return (header, [record_block, ...]). Records open with a '- id: ' line."""
    lines = text.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if line.startswith("- id: ")]
    if not starts:
        sys.exit("No records found; the file structure is not what this expects.")
    header = "".join(lines[: starts[0]])
    blocks = [
        "".join(lines[start:(starts[n + 1] if n + 1 < len(starts) else len(lines))])
        for n, start in enumerate(starts)
    ]
    return header, blocks


def apply(records: list[dict], resolved: dict[str, str]) -> None:
    """Fill journal names, keyed by DOI.

    Keyed by DOI rather than id on purpose: nine ids appeared twice in this file
    (each a paper entered as both preprint and published version), so an id-keyed
    lookup silently assigned one record's journal from the other's DOI. The
    duplicates are gone now, but DOI remains the field guaranteed unique.
    """
    text = DATA.read_text(encoding="utf-8")
    header, blocks = split_records(text)

    filled = 0
    unresolved: list[str] = []
    out_blocks: list[str] = []
    for block in blocks:
        doi_match = re.search(r"^  doi: (.*)$", block, re.M)
        doi = doi_match.group(1).strip().strip("'\"").lower() if doi_match else ""
        name = resolved.get(doi)
        if name and "  journal: ''" in block:
            escaped = name.replace("'", "''")
            block = block.replace("  journal: ''", f"  journal: '{escaped}'", 1)
            filled += 1
        elif "  journal: ''" in block:
            rid = re.search(r"^- id: (.*)$", block, re.M)
            unresolved.append(f"{rid.group(1).strip() if rid else '?'}  [{doi or 'no DOI'}]")
        out_blocks.append(block)

    new_text = header + "".join(out_blocks)
    count = len(re.findall(r"^- id: ", new_text, re.M))
    if count < MIN_PAPERS:
        sys.exit(
            f"REFUSING TO WRITE: found {count} records, floor is {MIN_PAPERS}. "
            "The file structure changed; fix that before running this."
        )

    DATA.write_text(new_text, encoding="utf-8")
    print(f"Filled {filled} journal names.")

    if unresolved:
        print(f"\n{len(unresolved)} left blank (no container title from Crossref):")
        for line in unresolved:
            print(f"  - {line}")
        print("\nThese need a journal or publisher set by hand, or they stay blank. "
              "Do not guess.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="query Crossref and cache")
    parser.add_argument("--apply", action="store_true", help="write cached names into the YAML")
    args = parser.parse_args()
    do_fetch = args.fetch or not args.apply
    do_apply = args.apply or not args.fetch

    records = load_records()
    if len(records) < MIN_PAPERS:
        sys.exit(f"Parsed only {len(records)} records, floor is {MIN_PAPERS}. Aborting.")
    print(f"Parsed {len(records)} records, {sum(1 for r in records if r.get('doi'))} with DOIs.")

    if do_fetch:
        print("Querying Crossref...")
        resolved = fetch(records)
    else:
        resolved = json.loads(CACHE.read_text(encoding="utf-8"))
    print(f"{len(resolved)} DOIs resolved to a container title.")

    if do_apply:
        apply(records, resolved)


if __name__ == "__main__":
    main()
