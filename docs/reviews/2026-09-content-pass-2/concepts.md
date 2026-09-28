# Concepts explorer review (content pass 2)

Date: 2026-09-27
Branch: compass-workshops
Scope: `_data/concepts.yml` (grown from 12 to 60 entries by an earlier agent that was cut off before verifying), `concepts/index.md`, and the consumers that read the data file.

This report is appended to as the review proceeds.

## 1. Schema and consumers

Consumers of `site.data.concepts.concepts` (all read-only; none was changed):

- `concepts/index.md`: the explorer. Renders every concept through `_includes/cards/concept-card.html`, grouped by `_data/track_catalog.yml` track; builds the "What you are trying to do" dropdown from each card's `data-needs` (the `user_needs` list, joined with `|` and downcased); honors `?track=` and `?need=` query strings (compared lowercase); "Start with these" lists the first five visible card titles.
- `_includes/ui/track-need-explorer.html`: the "Concepts in This Track" section on `tracks/core-concepts-methods.md`, `tracks/research-in-action.md`, `tracks/career-and-community.md`. Same card and same need dropdown, filtered to one `track`.
- `_includes/ui/technical-unit-concepts.html` (via `_layouts/page.html`): the "Related concepts" block on each technical unit, looked up by `_data/technical_track.yml` `primary_concepts` slug; links to the explorer with `?track=<concept.track>&need=<first user_need>`.
- `technical-training/index.md`: the unit grid looks up each unit's first `primary_concepts` slug to get its `track` for the need-tag links, and the "If you need one skill now" section links five needs by exact string: `starting a research question`, `improving data quality`, `reducing identity confusion` (track `core-concepts-methods`); `prioritizing corrections`, `designing graph analyses` (track `research-in-action`).

Schema per entry: `slug`, `title`, `track`, `user_needs` (list), `summary`, `explanation`, `resources` (first entry is the card's title link), optional `teaching_resources` with `lesson`/`activity`/`slides`/`references` lists of `{title, url}`. The card shows `teaching_resources` when present, else "Related resources" from `resources[1..]`.

Slugs that other data depends on (all ten in `technical_track.yml` `primary_concepts`, unchanged and present): hypothesis-framing, scale-selection, em-artifacts-and-qa, reconstruction-architecture, ultrastructure-annotation, process-classification, glia-identification, proofreading-qc, motif-analysis, reproducibility-and-atlas. The other two originals, hidden-curriculum-navigation and mentoring-and-growth, are referenced by nothing outside the data file.

## 2. Entry-by-entry verification

### 2a. Mechanical checks (scripted, over all 60 entries)

- Count: 60 concepts (27 core-concepts-methods, 24 research-in-action, 9 career-and-community). No duplicate slugs or titles.
- The 12 original slugs are present with their original `slug`, `track` and `user_needs` values (diffed against `git show HEAD:_data/concepts.yml`).
- Every entry has `slug`, `title`, `track`, `user_needs`, `summary`, `explanation`, `resources` and `teaching_resources`; every `track` is one of the three catalog slugs.
- Paths: 137 distinct link targets; all 137 resolve to a page with that `permalink:` in the working tree (modules collection and `/modules/:basename/` default included). None of the 60 entries links any of the five pages being created in this pass (`/content-library/imaging/beyond-em/`, `/hidden-curriculum/funding-and-jobs/`, `/teaching/faq/`, `/teaching/assessment/units/`, `/teaching/syllabi/two-day/`).
- Fragments: 132 fragment links. 131 match a heading (GFM-style id) or explicit id in the source; the one my heading scan missed, `/models/#professional-pathways-workshops` (used twice by `pathways-workshops`), is an explicit kramdown block attribute (`{: #professional-pathways-workshops}` at `models.md:160`), so it resolves. The built-site check (`check_anchor_links.rb`) is in section 6.
- The five technical-training need buttons each have at least one card in the track they name: starting a research question (2 core cards), improving data quality (5), reducing identity confusion (5), prioritizing corrections (6 research cards), designing graph analyses (6).
- `user_needs` vocabulary: 31 distinct phrases. 24 are the original vocabulary (shared with `technical_track.yml`); 7 were coined by the growth pass: `choosing a dataset` (7 cards), `teaching a session` (4), `assessing learners` (2), `scoping a student project` (2), `planning a course` (1), `communicating results` (1), `reusing data responsibly` (1). See section 3 for what was consolidated.

### 2b. Coverage

- Units 01-09 and the atlas each have at least one concept, and each of the original per-unit concepts remains the unit's `primary_concepts` entry.
- Content library: every section is linked (imaging, neuroanatomy, cell-types, infrastructure, proofreading, connectomics, case-studies, em-figures) except the journal-papers bibliography (`/content-library/journal-papers/` and its 13 topic pages). Not linked at all: `/content-library/imaging/beyond-em/` (new this pass).
- Hidden curriculum: belonging, career-mechanics, conflict, lab-norms, reading-and-judging are linked; `meta-learning`, `technical-practice` and the new `funding-and-jobs` are not.
- Teaching layer: facilitator guide, session kits index, lectures (plans, worksheets, model responses), Pathways (all ten plans and worksheets), syllabi, four-session sequence, assessment bank, module model-responses index are linked. Not linked: the new `/teaching/faq/`, `/teaching/assessment/units/`, `/teaching/syllabi/two-day/`, and `/teaching/projectome-to-synapse/`.

### 2c. Content verification

(pending; every entry's summary, explanation and link titles checked against the target pages)

## 3. Defects fixed

(pending)

## 4. concepts/index.md

(pending)

## 5. Validation

(pending)

## 6. Rendered check

(pending)
