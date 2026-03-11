---
layout: page
title: "01 Why Map the Brain"
permalink: /technical-training/01-why-map-the-brain/
slug: 01-why-map-the-brain
track: core-concepts-methods
pathways:
  - technical foundation
  - conceptual framing
---

## Why this unit
Connectomics turns a broad scientific goal into a measurable technical program: map structure to generate testable hypotheses about function.

## Technical scope
This unit defines what questions connectomics can answer, what it cannot answer alone, and how to convert biological motivation into a tractable reconstruction-and-analysis plan. The focus is on hypothesis framing, measurement targets, and evidentiary boundaries.

## Learning goals
- Explain why structural maps matter for neuroscience and AI.
- Distinguish motivation from overclaim (structure informs, not alone explains, function).
- Write a technically testable connectomics question with measurable outputs.

## Core technical anchors
- Circuit topology as a hypothesis engine.
- Comparative and developmental mapping.
- AI transfer through constraints and priors, not direct emulation.

## Visual context set (draft)
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-21_02388_X_TECHTALK_-S10-01.png' | relative_url }}" alt="Motivating question visual for why map the brain" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Techtalk S10:</strong> motivating question framing.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-21_02388_X_TECHTALK_-S11-01.png' | relative_url }}" alt="Brain data framing visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Techtalk S11:</strong> brain-data framing context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-21_02388_X_TECHTALK_-S12-01.png' | relative_url }}" alt="Reverse engineering analogy visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Techtalk S12:</strong> reverse-engineering analogy and limits.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-MODULE12_LESSON1-S04-01.png' | relative_url }}" alt="Course motivation context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L1 S04:</strong> motivation and scope framing.</p>
  </article>
</div>

<p><small>Attribution: neuroAI and outreach source decks (historical/context visuals).</small></p>

## Method deep dive: from question to measurable endpoint
1. Start with a mechanistic question that has a structural signature (for example: recurrent microcircuit enrichment, axon targeting bias, cell-type-specific fan-in/fan-out).
2. Define measurement units before touching data: synapse counts, motif frequencies, path lengths, compartment-targeting ratios, spatial gradients.
3. Specify required reconstruction completeness (cell fragments, neurite-level, or near-complete local circuit) and acceptable error bounds.
4. Choose inferential frame:
   - Descriptive atlas output.
   - Hypothesis test against null models.
   - Comparative analysis across developmental stage/species/condition.
5. Pre-register interpretation limits: structure can constrain possible computations, but does not by itself establish dynamic causal function.

## Quantitative quality gates
- Annotation agreement: inter-rater agreement target for key labels before scaling.
- Reconstruction quality: minimum edge precision/recall requirements for the downstream claim type.
- Statistical validity: correction for multiple motif tests and transparent null-model choice.
- External validity: explicit statement of sampled region/species/age limits.

## Failure modes and mitigation
- Vague question framing:
  Convert broad goals ("understand intelligence") into measurable structural hypotheses.
- Claim inflation:
  Require each conclusion to cite both supporting metric and missing evidence.
- Metric mismatch:
  Avoid using graph-level summary metrics when the hypothesis is local microcircuit-specific.
- Dataset mismatch:
  Confirm acquisition scale and completeness actually support the claim.

## Course links
- Existing module overlap: [module01]({{ '/modules/module01/' | relative_url }})
- Next unit: [02 Brain Data Across Scales]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }})

## Practical workflow
1. Start with a concrete biological question.
2. Identify what structural evidence could constrain that question.
3. Map required data scale and workflow dependencies.
4. Define limits of interpretation before drawing conclusions.

## Discussion prompts
- What makes a brain-mapping goal technically actionable rather than aspirational?
- Where are the strongest boundaries between structural and functional claims?

## Mini-lab
Draft one connectomics study brief with:
1. Biological question.
2. Structural measurements (at least three).
3. Dataset requirements (resolution, volume, completeness).
4. One null model and one key confound.
5. One non-supported claim you will explicitly avoid.

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Write one 2-3 sentence hypothesis that could be constrained by structural connectivity, and list one limitation of using structure alone.


## Draft lecture deck
- Slide draft page: [Why Map the Brain deck draft]({{ '/technical-training/slides/01-why-map-the-brain/' | relative_url }})
