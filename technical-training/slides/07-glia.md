---
layout: page
title: "Slide Deck Draft: Glia"
permalink: /technical-training/slides/07-glia/
slug: slides-07-glia
---

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

## Slide source file
- Marp draft source: `course/decks/marp/{{ page.slug | remove: "slides-" }}.marp.md`
- Rendered HTML deck: `/course/decks/marp/out/{{ page.slug | remove: "slides-" }}.html`
- PowerPoint deck: `/course/decks/marp/out/{{ page.slug | remove: "slides-" }}.pptx`
- Batch render helper: `./scripts/render_marp.sh`
