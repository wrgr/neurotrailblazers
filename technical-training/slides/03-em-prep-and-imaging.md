---
layout: page
title: "Lecture Plan: EM Prep and Imaging"
permalink: /technical-training/slides/03-em-prep-and-imaging/
slug: slides-03-em-prep-and-imaging
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
- Audience: learners working with EM data acquisition or QA.
- Duration: 75 minutes lecture + 15 minutes QA exercise.
- Output: acquisition risk register and QA gate plan.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and positioning
2. Slide 2 (4 min): Acquisition quality as reconstruction ceiling
3. Slide 3 (6 min): End-to-end prep chain
   - Fixation, staining, sectioning/block-face, imaging.
4. Slide 4 (6 min): Imaging parameter tradeoffs
   - Dwell time, beam current, overlap, and throughput.
5. Slide 5 (6 min): Artifact taxonomy I
   - Physical artifacts: fold, tear, chatter, compression.
6. Slide 6 (6 min): Artifact taxonomy II
   - Contrast/charging/drift and alignment implications.
7. Slide 7 (6 min): Stitching and stack assembly QA
8. Slide 8 (6 min): Pilot segmentation as acquisition validation
9. Slide 9 (7 min): Worked artifact triage example
10. Slide 10 (5 min): Metadata standards and provenance requirements
11. Slide 11 (5 min): Failure escalation protocol
12. Slide 12 (5 min): Throughput vs fidelity governance decisions
13. Slide 13 (5 min): Mini-lab
    - Build a risk register for one tissue/imaging configuration.
14. Slide 14 (6 min): Bridge to infrastructure and large-scale processing.

## Figure integration points
- Primary shortlist: `course/units/figures/03-em-prep-and-imaging-selected-v1.md`.
- Include at least one before/after artifact correction panel.

## Speaker notes (expert-level)
- Tie every artifact class to a concrete downstream segmentation failure type.
- Emphasize regional QA rather than global aggregate quality claims.

## Assessment and artifacts
- Deliverable: acquisition QA checklist with quantitative triggers.
- Rubric dimensions: artifact coverage, detection metrics, mitigation realism.

## Connections
- Unit page: [EM Prep and Imaging]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module05]({{ '/modules/module05/' | relative_url }})

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