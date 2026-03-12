---
layout: page
title: "03 EM Prep and Imaging"
permalink: /technical-training/03-em-prep-and-imaging/
slug: 03-em-prep-and-imaging
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
---

## Why this unit
Acquisition quality sets the upper bound on downstream reconstruction quality.

## Technical scope
This unit covers the acquisition chain from tissue handling to image stack generation, emphasizing how preparation and imaging decisions create specific artifact profiles that propagate into segmentation, proofreading, and analysis.

## Learning goals
- Explain practical EM prep/imaging stages.
- Identify artifact classes that impact segmentation and proofreading.
- Build an acquisition QA checklist tied to downstream reconstruction risk.

## Core technical anchors
- Fixation/staining/sectioning/imaging chain.
- Throughput-volume-resolution tradeoffs.
- Provenance and acquisition QA.

## Visual context set
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/03-em-prep-and-imaging/FIG-SRC-MODULE12_LESSON3-S04-01.png' | relative_url }}" alt="High-resolution imaging context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L3 S04:</strong> high-resolution imaging context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/03-em-prep-and-imaging/FIG-SRC-MODULE12_LESSON3-S08-01.png' | relative_url }}" alt="High-throughput sectioning context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L3 S08:</strong> high-throughput sectioning context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/03-em-prep-and-imaging/FIG-SRC-MODULE12_LESSON3-S10-01.png' | relative_url }}" alt="Imaging pipeline transition visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L3 S10:</strong> imaging-to-pipeline transition.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/03-em-prep-and-imaging/FIG-SRC-MODULE13_LESSON2-S08-01.png' | relative_url }}" alt="Manual versus automated context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module13 L2 S08:</strong> manual vs automated context.</p>
  </article>
</div>

<p><small>Attribution: assets_outreach source decks (historical/context visuals).</small></p>

## Method deep dive: acquisition pipeline
1. Tissue preparation:
   Stabilize ultrastructure while minimizing shrinkage and extraction artifacts.
2. Contrast generation:
   Heavy-metal staining protocol chosen for membrane and synapse visibility.
3. Sectioning or block-face strategy:
   Balance section integrity, throughput, and z-consistency.
4. Imaging:
   Set dwell time, beam current, and tile overlap for contrast/SNR versus acquisition speed.
5. Stitching and stack assembly:
   Correct tile seams, monitor drift, and preserve metadata for every transform.

## Artifact taxonomy and downstream impact
- Knife chatter / section compression:
  Induces false boundaries and continuity breaks.
- Charging / uneven contrast:
  Destabilizes model confidence and raises false split rates.
- Fold, tear, missing section:
  Produces non-recoverable topology gaps unless bridged with explicit uncertainty.
- Misalignment drift:
  Creates false branch points and synapse mislocalization.

## Quantitative QA gates
- Per-tile intensity distribution and SNR monitoring.
- Seam visibility rate and residual alignment error distributions.
- Missing/damaged section rate with flagged coordinate intervals.
- Pilot segmentation score before full-volume ingestion.

## Failure modes and mitigation
- Late QA discovery:
  Run small pilot reconstructions early; do not wait until full acquisition completes.
- Metadata gaps:
  Require machine-readable acquisition logs (instrument settings, timestamps, operator notes).
- Throughput bias:
  Avoid sacrificing contrast consistency for speed without measuring downstream penalty.
- Non-localized QA:
  Report quality per region/tile group instead of global averages only.

## Course links
- Existing overlap: [module05]({{ '/modules/module05/' | relative_url }})
- Next unit: [04 Volume Reconstruction Infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})

## Practical workflow
1. Specify target structures and required resolution.
2. Choose prep/imaging strategy compatible with that target.
3. Anticipate artifact classes and mitigation checkpoints.
4. Capture acquisition metadata for downstream reproducibility.

## Discussion prompts
- Which imaging artifact has the highest downstream cost in your workflow?
- Where should imaging QA gates be mandatory before reconstruction proceeds?

## Mini-lab
Create an acquisition risk register with:
1. Three likely artifacts for your target tissue.
2. Detection metric for each artifact.
3. Mitigation action and escalation trigger.
4. Expected effect on segmentation precision/recall if unresolved.

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Identify one likely imaging artifact in a sample dataset and describe how it could affect segmentation quality.


## Teaching slide deck
- Slide draft page: [EM Prep and Imaging deck draft]({{ '/technical-training/slides/03-em-prep-and-imaging/' | relative_url }})
