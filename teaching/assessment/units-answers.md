---
layout: page
title: "Technical unit items: worked answers"
permalink: /teaching/assessment/units-answers/
slug: assessment-bank-units-answers
content_type: delivery
description: "Worked answers and error-specific feedback for the technical-unit assessment items, with every calculation recomputed."
---

[Unit items]({{ '/teaching/assessment/units/' | relative_url }}) · [Lecture answers]({{ '/teaching/assessment/answers/' | relative_url }}) · [Technical Course]({{ '/technical-training/' | relative_url }})

These answers use the pool's **synthetic** data. They are public and formative. Every
calculation was recomputed with Python (exact integer or fraction arithmetic where the
numbers allow it). For each item, the feedback lines name a specific wrong answer or
reasoning error and what to say to a learner who gives it.

This pool is not secure. For summative use, write a variant from the template on each
item and recompute its answers. Nothing here is a validated assessment instrument.

## Scoring

Use the same local rubric as the [lecture bank]({{ '/teaching/assessment/answers/' | relative_url }}#scoring).
Score each short-answer and claim-sorting item **0–2**: two for a correct answer with its
reason, one for a correct answer with a missing or partial reason, zero for an incorrect
or unsupported answer. Score each calculation **0–2**: two for correct values with
denominators or units shown, one for a single recoverable slip with correct setup, zero
for a wrong setup. For claim-sorting items, score each claim separately. Credit a
defensible alternative where the feedback says so.

## Unit 01

### U1.1 (U1-1)

(a) **Resolved**, no EM needed; 1.2 µm is about five times the 230 nm limit.
(b) **Not resolved.** 140 nm is below the limit; in packed neuropil it blurs with its
neighbors. EM is needed to follow it.
(c) **Not resolved.** 18 nm is more than ten times below the limit. EM is needed.
(d) **Resolved, marginally.** 600 nm is above the limit, but the neck that joins the
head to its dendrite usually is not (the unit's table gives 50–200 nm).

Final part: **no.** Resolving the axon shows where it is, not whether it forms a
synapse. A synapse call needs a vesicle pool, a cleft and a postsynaptic density
(Unit 05), all tens of nanometers, and the identity of the partner. Contact is not
connection: axons and dendrites that touch often form no synapse.

Feedback by error:

- **(d) "not resolved."** The head is above the limit. Ask what part of a spine the
  learner is thinking of; usually it is the neck, which is a good instinct.
- **"Yes, if we can see it touching, it's connected."** This is the Peters' rule
  inference. Ask what three things must be seen to call a synapse.

### U1.2 (U1-2)

(a) 300,000 / 6 = **50,000**; 240,000 / 6 = **40,000**; 120,000 / 30 = **4,000** voxels.
Total **8,000,000,000,000 (8 × 10¹²)** voxels, **8 TB** at one byte.
(b) **16 TB.**
(c) 25,000 × 20,000 × 10,000 = **5 × 10¹²** voxels, **5 TB**. Ratio (a)/(c) = **1.6**.
The isotropic volume removes the z anisotropy, so processes that cross the stack steeply
are as easy to follow as those in-plane. (It is smaller here because the 12 nm xy pixel
is coarser; it does not resolve a cleft as cleanly.)

Feedback by error:

- **8 × 10⁹ or 8 × 10¹⁵.** A millimeter-to-nanometer slip. 1 mm = 10⁶ nm.
- **Ratio 0.625.** The learner divided (c) by (a). Accept with the direction stated.
- **"Isotropic is always better."** Ask what the 12 nm xy pixel does to a 20 nm cleft.

### U1.3 (U1-2)

0.02 mm³ = 0.02 × 10¹⁸ nm³ = 2 × 10¹⁶ nm³. Voxel volume = 4 × 4 × 40 = 640 nm³.
2 × 10¹⁶ / 640 ≈ **3.1 × 10¹³ voxels, about 31 TB** at one byte. Accept anything from
about 10 to 100 TB with the conversion shown.

Costs not in the byte count (any two): alignment and segmentation compute, derived
products (meshes, skeletons, synapse tables), backup copies, and above all
proofreading labor.

Feedback by error:

- **2 × 10⁷ nm³ or 2 × 10¹⁰ nm³.** The learner cubed the wrong factor. 1 mm³ =
  (10⁶ nm)³ = 10¹⁸ nm³.
- **Only compute costs named.** Ask who fixes the segmentation and how that scales.

### U1.4 (U1-3)

1. **A.** Direct count in a proofread region.
2. **B.** Assumes asymmetric morphology predicts glutamatergic transmission. Full
   credit needs the assumption named: "putatively excitatory (asymmetric morphology)".
3. **B.** "Strongest" assumes synapse count tracks physiological strength. "Wren makes
   more synapses onto Sparrow than any other input" is A, because Sparrow's dendrites
   are closed.
4. **C.** A claim about activity during behavior needs physiology.
5. **Not supported by this reconstruction.** Finch is 40% proofread, so a lower count
   onto Finch cells is confounded with missing arbor. Accept **C** if the reason is
   completeness, and accept "A once both populations are proofread to comparable
   completeness." Do not accept A as the data stand.

Feedback by error:

- **2 as A.** Ask what the image shows and what it implies. The morphology is observed;
  the transmitter is inferred.
- **5 as A.** Point to the "Type A prefers type B over type C" row of the unit's §4
  table: differential completeness looks like biological preference.
- **3 as C.** Too strict. Strength by synapse count is a declared assumption, not
  impossible; the claim moves to A if reworded as a count.

### U1.5 (U1-4)

A model brief (other endpoints earn full credit if they meet the three requirements):

- **Endpoint.** For each proofread CA1 pyramidal cell in the volume, the number of CA3
  input synapses per 100 µm of dendrite, binned by layer (stratum oriens, radiatum,
  lacunosum-moleculare), reported per cell with n cells.
- **Null.** CA3 synapses are distributed across layers in proportion to available
  dendritic length in each layer.
- **Non-claim.** "These data describe where CA3 input arrives. They do not show that
  these synapses store a memory, that they were potentiated, or that they are active
  during recall."

Feedback by error:

- **Endpoint without units or a unit of analysis** ("more connections"). Ask the
  learner to write the figure caption with made-up numbers (the unit's first
  common error).
- **Null is "random."** Ask random with respect to what. Surface area or dendritic length
  is the usual nuisance.
- **Non-claim missing, or the endpoint still says "stores".** The claim is Bin C;
  memory storage needs function or perturbation.

## Unit 02

### U2.1 (U2-1)

(a) Finest to coarsest: **FIB-SEM (4–8 nm) → SBEM (10–20 nm xy) → expansion microscopy
(~25–70 nm effective) → light-sheet (0.5–2 µm) → diffusion MRI (0.5–2 mm).**
(b) Largest to smallest volume: **diffusion MRI (whole human brain) → light-sheet
(whole mouse brain) → expansion microscopy (up to a whole fly brain) → SBEM
(~10⁶–10⁷ µm³) → FIB-SEM (~10⁵–10⁶ µm³).**

Together: the second ordering is the reverse of the first. That is the tradeoff
triangle; resolution is bought with volume or throughput. Credit a learner who notes
that the 1 mm³ multibeam and multi-TEM volumes bent the curve by parallelizing
acquisition.

Feedback by error:

- **Expansion microscopy placed finer than SBEM.** Its effective resolution is
  tens of nanometers; SBEM's xy pixel is 10–20 nm. Ask for the numbers from the chart.
- **Correct orders, no interpretation.** Ask which two corners of the triangle each
  modality bought.

### U2.2 (U2-2)

(a) **Light-sheet LM with a bulk tracer, ~1 µm.** The question is about axon
bundles, not synapses. The coarser step, MRI, cannot see axons at all, and
tractography has no direction.
(b) **EM** (serial-section or SBEM at tens of nanometers or finer). A symmetric synapse
is called from cleft, vesicles and a thin postsynaptic density; confocal at 200–300 nm
cannot resolve any of them and would report only overlap.
(c) **Diffusion MRI, ~1–2 mm.** Only it works in living humans. There is no coarser step
that still resolves a pathway; the limit to state is that a streamline is a model output,
not an observed axon.

Feedback by error:

- **EM for (a).** Ask what the analysis unit is. The rule is the *coarsest* scale that
  works; EM multiplies data and proofreading by about a million per voxel of tissue.
- **Confocal for (b) "with a synaptic marker."** A marker can place a puncta near a
  segment; it cannot show symmetric morphology. Accept it only if the learner changes
  the endpoint to marker puncta and says so.

### U2.3 (U2-3)

Skeletons: 0.1–5 MB × 450 = **45 MB to 2.25 GB**. Meshes: 10–100 MB × 450 = **4.5 to
45 GB**.

The endpoint needs **meshes**: spine head volume is surface geometry. The **graph**
discards all geometry; the **skeleton** discards spine head shape and maps spines onto
the shaft. Archive the **volume** (labeled voxels) or keep access to it, since any merge
or split question returns to the voxels.

Feedback by error:

- **Skeleton chosen because it is small.** Ask what a skeleton keeps of a spine head.
- **450 GB to 45 TB for meshes.** A MB-to-GB slip; 1 GB = 1,000 MB.
- **Nothing archived.** Point to the rule: keep the next-richer representation.

### U2.4 (U2-4)

(a) **4.2 µm, the held-out residual.** The 2.3 µm figure measures how flexibly the
transform fits its own anchors, not its accuracy.
(b) 52 / 400 = **13%**.
(c) Where the local residual (18 µm) exceeds soma spacing (~12 µm), a trace can be
assigned to the wrong cell. Exclude the corner or add anchors there and refit; do not
force matches. Report the number excluded (52 if excluded) or marked ambiguous, and the
residual distribution with its maximum, not only the mean.

Feedback by error:

- **2.3 µm reported.** Ask what the fit never saw.
- **"13% is small, keep them."** Ask what fraction of those 52 could be swapped with a
  neighbor. The error is not random; it is concentrated where the claim is weakest.

### U2.5 (U2-4)

Script: √(300² + 400² + 50²) = √252,500 ≈ **502.5 voxels × 4 nm ≈ 2,010 nm**.
True: offsets are 1,200, 1,600 and 2,000 nm, so √8,000,000 ≈ **2,828 nm**.
Ratio true/script ≈ **1.41**. Treating z as 4 nm when it is 40 nm **underestimates**
any distance with a z component, so distance-based measurements are biased low, and
most for structures running through the stack.

Feedback by error:

- **2,000 nm.** The learner dropped z. That is the same bug in a different form.
- **Multiplied every axis by 40.** Ask for the xy spacing.

### U2.6 (U2-5)

1. **Leakage.** Millimeter-scale streamlines cannot show synapses or which cells connect.
2. **Sound.** Projection presence at micrometer resolution; it does not claim synapses.
3. **Leakage.** At confocal resolution touching is overlap, not synapse (Peters' rule).
4. **Leakage, twice.** "Throughout cortex" extends a 0.1 mm³ sample (sampling); "silence"
   is a functional claim from morphology. The sound version: "In this volume, Kite
   cells form symmetric synapses on axon initial segments."
5. **Sound.** It reports projection presence per cell, which is what barcoding
   measures. It would leak if it said "form synapses in both areas."

Feedback by error:

- **5 marked leakage.** Ask what the method measures. The claim stays inside it.
- **4 marked leakage only for function.** Ask what volume the data came from.

## Unit 03

### U3.1 (U3-1)

(a) **Fixation**: incomplete perfusion, so fixative did not reach tissue near those
vessels.
(b) **Staining**: precipitate, often lead carbonate, from the staining chemistry.
(c) **Dehydration and embedding** (too-rapid dehydration or poorly infiltrated resin),
with sectioning stress as the other candidate. Accept either with the reason.
(d) **Fixation**: delayed fixation or ischemia before the fixative arrived.

Feedback by error:

- **(b) as "debris."** Debris is usually out of focus and irregular in size. Ask what
  chemistry leaves dark particles.
- **(d) as a staining failure.** Weak staining thins membranes; it does not swell
  processes. Ask what arrests swelling.

### U3.2 (U3-2)

(a) **Charging**, from a non-conductive surface; follows **block position** (the
resin-rich region) and scan direction.
(b) **Curtaining**, from uneven milling; follows the **milling geometry** (processing
of the block face).
(c) **Beam or detector drift, or focus drift**; follows **acquisition time**. The
recovery after service is the tell.
(d) **Section-to-section misalignment**; follows **processing** (the alignment step),
not anatomy. It is correctable by re-running alignment.

Feedback by error:

- **(c) as staining gradient.** A staining gradient follows block depth in every
  section, not the clock. Ask what per-tile timestamps would show.
- **(d) as a lost section.** Nothing is missing; everything is shifted. Ask whether a
  process disappears or moves.

### U3.3 (U3-3)

Labels: (a) **data loss**; (b) **data loss**, but routinely bridged; (c) **labor**
(splits); (d) **labor, high** (merges); (e) **labor, low**.

Scattered-loss rate: 9 / 30,000 = **0.03%**. Gap in (a): 3 × 40 = 120 nm of missing
tissue, **160 nm between surviving neighbors**.

Ranking: **(a) > (d) > (c) > (b) > (e)**. Accept (d) above (a) if the learner's
endpoint lives mainly in the bottom third and says so. The consecutive loss breaks the
volume at one z plane; weak contrast raises the merge rate across a third of the block
and cannot be fixed by re-imaging; chatter adds splits, which are visible and
proofreadable; scattered single losses are normal operating loss.

Feedback by error:

- **(b) ranked above (a) because 9 > 3.** Distribution matters more than count.
- **(d) labeled data loss.** The data are there; the boundaries are hard to find. It
  costs labor, heavily.
- **Gap given as 120 nm.** That is the missing tissue; the neighbors are one more
  section apart.

### U3.4 (U3-4)

(a) 600,000 / 8 × 500,000 / 8 = 75,000 × 62,500 = **4.6875 × 10⁹ px per section**;
300,000 / 30 = **10,000 sections**; total **4.6875 × 10¹³ px**.
(b) 4.6875 × 10¹³ / 5 × 10⁷ = 937,500 s ≈ **10.9 days** continuous; / 0.7 ≈ **15.5 days**.
(c) SNR scales with the square root of dose, so twice the SNR at fixed current needs
about 4× the dwell: **≈ 62 days** at 70% uptime. Left out: sectioning, QA,
re-imaging failed sections, and any added beam damage or charging from the higher dose.

Feedback by error:

- **Doubled the time for twice the SNR.** SNR goes as √dose.
- **Divided by 0.7 twice, or multiplied by 0.7.** Uptime lengthens the calendar time.
- **Off by 10³.** 0.05 gigapixels per second is 5 × 10⁷, not 5 × 10¹⁰.

### U3.5 (U3-5)

- **Membrane CNR:** (6.0 − 4.5) / 6.0 = **25% drop**, above the 20% gate. **Stop**;
  check the staining batch and beam conditions.
- **Alignment residual:** 1.4 voxels exceeds 1 voxel. **Re-run alignment** before
  ingesting.
- **Cumulative lost sections:** 0.4% is below 1%, and none are consecutive. No action;
  log it.
- **Fold area:** 7% on section 812 exceeds 5%. **Flag the section**; re-cut if the
  block allows.

A model report: "Labor: membrane contrast has fallen 25% from baseline, which will raise
the merge rate; acquisition is paused until the staining batch and beam are checked,
and alignment will be re-run (99th-percentile residual 1.4 voxels) before ingest. Data
loss: 0.4% of sections lost, none consecutive, plus a 7% fold on section 812, which is
masked and flagged."

Feedback by error:

- **One overall quality score.** It hides the labor/data-loss distinction the team
  needs.
- **"CNR dropped 1.5."** Give the drop relative to baseline; the gate is a percentage.
- **Thresholds changed after seeing the log.** A threshold set after the data is not a
  threshold.

## Unit 04

### U4.1 (U4-1)

(a) **Ingest.** (b) **Stitching and alignment.** (c) **Boundary/affinity prediction.**
(d) **Supervoxel generation.** (e) **Synapse detection.**
(f) **Boundary/affinity prediction**: block-boundary seams, because blocks did not
overlap enough. The fix is more overlap plus blending, then re-running downstream
stages for the affected region. The tell is that the errors follow the processing grid.
(g) 0.05 × 12,000 = **600 voxels**; 600 × 4 nm = **2.4 µm**.

Feedback by error:

- **(d) as agglomeration.** Agglomeration groups supervoxels into objects; it does not
  create the fragments.
- **(f) as an imaging seam.** Tile seams follow the tile size in the raw images. Ask
  whether 512 voxels is a tile or a processing block here.
- **(g) 0.6 µm or 24 µm.** A unit slip; 600 × 4 nm = 2,400 nm.

### U4.2 (U4-2)

(a) A merge **adds an edge** between supervoxels in the graph; a split **removes edges**
by finding a minimum cut between two points. Each is an entry in the append-only edit
log, with author and timestamp. No voxels are rewritten.
(b) **Zero** with supervoxel IDs; the rows are resolved to the new root at query time.
**2,400** with root IDs (plus the rows of any other object whose root changed).
(c) Supervoxel design: the old copy stays correct; it needs resolving against a stated
version. Root-ID design: the old copy is silently wrong for every edited object.

Feedback by error:

- **"The segmentation volume is rewritten."** That is the naive design the graph
  replaces. Ask what an object is in the graph (a connected component).
- **3 × 10⁸ rows.** Only rows on the edited objects change under the root-ID design.

### U4.3 (U4-3)

(a) 119 + 21 × 2 + 10 / 2 = 119 + 42 + 5 = **166** current roots.
(b) Changed: 21 + 10 = 31 of 150 = **20.7%**. One-to-one: 119 / 150 = **79.3%**.
(c) **Query the old version directly.** Mapping forward gives today's objects, which
differ for 31 of the IDs. The methods state the version, the timestamp, the lineage
counts (119 / 21 / 10) and the query code.

Feedback by error:

- **150 current roots.** Splits add roots and merges remove them.
- **"Map forward and use today's counts" for exact reproduction.** That answers a
  different question; report both only if the difference is explained.

### U4.4 (U4-4)

Missing: the **materialization version** (or timestamp), the **root ID as of that
version**, the **query code** (commit hash) and client or package version, the
**filters** (synapse score threshold, autapse handling, any size cut), and the
**date** of the query. "In March" is not a version.

Rewrite: "Querying materialization version [V] of the Lark dataset (root ID [ID] as of
[V]) with [code, commit hash; client version], keeping synapses with [filter], cell 4417
receives 1,204 input synapses (query run [date])."

Feedback by error:

- **Only "add the date."** Two versions can bracket one date. Ask which version the
  date corresponds to.
- **Filters left out.** Two analysts with different score thresholds get different
  counts from the same version.

### U4.5 (U4-5)

(a) 500,000 / 8 × 400,000 / 8 × 250,000 / 40 = 62,500 × 50,000 × 6,250 =
**1.953125 × 10¹³ voxels ≈ 19.5 TB** raw.
(b) Pyramid: × 4/3 ≈ **26.0 TB**. Three affinity channels: 3 × 19.5 ≈ **58.6 TB**.
(c) 1.953 × 10¹³ / 10⁷ ≈ 1.95 × 10⁶ GPU-seconds ≈ **22.6 GPU-days** per pass;
**≈ 90.4 GPU-days** for four.
(d) 600 × 5 = **3,000 person-hours ≈ 1.875 annotator-years**.
(e) **Proofreading labor** is dominant: it is a hiring, training and quality problem,
not a vendor line item. Delete the **affinity maps** after supervoxel generation, once
you are confident you will not re-agglomerate. Move the raw archive to cold storage;
never delete it.

Feedback by error:

- **Affinity maps treated as permanent.** They are the largest recomputable item.
- **Raw archive deleted to save money.** It is the only irreplaceable asset.
- **"GPU is the dominant cost."** Compare 90 GPU-days with nearly two annotator-years
  of skilled work, before review and retraining.

## Unit 05

### U5.1 (U5-1)

(a) **Astrocyte**: glycogen granules, near-diagnostic.
(b) **Not axon; probable dendrite (or soma-proximal process).** Ribosomes rule out
axon, a near-diagnostic exclusion; microtubules are only consistent.
(c) **Probably axon**, carrying the vesicle in transit, or a peptidergic terminal
elsewhere. One dense-core vesicle without a cluster is consistent, not diagnostic.
(d) **Myelinated axon**, near-diagnostic.
(e) **Axon initial segment**: the undercoating plus fasciculated microtubules, 20–60 µm
from the soma. Near-diagnostic.

Feedback by error:

- **(b) "dendrite, high confidence."** Ribosomes exclude axon; they do not by
  themselves exclude a soma-proximal process or confirm a spine-bearing dendrite.
- **(c) "presynaptic terminal."** No cluster at an apposition, so no terminal call.

### U5.2 (U5-2)

(a) **Synapse.** All three criteria plus persistence.
(b) **Not a synapse.** An adherens junction: symmetric densities and no vesicle pool
(criterion 1 fails).
(c) **Not a synapse.** Criterion 2 fails (non-uniform gap) and criterion 3 fails (no
density).
(d) **Check further, probably a synapse.** A face-on PSD appears on only one or two
sections; do not reject it for short persistence. Confirm from a neighboring plane or a
reslice.

PSD 280 nm edge-on at 35 nm: 280 / 35 = **8 sections**. An edge-on candidate on one
section is one sample of something that should give about eight: most likely a
tangential membrane or precipitate.

Feedback by error:

- **(d) rejected for persistence.** Ask which way the PSD lies in the section plane.
- **(b) called as a symmetric (type II) synapse.** Type II still needs vesicles.
- **About 11 sections.** The learner used 25 nm; check the stated thickness.

### U5.3 (U5-3)

1. **Needs the assumption named.** Asymmetric morphology on a spine is a strong
   association with excitation, not an identity. Write "putatively excitatory
   (asymmetric)".
2. **Licensed as written.** The assumption is named.
3. **Not licensed.** Vesicle shape is partly a fixation artifact; it supports the
   inference, it does not prove transmitter identity.
4. **Licensed as a structural statement, and the strongest of the five.** Presynaptic
   cell type usually corroborates sign better than morphology. "Inhibitory" still needs
   "putatively" unless transmitter identity is measured.
5. **Not licensed.** Neuromodulatory terminals do not fit the type I/II dichotomy.

Feedback by error:

- **4 as "needs assumption."** Accept if the learner says the sign is still inferred.
- **5 as licensed.** Ask what a dense-core vesicle tells you about the terminal.

### U5.4 (U5-4)

(a) **Medium.** One strong cue (ribosomes) from one family (organelles); microtubules
and mitochondria are consistent, not independent evidence; continuity checked on only
2 sections.
(b) **Medium.** Presence and shape of vesicles are not independent; both depend on
seeing vesicles. Partner unclear.
(c) **High.** Organelles (ribosomes), geometry (a spine) and synaptic role (incoming
asymmetric density) agree; continuity across ≥ 3 sections.
(d) **Uncertain.** Cues conflict and the decisive region is in a fold.

Zero uncertain calls in 240: the annotator is forcing labels. A calibrated annotator
has some uncertain calls, and the uncertain set is the review queue. Track the rate as a
calibration statistic, not a penalty.

Feedback by error:

- **(b) high because "two cues."** Two cues from one family are one cue.
- **(a) high because ribosomes are strong.** One strong cue is medium by definition.
- **"Zero uncertain means a good annotator."** Ask how a reviewer would find their
  errors.

### U5.5 (U5-5)

(a) (60 − 14) / 60 = 46 / 60 ≈ **76.7%**.
(b) The 9 contrast-only calls and the 3 adherens junctions lack a vesicle cluster:
12 / 14 ≈ **85.7%**.
(c) The annotator over-trusts **dark contrast at a membrane** and does not check
criterion 1. Protocol change: require the annotator to mark the vesicle cluster at the
apposition before a synapse can be saved. The remaining 2 errors (2 / 14 ≈ 14.3%) call
for a scroll check on persistence.

Feedback by error:

- **Precision 14 / 60.** That is the false-discovery rate, 23.3%.
- **9 / 14.** The adherens junctions also have no vesicle pool.
- **"Be more careful."** Not a protocol change; a reviewer cannot check it.

## Unit 06

### U6.1 (U6-1)

(a) **Uncertain.** Step 1: no synapse. Step 2: no ribosomes, but at 170 nm absence is
weak evidence. Step 3: no myelin. Step 4: no beading, no taper, no spine. Step 5:
record the missing cue and route to review.
(b) **Dendrite, high.** Step 2 (ribosomes) plus step 4 (a spine): two families.
(c) **Axon, high.** Step 3 (fiber bundle, context).
(d) **Axon initial segment receiving a synapse, high.** Step 1 sends a PSD to the AIS
check; undercoating plus fasciculated microtubules 20–60 µm from a soma settles it.

Feedback by error:

- **(a) axon because thin and no ribosomes.** Caliber and absence are the two cues the
  unit warns about. Ask whether a ribosome would be visible at 170 nm.
- **(d) dendrite.** "PSD ⇒ dendrite" applied mechanically; this is exception 2.

### U6.2 (U6-2)

The four: **dendro-dendritic synapses**, **axo-axonic synapses** (onto the AIS),
**presynaptic dendrites in retina** (amacrine cells), and **invertebrate neurons** with
mixed input and output on one neurite.

(a) **Safe default** (hippocampus is well-behaved), with the AIS check still in place.
(b) **Not safe**: dendro-dendritic reciprocal synapses.
(c) **Not safe**: invertebrate neurons; assess polarity synapse by synapse.
(d) **Not safe**: interneuron presynaptic dendrites.

Feedback by error:

- **Axo-axonic left out.** It exists in cortex too, which is why the AIS check is part
  of step 1 everywhere.
- **Decided per image.** The tissue question belongs in the protocol, answered once.

### U6.3 (U6-3)

(a) A one-way connection appears reciprocal when at least one synapse is reversed and
at least one is not: 1 − 0.9³ − 0.1³ = 1 − 0.729 − 0.001 = **0.27**.
(b) 400 × 0.27 = **108**.
(c) Two synapses: 1 − 0.9² − 0.1² = **0.18**. One synapse: **0**; a single flip reverses
the edge but cannot make it reciprocal.
(d) "Direction errors are a bias, not noise: reversing some synapses in multi-synapse
connections manufactures reciprocal pairs, pushing the measured rate up. The measured
enrichment may be partly made of our errors, so we should re-run on high-confidence
edges and simulate our measured error rate."

Feedback by error:

- **0.1 or 0.3.** The learner counted one flip only, or multiplied 3 × 0.1. Ask what
  happens when all three flip (the edge reverses, still one-way).
- **(c) one synapse gives 0.1.** A reversed single-synapse edge is B→A only.
- **Accepting "only noise."** Ask which way the error pushes this statistic.

### U6.4 (U6-4)

(a) High **13 / 16 = 81.3%**. Medium **7 / 9 = 77.8%**. Uncertain best guess **3 / 5 =
60%**. Overall **23 / 30 = 76.7%**; on committed calls, 20 / 25 = 80%.
(b) **No, overconfident.** High-confidence accuracy is below about 90% and barely above
medium; the tiers carry little information.
(c) **Caliber** (4 of 5). The other error is the AIS exception: a PSD on an axon initial
segment read as dendrite.

Feedback by error:

- **Overall accuracy only.** Ask what a downstream reviewer can trust.
- **"80% overall, proficient, done."** The unit's rubric puts calibration above raw
  accuracy.

### U6.5 (U6-5)

Two checkable rules (others earn credit if specific and checkable):

1. "When caliber is the only available cue, mark the call uncertain and record
   'caliber only'."
2. "Before calling dendrite from a PSD, record whether the process has an undercoating
   and fasciculated microtubules within 60 µm of a soma; if yes, call AIS."

A rule that fails: "Be careful with thin processes." A reviewer cannot tell from the
record whether it was followed.

Feedback by error:

- **Rules restate cues** ("thin processes are often axons"). A rule says what to do.
- **Rule targets a cue that caused no errors.** Tie the rule to U6.4's tally.

## Unit 07

### U7.1 (U7-1)

(a) **Oligodendrocyte**: the darkest nucleus in the field, small and round, with a myelin
link.
(b) **Astrocyte**: glycogen granules, with a pale irregular nucleus.
(c) **Microglia**: dense elongated nucleus with peripheral heterochromatin, plus
lysosomal content.
(d) **OPC candidate: flag, do not force.** Record the evidence for and against (nucleus
intermediate in density, no myelin link, neuronal features not seen). Do not write
"OPC, not sure": OPC is a class, uncertain is a confidence.

Feedback by error:

- **(d) oligodendrocyte.** Ask for the comparison with the oligodendrocyte in the next
  field.
- **(c) oligodendrocyte on nucleus darkness alone.** Check shape and cytoplasm.

### U7.2 (U7-2)

**Tern: astrocytic process, medium-high** (step 4, space-filling contour over 5–10
sections). **Egret: neurite, high**; the vesicle cluster (step 2, synaptic
participation) settles it, and the tube shape agrees. The cue that survives poor
staining is **cross-sectional shape**: space-filling versus tube.

Feedback by error:

- **Both uncertain because granules are not visible.** Absence of granules is weak
  evidence, and shape is still available.
- **Egret neurite at medium.** Before the ninth section, yes; synaptic participation
  makes it high.

### U7.3 (U7-3)

(a) 38 × 0.9 = 34.2, about **34 false inputs**; 34 / 610 ≈ **5.6%** inflation (644
total).
(b) Before: 120 / 610 ≈ **19.7%**. After: (120 + 34) / 644 ≈ **23.9%**.
(c) **Toward more local structure**: higher clustering, inflated short-range
connectivity. The false inputs come from the cell's neighbors, because that is where
the astrocytic process ran. The bias points toward the interesting result.

Feedback by error:

- **"5.6% is small, it's noise."** The added inputs are all local; ask what they do to
  the local fraction.
- **After-fraction as 154 / 610.** The denominator grows too.

### U7.4 (U7-4)

Ranking: **(a) > (d) > (c) > (b) ≈ (e)**. (a) adds about 30 false, local inputs to an
analysis cell; it goes above conspicuous splits. (d) is a real but small loss on an
analysis cell. (c) matters only through that cell's outputs onto the 40, if any.
(b) is conspicuous but outside the endpoint. (e) affects astrocyte morphometry, not
this endpoint.

Feedback by error:

- **(b) first because it is obvious.** The unit's rule: rank by effect on the endpoint,
  not conspicuousness.
- **(c) ignored entirely.** Accept a low rank; ask whether that cell synapses onto
  the 40.

### U7.5 (U7-5)

(a) Correct: 6 + 9 + 5 + 3 + 4 + 2 = 29. Overall **29 / 40 = 72.5%**. Committed calls:
40 − 4 uncertain = 36; **29 / 36 ≈ 80.6%**.
(b) **Astrocytic process called neurite (3).** The annotator under-weights shape and
space-filling. This is the merge-generating error, the costly direction. The next
largest is oligodendrocyte ↔ microglia (3 in total), which suggests reliance on "dark
nucleus" without checking shape and cytoplasm.
(c) **Not yet** on accuracy (72.5% overall, below 80%). **Not yet** on asymmetry:
astrocyte → neurite (3) exceeds neurite → astrocyte (1). The OPC uncertain calls are
appropriate flags, not failures.
(d) Ten fresh astrocytic-process versus thin-neurite patches, as short z-stacks, and
only that confusion.

Feedback by error:

- **Accuracy 29 / 36 reported as the overall score.** Report both, with denominators.
- **Re-drill the whole set.** Targeted repetition on the dominant cell is the point.
- **OPC-uncertain treated as the main problem.** Flagging OPC is the protocol's
  instruction.

## Unit 08

### U8.1 (U8-1)

Ranking: **(a) > (c) ≈ (d) > (b) > (e)**. (a) is a merge that changes presynaptic
identity: another type's synapses are counted as Gannet's, silently. It is also the
hardest to detect, because the object still looks like an axon. (c) and (d) bias counts
directly; missed synapses fall unevenly by size, and false ones weigh most on
one-synapse connections. (b) loses Gannet synapses, but visibly: the axon stops in
mid-neuropil. (e) matters only if the fragments carry Gannet synapses onto the layer 4
cells.

Feedback by error:

- **(b) first because a large piece is lost.** Size ranks within type, not across.
  A visible truncation is bounded.
- **(d) marked easy to detect.** You are looking for absence; it needs a sampled
  audit.

### U8.2 (U8-2)

(a) Q's total is (1.07 − 0.94) / 1.07 ≈ **12.1%** lower; its merge component grew
0.34 / 0.12 ≈ **2.8×**. **Do not ship on total VI.** Merges are the expensive error;
recompute the endpoint on a fixed set of neurons and check ERL first.
(b) ERL = (40² + 25² + 15² + 10² + 10²) / 100 = 2,650 / 100 = **26.5 µm**. Before
comparing: whether the implementation penalizes merges (the common convention gives a
merged segment zero run length), and the ground-truth set it was measured on.

Feedback by error:

- **ERL 20 µm (the mean run).** ERL weights each run by its length, because a random
  point is more likely to fall in a long run.
- **"Q is better, ship it."** Ask for the merge column.

### U8.3 (U8-3)

A defensible order: **R (12) and P (25)** first, since both corrupt the endpoint
(R scrambles presynaptic identity; P adds false local inputs). Then **Q (8)**, a large
but visible, bounded split on an analysis cell. Then **S's partner check (2)**; fix S
only if it touches the set. Then **T (3)**. Total 12 + 25 + 8 + 2 + 3 = **50 minutes**.
Left undone: fixing S, unless the check finds synapses onto the set, in which case it
displaces T.

Feedback by error:

- **S fixed first because it is conspicuous.** Conspicuousness is not a factor.
- **S dismissed without the check.** Two minutes of checking is part of triage.
- **Q before P because it is cheaper.** Cost matters per unit of endpoint change;
  silent corruption outranks a visible truncation.

### U8.4 (U8-4)

(a) **(ii)** is checkable: it is stated in advance, measurable and tied to the
endpoint. (i) has no measurable condition. (iii) becomes usable with declared coverage:
"Proofread to L2 on as many cells as the budget allows; report each cell's level; make
no claims about cells below L2."
(b) 2.40 → 2.31: change (2.40 − 2.31) / 2.40 = **3.75%**, below 5%: **stop**.
2.40 → 2.22: **7.5%**, above 5%: **continue**.

Feedback by error:

- **(iii) accepted as is.** A budget is a reason to stop, not a claim about quality.
- **Change computed against 2.31.** Accept if stated; the tolerance is relative to the
  first-pass value in the unit's wording.

### U8.5 (U8-5)

(a) Mean **4.5 h**, median **4.25 h**, range **2.5–7.0 h**. The **mean** drives the
total, because hours add; the median understates a right-skewed cost.
(b) 180 × 4.5 = **810 h**; second pass on 27 cells = **121.5 h**; exhaustive check,
20 × 9 = **180 h**. Total **1,111.5 h**.
(c) 1,111.5 / 5 ≈ **222 annotator-days**.
(d) Any two: 8 pilot cells is a small sample; pilot cells may not represent the set
(size, location near artifacts); annotators slow down with fatigue and speed up with
practice; rework after verification is not included. Defend it by stating the pilot,
giving a range (180 × 2.5 to 180 × 7.0 = 450 to 1,260 h for the base alone), and
re-estimating after the first 20 production cells.

Feedback by error:

- **Median used for the total.** Ask what the sum of 180 cells depends on.
- **No verification or endpoint check budgeted.** They are part of the job, not
  overhead.
- **Days at 8 hours.** Accept if stated; the unit treats fatigue as a data-quality
  variable, so bounded blocks are the better assumption.

## Unit 09

### U9.1 (U9-1)

(a) ≥ 1: **3,250**; ≥ 2: **1,150**; ≥ 3: **450**. Removed at ≥ 3: 2,800 / 3,250 ≈
**86.2%**.
(b) Kite: 60 / 360 ≈ **16.7%** survive at ≥ 2, against 1,150 / 3,250 ≈ **35.4%** overall.
The threshold removes Kite's connections at more than twice the average rate, so a
type-level comparison would under-state Kite's connectivity. Report the threshold and
re-run the headline at a second one.
(c) Node definition; weighted or binary (and which weight); how direction was called;
inclusion criteria (for example, proofreading level); boundary handling; plus the
materialization version and synapse-confidence cutoff.

Feedback by error:

- **≥ 2 edge count 700.** Connections with three or more synapses also pass ≥ 2.
- **Threshold treated as a technical detail.** Point to (b): it is non-uniform across
  types.

### U9.2 (U9-2)

(a) p = 790 / (80 × 79) = 790 / 6,320 = **0.125**. Expected = 0.125² × 3,160 =
**49.375**. Observed/expected = 118 / 49.375 ≈ **2.39×**.
(b) 118 / 96 ≈ **1.23×**; z = (118 − 96) / 9 ≈ **2.44**.
(c) 118 / 109 ≈ **1.08×**; z = (118 − 109) / 10 = **0.9**.
(d) (96 − 49.375) / (118 − 49.375) = 46.625 / 68.625 ≈ **67.9%** of the excess.
Conclusion: "Reciprocity is consistent with what degree and spatial proximity predict;
we find no evidence of additional reciprocal wiring." The Erdős–Rényi ratio should not
be reported as the result.

Feedback by error:

- **p = 790 / 6,400.** Self-loops are excluded: N(N − 1), not N².
- **Expected = p × N(N − 1)/2.** A reciprocal pair needs both directions: p².
- **Reporting 2.39× "p < 0.001" as the finding.** Ask what the Erdős–Rényi null fails
  to preserve.

### U9.3 (U9-3)

(a) **6** below 0.05. Expected false positives: 16 × 0.05 = **0.8**.
(b) Bonferroni threshold 0.05 / 16 = 0.003125: **2** survive (0.0004, 0.0021).
(c) BH: compare the k-th smallest p with (k / 16) × 0.05. k = 4: 0.011 ≤ 0.0125, yes;
k = 5: 0.019 > 0.015625; no larger k passes. **4** survive.
(d) Triad counts are strongly dependent (one edge changes many triads), and permutation
respects that dependence. Report that 16 tests were run, including the ones not shown,
the correction used and the null the permutations preserved.

Feedback by error:

- **BH stops at the first failure scanning upward.** Accept here (the answer is the
  same), but the rule is the largest k that passes.
- **"Six enriched motifs."** Ask how many tests were run.

### U9.4 (U9-4)

(a) 4 × 3 = **12** new partner pairs. With 2 of them connected, **2** triangles pass
through the merged object. Without such connections the merge creates open wedges, not
triangles; it can also collapse edges or create a dropped self-loop, so the sign of the
bias depends on the motif and the graph rules.
(b) **No.** The band (0.97–1.36) crosses the null of 1.0, so the result does not survive
the project's own measured error rate. The band shows the spread under that error model
only; it is **not** a calibrated confidence interval.

Feedback by error:

- **(a) 7 pairs.** The learner added the sets; pairs multiply.
- **"Errors only make it conservative."** The unit's point: you cannot assume a
  direction. Model it.
- **Band read as a 90% confidence interval.** It holds only if the error model is right.

### U9.5 (U9-5)

1. **Defensible.** This is the strongest current result type.
2. **Overclaim.** Synapse count is a proxy for strength, not a weight; sign, dynamics,
   plasticity and neuromodulation are absent.
3. **Dismissive underclaim.** Fly visual-system models constrained by the connectome
   predicted responses that were compared against recorded activity (Lappalainen et al.
   2024, cited in the unit).
4. **Defensible.**
5. **Overclaim.** A runnable brain from a connectome is not on the near horizon.

Feedback by error:

- **3 as defensible.** Ask the learner to check the unit's §5 example.
- **1 as overclaim.** It says what the connectome removes, not that the model is right.

Teaching material: CC BY 4.0, NeuroTrailblazers.
