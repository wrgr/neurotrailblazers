---
layout: page
title: "Journal Papers: Datasets & Case Studies"
permalink: /content-library/journal-papers/case-studies/
description: "Ten papers that each present a major connectomics dataset or reconstruction, with summaries at beginner, intermediate, and advanced levels."
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
use_layout_hero: false
content_type: core
---

# Datasets & Case Studies Journal Papers

Ten papers, each presenting a major connectomics dataset or reconstruction. Each paper has summaries at three expertise levels.

---

## 1. White et al. (1986) — The Structure of the Nervous System of C. elegans

**Citation:** White JG, Southgate E, Thomson JN, Brenner S. The structure of the nervous system of the nematode *Caenorhabditis elegans*. *Philosophical Transactions of the Royal Society of London B*. 1986;314(1165):1-340.
**DOI:** [10.1098/rstb.1986.0056](https://doi.org/10.1098/rstb.1986.0056)

**Tags:** `case-studies:C-elegans` `case-studies:whole-brain` `case-studies:dense-reconstruction` `imaging:serial-section` `imaging:TEM` `connectomics:graph-theory` `methodology:ground-truth`

### Summaries

**Beginner:** Published in 1986, this paper describes the first complete wiring diagram of an animal's nervous system: the 302 neurons of the roundworm *C. elegans* hermaphrodite and about 5,000 chemical synapses, 2,000 neuromuscular junctions and 600 gap junctions, traced by hand from thousands of electron micrographs. Later connectomics projects measure themselves against it.

**Intermediate:** White et al. produced the first (and for decades, the only) complete nervous system wiring diagram. Using serial section TEM of multiple animals, they reconstructed all neurons, identified their synaptic connections, and classified the connections as chemical synapses or gap junctions. Key contributions include a complete parts list (302 neurons in 118 classes, named and described) and a wiring diagram of their synaptic partners. Serial-section TEM with manual tracing stayed the standard method until automated segmentation arrived in the 2000s.

**Advanced:** This 340-page paper is still a model of thoroughness. It set practices still used today: several animals for cross-checking and systematic documentation of every neuron and its connections. Limitations that became apparent later include: reliance on a small number of animals (introducing individual variability), missed connections subsequently identified by Cook et al. (2019), and the absence of quantitative synapse size data. The paper's classification of neuron types by morphology and connectivity anticipated modern computational approaches. Reanalyses of the data with graph methods are still being published.

**Key figures:** The appendix of neuron-class descriptions, which gives each class's morphology and synaptic partners.

**Discussion prompts:**
- Which methodological limitations of 1986 have been resolved by modern connectomics, and which persist?
- What evidence in this paper is descriptive versus mechanistic?
- How would this project be designed differently today?

**Related content:** [C. elegans revisited](/content-library/case-studies/c-elegans-revisited/), [Connectome history](/content-library/connectomics/connectome-history/)

---

## 2. Kasthuri et al. (2015) — Saturated Reconstruction of a Volume of Neocortex

**Citation:** Kasthuri N, Hayworth KJ, Berger DR, Schalek RL, Conchello JA, Knowles-Barley S, et al. Saturated reconstruction of a volume of neocortex. *Cell*. 2015;162(3):648-661.
**DOI:** [10.1016/j.cell.2015.06.054](https://doi.org/10.1016/j.cell.2015.06.054)

**Tags:** `case-studies:mouse` `case-studies:dense-reconstruction` `imaging:ATUM` `imaging:serial-section` `neuroanatomy:synapse` `neuroanatomy:dendrite` `methodology:ground-truth`

### Summaries

**Beginner:** This paper mapped every single neuron, synapse, and glial cell in a tiny cube of mouse brain tissue. "Saturated" means nothing was left out — every object was identified and traced. The volume was far smaller than a grain of sand but still contained thousands of synaptic connections. This was one of the first demonstrations that dense wiring maps could be created for mammalian brain tissue.

**Intermediate:** Kasthuri et al. performed dense reconstruction of a 1,500 μm³ volume of mouse somatosensory cortex using ATUM-SEM. All neuronal and glial profiles were segmented, all synapses were identified, and connectivity was fully mapped. Key finding: by tracing every excitatory axon and noting each place it touches a dendritic spine, synaptically or not, the authors showed that physical proximity alone does not predict which pairs form synapses (a test of the so-called Peters' rule). The reconstruction is itemized in an online, minable database. The dataset became an important benchmark for segmentation algorithm development.

**Advanced:** This paper established the concept of "saturated reconstruction" — the explicit goal of identifying every object and connection within a volume, as opposed to sparse tracing of selected neurons. The methodological contribution extends beyond the biology: the paper itemizes every cellular object and many subcellular components (synapses, vesicles, spines, mitochondria) in a public database that others can query and use as a benchmark. The small volume (1,500 μm³, a cube about 11 μm on a side) means that few neurons, if any, have complete arbors inside it, raising questions about how to interpret truncated connectivity patterns. The finding that proximity does not determine connectivity, even at this scale, motivated larger reconstruction efforts.

**Key figures:** Look for the renderings of the saturated volume, the synapse and spine measurements, and the axon-spine contact analysis that tests Peters' rule.

**Discussion prompts:**
- What does "saturated" mean operationally, and how would you verify it in your own reconstruction?
- How do volume boundary effects affect conclusions about connectivity patterns?

**Related content:** [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [Synapse classification](/content-library/neuroanatomy/synapse-classification/)

---

## 3. MICrONS Consortium (2025) — Functional Connectomics Spanning Multiple Areas of Mouse Visual Cortex

**Citation:** MICrONS Consortium, Bae JA, Baptiste M, Baptiste MR, Bishop CA, Bodor AL, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640(8058):435-447. Preprint: *bioRxiv* 2021, [doi:10.1101/2021.07.28.454025](https://doi.org/10.1101/2021.07.28.454025).
**DOI:** [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)

**Tags:** `case-studies:MICrONS` `case-studies:mouse` `case-studies:visual-cortex` `case-studies:dense-reconstruction` `neuroai:structure-function` `imaging:ATUM` `imaging:serial-section` `connectomics:graph-theory`

### Summaries

**Beginner:** MICrONS is one of the largest connectomics projects to date. Scientists first recorded the activity of tens of thousands of neurons in a living mouse as it watched visual stimuli, then removed that same piece of brain and mapped all the connections using electron microscopy. The result is a dataset where you can see both what many neurons do (their function) and what they connect to (their structure), so you can test how wiring relates to function.

**Intermediate:** The MICrONS consortium produced about 1 mm³ of mouse visual cortex with matched functional imaging (two-photon calcium imaging of about 75,000 neurons) and structural reconstruction (serial-section EM containing more than 200,000 cells and about 524 million synapses). The volume spans primary visual cortex and three higher visual areas (RL, AL and LM) across all cortical layers. This paper describes the resource; the structure-function analyses, such as whether functionally similar neurons connect preferentially, are in companion papers published alongside it.

**Advanced:** MICrONS represents the convergence of multiple technical advances: large-scale two-photon imaging with single-cell resolution, petascale EM acquisition, convolutional-network affinity-based segmentation, and CAVE-based proofreading. The functional-structural matching required solving a challenging cross-modal registration problem (in vivo optical to ex vivo EM). Key caveats: calcium imaging provides noisy functional characterization (compared with electrophysiology), the EM volume boundaries truncate many neurons, and proofreading completeness varies across the volume. For the structure-function results, read the companion papers: Ding et al. (2025, *Nature* 640:459-469) report that neurons with similar response properties are more likely to connect, within and across layers and areas. Check the effect sizes there before generalizing.

**Key figures:** Fig. 1 (data types and data products), Fig. 2 (data acquisition workflow), Fig. 4 (EM dataset), Fig. 5 (reconstruction), Fig. 7 (connectivity matrices)

**Discussion prompts:**
- How large are the structure-function effects reported in the companion papers, and what size of effect would change how you think about cortical wiring?
- How does the quality of functional characterization limit structural-functional analysis?
- What would you do differently in a next-generation functional connectomics experiment?

**Related content:** [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/)

---

## 4. Shapson-Coe et al. (2024) — A Petavoxel Fragment of Human Cerebral Cortex

**Citation:** Shapson-Coe A, Januszewski M, Berger DR, Pope A, Wu Y, Blakely T, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384(6696):eadk4858.
**DOI:** [10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)

**Tags:** `case-studies:H01` `case-studies:human` `case-studies:dense-reconstruction` `imaging:serial-section` `imaging:SEM` `neuroanatomy:synapse` `neuroanatomy:dendrite` `cell-types:pyramidal-cell`

### Summaries

**Beginner:** This paper presents the first large-scale wiring map from a human brain. A small piece of temporal cortex (about 1 cubic millimeter) was removed during epilepsy surgery and mapped at nanometer resolution, revealing about 57,000 cells and 150 million synapses. The tissue showed several surprising features, including more glia than neurons, rare but very strong connections between single axons and single neurons, and unusual axon structures, which raise questions about how well model organisms represent human cortex.

**Intermediate:** Shapson-Coe et al. present the H01 dataset: a petavoxel (~1.4 PB) serial section SEM volume of about 1 mm³ of resected human temporal cortex at 4 nm lateral resolution. The reconstruction reveals ~57,000 cells with ~150 million synapses across cortical layers 1-6. Key findings in the abstract: glia outnumber neurons about 2:1, and oligodendrocytes are the most common cell; deep-layer excitatory neurons can be classified by the orientation of their dendrites; and among the thousands of weak inputs to each neuron are rare, powerful axonal inputs of up to 50 synapses. The dataset comes from a surgical specimen (epilepsy patient), raising questions about typicality.

**Advanced:** H01 is important as the first dense human connectomics dataset, but interpretation requires careful consideration of several factors: (1) the tissue source (a single epilepsy surgery specimen) means some features may be pathological rather than typical; (2) the tissue was immersion-fixed after surgical removal, not perfusion-fixed like the mouse volumes, which can affect ultrastructure; (3) temporal cortex may differ from primary sensory cortex in connectivity patterns. Its most discussed contribution may be its catalog of unexpected features, such as the rare multi-synapse axonal inputs, the dendritic-orientation classes of deep-layer neurons, and axon whorls of unknown function. Whether these are human-specific, region-specific or pathological is an open question that bears on how far mouse cortex can serve as a model for human brain organization.

**Key figures:** Volume overview; cell census; deep-layer dendritic orientation; strong multi-synaptic connections

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

**Beginner:** In 2024, scientists published the first complete wiring diagram of an adult animal brain — the fruit fly *Drosophila melanogaster*, with 139,255 neurons and about 54.5 million synapses. Hundreds of researchers worldwide used a web-based tool to check and correct the computer-generated neuron shapes, an estimated 33 person-years of proofreading. The result is a parts list and wiring diagram for a whole brain, which lets researchers study how its circuits produce behavior.

**Intermediate:** Dorkenwald et al. present the FlyWire connectome: a complete, proofread wiring diagram of the adult *Drosophila* brain. Built from the FAFB EM dataset (Zheng et al., 2018), the connectome was generated through convolutional-network segmentation followed by community-scale proofreading via CAVE. Key features: 139,255 neurons and about 54.5 million synapses; collaborative proofreading by hundreds of contributors; hierarchical annotations of every neuron (detailed in the companion paper by Schlegel et al.); freely available data and analysis tools. The paper's analyses cover neuron categories, neuropil-to-neuropil projections, left-right comparisons, information flow and the optic lobes.

**Advanced:** FlyWire is the first whole-brain connectome of an adult fly at synaptic resolution. Key methodological contributions: (1) a community proofreading model that scaled human effort beyond any single lab; (2) the ChunkedGraph and CAVE infrastructure that let hundreds of users edit concurrently; (3) explicit accuracy checks, such as re-proofreading 826 central-brain neurons, against which the released segments scored an average F1 of 99.2% by volume. The connectome's completeness is not absolute: small-caliber neurites in the anisotropic EM volume have higher error rates, and some neuron types were proofread more thoroughly than others. Companion papers analyze cell types (Schlegel et al.) and specific circuits (multiple papers in the same Nature issue).

**Key figures:** Fig. 1 (whole-brain reconstruction), Fig. 2 (neuron categories by flow and superclass), Fig. 3 (neuron and connection sizes), Fig. 4 (neuropil projections and crossing neurons), Fig. 6 (information flow through the central brain)

**Discussion prompts:**
- How should the completeness of a whole-brain connectome be assessed and reported?
- What are the next milestones after completing a wiring diagram — what questions does it answer versus open?
- How does the crowd-sourced model scale to larger brains (mouse, human)?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Connectome history](/content-library/connectomics/connectome-history/)

---

## 6. Zheng et al. (2018) — A Complete Electron Microscopy Volume of the Brain of Adult Drosophila

**Citation:** Zheng Z, Lauritzen JS, Perlman E, Robinson CG, Nichols M, Milkie D, et al. A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell*. 2018;174(3):730-743.e22.
**DOI:** [10.1016/j.cell.2018.06.019](https://doi.org/10.1016/j.cell.2018.06.019)

**Tags:** `case-studies:Drosophila` `case-studies:FAFB` `case-studies:whole-brain` `imaging:TEM` `imaging:serial-section` `infrastructure:pipeline` `infrastructure:alignment`

### Summaries

**Beginner:** Before you can map a brain's wiring, you need to image the entire brain at high enough resolution to see individual connections. This paper describes how scientists imaged a complete adult fruit fly brain — producing about 21 million camera images, about 106 terabytes, stitched together into one continuous 3D volume. This dataset (called FAFB) became the foundation for the FlyWire wiring diagram project.

**Intermediate:** Zheng et al. produced the FAFB (Full Adult Fly Brain) dataset: the complete *Drosophila* brain imaged at ~4x4x40 nm resolution using serial section transmission EM on a custom high-throughput platform (TEMCA2). Key technical achievements: about 7,050 serial sections imaged, multi-microscope parallelization for throughput, and computational alignment of ~21 million camera images. The paper demonstrates tracing of individual neurons across the full brain, validating that the image quality is sufficient for connectomics.

**Advanced:** FAFB is the imaging foundation of the FlyWire connectome and illustrates the engineering scale of modern connectomics. Serial section TEM preserves sections (unlike SBEM), enabling re-imaging and troubleshooting. The 10x z-anisotropy (4 nm lateral, 40 nm axial) creates directional biases in segmentation accuracy — thin processes running in-plane are better resolved than those running axially. The paper's reporting of section loss rate, stitching quality, and alignment accuracy provides benchmarks for future projects. Distributing sections across several microscopes kept the timeline practical; the MICrONS project later used the same strategy.

**Key figures:** Whole-brain overview; imaging platform and workflow; section quality; neuron tracing examples (mushroom body inputs)

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

**Intermediate:** Cook et al. present updated connectomes for both *C. elegans* sexes, substantially revising the original White et al. (1986) hermaphrodite connectome and providing the first complete male connectome. They reanalyzed previously published micrographs together with new ones, updated the hermaphrodite connectivity, and mapped the complete male nervous system, including the male-specific neurons. The comparative analysis reveals that several sex-shared neurons are dimorphic in structure and connectivity, that sex-specific circuits feed into central circuitry at identifiable convergence points, and that a substantial number of connections in sex-shared pathways differ in strength between the sexes.

**Advanced:** This paper revisits the classic single-animal data by combining new and previously published micrographs from both sexes. That the canonical 1986 wiring diagram needed updating has sobering implications for the completeness claims of any connectome. The way sex-specific circuits connect to a largely shared backbone raises questions about how circuits diversify during evolution. The differences in connection strength within sex-shared pathways also show that a shared wiring diagram does not imply shared weights.

**Key figures:** Fig. 1 (adult nervous system, neuroanatomy and connectivity), Fig. 3 (sensory streams entering the network), Fig. 5 (left-right and hermaphrodite-male comparisons), Fig. 6 (sexual pathways and dimorphic shared neurons)

**Discussion prompts:**
- What does the need to revise the 1986 connectome tell us about the reliability of other "complete" connectomes?
- How does the way sex-specific circuits attach to shared circuitry inform our understanding of brain evolution?

**Related content:** [C. elegans revisited](/content-library/case-studies/c-elegans-revisited/), [Connectome history](/content-library/connectomics/connectome-history/)

---

## 8. Takemura et al. (2013) — A Visual Motion Detection Circuit Suggested by Drosophila Connectomics

**Citation:** Takemura S, Bharioke A, Lu Z, Nern A, Vitaladevuni S, Rivlin PK, et al. A visual motion detection circuit suggested by Drosophila connectomics. *Nature*. 2013;500(7461):175-181.
**DOI:** [10.1038/nature12450](https://doi.org/10.1038/nature12450)

**Tags:** `case-studies:Drosophila` `case-studies:optic-lobe` `connectomics:graph-theory` `neuroanatomy:synapse` `neuroai:structure-function`

### Summaries

**Beginner:** This early connectomics study mapped the wiring of neurons in the fly's visual system to figure out how the brain detects motion. Scientists used electron microscopy to trace the connections between specific cell types in the fly's medulla (a visual processing region). By identifying which neurons connect to which, they proposed a circuit diagram that explains how the fly computes the direction of moving objects — showing that the physical wiring of the brain can predict the computations it performs.

**Intermediate:** Takemura et al. used serial section TEM to densely reconstruct columns of the *Drosophila* medulla, identifying the cell types and synaptic connections involved in motion detection. The reconstructed connectivity revealed a circuit architecture consistent with variants of the Hassenstein-Reichardt correlator model for elementary motion detection. The reconstruction contains 379 neurons and 8,637 chemical synaptic contacts. Key findings include: identification of the columnar cell types (notably Mi1 and Tm3) that provide input to motion-sensitive T4 cells, with spatially offset inputs consistent with each T4 cell's direction selectivity; quantitative synapse counts revealing connection strength differences between pathway branches; and a wiring diagram that predicts the computational algorithm (correlation of luminance signals across space and time). This was among the first demonstrations that connectomics data could directly constrain computational models.

**Advanced:** This paper is an example of targeted connectomics: reconstructing a specific circuit to answer a specific computational question, rather than pursuing whole-brain completeness. The motion detection circuit had been studied electrophysiologically and computationally for decades, but the cellular implementation remained disputed. The connectomic data proposed an answer by identifying candidate cell types and connections (the title says "suggested"). Methodological strengths include reconstruction of multiple columns for statistical power and explicit mapping from anatomy to algorithm. Limitations: the reconstruction covered a small number of columns, synapse identification relied on morphological criteria without functional validation, and the mapping from connectivity to computation required assumptions about synaptic sign (excitatory vs. inhibitory) that anatomy alone cannot settle. Later functional studies, such as Maisak et al. (2013), recorded direction-selective responses in T4 and T5 cells and tested parts of this picture.

**Key figures:** Fig. 1 (the motion detection model and the fly visual system), Fig. 2 (connectome reconstruction from serial-section EM), Fig. 4 (spatially offset Mi1 and Tm3 inputs onto a single T4 cell), Fig. 5 (displacements for all T4 cells)

**Discussion prompts:**
- How does targeted reconstruction of a specific circuit differ in strategy and outcome from dense whole-brain reconstruction?
- What additional data (beyond connectivity) was needed to go from wiring diagram to computational model?
- How should we evaluate the predictive power of a connectomics-derived circuit model?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/)

---

## 9. Bock et al. (2011) — Network Anatomy and In Vivo Physiology of Visual Cortical Neurons

**Citation:** Bock DD, Lee WCA, Kerlin AM, Andermann ML, Hood G, Wetzel AW, et al. Network anatomy and in vivo physiology of visual cortical neurons. *Nature*. 2011;471(7337):177-182.
**DOI:** [10.1038/nature09802](https://doi.org/10.1038/nature09802)

**Tags:** `case-studies:mouse` `case-studies:visual-cortex` `imaging:serial-section` `imaging:ATUM` `neuroai:structure-function` `methodology:correlative-imaging`

### Summaries

**Beginner:** This paper was one of the first to combine two techniques: watching neurons fire in a living mouse brain, and then mapping their connections with an electron microscope. Scientists first showed mice visual patterns and recorded which neurons responded to which orientations (using two-photon calcium imaging). Then they sliced and imaged the same piece of brain tissue to trace the wires between those neurons. They discovered that inhibitory neurons receive input from neurons with many different orientation preferences — meaning inhibition is broadly tuned, not selective.

**Intermediate:** Bock et al. performed correlative functional-structural imaging in mouse primary visual cortex. In vivo two-photon calcium imaging characterized orientation selectivity of neurons in a local patch of V1, after which the same tissue was processed for serial section EM and reconstructed. By matching functionally characterized neurons to their EM profiles, they traced synaptic inputs onto specific inhibitory interneurons. Key finding: inhibitory neurons receive synaptic input from excitatory neurons spanning the full range of orientation preferences, rather than from a functionally homogeneous subset. This broad connectivity provides a structural basis for non-selective inhibition in cortical circuits.

**Advanced:** This paper pioneered the correlative functional-structural approach that later scaled up dramatically in the MICrONS project. Registering the in vivo two-photon data to the ex vivo EM volume was hard; the paper matches in vivo fluorescence anatomy to the EM images. It also argues that the convergent input onto interneurons is predicted by the proximity of axons and dendrites rather than by function. The biological conclusion — that inhibitory neurons sample broadly from the local excitatory population — addressed a longstanding debate about the role of inhibition in sharpening tuning curves. Limitations include: the small number of reconstructed inhibitory neurons (constraining statistical power), the inability to identify all presynaptic partners (many axons could not be traced to their somata), and the use of calcium imaging rather than electrophysiology for functional characterization (limiting temporal resolution and sensitivity). Despite these limitations, the paper established a paradigm — function first, then structure — that became central to modern connectomics.

**Key figures:** Fig. 1 (functional characterization before reconstruction), Fig. 2 (large-scale EM), Fig. 3 (matching in vivo fluorescence anatomy to EM), Fig. 4 (convergent input onto inhibitory interneurons), Fig. 6 (convergence predicted by proximity, not function)

**Discussion prompts:**
- What are the advantages and limitations of correlative functional-structural approaches compared with purely structural connectomics?
- How does the finding of broadly tuned inhibitory input constrain models of orientation selectivity?
- What technical improvements since 2011 have addressed the limitations of this study?

**Related content:** [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/)

---

## 10. Witvliet et al. (2021) — Connectomes Across Development Reveal Principles of Brain Maturation

**Citation:** Witvliet D, Mulcahy B, Mitchell JK, Meirovitch Y, Berger DR, Wu Y, et al. Connectomes across development reveal principles of brain maturation. *Nature*. 2021;596(7871):257-261.
**DOI:** [10.1038/s41586-021-03778-8](https://doi.org/10.1038/s41586-021-03778-8)

**Tags:** `case-studies:C-elegans` `case-studies:dense-reconstruction` `connectomics:connectome-comparison` `neuroanatomy:synapse` `methodology:reproducibility`

### Summaries

**Beginner:** This paper asks how a brain's wiring changes as an animal grows up. Scientists mapped the brain wiring diagram of the roundworm *C. elegans* in eight animals at different ages during development, from a newly hatched larva to an adult. They found that the overall layout of the brain stays the same from birth to adulthood, but existing connections get stronger and new connections form on top of that stable scaffold. It was the first study to compare whole-brain connectomes across a developmental series.

**Intermediate:** Witvliet et al. reconstructed the brains (nerve ring and ventral ganglion) of eight isogenic *C. elegans* individuals spanning development from the first larval stage (L1) to adulthood. By comparing these connectomes, they identified consistent principles of brain maturation: (1) the overall geometry of the brain is preserved from birth to adulthood; (2) on that scaffold, chemical synaptic connectivity changes substantially, as existing connections strengthen and new connections are created; (3) the central decision-making circuitry is maintained while sensory and motor pathways remodel, and the network becomes more feedforward and more modular with age. Comparing individuals also revealed substantial differences in connectivity that make each brain partly unique.

**Advanced:** This is the first developmental connectomics study with multiple complete time points, enabling statistical analysis of wiring changes rather than pairwise comparison. The finding that a stable scaffold coexists with substantial strengthening and addition of connections raises the question of which parts of the wiring are genetically specified and which reflect experience-dependent plasticity or developmental programs. Methodological considerations include: inter-individual variability confounds developmental trends (each time point is a different animal), the definition of "same connection" across developmental stages requires careful cell identity tracking, and synapse count is a proxy for connection strength that may not capture other forms of plasticity (receptor composition, release probability). The dataset provides a unique resource for testing models of neural development and establishes baseline expectations for how much connectome variability is developmental versus individual.

**Key figures:** Fig. 1 (overall geometry maintained as synapses and connections increase), Fig. 2 (stereotyped and variable connections across isogenic individuals), Fig. 3 (increasing feedforward signaling and modularity), Fig. 4 (summary of maturation principles)

**Discussion prompts:**
- How should we separate developmental changes from individual-to-individual variability when each time point comes from a different animal?
- What does the stability of the brain's overall scaffold imply about the genetic versus activity-dependent specification of neural circuits?
- How might these developmental principles differ in organisms with larger, more plastic brains?

**Related content:** [C. elegans revisited](/content-library/case-studies/c-elegans-revisited/), [Connectome history](/content-library/connectomics/connectome-history/)
