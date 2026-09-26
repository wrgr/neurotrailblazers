---
layout: page
title: "Neuron Type Identification"
permalink: /content-library/cell-types/neuron-type-identification/
image: /assets/images/content-library/cell-types/neuron-type-identification.svg
image_alt: "Stylized vector art: three cell silhouettes: branched, star-form, and amoeboid."
description: "Classifying neuron types in EM connectomics from morphology, connectivity or both, with the FlyWire and MICrONS approaches, two worked examples and the limits of each method."
topics:
  - cell-types
  - morphology
  - classification
  - pyramidal-cells
  - interneurons
primary_units:
  - "05"
  - "06"
  - "09"
difficulty: "Advanced"
tags:
  - cell-types:neuron-classification
  - cell-types:morphological-classification
  - cell-types:connectivity-based-classification
  - connectomics:cell-census
  - neuroanatomy:cortical-circuits
  - neuroai:clustering
micro_lesson_id: ml-cell-neuron-types
combines_with:
  - axon-dendrite-classification
  - glia-recognition
  - data-formats
content_type: core
---

## Overview

A wiring diagram of unlabeled nodes explains little. Once each node carries a cell-type label, you can say which connections are expected (excitatory neurons contacting nearby neurons) and which are surprising (a rare long-range inhibitory projection). In EM connectomics, types are inferred from morphology and connectivity, plus functional or molecular data when a dataset has them.

---

## Instructor script: the cell-type classification challenge

### What defines a cell type?

There is no settled definition. In practice, a cell type is a group of neurons that share morphological, physiological and molecular properties. EM gives you morphology and connectivity but usually not molecular markers or electrophysiology. MICrONS is a partial exception: it pairs EM with calcium imaging of about 75,000 neurons (MICrONS Consortium 2025).

Whole-brain fly data made the definition testable. Schlegel et al. (2024) proposed that a cell type is a group of cells, each more similar to cells in a *different* brain than to any other cell in its own brain. They could then check types across two brains. About a third of the cell types proposed for the hemibrain could not be reliably re-identified in FlyWire, even though nearly all hemibrain neurons could be matched by morphology.

Earlier systems relied on light microscopy: Cajal and Lorente de Nó on Golgi-stained cells, later work on intracellular fills (reviewed in Markram et al. 2004). EM gives more complete morphology (every branch, every spine), but without the sparse staining that makes one cell stand out against a blank background.

### Excitatory vs inhibitory is the first split

In mammalian cortex, the first split is:

**Excitatory neurons (about 80% of neurons in rodent and primate neocortex; the ratio differs by region, layer and species, so state which you mean; DeFelipe & Fariñas 1992; Markram et al. 2004):**
- Glutamatergic
- Spiny dendrites (spines are sites of excitatory input)
- Pyramidal morphology in most cases; spiny stellate cells in layer 4 of some primary sensory areas
- Asymmetric (Type I) output synapses
- Project locally and to distant targets (other cortical areas, subcortical structures)

**Inhibitory interneurons (about 20% of cortical neurons):**
- GABAergic
- Smooth (aspiny) or sparsely spiny dendrites
- Diverse morphologies (basket, chandelier, Martinotti, bipolar, neurogliaform and others)
- Symmetric (Type II) output synapses
- Mostly local axons, within the same cortical area (a minority project long-range)

**EM rule of thumb:**
- Spiny dendrites + asymmetric output synapses → excitatory
- Smooth dendrites + symmetric output synapses → inhibitory

This works for most cortical neurons. It fails for sparsely spiny interneurons, and it assumes that synapse shape predicts transmitter, which is itself an inference (Unit 05 covers the asymmetric/symmetric distinction).

---

## Morphological classification in EM

### Pyramidal neurons

The most common excitatory neuron in cortex (layers 2-6):

**Identification cues:**
- **Soma**: triangular or pyramidal in 3D, which is harder to see in a single section cut at an arbitrary angle. Roughly 10–25 µm across.
- **Apical dendrite**: one thick, spiny dendrite rising from the apex of the soma toward the pia, with oblique branches along the way. In many pyramidal cells it ends in a tuft in layer 1; in layer 6 corticothalamic cells it usually stops lower (see the table). It is the most distinctive feature of the type.
- **Basal dendrites**: several spiny dendrites leaving the base of the soma and branching locally.
- **Axon**: leaves the base of the soma (or a proximal basal dendrite) and heads toward the white matter; it is often myelinated. Local collaterals make synapses nearby.

**Subtype classification by layer and projection:**
| Subtype | Layer | Projection target | EM distinguishing features |
|---------|-------|-------------------|---------------------------|
| Layer 2/3 pyramidal | 2/3 | Other cortical areas (callosal, associational) | Medium soma, prominent apical reaching L1 |
| Layer 4 spiny stellate | 4 (in some primary sensory areas) | Local (within column) | Stellate dendrites (no clear apical), heavily spiny |
| Layer 5 thick-tufted (ET) | 5 | Subcortical (thalamus, brainstem, spinal cord) | Large soma, thick apical with prominent L1 tuft, thick axon |
| Layer 5 thin-tufted (IT) | 5 | Other cortical areas | Smaller soma, thinner apical, less prominent tuft |
| Layer 6 corticothalamic | 6 | Thalamus | Short apical that usually ends in L4, not L1 |

Projection targets in this table come from tracing studies, not from the EM volume. In a 1 mm³ volume most long-range axons leave the block, so the EM supports the layer and shape columns; the target column is an inference.

### Inhibitory interneuron types

Inhibitory neurons are far more varied in shape. The types most often recognized in EM:

**Basket cells (usually PV+):**
- Smooth or sparsely spiny dendrites
- Axon wraps target somata in basket-like arrays of boutons (perisomatic synapses)
- Symmetric synapses onto the soma and proximal dendrites of pyramidal cells and of other interneurons
- Fast-spiking, if electrophysiology is available
- EM cue: symmetric synapses concentrated on somata

**Chandelier cells (often PV+):**
- Axon terminals form "cartridges": vertical rows of boutons along the axon initial segment (AIS) of pyramidal cells
- The only interneuron type that targets the AIS this selectively
- EM cue: strings of symmetric synapses on an AIS, which you recognize by the dense undercoating of its membrane and its fasciculated microtubules

**Martinotti cells (SST+):**
- Found in layers 2–6, most often in layer 5
- Ascending axon that branches in layer 1 and synapses on distal dendritic tufts
- EM cue: an axon climbing to layer 1 with symmetric synapses on distal dendrites

**Bipolar/VIP+ cells:**
- Elongated soma with two main dendritic trunks running vertically (up and down)
- Narrow axonal arbor that often targets other interneurons
- EM cue: bipolar dendrites and output concentrated on interneurons

**Neurogliaform cells:**
- Small soma with a dense local axonal arbor
- A single cell releases enough GABA to act by volume transmission within its axonal cloud, without needing synapses (Oláh et al. 2009)
- EM cue: a dense, fine local axon cloud. Do not expect every bouton to face a clear postsynaptic partner, and do not count "missing" partners as a detection failure

---

## Connectivity-based classification

### The connectivity fingerprint

Even without morphological reconstruction, neurons can be classified by their connectivity pattern alone:

- **Input fingerprint**: Which cell types provide synaptic input, and in what proportions?
- **Output fingerprint**: Which cell types receive synaptic output, and onto which compartments?

Neurons of the same type tend to have similar connectivity fingerprints. This allows clustering-based classification using the connectome graph directly.

### Methods

1. **Feature engineering**: For each neuron, compute: in-degree, out-degree, fraction of input from excitatory vs inhibitory sources, fraction of output onto soma vs dendrites, laminar distribution of inputs/outputs.
2. **Dimensionality reduction**: PCA, UMAP, or t-SNE on the feature vectors.
3. **Clustering**: K-means, hierarchical clustering, or Gaussian mixture models on the reduced representation.
4. **Validation**: Compare to morphological types (where known) or molecular markers (if available from correlative data).

### FlyWire: 8,453 types from morphology, connectivity and a second brain

In the FlyWire whole-brain connectome (Dorkenwald et al. 2024; Schlegel et al. 2024), cell types were assigned by combining:
- Morphological similarity (NBLAST scores)
- Connectivity (which neurons each cell receives input from and sends output to)
- Expert annotation and the existing hemibrain type names
- Matching across brains: the left and right hemispheres of FlyWire, and the hemibrain

Schlegel et al. (2024) report 8,453 annotated cell types: 3,643 previously proposed in the hemibrain and 4,581 new, mostly from regions outside the hemibrain volume. The comparison across brains is what lets them test a type rather than just name it.

### MICrONS: two routes to cell types

In the MICrONS cubic millimeter of mouse visual cortex, two 2025 *Nature* papers take two routes:
- Elabbady et al. (2025) classified every cell in the volume from quantitative features of the soma and nucleus region (perisomatic ultrastructure). They showed that these features are enough to identify cell types, including types defined mainly by connectivity. That matters because most cells in the volume have incomplete reconstructions.
- Schneider-Mizell et al. (2025) mapped the connectivity of every inhibitory neuron in a densely segmented population of 1,352 cells spanning all layers, a wiring diagram of inhibition with more than 70,000 synapses. They classified inhibitory neurons by which dendritic compartments they target.

### Worked example: typing from a connectivity fingerprint

This example uses a synthetic release, **T67**, with invented cells and counts. It is not drawn from any real dataset.

In T67, four interneurons (IN-a to IN-d) have proofread axons, and every output synapse is labeled with the compartment it lands on:

| Cell | Output synapses | Onto soma | Onto proximal dendrite | Onto distal dendrite / tuft | Onto AIS |
|---|---|---|---|---|---|
| IN-a | 400 | 220 | 140 | 40 | 0 |
| IN-b | 350 | 200 | 120 | 30 | 0 |
| IN-c | 300 | 10 | 30 | 260 | 0 |
| IN-d | 120 | 0 | 0 | 0 | 120 |

As fractions of each cell's output, IN-a is 55% soma and 35% proximal, IN-b 57% and 34%, IN-c 87% distal, and IN-d 100% AIS. IN-a and IN-b share a perisomatic fingerprint (basket-like). IN-c fits a distal-targeting, Martinotti-like profile. IN-d targets only the AIS, the chandelier signature.

What the table does not show: whether IN-a and IN-b are one type or two. Two cells cannot settle that. You need enough cells to see whether the fingerprints form separate clusters or a continuum, and ideally a match in a second volume.

---

## Worked example: classifying a neuron in layer 2/3

**Given:** A fully reconstructed neuron in layer 2/3 of mouse visual cortex.

**Step 1: Excitatory or inhibitory?**
- Dendrites: densely spiny → excitatory
- Output synapses: asymmetric (thick PSD, round vesicles) → excitatory, by a second, independent cue

**Step 2: Morphological subtype**
- Soma: triangular, ~15 μm diameter, in layer 2/3
- One prominent apical dendrite ascending toward layer 1, with terminal tuft
- 5 basal dendrites extending laterally
- Axon: descends from soma base, sends collaterals in layers 2/3 and 5, main axon continues toward white matter
→ **Layer 2/3 pyramidal cell**

**Step 3: Connectivity check** (invented counts for this example cell, whose arbor is cut off by the volume edge; a complete layer 2/3 pyramidal cell receives thousands of synapses, so counts this low are themselves a sign of truncation)
- Receives ~200 excitatory synapses (mostly on spines from other L2/3 and L4 neurons)
- Receives ~50 inhibitory synapses (mostly on soma and proximal dendrites from basket cells)
- Makes ~300 excitatory synapses on nearby L2/3 and L5 neurons
→ Connectivity profile consistent with L2/3 pyramidal cell

**Step 4: Functional data (if available)**
- Calcium imaging shows orientation-selective responses to visual stimuli
→ Consistent with a layer 2/3 cell in visual cortex, but weak evidence for type: many excitatory and inhibitory neurons in V1 are orientation-selective

**Classification:** Layer 2/3 pyramidal neuron. Confidence: **high**, from spines, asymmetric outputs, an apical dendrite and laminar position. Projection target: **unknown**. An axon heading for the white matter fits a callosal or an ipsilateral cortico-cortical projection, and the volume cannot tell the two apart.

---

## Challenges and limitations

### Incomplete reconstructions

Most neurons in a connectomics volume are not fully reconstructed: their axons or dendrites leave the imaged block. A call from partial morphology is less reliable. Record which parts you had, weight the call accordingly, and flag the cell as incomplete. Perisomatic features (Elabbady et al. 2025) are one way to type cells whose arbors are cut off.

### Continuous variation

Some types grade into each other rather than forming clean clusters. In more than 1,300 Patch-seq neurons from mouse motor cortex, Scala et al. (2021) found that broad families (Pvalb, Sst, Vip and so on) had distinct, non-overlapping morpho-electric phenotypes, but neighboring transcriptomic types within a family formed a continuum without clear boundaries. Whether to split one group into two, or keep one type with variation, depends on the analysis question. Say which you chose and why.

### Species differences

Taxonomies built in mouse may not carry over to human or fly. The same feature can mark different types in different species, so comparing across species needs explicit homology mapping.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "Cell types are discrete and obvious" | Many neurons fall on continua between types (Scala et al. 2021), and about a third of hemibrain types could not be reliably re-identified in a second brain (Schlegel et al. 2024) | Report classification confidence and criteria |
| "Morphology alone is sufficient" | Molecular markers and physiology can distinguish types that look similar in EM | Use all available evidence; flag morphology-only classifications |
| "The same types exist in all species" | Cell-type diversity varies across species and regions | Don't assume mouse taxonomy applies to fly or human |
| "More types = better classification" | Over-splitting creates types with too few members for statistical analysis | Balance granularity with statistical power |
| "Orientation tuning (or any single functional property) identifies the type" | Many excitatory and inhibitory cells share the same tuning | Use function as corroboration, not as the deciding cue |

---

## References

- DeFelipe J, Fariñas I (1992) "The pyramidal neuron of the cerebral cortex: morphological and chemical characteristics of the synaptic inputs." *Progress in Neurobiology* 39(6):563-607.
- DeFelipe J et al. (2013) "New insights into the classification and nomenclature of cortical GABAergic interneurons." *Nature Reviews Neuroscience* 14(3):202-216.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.
- Elabbady L et al. (2025) "Perisomatic ultrastructure efficiently classifies cells in mouse cortex." *Nature* 640:478-486. [10.1038/s41586-024-07765-7](https://doi.org/10.1038/s41586-024-07765-7)
- Harris KD, Shepherd GMG (2015) "The neocortical circuit: themes and variations." *Nature Neuroscience* 18(2):170-181.
- Markram H et al. (2004) "Interneurons of the neocortical inhibitory system." *Nature Reviews Neuroscience* 5(10):793-807.
- MICrONS Consortium et al. (2025) "Functional connectomics spanning multiple areas of mouse visual cortex." *Nature* 640:435-447. [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
- Oláh S et al. (2009) "Regulation of cortical microcircuits by unitary GABA-mediated volume transmission." *Nature* 461:1278-1281. [10.1038/nature08503](https://doi.org/10.1038/nature08503)
- Scala F et al. (2021) "Phenotypic variation of transcriptomic cell types in mouse motor cortex." *Nature* 598:144-150. [10.1038/s41586-020-2907-3](https://doi.org/10.1038/s41586-020-2907-3)
- Schlegel P et al. (2024) "Whole-brain annotation and multi-connectome cell typing of *Drosophila*." *Nature* 634:139-152. [10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5)
- Schneider-Mizell CM et al. (2025) "Inhibitory specificity from a connectomic census of mouse visual cortex." *Nature* 640:448-458. [10.1038/s41586-024-07780-8](https://doi.org/10.1038/s41586-024-07780-8)
- Turner NL et al. (2022) "Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity." *Cell* 185(6):1082-1100.
- Zeng H, Sanes JR (2017) "Neuronal cell-type classification: challenges, opportunities and the path forward." *Nature Reviews Neuroscience* 18(9):530-546.
