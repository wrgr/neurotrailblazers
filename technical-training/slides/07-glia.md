---
layout: page
title: "Lecture Plan: Glia"
permalink: /technical-training/slides/07-glia/
slug: slides-07-glia
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
- Audience: learners needing robust neuron-glia boundary decisions.
- Duration: 70 minutes lecture + 20 minutes morphology drill.
- Output: glia recognition checklist and adjudication log.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and glia relevance
2. Slide 2 (5 min): Why glia are not "background"
3. Slide 3 (6 min): Class overview
   - Astrocytes, microglia, oligodendrocytes.
4. Slide 4 (6 min): Morphological and contextual cues
5. Slide 5 (6 min): Vascular and myelin context interpretation
6. Slide 6 (6 min): Glia-neuron ambiguity classes
7. Slide 7 (7 min): Worked case I: astrocyte-like process
8. Slide 8 (7 min): Worked case II: microglia confusion case
9. Slide 9 (6 min): Worked case III: oligodendrocyte/myelin boundaries
10. Slide 10 (5 min): QC metrics for glia labeling
11. Slide 11 (5 min): Escalation and second-pass review workflow
12. Slide 12 (5 min): Common failure patterns in practice
13. Slide 13 (5 min): Activity
    - classify and justify two ambiguous examples.
14. Slide 14 (5 min): Debrief and bridge to segmentation/proofreading.

## Figure integration points
- Primary shortlist: `course/units/figures/07-glia-selected-v1.md`.
- Include one class comparison table and one ambiguity panel.

## Speaker notes (expert-level)
- Stress glia corrections as high-value QC, not optional cleanup.
- Tie glia labeling errors to false neuronal connectivity inferences.

## Assessment and artifacts
- Deliverable: glia checklist with evidence requirements.
- Rubric dimensions: class discrimination quality and uncertainty handling.

## Connections
- Unit page: [Glia]({{ '/technical-training/07-glia/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module04]({{ '/modules/module04/' | relative_url }})

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