---
layout: page
title: "02 Brain Data Across Scales"
permalink: /technical-training/02-brain-data-across-scales/
slug: 02-brain-data-across-scales
---

## Why this unit
Technical decisions depend on scale. Data representation, compute cost, and biological interpretation all shift from macroscale to ultrastructure.

## Technical scope
This unit covers cross-scale reasoning from mesoscale maps to nanometer-resolution EM, including representation changes, registration assumptions, and how scale selection constrains valid biological claims.

## Learning goals
- Separate modality scale from analysis scale.
- Plan scale-aware workflows and questions.
- Select a minimal sufficient scale for a target hypothesis and justify tradeoffs.

## Core technical anchors
- Registration and coordinate consistency.
- Resolution anisotropy risks.
- Volumes, meshes, skeletons, and graphs as scale-dependent representations.

## Visual context set (draft)
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON1-S06-01.png' | relative_url }}" alt="Scale and voxel-size context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L1 S06:</strong> scale/voxel context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON2-S04-01.png' | relative_url }}" alt="Macroscale pipeline visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L2 S04:</strong> macroscale pipeline view.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON2-S05-01.png' | relative_url }}" alt="Microscale bridge visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L2 S05:</strong> microscale/preprocessing bridge.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON3-S08-01.png' | relative_url }}" alt="High-throughput imaging context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L3 S08:</strong> high-throughput imaging context.</p>
  </article>
</div>

<p><small>Attribution: assets_outreach source decks (historical/context visuals).</small></p>

## Scale-aware data model
- Acquisition scale:
  Voxel size, field of view, modality physics, contrast mechanism.
- Reconstruction scale:
  Objects that can be reliably segmented (organelles, neurites, cells, tracts).
- Analysis scale:
  Features extracted (motifs, cell-type distributions, connectivity statistics).
- Decision rule:
  Choose the lowest-cost scale that still resolves all structures needed for your endpoint metric.

## Method deep dive: cross-scale linkage
1. Define anchor points across scales (landmarks, vasculature, layer boundaries, atlas coordinates).
2. Register with transform provenance (rigid, affine, non-linear) and uncertainty estimates.
3. Track anisotropy explicitly; avoid isotropic assumptions on anisotropic stacks.
4. Build representations per stage:
   - Volumes for raw inspection and alignment.
   - Segmentations for object identity.
   - Skeletons/meshes for morphology.
   - Graphs for connectivity analysis.
5. Propagate confidence across transforms so downstream users can see where uncertainty grows.

## Quantitative quality gates
- Registration residuals reported per region, not only global averages.
- Sampling bias check across laminae/regions/cell classes.
- Representation fidelity checks (skeleton branch loss, mesh topology errors, graph edge uncertainty).
- Compute budget tracking: storage growth, I/O bottlenecks, query latency by scale.

## Failure modes and mitigation
- Scale leakage:
  Drawing fine-grained mechanistic conclusions from coarse data.
- Over-registration confidence:
  Treating warped alignments as ground truth without local residual checks.
- Representation collapse:
  Losing biologically relevant geometry during conversion to graph-only formats.
- Cost underestimation:
  Ignoring downstream storage/index/query expansion when moving to higher resolution.

## Course links
- Existing overlap: [module04]({{ '/modules/module04/' | relative_url }}), [module05]({{ '/modules/module05/' | relative_url }}), [module12]({{ '/modules/module12/' | relative_url }})
- Next unit: [03 EM Prep and Imaging]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})

## Practical workflow
1. Define the target biological question.
2. Select modality/scale that can resolve needed features.
3. Estimate compute/storage implications.
4. Plan cross-scale linkage and provenance.

## Discussion prompts
- What is lost and gained when moving across scales?
- Which cross-scale assumptions most often fail in practice?

## Mini-lab
Given a candidate question ("How cell-type-specific is local recurrent connectivity?"), produce:
1. Required observable structures.
2. Minimum voxel resolution and volume coverage.
3. Registration strategy and validation metric.
4. Final analysis representation and one expected bottleneck.

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Pick a research question and propose the minimum data scale needed to answer it, including one tradeoff you accept.


## Draft lecture deck
- Slide draft page: [Brain Data Across Scales deck draft]({{ '/technical-training/slides/02-brain-data-across-scales/' | relative_url }})
