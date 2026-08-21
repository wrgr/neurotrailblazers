#!/usr/bin/env python3
"""Remove duplicate records from _data/journal_papers.yml.

Surfaced while backfilling journal names: 9 ids appeared twice, 18 records in
all. DOIs were unique, so nothing had flagged it — but each pair is one paper
entered twice, which meant the journal club advertised 200 papers and showed six
landmark ones (FlyWire, MICrONS-adjacent, Witvliet, Eckstein, Zheng, Bates)
under both their bioRxiv preprint and their published version, with different
years and different summaries.

That is the exact failure the site teaches against: cite the primary source,
state the version. It also breaks lookups, since `where: 'id'` and the card's
`data-id` attribute both assume ids are unique.

Resolution, per pair, decided by checking each DOI against Crossref:

  * 6 preprint/published pairs -> keep the published record, drop the preprint.
  * support-vector-networks    -> two Springer DOIs for the identical 1995
                                  Machine Learning paper. Keep 10.1007/bf00994018.
  * co-planar-stereotaxic-atlas -> the 1989 record is a *book review* of the
                                  atlas in Clinical Neurology and Neurosurgery
                                  that the scrape mistook for the atlas itself.
                                  Keep the 1988 book, drop the review.
  * the-elements-of-statistical-learning -> genuinely two editions (2001, 2009).
                                  Both kept; ids disambiguated by edition.

Edits the file as text so the surviving 192 records stay byte-identical and the
diff shows only what was removed.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "journal_papers.yml"

# DOIs of the records to remove. Keyed by DOI because ids are what is broken.
DROP_DOIS = {
    "10.1101/2020.01.19.911453": "preprint of Cell Rep/Curr Biol 10.1016/j.cub.2020.06.042",
    "10.1101/2020.04.30.066209": "preprint of Nature 10.1038/s41586-021-03778-8",
    "10.1101/2020.08.30.274225": "preprint of Nat Methods 10.1038/s41592-021-01330-0",
    "10.1101/2023.06.27.546656": "preprint of Nature 10.1038/s41586-024-07558-y",
    "10.1101/2020.06.12.148775": "preprint of Cell 10.1016/j.cell.2024.03.016",
    "10.1101/2020.04.17.047167": "preprint of Curr Biol 10.1016/j.cub.2022.06.031",
    "10.1023/a:1022627411411": "duplicate DOI for the same 1995 Machine Learning paper",
    "10.1016/0303-8467(89)90128-5": "book review of the atlas, not the atlas",
}

# id -> new id, for records that are legitimately distinct but collided.
RENAME_BY_DOI = {
    "10.1007/978-0-387-21606-5": "the-elements-of-statistical-learning-1st-edition",
    "10.1007/978-0-387-84858-7": "the-elements-of-statistical-learning-2nd-edition",
}


def split_records(text: str) -> tuple[str, list[str]]:
    """Return (header, [record_block, ...]). Records start at a '- id: ' line."""
    lines = text.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if line.startswith("- id: ")]
    if not starts:
        sys.exit("No records found; file structure is not what this script expects.")
    header = "".join(lines[: starts[0]])
    blocks = []
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        blocks.append("".join(lines[start:end]))
    return header, blocks


def field(block: str, key: str) -> str | None:
    # `id` opens the record as "- id: value"; every other field is indented.
    pattern = r"^- id: (.*)$" if key == "id" else rf"^  {key}: (.*)$"
    m = re.search(pattern, block, re.M)
    return m.group(1).strip().strip("'\"") if m else None


def main() -> None:
    text = DATA.read_text(encoding="utf-8")
    header, blocks = split_records(text)
    print(f"Parsed {len(blocks)} records.")

    kept, dropped = [], []
    for block in blocks:
        doi = (field(block, "doi") or "").lower()
        if doi in DROP_DOIS:
            dropped.append((field(block, "id"), doi, DROP_DOIS[doi]))
            continue
        if doi in RENAME_BY_DOI:
            block = re.sub(r"^- id: .*$", f"- id: {RENAME_BY_DOI[doi]}",
                           block, count=1, flags=re.M)
        kept.append(block)

    missing = set(DROP_DOIS) - {d for _, d, _ in dropped}
    if missing:
        sys.exit(f"Expected to drop these DOIs but did not find them: {sorted(missing)}")

    new_text = header + "".join(kept)
    _, new_blocks = split_records(new_text)

    ids = [field(b, "id") for b in new_blocks]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        sys.exit(f"Duplicate ids remain after dedupe: {sorted(dupes)}")

    DATA.write_text(new_text, encoding="utf-8")

    print(f"\nDropped {len(dropped)}:")
    for rid, doi, why in dropped:
        print(f"  - {rid}\n      {doi} — {why}")
    for doi, new_id in RENAME_BY_DOI.items():
        print(f"  ~ renamed {doi} -> {new_id}")
    print(f"\n{len(new_blocks)} records remain, all ids unique.")


if __name__ == "__main__":
    main()
