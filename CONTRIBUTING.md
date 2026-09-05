# Contributing to NeuroTrailblazers

Contributions are welcome: corrections, new content, figures, and fixes to the generators
and validators. This file is the standard the material is written to and the mechanics of
working in the repository.

If you only want to report that something is wrong, you do not need any of this — open an
issue at <https://github.com/wrgr/neurotrailblazers/issues> and name the page and the
line, or email <info@neurotrailblazers.org>.

By contributing you agree that your content contributions are licensed CC BY 4.0 and your
code contributions MIT, matching [`LICENSE`](LICENSE).

---

## 1. The content standard

This is the part that matters most, and it is where most drafts need work. It is
summarised here from `docs/CONTENT_REVIEW.md` on the
[`holding/internal-planning`](https://github.com/wrgr/neurotrailblazers/tree/holding/internal-planning)
branch, where the full review lives.

The standard exists because of a specific failure the site has already had once. The
technical units were originally about 700 words each and consisted almost entirely of
noun-phrase bullets naming topics. A representative line:

> **Tissue preparation:** Stabilize ultrastructure while minimizing shrinkage and
> extraction artifacts.

That states a goal. It has no protocol, no reagent, no number, no failure signature, and
no way to tell whether you did it. A learner cannot act on it and an instructor cannot
teach from it. **Those were specifications, not instruction** — a correct list of what a
course should contain, published as if it were the course.

The reason this matters more here than in most technical curricula: **the core skills in
connectomics are perceptual and judgemental, not procedural.** Reading an EM image,
deciding whether a segmentation is trustworthy, choosing a null model — none of these
transfer by explanation. Someone who can recite the three criteria for calling a synapse
will still, on their first real patch, call a tangentially cut membrane a synapse. A list
of topic names is the least effective possible format for that, because it gives no
worked example to imitate, no numbers to calibrate against, no retrieval practice, no
feedback loop, and no answer key for the learner working alone — which is most of the
audience.

### What a learner-facing page must have

| Section | What it does |
|---|---|
| **Before you start** | Time, prerequisites, what you need, what you finish with. Lets a reader decide whether to start. |
| **What you'll be able to do** | **Observable, testable competencies** — not "understand X". If you cannot imagine grading it, rewrite it. |
| **Numbered content sections** | Real numbers, protocols, decision tables. Every claim actionable. |
| **Check yourself** | Retrieval-practice questions with the answers in collapsed `<details>` blocks. The answers explain the reasoning and generalise the principle; they do not merely confirm the fact. |
| **Worked example** | One expert judgement narrated in full, **including the uncertainty** — what you weighed, what you were unsure of, what would have changed your mind. |
| **Lab** | A graded exercise producing an artifact, with a rubric. |
| **Common errors and how to recover** | Each error paired with a specific recovery action. |
| **What this page does not cover** | Honest scope, with pointers to what does cover it. A boundary is a feature, not a disclaimer. |
| **Go deeper** | Links into the content library — the reference layer behind the page. |

### The rules underneath it

- **Numbers over adjectives.** "About 2 PB per mm³" beats "very large". Structure sizes,
  resolutions, dose tradeoffs, data volumes, GPU-days, proofreading hours — a reader
  should be able to estimate afterwards, not gesture.
- **Cite the number.** If a figure is checkable, give the source. Numbers on this site
  have drifted before; that is what the validators are for.
- **Rubrics have three levels: Not yet / Proficient / Strong.** "Strong" is consistently
  *the thing that separates a practitioner from someone who followed the steps* — naming
  the assumption, measuring calibration rather than accuracy, reporting the error band.
- **Answers ship with the questions,** in collapsed disclosure elements, so a learner
  alone can test themselves honestly. Tell them not to open it yet; do not withhold it.
- **Cost reasoning is content.** Merge versus split errors, data-loss versus labour
  artifacts, triage by endpoint impact rather than conspicuousness. This is the field's
  central operational logic.
- **Say what the page does not show.** State scope boundaries explicitly and point
  onward.
- **Plain verbs, short sentences, no hype.** No "audacious", "revolutionary", "unlock".
- **Address the reader as a colleague who has not done this yet,** never as a novice.
- **Headings state the claim, not the topic.**

Voice notes are in `docs/brand/BRAND_GUIDE.md` §2 (excluded from the build; read it in
the repository).

---

## 2. Files you must not hand-edit

Several directories are **generated**. Editing them looks like it works and is silently
reverted the next time a generator runs.

| Generated | Produced by | Edit this instead |
|---|---|---|
| `assets/worksheets/moduleNN/` | `scripts/generate_module_teaching_materials.rb` | `modules/moduleNN.md` |
| `course/decks/marp/modules/` | `scripts/generate_module_teaching_materials.rb` | `modules/moduleNN.md` |
| `modules/slides/` | `scripts/generate_module_teaching_materials.rb` | `modules/moduleNN.md` |
| `assets/images/modules/*.svg` | `scripts/generate_module_art.rb` | the art generator |
| `_data/journal_papers.yml` | `scripts/derive_journal_papers.py` | the corpus and the derivation script |

To change a worksheet or a module deck, edit the module page and re-run:

```bash
ruby scripts/generate_module_teaching_materials.rb
```

The generator reads specific headings from each module page: `## Capability target`,
`## Concept set` (including its `- **Misconception guardrail:**` lines), `## Core
workflow`, a run-of-show section, `## Studio activity` (with its `**Scenario:**`,
numbered steps and outputs list), `## Assessment rubric`, and `## Quick practice prompt`.
**Removing or renaming one of these silently degrades the generated worksheet to a
placeholder** — so if a worksheet suddenly says "See module page for details", a heading
moved.

Rendered decks under `course/decks/marp/out/` are produced by `scripts/render_marp.sh`,
which records a SHA-256 per source; `check_deck_freshness.rb` fails if a source has
changed and the deck has not been re-rendered.

---

## 3. Validators

Run from the repository root. All exit non-zero on a problem, and all run in CI
(`.github/workflows/validate.yml`). The first group needs no gems — plain `ruby`:

```bash
export LANG=C.UTF-8 LC_ALL=C.UTF-8

ruby scripts/validate_frontmatter.rb          # required front-matter keys by page type
ruby scripts/validate_figure_refs.rb          # figure IDs resolve; Marp image paths exist
ruby scripts/validate_technical_evidence.rb   # technical_track.yml vs technical_evidence.yml
ruby scripts/validate_paper_counts.rb         # journal-paper counts, schema, authors, years
ruby scripts/check_deck_freshness.rb          # rendered decks match their sources
ruby scripts/validate_dictionary.rb           # dictionary entries carry the promised fields
```

The two link audits need a build first, because they read `_site/`:

```bash
bundle exec jekyll build
ruby scripts/check_site_links.rb              # internal links resolve to real pages
ruby scripts/check_anchor_links.rb            # cross-page #fragments resolve to real ids
```

`check_site_links.rb` only confirms a link's target page exists; `check_anchor_links.rb`
catches the other half — a deep link into a heading that has since been renamed.

`LANG`/`LC_ALL` matter: the scripts read files as UTF-8, but the locale still governs
Ruby's default external encoding and Jekyll's SCSS converter, which will otherwise fail on
non-ASCII characters in the stylesheets.

---

## 4. Building the site

Requires **Ruby 3.1.6**, matching the `ruby` pin in the `Gemfile` and the GitHub Pages
runtime the site deploys to. (The validation scripts are stdlib-only and run under 3.3 in
CI; only the build needs 3.1.6, because Bundler refuses to install under a version other
than the pin.)

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000/>. `baseurl` is `""`, so there is no path prefix locally.

Use `{{ '/path/' | relative_url }}` for internal links rather than bare paths, and keep
the trailing slash — several link classes have broken on a missing one.

---

## 5. Submitting a change

1. Branch from the deployed branch.
2. Make the change. If it touches a module page, re-run the generator and commit the
   regenerated files with it.
3. Run the validators above, and the build plus both link audits.
4. Open a pull request describing what changed and, for content, which part of the
   standard in §1 it satisfies — particularly the worked example, the self-check answers,
   and the "what this does not cover" section, which are the three most often missing.

New content that is a topic list without worked judgement will be sent back, however
accurate it is. That is the one thing this repository has already had to fix at scale.
