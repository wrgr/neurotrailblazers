---
layout: page
title: "06 Axons and Dendrites"
permalink: /technical-training/06-axons-and-dendrites/
slug: 06-axons-and-dendrites
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
---

## Why this unit
Process-type misclassification is a major source of downstream graph error.

## Learning goals
- Distinguish axons and dendrites with morphology + organelle cues.
- Handle ambiguous edge cases with confidence scoring and continuity checks.

## Core technical anchors
- Combined cue strategy: morphology, organelles, local connectivity.
- Edge cases: en passant boutons, thin dendrites, truncations.
- Auditability via confidence and correction logs.

## Method deep dive: axon-vs-dendrite classification
1. Morphology pass:
   Branch caliber, tortuosity, spine presence, and process tapering.
2. Organelle pass:
   Vesicle clustering, microtubule patterning, mitochondrial distribution.
3. Connectivity pass:
   Input/output pattern and bouton/spine relationships in neighborhood.
4. Continuity pass:
   Validate interpretation along additional slices and branch points.
5. Decision logging:
   Capture confidence and alternative hypothesis if ambiguous.

## Quantitative QA checkpoints
- Confusion matrix for axon/dendrite labels against adjudicated truth set.
- Error concentration map by tissue region and annotator.
- Rework fraction: percent of labels reversed during secondary review.
- Downstream sensitivity: impact of class errors on motif counts and graph metrics.

## Frequent failure modes
- Thin dendrites mislabeled as axons:
  Add local synaptic-role evidence before finalizing.
- Truncated field-of-view bias:
  Mark as provisional when continuity evidence is missing.
- Bouton-centric bias:
  Avoid relying only on vesicle presence without full context.
- Inconsistent team criteria:
  Calibrate weekly with shared edge-case panels.

## Visual training set
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S01-01.png' | relative_url }}" alt="Axon/dendrite training visual: orientation" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S01:</strong> orientation figure for process-type comparison.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S08-01.png' | relative_url }}" alt="Axon/dendrite training visual: dendritic morphology cue" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S08:</strong> dendrite-focused morphology cue.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S11-01.png' | relative_url }}" alt="Axon/dendrite training visual: classification cue" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S11:</strong> process classification cue in dense context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S13-01.png' | relative_url }}" alt="Axon/dendrite training visual: side-by-side comparison" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S13:</strong> side-by-side axon/dendrite comparison panel.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S14-01.png' | relative_url }}" alt="Axon/dendrite training visual: advanced cue set" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S14:</strong> advanced feature set for ambiguity handling.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S18-01.png' | relative_url }}" alt="Axon/dendrite training visual: edge-case morphology" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S18:</strong> edge-case morphology requiring multi-cue interpretation.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S22-01.png' | relative_url }}" alt="Axon/dendrite training visual: high-complexity cue" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S22:</strong> high-complexity proofreading cue.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S23-01.png' | relative_url }}" alt="Axon/dendrite training visual: late-stage synthesis example" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S23:</strong> synthesis example for final class assignment.</p>
  </article>
</div>

<p><small>Attribution: Pat Rivlin training materials (MICrONS proofreading deck). Some manifest-listed IDs used in planning (`S04`, `S06`, `S10`, `S16`) were not present in extracted thumbnails and were replaced with available neighboring cues.</small></p>

## Course links
- Existing overlap: [module04]({{ '/modules/module04/' | relative_url }}), [module09]({{ '/modules/module09/' | relative_url }})
- Next unit: [07 Glia]({{ '/technical-training/07-glia/' | relative_url }})

## Practical workflow
1. Start with morphology cues.
2. Add organelle and synaptic-context checks.
3. Verify continuity in neighboring sections.
4. Assign class with confidence and review note.

## Discussion prompts
- Which edge cases most frequently produce classifier disagreement?
- How should teams calibrate confidence thresholds for class assignments?

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Choose one ambiguous process and document the three strongest cues you used to classify it.


## Content library references
- [Axon-dendrite classification]({{ '/content-library/cell-types/axon-dendrite-classification/' | relative_url }}) — Multi-cue protocol, edge cases, confidence scoring
- [Axon biology]({{ '/content-library/neuroanatomy/axon-biology/' | relative_url }}) — AIS, boutons, vesicle pools, myelination
- [Dendrite biology]({{ '/content-library/neuroanatomy/dendrite-biology/' | relative_url }}) — Spine types, local translation, organelle gradients
- [Organelle annotation cues]({{ '/content-library/neuroanatomy/organelle-cues/' | relative_url }}) — Using organelles to resolve ambiguous compartments
- [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) — Morphological and connectivity-based classification

## Teaching slide deck
- Slide draft page: [Axons and Dendrites deck draft]({{ '/technical-training/slides/06-axons-and-dendrites/' | relative_url }})
