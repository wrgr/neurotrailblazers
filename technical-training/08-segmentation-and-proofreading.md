---
layout: page
title: "08 Segmentation and Proofreading"
permalink: /technical-training/08-segmentation-and-proofreading/
slug: 08-segmentation-and-proofreading
---

## Why this unit
Proofreading is the scientific QC layer that determines whether downstream analyses are trustworthy.

## Learning goals
- Classify and correct merge/split/boundary errors.
- Tie corrections to explicit quality metrics and logs.

## Core technical anchors
- Metrics: VI, edge precision/recall, ERL, synapse-centric F1.
- Priority strategy for high-impact error correction.
- Human-machine workflow separation: discovery, adjudication, finalization.

## Method deep dive: production proofreading loop
1. Candidate triage:
   Rank errors by estimated downstream impact (edge loss, motif distortion, cell identity risk).
2. Local correction:
   Resolve merge/split/boundary errors with 2D/3D contextual validation.
3. Global consistency:
   Recheck branch continuity and synaptic partner plausibility.
4. Metric update:
   Recompute targeted QC metrics after each correction batch.
5. Release gate:
   Promote only segments that pass predefined quality thresholds.

## Recommended QC thresholding strategy
- Use block-level dashboards for VI and edge precision/recall, not just whole-volume means.
- Track ERL by cell class to detect morphology-dependent blind spots.
- Maintain synapse-centric precision/recall for biologically relevant correctness.
- Require explicit uncertainty tags for unresolved defects rather than silent acceptance.

## Frequent failure modes
- Over-fixing low-impact errors:
  Prioritize corrections that materially change downstream conclusions.
- Inconsistent adjudication:
  Maintain standard operating examples for merge/split edge cases.
- Metric gaming:
  Pair global metrics with qualitative audits of biologically important structures.
- Human-fatigue drift:
  Rotate reviewers and monitor disagreement trends over time.

## Practical workflow
1. Detect candidate errors in 2D and 3D context.
2. Classify error type (merge, split, boundary ambiguity, identity confusion).
3. Correct labels and record decision rationale.
4. Validate continuity and synaptic context after correction.
5. Log quality metrics for reproducibility and team review.

## Visual training set (draft)
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S06-01.png' | relative_url }}" alt="Segmentation proofreading visual: neuronal structure orientation" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S06:</strong> orientation cue for robust proofreading context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S09-01.png' | relative_url }}" alt="Segmentation proofreading visual: synapse identification cues" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S09:</strong> synapse-oriented features relevant to correction decisions.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S11-01.png' | relative_url }}" alt="Segmentation proofreading visual: ultrastructural feature panel" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S11:</strong> vesicle and organelle cues for ambiguity resolution.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-AXDEN-S13-01.png' | relative_url }}" alt="Segmentation proofreading visual: axon versus dendrite comparison" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S13:</strong> axon-vs-dendrite differentiation for identity checks.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-AXDEN-S18-01.png' | relative_url }}" alt="Segmentation proofreading visual: edge-case process morphology" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S18:</strong> edge-case morphology for high-risk correction review.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-AXDEN-S22-01.png' | relative_url }}" alt="Segmentation proofreading visual: advanced morphology cue set" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S22:</strong> advanced cue set for difficult boundary calls.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S03-01.png' | relative_url }}" alt="Segmentation proofreading visual: method overview context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S03:</strong> method overview context for processing/QC integration.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S08-01.png' | relative_url }}" alt="Segmentation proofreading visual: graph and pipeline transition" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S08:</strong> graph/pipeline transition context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S09-01.png' | relative_url }}" alt="Segmentation proofreading visual: automated detection context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S09:</strong> automated detection context for human-machine workflows.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S10-01.png' | relative_url }}" alt="Segmentation proofreading visual: processing-stage quality context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S10:</strong> quality-relevant processing stage.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S13-01.png' | relative_url }}" alt="Segmentation proofreading visual: evaluation and metrics context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S13:</strong> evaluation/metrics context for QC reporting.</p>
  </article>
</div>

<p><small>Attribution: Pat Rivlin training materials for `RIV-*` visuals; outreach visuals from module14 lesson2 extraction. Some planned IDs were unavailable in extracted thumbnails and were replaced with nearest available alternatives.</small></p>

## Discussion prompts
- Which error types most strongly alter downstream network conclusions?
- Where should human review be mandatory, even with strong model performance?
- What QC metadata is minimally required to make proofreading decisions auditable?

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Course links
- Existing overlap: [module06]({{ '/modules/module06/' | relative_url }}), [module07]({{ '/modules/module07/' | relative_url }})
- Next unit: [09 Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})

## Quick activity
Take one candidate merge/split case and write a short correction log with before/after rationale and one QC metric.


## Draft lecture deck
- Slide draft page: [Segmentation and Proofreading deck draft]({{ '/technical-training/slides/08-segmentation-and-proofreading/' | relative_url }})
