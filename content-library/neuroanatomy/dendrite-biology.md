---
layout: page
title: "Dendrite Biology and Ultrastructure"
permalink: /content-library/neuroanatomy/dendrite-biology/
image: /assets/images/content-library/neuroanatomy/dendrite-biology.svg
image_alt: "Stylized vector art: organelle profiles inside a curved membrane section."
description: >
  Instructor reference on dendritic structure and ultrastructure as
  observed in electron microscopy, covering proximal-to-distal morphology gradients,
  dendritic spine classification, postsynaptic density, microtubule organization,
  local protein synthesis, and practical identification strategies for annotators.
topics:
  - dendrites
  - dendritic spines
  - thin spines
  - mushroom spines
  - stubby spines
  - spine apparatus
  - postsynaptic density
  - microtubule polarity
  - local translation
  - dendritic mitochondria
  - smooth endoplasmic reticulum
primary_units:
  - "05"
  - "06"
difficulty: intermediate
tags:
  - neuroanatomy:dendrite
  - neuroanatomy:spine
  - neuroanatomy:postsynaptic-density
  - neuroanatomy:cytoskeleton
  - connectomics:synapse
  - imaging:electron-microscopy
  - methodology:identification
  - cell-types:pyramidal-neuron
micro_lesson_id: ml-neuro-dendrite
combines_with:
  - soma-ultrastructure
  - synapse-classification
  - organelle-cues
use_layout_hero: false
content_type: core
---

# Dendrite Biology and Ultrastructure

## Introduction

Dendrites are where most of a neuron's synaptic input arrives. They leave the soma as tapering, branching processes that together form the dendritic arbor. In electron microscopy they carry a set of ultrastructural features that separate them from axons and glia. This entry covers dendritic morphology, spine classification, and the organelle cues annotators use to call a profile a dendrite. It does not cover dendritic physiology beyond what helps with identification.

---

## 1. Overview of Dendritic Function

Dendrites receive synaptic input from presynaptic terminals, integrate excitatory and inhibitory signals through passive cable properties and active conductances, and transmit the resulting electrical signals toward the soma. Unlike axons, dendrites:

- **Taper distally**: Their caliber decreases progressively from the soma toward distal tips.
- **Branch extensively**: The basal arbor of a single pyramidal neuron can have dozens of branch points.
- **Contain visible ribosomes**: Dendrites carry out local protein synthesis, and polyribosomes are easy to find in them in EM. Mature axons also translate some mRNAs (Shigeoka et al., 2016), but at levels low enough that ribosomes are rarely seen in axons in conventional EM.
- **Have mixed microtubule polarity**: Both plus-end-out and minus-end-out microtubules coexist (Baas et al., 1988), unlike the uniform plus-end-out polarity of axonal microtubules.

---

{% include figure.html
   src="/assets/images/content-library/em/dendrite-and-organelles.jpg"
   alt="A dendritic profile in human cortex at 4 nm per pixel showing a dark mitochondrion within pale cytoplasm, with a myelinated axon above it and smaller neighboring profiles around it."
   caption="A dendritic profile at full resolution, identified as dendrite by the dataset&#39;s subcompartment model. The dark body with internal membranes, about half a micrometer across, is a mitochondrion cut in cross-section. One section cannot show how long or branched it is; that takes serial sections. The myelinated axon at the top is a useful contrast."
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024). Rendered by <code>scripts/render_em_figures.py</code>." %}

## 2. Proximal vs. Distal Morphology

A dendrite looks different near the soma than at its tips.

### Proximal Dendrites (within ~50 micrometers of the soma)

- **Caliber**: Several micrometers at the origin; the apical trunk of a large pyramidal neuron is the thickest dendrite you will meet, and basal dendrites start thinner.
- **Organelle content**: Rich in rough ER (continuous with somatic Nissl substance), abundant mitochondria and dense microtubule arrays. Some dendrites, especially apical trunks, also carry Golgi outposts.
- **Ribosomes**: Polyribosomes are plentiful both on ER membranes and free in the cytoplasm.
- **EM appearance**: The cytoplasm appears relatively dark and granular due to the density of ribosomes and organelles. Microtubules run longitudinally in loose parallel bundles.

### Distal Dendrites (terminal branches)

- **Caliber**: Often less than 1 micrometer, sometimes as thin as 0.3 micrometers.
- **Organelle content**: Rough ER is reduced to scattered polyribosomes. Smooth ER tubules persist. Mitochondria are present but fewer and smaller.
- **Spines**: Dendritic spines are most abundant on mid-to-distal dendrite segments of spiny neurons (pyramidal cells, medium spiny neurons).
- **EM appearance**: The cytoplasm is lighter, with fewer ribosomes. Microtubules are still present but in smaller numbers. The process may be difficult to distinguish from thin axons without careful examination of organelle content.

### The Organelle Gradient

Organelle density falls from proximal to distal, and annotators use that gradient. If a process you are tracing away from a soma gradually loses rough ER, becomes thinner and develops spines, you are following a dendrite.

---

## 3. Dendritic Spines in Detail

Dendritic spines are small protrusions from the dendritic shaft that carry the postsynaptic side of most excitatory synapses in the mammalian forebrain. Missing a spine, or attaching it to the wrong dendrite, removes or misassigns a synapse, so spines are a large share of proofreading work.

The named classes below come from Peters and Kaiserman-Abramof (1970), made quantitative by Harris et al. (1992), who separated mushroom from thin spines by a head diameter of about 0.6 micrometers. Treat the classes as landmarks on a continuum. In serial-section reconstructions of 144 spines on layer 2/3 pyramidal cells of mouse visual cortex, every measured parameter varied continuously, with no clearly separable spine types (Arellano et al., 2007). Useful ranges from that study: spine head volume 0.01-0.30 cubic micrometers (75% below 0.1), neck diameter 0.09-0.51 micrometers (mean 0.2), neck length 0.1-2.2 micrometers.

### 3.1 Thin Spines

- **Morphology**: Long, narrow neck topped by a small head, with head diameter below about 0.6 micrometers.
- **Head volume**: Small, mostly below 0.1 cubic micrometers.
- **Frequency**: Usually the most common spine type in adult cortex and hippocampus; the exact share depends on region and on the classification criteria. In rat CA1, thin-spine density increases about four-fold between postnatal day 15 and adulthood (Harris et al., 1992).
- **Functional significance**: Often called "learning spines" because they are thought to be dynamic structures that can enlarge (becoming mushroom spines) during synaptic potentiation or retract during depression.
- **EM identification**: Look for a narrow stalk connecting to the dendrite shaft, with a small terminal swelling containing a PSD.

### 3.2 Mushroom Spines

- **Morphology**: Short, wide neck supporting a large, bulbous head.
- **Head size**: Head diameter above about 0.6 micrometers (Harris et al., 1992), which corresponds to a head volume of roughly 0.1 cubic micrometers or more.
- **Frequency**: A minority of spines; the share depends on region, age and where the classifier draws the line. In rat CA1, mushroom spines with perforated PSDs and spine apparatuses increased about four-fold in density between postnatal day 15 and adulthood (Harris et al., 1992).
- **Functional significance**: Called "memory spines" because they are stable over time and associated with strong, potentiated synapses. The large head accommodates a larger PSD with more AMPA receptors.
- **EM identification**: The large head is conspicuous and often contains a spine apparatus. The PSD is prominent and easy to identify.

### 3.3 Stubby Spines

- **Morphology**: No clear neck; the head appears to sit directly on the dendritic shaft.
- **Head volume**: Variable, typically intermediate.
- **Frequency**: More common in developing tissue. In rat CA1, stubby spine density fell by more than half between postnatal day 15 and adulthood (Harris et al., 1992).
- **Functional significance**: May represent a transitional form. In a single section, a thin or mushroom spine whose neck runs out of the plane can look stubby, which is why Harris et al. (1992) classified spines through serial sections.
- **EM identification**: A PSD-bearing protrusion with little or no constriction at its base.

### 3.4 Branched and Complex Spines

- **Morphology**: A single spine stalk branches to produce two or more heads, each potentially bearing its own synapse.
- **Frequency**: Uncommon. In rat CA1 their density increased about four-fold between postnatal day 15 and adulthood (Harris et al., 1992).
- **Significance**: Each head can receive its own presynaptic partner, so one branched spine can mean two synapses in the connectome. Check each head separately.

### 3.5 The Spine Apparatus

The spine apparatus is a smooth ER derivative found within the necks and heads of a subset of dendritic spines, particularly mushroom spines. In EM:

- **Appearance**: Stacked, flattened cisternae of smooth membrane separated by electron-dense plates (containing the protein synaptopodin).
- **Size**: A small stack of cisternae, usually only a few, often lying in the neck or at the base of the head.
- **Function**: Proposed as a local calcium store and implicated in synaptic plasticity. Mice lacking synaptopodin have no spine apparatuses and show reduced long-term potentiation in CA1 (Deller et al., 2003).
- **Not all spines have one**: Spine apparatuses occur in a subset of spines, predominantly large mushroom spines. In adult rat CA1, more than 80% of large mushroom spines had a spine apparatus, while fewer than half of small spines contained any smooth ER (Spacek & Harris, 1997).

---

## 4. The Postsynaptic Density (PSD)

The PSD is the defining ultrastructural feature of excitatory postsynaptic sites. In EM it appears as an electron-dense band on the cytoplasmic face of the postsynaptic membrane.

- **Dimensions**: On layer 2/3 pyramidal cell spines in mouse visual cortex, PSD areas on spines ranged from 0.01 to 0.33 square micrometers, mean 0.08 (Arellano et al., 2007). For a round PSD that is about 110-650 nm across. At Type I (asymmetric) synapses the PSD is a few tens of nanometers thick.
- **Composition**: A dense meshwork of scaffolding proteins (PSD-95, Homer, Shank) that anchor glutamate receptors (AMPA and NMDA subtypes), adhesion molecules, and signaling enzymes.
- **PSD size correlates with synapse strength**: Larger PSDs contain more AMPA receptors and correlate with larger spine heads and higher synaptic efficacy (Harris & Weinberg, 2012).
- **EM appearance**: A dark band closely apposed to the postsynaptic membrane, usually thicker than any corresponding presynaptic density. In en face reconstructions from serial sections, the PSD appears as a disc or irregular patch.

---

## 5. Microtubule Organization in Dendrites

Microtubules in dendrites have a characteristic mixed polarity arrangement (Baas et al., 1988):

- **Plus-end-out microtubules**: Similar to axonal microtubules, oriented with growing ends pointing distally.
- **Minus-end-out microtubules**: Unique to dendrites in vertebrate neurons, oriented with growing ends pointing toward the soma.
- **Proportion**: In cultured rat hippocampal neurons, microtubules in the dendrite mid-region (about 75 micrometers from the soma) were split roughly equally between the two orientations, while within 15 micrometers of the growing tip they were uniformly plus-end-out, as in axons (Baas et al., 1988).
- **Functional significance**: Minus-end-out microtubules let dynein, a minus-end-directed motor, carry cargo away from the soma into dendrites. This is one proposed basis for sorting cargo between dendrites and axons.
- **Contrast with axons**: Vertebrate axons have uniformly plus-end-out microtubules. This polarity difference is one of the fundamental molecular distinctions between the two compartment types.

In EM, microtubules appear as hollow cylinders approximately 25 nm in outer diameter. They are visible in longitudinal section as parallel lines and in cross-section as small circles. Annotators cannot determine polarity from standard EM images, but the distinction is important for understanding why dendrites and axons have different organelle distributions.

---

## 6. Ribosomes in Dendrites: Local Protein Synthesis

Steward and Levy (1982) found that polyribosomes in dentate granule cell dendrites sit preferentially under the base of spines: 71% were under membrane mounds that were probably spine bases and about 10% under identified spine necks. That result was an early piece of evidence for synapse-specific local translation.

- **Polyribosome clusters**: Small groups of ribosomes arranged in rosettes or spirals, often at the base of dendritic spines and within the dendritic shaft.
- **mRNA localization**: Specific mRNAs (CaMKII-alpha, Arc/Arg3.1, MAP2) are transported into dendrites and translated locally in response to synaptic activity.
- **Functional significance**: Local translation allows individual synapses to modify their protein composition independently, supporting synapse-specific plasticity.
- **EM identification**: Ribosomes appear as electron-dense particles approximately 20-25 nm in diameter. Polyribosomes are visible as clusters. Their presence in a process is strong evidence for dendritic (not axonal) identity.
- **Rough ER in dendrites**: In proximal dendrites, polyribosomes are often attached to ER membranes (rough ER). In distal dendrites, free polyribosomes predominate.

---

## 7. Mitochondria in Dendrites

Dendritic mitochondria have distinctive features compared to axonal mitochondria:

- **Size**: In cortical pyramidal neurons, dendritic mitochondria are typically long and tubular, often several micrometers, and can fill much of the shaft (Lewis et al., 2018).
- **Distribution**: Found throughout the dendritic shaft and at branch points, running parallel to the microtubules.
- **Cristae**: Well-developed lamellar cristae.
- **Contrast with axons**: In the same neurons, axonal mitochondria are uniformly short (Lewis et al., 2018).
- **Annotation cue**: A long mitochondrion followed across serial sections, alongside ribosomes, points to a dendrite. A single section shows only a cross-section, so length needs neighboring sections.

---

## 8. Smooth Endoplasmic Reticulum in Dendrites

The smooth ER forms a continuous tubular network extending throughout dendrites:

- **Dendritic shaft**: SER runs as a tubular network parallel to microtubules, sometimes forming a continuous lumen extending from the soma to distal tips.
- **Spine entry**: SER tubules enter dendritic spines, sometimes forming the spine apparatus (see Section 3.5).
- **Calcium signaling**: The SER serves as the primary intracellular calcium store. IP3 receptors and ryanodine receptors on the SER membrane mediate calcium release during synaptic signaling.
- **EM appearance**: Smooth-walled tubular profiles, 30-50 nm in diameter, without ribosomes on their surface. In cross-section they appear as small circular profiles.

---

## 9. Worked Example: Identifying a Spine Synapse

**Scenario**: In a cortical EM volume, you see a small protrusion extending from a larger process, with a darkened presynaptic terminal apposed to it.

Step-by-step identification:

1. **Identify the dendrite**: The larger parent process (approximately 1.5 micrometers diameter) contains microtubules, a few mitochondria, and scattered polyribosomes. This confirms it as a dendrite.
2. **Identify the spine**: A narrow neck (approximately 0.15 micrometers) extends from the dendrite shaft, widening into a small head (approximately 0.4 micrometers across).
3. **Find the PSD**: On the head of the spine, a thick electron-dense band (approximately 200 nm long, 40 nm thick) is visible on the cytoplasmic face of the membrane.
4. **Check the presynaptic side**: Apposed to the PSD, a terminal containing clustered round vesicles (approximately 40 nm diameter) is present. The presynaptic membrane shows active zone densification.
5. **Classify the synapse**: Thick PSD + round vesicles + wide cleft = asymmetric (Type I) excitatory synapse on a spine.
6. **Classify the spine**: A 0.4 micrometer head is below the 0.6 micrometer mushroom threshold, and the neck is clearly defined, so this is a thin spine by the Harris et al. (1992) criteria. Measure the head at its widest section across the series, not in whichever section you happen to be viewing.
7. **Check adjacent sections**: Verify the spine connection to the parent dendrite in 2-3 neighboring sections to confirm it is not an isolated profile.

---

## 10. Worked Example: Distinguishing a Thin Dendrite from an Axon

**Scenario**: You encounter a small-caliber process (approximately 0.5 micrometers) running through the neuropil. Is it a thin dendrite or an unmyelinated axon?

| Feature | Thin Dendrite | Unmyelinated Axon |
|---|---|---|
| Caliber | Gradually tapering, may vary | Roughly constant between varicosities (boutons) |
| Ribosomes | Scattered polyribosomes present | Rarely seen (axonal translation exists, at low levels) |
| Microtubule polarity | Mixed (cannot see directly in EM) | Uniform plus-end-out |
| Microtubule spacing | Loosely spaced, irregular | More regular spacing |
| Rough ER | May have sparse RER profiles | Absent |
| Smooth ER | Tubular SER network present | Single SER tubule or absent |
| Mitochondria | Often long and tubular across sections | Short, uniform in length |
| Spines | May bear spines (if spiny neuron) | Does not bear spines |
| Synaptic contacts | Mainly receives synapses (postsynaptic) | Mainly makes synapses (presynaptic) |

**Decision process**:

1. Look for ribosomes or rough ER. If present, the process is almost certainly a dendrite. This is the strongest single cue, but ribosomes are hard to resolve at 8 nm per pixel or coarser.
2. Look for spines or PSDs on the process. Postsynaptic specializations indicate a dendrite.
3. Check for vesicle clusters within the process. Synaptic vesicles indicate an axon terminal.
4. Examine caliber changes. Tapering suggests a dendrite.
5. Consider context. Trace the process toward a soma if possible.

---

## 11. Common Misconceptions

| Misconception | Reality |
|---|---|
| "All dendrites have spines." | Only certain neuron types are spiny (pyramidal cells, medium spiny neurons). Many interneuron subtypes have smooth (aspiny) dendrites that receive synapses directly on the shaft. |
| "Spine size is fixed." | Spines are highly dynamic structures that change size and shape over minutes to hours in response to activity. Long-term potentiation enlarges spines; depression shrinks them (Bourne & Harris, 2008). |
| "Thin spines are immature." | Thin spines are abundant in adult tissue; in rat CA1 their density rises about four-fold from postnatal day 15 to adulthood (Harris et al., 1992). They may be learning substrates rather than developmental precursors. |
| "Every spine fits one of the four named types." | The types are landmarks on a continuum. In a serial-section study of mouse visual cortex, spine shapes varied continuously with no clearly separable types (Arellano et al., 2007). Record the measurements, not only the label. |
| "Dendrites do not conduct action potentials." | Many dendrites support backpropagating action potentials and dendritic spikes (calcium or sodium), though these are not visible in EM. |
| "Ribosomes are always on rough ER." | Free polyribosomes (not attached to ER membranes) are abundant in dendrites and are the primary site of local dendritic translation. |
| "The PSD is a membrane structure." | The PSD is a cytoplasmic protein meshwork on the intracellular face of the postsynaptic membrane, not a membrane itself. |

---

## References

1. Harris KM, Jensen FE, Tsao B (1992) "Three-dimensional structure of dendritic spines and synapses in rat hippocampus (CA1) at postnatal day 15 and adult ages." *Journal of Neuroscience* 12:2685-2705.
2. Bourne JN, Harris KM (2008) "Balancing structure and function at hippocampal dendritic spines." *Annual Review of Neuroscience* 31:47-67.
3. Harris KM, Weinberg RJ (2012) "Ultrastructure of synapses in the mammalian brain." *Cold Spring Harbor Perspectives in Biology* 4:a005587.
4. Fiala JC, Harris KM (1999) "Dendrite structure." In: *Dendrites* (Stuart G, Spruston N, Hausser M, eds), pp 1-34. Oxford University Press.
5. Baas PW, Deitch JS, Black MM, Banker GA (1988) "Polarity orientation of microtubules in hippocampal neurons: uniformity in the axon and nonuniformity in the dendrite." *Proceedings of the National Academy of Sciences* 85:8335-8339.
6. Steward O, Levy WB (1982) "Preferential localization of polyribosomes under the base of dendritic spines in granule cells of the dentate gyrus." *Journal of Neuroscience* 2:284-291.
7. Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System*, 3rd edition. Oxford University Press.
8. Spacek J, Harris KM (1997) "Three-dimensional organization of smooth endoplasmic reticulum in hippocampal CA1 dendrites and dendritic spines of the immature and mature rat." *Journal of Neuroscience* 17:190-203.
9. Deller T, Korte M, Chabanis S, et al. (2003) "Synaptopodin-deficient mice lack a spine apparatus and show deficits in synaptic plasticity." *Proceedings of the National Academy of Sciences* 100:10494-10499.
10. Arellano JI, Benavides-Piccione R, DeFelipe J, Yuste R (2007) "Ultrastructure of dendritic spines: correlation between synaptic and spine morphologies." *Frontiers in Neuroscience* 1:131-143. doi:10.3389/neuro.01.1.1.010.2007
11. Shigeoka T, Jung H, Jung J, et al. (2016) "Dynamic axonal translation in developing and mature visual circuits." *Cell* 166:181-192. doi:10.1016/j.cell.2016.05.029
12. Lewis TL, Kwon SK, Lee A, Shaw R, Polleux F (2018) "MFF-dependent mitochondrial fission regulates presynaptic release and axon branching by limiting axonal mitochondria size." *Nature Communications* 9:5008. doi:10.1038/s41467-018-07416-2
13. Peters A, Kaiserman-Abramof IR (1970) "The small pyramidal neuron of the rat cerebral cortex. The perikaryon, dendrites and spines." *American Journal of Anatomy* 127:321-355. doi:10.1002/aja.1001270402

---

*This document is part of the NeuroTrailblazers Content Library. It is intended as an instructor reference and annotator training script. Last updated: 2026.*
