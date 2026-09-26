---
layout: page
title: "Reconstruction Pipeline"
permalink: /content-library/infrastructure/reconstruction-pipeline/
image: /assets/images/content-library/infrastructure/reconstruction-pipeline.svg
image_alt: "Stylized vector art: pipeline stages running above a chunk grid."
description: "End-to-end connectome reconstruction: raw image ingest, alignment, segmentation, agglomeration, synapse detection and serving, with what each stage costs. Instructor script with references."
topics:
  - pipeline
  - segmentation
  - alignment
  - agglomeration
  - synapse-detection
primary_units:
  - "04"
difficulty: "Advanced"
tags:
  - infrastructure:pipeline-architecture
  - infrastructure:cloud-computing
  - infrastructure:scalability
  - connectomics:segmentation
  - connectomics:alignment
  - neuroai:agglomeration
micro_lesson_id: ml-infra-pipeline
combines_with:
  - data-formats
  - provenance-and-versioning
  - acquisition-qa
content_type: core
---

## Overview

Connectome reconstruction is a production data-engineering problem as much as a neuroscience problem. Turning petabytes of raw EM images into a queryable graph of neurons and synapses takes a chain of dependent computational stages, each with its own failure modes, quality metrics and scaling limits. This page walks through the standard pipeline used by current large projects.

---

## Instructor script: pipeline architecture

### The five-layer model

Think of the reconstruction pipeline as five layers, each transforming the data toward a higher-level representation:

```
Raw images → Aligned volume → Segmentation → Refined objects + synapses → Served graph
   (L1)          (L2)            (L3)                 (L4)                    (L5)
```

Each layer depends on the previous one, errors propagate forward, and reprocessing may require re-running everything downstream of the change.

### Layer 1: Ingest

**What happens:** Raw image tiles arrive from the microscope. Each tile is a 2D image, typically 4K×4K to 8K×8K pixels at 4-8 nm/pixel. A single section may contain hundreds to thousands of tiles. A full dataset may have thousands to tens of thousands of sections.

**Key operations:**
- **Checksum validation**: Verify data integrity during transfer from microscope to storage. A single corrupted tile can create a segmentation void.
- **Format standardization**: Convert instrument-native formats to analysis-ready formats (e.g., N5, Zarr, Neuroglancer precomputed). Store at multiple resolution levels (image pyramid) for efficient browsing and analysis.
- **Immutable archive**: Raw data is never modified. All downstream processing reads from the raw archive and writes to separate output locations. This enables reprocessing from scratch if needed.

**Scale context:** The MICrONS volume (about 1 mm³ of mouse cortex, imaged at about 4 nm per pixel in 40 nm sections) produced about 2 PB of raw imagery (MICrONS Consortium 2025). The H01 human cortex fragment is 1.8 PB of raw data and 1.4 PB as an aligned volume (Shapson-Coe et al. 2024). Storage and I/O bandwidth are first-order constraints.

### Layer 2: Alignment

**What happens:** Individual tiles are stitched into section mosaics, and consecutive sections are registered to produce a coherent 3D volume.

**Tile stitching:** Adjacent tiles overlap by 5-15%. Cross-correlation of overlapping regions determines the precise offset. Intensity normalization across tiles corrects for illumination non-uniformity.

**Section registration:** Consecutive sections are aligned using feature matching or cross-correlation. This is conceptually similar to video stabilization but with unique challenges:
- Sections are not identical — biological structures change over 25-40 nm in z.
- Mechanical distortions (compression, shearing) mean rigid alignment is insufficient; elastic (non-rigid) transformations are often needed.
- Missing or damaged sections create gaps that must be bridged.

**Methods:** Saalfeld et al. (2012) developed TrakEM2's elastic alignment for serial-section datasets. More recent approaches use learned image encodings trained with self-supervision (Mitchell et al. 2019). The key metric is registration residual — the remaining misalignment after correction, typically targeting <1 pixel (4-8 nm).

**Critical failure mode:** Accumulated alignment drift. If each section-to-section registration leaves a random residual of ~0.5 pixel, errors add like a random walk: over 10,000 sections that is about 0.5 × √10,000 = 50 pixels (~400 nm at 8 nm/pixel) of drift. A systematic bias in the same direction grows linearly and is far worse. Mitigation: anchor alignment to known structures (blood vessels, soma boundaries) and apply global optimization.

### Layer 3: Segmentation

**What happens:** Every voxel in the aligned volume is assigned to a specific object (neuron, glia, blood vessel, extracellular space, etc.). This is an instance segmentation problem — not just "this is neural tissue" but "this is neuron #47,293."

**Modern approach — two-stage pipeline:**

1. **Affinity/boundary prediction**: A convolutional neural network (typically a 3D U-Net or similar encoder-decoder architecture) predicts, for each voxel, the probability that it belongs to the same object as each of its neighbors (affinity map) or the probability that it sits on an object boundary (boundary map). Trained on manually annotated ground-truth regions.

2. **Watershed + agglomeration**: Initial over-segmentation via watershed transform on the affinity/boundary maps produces millions of small "supervoxels" — fragments that are almost certainly part of a single neuron. These supervoxels are then agglomerated (merged) based on affinity scores between adjacent supervoxels.

**Alternative approach — Flood-Filling Networks (FFN):** Januszewski et al. (2018) introduced an iterative approach where a neural network "grows" each segment by predicting which neighboring voxels belong to the same object, starting from a seed point and expanding outward (like flood-fill). FFNs produced the segmentations of the *Drosophila* hemibrain (Scheffer et al. 2020) and H01 (Shapson-Coe et al. 2024). FlyWire's segmentation came from a different pipeline (Dorkenwald et al. 2022).

**Scale challenges:** A 1 mm³ volume at 4 × 4 × 40 nm voxels holds ~1.6 × 10^15 voxels; segmentation networks often run at a coarser 8 × 8 × 40 nm, which still leaves ~4 × 10^14. Inference is distributed across many GPUs, and the GPU-hour total follows from your model's throughput (see the arithmetic below).

**Quality:** Lee et al. (2017) reported "superhuman" accuracy on the SNEMI3D benchmark, meaning their segmentation scored better than a human annotator's on that small test volume. That does not carry over to a whole volume: an error rate of even 0.1% per supervoxel, across hundreds of millions of supervoxels, leaves hundreds of thousands of errors.

### Layer 4: Post-processing and synapse detection

**Agglomeration refinement:** The initial agglomeration (Layer 3) produces objects that are mostly correct but contain merge and split errors. Post-processing refines these:

- **Size-based filtering**: Remove very small fragments (likely noise) and flag very large objects (likely merges of multiple neurons).
- **Skeleton extraction**: Convert volumetric segments to skeleton representations (medial axis trees). Enables efficient morphological analysis and error detection.
- **Mesh generation**: Create surface meshes for 3D visualization and morphometric measurements. Marching cubes or similar algorithms applied to segmentation volumes.
- **Graph extraction**: From skeletons/meshes, extract a neuron-level graph with nodes (neurons) and edges (synaptic connections).

**Synapse detection:** A separate neural network identifies synapses in the aligned volume:
- Predicts cleft locations (membrane appositions with vesicle clusters and PSD)
- Assigns pre-synaptic and post-synaptic partners based on which segments are on each side of the cleft
- Classifies synapse type (excitatory/inhibitory) based on PSD morphology and vesicle shape

The connectome graph's edges come from this step, so its errors become edge errors. [Synapse detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}) covers it in depth.

### Layer 5: Graph and serving

**What happens:** The reconstructed volume, segmentation, synapses, and graph are made available for proofreading and analysis through web APIs and visualization tools.

**Key components:**
- **Chunked volume serving**: Multiscale image pyramids served via HTTP (Neuroglancer precomputed format, CloudVolume). Enables fast browsing of petabyte-scale data.
- **Segmentation serving**: On-the-fly lookup of segment ID at any coordinate. Support for supervoxel-level queries.
- **Annotation databases**: Store synapse locations, cell-type labels, proofreading edits, and other annotations. CAVE (Dorkenwald et al. 2025) provides versioned annotation storage with materialization snapshots.
- **Graph APIs**: Query the connectome graph — "give me all neurons connected to neuron X" — without loading the entire graph.

---

## What it costs, in the units that bind

Most descriptions of reconstruction leave out what trainees most need to know:
what running the pipeline consumes. The binding
constraints are not the same at each stage, which is why "it's expensive" is
not useful planning information.

| Stage | Binding constraint | Roughly what dominates |
|---|---|---|
| **Ingest and alignment** | Wall clock and I/O | Reading and rewriting petabytes; alignment itself is cheap by comparison |
| **Boundary / affinity prediction** | **GPU time** | Every voxel passes through a network. This is where a mm³ reconstruction's compute bill is |
| **Supervoxel and agglomeration** | CPU and memory | Graph operations over billions of fragments; memory, not FLOPs |
| **Meshing and skeletonization** | CPU, embarrassingly parallel | Cheap per object, expensive because there are millions |
| **Proofreading** | **Human hours** | The most expensive input, the hardest to scale, and the one you cannot buy more of at short notice |
| **Serving** | Storage and egress | Ongoing rather than one-off; egress is what surprises people |

Two things follow. First, **GPU time and human hours are the two large numbers,
and they trade against each other**: a better segmentation costs more compute
and less proofreading. That trade is the actual design decision behind a
reconstruction pipeline, and the agglomeration threshold is the dial.

Second, **only one of those two scales by spending money.** You can rent more
GPUs this week. You cannot rent more trained proofreaders this week, and an
untrained proofreader can introduce errors faster than they fix them. That
asymmetry is why acquisition QA and segmentation quality matter so much: they
reduce demand on the input you cannot scale.

**Do the arithmetic before you commit.** Take the voxel count from Unit 03's
cost arithmetic, your model's throughput in voxels per GPU-hour, and your pilot's
measured error rate against your per-neuron proofreading time. The result is a
GPU-hour figure and a person-hour figure. If the second is larger than your
program can staff, proofreading faster will not fix it. Change the segmentation or
the acquisition, upstream, where changes are still cheap.

---

## Where the pipeline is *not* a pipeline

The five-layer model above is a batch pipeline: data flows one way and each
stage completes before the next begins. That is true right up until the first
edit, and then it stops being true.

Proofreading edits do not re-run the pipeline. They change which supervoxels are
grouped together, and that grouping lives in the ChunkedGraph, which sits
*beside* the batch pipeline rather than inside it. The consequences are the ones
that confuse people most often:

- **Supervoxels are immutable; segments are not.** An edit never changes a
  fragment, only which fragments are joined. This is what makes an edit cheap
  and reversible.
- **Root IDs change under you.** The identifier for an object is valid at a
  moment in time. Code that hardcodes one and runs six months later is querying
  a different object, silently.
- **Meshes are regenerated, not edited.** Which is why a Neuroglancer link can
  show two people different shapes at the same URL.
- **Materializations are snapshots of a moving target.** They exist so that an
  analysis can be pinned to a state that will not move, which is the only way a
  query is reproducible.

If you take one thing from this page into your own work: **the batch pipeline
produced the segmentation, but the ChunkedGraph is what you are actually
querying**, and the version you pin is a property of the second, not the first.

---

## Provenance and reproducibility

Every stage must record:

| Provenance field | Purpose |
|-----------------|---------|
| Input data version/hash | Exactly which data was processed |
| Code revision (git hash) | Which software version ran |
| Model artifact ID | Which trained model (for ML stages) |
| Parameter configuration | All hyperparameters and thresholds |
| Runtime environment | Hardware, OS, library versions |
| Output data version/hash | Fingerprint of results |

**Why this matters:** If a downstream analysis produces unexpected results, you need to trace back through the pipeline to determine whether it's a biological finding or a processing artifact. Without provenance, this is impossible.

---

## Worked example: diagnosing a connectivity anomaly

**Scenario (invented for teaching):** An analysis shows that neurons in one corner of the imaged volume have 30% fewer synaptic connections than neurons in the center.

**Diagnostic pipeline trace:**

1. **L5 (Graph):** Verify the connectivity difference is real in the graph database, not a query bug.
2. **L4 (Synapse detection):** Check synapse detection confidence scores in the two regions. Finding: synapse confidence is 15% lower in the corner.
3. **L3 (Segmentation):** Check segmentation quality. Finding: more split errors in the corner.
4. **L2 (Alignment):** Check alignment residuals. Finding: normal.
5. **L1 (Raw images):** Inspect raw image quality. Finding: membrane contrast is reduced in the corner, which lay deepest in the stained block: a staining gradient from incomplete osmium penetration.
6. **Root cause:** Staining artifact → reduced membrane detection → more split errors → missed synapses → apparent connectivity deficit.
7. **Resolution:** (a) Flag region in metadata. (b) Re-run segmentation with adjusted model threshold. (c) Prioritize proofreading in that region. (d) Report the spatial quality gradient in any publication using this data.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "Segmentation is the hard part" | Alignment errors can be just as damaging as segmentation errors | Quality is a chain; the weakest link dominates |
| "Once segmentation is done, we have a connectome" | Synapse detection, proofreading, and graph construction are separate, critical stages | Segmentation alone gives you objects, not connections |
| "Reprocessing means starting over" | Good pipeline design supports partial reprocessing — e.g., re-segment one region without re-aligning the whole volume | Design for regional rollback from the start |
| "More GPUs = faster results" | I/O bandwidth and data staging often bottleneck before compute | Profile your pipeline for I/O vs compute balance |

---

## References

- Dorkenwald S et al. (2022) "FlyWire: online community for whole-brain connectomics." *Nature Methods* 19:119-128.
- Dorkenwald S et al. (2025) "CAVE: Connectome Annotation Versioning Engine." *Nature Methods* 22:1112-1120. doi:10.1038/s41592-024-02426-z.
- Funke J et al. (2019) "Large scale image segmentation with structured loss based on deep learning for connectome reconstruction." *IEEE Transactions on Pattern Analysis and Machine Intelligence* 41(7):1669-1680.
- Januszewski M et al. (2018) "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods* 15(8):605-610.
- Lee K et al. (2017) "Superhuman accuracy on the SNEMI3D connectomics challenge." *arXiv:1706.00120*.
- MICrONS Consortium (2025) "Functional connectomics spanning multiple areas of mouse visual cortex." *Nature* 640:435-447. doi:10.1038/s41586-025-08790-w.
- Mitchell E, Keselj S, Popovych S, Buniatyan D, Seung HS (2019) "Siamese encoding and alignment by multiscale learning with self-supervision." *arXiv:1904.02643*.
- Saalfeld S et al. (2012) "Elastic volume reconstruction from series of ultra-thin microscopy sections." *Nature Methods* 9(7):717-720.
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384:eadk4858.
- Turner NL et al. (2022) "Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity." *Cell* 185(6):1082-1100.
