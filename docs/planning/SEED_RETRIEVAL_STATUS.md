# Seed corpus retrieval — status (2026-08-21)

Working notes for resuming this thread. Read this before re-reading the whole
session transcript.

## Where things stand

Branch: `claude/seed-corpus-retrieval` (not yet merged to `main`).
Latest pushed commit: `61dc0b3` — "Fix two relevance-discarding Crossref queries
in the seed retrieval sweep".

The decision already made and executed: **reset, not repair**, the corrupted
`_data/expert_seed_papers/` (see `docs/planning/SEED_CORPUS_RESET_BRIEF.md` for the
full rationale and the deep-research query, merged to `main` in PR #156). Division
of labor agreed with the user: this session does **retrieval** as deterministic code
(`scripts/seed_retrieval.py`) so nothing can be a fabricated DOI by construction;
judgment (inclusion, tiering, area/summary writing) is meant to happen in a separate
"clean" LLM run with no repo access, so it isn't primed by the corpus that broke.

## What `scripts/seed_retrieval.py` does

Five stages: NIH RePORTER awards → institutional seed of PI names (Stage A);
a Crossref sweep over 31 hand-picked vocabulary phrases, two strategies kept
separate for later capture-recapture (Stage B); reference-list expansion from the
top-cited seeds, pulling in anything cited by 3+ pool papers (Stage C); PageRank
over the citation graph and Brandes betweenness over co-authorship, pure Python,
no numpy available here (Stage D); bibliometric statistics — concentration, year/
language histograms, capture-recapture estimate (Stage E); then a self-test against
7 held-out landmark DOIs that were **never** used to tune the search.

## The bug that was found and fixed today

The first full run (`--rows-per-term 60 --max-expand 400`) completed without
crashing but was bad: self-test found only **1 of 7** held-out papers, and the pool
was full of off-topic noise — chemical engineering, power systems, object-detection
CV papers, one with a bogus year of 2027.

Root cause: both of Stage B's Crossref calls used a `sort=` parameter
(`is-referenced-by-count` for the "citation" strategy, `published` for the "date"
strategy). Both **discard Crossref's relevance ranking entirely** — for a
multi-word technical phrase like `flood-filling network segmentation`, sorting by
citation count or publish date just returns whatever matches any stray token,
sorted by that other axis. `synapse detection electron microscopy` was returning
YOLO, Faster R-CNN, and a DFT electron-gas paper — all real, all hugely cited,
none about synapses.

Fix (commit `61dc0b3`): dropped both `sort=` params so both strategies use
Crossref's default relevance ranking, and added `title_matches()` — a
deterministic post-filter requiring (a) every word in the search term outside a
curated generic-suffix set (`segmentation`, `network`, `model`, ...) to appear in
the title Crossref returned, and (b) at least one domain-anchor word
(`connectome`, `neuron`, `synapse`, `microscopy`, ...) present regardless, since
some terms reduce to nothing but generic words once the suffix set is stripped. A
reduced-scale rerun (`--rows-per-term 15 --max-expand 60`) tripled the self-test
hit rate (1/7 → 3/7); the 4 still-missing papers are all 2023–2025 releases
(LICONN, MICrONS functional connectomics, H01, Winding insect brain), which a
full-size sweep should catch better since they're very recent and the "recent"
strategy's `rows` cap was the likely limiter at reduced scale.

## What's running right now

Full-scale run relaunched after the fix: `python3 -u scripts/seed_retrieval.py
--rows-per-term 60 --max-expand 400`, log at `/tmp/seedrun2.log`, started
2026-08-21 ~15:15 UTC. **This is an untracked OS background process** (started via
nested shell backgrounding, not the harness's tracked-task mechanism), so no
automatic completion notification will arrive — check it directly:

```
ps aux | grep seed_retrieval          # confirm still running
tail -50 /tmp/seedrun2.log            # progress
```

When it finishes, the log ends with `Wrote N candidates to _data/seed_retrieval/`
and these files are rewritten:
`_data/seed_retrieval/{candidate_pool,graph_scores,method_report,stage_b_index}.json`
(`stage_a_awards.json` is written earlier, at the start of Stage B).

## What to do once it finishes

1. Read `_data/seed_retrieval/method_report.json` — report the self-test result
   (`self_test.found`/`self_test.of`), pool size, capture-recapture estimate, and
   concentration stats **honestly, without rounding up**. The self-test exists
   specifically so it can fail visibly; it was never used to steer the search.
2. Spot-check `candidate_pool.json` for remaining off-topic noise the same way
   this session did (`journal`, `year` fields — watch for implausible years, and
   for journals clearly outside the field).
3. Commit and push the real output — the current committed state on
   `claude/seed-corpus-retrieval` deliberately has the *stale smoke-test* data
   reverted out (`git checkout --` was used to keep the tree clean while the real
   run was mid-flight), so the fresh files are new work, not a diff to review
   line-by-line.
4. If quality looks sound (self-test meaningfully better than 1/7, low
   off-topic rate on spot-check): hand `candidate_pool.json` +
   `method_report.json` + `graph_scores.json` to the "clean run" judgment step —
   the deep-research brief in `SEED_CORPUS_RESET_BRIEF.md` already specifies the
   output schema (tiers, areas, summaries) that step should produce.
5. If quality is still weak: the next likely lever is widening `--max-expand`
   (the reference-expansion stage, Stage C) rather than the vocabulary sweep
   itself — Stage C's "cited by 3+ pool papers" backward-expansion is a stronger
   relevance signal than any single term search, since it requires convergent
   citation from multiple already-verified-relevant seeds.

## Independent cross-check channel (new, this session)

At the user's request: `_data/seed_retrieval/recall_cross_check.md` is a
**deliberately un-retrieved**, memory-based list (~180 papers, ~70 people)
produced without looking at this repo's data, meant as a second independent
"capture" for a capture-recapture-style sanity check on retrieval coverage — not
as a citation source. It is explicitly marked unverified throughout; nothing in it
should reach the corpus without going through Crossref verification first. Use it
by diffing its titles against `candidate_pool.json`: real gaps (things on that list
with no match in the pool) are worth a targeted Crossref lookup; things the pool
found that aren't on that list just mean my training data under-weighted them,
which is not a defect.

## Still pending after all of the above

- No PR has been opened for `claude/seed-corpus-retrieval` yet.
- No verification pass (`scripts/audit_citations.py`) has been run against any
  candidate pool — there wasn't a trustworthy pool to check until now.
- `_data/expert_seed_papers/` (the corrupted corpus) is untouched, as decided —
  it gets replaced only once verified, judged output exists.
- Task #21 in the session's task list ("Rebuild the seed corpus from verified
  deep-research output") is `in_progress`, not done.
