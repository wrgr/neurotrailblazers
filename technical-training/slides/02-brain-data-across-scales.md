---
layout: page
title: "Slide Deck Draft: Brain Data Across Scales"
permalink: /technical-training/slides/02-brain-data-across-scales/
slug: slides-02-brain-data-across-scales
---

## Session profile
- Audience: learners who will design or evaluate cross-scale studies.
- Duration: 75 minutes lecture + 15 minutes exercise.
- Output: scale selection worksheet for one research question.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and unit objective
2. Slide 2 (5 min): Why scale is a technical, not cosmetic, choice
3. Slide 3 (6 min): Modality ladder
   - Macro to nano; what each tier can resolve.
4. Slide 4 (6 min): Acquisition scale vs analysis scale
   - Common mismatch patterns and consequences.
5. Slide 5 (6 min): Representation stack
   - Volumes, segments, skeletons, meshes, graphs.
6. Slide 6 (6 min): Registration fundamentals
   - Transform classes and uncertainty propagation.
7. Slide 7 (6 min): Anisotropy and sampling artifacts
   - Why isotropic assumptions fail.
8. Slide 8 (6 min): Compute/storage implications by scale
   - I/O, memory, and indexing costs.
9. Slide 9 (7 min): Worked case
   - Same hypothesis evaluated at two scales, different conclusions.
10. Slide 10 (5 min): Cross-scale provenance
    - Required metadata for reproducible linkage.
11. Slide 11 (5 min): Failure modes
    - Scale leakage, over-registration confidence, representation collapse.
12. Slide 12 (5 min): Protocol checklist
    - Minimal sufficient scale decision template.
13. Slide 13 (5 min): Activity
    - Pick one question and defend your chosen scale.
14. Slide 14 (5 min): Bridge to acquisition quality in Unit 03.

## Figure integration points
- Primary shortlist: `course/units/figures/02-brain-data-across-scales-selected-v1.md`.
- Must include one panel showing representation conversion and one showing registration residuals.

## Speaker notes (expert-level)
- Quantify tradeoffs whenever possible (resolution vs volume vs cost).
- Highlight how scale-dependent uncertainty should be reported in final claims.

## Assessment and artifacts
- Deliverable: scale-aware study design card.
- Rubric dimensions: feature resolvability, transform traceability, and resource realism.

## Connections
- Unit page: [Brain Data Across Scales]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module04]({{ '/modules/module04/' | relative_url }}), [module05]({{ '/modules/module05/' | relative_url }}), [module12]({{ '/modules/module12/' | relative_url }})

## Slide source file
- Marp draft source: `course/decks/marp/{{ page.slug | remove: "slides-" }}.marp.md`
- Rendered HTML deck: `/course/decks/marp/out/{{ page.slug | remove: "slides-" }}.html`
- PowerPoint deck: `/course/decks/marp/out/{{ page.slug | remove: "slides-" }}.pptx`
- Batch render helper: `./scripts/render_marp.sh`
