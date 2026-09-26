---
layout: page
title: "MICrONS Visual Cortex"
permalink: /content-library/case-studies/microns-visual-cortex/
image: /assets/images/content-library/case-studies/microns-visual-cortex.svg
image_alt: "Stylized vector art: a specimen ring with landmark points beside a data band."
description: >
  Case study of MICrONS (Machine Intelligence from Cortical Networks), which
  paired two-photon calcium imaging of about 75,000 excitatory neurons with an
  electron microscopy reconstruction of about 1 mm³ of the same mouse's visual
  cortex, so that activity and synaptic wiring could be compared cell by cell.
topics:
  - functional connectomics
  - mouse visual cortex
  - calcium imaging
  - multi-modal neuroscience
  - structure-function correlation
  - deep learning segmentation
  - cortical circuitry
primary_units:
  - "01"
  - "03"
  - "08"
  - "09"
difficulty: intermediate
tags:
  - case-studies:MICrONS
  - connectomics:dense-reconstruction
  - connectomics:functional-connectomics
  - imaging:electron-microscopy
  - imaging:calcium-imaging
  - cell-types:pyramidal-cell
  - cell-types:interneuron
  - neuroanatomy:visual-cortex
  - methodology:structure-function
micro_lesson_id: ml-case-microns
combines_with:
  - h01-human-cortex
  - mouseconnects-himc
  - flywire-whole-brain
use_layout_hero: false
content_type: core
---

# MICrONS Visual Cortex

> ### Before you quote a number from this page
>
> Every figure below (cell counts, synapse counts, volume sizes, proofreading
> coverage) is a property of **a particular release** of this dataset, not of
> the tissue. Releases are re-segmented, re-proofread and re-materialized, and
> the numbers move when they are.
>
> This page deliberately does not pin a version, because it would be stale
> within months and you would inherit a wrong number with a citation attached.
> Treat what follows as orientation. Before any figure reaches a paper, a talk,
> or a grant, pull it yourself from the release you are analyzing and record the
> version alongside it. [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
> covers how; [Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
> has the lab.


## Overview

The Machine Intelligence from Cortical Networks (MICrONS) program built a
millimeter-scale connectome of mouse visual cortex and paired it with functional
recordings from the same tissue. It was funded by the Intelligence Advanced Research
Projects Activity (IARPA) as part of the BRAIN Initiative. Its question was short:
does the way neurons are wired predict what they do?

The volume is about 1 mm³ of one male mouse's visual cortex (1.3 × 0.87 × 0.82 mm in
vivo), centered on the junction of primary visual cortex (V1) and three higher visual
areas (LM, AL and RL). It was imaged at about 4 nm per pixel in sections 40 nm thick.
The reconstruction contains more than 200,000 cells and about 524 million synapses
(MICrONS Consortium 2025). Before the tissue was prepared for electron microscopy,
about 75,000 excitatory neurons in the same volume were recorded with two-photon
calcium imaging while the mouse was alive. Recording activity first and mapping the
wiring afterwards is what the field calls "functional connectomics", and MICrONS is
its largest published example.


## The Multi-Modal Approach: Why It Matters

### The Core Insight

Traditional connectomics provides a wiring diagram: neuron A connects to neuron B with
N synapses. Traditional systems neuroscience provides functional descriptions: neuron A
responds to vertical bars moving leftward. These two descriptions live in different
worlds. MICrONS bridged them by ensuring that the same physical neurons appear in both
the functional recordings and the EM reconstruction.

That makes a new kind of analysis possible: given that neuron A prefers vertical gratings and neuron B prefers horizontal
gratings, are they more or less likely to be synaptically connected than a random pair?
Do neurons with similar tuning properties form preferential subnetworks? Does
connectivity predict correlated activity?

### Two-Photon Calcium Imaging

Before EM preparation, the head-fixed mouse viewed natural movies and parametric
stimuli (including the directional "Monet2" noise stimulus) while neural activity was
recorded with two-photon microscopy. The mouse expressed the calcium indicator GCaMP6s
in excitatory neurons. Fourteen scans, collected between postnatal days 75 and 81,
captured responses from approximately 75,000 neurons across the depths accessible to
two-photon imaging.

From these recordings, neurons can be characterized by properties such as:

- **Orientation and direction selectivity**: Preferred direction of moving stimuli.
- **Reliability**: Consistency of responses across stimulus repetitions.
- **Signal correlations**: Similarity of stimulus-driven responses with other neurons.
- **Noise correlations**: Shared trial-to-trial variability with other neurons.

### Co-Registration Challenge

Matching neurons between in vivo calcium imaging and post-mortem EM volumes is a
hard registration problem. The tissue undergoes dehydration, embedding, and
sectioning for EM, which introduces distortions. The MICrONS team fit a transform
between the two coordinate frames from 2,934 expert-matched fiducials (1,994 somata
and 942 blood-vessel points) in the two-photon structural stack and the EM volume.
The average residual was 3.8 µm. Experts then used that transform to match 19,181
functional ROIs to 15,439 EM neurons by hand (MICrONS Consortium 2025). Every
structure-function result rests on these matches, so a matching error becomes an
analysis error.


## Technical Pipeline

### EM Acquisition

The EM data was acquired by serial-section transmission electron microscopy. The tissue
block was cut into 27,972 sections at a nominal thickness of 40 nm, collected onto
GridTape, and imaged at about 4 nm pixel resolution by a fleet of five automated TEMs
(autoTEMs). Imaging took about six months and produced about 2 PB of raw imagery
(MICrONS Consortium 2025).

Key technical challenges included:

- **Section loss and damage**: Inevitable imperfections in ultramicrotomy result in
  occasional lost or damaged sections. The pipeline had to handle gaps in the z-stack
  without catastrophic segmentation failures.
- **Stitching**: Each section was imaged as a mosaic of overlapping tiles that must be
  aligned both within-section (x-y stitching) and between-section (z alignment).
- **Contrast and noise**: TEM imaging at high throughput requires balancing acquisition
  speed with signal quality.

### Segmentation

Neuron segmentation used convolutional neural networks that predict affinities
between neighboring voxels, followed by mean-affinity agglomeration of the resulting
over-segmented fragments. It ran on the aligned volume at 8 × 8 × 40 nm, not the 4 nm
imaging resolution.

### Synapse Detection

Synapses were detected using a separate deep learning model trained to identify the
characteristic ultrastructural features of chemical synapses: presynaptic vesicle
clouds, synaptic clefts, and postsynaptic densities. The model produced both the
location and the directionality (pre vs. post) of each synapse, enabling construction
of a directed connectivity graph. Against 8,611 hand-annotated synapses, the paper
reports 96% precision and 89% recall for detection.

### Proofreading and CAVE

Proofreading used the ChunkedGraph system, now part of CAVE (Connectome Annotation
Versioning Engine), with a modified Neuroglancer as the browser interface. The
released segmentation contains all 1,046,656 proofreading edits made up to
16 September 2024 (MICrONS Consortium 2025). That is a large number, but the volume
has not been exhaustively proofread. Proofreaders targeted neurons that particular
analyses needed, especially those with matched functional data.


## Key Scientific Findings

### Structure-Function Correlations (Ding et al. 2025)

The headline structure-function result from the full MICrONS volume, reported by Ding
et al. in *Nature* (2025), is a "like-to-like" wiring rule: excitatory neurons with
similar response properties are preferentially connected.

Key results include:

- **Like-to-like connectivity generalizes.** Earlier work in mouse V1 had shown that
  excitatory neurons with similar response properties are more likely to be connected.
  Ding et al. found this preference within and across layers and areas, including
  feedback connections. Using a model of each neuron's responses, they found that
  *what* a neuron responds to predicts fine-scale connections beyond axon-dendrite
  proximity, while *where* its receptive field sits does not.

- **The rule is statistical, not deterministic.** A preference does not mean every
  connected pair is functionally similar. Connectivity also depends on factors such as
  physical proximity, laminar position, and cell type, so functional similarity is one
  factor among several.

- **The earlier pilot.** Turner et al. (2022) reconstructed a smaller layer 2/3 volume
  from an earlier phase of the project. They reported that pyramidal cells receiving
  more connections from nearby cells had stronger and more reliable visual responses.

### Pyramidal Cell Morphometry

The MICrONS dataset supports large-scale quantitative analysis of cortical pyramidal
cell morphology. Measurements such as dendritic arbor extent, spine density, axonal
branching patterns, and soma size can be compared across layers and areas.

### Inhibitory Circuitry

Inhibitory interneurons, roughly 15–20% of cortical neurons, were analyzed in detail. Different interneuron classes (basket cells, chandelier cells,
Martinotti cells, and others) showed distinct targeting: basket cells preferentially
target the perisomatic region of pyramidal cells, while Martinotti cells target distal
dendrites. Schneider-Mizell et al. (2025) mapped the connectivity of all inhibitory
neurons in a densely segmented column of 1,352 cells, and identified a class of
disinhibitory specialist that targets basket cells.

### Connectivity Motifs

Analysis of small network motifs (patterns of connectivity among groups of 3-4
neurons) asks whether patterns such as reciprocal connections, chains, and convergent
inputs occur more or less often than a null model predicts. A dataset of this size lets
you test such questions directly, but the answer depends on the null model and on how
well the neurons involved are proofread.


## Data Access

The MICrONS dataset is publicly available through several channels:

- **MICrONS Explorer (microns-explorer.org)**: A web portal providing interactive
  browsing of the EM volume, segmentation, and connectivity data through Neuroglancer.

- **CAVE Client (caveclient Python package)**: Programmatic access to the segmentation,
  synapse tables, and annotation layers. The volume was processed as two subvolumes
  because the block had to be re-trimmed and the knife changed: `minnie65` (about 65% of
  the sections; the subvolume most proofreading targeted, served as `minnie65_public`)
  and `minnie35` (the remaining ~35%). The names count sections, not neurons.

- **Cloud storage**: Raw EM imagery and derived data products are hosted on cloud
  infrastructure for bulk download.

### Working with the Data

Typical analysis workflows involve:

1. Querying the CAVE client for neurons of interest (by cell type, layer, or region).
2. Retrieving synapse tables to construct connectivity matrices.
3. Matching EM-identified neurons to their functional signatures from the calcium
   imaging dataset.
4. Computing structure-function metrics (e.g., correlation between connectivity
   strength and signal correlation).

The dataset's size (approximately 2 PB) means that most researchers work with derived
data products (segmentations, synapse tables, skeleton representations) rather than
raw imagery.


## Challenges and Lessons

### Scale and Computational Demands

Segmenting a volume imaged as 2 PB of raw data took large-scale GPU compute, and
synapse detection added more. Proofreading, even when targeted, ran to more than a
million edits. The paper does not publish a person-years figure for that effort, so
do not quote one. [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }})
shows how to estimate the compute and human hours for a volume of your own.

### The Limits of a Single Volume

A 1 mm³ volume captures only a tiny fraction of the mouse brain. Axons frequently exit
the volume, meaning that long-range connections are truncated. This limits analysis to
local circuitry and prevents a full accounting of each neuron's input-output
relationships. Future projects (such as MouseConnects) aim to address this limitation
by imaging larger volumes.

### The Functional Connectomics Paradigm

MICrONS showed that structural and functional data from the same neurons answer
questions that neither answers alone. A wiring diagram without activity leaves many
circuits consistent with it. Activity without wiring leaves the mechanism open.
What the combination does not give you is causation: a like-to-like wiring rule is a
correlation measured in one animal, and testing what it does needs perturbation
experiments or models.

### Proofreading Completeness

Unlike FlyWire, which achieved near-complete proofreading of an entire brain, MICrONS
has been proofread selectively. This means that analyses must account for residual
segmentation errors, and findings may be biased toward well-proofread regions or cell
types. The tension between thoroughness and feasibility is a persistent challenge in
large-volume connectomics.


## Discussion Questions for Instructors

1. Why is the co-registration between calcium imaging and EM volumes so critical?
   What would happen to the scientific conclusions if the registration contained
   systematic errors?
2. The like-to-like rule in MICrONS is statistical: many connected pairs are not
   functionally similar. What does a real but partial rule mean for our understanding
   of cortical computation? Is connectivity destiny, or one factor among many?
3. Compare the proofreading strategy of MICrONS (targeted) with FlyWire (exhaustive).
   Under what circumstances is each approach appropriate?
4. The MICrONS volume spans the border between V1, LM, AL, and RL. How might areal
   boundaries within the volume complicate or enrich the analysis?
5. If you could add one additional data modality to MICrONS (e.g., gene expression,
   neuromodulator receptor distribution, developmental lineage), which would you
   choose and why?


## Key References

- The MICrONS Consortium. (2025). Functional connectomics spanning multiple areas of
  mouse visual cortex. *Nature*, 640, 435-447.
  [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
  (Preprint: *bioRxiv* 2021.07.28.454025.)
- Ding, Z., et al. (2025). Functional connectomics reveals general wiring rule in mouse
  visual cortex. *Nature*, 640, 459-469.
  [10.1038/s41586-025-08840-3](https://doi.org/10.1038/s41586-025-08840-3)
- Turner, N. L., et al. (2022). Reconstruction of neocortex: Organelles, compartments,
  cells, circuits, and activity. *Cell*, 185(6), 1082-1100.
  [10.1016/j.cell.2022.01.023](https://doi.org/10.1016/j.cell.2022.01.023)
- Schneider-Mizell, C. M., et al. (2025). Inhibitory specificity from a connectomic
  census of mouse visual cortex. *Nature*, 640, 448-458.
  [10.1038/s41586-024-07780-8](https://doi.org/10.1038/s41586-024-07780-8)
- Dorkenwald, S., et al. (2025). CAVE: Connectome Annotation Versioning Engine.
  *Nature Methods*, 22(5), 1112-1120.
  [10.1038/s41592-024-02426-z](https://doi.org/10.1038/s41592-024-02426-z)
