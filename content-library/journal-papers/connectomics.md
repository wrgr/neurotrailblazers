---
layout: page
title: "Journal Papers: Graph Analysis & Network Science"
permalink: /content-library/journal-papers/connectomics/
description: "Curated papers on connectome graph analysis, network neuroscience, and circuit motifs with summaries at beginner, intermediate, and advanced levels."
dimension: connectomics
tags:
  - connectomics:graph-theory
  - connectomics:degree-distribution
  - connectomics:community-detection
  - connectomics:motif
  - connectomics:small-world
  - connectomics:hub
  - connectomics:connectome-comparison
use_layout_hero: false
content_type: core
---

# Graph Analysis & Network Science Journal Papers

Curated papers on connectome graph analysis, network properties, circuit motifs, and comparative connectomics. Each paper includes summaries at three expertise levels.

---

## 1. Bullmore & Sporns (2009) — Complex Brain Networks

**Citation:** Bullmore E, Sporns O. Complex brain networks: graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*. 2009;10(3):186-198.
**DOI:** [10.1038/nrn2575](https://doi.org/10.1038/nrn2575)

**Tags:** `connectomics:graph-theory` `connectomics:small-world` `connectomics:hub` `connectomics:community-detection` `connectomics:degree-distribution` `methodology:statistical-analysis`

### Summaries

**Beginner:** The brain can be studied as a network — neurons as dots, connections as lines. This influential review introduces the basic tools from network science (graph theory) and shows how they apply to brain data. Key ideas include: the brain has "small-world" properties (most neurons can reach most others in a few steps), some neurons are "hubs" with many connections, and the network is organized into communities (modules) that correspond to functional systems. This paper is a great starting point for understanding how wiring diagrams are analyzed.

**Intermediate:** Bullmore and Sporns introduce graph-theoretic analysis of brain networks, mostly at the macroscale (region-to-region networks from tractography or fMRI), with cellular networks such as the *C. elegans* wiring diagram as comparison. They cover key network measures — degree distribution, clustering coefficient, path length, betweenness centrality, modularity — and their biological interpretation. The review discusses small-world architecture, hub organization, and the relationship between network topology and neural function. Importantly, they address methodological pitfalls including thresholding effects, normalization against random graphs, and the distinction between structural and functional networks.

**Advanced:** While focused on macroscale connectomics, this review established the analytical vocabulary now applied to nanoscale EM connectomes. Critical methodological points for EM connectomics: (1) the distinction between binary and weighted graph analyses, and when each is appropriate; (2) the importance of null models — claims of "small-world" or "rich-club" organization are only meaningful relative to appropriately randomized graphs; (3) the scale dependence of network measures (a network property at the neuron level may not hold at the type level or region level). The review's call for standardized analysis pipelines and reproducible reporting remains relevant.

**Key figures:** Look for the schematic of how a brain graph is built from imaging data and the illustrations of the core graph measures.

**Discussion prompts:**
- How do graph measures computed on EM connectomes compare with those from macroscale tractography?
- Which network measures are most robust to missing data (incomplete reconstructions)?
- When is a "small-world" claim meaningful versus trivial?

**Related content:** [Graph representations](/content-library/connectomics/graph-representations/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 2. Winding et al. (2023) — The Connectome of an Insect Brain

**Citation:** Winding M, Pedigo BD, Barnes CL, Patsolic HG, Park Y, Kazimiers T, et al. The connectome of an insect brain. *Science*. 2023;379(6636):eadd9330.
**DOI:** [10.1126/science.add9330](https://doi.org/10.1126/science.add9330)

**Tags:** `connectomics:graph-theory` `connectomics:community-detection` `connectomics:motif` `connectomics:hub` `case-studies:larval-Drosophila` `case-studies:whole-brain` `case-studies:dense-reconstruction`

### Summaries

**Beginner:** This paper presents the complete wiring diagram of a larval fruit fly brain: 3,016 neurons and about 548,000 synapses. Because the brain is small enough to map completely, the authors could analyze the entire network at once, revealing how information flows from sensory inputs through processing centers to motor outputs. They found widespread integration across senses and across the two brain hemispheres, many recurrent loops, and some features, such as shortcuts that skip processing layers, that resemble modern deep learning architectures.

**Intermediate:** Winding et al. present the first complete connectome of an insect brain (*Drosophila* larva, L1 stage). The connectome comprises 3,016 neurons and 548,000 synapses. The dense reconstruction enables whole-brain graph analysis of neuron types, hubs, feedforward and feedback pathways, and interactions across hemispheres and between brain and nerve cord. Reported findings include pervasive multisensory and interhemispheric integration, a highly recurrent architecture, abundant feedback from descending neurons, and several novel circuit motifs; the most recurrent circuits involve the input and output neurons of the learning center (mushroom body).

**Advanced:** This paper demonstrates what becomes possible with a complete connectome: global network analysis without boundary effects. Key analytical themes include: (1) ordering neurons along a sensory-to-output processing axis to separate feedforward from feedback connections; (2) identification of multi-hop pathways from sensory input to output neurons; (3) comparison of pathways across sensory modalities and hemispheres. Some structural features, including multilayer shortcuts and nested recurrent loops, resemble deep learning architectures. Readers should check which null models underlie each claim of non-random structure.

**Key figures:** Fig. 1 (reconstruction of the larval brain), Fig. 2 (axons, dendrites and the four connection types), Fig. 3 (hierarchical clustering of neurons), Fig. 4 (multisensory integration), Fig. 6 (recurrent pathways)

**Discussion prompts:**
- How does the layered processing architecture compare with deep neural network architectures?
- Which findings generalize from the larval brain to the adult brain, and which are development-specific?
- What null model choices most affect the conclusions about circuit structure?

**Related content:** [Network analysis methods](/content-library/connectomics/network-analysis-methods/), [Motif analysis](/content-library/connectomics/motif-analysis/)

---

## 3. Varshney et al. (2011) — Structural Properties of the C. elegans Neuronal Network

**Citation:** Varshney LR, Chen BL, Paniagua E, Hall DH, Chklovskii DB. Structural properties of the *Caenorhabditis elegans* neuronal network. *PLoS Computational Biology*. 2011;7(2):e1001066.
**DOI:** [10.1371/journal.pcbi.1001066](https://doi.org/10.1371/journal.pcbi.1001066)

**Tags:** `connectomics:graph-theory` `connectomics:degree-distribution` `connectomics:small-world` `connectomics:hub` `connectomics:community-detection` `case-studies:C-elegans` `methodology:statistical-analysis`

### Summaries

**Beginner:** The nematode worm *C. elegans* has exactly 302 neurons, and its wiring diagram was mapped decades ago. This paper performs a thorough network analysis of that wiring diagram, asking: what mathematical patterns exist in how these neurons are connected? They find that the network has "small-world" properties, identify neurons that may play central roles in information processing, and find recurring small wiring patterns (motifs). These patterns may reflect fundamental principles of how nervous systems are organized.

**Intermediate:** Varshney et al. assembled whole, self-consistent gap junction and chemical synapse networks of the hermaphrodite *C. elegans* from White et al. (1986) materials plus new electron micrographs. They compute degree distributions, synaptic multiplicities, and small-world properties; identify neurons that may be central to information processing and network motifs that could serve as functional modules; and model activity propagation with linear systems theory. They note that several statistics, such as multiplicity and motif distributions, resemble those reported for mammalian neocortex.

**Advanced:** This paper is a methodological template for connectome network analysis. Notable contributions: (1) use of synaptic multiplicity (weights) alongside binary connectivity; (2) comparison of network statistics against randomized graphs; (3) analysis of the gap junction and chemical synapse networks separately and of their interaction; (4) a visualization of the wiring diagram that reflects signal flow. (The "rich club" of hub interneurons in *C. elegans* was described in later work, not in this paper: Towlson EK, Vértes PE, Ahnert SE, Schafer WR, Bullmore ET. The rich club of the *C. elegans* neuronal connectome. *Journal of Neuroscience*. 2013;33(15):6380-6387. [doi:10.1523/JNEUROSCI.3784-12.2013](https://doi.org/10.1523/JNEUROSCI.3784-12.2013).) The discussion of data quality issues (inconsistencies in the original White et al. data, corrections based on re-examination) is a useful reminder that even "complete" connectomes contain errors.

**Key figures:** Signal-flow visualization of the wiring diagram; degree and multiplicity distributions; network motifs; activity propagation analysis

**Discussion prompts:**
- How do the network properties of *C. elegans* compare with larger connectomes (fly, mouse)?
- What are the limitations of analyzing a connectome from a single individual?
- How should gap junctions versus chemical synapses be integrated in network analysis?

**Related content:** [C. elegans revisited](/content-library/case-studies/c-elegans-revisited/), [Graph representations](/content-library/connectomics/graph-representations/)

---

## 4. Schlegel et al. (2024) — Whole-Brain Annotation and Multi-Connectome Cell Typing

**Citation:** Schlegel P, Yin Y, Bates AS, Dorkenwald S, Eichler K, Brooks P, et al. Whole-brain annotation and multi-connectome cell typing of *Drosophila*. *Nature*. 2024;634(8032):139-152.
**DOI:** [10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5)

**Tags:** `connectomics:connectome-comparison` `connectomics:graph-theory` `cell-types:connectivity-based-classification` `case-studies:Drosophila` `case-studies:FlyWire` `methodology:reproducibility`

### Summaries

**Beginner:** If you map the brain of two different fruit flies, how similar are the wiring diagrams? This paper compared the FlyWire connectome with the hemibrain connectome (a different fly, different imaging method) and found that most connections are consistent between individuals. This is important because it means a connectome from one animal can teach us about the species, not just that individual.

**Intermediate:** Schlegel et al. compare two independently reconstructed connectomes of the adult fly brain (FlyWire and the hemibrain), annotating 8,453 cell types in FlyWire, of which 3,643 were previously proposed in the hemibrain. They quantify connectivity stereotypy between matched cell types in the two datasets. Results show broad stereotypy with occasional variability in neuron count and connectivity, simple heuristics for which connections are reliable across brains, and evidence in the mushroom body that the total excitatory input can change while the excitation/inhibition ratio is maintained.

**Advanced:** This paper sets out a framework for comparing connectomes, and asks: What is biological variability versus reconstruction error? How should connection strength be normalized for comparison? Which statistical tests are appropriate for comparing connectivity matrices? The cell type matching pipeline uses a combination of morphological similarity (NBLAST), neuropil innervation patterns, and connectivity fingerprints. About one-third of cell types proposed for the hemibrain could not be reliably reidentified in FlyWire, which led the authors to define a cell type as a group of cells that are each more similar to cells in another brain than to any other cell in the same brain. Because weak connections are less reliable across brains, detecting differences in them requires more replicates than detecting differences in strong connections.

**Key figures:** Cross-dataset cell type matching; connectivity stereotypy; connection reliability heuristics; mushroom body input homeostasis

**Discussion prompts:**
- How many connectomes are needed to establish "normal" wiring with statistical confidence?
- How should you distinguish biological variability from reconstruction artifacts in cross-dataset comparisons?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 5. MICrONS Consortium (2025) — Functional Connectomics Spanning Multiple Areas of Mouse Visual Cortex

**Citation:** MICrONS Consortium, Bae JA, Baptiste M, Baptiste MR, Bishop CA, Bodor AL, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640(8058):435-447. Preprint: *bioRxiv* 2021, [doi:10.1101/2021.07.28.454025](https://doi.org/10.1101/2021.07.28.454025).
**DOI:** [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)

**Tags:** `connectomics:graph-theory` `connectomics:community-detection` `neuroai:structure-function` `case-studies:MICrONS` `case-studies:mouse` `case-studies:visual-cortex` `methodology:experimental-design`

### Summaries

**Beginner:** Can you predict what a neuron does (its function) from how it is wired (its connections)? This study from the MICrONS project first recorded the activity of thousands of neurons in a living mouse watching visual stimuli, then mapped all their connections using electron microscopy. Combining the recordings with the wiring diagram lets researchers test whether neurons that respond similarly to visual stimuli tend to connect to each other. A companion paper (Ding et al. 2025) reports that they do, within and across layers and areas.

**Intermediate:** The MICrONS Consortium present the functional connectomics dataset: two-photon calcium imaging of about 75,000 neurons in primary and higher visual areas of mouse visual cortex, followed by serial-section EM reconstruction of about 1 mm³ of the same tissue (more than 200,000 cells, about 524 million synapses). This paper describes the resource and its data products. The structure-function tests are in companion papers; Ding et al. (2025, *Nature* 640:459-469) report "like-to-like" connectivity within and across layers and areas, and that the feature component of tuning, not receptive-field location, predicts fine-scale connections beyond axon-dendrite proximity.

**Advanced:** This dataset makes it possible to test Hebbian-like wiring rules across a cubic millimeter of cortex. The hard technical steps are registering the in vivo two-photon volume to the ex vivo EM volume, matching cells across the two, and controlling for the fact that nearby neurons are more likely to connect whatever their tuning. When you read the companion analyses, check how each one handles distance dependence and proofreading completeness, since both can produce or hide an apparent wiring rule.

**Key figures:** Fig. 1 (data types and data products), Fig. 2 (data acquisition workflow), Fig. 3 (in vivo calcium imaging), Fig. 4 (EM dataset registered to the two-photon data), Fig. 7 (connectivity matrices)

**Discussion prompts:**
- How strong would a structure-function relationship need to be to change how you model cortex, and how would you measure it?
- What experimental improvements would strengthen the co-registration between functional and structural data?

**Related content:** [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/)

---

## 6. Cook et al. (2019) — Whole-Animal Connectomes of Both C. elegans Sexes

**Citation:** Cook SJ, Jarrell TA, Brittin CA, Wang Y, Bloniarz AE, Yakovlev MA, et al. Whole-animal connectomes of both *Caenorhabditis elegans* sexes. *Nature*. 2019;571(7763):63-71.
**DOI:** [10.1038/s41586-019-1352-7](https://doi.org/10.1038/s41586-019-1352-7)

**Tags:** `connectomics:graph-theory` `connectomics:connectome-comparison` `case-studies:C-elegans` `case-studies:whole-brain` `case-studies:dense-reconstruction` `methodology:reproducibility`

### Summaries

**Beginner:** The worm *C. elegans* comes in two sexes: hermaphrodite and male. This study mapped the complete nervous system of both sexes, showing that the shared (non-sex-specific) circuits are largely similar while the sex-specific neurons add distinct circuitry for mating behavior. Having two complete connectomes from the same species allows comparison of what is consistent versus what varies.

**Intermediate:** Cook et al. present complete connectomes for both *C. elegans* sexes, extending the classic White et al. (1986) hermaphrodite connectome with a complete male nervous system (385 neurons, including the male-specific neurons). The comparative analysis reveals: (1) the shared nervous system is highly conserved between sexes with quantitative differences in connection strength; (2) several sex-shared neurons that function in sexual behavior are dimorphic in structure and connectivity, and inputs from sex-specific circuitry reveal points where sexual and non-sexual pathways converge.

**Advanced:** This paper is a reference point for studying connectomic variation within a species. Points to take from it: (1) many connections in sex-shared pathways differ in strength between the sexes, so "conserved" connectivity has to be defined before it is claimed; (2) the question of how sex-specific circuits attach to a shared backbone; (3) the technical challenges of comparing connectomes across datasets with different acquisition and reconstruction parameters. The reconstructions combine new and previously published electron micrographs, updating the original White et al. results.

**Key figures:** Sex comparison overview; connectivity matrices from sensory input to end-organ output; shared vs. dimorphic connectivity

**Discussion prompts:**
- How does sexual dimorphism in wiring compare with transcriptomic sexual dimorphism?
- What does the way sex-specific circuits connect to shared circuitry suggest about circuit evolution?

**Related content:** [C. elegans revisited](/content-library/case-studies/c-elegans-revisited/), [Graph representations](/content-library/connectomics/graph-representations/), [Connectome history](/content-library/connectomics/connectome-history/)

---

## 7. Dorkenwald et al. (2024) — Neuronal Wiring Diagram of an Adult Brain

**Citation:** Dorkenwald S, Matsliah A, Sterling AR, Schlegel P, Yu SC, McKellar CE, et al. Neuronal wiring diagram of an adult brain. *Nature*. 2024;634(8032):124-138.
**DOI:** [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)

**Tags:** `connectomics:graph-theory` `connectomics:connectome-comparison` `case-studies:FlyWire` `case-studies:Drosophila` `case-studies:whole-brain`

### Summaries

**Beginner:** This paper presents the complete wiring diagram of an adult fruit fly brain, the FlyWire connectome. Every neuron in the brain was reconstructed from electron microscopy and its chemical synapses mapped, the first whole-brain connectome of an adult fly. With 139,255 neurons and about 54.5 million synapses, it is about 46 times larger by neuron count than the larval fly connectome.

**Intermediate:** Dorkenwald et al. present the FlyWire whole-brain connectome of an adult *Drosophila melanogaster*, reconstructed from a serial section electron microscopy volume using a combination of automated segmentation and large-scale community proofreading. The connectome comprises 139,255 neurons and about 54.5 million synapses. The paper describes the reconstruction pipeline, accuracy checks, and initial analyses including neuron categories, neuropil-level connectivity, left-right comparisons, and information flow.

**Advanced:** FlyWire goes beyond the hemibrain in coverage (whole brain versus part of the central brain) and in community proofreading at scale. Key technical contributions include: (1) the distributed proofreading framework that let hundreds of contributors correct segmentation errors; (2) automated synapse detection (Buhmann et al. 2021) attached to the proofread neurons; (3) a hierarchical annotation of neuron classes, with cell types described in the companion paper by Schlegel et al. The whole-brain coverage eliminates boundary effects that limited hemibrain analyses and enables systematic study of inter-hemispheric connectivity, commissural circuits, and brain-wide feedback pathways.

**Key figures:** Fig. 1 (whole-brain reconstruction), Fig. 2 (neuron categories by flow and superclass), Fig. 3 (neuron and connection sizes), Fig. 4 (neuropil projections and crossing neurons), Fig. 6 (information flow)

**Discussion prompts:**
- How does whole-brain coverage change the conclusions compared with the partial hemibrain dataset?
- What are the limitations of a single-animal connectome for understanding species-typical wiring?
- How should the community prioritize analyses of this dataset?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 8. Shapson-Coe et al. (2024) — A Petavoxel Fragment of Human Cerebral Cortex Reconstructed at Nanoscale Resolution

**Citation:** Shapson-Coe A, Januszewski M, Berger DR, Pope A, Wu Y, Blakely T, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
**DOI:** [10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)

**Tags:** `connectomics:graph-theory` `case-studies:human` `case-studies:H01` `neuroanatomy:synapse` `cell-types:neuron-classification`

### Summaries

**Beginner:** For the first time, a small piece of human brain — about one cubic millimeter from the temporal cortex — was reconstructed at the level of individual synapses. This is the H01 dataset, and it reveals the detailed wiring of about 57,000 cells, about 16,000 of them neurons; glia outnumber neurons about two to one. The reconstruction uncovered surprising features of human brain wiring, including unusual axonal structures and connectivity patterns not seen in other species.

**Intermediate:** Shapson-Coe et al. present the H01 dataset: a 1 mm³ fragment of human temporal cortex reconstructed at nanometer resolution using serial section electron microscopy and automated segmentation. The volume contains ~57,000 cells and ~150 million synapses. Findings reported in the abstract include: glia outnumber neurons about 2:1, with oligodendrocytes the most common cell; deep-layer excitatory neurons can be classified by the orientation of their dendrites; and among thousands of weak connections onto each neuron there are rare, powerful axonal inputs of up to 50 synapses. The paper also describes unusual axonal structures such as axon whorls. The dataset enables the first large-scale analysis of human cortical connectivity at synaptic resolution.

**Advanced:** The H01 dataset is the first EM connectomics dataset at scale from human tissue, raising both opportunities and challenges. Key findings: (1) the rare, powerful multi-synaptic inputs sit within a background of mostly single-synapse connections, which raises the question of whether a small number of strong connections carries disproportionate influence; (2) the presence of axon whorls of unknown function highlights how much remains to be discovered in human neuroanatomy; (3) deep-layer excitatory neurons fall into classes based on dendritic orientation. Technical challenges include: tissue from a surgical resection (epilepsy patient) rather than healthy tissue, incomplete neuropil coverage at the volume boundaries, and the computational cost of petascale reconstruction. The dataset establishes a methodological foundation for future human connectomics at larger scales.

**Key figures:** Reconstruction overview; cell census; dendritic orientation classes; strong multi-synaptic connections; axon whorls

**Discussion prompts:**
- How do the connectivity patterns in human cortex compare with those from mouse cortex datasets (e.g., MICrONS)?
- What are the implications of using pathological tissue for establishing "normal" human connectivity?
- How should human connectomics scale up from 1 mm³ to larger volumes?

**Related content:** [Graph representations](/content-library/connectomics/graph-representations/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)
