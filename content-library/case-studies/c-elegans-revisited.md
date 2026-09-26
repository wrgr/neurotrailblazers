---
layout: page
title: "C. elegans Revisited"
permalink: /content-library/case-studies/c-elegans-revisited/
image: /assets/images/content-library/case-studies/c-elegans-revisited.svg
image_alt: "Stylized vector art: a specimen ring with landmark points beside a data band."
description: >
  Case study of the C. elegans connectome from White et al. (1986) through later
  re-analyses and developmental connectomics: how the field's first complete wiring
  diagram has been corrected and extended over four decades, and what that says
  about any connectome.
topics:
  - C. elegans
  - historical connectomics
  - serial-section TEM
  - developmental connectomics
  - connectome revisions
  - model organisms
  - gap junctions
  - circuit motifs
primary_units:
  - "01"
  - "09"
difficulty: beginner
tags:
  - case-studies:C-elegans
  - connectomics:whole-brain
  - connectomics:dense-reconstruction
  - connectomics:developmental
  - methodology:graph-theory
  - methodology:connectome-comparison
  - imaging:serial-section-TEM
  - neuroanatomy:nematode
  - proofreading:manual-tracing
micro_lesson_id: ml-case-celegans
combines_with:
  - flywire-whole-brain
  - h01-human-cortex
  - microns-visual-cortex
use_layout_hero: false
content_type: core
---

# C. elegans Revisited

> ### Before you quote a number from this page
>
> Synapse counts below are properties of **a particular reconstruction**, not of
> the worm. White et al. (1986), Varshney et al. (2011), Cook et al. (2019) and
> Witvliet et al. (2021) counted different animals, different body regions and
> different kinds of contact, and their numbers differ for those reasons. Before
> a figure reaches a paper, a talk or a grant, name the reconstruction it comes
> from. [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
> covers the habit.


## Overview

The connectome of the nematode *Caenorhabditis elegans* is where connectomics began.
Published by White, Southgate, Thomson, and Brenner in 1986 in the *Philosophical
Transactions of the Royal Society*, the original wiring diagram of this tiny worm's
302-neuron nervous system is still one of the most used datasets in neuroscience.
It took more than a decade of manual tracing through serial-section transmission
electron micrographs, all of it before any of the tools, algorithms or platforms in
the other case studies here existed.

Four decades later it is still being revised. Several groups have re-analyzed,
corrected and extended it. It has been the test bed for computational models of
neural circuits. Most recently it has been mapped across developmental stages, which
shows how a connectome changes over an animal's life. This case study follows that
history and the lessons it holds for brains millions of times larger.


## The Original Connectome: White et al. (1986)

### What Made It Possible

Three biological properties of *C. elegans* made it the obvious first organism for a
complete connectome:

1. **Invariant cell lineage.** Every *C. elegans* hermaphrodite has exactly 302
   neurons (males have 385). The developmental lineage of every cell is known and
   identical across individuals. Each neuron has a unique name (e.g., AVAL, AVAR,
   PVDL) and occupies a predictable position. This means that findings from one
   animal can be directly mapped onto another.

2. **Small size.** The entire animal is approximately 1 mm long. The nervous system
   is compact enough to be captured in a manageable number of serial sections (a few
   thousand), making complete reconstruction physically feasible with the technology
   of the 1970s and 1980s.

3. **Transparency.** The living animal is transparent, enabling correlative studies
   with light microscopy, laser ablation of identified neurons, and (later)
   optogenetic manipulation. This transparency meant that the connectome could be
   directly linked to behavioral experiments.

### The Method

The reconstruction used serial-section transmission electron microscopy (ssTEM).
The animal was fixed, embedded in resin, and cut into ultrathin serial sections
(approximately 50 nm thick). Each section was placed on a grid, imaged in a TEM, and
the resulting micrographs were printed on paper. Neurons were traced by hand across
consecutive sections, with researchers physically marking up prints and maintaining
notebooks of identified processes.

There was no automated segmentation, no digital image processing, and no 3D
visualization software. The reconstruction was an act of sustained manual labor and
expert neuroanatomical interpretation over more than a decade.

### The Dataset

The original White et al. (1986) paper reported:

- **302 neurons** in the hermaphrodite nervous system.
- **About 5,000 chemical synapses** (connections where neurotransmitter is released
  from a presynaptic terminal onto a postsynaptic target).
- **About 2,000 neuromuscular junctions.**
- **About 600 gap junctions** (electrical synapses that directly couple the cytoplasm
  of two neurons).

The neurons were classified into 118 classes based on morphology and position. The
connectivity was represented as an adjacency matrix listing the number of synapses
between each neuron pair.

### What the Original Map Made Possible

- **Specific, sparse wiring.** Identified neuron pairs are connected, most possible
  pairs are not, and the named classes let a connection in one animal be looked for
  in another. Later analyses asked how stereotyped that wiring really is; Witvliet
  et al. (2021) found substantial differences between individuals.

- **Circuit motifs, found later.** The formal counting of over-represented motifs
  (feedforward chains, reciprocal connections and the like) came after 1986, in
  network analyses such as Varshney et al. (2011). White et al. supplied the data
  those analyses needed.

- **The nerve ring.** Much of the connectivity sits in a dense ring of neuropil around
  the pharynx, which Witvliet et al. later treat as the worm's brain.

- **Sensory-to-motor pathways.** Tracing from sensory neurons through interneurons to
  motor neurons gave the first wiring-level description of a complete sensorimotor
  system, and the circuit hypotheses that laser-ablation studies then tested.

- **A hermaphrodite-only map.** White et al. mapped the hermaphrodite. The male, with
  its additional neurons (385 in total) and mating circuits, was mapped later; Cook et
  al. (2019) published whole-animal connectomes of both sexes.


## Re-Analysis and Updates

### Varshney et al. (2011)

Twenty-five years after the original publication, Varshney et al. revisited the
*C. elegans* connectome. They went back to White and colleagues' laboratory notebooks
and original electron micrographs to assign connections to the correct left or right
neuron, added new micrographs, and applied graph-theoretic methods that were not in
use in 1986.

Key contributions:

- Assembled a self-consistent wiring diagram of the somatic nervous system from White
  et al.'s data, later work, and new reconstructions; over 3,000 synaptic contacts
  (chemical synapses, gap junctions and neuromuscular junctions) were added or updated
  relative to the previous version of the wiring diagram.
- Provided the connectome in digital formats suitable for computational analysis.
- Performed network analysis, including degree distributions, small-world properties,
  central neurons, and over-represented network motifs.
- Tested how robust these network properties are to remaining errors in the wiring
  diagram.

### Cook et al. (2019)

Cook et al. gave the largest update so far, reconstructing both adult sexes from new
and previously published electron micrographs: 460 nodes for the hermaphrodite
(302 neurons, 132 muscles and 26 non-muscle end organs) and 579 for the male
(385 neurons, 155 muscles and 39 end organs). Their key contributions:

- Quantitative connectivity matrices spanning the whole animal, from sensory input to
  end-organ output, which is the information needed to model behavior.
- Updated earlier results, and added data on the male head.
- Showed that the nervous system differs between the sexes at multiple levels,
  including sex-shared neurons whose structure and connectivity are sexually
  dimorphic.
- Released the data in digital, machine-readable form.

### Lessons from the Revisions

The revisions carry three messages:

- **Errors persist in manually annotated datasets.** After more than a decade of
  careful work by expert neuroanatomists, the original dataset still needed thousands
  of synaptic contacts added or updated. That is not a criticism of White et al. It is
  a limit of manual annotation at this scale.
- **The big picture held up.** Later revisions updated connections and synapse counts,
  but the neuron classes and major pathways described in the original remain the
  foundation of the field.
- **Re-analysis is essential.** Every major connectomics dataset should be expected
  to contain errors and should be revisited as tools improve.


## Developmental Connectomics: Witvliet et al. (2021)

### The Question

A connectome is a snapshot of wiring at a single moment. Nervous systems develop,
mature and, in some organisms, degenerate. Because every *C. elegans* neuron can be
named in every animal, the worm let Witvliet et al. ask how a connectome changes over
an animal's life, neuron by neuron.

### The Study

Witvliet et al. (2021) used serial-section EM to reconstruct the full brain (the nerve
ring and its associated neurons) of eight isogenic hermaphrodites at different ages,
from birth (L1, shortly after hatching) to adulthood. Each time point required a
separate EM volume from a different animal.

### Key Findings

The abstract reports five patterns:

- **A stable scaffold.** The overall geometry of the brain is preserved from birth to
  adulthood.

- **Substantial change on that scaffold.** Chemical synaptic connectivity changes
  substantially over development; the total number of chemical synapses rises about
  six-fold, from roughly 1,300 at birth to roughly 8,000 in adults, counting the brain
  only.

- **Differential remodeling.** The central decision-making circuitry is maintained,
  whereas sensory and motor pathways substantially remodel.

- **A changing architecture.** With age, the brain becomes progressively more
  feedforward and discernibly modular.

- **Individual variability.** Comparing connectomes between individuals revealed
  substantial differences in connectivity that make each brain partly unique.

### Significance

The Witvliet et al. study was the first systematic mapping of how a whole brain's
connectome changes over an organism's development. It established that:

- A single time-point connectome is an incomplete picture. Development matters.
- Even in an organism with an invariant cell lineage, the connectome is not fully
  determined at birth, and individuals differ.


## The Model Organism Legacy

### Connectome-to-Behavior Pipeline

*C. elegans* was the first organism with a working pipeline from connectome to
behavior, and it remains one of the most complete:

1. **Connectome**: The complete wiring diagram identifies all possible circuit pathways.
2. **Genetic tools**: A large mutant collection and cell-specific promoters make it
   possible to target identified neurons, and the CeNGEN project profiled gene
   expression across the whole nervous system (Taylor et al. 2021).
3. **Laser ablation**: Individual identified neurons can be killed with a laser in
   the living animal, and the behavioral consequences observed.
4. **Optogenetics**: Specific neurons can be activated or silenced with light,
   enabling precise tests of circuit models derived from the connectome.
5. **Calcium imaging**: Neural activity can be recorded from identified neurons in
   behaving animals, linking connectome structure to dynamic function.
6. **Computational modeling**: The complete connectome has been used to build
   whole-nervous-system simulations (e.g., the OpenWorm project) that generate
   testable predictions.

The pipeline has been used to identify interneurons that drive behavioral decisions,
to work out circuits for sensory integration, and to relate network topology to the
behavioral repertoire. Each of those studies started from a named neuron in the
wiring diagram.

### Limitations as a Model

*C. elegans* has real limits as a model for larger brains:

- **302 neurons is not 100,000 or 100 billion.** The computational principles that
  govern a 302-neuron nervous system may not scale to larger brains with fundamentally
  different architectures.
- **No layered or columnar architecture.** The worm's brain is a nerve ring. It has
  none of the layered cortex, columnar organization or long-range recurrent loops
  that characterize vertebrate brains.
- **Stereotyped, but not identical.** The invariant cell lineage fixes which neurons
  exist, and much of the wiring is reproducible. Witvliet et al. still found
  substantial differences in connectivity between isogenic individuals, and in
  mammalian brains experience shapes connectivity far more.
- **Neuropeptide signaling.** *C. elegans* relies heavily on neuropeptide (wireless)
  signaling in addition to synaptic (wired) signaling. The connectome captures only
  the wired component, potentially missing a large fraction of neural communication.


## Discussion Questions for Instructors

1. White et al. (1986) took more than a decade to reconstruct 302 neurons. FlyWire reconstructed
   ~139,000 neurons in a few years. What changed, and what stayed the same?
2. The original connectome needed thousands of synaptic contacts added or updated
   decades later. What does this imply for modern connectomics datasets that are orders of
   magnitude larger?
3. Witvliet et al. showed that the connectome changes during development. How should
   this inform the interpretation of single-time-point connectomes from other species?
4. *C. elegans* has an invariant cell lineage, meaning every animal has the same 302
   neurons. How does this simplify connectomics, and what does it mean for
   generalizability?
5. The OpenWorm project aims to simulate the entire *C. elegans* nervous system from
   the connectome. What additional information beyond connectivity would be needed for
   an accurate simulation?


## Key References

- White, J. G., Southgate, E., Thomson, J. N., & Brenner, S. (1986). The structure of
  the nervous system of the nematode *Caenorhabditis elegans*. *Philosophical
  Transactions of the Royal Society B*, 314(1165), 1-340.
  [10.1098/rstb.1986.0056](https://doi.org/10.1098/rstb.1986.0056)
- Varshney, L. R., Chen, B. L., Paniagua, E., Hall, D. H., & Chklovskii, D. B. (2011).
  Structural properties of the *Caenorhabditis elegans* neuronal network. *PLoS
  Computational Biology*, 7(2), e1001066.
  [10.1371/journal.pcbi.1001066](https://doi.org/10.1371/journal.pcbi.1001066)
- Cook, S. J., et al. (2019). Whole-animal connectomes of both *Caenorhabditis
  elegans* sexes. *Nature*, 571(7763), 63-71.
  [10.1038/s41586-019-1352-7](https://doi.org/10.1038/s41586-019-1352-7)
- Witvliet, D., et al. (2021). Connectomes across development reveal principles of
  brain maturation. *Nature*, 596(7871), 257-261.
  [10.1038/s41586-021-03778-8](https://doi.org/10.1038/s41586-021-03778-8)
- Taylor, S. R., et al. (2021). Molecular topography of an entire nervous system.
  *Cell*, 184(16), 4329-4347. [10.1016/j.cell.2021.06.023](https://doi.org/10.1016/j.cell.2021.06.023)
- Brenner, S. (1974). The genetics of *Caenorhabditis elegans*. *Genetics*, 77(1),
  71-94. [10.1093/genetics/77.1.71](https://doi.org/10.1093/genetics/77.1.71)
