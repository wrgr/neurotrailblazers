---
layout: page
title: "Synapse Classification and Identification"
permalink: /content-library/neuroanatomy/synapse-classification/
image: /assets/images/content-library/neuroanatomy/synapse-classification.svg
image_alt: "Stylized vector art: organelle profiles inside a curved membrane section."
description: >
  Instructor reference on synapse classification in electron microscopy,
  covering the Gray Type I/Type II system, synaptic cleft structure, pre- and
  postsynaptic specializations, electrical synapses, multi-synapse boutons, and a
  step-by-step synapse identification protocol for annotators.
topics:
  - synapse classification
  - Gray Type I synapses
  - Gray Type II synapses
  - asymmetric synapses
  - symmetric synapses
  - synaptic cleft
  - postsynaptic density
  - active zone
  - gap junctions
  - electrical synapses
  - multi-synapse boutons
  - synapse annotation protocol
primary_units:
  - "05"
difficulty: intermediate
tags:
  - neuroanatomy:synapse
  - neuroanatomy:postsynaptic-density
  - neuroanatomy:vesicle
  - connectomics:excitatory-synapse
  - connectomics:inhibitory-synapse
  - connectomics:gap-junction
  - imaging:electron-microscopy
  - proofreading:synapse-annotation
  - methodology:classification
micro_lesson_id: ml-neuro-synapse
combines_with:
  - dendrite-biology
  - axon-biology
  - organelle-cues
use_layout_hero: false
content_type: core
---

# Synapse Classification and Identification

## Introduction

A connectome is a list of synapses, so every error in finding or typing a synapse becomes an error in the wiring diagram. This script covers how to tell excitatory from inhibitory synapses, how to separate real synapses from look-alikes, and how to annotate them consistently across a volume. The framework starts with E. G. Gray in 1959 and was extended by others over the following decade.

---

## 1. The Gray Classification System

In 1959, Edward George Gray described two morphologically distinct synapse types in the rat cerebral cortex (Gray, 1959). His criteria were the extent and thickness of the membrane densities and the width of the cleft. He found Type 1 contacts mostly on dendrites and Type 2 contacts on cell bodies. Two parts of the modern scheme came later: Uchizono (1965) linked flattened vesicles to inhibitory synapses and round vesicles to excitatory ones, and Colonnier (1968) introduced the terms "asymmetric" and "symmetric". The excitatory/inhibitory reading of the two types was confirmed later still, when glutamate and GABA were localized to them (Klemann & Roubos, 2011). The scheme remains the standard framework for EM-based synapse identification.

### 1.1 Type I (Asymmetric) Synapses

Type I synapses are characterized by a pronounced asymmetry between the pre- and postsynaptic densities:

- **Postsynaptic density (PSD)**: Thick and conspicuous, extending about 35-50 nm into the cytoplasm (Harris & Weinberg, 2012). The PSD appears as a prominent electron-dense band on the cytoplasmic face of the postsynaptic membrane.
- **Presynaptic density**: Thin or modest, creating the defining asymmetry — the postsynaptic side is much more electron-dense than the presynaptic side.
- **Vesicle morphology**: Round, clear vesicles, about 35-45 nm in diameter (Harris & Weinberg, 2012, give about 35 nm). The round shape is kept in well-fixed, aldehyde-fixed tissue.
- **Synaptic cleft width**: Approximately 20 nm, wider than Type II synapses (Harris & Weinberg, 2012; High et al., 2015).
- **Cleft material**: Dense proteinaceous material fills the cleft, visible as a fuzzy band between the membranes. This material includes trans-synaptic adhesion molecules (neurexin-neuroligin complexes, SynCAMs).
- **Neurotransmitter**: Predominantly glutamatergic (excitatory).
- **Postsynaptic targets**: Most commonly found on dendritic spines (axospinous synapses) and dendritic shafts (axodendritic synapses). Rare on somata: in cat area 17, 79% of asymmetric synapses were on spines, 21% on dendritic shafts and 0.1% on cell bodies (Beaulieu & Colonnier, 1985). Interneuron somata are the main exception.

### 1.2 Type II (Symmetric) Synapses

Type II synapses show roughly equal density on both sides of the synaptic junction:

- **Postsynaptic density**: Thin, comparable in thickness to the presynaptic density. Both sides show a modest electron-dense coating, creating the symmetric appearance.
- **Presynaptic density**: Similar thickness to the PSD, contributing to the overall symmetry.
- **Vesicle morphology**: Pleomorphic (variable in shape) or flattened vesicles. In aldehyde-fixed tissue, these vesicles tend to adopt oval or flattened profiles rather than the perfectly round shape of Type I vesicles. Note: vesicle shape is somewhat fixation-dependent, and some authors prefer to describe these as "pleomorphic" rather than "flattened."
- **Synaptic cleft width**: Approximately 12 nm, narrower than Type I. Electron tomography found inhibitory clefts narrowing to 6 nm at their edges, against a uniform 18 nm at excitatory synapses (High et al., 2015).
- **Cleft material**: Present but less prominent than in Type I.
- **Neurotransmitter**: Predominantly GABAergic (inhibitory). Also includes glycinergic synapses in brainstem and spinal cord.
- **Postsynaptic targets**: Found on somata (axosomatic synapses), dendritic shafts (axodendritic synapses) and the axon initial segment (axoaxonic synapses). They are not confined to those sites: in cat area 17, 62% of symmetric synapses were on dendritic shafts, 31% on spines and 7% on somata (Beaulieu & Colonnier, 1985).

### 1.3 Summary Comparison Table

| Feature | Type I (Asymmetric) | Type II (Symmetric) |
|---|---|---|
| PSD thickness | Thick (about 35-50 nm) | Thin, about as thick as the presynaptic density |
| Pre vs. post density | Asymmetric (post >> pre) | Symmetric (post approximately equals pre) |
| Vesicle shape | Round/spherical | Pleomorphic/flattened |
| Cleft width | ~20 nm | ~12 nm |
| Neurotransmitter | Glutamate (excitatory) | GABA (inhibitory) |
| Typical targets | Spines, dendritic shafts | Dendritic shafts, soma, AIS; some spines |

---

{% include figure.html
   src="/assets/images/content-library/em/synapse-asymmetric-vs-symmetric.jpg"
   alt="Two synapses side by side at 4 nm per pixel: an excitatory synapse on the left and an inhibitory synapse on the right, each marked only by ticks at the frame edge so the densities are unobstructed."
   caption="Two real synapses at matched scale, the dataset&#39;s own excitatory (left) and inhibitory (right) calls. Nothing is drawn over either synapse. The ticks sit at the frame edge and point to the center, because the density is the evidence. The asymmetry is <em>subtle</em>: at 4 nm per pixel a Type I PSD is only 8&ndash;12 pixels thick, and H01&#39;s own excitatory/inhibitory classifier is right about 85&ndash;87% of the time. Idealized diagrams hide this."
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024). Rendered by <code>scripts/render_em_figures.py</code>." %}

## 2. The Continuum Problem

Not every synapse fits the Type I / Type II split. Many are hard to classify as either, and the correspondence between shape and function has exceptions (Klemann & Roubos, 2011). The usual sources of ambiguity:

- **Intermediate synapses**: Some synapses show a PSD that is thicker than typical Type II but thinner than classic Type I. Vesicles may be round but the density is not strongly asymmetric.
- **Fixation effects**: Vesicle shape is influenced by fixation and osmolarity of the fixative. Glutaraldehyde fixation tends to preserve round vesicle shape, while some fixation protocols can flatten vesicles artifactually.
- **Sectioning angle**: A synapse cut obliquely may appear to have a thinner PSD than it actually does, because the section grazes the PSD rather than cutting through its full thickness.
- **Regional variation**: Synapse morphology varies across brain regions. Synapses in the cerebellum, for example, have somewhat different morphological features than cortical synapses.

**Practical guidance for annotators**: When a synapse does not clearly fit Type I or Type II, classify it as "uncertain" or "intermediate" rather than forcing a categorization. Record the features that made classification difficult. Serial-section analysis (examining the synapse across 2-3 adjacent sections) often resolves ambiguous cases.

---

## 3. Synaptic Cleft Structure

The synaptic cleft is the extracellular gap between the pre- and postsynaptic membranes. Despite its small size, it has important structural features:

- **Width**: 12-20 nm, depending on synapse type. The cleft is not empty but filled with proteinaceous material.
- **Cleft material**: Trans-synaptic adhesion complexes span the cleft, including:
  - Neurexin (presynaptic) binding to neuroligin (postsynaptic)
  - SynCAM homophilic interactions
  - Ephrin-Eph receptor signaling complexes
- **EM appearance**: A lighter band (the cleft lumen) flanked by two dark lines (the pre- and postsynaptic membranes). The cleft material appears as a faint, granular or filamentous density within the lighter band.
- **Identification significance**: The cleft is one of the features that confirms a genuine synapse. Simple membrane appositions without cleft specialization are not synapses.

---

## 4. Presynaptic Specializations

The presynaptic terminal contains several ultrastructural features beyond the vesicle cluster:

- **Active zone**: The electron-dense material on the cytoplasmic face of the presynaptic membrane where vesicle docking and fusion occur. See [Axon biology]({{ '/content-library/neuroanatomy/axon-biology/' | relative_url }}) for detail.
- **Vesicle clustering**: Synaptic vesicles are concentrated at the active zone, with a gradient from tightly packed (docked) vesicles at the membrane to more dispersed vesicles deeper in the bouton.
- **Mitochondria**: Frequently present in presynaptic terminals, positioned near the vesicle cluster to supply ATP for vesicle recycling. Their presence helps distinguish boutons from other small profiles.
- **Endocytic zones**: Lateral to the active zone, clathrin-coated pits and coated vesicles represent the endocytic machinery for vesicle membrane retrieval following exocytosis.
- **Smooth ER**: Occasionally present, sometimes forming an extension from the axonal SER network.
- **Dense projections**: In some synapse types (e.g., ribbon synapses of sensory neurons), specialized dense bodies tether vesicles near the active zone. In conventional cortical synapses, smaller dense projections may be visible as filamentous structures extending from the active zone into the vesicle cluster.

---

## 5. Postsynaptic Specializations

The postsynaptic side has its own set of ultrastructural features:

- **Postsynaptic density (PSD)**: The defining feature of the postsynaptic side, containing scaffolding proteins, receptors, and signaling molecules. Size and thickness correlate with synapse strength and type.
- **Spine apparatus**: In spine synapses, a smooth ER derivative may be present in the spine neck or head (see [Dendrite biology]({{ '/content-library/neuroanatomy/dendrite-biology/' | relative_url }})).
- **Smooth ER**: Tubular profiles of SER are often found near the PSD, serving as local calcium stores. IP3 receptor-mediated calcium release from this ER contributes to postsynaptic signaling.
- **Endocytic zones**: Clathrin-coated pits lateral to the PSD mediate AMPA receptor internalization during synaptic depression. These appear as membrane invaginations with a fuzzy coat.
- **Polyribosomes**: Clusters of ribosomes near the base of dendritic spines support local protein synthesis for synaptic plasticity.
- **Subsynaptic cistern**: In some soma synapses, a flattened cistern of ER lies just beneath the PSD, involved in calcium signaling.

---

## 6. Electrical Synapses (Gap Junctions)

While chemical synapses dominate in the mammalian brain, electrical synapses also exist:

- **Structure**: Gap junctions are composed of hexagonal arrays of connexin hemichannels (connexons). Each connexon on one cell aligns with a connexon on the adjacent cell to form a complete channel.
- **EM appearance**: The two apposed membranes are separated by a gap of about 2 nm (compared to 12-20 nm for chemical synapses). Revel and Karnovsky (1967) showed the gap by filling it with lanthanum, which also revealed the hexagonal array of subunits in face view. That array is seen in freeze-fracture or tracer-filled preparations, not in a routinely stained connectomics volume.
- **Not a tight junction**: A tight junction is pentalaminar: the outer leaflets of the two membranes fuse and no gap remains. A gap junction keeps its narrow gap. At 4-8 nm pixels, though, a 2 nm gap is below one pixel, so in most connectomics volumes a gap junction looks like a short stretch of fused, darkened membrane with no vesicles on either side.
- **Distribution in cortex**: Gap junctions are found primarily between GABAergic interneurons (especially parvalbumin-positive basket cells and between cells of the same subtype). They are composed of connexin-36 (Cx36) in neurons.
- **Frequency**: Rare compared to chemical synapses. Neuronal coupling and Cx36 expression rise transiently in early postnatal development and then stay low in the adult, confined to specific subsets of neurons (Belousov & Fontes, 2013). Expect to meet gap junctions only occasionally in an adult cortical volume, and do not expect a detector trained on chemical synapses to find them.
- **Functional significance**: Gap junctions allow direct electrical coupling and can synchronize the firing of connected interneurons, contributing to network oscillations (particularly gamma oscillations).

---

## 7. Multi-Synapse Boutons

In hippocampal and cortical EM, a single presynaptic bouton often contacts more than one postsynaptic target:

- **Prevalence**: Along CA3-to-CA1 axons in rat hippocampal stratum radiatum, 19% of varicosities had 2-4 postsynaptic densities, 68% had one, and 13% had none (Shepherd & Harris, 1998).
- **Arrangement**: The bouton may contact spines from different dendrites (divergent output: one axon, several postsynaptic partners) or two spines from the same dendrite (same-cell contact).
- **Active zones**: Each contact typically has its own active zone and PSD, though they share the same vesicle pool.
- **Annotation implications**: Multi-synapse boutons must be carefully annotated. Each synaptic contact is a separate synapse, even though they share a presynaptic terminal. Annotators should record both the bouton identity and the individual synaptic connections.

---

## 8. Synapse Identification Protocol for Annotators

A systematic approach reduces errors and increases consistency:

### Step 1: Find a Membrane Apposition

Identify two profiles (one potential presynaptic, one potential postsynaptic) whose membranes are closely apposed and running roughly parallel for at least 100-200 nm.

### Step 2: Check for a Vesicle Cluster

On the candidate presynaptic side, look for a cluster of vesicles (at least 3-5 vesicles) near the apposed membrane. Vesicles should be round or slightly pleomorphic, about 35-45 nm in diameter. If no vesicles are present, the apposition is unlikely to be a synapse.

### Step 3: Identify the Postsynaptic Density

On the opposite side of the membrane apposition, look for an electron-dense band on the cytoplasmic face. For Type I synapses, this should be thick and prominent. For Type II, it may be subtle.

### Step 4: Verify Across Adjacent Sections

A genuine synapse should be visible in at least 2-3 serial sections. Single-section appearances may be:
- A grazing cut through a synapse (still valid but less certain)
- An artifact or non-synaptic membrane apposition
If the synapse is confirmed across multiple sections, confidence is high.

### Step 5: Classify the Synapse Type

Using the criteria in Section 1:
- Thick PSD + round vesicles + wide cleft = Type I (asymmetric, excitatory)
- Thin symmetric densities + pleomorphic vesicles + narrow cleft = Type II (symmetric, inhibitory)
- Ambiguous features = mark as uncertain

### Step 6: Assign Confidence

Rate your confidence:
- **High**: All features clearly present, verified in multiple sections, unambiguous type classification.
- **Medium**: Most features present but one criterion is unclear (e.g., vesicle shape hard to judge).
- **Low**: Possible synapse but features are marginal; could be a non-synaptic apposition.

---

## 9. Worked Examples

### 9.1 Identifying an Asymmetric Spine Synapse

**Scenario**: On a dendritic spine head in layer II/III of cortex, you observe a membrane apposition with an adjacent axon terminal.

1. **Vesicle check**: The axon terminal contains approximately 150 round vesicles (~45 nm diameter) clustered near the apposed membrane. Confirmed presynaptic.
2. **PSD check**: A prominent electron-dense band (~40 nm thick, ~250 nm long) is present on the cytoplasmic face of the spine head membrane. Confirmed postsynaptic.
3. **Cleft**: The gap between membranes is approximately 20 nm, with visible cleft material.
4. **Serial sections**: The synapse is present in 4 consecutive sections.
5. **Classification**: Thick PSD + round vesicles + 20 nm cleft = Type I asymmetric (excitatory, glutamatergic).
6. **Confidence**: High.

### 9.2 Identifying a Symmetric Soma Synapse

**Scenario**: On the surface of a pyramidal neuron soma, a bouton is apposed to the cell body membrane.

1. **Vesicle check**: The bouton contains vesicles that are smaller and more variable in shape — some oval, some slightly flattened. They cluster near the apposed membrane.
2. **Density check**: Both the presynaptic and postsynaptic sides show a thin electron-dense coating. The postsynaptic density is not dramatically thicker than the presynaptic density. Approximately symmetric.
3. **Cleft**: The gap is approximately 12 nm, narrower than the previous example.
4. **Serial sections**: Visible in 3 sections.
5. **Classification**: Symmetric densities + pleomorphic vesicles + narrow cleft = Type II symmetric (inhibitory, GABAergic).
6. **Confidence**: High.

### 9.3 An Ambiguous Case

**Scenario**: On a dendritic shaft, a bouton is apposed with vesicles present, but the PSD is thinner than typical Type I.

1. **Vesicle check**: Vesicles present, mostly round but a few appear slightly ovoid.
2. **Density check**: The postsynaptic density is present but only approximately 20 nm thick — thicker than a classic Type II but thinner than a clear Type I. The presynaptic density is modest.
3. **Cleft**: Approximately 15 nm — intermediate.
4. **Considerations**: This could be a Type I synapse cut obliquely (which would thin the apparent PSD), or a genuine intermediate-type synapse. The shaft location is compatible with either type.
5. **Resolution strategy**: (a) Examine adjacent sections for a section where the PSD may appear thicker. (b) Note the postsynaptic target — if the dendrite is aspiny (smooth), the synapse is more likely inhibitory (Type II on a GABAergic interneuron dendrite). (c) If resolution remains uncertain, mark as "ambiguous" with a note.
6. **Confidence**: Low to medium.

---

## 10. Common Misconceptions

| Misconception | Reality |
|---|---|
| "Type I is always excitatory and Type II is always inhibitory." | This is the general rule and holds for most cortical synapses, but exceptions exist (Klemann & Roubos, 2011). Some neuromodulatory synapses do not fit neatly into either category. The morphological classification is a structural description, not a neurotransmitter assay. |
| "Vesicle shape alone determines synapse type." | Vesicle shape is influenced by fixation conditions. It should be considered alongside PSD thickness, cleft width, and synaptic location. No single feature is sufficient. |
| "Gap junctions are not synapses." | Electrical synapses (gap junctions) are genuine synaptic connections that mediate direct electrical communication between neurons. They are synapses by any functional definition, even though they lack vesicles. |
| "Every membrane apposition with vesicles nearby is a synapse." | Non-synaptic membrane appositions are common in the neuropil. A genuine synapse requires vesicle clustering at the active zone, a PSD (for chemical synapses), and cleft specialization. Random proximity of vesicle-containing profiles to other membranes does not constitute a synapse. |
| "Symmetric synapses are rare." | Symmetric synapses are a minority, 16% of synapses in cat area 17 (Beaulieu & Colonnier, 1985), but they are not rare, and their subtler densities make them easier to miss. In H01, the automated detector missed about 35% of inhibitory synapses, far more than excitatory ones; see [Synapse detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}). |
| "All synapses look the same across brain regions." | Synapse morphology varies significantly across regions. Cerebellar parallel fiber synapses, hippocampal mossy fiber synapses, and cortical pyramidal cell synapses each have distinctive features. |

---

## References

1. Gray EG (1959) "Axo-somatic and axo-dendritic synapses of the cerebral cortex: an electron microscope study." *Journal of Anatomy* 93:420-433. PMC1244535
2. Colonnier M (1968) "Synaptic patterns on different cell types in the different laminae of the cat visual cortex: an electron microscope study." *Brain Research* 9:268-287. doi:10.1016/0006-8993(68)90234-5
3. Harris KM, Weinberg RJ (2012) "Ultrastructure of synapses in the mammalian brain." *Cold Spring Harbor Perspectives in Biology* 4:a005587. doi:10.1101/cshperspect.a005587
4. Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System*, 3rd edition. Oxford University Press.
5. Bhatt DH, Zhang S, Gan WB (2009) "Dendritic spine dynamics." *Annual Review of Physiology* 71:261-282.
6. Shepherd GMG, Harris KM (1998) "Three-dimensional structure and composition of CA3→CA1 axons in rat hippocampal slices: implications for presynaptic connectivity and compartmentalization." *Journal of Neuroscience* 18:8300-8310. doi:10.1523/JNEUROSCI.18-20-08300.1998
7. Uchizono K (1965) "Characteristics of excitatory and inhibitory synapses in the central nervous system of the cat." *Nature* 207:642-643. doi:10.1038/207642a0
8. Beaulieu C, Colonnier M (1985) "A laminar analysis of the number of round-asymmetrical and flat-symmetrical synapses on spines, dendritic trunks, and cell bodies in area 17 of the cat." *Journal of Comparative Neurology* 231:180-189. doi:10.1002/cne.902310206
9. Klemann CJHM, Roubos EW (2011) "The gray area between synapse structure and function: Gray's synapse types I and II revisited." *Synapse* 65:1222-1230. doi:10.1002/syn.20962
10. High B, Cole AA, Chen X, Reese TS (2015) "Electron microscopic tomography reveals discrete transcleft elements at excitatory and inhibitory synapses." *Frontiers in Synaptic Neuroscience* 7:9. doi:10.3389/fnsyn.2015.00009
11. Revel JP, Karnovsky MJ (1967) "Hexagonal array of subunits in intercellular junctions of the mouse heart and liver." *Journal of Cell Biology* 33:C7-C12. doi:10.1083/jcb.33.3.c7
12. Belousov AB, Fontes JD (2013) "Neuronal gap junctions: making and breaking connections during development and injury." *Trends in Neurosciences* 36:227-236. doi:10.1016/j.tins.2012.11.001

---

*This document is part of the NeuroTrailblazers Content Library. It is intended as an instructor reference and annotator training script. Last updated: 2026.*
