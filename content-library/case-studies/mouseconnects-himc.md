---
layout: page
title: "MouseConnects and HI-MC"
permalink: /content-library/case-studies/mouseconnects-himc/
image: /assets/images/content-library/case-studies/mouseconnects-himc.svg
image_alt: "Stylized vector art: a specimen ring with landmark points beside a data band."
description: >
  Case study of MouseConnects and HI-MC (the Center for High-throughput Integrative
  Mouse Connectomics), an NIH BRAIN CONNECTS project imaging 10 mm³ of mouse
  hippocampal formation at synaptic resolution. NeuroTrailblazers was developed
  within it. No data has been released yet.
topics:
  - hippocampal connectomics
  - BRAIN Initiative
  - large-scale EM
  - memory circuits
  - trisynaptic pathway
  - multibeam SEM
  - flood-filling networks
  - proofreading at scale
primary_units:
  - "01"
  - "04"
difficulty: intermediate
tags:
  - case-studies:MouseConnects
  - connectomics:dense-reconstruction
  - neuroanatomy:hippocampus
  - neuroanatomy:mouse
  - infrastructure:cloud-computing
  - infrastructure:BRAIN-Initiative
  - methodology:pipeline
  - imaging:multi-beam-SEM
  - proofreading:AI-assisted
micro_lesson_id: ml-case-mouseconnects
combines_with:
  - microns-visual-cortex
  - flywire-whole-brain
  - h01-human-cortex
use_layout_hero: false
content_type: core
---

# MouseConnects and HI-MC

> ### Before you quote a number from this page
>
> MouseConnects has released no data. Every number below is a target or a
> projection taken from the NIH award abstract or the partners' 2023
> announcements, not a measurement, and the sources do not agree on data size.
> When the project releases data, cite the release and its version, as
> [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
> describes. The [MouseConnects dataset page]({{ '/datasets/mouseconnects/' | relative_url }})
> tracks the project's status.


## Overview

MouseConnects is funded through the NIH BRAIN Initiative's Connectivity Across
Scales (BRAIN CONNECTS) program as award UM1NS132250, "A Center for High-throughput
Integrative Mouse Connectomics" (HI-MC). The principal investigator is Jeff W.
Lichtman at Harvard University, and the award runs from September 2023 to August 2028
(NIH RePORTER). Harvard's announcement lists Princeton, MIT, Cambridge University and
Johns Hopkins among the partners, with $30 million from NIH and $3 million more from
Harvard and Princeton. Google Research is a partner and contributes its own resources
without NIH funding. RePORTER records budget-year awards through fiscal 2026; check
the [current record](https://reporter.nih.gov/project-details/UM1NS132250) before
citing the project's status.

The award abstract says the project "will image 10 cubic millimeters" of the mouse
hippocampal formation, a dataset that "may exceed tens of petabytes". That is roughly
ten times the volume of MICrONS or H01 (our arithmetic). The abstract frames the work
as a feasibility test for a whole mouse brain, which "is 50 times larger". The
hippocampal formation was chosen because it is central to memory and spatial
navigation, and it is also where Alzheimer's disease and temporal lobe epilepsy take
an early toll.


## Why the Hippocampus?

### A Heavily Studied Circuit Without a Synaptic Map

The hippocampus has been a focus of neuroscience research for over half a century.
Several features make it a strong target for large-scale connectomics:

- **Well-defined architecture.** The hippocampus has a distinctive layered structure
  with clearly delineated subregions (dentate gyrus, CA3, CA2, CA1, subiculum) and
  strata (stratum oriens, pyramidale, radiatum, lacunosum-moleculare). Cell types
  and their approximate locations are well characterized from decades of anatomical
  and physiological studies.

- **The trisynaptic circuit.** The canonical hippocampal circuit runs from entorhinal
  cortex to dentate gyrus (via the perforant path), to CA3 (via mossy fibers), to CA1
  (via Schaffer collaterals). It is one of the most studied circuit motifs in
  neuroscience.
  It has been dissected with electrophysiology, modeled computationally, and linked to
  specific cognitive functions. It has not yet been mapped at synaptic resolution
  across a volume large enough to capture the full spatial extent of its connectivity.

- **Functional significance.** The hippocampus is essential for episodic memory
  formation, spatial navigation (place cells, grid cells), and contextual learning.
  Understanding its wiring at synaptic resolution could illuminate the circuit
  mechanisms underlying these cognitive functions.

- **Clinical relevance.** The hippocampus is one of the first brain regions affected
  in Alzheimer's disease and is the focus of seizure activity in temporal lobe
  epilepsy. A reference connectome of the normal hippocampus would provide a baseline
  for understanding how disease disrupts circuit function.

### Hypotheses a Synaptic Map Could Test

Decades of hippocampal research have produced theories whose synaptic-level
predictions have not been tested at population scale:

- **Pattern separation in the dentate gyrus.** The dentate gyrus is hypothesized to
  separate overlapping input patterns into distinct representations through sparse
  coding and lateral inhibition. The specific connectivity that implements this
  computation (how entorhinal inputs diverge onto granule cells, how few CA3 cells
  each granule cell's mossy fiber contacts, how interneurons mediate separation) is
  unknown at the population level.

- **Attractor dynamics in CA3.** CA3 is proposed to function as an auto-associative
  memory network, using its dense recurrent excitatory connections to store and
  retrieve patterns. The topology of the CA3 recurrent network (its degree
  distribution, clustering, and relationship to stored memories) has not been
  mapped at synaptic resolution at population scale.

- **Replay sequences.** During sleep and rest, hippocampal neurons replay activity
  sequences experienced during waking behavior. Whether replay sequences correspond
  to specific synaptic pathways is a fundamental question that requires connectomic
  data to answer.

- **Engram connectivity.** Memory engrams, the physical traces of specific
  memories, are thought to be encoded in specific patterns of synaptic connectivity.
  A large-scale hippocampal connectome could reveal whether engram-tagged neurons
  (identified through activity markers) share distinctive wiring signatures.


## Technical Approach

### What the Award Abstract Describes

The method is described in the NIH award abstract and the partners' 2023
announcements. Nothing below is yet reported in a paper.

- **Targeting.** The volume of interest is chosen from a micro-CT scan of a whole
  brain.

- **Semithin sections, milled and imaged.** The block is cut into semithin serial
  sections. Each section is imaged by multibeam scanning electron microscopy; an ion
  beam then mills away a thin layer and the new surface is imaged, "until each section
  is fully imaged". The abstract gives the aim as "minimizing distortions caused by
  previous ultra-thin sectioning approaches". This builds on the Lichtman lab's
  multibeam SEM work for H01, but it is a different sectioning scheme from H01's
  ultrathin ATUM sections. Harvard's 2023 announcement describes two 91-beam SEMs,
  one at Harvard and one at Princeton.

- **Automated reconstruction.** The abstract describes quality monitoring, image
  compression, assembly of the volume, and labeling of neurons, glia, blood vessels,
  myelin, cell bodies and synapses. Google Research's announcement says it will
  refine its flood-filling networks (the segmentation method used for H01) and extend
  SegCLR, its self-supervised method for cell-type and compartment labels.

- **Proofreading, registration and access.** The reconstruction is to be proofread,
  registered to the Allen Institute mouse brain atlas, and shared through free online
  tools to "render, proofread, or otherwise analyze" it. The abstract does not name
  the proofreading platform. CAVE, used by FlyWire, MICrONS and H01, is the
  best-documented system of that kind, and [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
  explains how it works.

### What Ten Times the Volume Does to the Pipeline

At 10 mm³, the MouseConnects volume is an order of magnitude larger than MICrONS
(about 1 mm³). That changes every stage of the pipeline:

- **Acquisition throughput.** H01's 1 mm³ took 326 days on one 61-beam microscope (Shapson-Coe et al. 2024).
  Ten times the volume needs higher throughput per microscope, more microscopes, or
  both; the abstract lists single-microscope imaging throughput as a performance
  parameter the project will monitor.

- **Data storage.** The published projections differ: "may exceed tens of petabytes"
  (NIH abstract), "about 10,000 terabytes" (Harvard, 2023) and "about 25,000
  terabytes, or 25 petabytes" (Google Research, 2023). Derived data (segmentations,
  synapse maps, skeletons) add more.

- **Computational load.** Segmenting and synapse-detecting across tens of petabytes will
  require proportionally more compute than MICrONS. Algorithmic improvements that
  reduce per-voxel compute costs will be as important as raw compute scaling.

- **Proofreading at scale.** FlyWire's whole fly brain took an estimated 33
  person-years of proofreading. Exhaustive manual proofreading of 10 mm³ of mouse
  tissue is unlikely to be affordable with current tools, so expect automated error
  detection plus targeted human review of the circuits and cell types an analysis
  needs. How to do that well is an open methods question.


## Expected Scientific Impact

### What the Project Says It Will Deliver

Published hippocampal EM reconstructions cover much smaller volumes than the one
planned here. The award abstract lists these aims:

- Identify cell types by region and layer, defined by morphology and connectivity,
  and relate them to transcriptomic classifications.
- Reveal the detailed connectivity of hippocampal formation circuits, including local
  and long-range microcircuit motifs.
- Use those circuits to test and improve models of memory and spatial cognition.
- Integrate the structural results with light microscopy and single-cell gene
  expression data.
- Monitor throughput and cost to judge what a whole-mouse-brain connectome would take.

Which subregions and pathways (dentate gyrus, CA3, CA1, the mossy fibers, the
Schaffer collaterals) fall inside the final volume is not stated in the sources
above. Treat any such list as a hope until the data is released.

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

A hippocampal connectome at or above MICrONS scale would allow direct comparison of
wiring principles between cortex and hippocampus. Questions include:

- Are the same connectivity motifs (e.g., reciprocal excitation, perisomatic
  inhibition) present in both structures, or does the hippocampus have unique motifs?
- How does the connectivity of hippocampal interneuron classes compare to their
  cortical counterparts?
- Is the degree of recurrent connectivity in CA3 quantitatively different from
  recurrent connectivity in cortical layers 2/3?


## Connection to NeuroTrailblazers

NeuroTrailblazers was developed within the HI-MC project
([About]({{ '/about/' | relative_url }})). It is a training site, not a part of the
project's research plan, and it has no formal role in producing or proofreading the
MouseConnects data.

### Training for the Kind of Work the Project Needs

A project of this size needs people who can proofread, annotate and analyze. The
[technical units]({{ '/technical-training/' | relative_url }}) teach EM image
interpretation, segmentation proofreading, synapse identification and connectomic
data analysis on released datasets (MICrONS, H01, FlyWire) that use the same kinds of
tools.

### What the Award Commits To

The award abstract commits the project to "involve undergraduates from
underrepresented backgrounds in the proofreading and scientific discovery phases of
our work, offering them mentoring as well as research experience." That is the
project's own commitment, run by the project. Training here does not guarantee a
place in it.

### Broadening Participation

Connectomics has been concentrated in a small number of well-resourced laboratories.
NeuroTrailblazers publishes its training materials openly so that students at
institutions without connectomics infrastructure can learn the same methods.


## Timeline and Milestones

The MouseConnects award runs for five years (September 2023 to August 2028). The
project has not published a milestone plan. The sequence below is our generic outline
of how a project of this kind tends to unfold, not the project's schedule:

- **Year 1-2**: Tissue preparation, initial EM acquisition, pipeline optimization.
  Development of hippocampus-specific segmentation models and quality metrics.
- **Year 2-3**: Large-scale EM acquisition. Initial segmentation of acquired volumes.
  Begin targeted proofreading of early data.
- **Year 3-4**: Continued acquisition and segmentation. First scientific analyses of
  partially complete datasets. Community access to early data releases.
- **Year 4-5**: Completion of acquisition. Large-scale proofreading campaigns.
  Analysis and publication of findings. Public data release.

Large connectomics projects often take longer than planned: the MICrONS mouse was
perfused in 2018, and the main MICrONS paper was published in 2025.


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
5. Once the MouseConnects data is released, which analyses could a student team run
   on it beyond proofreading? What analytical skills would be most valuable?


## Key References

- NIH BRAIN Initiative. BRAIN CONNECTS: Comprehensive Centers for Mouse Brain
  ([RFA-NS-22-048](https://grants.nih.gov/grants/guide/rfa-files/RFA-NS-22-048.html)).
  *National Institutes of Health*.
- Lichtman, J. W., & Sanes, J. R. (2008). Ome sweet ome: what can the genome tell us
  about the connectome? *Current Opinion in Neurobiology*, 18(3), 346-353.
  [10.1016/j.conb.2008.08.010](https://doi.org/10.1016/j.conb.2008.08.010)
- Lichtman, J. W., Pfister, H., & Shavit, N. (2014). The big data challenges of
  connectomics. *Nature Neuroscience*, 17(11), 1448-1454.
  [10.1038/nn.3837](https://doi.org/10.1038/nn.3837)
- The MICrONS Consortium. (2025). Functional connectomics spanning multiple areas of
  mouse visual cortex. *Nature*, 640, 435-447.
  [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
- Dorkenwald, S., et al. (2025). CAVE: Connectome Annotation Versioning Engine.
  *Nature Methods*, 22(5), 1112-1120.
  [10.1038/s41592-024-02426-z](https://doi.org/10.1038/s41592-024-02426-z)
- NIH RePORTER. BRAIN CONNECTS: A Center for High-throughput Integrative Mouse
  Connectomics (UM1NS132250; PI Jeff W. Lichtman).
  [reporter.nih.gov](https://reporter.nih.gov/project-details/10665380)
- Harvard Gazette. (September 2023). Human brain too big to map, so they're starting
  with mice.
  [news.harvard.edu](https://news.harvard.edu/gazette/story/2023/09/human-brain-too-big-to-map-so-theyre-starting-with-mice/)
- Google Research. (2023). Google Research embarks on effort to map a mouse brain.
  [research.google](https://research.google/blog/google-research-embarks-on-effort-to-map-a-mouse-brain/)
- Amaral, D. G., & Witter, M. P. (1989). The three-dimensional organization of the
  hippocampal formation: a review of anatomical data. *Neuroscience*, 31(3), 571-591.
  [10.1016/0306-4522(89)90424-7](https://doi.org/10.1016/0306-4522(89)90424-7)
