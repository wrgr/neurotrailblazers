---
layout: page
title: "Axon Biology and Ultrastructure"
permalink: /content-library/neuroanatomy/axon-biology/
image: /assets/images/content-library/neuroanatomy/axon-biology.svg
image_alt: "Stylized vector art: organelle profiles inside a curved membrane section."
description: >
  Instructor reference on axonal structure and ultrastructure as
  observed in electron microscopy, covering the axon initial segment, myelinated
  and unmyelinated axon morphology, synaptic boutons, vesicle pools, active zones,
  dense-core vesicles, and practical identification strategies for annotators.
topics:
  - axons
  - axon initial segment
  - unmyelinated axons
  - myelinated axons
  - en passant boutons
  - terminal boutons
  - synaptic vesicle pools
  - active zones
  - dense-core vesicles
  - neurofilaments
  - axonal transport
primary_units:
  - "05"
  - "06"
difficulty: intermediate
tags:
  - neuroanatomy:axon
  - neuroanatomy:bouton
  - neuroanatomy:vesicle
  - neuroanatomy:cytoskeleton
  - neuroanatomy:axon-initial-segment
  - connectomics:synapse
  - imaging:electron-microscopy
  - methodology:identification
micro_lesson_id: ml-neuro-axon
combines_with:
  - myelin-and-nodes
  - synapse-classification
  - soma-ultrastructure
use_layout_hero: false
content_type: core
---

# Axon Biology and Ultrastructure

## Introduction

The axon is the output process of the neuron. Each neuron typically gives rise to a single axon that carries action potentials away from the soma and delivers signals to target cells through synaptic transmission. Axons are structurally and molecularly distinct from dendrites, and most tracing errors in EM volumes involve thin axons, so an annotator needs to know what one looks like in cross-section. This script covers the axon from its origin at the axon initial segment through its unmyelinated and myelinated lengths to its synaptic terminals.

---

## 1. Axon Overview

Key distinguishing properties of axons compared to dendrites:

- **Single per neuron**: In most cases, each neuron has exactly one axon (though it may branch extensively).
- **Uniform caliber**: Unlike dendrites, axons maintain a relatively constant diameter along their length (except at branch points and boutons).
- **Extended length**: Axons range from less than a millimeter (local interneurons) to over a meter (corticospinal tract neurons, peripheral motor neurons).
- **No visible ribosomes beyond the initial segment**: In routine EM, mature vertebrate axons show no rough ER and no recognizable ribosome clusters past the axon initial segment. Most axonal proteins are made in the soma and transported. Local translation in axons does happen: expansion microscopy found mRNA and ribosomes in most presynaptic terminals in hippocampus and forebrain (Hafner et al., 2019). Those ribosomes are too sparse to see in a connectomics volume, which is why "no ribosomes" still works as an EM cue.
- **Uniform microtubule polarity**: In vertebrates, axonal microtubules are oriented uniformly with plus-ends pointing distally (away from the soma). This contrasts with the mixed polarity in dendrites.
- **Synaptic vesicles**: Axons contain clusters of synaptic vesicles at their boutons. In cortex and hippocampus, dendrites almost never do. The exceptions are dendrodendritic synapses, such as those between mitral and granule cells in the olfactory bulb (Rall et al., 1966), where a dendrite is presynaptic and carries vesicles.

---

## 2. The Axon Initial Segment (AIS)

The axon initial segment is the specialized proximal region of the axon where action potential initiation occurs. It spans roughly 20-60 micrometers from the soma and has a unique ultrastructure that makes it identifiable in EM (Leterrier, 2018).

### Structural Features Visible in EM

- **Dense undercoat**: A layer of finely granular, electron-dense material lines the cytoplasmic face of the plasma membrane (Palay et al., 1968). A similar undercoat lies beneath the membrane at nodes of Ranvier. The undercoat contains ankyrin-G, betaIV-spectrin, and associated proteins that anchor voltage-gated sodium channels (Nav1.6, Nav1.2) and potassium channels (Kv7, Kv1).
- **Fasciculated microtubules**: Unlike the loosely arranged microtubules in dendrites and the soma, AIS microtubules are bundled into small fascicles of closely spaced, parallel microtubules. Palay et al. (1968) found these fascicles only in the axon hillock and initial segment and called them the principal identifying mark. The protein TRIM46 is required to form these parallel, plus-end-out bundles (van Beuningen et al., 2015).
- **Few ribosomes, no Nissl bodies**: The AIS contains scattered clusters of ribosomes, but they are not organized into Nissl bodies (stacked rough ER) and they vanish at the end of the initial segment (Palay et al., 1968). So a few ribosomes in the first tens of micrometers of an axon do not argue against axon identity. Stacked rough ER does.
- **Sparse organelles**: Compared to proximal dendrites of similar caliber, the AIS has fewer mitochondria, no Golgi outposts, and no rough ER.
- **Occasional synapses**: The AIS receives GABAergic synapses, often from chandelier cells (axo-axonic cells). These Type II symmetric synapses on the AIS are a distinctive feature and can help confirm AIS identity.

### Functional Significance

The AIS is where action potentials usually start. In cortical pyramidal neurons, the sodium channel density at the AIS is about 50 times that in the proximal dendrites (Kole et al., 2008), which gives the AIS the lowest threshold in the cell. The undercoat is the scaffold that holds those channels in place.

---

## 3. Unmyelinated Axons

Many axons in the central nervous system are unmyelinated, particularly those of local-circuit interneurons and some long-range projection neurons. In EM:

- **Diameter**: Typically 0.1-1.0 micrometers. Thin local axons sit at the bottom of that range: the shafts between varicosities on CA3-to-CA1 axons measured 0.17 ± 0.04 micrometers (Shepherd & Harris, 1998).
- **Cytoskeletal contents**: Neurofilaments (10 nm intermediate filaments) and microtubules (25 nm outer diameter) run longitudinally. The ratio of neurofilaments to microtubules increases with axon diameter.
- **Smooth ER**: One or a few narrow smooth ER tubules run along the axon, serving as a calcium store and membrane reservoir.
- **Mitochondria**: Sparse, short and uniform. In layer 2/3 cortical pyramidal neurons, axonal mitochondria were 0.45-1.13 micrometers long (10th-90th percentile) and occupied about 8% of axon length (Lewis et al., 2018). Many boutons have none: 53% of CA3-to-CA1 varicosities lacked mitochondria (Shepherd & Harris, 1998).
- **No ribosomes**: The complete absence of ribosomes and rough ER is a defining negative feature.
- **Ensheathing glia**: In the CNS, unmyelinated axons may be partially wrapped by astrocyte processes but lack the compact myelin of oligodendrocytes. In the PNS, Remak bundles group multiple unmyelinated axons within a single Schwann cell.

### Annotation Challenges

Unmyelinated axons are among the most difficult structures to trace in EM volumes because:

- Their small diameter means they occupy only a few pixels in lower-resolution datasets.
- They can be confused with thin dendritic branches, glial processes, or even imaging artifacts.
- They run in dense bundles where individual axons are hard to separate.

---

## 4. Axon Terminals: Boutons

Axon terminals are the synaptic output sites where action potentials trigger neurotransmitter release. Two major types exist.

### 4.1 En Passant Boutons

- **Definition**: Swellings along the axon shaft that form synapses without terminating the axon. The axon continues beyond the bouton to form additional synapses.
- **Morphology**: The axon locally swells to roughly 0.5-1 micrometers across. On CA3-to-CA1 axons, varicosities were 1.1 ± 0.7 micrometers long, joined by shafts only 0.17 micrometers wide (Shepherd & Harris, 1998).
- **Vesicle content**: Clusters of synaptic vesicles congregate at the active zone face of the bouton. Mitochondria are frequently present.
- **Prevalence**: The usual form in cortex and hippocampus. Along CA3-to-CA1 axons, synapses occurred every 2.7 micrometers on average (Shepherd & Harris, 1998). That is about 370 synapses per millimeter of axon, so an axon with several millimeters of local branches carries thousands.
- **EM identification**: Look for a local swelling in an axon profile containing vesicle clusters apposed to a postsynaptic target with visible PSD.

### 4.2 Terminal Boutons

- **Definition**: Boutons at the end of an axonal branch, where the axon terminates.
- **Morphology**: Variable. Size alone does not separate terminal from en passant boutons.
- **Classic examples**: Neuromuscular junction terminals and the calyx of Held. Hippocampal mossy fiber boutons are often cited here, but most sit en passant along the mossy fiber axon. They are giant all the same: one reconstructed bouton averaged 25 active zones and about 20,400 synaptic vesicles (Rollenhagen et al., 2007).
- **EM identification**: A vesicle-filled profile where the axon ends. You can only call a bouton terminal after tracing it across enough sections to show the axon does not continue.

---

## 5. Synaptic Vesicle Pools

Within each bouton, synaptic vesicles are organized into functionally distinct pools (Rizzoli & Betz, 2005). While these pools are defined physiologically, they have ultrastructural correlates:

### 5.1 Readily Releasable Pool (RRP)

- **Size**: Approximately 1-2% of total vesicles (roughly 5-10 vesicles per active zone).
- **Location**: Docked at the active zone membrane, in direct contact with or within nanometers of the presynaptic membrane.
- **EM correlate**: Vesicles directly touching the presynaptic membrane at the active zone. These "docked vesicles" are visible in well-preserved tissue.
- **Function**: Released first upon action potential arrival. Determines initial release probability.

### 5.2 Recycling Pool

- **Size**: Approximately 10-20% of total vesicles.
- **Location**: Not a fixed place. In the preparations Rizzoli and Betz (2005) reviewed, recycling vesicles were scattered throughout the terminal, mixed with reserve vesicles.
- **EM correlate**: None in a conventional EM volume. Recycling and reserve vesicles look identical; telling them apart needs activity-dependent labeling, such as photoconverted FM dye.
- **Function**: Replenishes the RRP during moderate, sustained activity. Vesicles cycle between release, endocytosis, refilling, and re-docking.

### 5.3 Reserve Pool

- **Size**: Approximately 80-90% of total vesicles.
- **Location**: Distributed throughout the bouton, often tethered to the cytoskeleton by synapsin proteins.
- **EM correlate**: Most of the vesicle cloud. Because recycling vesicles are mixed in, you cannot assign any single undocked vesicle to the reserve pool from morphology.
- **Function**: Mobilized only during intense, prolonged stimulation. Synapsin phosphorylation releases vesicles from cytoskeletal tethers.

### Practical Note for Annotators

The total number of vesicles per bouton varies enormously: small en passant boutons in cortex may contain 100-300 vesicles, while large terminals like the calyx of Held and hippocampal mossy fiber boutons contain tens of thousands. Serial-section EM gives you total counts and docked counts. It does not give you the recycling/reserve split, which is a physiological measurement. Rollenhagen et al. (2007) binned mossy fiber vesicles by distance instead: about 900 within 60 nm of an active zone, about 4,400 between 60 and 200 nm, and the rest beyond.

---

## 6. Active Zones

Active zones are the specialized presynaptic membrane domains where vesicle fusion occurs. In EM:

- **Electron-dense material**: A fuzzy, electron-dense coating on the cytoplasmic face of the presynaptic membrane, directly opposite the postsynaptic PSD.
- **Vesicle docking**: Vesicles are clustered at and docked to the active zone membrane.
- **Size**: Typically 200-500 nm in diameter (en face), matching or slightly smaller than the opposing PSD.
- **Molecular composition**: RIM, Munc13, RIM-BP, ELKS, and liprin-alpha proteins form the active zone scaffold (not directly visible in conventional EM but demonstrated by immuno-EM).
- **Number per bouton**: Small cortical boutons typically have one active zone. Large terminals have many: a hippocampal mossy fiber bouton averaged 25 (range 7-45; Rollenhagen et al., 2007), and one fully reconstructed calyx of Held from a 9-day-old rat had 554, with about two anatomically docked vesicles at each (Sätzler et al., 2002).

---

## 7. Dense-Core Vesicles

In addition to the small, clear synaptic vesicles that contain classical neurotransmitters (glutamate, GABA), some boutons contain dense-core vesicles (DCVs):

- **Size**: About 80-100 nm diameter, clearly larger than clear synaptic vesicles (about 35-45 nm) (Harris & Weinberg, 2012).
- **Appearance**: A dark, electron-dense core surrounded by a clear halo and a vesicle membrane. The dense core contains the packaged neuropeptide or monoamine.
- **Contents**: Neuropeptides (substance P, neuropeptide Y, enkephalins, BDNF) or monoamines (dopamine, norepinephrine, serotonin).
- **Distribution**: Not concentrated at active zones like clear vesicles. DCVs are often found scattered throughout the bouton and may be released extrasynaptically through volume transmission.
- **Neuron-type specificity**: Particularly abundant in monoaminergic neurons (locus coeruleus, raphe nuclei, ventral tegmental area) and peptidergic interneurons. Relatively rare in glutamatergic pyramidal neurons.
- **Annotation note**: The presence of numerous DCVs in a bouton can help identify the presynaptic neuron type. A bouton with exclusively clear, round vesicles is likely glutamatergic. A bouton with pleomorphic vesicles and scattered DCVs may be from a peptide-co-releasing interneuron.

---

## 8. Worked Example: Identifying the Axon Initial Segment

**Scenario**: Tracing outward from a pyramidal neuron soma, you meet two major processes. One tapers and contains Nissl substance; the other keeps a uniform caliber and has a distinctive membrane undercoat.

Step-by-step identification:

1. **Check for rough ER**: The tapering process contains stacked rough ER and polyribosomes, so it is a dendrite. The uniform-caliber process has no rough ER and only a few small ribosome clusters near its origin, which the AIS is allowed to have. Candidate axon.
2. **Look for dense undercoat**: The candidate axon has a conspicuous electron-dense lining along the inner membrane, extending for approximately 40 micrometers from the soma. This is the AIS dense undercoat.
3. **Check microtubule organization**: Within the process, microtubules are bundled into tight fascicles rather than loosely distributed. This is characteristic of the AIS.
4. **Look for axo-axonic synapses**: Two symmetric synapses with pleomorphic vesicles are present on the process — consistent with chandelier cell inputs to the AIS.
5. **Confirm**: Dense undercoat + fasciculated microtubules + no rough ER + axo-axonic synapses = axon initial segment. If you follow the process further, the ribosome clusters should disappear where the undercoat ends.

---

## 9. Worked Example: Distinguishing an En Passant Bouton from a Dendritic Spine

**Scenario**: You see a small swelling (approximately 0.8 micrometers) associated with a synapse. Is it presynaptic (bouton) or postsynaptic (spine)?

| Feature | En Passant Bouton | Dendritic Spine |
|---|---|---|
| Contains vesicle cluster | Yes — clustered at active zone | No vesicles (or very rare) |
| Contains PSD | No (the density is on the other side of the cleft) | Yes — thick electron-dense band on cytoplasmic face |
| Ribosomes | Absent | May have polyribosomes at base |
| Continuous with | An axon of uniform caliber | A tapering dendrite shaft |
| Mitochondria | Often present | Occasionally present in larger spines |
| Spine apparatus | Never | Sometimes (smooth ER stacks) |

**Decision process**:

1. Which side has the vesicles? The vesicle-containing side is presynaptic (bouton).
2. Which side has the thick PSD? The PSD side is postsynaptic (spine or shaft).
3. Trace connections in adjacent sections to confirm continuity with parent processes.

---

## 10. Common Misconceptions

| Misconception | Reality |
|---|---|
| "Axons are always thinner than dendrites." | Myelinated axons can be several micrometers in diameter, much thicker than distal dendrites. The caliber comparison is not a reliable identification rule. |
| "All axons are myelinated." | Many CNS axons are unmyelinated, especially those of local interneurons. In cortex, unmyelinated axons vastly outnumber myelinated ones. |
| "One bouton contacts one target." | Multi-synapse boutons are common: along CA3-to-CA1 axons in rat hippocampus, 19% of varicosities had 2-4 postsynaptic densities (Shepherd & Harris, 1998). |
| "Every vesicle's position in the bouton tells you its pool." | Only docked vesicles have a pool you can read from EM (the readily releasable pool). Recycling and reserve vesicles are intermixed and look the same (Rizzoli & Betz, 2005). |
| "Dense-core vesicles are released at active zones." | DCVs are often released at non-active-zone sites on the bouton membrane, contributing to volume transmission rather than point-to-point synaptic signaling. |
| "The AIS is just a bare patch of membrane." | Two AIS features are visible in EM: the dense undercoat and the fasciculated microtubules. The clustered ion channels are not visible, but the undercoat is the scaffold that holds them. |
| "Any ribosome in a process rules out an axon." | The axon initial segment contains scattered ribosome clusters (Palay et al., 1968). What rules out an axon is stacked rough ER or ribosomes well past the initial segment. |
| "Axons never have mitochondria." | Axons contain mitochondria, though they are smaller and sparser than in somata. Boutons frequently contain mitochondria to support the energy demands of vesicle cycling. |

---

## References

1. Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System*, 3rd edition. Oxford University Press.
2. Rizzoli SO, Betz WJ (2005) "Synaptic vesicle pools." *Nature Reviews Neuroscience* 6:57-69.
3. Leterrier C (2018) "The axon initial segment: an updated viewpoint." *Journal of Neuroscience* 38:2135-2145. doi:10.1523/JNEUROSCI.1922-17.2018
4. Shepherd GMG, Harris KM (1998) "Three-dimensional structure and composition of CA3→CA1 axons in rat hippocampal slices: implications for presynaptic connectivity and compartmentalization." *Journal of Neuroscience* 18:8300-8310. doi:10.1523/JNEUROSCI.18-20-08300.1998
5. Rasband MN (2010) "The axon initial segment and the maintenance of neuronal polarity." *Nature Reviews Neuroscience* 11:552-562.
6. Kole MHP, Stuart GJ (2012) "Signal processing in the axon initial segment." *Neuron* 73:235-247.
7. Harris KM, Weinberg RJ (2012) "Ultrastructure of synapses in the mammalian brain." *Cold Spring Harbor Perspectives in Biology* 4:a005587. doi:10.1101/cshperspect.a005587
8. Palay SL, Sotelo C, Peters A, Orkand PM (1968) "The axon hillock and the initial segment." *Journal of Cell Biology* 38:193-201. doi:10.1083/jcb.38.1.193
9. Kole MHP, Ilschner SU, Kampa BM, Williams SR, Ruben PC, Stuart GJ (2008) "Action potential generation requires a high sodium channel density in the axon initial segment." *Nature Neuroscience* 11:178-186. doi:10.1038/nn2040
10. van Beuningen SFB, Will L, Harterink M, et al. (2015) "TRIM46 controls neuronal polarity and axon specification by driving the formation of parallel microtubule arrays." *Neuron* 88:1208-1226. doi:10.1016/j.neuron.2015.11.012
11. Sätzler K, Söhl LF, Bollmann JH, et al. (2002) "Three-dimensional reconstruction of a calyx of Held and its postsynaptic principal neuron in the medial nucleus of the trapezoid body." *Journal of Neuroscience* 22:10567-10579. doi:10.1523/JNEUROSCI.22-24-10567.2002
12. Rollenhagen A, Sätzler K, Rodríguez EP, et al. (2007) "Structural determinants of transmission at large hippocampal mossy fiber synapses." *Journal of Neuroscience* 27:10434-10444. doi:10.1523/JNEUROSCI.1946-07.2007
13. Lewis TL, Kwon SK, Lee A, et al. (2018) "MFF-dependent mitochondrial fission regulates presynaptic release and axon branching by limiting axonal mitochondria size." *Nature Communications* 9:5008. doi:10.1038/s41467-018-07416-2
14. Hafner AS, Donlin-Asp PG, Leitch B, Herzog E, Schuman EM (2019) "Local protein synthesis is a ubiquitous feature of neuronal pre- and postsynaptic compartments." *Science* 364:eaau3644. doi:10.1126/science.aau3644
15. Rall W, Shepherd GM, Reese TS, Brightman MW (1966) "Dendrodendritic synaptic pathway for inhibition in the olfactory bulb." *Experimental Neurology* 14:44-56. doi:10.1016/0014-4886(66)90023-9

---

*This document is part of the NeuroTrailblazers Content Library. It is intended as an instructor reference and annotator training script. Last updated: 2026.*
