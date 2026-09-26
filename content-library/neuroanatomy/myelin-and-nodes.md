---
layout: page
title: "Myelin Sheath and Nodes of Ranvier"
permalink: /content-library/neuroanatomy/myelin-and-nodes/
image: /assets/images/content-library/neuroanatomy/myelin-and-nodes.svg
image_alt: "Stylized vector art: organelle profiles inside a curved membrane section."
description: >
  Instructor reference on myelin ultrastructure and nodal domains
  as observed in electron microscopy, covering compact myelin periodicity, wrap
  number, nodes of Ranvier, paranodal loops, Schmidt-Lanterman incisures, inner
  and outer tongues, and practical identification strategies for annotators.
topics:
  - myelin sheath
  - compact myelin
  - major dense line
  - intraperiod line
  - nodes of Ranvier
  - paranodal loops
  - Schmidt-Lanterman incisures
  - oligodendrocytes
  - Schwann cells
  - saltatory conduction
  - myelinated axons
primary_units:
  - "06"
  - "07"
difficulty: intermediate
tags:
  - neuroanatomy:myelin
  - neuroanatomy:node-of-ranvier
  - neuroanatomy:axon
  - neuroanatomy:oligodendrocyte
  - imaging:electron-microscopy
  - infrastructure:white-matter
  - proofreading:tracing
  - methodology:identification
micro_lesson_id: ml-neuro-myelin
combines_with:
  - axon-biology
  - organelle-cues
  - soma-ultrastructure
use_layout_hero: false
content_type: core
---

# Myelin Sheath and Nodes of Ranvier

## Introduction

Myelin is a spiral of glial membrane wrapped around an axon. It speeds action potential conduction and lowers the energy cost of each spike. For EM annotators it is one of the most reliable markers of axonal identity, and its periodicity, wrap number and nodal domains carry information about axon caliber, maturation and health.

This entry runs from membrane periodicity up to nodal architecture, with guidance for identification in EM datasets. It does not cover myelin development in depth or the physiology of conduction beyond what helps with identification.

---

## 1. Origin of the Myelin Sheath

### Central Nervous System (CNS)

In the CNS, myelin is produced by oligodendrocytes. Each oligodendrocyte extends several processes, each of which wraps a segment of a different axon, so one oligodendrocyte myelinates many axons at once. The number of sheaths per cell varies widely by region. The oligodendrocyte cell body is typically located some distance from the myelinated segments, connected by thin cytoplasmic processes.

### Peripheral Nervous System (PNS)

In the PNS, myelin is produced by Schwann cells. Each Schwann cell wraps a single internode of a single axon — a one-to-one relationship. The Schwann cell body sits adjacent to the myelin sheath, and its nucleus is often visible alongside the outer myelin surface in longitudinal sections.

### The Wrapping Process

Myelin formation begins when a glial process contacts an axon and begins to spiral around it. The cytoplasm is progressively squeezed out as the membrane wraps tighten, producing compact myelin. The innermost wrap (inner tongue) and outermost wrap (outer tongue) retain cytoplasm, as do occasional channels through the compact myelin (Schmidt-Lanterman incisures in PNS).

---

{% include figure.html
   src="/assets/images/content-library/em/myelin-in-grey-matter.jpg"
   alt="A field of human cortical gray matter with every myelinated axon highlighted in orange by the dataset's myelin mask, showing that they are a small minority of the profiles present."
   caption="Every myelinated axon in this gray-matter field, marked in orange by H01&#39;s myelin mask. Count profiles and the myelinated ones are a small minority, which is the claim in &sect;11 made visible. By area the mask covers 13.4% of this field, because each myelinated profile is large."
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024). Rendered by <code>scripts/render_em_figures.py</code>." %}

## 2. Compact Myelin Ultrastructure

Compact myelin has a highly regular, periodic structure that is one of the most distinctive features in EM.

### 2.1 The Major Dense Line

- **Formation**: When the cytoplasmic faces of the glial cell membrane come together (as the wrapping process squeezes out cytoplasm), the intracellular surfaces fuse to form the major dense line.
- **Appearance**: A dark, electron-dense line approximately 3 nm thick.
- **Composition**: Primarily myelin basic protein (MBP) in the CNS, which is essential for holding the cytoplasmic faces together. In the PNS, both MBP and P0 protein contribute.

### 2.2 The Intraperiod Line

- **Formation**: Where the extracellular faces of adjacent membrane wraps appose each other.
- **Appearance**: A slightly less dense line than the major dense line, sometimes appearing as a double line at high resolution (because the extracellular surfaces do not fully fuse).
- **Composition**: Proteolipid protein (PLP) and P0 protein span the membrane and contribute to extracellular adhesion.

### 2.3 Myelin Periodicity

The repeat distance from one major dense line to the next — encompassing two lipid bilayers, one major dense line, and one intraperiod line — is the myelin period:

- **In living or unfixed nerve** (X-ray diffraction): about 15.4-16.0 nm for CNS myelin and 17.3-17.8 nm for PNS myelin (Kirschner et al., 2010). PNS myelin has the wider extracellular space at the intraperiod line.
- **In fixed, resin-embedded tissue** (what EM datasets show): the period shrinks during processing, to roughly 11-12 nm, and the CNS-PNS difference becomes hard to measure. Use about 12 nm as a working value for counting lamellae.
- **EM appearance**: In high-resolution cross-sections, compact myelin appears as a series of alternating dark (major dense) and lighter (intraperiod) lines, creating a characteristic laminated or banded pattern. At lower magnification, the myelin sheath appears as a dark, homogeneous ring around the axon.

### 2.4 Visualization Considerations

- **High magnification** (>30,000x): Individual lamellae are resolved. The alternating dark/light periodicity is clearly visible. Annotators can count individual wraps.
- **Medium magnification** (10,000-30,000x): The myelin sheath appears as a thick dark ring. Individual lamellae may be partially resolved.
- **Low magnification** (<10,000x): Myelin appears as a dark annulus around a lighter axonal profile. The number of wraps is not discernible, but myelinated axons are easily distinguished from unmyelinated ones.

Connectomics volumes are described in nanometers per pixel, not magnification. Resolving a 12 nm period needs pixels of 6 nm or smaller (two pixels per period). At 4 nm per pixel, as in H01 and MICrONS, lamellae are three pixels apart and only partly resolved; at 8 nm or coarser the sheath is a dark band and wraps cannot be counted.

---

## 3. Number of Myelin Wraps

Sheath thickness scales with axon diameter, so the number of lamellae does too. You can estimate it from two measurements: lamellae ≈ sheath thickness ÷ period, where sheath thickness = (outer diameter − axon diameter) ÷ 2. With a 12 nm period:

- **0.5 micrometer axon, g-ratio 0.75**: sheath about 83 nm, about 7 lamellae.
- **1 micrometer axon, g-ratio 0.7**: sheath about 214 nm, about 18 lamellae.
- **3 micrometer axon, g-ratio 0.7**: sheath about 640 nm, about 54 lamellae.
- **10 micrometer PNS axon, g-ratio 0.6**: sheath about 3.3 micrometers, about 280 lamellae.

These are arithmetic from assumed g-ratios, not measurements; real sheaths vary around them.

### The g-ratio

The ratio of inner axon diameter to total outer diameter (including myelin) is called the g-ratio:

- **Optimal g-ratio**: Rushton's classic estimate, based on conduction speed alone, is about 0.6, which fits some peripheral fibers. CNS fibers have thinner myelin; a theoretical analysis that also weighs space and energy puts the CNS optimum near 0.77 (Chomiak & Hu, 2009). A g-ratio of 0.6-0.8 means the sheath takes up 20-40% of the fiber diameter (1 − g).
- **Significance**: For a fixed fiber diameter, too little myelin (high g-ratio) slows conduction, and too much (low g-ratio) leaves too small an axon inside.
- **Annotation use**: Measuring the g-ratio in EM volumes can flag axons with unusually thin myelin (possible demyelination or remyelination). Abnormally thick, folded myelin (tomacula) is a peripheral-nerve finding and will rarely appear in brain volumes.

---

## 4. Nodes of Ranvier

Nodes of Ranvier are the regularly spaced gaps in the myelin sheath where the axon membrane is exposed to the extracellular space. They are the sites of saltatory conduction — action potentials "jump" from node to node.

### 4.1 Nodal Architecture

- **Length**: The bare nodal gap is on the order of 1 micrometer long. In rat optic nerve and cortex, node length varied 4.4-fold and 8.7-fold between axons, but much less along a single axon (Arancibia-Cárcamo et al., 2017).
- **Internode distance**: The myelinated segment between nodes (the internode) is longer in larger fibers. Large peripheral fibers have internodes around a millimeter long; CNS internodes, especially in gray matter, are often much shorter, so a single EM volume can contain several nodes on one axon.
- **Exposed axolemma**: The nodal membrane is not truly bare. It is covered by a specialized extracellular matrix and contacted by glial processes.

### 4.2 Ultrastructural Features in EM

- **Dense undercoat**: The nodal axolemma has a thick, electron-dense coating on its cytoplasmic face, similar to (and molecularly related to) the AIS undercoat. This undercoat is composed of ankyrin-G and betaIV-spectrin, which anchor voltage-gated sodium channels (Nav1.6 is the predominant subtype at mature nodes).
- **Sodium channel clustering**: Although individual channels are not visible in conventional EM, their functional presence is inferred from the dense undercoat. Immuno-EM confirms the extreme concentration of Nav channels at nodes.
- **Nodal microvilli (PNS)**: In peripheral nerves, Schwann cell microvilli project from the terminal ends of the myelin sheath to contact the nodal axolemma. These appear as small finger-like projections surrounding the node.
- **Astrocyte contacts (CNS)**: In the central nervous system, perinodal astrocyte processes fill the space around the node instead of Schwann cell microvilli. These pale, glycogen-containing processes can be identified by their characteristic astrocytic features.
- **Extracellular matrix**: The nodal gap is filled with a proteoglycan-rich extracellular matrix that helps maintain the nodal domain. This material may appear as a faint, granular density in the extracellular space.

### 4.3 Paranodal Regions

Flanking each node are the paranodal regions, where the myelin sheath terminates:

- **Paranodal loops**: The terminal turns of the myelin spiral do not end abruptly. Instead, each lamella forms a cytoplasm-containing loop that contacts the axon membrane. These loops stack in a regular array along the paranode, creating a distinctive "staircase" pattern in longitudinal sections.
- **Septate-like junctions**: Each paranodal loop forms a specialized junction with the axolemma, mediated by the Caspr/contactin/neurofascin-155 complex. In EM, these junctions appear as periodic densities (transverse bands) bridging a gap of only a few nanometers between the loop membrane and the axon membrane.
- **Function**: Paranodal junctions serve as a diffusion barrier, preventing lateral movement of nodal sodium channels and juxtaparanodal potassium channels. They effectively define and maintain the molecular domains of the node.
- **Length**: The paranodal region is a few micrometers long on each side of the node, longer in fibers with more lamellae because each lamella adds a loop.

### 4.4 Juxtaparanodal Region

Just beyond the paranode, beneath the compact myelin:

- **Potassium channels**: Kv1.1 and Kv1.2 channels cluster in the juxtaparanodal axolemma. They are not visible in conventional EM but are important for understanding nodal physiology.
- **EM appearance**: The juxtaparanodal axolemma may show a modest undercoat density, less prominent than the nodal undercoat.

---

## 5. Schmidt-Lanterman Incisures

Schmidt-Lanterman incisures (also called Schmidt-Lanterman clefts) are cytoplasmic channels that spiral through the compact myelin sheath:

- **Location**: Primarily found in PNS myelin; rare or absent in CNS myelin.
- **Structure**: Regions where the major dense line opens to create a narrow channel of Schwann cell cytoplasm connecting the inner and outer tongues through the myelin sheath. The cytoplasmic channel spirals through the myelin, following the original wrapping trajectory.
- **EM appearance**:
  - **Longitudinal section**: Lighter streaks or bands running obliquely through the dark myelin sheath, creating a characteristic "herringbone" pattern.
  - **Cross-section**: Appear as interruptions in the compact myelin lamellae where a small pocket of cytoplasm separates adjacent lamellae.
- **Function**: Provide a cytoplasmic pathway for transport of metabolites, signaling molecules, and organelles between the Schwann cell body (outer surface) and the inner tongue (nearest the axon). Along the internode, where compact myelin would otherwise block the route, incisures are the shortcut; the paranodal loops are the other cytoplasmic path, at the ends of the sheath.
- **Contents**: The cytoplasm within incisures contains microtubules, actin filaments, and occasionally small organelles (mitochondria, ER tubules).

---

## 6. Inner and Outer Tongues

The innermost and outermost wraps of the myelin sheath retain cytoplasm and serve as the interface between compact myelin and the cell:

### 6.1 Inner Tongue (Innermost Loop)

- **Location**: The cytoplasm-containing layer directly apposed to the axon membrane.
- **Appearance**: A thin crescent of pale cytoplasm between the innermost myelin lamella and the axolemma.
- **Function**: The inner tongue is where new myelin membrane is added as the sheath grows.
- **Width**: Varies; usually very thin in mature myelin and thicker during active myelination.

### 6.2 Outer Tongue (Outermost Loop)

- **Location**: The outermost wrap of the myelin sheath, connected to the glial cell body (via the process in CNS, directly in PNS).
- **Appearance**: A thin crescent of cytoplasm on the external surface of the myelin sheath.
- **Function**: Continuous with the cell body cytoplasm (in Schwann cells) or the oligodendrocyte process (in CNS). Serves as the route for transport of newly synthesized myelin components.

---

## 7. Annotation Implications of Myelin

### 7.1 Myelin as an Axon Identifier

- **Strong positive cue**: The presence of a myelin sheath is strong evidence that the enclosed process is an axon. In the CNS, myelin is almost exclusively found around axons; dendrites are not myelinated.
- **Caveat: unmyelinated axons**: Most thin CNS axons are unmyelinated, so the absence of myelin does not exclude axon identity. Myelin does not mean a long-range excitatory axon either: in mouse neocortex, about half the myelin in layer 2/3 and a quarter in layer 4 wraps axons of parvalbumin-positive basket cells (Micheva et al., 2016).
- **Caveat: partial myelination**: Some axons are myelinated along part of their length but unmyelinated at their terminals and sometimes along intermediate segments. An axon may therefore transition from myelinated to unmyelinated within a single EM volume.

### 7.2 Node Identification for Tracing

Nodes of Ranvier can be challenging for automated segmentation and manual tracing because:

- The axon is constricted at the node (Hildebrand et al., 1993), so the profile shrinks.
- The myelin sheath is absent, so the characteristic dark ring that aids tracing disappears.
- Paranodal loops and glial contacts create a complex local environment that can confuse segmentation algorithms.

**Strategy**: When a myelinated axon seems to "disappear" between sections, check for a node. Look for the characteristic paranodal loop pattern, the dense undercoat on a bare segment of axolemma, and the re-emergence of myelin on the far side.

### 7.3 Myelin Pathology Indicators

- **Thin myelin relative to axon diameter** (high g-ratio): May indicate remyelination (new myelin sheaths are thinner than original ones) or incomplete myelination.
- **Split or vacuolated myelin**: Separation of lamellae with fluid-filled spaces, seen in edema or early demyelination.
- **Myelin debris (ovoid bodies)**: Fragments of myelin in the neuropil, indicating active demyelination. Often phagocytosed by macrophages or microglia.
- **Redundant myelin (outfolding)**: Excessive myelin forming loops that extend away from the axon. Can be a fixation artifact or a genuine pathological finding (tomaculous neuropathy).

---

## 8. Worked Example: Recognizing a Myelinated Axon in Cross-Section

**Scenario**: In a cross-section through cortical white matter, you see a circular profile surrounded by a thick dark ring.

Step-by-step identification:

1. **Dark ring assessment**: The ring shows a laminated structure at high magnification — alternating dark and lighter lines with approximately 12 nm periodicity. This is compact myelin.
2. **g-ratio estimation**: The inner axon diameter is approximately 1.5 micrometers; the total outer diameter (with myelin) is approximately 2.3 micrometers. The g-ratio is 1.5 ÷ 2.3 ≈ 0.65, within the normal range.
3. **Wrap count check**: The sheath is (2.3 − 1.5) ÷ 2 = 0.4 micrometers thick. At a 12 nm period that predicts about 33 lamellae. Counting about 33 at high resolution confirms the measurement; a very different count means the section is oblique or the period is distorted.
4. **Axon contents**: The enclosed profile contains a few small mitochondria (approximately 0.5 micrometers), neurofilaments and microtubules cut in cross-section (small dots and circles), and a single SER tubule. No ribosomes are visible.
5. **Inner tongue**: A thin crescent of pale cytoplasm is visible between the innermost lamella and the axon membrane.
6. **Conclusion**: Compact myelin + appropriate contents + normal g-ratio = healthy myelinated axon.

---

## 9. Worked Example: Identifying a Node of Ranvier

**Scenario**: While tracing a myelinated axon through serial sections, the myelin sheath suddenly terminates on both sides, leaving a short bare segment.

Step-by-step identification:

1. **Myelin termination pattern**: On each side of the bare segment, the myelin lamellae terminate in a series of cytoplasm-filled loops (paranodal loops) that stack against the axon membrane. The characteristic "staircase" pattern is visible.
2. **Nodal gap length**: The bare axon segment is approximately 1.5 micrometers long — consistent with a node of Ranvier.
3. **Dense undercoat**: The axolemma in the bare segment shows a dark electron-dense coating on the cytoplasmic face. This is the ankyrin-G-based undercoat enriched in sodium channels.
4. **Glial contacts**: Pale astrocyte processes (containing glycogen granules) contact the nodal axolemma. No Schwann cell microvilli are present (confirming CNS location).
5. **Axon caliber**: The axon diameter narrows slightly at the node compared with the internode. This is normal.
6. **Continuity confirmation**: The myelin resumes on the far side with similar periodicity and wrap number, confirming this is the same axon.
7. **Conclusion**: Paranodal loops + bare axolemma with dense undercoat + astrocyte contacts + transient caliber reduction = node of Ranvier (CNS).

---

## 10. Worked Example: Distinguishing Compact Myelin from Artifact

**Scenario**: A dark, laminated ring surrounds a small profile, but something looks unusual.

Potential artifacts that mimic or distort myelin:

1. **Fixation-induced myelin splitting**: If alternating lamellae are separated by clear spaces, the "myelin" may be artifactually swollen. Genuine compact myelin has tightly apposed lamellae with no gaps between them at EM resolution. Mild splitting at the intraperiod line can occur during fixation and is a common processing artifact, not necessarily pathology.
2. **Oblique sectioning**: If the section cuts through myelin at an angle rather than perpendicular to the axon, the myelin ring may appear asymmetric — thicker on one side, thinner on the other. This is a geometric artifact, not a biological feature.
3. **Membrane whorls**: Occasionally, membrane debris in the neuropil forms concentric lamellated structures that superficially resemble myelin. To distinguish: (a) check for an enclosed axon with appropriate cytoskeletal contents, (b) check for inner and outer tongues, (c) verify that the periodicity matches known myelin values. Membrane whorls often have irregular periodicity and lack a central axon.
4. **Resin artifacts**: Folds or wrinkles in the section can create dark bands that mimic lamellae. These typically extend linearly across multiple structures rather than forming a closed ring.

---

## 11. Common Misconceptions

| Misconception | Reality |
|---|---|
| "All axons in the CNS are myelinated." | Most thin CNS axons are unmyelinated. In cortical gray matter, unmyelinated axons vastly outnumber myelinated ones (see the H01 field above). |
| "Myelin is made of fat." | Myelin is made of tightly compacted glial cell membrane, which is lipid-rich (roughly 70-80% lipid by dry weight) but also contains structural proteins (MBP, PLP, P0). |
| "The node of Ranvier is a gap in insulation." | While the node is a gap in myelin, it is a highly organized functional domain with clustered ion channels, specialized extracellular matrix, and glial contacts. |
| "CNS and PNS myelin are the same." | CNS myelin (oligodendrocyte) and PNS myelin (Schwann cell) differ in main structural protein (PLP vs. P0), periodicity in unfixed tissue, one-to-many vs. one-to-one wrapping, and how common Schmidt-Lanterman incisures are. |
| "Thicker myelin always means faster conduction." | For a fiber of fixed total diameter, conduction speed peaks at an intermediate g-ratio. Past that point, more myelin means a thinner axon inside, and conduction slows. |
| "Paranodal loops are just myelin endings." | Paranodal loops form septate-like junctions that serve as molecular fences, maintaining the distinct ion channel domains of the node and juxtaparanode. |

---

## References

1. Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System*, 3rd edition. Oxford University Press.
2. Hildebrand C, Remahl S, Persson H, Bjartmar C (1993) "Myelinated nerve fibres in the CNS." *Progress in Neurobiology* 40:319-384.
3. Stassart RM, Möbius W, Nave KA, Edgar JM (2018) "The axon-myelin unit in development and degenerative disease." *Frontiers in Neuroscience* 12:467.
4. Salzer JL (2003) "Polarized domains of myelinated axons." *Neuron* 40:297-318.
5. Rasband MN, Peles E (2021) "Mechanisms of node of Ranvier assembly." *Nature Reviews Neuroscience* 22:7-20.
6. Nave KA, Werner HB (2014) "Myelination of the nervous system: mechanisms and functions." *Annual Review of Cell and Developmental Biology* 30:503-533.
7. Waxman SG, Ritchie JM (1993) "Molecular dissection of the myelinated axon." *Annals of Neurology* 33:121-136.
8. Kirschner DA, Avila RL, Gamez Sazo RE, et al. (2010) "Rapid assessment of internodal myelin integrity in central nervous system tissue." *Journal of Neuroscience Research* 88:712-721. doi:10.1002/jnr.22241
9. Chomiak T, Hu B (2009) "What is the optimal value of the g-ratio for myelinated fibers in the rat CNS? A theoretical approach." *PLoS ONE* 4:e7754. doi:10.1371/journal.pone.0007754
10. Arancibia-Cárcamo IL, Ford MC, Cossell L, et al. (2017) "Node of Ranvier length as a potential regulator of myelinated axon conduction speed." *eLife* 6:e23329. doi:10.7554/eLife.23329
11. Micheva KD, Wolman D, Mensh BD, et al. (2016) "A large fraction of neocortical myelin ensheathes axons of local inhibitory neurons." *eLife* 5:e15784. doi:10.7554/eLife.15784

---

*This document is part of the NeuroTrailblazers Content Library. It is intended as an instructor reference and annotator training script. Last updated: 2026.*
