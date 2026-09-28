---
layout: page
title: "MICrONS Visual Cortex"
permalink: /content-library/case-studies/microns-visual-cortex/
image: /assets/images/content-library/case-studies/microns-visual-cortex.svg
image_alt: "Stylized vector art: a specimen ring with landmark points beside a data band."
description: >
  Case study of MICrONS (Machine Intelligence from Cortical Networks), which
  paired two-photon calcium imaging of about 75,000 excitatory neurons with an
  electron microscopy reconstruction of about 1 mm³ of the same mouse's visual
  cortex. It covers how the two coordinate frames were co-registered, how a
  calcium-imaged cell is matched to an EM soma, and what the calcium data do and
  do not license you to claim.
topics:
  - functional connectomics
  - mouse visual cortex
  - calcium imaging
  - co-registration
  - multi-modal neuroscience
  - structure-function correlation
  - deep learning segmentation
  - cortical circuitry
primary_units:
  - "01"
  - "03"
  - "04"
  - "08"
  - "09"
difficulty: intermediate
tags:
  - case-studies:MICrONS
  - connectomics:dense-reconstruction
  - connectomics:functional-connectomics
  - imaging:electron-microscopy
  - imaging:calcium-imaging
  - cell-types:pyramidal-cell
  - cell-types:interneuron
  - neuroanatomy:visual-cortex
  - methodology:structure-function
micro_lesson_id: ml-case-microns
combines_with:
  - h01-human-cortex
  - mouseconnects-himc
  - flywire-whole-brain
use_layout_hero: false
content_type: core
---

# MICrONS Visual Cortex

> ### Before you quote a number from this page
>
> Every figure below (cell counts, synapse counts, match counts, proofreading
> coverage) is a property of **a particular release** of this dataset, not of
> the tissue. Releases are re-segmented, re-proofread and re-materialized, and
> the numbers move when they are. The counts on this page are the ones printed
> in the 2025 *Nature* papers; the live tables have changed since.
>
> This page does not pin a version, because it would be stale within months and
> you would inherit a wrong number with a citation attached. Treat what follows
> as orientation. Before any figure reaches a paper, a talk or a grant, pull it
> from the release you are analyzing and record the version alongside it.
> [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
> covers how; [Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
> has the lab; the [MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }})
> is a worked, version-pinned example that needs no account.


## Overview

The Machine Intelligence from Cortical Networks (MICrONS) program built a
millimeter-scale connectome of mouse visual cortex and paired it with functional
recordings from the same tissue. It was funded by the Intelligence Advanced Research
Projects Activity (IARPA) as part of the BRAIN Initiative. Its question was short:
does the way neurons are wired predict what they do?

The volume is about 1 mm³ of one male mouse's visual cortex (1.3 × 0.87 × 0.82 mm in
vivo), centered on the junction of primary visual cortex (VISp) and three higher visual
areas (VISlm, VISal and VISrl). It was imaged at about 4 nm per pixel in sections 40 nm
thick. The reconstruction contains more than 200,000 cells and about 524 million
synapses (MICrONS Consortium 2025). Before the tissue was prepared for electron
microscopy, an estimated 75,909 excitatory neurons in the same volume were recorded with
two-photon calcium imaging while the mouse watched videos. Recording activity first and
mapping the wiring afterwards is what the field calls "functional connectomics", and
MICrONS is its largest published example.

The hard part is not either measurement. It is the join between them. This page spends
most of its length on that join: how a point in the in vivo optical volume was mapped to
a point in the ex vivo EM volume, how a calcium trace was attached to an EM soma, and
what a matched pair licenses you to say.


## The join is the experiment

A wiring diagram says neuron A makes N synapses onto neuron B. A calcium recording says
neuron A responds to a particular set of movie frames. On their own, each statement lives
in its own coordinate frame, with its own object identifiers. MICrONS made the same
physical neurons appear in both, so that a connectivity question can be asked of cells
whose responses are known: given that A and B respond alike, are they more likely to be
connected than a pair that does not?

That question has a correct null, and the null is anatomical. Two neurons can only be
connected if the axon of one comes close to a dendrite of the other. So the comparison
that matters is not "connected pairs versus all pairs" but "connected pairs versus pairs
whose axon and dendrite came within striking range and did not connect". Only a dense
reconstruction can supply that second group, because it needs the geometry of every
axon and dendrite in the neighborhood, not just the proofread ones. This is the reason
the companion analysis (Ding et al. 2025) is possible in MICrONS and was not possible in
sparser predecessors, and it is the pattern to copy in your own work: state the
anatomical null before you state the functional result.


## Two-photon imaging came first, in one mouse

### What was recorded

The mouse expressed the calcium indicator GCaMP6s in excitatory neurons (Slc17a7-Cre
crossed to Ai162). Imaging used a two-photon random-access mesoscope (2P-RAM) with a
wide field of view. Fourteen scans, out of 19 completed over six days of imaging, are
released; the paper gives their ages as postnatal day 75 to 81, and its Methods timeline
lists imaging from 4 to 9 March 2018 and perfusion on 16 March 2018 (P87). The imaged
volume was about 1,200 × 1,100 × 500 µm (anteroposterior × mediolateral × depth),
covering cortical layers 2 to 5, and was placed so that about half of it was VISp and
half higher visual areas (MICrONS Consortium 2025, "2P calcium imaging" and Methods).

Each scan tiled the field of view with overlapping 620 µm-wide fields at several depths.
Eleven scans imaged four planes spread across 300 to 400 µm of depth at 6.3 Hz; two scans
ran at 8.6 Hz and one at 9.6 Hz with fewer, more closely spaced planes. Scans were placed
at 10 to 15 µm depth increments across days to cover the volume, and the site was
re-found each day using horizontal blood vessels and the pattern of somata, which show up
as dark spots where GCaMP6s is excluded.

Somata were segmented from each scan by constrained non-negative matrix factorization
(CaImAn) and the fluorescence traces were deconvolved into estimates of spiking. A
classifier removed masks that were not somata (8.1% of masks). The mouse was head-fixed
on a treadmill with the stimulus in its left visual field, and treadmill speed, eye
position and pupil diameter were recorded throughout.

### What the mouse saw

Each scan's stimulus lasted about 84 minutes. Sixty-four minutes were 10 s natural video
clips drawn from films, the Sports-1M dataset and a rendered first-person walk through a
virtual environment. Ten minutes each went to two parametric stimuli: Monet2, a smoothed
Gaussian noise movie with coherent orientation and motion in 16 directions, for
orientation and direction tuning; and Trippy, drifting gratings built from smoothed noise
so that spatial frequency and orientation vary locally. Six natural
clips totaling one minute were shown ten times per scan and are conserved across all
scans. These "oracle" trials give a reliability measure for every neuron: the
oracle score is the jackknife mean of the correlation between the leave-one-out average
response and the held-out trial (MICrONS Consortium 2025, Methods, "Stimulus composition"
and "Oracle score").

The oracle score matters for everything downstream. It is the field's proxy for "this
neuron responded reliably to the visual stimulus", and it was used to prioritize which
neurons were matched (MICrONS Consortium 2025, Methods) and which were proofread (Ding et
al. 2025, Methods). A neuron with a
low oracle score is not a neuron without function; it is a neuron whose function this
stimulus set did not capture.

### Units are not neurons

The scans produced 125,413 masks, of which 115,372 were classified as somatic. The
released neuron count is 75,909. The difference is not an error. The same neuron was often
imaged in more than one scan, because scan planes were placed to overlap and the tissue
deformed a little from day to day. Each scan's 2D centroids were registered into a
structural stack and given 3D coordinates, then the closest pairs of masks from different
scans were merged iteratively until every remaining pair was at least 10 µm apart or a
further merge would produce an unrealistically tall object (20 µm in z) (MICrONS
Consortium 2025, Methods, "2P structural stack").

So a "functional unit" or "functional ROI" is one mask in one scan, identified by session,
scan index, field and unit ID. A "neuron" is the estimated physical cell those units
belong to. The co-registration tables are keyed by unit, and one EM neuron can be matched
to several units. Keep the two words apart when you count.


## Co-registration maps an optical volume onto an EM volume

### Why the two frames disagree

Between the last scan and the first EM image, the tissue was perfused with fixative,
sliced, stained with osmium, embedded in resin, trimmed, cut into 27,972 sections and
imaged section by section.
Each step shrinks or warps it, and the warp is not uniform. The EM volume was also
assembled from about 95 million tiles that were stitched and aligned by a separate
pipeline, so it carries its own residual distortions, including systematic ones on the
length scale of knife cleanings and tape changes. The co-registration problem is to find
a smooth transform that carries a point in the 2P structural stack to the corresponding
point in EM, well enough that the right soma is within reach.

### Fiducials and a staged transform

The MICrONS team hand-matched 2,934 fiducials between the EM volume and the 2P
structural stack: 1,994 somata and 942 blood-vessel points, mostly branch points. Below
about 400 µm from the surface, the 2P structural signal is weaker and somata are harder
to identify, so more of the deep fiducials are vascular. Fiducials were placed on a
down-sampled EM volume (256 × 256 × 940 nm voxels), which is coarse enough to make the
somata and vessels visible at once (MICrONS Consortium 2025, Methods, "Transform").

The transform was fit in stages, coarse to fine, so that the last steps only move points
by small amounts. The paper reports the average residual after each stage:

| Stage | What it does | Average residual after |
|---|---|---|
| One second-order polynomial | Scale, rotate and globally warp 2P into EM space | ~10 µm |
| Polynomials per z-bin (5 bins, then 21) | Remove systematic trends along the EM z axis, spaced like knife and tape changes | 5.6 µm, then 4.6 µm |
| Thin-plate splines on grids of 3³, 5³, 10³, 12³ control points | Deformation at successively finer scales | 3.9, 3.5, 3.1, 2.9 µm |
| One thin-plate spline with every fiducial as a control point | Pins the fiducials themselves | 0.003 µm |

The paper's headline figure, given in the Results, is an average residual of 3.8 µm: the
distance between where a fiducial lands after co-registration and where it was placed.
The last stage makes that residual meaningless *at the fiducials themselves*, because it
fits them exactly, so the Methods describe a second measure for how the transform does on
a new point: refit it 2,933 times, each time leaving one fiducial out, and evaluate the
residual at the left-out point (MICrONS Consortium 2025, "Functional–structural
co-registration" and Methods, "Transform"). When you quote 3.8 µm, quote it as the paper's
average residual and cite the section.

What 3.8 µm means in practice: the same paper treats two masks from different scans as
the same neuron when they fall within 10 µm of each other, which is the scale at which
neighboring somata become ambiguous in these data. An error of a few micrometers is small
against that, and large enough that "the nearest EM soma to the transformed point" is not
always the right answer. That gap is why the matching step is separate from the transform.

### Matching a functional unit to an EM soma, by hand

For the manual match, an expert saw both modalities side by side in a custom interface.
The functional side showed the product of the scan's average image and its
pixel-correlation image, which makes somata stand out. The EM side showed imagery and the
nucleus segmentation, resampled to 1 µm³ and pushed through the transform into 2P
coordinates so that the same field could be cut from both volumes. Vessels labeled with
Texas Red in the 2P stack were overlaid on EM vessels to confirm local alignment. The
matcher then compared the constellation of somata around the target, proposed an EM
nucleus, and confirmed it in a modified Neuroglancer on the full-resolution EM (MICrONS
Consortium 2025, Methods, "Assigning manual matches").

The result of that effort was 19,181 functional units from 14 scans matched to 15,439 EM
neurons. The manual table is `coregistration_manual_v4` in CAVE, and the
`microns-explorer.org` co-registration section names the recommended current table.

Every row carries two confidence numbers:

- **Residual**: the distance, in 2P space, between the unit's centroid and the matched EM
  soma's centroid after the transform. Smaller is better.
- **Separation score**: the residual of the nearest EM neuron that was *not* chosen, minus
  the residual of the chosen one. Large positive means the chosen soma was clearly the
  closest candidate. Negative means the matcher overrode the nearest neighbor because the
  imagery said otherwise.

For an independent check, the team took every EM neuron that had been matched in at least
two scans and computed the signal correlation between the two matched units (their
trial-averaged responses to the oracle clips). Matched units were more correlated with each
other than with the nearest non-matched unit in the other scan, and the effect grew when
restricted to units with oracle scores above 0.2 (MICrONS Consortium 2025, Extended Data
Fig. 4). That check does not prove any single match. It shows the population of matches is
enriched for the same cell.

### Matching the rest automatically

Manual matching does not scale to 115,372 units, so the manual table became ground truth
for two automated matchers, both of which end in the same step: transform every EM
neuron's nucleus centroid into 2P space, then solve minimum-weight bipartite matching
between EM centroids and unit centroids (`scipy.optimize.linear_sum_assignment`).

| Automatch | How it registers | Result | Precision vs. manual | After dropping the bottom 30% by separation score |
|---|---|---|---|---|
| Fiducial-based (`coregistration_auto_phase3_fwd`) | The fiducial transform above | 84,198 units → 37,364 EM neurons | 83% | 90%, keeping 59,934 units / 31,042 neurons |
| Vessel-based (`apl_functional_coreg_vess_fwd`) | A multi-scale B-spline registration of the vasculature alone, no fiducials (SimpleITK) | 75,856 units → 34,712 EM neurons | 84% | 90%, keeping 53,248 units / 28,233 neurons |
| Fiducial–vessel agreement | Rows on which both tables agree | 60,091 units → 29,620 EM neurons | 89%, no filtering | — |

Source: MICrONS Consortium 2025, "Functional–structural co-registration" and Extended Data
Fig. 5. Precision here is agreement with the manual matches, computed only on units and
neurons that both methods attempted.

Two things to take from this table. First, a registration built from vessels alone did as
well as one built from 2,934 hand-placed fiducials, which is good news for anyone
planning a similar experiment without a fiducial budget. Second, precision is a knob, not a
property. The tables ship with residual and separation percentiles so that you choose the
trade-off: threshold residual from above and separation from below, and the paper's
heat maps tell you what precision and how many neurons you keep.

### What Ding et al. actually used

The structure-function paper did not use the automatch. It used `coregistration_manual_v4`,
dropped one scan with compromised optics (water ran out from under the objective for
about 20 minutes), and applied two thresholds: residual below 20 and separation score
above −10. Where more than one unit matched a single EM neuron, the unit with the higher
oracle score was used. Their analysis volume is the overlap of the larger EM subvolume and
the 2P volume, about 560 × 1,100 × 500 µm in vivo, in which 43,679 of the 82,247
automatically detected neuronal nuclei were classified excitatory, and 13,952 excitatory
neurons had a manual match (Ding et al. 2025, "MICrONS functional connectomic dataset" and
Methods, "2P–EM matching").

So the population you can ask structure-function questions of is not 75,909 neurons and
not 200,000 cells. It is the manually matched, visually responsive, well-modeled subset
that sits in the overlap of the three volumes. Read the inclusion criteria before you read
the effect sizes.


## What the calcium data license, and what they do not

[Unit 01]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}) sorts every
connectivity claim into three bins: A, structure alone is sufficient evidence; B,
structure plus one declared assumption; C, structure cannot establish this. (The
[Introduction lecture]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }})
teaches the same three bins.) Adding a functional measurement to the same cells moves
some claims out of Bin C. It does not move all of them, and it adds assumptions of its own.

### What a match gives you

A matched pair gives you, for one cell, both a row in the synapse table and a deconvolved
calcium trace under a known stimulus. That is enough to compute:

- **Signal correlation** between two neurons: the correlation of their trial-averaged
  responses to the same clips.
- **Tuning summaries**: orientation and direction preference from Monet2, reliability from
  the oracle trials.
- **Model-derived properties**: Ding et al. fit a deep network ("digital twin") whose
  core was trained on recordings from eight other mice and whose per-neuron readouts were
  fit to this mouse's responses. They used it to predict responses to 250 novel 10 s
  clips, to estimate signal correlations over a larger stimulus set than the mouse saw,
  and to factor each neuron's tuning into a feature component (what it responds to) and a
  spatial component (where its receptive field is).

With those in hand, the structural counts become conditional. "Connected pairs have higher
signal correlation than unconnected pairs whose axon and dendrite came within 5 µm" is a
statistic against a stated null, with a measured functional variable on each side. It is as
close to Bin A as a structure-function claim gets.

### The assumptions you inherit

Each functional variable rests on assumptions that a structural count does not carry.
Name them in the same sentence, the way Unit 01 asks you to name a Bin B assumption.

1. **The match is right.** Residual and separation score are per-row confidence; a
   population-level enrichment check is not a per-cell guarantee. Report the thresholds
   you used.
2. **Deconvolved calcium is a proxy for spiking.** GCaMP6s fluorescence was sampled at
   6.3 to 9.6 Hz here. The paper is explicit that "simultaneously recording single action
   potentials from tens of thousands of neurons is constrained by sensor dynamics and
   optical sampling constraints" (MICrONS Consortium 2025, Discussion). Anything that
   depends on spike timing at the millisecond scale is not in these data.
3. **The signal is clean at depth.** Dense GCaMP6s expression in excitatory somata and
   neurites means photon scattering and out-of-plane fluorescence contaminate signals
   more as depth increases. The paper asks you to separate a real laminar difference in
   tuning from this optical artifact by comparing at matched depths or validating with a
   method less prone to it (MICrONS Consortium 2025, Discussion).
4. **The scans are comparable.** Fourteen scans across six days, with the mouse in
   different states. Treadmill and pupil traces exist so that state can be modeled; they
   do not remove the issue.
5. **The stimulus spans the relevant features.** A neuron with a low oracle score under
   84 minutes of movies and noise may be tuned to something the screen never showed.
6. **The model is right where you use it.** Digital-twin signal correlations were validated
   against in vivo measurements in separate mice, and the like-to-like results replicate
   with in vivo correlations (Ding et al. 2025, Extended Data Figs. 2 and 3). But the
   model's receptive-field centers are shifted toward the monitor center relative to
   spike-triggered averages, and the authors say of its internal representations that
   "care should be taken in interpreting" them.

### What the data do not license

- **Function for inhibitory neurons.** GCaMP6s was expressed in excitatory neurons only.
  Every inhibitory cell in the volume is structure-only, so every claim about inhibitory
  function in MICrONS is Bin B or C.
- **Function below the scans.** The scans reached about 500 µm below the surface and the
  paper describes the imaged neurons as spanning layers 2 to 5; the EM volume runs from
  pia to white matter. Cells deeper than the scans reached have no functional data.
- **Function outside the overlap.** The smaller EM subvolume (`minnie35`) has a synapse
  table but little proofreading and no other annotation tables in the 2025 release.
- **Causation.** "Neurons with correlated responses are more likely to be connected" is a
  correlation measured once. Ding et al. write that their findings are "consistent with an
  underlying Hebbian plasticity mechanism"; that is an interpretation, and testing it needs
  perturbation or development data. "This wiring causes the tuning" stays in Bin C.
- **Generalization across animals.** Every number on this page comes from one male mouse.
  Schneider-Mizell et al. name this as their principal limitation ("a single animal, in one
  location near the edge of VISp"), and Ding et al. restrict their claims to this volume.
  Rules learned here are hypotheses for the next mouse.
- **Completeness of the graph.** Proofread axons are a small minority, and even fully
  proofread axons had a median 43% of ends that could not be traced further, not counting
  ends at the volume boundary (Ding et al. 2025, Methods, "Manual proofreading
  completion"). Pairs that are connected but whose
  synapse sits on an unproofread branch end up in the control group, which makes the
  measured like-to-like effect a conservative estimate, in the authors' words, and makes
  absolute connection probabilities from this graph lower bounds.


## The EM pipeline

### Acquisition

After perfusion the block was cut into 27,972 serial sections at a nominal 40 nm onto
grid tape, with people supervising the automated ultramicrotome in shifts around the
clock for 12 days, ready to stop it if consecutive sections were at risk. Five automated
transmission electron microscopes (autoTEMs) imaged 26,652 of those sections at about 4 nm
per pixel over about six months, producing about 2 PB of raw imagery (MICrONS Consortium
2025, "The EM volume"). An 800 µm span (sections 7,931 to 27,904), with no consecutive
section loss and about 0.1% loss overall, went forward to reconstruction.

The block had to be re-trimmed and the knife changed partway through, so the data are
two subvolumes: sections 7,931 to 14,815 (about 35% of sections, `minnie35`) and sections
14,816 to 27,904 (about 65%, `minnie65`). They were reconstructed separately and aligned
into one coordinate frame, and a composite image at the interface lets you trace across
it. The "65" is a share of sections, not a neuron count.

### Alignment and segmentation

Stitching and alignment ran as a coarse pipeline (per-image affine, then polynomial where
local misalignment exceeded five pixels, then rough 3D alignment) and a fine pipeline that
used convolutional networks to estimate pixel-wise displacement fields between
neighboring sections, which corrected the distortions around cracks and folds without
restoring what a fold hides. Although imaging was at 4 nm, the aligned volume was
generated at 8 nm to cut data size, so the segmentation ran at 8 × 8 × 40 nm.

Segmentation used affinity-predicting convolutional networks followed by mean-affinity
agglomeration, and was skipped where alignment was judged insufficient or tissue was
missing across several sections. Dendrites and spines came out well, and so did
larger-caliber axons, including inhibitory ones; most excitatory axons are thinner and
less complete, and processes near the pia and white matter often contain errors because
imaging defects cluster there. A separate network
segmented 144,120 nuclei in `minnie65`, and a nucleus-feature classifier (support vector
machine; 96.9% precision, 99.6% recall against manual calls) predicted 82,247 of them to
be neurons (MICrONS Consortium 2025, "Automated reconstruction" and Methods, "Cell
classification").

### Synapse detection

A separate model detected synaptic clefts in the aligned imagery and assigned each a
presynaptic and postsynaptic partner from the segmentation: 524 million across both
subvolumes (186 million in `minnie35`, 337 million in `minnie65`). Against 8,611 synapses
hand-annotated in 70 small test subvolumes, detection had an estimated precision of 96%
and recall of 89%; partner assignment was 98% accurate on a separate held-out set of 191
synapses (MICrONS Consortium 2025, "Automated reconstruction"). Smaller synapses are harder
to detect, so Ding et al. flag a possible bias toward larger synapses in their results.
[Synapse detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }})
covers what those two numbers hide.

### Proofreading was targeted, and the targets were functional

Proofreading ran on the ChunkedGraph system, now part of CAVE (Dorkenwald et al. 2025),
through a modified Neuroglancer for manual edits and a REST API for automated ones. All
of it was in `minnie65`. The 2025 release contains all 1,046,656 edits made up to 16
September 2024, with quarterly updates since (MICrONS Consortium 2025, "Proofreading").

The paper publishes no person-years figure, so do not quote one. What it does publish is
who got proofread and why. Choice of neuron followed the needs of the companion studies:
85 excitatory neurons were proofread to the full extent of axon and dendrite for the
functional connectomics analysis; 1,188 excitatory neurons had only their dendrites
proofread for the columnar census; 1,433 neurons in total have axons cleaned of false
merges with some degree of extension. Extending an axon costs 100 to 1,000 edits, and a
full-time proofreader makes 400 to 600 axon-extension edits in a work week. Automated
error correction with NEURD (Celii et al. 2025) added more than 164,000 edits, most of
them splitting false merges, and the multi-soma cleanup brought the count of individually
segmented neurons to 84,035.

Each proofread cell carries labels in the CAVE table `proofreading_status_and_strategy`:
`status_dendrite`, `status_axon`, and a `strategy_axon` such as `axon_fully_extended`,
`axon_partially_extended` or `axon_interareal`. Ding et al. chose their presynaptic
cells from neurons with an oracle score above 0.25 and a model test correlation above
0.15, clustered in columns in V1 and RL chosen from retinotopic maps; the first 40 were
picked by neuroscientists who could see the functional properties, and the rest were
picked blind to them (Ding et al. 2025, Methods, "Presynaptic neuron selection"). This is
the sampling frame behind every structure-function number from this dataset. The
[MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }}) filters on these
labels before it counts anything, and
[Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
covers how to budget a proofreading plan of your own.


## What the companion papers found

### Like-to-like wiring, with the anatomical null in place (Ding et al. 2025)

The headline structure-function result is a "like-to-like" rule: excitatory neurons with
similar responses are preferentially connected, within and across layers and areas,
including feedback from higher visual areas to V1. The design is the part to learn from.

**The graph.** 148 manually proofread presynaptic neurons (84 with axons fully extended,
64 with only branches heading from higher areas back toward V1 extended) and 4,811
functionally matched postsynaptic partners, whose dendrites were cleaned automatically
with NEURD. After requiring in vivo reliability (CC<sub>max</sub> > 0.4) and model
performance (CC<sub>abs</sub> > 0.2), 144 presynaptic and 3,920 postsynaptic neurons
remained. Together the proofread cells hold more than 1.5 m of reconstructed axon and
dendrite.

**The nulls.** For each presynaptic cell, three cohorts: its connected targets; "ADP
controls", neurons whose dendrite passed within 5 µm of its axon somewhere but received
no synapse; and "same-region controls", neurons in the same area with no such proximity.
The axon–dendrite co-travel distance *L*<sub>d</sub> (the length of dendrite within 5 µm
of the axon) measures opportunity, and synapses per unit *L*<sub>d</sub> measures how
often opportunity became a synapse.

**The results.**

- Mean signal correlation was ordered connected > ADP > same-region, for V1→V1, HVA→HVA,
  V1→HVA and HVA→V1 alike. Axons travel farther alongside the dendrites of similarly tuned
  cells (an axonal-scale effect), and given equal opportunity, similarly tuned pairs form
  more synapses (a synaptic-scale effect).
- Among 6,608 connected pairs, synapse cleft volume rose with signal correlation
  (*r* = 0.032, *P* < 0.001), and pairs with more than one synapse were more correlated
  than single-synapse pairs. The effect is real and small; quote the coefficient.
- Splitting tuning into "what" and "where": both feature similarity and receptive-field
  proximity predicted co-travel distance, but only feature similarity predicted synapses
  per unit co-travel. Receptive-field distance was uncorrelated with synaptic-scale
  connectivity, or anticorrelated in V1.
- Within V1 layer 2/3, orientation preference alone did *not* show a like-to-like effect,
  unlike earlier studies, because unconnected pairs there were as similar as connected
  ones: the volume sits in a region of V1 with a local orientation bias. The measured
  rule depends on the null, and the null depends on where the volume is.
- Cells downstream of a common presynaptic neuron were more similar to each other than a
  pairwise like-to-like rule predicts, in three of four projection types.
- A recurrent network trained on image classification developed like-to-like connections
  of similar magnitude, and removing them hurt performance more than removing random
  connections of the same weight.

All of that was replicated with signal correlations measured directly in vivo rather than
through the model (Ding et al. 2025, Extended Data Fig. 3). The claims are statistical,
from one animal, in a subset of cells chosen for reliability and proofreading; the paper
says so in its own limitations paragraph.

### The pilot that preceded it (Turner et al. 2022)

An earlier phase of the program reconstructed a roughly 250 × 140 × 90 µm volume of
layer 2/3 of mouse primary visual cortex, with visual responses for a subset of pyramidal
cells. Its abstract reports that "pyramidal cells receiving more connections from nearby
cells exhibit stronger and more reliable visual responses" and that pyramidal
connectivity motif frequencies were predicted by a configuration-model random graph
(Turner et al. 2022). The 2025 resource paper describes it as yielding "many more overall
connections, but still only twice the number of functionally characterized cells" as the
50-cell study by Lee et al. before it.

### A census of inhibition in one column (Schneider-Mizell et al. 2025)

A 100 × 100 µm column in VISp, extended from layer 1 to white matter, holds 1,886 cells,
of which 1,352 are neurons. All cells were classified and the neurons were proofread (more
than 46,000 edits), producing a wiring diagram of inhibition with more than 70,000
synapses.
Inhibitory neurons were sorted by the compartment they target (perisomatic targeting
cells, the classical basket cells; distal targeting cells, the Martinotti cells; and
others), and excitatory neurons were clustered from dendritic reconstructions with
whole-cell maps of synaptic input. Among the 29 cells that target other inhibitory
neurons almost exclusively, 21 targeted distal-targeting cells, as expected of VIP
interneurons, and 8 targeted perisomatic-targeting (basket) cells, a disinhibitory
specialist not previously described. The authors' first-named limitation is that this is
one animal at one location. None of these cells has functional data, so every functional
reading of the census is Bin B or C.

### Cell typing from the soma alone (Elabbady et al. 2025)

Most of the 200,000 cells are truncated or imperfectly segmented, so whole-arbor
classification is not available for them. Elabbady et al. show that quantitative
features of the perisomatic region, extracted from EM, are enough to identify cell
classes and subclasses across the cubic millimeter, including types defined by
connectivity. This is what makes the cell-type labels in the CAVE tables possible for
cells no one has proofread.


## Data access

The MICrONS dataset is public through several channels:

- **MICrONS Explorer** (`microns-explorer.org`): browse EM imagery, segmentation and
  annotations in Neuroglancer, with example views to start from.
- **CAVE** (`caveclient`, Dorkenwald et al. 2025): the segmentation, synapse table,
  cell-type, proofreading-status and co-registration tables for `minnie65`. The synapse
  table alone holds 337.3 million rows. Every query pins a materialization version; the
  long-lived analysis versions are 943 and 1300, and
  [provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
  explains why that matters.
- **Static exports**: CSV exports of the annotation tables on Google Cloud Storage need no
  account. The [MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }})
  reads them and records their checksums.
- **Functional data**: calcium traces, stimuli and behavior in a DataJoint database, and as
  NWB files on the DANDI Archive (dandiset 000402).
- **Imagery and meshes**: `cloud-volume` reads the EM and segmentation volumes and
  downloads meshes; NEURD decomposes meshes into annotated graphs.

### A typical structure-function workflow

1. Pick a materialization version and write it down.
2. Query `proofreading_status_and_strategy` for cells with the axon and dendrite status
   your question needs.
3. Query the co-registration table you have chosen, and apply residual and separation
   thresholds. Record them.
4. Pull the synapse rows among the cells that survive both filters, and build the null
   from the geometry of unconnected neighbors, not from all cells.
5. Join the functional data by session, scan index, field and unit ID; where a neuron has
   several units, decide which one you keep and why.
6. Compute your statistic against the null, and state the sampling frame in the caption.

The dataset's size (about 2 PB of raw imagery) means almost everyone works from the
derived tables and meshes, not the pixels.


## Challenges and lessons

### The join is where most of the assumptions live

Nothing in the EM volume depends on the calcium data, and nothing in the calcium data
depends on the EM volume. Every structure-function result depends on both, plus the
transform, plus the match, plus the inclusion thresholds. When you read a MICrONS
structure-function figure, find the paragraph that lists those thresholds. When you
write one, put it in the caption.

### Scale and compute

Segmenting a volume imaged as 2 PB of raw data took large-scale GPU compute, and synapse
detection added more. Proofreading, even when targeted, ran past a million edits. The
paper ranks the marginal costs of producing more data at this scale as human labor
first, automated segmentation compute second, and grid tape third, and says there is
no fundamental technical barrier to doing it again for another animal, species or region.
[Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }})
shows how to estimate the compute and human hours for a volume of your own.

### A single volume truncates long-range wiring

A cubic millimeter is a small fraction of a mouse brain. Axons leave the volume, so
inter-areal connections are sampled only where both cells happen to sit inside it, and
no neuron's full input–output relationship is available. The consortium's own comparison
with H01 makes the trade-off explicit: the human volume is wide and thin to sample all
layers, and MICrONS is nearly cubic to keep local circuits and cross-area connections
intact. Projects such as [MouseConnects]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }})
aim at larger volumes.

### Proofreading is selective, and the selection was functional

Unlike [FlyWire]({{ '/content-library/case-studies/flywire-whole-brain/' | relative_url }}),
which proofread a whole brain, MICrONS proofread the cells its companion studies needed,
and for the structure-function work those were visually responsive, well-modeled cells in
particular columns. Analyses must account for residual segmentation error in everything
else, and findings can be biased toward the proofread regions and cell types. The
tension between thoroughness and feasibility is a standing feature of large-volume
connectomics, and the Virtual Observatory of the Cortex (VORTEX) now takes requests to
steer further proofreading.


## Check yourself

<details markdown="1">
<summary>The functional release contains 115,372 somatic masks and an estimated 75,909
neurons. A colleague reports "115,372 functionally characterized neurons". What went
wrong, and what would you check in the co-registration table before joining it to the
synapse table?</summary>

Masks are per scan, and the same neuron appears in more than one scan where planes
overlap; the neuron count comes from merging masks closer than 10 µm across scans. The
colleague counted units. Before joining, check how many units map to each EM neuron in
the table you are using, decide which unit to keep (Ding et al. kept the one with the
higher oracle score), and confirm that your synapse rows and your co-registration rows
come from the same materialization version.
</details>

<details markdown="1">
<summary>A manual match has residual 15 µm and separation score −6 µm. What does each
number mean, and does the negative sign make the match wrong?</summary>

The residual says that after the transform, the unit's centroid landed 15 µm from the
chosen EM soma's centroid, about four times the average fiducial residual. The negative
separation says some other EM neuron was 6 µm closer to the transformed point than the
one chosen. That is not automatically wrong: matchers had the imagery and the constellation
of neighboring somata, and the score records that they overrode the nearest neighbor. It
is a low-confidence row. Ding et al. kept rows with residual below 20 and separation above
−10, so this row would survive their filter; whether it survives yours is a decision you
should state.
</details>

<details markdown="1">
<summary>Sort into Bin A / B / C, given the MICrONS data: (i) "Connected pairs have higher
signal correlation than pairs with axon–dendrite proximity and no synapse." (ii) "Larger
synapses between similarly tuned cells are stronger synapses." (iii) "Like-to-like
connectivity in this volume arose through Hebbian plasticity."</summary>

**(i)** As close to Bin A as functional connectomics gets: a measured structural
statistic against a stated anatomical null, with a measured functional variable on
each side. Its residual assumptions are the match, the proxy from calcium to spiking,
and the inclusion thresholds, which should be stated.

**(ii)** Bin B. Cleft volume is measured; "stronger" assumes that cleft volume is
monotonic in physiological strength. Ding et al. say the assumption in the same sentence
("a proxy for synaptic strength"). Do the same.

**(iii)** Bin C. The data are one snapshot of one adult animal; a developmental or
plasticity mechanism needs perturbation, time series or a molecular measure. The authors
write "consistent with", which is the right verb.
</details>


## Discussion Questions for Instructors

1. The average co-registration residual is 3.8 µm, and the paper merges masks from
   different scans into one neuron when they fall within 10 µm. Why is a separate matching
   step still necessary, and what would change in the analysis if the residual were 15 µm
   instead?
2. Ding et al. found no like-to-like effect for orientation preference within V1 layer
   2/3, in contrast to earlier work, because unconnected pairs were as similar as connected
   ones. What does this tell you about the null model, and how would you design a volume
   placement to avoid the problem?
3. The like-to-like rule in MICrONS is statistical: many connected pairs are not
   functionally similar. What does a real but partial rule mean for our understanding
   of cortical computation? Is connectivity destiny, or one factor among many?
4. Inhibitory neurons have no functional data in MICrONS. Write one Bin A claim, one
   Bin B claim and one Bin C claim about the basket-cell-targeting disinhibitory
   specialist, and say what measurement would move the Bin C claim.
5. Compare the proofreading strategy of MICrONS (targeted by scientific question, with
   functional criteria) with FlyWire (exhaustive). What biases does each introduce into a
   connectivity statistic, and under what circumstances is each appropriate?
6. If you could add one additional data modality to MICrONS (gene expression,
   neuromodulator receptor distribution, developmental lineage, a second animal), which
   would you choose and why?


## Related

- [Unit 01: Why map the brain]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}) — the three bins
- [Unit 04: Volume reconstruction infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}) — CAVE, materialization and the lab
- [Unit 08: Segmentation and proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
- [Unit 09: Connectome analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}) — null models
- [MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }})
- [MICrONS dataset record]({{ '/datasets/catalog/microns/' | relative_url }})
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }})
- [Synapse detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }})
- [Case-study papers]({{ '/content-library/journal-papers/case-studies/' | relative_url }})
- [H01 human cortex]({{ '/content-library/case-studies/h01-human-cortex/' | relative_url }}) · [FlyWire whole brain]({{ '/content-library/case-studies/flywire-whole-brain/' | relative_url }}) · [MouseConnects]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }})


## Key References

- The MICrONS Consortium. (2025). Functional connectomics spanning multiple areas of
  mouse visual cortex. *Nature*, 640, 435–447.
  [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
  (Preprint: *bioRxiv* 2021.07.28.454025.)
- Ding, Z., et al. (2025). Functional connectomics reveals general wiring rule in mouse
  visual cortex. *Nature*, 640, 459–469.
  [10.1038/s41586-025-08840-3](https://doi.org/10.1038/s41586-025-08840-3)
- Schneider-Mizell, C. M., et al. (2025). Inhibitory specificity from a connectomic
  census of mouse visual cortex. *Nature*, 640, 448–458.
  [10.1038/s41586-024-07780-8](https://doi.org/10.1038/s41586-024-07780-8)
- Elabbady, L., et al. (2025). Perisomatic ultrastructure efficiently classifies cells in
  mouse cortex. *Nature*, 640, 478–486.
  [10.1038/s41586-024-07765-7](https://doi.org/10.1038/s41586-024-07765-7)
- Celii, B., et al. (2025). NEURD offers automated proofreading and feature extraction
  for connectomics. *Nature*, 640, 487–496.
  [10.1038/s41586-025-08660-5](https://doi.org/10.1038/s41586-025-08660-5)
- Dorkenwald, S., et al. (2025). CAVE: Connectome Annotation Versioning Engine.
  *Nature Methods*, 22, 1112–1120.
  [10.1038/s41592-024-02426-z](https://doi.org/10.1038/s41592-024-02426-z)
- Turner, N. L., et al. (2022). Reconstruction of neocortex: Organelles, compartments,
  cells, circuits, and activity. *Cell*, 185(6), 1082–1100.
  [10.1016/j.cell.2022.01.023](https://doi.org/10.1016/j.cell.2022.01.023)
