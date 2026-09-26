---
layout: page
title: "FlyWire Whole-Brain Connectome"
permalink: /content-library/case-studies/flywire-whole-brain/
image: /assets/images/content-library/case-studies/flywire-whole-brain.svg
image_alt: "Stylized vector art: a specimen ring with landmark points beside a data band."
description: >
  Case study of FlyWire, the first complete synaptic wiring diagram of an adult fly
  brain (Drosophila melanogaster): 139,255 neurons and about 54.5 million chemical
  synapses, proofread by a consortium of labs and volunteers.
topics:
  - whole-brain connectomics
  - Drosophila melanogaster
  - collaborative proofreading
  - convolutional-network segmentation
  - cell-type classification
  - circuit architecture
  - crowd-sourced annotation
primary_units:
  - "08"
  - "09"
difficulty: intermediate
tags:
  - case-studies:FlyWire
  - connectomics:whole-brain
  - connectomics:dense-reconstruction
  - proofreading:crowd-sourced
  - cell-types:neuron-classification
  - imaging:serial-section-TEM
  - methodology:automated-segmentation
  - neuroanatomy:Drosophila
micro_lesson_id: ml-case-flywire
combines_with:
  - c-elegans-revisited
  - microns-visual-cortex
  - mouseconnects-himc
use_layout_hero: false
content_type: core
---

# FlyWire Whole-Brain Connectome

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

FlyWire produced the first complete synaptic-resolution wiring diagram of an adult
fly brain, from one female *Drosophila melanogaster*. Dorkenwald et al. (2024,
*Nature*) report 139,255 neurons and 54.5 million chemical synapses between them.
A companion paper, Schlegel et al. (2024), sorts the neurons into 8,453 annotated
cell types. Together they show that whole-brain connectomics is feasible for a brain
of this size, and they give fly neuroscience a shared reference map.

The way the work was done matters as much as the dataset. Automated segmentation
produced the first draft. The FlyWire Consortium then corrected it by hand, with an
estimated 33 person-years of proofreading (Dorkenwald et al. 2024). The University
of Cambridge's October 2024 announcement describes the consortium as teams in more
than 76 laboratories and 287 researchers around the world, plus volunteers from the
public; Princeton's release says "at least 76 laboratories". Neither the machine
draft nor the human effort would have been enough alone.


## The Starting Point: FAFB

FlyWire did not begin from scratch. The project built upon the Full Adult Fly Brain
(FAFB) electron microscopy volume, a serial-section transmission electron microscopy
(ssTEM) dataset acquired by Zheng et al. (2018) and published in *Cell*. The FAFB
volume captured an entire adult female *Drosophila* brain at synaptic resolution:
7,062 sections of about 40 nm, imaged at 4 nm per pixel, giving about 106 TB in
roughly 21 million camera images (Zheng et al. 2018).

Raw images alone are not a connectome. To go from images to a wiring diagram required two additional steps:
automated segmentation (assigning each voxel to a specific neuron) and proofreading
(correcting the inevitable errors in automated segmentation). FlyWire tackled both.


## Technical Pipeline

### Automated Segmentation

FlyWire realigned the FAFB images and segmented them automatically with convolutional
neural networks (Dorkenwald et al. 2022). This was a different segmentation from the
flood-filling network (FFN) reconstruction of FAFB that Google Research produced
separately.

The automated segmentation was deliberately biased toward over-segmentation: individual
neurons were often split into several fragments. Pipelines make this choice because
joining two fragments is a single merge edit, while separating two wrongly merged
neurons means finding the merge point and cutting it cleanly.

### The FlyWire Platform: CAVE and Neuroglancer

To enable collaborative proofreading at scale, the FlyWire team built a web-based
platform on top of two key technologies:

- **CAVE (Connectome Annotation Versioning Engine)**: A backend system described by
  Dorkenwald et al. (2025) that manages the segmentation as a dynamic, versioned
  chunked graph. CAVE allows multiple users to edit the segmentation simultaneously
  without conflicts, tracks every edit with full version history, and serves the
  current state of the segmentation in real time.

- **Neuroglancer**: A WebGL-based viewer for large-scale volumetric data. FlyWire
  extended Neuroglancer with proofreading tools — the ability to merge segments
  (correct splits) and split segments (correct merges) directly in the browser. No
  software installation was required; anyone with a web browser could proofread.

Together, CAVE and Neuroglancer moved connectome proofreading from single-user
desktop tools to a web platform where many people edit the same brain at once.


## Proofreading at Scale: The Social Engineering Challenge

### Recruitment and Training

FlyWire's community model is as instructive as its software. The FlyWire Consortium
brought together researchers from many labs, dedicated proofreading teams, and
volunteers from the public. The consortium is listed as an
author of the Dorkenwald et al. (2024) paper, with members' contributions given in its
supplementary material.

A distributed effort like this raises design questions that any large proofreading
campaign must answer:

- **Training**: How do new proofreaders learn the basic operations (merge and split)
  before they edit shared data?
- **Motivation**: What keeps contributors engaged over a multi-year campaign?
  FlyWire's edit history is programmatically accessible, which supports uses such as
  estimating proofreading accuracy or building incentive systems.
- **Quality control**: How are errors caught and ambiguous cases (damaged tissue,
  uncertain synapses) resolved consistently across many people?


## Key Scientific Findings

### Brain-Wide Cell-Type Atlas

One of the main outputs of FlyWire is a cell-type atlas of the adult *Drosophila*
brain. Schlegel et al. (2024), published alongside it in *Nature*, annotated 8,453
cell types covering 96.4% of the brain's neurons, using morphology, connectivity and
matching against the hemibrain connectome. Of those types, 3,643 had been proposed
from the hemibrain and 4,581 were new, mostly from regions outside the hemibrain
volume. The authors describe it as, to their knowledge, the largest cell-type atlas
yet proposed for any brain.

Questions the atlas lets you ask include:

- How many cell types are there compared with estimates from light microscopy?
- How many cell types are represented by only one or two neurons per hemisphere?
- Do cell types group into families with shared morphology and connectivity?

### Circuit Architecture of the Central Complex

The central complex is a midline neuropil structure involved in navigation, spatial
orientation, and locomotor control. Its first comprehensive connectome came from the
hemibrain dataset (Hulse et al. 2021); FlyWire places it in the context of the whole
brain. Features of central complex wiring include:

- A columnar organization that maps heading direction onto neural activity.
- Ring neuron inputs that carry visual and other sensory information.
- Output pathways toward premotor and descending neurons that influence steering and
  locomotion.
- Circuit architecture consistent with ring attractor models proposed for
  head-direction coding.

### Sensorimotor Pathways and Descending Neurons

The complete brain connectome enabled systematic tracing of pathways from sensory
input to motor output. The descending neurons, which project from the brain to the
ventral nerve cord (the fly equivalent of the spinal cord), could be identified as a
complete set:

- Dorkenwald et al. (2024) grouped the neurons crossing the neck connective into 1,303
  efferent (descending) and 2,362 afferent (ascending) neurons.
- With every descending neuron's brain inputs mapped, you can ask how many sensory
  modalities converge on each one.
- Descending neurons with known behavioral roles (for example in walking, flight, or
  grooming) can be traced back to their upstream circuits.

### Information Flow and Feedback

Dorkenwald et al. traced synaptic pathways from the brain's inputs (sensory and
ascending neurons) to its outputs (motor, endocrine and descending neurons), across
both hemispheres and between the central brain and the optic lobes. Two points from
the paper are worth carrying into your own analyses:

- **Early vision is not purely feedforward.** Half of all optic lobe neurons receive
  five or more synapses from visual centrifugal neurons, which carry signals from the
  central brain back into the optic lobe.
- **Direction of flow is subtler than input and output.** Most fly neurites carry a
  mixture of presynapses and postsynapses on both dendrites and axons, so labeling a
  neuron "input" or "output" does not settle which way information moves through it.

A companion paper (Lin et al. 2024) analyzes the network statistics, and Codex tags
neurons with the resulting labels, such as rich club, broadcaster and highly
reciprocal.


## Data Availability and Tools

The FlyWire connectome is publicly available through several access points:

- **Codex (codex.flywire.ai)**: A web-based portal for browsing the connectome. Users
  can search for neurons by cell type, brain region, or connectivity, and visualize
  their morphology and synaptic partners in 3D.

- **FAFB-FlyWire CAVE tables**: The complete connectivity data is available through
  the CAVE API, which provides programmatic access to neuron segmentation, synapse
  tables, cell-type annotations, and proofreading status.

- **NAVis and fafbseg**: Python libraries for neuron analysis; fafbseg adds FlyWire
  access on top of NAVis. Researchers can download neuron skeletons, compute
  morphological features, and analyze connectivity programmatically. Dorkenwald et al.
  also list natverse (R), Catmaid Spaces, braincircuits.io and static exports as
  access routes.

- **Neuroglancer**: The raw EM data and segmentation can be browsed interactively
  through the FlyWire Neuroglancer instance.

### Example Access Pattern (Python)

Researchers typically access FlyWire data through the `caveclient` Python package,
which provides authenticated access to the CAVE backend. Queries can retrieve
individual neuron morphologies, synapse lists between specified neuron pairs, or
bulk connectivity matrices for entire brain regions.


## Lessons for the Field

### Whole-Brain Connectomics Is Achievable for a Fly

FlyWire showed that the complete synaptic wiring diagram of an adult insect brain can
be reconstructed. *Drosophila* has about 140,000 neurons in its brain. The tools
(automated segmentation, collaborative proofreading, versioned annotation) carry over
to larger brains, but the effort grows with volume: a whole mouse brain is about
500 mm³ (Badea et al. 2007), roughly 500 times the MICrONS cubic millimeter.

### Crowd-Sourced Proofreading Works

FlyWire showed that connectome reconstruction does not have to rest on a small team
of specialist annotators. With training, shared tools and quality control, a
distributed community reached the accuracy the published analyses needed.

### Automation Alone Is Not Enough

The automated segmentation still needed about 33 person-years of human correction.
Left uncorrected, its split and merge errors would have corrupted the downstream
analyses. Human review remains part of the pipeline, not an optional finishing step.

### The Connectome Is a Beginning, Not an End

The wiring diagram is a static snapshot of one female fly. It does not show
neuromodulation, gap junctions, or how the same brain differs between individuals
or sexes; Dorkenwald et al. note known male-female differences and high variability
in mushroom body neurons. Interpreting it takes functional experiments, models and
comparison with other connectomes such as the hemibrain.


## Discussion Questions for Instructors

1. Why was over-segmentation preferred to under-segmentation in the initial automated
   pipeline? What are the tradeoffs?
2. How would you design a quality control system for a proofreading effort with 500+
   contributors? What metrics would you track?
3. The central complex circuit architecture matches computational models of ring
   attractor networks. Does this validate the models, or could the match be
   coincidental?
4. What are the limitations of a connectome derived from a single individual brain?
   How might brain-to-brain variability affect the generality of findings?
5. Compare the FlyWire community model with traditional academic lab structures. What
   are the advantages and disadvantages of each for large-scale data projects?


## Key References

- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. *Nature*,
  634, 124-138. [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)
- Schlegel, P., et al. (2024). Whole-brain annotation and multi-connectome cell typing
  of *Drosophila*. *Nature*, 634, 139-152.
  [10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5)
- Lin, A., et al. (2024). Network statistics of the whole-brain connectome of
  *Drosophila*. *Nature*, 634, 153-165. [10.1038/s41586-024-07968-y](https://doi.org/10.1038/s41586-024-07968-y)
- Zheng, Z., et al. (2018). A complete electron microscopy volume of the brain of
  adult *Drosophila melanogaster*. *Cell*, 174(3), 730-743.
  [10.1016/j.cell.2018.06.019](https://doi.org/10.1016/j.cell.2018.06.019)
- Dorkenwald, S., et al. (2022). FlyWire: online community for whole-brain
  connectomics. *Nature Methods*, 19, 119-128.
  [10.1038/s41592-021-01330-0](https://doi.org/10.1038/s41592-021-01330-0)
- Dorkenwald, S., et al. (2025). CAVE: Connectome Annotation Versioning Engine.
  *Nature Methods*, 22(5), 1112-1120.
  [10.1038/s41592-024-02426-z](https://doi.org/10.1038/s41592-024-02426-z)
- Hulse, B. K., et al. (2021). A connectome of the *Drosophila* central complex reveals
  network motifs suitable for flexible navigation and context-dependent action
  selection. *eLife*, 10, e66039.
- University of Cambridge. (2 October 2024). First map of every neuron in an adult fly
  brain complete. [cam.ac.uk](https://www.cam.ac.uk/research/news/first-map-of-every-neuron-in-an-adult-fly-brain-complete)
- Li, F., et al. (2020). The connectome of the adult *Drosophila* mushroom body
  provides insights into function. *eLife*, 9, e62576.
