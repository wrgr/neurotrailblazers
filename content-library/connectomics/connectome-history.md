---
layout: page
title: "Connectome History"
permalink: /content-library/connectomics/connectome-history/
description: "The history of connectomics from Cajal to whole-brain wiring diagrams — milestones, methods, and lessons learned across four decades of mapping neural circuits."
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
---

## Overview

Connectomics — the systematic mapping of neural connections — has progressed from a single-organism, single-lab endeavor to a global, multi-petabyte field in roughly four decades. Understanding this trajectory helps practitioners appreciate why certain methods exist, what lessons have been learned (sometimes painfully), and where the field is headed.

---

## Instructor script: a chronological tour

### The pre-connectome era (1880s-1980s)

**Santiago Ramón y Cajal** (1852-1934) established the neuron doctrine: the brain is composed of discrete cells (neurons) that communicate at specialized junctions. Using the Golgi staining method — which, by a still-mysterious mechanism, labels only ~1% of neurons in a tissue sample — Cajal produced hundreds of exquisite drawings of neural circuits. These drawings were, in effect, the first wiring diagrams, though they captured morphology rather than verified synaptic connections.

Cajal's key insight: neurons have a directional flow of information — dendrites receive, axons transmit. This "law of dynamic polarization" anticipated the directed graphs that modern connectomics produces.

**Key limitation of the Cajal era:** Golgi staining shows individual cell morphology beautifully but cannot reliably identify synaptic connections between specific neurons. You can see the tree, but not which branches actually touch.

**Electron microscopy enters neuroscience (1950s-1960s):** The development of transmission EM revealed synaptic ultrastructure for the first time. Gray (1959) classified synapses into Type I (asymmetric, excitatory) and Type II (symmetric, inhibitory). Palay and colleagues established the ultrastructural vocabulary — vesicles, clefts, postsynaptic densities — that connectomics annotators still use today.

### The C. elegans connectome (1970s-1986)

**The landmark:** White JG, Southgate E, Thomson JN, Brenner S (1986). "The structure of the nervous system of the nematode *Caenorhabditis elegans*." *Philosophical Transactions of the Royal Society of London B* 314:1-340.

This 340-page monograph reported the first complete connectome of any organism: 302 neurons, approximately 7,000 chemical synapses, and approximately 900 gap junctions (electrical synapses).

**Why C. elegans was feasible:**
- Fixed cell lineage: every individual has exactly the same 302 neurons, with the same cell names and positions (Sulston et al. 1983)
- Small size: the entire nervous system fits within a ~1 mm body
- Transparent body: enables correlative light microscopy
- Genetic tractability: Sydney Brenner chose C. elegans specifically as a model for relating genes to behavior (Brenner 1974)

**Method:** Manual serial-section TEM. Physical ultrathin sections were cut, collected on grids, imaged on a TEM, and traced by hand. The project took approximately 15 years. Much of the tracing was performed by Nichol Thomson, working through stacks of photographic prints.

**Key findings from the original connectome:**
- Connectivity is non-random: certain connection patterns (motifs) occur far more often than expected by chance
- Bilateral symmetry with individual variation: left-right neuron pairs have similar but not identical connectivity
- The nerve ring (circumpharyngeal ring) is a central processing hub containing ~180 neurons
- Sexually dimorphic circuits: male and hermaphrodite wiring differs in specific circuits (later elaborated by Cook et al. 2019)

**Teaching point:** "Even with 302 neurons, the connectome took 15 years and required multiple subsequent revisions. This sets expectations for the challenge of larger organisms."

### The term "connectome" is coined (2005)

Two groups independently introduced the word:

- **Sporns O, Tononi G, Kötter R (2005)** "The human connectome: a structural description of the human brain." *PLoS Computational Biology* 1(4):e42. — Defined three scales: macro-connectome (brain region connections, from MRI), meso-connectome (neuron population projections, from tract tracing), and micro/nano-connectome (individual synapses, from EM).

- **Hagmann P (2005)** PhD thesis, EPFL. — Independently coined the same term in the context of diffusion MRI tractography.

The term catalyzed the field by providing a unified vocabulary and framing brain mapping as a systematic, completable project rather than an open-ended exploration.

### The macro-connectome era: Human Connectome Project (2010-present)

The NIH-funded **Human Connectome Project** (Van Essen et al. 2013) mapped brain-wide connectivity in ~1,200 healthy adults using diffusion MRI and resting-state fMRI. This is a different enterprise from EM connectomics — it maps tract-level connections between brain regions (macroscale), not synapse-level connections between individual neurons (nanoscale).

**Relevance to this course:** The HCP demonstrated that large-scale, systematic brain mapping is scientifically productive and fundable. It created infrastructure, data standards, and analysis tools that influenced the EM connectomics community. But it cannot resolve individual synapses — for that, we need electron microscopy.

### The volume EM revolution (2004-2015)

**Serial block-face SEM (SBEM):** Denk & Horstmann (2004) demonstrated automated volume EM: a diamond knife inside the SEM chamber cuts a thin layer, the exposed surface is imaged, and the process repeats. No manual section handling, no lost sections, automatic z-alignment.

**Focused ion beam SEM (FIB-SEM):** Knott et al. (2008) showed that a gallium ion beam could mill even finer layers (4-8 nm), achieving isotropic resolution for the first time.

**ATUM (Automated Tape-collecting Ultramicrotome):** Hayworth et al. (2014) enabled automated collection of thousands of ultrathin sections on tape, dramatically scaling serial-section TEM.

These technologies transformed connectomics from an artisanal craft to a scalable data-generation pipeline.

### Retinal connectomics proves functional relevance (2011-2013)

**Briggman KL, Helmstaedter M, Denk W (2011)** "Wiring specificity in the direction-selectivity circuit of the retina." *Nature* 471:183-188. — Combined SBEM with calcium imaging to show that direction-selective ganglion cells receive wiring that specifically implements their directional preference. This was a landmark because it connected structure (which neurons are connected) to function (direction selectivity) at the synaptic level.

**Helmstaedter M et al. (2013)** "Connectomic reconstruction of the inner plexiform layer in the mouse retina." *Nature* 500:168-174. — Reconstructed ~1,000 neurons in the inner plexiform layer, revealing precise wiring rules between bipolar cell types and ganglion cell types.

**Teaching point:** "Retinal connectomics proved that EM wiring diagrams can answer functional questions, not just describe anatomy. This justified the enormous investment required for larger-scale projects."

### Drosophila connectomics timeline (2013-2024)

The fruit fly brain became the proving ground for scaling connectomics:

| Year | Milestone | Scale | Reference |
|------|-----------|-------|-----------|
| 2013 | Medulla columns (7 columns) | ~800 neurons | Takemura et al. (2013) Nature |
| 2015 | Medulla expanded | ~1,500 neurons | Takemura et al. (2015) PNAS |
| 2018 | FAFB: complete adult brain EM volume | Imaging only (no full reconstruction) | Zheng et al. (2018) Cell |
| 2020 | Hemibrain connectome | ~25,000 neurons, ~20M synapses | Scheffer et al. (2020) eLife |
| 2023 | Larval brain connectome (complete) | ~3,016 neurons | Winding et al. (2023) Science |
| 2024 | FlyWire: whole adult brain connectome | ~139,255 neurons, ~54.5M synapses | Dorkenwald et al. (2024) Nature |

**The progression:** Column-level → hemisphere → complete adult brain. Each step required order-of-magnitude improvements in automated segmentation, proofreading infrastructure, and community coordination.

### Mammalian cortex milestones (2015-2024)

| Year | Milestone | Scale | Reference |
|------|-----------|-------|-----------|
| 2015 | Saturated reconstruction of mouse neocortex | ~1,500 μm³ (1,600 neurites) | Kasthuri et al. (2015) Cell |
| 2019 | Mouse cortex dense reconstruction | ~90,000 μm³ | Motta et al. (2019) Science |
| 2021 | MICrONS: mm³ mouse visual cortex + function | ~80,000 neurons, ~500M synapses | MICrONS Consortium (2021) bioRxiv |
| 2024 | H01: human cortex fragment | ~1 mm³, ~57,000 cells | Shapson-Coe et al. (2024) Science |

### The BRAIN CONNECTS era (2023-present)

The NIH **BRAIN Initiative CONNECTS** program funds large-scale connectomics projects:
- **MouseConnects/HI-MC**: ~10 mm³ mouse hippocampus (Lichtman, Jain, and collaborators)
- Additional funded projects targeting other brain regions and species

This represents an institutional commitment to connectomics as infrastructure — not just individual lab projects but community resources.

### Developmental connectomics (2021)

**Witvliet et al. (2021)** "Connectomes across development reveal principles of brain maturation." *Nature* 596:257-261. — Mapped the C. elegans connectome at 8 developmental time points, from L1 larva to adult. Key finding: the overall architecture is established early, but significant rewiring occurs during development — some connections strengthen, others weaken, and new connections form.

**Teaching point:** "A connectome is a snapshot. Development reminds us that wiring is dynamic, even within an individual."

---

## Key lessons from the field's history

1. **Completeness takes time**: Even 302 neurons took 15 years (C. elegans). Whole fly brain took the community ~6 years from volume to connectome.
2. **Automation is necessary but insufficient**: Every project required human proofreading after automated segmentation.
3. **Revisions are expected**: The C. elegans connectome has been revised multiple times (Varshney 2011, Cook 2019). Published connectomes should be treated as living datasets.
4. **Structure informs but doesn't determine function**: Retinal connectomics showed structure-function links, but Bargmann & Marder (2013) caution that wiring alone doesn't specify dynamics.
5. **Community infrastructure scales**: FlyWire showed that 287 distributed proofreaders can collectively reconstruct an entire brain.
6. **The field is accelerating**: The time from EM volume to published connectome is shrinking with each project.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "We've already mapped the brain" | We've mapped one worm, one fly, and small pieces of mouse and human cortex | Emphasize how much remains undone |
| "Cajal already drew the wiring diagram" | Cajal mapped morphology, not verified synaptic connections | Distinguish morphological inference from EM-verified connectivity |
| "The C. elegans connectome is finished" | It has been revised 3 times and still has gaps | Connectomes are living datasets |
| "Bigger volumes are always better" | The scientific question determines the required scale | Small, focused datasets can answer big questions |

---

## References

- Bargmann CI, Marder E (2013) "From the connectome to brain function." *Nature Methods* 10(6):483-490.
- Brenner S (1974) "The genetics of *Caenorhabditis elegans*." *Genetics* 77(1):71-94.
- Briggman KL, Helmstaedter M, Denk W (2011) "Wiring specificity in the direction-selectivity circuit of the retina." *Nature* 471:183-188.
- Cook SJ et al. (2019) "Whole-animal connectomes of both *Caenorhabditis elegans* sexes." *Nature* 571:63-71.
- DeFelipe J (2010) "From the connectome to the synaptome: an epic love story." *Science* 330(6008):1198-1201.
- Denk W, Horstmann H (2004) "Serial block-face scanning electron microscopy." *PLoS Biology* 2(11):e329.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.
- Hagmann P (2005) "From diffusion MRI to brain connectomics." PhD thesis, EPFL.
- Hayworth KJ et al. (2014) "Ultrastructurally smooth thick partitioning and volume stitching for large-scale connectomics." *Nature Methods* 12:319-322.
- Helmstaedter M et al. (2013) "Connectomic reconstruction of the inner plexiform layer in the mouse retina." *Nature* 500:168-174.
- Kasthuri N et al. (2015) "Saturated reconstruction of a volume of neocortex." *Cell* 162(3):648-661.
- Knott G et al. (2008) "Serial section scanning electron microscopy of adult brain tissue using focused ion beam milling." *Journal of Neuroscience* 28(12):2959-2964.
- MICrONS Consortium (2021) "Functional connectomics spanning multiple areas of mouse visual cortex." *bioRxiv*.
- Motta A et al. (2019) "Dense connectomic reconstruction in layer 4 of the somatosensory cortex." *Science* 366(6469):eaay3134.
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex." *Science* 384(6696):eadk4858.
- Sporns O, Tononi G, Kötter R (2005) "The human connectome: a structural description of the human brain." *PLoS Computational Biology* 1(4):e42.
- Van Essen DC et al. (2013) "The WU-Minn Human Connectome Project: an overview." *NeuroImage* 80:62-79.
- Varshney LR et al. (2011) "Structural properties of the *Caenorhabditis elegans* neuronal network." *PLoS Computational Biology* 7(2):e1001066.
- White JG et al. (1986) "The structure of the nervous system of *C. elegans*." *Philosophical Transactions of the Royal Society B* 314:1-340.
- Winding M et al. (2023) "The connectome of an insect brain." *Science* 379(6636):eadd9330.
- Witvliet D et al. (2021) "Connectomes across development reveal principles of brain maturation." *Nature* 596:257-261.
- Zheng Z et al. (2018) "A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*." *Cell* 174(3):730-743.
