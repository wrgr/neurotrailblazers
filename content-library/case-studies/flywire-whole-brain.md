---
layout: page
title: "FlyWire Whole-Brain Connectome"
permalink: /content-library/case-studies/flywire-whole-brain/
description: >
  A comprehensive case study of the FlyWire project — the first complete connectome
  of an adult animal brain (Drosophila melanogaster), mapping ~139,255 neurons and
  ~54.5 million chemical synapses through large-scale collaborative proofreading.
topics:
  - whole-brain connectomics
  - Drosophila melanogaster
  - collaborative proofreading
  - flood-filling networks
  - cell-type classification
  - circuit architecture
  - crowd-sourced annotation
primary_units:
  - unit-01-intro-to-connectomics
  - unit-03-image-segmentation
  - unit-05-proofreading
  - unit-07-circuit-analysis
difficulty: intermediate
tags:
  - case-studies:FlyWire
  - connectomics:whole-brain
  - connectomics:dense-reconstruction
  - proofreading:crowd-sourced
  - cell-types:neuron-classification
  - imaging:serial-section-TEM
  - methodology:flood-filling-networks
  - neuroanatomy:Drosophila
micro_lesson_id: ml-case-flywire
reference_images:
  - src: /assets/images/content-library/case-studies/flywire-whole-brain/whole-brain-render.png
    alt: "3D rendering of the complete Drosophila brain from FlyWire with major neuropils colored"
    caption: "FlyWire whole-brain connectome: ~140,000 neurons reconstructed and proofread across all major neuropils."
  - src: /assets/images/content-library/case-studies/flywire-whole-brain/proofreading-interface.png
    alt: "FlyWire browser-based proofreading interface showing collaborative segment editing"
    caption: "FlyWire's Neuroglancer-based proofreading platform enabled 287 contributors to collaboratively correct segmentation errors."
  - src: /assets/images/content-library/case-studies/flywire-whole-brain/circuit-diagram.png
    alt: "Circuit diagram of a visual motion detection pathway reconstructed from FlyWire data"
    caption: "Motion detection circuit extracted from FlyWire: T4/T5 neurons with directionally tuned medulla inputs."
combines_with:
  - c-elegans-revisited
  - microns-visual-cortex
  - mouseconnects-himc
---

# FlyWire Whole-Brain Connectome

## Overview

The FlyWire project delivered the first complete synaptic-resolution connectome of an
adult animal brain — that of the fruit fly *Drosophila melanogaster*. Published by
Dorkenwald et al. in *Nature* (2024), this landmark dataset comprises approximately
139,255 neurons connected by roughly 54.5 million chemical synapses, organized into
an estimated 8,453 cell types. The achievement demonstrates that whole-brain
connectomics is feasible for small brains and establishes a reference framework for
understanding how an entire nervous system is wired.

The significance of FlyWire extends beyond the dataset itself. The project pioneered
a model of large-scale, community-driven proofreading that may define how future
connectomics projects operate. By combining state-of-the-art automated segmentation
with the collective effort of 287 contributors worldwide, FlyWire showed that neither
machines nor humans alone can reconstruct a brain — but together, they can.


## The Starting Point: FAFB

FlyWire did not begin from scratch. The project built upon the Full Adult Fly Brain
(FAFB) electron microscopy volume, a serial-section transmission electron microscopy
(ssTEM) dataset acquired by Zheng et al. (2018) and published in *Cell*. The FAFB
volume captured an entire adult female *Drosophila* brain at synaptic resolution,
producing roughly 21 million images at 4 nm x 4 nm in-plane resolution with 40 nm
section thickness.

The FAFB volume was a monumental imaging achievement, but raw images alone are not a
connectome. To go from images to a wiring diagram required two additional steps:
automated segmentation (assigning each voxel to a specific neuron) and proofreading
(correcting the inevitable errors in automated segmentation). FlyWire tackled both.


## Technical Pipeline

### Automated Segmentation with Flood-Filling Networks

The initial segmentation of the FAFB volume used flood-filling networks (FFNs), a
deep learning architecture developed at Google Research. Unlike conventional
segmentation approaches that classify each voxel independently, FFNs iteratively
"grow" segments by predicting, at each step, which neighboring voxels belong to the
same neuron. This approach naturally handles the complex, branching morphology of
neurons.

The FFN segmentation produced an over-segmented representation of the brain — meaning
that individual neurons were often split into multiple fragments. This is by design:
over-segmentation is preferable to under-segmentation (merging two neurons) because
splits are easier to correct than merges during proofreading.

### The FlyWire Platform: CAVE and Neuroglancer

To enable collaborative proofreading at scale, the FlyWire team built a web-based
platform on top of two key technologies:

- **CAVE (Connectome Annotation Versioning Engine)**: A backend system developed by
  Dorkenwald et al. (2022) that manages the segmentation as a dynamic, versioned
  chunked graph. CAVE allows multiple users to edit the segmentation simultaneously
  without conflicts, tracks every edit with full version history, and serves the
  current state of the segmentation in real time.

- **Neuroglancer**: A WebGL-based viewer for large-scale volumetric data. FlyWire
  extended Neuroglancer with proofreading tools — the ability to merge segments
  (correct splits) and split segments (correct merges) directly in the browser. No
  software installation was required; anyone with a web browser could proofread.

Together, CAVE and Neuroglancer transformed connectome proofreading from a
specialized, single-user desktop application task into a massively parallel,
web-based collaborative effort.


## Proofreading at Scale: The Social Engineering Challenge

### Recruitment and Training

Perhaps the most innovative aspect of FlyWire was not its technology but its community
model. The project recruited 287 proofreaders from around the world, including
professional neuroscientists, postdocs, graduate students, and trained citizen
scientists. Recruitment occurred through lab networks, conference presentations,
social media, and word of mouth.

New proofreaders underwent a structured training protocol:

1. **Tutorial missions**: Guided tasks that introduced the basic proofreading
   operations (merge and split) on pre-selected neurons with known ground truth.
2. **Supervised proofreading**: New contributors worked on neurons that were
   subsequently reviewed by experienced proofreaders, with feedback provided.
3. **Independent proofreading**: After demonstrating proficiency, contributors were
   given access to proofread neurons independently.

### Gamification and Motivation

FlyWire incorporated gamification elements to sustain motivation over the multi-year
proofreading campaign:

- **Leaderboards**: Public displays of proofreading contributions, ranked by number
  of edits, neurons completed, and other metrics.
- **Progress dashboards**: Visual indicators of overall project completion, giving
  contributors a sense of collective progress.
- **Neuron adoption**: Contributors could "claim" specific neurons or brain regions,
  fostering a sense of ownership and investment.
- **Community recognition**: Regular acknowledgment of top contributors in project
  communications and ultimately in the published papers (all 287 contributors are
  co-authors on the Dorkenwald et al. 2024 paper).

### Quality Control and Inter-Annotator Agreement

Ensuring consistency across 287 proofreaders required robust quality control:

- **Redundant proofreading**: Critical neurons and circuits were proofread by multiple
  independent annotators, and discrepancies were resolved through discussion or expert
  adjudication.
- **Automated error detection**: Computational tools flagged statistically unusual
  morphologies (e.g., neurons with unexpectedly high or low synapse counts) for
  additional review.
- **Community governance**: A core team of experienced proofreaders served as
  moderators, resolving disputes and setting standards for ambiguous cases (e.g., how
  to handle damaged tissue regions or ambiguous synaptic contacts).


## Key Scientific Findings

### Brain-Wide Cell-Type Atlas

One of the primary outputs of FlyWire is a comprehensive cell-type atlas of the adult
*Drosophila* brain. Schlegel et al. (2024), published concurrently in *Nature*,
used the FlyWire connectome to classify neurons into approximately 8,453 cell types
based on morphology, connectivity, and spatial position. This atlas provides the most
complete catalog of cell types in any adult brain to date.

The cell-type classification revealed several important patterns:

- The brain contains far more cell types than previously estimated from light
  microscopy studies alone.
- Many cell types are represented by only 1-2 neurons per hemisphere, suggesting a
  high degree of cellular specialization.
- Cell types cluster into families with shared morphological and connectivity features,
  suggesting common developmental origins.

### Circuit Architecture of the Central Complex

The central complex is a midline neuropil structure involved in navigation, spatial
orientation, and locomotor control. FlyWire provided the first complete wiring diagram
of this structure, revealing:

- A columnar organization that maps heading direction onto neural activity.
- Ring neuron inputs that carry visual and proprioceptive information.
- Output pathways to descending neurons that control turning and forward locomotion.
- The circuit architecture closely matches computational models of a ring attractor
  network proposed for head-direction coding.

### Sensorimotor Pathways and Descending Neurons

The complete brain connectome enabled systematic tracing of pathways from sensory
input to motor output. The catalog of descending neurons — neurons that project from
the brain to the ventral nerve cord (the fly equivalent of the spinal cord) — was
mapped in its entirety for the first time. This revealed:

- Approximately 1,100 descending neuron pairs connect the brain to motor circuits.
- Most descending neurons receive convergent input from multiple sensory modalities.
- Specific descending neurons can be linked to known behavioral outputs (flight,
  walking, grooming) based on their connectivity patterns.

### Convergence and Divergence Patterns

Analysis of the complete connectome revealed systematic patterns of information flow:

- **Convergence**: Sensory information is progressively integrated as it flows from
  peripheral sensory neurons through interneurons toward output neurons.
- **Divergence**: Individual sensory channels broadcast to many downstream targets,
  enabling parallel processing.
- **Recurrence**: Feedback loops are pervasive throughout the brain, challenging
  simple feedforward models of neural computation.


## Data Availability and Tools

The FlyWire connectome is publicly available through several access points:

- **Codex (codex.flywire.ai)**: A web-based portal for browsing the connectome. Users
  can search for neurons by cell type, brain region, or connectivity, and visualize
  their morphology and synaptic partners in 3D.

- **FAFB-FlyWire CAVE tables**: The complete connectivity data is available through
  the CAVE API, which provides programmatic access to neuron segmentation, synapse
  tables, cell-type annotations, and proofreading status.

- **Navis/NAVis**: A Python library for neuron analysis that supports direct queries
  to the FlyWire dataset. Researchers can download neuron skeletons, compute
  morphological features, and analyze connectivity patterns programmatically.

- **Neuroglancer**: The raw EM data and segmentation can be browsed interactively
  through the FlyWire Neuroglancer instance.

### Example Access Pattern (Python)

Researchers typically access FlyWire data through the `caveclient` Python package,
which provides authenticated access to the CAVE backend. Queries can retrieve
individual neuron morphologies, synapse lists between specified neuron pairs, or
bulk connectivity matrices for entire brain regions.


## Lessons for the Field

### Whole-Brain Connectomics Is Achievable

FlyWire proved that it is possible to reconstruct the complete synaptic wiring diagram
of an adult brain. While *Drosophila* is a small brain (~100,000 neurons), the
principles and tools developed for FlyWire — automated segmentation, collaborative
proofreading, versioned annotation infrastructure — are directly applicable to larger
brains.

### Crowd-Sourced Proofreading Works

The 287-person proofreading community demonstrated that connectome reconstruction does
not require a small team of highly specialized annotators. With proper training,
tooling, and quality control, a large distributed community can collectively achieve
the accuracy required for scientific analysis.

### Automation Alone Is Not Enough

Despite using state-of-the-art deep learning for segmentation, extensive human
proofreading was still required. The automated segmentation contained numerous split
and merge errors that would have corrupted downstream analyses if left uncorrected.
This underscores the continued importance of human-in-the-loop approaches in
connectomics.

### The Connectome Is a Beginning, Not an End

The publication of the FlyWire connectome is not the conclusion of a project but the
opening of a new era. The wiring diagram is a static snapshot that must be interpreted
through functional experiments, computational modeling, and comparative analysis. The
real scientific payoff will come from the community of researchers who use this
resource over the coming decades.


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
  634, 124-138.
- Schlegel, P., et al. (2024). Whole-brain annotation and multi-connectome cell typing
  of *Drosophila*. *Nature*, 634, 139-152.
- Zheng, Z., et al. (2018). A complete electron microscopy volume of the brain of
  adult *Drosophila melanogaster*. *Cell*, 174(3), 730-743.
- Dorkenwald, S., et al. (2022). CAVE: Connectome Annotation Versioning Engine.
  *bioRxiv*.
- Li, F., et al. (2020). The connectome of the adult *Drosophila* mushroom body
  provides insights into function. *eLife*, 9, e62576.
