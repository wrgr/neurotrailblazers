---
layout: page
title: "MouseConnects and HI-MC"
permalink: /content-library/case-studies/mouseconnects-himc/
description: >
  A comprehensive case study of the MouseConnects project and its HI-MC (Hippocampal
  Connectome) initiative — an NIH BRAIN Initiative CONNECTS-funded effort to map the
  synaptic connectome of the mouse hippocampus across ~10 mm³, representing the
  largest connectomics undertaking to date and a flagship project for NeuroTrailblazers.
topics:
  - hippocampal connectomics
  - BRAIN Initiative
  - large-scale EM
  - memory circuits
  - trisynaptic pathway
  - serial-section TEM
  - flood-filling networks
  - proofreading at scale
primary_units:
  - unit-01-intro-to-connectomics
  - unit-02-em-acquisition
  - unit-03-image-segmentation
  - unit-05-proofreading
  - unit-07-circuit-analysis
  - unit-09-future-directions
difficulty: intermediate
---

# MouseConnects and HI-MC

## Overview

The MouseConnects project, funded through the NIH BRAIN Initiative CONNECTS
(Connectome of a Neural Ensemble by Comprehensive Tracing at Synaptic resolution)
program, represents the most ambitious connectomics undertaking yet attempted. Led by
Jeff Lichtman at Harvard University and Viren Jain at Google Research, with a network
of collaborators across multiple institutions, the project aims to reconstruct the
synaptic connectome of the mouse hippocampus — a volume of approximately 10 mm³
spanning CA1, CA3, the dentate gyrus, and associated regions. Funded from 2023 to
2028, with an expected dataset exceeding 10 petabytes, MouseConnects will produce a
connectome roughly ten times the volume of MICrONS and orders of magnitude larger
than any previous reconstruction.

The project's specific hippocampal initiative, referred to as HI-MC (Hippocampal
Connectome), focuses on capturing the complete synaptic wiring of one of the most
studied and least understood circuits in neuroscience — the hippocampal formation,
which is central to memory, spatial navigation, and the pathology of Alzheimer's
disease and epilepsy.


## Why the Hippocampus?

### The Most Studied Circuit in Neuroscience

The hippocampus has been a focus of neuroscience research for over half a century.
Several features make it an ideal target for large-scale connectomics:

- **Well-defined architecture.** The hippocampus has a distinctive layered structure
  with clearly delineated subregions (dentate gyrus, CA3, CA2, CA1, subiculum) and
  strata (stratum oriens, pyramidale, radiatum, lacunosum-moleculare). Cell types
  and their approximate locations are well characterized from decades of anatomical
  and physiological studies.

- **The trisynaptic circuit.** The canonical hippocampal circuit — entorhinal cortex
  to dentate gyrus (via the perforant path) to CA3 (via mossy fibers) to CA1 (via
  Schaffer collaterals) — is one of the most studied circuit motifs in neuroscience.
  It has been dissected with electrophysiology, modeled computationally, and linked to
  specific cognitive functions. Yet it has never been mapped at synaptic resolution
  across a volume large enough to capture the full spatial extent of its connectivity.

- **Functional significance.** The hippocampus is essential for episodic memory
  formation, spatial navigation (place cells, grid cells), and contextual learning.
  Understanding its wiring at synaptic resolution could illuminate the circuit
  mechanisms underlying these cognitive functions.

- **Clinical relevance.** The hippocampus is one of the first brain regions affected
  in Alzheimer's disease and is the focus of seizure activity in temporal lobe
  epilepsy. A reference connectome of the normal hippocampus would provide a baseline
  for understanding how disease disrupts circuit function.

### Untested Hypotheses

Decades of hippocampal research have generated rich theoretical frameworks that
remain untested at the synaptic level:

- **Pattern separation in the dentate gyrus.** The dentate gyrus is hypothesized to
  separate overlapping input patterns into distinct representations through sparse
  coding and lateral inhibition. The specific connectivity that implements this
  computation — how many granule cells each mossy fiber contacts, how interneurons
  mediate separation — is unknown at the population level.

- **Attractor dynamics in CA3.** CA3 is proposed to function as an auto-associative
  memory network, using its dense recurrent excitatory connections to store and
  retrieve patterns. The topology of the CA3 recurrent network — its degree
  distribution, clustering, and relationship to stored memories — has never been
  mapped.

- **Replay sequences.** During sleep and rest, hippocampal neurons replay activity
  sequences experienced during waking behavior. Whether replay sequences correspond
  to specific synaptic pathways is a fundamental question that requires connectomic
  data to answer.

- **Engram connectivity.** Memory engrams — the physical traces of specific
  memories — are thought to be encoded in specific patterns of synaptic connectivity.
  A large-scale hippocampal connectome could reveal whether engram-tagged neurons
  (identified through activity markers) share distinctive wiring signatures.


## Technical Approach

### Building on Established Methods

MouseConnects builds directly on the technical foundations laid by previous large-scale
connectomics projects, particularly MICrONS and the Lichtman lab's extensive
experience with serial-section electron microscopy:

- **Serial-section TEM.** The primary acquisition method is automated serial-section
  transmission electron microscopy, using tape-based section collection (ATUM or
  similar) and high-throughput imaging. The Lichtman lab has decades of experience
  with this approach and has progressively increased throughput with each generation
  of instrumentation.

- **Flood-filling network segmentation.** Automated segmentation will use flood-
  filling networks (FFNs) developed at Google Research, the same core technology used
  in FlyWire and other large-scale reconstructions. The Google team's ongoing
  improvements to FFN architecture, training procedures, and inference efficiency are
  expected to yield better segmentation quality and faster processing.

- **CAVE infrastructure.** The Connectome Annotation Versioning Engine, originally
  developed for FlyWire and used in MICrONS, will serve as the backend for
  segmentation management, annotation, and collaborative proofreading.

### Pushing the Boundaries of Scale

At 10 mm³, the MouseConnects hippocampal volume is an order of magnitude larger than
the MICrONS volume (1 mm³). This scale increase creates challenges across every stage
of the pipeline:

- **Acquisition throughput.** Imaging 10 mm³ at synaptic resolution will require
  sustained high-throughput operation of multiple electron microscopes over years.
  Advances in multi-beam SEM and automated section handling are critical to meeting
  the timeline.

- **Data storage.** The expected dataset size exceeds 10 petabytes of raw imagery,
  with additional petabytes of derived data (segmentations, synapse maps, skeletons).
  Cloud-based storage and compute infrastructure is essential.

- **Computational load.** Segmenting and synapse-detecting across 10 PB of data will
  require proportionally more compute than MICrONS. Algorithmic improvements that
  reduce per-voxel compute costs will be as important as raw compute scaling.

- **Proofreading at scale.** Complete manual proofreading of a 10 mm³ volume is
  almost certainly infeasible with current approaches. MouseConnects will likely
  require novel proofreading strategies that combine heavy automation (AI-assisted
  error detection and correction) with targeted human review of high-priority
  circuits and cell types. This is an area of active methodological development.


## Expected Scientific Impact

### The First Large-Scale Hippocampal Connectome

No previous connectomics dataset has covered the hippocampus at the scale and
resolution planned for MouseConnects. Existing hippocampal EM data consists of small
volumes (tens of micrometers) or sparse reconstructions that cannot capture the full
spatial extent of hippocampal circuits. MouseConnects will provide:

- Complete wiring diagrams of the dentate gyrus, CA3, CA2, and CA1 subregions.
- Full reconstruction of the mossy fiber pathway from dentate granule cells to CA3.
- Mapping of the Schaffer collateral system from CA3 to CA1.
- Characterization of interneuron diversity and connectivity across all hippocampal
  layers.
- Long-range input pathways from entorhinal cortex (to the extent they are contained
  within the volume).

### Testing Computational Theories

The hippocampal connectome will enable direct testing of long-standing computational
theories:

- Does the dentate gyrus connectivity support the pattern separation computation
  proposed by theory?
- Is the CA3 recurrent network topology consistent with auto-associative memory
  models?
- Do place cells with overlapping place fields share more synaptic connections than
  those with non-overlapping fields? (This question may require functional data in
  addition to the connectome.)

### Comparison with Cortical Connectomics

By producing a hippocampal connectome at a scale comparable to MICrONS, MouseConnects
will enable direct comparison of wiring principles between cortex and hippocampus.
Questions include:

- Are the same connectivity motifs (e.g., reciprocal excitation, perisomatic
  inhibition) present in both structures, or does the hippocampus have unique motifs?
- How does the connectivity of hippocampal interneuron classes compare to their
  cortical counterparts?
- Is the degree of recurrent connectivity in CA3 quantitatively different from
  recurrent connectivity in cortical layers 2/3?


## Connection to NeuroTrailblazers

MouseConnects is the flagship project that the NeuroTrailblazers training program
directly supports. The relationship operates at multiple levels:

### Workforce Development

The scale of MouseConnects demands a trained workforce for proofreading, annotation,
and analysis. NeuroTrailblazers provides structured training in the skills needed to
contribute to the project — EM image interpretation, segmentation proofreading,
synapse identification, and connectomic data analysis. Students who complete the
training program will be equipped to contribute directly to MouseConnects.

### Proofreading Contributions

As the MouseConnects dataset becomes available for proofreading, NeuroTrailblazers
participants may contribute to the proofreading effort as part of their training.
This creates a mutually beneficial arrangement: students gain hands-on experience
with real connectomics data, and the project benefits from additional proofreading
labor.

### Analysis and Interpretation

Beyond proofreading, NeuroTrailblazers aims to train students in the computational
skills needed to analyze connectomic data — network analysis, statistical modeling,
visualization, and comparison with functional data. MouseConnects will generate an
enormous volume of data that will require years of analysis by many researchers.
NeuroTrailblazers alumni will be among those equipped to contribute.

### Broadening Participation

A key goal of both MouseConnects and NeuroTrailblazers is broadening participation
in connectomics. The field has historically been concentrated in a small number of
well-resourced laboratories. By providing training materials, tools, and pathways
to contribution, NeuroTrailblazers aims to make connectomics accessible to a wider
community — including students at institutions without existing connectomics
infrastructure.


## Timeline and Milestones

The MouseConnects project operates on a five-year timeline (2023-2028) with major
milestones including:

- **Year 1-2**: Tissue preparation, initial EM acquisition, pipeline optimization.
  Development of hippocampus-specific segmentation models and quality metrics.
- **Year 2-3**: Large-scale EM acquisition. Initial segmentation of acquired volumes.
  Begin targeted proofreading of early data.
- **Year 3-4**: Continued acquisition and segmentation. First scientific analyses of
  partially complete datasets. Community access to early data releases.
- **Year 4-5**: Completion of acquisition. Large-scale proofreading campaigns.
  Comprehensive analysis and publication of findings. Full public data release.

These timelines are approximate and subject to the technical challenges inherent in
a project of this scale. Previous large-scale connectomics projects have consistently
encountered unforeseen obstacles that required timeline adjustments.


## Discussion Questions for Instructors

1. The MouseConnects volume (10 mm³) is 10 times larger than MICrONS (1 mm³). What
   aspects of the pipeline scale linearly with volume, and what aspects scale
   super-linearly? Where are the bottlenecks?
2. Complete manual proofreading of 10 mm³ may be infeasible. How would you design a
   proofreading strategy that balances thoroughness with feasibility? What circuits
   or cell types would you prioritize?
3. The hippocampus is often studied in the context of memory. What experimental
   paradigms could be combined with the MouseConnects connectome to link wiring to
   memory function?
4. Compare the scientific strategy of MouseConnects (one region, very large volume)
   with an alternative approach (many small volumes from different brain regions).
   What are the tradeoffs?
5. How might NeuroTrailblazers-trained students contribute to MouseConnects beyond
   proofreading? What analytical skills would be most valuable?


## Key References

- NIH BRAIN Initiative CONNECTS Program. (2023). Program announcement and funded
  projects. *National Institutes of Health*.
- Lichtman, J. W., & Sanes, J. R. (2008). Ome sweet ome: what can the genome tell us
  about the connectome? *Current Opinion in Neurobiology*, 18(3), 346-353.
- Lichtman, J. W., Pfister, H., & Shavit, N. (2014). The big data challenges of
  connectomics. *Nature Neuroscience*, 17(11), 1448-1454.
- MICrONS Consortium. (2021). Functional connectomics spanning multiple areas of mouse
  visual cortex. *bioRxiv*, 2021.07.28.454025.
- Dorkenwald, S., et al. (2022). CAVE: Connectome Annotation Versioning Engine.
  *bioRxiv*.
- Amaral, D. G., & Witter, M. P. (1989). The three-dimensional organization of the
  hippocampal formation: a review of anatomical data. *Neuroscience*, 31(3), 571-591.
