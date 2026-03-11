---
layout: page
title: "Slide Deck Draft: Axons and Dendrites"
permalink: /technical-training/slides/06-axons-and-dendrites/
slug: slides-06-axons-and-dendrites
---

## Session profile
- Audience: annotation and QC teams handling process-type decisions.
- Duration: 75 minutes lecture + 15 minutes edge-case adjudication.
- Output: axon-vs-dendrite decision matrix and confusion analysis.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and decision impact on graphs
2. Slide 2 (5 min): Why process misclassification propagates error
3. Slide 3 (6 min): Morphology cue library
4. Slide 4 (6 min): Organelle and synaptic-role cues
5. Slide 5 (6 min): Multi-cue voting strategy
6. Slide 6 (6 min): Continuity checks across slices/branches
7. Slide 7 (7 min): Edge case I: thin dendrites
8. Slide 8 (7 min): Edge case II: en passant boutons
9. Slide 9 (6 min): Edge case III: truncation and missing context
10. Slide 10 (5 min): Confidence schema and escalation rules
11. Slide 11 (5 min): Team calibration protocol
12. Slide 12 (5 min): QA metrics and confusion matrix interpretation
13. Slide 13 (5 min): Activity setup
    - adjudicate three ambiguous examples.
14. Slide 14 (5 min): Debrief and bridge to glia boundaries.

## Figure integration points
- Primary shortlist: `course/units/figures/06-axons-and-dendrites-selected-v1.md`.
- Include side-by-side cue panels and at least one contested case.

## Speaker notes (expert-level)
- Avoid single-cue decisions; require convergence or explicit provisional labels.
- Quantify downstream impact (motif counts, edge direction errors).

## Assessment and artifacts
- Deliverable: decision matrix with evidence fields and confidence tags.
- Rubric dimensions: cue integration quality, consistency, and auditability.

## Connections
- Unit page: [Axons and Dendrites]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module04]({{ '/modules/module04/' | relative_url }}), [module09]({{ '/modules/module09/' | relative_url }})
