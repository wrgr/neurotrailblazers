---
layout: page
title: "04 Volume Reconstruction Infrastructure"
permalink: /technical-training/04-volume-reconstruction-infrastructure/
slug: 04-volume-reconstruction-infrastructure
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
---

## Why this unit
Reconstruction at connectome scale is a systems-engineering problem: alignment, storage, compute, orchestration, and reliability.

## Technical scope
This unit treats connectome reconstruction as a production data platform problem: ingest, alignment, segmentation orchestration, object storage/indexing, provenance, and reproducible reprocessing.

## Learning goals
- Describe architecture layers for large-volume reconstruction.
- Evaluate throughput, cost, and reproducibility tradeoffs.
- Design an end-to-end pipeline with explicit reliability and rollback strategy.

## Core technical anchors
- Stitching/alignment/normalization pipelines.
- Multiresolution storage and APIs.
- Provenance/versioning and recovery workflows.

## Visual context set
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/04-volume-reconstruction-infrastructure/FIG-SRC-MODULE14_LESSON1-S04-01.png' | relative_url }}" alt="High-level architecture visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L1 S04:</strong> high-level architecture context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/04-volume-reconstruction-infrastructure/FIG-SRC-MODULE14_LESSON1-S07-01.png' | relative_url }}" alt="Workflow API integration visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L1 S07:</strong> workflow/API integration context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/04-volume-reconstruction-infrastructure/FIG-SRC-MODULE14_LESSON1-S12-01.png' | relative_url }}" alt="Service decomposition visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L1 S12:</strong> service decomposition context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/04-volume-reconstruction-infrastructure/FIG-SRC-MODULE13_LESSON1-S08-01.png' | relative_url }}" alt="Scalable analytics context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module13 L1 S08:</strong> scalable analytics context.</p>
  </article>
</div>

<p><small>Attribution: assets_outreach source decks (historical/context visuals).</small></p>

## Reference architecture
1. Ingest layer:
   Tile validation, checksum tracking, and immutable raw archive.
2. Transform layer:
   Stitching/alignment/normalization jobs with versioned parameter sets.
3. Inference layer:
   Segmentation/synapse models executed with tracked model hashes and runtime config.
4. Post-processing layer:
   Agglomeration, mesh/skeleton generation, and graph extraction.
5. Serving layer:
   Chunked multiscale volumes plus query APIs for analysis/proofreading.

## Operational design details
- Orchestration:
  Queue-based jobs with retry policies and idempotent stage outputs.
- Data layout:
  Chunking strategy optimized separately for proofreading traversal and analysis queries.
- Versioning:
  Every stage writes lineage metadata (input IDs, code revision, params, model artifact ID).
- Reprocessing:
  Support partial invalidation (region-level) rather than full rerun by default.

## Quantitative SLOs and QC
- Throughput SLO:
  Target ingest/inference rates needed to meet project timeline.
- Reliability SLO:
  Failure/retry rate and mean time to recovery per stage.
- Quality SLO:
  Segmentation and synapse metrics tracked per release candidate.
- Cost envelope:
  Compute and storage cost per cubic micron/cubic millimeter equivalent.

## Failure modes and mitigation
- Hidden non-determinism:
  Pin dependency versions and random seeds in production jobs.
- Provenance drift:
  Reject outputs that do not include required lineage fields.
- Hotspot bottlenecks:
  Monitor I/O and index saturation; rebalance chunking/index strategy.
- Unbounded reprocessing:
  Implement region-scoped rollback and patch releases.

## Course links
- Existing overlap: [module12]({{ '/modules/module12/' | relative_url }}), [module18]({{ '/modules/module18/' | relative_url }})
- Next unit: [05 Neuronal Ultrastructure]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }})

## Practical workflow
1. Define throughput and quality targets.
2. Design ingest/alignment/storage components against those targets.
3. Add versioning and provenance at each transform stage.
4. Validate failure handling and reprocessing paths.

## Discussion prompts
- Which architecture choices most improve reproducibility?
- What tradeoffs are acceptable between latency, cost, and fidelity?

## Mini-lab
Draft a pipeline release plan that includes:
1. Stage diagram with inputs/outputs.
2. Three required provenance fields at each stage.
3. Rollback strategy for a bad agglomeration release.
4. One dashboard view with throughput, quality, and cost metrics.

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Sketch a 4-stage reconstruction pipeline and mark where you would enforce provenance/version checkpoints.


## Content library references
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) — Full five-layer architecture: ingest, alignment, segmentation, post-processing, serving
- [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) — Volumes, meshes, skeletons, graphs; format specs and tradeoffs
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) — CAVE materialization, pipeline lineage, reproducible reprocessing

## Teaching slide deck
- Slide draft page: [Volume Reconstruction Infrastructure deck draft]({{ '/technical-training/slides/04-volume-reconstruction-infrastructure/' | relative_url }})
