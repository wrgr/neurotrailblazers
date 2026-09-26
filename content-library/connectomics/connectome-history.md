---
layout: page
title: "Connectome History"
permalink: /content-library/connectomics/connectome-history/
image: /assets/images/content-library/connectomics/connectome-history.svg
image_alt: "Stylized vector art: a network graph with one community circled."
description: "How connectomics got from Cajal's drawings to whole-brain wiring diagrams: the milestones, the methods that made each one possible, and what the first 40 years of synapse-level maps taught the field."
topics:
  - history
  - connectomics
  - milestones
  - C-elegans
  - drosophila
primary_units:
  - "01"
  - "09"
difficulty: "Foundational"
tags:
  - connectomics:history
  - connectomics:whole-brain
  - connectomics:dense-reconstruction
  - neuroanatomy:c-elegans
  - neuroanatomy:drosophila
  - neuroanatomy:mouse-cortex
  - neuroanatomy:human-cortex
  - imaging:serial-section-em
  - imaging:volume-em
  - infrastructure:flywire
  - infrastructure:microns
  - methodology:experimental-design
micro_lesson_id: ml-conn-history
combines_with:
  - graph-representations
  - network-analysis-methods
  - neuroai-bridge
content_type: core
---

## Overview

The first synapse-level wiring diagram, of the 302-neuron worm *C. elegans*, was published in 1986 after about 15 years of work by a small team in one lab. In 2024 a consortium of hundreds published one for a whole adult fly brain of 139,255 neurons. This page walks through what happened in between: which methods made each step possible, which results changed what people thought a connectome could answer, and what the field learned the hard way. Knowing that history explains why current pipelines look the way they do.

---

## Instructor script: a chronological tour

### The pre-connectome era (1880s-1980s)

**Santiago Ramón y Cajal** (1852-1934) argued for the neuron doctrine: the brain is made of discrete cells that communicate at specialized junctions. He used the Golgi method, which stains only a small, apparently random fraction of the neurons in a sample (often quoted as a few percent) by a mechanism that is still not fully understood. Because so few cells are stained, each one stands out whole, and Cajal drew hundreds of them. His drawings were early wiring diagrams in spirit, but they record morphology, not verified synaptic connections (DeFelipe 2010 tells the story).

Cajal also proposed that information flows one way through a neuron, from dendrites and soma to axon. This "law of dynamic polarization" is the reason a connectome is drawn as a directed graph.

**What Golgi staining cannot do:** it shows single cells in detail but cannot establish which cells synapse on which. You can see the tree, but not which branches actually touch.

**Electron microscopy enters neuroscience (1950s):** Transmission EM showed synaptic ultrastructure for the first time. Palay (1956) and his contemporaries described the synaptic vesicles, the cleft and the membrane thickenings that EM annotators still look for. Gray (1959) sorted cortical synapses into Type I (asymmetric) and Type II (symmetric); later work tied these mostly to excitatory and inhibitory synapses respectively.

### The C. elegans connectome (1969-1986)

**The landmark:** White JG, Southgate E, Thomson JN, Brenner S (1986). "The structure of the nervous system of the nematode *Caenorhabditis elegans*." *Philosophical Transactions of the Royal Society of London B* 314:1-340.

This 340-page monograph gave the first essentially complete wiring diagram of an animal's nervous system: 302 neurons in the hermaphrodite, grouped into 118 classes, connected by about 5,000 chemical synapses, 2,000 neuromuscular junctions and 600 gap junctions (electrical synapses), in the counts its abstract gives.

**Why C. elegans was feasible:**
- Invariant cell lineage: the embryonic lineage is essentially the same in every animal (Sulston et al. 1983), so each of the 302 neurons has a name and a predictable position
- Small size: the whole animal is about 1 mm long
- Transparent body: cells can be watched in the living animal, which is how the lineage was traced
- Genetic tractability: Sydney Brenner chose the worm as a model for relating genes to behavior (Brenner 1974)

**Method:** Manual serial-section TEM. Nichol Thomson cut long unbroken series of ultrathin sections and imaged them. Eileen Southgate printed the micrographs as 12 × 16 inch glossy prints, and she and John White traced each neuron through them by hand with ink pens. From White's start in 1969 to completion took about 15 years (Emmons 2015).

**What the 1986 paper established:**
- The structure is essentially invariant between animals, which is what made one reconstruction worth publishing
- Neurons have simple morphologies with few branches, run in defined positions within process bundles, and make most synapses *en passant*
- Neurons are mostly locally connected, synapsing with many of their neighbors

Several things often credited to the 1986 paper came later. Statistical findings such as over-represented motifs came from reanalyses of the diagram (Varshney et al. 2011). The male was a separate effort: the male tail circuits were completed by Jarrell et al. (2012), and the whole male connectome by Cook et al. (2019). Emmons (2015) also records that for the nerve ring, in contrast to the ventral cord, "no clear circuits were apparent in the wiring diagrams": having the map did not immediately explain the behavior.

**Teaching point:** "Even with 302 neurons, the connectome took about 15 years, and it has been revised and extended several times since. Set expectations for larger animals accordingly."

### The term "connectome" is coined (2005)

Two groups introduced the word independently in 2005:

- **Sporns O, Tononi G, Kötter R (2005)** "The human connectome: a structural description of the human brain." *PLoS Computational Biology* 1(4):e42. The paper proposed a research strategy for a human connection matrix and distinguished three scales: the microscale of single neurons and synapses, the mesoscale of neuronal groups such as minicolumns, and the macroscale of brain regions and the pathways between them. It argued the macroscale was the feasible starting point for humans.

- **Hagmann P (2005)** PhD thesis, EPFL, "From diffusion MRI to brain connectomics", used the same term for connectivity mapped with diffusion MRI tractography.

The word gave the field a shared name and framed brain mapping as a defined, finishable dataset rather than an open-ended survey.

### The macro-connectome era: the Human Connectome Project (2010 onward)

The NIH-funded **Human Connectome Project** (Van Essen et al. 2013) mapped brain-wide connectivity in about 1,200 healthy young adults using diffusion MRI and resting-state fMRI. This is a different enterprise from EM connectomics: it maps tract-level connections between brain regions (macroscale), not synapses between individual neurons.

**Relevance to this course:** The HCP showed that large, systematic brain mapping could be funded and could produce widely reused data, and its data standards and open-release practices influenced the EM community. It cannot resolve individual synapses. For that you need electron microscopy.

### Volume EM makes large reconstructions possible (2004-2015)

**Serial block-face SEM (SBEM):** Denk & Horstmann (2004) put an ultramicrotome inside the SEM chamber. A diamond knife cuts a thin layer, the exposed block face is imaged, and the cycle repeats. There are no sections to handle or lose, and consecutive images are already nearly aligned.

**Focused ion beam SEM (FIB-SEM):** Knott et al. (2008) applied focused ion beam milling to serial imaging of adult brain tissue. Because an ion beam removes much thinner layers than a diamond knife, FIB-SEM can reach near-isotropic voxels, at the cost of small imaged volumes.

**ATUM (Automated Tape-collecting Ultramicrotome):** ATUM (Hayworth et al. 2006) collects thousands of ultrathin sections on tape for later imaging by SEM; Hayworth et al. (2014) describe imaging these section libraries at scale with WaferMapper.

With automated sectioning and imaging, the bottleneck moved from acquiring images to reconstructing them, which is where it has stayed.

### EM wiring diagrams meet physiology (2011-2013)

Two *Nature* papers published back to back in March 2011 measured function in living tissue and then reconstructed the same cells with EM:

**Bock DD et al. (2011)** "Network anatomy and in vivo physiology of visual cortical neurons." *Nature* 471:177-182. Two-photon calcium imaging measured the preferred orientation of neurons in mouse primary visual cortex; serial-section TEM then traced part of their local network. Inhibitory interneurons received convergent input from excitatory neurons with a broad range of preferred orientations.

**Briggman KL, Helmstaedter M, Denk W (2011)** "Wiring specificity in the direction-selectivity circuit of the retina." *Nature* 471:183-188. Calcium imaging followed by SBEM of the same retina showed that starburst amacrine cell dendrites connect selectively to direction-selective ganglion cells according to each ganglion cell's preferred direction: the wiring matches the function.

**Helmstaedter M et al. (2013)** "Connectomic reconstruction of the inner plexiform layer in the mouse retina." *Nature* 500:168-174. A dense reconstruction of 950 neurons and their contacts, combining crowd-sourced annotation with machine-learning segmentation. It identified a new bipolar cell type and subdivided a known one by connectivity alone.

**Teaching point:** "These papers showed that EM wiring diagrams could test functional hypotheses, not only describe anatomy. That result is a large part of the case later made for funding bigger volumes."

### Drosophila connectomics timeline (2013-2024)

The fruit fly brain became the testing ground for scaling connectomics:

| Year | Milestone | Scale | Reference |
|------|-----------|-------|-----------|
| 2013 | Medulla columns | 379 neurons, 8,637 synaptic contacts | Takemura et al. (2013) Nature |
| 2015 | Seven medulla columns compared | Column-to-column circuit variation | Takemura et al. (2015) PNAS |
| 2018 | FAFB: complete adult brain EM volume | Imaging only (no full reconstruction) | Zheng et al. (2018) Cell |
| 2020 | Hemibrain connectome | ~25,000 neurons, ~20M synapses | Scheffer et al. (2020) eLife |
| 2023 | Larval brain connectome (complete) | 3,016 neurons, ~548,000 synapses | Winding et al. (2023) Science |
| 2024 | FlyWire: whole adult brain connectome | 139,255 neurons, ~54.5M synapses | Dorkenwald et al. (2024) Nature |

**The progression:** from a repeating column of one optic-lobe region, to half a central brain, to a whole adult brain. Each step needed better automated segmentation, more proofreading infrastructure and a larger group of people to coordinate.

### Mammalian cortex milestones (2015-2025)

| Year | Milestone | Scale | Reference |
|------|-----------|-------|-----------|
| 2015 | Saturated reconstruction of mouse neocortex | ~1,500 μm³ saturated | Kasthuri et al. (2015) Cell |
| 2019 | Mouse cortex dense reconstruction | ~500,000 μm³, ~400,000 synapses | Motta et al. (2019) Science |
| 2021 (preprint), 2025 (paper) | MICrONS: ~1 mm³ mouse visual cortex + calcium imaging | >200,000 cells, ~524M synapses | MICrONS Consortium (2025) Nature |
| 2024 | H01: human cortex fragment | ~1 mm³, ~57,000 cells, ~150M synapses | Shapson-Coe et al. (2024) Science |

### The BRAIN CONNECTS era (2023-present)

NIH's BRAIN Initiative Connectivity Across Scales (**BRAIN CONNECTS**) program announced its first awards on 26 September 2023: 11 grants projected to total $150 million over 5 years, with collaborators at over 40 institutions. The awards span electron microscopy pipelines for the mouse brain, DNA-barcoding methods for mapping projections, and imaging methods for human and non-human primate brains. Examples from NIH RePORTER:

- **[MouseConnects/HI-MC]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }})** (UM1NS132250, contact PI Jeff Lichtman, Harvard): a 10 mm³ volume of mouse hippocampal formation, pitched as a test of whether the pipeline could scale to a whole mouse brain, "50 times larger".
- A center for a high-throughput volume EM pipeline aimed at whole-mouse-brain connectomics (UM1NS132253, Allen Institute).
- Barcoded and trans-synaptic methods for mapping brain-wide connectivity of defined cell types (for example U01NS132161).
- Multi-scale imaging of axonal projections in macaque and human brains (UM1NS132358, the LINC center at Massachusetts General Hospital).

For connectomics this is a change of scale in how the work is funded: shared pipelines and community resources, not only single-lab projects.

### Developmental connectomics (2021)

**Witvliet et al. (2021)** "Connectomes across development reveal principles of brain maturation." *Nature* 596:257-261. The authors reconstructed the full brain of eight isogenic *C. elegans* individuals from birth (L1) to adulthood. The overall geometry of the brain was preserved, while chemical synapse numbers rose about sixfold. Existing connections strengthened and new ones formed; sensory and motor pathways remodeled substantially while the central decision-making circuitry was maintained. Individuals also differed from one another in a substantial fraction of their connections.

**Teaching point:** "A connectome is a snapshot of one animal at one age. Development shows that wiring changes, and comparing individuals shows that it varies."

---

## What the field's history teaches

1. **Completeness takes time, though less than it did.** 302 neurons took about 15 years (1969 to 1986). The FlyWire connectome of 139,255 neurons came about six years after the FAFB image volume was published (2018 to 2024).
2. **Automation is necessary but not sufficient.** Every project listed here needed human proofreading after automated segmentation. FlyWire estimates about 33 person-years of it; the hemibrain, over 50.
3. **Revisions are expected.** The *C. elegans* connectome has been revised and extended several times (Varshney et al. 2011, Jarrell et al. 2012, Cook et al. 2019). Treat a published connectome as a versioned dataset.
4. **Structure informs function but does not determine it.** Retinal and cortical studies found clear structure-function links, but Bargmann & Marder (2013) caution that wiring alone doesn't specify dynamics: neuromodulation and other factors also shape what a circuit does.
5. **Community infrastructure scales.** The FlyWire Consortium (287 researchers in at least 76 labs, plus citizen-science volunteers, per Princeton University's 2024 press release) reconstructed an entire brain on a shared platform.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "We've already mapped the brain" | Complete synapse-level maps exist for the worm (both sexes), the larval fly brain and the adult fly brain. For mouse and human there are pieces of about 1 mm³ | A mouse brain is about 500 mm³; say how much remains |
| "Cajal already drew the wiring diagram" | Cajal drew morphology from sparse Golgi stains, not verified synaptic connections | Distinguish morphological inference from EM-verified connectivity |
| "The C. elegans connectome is finished" | It has been revised and extended several times (e.g., Varshney et al. 2011, Cook et al. 2019), and Witvliet et al. (2021) showed that individuals differ | Connectomes are versioned datasets, and each is one animal |
| "Bigger volumes are always better" | The scientific question determines the required scale | The 2011 retina and cortex papers answered their questions with small volumes |

---

## References

- Bargmann CI, Marder E (2013) "From the connectome to brain function." *Nature Methods* 10(6):483-490.
- Bock DD et al. (2011) "Network anatomy and in vivo physiology of visual cortical neurons." *Nature* 471:177-182.
- Brenner S (1974) "The genetics of *Caenorhabditis elegans*." *Genetics* 77(1):71-94.
- Briggman KL, Helmstaedter M, Denk W (2011) "Wiring specificity in the direction-selectivity circuit of the retina." *Nature* 471:183-188.
- Cook SJ et al. (2019) "Whole-animal connectomes of both *Caenorhabditis elegans* sexes." *Nature* 571:63-71.
- DeFelipe J (2010) "From the connectome to the synaptome: an epic love story." *Science* 330(6008):1198-1201.
- Denk W, Horstmann H (2004) "Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure." *PLoS Biology* 2(11):e329.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.
- Emmons SW (2015) "The beginning of connectomics: a commentary on White et al. (1986)." *Philosophical Transactions of the Royal Society B* 370:20140309. [PMC4360118](https://pmc.ncbi.nlm.nih.gov/articles/PMC4360118/)
- Gray EG (1959) "Axo-somatic and axo-dendritic synapses of the cerebral cortex: an electron microscope study." *Journal of Anatomy* 93:420-433.
- Hagmann P (2005) "From diffusion MRI to brain connectomics." PhD thesis, EPFL.
- Hayworth KJ, Kasthuri N, Schalek R, Lichtman JW (2006) "Automating the collection of ultrathin serial sections for large volume TEM reconstructions." *Microscopy and Microanalysis* 12(S02):86-87.
- Hayworth KJ, Morgan JL, Schalek R, Berger DR, Hildebrand DGC, Lichtman JW (2014) "Imaging ATUM ultrathin section libraries with WaferMapper: a multi-scale approach to EM reconstruction of neural circuits." *Frontiers in Neural Circuits* 8:68.
- Helmstaedter M et al. (2013) "Connectomic reconstruction of the inner plexiform layer in the mouse retina." *Nature* 500:168-174.
- Jarrell TA et al. (2012) "The connectome of a decision-making neural network." *Science* 337(6093):437-444.
- Kasthuri N et al. (2015) "Saturated reconstruction of a volume of neocortex." *Cell* 162(3):648-661.
- Knott G, Marchman H, Wall D, Lich B (2008) "Serial section scanning electron microscopy of adult brain tissue using focused ion beam milling." *Journal of Neuroscience* 28(12):2959-2964.
- MICrONS Consortium et al. (2025) "Functional connectomics spanning multiple areas of mouse visual cortex." *Nature* 640:435-447. (Preprint: *bioRxiv*, 2021.)
- Motta A et al. (2019) "Dense connectomic reconstruction in layer 4 of the somatosensory cortex." *Science* 366(6469):eaay3134.
- NIH BRAIN Initiative (26 September 2023) "NIH BRAIN Initiative awards new projects to develop innovative brain mapping technologies." Award details from [NIH RePORTER](https://reporter.nih.gov/).
- Palay SL (1956) "Synapses in the central nervous system." *Journal of Biophysical and Biochemical Cytology* 2(4 Suppl):193-202.
- Princeton University (2 October 2024) press release on the FlyWire connectome, via [EurekAlert!](https://www.eurekalert.org/news-releases/1059340).
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384(6696):eadk4858.
- Sporns O, Tononi G, Kötter R (2005) "The human connectome: a structural description of the human brain." *PLoS Computational Biology* 1(4):e42.
- Sulston JE, Schierenberg E, White JG, Thomson JN (1983) "The embryonic cell lineage of the nematode *Caenorhabditis elegans*." *Developmental Biology* 100(1):64-119.
- Takemura SY et al. (2013) "A visual motion detection circuit suggested by *Drosophila* connectomics." *Nature* 500:175-181.
- Takemura SY et al. (2015) "Synaptic circuits and their variations within different columns in the visual system of *Drosophila*." *PNAS* 112(44):13711-13716.
- Van Essen DC et al. (2013) "The WU-Minn Human Connectome Project: an overview." *NeuroImage* 80:62-79.
- Varshney LR et al. (2011) "Structural properties of the *Caenorhabditis elegans* neuronal network." *PLoS Computational Biology* 7(2):e1001066.
- White JG, Southgate E, Thomson JN, Brenner S (1986) "The structure of the nervous system of the nematode *Caenorhabditis elegans*." *Philosophical Transactions of the Royal Society of London B* 314:1-340.
- Winding M et al. (2023) "The connectome of an insect brain." *Science* 379(6636):eadd9330.
- Witvliet D et al. (2021) "Connectomes across development reveal principles of brain maturation." *Nature* 596:257-261.
- Zheng Z et al. (2018) "A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*." *Cell* 174(3):730-743.
