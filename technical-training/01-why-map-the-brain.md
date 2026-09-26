---
layout: page
title: "01 Why Map the Brain"
description: "What a synapse-resolution wiring diagram can and cannot tell you, and how to turn a broad brain question into a measurable connectomics study."
permalink: /technical-training/01-why-map-the-brain/
image: /assets/images/units/01-why-map-the-brain.svg
image_alt: "Stylized vector art: an unresolved point cloud crossing a frontier line into a crisp measured graph."
slug: 01-why-map-the-brain
track: core-concepts-methods
pathways:
  - technical foundation
  - conceptual framing
level: "Foundational"
time_estimate: "90 minutes reading + 60 minute lab"
prerequisites: "None. Introductory neuroscience helps but is not required."
content_type: path
---

{% include callouts/community-resources.html unit="01" %}

## Before you start

| | |
|---|---|
| **Time** | **Self-study ~2.5 h:** about 90 min of reading plus the 60 min lab. **Taught:** an 85 min session, per the [lecture plan]({{ '/technical-training/slides/01-why-map-the-brain/' | relative_url }}). **Deck:** the unit's slide deck is scoped to 60 min and does not follow the plan slide for slide. |
| **Prerequisites** | None |
| **You need** | Paper or a text editor. No data or code. |
| **You finish with** | A one-page study brief for a connectomics question of your own |

This unit is deliberately not about microscopes. It is about the reasoning step that
happens *before* anyone buys a microscope, and the one that is easiest to skip:
deciding what claim the data will be asked to support.

---

## What you'll be able to do

By the end of this unit you should be able to:

1. State, from memory, what physical features require electron-microscopy resolution and why light microscopy cannot substitute.
2. Estimate the raw data volume of a proposed EM experiment to within an order of magnitude, given a target tissue volume and voxel size.
3. Classify a connectivity claim as *supported by structure alone*, *supported by structure plus an extra assumption*, or *not supportable by structure*.
4. Convert a vague biological interest into a study brief containing a measurable structural endpoint, a null model, and an explicit non-claim.

Item 3 is the one that matters most. It is also the one most often failed.

---

## 1. The resolution argument, in numbers

Connectomics exists because of a physical mismatch between the size of the things
that carry information in the brain and the resolution of the instruments that are
cheap and fast.

| Structure | Approximate size | Resolvable by light microscopy (~200–250 nm limit)? |
|---|---|---|
| Cortical neuron soma | 10–25 µm | Yes, easily |
| Dendritic shaft | 0.5–3 µm | Yes |
| Myelinated axon | 0.5–2 µm | Usually |
| Dendritic spine head | 300–800 nm | Marginally |
| **Unmyelinated axon in neuropil** | **80–300 nm** | **No** |
| **Dendritic spine neck** | **50–200 nm** | **No** |
| **Synaptic cleft** | **~20 nm** | **No** |
| Synaptic vesicle | ~40 nm | No |
| Postsynaptic density | 30–50 nm thick | No |

The consequence is specific, not general. Light microscopy can tell you that two
neurons' arbors *overlap in space*. It cannot tell you whether they are *connected*,
because at 250 nm two membranes 20 nm apart are one blur. In dense cortical neuropil,
unmyelinated axons 80–300 nm across are packed membrane to membrane, so a single
250 nm blur can span several of them.

Electron microscopy at 4 nm × 4 nm × 40 nm resolves every row above in the section
plane. The 40 nm step in z is coarser, which is why clefts cut at an angle and thin
spine necks that run steeply through the stack stay hard to follow (Unit 08). That
resolution is the reason the field tolerates the cost described in the next section.

> **A caution that belongs here and not later.** Resolving a synapse is not the same as
> knowing its sign, strength, or whether it is active in a behaving animal. EM gives
> you an *anatomical* synapse: a presynaptic vesicle pool, a cleft, and a postsynaptic
> specialization. Sign (excitatory/inhibitory) is usually *inferred* from morphology
> (see Unit 05) or from a separate molecular measurement, not read off directly.

### Check yourself

<details markdown="1">
<summary>A colleague proposes using confocal microscopy of sparsely labeled neurons to
"map the connectome" of a cortical column. What is the strongest single objection?</summary>

Sparse labeling plus diffraction-limited optics gives *potential* contact (arbor
overlap), not synaptic connection. Predicting synapses from contact ("Peters' rule")
is unreliable at the level of individual neuron pairs: axons and dendrites that touch
often do not form a synapse, and connection probability varies by cell type. You
would be measuring a proxy whose relationship to the quantity of interest is itself
an open research question.

A secondary objection: sparse labeling means you cannot see the unlabeled
partner, so even a true synapse has an anonymous other side.
</details>

---

## 2. The cost argument, in numbers you can compute

You should be able to do this arithmetic in your head, because it is the fastest way
to sanity-check any proposal.

**Raw voxel count = (volume) ÷ (voxel volume).**

Work an example. Take 1 mm³ of cortex at 4 nm × 4 nm × 40 nm:

```
x: 1 mm / 4 nm    = 1,000,000 nm / 4 nm    = 250,000 voxels
y: 1 mm / 4 nm    =                          250,000 voxels
z: 1 mm / 40 nm   = 1,000,000 nm / 40 nm  =  25,000 voxels

total = 250,000 x 250,000 x 25,000 = 1.56 x 10^15 voxels
```

At 8-bit grayscale that is **~1.56 petabytes of raw image data for one cubic
millimeter**, before alignment, segmentation, meshes or any other derived product.
Published petascale volumes land in this range. Both are about 1 mm³: H01 (human
temporal cortex) is 1.4 PB aligned and 1.8 PB raw (Shapson-Coe et al. 2024), and
MICrONS (mouse visual cortex) is about 2 PB raw (MICrONS Consortium 2025).

Now extrapolate, and notice where it breaks. Every row is arithmetic at the stated voxel
size, 8-bit and uncompressed, not the size of a released dataset (FAFB, imaged at
4×4×40 nm, is about 106 TB). The two bottom rows are projections. Published projections
are rougher: Abbott et al. (2020, *Cell*) put a whole mouse brain at roughly a million
terabytes, about 1 EB.

| Target | Volume | Raw data at 4×4×40 nm | Status |
|---|---|---|---|
| *C. elegans* nervous system | ~0.00005 mm³ | ~0.1 TB | Done, repeatedly, since 1986 |
| Adult *Drosophila* brain | ~0.08 mm³ | ~125 TB | Done (FAFB / FlyWire; the hemibrain covers the central brain) |
| 1 mm³ of cortex | 1 mm³ | ~1.6 PB | Done (MICrONS in mouse, H01 in human) |
| Whole mouse brain | ~500 mm³ | **~800 PB** (est.) | The current grand challenge |
| Whole human brain | ~1.2 × 10⁶ mm³ | **~2 × 10²¹ bytes** (est.) | Not a plan; a horizon |

**Teaching point.** The jump from fly brain to 1 mm³ of mouse cortex is ~12×. The jump
from 1 mm³ to whole mouse brain is ~500×, and imaging is only one part of it. The same
factor applies to sectioning reliability, storage, alignment, segmentation accuracy
and, above all, *proofreading labor*. NIH's BRAIN CONNECTS program, whose first 11
awards were announced in September 2023, funds exactly this scaling work: its first
theme is electron microscopy pipelines to map the mouse brain.

### Check yourself

<details markdown="1">
<summary>You are offered beam time to image 0.05 mm³ of mouse hippocampus at
isotropic 8 nm (FIB-SEM). How much raw data, roughly, and what changes relative to
4×4×40 nm?</summary>

Voxel volume = 8 × 8 × 8 = 512 nm³. 0.05 mm³ = 5 × 10⁷ µm³ = 5 × 10¹⁶ nm³.
5 × 10¹⁶ / 512 ≈ **1 × 10¹⁴ voxels ≈ 100 TB at 8 bits per voxel.** For comparison,
the same 0.05 mm³ at 4 × 4 × 40 nm is 5 × 10¹⁶ / 640 ≈ 8 × 10¹³ voxels, about 80 TB.

What changes: isotropy. At 4 × 4 × 40 nm the z-axis is 10× coarser than xy, so thin
processes running in-plane are easy to follow and processes crossing z steeply are
hard. This anisotropy is a major source of automated segmentation errors (Unit 08).
Isotropic 8 nm removes the asymmetry. The price is throughput, and a practical limit
on how much volume FIB-SEM can mill in one run; larger volumes have to be cut into
slabs first.
</details>

---

## 3. What structure can and cannot establish

This is the section to argue about. Sort every claim you plan to make into one of
three bins.

### Bin A — structure alone is sufficient evidence

- *"Neuron X makes 42 synapses onto neuron Y."* Direct anatomical observation.
- *"Cell type A targets the proximal dendrites of type B, while type C targets distal
  dendrites."* Compartment-targeting is measured, not inferred.
- *"Reciprocal pairs occur 4× more often than expected under a degree-preserving null
  model."* A structural statistic against a stated null.
- *"This projection does not exist in this volume."* A negative result, with a stated
  detection sensitivity.

### Bin B — structure plus one declared assumption

- *"This synapse is excitatory."* Requires the assumption that asymmetric
  (Gray type I) morphology predicts glutamatergic transmission. Usually a good
  assumption in cortex; it is still an assumption, and it fails for known exceptions.
- *"This is a strong connection."* Requires assuming synapse count or total
  postsynaptic-density area is monotonic in physiological strength. Defensible, and
  supported in some systems, but it is a model.
- *"This circuit performs coincidence detection."* Requires a biophysical model
  linking morphology and connectivity to integration.

**Rule: any Bin B claim must name its assumption in the same sentence, or in the
figure caption.** "Putatively excitatory (asymmetric morphology)" costs four words.

### Bin C — structure cannot establish this

- *"This circuit computes X during behavior Y."* Requires physiology.
- *"This synapse is potentiated."* Requires a functional or molecular measure.
- *"This wiring causes the animal's decision."* Requires perturbation.
- *"Neuromodulatory state Z reconfigures this circuit."* Volume transmission is
  largely invisible in a standard EM volume.

A wiring diagram is a *constraint on the space of possible dynamics*, not a
simulation. The most common failure of connectomics writing is a Bin C sentence in
the abstract supported by a Bin A measurement in the results.

### Worked example: repairing a research question

> **Version 0 (as originally proposed):** "We will use connectomics to understand how
> the cortex implements predictive coding."

This is Bin C, it has no measurable endpoint, and no result could falsify it.
Repair it in four moves.

**Move 1 — find the structural signature.** Predictive-coding architectures generally
require some form of asymmetry between feedforward and feedback pathways, and a
population that receives both. In mouse visual cortex, a candidate structural
signature is: *feedback axons from higher visual areas preferentially target a
different dendritic compartment of layer 2/3 pyramidal cells than feedforward
thalamocortical and layer 4 inputs do.*

**Move 2 — define the measurement, with units.** For each proofread L2/3 pyramidal
cell, compute the fraction of input synapses by presynaptic source class, binned by
path distance from soma (0–50, 50–150, 150–300, >300 µm) and by compartment (spine
head, spine neck, shaft, soma, AIS). Report as synapses per source class per
compartment per cell, n cells.

**Move 3 — state the null.** Sources are distributed across compartments in
proportion to available postsynaptic surface area in each compartment. This null is
important: dendrites have more distal surface than proximal, so "more distal
synapses" is the *expected* result and is not evidence of anything.

**Move 4 — write the non-claim.** "These data constrain where feedback input arrives
on the dendritic tree. They do not establish that these synapses carry prediction
error signals, and they do not establish sign; sign is inferred from synaptic
morphology and from the identified source cell type."

> **Version 1 (usable):** "In mouse visual cortex, do inter-areal feedback axons
> target a systematically more distal dendritic compartment of L2/3 pyramidal cells
> than L4 feedforward axons do, relative to a surface-area-proportional null,
> measured across ≥50 proofread cells?"

Version 1 can be answered, can be wrong, and can be scoped in a grant.

### Check yourself

<details markdown="1">
<summary>Sort these into Bin A / B / C.
(i) "The mushroom body Kenyon cell input is random with respect to glomerular identity."
(ii) "This interneuron inhibits pyramidal cell firing."
(iii) "Layer 5 thick-tufted cells receive 3× more synapses on their apical tuft than
layer 5 slender-tufted cells."</summary>

**(i) Bin A**, provided "random" is defined against a stated null model and the
claim is restricted to the reconstructed population. It becomes Bin B if it is
extended to "input is unstructured", since unstructured with respect to one
labeling scheme may be structured with respect to another.

**(ii) Bin B, verging on C.** "Is GABAergic and forms symmetric synapses onto the
pyramidal cell's soma and proximal dendrite" is Bin A/B. "Inhibits firing" is a
functional claim; a GABAergic synapse can be depolarizing depending on chloride
reversal potential and developmental stage. State it as "putatively inhibitory".

**(iii) Bin A**, and note that it is a *ratio*, which quietly controls for a lot of
reconstruction bias. Ratios between comparably reconstructed populations are more
stable than absolute counts, which are sensitive to completeness. This is a habit
worth acquiring early.
</details>

---

## 4. Sizing the claim to the reconstruction

A structural claim is only as good as the completeness of the reconstruction behind
it. Match the claim type to the reconstruction state you actually have:

| Claim type | Minimum reconstruction state | Typical failure if you skip this |
|---|---|---|
| "Cell X synapses onto cell Y" | Both partners proofread through the synapse; synapse manually verified | A merge error invents the connection |
| "Cell X has n inputs" | Full dendritic arbor proofread and closed | Split errors truncate the arbor; n is an undercount of unknown size |
| "Type A prefers type B over type C" | Both target populations proofread to comparable completeness | Differential completeness masquerades as biological preference |
| "Motif M is enriched" | A closed subgraph with quantified edge precision/recall | Merges and splits change motif counts in a direction that depends on the motif and the graph rules |
| "This projection is absent" | Stated detection sensitivity and searched volume | Absence of evidence reported as evidence of absence |

The fourth row comes back in Unit 09. A single merge fuses two neurons' partner lists.
That can close triangles and reciprocal pairs that do not exist, but it can also
collapse two edges into one or turn a real connection into a self-loop that the graph
drops. Which way the count moves depends on the motif and on how the graph was built.
So motif analysis on unproofread segmentation is not automatically conservative, and
you cannot assume the errors cancel: you have to model them for your own graph.

---

## 5. What connectomics has actually delivered

Concrete anchors, so that "connectomics is useful" is a claim you can defend with
examples rather than enthusiasm.

- ***C. elegans*, 302 neurons (White et al. 1986; Cook et al. 2019; Witvliet et al.
  2021).** The first complete nervous system. Its lasting lesson is negative and
  useful: having the complete wiring diagram of 302 neurons did *not* immediately
  yield an understanding of behavior. It took decades of physiology and genetics on
  top of the map. Witvliet's developmental series added something the single adult
  map could not: which connections are stable across maturation and which are not.
- **Adult *Drosophila* (hemibrain, ~25,000 neurons, Scheffer et al. 2020; FlyWire
  whole brain, 139,255 neurons and ~54.5 million synapses, Dorkenwald et al. 2024).**
  The first complete wiring diagram of an adult fly brain. It produced new biology:
  complete cell-type censuses (Schlegel et al. 2024); a central-complex connectome
  whose network motifs fit an attractor model of head direction (Hulse et al. 2021);
  and a whole-brain model built from FlyWire connectivity that predicted which
  neurons drive feeding, a prediction then tested with optogenetics and behavior
  (Shiu et al. 2024).
- **MICrONS, ~1 mm³ mouse visual cortex (more than 200,000 cells, ~524 million
  synapses), with two-photon calcium imaging of ~75,000 neurons in the same tissue
  (MICrONS Consortium 2025).** Size is not the point here; co-registration is.
  Structure and function in the same neurons let you ask whether wiring predicts
  tuning. So far the answer is "partly": neurons with similar responses are more
  likely to be connected, across layers and areas (Ding et al. 2025). Only this data
  type can produce that kind of result.
- **H01, ~1 mm³ human temporal cortex (~57,000 cells, ~150 million synapses;
  Shapson-Coe et al. 2024).** Showed that tissue removed in surgery can be prepared and
  reconstructed at this scale. Among thousands of weak inputs to each neuron it found
  rare, powerful axonal inputs of up to 50 synapses onto a single target.

Note what is common to the useful results: each one is a *census* or a *comparison*,
not an assertion about computation. That is the shape of a defensible connectomics
result today.

---

## Visual context set

These five slides are framing devices, not evidence. Use each one to rehearse the sort in §3: for whatever claim the slide invites, ask whether structure alone could establish it, whether it needs a declared assumption, or whether it needs physiology the data does not contain.

<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-21_02388_X_TECHTALK_-S10-01.png' | relative_url }}" alt="Diagram of a brain with arrows to four functions: perception, navigation, memory, and decision and action selection" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Techtalk S10:</strong> The motivating question, asked before any instrument is chosen: how does the brain support perception, navigation, memory and decisions? Each of those is a Bin C topic as stated. Use it to practice the move this unit is built on: name the measurable structural endpoint, the null model, and the explicit non-claim that would have to replace it before the question is fundable.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-21_02388_X_TECHTALK_-S11-01.png' | relative_url }}" alt="A densely segmented cylinder of neuropil, each process shown in a different color" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Techtalk S11:</strong> Brain data at synapse resolution: a small cylinder of neuropil in which every process has its own color. Read it against the resolution table in §1. Dense segmentation like this depends on resolving the bold rows, which is what lets you tell arbor overlap from an actual connection.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-21_02388_X_TECHTALK_-S12-01.png' | relative_url }}" alt="Stock image of a computer chip on a circuit board" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Techtalk S12:</strong> The reverse-engineering analogy, and where it stops. Check it against the bin boundaries in §3. A wiring diagram constrains the space of possible dynamics; it is not a simulation. Any “this circuit computes X” reading of the analogy is a Bin C claim wearing Bin A clothing.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-MODULE12_LESSON1-S04-01.png' | relative_url }}" alt="Electron micrograph of densely packed cortical neuropil" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L1 S04:</strong> One EM field of neuropil, the raw material of every row in the §2 extrapolation table. Every value in it is one byte of the arithmetic in §2. Ask how many fields like this a whole mouse brain would take, and whether the limiting factor at that scale is microscopy or proofreading labor.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/01-why-map-the-brain/FIG-SRC-MODULE12_LESSON1-S07-01.png' | relative_url }}" alt="Illustration of the pipeline from brain tissue and an electron microscope, through an image stack and a server room, to reconstructed neurons and a brain drawn over a computer chip" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L1 S07:</strong> The whole pipeline as one illustration: tissue and microscope, image stack, compute, reconstructed neurons, and a final arrow to a brain drawn over a chip. Sort the arrows with §3. Everything up to the reconstruction is structure. The last arrow is a claim about computation, and it stays in Bin C until someone names the assumption that would carry it.</p>
  </article>
</div>

<p><small>Attribution: NeuroAI and outreach source decks (historical and context visuals).</small></p>

---

## Lab: write a study brief (60 minutes)

**Deliverable:** one page. Produce it in this order; do not skip to the method.

1. **Biological question** (2–3 sentences). Must contain a noun phrase naming a
   structure and a verb phrase naming a relationship.
2. **Structural signature.** What would have to be true of the wiring if your
   hypothesis were correct? What would have to be true if it were false? If you cannot
   answer the second, stop and reframe. An unfalsifiable signature is the usual defect
   at this step.
3. **Three measurements, with units.** For example: synapses per connected pair
   (count); fraction of output synapses onto spines vs shafts (dimensionless ratio);
   path length from soma to synapse (µm). "Connectivity" is not a measurement.
4. **Dataset requirements.** Voxel size; volume; species and age; required
   completeness (fragments / neurite-level / near-complete local circuit); estimated
   raw data volume computed as in §2.
5. **One null model,** stated precisely enough that someone else could implement it.
6. **One confound** you cannot remove, and how you will report it.
7. **One non-claim** — a sentence you will not write, in quotation marks, with the
   reason.

### Rubric

| | Not yet | Proficient | Strong |
|---|---|---|---|
| **Falsifiability** | No stated outcome would disconfirm the hypothesis | A disconfirming outcome is named | Disconfirming outcome named *and* distinguished from "underpowered" |
| **Measurement** | Named qualitatively ("look at connectivity") | Three measurements with units | Measurements chosen at the right scale for the hypothesis (local motif claims use local statistics, not whole-graph summaries) |
| **Null model** | Absent, or "compare to random" | A named null | Null preserves the nuisance structure that matters (degree, distance, cell-type composition) |
| **Scope discipline** | Bin C claims present | Non-claim stated | Bin B assumptions named inline where they occur |
| **Feasibility** | No data estimate | Volume and voxel size given | Data estimate computed, and proofreading effort acknowledged as the binding constraint |

**Self-grading tip:** the single best predictor of a weak brief is that step 7 is
empty or vague. If you cannot name a sentence you refuse to write, you have not yet
found the boundary of your evidence.

---

## Common errors and how to recover

**"We'll figure out the analysis once we have the data."**
Recover by writing the figure caption for your main result *now*, with fake numbers.
If you cannot write the caption, the experiment is not specified.

**Using whole-graph summary statistics to test a local hypothesis.**
Mean path length and global clustering coefficient are nearly useless for claims about
a specific microcircuit, and they are highly sensitive to reconstruction errors. If
the hypothesis is about a three-cell motif, measure the three-cell motif.

**Treating a reconstruction boundary as a biological boundary.**
Neurons cut by the volume edge have truncated arbors. Any per-cell count is biased
downward, and the bias is worse for cells near the edge and for cell types with large
arbors. Either restrict analysis to cells whose relevant arbor is fully contained, or
model the truncation explicitly.

**Comparing populations that were proofread differently.**
If population A was proofread to completion and population B was not, every
difference you find is confounded with effort. Match proofreading protocol before
comparing, and report proofreading state per cell.

---

## The norm behind this unit

Some of what this unit teaches is technique. Some of it is **professional norm** — the
things experienced people do without being asked, and which nobody states out loud
because they assume you already know. Those are worth naming, because they are
[distributed unequally by background]({{ '/hidden-curriculum/' | relative_url }}) rather
than by ability.

From this unit:

- **Name the assumption in the same sentence as the claim.**
  "Putatively excitatory (asymmetric morphology)" costs four words. Writing "excitatory" instead is not a shorthand; it is a different claim.

- **Write down the sentence you refuse to write.**
  Every study brief should carry an explicit non-claim. It shows a reader where your evidence stops, which is a sign of control, not weakness. Nobody tells you this, so the line is often left blank.

- **Prefer ratios to absolute counts when comparing.**
  A ratio between comparably reconstructed populations quietly controls for a great deal of reconstruction bias. Experienced people reach for it automatically.

The collected set, and why making these explicit is a fairness intervention rather than
etiquette, is in [the hidden curriculum]({{ '/hidden-curriculum/technical-practice/' | relative_url }}).

## What this unit does not cover

Imaging physics (Unit 03), segmentation methods (Unit 08), and the statistics of
motif testing (Unit 09). It also does not cover non-EM connectomics, such as
barcoding approaches (MAPseq/BARseq) and diffusion MRI tractography, which answer
different questions at different scales; Unit 02 shows how these fit together.

---

## Sources for the numbers in this unit

- Abbott L.F. et al. (2020). The mind of a mouse. *Cell* 182:1372–1376. [doi:10.1016/j.cell.2020.08.010](https://doi.org/10.1016/j.cell.2020.08.010)
- Cook S.J. et al. (2019). Whole-animal connectomes of both *Caenorhabditis elegans* sexes. *Nature* 571:63–71. [doi:10.1038/s41586-019-1352-7](https://doi.org/10.1038/s41586-019-1352-7)
- Ding Z. et al. (2025). Functional connectomics reveals general wiring rule in mouse visual cortex. *Nature* 640:459–469. [doi:10.1038/s41586-025-08840-3](https://doi.org/10.1038/s41586-025-08840-3)
- Dorkenwald S. et al. (2024). Neuronal wiring diagram of an adult brain. *Nature* 634:124–138. [doi:10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)
- Hulse B.K. et al. (2021). A connectome of the *Drosophila* central complex reveals network motifs suitable for flexible navigation and context-dependent action selection. *eLife* 10:e66039. [doi:10.7554/eLife.66039](https://doi.org/10.7554/eLife.66039)
- MICrONS Consortium et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. *Nature* 640:435–447. [doi:10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
- Scheffer L.K. et al. (2020). A connectome and analysis of the adult *Drosophila* central brain. *eLife* 9:e57443. [doi:10.7554/eLife.57443](https://doi.org/10.7554/eLife.57443)
- Schlegel P. et al. (2024). Whole-brain annotation and multi-connectome cell typing of *Drosophila*. *Nature* 634:139–152. [doi:10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5)
- Shapson-Coe A. et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science* 384:eadk4858. [doi:10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)
- Shiu P.K. et al. (2024). A *Drosophila* computational brain model reveals sensorimotor processing. *Nature* 634:210–219. [doi:10.1038/s41586-024-07763-9](https://doi.org/10.1038/s41586-024-07763-9)
- White J.G. et al. (1986). The structure of the nervous system of the nematode *Caenorhabditis elegans*. *Phil. Trans. R. Soc. B* 314:1–340. [doi:10.1098/rstb.1986.0056](https://doi.org/10.1098/rstb.1986.0056)
- Witvliet D. et al. (2021). Connectomes across development reveal principles of brain maturation. *Nature* 596:257–261. [doi:10.1038/s41586-021-03778-8](https://doi.org/10.1038/s41586-021-03778-8)
- Zheng Z. et al. (2018). A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell* 174:730–743. [doi:10.1016/j.cell.2018.06.019](https://doi.org/10.1016/j.cell.2018.06.019)

The extrapolation table in §2 is our arithmetic at 4 × 4 × 40 nm, 8-bit, uncompressed;
the *C. elegans* volume is a rough estimate, not a measured value.

## Go deeper

- [Connectome history]({{ '/content-library/connectomics/connectome-history/' | relative_url }}) — Cajal through BRAIN CONNECTS, with the lessons from each era
- [NeuroAI bridge]({{ '/content-library/connectomics/neuroai-bridge/' | relative_url }}) — structure-function relationships and honest boundaries
- [MICrONS visual cortex]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }}) — the functional co-registration case study
- [MouseConnects HI-MC]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}) — a BRAIN CONNECTS project scaling EM to about 10 mm³ of mouse hippocampus
- [*C. elegans* revisited]({{ '/content-library/case-studies/c-elegans-revisited/' | relative_url }}) — why a complete connectome was not an explanation

## Course links

- Reading list: [Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Related module: [Module 01]({{ '/modules/module01/' | relative_url }})
- Lecture plan: [Why Map the Brain lecture plan]({{ '/technical-training/slides/01-why-map-the-brain/' | relative_url }})
- Graduate lecture: [Introduction to Connectomics]({{ '/course/decks/marp/out/en585781/module07-introduction-to-connectomics.html' | relative_url }}) — 59-slide EN.585.781 deck ([source]({{ site.deck_source_base }}/en585781/module07-introduction-to-connectomics.marp.md))
- **Next unit:** [02 Brain Data Across Scales]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }})
