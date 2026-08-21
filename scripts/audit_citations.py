#!/usr/bin/env python3
"""Check every resolvable citation in the content library against Crossref/arXiv.

Prompted by two findings in content-library/proofreading/error-taxonomy.md:

  * "Lee, K., Lu, R., Luther, K., & Bhatt, M. (2019). Superhuman accuracy on the
    SNEMI3D connectomics benchmark. arXiv:1706.00120" -- the arXiv ID is real,
    but it is Lee, Zung, Li, Jain & Seung (2017). Wrong authors, wrong year.
  * content-library/imaging/tissue-preparation.md cites "(Bhatt & Bhatt,
    various)" for an osmium penetration rate -- no year, no title, no DOI.

"Bhatt" appearing in both, attached to different claims, is the signature of a
fabricated citation rather than a typo. This checks the ones that can be
checked: every DOI and arXiv identifier in the library is resolved and its real
authors and year compared against the surrounding text.

It cannot check a citation with no identifier. Those are listed separately, so a
human knows what still needs eyes.

A diagnostic, not a CI gate. It needs network access, and the surname regex
produces predictable false positives that a human reads past in seconds but a
gate cannot: consortium authorships ("MICrONS et al."), surnames containing a
space ("Van Essen"), and capitalised words in a citation line that are not names
at all. Run it after touching references; do not wire it into the build.

Usage:
    python3 scripts/audit_citations.py [path ...]     # defaults to content-library
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / "scripts" / ".citation-audit-cache.json"
MAILTO = "willgray@gmail.com"
UA = f"neurotrailblazers-citation-audit (mailto:{MAILTO})"

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\)\]\}\"'<>,;]+")
ARXIV_RE = re.compile(r"arXiv[:\s]*(\d{4}\.\d{4,5})", re.I)
# "Berger, D. R., Seung, H. S., & Lichtman, J. W. (2018)." -> surname + year
CITE_RE = re.compile(r"([A-Z][A-Za-zÀ-ſ'-]+)[^()\n]{0,120}?\((\d{4})[a-z]?\)")


def fetch(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.read().decode("utf-8", "replace")
    except Exception:  # noqa: BLE001
        return None


def crossref(doi: str) -> dict | None:
    body = fetch(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}?mailto={MAILTO}")
    if not body:
        return None
    try:
        m = json.loads(body)["message"]
    except Exception:  # noqa: BLE001
        return None
    return {
        "title": (m.get("title") or [""])[0],
        "year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
        "authors": [a.get("family", "") for a in m.get("author", []) if a.get("family")],
        "container": (m.get("container-title") or [""])[0],
    }


def arxiv(ident: str) -> dict | None:
    body = fetch(f"http://export.arxiv.org/api/query?id_list={ident}")
    if not body:
        return None
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return None
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entry = root.find("a:entry", ns)
    if entry is None:
        return None
    published = (entry.findtext("a:published", "", ns) or "")[:4]
    names = [
        (a.findtext("a:name", "", ns) or "").split()[-1]
        for a in entry.findall("a:author", ns)
    ]
    return {
        "title": " ".join((entry.findtext("a:title", "", ns) or "").split()),
        "year": int(published) if published.isdigit() else None,
        "authors": names,
        "container": f"arXiv:{ident}",
    }


def main() -> None:
    targets = [pathlib.Path(a) for a in sys.argv[1:]] or [ROOT / "content-library"]
    files = sorted(
        f for t in targets
        for f in ([t] if t.is_file() else t.rglob("*.md"))
    )

    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    mismatches: list[str] = []
    unresolvable: list[str] = []
    unidentified: dict[str, set[str]] = {}
    checked = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        lines = text.splitlines()

        for i, line in enumerate(lines, 1):
            ids: list[tuple[str, str]] = []
            ids += [("doi", d.rstrip(".")) for d in DOI_RE.findall(line)]
            ids += [("arxiv", a) for a in ARXIV_RE.findall(line)]
            if not ids:
                continue

            # Citations are often split across wrapped lines; take a window.
            window = " ".join(lines[max(0, i - 4):i + 2])

            for kind, ident in ids:
                key = f"{kind}:{ident.lower()}"
                if key not in cache:
                    cache[key] = (crossref(ident) if kind == "doi" else arxiv(ident)) or {}
                    time.sleep(0.3)
                meta = cache[key]
                checked += 1

                if not meta:
                    unresolvable.append(f"{rel}:{i}  {kind} {ident} does not resolve")
                    continue

                surnames = {a.lower() for a in meta.get("authors", [])}
                cited = {m.group(1).lower() for m in CITE_RE.finditer(window)}
                years_cited = {int(m.group(2)) for m in CITE_RE.finditer(window)}
                if not cited:
                    continue

                # Flag only when no cited surname appears in the real author list.
                # A citation naming a first author who is not on the paper is the
                # failure worth reporting; ordering and et al. are not.
                if surnames and not (cited & surnames):
                    mismatches.append(
                        f"{rel}:{i}\n"
                        f"    cited as: {', '.join(sorted(cited))} ({', '.join(str(y) for y in sorted(years_cited))})\n"
                        f"    actually: {', '.join(meta['authors'][:4])} ({meta.get('year')})\n"
                        f"    {meta.get('title', '')[:90]}\n"
                        f"    {kind}:{ident}"
                    )
                # A journal's online-first year and its issue year routinely
                # differ by one, and Crossref reports the earlier. Only a gap
                # bigger than that is worth a human's attention.
                elif (meta.get("year") and years_cited
                      and min(abs(meta["year"] - y) for y in years_cited) > 1):
                    mismatches.append(
                        f"{rel}:{i}  year: cited {sorted(years_cited)}, "
                        f"actually {meta['year']} — {kind}:{ident}"
                    )

        # Author-year citations carrying no identifier at all.
        for m in CITE_RE.finditer(text):
            span = text[max(0, m.start() - 200):m.end() + 200]
            if not DOI_RE.search(span) and not ARXIV_RE.search(span):
                unidentified.setdefault(str(rel), set()).add(f"{m.group(1)} {m.group(2)}")

    CACHE.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"Checked {checked} identifiers across {len(files)} files.\n")

    if mismatches:
        print(f"== {len(mismatches)} citation(s) whose metadata does not match ==\n")
        for m in mismatches:
            print(f"  {m}\n")

    if unresolvable:
        print(f"== {len(unresolvable)} identifier(s) that do not resolve ==")
        for u in unresolvable:
            print(f"  {u}")
        print()

    total_unid = sum(len(v) for v in unidentified.values())
    print(f"== {total_unid} author-year citation(s) with no DOI or arXiv id ==")
    print("   Not necessarily wrong, but not checkable here. Densest files:\n")
    for rel, names in sorted(unidentified.items(), key=lambda kv: -len(kv[1]))[:12]:
        print(f"  {len(names):3}  {rel}")

    sys.exit(1 if mismatches or unresolvable else 0)


if __name__ == "__main__":
    main()
