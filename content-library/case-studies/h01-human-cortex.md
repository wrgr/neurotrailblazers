---
layout: page
title: "H01 Human Cortex Fragment"
permalink: /content-library/case-studies/h01-human-cortex/
image: /assets/images/content-library/case-studies/h01-human-cortex.svg
image_alt: "Stylized vector art: a specimen ring with landmark points beside a data band."
description: >
  Case study of H01, a reconstruction of about 1 mm³ of human temporal cortex at
  nanoscale resolution: 57,180 cells, about 150 million synapses, and the caveats
  that come with surgical tissue from one person.
topics:
  - human connectomics
  - temporal cortex
  - surgical tissue
  - nanoscale reconstruction
  - species comparison
  - pathological features
  - cortical architecture
primary_units:
  - "05"
  - "08"
difficulty: advanced
tags:
  - case-studies:H01
  - connectomics:dense-reconstruction
  - neuroanatomy:human-cortex
  - neuroanatomy:temporal-lobe
  - imaging:electron-microscopy
  - cell-types:pyramidal-cell
  - cell-types:interneuron
  - methodology:species-comparison
  - infrastructure:cloud-storage
micro_lesson_id: ml-case-h01
combines_with:
  - microns-visual-cortex
  - c-elegans-revisited
  - mouseconnects-himc
use_layout_hero: false
content_type: core
---

# H01 Human Cortex Fragment

<div class="callout-box callout-note">
  <p><strong>Looking for how it was built?</strong> This page is the overview: what H01
  is and what it shows. <a href="{{ '/content-library/case-studies/h01-pipeline/' | relative_url }}">H01, Step by Step</a>
  walks the production pipeline stage by stage, from surgical tissue through staining,
  sectioning, 61-beam imaging, alignment, segmentation and synapse detection, with
  figures rendered from the public volume.</p>
</div>

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

H01 is a petavoxel reconstruction of human cortex published by Shapson-Coe et al.
(2024, *Science*). The authors' accepted manuscript (PMC11718559) describes it as, to
their knowledge, the largest volume of human cortex imaged at electron-microscopic
resolution and the first EM dataset to exceed a petabyte. The tissue is a fragment of temporal
lobe cortex, about 1 mm³, removed during surgery for drug-resistant epilepsy in a
45-year-old woman. It was imaged at 4 nm per pixel in sections averaging 33.9 nm.
The aligned volume is 1.4 petabytes (1.8 PB of raw acquisition). It contains 57,180
cells, of which 16,087 are neurons, and about 150 million synapses.

Most of what is known about cortical circuitry comes from rodents. H01, together with
smaller human datasets such as Loomba et al. (2022), lets you check that knowledge
against human tissue synapse by synapse, and ask how much of what we learned from mice
applies to humans.


## The Source Tissue: Surgical Resection

### Clinical Context

The tissue was obtained from a surgical resection performed to treat medically
refractory temporal lobe epilepsy. In such procedures, a portion of the temporal lobe
(including the epileptic focus) is removed to reduce seizure frequency. The resected
tissue, which would otherwise be discarded, was redirected for research with informed
consent.

This clinical origin shapes the dataset in three ways:

- **Immersion fixation, not perfusion fixation.** In animal studies, the gold standard
  for EM tissue preservation is transcardiac perfusion with fixative, which delivers
  fixative to every capillary simultaneously. Human surgical tissue cannot be
  perfusion-fixed; instead, it is immersed in fixative after removal. Immersion can
  leave a gradient of preservation quality from the tissue surface to the interior, so
  it is worth checking. For H01, the authors judged the histological quality
  "equivalent to the rodent perfused cardiac samples used in the past."

- **Pathological context.** The tissue was resected because it was near or part of an
  epileptic focus. Some regions of the volume may contain pathological features —
  aberrant connectivity patterns, unusual neuronal morphologies, or gliosis — that
  reflect the disease rather than normal brain architecture. Distinguishing disease-
  related features from normal variation is a persistent interpretive challenge.

- **A single individual.** The dataset comes from one person of a particular age, sex,
  and medical history. Generalizing findings to "the human brain" requires caution.

### Tissue Characteristics

Human cortical tissue differs from rodent tissue in several ways that are immediately
apparent in the EM data:

- **Larger neurons, at lower density.** Human cortical pyramidal cells are larger than
  their mouse counterparts. H01's neuron density is about 16,000/mm³, which the authors
  report is nearly 10-fold lower than mouse association cortex.

- **Lipofuscin granules.** These age-related lysosomal residual bodies accumulate in
  human neurons over decades and appear as dense, heterogeneous inclusions in EM
  images. They must be distinguished from other electron-dense
  structures (e.g., mitochondria, dense-core vesicles) during both manual and
  automated analysis. Lipofuscin is rarely encountered in the young adult rodent
  tissue used in most connectomics studies.

- **Abundant glia.** In H01, glia outnumber neurons 2:1 (32,315 versus 16,087), and
  oligodendrocytes are the single most common cell type. Astrocytes, oligodendrocytes,
  microglia, and oligodendrocyte precursor cells are all visible in the EM volume.


## Technical Pipeline

### Acquisition

The tissue block was cut into 5,019 sections on an automated tape-collecting
ultramicrotome (ATUM) and imaged with a 61-beam scanning electron microscope
(MICrONS, by contrast, used transmission EM). Sections averaged 33.9 nm thick,
slightly thinner than the 40 nm used in MICrONS.

### Segmentation and Reconstruction

Automated segmentation was performed with flood-filling networks trained on ground
truth painted by human annotators. Human tissue brings features that are rare in young
rodent tissue, such as lipofuscin granules; the H01 pipeline, for example, blocked
segments from being seeded inside myelin, lipofuscin and other electron-dense
structures.

### Scale of the Dataset

H01's raw acquisition was 1.8 PB, of the same order as MICrONS's ~2 PB of raw imagery.
Compare like with like: H01's often-quoted 1.4 PB is the aligned volume, not the raw
data. The reconstruction identified:

- 57,180 cells: 49,080 neurons and glia plus 8,100 blood-vessel-related cells
- 16,087 neurons and 32,315 glia
- 149,871,669 automatically detected synapses
- 104 proofread neurons

These are the *Science* paper's counts. Counts from the release site differ because they
describe different pipeline products; see
[H01, Step by Step]({{ '/content-library/case-studies/h01-pipeline/' | relative_url }}).


## Key Scientific Findings

### Discovery of Axon Whorls

Among the most unexpected observations in H01 was a small number of axons that formed
extensive whorls, alongside extremely large spines and axon varicosities filled with
unusual material. The authors write that "at present, we are unable to determine
whether these resulted from a pathological process or if they are simply rare."

The significance of axon whorls remains unclear. Hypotheses include:

- Developmental remnants of axon pathfinding errors.
- Pathological features related to the epileptic condition.
- Normal but previously undetected structural features only visible at EM resolution.
- Artifacts of tissue handling or fixation.

The whorls illustrate a general point: when you image tissue at a scale and
resolution not reached before, you find structures nobody predicted. Interpreting
them needs comparison samples, which is why the authors call for "comparing samples
obtained from individuals with different underlying disorders".

### Rare, Powerful Axonal Inputs

Most axons that contact a given neuron make just one synapse onto it (96.49% of
connections). Yet 39% of the 2,743 well-innervated neurons had at least one input
making seven or more synapses, and one proofread layer 3 pyramidal axon made 53
synapses onto a single interneuron. The authors conclude that, among many weak
incidental connections, a small subset of inputs "purposefully establish more powerful
connections." Whether these strong inputs have a distinct function remains open.

### Layer-Specific Connectivity

H01 spans all six cortical layers plus white matter, and the layers differ in cell and
synapse composition. Layer boundaries were derived from soma size and clustering
density rather than drawn by hand.

Layer-specific findings reported in the paper include:

- Excitatory synapse density is highest in layers 1 and 3; inhibitory synapse density
  peaks in layer 1.
- The excitatory share of synapses is broadly similar across layers, slightly lower in
  layer 1.
- The largest cells sit mostly in a deep band corresponding to layer 5 and a
  supragranular band corresponding to layer 3.
- Oligodendrocyte density follows a gradient, lowest in the upper layers and highest in
  the white matter.
- In layers 5 and 6, 876 "triangular" neurons have basal dendrites whose orientations
  form a bimodal, mirror-image distribution.

### Comparison with Mouse Cortex

Setting H01 beside mouse cortical datasets (particularly MICrONS) suggests:

- **Conserved features**: Basic elements of cortical organization, such as layered
  structure and perisomatic inhibition of pyramidal cells, are present in both species.
- **Quantitative differences**: H01's neuron density is nearly 10-fold lower than mouse
  association cortex, and glia outnumber neurons 2:1. A dedicated comparison of mouse,
  macaque and human cortex is Loomba et al. (2022).
- **Unexplained features**: The authors could not determine whether the whorls and other
  oddities in H01 are pathological or simply rare. Whether they reflect species
  differences, tissue age, pathology, or preparation remains open.


## Data Access

The H01 dataset is publicly available for browsing and analysis:

- **Neuroglancer**: The primary interface for browsing the EM volume and segmentation
  is Neuroglancer, linked from the [H01 release site](https://h01-release.storage.googleapis.com/landing.html). Users can
  navigate the volume in 3D, inspect individual neurons, and examine synaptic contacts.

- **Cloud storage**: Derived data products, including segmentation volumes and synapse
  tables, are available through Google Cloud Storage for programmatic access and bulk
  download.

- **Pre-computed analyses**: The Shapson-Coe et al. paper includes supplementary
  tables, among them counts of inputs to all neurons (table S8).

Like FlyWire and MICrONS, H01 has a CAVE instance for community proofreading. The
release also ships CREST, a tool for exploring and correcting reconstructions. The
dataset comes from a collaboration between the Lichtman lab at Harvard and the
Connectomics at Google team.


## Challenges and Interpretive Cautions

### Fixation Quality

Immersion fixation can leave a gradient of tissue preservation, with better
preservation near the surface than deeper in the block. The H01 authors report few
membrane breaks and histological quality equivalent to perfused rodent tissue, but any
analysis sensitive to membrane or synapse visibility should still check preservation
quality in the region it uses.

### Pathological Features

Because the tissue was resected from an epileptic brain, some features in the dataset
may reflect pathology rather than normal anatomy. Reactive gliosis, neuronal loss,
aberrant sprouting, and other epilepsy-related changes could be present. There is no
"normal" human cubic millimeter to compare against, and the authors note that fresh
samples from healthy individuals "are unlikely to ever be available" through
neurosurgery.

### Generalizability

A single 1 mm³ fragment from one person's temporal lobe cannot represent the full
diversity of human cortical architecture. Cortical regions differ in their laminar
structure, cell type composition, and connectivity patterns. Age, sex, genetic
background, and life experience all influence brain structure. H01 is a proof of
concept, not a definitive atlas.

### Ethical Considerations

Human tissue connectomics raises ethical questions that do not arise with animal
tissue:

- **Informed consent**: The patient consented to research use of the resected tissue,
  but the scope of connectomic analysis may exceed what was originally envisioned.
- **Identifiability**: Could the connectomic data, combined with clinical records,
  identify the individual? Nobody has shown it can, and nobody has shown it cannot.
  [Ethics and governance]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }})
  covers de-identification in EM.
- **Incidental findings**: If the dataset reveals unexpected pathological features,
  is there an obligation to communicate these to the patient? In practice, the
  surgical tissue was already removed, but the principle matters for future studies.


## Significance for the Field

### Human Connectomics Is Feasible

H01 shows that the pipeline developed for rodent connectomics (automated sectioning,
multi-beam SEM, deep learning segmentation) works on human surgical tissue. It needs
adapting for lipofuscin, larger cells and immersion fixation, and the authors
conclude that "rapid immersion of fresh tissue in fixative is a viable alternative
to perfusion".

### A Reference for Cross-Species Comparison

Worm, fly and mouse have been mapped at synaptic resolution, and H01 adds a human
sample. That makes cross-species comparison of circuit motifs possible, with one
limit worth stating each time: the human end is one fragment from one person.

### A Foundation for Clinical Connectomics

In the long term, nanoscale connectomics of human tissue could contribute to
understanding neurological and psychiatric disorders. That depends on linking wiring
differences to disease states, which needs many samples from people with different
conditions. H01 is one sample.


## Discussion Questions for Instructors

1. How should researchers handle the interpretive challenges posed by pathological
   tissue? What controls or comparisons would strengthen conclusions drawn from H01?
2. Lipofuscin granules are abundant in human neurons but rare in young rodent tissue.
   What challenges do they pose for automated segmentation, and how might training
   data need to be adapted?
3. The axon whorls were unexpected. How should the field approach novel structures
   that do not map onto existing anatomical knowledge?
4. Compare the ethical considerations of human tissue connectomics with those of animal
   tissue connectomics. Are the ethical frameworks fundamentally different?
5. If you were designing the next human connectomics project, what tissue source,
   brain region, and clinical context would you choose, and why?


## Key References

- Shapson-Coe, A., et al. (2024). A petavoxel fragment of human cerebral cortex
  reconstructed at nanoscale resolution. *Science*, 384(6696), eadk4858.
  [10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)
- Lichtman, J. W., & Denk, W. (2011). The big and the small: challenges of imaging
  the brain's circuits. *Science*, 334(6056), 618-623.
  [10.1126/science.1209168](https://doi.org/10.1126/science.1209168)
- Dorkenwald, S., et al. (2025). CAVE: Connectome Annotation Versioning Engine.
  *Nature Methods*, 22(5), 1112-1120.
  [10.1038/s41592-024-02426-z](https://doi.org/10.1038/s41592-024-02426-z)
- Loomba, S., et al. (2022). Connectomic comparison of mouse and human cortex.
  *Science*, 377, eabo0924.
  [10.1126/science.abo0924](https://doi.org/10.1126/science.abo0924)
- Kasthuri, N., et al. (2015). Saturated reconstruction of a volume of neocortex.
  *Cell*, 162(3), 648-661.
  [10.1016/j.cell.2015.06.054](https://doi.org/10.1016/j.cell.2015.06.054)
