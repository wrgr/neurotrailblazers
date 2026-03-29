---
layout: page
title: "Journal Papers: Datasets & Case Studies"
permalink: /content-library/journal-papers/case-studies/
description: "Curated landmark connectomics papers with summaries at beginner, intermediate, and advanced levels."
dimension: case-studies
tags:
  - case-studies:C-elegans
  - case-studies:Drosophila
  - case-studies:mouse
  - case-studies:human
  - case-studies:FlyWire
  - case-studies:MICrONS
  - case-studies:H01
  - case-studies:dense-reconstruction
---

# Datasets & Case Studies Journal Papers

Landmark connectomics papers that defined the field — each presenting a major dataset or reconstruction. Each paper includes summaries at three expertise levels.

---

## 1. White et al. (1986) — The Structure of the Nervous System of C. elegans

**Citation:** White JG, Southgate E, Thomson JN, Brenner S. The structure of the nervous system of the nematode *Caenorhabditis elegans*. *Philosophical Transactions of the Royal Society of London B*. 1986;314(1165):1-340.
**DOI:** [10.1098/rstb.1986.0056](https://doi.org/10.1098/rstb.1986.0056)

**Tags:** `case-studies:C-elegans` `case-studies:whole-brain` `case-studies:dense-reconstruction` `imaging:serial-section` `imaging:TEM` `connectomics:graph-theory` `methodology:ground-truth`

### Summaries

**Beginner:** This is the paper that started connectomics. Published in 1986, it describes the complete wiring diagram of the roundworm *C. elegans* — all 302 neurons and roughly 5,000 chemical synapses, traced by hand from thousands of electron microscope images. It took over a decade to complete. Every subsequent connectomics project traces its intellectual lineage back to this work. If you read one paper in this field, this is it.

**Intermediate:** White et al. produced the first (and for decades, the only) complete nervous system wiring diagram. Using serial section TEM of multiple animals, they reconstructed all neurons, identified their synaptic connections, and classified the connections as chemical synapses or gap junctions. Key contributions include: a complete parts list (302 neurons, named and classified), a complete wiring diagram (adjacency matrix), and identification of circuit motifs underlying known behaviors (locomotion, feeding, sensory processing). The methodology — serial section TEM with manual tracing — remained the dominant approach for 25 years.

**Advanced:** This 340-page paper remains a model of thoroughness. Methodologically, it established practices still used today: multiple animals for verification, systematic documentation of every neuron and connection, and explicit accounting of reconstruction confidence. Limitations that became apparent later include: reliance on a small number of animals (introducing individual variability), missed connections subsequently identified by Cook et al. (2019), and the absence of quantitative synapse size data. The paper's classification of neuron types by morphology and connectivity anticipated modern computational approaches. The complete dataset, reanalyzed with modern graph theory tools, continues to yield new biological insights.

**Key figures:** Fig. 1-5 (nervous system overview), Appendix tables (complete connectivity matrices)

**Discussion prompts:**
- Which methodological limitations of 1986 have been resolved by modern connectomics, and which persist?
- What evidence in this paper is descriptive versus mechanistic?
- How would this project be designed differently today?

**Related content:** [C. elegans revisited](/content-library/case-studies/c-elegans-revisited/), [Connectome history](/content-library/connectomics/connectome-history/)

---

## 2. Kasthuri et al. (2015) — Saturated Reconstruction of a Volume of Neocortex

**Citation:** Kasthuri N, Hayworth KJ, Berger DR, Schalek RL, Conchello JA, Knowles-Barley S, et al. Saturated reconstruction of a volume of neocortex. *Cell*. 2015;163(3):633-647.
**DOI:** [10.1016/j.cell.2015.06.054](https://doi.org/10.1016/j.cell.2015.06.054)

**Tags:** `case-studies:mouse` `case-studies:dense-reconstruction` `imaging:ATUM` `imaging:serial-section` `neuroanatomy:synapse` `neuroanatomy:dendrite` `methodology:ground-truth`

### Summaries

**Beginner:** This paper mapped every single neuron, synapse, and glial cell in a tiny cube of mouse brain tissue. "Saturated" means nothing was left out — every object was identified and traced. The cube was tiny (about the width of a hair) but incredibly complex, containing thousands of synaptic connections. This was one of the first demonstrations that dense wiring maps could be created for mammalian brain tissue.

**Intermediate:** Kasthuri et al. performed dense reconstruction of a 1,500 μm³ volume of mouse somatosensory cortex using ATUM-SEM. All neuronal and glial profiles were segmented, all synapses were identified, and connectivity was fully mapped. Key findings: axonal boutons synapse on diverse targets rather than concentrating on single partners; synapse size varies over two orders of magnitude; and even in this small volume, non-random connectivity patterns are evident. The dataset became an important benchmark for segmentation algorithm development.

**Advanced:** This paper established the concept of "saturated reconstruction" — the explicit goal of identifying every object and connection within a volume, as opposed to sparse tracing of selected neurons. The methodological contribution extends beyond the biology: the paper defines completeness criteria, reports inter-annotator agreement, and provides the dataset as a benchmark. The volume size limitation (1,500 μm³, roughly one dendritic field) means that few neurons have complete arbors within the volume, raising questions about how to interpret truncated connectivity patterns. The finding that connectivity is non-random even at this scale motivated larger reconstruction efforts.

**Key figures:** Fig. 1 (saturated volume), Fig. 3 (synapse size distribution), Fig. 5 (connectivity matrix), Fig. 7 (wiring diagram)

**Discussion prompts:**
- What does "saturated" mean operationally, and how would you verify it in your own reconstruction?
- How do volume boundary effects affect conclusions about connectivity patterns?

**Related content:** [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [Synapse classification](/content-library/neuroanatomy/synapse-classification/)

---

## 3. MICrONS Consortium (2021) — Functional Connectomics Spanning Multiple Areas of Mouse Visual Cortex

**Citation:** MICrONS Consortium, Bae JA, Baptiste M, Bodor AL, Brittan D, Buchanan J, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *bioRxiv*. 2021.
**DOI:** [10.1101/2021.07.28.454025](https://doi.org/10.1101/2021.07.28.454025)

**Tags:** `case-studies:MICrONS` `case-studies:mouse` `case-studies:visual-cortex` `case-studies:dense-reconstruction` `neuroai:structure-function` `imaging:ATUM` `imaging:serial-section` `connectomics:graph-theory`

### Summaries

**Beginner:** The MICrONS project is one of the most ambitious connectomics efforts to date. Scientists first recorded the activity of tens of thousands of neurons in a living mouse as it watched visual stimuli, then removed that same piece of brain and mapped all the connections using electron microscopy. This creates a unique dataset where you can see both what each neuron does (its function) and who it connects to (its structure) — enabling direct tests of how wiring relates to function.

**Intermediate:** The MICrONS consortium produced a mm³ volume of mouse visual cortex with matched functional imaging (two-photon calcium imaging of ~75,000 neurons) and structural reconstruction (serial section EM with ~80,000 reconstructed neurons and ~524 million synapses). The functional-structural co-registration enables direct testing of structure-function hypotheses: are functionally similar neurons preferentially connected? The dataset spans multiple visual areas (V1, LM, AL) and all cortical layers, providing the most comprehensive functional connectomics resource for any mammalian brain region.

**Advanced:** MICrONS represents the convergence of multiple technical advances: large-scale two-photon imaging with single-cell resolution, petascale EM acquisition, FFN-based segmentation, and CAVE-based proofreading. The functional-structural matching required solving a challenging cross-modal registration problem (in vivo optical to ex vivo EM). Key caveats: calcium imaging provides noisy functional characterization (compared with electrophysiology), the EM volume boundaries truncate many neurons, and proofreading completeness varies across the volume. The structure-function correlations reported are modest in magnitude (~0.1-0.2), consistent with the view that connectivity reflects multiple organizing principles beyond functional similarity.

**Key figures:** Fig. 1 (experimental pipeline), Fig. 2 (EM volume overview), Fig. 5 (structure-function correlations)

**Discussion prompts:**
- What does the modest magnitude of structure-function correlations tell us about brain organization?
- How does the quality of functional characterization limit structural-functional analysis?
- What would you do differently in a next-generation functional connectomics experiment?

**Related content:** [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/)

---

## 4. Shapson-Coe et al. (2024) — A Petavoxel Fragment of Human Cerebral Cortex

**Citation:** Shapson-Coe A, Januszewski M, Berger DR, Pope A, Wu Y, Blakely T, et al. A connectomic study of a petascale fragment of human cerebral cortex. *Science*. 2024;384(6696):eadk4858.
**DOI:** [10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)

**Tags:** `case-studies:H01` `case-studies:human` `case-studies:dense-reconstruction` `imaging:serial-section` `imaging:SEM` `neuroanatomy:synapse` `neuroanatomy:dendrite` `cell-types:pyramidal-cell`

### Summaries

**Beginner:** This paper presents the first large-scale wiring map from a human brain. A small piece of temporal cortex (about 1 cubic centimeter) was removed during epilepsy surgery and mapped at nanometer resolution, revealing about 50,000 neurons and 130 million synapses. The human tissue showed several features never seen in mouse or fly brains, including unusually large neurons, rare multinucleated cells, and unique wiring patterns, suggesting that human brain organization differs from model organisms in important ways.

**Intermediate:** Shapson-Coe et al. present the H01 dataset: a petavoxel (~1.4 PB) serial section SEM volume of resected human temporal cortex at 4 nm lateral resolution. The reconstruction reveals ~50,000 neurons with ~130 million synapses across cortical layers 1-6. Key findings include: human-specific morphological features (large L3 pyramidal neurons with extensive basal dendrites), unusual connectivity patterns (axonal whorls, multinucleated neurons), and quantitative differences from rodent cortex (higher spine density, larger synapses). The dataset comes from a surgical specimen (epilepsy patient), raising questions about typicality.

**Advanced:** H01 is important as the first dense human connectomics dataset, but interpretation requires careful consideration of several factors: (1) the tissue source (epilepsy surgery specimen from a 45-year-old female) means some features may be pathological rather than typical; (2) fixation was delayed compared with perfusion-fixed mouse tissue, affecting ultrastructural preservation; (3) temporal cortex may differ from primary sensory cortex in connectivity patterns. The paper's most impactful contribution may be the catalog of human-specific features that were unknown from model organisms: the "deep axo-axonic" connections, the axonal whorls of unknown function, and the multinucleated neurons. These features challenge the assumption that mouse cortex is a sufficient model for human brain organization.

**Key figures:** Fig. 1 (volume overview), Fig. 2 (human-specific morphology), Fig. 4 (connectivity patterns), Fig. 6 (pathological features)

**Discussion prompts:**
- How should findings from a single pathological specimen be interpreted?
- Which human-specific features are likely general versus specific to temporal cortex or epilepsy?
- What would be needed to create a "healthy" human cortex connectomics dataset?

**Related content:** [H01 human cortex](/content-library/case-studies/h01-human-cortex/), [Soma ultrastructure](/content-library/neuroanatomy/soma-ultrastructure/)

---

## 5. Dorkenwald et al. (2024) — Neuronal Wiring Diagram of an Adult Brain (FlyWire)

**Citation:** Dorkenwald S, Matsliah A, Sterling AR, Schlegel P, Yu SC, McKellar CE, et al. Neuronal wiring diagram of an adult brain. *Nature*. 2024;634:124-138.
**DOI:** [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)

**Tags:** `case-studies:FlyWire` `case-studies:Drosophila` `case-studies:whole-brain` `case-studies:dense-reconstruction` `proofreading:crowd-sourced-proofreading` `infrastructure:CAVE` `connectomics:graph-theory`

### Summaries

**Beginner:** In 2024, scientists published the first complete wiring diagram of an adult animal brain — the fruit fly *Drosophila melanogaster*, with about 139,000 neurons and 50 million synaptic connections. This was accomplished through a massive collaborative effort: hundreds of researchers worldwide used a web-based tool to check and correct the computer-generated neuron shapes. The result is a complete "parts list and wiring manual" for a brain, enabling systematic study of how brain circuits produce behavior.

**Intermediate:** Dorkenwald et al. present the FlyWire connectome: a complete, proofread wiring diagram of the adult *Drosophila* brain. Built from the FAFB EM dataset (Zheng et al., 2018), the connectome was generated through FFN segmentation followed by community-scale proofreading via CAVE. Key features: ~139,000 neurons and ~50 million synapses; collaborative proofreading by 300+ contributors; cell type annotation for all neurons; freely available data and analysis tools. Initial analyses reveal brain-wide circuit architecture, including processing hierarchies, bilateral symmetry, and cell-type-specific wiring rules.

**Advanced:** FlyWire is the first whole-brain connectome at single-synapse resolution for an organism with complex behavior, making it a milestone comparable to White et al. (1986) for *C. elegans*. Key methodological contributions: (1) the crowd-sourced proofreading model that scaled human effort beyond what any single lab could achieve; (2) the CAVE infrastructure that enabled concurrent editing by hundreds of users; (3) the quality metrics framework that quantifies proofreading completeness. The connectome's completeness is not absolute: small-caliber neurites in the anisotropic EM volume have higher error rates, and some neuron types were proofread more thoroughly than others. Companion papers analyze cell types (Schlegel et al.), neuropeptide signaling (Dacks et al.), and specific circuits (multiple papers in the same Nature issue).

**Key figures:** Fig. 1 (whole-brain overview), Fig. 2 (reconstruction statistics), Fig. 3 (cell type diversity), Fig. 4 (circuit examples)

**Discussion prompts:**
- How should the completeness of a whole-brain connectome be assessed and reported?
- What are the next milestones after completing a wiring diagram — what questions does it answer versus open?
- How does the crowd-sourced model scale to larger brains (mouse, human)?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Connectome history](/content-library/connectomics/connectome-history/)

---

## 6. Zheng et al. (2018) — A Complete Electron Microscopy Volume of the Brain of Adult Drosophila

**Citation:** Zheng Z, Lauritzen JS, Perlman E, Robinson CG, Nichols M, Milkie D, et al. A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell*. 2018;174(3):730-743.e22.
**DOI:** [10.1016/j.cell.2018.06.019](https://doi.org/10.1016/j.cell.2018.06.019)

**Tags:** `case-studies:Drosophila` `case-studies:FAFB` `case-studies:whole-brain` `imaging:ATUM` `imaging:serial-section` `infrastructure:pipeline` `infrastructure:alignment`

### Summaries

**Beginner:** Before you can map a brain's wiring, you need to image the entire brain at high enough resolution to see individual connections. This paper describes how scientists imaged a complete adult fruit fly brain — producing about 21 million images that were stitched together into one continuous 3D picture. The imaging alone took years and produced ~50 terabytes of data. This dataset (called FAFB) became the foundation for the FlyWire wiring diagram project.

**Intermediate:** Zheng et al. produced the FAFB (Full Adult Fly Brain) dataset: the complete *Drosophila* brain imaged at ~4x4x40 nm resolution using automated tape-collecting ultramicrotomy (ATUM) and multi-microscope SEM. Key technical achievements: ~7,000 serial sections with only 36 unusable, multi-microscope parallelization for throughput, and computational alignment of ~21 million tile images. The paper demonstrates tracing of individual neurons across the full brain, validating that the image quality is sufficient for connectomics.

**Advanced:** FAFB is the imaging foundation of the FlyWire connectome and illustrates the engineering scale of modern connectomics. The ATUM workflow preserves sections (unlike SBEM), enabling re-imaging and troubleshooting. The 10x z-anisotropy (4 nm lateral, 40 nm axial) creates directional biases in segmentation accuracy — thin processes running in-plane are better resolved than those running axially. The paper's reporting of section loss rate, stitching quality, and alignment accuracy provides benchmarks for future projects. The multi-microscope parallelization strategy (partitioning the tape across instruments) was essential for practical timeline and was subsequently adopted by larger projects.

**Key figures:** Fig. 1 (whole-brain overview), Fig. 2 (ATUM workflow), Fig. 3 (section quality), Fig. 4 (neuron tracing examples)

**Discussion prompts:**
- How does section loss affect downstream reconstruction and what mitigation strategies exist?
- What imaging modality would you choose today if repeating this project from scratch?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [EM principles](/content-library/imaging/em-principles/), [Acquisition QA](/content-library/imaging/acquisition-qa/)

---

## 7. Cook et al. (2019) — Whole-Animal Connectomes of Both C. elegans Sexes

**Citation:** Cook SJ, Jarrell TA, Brittin CA, Wang Y, Bloniarz AE, Yakovlev MA, et al. Whole-animal connectomes of both *Caenorhabditis elegans* sexes. *Nature*. 2019;571(7763):63-71.
**DOI:** [10.1038/s41586-019-1352-7](https://doi.org/10.1038/s41586-019-1352-7)

**Tags:** `case-studies:C-elegans` `case-studies:whole-brain` `case-studies:dense-reconstruction` `connectomics:connectome-comparison` `connectomics:graph-theory` `methodology:reproducibility`

### Summaries

**Beginner:** The original *C. elegans* wiring diagram from 1986 mapped the hermaphrodite (the more common sex). This paper completes the picture by mapping the male nervous system too, and also corrects errors in the original reconstruction. The male has about 385 neurons (83 more than the hermaphrodite), with the extra neurons forming circuits for mating behavior. Comparing the two sexes shows which wiring is shared and which differs.

**Intermediate:** Cook et al. present updated connectomes for both *C. elegans* sexes, substantially revising the original White et al. (1986) hermaphrodite connectome and providing the first complete male connectome. They identified ~1,500 previously missed synapses in the hermaphrodite and mapped the complete male nervous system including 91 male-specific neurons. The comparative analysis reveals: shared circuits are quantitatively conserved between sexes, while male-specific neurons form modular additions that modify shared circuit function for reproductive behavior.

**Advanced:** This paper addresses a fundamental limitation of single-animal connectomics by incorporating data from multiple individuals and both sexes. The finding that ~1,500 synapses were missed in the original White et al. reconstruction (a ~25% increase in edge count) has sobering implications for the completeness claims of any connectome. The modular organization of sex-specific circuits — added as appendages to a conserved shared backbone rather than deeply integrated — suggests an evolutionary mechanism for circuit diversification. The quantitative conservation of shared connectivity between sexes (high correlation of connection strengths) establishes a baseline expectation for individual-to-individual variability in this species.

**Key figures:** Fig. 1 (sex comparison overview), Fig. 2 (updated hermaphrodite connectivity), Fig. 3 (male-specific circuits), Fig. 5 (shared vs. dimorphic connectivity)

**Discussion prompts:**
- What does the ~25% revision rate tell us about the reliability of other "complete" connectomes?
- How does the modular addition of sex-specific circuits inform our understanding of brain evolution?

**Related content:** [C. elegans revisited](/content-library/case-studies/c-elegans-revisited/), [Connectome history](/content-library/connectomics/connectome-history/)
