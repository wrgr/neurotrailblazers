---
layout: page
title: "Slide Deck Draft: EM Prep and Imaging"
permalink: /technical-training/slides/03-em-prep-and-imaging/
slug: slides-03-em-prep-and-imaging
---

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

## Slide source file
- Marp draft source: `course/decks/marp/{{ page.slug | remove: "slides-" }}.marp.md`
- Rendered HTML deck: `/course/decks/marp/out/{{ page.slug | remove: "slides-" }}.html`
- PowerPoint deck: `/course/decks/marp/out/{{ page.slug | remove: "slides-" }}.pptx`
- Batch render helper: `./scripts/render_marp.sh`
