---
layout: page
title: "Slide Deck Draft: Atlas Connectomics Reference"
permalink: /technical-training/slides/atlas-connectomics-reference/
slug: slides-atlas-connectomics-reference
---

## Session profile
- Audience: course staff, advanced learners, and journal-club facilitators.
- Duration: 55 minutes workshop + 20 minutes curation exercise.
- Output: three fully curated atlas entries with complete metadata.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and role of the atlas
2. Slide 2 (4 min): Why static reading lists fail at this scale
3. Slide 3 (5 min): Atlas metadata schema
4. Slide 4 (5 min): Workflow-stage indexing model
5. Slide 5 (5 min): Maturity and evidence grading
6. Slide 6 (5 min): Reproducibility and artifact availability criteria
7. Slide 7 (5 min): Link hygiene and deprecation policy
8. Slide 8 (6 min): Worked curation example (paper + dataset + tool)
9. Slide 9 (5 min): Common curation failure modes
10. Slide 10 (5 min): Governance roles and review cadence
11. Slide 11 (6 min): Hands-on curation activity setup
12. Slide 12 (7 min): Debrief and next update cycle

## Figure integration points
- Primary shortlist: `course/units/figures/atlas-connectomics-reference-selected-v1.md`.
- Use workflow-stage schematic and metadata checklist visual.

## Speaker notes (expert-level)
- Keep entries operationally useful: each should answer "when do I use this?" quickly.
- Flag historical but influential resources without presenting them as current defaults.

## Assessment and artifacts
- Deliverable: curated entry set with required schema fields.
- Rubric dimensions: metadata completeness, workflow relevance, and limitation clarity.

## Connections
- Unit page: [Atlas Connectomics Reference]({{ '/technical-training/atlas-connectomics-reference/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: none yet (reference unit)

## Slide source file
- Marp draft source: `course/decks/marp/{{ page.slug | remove: "slides-" }}.marp.md`
- Rendered HTML deck: `/course/decks/marp/out/{{ page.slug | remove: "slides-" }}.html`
- PowerPoint deck: `/course/decks/marp/out/{{ page.slug | remove: "slides-" }}.pptx`
- Batch render helper: `./scripts/render_marp.sh`
