---
layout: page
title: "Slide Deck Draft: Segmentation and Proofreading"
permalink: /technical-training/slides/08-segmentation-and-proofreading/
slug: slides-08-segmentation-and-proofreading
---

## Session profile
- Audience: teams operating proofreading or segmentation-QC workflows.
- Duration: 80 minutes lecture + 15 minutes correction-log exercise.
- Output: prioritized error triage plan and QC dashboard spec.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and QC framing
2. Slide 2 (5 min): Why proofreading determines scientific validity
3. Slide 3 (6 min): Error taxonomy
   - merge, split, boundary, identity errors.
4. Slide 4 (6 min): Human-machine division of labor
5. Slide 5 (6 min): Correction protocol (local to global consistency)
6. Slide 6 (6 min): Metrics deep dive I
   - VI, edge precision/recall.
7. Slide 7 (6 min): Metrics deep dive II
   - ERL and synapse-centric F1.
8. Slide 8 (7 min): Prioritization by downstream impact
9. Slide 9 (7 min): Worked correction case I
10. Slide 10 (7 min): Worked correction case II
11. Slide 11 (5 min): Release gating and audit logs
12. Slide 12 (5 min): Team operations and reviewer calibration
13. Slide 13 (5 min): Failure modes and anti-patterns
14. Slide 14 (7 min): Activity + debrief
    - write a correction rationale and metric update.

## Figure integration points
- Primary shortlist: `course/units/figures/08-segmentation-and-proofreading-selected-v1.md`.
- Include at least one before/after correction sequence and one metric dashboard panel.

## Speaker notes (expert-level)
- Emphasize high-impact-first correction strategy.
- Pair aggregate metrics with targeted biological sanity checks.

## Assessment and artifacts
- Deliverable: correction log with before/after rationale and metric deltas.
- Rubric dimensions: error classification, correction quality, and reproducibility.

## Connections
- Unit page: [Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module06]({{ '/modules/module06/' | relative_url }}), [module07]({{ '/modules/module07/' | relative_url }})
