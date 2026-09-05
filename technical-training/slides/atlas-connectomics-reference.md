---
layout: page
title: "Lecture Plan: Atlas Connectomics Reference"
permalink: /technical-training/slides/atlas-connectomics-reference/
slug: slides-atlas-connectomics-reference
content_type: delivery
---

## What this document is

This page is a **build plan for an instructor assembling a lecture** on this unit. It gives the
slide sequence, per-slide timing, the points at which figures belong, and the speaker notes that
carry the argument. It is a design document, not a rendered deck: there are no slides on this
page to project, and nothing here is written to be shown to learners as it stands.

A separately maintained Marp deck for this unit does exist, and it is linked at the foot of this
page under *Rendered deck artifacts*. That deck was authored in its own right and does not follow
this plan slide for slide, so treat this page as the teaching design and the Marp file as one
existing implementation of it. The learner-facing material is the unit page linked under
*Connections*.

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

## Rendered deck artifacts
<div class="resource-card">
  <p>These are the separately maintained Marp deck artifacts for this unit. They are not generated from the plan above, so their sequence and timing differ from it.</p>
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/' | append: page.slug | remove: 'slides-' | append: '.html' | relative_url }}">Open HTML Deck</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/{{ page.slug | remove: 'slides-' }}.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/technical-training/' | append: page.slug | remove: 'slides-' | append: '/' | relative_url }}">Open Unit Page</a>
  </div>
  <p><small>The HTML deck presents directly in a browser. The Markdown source is the one to
  take if you want to adapt it &mdash; it renders with <a href="https://marp.app/">Marp</a>.
  For PowerPoint, run <code>./scripts/render_marp.sh --pptx</code>; the exports are not
  committed because the full set runs to tens of megabytes.</small></p>
  <p><strong>Batch render helper:</strong> <code>./scripts/render_marp.sh</code></p>
</div>