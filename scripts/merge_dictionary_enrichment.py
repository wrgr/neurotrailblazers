#!/usr/bin/env python3
"""Merge authored `matters` / `typical` / `confuse` fields into the dictionary.

`technical-training/dictionary/index.md` tells readers that entries carry a
typical value where a term has a characteristic magnitude, a why-it-matters line
where it drives a practical decision, and the confusion where one is routinely
made -- and then says "treat the 'why it matters' line as the real content".

The data did not hold up its end. Of 127 terms, 79 had `matters`, 27 had
`typical`, and 8 had `confuse`, and several definitions ran to five words.

Takes an enrichment module exposing ENRICH = {term: {field: value}} and writes
the fields in, in place. Rules:

  * Never overwrite an existing value. Everything already authored wins.
  * Only known fields, only known terms -- an unmatched term name is an error,
    not a silent no-op, because a typo would otherwise drop authored text.
  * Field order is fixed (definition, typical, matters, confuse, units) so
    entries stay consistent with the ones already in the file.
  * Line-level edit rather than a YAML round-trip, so unchanged entries stay
    byte-identical and the diff shows only what was added.

Usage:
    python3 scripts/merge_dictionary_enrichment.py <enrichment_module.py> [...]
"""

from __future__ import annotations

import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "connectomics_dictionary.yml"
ALLOWED = {"definition", "typical", "matters", "confuse"}
# Where each field goes if it is being added. `units` always stays last.
ORDER = ["term", "category", "definition", "typical", "matters", "confuse", "units"]


def load_enrichment(path: pathlib.Path) -> dict:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.ENRICH


def quote(value: str) -> str:
    """YAML double-quoted scalar. Values contain apostrophes and colons freely."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    enrich: dict[str, dict] = {}
    for arg in sys.argv[1:]:
        for term, fields in load_enrichment(pathlib.Path(arg)).items():
            enrich.setdefault(term, {}).update(fields)

    bad = {f for fields in enrich.values() for f in fields} - ALLOWED
    if bad:
        sys.exit(f"Unknown field(s) in enrichment: {sorted(bad)}")

    text = DATA.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if line.startswith("- term: ")]
    if not starts:
        sys.exit("No '- term:' entries found; file structure is not as expected.")

    header = "".join(lines[: starts[0]])
    blocks = [
        "".join(lines[s:(starts[n + 1] if n + 1 < len(starts) else len(lines))])
        for n, s in enumerate(starts)
    ]

    def term_of(block: str) -> str:
        m = re.match(r'- term: (?:"(.*)"|\'(.*)\'|(.*))\n', block)
        return next(g for g in m.groups() if g is not None).strip()

    present = {term_of(b) for b in blocks}
    unmatched = set(enrich) - present
    if unmatched:
        sys.exit("Enrichment names terms not in the dictionary:\n  "
                 + "\n  ".join(sorted(unmatched)))

    added = {f: 0 for f in ALLOWED}
    replaced = 0
    out: list[str] = []

    for block in blocks:
        term = term_of(block)
        fields = enrich.get(term)
        if not fields:
            out.append(block)
            continue

        entry_lines = block.splitlines(keepends=True)

        # Split the entry into whole field spans. A field opens with a
        # two-space "name:" line; everything after it, including deeper-indented
        # continuation lines and list items, belongs to that field. Indexing by
        # opening line alone is not enough -- inserting after a wrapped
        # definition's first line lands the new field inside the old value and
        # breaks the YAML.
        opens = [
            i for i, line in enumerate(entry_lines)
            if re.match(r"  [a-z_]+:", line)
        ]
        spans: dict[str, str] = {"term": entry_lines[0]}
        for n, i in enumerate(opens):
            name = re.match(r"  ([a-z_]+):", entry_lines[i]).group(1)
            stop = opens[n + 1] if n + 1 < len(opens) else len(entry_lines)
            spans[name] = "".join(entry_lines[i:stop])

        for field, value in fields.items():
            if field in spans:
                if field != "definition":
                    continue  # never overwrite an authored value
                # Replace a definition only when the new one is substantially
                # longer; the five-word ones are the reason for replacing any.
                if len(value.split()) <= len(spans[field].split()) + 2:
                    continue
                spans[field] = f"  {field}: {quote(value)}\n"
                replaced += 1
            else:
                spans[field] = f"  {field}: {quote(value)}\n"
                added[field] += 1

        # Re-emit in canonical order, then anything unrecognised, so entries
        # stay consistent with the ones already in the file.
        ordered = [spans[f] for f in ORDER if f in spans]
        ordered += [v for k, v in spans.items() if k not in ORDER]
        out.append("".join(ordered))

    new_text = header + "".join(out)
    count = len(re.findall(r"^- term: ", new_text, re.M))
    if count != len(blocks):
        sys.exit(f"REFUSING TO WRITE: entry count changed {len(blocks)} -> {count}.")

    DATA.write_text(new_text, encoding="utf-8")
    print(f"{count} entries. Added: "
          + ", ".join(f"{n} {f}" for f, n in sorted(added.items()) if n)
          + f". Replaced {replaced} thin definition(s).")


if __name__ == "__main__":
    main()
