---
layout: page
title: "Lecture Plan: Connectome Analysis and NeuroAI"
permalink: /technical-training/slides/09-connectome-analysis-neuroai/
slug: slides-09-connectome-analysis-neuroai
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
- Audience: advanced learners bridging connectomics with computational modeling.
- Duration: 85 minutes lecture + 15 minutes motif-design exercise.
- Output: executable motif-analysis plan with null-model justification.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and learning objective
2. Slide 2 (5 min): From reconstructed circuit to testable graph hypotheses
3. Slide 3 (6 min): Motif analysis workflow overview
4. Slide 4 (6 min): Query language and representation choices
5. Slide 5 (6 min): Subgraph isomorphism complexity and tooling
6. Slide 6 (6 min): Null models I
   - degree preserving and random rewires.
7. Slide 7 (6 min): Null models II
   - spatial and cell-type constrained controls.
8. Slide 8 (7 min): Multiple-testing and statistical interpretation
9. Slide 9 (7 min): Worked query example (DotMotif-style)
10. Slide 10 (7 min): Reproducibility requirements
    - versioned data, query code, seeds.
11. Slide 11 (5 min): Cross-dataset comparability caveats
12. Slide 12 (5 min): NeuroAI transfer: where it helps, where it overreaches
13. Slide 13 (6 min): Failure modes
    - post-hoc hypotheses, null mismatch, overgeneralization.
14. Slide 14 (6 min): Activity + debrief
    - define motif, null, and success criterion.

## Figure integration points
- Primary shortlist: `course/units/figures/09-connectome-analysis-neuroai-selected-v1.md`.
- Use one algorithmic complexity visual, one motif query visual, one benchmark caveat panel.

## Speaker notes (expert-level)
- Keep exploratory and confirmatory analyses explicitly separated.
- Treat all benchmark performance from older decks as historical unless revalidated.

## Assessment and artifacts
- Deliverable: motif-analysis protocol card.
- Rubric dimensions: hypothesis clarity, statistical rigor, and reproducibility.

## Connections
- Unit page: [Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module10]({{ '/modules/module10/' | relative_url }}), [module13]({{ '/modules/module13/' | relative_url }}), [module14]({{ '/modules/module14/' | relative_url }}), [module15]({{ '/modules/module15/' | relative_url }}), [module20]({{ '/modules/module20/' | relative_url }})

## Rendered deck artifacts
<div class="resource-card">
  <p>These are the separately maintained Marp deck artifacts for this unit. They are not generated from the plan above, so their sequence and timing differ from it.</p>
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/' | append: page.slug | remove: 'slides-' | append: '.html' | relative_url }}">Open HTML Deck</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/' | append: page.slug | remove: 'slides-' | append: '.pptx' | relative_url }}">Download PowerPoint (.pptx)</a>
    <a class="resource-link" href="{{ '/technical-training/' | append: page.slug | remove: 'slides-' | append: '/' | relative_url }}">Open Unit Page</a>
  </div>
  <p><strong>Marp source path:</strong> <code>course/decks/marp/{{ page.slug | remove: "slides-" }}.marp.md</code></p>
  <p><strong>Batch render helper:</strong> <code>./scripts/render_marp.sh</code></p>
</div>