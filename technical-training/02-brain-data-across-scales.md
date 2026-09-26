---
layout: page
title: "02 Brain Data Across Scales"
description: "How to choose a modality, resolution, and representation for a connectomics question, and how to link measurements across scales without over-claiming."
permalink: /technical-training/02-brain-data-across-scales/
image: /assets/images/units/02-brain-data-across-scales.svg
image_alt: "Stylized vector art: three nested zoom frames, from brain outline to circuit to vesicles."
slug: 02-brain-data-across-scales
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
level: "Foundational"
time_estimate: "90 minutes reading + 75 minute lab"
prerequisites: "Unit 01"
content_type: path
---

{% include callouts/community-resources.html unit="02" %}

## Before you start

| | |
|---|---|
| **Time** | **Self-study ~2.75 h:** about 90 min of reading plus the 75 min lab. **Taught:** a 90 min session, per the [lecture plan]({{ '/technical-training/slides/02-brain-data-across-scales/' | relative_url }}). **Deck:** the unit's slide deck is scoped to 60 min and does not follow the plan slide for slide. |
| **Prerequisites** | [Unit 01]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}), specifically the voxel-count arithmetic in §2 |
| **You need** | A calculator. Optional: a Neuroglancer link to any public volume |
| **You finish with** | A scale-selection memo defending one modality choice against two alternatives |

Almost every practical connectomics decision is a scale decision in disguise. "Should
we use SBEM or ssTEM?" is a scale decision. "Can we answer this with the existing
public dataset?" is a scale decision. "Why doesn't our tractography result match the
EM result?" is a scale decision that was made badly, earlier.

---

## What you'll be able to do

1. Place any neuroscience measurement modality on a resolution/volume/throughput chart from memory, within an order of magnitude.
2. Given a biological question, name the *smallest sufficient* resolution and justify why the next step coarser fails.
3. Choose among volume, mesh, skeleton, and graph representations for a given analysis, and state what each discards.
4. Describe how a claim measured at one scale can and cannot be transferred to another.
5. Detect "scale leakage" (a mechanistic claim resting on data that cannot resolve the mechanism) in someone else's writing and in your own.

---

## 1. The three scales that are not the same thing

Three different scales get conflated all the time. Keeping them apart prevents a
lot of downstream confusion.

**Acquisition scale** is the voxel size and field of view your instrument produces.
Physics and budget set it, and it is fixed once the data exists.

**Reconstruction scale** is the smallest object you can *reliably* segment. It is
always coarser than acquisition scale, sometimes much coarser. At 4 × 4 × 40 nm you
acquire enough signal to see a 20 nm cleft in the section plane. Segmentation needs
an object to span several pixels in each section and to appear in several sections.
In z each 40 nm section is a single sample, so a 50 nm spine neck running steeply
through the stack may show up in only one or two sections, and that is where
reconstruction fails first.

**Analysis scale** is the unit your conclusions are about: a synapse, a cell, a cell
type, a layer, an area, a projection.

> **The decision rule.** Choose the coarsest acquisition scale whose *reconstruction*
> scale still resolves every object your *analysis* scale depends on. Not the finest
> you can afford: the coarsest that works. Every step finer multiplies data volume,
> alignment difficulty and proofreading hours.

A worked instance of the rule: if your endpoint is "fraction of inputs onto spines vs
shafts", your analysis scale is the synapse and the spine neck. Spine necks are
50–200 nm. So your reconstruction scale must be ≤ 50 nm, which forces EM. If instead
your endpoint is "does area A project to area B at all", your analysis scale is the
axon bundle. Light-sheet imaging of a bulk tracer at 1 µm is then the correct choice,
not a compromise: a 1 µm³ voxel holds 10⁹ / 640 ≈ 1.6 million voxels of
4 × 4 × 40 nm, so it needs roughly a million times fewer voxels.

---

## 2. The modality chart

Learn this table. Ranges are typical rather than record-setting.

| Modality | Resolution (typical) | Practical volume | What it uniquely gives you | What it cannot do |
|---|---|---|---|---|
| Diffusion MRI tractography | 0.5–2 mm | Whole human brain, in vivo | Whole-brain, living, repeatable, human | Cannot see individual axons; produces false and missing tracts; no synapses; no direction |
| Light-sheet / whole-brain LM with tracers | 0.5–2 µm (xy) | Whole mouse brain | Long-range projection maps, many animals | Cannot resolve neurites in neuropil; no synapses |
| Confocal / two-photon | 200–300 nm lateral | mm³, in vivo possible | Function (calcium), molecular labels, live | Diffraction-limited; overlap ≠ connection |
| Expansion microscopy | ~25–70 nm effective | Up to a whole fly brain or the full depth of mouse cortex (Gao et al. 2019) | Molecular identity *plus* near-EM geometry | Expansion distortion; not yet routine for dense reconstruction at scale |
| Array tomography | ~200 nm lateral (diffraction-limited), 50–200 nm sections | ~10⁵ µm³ | Multiplexed protein labeling on ultrathin sections, with z-resolution set by section thickness (Micheva & Smith 2007) | Section loss; lateral resolution too coarse for dense neurite tracing |
| Barcoded projection mapping (MAPseq/BARseq) | Single-cell identity, no geometry | Whole brain; thousands of neurons per brain (3,579 in Chen et al. 2019) | Projection patterns of many individual cells, cheaply | No synapses, no morphology, no local circuit |
| ssTEM / ssSEM (multibeam) | 4 × 4 × 40 nm | Up to ~1 mm³ today | Dense synapse-resolution reconstruction at scale | Anisotropic; section artifacts; enormous cost |
| SBEM | 10–20 × 10–20 × 25–50 nm | ~10⁶–10⁷ µm³ | Automated block-face series, no section handling | Destructive; z-resolution limits thin-process tracing |
| FIB-SEM | 4–8 nm isotropic | ~10⁵–10⁶ µm³ (larger with hot-knife partitioning) | Isotropic voxels, the best tracing conditions available | Slow; limited volume per run |

### The tradeoff triangle

Resolution, volume and throughput form a budget you cannot escape: **you may choose
two.** FIB-SEM buys resolution and gives up volume. Light-sheet buys volume and
throughput and gives up resolution. The 1 mm³ volumes bought resolution and volume by
parallelizing acquisition. H01 was imaged on a 61-beam multibeam SEM (Shapson-Coe et
al. 2024). MICrONS used five automated TEMs running for about six months (MICrONS
Consortium 2025).

### Check yourself

<details markdown="1">
<summary>You want to know whether individual layer 2/3 neurons in mouse visual cortex
that project to area AL also project to area PM, across thousands of cells. Which
modality, and why not EM?</summary>

**Barcoded projection mapping (MAPseq/BARseq).** The question is about
*single-cell projection classes* across thousands of cells. It needs statistical
power over cells, not geometry within a cell. MAPseq gives exactly that, at a cost
per cell far below EM.

EM is the wrong tool here for two reasons. (1) A 1 mm³ volume does not span V1, AL
and PM together. MICrONS, for example, covers V1 and three higher visual areas (AL,
RL and LM), but not PM (MICrONS Consortium 2025). You would need a much larger volume
than anyone has imaged. (2) Even then, the answer needs *n* in the thousands, and
proofreading thousands of complete long-range axons in EM is not tractable today.

The honest limitation to state: barcoding gives you projection *presence* in a
target region, not synapses in that region, and it is vulnerable to
fibers-of-passage and to barcode-sharing artifacts.
</details>

<details markdown="1">
<summary>A tractography paper reports a "structural connection" between two regions.
An EM study of one of those regions finds no axons from the other. Both can be
correct. Explain.</summary>

They are measuring different things at scales that do not nest cleanly.

Tractography infers streamlines from voxel-scale water diffusion orientation. A
streamline is a model output, not an observed axon. Known failure modes include
false continuations where fibers cross, and a "gyral bias": streamlines terminate
preferentially on gyral crowns rather than in the banks of sulci (Schilling et al.
2018). A tractography "connection" is a statement about the most probable pathway
given a diffusion model. It is *not* a claim that a specific axon terminates there.

Meanwhile, an EM volume samples a small region. Absence of axons in that volume is
evidence about *that volume*, at whatever detection sensitivity the reconstruction
achieved. If the projection terminates in an adjacent layer or a neighboring
column, EM would miss it.

The resolution is not "one of them is wrong". It is that neither claim, as usually
written, states its sampling and its inference model clearly enough to be compared.
This is scale leakage in both directions.
</details>

---

## 3. Representations: what each one throws away

After reconstruction, the same neuron exists in four representations. Choosing wrongly
is a common and expensive mistake because conversions are lossy and usually one-way.

| Representation | What it is | Keeps | Discards | Typical size, one cortical neuron |
|---|---|---|---|---|
| **Volume / labeled voxels** | The segmentation itself | Everything, including membrane geometry and organelles | Nothing, but unwieldy for most analysis | GB per neuron at native resolution |
| **Mesh** | Triangulated surface | Surface geometry, volume, surface area, spine shape | Interior, intensity, organelles | 10–100 MB |
| **Skeleton** | Centerline graph with radii | Topology, path length, branch structure, radius | Surface detail, spine head shape, membrane apposition | 0.1–5 MB |
| **Connectivity graph** | Nodes = cells, edges = synapse counts | Who connects to whom, how strongly | *All* geometry: compartment, distance, position | Kilobytes per neuron (a few thousand edges) |

**The rule that saves projects:** decide which representation your endpoint metric
requires *before* the pipeline runs, and keep the next-richer one archived.

Concrete example of getting this wrong: a team exports a connectivity graph, runs
motif analysis, and finds an enrichment. A reviewer asks whether the enrichment is
explained by spatial proximity, since dendrites that are close connect more. The graph has
no geometry, so the question cannot be answered without re-running from skeletons.
Archiving skeletons alongside the graph costs gigabytes, not terabytes, and avoids
the re-run.

### Which representation for which question

- "How many synapses between A and B?" → **graph**
- "Where on the dendrite do those synapses land?" → **skeleton** (path distance from soma) **+ synapse coordinates**
- "Are spines on this dendrite larger than on that one?" → **mesh**
- "Is this a merge error?" → **volume**, always. Every proofreading decision ultimately returns to the voxels.

### Worked example: choosing a representation for an inhibition-distance question

> **Question as posed:** "On layer 2/3 pyramidal cells, do putatively inhibitory
> (symmetric) synapses sit closer to the soma, in path distance, than putatively
> excitatory (asymmetric) ones?" Planned scope: ~300 proofread cells from an
> existing public volume.

Start from the endpoint, not from what the pipeline happens to emit. The
measurement is a distribution of path distance from soma, per synapse, per synapse
class. Now hold each representation against that requirement.

**Graph:** discards all geometry, including the one quantity the question is
about. Rejected in one line.

**Volume:** contains everything, at GB per neuron, so hundreds of GB to about 1 TB
of hot label data for 300 cells. Computing path distance from voxels means
extracting a centerline anyway. You would be building skeletons expensively, on demand, forever.

**Mesh:** 10–100 MB per neuron, so 3–30 GB for the study. Surfaces are the right
tool for spine shape, which this endpoint does not need, and path distance along
the arbor is not a natural mesh operation.

**Skeleton plus synapse coordinates:** 0.1–5 MB per neuron, so 30 MB to 1.5 GB for
all 300 cells, and path distance from soma is the native query on a centerline
graph. This is exactly the pairing the list above prescribes for "where on the
dendrite do those synapses land?"

So far the decision looks free. Here is where it is not. Skeletons discard spine
geometry, so a synapse on a spine head gets mapped to the nearest shaft node, and
its path distance loses the neck. Asymmetric synapses land mostly on spines;
symmetric ones mostly on shafts and somata (Unit 05). The shortening therefore
falls mostly on one of the two classes being compared. That is a differential bias,
the dangerous kind. How large is it? The skeleton cannot tell you; it discarded
precisely that quantity. A spine neck is a micrometer or two long, which is probably
small against distance bins tens of micrometers wide. But "probably" is not a number
you can print.

The resolution is the archiving rule from this section: run the analysis on
skeletons, and archive the meshes. At 3–30 GB they are noise next to the
petabyte-scale image data the volume already carries. On a 20-cell subsample, measure the
spine-neck offset on the mesh, and either correct the distances or report the
bound.

**Transferable principle:** choose the representation whose native operation is
your endpoint metric; reject the coarser candidates by naming the discarded
quantity that disqualifies them; and archive the next-richer representation
specifically so you can bound the bias the one you chose introduces.

---

## 4. Cross-scale linkage: registration and its residuals

Linking scales (EM to two-photon function, EM to a reference atlas, one animal to
another) is registration, and registration is where confident-looking errors are
manufactured.

### The pipeline

1. **Choose anchors.** Vasculature is a strong anchor for EM↔LM in cortex: it is
   sparse, high-contrast in both modalities, distributed throughout the volume, and
   stable within an animal. Soma positions are the other common anchor. MICrONS fit
   its EM↔two-photon transform to 2,934 expert-matched fiducials (1,994 somata and
   942 blood-vessel points; the paper's parts sum to 2,936) and reported a mean residual of 3.8 µm (MICrONS
   Consortium 2025). Layer boundaries are a weak anchor, because they are gradual and
   observer-dependent.
2. **Fit a transform, of the lowest complexity that works.** Rigid → affine →
   non-linear, in that order. Reach for a non-linear warp only when residuals demand
   it, because a sufficiently flexible warp will align *anything*, including things
   that do not correspond.
3. **Report residuals locally, not globally.** A mean residual of 3 µm over the whole
   volume can hide a 40 µm error in one corner. Report a residual map or, at minimum,
   per-region residual distributions with the maximum.
4. **Hold out anchors.** Fit on a subset, measure residuals on anchors the fit never
   saw. A model evaluated on its own training points reports its flexibility, not its
   accuracy.
5. **Propagate the uncertainty.** If EM↔functional registration has 5 µm local
   residual and you are assigning calcium traces to somata that are 15 µm across and
   sometimes 10 µm apart, some assignments are wrong. Quantify how many, and carry
   that number into the result.

> **Anisotropy warning.** On a 4 × 4 × 40 nm stack, an isotropic Gaussian smoothing
> kernel, an isotropic distance metric, or an isotropic morphological operation is
> silently wrong by a factor of 10 in z. Check every library call for whether it takes
> voxel spacing. The bug is common and quiet, and it biases every distance-based
> measurement you make.

### Check yourself

<details markdown="1">
<summary>Your EM↔two-photon registration reports mean residual 2.1 µm, max 31 µm.
Should you proceed to assign functional traces to reconstructed cells?</summary>

Not globally, and not yet. The max tells you there is a region where the transform
fails. Steps, in order:

1. Map residuals spatially. A 31 µm error is rarely uniform noise. It usually marks
   a region (a volume edge, a tissue fold, a poorly anchored depth) where the
   transform extrapolates.
2. Decide whether to exclude that region or add anchors there.
3. For the regions you keep, compute a per-cell assignment confidence using the
   *local* residual and the local soma density. Where nearest-neighbor soma
   spacing is comparable to local residual, mark assignments ambiguous rather than
   forcing a match.
4. Report the number of cells excluded and the number ambiguous. A functional
   connectomics result whose paper does not state its registration residual
   distribution has not shown its work.
</details>

---

## 5. Compute and storage, planned rather than discovered

Storage for the raw volume is the *smallest* line item. Plan for the multiplier.

For a 1 mm³ ssTEM volume (~1.6 PB raw), here are rough planning ranges. They are our
order-of-magnitude estimates for budgeting, not measurements of any released dataset.

- Aligned image pyramid (multi-resolution, for interactive viewing): **~1.3× raw** if
  a full-resolution aligned copy is kept, because each 2× downsampling in xy adds a
  quarter of the level above (1/4 + 1/16 + … ≈ 1/3). Less if alignment is done on a
  coarser grid; MICrONS generated its aligned volume at 8 nm rather than 4 nm.
- Affinity / boundary predictions: **~1×** raw (often float, then quantized)
- Segmentation labels (64-bit IDs, compressed): **0.1–0.5×** raw
- Meshes at multiple levels of detail, all objects: **1–10 TB**
- Skeletons, all objects: **10–100 GB**
- Synapse table (~5 × 10⁸ rows, the scale of the 524 million synapses detected in
  MICrONS, with coordinates, partner IDs, sizes and scores): **~50–200 GB**
- Proofreading edit history and versioned materializations: **grows without bound**
  and must be curated

The operational lesson: the raw volume is written once and read rarely. The synapse
table and the segmentation are read constantly, by many people, with latency
expectations measured in milliseconds. **Budget for query load, not just capacity.**
A petabyte that is rarely read can sit in low-cost archival storage. A 200 GB table
that must answer 50 concurrent interactive queries is the part that needs
engineering. Unit 04 covers the
architecture that follows from this.

---

## Visual context set

Use this panel to rehearse the three-scale separation from §1. For each slide, say which scale it is actually about: acquisition, reconstruction or analysis. Pipeline diagrams often blur all three, and noticing the blur is the skill this unit teaches.

<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON1-S06-01.png' | relative_url }}" alt="Electron micrograph of densely packed cortical neuropil" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L1 S06:</strong> An EM field of neuropil at synapse resolution. Run it through the decision rule in §1. Reconstruction scale is always coarser than acquisition scale, so ask which of the processes in this frame could be segmented reliably, not just which ones you can see.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON2-S04-01.png' | relative_url }}" alt="Brain with two numbered regions linked by a tract, mapped to one cell of a region-by-region connection matrix, above a whole-brain tractogram and its full matrix" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L2 S04:</strong> A macroscale pipeline. Place it on the modality chart in §2 and name which two corners of the resolution/volume/throughput triangle it buys, and therefore which one it gives up. Nothing at macroscale resolves neurites in neuropil, so connectivity read off it is model output, not observation.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON2-S05-01.png' | relative_url }}" alt="Flowchart of an image-analysis pipeline: 3D image stacks and labeled training data feed a vessel-segmentation step and a cell-detection step" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L2 S05:</strong> A mesoscale pipeline that segments vessels and detects cells in 3D image stacks, the scale between tractography and EM. Joins between scales are where scale leakage is manufactured: check what claim is being carried across the join, and whether the transfer comes with a stated registration residual and its maximum, not just its mean (§4).</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON3-S08-01.png' | relative_url }}" alt="Stock image of a brain drawn as glowing circuit-board traces" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L3 S08:</strong> A brain drawn as a circuit board, the image the source lesson used for high-throughput methods. It shows only a graph: nodes and wires with no geometry. Ask which representation from §3 it resembles, what that representation discards, and which richer one you would archive to check a claim made from it.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON3-S03-01.png' | relative_url }}" alt="Whole-brain diffusion tractography: dense bundles of color-coded streamlines" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L3 S03:</strong> Whole-brain diffusion tractography. Place it on the modality chart in §2 (0.5–2 mm resolution, whole living human brain) and read its last column: no individual axons, no synapses, no direction. Every colored line is a streamline, a model output. That is half of the answer to the tractography check-yourself in §2; the other half is how little of the brain an EM volume samples.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/02-brain-data-across-scales/FIG-SRC-MODULE12_LESSON2-S06-01.png' | relative_url }}" alt="Line drawing of a network: nodes joined by edges, grouped into dense clusters" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module12 L2 S06:</strong> A network drawing: nodes, edges, and clusters. This is the connectivity-graph row of the §3 table, the smallest representation and the one that discards all geometry. Before trusting any cluster in a picture like this, ask the reviewer's question from §3: would proximity alone explain it, and is there a richer representation archived to check?</p>
  </article>
</div>

<p><small>Attribution: outreach source decks (historical and context visuals).</small></p>

---

## Lab: scale-selection memo (75 minutes)

**Scenario.** Your lab wants to test whether inhibitory interneurons in mouse visual
cortex preferentially target the axon initial segment (AIS) of pyramidal neurons that
share functional tuning, versus pyramidal neurons that do not.

Write a two-page memo that selects a data strategy. Required sections:

1. **Decompose the question.** List every physical object your endpoint depends on.
   (Hint: there are at least four, and one of them is not anatomical.)
2. **Minimum resolution, defended.** For each object, the size and therefore the
   required reconstruction scale. Then state explicitly what fails if you go one step
   coarser.
3. **Modality choice, with two rejected alternatives.** For each rejection, name the
   specific structure it would fail to resolve or the specific measurement it could
   not make. "Too low resolution" is not a reason; "cannot resolve a 1 µm AIS
   segment's synaptic input, and cannot distinguish symmetric from asymmetric
   synapses" is.
4. **Cross-scale plan.** How functional tuning gets linked to reconstructed cells:
   anchors, transform class, residual target, and holdout validation.
5. **Representations.** Which representation each of your three measurements comes
   from, and what you will archive.
6. **Budget estimate.** Raw volume by the Unit 01 arithmetic, plus a derived-product
   multiplier, plus an estimate of proofreading hours with your stated assumption
   about hours per neuron.
7. **The bottleneck.** Name the single step most likely to end the project, and one
   mitigation.

### Rubric

| | Not yet | Proficient | Strong |
|---|---|---|---|
| **Decomposition** | Question restated | All required objects listed with sizes | Includes the non-anatomical requirement (functional tuning) and notes it forces in-vivo imaging *before* fixation |
| **Resolution defense** | Asserts EM | States required scale per object | States what specifically fails one step coarser, per object |
| **Rejections** | Alternatives listed | Rejected with a reason | Rejected with the specific unresolvable structure named |
| **Registration** | Mentioned | Anchors and transform named | Residual target, holdout plan, and consequence of failure quantified |
| **Budget** | Absent | Raw volume computed | Derived products and proofreading labor included; labor identified as dominant |
| **Bottleneck** | Generic ("funding") | A real pipeline step | A step with a stated failure probability and a concrete mitigation |

<details markdown="1">
<summary>Sample answer sketch for step 1 (open only after attempting it)</summary>

Objects the endpoint depends on:

1. **The AIS:** a ~20–60 µm segment of proximal axon, identifiable in EM by its
   membrane undercoating and fascicled microtubules. Requires EM; it is not
   distinguishable from proximal dendrite in LM without a molecular label.
2. **Synapses onto the AIS:** chandelier-cell cartridges, symmetric. Requires
   ≤ 50 nm to identify and to classify as symmetric.
3. **Identity of the presynaptic interneuron:** requires tracing the axon back to a
   soma with enough arbor to type the cell. This is the expensive part: it needs a
   proofread axon, not just a synapse detection.
4. **Functional tuning of the postsynaptic pyramidal cell:** *not anatomical*.
   Requires two-photon calcium imaging of the same tissue before fixation, hence the
   whole experiment must be planned as a functional-then-structural pipeline, with
   registration as a first-class design constraint rather than an afterthought.

The point of the exercise: step 4 changes the entire project structure and is the
thing most often discovered too late.
</details>

---

## Common errors and how to recover

**Scale leakage.** A mechanistic claim resting on data that cannot resolve the
mechanism. Recovery: write the sentence, then write underneath it the smallest object
the sentence depends on, then check that object against your reconstruction scale.

**Trusting a global registration metric.** Recovery: always produce a residual map.
If your tooling does not produce one, produce it manually from held-out anchors.

**One-way representation conversion.** Recovery: archive the next-richer
representation. Skeletons alongside graphs; meshes alongside skeletons if storage
allows.

**Isotropic operations on anisotropic data.** Recovery: audit every distance,
smoothing, and morphology call for voxel-spacing arguments. Add a unit test that
computes a known distance along z.

**Assuming public data fits your question.** Recovery: before proposing new
acquisition, check whether MICrONS, FlyWire, H01, or a BossDB volume already contains
the objects you need at the scale you need. Sometimes one does, and the honest answer
to "what modality?" is "none; this is a re-analysis".

---

## The norm behind this unit

Some of what this unit teaches is technique. Some of it is **professional norm** — the
things experienced people do without being asked, and which nobody states out loud
because they assume you already know. Those are worth naming, because they are
[distributed unequally by background]({{ '/hidden-curriculum/' | relative_url }}) rather
than by ability.

From this unit:

- **Report registration residuals locally, with the maximum, never as a global mean alone.**
  A mean residual of 3 µm can hide a 40 µm failure in one corner. A reader who knows the field looks for the distribution first and is wary of a paper that reports only the mean.

- **Archive the next-richer representation.**
  Keeping skeletons alongside a connectivity graph costs gigabytes, not terabytes, and answers the reviewer question you otherwise cannot answer without re-running the pipeline.

The collected set, and why making these explicit is a fairness intervention rather than
etiquette, is in [the hidden curriculum]({{ '/hidden-curriculum/technical-practice/' | relative_url }}).

## What this unit does not cover

The physics of image formation and the artifact catalog (Unit 03), the systems
architecture that stores and serves these representations (Unit 04), and the
statistics that operate on the resulting graph (Unit 09).

---

## Sources for the numbers in this unit

- Chen X. et al. (2019). High-throughput mapping of long-range neuronal projection using in situ sequencing. *Cell* 179:772–786. [doi:10.1016/j.cell.2019.09.023](https://doi.org/10.1016/j.cell.2019.09.023)
- Gao R. et al. (2019). Cortical column and whole-brain imaging with molecular contrast and nanoscale resolution. *Science* 363:eaau8302. [doi:10.1126/science.aau8302](https://doi.org/10.1126/science.aau8302)
- Micheva K.D. & Smith S.J. (2007). Array tomography: a new tool for imaging the molecular architecture and ultrastructure of neural circuits. *Neuron* 55:25–36. [doi:10.1016/j.neuron.2007.06.014](https://doi.org/10.1016/j.neuron.2007.06.014)
- MICrONS Consortium et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. *Nature* 640:435–447. [doi:10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
- Schilling K. et al. (2018). Confirmation of a gyral bias in diffusion MRI fiber tractography. *Human Brain Mapping* 39:1449–1466. [doi:10.1002/hbm.23936](https://doi.org/10.1002/hbm.23936)
- Shapson-Coe A. et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science* 384:eadk4858. [doi:10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)

The modality ranges and the derived-product footprints in §5 are typical working
ranges and our estimates, not values from a single source.

## Go deeper

- [Atlas and connectomics reference]({{ '/technical-training/atlas-connectomics-reference/' | relative_url }}) — the dataset specs, scale figures, and acronyms this unit cites, in one lookup table
- [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) — volumes, meshes, skeletons, graphs in detail
- [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }}) — the resolution/field-of-view/throughput triangle from the physics side
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) — end-to-end architecture
- [MRI connectomics reading]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }}) — where the macroscale literature and this track meet

## Course links

- Reading list: [Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Related modules: [Module 04]({{ '/modules/module04/' | relative_url }}), [Module 05]({{ '/modules/module05/' | relative_url }}), [Module 12]({{ '/modules/module12/' | relative_url }})
- Lecture plan: [Brain Data Across Scales lecture plan]({{ '/technical-training/slides/02-brain-data-across-scales/' | relative_url }})
- Graduate lecture: [Introduction to Connectomics]({{ '/course/decks/marp/out/en585781/module07-introduction-to-connectomics.html' | relative_url }}) — 59-slide EN.585.781 deck ([source]({{ site.deck_source_base }}/en585781/module07-introduction-to-connectomics.marp.md))
- **Next unit:** [03 EM Prep and Imaging]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})
