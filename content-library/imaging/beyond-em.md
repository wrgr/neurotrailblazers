---
layout: page
title: "Beyond EM"
permalink: /content-library/imaging/beyond-em/
description: "What expansion microscopy, LICONN, X-ray nanotomography, array tomography, MAPseq and BARseq, and diffusion MRI each establish about connectivity, what each cannot show, and why volume EM stays the default for synapse-resolution wiring. Every number is from the primary paper."
topics:
  - expansion-microscopy
  - light-microscopy-connectomics
  - x-ray-tomography
  - array-tomography
  - projection-barcoding
  - modality-choice
primary_units:
  - "02"
  - "03"
difficulty: "Intermediate"
tags:
  - imaging:expansion-microscopy
  - imaging:light-microscopy
  - imaging:x-ray-tomography
  - imaging:array-tomography
  - imaging:resolution
  - methodology:experimental-design
  - connectomics:projection-mapping
micro_lesson_id: ml-img-beyond-em
combines_with:
  - em-principles
  - tissue-preparation
  - synapse-detection
  - 02-brain-data-across-scales
content_type: core
---

## Overview

Every other page in this imaging section assumes electron microscopy. This one is the reference behind the single slide in the graduate [Module 7 deck]({{ '/course/decks/marp/out/en585781/module07-introduction-to-connectomics.html' | relative_url }}) ("Different tools for different jobs") where the other modalities appear once, as the scale-choice example, and behind the modality chart in [Unit 02]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}). The argument is the same in both places: the alternatives to EM are instruments for different questions, not weaker connectomics. This page gives the numbers behind that argument, from the papers that introduced each method.

The rule to carry away: **if the claim is "cell A makes a synapse onto cell B", the evidence is volume EM, or, since 2025, a hydrogel-expanded light-microscopy volume whose traceability has been checked.** Everything else on this page answers a question that EM cannot answer at all, or cannot answer at the scale or cost the question needs.

---

## EM is the default because it sees the synapse without a label

Light microscopy is diffraction-limited to roughly 200 to 250 nm laterally, and confocal axial resolution is rarely better than 700 nm (Micheva & Smith 2007, citing Pawley 1995). A membrane is about 7 nm thick, a synaptic vesicle about 40 nm across, and the thinnest axons in cortex are under 100 nm in diameter (the figures [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }}) works from). Volume EM images at about 4 nm per pixel (MICrONS and H01) with 33 to 40 nm sections, or at 8 nm isotropic for FIB-SEM (hemibrain). At that sampling, membranes, vesicles and postsynaptic densities are visible in every process, without choosing what to label. [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }}) covers the physics.

That is what EM uniquely gives: dense, unbiased structure. It is also the list of what EM does not give.

| What you want | Why EM cannot supply it | What supplies it |
|---|---|---|
| Which proteins are at this synapse | Heavy-metal stain marks membranes and protein density, not identity | Expansion microscopy, LICONN, array tomography |
| Where the axons of 3,000 individual cells go, brain-wide | A 1 mm³ volume does not contain both the somata and their distant targets, and proofreading thousands of long axons is not tractable today | MAPseq, BARseq |
| Cell-scale morphology across millimeters, in hours, without cutting the block | EM sections, stains and images the whole block at synapse resolution whether or not you need it everywhere | X-ray tomography |
| A living human brain, measured repeatedly | EM requires fixed, stained, sectioned tissue | Diffusion MRI |
| The same volume imaged twice, on a modest budget | A cubic millimeter of EM is about 2 PB of raw data and months of instrument time (MICrONS Consortium 2025; Shapson-Coe et al. 2024) | Expansion-based light microscopy, X-ray |

For each method below, the questions are the same: what does it resolve, over what volume, what does it establish about connectivity, and what does it not.

---

## Expansion microscopy trades a label for resolution below the diffraction limit

Chen, Tillberg and Boyden (2015) embedded fixed tissue in a swellable polyelectrolyte gel, anchored fluorescent labels to the gel, digested the tissue with protease and let the gel swell in water. The specimen expanded 4.5-fold in each linear dimension. The optics did not change; the sample did. With a diffraction-limited confocal microscope they reported an effective lateral resolution of about 70 nm and an axial resolution of about 200 nm. On microtubules the measured full width at half maximum was 82.4 ± 6.01 nm, which deconvolves to an effective resolution of about 60 nm. They imaged a 500 × 180 × 100 µm slab of mouse brain (about 10⁷ µm³, spanning hippocampus) with three labels on a spinning-disc confocal. In cortex, they resolved presynaptic Bassoon from postsynaptic Homer1 as separate spots, 169 ± 32.6 nm apart across 277 synapses; before expansion the two labels overlapped.

The measured distortion matters more than the headline resolution. By registering pre- and post-expansion images they put the root-mean-square length error below 1% of the measured distance, for distances larger than the point spread function. That figure is for a 4.5× gel. Higher expansion factors have to be checked separately.

Two extensions set the range you will see quoted:

- **Iterative expansion (iExM).** Chang et al. (2017) formed a second swellable gel in the space opened by the first expansion, for about 4.5 × 4.5, or roughly 20×, and reported about 25 nm resolution on conventional microscopes. Hollow microtubules, 25 nm in outer diameter, were resolved with confocal imaging.
- **Expansion plus lattice light-sheet (ExLLSM).** Gao et al. (2019) combined 4× expansion with lattice light-sheet microscopy to image the full thickness of mouse cortex and the entire *Drosophila* brain at about 60 × 60 × 90 nm effective resolution. A whole fly brain took 62.5 hours. Volumes were stitched from as many as 25,000 tiles into multi-terabyte datasets. They chose 4× deliberately: at 8× with an iterated protocol they saw regions of clear distortion, including irregularly shaped somata and nuclei, and they argue that immunostaining is probably not dense enough to deliver resolution much beyond what 4× already gives.

**What ExM establishes.** The positions of labeled molecules, relative to each other and to labeled cells, below the diffraction limit, over volumes that reach a whole fly brain. Gao et al. counted synapses per fly brain region and measured spine morphology across the depth of cortex, with molecular contrast that EM cannot provide.

**What it does not.** In these papers, dense reconstruction of unlabeled neuropil. An expanded volume shows what you labeled. A cytosolic label in a subset of neurons (Thy1-YFP, in both Chen and Gao) gives clean single cells, but the unlabeled processes between them are invisible, so "A contacts B" is only answerable for the labeled pair, and contact is not a synapse. The step from labeled sparse cells to dense wiring is what LICONN adds.

---

## LICONN reaches dense, synapse-level reconstruction with light

Tavakoli et al. (2025) describe light-microscopy-based connectomics (LICONN). The recipe: a purpose-built triple-hydrogel embedding that expands tissue about 16-fold (measured 15.44 ± 1.68, mean ± s.d.), an indiscriminate protein-density stain (fluorophore NHS esters, which mark primary amines on proteins) instead of a targeted label, spinning-disc confocal imaging, and flood-filling-network segmentation borrowed from EM connectomics.

The numbers, all from the paper:

- **Resolution.** The confocal system gave about 280 nm lateral and 730 nm axial resolution. Divided by the expansion factor, that is an effective resolution of about 20 nm lateral and 50 nm axial, sampled at an effective voxel size of about 10 × 10 × 25 nm.
- **Volume and speed.** The largest volume was about 1 × 10⁶ µm³ of mouse primary somatosensory cortex at native scale (396 × 109 × 22 µm, layers II/III to IV), imaged as 132 overlapping tiles on a 6 × 22 grid, 0.47 teravoxels including overlap, in 6.5 hours.
- **Segmentation accuracy.** In a proofread 85 × 69 × 14 µm box of hippocampal CA1 (68.6 gigavoxels), the base FFN segmentation, evaluated against 99 manually skeletonized neurites (69 axons totaling 1.8 mm of path, 30 dendrites with 1,041 spines), had 0 mergers, 413 splits and 80.1% edge accuracy. Automated agglomeration raised edge accuracy to 92.8% and cut splits to 31. The remaining error was dominated by spines the network did not label (83 of 1,041, 8.0%).
- **Traceability.** In randomly sampled 2 × 2 × 2 µm subvolumes, an annotator traced 285 of 306 spine heads (93.1%) to a parent dendrite from raw data alone, and 281 of 301 (93.4%) in a second volume.
- **Synapses with molecules attached.** In the same specimens they immunolabeled bassoon, PSD95, SHANK2 (excitatory postsynapses) and gephyrin (inhibitory postsynapses). A deep-learning predictor of excitatory synapse locations, tested against 1,059 manually validated synapses, reached F1 = 0.90 for fully assembled synapses (0.94 pre-synaptic, 0.95 post-synaptic). On 11 spiny dendrites (123 µm, 322 spines) they counted 2.8 ± 1.2 inputs per µm, 2.6 ± 1.1 of them SHANK2-positive.
- **Depth.** High-NA objectives have a working distance of 0.6 mm, which limits imaging depth. They extended volumes axially by imaging a slab, vibratome-cutting most of the imaged gel away, imaging again and fusing the overlap voxel-exactly. Twelve rounds on a 3 × 3 × 12 tile grid covered 205 µm axially.

The Module 8 deck calls LICONN the first demonstrated light-microscopy route to dense synapse-level reconstruction. That is the authors' framing: their abstract says such reconstruction "has been out of reach" until now.

**What LICONN establishes.** Dense segmentation of every process in the volume, with synapse locations, and with molecular identity read from additional channels in the same specimen. That last part is the thing EM cannot do, and it is why the paper matters.

**What is not yet established.** Three things, none of which the paper claims:

1. **Agreement with EM on the same tissue.** Validation was against manual skeletons drawn on LICONN data, sparse positive labels, spine traceability, and statistical comparison with published EM values (for example, spine density of 1.0 ± 0.3 per µm³, consistent with prior cortical data). There is no voxel-level EM ground truth of the same block.
2. **Scale.** The largest volume is 10⁶ µm³, which is 0.001 mm³, in a 22 µm thick slab. The mm³ EM volumes are a thousand times larger. Whether the imaging rate and the axial-extension method carry to a cubic millimeter is open, and the axial extension is destructive, like SBEM.
3. **Fine axons at scale.** The 0-merger result is on an 85 × 69 × 14 µm box with its own skeletons. It is not a run-length figure over millimeters of axon.

If it scales, the cost argument in Module 7 changes: no ultramicrotome, no heavy metals, protein labels in the same specimen, and a spinning-disc confocal instead of a multibeam SEM. That is why the deck lists it under open problems rather than under methods.

---

## X-ray tomography images the block whole, at cell to neurite resolution

Two X-ray methods appear in the connectomics literature, and they differ by an order of magnitude in resolution. The site's [initiatives page]({{ '/initiatives/' | relative_url }}) credits both correctly: microtomography at Argonne, holographic nanotomography at the ESRF.

**Synchrotron microtomography (µCT).** Dyer et al. (2017) imaged aldehyde-fixed, heavy-metal-stained, plastic-embedded mouse brain at the 2-BM beamline of the Advanced Photon Source. Resolution was about 1 µm isotropic over millimeter-scale volumes, without sectioning. That resolves cell bodies, blood vessels, large apical dendrites and myelinated axons, and the paper's pipeline segments and counts them. Bosch et al. (2022) used propagation-based phase contrast at 325 nm voxels (measured resolution about 2 to 3 µm) to see subcellular context in olfactory bulb and hippocampus, then acquired targeted SBEM subvolumes at 50 nm isotropic. The X-ray scan told them where to spend the EM time.

**X-ray holographic nanotomography (XNH).** Kuan et al. (2020) imaged mouse cortex and adult *Drosophila* brain, ventral nerve cord and leg at the ID16A beamline of the European Synchrotron (ESRF). Voxel sizes ran from 30 to 120 nm, and the measured resolution (Fourier shell correlation) ran from 87 to 222 nm. The abstract's "sub-100 nm" is the best case at the smallest voxel. At 30 nm voxels they could see mitochondria, endoplasmic reticulum, dendrites and myelinated axons, though identification leaned on prior knowledge of 3D shape. Samples were imaged at 120 K to limit warping from beam heating, and scans with major warping artifacts were excluded. Two overlapping XNH scans of posterior parietal cortex spanning layers I to V took about 8 hours and contained 3,234 cells, each classified as pyramidal, interneuron or glia from morphology. They also imaged an intact fly leg, a structure that is hard to section, and traced motor axons from muscle to the central nervous system.

**What XNH establishes.** Neuronal morphology at the scale of main branches, densely, across millimeter-sized volumes, in hours, with the block available for EM afterward. Because no genetic label is needed, it works on any species.

**What it does not.** Synapses. To get synaptic inputs on the apical dendrites they had reconstructed in XNH, Kuan et al. imaged a synapse-resolution EM dataset of the same tissue (about 150 hours of imaging) and registered the two. Ultrastructure, including chemical synapses, survived the X-ray scan, though the EM images contained small cracks and bubbles that may have come from XNH imaging. The paper's connectivity result, that more superficial pyramidal cells receive stronger synaptic inhibition on their apical dendrites, is an XNH-plus-EM result. The thinnest axons are also out of reach: in the fly leg, motor, hair-plate and some campaniform-sensillum axons were large enough to reconstruct at the 150 to 200 nm resolution of those scans, chordotonal and bristle axons were narrower, and bristle axons in particular were too small to trace accurately.

---

## Array tomography multiplexes protein labels on ultrathin sections

Micheva and Smith (2007) cut ribbons of 50 to 200 nm sections from LR White resin blocks, bonded them to glass slides in ordered arrays, and immunostained and imaged them. The trick is the section, not the optics. Lateral resolution stays diffraction-limited, but axial resolution is now the section thickness (70 to 200 nm in their examples), against the 700 nm or worse a confocal achieves. Because the section is thin and planar, staining is depth-independent.

The other property is multiplexing. Antibodies can be eluted and the array restained; the paper reports "no apparent limit" to the number of rounds and demonstrates nine cycles of double immunolabeling on one array, with synapsin intensity at ten synapses stable across six rounds. After fluorescence imaging the same sections can be stained with heavy metals and imaged in a scanning electron microscope, giving light and EM views of the same 70 nm section in register.

**What it establishes.** The presence and co-localization of tens of proteins at individual synapses, in a defined volume, with synapse-scale axial sampling. Presynaptic synapsin and postsynaptic PSD-95 can be followed through consecutive sections as a pair.

**What it does not.** Dense neurite tracing. With about 250 nm lateral resolution, the fine processes between labeled synapses cannot be followed, so array tomography counts and characterizes synapses but does not say which neuron each belongs to unless that neuron is labeled. Section loss and folds are the same failure modes as serial-section EM.

---

## Sequencing-based projection mapping counts cells, not synapses

**MAPseq.** Kebschull et al. (2016) replaced microscopy with sequencing. Neurons at an injection site are infected with a Sindbis virus library carrying random RNA barcodes. A 30-nucleotide barcode has a potential diversity of about 10¹⁸, against roughly 10⁸ neurons in a mouse brain, so each infected cell gets a unique tag. An engineered presynaptic protein carries the barcode mRNA into axons. Target regions are dissected, barcode mRNA is extracted and sequenced, and the counts become a matrix of single-neuron projection patterns. In the proof of principle, 995 barcodes from the locus coeruleus in four animals (249 ± 103 per animal) were read against the olfactory bulb and 22 coronal 300 µm slices of ipsilateral cortex. Individual neurons had idiosyncratic patterns: some projected almost exclusively to one preferred cortical target, others broadly. The brain-wide map from one injection took less than a week.

**BARseq.** MAPseq loses the soma, because the injection site is homogenized. Chen et al. (2019) read the barcodes in situ, by sequencing them in place in the cortex, so each projection pattern is attached to a cell at a known position, which can also be read for gene or Cre expression. Their demonstration mapped the projections of 3,579 neurons in mouse auditory cortex to 11 target areas, recovered the laminar organization of the intratelencephalic, pyramidal-tract-like and corticothalamic classes, and found a projection type almost restricted to transcriptionally defined IT subtypes.

**What barcoding establishes.** For each of thousands of neurons in one brain, which dissected regions its axon reaches, at a cost per cell far below any imaging method. It gives statistical power over cells, which is exactly what EM lacks.

**What it does not.**

- **Synapses.** A barcode count in a dissected region says axonal mRNA arrived there. It does not say the axon made a synapse, or with which cell. Both papers are explicit: MAPseq, like GFP tracing, does not distinguish fibers of passage. Kebschull et al. minimized the effect by avoiding large fiber bundles during dissection; Chen et al. argue the contribution is small in practice because the carrier protein is enriched at synapses and passing fibers contribute little material.
- **Geometry.** No morphology, no branch structure, no local circuit. Spatial resolution in MAPseq is set by the dissection, not by any optic.
- **Completeness.** The 995 barcodes "roughly correspond" to an equal number of neurons; the mapping from barcodes to cells assumes one barcode per cell and depends on library diversity.

This is the worked case in Unit 02: "do individual layer 2/3 neurons that project to AL also project to PM, across thousands of cells?" is a barcoding question. It needs cells, not geometry, and no EM volume yet contains the somata and both targets.

---

## Diffusion MRI is the only living, whole-brain measurement, and every edge is a model

Diffusion MRI tractography infers streamlines from the orientation of water diffusion in millimeter-scale voxels. It is the one method on this page that measures a living human brain and can be repeated on the same person. The site's [MRI connectomics reading list]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }}) covers the field; the point here is the boundary. Maier-Hein et al. (2017) ran an open challenge on a simulated brain with 25 ground-truth bundles: 96 submissions from 20 groups. Most tractograms recovered 90% of the true bundles, to some extent, but contained more invalid bundles than valid ones, and half of the invalid bundles recurred across groups. A tractography "connection" is a statement about the most probable path given a diffusion model. It is not an axon, and it is never a synapse. Unit 02 has the check-yourself on how a tractography result and an EM result can disagree while both are correct.

---

## Comparison: resolution, volume, what each establishes and what it does not

Every row cites the paper the numbers come from. Volumes are the largest each paper reports, not theoretical limits.

| Method | Resolution | Volume demonstrated | Establishes | Does not establish | Source |
|---|---|---|---|---|---|
| Serial-section EM (TEM or multibeam SEM) | ~4 nm pixels, 33–40 nm sections | ~1 mm³ (MICrONS, H01) | Dense wiring with synapses, unlabeled | Molecular identity; anything alive; more than one animal per dataset | MICrONS Consortium 2025; Shapson-Coe et al. 2024 |
| FIB-SEM | 8 nm isotropic | Hemibrain, ~25,000 neurons | Same, with isotropic voxels | Same; volume per run is smaller | Scheffer et al. 2020 |
| Expansion microscopy (4.5×) | ~70 nm lateral, ~200 nm axial | 500 × 180 × 100 µm | Labeled molecules and labeled cells below the diffraction limit | Unlabeled processes; dense wiring | Chen, Tillberg & Boyden 2015 |
| Iterative ExM (~20×) | ~25 nm | Cells and mouse brain tissue | Synaptic protein arrangement, spine architecture | Dense wiring; distortion at high expansion must be measured | Chang et al. 2017 |
| ExLLSM (4×) | ~60 × 60 × 90 nm | Whole fly brain (62.5 h); full cortical thickness in mouse | Molecular counts across whole brains, many animals | Dense wiring; they saw distortion at 8× | Gao et al. 2019 |
| LICONN (~16×) | ~20 nm lateral, ~50 nm axial | 396 × 109 × 22 µm cortex (~10⁶ µm³) in 6.5 h | Dense segmentation, synapses (F1 0.90), molecules in the same specimen | EM-level ground truth on the same tissue; mm³ scale | Tavakoli et al. 2025 |
| X-ray holographic nanotomography | 87–222 nm measured, 30–120 nm voxels | Millimeter-scale; 3,234 cells in ~8 h | Dense main-branch morphology, block intact, any species | Synapses (EM was added for those); thinnest axons | Kuan et al. 2020 |
| Synchrotron microtomography | ~1 µm isotropic | Millimeter-scale | Cell bodies, vessels, myelinated axons; where to aim EM | Neurites in neuropil; synapses | Dyer et al. 2017; Bosch et al. 2022 |
| Array tomography | ~250 nm lateral; 50–200 nm sections | Ribbons of sections; nine restaining cycles shown | Tens of proteins per synapse, in register with SEM | Dense tracing; neuron identity of unlabeled synapses | Micheva & Smith 2007 |
| MAPseq | Dissection-limited; no image | Whole brain; 995 barcodes, 4 animals | Per-cell projection targets for thousands of cells | Synapses; morphology; fibers of passage excluded only by dissection | Kebschull et al. 2016 |
| BARseq | Cellular (soma position); no neurite image | 3,579 neurons to 11 areas, one brain | Projection pattern plus gene expression per cell | Synapses; morphology; local circuit | Chen et al. 2019 |
| Diffusion MRI tractography | Millimeters | Whole living human brain, repeatable | Probable white-matter pathways in vivo | Axons; synapses; more invalid than valid bundles in a controlled test | Maier-Hein et al. 2017 |

Two habits when you read this table. First, a resolution figure is a claim about a specific measurement: Kuan et al.'s "sub-100 nm" is the 87 nm best case, and LICONN's "20 nm" is confocal resolution divided by 16. Ask how it was measured. Second, volume and resolution move together. The mm³ EM rows and the nanometer rows are not the same rows, and the LICONN row is a thousandth of a cubic millimeter.

---

## How to choose

Write the claim first. "Synapse between identified cells" sends you to EM or, with the caveats above, LICONN. "Molecule X at synapses of type Y" sends you to expansion or array tomography. "Projection targets of n cells" sends you to barcoding. "Living human" sends you to MRI. Then take the coarsest method that answers it: an XNH scan in 8 hours that settles a morphology question beats an EM volume in 150 hours that settles it too, and Bosch et al. and Kuan et al. both used X-ray to decide where to spend EM time. Last, state the non-claim. A barcoding result reported as "connected", then cited as a synapse, is the scale-leakage failure the Module 7 deck warns about.

---

## Check yourself

<details markdown="1">
<summary>A paper reports that LICONN achieves "20 nm resolution" and asks whether that makes it equivalent to EM at 4 nm pixels. What do you say?</summary>

The 20 nm is confocal lateral resolution (about 280 nm) divided by the expansion factor (about 16); axial is about 50 nm. It is an effective resolution in a physically expanded protein-density stain, not an EM pixel size, and the validation in Tavakoli et al. (2025) is against manual skeletons on LICONN data and statistical comparison with prior EM, not against EM of the same tissue. The demonstrated volume is about 10⁶ µm³ (0.001 mm³). So: the same *kind* of claim as EM (dense segmentation with synapses, F1 0.90 on 1,059 validated synapses), in a volume a thousand times smaller, without EM ground truth, and with molecular channels EM cannot provide. Equivalent is the wrong word; complementary and not yet at scale is right.
</details>

<details markdown="1">
<summary>A BARseq study finds that 40% of a transcriptomic subtype projects to both area A and area B. A reviewer asks whether those cells synapse in area B. What can the data say?</summary>

Nothing about synapses. Barcode mRNA detected in area B means the axon reached the dissected tissue. It could be a terminal field or a fiber of passage, and even a terminal field does not identify a postsynaptic partner. What the data does establish, and what EM could not, is a per-cell projection pattern across thousands of cells with the transcriptomic identity attached (Chen et al. 2019 mapped 3,579 cells to 11 areas in one brain). The reviewer's question needs EM or a synapse-level method in area B, and it will get an answer for tens of cells, not thousands.
</details>

<details markdown="1">
<summary>You have one block of mouse cortex and a question about the branching pattern of every layer 5 apical dendrite in a 1 mm column. Which method first, and why?</summary>

X-ray holographic nanotomography, then EM only if a synapse question follows. Kuan et al. (2020) imaged layers I to V of parietal cortex in two overlapping scans in about 8 hours and identified all 3,234 cells at 100 nm voxels (the measured resolution across the paper's scans ran from 87 to 222 nm), and the block was available for EM afterward. The synapse-level EM of the same tissue took about 150 hours for one layer. Branching is a morphology question; XNH answers it at a fraction of the cost and leaves the block for targeted EM.
</details>

---

## What this page does not cover

- **Tracer-based mesoscale atlases** (anterograde and retrograde tracers with light-sheet imaging, such as the Allen Mouse Brain Connectivity Atlas). Unit 02 places them on the modality chart.
- **Correlative light and EM (CLEM)** as a method in its own right, genetically encoded EM tags such as APEX2, and cryo-electron tomography. Lichtman and Denk's perspective on the [volume EM and optics papers]({{ '/content-library/journal-papers/imaging/' | relative_url }}) page introduces CLEM as a way to target EM; the rest is not covered on this site.
- **Functional methods.** Calcium imaging and electrophysiology give activity, not structure; the [MICrONS case study]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }}) covers how they are co-registered to EM.
- **Newer EM acquisition routes** named in the Module 7 deck (FAST-EM array tomography by SEM, machine-learning-guided acquisition). They are EM, and they are not verified on this page.
- **Throughput and cost beyond what each paper reports.** Imaging time for one demonstration is not a rate you can plan a project from.

---

## Related

- [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }}): why 4 nm pixels, and the resolution, volume, throughput triangle
- [Tissue preparation]({{ '/content-library/imaging/tissue-preparation/' | relative_url }}): what the heavy-metal chain fixes and what it removes; the expansion and X-ray methods above start from different preparation
- [Synapse detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}): the EM-side metrics (precision, recall, F1) that LICONN's synapse figures should be read against
- [Unit 02: Brain data across scales]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}): the modality chart, the decision rule, and the two check-yourself cases this page expands
- [Volume EM and optics papers]({{ '/content-library/journal-papers/imaging/' | relative_url }}): the EM acquisition literature
- [MRI connectomics papers]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }}): the macroscale side
- [Module 7 deck, "Different tools for different jobs"]({{ '/course/decks/marp/out/en585781/module07-introduction-to-connectomics.html' | relative_url }}): the one slide where the graduate course names these modalities, as the scale-choice example ([source]({{ site.deck_source_base }}/en585781/module07-introduction-to-connectomics.marp.md))
- [FANC dataset]({{ '/datasets/catalog/fanc/' | relative_url }}): a connectome whose motor-neuron atlas used X-ray holographic nanotomography

---

## References

- Bosch C et al. (2022) "Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy." *Nature Communications* 13:2923. [10.1038/s41467-022-30199-6](https://doi.org/10.1038/s41467-022-30199-6)
- Chang J-B et al. (2017) "Iterative expansion microscopy." *Nature Methods* 14(6):593-599. [10.1038/nmeth.4261](https://doi.org/10.1038/nmeth.4261)
- Chen F, Tillberg PW, Boyden ES (2015) "Expansion microscopy." *Science* 347(6221):543-548. [10.1126/science.1260088](https://doi.org/10.1126/science.1260088)
- Chen X et al. (2019) "High-throughput mapping of long-range neuronal projection using in situ sequencing." *Cell* 179(3):772-786. [10.1016/j.cell.2019.09.023](https://doi.org/10.1016/j.cell.2019.09.023)
- Dyer EL et al. (2017) "Quantifying mesoscale neuroanatomy using X-ray microtomography." *eNeuro* 4(5):ENEURO.0195-17.2017. [10.1523/ENEURO.0195-17.2017](https://doi.org/10.1523/ENEURO.0195-17.2017)
- Gao R et al. (2019) "Cortical column and whole-brain imaging with molecular contrast and nanoscale resolution." *Science* 363(6424):eaau8302. [10.1126/science.aau8302](https://doi.org/10.1126/science.aau8302)
- Kebschull JM et al. (2016) "High-throughput mapping of single-neuron projections by sequencing of barcoded RNA." *Neuron* 91(5):975-987. [10.1016/j.neuron.2016.07.036](https://doi.org/10.1016/j.neuron.2016.07.036)
- Kuan AT et al. (2020) "Dense neuronal reconstruction through X-ray holographic nano-tomography." *Nature Neuroscience* 23(12):1637-1643. [10.1038/s41593-020-0704-9](https://doi.org/10.1038/s41593-020-0704-9)
- Maier-Hein KH et al. (2017) "The challenge of mapping the human connectome based on diffusion tractography." *Nature Communications* 8:1349. [10.1038/s41467-017-01285-x](https://doi.org/10.1038/s41467-017-01285-x)
- Micheva KD, Smith SJ (2007) "Array tomography: a new tool for imaging the molecular architecture and ultrastructure of neural circuits." *Neuron* 55(1):25-36. [10.1016/j.neuron.2007.06.014](https://doi.org/10.1016/j.neuron.2007.06.014)
- MICrONS Consortium (2025) "Functional connectomics spanning multiple areas of mouse visual cortex." *Nature* 640:435-447. [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443. [10.7554/eLife.57443](https://doi.org/10.7554/eLife.57443)
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384(6696):eadk4858. [10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)
- Tavakoli MR et al. (2025) "Light-microscopy-based connectomic reconstruction of mammalian brain tissue." *Nature* 642(8067):398-410. [10.1038/s41586-025-08985-1](https://doi.org/10.1038/s41586-025-08985-1)
