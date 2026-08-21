#!/usr/bin/env python3
"""Second pass over _data/journal_papers.yml: handle the preprint citations.

`fetch_journal_names.py` resolved 172 of 200 journal names from Crossref and
left 25 blank. 23 of those are `10.1101/...` bioRxiv DOIs, which have no
container title because a preprint is not in a journal.

That is worth more than a cosmetic fix. The site teaches, repeatedly, that you
cite the primary source and state the version — and its own reading list points
at preprints for landmark papers that have since appeared in Nature, Science and
eLife. Crossref records the link in a `is-preprint-of` relation, so the published
version can be recovered rather than guessed.

This pass:

  * follows `is-preprint-of` and reports the published DOI, journal and year;
  * flags any preprint whose published DOI is *already* a separate record, since
    those are duplicate entries for one paper and need merging by hand rather
    than rewriting;
  * writes `journal: 'bioRxiv (preprint)'` for preprints with no published
    version, which is what they actually are.

It only writes journal names. DOI rewrites and merges are reported, never
applied — changing which paper a record points at is an editorial decision.

Usage:
    python3 scripts/resolve_preprints.py --report     # look, change nothing
    python3 scripts/resolve_preprints.py --apply      # also write journal names
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
CACHE = ROOT / "scripts" / ".crossref-preprints.json"
MIN_PAPERS = 190  # a floor; 8 duplicate records were merged out. See dedupe_journal_papers.py.
MAILTO = "willgray@gmail.com"
USER_AGENT = f"neurotrailblazers-preprint-resolve (mailto:{MAILTO})"

PREPRINT_LABELS = {
    "10.1101": "bioRxiv (preprint)",
    "10.48550": "arXiv (preprint)",
    "10.21203": "Research Square (preprint)",
}


def crossref(doi: str) -> dict | None:
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}?mailto={MAILTO}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.load(resp).get("message")
    except Exception as exc:  # noqa: BLE001
        print(f"  ! {doi}: {exc}", file=sys.stderr)
        return None


def load_records() -> list[dict]:
    records: list[dict] = []
    current: dict | None = None
    for line in DATA.read_text(encoding="utf-8").splitlines():
        if line.startswith("- id: "):
            if current:
                records.append(current)
            current = {"id": line[len("- id: "):].strip()}
        elif current is not None:
            for key in ("doi", "title", "year", "journal"):
                prefix = f"  {key}: "
                if line.startswith(prefix):
                    current.setdefault(key, line[len(prefix):].strip().strip("'\""))
    if current:
        records.append(current)
    return records


def preprint_label(doi: str) -> str | None:
    return PREPRINT_LABELS.get(doi.split("/", 1)[0])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write journal names")
    parser.add_argument("--report", action="store_true", help="report only (default)")
    args = parser.parse_args()

    records = load_records()
    if len(records) < MIN_PAPERS:
        sys.exit(f"Parsed only {len(records)} records, floor is {MIN_PAPERS}. Aborting.")

    all_dois = {(r.get("doi") or "").lower(): r["id"] for r in records if r.get("doi")}
    blank = [r for r in records if not r.get("journal") and r.get("doi")]
    print(f"{len(blank)} records with a DOI and no journal.\n")

    if CACHE.exists():
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
    else:
        cache = {}

    published: dict[str, dict] = {}   # record id -> published info
    standalone: list[dict] = []       # preprints with no published version
    duplicates: list[tuple[dict, str]] = []

    for rec in blank:
        doi = rec["doi"].lower()
        if doi in cache:
            info = cache[doi]
        else:
            msg = crossref(doi)
            info = {}
            if msg:
                rel = msg.get("relation", {}).get("is-preprint-of", [])
                target = next((x.get("id") for x in rel if x.get("id-type") == "doi"), None)
                if target:
                    pub = crossref(target)
                    if pub:
                        titles = [t for t in pub.get("container-title", []) if t.strip()]
                        info = {
                            "published_doi": target.lower(),
                            "journal": titles[0].strip() if titles else "",
                            "year": (pub.get("issued", {}).get("date-parts") or [[None]])[0][0],
                        }
            cache[doi] = info
            time.sleep(0.3)

        if info.get("journal"):
            if info["published_doi"] in all_dois:
                duplicates.append((rec, info["published_doi"]))
            else:
                published[rec["id"]] = info
        else:
            standalone.append(rec)

    CACHE.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if published:
        print(f"== {len(published)} preprints now published elsewhere ==")
        print("   Journal is filled in below. The DOI still points at the preprint;")
        print("   updating it is an editorial call, so it is reported, not applied.\n")
        for rid, info in published.items():
            print(f"  {rid}\n      -> {info['journal']} ({info['year']})  {info['published_doi']}")
        print()

    if duplicates:
        print(f"== {len(duplicates)} preprints whose published version is ALREADY a record ==")
        print("   These are two entries for one paper. Merge by hand.\n")
        for rec, pub_doi in duplicates:
            print(f"  {rec['id']}\n      duplicates -> {all_dois[pub_doi]}  ({pub_doi})")
        print()

    if standalone:
        print(f"== {len(standalone)} still preprints, with no published version found ==")
        for rec in standalone:
            print(f"  {rec['id']}  [{rec['doi']}]")
        print()

    if not args.apply:
        print("Report only. Re-run with --apply to write journal names.")
        return

    # ---- write journal names -------------------------------------------------
    fills: dict[str, str] = {}
    for rid, info in published.items():
        fills[rid] = info["journal"]
    for rec, pub_doi in duplicates:
        # Still a preprint record until someone merges it; label it honestly.
        label = preprint_label(rec["doi"])
        if label:
            fills[rec["id"]] = label
    for rec in standalone:
        label = preprint_label(rec["doi"])
        if label:
            fills[rec["id"]] = label

    text = DATA.read_text(encoding="utf-8")
    out: list[str] = []
    current_id: str | None = None
    written = 0
    for line in text.splitlines(keepends=True):
        if line.startswith("- id: "):
            current_id = line[len("- id: "):].strip()
        if line.rstrip("\n") == "  journal: ''" and current_id in fills:
            out.append(f"  journal: '{fills[current_id].replace(chr(39), chr(39) * 2)}'\n")
            written += 1
            continue
        out.append(line)

    new_text = "".join(out)
    count = len(re.findall(r"^- id: ", new_text, re.M))
    if count < MIN_PAPERS:
        sys.exit(f"REFUSING TO WRITE: {count} records, floor is {MIN_PAPERS}.")

    DATA.write_text(new_text, encoding="utf-8")
    print(f"Wrote {written} journal names.")


if __name__ == "__main__":
    main()
