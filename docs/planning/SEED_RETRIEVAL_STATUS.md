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

## Final result of the corrected full run

`python3 -u scripts/seed_retrieval.py --rows-per-term 60 --max-expand 400`
completed. Output committed and pushed as `36bb777`.

- **776 candidates**, 0 without a DOI, no implausible years (range 1955–2026).
- **Self-test: 6 of 7** held-out papers found (up from 1/7 pre-fix). Only LICONN
  (2025, light-microscopy connectomics — the newest and most narrowly-scoped of
  the seven) is still missed.
- Top journals: Nature (45), Neuron (31), Nature Methods (26), Microscopy and
  Microanalysis (23), eLife (22), Cell (20), Science (16), PNAS (15) — a
  legitimate neuroscience/microscopy distribution, not the chemical-engineering/
  object-detection noise the pre-fix run produced.
- Capture-recapture: 282 found by the all-time-relevance strategy, 210 by the
  recent-filtered strategy, 115 by both, Lincoln-Petersen estimate ~515
  (indicative only — the two strategies aren't fully independent).
- `top_three_institution_share`: 0.015 (low concentration, as expected for a
  field-wide sweep rather than a single-lab bias).
- Author-count distribution: 517 papers with 1–5 authors, 223 with 6–20, 32 with
  21–100, 4 with 100+ (consortium papers). 11 consortium-authored records.

**Incident during wrap-up:** a `git checkout --` run to clean the working tree
executed *after* the background run had already finished writing fresh output,
reverting the 776-candidate result back to an old committed 219-candidate
smoke-test artifact. Recovered by replaying the script against its own disk
cache (`_data/seed_retrieval/cache/`, gitignored, 842 cached responses) — same
inputs, same result, ~8 seconds, no new API calls. Lesson for future sessions:
don't run `git checkout --` on paths a background process still owns without
confirming the process has actually exited.

## What to do next

1. Quality looks sound (6/7 self-test, clean journal/year distribution) — this
   pool is ready to hand to the "clean run" judgment step. Give it
   `candidate_pool.json` + `method_report.json` + `graph_scores.json`; the deep-
   research brief in `SEED_CORPUS_RESET_BRIEF.md` already specifies the output
   schema (tiers, areas, summaries) that step should produce.
2. Optionally chase the LICONN gap before handoff: it's a single specific 2025
   Nature paper, findable directly by DOI/title lookup rather than another full
   sweep — the vocabulary-sweep terms don't include "LICONN" or "light
   microscopy" phrasing, which is likely why it wasn't retrieved.
3. Once judged output exists: run `scripts/audit_citations.py` against it before
   it replaces `_data/expert_seed_papers/`.

## Independent cross-check channel (new, this session)

At the user's request: `_data/seed_retrieval/recall_cross_check.md` is a
**deliberately un-retrieved**, memory-based list produced without looking at
this repo's data, meant as a second independent "capture" for a
capture-recapture-style sanity check on retrieval coverage — not as a citation
source. It is explicitly marked unverified throughout; nothing in it should
reach the corpus without going through Crossref verification first. Use it by
diffing its titles against `candidate_pool.json`: real gaps (things on that
list with no match in the pool) are worth a targeted Crossref lookup; things
the pool found that aren't on that list just mean my training data
under-weighted them, which is not a defect.

**Count correction:** the file's own "Honest accounting" section originally
claimed ~180 papers; the actual bullet count is 77 papers plus ~90 people
(~167 total). That overstatement has been fixed in the file itself — see the
commit that corrects it. The user's ask was "at least 200"; 167 falls short of
that threshold, so this list should be treated as a partial cross-check, not a
complete one, unless extended.

## Still pending after all of the above

- No PR has been opened for `claude/seed-corpus-retrieval` yet.
- No verification pass (`scripts/audit_citations.py`) has been run against any
  candidate pool — there wasn't a trustworthy pool to check until now.
- `_data/expert_seed_papers/` (the corrupted corpus) is untouched, as decided —
  it gets replaced only once verified, judged output exists.
- Task #21 in the session's task list ("Rebuild the seed corpus from verified
  deep-research output") is `in_progress`, not done.
- The recall cross-check (~167 entries) is short of the user's "at least 200"
  ask — extend it if a fuller cross-check is wanted before handoff.
