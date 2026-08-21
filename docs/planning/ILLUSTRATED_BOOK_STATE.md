# Illustrated book — state of work

*Branch: `claude/brain-connects-narrative-5qo317` · Last updated: 2026-08-21*

The ask this branch answers: **"BRAIN and CONNECTS struggles to explain strategy and
impact for the work and investment to the public. Can we put together a compelling
book — illustrated cartoon? With clear evidence and accomplishments so far."**

---

## What exists and works

**`/book/` — "The Last Great Map"** (`book/index.html`, one self-styled page on the
default layout, linked from the About dropdown and the homepage impact section).

Eleven chapters, each with a hand-drawn inline SVG cartoon panel, public-friendly
narrative, and an evidence box whose every claim resolves to a numbered source:

| # | Chapter | Carries |
|---|---|---|
| 1 | The uncharted country | 86B neurons; the connectome as the missing map |
| 2 | Why bother | GBD 2021: 3.4B people, #1 cause of ill health; repair-without-schematic framing |
| 3 | The strategy | 2013 tools-first bet; >$3B, 1,300+ projects |
| 4 | Proof it works | Worm (15 yr by hand) → fly (139,255 neurons, 287 co-author proofreaders); ~1,000× per-neuron speedup (labeled as our arithmetic) |
| 5 | A grain of sand | MICrONS 1 mm³ (2 PB, function+wiring); H01 human fragment |
| 6 | Dividends | BICCN atlas (32M cells, 5,300+ types); DBS, dopamine sensor; AI both directions |
| 7 | From wiring to health | Retina motion rule (2011); like-to-like cortex rule (2025); H01 axon whorls; adaptive DBS FDA approval (Feb 2025); NIH speech BCI (Mar 2025); Alzheimer's/epilepsy baselines as *prospects* |
| 8 | Why is this so hard | The four chores: slice / photograph / store / untangle; proofreaders as the scarce resource |
| 9 | BRAIN CONNECTS | 11 awards, ~$150M, 40+ institutions; ELI5 cards for the three routes; HI-MC flagship |
| 10 | Limits | Bargmann & Marder; map of roads not traffic; genome-project analogy (provenance flagged) |
| 11 | Room for your name | EyeWire 200k players; FlyWire citizen co-authors; NeuroTrailblazers as workforce arm |

Plus: eight-number spread, 1986→2028 timeline, "A note on the receipts" (release-specific
counts caveat), 27 numbered sources, print CSS, CTA. Shared cartoon characters (Maya,
Pip) live in one SVG `<defs>` block and are `<use>`-referenced by panels.

**Validation:** `validate_frontmatter.rb`, `check_site_links.rb`, `check_anchor_links.rb`
all pass on the built site. Build recipe on this container: `export
PATH=/opt/rbenv/versions/3.1.6/bin:$PATH` (Gemfile pins Ruby 3.1.6), `bundle install`,
`LANG=C.UTF-8 LC_ALL=C.UTF-8 bundle exec jekyll build`. Panels were visually verified
with headless Chromium screenshots.

## Editorial ground rules established (keep these)

- Every evidence-box claim needs a numbered source; derived arithmetic and analogies
  are explicitly labeled as ours (per-neuron speedup, slice-per-hair, HGP comparison).
- Numbers describe a **specific data release**, not the animal — stated in ch. "A note
  on the receipts."
- Claims this repo's own fabrication audit flagged as uncited are **deliberately not
  used**: the "$40M" figure, "50× larger", the "91-beam" count, the conflicting
  4 nm / 8 nm HI-MC resolutions, the repo-only CONNECTS acronym expansion. If these
  get sourced upstream, they can come back.
- Health claims are split into delivered results (cited) vs. baselines/prospects
  (future-tensed, hedged) — never promise a cure by a date.
- Newly verified sources beyond the repo: NINDS CONNECTS announcement, NIH awards
  release (>$3B / deliverables), GBD 2021 / WHO, MICrONS Nature 640 (2025) + Ding et
  al. wiring rule, Medtronic adaptive-DBS FDA approval (Feb 2025), NIH Research
  Matters speech-BCI (Mar 2025).

## Requested next (pending, in priority order)

1. **The inverse chapter** (task: "Show the inverse. Disease, computation. We know
   stuff. Stuck. Imprecise. People dying. No map!! Need to do the following…").
   Mirror of ch. 7: stand on the clinic bank and the computation bank looking back at
   the fog where the map should be. Structure: what medicine already knows (genes,
   cells, symptoms) → where it is stuck without circuit sight (trial-and-error meds,
   ~30% drug-resistant epilepsy [verify via WHO fact sheet], no Alzheimer's cure) →
   same inversion for AI (20 W vs gigawatts; the one wiring sketch we copied launched
   CNNs; no further blueprints) → ends in a concrete numbered **"what must be done"**
   list mapping to CONNECTS routes + workforce + open data + sustained funding
   [sources 8, 15–17 already in the book]. Suggested placement: after ch. 7, before
   "Why is this so hard" (renumber 8→9 etc. — badge numbers are hardcoded spans).
2. **Hitchhiker's Guide + PDF edition** ("combine this with a hitchhiker's guide to
   brain mapping with summaries of all the key reference things — a pdf/book that
   takes the key site points"). Plan: new `/book/guide/` reference companion
   (dataset cheat-sheets, pipeline stages from `/datasets/workflow/`, glossary from
   the site dictionary data, acronym decoder, key-papers reading list from
   `content-library/journal-papers/`), then print `/book/` + `/book/guide/` to PDF
   with headless Chromium, merge, commit as a downloadable asset linked from the
   book page.
3. **Technical gap audit** ("audit site for technical gaps"). Sweep
   `technical-training/`, `content-library/`, `modules/` for missing/thin topics and
   internal inconsistencies; deliver `docs/TECHNICAL_GAPS.md` with prioritized,
   file-referenced findings. Known seeds from the earlier fact-extraction pass: HI-MC
   resolution stated as 4 nm vs 8 nm in different pages; mSEM-IBEAM vs ATUM described
   as the acquisition method in different pages; H01 z-resolution 33 vs 30 nm;
   MICrONS 80k neurons vs 200k cells and "2021 bioRxiv" vs "2025 release" not
   reconciled; C. elegans gap junctions 900 (text) vs 600 (caption); two different
   titles for the same H01 DOI and for Lappalainen et al. 2024.

## Session-container notes for whoever resumes

- Screenshots and Playwright scripts live in the session scratchpad (ephemeral).
- Local preview: `python3 -m http.server 8123` from `_site/`, then screenshot with
  Playwright using the pre-installed Chromium (`NODE_PATH=$(npm root -g)`).
- The earlier fact-extraction summary (per-case-study numbers, contradictions, and
  which claims are uncited) is reproduced in essentials above; the case-study pages
  themselves are the ground truth to re-check against.
