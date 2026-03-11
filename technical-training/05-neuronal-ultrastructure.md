---
layout: page
title: "05 Neuronal Ultrastructure"
permalink: /technical-training/05-neuronal-ultrastructure/
slug: 05-neuronal-ultrastructure
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
---

## Why this unit
Ultrastructure is the operational visual language of connectomics annotation and quality control.

## Learning goals
- Identify core neuronal ultrastructural features in EM data.
- Apply context-aware interpretation with explicit uncertainty.

## Core technical anchors
- Compartments: soma, dendrite, axon, bouton, spine.
- Cues: vesicles, PSD/active zone, mitochondria, ER, microtubules.
- Multi-slice context before final annotation decisions.

## Method deep dive: compartment-level decision protocol
1. Start with local geometry (diameter changes, branching pattern, cytoplasmic density).
2. Add organelle evidence (microtubule organization, mitochondria morphology, vesicle fields).
3. Evaluate synaptic architecture (active zone alignment, vesicle clusters, PSD profile).
4. Confirm continuity across adjacent sections before committing label.
5. Assign confidence tier (`high`, `medium`, `uncertain`) with rationale.

## Quantitative QA checkpoints
- Inter-annotator agreement on compartment labels.
- Synapse call precision/recall on a gold-standard subset.
- Uncertain-label rate by region as an indicator of dataset difficulty.
- Turnaround time per corrected ambiguity (captures workflow scalability).

## Frequent failure modes
- Single-slice overconfidence:
  Resolve only after short z-stack review.
- Organelle misread due to staining variability:
  Use multi-cue voting instead of one-feature decisions.
- False synapse positives in noisy contrast:
  Require structural context around candidate cleft.
- Label drift across long neurite paths:
  Enforce periodic consistency checks during tracing.

## Visual training set (draft)
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S04-01.png' | relative_url }}" alt="Ultrastructure training visual: neuron structure overview" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S04:</strong> neuron-structure overview for compartment grounding.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S08-01.png' | relative_url }}" alt="Ultrastructure training visual: dendritic context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S08:</strong> dendritic ultrastructure context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S09-01.png' | relative_url }}" alt="Ultrastructure training visual: synapse cues" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S09:</strong> synapse-identification cue set.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S10-01.png' | relative_url }}" alt="Ultrastructure training visual: vesicle and organellar detail" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S10:</strong> vesicle and organellar features relevant to annotation.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S14-01.png' | relative_url }}" alt="Ultrastructure training visual: comparative panel" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S14:</strong> comparative ultrastructure panel.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S20-01.png' | relative_url }}" alt="Ultrastructure training visual: ambiguity case" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S20:</strong> ambiguity case for context-aware interpretation.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S24-01.png' | relative_url }}" alt="Ultrastructure training visual: advanced structural example" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S24:</strong> advanced structural example for review.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S30-01.png' | relative_url }}" alt="Ultrastructure training visual: synthesis panel" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S30:</strong> synthesis panel for final interpretation checks.</p>
  </article>
</div>

<p><small>Attribution: Pat Rivlin training materials (MICrONS proofreading deck).</small></p>

## Course links
- Existing overlap: [module04]({{ '/modules/module04/' | relative_url }}), [module09]({{ '/modules/module09/' | relative_url }}), [module11]({{ '/modules/module11/' | relative_url }})
- Next unit: [06 Axons and Dendrites]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }})

## Practical workflow
1. Localize candidate compartment and neighborhood context.
2. Evaluate ultrastructural cues across adjacent slices.
3. Assign provisional interpretation with confidence level.
4. Escalate ambiguous cases for secondary review.

## Discussion prompts
- Which ultrastructural cues are most robust across annotators?
- Where should uncertainty remain explicit rather than forced to a hard label?

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Using one training image, label at least three ultrastructural cues and state your confidence for each interpretation.


## Draft lecture deck
- Slide draft page: [Neuronal Ultrastructure deck draft]({{ '/technical-training/slides/05-neuronal-ultrastructure/' | relative_url }})
