---
layout: page
title: "H01 Human Cortex Fragment"
permalink: /content-library/case-studies/h01-human-cortex/
description: >
  A comprehensive case study of the H01 dataset — the first nanoscale connectomic
  reconstruction of human brain tissue, derived from a ~1 mm³ fragment of temporal
  lobe cortex containing ~57,000 cells and ~150 million synapses, revealing both
  conserved and novel features of human cortical wiring.
topics:
  - human connectomics
  - temporal cortex
  - surgical tissue
  - nanoscale reconstruction
  - species comparison
  - pathological features
  - cortical architecture
primary_units:
  - unit-01-intro-to-connectomics
  - unit-02-em-acquisition
  - unit-06-data-analysis
  - unit-07-circuit-analysis
  - unit-08-comparative-connectomics
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
reference_images:
  - src: /assets/images/content-library/case-studies/h01-human-cortex/volume-render.png
    alt: "3D rendering of H01 human cortex fragment with layer annotations"
    caption: "H01 petavoxel dataset: ~1 mm³ fragment of human temporal cortex at 4 nm resolution containing ~57,000 cells and 150 million synapses."
  - src: /assets/images/content-library/case-studies/h01-human-cortex/axon-whorls.png
    alt: "Novel axon whorl structures discovered in the H01 human cortex dataset"
    caption: "Axon whorls: tightly wound tangles of axonal processes discovered in H01, not previously described in neuroanatomical literature."
  - src: /assets/images/content-library/case-studies/h01-human-cortex/species-comparison.png
    alt: "Side-by-side comparison of human and mouse pyramidal cell morphology"
    caption: "Cross-species comparison: human pyramidal cells are larger with more extensive dendritic arbors and thicker myelin sheaths than mouse counterparts."
combines_with:
  - microns-visual-cortex
  - c-elegans-revisited
  - mouseconnects-himc
---

# H01 Human Cortex Fragment

## Overview

The H01 dataset represents a watershed moment in neuroscience: the first nanoscale
reconstruction of human brain tissue at synaptic resolution. Published by Shapson-Coe
et al. in *Science* (2024), this dataset derives from a small fragment of temporal lobe
cortex — approximately 1 mm³ — removed during surgical treatment of drug-resistant
epilepsy in a 45-year-old woman. Imaged at 4 nm XY and 33 nm Z resolution, the
resulting dataset comprises roughly 1.4 petabytes of imaging data and contains
approximately 57,000 cells, 150 million synapses, and about 8,000 neurons with
cell-body-containing profiles.

For decades, our understanding of cortical circuitry has been built primarily on
rodent models. H01 provides the first opportunity to examine human cortical wiring at
the level of individual synapses and to ask: how much of what we have learned from
mice actually applies to humans?


## The Source Tissue: Surgical Resection

### Clinical Context

The tissue was obtained from a surgical resection performed to treat medically
refractory temporal lobe epilepsy. In such procedures, a portion of the temporal lobe
(including the epileptic focus) is removed to reduce seizure frequency. The resected
tissue, which would otherwise be discarded, was redirected for research with informed
consent.

This clinical origin has profound implications for the dataset:

- **Immersion fixation, not perfusion fixation.** In animal studies, the gold standard
  for EM tissue preservation is transcardiac perfusion with fixative, which delivers
  fixative to every capillary simultaneously. Human surgical tissue cannot be
  perfusion-fixed; instead, it is immersed in fixative after removal, leading to a
  gradient of preservation quality from the tissue surface (better) to the interior
  (worse). This fixation gradient is visible in the H01 dataset and must be accounted
  for during analysis.

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

- **Larger neurons.** Human cortical pyramidal cells are substantially larger than
  their mouse counterparts, with more extensive dendritic arbors and thicker axons.

- **Thicker myelin sheaths.** Myelinated axons in human cortex have thicker myelin
  wrappings, reflecting the longer distances that signals must travel.

- **Lipofuscin granules.** These age-related lysosomal residual bodies are abundant in
  human neurons (especially in a 45-year-old) and appear as dense, heterogeneous
  inclusions in EM images. They must be distinguished from other electron-dense
  structures (e.g., mitochondria, dense-core vesicles) during both manual and
  automated analysis. Lipofuscin is rarely encountered in the young adult rodent
  tissue used in most connectomics studies.

- **More diverse glial population.** Human cortex contains a greater diversity of
  glial cell types, including astrocytes, oligodendrocytes, microglia, and
  oligodendrocyte precursor cells, all of which are visible in the EM volume.


## Technical Pipeline

### Acquisition

The tissue block was sectioned using automated ultramicrotomy and imaged using
multi-beam scanning electron microscopy, similar in principle to the MICrONS pipeline
but adapted for the specific challenges of human tissue. The 33 nm section thickness
(slightly thinner than the 40 nm used in many mouse studies) was chosen to improve
z-resolution and aid in tracing fine neuronal processes through the volume.

### Segmentation and Reconstruction

Automated segmentation was performed using deep learning models trained on human tissue
ground truth. The segmentation pipeline had to contend with features not present in
rodent training data, including lipofuscin granules, larger cell bodies, and the
fixation quality gradient. Additional post-processing steps were developed to handle
these human-specific challenges.

### Scale of the Dataset

At 1.4 petabytes, H01 is comparable in raw data volume to MICrONS. The reconstruction
identified approximately:

- 57,000 cells (neurons and glia combined)
- 8,000 neurons with soma profiles contained within the volume
- 150 million synaptic connections
- 23,000 neurons with at least partial process reconstructions

These numbers are approximate because the boundaries of the well-preserved tissue are
not sharp, and inclusion criteria for "reconstructed" neurons depend on the analysis.


## Key Scientific Findings

### Discovery of Axon Whorls

Perhaps the most unexpected finding in H01 was the discovery of "axon whorls" —
unusual, tightly wound tangles of axonal processes that had not been previously
described in the neuroanatomical literature. These structures consist of one or more
axons forming complex loops and spirals, sometimes encapsulating other cellular
elements.

The significance of axon whorls remains unclear. Hypotheses include:

- Developmental remnants of axon pathfinding errors.
- Pathological features related to the epileptic condition.
- Normal but previously undetected structural features only visible at EM resolution.
- Artifacts of tissue handling or fixation.

The existence of axon whorls illustrates a key principle: when you image tissue at a
resolution never before achieved, you will find things that nobody predicted. The
connectomics community must develop frameworks for interpreting novel structures that
do not map onto existing knowledge.

### Neurons with Unusually High Synapse Counts

A small population of neurons in H01 was found to have synapse counts far exceeding
the expected range. These "hyper-connected" neurons received or made many more
synapses than their neighbors, raising questions about whether they represent a
distinct functional class, a pathological feature, or a normal extreme of the
connectivity distribution.

### Layer-Specific Connectivity

Despite the tissue being from a single cortical region and a single individual, H01
revealed clear layer-specific differences in connectivity density, cell type
composition, and synapse ultrastructure. These laminar patterns are broadly consistent
with what is known from rodent studies, suggesting that the basic laminar organization
of cortex is conserved across mammals.

Key layer-specific findings include:

- Layer 1 is dominated by axo-dendritic synapses onto the apical tufts of pyramidal
  cells from deeper layers, consistent with top-down and cross-areal input.
- Layers 2/3 show the highest density of excitatory-to-excitatory recurrent
  connections.
- Layer 4 (where present) receives dense thalamocortical input with characteristic
  large boutons.
- Layers 5 and 6 contain the largest pyramidal cells with the most extensive local
  axonal arbors.

### Comparison with Mouse Cortex

Direct comparison between H01 and mouse cortical connectomics datasets (particularly
MICrONS) reveals:

- **Conserved features**: The basic motifs of cortical connectivity — recurrent
  excitation, perisomatic inhibition by basket cells, layer-specific input/output
  organization — are present in both species.
- **Quantitative differences**: Human neurons are larger, have more synapses per
  neuron, show higher spine density on apical dendrites, and have more extensive
  axonal arbors. These quantitative differences may have functional consequences that
  are not yet understood.
- **Human-specific features**: Axon whorls and certain glial arrangements appear to be
  absent from published mouse datasets, though it remains unclear whether this reflects
  genuine species differences or differences in tissue age, pathology, or preparation.


## Data Access

The H01 dataset is publicly available for browsing and analysis:

- **Neuroglancer**: The primary interface for browsing the EM volume and segmentation
  is a Neuroglancer instance hosted at h01-release.storage.googleapis.com. Users can
  navigate the volume in 3D, inspect individual neurons, and examine synaptic contacts.

- **Cloud storage**: Derived data products, including segmentation volumes and synapse
  tables, are available through Google Cloud Storage for programmatic access and bulk
  download.

- **Pre-computed analyses**: The Shapson-Coe et al. paper includes extensive
  supplementary tables with cell-type classifications, synapse counts, and
  connectivity statistics.

Unlike FlyWire and MICrONS, H01 does not currently use the CAVE infrastructure,
which means that collaborative proofreading and annotation versioning are handled
differently. This reflects the dataset's origin as a collaboration led by Google
Research and the Lichtman lab at Harvard.


## Challenges and Interpretive Cautions

### Fixation Quality

The immersion fixation protocol results in a gradient of tissue preservation across
the volume. Regions near the tissue surface are well preserved, with clear membrane
contrast and identifiable synaptic specializations. Regions deeper in the block may
show extraction artifacts, membrane disruption, or reduced contrast. Analyses must
either restrict themselves to well-preserved regions or explicitly account for
preservation quality as a covariate.

### Pathological Features

Because the tissue was resected from an epileptic brain, some features in the dataset
may reflect pathology rather than normal anatomy. Reactive gliosis, neuronal loss,
aberrant sprouting, and other epilepsy-related changes could be present. The
challenge is that we do not have a "normal" human connectomics dataset for
comparison — H01 is the only dataset of its kind.

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
  identify the individual? Current consensus is that this is extremely unlikely, but
  the question deserves ongoing consideration.
- **Incidental findings**: If the dataset reveals unexpected pathological features,
  is there an obligation to communicate these to the patient? In practice, the
  surgical tissue was already removed, but the principle matters for future studies.


## Significance for the Field

### Human Connectomics Is Feasible

H01 demonstrates that the technical pipeline developed for rodent connectomics —
automated sectioning, multi-beam SEM, deep learning segmentation — can be applied to
human tissue. The pipeline requires adaptation (handling lipofuscin, larger cells,
fixation gradients) but is fundamentally workable.

### A Reference for Cross-Species Comparison

As more species are mapped at synaptic resolution (fly, worm, mouse, and now human),
a comparative connectomics framework is emerging. H01 anchors the human end of this
spectrum and enables direct comparison of circuit motifs across species.

### A Foundation for Clinical Connectomics

In the long term, nanoscale connectomics of human tissue could contribute to
understanding neurological and psychiatric disorders. If wiring differences can be
linked to disease states, connectomics could complement genomic and functional
approaches to diagnosis and treatment. H01 is the first step on this path.


## Discussion Questions for Instructors

1. How should researchers handle the interpretive challenges posed by pathological
   tissue? What controls or comparisons would strengthen conclusions drawn from H01?
2. Lipofuscin granules are abundant in human neurons but rare in young rodent tissue.
   What challenges do they pose for automated segmentation, and how might training
   data need to be adapted?
3. The discovery of axon whorls was entirely unexpected. How should the field approach
   novel structures that do not map onto existing anatomical knowledge?
4. Compare the ethical considerations of human tissue connectomics with those of animal
   tissue connectomics. Are the ethical frameworks fundamentally different?
5. If you were designing the next human connectomics project, what tissue source,
   brain region, and clinical context would you choose, and why?


## Key References

- Shapson-Coe, A., et al. (2024). A petavoxel fragment of human cerebral cortex
  reconstructed at nanoscale resolution. *Science*, 384(6696), eadk4858.
- Lichtman, J. W., & Denk, W. (2011). The big and the small: challenges of imaging
  the brain's circuits. *Science*, 334(6056), 618-623.
- Dorkenwald, S., et al. (2022). CAVE: Connectome Annotation Versioning Engine.
  *bioRxiv*.
- Kasthuri, N., et al. (2015). Saturated reconstruction of a volume of neocortex.
  *Cell*, 162(3), 648-661.
