---
layout: page
title: "Comparative Connectomics"
permalink: /content-library/connectomics/comparative-connectomics/
description: >
  What carries over between the worm, larval and adult fly, mouse and human
  connectomes, and what does not. Whole brains of small animals can be compared
  neuron by neuron and animal by animal; cubic-millimeter fragments of mammalian
  cortex cannot. Every number on the page is from the primary papers.
topics:
  - comparative connectomics
  - stereotypy and variability
  - cell types
  - dataset completeness
primary_units:
  - "09"
difficulty: intermediate
tags:
  - connectomics:whole-brain
  - connectomics:dense-reconstruction
  - neuroanatomy:c-elegans
  - neuroanatomy:drosophila
  - neuroanatomy:mouse-cortex
  - neuroanatomy:human-cortex
  - infrastructure:flywire
  - infrastructure:microns
  - methodology:connectome-comparison
  - methodology:experimental-design
micro_lesson_id: ml-conn-comparative
combines_with:
  - connectome-history
  - network-analysis-methods
  - motif-analysis
use_layout_hero: false
content_type: core
---

# Comparative Connectomics

Six reconstructions dominate teaching and analysis today: the *C. elegans*
hermaphrodite, the larval and adult *Drosophila* brains, the fly hemibrain,
the MICrONS cubic millimeter of mouse visual cortex and the H01 cubic
millimeter of human temporal cortex. They are often put in one table and
read as a ladder of size. That table is useful, but it hides the fact that
the six datasets answer different kinds of question. This page sets out
which findings and habits carry across species and which do not.

## The six datasets differ in coverage as much as in size

| Animal | Dataset | Coverage | Neurons | Synapses | Source |
|---|---|---|---|---|---|
| *C. elegans* (hermaphrodite) | White et al. | Whole nervous system | 302 | about 5,000 chemical synapses, 2,000 neuromuscular junctions, 600 gap junctions | White et al. 1986 |
| *Drosophila* larva | Winding et al. | Whole brain | 3,016 | about 548,000 | Winding et al. 2023 |
| *Drosophila* adult | FlyWire (FAFB) | Whole brain | 139,255 | about 54.5 million | Dorkenwald et al. 2024 |
| *Drosophila* adult | Hemibrain | A large part of one central brain | about 25,000 | about 20 million | Scheffer et al. 2020 |
| Mouse | MICrONS | About 1 mm³ of visual cortex | more than 200,000 cells | about 524 million | MICrONS Consortium 2025 |
| Human | H01 | About 1 mm³ of temporal cortex | 57,180 cells, 16,087 of them neurons | about 150 million | Shapson-Coe et al. 2024 |

The first three rows are complete brains. Every neuron's inputs and outputs
inside the brain are in the data, up to reconstruction error. The hemibrain
is part of one fly brain, so neurons that leave the volume are cut
off. The last two rows are fragments. A mouse brain is about 500 mm³ (Badea
et al. 2007), so MICrONS covers roughly one five-hundredth of it. Almost
every neuron in the mouse and human volumes has part of its dendrites or
axon outside the block.

Two further differences are easy to miss when reading the table:

- **Synapse counts mean different things.** White et al. counted gap
  junctions and neuromuscular junctions as well as chemical synapses. The
  FlyWire figure is chemical synapses between proofread neurons. The MICrONS
  and H01 figures are automatically detected synapses across the whole
  volume, most of them on neurites that were never proofread.
- **Animals differ in age, sex and condition.** Cook et al. (2019) mapped
  both sexes of the worm and found 302 neurons in the hermaphrodite and
  385 in the male. MICrONS comes from one male mouse at postnatal day 87.
  H01 comes from a 45-year-old woman having surgery for drug-resistant
  epilepsy. None of the vertebrate datasets has a second animal to compare
  against.

## What carries over

### The same pipeline works from worm to human

Every dataset in the table was made the same way in outline: fix and stain
the tissue, cut or mill it, image it by electron microscopy, segment it
automatically, and correct the segmentation by hand. The later datasets
share software as well. FlyWire and MICrONS were proofread and annotated in
the Connectome Annotation Versioning Engine (CAVE), which was built for
volumes up to about 1 mm³ (Dorkenwald et al. 2025). Skills you learn on one
of them, such as reading a Neuroglancer view, querying a materialization or
spotting a merge error, transfer directly. The
[MICrONS lab notebook]({{ '/notebooks/microns-lab/' | relative_url }}) and
the [proofreading error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }})
are written with this in mind.

### Most connections are weak, and weak connections are the least reliable

In every dataset where it has been measured, most neuron-to-neuron
connections are made of one or two synapses, and those weak connections are
the ones least likely to recur.

- **Larval fly.** 66% of edges have only 1 or 2 synapses, but edges of 5 or
  more synapses carry 55% of all synapses (Winding et al. 2023).
- **Adult fly.** Schlegel et al. (2024) compared the hemibrain with both
  hemispheres of FlyWire. A connection made by a single synapse in the
  hemibrain had a 42% chance of appearing in one FlyWire hemisphere and a
  16% chance of appearing in both. Connections of more than ten synapses
  were found in the other two hemispheres more than 90% of the time. Those
  strong connections were only 16% of edges but about 79% of synapses.
- **Worm.** Witvliet et al. (2021) reconstructed the brains of eight
  genetically identical animals. About 43% of cell-to-cell connections were
  not conserved between animals, but those connections accounted for only
  16% of chemical synapses.

The pattern transfers. The threshold does not. The fly and worm figures
come from whole brains, where every synapse between two neurons is in the
data. In a cortical fragment, a pair of neurons may also connect outside
the volume, so a weak edge in the data may be a stronger connection that
was cut off. No one has measured edge reproducibility across animals in
mammalian EM, because there is no second animal. Before you threshold a
mammalian graph, say what the threshold is protecting you from.
The [network analysis methods]({{ '/content-library/connectomics/network-analysis-methods/' | relative_url }})
page covers weighted and thresholded graphs.

### Graph methods apply everywhere, with the same caveats

Degree distributions, motif counts and community detection run on any
directed graph. The [motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }})
page's warnings about null models apply with more force to fragments,
because truncation removes edges non-randomly: neurons near the edge of the
volume lose more partners than neurons in the middle.

## What does not carry over

### Identified neurons exist in worms and flies, not in mammals

A worm neuron has a name, and the same named neuron is found in every
animal. That is what let Witvliet et al. ask whether a given connection is
present in all eight worms. Flies are close to this. Schlegel et al. (2024)
annotated 8,453 cell types in FlyWire and matched nearly all hemibrain
neurons to FlyWire neurons by shape. They also found that about one-third
of the cell types proposed from the hemibrain could not be reliably found
again. They proposed a definition that needs two brains: a cell type is a
group of cells that are each more similar to cells in another brain than to
any other cell in their own brain.

Mouse and human cortex have no identified neurons in this sense. A layer
2/3 pyramidal cell in one mouse has no counterpart in another. Cell types
there are statistical categories, defined from morphology, connectivity,
gene expression or physiology. "Is this connection present in every
animal?" becomes "Do cells of type A connect to cells of type B at a
similar rate across animals?", and with one animal per species the second
question cannot yet be answered from EM alone. See
[neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }})
for how mammalian types are assigned in practice.

### Completeness claims do not transfer

"The fly brain has 139,255 neurons" is a statement about a brain.
"MICrONS has more than 200,000 cells" is a statement about a block of
tissue. A finding such as "neuron X receives most of its input from type Y"
can be checked against the whole input tree in a fly. In a cortical
fragment, part of the input tree lies outside the volume, so the same
sentence needs a qualifier about what fraction of the dendrite was
reconstructed. When you read a mammalian connectivity result, look for how
the authors handled truncation. If they did not, the result may describe
the block rather than the cell.

### Cell composition differs

In H01, glia outnumber neurons by about two to one (32,315 against 16,087),
and a further 8,100 cells are associated with blood vessels (Shapson-Coe et
al. 2024). The fly and worm datasets in the table are reported as neuron
counts. If you move from fly data to mammalian data, expect to spend time on
[glia recognition]({{ '/content-library/cell-types/glia-recognition/' | relative_url }}).

### Development and individual history differ

Witvliet et al. (2021) followed the worm brain from birth to adulthood
across eight animals. Chemical synapses in the brain rose about six-fold,
from about 1,300 at birth to about 8,000 in adults, while the overall
geometry of the brain stayed the same. No vertebrate connectome yet has
this kind of series. Each mouse and human volume is one animal at one age,
and in H01's case one person with a neurological disease. It is not
possible to say from H01 alone which features are typical of human cortex
and which reflect epilepsy, medication or surgery.

### The cost per neuron differs by orders of magnitude

FlyWire's whole-brain reconstruction took about 33 person-years of
proofreading for 139,255 neurons (Dorkenwald et al. 2024). The hemibrain
took more than 50 person-years for part of one brain (Scheffer et al.
2020). The MICrONS paper reports 1,046,656 proofreading edits as of
16 September 2024 but publishes no person-years figure. Its release
includes 1,433 neurons with proofread axons, a small fraction of the
volume's neurons. The authors name extending axons as the most
time-consuming task: 100 to 1,000 edits per axon, with more edits for
more extensive axons (MICrONS Consortium 2025).
The [proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }})
page works through the arithmetic.

## Questions to ask before comparing two datasets

1. Is each dataset a whole brain or a fragment? If a fragment, how does
   truncation affect the measure you are comparing?
2. Do the synapse counts include the same things (chemical only, or also
   gap junctions and neuromuscular junctions; proofread neurons only, or
   the whole volume)?
3. Are the neurons identifiable across animals, or are you comparing
   statistical cell types?
4. How many animals are behind each number? For every vertebrate dataset in
   the table, the answer is one.
5. Is a threshold on synapse count doing the same job in both datasets?

## What this page does not cover

It does not cover mesoscale connectomes built from tract tracing or
diffusion MRI, which answer region-to-region questions and are not
comparable with synapse-level data. It also does not cover other synaptic
datasets such as the fly ventral nerve cord (MANC, FANC) or the zebrafish
larva; see the [dataset catalog]({{ '/datasets/' | relative_url }}) for those.
For the history of how these datasets came to be, see
[connectome history]({{ '/content-library/connectomics/connectome-history/' | relative_url }}).

## References

- Badea, A., Ali-Sharief, A. A., & Johnson, G. A. (2007). Morphometric
  analysis of the C57BL/6J mouse brain. *NeuroImage*, 37, 683-693.
  doi:10.1016/j.neuroimage.2007.05.046.
- Cook, S. J., et al. (2019). Whole-animal connectomes of both
  *Caenorhabditis elegans* sexes. *Nature*, 571, 63-71.
  doi:10.1038/s41586-019-1352-7.
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain.
  *Nature*, 634, 124-138. doi:10.1038/s41586-024-07558-y.
- Dorkenwald, S., Schneider-Mizell, C. M., et al. (2025). CAVE: Connectome
  Annotation Versioning Engine. *Nature Methods*, 22, 1112-1120.
  doi:10.1038/s41592-024-02426-z.
- MICrONS Consortium, et al. (2025). Functional connectomics spanning
  multiple areas of mouse visual cortex. *Nature*, 640, 435-447.
  doi:10.1038/s41586-025-08790-w.
- Scheffer, L. K., et al. (2020). A connectome and analysis of the adult
  *Drosophila* central brain. *eLife*, 9, e57443. doi:10.7554/eLife.57443.
- Schlegel, P., et al. (2024). Whole-brain annotation and multi-connectome
  cell typing of *Drosophila*. *Nature*, 634, 139-152.
  doi:10.1038/s41586-024-07686-5.
- Shapson-Coe, A., et al. (2024). A petavoxel fragment of human cerebral
  cortex reconstructed at nanoscale resolution. *Science*, 384, eadk4858.
  doi:10.1126/science.adk4858.
- White, J. G., Southgate, E., Thomson, J. N., & Brenner, S. (1986). The
  structure of the nervous system of the nematode *Caenorhabditis elegans*.
  *Philosophical Transactions of the Royal Society B*, 314, 1-340.
  doi:10.1098/rstb.1986.0056.
- Winding, M., et al. (2023). The connectome of an insect brain. *Science*,
  379, eadd9330. doi:10.1126/science.add9330.
- Witvliet, D., et al. (2021). Connectomes across development reveal
  principles of brain maturation. *Nature*, 596, 257-261.
  doi:10.1038/s41586-021-03778-8.
