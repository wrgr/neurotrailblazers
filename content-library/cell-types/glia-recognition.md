---
layout: page
title: "Glia Recognition"
permalink: /content-library/cell-types/glia-recognition/
image: /assets/images/content-library/cell-types/glia-recognition.svg
image_alt: "Stylized vector art: three cell silhouettes: branched, star-form, and amoeboid."
description: "Identifying astrocytes, oligodendrocytes, OPCs and microglia in EM: the cues for each, a four-step decision procedure, two worked examples and why glia-neuron merges matter."
topics:
  - glia
  - astrocytes
  - microglia
  - oligodendrocytes
  - myelin
  - proofreading
primary_units:
  - "07"
difficulty: "Intermediate"
tags:
  - cell-types:glia-recognition
  - cell-types:astrocyte
  - cell-types:oligodendrocyte
  - cell-types:microglia
  - imaging:electron-microscopy
  - proofreading:boundary-detection
micro_lesson_id: ml-cell-glia
combines_with:
  - axon-dendrite-classification
  - neuron-type-identification
  - artifact-taxonomy
content_type: core
---

## Overview

In the H01 sample of human temporal cortex, glia outnumbered neurons 2:1 (32,315 versus 16,087; Shapson-Coe et al. 2024). Glia also fill a sizeable share of the neuropil. A glial process wrongly merged into a neuron inflates that neuron's arbor and can hand it synapses it does not have. This page gives the EM cues and a decision procedure for the three main glial types. [Unit 07]({{ '/technical-training/07-glia/' | relative_url }}) is the course unit that teaches them.

---

## Instructor script: why glia matter for connectomics

### Glia are a large share of what the segmentation has to get right

Glial cells and their processes occupy a large share of cortical tissue. Published volume fractions vary with region, species and what counts as "glial volume", so take the figure for your own dataset rather than a single textbook number. In a densely segmented EM volume:

- **Astrocytic processes** form a fine meshwork that wraps synapses, contacts blood vessels and interleaves with neuronal processes throughout the neuropil
- **Oligodendrocyte processes** end in myelin sheaths around axons
- **Microglial processes** survey the tissue and branch extensively

When automated segmentation merges a glial process into a nearby neuron:
- The neuron gains a false branch, which distorts its morphology
- Synapses on or near the glial process can be assigned to the neuron, which corrupts connectivity
- The glial cell loses part of its territory, which distorts glial measurements

**Teaching point:** glia segmentation errors end up in the neuronal connectome.

---

{% include figure.html
   src="/assets/images/content-library/em/astrocyte-process.jpg"
   alt="Human cortex at 8 nm per pixel: a large region of pale, organelle-poor cytoplasm with scattered mitochondria, bordered by a nucleus on the right and by neuropil with a myelinated axon at the upper left."
   caption="Centered on the densest patch that H01&#39;s subcompartment model labels astrocyte in this field. Most of the frame is pale, watery cytoplasm with a few mitochondria and little else, which is the texture cue this section describes. The curved membrane on the right, with clumped chromatin behind it, is a nucleus, so this is perinuclear cytoplasm near a cell body rather than a fine process. Perisynaptic astrocyte processes are far thinner than anything here and much harder to see. Glycogen granules (20&ndash;30 nm) are under four pixels at this rendering, so not seeing them here is weak evidence. The label comes from a model, not from proofreading."
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024). Rendered by <code>scripts/render_em_figures.py</code>." %}

## Astrocytes

### EM identification cues

Astrocytes are among the most numerous glia in cortical gray matter, and their processes are the glia most often confused with neuronal processes.

**Soma features:**
- Nucleus: pale, with dispersed chromatin (euchromatic) and often an irregular outline. Compare oligodendrocyte nuclei (very dark, heterochromatic) and neuronal nuclei (pale, round, prominent nucleolus).
- Cytoplasm: glycogen granules (electron-dense particles about 20–30 nm across, often clustered) and intermediate filaments (GFAP), which show as fine filament bundles. The bundles are more prominent in fibrous astrocytes of white matter than in the protoplasmic astrocytes of gray matter. Neurons store little glycogen, so granule clusters are a strong astrocyte cue.
- Size: soma roughly 8–10 µm across, smaller than most neuronal somata.

**Process features:**
- Fine, irregular processes that fill the gaps between neuronal elements, with pale, "watery" cytoplasm and few organelles.
- Thin sheets that wrap synapses (the "tripartite synapse": presynaptic terminal, postsynaptic element and astrocytic process). These perisynaptic processes can be under 100 nm thick and are hard to segment.
- Glycogen granules in the processes.
- No synaptic vesicles, no PSDs, and few or no microtubules.
- Endfeet on blood vessels: processes flatten into sheets that cover almost the entire vascular surface. This is a strong identification cue.

**Key distinction from neurons:**
The usual confusion is between fine astrocytic processes and thin dendrites or axons. The discriminating cues:

| Feature | Astrocyte process | Neuronal process |
|---------|------------------|------------------|
| Glycogen granules | Present | Absent |
| Synaptic participation | No vesicles, no PSD | Vesicles (axon) or PSD (dendrite) |
| Microtubules | Absent or very rare | Usually present |
| Shape | Irregular, sheet-like, fills gaps | Cylindrical, continuous trajectory |
| Cytoplasm appearance | Pale, "watery," few organelles | Denser, with visible organelles |
| GFAP filaments | Sometimes visible as fine bundles (more in fibrous astrocytes) | Absent; neurons have neurofilaments instead, mostly in axons |

---

## Oligodendrocytes

### EM identification cues

Oligodendrocytes make and maintain CNS myelin. They are the easiest glia to identify, because of their dark nucleus and their link to myelinated axons.

**Soma features:**
- Nucleus: small, round, very electron-dense (heterochromatic). Usually the darkest nucleus in the field, clearly darker than neuronal or astrocytic nuclei. This is the most reliable single cue.
- Cytoplasm: dense, with abundant rough ER and ribosomes, a prominent Golgi apparatus and microtubules, which fits the protein synthesis myelin needs.
- Size: soma roughly 6–8 µm across.

**Process features:**
- Processes run from the soma to myelin sheaths. One oligodendrocyte can myelinate tens of axon segments.
- Cytoplasmic tongues: the innermost and outermost wraps of a sheath keep some cytoplasm. The oligodendrocyte process joins the sheath at the outer tongue; the inner tongue lies against the axon.
- Paranodal loops: at each end of a sheath, next to the node of Ranvier, the wraps end in cytoplasm-filled loops that form junctions with the axon membrane.

**Key distinction from neurons:**
Oligodendrocyte somata are rarely mistaken for neurons because the nucleus is so dark. The hard case is the oligodendrocyte precursor cell (OPC), which has a paler nucleus and can resemble a small neuron or an astrocyte. OPCs also receive genuine synapses from axons (Bergles et al. 2000), so a PSD-like contact on a process does not by itself rule out an OPC.

---

## Microglia

### EM identification cues

Microglia are the resident immune cells of the CNS. Of the three glial types they are the least numerous and the most variable in shape.

**Soma features:**
- Nucleus: elongated, bean- or kidney-shaped (indented), with clumps of heterochromatin. The irregular shape is a useful cue.
- Cytoplasm: dense, with prominent lysosomes and lipid inclusions from phagocytosis. Darker than astrocyte cytoplasm.
- Size: soma roughly 5–7 µm across, the smallest of the glial somata.

**Process features:**
- Thin, branching processes that survey the surrounding tissue, often with an angular, "spiky" branching pattern.
- Lysosomes and phagocytic inclusions in the processes as well as the soma.
- Processes make brief contacts with synapses (Wake et al. 2009; Tremblay et al. 2010), but they do not wrap synapses in stable sheets as astrocytes do, and they do not make myelin.
- Processes sometimes engulf synaptic elements or debris, which shows as partly internalized profiles.

**Key distinction from neurons and other glia:**
The bean-shaped nucleus and lysosome-rich cytoplasm are the main cues. Activated microglia (after injury or in disease) have swollen somata and retracted processes. That makes them easier to spot but easier to confuse with macrophages or other immune cells.

---

## Decision protocol: glial classification in practice

### Step 1: Is this a neuronal process or a glial process?

This is the question you will ask most often.

**Quick tests:**
1. Does the process contain a synaptic vesicle cluster? → **Neuronal** (high confidence). A PSD on the process → neuronal (high confidence), unless it could be an OPC, which receives synapses too.
2. Does it contain clustered glycogen granules? → **Astrocyte** (high confidence)
3. Is it continuous with a myelin sheath? → **Oligodendrocyte** (high confidence). A process that merely *touches* a sheath could be anything.
4. Does it contain microtubules? → Leans neuronal, not conclusive (oligodendrocytes have them too)
5. Is the cytoplasm pale, "watery" and organelle-poor? → Leans astrocyte

If none of these settles it, go to Step 2.

### Step 2: Follow the process to its soma

If you can trace the process back to a soma, nuclear morphology is the most reliable discriminator:

| Nucleus | Identity |
|---------|----------|
| Large, pale, round, prominent nucleolus | **Neuron** |
| Pale, irregular contour, dispersed chromatin | **Astrocyte** |
| Small, very dark, round | **Oligodendrocyte** |
| Bean-shaped, heterochromatin clumps | **Microglia** |

### Step 3: Use neighborhood context

If you cannot trace to a soma and local cues are inconclusive:

- Is the process adjacent to a blood vessel, forming a flat contact? → **Astrocyte end-foot**
- Is the process continuous with a myelin sheath? → **Oligodendrocyte**
- Is the process surrounded by synapses it appears to be wrapping? → **Astrocyte perisynaptic process**
- Does the process contain phagocytic inclusions? → **Microglia**

### Step 4: Assign confidence and escalate if needed

If the evidence is still ambiguous, label the process `uncertain-glia` or `uncertain-neuron/glia` (or your project's equivalent) and flag it for a second review. A forced call on thin evidence produces errors that are harder to find later.

---

## Worked example: astrocyte vs thin dendrite

This is a constructed case, not a specific process from a public dataset.

**Scenario:** a thin process (about 150 nm) runs between two synaptic boutons. Its only visible contents are two small dense granules (about 25 nm). It takes part in no synapse (no vesicles, no PSD). Its cytoplasm is paler than the neuronal processes around it.

**Analysis:**
1. No synaptic participation → not clearly neuronal, but absence at one location is weak evidence
2. Two small dense granules, the size of glycogen → suggests astrocyte
3. Pale cytoplasm with no microtubules → fits astrocyte, though a 150 nm axon can show few microtubules in one section
4. Lies between synaptic boutons → fits a perisynaptic astrocyte process
5. Followed five sections in each direction, it spreads into thin sheets rather than staying a cylinder → astrocyte shape

**Classification:** perisynaptic astrocyte process. Confidence: **high**, because glycogen, texture, sheet shape and position agree. Two granules is a small sample, though. If further sections showed a vesicle cluster or a continuous tube, reopen the call.

---

## Worked example: oligodendrocyte precursor cell (OPC) vs small neuron

This is also a constructed case.

**Scenario:** a small cell body (about 7 µm) with a moderately dark nucleus and several thin processes reaching into the neuropil. The nucleus is darker than nearby neuronal nuclei but lighter than a classic oligodendrocyte. The cytoplasm contains some RER.

**Analysis:**
1. Nucleus is intermediate: darker than an astrocyte's, lighter than a mature oligodendrocyte's
2. Small cell body with several processes (fits either a small neuron or an OPC)
3. No output synapses (no vesicle clusters) on the processes. OPCs *receive* synapses, so an input synapse would not have ruled them out, but an output would
4. No connection to a myelin sheath
5. RER present (found in neurons and in the oligodendrocyte lineage)
6. No glycogen granules (argues against astrocyte)

**Classification:** oligodendrocyte precursor cell (OPC, also called NG2 cell). Confidence: **medium**. Reasoning: intermediate nuclear darkness, small soma, no output synapses and no myelin link. OPCs are hard to call in EM without molecular markers. Following the processes further for an axon or an AIS would settle the neuron alternative.

---

## Impact on connectomics analysis

### Quantifying glia-neuron boundary errors

Glia-neuron merges are a recognized class of merge error in cortical reconstructions. We have not found a published estimate of their share of all merges in a public dataset, so this page does not quote one. Whatever their frequency, they do outsized damage:

1. The merge adds false "branches" to the neuron that are really astrocytic processes, distorting its morphology
2. Synapses near the merge boundary can be assigned to the wrong cell
3. If the glial process reaches a blood vessel, the neuron appears to contact the vessel, which is biologically false

### Put glia-neuron boundaries in the proofreading queue

Many proofreading campaigns look only at neurons. Glia-neuron boundaries belong in the high-priority QC queue, especially:
- Large segments with unusual morphology that suggests a neuron-glia merge
- Neurons near blood vessels, where astrocyte endfeet are easy to merge in
- Regions where the segmentation model is known to be weak at glial boundaries

---

## Common misconceptions

| Misconception | Reality | How to verify |
|---|---|---|
| "Glia are just background" | Glia-neuron boundary errors directly corrupt the neuronal connectome | Quantify false connections attributed to glia-neuron merges |
| "A small, dark nucleus is a small neuron" | Oligodendrocyte nuclei are usually the darkest in the field; neuronal nuclei are pale | Compare with known cell types; check for myelin association |
| "All thin processes are axons" | Many thin processes in neuropil are astrocytic | Check for glycogen, synaptic role and cytoplasm appearance |
| "A PSD proves the process is neuronal" | OPCs receive synapses from axons (Bergles et al. 2000) | Check nuclear darkness and whether the cell has any output synapses |
| "OPCs are easy to identify" | OPCs have intermediate features and are hard even for experts | Flag uncertain cases rather than forcing a classification |

---

## References

- Bergles DE, Roberts JDB, Somogyi P, Jahr CE (2000) "Glutamatergic synapses on oligodendrocyte precursor cells in the hippocampus." *Nature* 405:187-191. [10.1038/35012083](https://doi.org/10.1038/35012083)
- Bushong EA et al. (2002) "Protoplasmic astrocytes in CA1 stratum radiatum occupy separate anatomical domains." *Journal of Neuroscience* 22(1):183-192.
- Hildebrand C et al. (1993) "Myelinated nerve fibres in the CNS." *Progress in Neurobiology* 40(3):319-384.
- Kettenmann H, Ransom BR (2013) *Neuroglia*. 3rd ed. Oxford University Press. A comprehensive glia textbook.
- Nishiyama A et al. (2009) "Polydendrocytes (NG2 cells): multifunctional cells with lineage plasticity." *Nature Reviews Neuroscience* 10(1):9-22.
- Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System*. 3rd ed. Oxford University Press.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384(6696):eadk4858.
- Tremblay MÈ, Lowery RL, Majewska AK (2010) "Microglial interactions with synapses are modulated by visual experience." *PLoS Biology* 8(11):e1000527. [10.1371/journal.pbio.1000527](https://doi.org/10.1371/journal.pbio.1000527)
- Turner NL et al. (2022) "Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity." *Cell* 185(6):1082-1100.
- Wake H, Moorhouse AJ, Jinno S, Kohsaka S, Nabekura J (2009) "Resting microglia directly monitor the functional state of synapses in vivo and determine the fate of ischemic terminals." *Journal of Neuroscience* 29(13):3974-3980. [10.1523/JNEUROSCI.4363-08.2009](https://doi.org/10.1523/JNEUROSCI.4363-08.2009)
