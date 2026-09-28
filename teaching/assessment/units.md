---
layout: page
title: "Assessment bank: technical units"
permalink: /teaching/assessment/units/
slug: assessment-bank-units
content_type: delivery
description: "Public formative items for the nine technical units, tagged to each unit's outcomes, with synthetic numbers, variant templates and a note on calibration rounds."
---

[Worked answers and feedback]({{ '/teaching/assessment/units-answers/' | relative_url }}) · [Lecture items]({{ '/teaching/assessment/' | relative_url }}) · [Technical Course]({{ '/technical-training/' | relative_url }})

This pool has formative items for the nine technical units of the
[Technical Course]({{ '/technical-training/' | relative_url }}). Each item is tagged to
one outcome from its unit's "What you'll be able to do" list. Items mix calculations,
claim sorting and short answers. The [lecture bank]({{ '/teaching/assessment/' | relative_url }})
covers the four lectures; this page covers the units.

**Every number, cell name and scenario here is synthetic.** None is a measurement from
a published dataset. The numbers differ from the units' worked examples and
"Check yourself" questions, and from the lecture bank, so neither the unit text nor
the lecture keys answer these items directly.

**This pool is public and formative.** Use it for practice, review and in-class checks.
It is not secure exam material. Each item ends with a **variant template** line naming
what to change. Recompute every answer for a variant. Nothing here has been validated
as an assessment instrument, and item difficulty and discrimination are unmeasured.

## Outcome tags

Tag `U3-4` means Unit 03, outcome 4, as numbered on the unit page.

| Unit | Tag | Outcome (short form) |
|---|---|---|
| [01 Why Map the Brain]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}) | U1-1 | State what requires EM resolution and why light microscopy cannot substitute. |
| | U1-2 | Estimate raw data volume from tissue volume and voxel size. |
| | U1-3 | Classify a claim as structure alone, structure plus an assumption, or not supportable by structure. |
| | U1-4 | Turn a vague interest into a study brief with an endpoint, a null and a non-claim. |
| [02 Brain Data Across Scales]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}) | U2-1 | Place a modality on a resolution/volume/throughput chart. |
| | U2-2 | Name the smallest sufficient resolution and why the next coarser step fails. |
| | U2-3 | Choose a representation and state what it discards. |
| | U2-4 | Say how a claim can and cannot transfer between scales. |
| | U2-5 | Detect scale leakage. |
| [03 EM Prep and Imaging]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}) | U3-1 | Link each prep step to the defect it causes when it fails. |
| | U3-2 | Name the acquisition cause of a visible defect. |
| | U3-3 | Separate artifacts that cost proofreading hours from artifacts that cost data. |
| | U3-4 | Estimate acquisition time. |
| | U3-5 | Write an acquisition QA report a reconstruction team can act on. |
| [04 Volume Reconstruction Infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}) | U4-1 | Describe the pipeline and each stage's output. |
| | U4-2 | Explain the editable graph over immutable supervoxels. |
| | U4-3 | Explain materialization versions and why analysis is pinned to one. |
| | U4-4 | Query a volume reproducibly. |
| | U4-5 | Plan capacity and cost, naming the dominant cost. |
| [05 Neuronal Ultrastructure]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}) | U5-1 | Name organelles, sizes and the compartment each implies. |
| | U5-2 | Apply the three synapse criteria and refuse a call when one is missing. |
| | U5-3 | Distinguish Gray type I and II and the inference each licenses. |
| | U5-4 | Assign a confidence tier with an evidence chain. |
| | U5-5 | Diagnose errors by cue. |
| [06 Axons and Dendrites]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}) | U6-1 | Classify a process as axon or dendrite with a stated confidence. |
| | U6-2 | Name the four polarity exceptions. |
| | U6-3 | Explain quantitatively why direction errors cost more. |
| | U6-4 | Measure agreement and find the over-trusted cue. |
| | U6-5 | Write a protocol another annotator can follow. |
| [07 Glia]({{ '/technical-training/07-glia/' | relative_url }}) | U7-1 | Identify astrocytes, oligodendrocytes and microglia. |
| | U7-2 | Discriminate a fine astrocytic process from a thin neurite. |
| | U7-3 | Explain how one glia merge corrupts a connectivity measurement. |
| | U7-4 | Prioritize glia corrections by impact. |
| | U7-5 | Interpret a discrimination confusion matrix. |
| [08 Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}) | U8-1 | Rank error types by cost for an endpoint. |
| | U8-2 | Choose a metric and say what it hides. |
| | U8-3 | Triage by effect on the endpoint. |
| | U8-4 | Define a checkable stopping rule. |
| | U8-5 | Estimate and defend proofreading effort. |
| [09 Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}) | U9-1 | Construct a graph and justify each choice. |
| | U9-2 | Select a null that preserves the relevant nuisance structure. |
| | U9-3 | Run a motif analysis with multiple-comparison handling. |
| | U9-4 | Quantify sensitivity to reconstruction error. |
| | U9-5 | State what connectomes do and do not give machine learning. |

## Unit 01: Why map the brain

**U1.1 Short answer (U1-1).** A light microscope in this item resolves 230 nm laterally.
For each synthetic structure, say whether it can be resolved and whether EM is needed:
(a) a dendritic shaft 1.2 µm across; (b) an unmyelinated axon 140 nm across; (c) a
synaptic cleft 18 nm across; (d) a spine head 600 nm across. Then answer: if a
super-resolution method resolved (b), would you then know whether that axon synapses
on the neighboring dendrite?

*Variant template:* change the resolution limit and the four sizes, keeping at least one
structure on each side of the limit.

**U1.2 Calculation (U1-2).** A synthetic block of 0.30 × 0.24 × 0.12 mm is imaged at
6 × 6 × 30 nm, one byte per voxel, no compression.

(a) Give the voxel dimensions, total voxels and size in decimal TB.
(b) Give the size at two bytes per voxel.
(c) The same block is imaged instead at isotropic 12 nm. Give total voxels, decimal TB
at one byte, and the ratio of (a) to (c). Name one thing the isotropic volume gains.

*Variant template:* change the block dimensions, both voxel sizes and the bytes per
voxel; keep dimensions that divide evenly.

**U1.3 Calculation (U1-2).** Without a calculator, estimate the raw size of
0.02 mm³ imaged at 4 × 4 × 40 nm, one byte per voxel, to within a factor of ten. Show
the unit conversion. Then name two costs that grow with volume but do not appear in
the byte count.

*Variant template:* change the volume and the voxel size; keep the arithmetic doable by
hand.

**U1.4 Claim sorting (U1-3).** In a synthetic, fully proofread region, cell Wren makes
14 synapses onto cell Sparrow, all with asymmetric (Gray type I) morphology. Sparrow's
dendrites are closed; a neighboring population, type Finch, is only 40% proofread.
Sort each claim: **A**, structure alone; **B**, structure plus a stated assumption;
**C**, structure cannot establish it. Give the reason.

1. Wren makes 14 synapses onto Sparrow in this region.
2. Wren's input to Sparrow is excitatory.
3. Wren is Sparrow's strongest input.
4. Wren drives Sparrow to fire during locomotion.
5. Wren's axon targets Sparrow-type cells more than Finch-type cells.

*Variant template:* change the counts, the morphology and the completeness of the
comparison population; keep one claim that fails on completeness rather than on physiology.

**U1.5 Short answer (U1-4).** Repair this proposal into a study brief with a
measurable structural endpoint (with units), a null model and one explicit non-claim:
"We will use connectomics to understand how the hippocampus stores memories."

*Variant template:* change the region and the vague function (for example, "attention"
in thalamus or "learning" in cerebellum).

## Unit 02: Brain data across scales

**U2.1 Ordering (U2-1).** Using typical values from the unit's modality chart, order
these five modalities (a) from finest to coarsest resolution and (b) from largest to
smallest practical volume: diffusion MRI, light-sheet LM with tracers, expansion
microscopy, SBEM, FIB-SEM. What do the two orderings show together?

*Variant template:* swap in other rows of the chart (confocal, array tomography,
multibeam ssSEM, barcoded projection mapping), keeping five.

**U2.2 Short answer (U2-2).** For each question, name the smallest sufficient
acquisition scale and say why the next coarser step fails.

(a) Across one mouse brain, do axons from area Plover reach area Heron at all?
(b) In one cortical column, what fraction of synapses onto pyramidal-cell axon initial
segments are symmetric?
(c) In living human volunteers, is there a large white-matter pathway between two
cortical regions?

*Variant template:* change the three questions, keeping one that needs synapse
resolution, one that needs only projections and one that needs in vivo human data.

**U2.3 Calculation and choice (U2-3).** A synthetic study will compare spine head
volume between two classes of dendrite on 450 proofread neurons. Using the unit's
per-neuron size ranges, give the total size range for skeletons and for meshes of all
450 neurons. Which representation does the endpoint need, which does it rule out and
why, and what should be archived?

*Variant template:* change the neuron count and the endpoint (for example, path
distance of inputs from the soma, or a count of connections between two types).

**U2.4 Calculation (U2-4).** A synthetic EM↔two-photon registration fits 400 anchors.
The mean residual on the fitted anchors is 2.3 µm; on 80 held-out anchors it is
4.2 µm. Of 400 cells with functional traces, 52 sit in one corner where the local
residual is 18 µm and nearest-neighbor soma spacing is about 12 µm.

(a) Which residual should the methods report as accuracy, and why?
(b) What fraction of the traced cells sit in the poorly registered corner?
(c) What should happen to those cells, and what must the result report?

*Variant template:* change the residuals, the held-out count, the corner cell count and
the local soma spacing, keeping one region where spacing is below the local residual.

**U2.5 Calculation (U2-4).** Two points in a 4 × 4 × 40 nm stack differ by 300, 400
and 50 voxels in x, y and z. A script computes their distance as the voxel-unit
Euclidean distance times 4 nm. Give the script's value and the true distance in nm,
and the ratio between them. Which way does this error bias distance-based measurements?

*Variant template:* change the voxel offsets and the voxel size, keeping the z step
coarser than xy.

**U2.6 Claim check (U2-5).** Mark each statement **scale leakage** or **sound as
written**, and give the reason.

1. Tractography in 30 volunteers shows regions P and Q are connected, so P neurons
   synapse onto Q neurons.
2. Light-sheet imaging of a bulk tracer shows labeled axons from area Plover in area
   Heron.
3. In confocal images, a labeled axon touches a labeled dendrite at 40 sites, so the
   two cells share 40 synapses.
4. In a 0.1 mm³ EM volume, cell type Kite forms symmetric synapses on axon initial
   segments, so Kite cells silence pyramidal output throughout cortex.
5. Barcoded projection mapping shows that 22% of barcoded cells in area Rook send
   axons to both of two target areas.

*Variant template:* write new statements, keeping at least two that are sound and one
that leaks through sampling rather than resolution.

## Unit 03: EM preparation and imaging

**U3.1 Matching (U3-1).** Name the preparation step whose failure most likely produced
each synthetic observation, and say what went wrong.

(a) Red blood cells remain in many vessels, and the neuropil around them looks
under-fixed.
(b) Small, very dark, irregular particles are scattered across sections.
(c) A sharp-edged gap runs along a large vessel in several sections.
(d) Swollen, pale astrocytic processes and watery cytoplasm across the block.

*Variant template:* change the four defects, drawing on the unit's "what failure looks
like" lists for fixation, staining, embedding and sectioning.

**U3.2 Diagnosis (U3-2).** For each synthetic observation, name the likely acquisition
cause and the coordinate the defect follows (block position, anatomy, acquisition time
or processing).

(a) Bright streaks trail the scan direction in block-face images of a resin-rich
region.
(b) In a FIB-SEM run, vertical stripes run parallel to the milling direction.
(c) The per-tile sharpness proxy declines steadily over 30 hours of imaging and
recovers after instrument service.
(d) Structures jump sideways between sections 5,112 and 5,113; tiles within each
section line up.

*Variant template:* change the defects and the section numbers, keeping one that follows
acquisition time.

**U3.3 Triage (U3-3).** A synthetic 30,000-section volume, cut at 40 nm, has: (a) 3
consecutive lost sections; (b) 9 lost sections scattered at random; (c) knife chatter
on 8% of sections; (d) weak membrane contrast in the bottom third of the block;
(e) sparse precipitate. Label each **labor** or **data loss**, give the scattered-loss
rate as a percentage, give the gap in (a) between surviving neighbors, and rank the five
for triage.

*Variant template:* change the section count and thickness, the counts and fractions,
and which region has weak contrast.

**U3.4 Calculation (U3-4).** A synthetic volume of 600 × 500 × 300 µm will be imaged at
8 × 8 × 30 nm on an instrument that sustains 0.05 gigapixels per second including
overheads.

(a) Give pixels per section, section count and total pixels.
(b) Give continuous imaging time in days, and the time at 70% uptime.
(c) The team wants twice the SNR at the same beam current. Estimate the new time at
70% uptime. What does the estimate still leave out?

*Variant template:* change the volume, the voxel size, the rate and the uptime; keep
dimensions that divide evenly.

**U3.5 QA decision (U3-5).** A synthetic acquisition uses the unit's example gates.
Today's log: membrane CNR 4.5 against a baseline of 6.0; alignment residual 99th
percentile 1.4 voxels at native xy; cumulative lost-section rate 0.4%, none consecutive;
fold area 7% on section 812 only. Which gates are breached, and what action does each
require? Write the two sentences of the QA report that a reconstruction team most
needs, keeping labor and data loss separate.

*Variant template:* change the log values so a different set of gates is breached.

## Unit 04: Volume reconstruction infrastructure

**U4.1 Matching and calculation (U4-1).** Name the pipeline stage that produces each
output: (a) a checksummed archive and tile manifest; (b) a transform stack; (c) a
per-voxel affinity map; (d) small over-segmented fragments; (e) a table of coordinates
with pre- and postsynaptic supervoxel IDs.

Then: (f) segmentation errors in a synthetic volume fall on a regular grid spaced every
512 voxels, regardless of anatomy. Which stage, and what is the fix? (g) An alignment
has a bias of 0.05 voxel per section in one direction. Over 12,000 sections at 4 nm
per voxel in xy, how far does it drift, in voxels and in µm?

*Variant template:* change the outputs listed, the grid spacing, the per-section bias,
the section count and the pixel size.

**U4.2 Short answer (U4-2).** In a synthetic ChunkedGraph system with a synapse table
of 3 × 10⁸ rows, a proofreader merges two objects; the merged neuron carries 2,400
synapses. (a) What is written to the system for the merge, and what for a later split?
(b) How many synapse-table rows must be rewritten if partners are stored as supervoxel
IDs, and how many if stored as root IDs? (c) What happens to a copy of the table a
colleague downloaded last month under each design?

*Variant template:* change the table size, the synapse count on the edited object and
the edit type.

**U4.3 Calculation (U4-3).** A collaborator sends 150 root IDs from an older
materialization of a synthetic dataset. Lineage mapping to the current version shows:
119 map one-to-one, 21 each split into two current roots, and 10 merged in pairs.

(a) How many current roots do the 150 old IDs map to?
(b) What fraction of the old IDs changed? What fraction map one-to-one?
(c) The collaborator's figure must be reproduced exactly. Should you map forward or
query the old version? What goes in the methods?

*Variant template:* change the counts in each lineage category, and the split and merge
multiplicities.

**U4.4 Short answer (U4-4).** A synthetic methods sentence reads: "We queried the
synapse table of the Lark dataset in March and found that cell 4417 receives 1,204
input synapses." List what a reader needs to rerun this query and get the same number,
and rewrite the sentence with placeholders for each missing item.

*Variant template:* change the dataset name, the cell, the quantity and which items are
already present.

**U4.5 Calculation (U4-5).** Plan a synthetic volume of 0.5 × 0.4 × 0.25 mm at
8 × 8 × 40 nm, one byte per voxel.

(a) Give total voxels and raw size in decimal TB.
(b) Give the aligned pyramid at base plus one third, and three 8-bit affinity channels
at full resolution.
(c) At 10⁷ voxels per second per GPU, give GPU-days for one inference pass and for
four passes.
(d) The study needs 600 proofread neurons at 5 hours each. Taking 1,600 productive hours
per annotator-year, give person-hours and annotator-years.
(e) Name the dominant cost and one intermediate you would delete, with its condition.

*Variant template:* change the block, voxel size, GPU rate, pass count, neuron count,
hours per neuron and productive hours.

## Unit 05: Neuronal ultrastructure

**U5.1 Short answer (U5-1).** For each synthetic profile, name the compartment or cell
class it implies and say whether the cue is near-diagnostic or only consistent.

(a) A process holds clusters of very dark particles about 25 nm across.
(b) A 500 nm process contains ribosome rosettes and several microtubules.
(c) A thin process holds one vesicle about 100 nm across with a dark core, and no
vesicle cluster.
(d) A profile is wrapped in regular concentric dark lamellae.
(e) A process shows a granular density beneath its membrane and bundled microtubules,
40 µm from a soma.

*Variant template:* change the five profiles, drawing on other rows of the unit's
organelle table; keep one that is consistent with two compartments.

**U5.2 Synapse calls (U5-2).** Sections are 35 nm thick. Call each synthetic candidate
**synapse**, **not a synapse** or **check further**, and name the criterion that decides it.

(a) Vesicles cluster at an apposition; the cleft is uniform; a thick density lines the
partner; visible on 8 consecutive sections.
(b) Symmetric densities on both sides of a contact; no vesicle pool anywhere nearby.
(c) A dark thickening persists across 3 sections, with a vesicle cluster, but the gap
varies in width and there is no density on either side.
(d) Vesicles cluster at an apposition with a uniform cleft; on 2 sections a dark patch is
seen face-on across the partner membrane.

Then: a PSD 280 nm across is cut edge-on. On about how many 35 nm sections should it
appear? A candidate seen edge-on on one section only: what does that suggest?

*Variant template:* change the section thickness, the PSD width and the four candidates,
keeping one adherens-junction case and one face-on case.

**U5.3 Claim sorting (U5-3).** Label each statement **licensed as written**, **needs
the assumption named** or **not licensed**, and give the reason.

1. "This synapse onto a spine head is excitatory."
2. "This synapse is putatively inhibitory (symmetric morphology)."
3. "The vesicles are flattened, which proves the terminal releases GABA."
4. "This symmetric synapse comes from an axon traced to a type Vireo interneuron, all of
   whose other reconstructed synapses are symmetric."
5. "This dense-core-vesicle terminal is type II, so it is inhibitory."

*Variant template:* change the five statements, keeping one that adds presynaptic
cell-type corroboration and one that falls outside the type I/II dichotomy.

**U5.4 Confidence tiers (U5-4).** Assign **high**, **medium** or **uncertain** using the
unit's operational definitions, and name the cue families.

(a) Ribosome rosettes, microtubules and a mitochondrion; checked on 2 sections.
(b) A vesicle cluster, and the vesicles are pleomorphic; partner density unclear.
(c) Ribosome rosettes, a spine leaving the process, and an incoming asymmetric density;
confirmed across 5 sections.
(d) The process crosses a fold; the caliber suggests axon, one faint rosette suggests
dendrite.

Then: an annotator marks 0 of 240 calls uncertain. What does that suggest?

*Variant template:* change the evidence in each case and the uncertain count; keep one
case that stacks cues from a single family.

**U5.5 Calculation (U5-5).** A synthetic review of one annotator's 60 synapse calls
finds 14 false positives: 9 were dark membrane contrast with no vesicle cluster, 3 were
adherens junctions, and 2 had a vesicle cluster but appeared edge-on on one section only.

(a) Give the annotator's precision.
(b) What fraction of the false positives would criterion 1 (a presynaptic vesicle
cluster) alone have stopped?
(c) Which cue does this annotator over-trust, and what one protocol change follows?

*Variant template:* change the call count and the false-positive breakdown so a
different criterion dominates.

## Unit 06: Axons and dendrites

**U6.1 Protocol run (U6-1).** Apply the unit's local classification protocol to each
synthetic process in mouse cortex. Give the call, the confidence and the step that
decided it.

(a) A 170 nm process, no synapse in view, no ribosomes; over 3 µm it neither tapers nor
swells.
(b) A 900 nm process with ribosome rosettes; a spine leaves it two sections down.
(c) A process sits inside a bundle of myelinated fibers.
(d) A process bears a thin symmetric density; it has a granular undercoating and bundled
microtubules, 25 µm from a soma.

*Variant template:* change the calibers and cues, keeping one case that ends at
"uncertain" and one that is an exception.

**U6.2 Short answer (U6-2).** Name the four situations where the polarity rule (vesicle
cluster ⇒ axon, PSD ⇒ dendrite) fails. For each synthetic dataset, say whether the rule
is a safe protocol default: (a) mouse hippocampus CA1; (b) mouse olfactory bulb;
(c) a larval fly ventral nerve cord; (d) mouse thalamus.

*Variant template:* change the four datasets, keeping at least one safe and two unsafe.

**U6.3 Calculation (U6-3).** In a synthetic graph, 400 truly one-way connections each
carry exactly 3 synapses. Direction is called synapse by synapse, and each call is
reversed independently with probability 0.1.

(a) What is the probability that a given one-way connection appears reciprocal?
(b) How many of the 400 are expected to appear reciprocal?
(c) Repeat (a) for connections of exactly 2 synapses and of exactly 1 synapse.
(d) A co-author says the direction errors "only add noise, so the true reciprocity is
at least what we measured." Answer in two sentences.

*Variant template:* change the connection count, the synapses per connection and the
flip probability.

**U6.4 Calculation (U6-4).** A synthetic calibration round has 30 patches. High
confidence: 16 calls, 13 correct. Medium: 9 calls, 7 correct. Uncertain: 5, with the
best guess right on 3. The 5 wrong high- and medium-confidence calls cite these cues:
caliber (4), "PSD on the process, so dendrite" (1).

(a) Give accuracy by tier and overall.
(b) Is this annotator calibrated? Use the unit's threshold.
(c) Which cue is over-trusted, and in what context did the other error happen?

*Variant template:* change the tier counts and the cue tally so a different cue
dominates.

**U6.5 Short answer (U6-5).** Using U6.4's result, write two protocol rules another
annotator could follow and a reviewer could check. Then write one rule that fails
that test, and say why.

*Variant template:* change the dominant misleading cue and the dataset's tissue type.

## Unit 07: Glia

**U7.1 Short answer (U7-1).** Name the class of each synthetic soma and the feature that
decides it, or say what to do instead.

(a) A 7 µm soma with a small, round, very dark nucleus; a thin process leads toward a
myelin sheath.
(b) A soma with a pale, irregular nucleus, pale cytoplasm and clusters of very dark
20–30 nm particles.
(c) A soma with a dark, bean-shaped nucleus, heterochromatin clumped along the envelope,
and cytoplasm full of lysosomes and inclusions.
(d) A soma whose round nucleus is darker than nearby neurons but clearly paler than an
oligodendrocyte in the next field; no myelin in view.

*Variant template:* change the four descriptions, keeping one OPC-like case.

**U7.2 Discrimination (U7-2).** In a poorly stained synthetic region, glycogen granules
and microtubules cannot be resolved. Profile Tern is angular and changes contour over
8 sections to fill the gaps between neurites. Profile Egret holds a round cross-section
along a continuous path over 8 sections, and on the ninth section a vesicle cluster
appears on it. Call each, give the confidence, and name the cue that survives poor
staining.

*Variant template:* change which cues are visible and the section counts, keeping one
profile that is decided by synaptic participation.

**U7.3 Calculation (U7-3).** In a synthetic volume, a fine astrocytic process is merged
into a pyramidal cell. It adds 38 µm of path, along which synapse detections occur at
0.9 per µm; all of them come from cells within 20 µm. Before the merge, the cell had
610 true inputs, 120 of them from cells within 20 µm.

(a) About how many false inputs does the merge add, and by what percentage does it
inflate the input count?
(b) What fraction of the cell's inputs come from within 20 µm, before and after the
merge?
(c) Which way does the merge push a local-clustering or distance-dependence result, and
why?

*Variant template:* change the added path length, the detection density, the true input
count and the local count.

**U7.4 Triage (U7-4).** The endpoint is connection probability among 40 proofread
pyramidal cells. Rank these synthetic edits by effect on the endpoint, and say which
the unit would rank above a conspicuous split.

(a) An astrocytic process merged into one of the 40 cells, adding about 30 inputs.
(b) An obvious split in the axon of a cell outside the 40.
(c) An astrocytic process merged into a cell outside the 40.
(d) A dendrite tip split from one of the 40, losing 2 inputs.
(e) Two astrocytes merged with each other.

*Variant template:* change the endpoint, keeping one glia-neuron merge inside the
analysis set and one conspicuous error outside it.

**U7.5 Confusion matrix (U7-5).** A synthetic 40-patch drill gives these results (true
class → called class):

| True class | Called |
|---|---|
| Astrocytic process (10) | astrocyte 6, neurite 3, uncertain 1 |
| Thin neurite (10) | neurite 9, astrocyte 1 |
| Astrocyte soma (5) | astrocyte 5 |
| Oligodendrocyte soma (5) | oligodendrocyte 3, microglia 2 |
| Microglia soma (5) | microglia 4, oligodendrocyte 1 |
| OPC, reference-confirmed (5) | OPC 2, uncertain 3 |

(a) Give overall accuracy and accuracy on committed (non-uncertain) calls.
(b) Name the dominant off-diagonal cell, what it says about the annotator, and its cost.
(c) Where does this annotator sit on the unit's rubric for accuracy and error asymmetry?
(d) What should the re-drill contain?

*Variant template:* change the matrix so a different off-diagonal cell dominates.

## Unit 08: Segmentation and proofreading

**U8.1 Ranking (U8-1).** The synthetic endpoint is "synapses from type Gannet axons onto
each proofread layer 4 cell." Rank these error types by cost for that endpoint, and
say which would be hardest to detect: (a) a merge of a Gannet axon with an axon of
another type; (b) a split that detaches the distal half of a Gannet axon; (c) false
synapse detections; (d) missed synapse detections; (e) orphan fragments in white matter.

*Variant template:* change the endpoint and the five errors, keeping one merge that
changes presynaptic identity.

**U8.2 Calculation (U8-2).** (a) Two synthetic segmentation versions report VI:

```text
             split VI   merge VI   total VI
Version P      0.95       0.12       1.07
Version Q      0.60       0.34       0.94
```

By what percentage is Q's total lower, and by what factor has its merge component
grown? Should Q ship?

(b) A ground-truth skeleton totals 100 µm, and a segmentation traces it in error-free
runs of 40, 25, 15, 10 and 10 µm. Give the ERL. What would you need to know about the
implementation before comparing it with a paper's ERL?

*Variant template:* change the VI components and the run lengths; keep one version whose
total improves while merges get worse.

**U8.3 Triage (U8-3).** The endpoint is the fraction of input synapses by presynaptic
class on 150 analysis-set cells. You have 50 annotator-minutes. Order the work and say
what is left undone.

- **P:** a glia–neuron merge on an analysis-set cell's basal dendrite; 25 min.
- **Q:** a split near the soma of an analysis-set cell, detaching about half the arbor;
  8 min.
- **R:** a merge of two axons, both presynaptic to analysis-set cells; 12 min.
- **S:** a conspicuous two-soma merge, neither cell in the set; 15 min to fix, 2 min to
  check its partner list for synapses onto the set.
- **T:** a 3 µm twig split from an analysis-set cell's dendrite tip; 3 min.

*Variant template:* change the times, the budget and which cells sit in the analysis
set.

**U8.4 Stopping rules (U8-4).** (a) Say which of these synthetic rules is checkable by
someone else, and rewrite the one that is not: (i) "Stop when the data look clean";
(ii) "Stop when a second independent pass over a 20-cell sample changes the endpoint by
less than 5%"; (iii) "Proofread until the budget runs out."
(b) Under rule (ii), the endpoint ratio is 2.40 after the first pass. Should you stop if
the second pass gives 2.31? If it gives 2.22?

*Variant template:* change the rules, the tolerance and the before/after values; keep
one value on each side of the tolerance.

**U8.5 Calculation (U8-5).** A synthetic study needs 180 cells at level L2 (dendrite
complete). Pilot timings for 8 cells, in hours: 3.5, 4.0, 5.5, 2.5, 6.0, 4.5, 3.0, 7.0.

(a) Give the mean, median and range. Which should drive the total, and why?
(b) Estimate hours for: the 180 cells; an independent second pass on 15% of them; and an
exhaustive check of 20 cells taking twice the mean time each. Give the total.
(c) At 5 productive proofreading hours per annotator-day, how many annotator-days?
(d) Name two weaknesses of this estimate and how you would defend it to a reviewer.

*Variant template:* change the cell count, the pilot timings, the verification fraction
and the hours per day.

## Unit 09: Connectome analysis and NeuroAI

**U9.1 Calculation (U9-1).** A synthetic graph has 250 cells. Of its connections, 2,100
carry one synapse, 700 carry two and 450 carry three or more. Type Kite accounts for
360 of the connections, 300 of them single-synapse.

(a) Give the edge count at thresholds ≥ 1, ≥ 2 and ≥ 3, and the fraction of ≥ 1 edges
removed at ≥ 3.
(b) What fraction of Kite's connections survive at ≥ 2, against the fraction for the
whole graph? What does that do to a type-level comparison?
(c) Name the other construction choices a methods section must state.

*Variant template:* change the counts in each synapse bin and the type's share, keeping
one type that relies on single-synapse connections.

**U9.2 Calculation (U9-2).** A synthetic graph has 80 neurons, 790 directed edges and
118 reciprocal pairs.

(a) Under Erdős–Rényi, give p, the expected reciprocal pairs and observed/expected.
(b) A degree-preserving null gives mean 96, sd 9. Give observed/expected and z.
(c) A degree- and distance-preserving null gives mean 109, sd 10. Give observed/expected
and z.
(d) What share of the excess over Erdős–Rényi does degree alone account for? Write the
conclusion for the hypothesis "reciprocity exceeds what degree and proximity explain."

*Variant template:* change the node, edge and reciprocal counts and the two null means
and sds; keep one null under which the result survives and one under which it does not.

**U9.3 Calculation (U9-3).** A synthetic triad census tests all 16 classes by
permutation. The sorted p-values are 0.0004, 0.0021, 0.0048, 0.011, 0.019, 0.034, 0.08,
0.12, 0.19, 0.27, 0.35, 0.44, 0.58, 0.66, 0.79 and 0.93.

(a) How many are below 0.05 uncorrected? How many false positives would you expect at
α = 0.05 if no class were truly enriched?
(b) How many survive Bonferroni at family-wise α = 0.05?
(c) How many survive Benjamini–Hochberg at FDR 0.05? Show the step.
(d) Why is permutation inference preferred for triads, and what must the paper report
about the tests?

*Variant template:* change the p-values so Bonferroni and BH disagree by a different
number.

**U9.4 Short answer and calculation (U9-4).** (a) A merge fuses neuron Dunlin (partners
1–4) with neuron Knot (partners 5–7). How many new partner pairs does the merged object
create? If 2 of those pairs are themselves connected, how many triangles now pass
through a cell that does not exist?
(b) A synthetic reciprocity ratio is 1.31 against a null of 1.0. Applying the measured
merge and split rates to 200 perturbed graphs gives a 5th–95th percentile band of 0.97
to 1.36. Does the result survive? What exactly does the band mean, and what does it
not mean?

*Variant template:* change the partner sets, the connected pairs, the observed ratio and
the band, keeping one band that crosses the null.

**U9.5 Claim sorting (U9-5).** Label each statement **defensible**, **overclaim** or
**dismissive underclaim**, and give the reason.

1. Fixing a model's connectivity from a connectome removes free parameters and makes the
   model falsifiable.
2. Synapse counts can be loaded as the weights of an artificial network to reproduce the
   animal's computation.
3. Connectome-constrained models have never been compared against recorded activity.
4. Connectomics has posed hard machine-learning problems, such as petascale segmentation
   with few labels.
5. Simulating a mouse connectome will soon give a runnable mouse brain.

*Variant template:* write new statements, keeping at least one of each label.

## Running a calibration round

The judgment items (U5.2, U5.4, U6.1, U7.1, U7.2) work as a calibration round for
instructors or teaching assistants who will grade together. Everyone scores the same
three learner responses with the rubric on the
[answers page]({{ '/teaching/assessment/units-answers/' | relative_url }}#scoring),
then compares scores before grading the cohort. The procedure, and why the narrowing of
the spread is the point, is in the
[Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}#run-a-calibration-round-before-the-cohort-matters).
Record the spread before and after discussion; that is local evidence about the rubric,
not about the items.

**No validated instrument exists here.** These items have not been piloted, and their
difficulty, discrimination and reliability are unmeasured. A calibration round tells
you whether your graders agree with each other. It does not tell you whether the items
measure the unit outcomes. Do not use scores from this pool for high-stakes decisions.

Teaching material: CC BY 4.0, NeuroTrailblazers.
