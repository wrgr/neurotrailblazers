#!/usr/bin/env python3
"""Execute the retrieval half of docs/planning/SEED_CORPUS_RESET_BRIEF.md.

The brief's first constraint is "retrieve, never recall". A script enforces that
structurally rather than by instruction: every record here is whatever an API
returned, and there is no path by which a DOI could be invented. That is the
whole reason this stage is code and not a model.

What this does (brief steps 1, 2, and the bibliometric statistics):

  Stage A  institutional seed  - NIH RePORTER awards -> PI names
  Stage B  literature seed     - Crossref bibliographic sweep over the brief's
                                 vocabulary, run twice: by citation and by date,
                                 kept separate so they can serve as the two
                                 independent strategies for capture-recapture
  Stage C  citation expansion  - outbound references, which also resolves and
                                 therefore verifies every DOI in the pool
  Stage D  graph analysis      - PageRank over the citation graph, betweenness
                                 over co-authorship. Pure Python, no numpy.
  Stage E  statistics          - capture-recapture, concentration, year and
                                 language distribution

DEVIATION FROM THE BRIEF, recorded here and in the method report. The brief
specifies OpenAlex and forward citations. OpenAlex hard rate-limits this
container's shared IP - retries kept it in penalty rather than recovering - so
the primary source is Crossref, which sustained 10 records at 0.2s pacing with
no failures. Crossref has no forward-citation query, so expansion runs backwards
along reference lists instead. Three consequences worth knowing: references
arrive free on the record, so the graph costs no extra calls; resolving each
record verifies its DOI as a side effect, satisfying the brief's third
constraint; and backward expansion biases toward older, foundational work, which
the date-sorted pass in Stage B exists to counterbalance. Open-access status is
not available from Crossref and is recorded as not retrieved rather than guessed.

What it does NOT do, deliberately: decide which papers belong, assign areas or
tiers, or write summaries. Those are judgement, and judgement is the clean run's
job. This produces the candidate pool it judges.

Everything is cached to disk by URL, so a re-run is cheap and an interrupted run
resumes. Checkpoints are written after every stage.

Usage:
    python3 scripts/seed_retrieval.py                 # full run
    python3 scripts/seed_retrieval.py --stage b       # one stage
    python3 scripts/seed_retrieval.py --max-expand 400
"""

from __future__ import annotations

import argparse
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict, deque

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "seed_retrieval"
CACHE = OUT / "cache"
MAILTO = "willgray@gmail.com"
UA = f"neurotrailblazers-seed-retrieval (mailto:{MAILTO})"

# From the brief's BACKGROUND search vocabulary. Precise phrases only -- the
# bare word "connectomics" matches 4,622 works and would drown the sweep.
TERMS = [
    "volume electron microscopy connectomics", "serial section electron microscopy brain",
    "serial block-face scanning electron microscopy", "FIB-SEM connectomics",
    "automated tape-collecting ultramicrotome", "GridTape transmission electron microscopy",
    "multibeam scanning electron microscopy brain", "en bloc staining electron microscopy brain",
    "neural circuit reconstruction electron microscopy", "dense reconstruction neuropil",
    "saturated reconstruction neocortex", "neuron segmentation electron microscopy",
    "flood-filling network segmentation", "affinity prediction neuron segmentation",
    "supervoxel agglomeration connectomics", "proofreading connectome reconstruction",
    "split and merge errors segmentation", "synapse detection electron microscopy",
    "synaptic partner assignment", "skeletonization neuron morphology",
    "electron microscopy image alignment stitching", "connectome annotation versioning",
    "expansion microscopy connectomics", "X-ray holographic nano-tomography brain",
    "connectome motif analysis", "connectome null model", "connectome-constrained model",
    "whole brain connectome Drosophila", "C. elegans connectome",
    "petascale neuroscience data management", "cloud storage neuroimaging chunked",
]

REPORTER_QUERIES = [
    "connectomics electron microscopy", "BRAIN CONNECTS", "connectome reconstruction",
    "volume electron microscopy brain mapping",
]


# --------------------------------------------------------------------------
# HTTP with a disk cache and real backoff. Crossref sustained 10 records at
# 0.2s pacing with no failures, so 0.35s carries margin; retries stay in
# because a shared-IP container gets throttled without warning.
# --------------------------------------------------------------------------
def _cache_path(key: str) -> pathlib.Path:
    import hashlib
    return CACHE / f"{hashlib.sha256(key.encode()).hexdigest()[:24]}.json"


def get(url: str, *, tries: int = 6) -> dict | None:
    cp = _cache_path(url)
    if cp.exists():
        return json.loads(cp.read_text(encoding="utf-8"))
    delay = 2.0
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.load(resp)
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_text(json.dumps(data), encoding="utf-8")
            time.sleep(0.35)         # Crossref sustained 0.2s cleanly; 0.35 is margin
            return data
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < tries - 1:
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            print(f"    ! {exc.code} {url[:110]}")
            return None
        except Exception as exc:  # noqa: BLE001
            if attempt < tries - 1:
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            print(f"    ! {exc} {url[:110]}")
            return None
    return None


def post_json(url: str, payload: dict, *, tries: int = 5) -> dict | None:
    cp = _cache_path(url + json.dumps(payload, sort_keys=True))
    if cp.exists():
        return json.loads(cp.read_text(encoding="utf-8"))
    delay = 2.0
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                url, data=json.dumps(payload).encode(),
                headers={"User-Agent": UA, "Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.load(resp)
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_text(json.dumps(data), encoding="utf-8")
            time.sleep(1.1)
            return data
        except Exception as exc:  # noqa: BLE001
            if attempt < tries - 1:
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            print(f"    ! {exc}")
            return None
    return None


CR = "https://api.crossref.org/works"


def cr_search(term: str, *, rows: int, sort: str | None = None,
              order: str = "desc", filt: str | None = None) -> list[dict]:
    """Crossref bibliographic search. Note that `total-results` on a
    query.bibliographic call is a fuzzy relevance match, not a boolean count -
    it runs to millions and means nothing. The ranking is what is useful, so we
    take the top `rows` and never quote the total."""
    params = {"query.bibliographic": term, "rows": str(rows), "mailto": MAILTO}
    if sort:
        params["sort"] = sort
        params["order"] = order
    if filt:
        params["filter"] = filt
    data = get(f"{CR}?{urllib.parse.urlencode(params)}")
    return (data or {}).get("message", {}).get("items", [])


def cr_work(doi: str) -> dict | None:
    data = get(f"{CR}/{urllib.parse.quote(doi)}?mailto={MAILTO}")
    return (data or {}).get("message")


def wid(work: dict) -> str:
    """DOI is the identity key. Crossref DOIs are unique and always present on
    a Crossref record, which is why the pool is keyed on them."""
    return (work.get("DOI") or "").lower()


def slim(work: dict) -> dict:
    """Transcribe the fields the brief's schema needs. Nothing is derived."""
    auths = []
    n = len(work.get("author", []) or [])
    for i, a in enumerate(work.get("author", []) or []):
        name = " ".join(x for x in (a.get("family"), a.get("given")) if x) or a.get("name")
        auths.append({
            "name": name,
            "orcid": (a.get("ORCID") or "").replace("http://orcid.org/", "")
                     .replace("https://orcid.org/", "") or None,
            "position": "first" if i == 0 else ("last" if i == n - 1 else "middle"),
            "is_corresponding": bool(a.get("sequence") == "first") if a.get("sequence") else None,
            "institutions": [x.get("name") for x in (a.get("affiliation") or []) if x.get("name")],
            "is_consortium": bool(a.get("name") and not a.get("family")),
        })
    issued = (work.get("issued", {}).get("date-parts") or [[None]])[0]
    refs = [r["DOI"].lower() for r in (work.get("reference") or []) if r.get("DOI")]
    return {
        "doi": (work.get("DOI") or "").lower() or None,
        "title": " ".join((work.get("title") or [""])[0].split()) or None,
        "authors": auths,
        "author_count": len(auths),
        "has_consortium_author": any(a["is_consortium"] for a in auths),
        "year": issued[0],
        "journal": (work.get("container-title") or [""])[0] or None,
        "publisher": work.get("publisher"),
        "url": work.get("URL"),
        "work_type": work.get("type"),
        "language": work.get("language"),
        "is_referenced_by_count": work.get("is-referenced-by-count"),
        "references_with_doi": len(refs),
        "referenced_works": refs,
        "subject": (work.get("subject") or [])[:5],
        "open_access": None,   # Crossref does not carry OA status; not retrieved
        "retrieved": time.strftime("%Y-%m-%d"),
    }


# --------------------------------------------------------------------------
def stage_a() -> dict:
    """Institutional seed: NIH RePORTER awards -> PI names and organisations."""
    print("Stage A - NIH RePORTER awards")
    pis: dict[str, dict] = {}
    awards = []
    for q in REPORTER_QUERIES:
        payload = {
            "criteria": {"advanced_text_search": {
                "operator": "and", "search_field": "projecttitle,abstracttext",
                "search_text": q}},
            "include_fields": ["ProjectTitle", "ContactPiName", "Organization",
                               "ProjectNum", "FiscalYear", "AwardAmount"],
            "offset": 0, "limit": 250,
        }
        data = post_json("https://api.reporter.nih.gov/v2/projects/search", payload)
        if not data:
            continue
        results = data.get("results", [])
        print(f"    '{q}' -> {len(results)} awards (total {data.get('meta', {}).get('total')})")
        for r in results:
            awards.append({
                "query": q,
                "project_num": r.get("project_num"),
                "title": r.get("project_title"),
                "pi": r.get("contact_pi_name"),
                "org": (r.get("organization") or {}).get("org_name"),
                "fiscal_year": r.get("fiscal_year"),
            })
            name = r.get("contact_pi_name")
            if name:
                pis.setdefault(name, {"name": name,
                                      "org": (r.get("organization") or {}).get("org_name"),
                                      "awards": [], "found_via": "nih reporter"})
                pis[name]["awards"].append(r.get("project_num"))
    print(f"    {len(awards)} awards, {len(pis)} distinct PIs")
    return {"awards": awards, "pis": list(pis.values())}


def stage_b(rows_per_term: int) -> dict:
    """Literature seed, run as two deliberately separate strategies so their
    overlap can serve as a capture-recapture estimate later."""
    print("Stage B - Crossref vocabulary sweep")
    by_citation: dict[str, dict] = {}
    by_date: dict[str, dict] = {}
    per_term = {}
    for term in TERMS:
        cited = cr_search(term, rows=rows_per_term,
                          sort="is-referenced-by-count", order="desc")
        recent = cr_search(term, rows=rows_per_term, sort="published", order="desc",
                           filt="from-pub-date:2021-01-01")
        for w in cited:
            k = wid(w)
            if k:
                by_citation.setdefault(k, {**slim(w),
                                           "found_via": f"search '{term}' by citation"})
        for w in recent:
            k = wid(w)
            if k:
                by_date.setdefault(k, {**slim(w), "found_via": f"search '{term}' by date"})
        per_term[term] = {"by_citation": len(cited), "by_date": len(recent)}
        print(f"    {len(cited):3} cited / {len(recent):3} recent  {term[:52]}")
    print(f"    pool: {len(by_citation)} by citation, {len(by_date)} by date, "
          f"{len(set(by_citation) & set(by_date))} in both")
    return {"by_citation": by_citation, "by_date": by_date, "per_term": per_term}


def stage_c(pool: dict[str, dict], max_expand: int) -> dict:
    """Expand along reference lists. Every fetch resolves a DOI, so this is also
    the verification pass. The cap is reported, never silent."""
    print(f"Stage C - reference expansion (cap {max_expand} seeds)")
    ranked = sorted(pool.values(), key=lambda w: -(w.get("is_referenced_by_count") or 0))
    seeds = ranked[:max_expand]
    cited_counts: Counter = Counter()
    for n, w in enumerate(seeds, 1):
        if not w.get("doi"):
            continue
        full = cr_work(w["doi"])
        if not full:
            w["doi_resolved"] = False
            continue
        w["doi_resolved"] = True
        refs = [r["DOI"].lower() for r in (full.get("reference") or []) if r.get("DOI")]
        w["referenced_works"] = refs
        w["references_with_doi"] = len(refs)
        cited_counts.update(refs)
        if n % 50 == 0:
            print(f"    {n}/{len(seeds)} resolved, {len(cited_counts)} distinct refs seen")

    # A reference cited by several pool members is a strong candidate, and this
    # is where foundational work with no recent citations surfaces.
    frequent = [d for d, c in cited_counts.items() if c >= 3 and d not in pool]
    print(f"    {len(cited_counts)} distinct references; {len(frequent)} cited by 3+ pool papers")
    found: dict[str, dict] = {}
    for n, d in enumerate(frequent[:max_expand], 1):
        full = cr_work(d)
        if not full:
            continue
        found[d] = {**slim(full), "doi_resolved": True,
                    "found_via": f"reference cited by {cited_counts[d]} pool papers"}
        if n % 50 == 0:
            print(f"    pulled {n}/{min(len(frequent), max_expand)} frequent references")
    print(f"    {len(found)} new works added from references")
    return {"added": found, "seeds_expanded": len(seeds), "seeds_available": len(ranked),
            "capped": len(ranked) > max_expand,
            "frequent_refs_found": len(frequent),
            "frequent_refs_pulled": len(found),
            "frequent_refs_capped": len(frequent) > max_expand}


# --------------------------------------------------------------------------
def pagerank(graph: dict[str, set], damping: float = 0.85, iters: int = 40) -> dict[str, float]:
    nodes = set(graph) | {v for s in graph.values() for v in s}
    if not nodes:
        return {}
    n = len(nodes)
    pr = dict.fromkeys(nodes, 1.0 / n)
    outdeg = {x: len(graph.get(x, ())) for x in nodes}
    for _ in range(iters):
        nxt = dict.fromkeys(nodes, (1.0 - damping) / n)
        dangling = sum(pr[x] for x in nodes if outdeg[x] == 0) * damping / n
        for x in nodes:
            if outdeg[x]:
                share = damping * pr[x] / outdeg[x]
                for y in graph[x]:
                    nxt[y] += share
        pr = {k: v + dangling for k, v in nxt.items()}
    return pr


def betweenness(adj: dict[str, set], sample: list[str] | None = None) -> dict[str, float]:
    """Brandes' algorithm, unweighted. `sample` limits the sources for speed;
    the result is then an estimate and is labelled as one."""
    nodes = list(adj)
    sources = sample if sample is not None else nodes
    bc = dict.fromkeys(nodes, 0.0)
    for s in sources:
        stack, preds = [], {v: [] for v in nodes}
        sigma = dict.fromkeys(nodes, 0.0); sigma[s] = 1.0
        dist = dict.fromkeys(nodes, -1); dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft(); stack.append(v)
            for w in adj.get(v, ()):
                if dist.get(w, -1) < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist.get(w, -1) == dist[v] + 1:
                    sigma[w] += sigma[v]
                    preds[w].append(v)
        delta = dict.fromkeys(nodes, 0.0)
        while stack:
            w = stack.pop()
            for v in preds[w]:
                if sigma[w]:
                    delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != s:
                bc[w] += delta[w]
    return bc


def stage_d(pool: dict[str, dict]) -> dict:
    print("Stage D - graph analysis")
    ids = set(pool)
    cite_graph = {i: {r for r in pool[i].get("referenced_works", []) if r in ids} for i in ids}
    edges = sum(len(v) for v in cite_graph.values())
    print(f"    citation graph: {len(ids)} nodes, {edges} internal edges")
    pr = pagerank(cite_graph)

    coauth: dict[str, set] = defaultdict(set)
    for w in pool.values():
        names = [(a.get("orcid") or a.get("name")) for a in w["authors"] if a.get("name")]
        if len(names) > 60:      # consortium papers would make everyone adjacent
            continue
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                coauth[a].add(b); coauth[b].add(a)
    print(f"    co-authorship graph: {len(coauth)} authors")
    sample = sorted(coauth, key=lambda a: -len(coauth[a]))[:300]
    bc = betweenness(dict(coauth), sample=sample)
    return {
        "citation_edges": edges,
        "pagerank": dict(sorted(pr.items(), key=lambda kv: -kv[1])[:400]),
        "coauthor_nodes": len(coauth),
        "betweenness_estimated_from": len(sample),
        "betweenness": dict(sorted(bc.items(), key=lambda kv: -kv[1])[:200]),
    }


def stage_e(by_citation: dict, by_date: dict, pool: dict) -> dict:
    print("Stage E - bibliometric statistics")
    a, b = set(by_citation), set(by_date)
    both = a & b
    est = (len(a) * len(b) / len(both)) if both else None
    insts, journals, countries, years, langs = Counter(), Counter(), Counter(), Counter(), Counter()
    retracted = 0; no_doi = 0
    for w in pool.values():
        if w.get("journal"):
            journals[w["journal"]] += 1
        years[w.get("year")] += 1
        langs[w.get("language")] += 1
        pass  # open-access status is not available from Crossref
        no_doi += 0 if w.get("doi") else 1
        seen_i, seen_c = set(), set()
        for au in w["authors"]:
            for i in au.get("institutions") or []:
                seen_i.add(i)
            for c in au.get("countries") or []:
                seen_c.add(c)
        for i in seen_i:
            insts[i] += 1
        for c in seen_c:
            countries[c] += 1
    total = len(pool) or 1
    return {
        "capture_recapture": {
            "found_by_citation_strategy": len(a), "found_by_date_strategy": len(b),
            "found_by_both": len(both),
            "estimated_total": round(est) if est else None,
            "caveat": "Lincoln-Petersen. Assumes the two strategies are independent "
                      "and equally likely to find any paper; neither fully holds for "
                      "literature search. Indicative only.",
        },
        "pool_size": len(pool),
        "records_without_doi": no_doi,
        "top_institutions": insts.most_common(12),
        "top_three_institution_share": round(sum(c for _, c in insts.most_common(3)) / total, 3),
        "top_journals": journals.most_common(12),
        "top_three_journal_share": round(sum(c for _, c in journals.most_common(3)) / total, 3),
        "countries": countries.most_common(15),
        "years": dict(sorted((k, v) for k, v in years.items() if k)),
        "languages": langs.most_common(6),
        "open_access": "not retrieved - Crossref does not carry OA status; "
                       "resolve separately via Unpaywall if needed",
        "consortium_authored": sum(1 for w in pool.values() if w.get("has_consortium_author")),
        "author_count_distribution": {
            "1-5": sum(1 for w in pool.values() if (w.get("author_count") or 0) <= 5),
            "6-20": sum(1 for w in pool.values() if 5 < (w.get("author_count") or 0) <= 20),
            "21-100": sum(1 for w in pool.values() if 20 < (w.get("author_count") or 0) <= 100),
            "100+": sum(1 for w in pool.values() if (w.get("author_count") or 0) > 100),
        },
    }


HELD_OUT = {
    "10.1038/s41586-025-08985-1": "light-microscopy connectomic reconstruction, 2025",
    "10.1038/s41586-024-07558-y": "whole adult fly brain wiring diagram, 2024",
    "10.1038/s41586-025-08790-w": "functional connectomics, mouse visual cortex, 2025",
    "10.1126/science.adk4858": "petavoxel human cortex fragment, 2024",
    "10.7554/elife.57443": "adult Drosophila central brain connectome, 2020",
    "10.1016/j.cell.2015.06.054": "saturated reconstruction of neocortex, 2015",
    "10.1126/science.add9330": "insect brain connectome, 2023",
}


def self_test(pool: dict) -> dict:
    have = {(w.get("doi") or "").lower() for w in pool.values()}
    found = {d: (d in have) for d in HELD_OUT}
    return {"found": sum(found.values()), "of": len(HELD_OUT),
            "detail": {d: {"found": v, "what": HELD_OUT[d]} for d, v in found.items()}}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rows-per-term", type=int, default=40)
    ap.add_argument("--max-expand", type=int, default=250)
    ap.add_argument("--stage", default="all")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    started = time.strftime("%Y-%m-%d %H:%M:%S")

    a = stage_a()
    (OUT / "stage_a_awards.json").write_text(json.dumps(a, indent=2), encoding="utf-8")

    b = stage_b(args.rows_per_term)
    pool = {**b["by_date"], **b["by_citation"]}
    (OUT / "stage_b_index.json").write_text(json.dumps(b["per_term"], indent=2), encoding="utf-8")

    c = stage_c(pool, args.max_expand)
    for k, v in c["added"].items():
        pool.setdefault(k, v)
    print(f"    pool after expansion: {len(pool)}")

    d = stage_d(pool)
    e = stage_e(b["by_citation"], b["by_date"], pool)
    st = self_test(pool)
    print(f"Self-test: {st['found']}/{st['of']} held-out papers found independently")

    for w in pool.values():
        w["pagerank"] = round(d["pagerank"].get(w["doi"], 0.0), 8)

    (OUT / "candidate_pool.json").write_text(
        json.dumps(sorted(pool.values(), key=lambda w: -(w.get("pagerank") or 0)), indent=2),
        encoding="utf-8")
    (OUT / "method_report.json").write_text(json.dumps({
        "generated": started, "finished": time.strftime("%Y-%m-%d %H:%M:%S"),
        "sources_used": ["crossref", "nih reporter"],
        "deviation": "OpenAlex rate-limited this host; Crossref used as primary and expansion runs backwards along reference lists rather than forwards. See module docstring.",
        "terms_searched": TERMS, "reporter_queries": REPORTER_QUERIES,
        "rows_per_term": args.rows_per_term,
        "expansion": {k: v for k, v in c.items() if k != "added"},
        "graph": {k: v for k, v in d.items() if k not in ("pagerank", "betweenness")},
        "statistics": e, "self_test": st,
        "institutional_seed": {"awards": len(a["awards"]), "pis": len(a["pis"])},
    }, indent=2), encoding="utf-8")
    (OUT / "graph_scores.json").write_text(json.dumps(
        {"pagerank": d["pagerank"], "betweenness": d["betweenness"]}, indent=2), encoding="utf-8")
    print(f"\nWrote {len(pool)} candidates to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
