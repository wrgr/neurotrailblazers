---
layout: page
title: "Instructor FAQ"
permalink: /teaching/faq/
slug: teaching-faq
content_type: delivery
description: "Questions learners actually ask about EM, scale, segmentation error, synapse detection, nulls, versions and credit, answered from what the site teaches, with the page each answer comes from."
---

[Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}) · [Four-session block]({{ '/teaching/sequence/' | relative_url }}) · [Assessment bank]({{ '/teaching/assessment/' | relative_url }})

## How to use this page

These are the questions learners ask during the sessions, in roughly the words they
use, with the answer an instructor needs in the moment and the page to send them to
afterward. Every answer comes from a page on this site or from a primary source that
page cites, and each one links to where the full treatment lives. Nothing here adds a
claim the linked page does not make.

The questions were collected from three places: the "Misconceptions to target" list on
each [session kit]({{ '/teaching/sessions/' | relative_url }}), the "Instructor
cautions" and teaching notes on the [lecture plans]({{ '/teaching/lectures/' | relative_url }}),
and the failure modes in the [Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}#failure-modes-specific-to-this-material).
Dataset numbers use the site's canonical wording, and each carries its source. If a
question is not here, the [content library]({{ '/content-library/' | relative_url }}) is
where the depth lives.

## EM and tissue

**"We can already see neurons with confocal. Why does this need EM?"**
Light microscopy resolves down to about 200–250 nm. A synaptic cleft is about 20 nm, an
unmyelinated axon in neuropil 80–300 nm and a spine neck 50–200 nm, so at 250 nm two
membranes 20 nm apart are one blur, and one blur can span several axons. Light can show
that two arbors overlap in space; it cannot show that they are connected, and predicting
synapses from contact is unreliable at the level of individual pairs. The case is
specific, not general: for "which region projects to which", light is the right tool.
[Unit 01 §1]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}#1-the-resolution-argument-in-numbers)
and its check-yourself.

**"Is a length measured in an EM volume the real length?"**
Not exactly, and the error is systematic rather than random. Fixation, dehydration and
resin embedding change tissue dimensions by an amount that depends on the protocol and
is rarely measured in the sample itself; compared with high-pressure freezing, aldehyde
perfusion shrinks the extracellular space and enlarges glial volume (Korogod, Petersen
and Knott 2015, *eLife* 4:e05793). Every absolute length, area and volume in EM
connectomics is affected. Report measurements as measured, state the protocol, and
prefer ratios and within-volume comparisons over absolute values compared across studies.
[Unit 03 §1]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}#1-the-preparation-chain-step-by-step),
steps 1.1 and 1.3.

**"The images are noisy. Isn't that the biggest problem?"**
Usually not. Noise raises the split rate, and splits are visible and bounded: a
proofreader finds two fragments and joins them. Faint membranes raise the merge rate,
and a merge fuses two neurons, invents connections and hides in every summary
statistic. So when trading dose against speed, protect membrane contrast, and measure
membrane contrast-to-noise rather than overall image SNR. Doubling SNR costs about four
times the acquisition time at fixed beam current, which is why "image it better" is
rarely the answer at petascale.
[Unit 03 §2, the asymmetry]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}#the-asymmetry-you-must-internalize)
and §1.5. The [Module 05 kit]({{ '/teaching/sessions/module05/' | relative_url }}#misconceptions-to-target)
targets this belief directly.

**"Can't we proofread our way out of a bad image?"**
Only partly. Acquisition quality sets a ceiling on reconstruction quality that no
downstream model or labor can raise. Unit 03 sorts artifacts into two cost classes:
labor artifacts (knife chatter, charging, weak contrast) cost proofreading hours and are
eventually correctable; data-loss artifacts (lost sections, folds, tears, severe beam
damage) destroy tissue that was never imaged, so the biology inside them is unanswerable
in that region. A QA report with one quality score hides exactly this distinction.
[Unit 03 §2]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}#2-artifact-catalog-with-downstream-cost);
[Module 05 kit]({{ '/teaching/sessions/module05/' | relative_url }}#misconceptions-to-target).

**"Membranes fade toward the middle of each section. Is that a real difference in the tissue?"**
Probably not. Ask which coordinate system the defect lives in. A gradient that follows
block geometry, in every section, points to staining penetration; one that follows
acquisition order points to beam or detector drift; one that follows anatomy (only white
matter, say) could be tissue composition. The dangerous case is a depth-dependent
staining gradient that runs in the same direction as cortical layers, which can be
published as a laminar difference in synapse density. The acquisition fix is smaller
blocks; the analysis fix is to test the coordinate system before interpreting.
[Unit 03 §1 check-yourself]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}#1-the-preparation-chain-step-by-step);
Tools and Methods [teaching notes]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}#notes-for-whoever-teaches-it).

## Scale and data size

**"How big is a cubic millimeter, and why do I see 1.6 PB in one place and 2 PB in another?"**
At 4 × 4 × 40 nm, 1 mm³ is 250,000 × 250,000 × 25,000 voxels, about 1.56 × 10¹⁵, so about
1.6 PB at one byte per voxel. That is arithmetic, before alignment or any derived product.
Released datasets report their own figures: MICrONS produced about 2 PB of raw data
(MICrONS Consortium et al. 2025, *Nature* 640:435–447, "EM dataset"), and H01 is 1.4 PB
aligned and 1.8 PB raw (Shapson-Coe et al. 2024, *Science* 384:eadk4858). The raw figure
is also the smallest line item: the pyramid, affinity maps, segmentation, meshes, synapse
table and edit history multiply it, and the dominant project cost is none of them but
proofreading labor.
[Unit 01 §2]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}#2-the-cost-argument-in-numbers-you-can-compute)
for the arithmetic; [Unit 02 §5]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}#5-compute-and-storage-planned-rather-than-discovered)
and [Unit 04 §5]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}#5-capacity-and-cost-worked)
for the multiplier. The [Module 12 kit]({{ '/teaching/sessions/module12/' | relative_url }}#misconceptions-to-target)
targets "the dataset size is the petabyte figure quoted for the raw imagery" and
"storage cost is the storage line on the invoice".

**"If EM is the highest resolution, why isn't it always the right choice?"**
Because the rule is the coarsest acquisition scale whose reconstruction scale still
resolves every object the analysis depends on, not the finest you can afford. Every step
finer multiplies data volume, alignment difficulty and proofreading hours. If the
endpoint is "does area A project to area B", the unit is the axon bundle, and light-sheet
imaging of a bulk tracer at 1 µm is the correct choice: a 1 µm³ voxel holds about 1.6
million voxels of 4 × 4 × 40 nm. Learners arrive assuming nanoscale is the serious
scale; the decision rule is what dislodges that.
[Unit 02 §1]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}#1-the-three-scales-that-are-not-the-same-thing);
Introduction lecture [teaching notes]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }}#notes-for-whoever-teaches-it).

**"How far away is a whole mouse brain?"**
About 500 mm³ (Badea, Ali-Sharief and Johnson 2007, *NeuroImage* 37:683–693, measured at
508.9 ± 23.4 mm³) at 4 × 4 × 40 nm and 8 bits is roughly 800 PB of raw imagery. That is
the site's arithmetic, a projection and not a measurement. Abbott et al. (2020, *Cell*
182:1372–1376) put the whole project at "roughly 1 million terabytes", about an exabyte;
the two figures are a raw-voxel projection and a rougher whole-project estimate, not a
conflict. The jump from 1 mm³ to whole brain is about 500×, and imaging is one part of
it: sectioning reliability, storage, alignment, segmentation accuracy and proofreading
labor scale with it. NIH's BRAIN CONNECTS program announced its first 11 awards on
26 September 2023, and its first theme is EM pipelines for the mouse brain.
[Unit 01 §2]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}#2-the-cost-argument-in-numbers-you-can-compute),
extrapolation table.

## Segmentation and proofreading errors

**"Why do you keep saying merges are worse than splits?"**
A split leaves a neuron in pieces; the truncated arbor looks wrong, an endpoint detector
finds it, and the fix is local and bounded. A merge fuses two neurons into an object that
looks like a neuron and is not: it invents connections, possibly between cells of
different types or layers, it propagates into every downstream analysis, and nothing in
a summary statistic shows the join. That asymmetry is why pipelines are tuned to
over-segment, why proofreading is mostly joining, and why merges outrank splits in a
triage queue at equal size. The Facilitator Guide's question stem "If you had to be wrong
in one direction, which would you choose?" tests exactly this.
[Unit 08 §2]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}#2-error-taxonomy-and-cost);
[Module 06 kit]({{ '/teaching/sessions/module06/' | relative_url }}#misconceptions-to-target)
("merge and split errors are equally costly").

**"This object looks like a plausible neuron. Isn't that evidence the segmentation is right?"**
Weak evidence, because a merge between two plausible neurites also looks like a plausible
neuron. A morphology detector catches the impossible merges, two somata in one object or
ribosomes and presynaptic vesicle clusters in the same process, and the rest pass. So an
empty merge queue measures the detector, not the segmentation, and a long split queue is
the over-segmenting design working, not evidence that merges are rare. Unit 06 turns the
problem into a tool: when two high-reliability cues from different families contradict
each other, the leading hypothesis is "this is not one object". What settles the question
is exhaustive proofreading of a random sample of the analysis cells, and the size of the
endpoint shift it produces.
[Unit 08 §2 check-yourself]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}#2-error-taxonomy-and-cost)
and [§3, the metric that matters]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}#the-metric-that-actually-matters);
[Unit 06 §2 check-yourself]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}#2-the-exceptions-that-break-the-polarity-rule).

**"The methods say 'all cells were proofread'. What does that tell me?"**
On its own, almost nothing, because "proofread" covers everything from gross merges
removed to exhaustive, and a reader cannot tell whether a low connection count is biology
or incompleteness. A usable statement gives the level and its written criteria ("L2,
dendrite complete, defined as…"), per-cell level metadata with the number of cells
excluded, the stopping rule stated in advance, and the measured shift: what exhaustive
proofreading of a sample did to the endpoint. The last item answers the question the
reviewer is really asking, which is whether more proofreading would have changed the
result.
[Unit 08 §4, stopping rules]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}#stopping-rules)
and its check-yourself; [Module 07 kit]({{ '/teaching/sessions/module07/' | relative_url }}#misconceptions-to-target).

**"Why fix a thin glia merge before a split that detaches half a dendrite?"**
Because the split truncates visibly and the merge corrupts silently. A fine astrocytic
process fused to a dendrite wanders through neuropil the dendrite never visits, and
because astrocytic processes ensheathe synapses, it collects false inputs at a high rate
per unit length. Those inputs come from spatial neighbors, so they inflate exactly the
statistics that make a circuit look locally wired. An unfixed split delays a cell, which
fails its completeness criterion and is excluded until repaired; an unfixed merge poisons
one. Conspicuousness is not a triage factor.
[Unit 07 §1]({{ '/technical-training/07-glia/' | relative_url }}#1-why-a-glia-merge-is-expensive);
[Unit 08 §4]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}#4-the-production-proofreading-loop),
worked example; [Module 06 kit]({{ '/teaching/sessions/module06/' | relative_url }}#misconceptions-to-target)
("the most visually obvious errors are the ones most worth fixing").

**"Is 'uncertain' an acceptable answer, or does it mean I couldn't do it?"**
It is a valid and valuable output, and the facilitator should say so out loud, early.
Unit 05 defines the tiers operationally: high needs two independent cues from different
families plus continuity across three or more sections; uncertain means the cues conflict
or the decisive cue is not visible. A dataset in which some calls are flagged uncertain
with reasons is more useful than one in which every call is forced, because the
uncertain set is the review queue. Unit 06's lab scores accuracy within the
high-confidence tier for the same reason: an annotator whose tiers carry information is
worth more than one with a higher flat score. The Facilitator Guide's preparation
checklist includes deciding what "uncertain" earns before the session.
[Unit 05 §3, confidence tiers]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}#the-confidence-tiers-defined-operationally);
[Unit 06 lab]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}#lab-calibration-round-90-minutes);
[Facilitator Guide, assessment]({{ '/teaching/facilitator-guide/' | relative_url }}#assessment-that-scales);
[Module 01 kit]({{ '/teaching/sessions/module01/' | relative_url }}#misconceptions-to-target)
("good annotators never make errors").

## Synapse detection

**"What is the detector's accuracy, and can we quote the paper's number for our region?"**
There is no accuracy to quote. Accuracy needs true negatives and a defined negative
universe, and a synapse table has neither; report precision and recall with their
denominators, and call F1 "F1". Nor does a published figure transfer: MICrONS reports 96%
precision and 89% recall for its own automated detection, and 98% for partner assignment
(MICrONS Consortium et al. 2025, "Automated reconstruction"), and those describe that
volume, those thresholds and that matching rule. Detectors do not transfer across
preparations, and the evaluation unit matters, since per-synapse and per-connection
numbers from one detector can differ by ten points. Establish recall and partner
accuracy in your region with independently annotated patches, and report the table's
version.
Synapse Detection lecture, [Instructor cautions]({{ '/teaching/lectures/synapse-detection/' | relative_url }}#instructor-cautions);
[Synapse Detection reference, §6]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}#6-why-detectors-do-not-transfer)
and [§7]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}#7-before-you-trust-a-synapse-table);
assessment bank [S2]({{ '/teaching/assessment/answers/' | relative_url }}#s2-sd-2).

**"If precision is high, why does the excitatory/inhibitory ratio still come out wrong?"**
Because recall differs by class, and unequal recall biases raw counts even when nearly
every row is real. The site's worked case is H01, where the reference page reports
false-negative rates of 11% for excitatory against 35% for inhibitory synapses, while the
false-discovery rates are 3.2% and 2.7%. A single combined F1 hides that. Correct each
class by its own precision and recall, report the recall figures next to the ratio, and
treat the corrected number as a conditional estimate rather than recovered truth, since
it assumes the validation counts apply to the region you are correcting.
[Synapse Detection reference, "Detection performance depends on the claim"]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}#start-here-this-is-a-solved-problem-with-three-residuals);
Synapse Detection [timed plan]({{ '/teaching/lectures/synapse-detection/' | relative_url }}#timed-plan-and-instructor-cues),
minutes 20–40; assessment bank [S3]({{ '/teaching/assessment/answers/' | relative_url }}#s3-sd-3).

**"Can we estimate recall by checking a random sample of the table's rows?"**
No. Missed synapses are not in the table, so no sample of rows can find them; rows tell
you about precision. Recall needs regions annotated exhaustively and independently of the
predictions, matched one-to-one under a stated rule, with TP, FP and FN reported by class
and region. One region does not represent the dataset, checking predictions by eye is
biased toward accepting them, and increasing the sample to 5,000 rows changes none of
this. Synapse Detection [timed plan]({{ '/teaching/lectures/synapse-detection/' | relative_url }}#timed-plan-and-instructor-cues),
minutes 65–80; assessment bank [S5]({{ '/teaching/assessment/answers/' | relative_url }}#s5-sd-4).

**"This synapse is asymmetric, so it's excitatory, and more synapses means a stronger connection. Right?"**
Both are Bin B claims: structure plus one declared assumption. Gray type I (asymmetric)
morphology predicts glutamatergic transmission well in cortex, but it is a statistical
association, not an identity: vesicle shape depends on fixation, some glutamatergic
synapses onto interneuron shafts look less asymmetric, and neuromodulatory terminals do
not fit the dichotomy. Synapse count, or PSD area, is assumed monotonic in physiological
effect; defensible, and a model. Write "putatively excitatory (asymmetric)" and "makes
4.5 times as many synapses onto", and where the sign matters, use the presynaptic cell's
identity, which is usually the stronger evidence. A connectome gives neither weights nor
sign directly.
[Unit 05 §2, Gray type I vs type II]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}#gray-type-i-vs-type-ii);
[Unit 01 §3]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}#3-what-structure-can-and-cannot-establish);
[Unit 09 §5]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}#5-neuroai-what-actually-transfers);
[Module 11 kit]({{ '/teaching/sessions/module11/' | relative_url }}#misconceptions-to-target).

**"How do I know it's a synapse and not just a dark membrane?"**
All three criteria, then persistence: a vesicle cluster at the apposition, a cleft of
uniform width with parallel membranes, and a postsynaptic density, visible on more than
one consecutive section. Dark contrast alone is the most common beginner error; it can be
a tangentially cut membrane, staining precipitate, a glial apposition or an adherens
junction, which has symmetric densities on both sides and no vesicle pool. No vesicles, no
synapse. A PSD 200–500 nm across cut edge-on at 40 nm should span roughly 5 to 12
sections; one lying flat in the plane may show on only one or two, so check orientation
before rejecting. The Facilitator Guide opens with this failure: a learner who can recite
the criteria still calls a tangentially cut membrane a synapse on the first real patch.
[Unit 05 §2]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}#2-calling-a-synapse-the-three-criteria);
[Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}#read-this-first-the-constraint-that-shapes-everything).

## Graphs, nulls and statistics

**"Our motif is 2.9 times enriched over random. Is that a result?"**
Not yet, because "random" is the question. Unit 09's worked example, on a synthetic graph
with numbers made up for teaching, takes one dataset through three nulls: 2.9× under
Erdős–Rényi, 1.4× (z = 5.0) under a degree-preserving null, and 1.14× (z = 1.8, p ≈ 0.07)
once distance is preserved as well. Degree heterogeneity alone accounted for more than
half the excess. The same data support "p < 10⁻⁶" or "no detectable effect" depending on
a choice made before any test. Note too that observed over expected is an effect size,
not evidence: the assessment bank's A3 has an identical 19/15 ratio at two thresholds
with tail probabilities of 0.43 and 0.65, and failing a rule does not show the wiring is
random.
[Unit 09 §2]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}#2-null-models-what-are-you-controlling-for);
assessment bank [A3]({{ '/teaching/assessment/answers/' | relative_url }}#a3-aa-3-aa-4);
[Module 08 kit]({{ '/teaching/sessions/module08/' | relative_url }}#misconceptions-to-target)
and [Module 10 kit]({{ '/teaching/sessions/module10/' | relative_url }}#misconceptions-to-target).

**"Which null should we use?"**
Preserve everything you are not asking about. If the hypothesis is "reciprocity exceeds
what degree and distance explain", the null must hold degree and distance fixed;
otherwise you have measured degree heterogeneity and proximity and called it a motif.
Write the uninteresting explanation out in words before choosing; if you cannot write the
sentence, you do not yet know what you are testing. Degree-preserving is the minimum for
a connectome, add distance whenever soma positions exist, and use a type-preserving null
when type composition could explain the count. Choosing the null is the scientific step;
running the test is bookkeeping.
[Unit 09 §2]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}#2-null-models-what-are-you-controlling-for)
and its check-yourself; [Module 08 kit]({{ '/teaching/sessions/module08/' | relative_url }}#misconceptions-to-target)
("the statistical test is the scientific step, when the choice of null model is").

**"Does the synapse threshold really matter?"**
It can remove most of the edges. Synapses per connection are heavy-tailed and
single-synapse connections usually dominate by count, so moving from ≥ 1 to ≥ 3 can drop
more than half the edges, and it does so non-uniformly across cell types. Unit 09's
check-yourself has two correct graphs from the same data with 5,000 and 1,800 edges.
Report the threshold, and re-run the headline at a second one; if the conclusion flips,
that is the finding. The MICrONS lab runs its primary analysis at one synapse and its
sensitivity at two.
[Unit 09 §1]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}#1-graph-construction-is-a-sequence-of-consequential-choices);
[MICrONS lab]({{ '/notebooks/microns-lab/' | relative_url }});
[Module 10 kit]({{ '/teaching/sessions/module10/' | relative_url }}#misconceptions-to-target).

**"Won't reconstruction errors just add noise, so the true effect is at least as large as we measured?"**
No. That is true of noise and false of bias, and several connectomics errors are biases
toward the interesting answer. A direction error removes a true edge and adds its
reverse; where a connection carries several synapses, reversing one of them turns a
one-way connection into an apparent reciprocal pair. A glia merge adds inputs from
spatial neighbors and inflates local clustering. A neuron merge fuses two partner lists
and can close triangles that never existed, or collapse edges, depending on the motif
and the graph rules. Ask which way the error pushes the statistic you report, then run
the sensitivity check: perturb the graph at your measured merge and split rates and
report the band, which holds only under that error model.
[Unit 06 §4]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}#4-why-direction-errors-cost-more-the-arithmetic);
[Unit 09 §3]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}#3-motif-analysis-done-carefully);
[Unit 07 §1]({{ '/technical-training/07-glia/' | relative_url }}#1-why-a-glia-merge-is-expensive);
Algorithms and Applications [teaching notes]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }}#notes-for-whoever-teaches-it);
[Module 11 kit]({{ '/teaching/sessions/module11/' | relative_url }}#misconceptions-to-target).

**"We tested all sixteen triad classes and one is significant. Can we report it?"**
Report all sixteen tests, including the ones you ran and did not report. At α = 0.05 you
expect about one false positive among sixteen. Correct for it (Bonferroni is conservative
but defensible for 16; Benjamini–Hochberg if you prefer FDR), and prefer permutation
inference, because triad counts are correlated with each other and the sixteen tests are
not independent. If you tried other nulls until one worked, that is a multiple-comparison
problem no correction repairs after the fact.
[Unit 09 §3]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}#3-motif-analysis-done-carefully);
[Module 08 kit]({{ '/teaching/sessions/module08/' | relative_url }}#misconceptions-to-target)
("reporting the tests that worked is sufficient without reporting how many were run").

## Versions and reproducibility

**"We reran the notebook and the count changed. Which number is right?"**
Possibly both, for different objects. In a ChunkedGraph system the root ID of a neuron
changes on every edit, so an ID without a materialization version or timestamp is
meaningless, and a query against "latest" silently answers a different question each
week. Unit 04's worked example, an invented case, settles such a discrepancy by pinning
the query to each candidate version, matching per-partner counts row for row, and mapping
the old ID forward through the lineage service to show that merges attached more
dendrite. The converse also holds: an equal count is not a reproduction until the ID
lists match, as the assessment bank's T3 shows with two snapshots of equal size and
different rows. The repair is a version in the figure caption and a header in the
notebook.
[Unit 04 §2]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}#2-the-core-idea-an-editable-graph-over-immutable-atoms);
assessment bank [T3]({{ '/teaching/assessment/answers/' | relative_url }}#t3-tm-3);
Tools and Methods [plan]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}#teach-a-90-minute-session),
minutes 30–40; [Module 12 kit]({{ '/teaching/sessions/module12/' | relative_url }}#misconceptions-to-target)
("an object ID refers to the same neuron next month").

**"What has to go in the methods record, and isn't a link to the repository enough?"**
The minimum is a header stated once: dataset, datastack, version (never "latest"),
snapshot timestamp, tables, client or file route, run date, author. The full record has
seven groups: data identity; access and integrity (URL, bytes, hash, whether the hash was
checked); selection rules in order with counts excluded at each step and the
proofreading level required; the six graph-construction decisions; statistics (every
null tried, samples, seed, decision rule fixed in advance, number of tests); code and
environment; and the claim boundary with the data citation and the non-claim. A
repository link is where this starts. A notebook that ran end to end once in its author's
environment shows that it ran once; Unit 04 asks for pinned dependencies and a re-run
that matches, and Module 21's kit does the clean-environment rerun.
[Provenance and versioning, the header]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}#the-reproducibility-header-is-five-lines-stated-once-on-the-site)
and [seven groups]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}#a-methods-record-must-contain-seven-groups-of-fields);
[Unit 04 §4]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}#4-reproducibility-requirements);
[Module 17 kit]({{ '/teaching/sessions/module17/' | relative_url }}#misconceptions-to-target)
and [Module 21 kit]({{ '/teaching/sessions/module21/' | relative_url }}#misconceptions-to-target).

**"Which MICrONS version should learners use?"**
For the site's lab, v1507, read from the public static CSV exports: no account is needed,
the notebook stops if a file's hash does not match, and the archived outputs on the lab
page are the reference for a rerun. For live CAVE queries, use a version the MICrONS team
keeps long-term, 943 or 1300; v1507 was scheduled to leave the live service on 31 July
2026 and that date has passed. A live query at 1300 or 943 will not reproduce the v1507
numbers, because the proofread set and the root IDs differ between versions. That is the
point of pinning, not a defect in it.
[MICrONS lab, data source]({{ '/notebooks/microns-lab/' | relative_url }}#data-source-and-exact-version);
[Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}#microns-keeps-three-versions-long-term-and-expires-the-rest).

## Ethics and credit

**"The data are public. Why is there an ethics question?"**
Because two obligations are live now regardless of consent history: license compliance
and credit for proofreading labor. Public does not mean unlicensed, and the data license,
not the article license, governs reuse. FlyWire's *Nature* paper is CC BY 4.0 but its
data release is CC BY-NC 4.0, so a paid product built on the data is outside the license
even though the paper's figures are reusable; MICrONS data are CC BY 4.0 with attribution
required. Attribution also goes beyond the flagship paper: the MICrONS lab's data-citation
note says the proofreading and cell-type tables have their own papers to cite.
[Ethics and Governance, §3]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}#3-licenses-what-a-reuser-is-actually-obliged-to-do);
[MICrONS lab]({{ '/notebooks/microns-lab/' | relative_url }});
[Module 02 kit]({{ '/teaching/sessions/module02/' | relative_url }}#misconceptions-to-target)
and [Module 17 kit]({{ '/teaching/sessions/module17/' | relative_url }}#misconceptions-to-target)
("citing the original EM paper covers all required attributions").

**"Is the hemibrain CC BY or CC BY-NC?"**
Two sources disagree, and the answer to teach is to record the conflict rather than
resolve it. Janelia's hemibrain project page links CC BY 4.0; the v1.0 data deposit the
paper cites (doi:10.25378/janelia.11676099) is registered as CC BY-NC 4.0 in its DataCite
record, re-verified on 26 September 2026. The site applies the more restrictive terms
until Janelia confirms which governs, and the Ethics lecture's expected worksheet answer
is the same. Do not tell learners the conflict is settled.
Ethics lecture, [Instructor cautions]({{ '/teaching/lectures/ethics-and-governance/' | relative_url }}#instructor-cautions);
[Ethics and Governance, §3]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}#3-licenses-what-a-reuser-is-actually-obliged-to-do).

**"Could the H01 donor be identified from the data?"**
Discuss this only through what the paper publishes, and do not invite the room to try.
The published facts are tissue from the middle temporal gyrus of a 45-year-old woman with
drug-resistant epilepsy (Shapson-Coe et al. 2024). The site's position is that residual
re-identification risk lives in metadata, not in voxels. The main *Science* article
carries no consent or IRB statement; the plan's slide 9 is careful to say that, and not
that approval is lacking, so teach learners to look in the supplementary materials before
citing a human-tissue dataset.
Ethics lecture, [timed plan]({{ '/teaching/lectures/ethics-and-governance/' | relative_url }}#timed-plan-and-instructor-cues)
minutes 10–22 and [Instructor cautions]({{ '/teaching/lectures/ethics-and-governance/' | relative_url }}#instructor-cautions);
[Ethics and Governance, §1]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}#1-consent-and-human-brain-tissue)
and [§2]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}#2-de-identification-what-an-em-volume-can-and-cannot-reveal).

**"Who gets credit for proofreading, and does it count for anything?"**
The site describes four models in use: consortium co-authorship (the FlyWire Consortium),
collective acknowledgment in the author line ("and the EyeWirers"), per-contribution
platform attribution (FlyWire Codex), and named authorship with a contributions statement
(H01). Each has a cost; consortium membership is hard to claim in a tenure case, and
CRediT has no term for proofreading. The scale is real: FlyWire estimates about 33
person-years of manual proofreading (Dorkenwald et al. 2024, *Nature* 634:124–138) and
the hemibrain over 50 (Scheffer et al. 2020, *eLife* 9:e57443); MICrONS and H01 publish
no equivalent figure. The teachable rule is to write the credit policy before the work
starts, not after the paper is drafted.
[Ethics and Governance, §5]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}#5-credit-for-proofreading-labor);
[Module 19 kit]({{ '/teaching/sessions/module19/' | relative_url }}#misconceptions-to-target)
("contribution volume alone decides authorship").

## Running the sessions

**"Do learners need accounts, downloads or Python?"**
For the four-session block and the Ethics session, none of the three: every activity runs
from printed rows or a calculator, and Python is optional in Sessions 3 and 4. The MICrONS
lab needs Python 3.11–3.13, about 90 MB of downloads and outbound HTTPS to
`storage.googleapis.com`, but no account; the archived executed notebook is the offline
fallback. The Unit 03 QA lab opens a public volume in a browser viewer without an account,
but it is live data, so check that it loads the week before. Part A of Units 04 and 08
needs a proofreading-capable viewer and account, which is why both syllabus maps omit it.
[Four-session block]({{ '/teaching/sequence/' | relative_url }});
[MICrONS lab, access]({{ '/notebooks/microns-lab/' | relative_url }}#account-and-access-requirements);
[Syllabus maps, audience]({{ '/teaching/syllabi/' | relative_url }}#audience-and-prerequisites).

**"The session is running long. What do I cut?"**
Cut optional slides before the activity or its debrief; the learning evidence is the
revised claim, not the number of slides shown, and each lecture plan lists which slides
are extension material. In the technical units, cut the survey before the worked
example: for Unit 09, cut §4 "Beyond motifs", never the reciprocity example in §2. In a
module kit, the last step is usually the one to make homework, as the syllabus maps do
with Module 17's reviewer response and Unit 03's steps 6–7.
[Four-session block, preparation and pacing]({{ '/teaching/sequence/' | relative_url }}#preparation-and-pacing);
[Facilitator Guide, failure modes]({{ '/teaching/facilitator-guide/' | relative_url }}#failure-modes-specific-to-this-material);
[pacing notes]({{ '/teaching/syllabi/' | relative_url }}#pacing-notes).

**"Can I teach Units 05–07 as lectures if I have no time to build patch sets?"**
You can, and the Facilitator Guide names it as the first failure mode: learners who can
describe cues and cannot apply them. Convert at least half of contact time to scored
judgments on short z-stacks; single-image practice teaches the single-plane call the
units tell learners to break, and a curated set of clean patches produces overconfidence
that collapses on real data. Model one example aloud, including your own uncertainty,
rather than three worked cleanly. The preparation is real: the labs need a borderline set
for Unit 05, 20 labeled processes for Unit 06 and 40 glia patches for Unit 07, built from
a public volume, and the site does not ship them. If you cannot build a set, do what the
10-week map does and omit the lab rather than lecture it.
[Facilitator Guide, session design]({{ '/teaching/facilitator-guide/' | relative_url }}#session-design)
and [failure modes]({{ '/teaching/facilitator-guide/' | relative_url }}#failure-modes-specific-to-this-material);
[16-week map]({{ '/teaching/syllabi/16-week/' | relative_url }}), instructor preparation.

**"The answer keys are public. Can I still grade with them?"**
Grade the revision, not the first attempt. Every lecture and workshop key is published
and formative, and the syllabus maps grade the learner's revised study brief and
carried-forward package. For a check the public keys do not answer, the
[assessment bank]({{ '/teaching/assessment/' | relative_url }}) and the
[unit items]({{ '/teaching/assessment/units/' | relative_url }}) use different numbers and end every item with a variant template for
writing a secure version; recompute the answers for any variant. None of the rubrics is
a validated instrument, and nothing here should be reported as one.
[Syllabus maps, assessment]({{ '/teaching/syllabi/' | relative_url }}#assessment);
[assessment bank]({{ '/teaching/assessment/' | relative_url }});
[unit items]({{ '/teaching/assessment/units/' | relative_url }}).

**"What is a calibration round, and when do I run one?"**
Everyone scores the same three items independently, then the scores are compared
publicly before anyone proceeds. Expect a wide spread the first time and a narrower one
after discussion; the narrowing is the learning, and it shows why production annotation
teams run the same sessions. Run it before the cohort matters: at step 2 of the Unit 03
QA lab, as the Unit 05 consensus round, and as the Unit 06 lab, where the diagnostic is
accuracy within the high-confidence tier rather than overall accuracy. There is no
validated calibration instrument on this site; the procedure is the instrument.
[Facilitator Guide, calibration round]({{ '/teaching/facilitator-guide/' | relative_url }}#run-a-calibration-round-before-the-cohort-matters);
[unit items, running a calibration round]({{ '/teaching/assessment/units/' | relative_url }}#running-a-calibration-round).

[Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}) · [Session kits]({{ '/teaching/sessions/' | relative_url }}) · [Lecture plans]({{ '/teaching/lectures/' | relative_url }}) · [Syllabus maps]({{ '/teaching/syllabi/' | relative_url }})

Teaching material: CC BY 4.0, NeuroTrailblazers.
