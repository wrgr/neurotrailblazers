---
layout: page
title: "Axon-Dendrite Classification"
permalink: /content-library/cell-types/axon-dendrite-classification/
image: /assets/images/content-library/cell-types/axon-dendrite-classification.svg
image_alt: "Stylized vector art: three cell silhouettes: branched, star-form, and amoeboid."
description: "A four-pass procedure for telling axons from dendrites in EM (morphology, organelles, synaptic role, continuity), with a cue-reliability table, confidence tiers and a worked example."
topics:
  - axon
  - dendrite
  - classification
  - proofreading
  - morphology
primary_units:
  - "06"
difficulty: "Intermediate"
tags:
  - cell-types:axon-dendrite-distinction
  - cell-types:morphological-classification
  - imaging:electron-microscopy
  - proofreading:process-classification
  - neuroanatomy:ultrastructure
micro_lesson_id: ml-cell-axon-dendrite
combines_with:
  - neuron-type-identification
  - glia-recognition
  - em-principles
content_type: core
---

## Overview

Calling a dendrite an axon, or the reverse, is one of the most damaging annotation errors in connectomics. It does not add noise to the directed graph. It adds an edge pointing the wrong way. Cell-type identification, input/output analysis and motif counts all inherit the error. This page sets out a multi-cue procedure for telling axons from dendrites in EM. New annotators can learn from it, and experienced teams can use it to calibrate against each other. It is the reference companion to [Unit 06]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}), which has the full cue tables and the exceptions.

---

## Instructor script: the classification challenge

### Why textbook contrasts fail in real EM

In textbook diagrams, axons are thin and smooth and dendrites are thick and spiny. In real EM data the two overlap:

- **Thin distal dendrites** can be a few hundred nanometers across, the same range as unmyelinated axons (80–300 nm in cortical neuropil; Unit 06 §1).
- **En passant boutons** (axonal swellings with vesicles) can look like spine heads in a single section.
- **Truncated processes** at the volume edge lack the context you need for a confident call.
- **Glial processes** can be mistaken for either (see [Glia recognition]({{ '/content-library/cell-types/glia-recognition/' | relative_url }})).
- **Developing tissue** has weaker morphological signatures.

The working rule: **no single cue is reliable alone. A confident call needs agreement from independent kinds of evidence.**

---

{% include figure.html
   src="/assets/images/content-library/em/neuropil-raw-vs-subcompartments.jpg"
   alt="Human cortical neuropil at 8 nm per pixel shown twice: raw grayscale on the left, and on the right the same field colored by H01's subcompartment model into axon, dendrite and astrocyte."
   caption="Work the protocol on this before reading the answer. Left is raw human cortex. Right is the same pixels colored by H01&#39;s own six-class subcompartment model; three of its classes occur in this field. The large green profile is a dendrite: note the mitochondrion and the caliber, roughly 2&ndash;3 &micro;m across. Blue profiles are axons, most far smaller. Orange is astrocyte, threading between everything. The four myelinated axons are left uncolored because the overlay does not draw the model&#39;s myelin classes. The labels are a model&#39;s output, not proofread ground truth. The point of the exercise is how many blue and green profiles are hard to separate by eye at this scale."
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024). Rendered by <code>scripts/render_em_figures.py</code>." %}

## The four-pass classification protocol

### Pass 1: Morphology

Evaluate the process shape and branching pattern:

| Feature | Axon-like | Dendrite-like |
|---------|-----------|---------------|
| **Caliber** | Thin: 80–300 nm typical for unmyelinated axons in cortical neuropil | Shafts 0.5–3 µm, thickest near the soma |
| **Branching** | Collaterals often leave near-perpendicular, with little caliber change at the branch | Daughter branches are thinner than the parent |
| **Spines** | Absent (except rare axonal filopodia) | Present on most excitatory dendrites |
| **Surface** | Beaded: thin segments between vesicle-filled boutons | Spines on spiny cells; varicosities without vesicle clusters |
| **Tapering** | Minimal (caliber roughly constant between boutons) | Steady taper with distance from the soma |

Ranges follow Unit 06 §1. **Caveat:** most inhibitory neuron dendrites are smooth (aspiny), so the absence of spines does not mean "axon".

### Pass 2: Organelles

Evaluate the intracellular contents:

| Feature | Axon-like | Dendrite-like |
|---------|-----------|---------------|
| **Synaptic vesicles** | Clusters of ~40 nm clear vesicles at boutons, against the membrane | Absent (except at dendritic release sites, rare in cortex) |
| **Microtubules** | Uniformly plus-end-out (Baas et al. 1988); regularly spaced; fasciculated in the AIS | Mixed polarity in proximal dendrites; denser, less regular arrays |
| **Ribosomes/RER** | Effectively absent beyond the axon initial segment | Polyribosomes in shafts and at spine bases; RER near the soma |
| **Neurofilaments** | Abundant, especially in myelinated axons | Sparse |
| **Mitochondria** | Short; found in some boutons, missing from many | Often long and tubular in the shaft |
| **Smooth ER** | Thin tubules along the axon | Network; forms the spine apparatus in a minority of spines |
| **Dense-core vesicles** | Present in some axon types (roughly 80–120 nm) | Occasional, in transit |

Microtubule polarity cannot be read from a standard EM image; what you can see is the spacing and arrangement. **Key cue:** a cluster of clear vesicles against a membrane is the strongest single sign of an axon. At that point, the process is a presynaptic terminal.

### Pass 3: Synaptic role

Evaluate how the process participates in synapses:

| Role | Axon | Dendrite |
|------|------|----------|
| **Presynaptic** | Yes: forms output synapses | Rare in cortex (dendro-dendritic synapses are common in olfactory bulb and thalamus) |
| **Postsynaptic** | Rare (chandelier-cell synapses onto the AIS) | Yes: receives input synapses |
| **Spine-bearing** | No | Yes, on spiny (mostly excitatory) neurons |

**Decision rule:** a process that is consistently presynaptic (vesicles on its side, PSD on the partner's side) is an axon. One that is consistently postsynaptic is a dendrite. If it plays both roles at different places, suspect a merge error joining an axon to a dendrite, and check the tissue type against the exceptions in Unit 06 §2.

### Pass 4: Continuity

Check the call by following the process through more sections:

- **Trace toward the soma.** Does the process reach a cell body, and how? A neuron usually has one axon, starting at the axon hillock or from a proximal dendrite. Its AIS has a dense membrane undercoating and fasciculated microtubules. Dendrites leave the soma as several broad, tapering trunks.
- **Check consistency.** Does the call hold along the process? An abrupt switch from axon-like to dendrite-like features suggests a merge error.
- **Look at the arbor.** Dendritic trees often have a recognizable layout (apical, basal, stellate); axonal arbors are longer and wider-ranging.

---

## Edge cases and how to handle them

### Thin, aspiny dendrites of inhibitory neurons

**Problem:** the dendrites of many inhibitory interneurons (parvalbumin-positive basket cells, for example) are smooth, thin and long. All three features overlap with axons.

**Solution:** look for (a) a postsynaptic role, since these dendrites receive synapses directly on the shaft; (b) ribosomes or RER, which axons lack; (c) the microtubule arrangement, if the cross-section is clean; (d) the soma, if you can reach it.

### En passant boutons vs spines

**Problem:** an en passant bouton (a vesicle-filled swelling along an axon) can look like a spine head in a single section.

**Solution:** (a) Check for vesicles: boutons have vesicle clusters, spine heads usually do not. (b) Check the PSD: at a bouton it is on the *partner's* membrane; in a spine it is on the *spine head's* own membrane. (c) Follow it through z: a bouton continues into axon on both sides, while a spine joins a larger dendrite through a narrow neck.

### Truncated processes at the volume edge

**Problem:** the process leaves the imaged volume. You see a few micrometers, not enough to reach a soma or see the branching.

**Solution:** use the local cues (organelles, vesicles, synaptic role) and assign a confidence tier. If the evidence is thin, record "uncertain". Do not force a call: an honest "uncertain" costs a review; a wrong label corrupts every edge on the process.

### Myelinated processes

**Problem:** the sheath hides the cytoplasm, so organelle cues are hard to see.

**Solution:** myelin is itself a strong axon cue; Unit 06 treats myelinated dendrites as absent in the tissue it covers. Call the segment "myelinated axon" with high confidence. At nodes of Ranvier the cytoplasm is exposed and you can confirm with organelles.

---

## Worked example: a smooth 300 nm process with one input synapse

This is a constructed case, not a specific process from a public dataset.

**Scenario:** cortical neuropil, sections about 40 nm thick. A process about 300 nm across runs roughly 2 µm (about 50 sections). It contains a few microtubules, no vesicle clusters and no spines. It receives one synapse (PSD on its side) and makes no output synapses in view.

**Pass 1 (Morphology):** 300 nm sits at the top of the unmyelinated-axon range and at the bottom of the dendrite range. No spines, smooth surface. Verdict: inconclusive.

**Pass 2 (Organelles):** three to five microtubules, one small mitochondrion, no vesicles, no ribosomes visible. The missing ribosomes tempt you toward axon, but at 300 nm a polyribosome can easily miss every section you looked at. Absence is weak evidence. Verdict: inconclusive.

**Pass 3 (Synaptic role):** one synapse, with this process postsynaptic. Verdict: lean dendrite. Axons rarely receive synapses; the main cortical exception is the chandelier-cell input to the AIS. Nothing here looks like an AIS: no membrane undercoating, no fasciculated microtubules.

**Pass 4 (Continuity):** follow it about 1 µm further toward what looks like the proximal end. It widens to about 350 nm, a polyribosome cluster appears near a branch point, and two more synapses land on the shaft.

**Final call:** dendrite, probably of an inhibitory interneuron given the smooth shaft. Confidence: **medium**. Two cue families agree (synaptic role: three input synapses; organelles: one ribosome cluster), but the organelle evidence rests on a single cluster and the tracing is short. What would change the call: vesicle clusters or an output synapse further along, which would point to a merge rather than to an axon.

---

## Inter-annotator calibration protocol

To maintain consistent classification across a team:

1. **Weekly calibration sessions.** Review 10–20 ambiguous cases as a group, compare the cues each person used, and agree on a call.
2. **Shared edge-case library.** Keep the hard examples, with the agreed call and the reasoning.
3. **Confusion-matrix tracking.** Test annotators against an adjudicated truth set now and then, and track axon/dendrite accuracy per person and per confidence tier.
4. **An agreed evidence threshold.** Write down the minimum evidence for a committed call, for example "two independent cue families must agree".

---

## Organelles and synaptic role carry the call; caliber does not

The protocol above lists cues but does not say which ones fail, and that is
what you need to know when working under uncertainty. Roughly, in decreasing
order of reliability:

| Cue | Reliability | Fails when |
|---|---|---|
| **Polyribosomes / rough ER present** | Very high for dendrite. Axons lack them | The section misses them; a thin dendrite may show none in any single plane |
| **Vesicle-filled varicosity with an active zone** | Very high for axon | The bouton is out of plane; a dendrite receiving many inputs can look busy at low magnification |
| **Postsynaptic densities on the process itself** | High for dendrite | Chandelier cells synapse onto the AIS, so an AIS carries PSDs too |
| **Myelination** | Very high for axon | Only a minority of axons are myelinated, so absence proves nothing |
| **Microtubule arrangement** | Moderate | Both compartments contain microtubules; the difference is spacing and fasciculation, which needs a clean cross-section |
| **Spines** | High for dendrite | Aspiny and sparsely spiny dendrites are common, including those of most inhibitory neurons |
| **Taper at a branch point** | Moderate to high for dendrite, when a branch is in view | Needs the branch in the volume; daughters thinner than the parent point to dendrite (Unit 06 §1) |
| **Caliber** | **Low on its own** | Thin dendrites and thick axons both exist. Unit 06 §1 gives 80–300 nm for unmyelinated axons and 50–200 nm for spine necks: overlapping ranges |
| **Branching angle** | Low | Suggestive at best, and strongly affected by section angle |

**The rule the units enforce: two independent cue families before a confident
call.** Independence is what matters. Caliber and branching angle are both
geometric and both fail on a tangential cut, so they count as one family.
Organelle content and synaptic role do not depend on geometry, which is why
they carry the call.

### Attaching a confidence tier

Use the three tiers Unit 06 uses, so a call travels with its evidence:

- **High:** two independent cue families agree, both clearly visible. Record
  the call and the cues you used.
- **Medium:** one strong cue, or two weak ones that agree. Record the call *and*
  what would change your mind.
- **Uncertain:** the cues conflict, or the section shows nothing decisive.
  Record "uncertain". This is a real answer. In a dataset where nobody ever
  writes it, people are guessing.

(These tiers are about how sure you are of a label. The site's Bin A/B/C scheme
is different: it sorts *claims* by the kind of evidence they need.)

A tier is only useful if it predicts accuracy. Unit 06's rubric asks that
high-confidence calls be right at least 90% of the time while a non-trivial
share stay uncertain. If your high-tier accuracy matches your overall accuracy,
the tiers carry no information.

### Species and tissue caveats

Everything above is calibrated on mammalian cortical neuropil. It does not
transfer unchanged:

- In *Drosophila* there is no myelin, most neurons are unipolar, and one
  neurite can carry both inputs and outputs along its length. The
  axon/dendrite split is often the wrong frame.
- In *C. elegans*, processes are thin enough that organelle cues are often
  missing from any given section.
- In human surgical tissue such as H01, fixation quality can vary across the
  sample. Poorer fixation weakens membrane contrast, which the automated
  segmentation depends on.

Before applying this protocol to a new dataset, classify twenty processes you
can verify and check that the cues behave as described. If they do not, it is
the protocol that needs adjusting, not the tissue.

---

## Common misconceptions

| Misconception | Reality | How to verify |
|---|---|---|
| "Thin process = axon" | Thin aspiny dendrites are common in inhibitory neurons | Check synaptic role and ribosomes |
| "No spines = axon" | Roughly a fifth of cortical neurons are inhibitory, and most of them have smooth dendrites (see [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }})) | Trace to soma; check cell type |
| "Vesicles = always axon terminal" | Dense-core vesicles can be in transit through dendrites; some dendrites release transmitter | Look for clustered clear vesicles at a membrane apposition |
| "No ribosomes = axon" | A thin dendrite can show no polyribosome in any single section | Treat absence as evidence only when the feature would have been visible |
| "One synapse proves the classification" | A single synapse can be misdetected or ambiguous | Require multiple synapses or corroborating organelle evidence |

---

## References

- Baas PW, Deitch JS, Black MM, Banker GA (1988) "Polarity orientation of microtubules in hippocampal neurons: uniformity in the axon and nonuniformity in the dendrite." *PNAS* 85(21):8335-8339.
- Harris KM, Weinberg RJ (2012) "Ultrastructure of synapses in the mammalian brain." *Cold Spring Harbor Perspectives in Biology* 4(5):a005587.
- Kasthuri N et al. (2015) "Saturated reconstruction of a volume of neocortex." *Cell* 162(3):648-661.
- Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System*. 3rd ed. Oxford University Press.
- Schneider-Mizell CM et al. (2016) "Quantitative neuroanatomy for connectomics in *Drosophila*." *eLife* 5:e12059.
