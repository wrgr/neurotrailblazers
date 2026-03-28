---
layout: page
title: "Synapse Classification and Identification"
permalink: /content-library/neuroanatomy/synapse-classification/
description: >
  Comprehensive instructor reference on synapse classification in electron microscopy,
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
  - unit-3-synaptic-structure
  - unit-4-circuit-analysis
  - unit-5-annotation-methods
difficulty: intermediate
---

# Synapse Classification and Identification

## Introduction

Synapse identification and classification is one of the most critical skills for EM annotators and one of the primary goals of connectomics. The ability to distinguish excitatory from inhibitory synapses, to separate genuine synapses from look-alikes, and to systematically annotate them across a volume is foundational to circuit reconstruction. This script provides a detailed guide to synapse ultrastructure and classification, grounded in the framework established by E. G. Gray in 1959 and refined over subsequent decades.

---

## 1. The Gray Classification System

In 1959, Edward George Gray published a landmark paper describing two morphologically distinct synapse types in the cerebral cortex of the rat (Gray, 1959). This classification remains the standard framework for EM-based synapse identification.

### 1.1 Type I (Asymmetric) Synapses

Type I synapses are characterized by a pronounced asymmetry between the pre- and postsynaptic densities:

- **Postsynaptic density (PSD)**: Thick and conspicuous, typically greater than 30 nm in thickness. The PSD appears as a prominent electron-dense band on the cytoplasmic face of the postsynaptic membrane.
- **Presynaptic density**: Thin or modest, creating the defining asymmetry — the postsynaptic side is much more electron-dense than the presynaptic side.
- **Vesicle morphology**: Round or spherical vesicles, approximately 40-50 nm in diameter. The round shape is maintained in well-fixed, aldehyde-fixed tissue.
- **Synaptic cleft width**: Approximately 20 nm, wider than Type II synapses.
- **Cleft material**: Dense proteinaceous material fills the cleft, visible as a fuzzy band between the membranes. This material includes trans-synaptic adhesion molecules (neurexin-neuroligin complexes, SynCAMs).
- **Neurotransmitter**: Predominantly glutamatergic (excitatory).
- **Postsynaptic targets**: Most commonly found on dendritic spines (axospinous synapses) and dendritic shafts (axodendritic synapses). Rare on somata.

### 1.2 Type II (Symmetric) Synapses

Type II synapses show roughly equal density on both sides of the synaptic junction:

- **Postsynaptic density**: Thin, comparable in thickness to the presynaptic density. Both sides show a modest electron-dense coating, creating the symmetric appearance.
- **Presynaptic density**: Similar thickness to the PSD, contributing to the overall symmetry.
- **Vesicle morphology**: Pleomorphic (variable in shape) or flattened vesicles. In aldehyde-fixed tissue, these vesicles tend to adopt oval or flattened profiles rather than the perfectly round shape of Type I vesicles. Note: vesicle shape is somewhat fixation-dependent, and some authors prefer to describe these as "pleomorphic" rather than "flattened."
- **Synaptic cleft width**: Approximately 12 nm, narrower than Type I.
- **Cleft material**: Present but less prominent than in Type I.
- **Neurotransmitter**: Predominantly GABAergic (inhibitory). Also includes glycinergic synapses in brainstem and spinal cord.
- **Postsynaptic targets**: Found on somata (axosomatic synapses), proximal dendrites (axodendritic on shaft), and the axon initial segment (axoaxonic synapses). Can also occur on dendritic shafts at any level.

### 1.3 Summary Comparison Table

| Feature | Type I (Asymmetric) | Type II (Symmetric) |
|---|---|---|
| PSD thickness | Thick (>30 nm) | Thin (~15 nm) |
| Pre vs. post density | Asymmetric (post >> pre) | Symmetric (post approximately equals pre) |
| Vesicle shape | Round/spherical | Pleomorphic/flattened |
| Cleft width | ~20 nm | ~12 nm |
| Neurotransmitter | Glutamate (excitatory) | GABA (inhibitory) |
| Typical targets | Spines, distal dendrite shafts | Soma, proximal dendrites, AIS |

---

## 2. The Continuum Problem

An important caveat: not all synapses fit neatly into the Type I / Type II dichotomy. Colonnier (1968) was among the first to emphasize that synapses exist on a morphological continuum:

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

- **Active zone**: The electron-dense material on the cytoplasmic face of the presynaptic membrane where vesicle docking and fusion occur. See axon-biology.md for detail.
- **Vesicle clustering**: Synaptic vesicles are concentrated at the active zone, with a gradient from tightly packed (docked) vesicles at the membrane to more dispersed vesicles deeper in the bouton.
- **Mitochondria**: Frequently present in presynaptic terminals, positioned near the vesicle cluster to supply ATP for vesicle recycling. Their presence helps distinguish boutons from other small profiles.
- **Endocytic zones**: Lateral to the active zone, clathrin-coated pits and coated vesicles represent the endocytic machinery for vesicle membrane retrieval following exocytosis.
- **Smooth ER**: Occasionally present, sometimes forming an extension from the axonal SER network.
- **Dense projections**: In some synapse types (e.g., ribbon synapses of sensory neurons), specialized dense bodies tether vesicles near the active zone. In conventional cortical synapses, smaller dense projections may be visible as filamentous structures extending from the active zone into the vesicle cluster.

---

## 5. Postsynaptic Specializations

The postsynaptic side has its own set of ultrastructural features:

- **Postsynaptic density (PSD)**: The defining feature of the postsynaptic side, containing scaffolding proteins, receptors, and signaling molecules. Size and thickness correlate with synapse strength and type.
- **Spine apparatus**: In spine synapses, a smooth ER derivative may be present in the spine neck or head (see dendrite-biology.md).
- **Smooth ER**: Tubular profiles of SER are often found near the PSD, serving as local calcium stores. IP3 receptor-mediated calcium release from this ER contributes to postsynaptic signaling.
- **Endocytic zones**: Clathrin-coated pits lateral to the PSD mediate AMPA receptor internalization during synaptic depression. These appear as membrane invaginations with a fuzzy coat.
- **Polyribosomes**: Clusters of ribosomes near the base of dendritic spines support local protein synthesis for synaptic plasticity.
- **Subsynaptic cistern**: In some soma synapses, a flattened cistern of ER lies just beneath the PSD, involved in calcium signaling.

---

## 6. Electrical Synapses (Gap Junctions)

While chemical synapses dominate in the mammalian brain, electrical synapses also exist:

- **Structure**: Gap junctions are composed of hexagonal arrays of connexin hemichannels (connexons). Each connexon on one cell aligns with a connexon on the adjacent cell to form a complete channel.
- **EM appearance**: The two apposed membranes are separated by an extremely narrow gap of approximately 2-3 nm (compared to 12-20 nm for chemical synapses). At high magnification, the regular array of connexon complexes may be visible as a periodic structure with approximately 9 nm spacing.
- **Pentalaminar appearance**: In cross-section, the gap junction appears as five layers — outer leaflet, inner leaflet of cell 1, the narrow gap, inner leaflet, outer leaflet of cell 2 — with the two inner leaflets appearing darker due to the connexon proteins.
- **Distribution in cortex**: Gap junctions are found primarily between GABAergic interneurons (especially parvalbumin-positive basket cells and between cells of the same subtype). They are composed of connexin-36 (Cx36) in neurons.
- **Frequency**: Relatively rare compared to chemical synapses. In cortical EM volumes, gap junctions may be encountered only occasionally.
- **Functional significance**: Gap junctions allow direct electrical coupling and can synchronize the firing of connected interneurons, contributing to network oscillations (particularly gamma oscillations).

---

## 7. Multi-Synapse Boutons

A common finding in cortical EM is that a single presynaptic bouton contacts more than one postsynaptic target:

- **Prevalence**: In hippocampal CA1, approximately 20-40% of boutons are multi-synapse boutons contacting 2-3 postsynaptic targets (Shepherd & Harris, 1998).
- **Arrangement**: The bouton may contact two spines from different dendrites (convergent input) or two spines from the same dendrite (same-cell contact).
- **Active zones**: Each contact typically has its own active zone and PSD, though they share the same vesicle pool.
- **Annotation implications**: Multi-synapse boutons must be carefully annotated. Each synaptic contact is a separate synapse, even though they share a presynaptic terminal. Annotators should record both the bouton identity and the individual synaptic connections.

---

## 8. Synapse Identification Protocol for Annotators

A systematic approach reduces errors and increases consistency:

### Step 1: Find a Membrane Apposition

Identify two profiles (one potential presynaptic, one potential postsynaptic) whose membranes are closely apposed and running roughly parallel for at least 100-200 nm.

### Step 2: Check for a Vesicle Cluster

On the candidate presynaptic side, look for a cluster of vesicles (at least 3-5 vesicles) near the apposed membrane. Vesicles should be round or slightly pleomorphic, 35-50 nm in diameter. If no vesicles are present, the apposition is unlikely to be a synapse.

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
| "Type I is always excitatory and Type II is always inhibitory." | This is the general rule and holds for the vast majority of cortical synapses, but exceptions exist. Some neuromodulatory synapses do not fit neatly into either category. The morphological classification is a structural description, not a neurotransmitter assay. |
| "Vesicle shape alone determines synapse type." | Vesicle shape is influenced by fixation conditions. It should be considered alongside PSD thickness, cleft width, and synaptic location. No single feature is sufficient. |
| "Gap junctions are not synapses." | Electrical synapses (gap junctions) are genuine synaptic connections that mediate direct electrical communication between neurons. They are synapses by any functional definition, even though they lack vesicles. |
| "Every membrane apposition with vesicles nearby is a synapse." | Non-synaptic membrane appositions are common in the neuropil. A genuine synapse requires vesicle clustering at the active zone, a PSD (for chemical synapses), and cleft specialization. Random proximity of vesicle-containing profiles to other membranes does not constitute a synapse. |
| "Symmetric synapses are rare." | Type II symmetric synapses are less numerous than Type I (roughly 15-20% of cortical synapses), but they are functionally critical and must not be overlooked. Their subtler morphology makes them harder to detect, leading to systematic undercounting. |
| "All synapses look the same across brain regions." | Synapse morphology varies significantly across regions. Cerebellar parallel fiber synapses, hippocampal mossy fiber synapses, and cortical pyramidal cell synapses each have distinctive features. |

---

## References

1. Gray EG (1959) "Axo-somatic and axo-dendritic synapses of the cerebral cortex: an electron microscope study." *Journal of Anatomy* 93:420-433.
2. Colonnier M (1968) "Synaptic patterns on different cell types in the different laminae of the cat visual cortex: an electron microscope study." *Brain Research* 9:268-287.
3. Harris KM, Weinberg RJ (2012) "Ultrastructure of synapses in the mammalian brain." *Cold Spring Harbor Perspectives in Biology* 4:a005587.
4. Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System*, 3rd edition. Oxford University Press.
5. Bhatt DH, Zhang S, Bhatt WB (2009) "Dendritic spine dynamics." *Annual Review of Physiology* 71:261-282.
6. Shepherd GMG, Harris KM (1998) "Three-dimensional structure and composition of CA3-CA1 axons in rat hippocampal slices." *Journal of Neuroscience* 18:8300-8310.
7. Harris KM, Bhatt DH (2004) "Bhatt and Harris on synaptic ultrastructure." Reference for synapse quantification.

---

*This document is part of the NeuroTrailblazers Content Library. It is intended as an instructor reference and annotator training script. Last updated: 2026.*
