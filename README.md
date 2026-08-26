# NeuroTrailblazers

NeuroTrailblazers is a curriculum and mentorship platform for students and researchers
working in nanoscale connectomics. This repository contains the source for the
[NeuroTrailblazers website](https://neurotrailblazers.org), built with
[Jekyll](https://jekyllrb.com/).

## Repository overview

**Learner-facing content**

| Path | What it holds |
|---|---|
| `technical-training/` | The nine technical units — the canonical connectomics course, from motivation and scales through imaging, infrastructure, ultrastructure, proofreading, and analysis — plus the atlas reference that rides alongside them. Each unit is a self-contained lesson with worked examples, self-checks with answers, and a graded lab. |
| `technical-training/slides/` | Instructor **lecture plans** for each unit: slide sequence, timing, figure placement, speaker notes. These are build plans, not rendered decks. |
| `modules/` | The 25 curriculum modules, built for tutorial delivery — capability target, concept set, studio activity, rubric. |
| `content-library/` | Long-form reference material behind the units: neuroanatomy, imaging, cell types, proofreading, connectomics, case studies, and annotated reading lists. |
| `tracks/` | The three learning tracks, each with a sequenced path, time estimate, and capability-based completion criteria. |
| `teaching/` | Teaching hub and the facilitator guide. |
| `datasets/`, `tools/`, `concepts/`, `avatars/`, `notebooks/` | Dataset access, tool routing, the concept explorer, learner personas, and notebook paths. |

**Supporting**

| Path | What it holds |
|---|---|
| `_data/` | Site data: the connectomics dictionary, concepts, track catalog, module and journal-paper metadata, expert seed papers. |
| `course/` | Source material and Marp deck sources; `course/decks/marp/out/` holds rendered HTML and PPTX decks. |
| `scripts/` | Generators and validators (see below). |
| `assets/` | Styles, images, notebooks, slides, and generated worksheets. |

## Building the site

Requires Ruby 3.1.6, matching the `ruby` pin in the `Gemfile` and the GitHub Pages
runtime the site deploys to.

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000/>. The site sets `baseurl: ""`, so there is no path
prefix in local development.

Set `LANG=C.UTF-8 LC_ALL=C.UTF-8` if your environment defaults to a non-UTF-8 locale —
Jekyll's SCSS converter will otherwise fail on non-ASCII characters in the stylesheets.

## Scripts

Run from the repository root. All exit non-zero when they find a problem, and all run in
CI (`.github/workflows/validate.yml`).

| Script | What it does |
|---|---|
| `scripts/validate_frontmatter.rb` | Checks required front-matter keys by page type. |
| `scripts/validate_figure_refs.rb` | Checks figure IDs resolve to assets, and that Marp decks' local image paths exist. |
| `scripts/validate_technical_evidence.rb` | Cross-checks `_data/technical_track.yml` against `_data/technical_evidence.yml`. |
| `scripts/check_site_links.rb` | Audits internal links in `_site/`. Requires a build first. |
| `scripts/check_anchor_links.rb` | Audits cross-page fragment links against the ids actually present in target pages. Requires a build first. |
| `scripts/generate_module_teaching_materials.rb` | Regenerates worksheets, Marp module decks, and module slide pages from the module pages. |
| `scripts/generate_module_art.rb` | Regenerates the 25 module art banners in `assets/images/modules/` — deterministic vector art, one per module, keyed to pipeline stage. |

**Generated files — do not edit by hand.** `assets/worksheets/moduleNN/`,
`course/decks/marp/modules/`, and `modules/slides/` are all produced by
`generate_module_teaching_materials.rb` from the corresponding `modules/moduleNN.md`.
`assets/images/modules/*.svg` is produced by `generate_module_art.rb`.
Edit the module page (or the art generator) and re-run; hand edits are overwritten.

The generator reads specific sections from each module page: `## Capability target`,
`## Concept set` (including its `- **Misconception guardrail:**` lines), `## Core
workflow`, a run-of-show section, `## Studio activity` (with its `**Scenario:**`,
numbered steps, and an outputs list), `## Assessment rubric`, and `## Quick practice
prompt`. Removing or renaming one of these degrades the generated worksheet to a
placeholder.

## Contributing

Contributions are welcome — issues and pull requests with improvements, new content, or
corrections.

Before authoring learner-facing content, read `docs/CONTENT_REVIEW.md` on the
[`holding/internal-planning`](https://github.com/wrgr/neurotrailblazers/tree/holding/internal-planning)
branch (internal planning material lives there, off the deployed branch). It documents the
standard the technical units are written to: observable competencies rather than topic
lists, worked examples with the reasoning shown, retrieval-practice self-checks with
answers, graded rubrics, and an honest statement of what a page does not cover.
