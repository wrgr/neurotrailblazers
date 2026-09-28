---
layout: page
title: "Module 17: model responses"
permalink: /teaching/answers/module17/
slug: module-answers-17
content_type: delivery
description: "Three calibrated claims, a claim-evidence matrix, a results subsection with a hardened legend, a methods paragraph with full provenance and two structured reviewer responses for Module 17's fictional release T17 scenario."
---

[Learner worksheet]({{ '/assets/worksheets/module17/module17-activity.md' | relative_url }}) · [Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module17/' | relative_url }}) · [Module page]({{ '/modules/module17/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 17 worksheet in order. The studio
scenario is fictional: a mouse cortex volume called release T17, in which 1,247 of
12,891 possible excitatory–inhibitory pairs in layer 2/3 are reciprocally connected,
2.1 times the expectation of a degree-preserving null model, at a cleft score threshold
of 50. None of it describes a real dataset. The responses below are one **invented
learner's** work, Kwame Osei (invented), written at the level the content plan calls
**Proficient**: every Minimum line of the kit's rubric met and most Strong lines met,
with each annotation saying which. This page is public and suitable for formative
assessment.

**What this key adds to the scenario, all invented.** A proofread subset of 2,960 pairs
with 241 reciprocal pairs (1.8 times the null); a threshold sweep (1,612 pairs at 30,
1,398 at 40, 1,061 at 60, 842 at 70; enrichment 1.9, 2.0, 2.2, 2.3); a subclass split
(803 of the 1,247 reciprocal pairs involve basket-type interneurons, against 51% of all
possible pairs); and provenance placeholders (imaging resolution, dates, a commit). Every
value derived from these (fractions, expected counts, intervals) was recomputed with
Python. The intervals are Wilson 95% intervals on the observed fraction, divided by the
null's expected fraction with that expectation held fixed; the exemplar says so, because
that choice is a caveat.

The taught session's 08:00 block works on a mock figure set. Where a class uses the
[Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }}) for that, the
facilitator section below gives values computed from the kit's tables.

## Before you start

The two prerequisites are enough. An acceptable question to bring is “How much
uncertainty language is too much?” The answer this module gives: none of it is too much
if each hedge names a specific alternative; all of it is too much if none does.

## Questions this module answers

1. **What is the exact evidence for each claim?** A named figure panel, a metric with an
   effect size and an interval, and the dataset version the number came from; the
   claim-evidence matrix is where this is checked before prose exists.
2. **Where does uncertainty belong in the narrative?** In the same sentence as the number
   it qualifies, in the results, with the interval; the supplement is for the sensitivity
   analysis, not for the caveat.
3. **How should reviewers' methodological concerns be answered?** Quote, respond with
   evidence or a new analysis, and name the manuscript location that changed; when a
   request is declined, give the reason rather than the opinion.

## The task

### 1. Three result claims at three confidence levels

**Strong** (rung: *we measured*):

> In release T17, 1,247 of 12,891 possible excitatory–inhibitory pairs in layer 2/3
> (9.7%) were reciprocally connected, 2.1 times the 594 pairs expected under a
> degree-preserving null model (95% CI 2.0–2.2; Fig. 2a).

**Moderate** (rung: *consistent with*):

> The enrichment is consistent with a property of the circuit rather than of the
> reconstruction: in the proofread subset (2,960 pairs, 23% of the total), reciprocal
> pairs were 1.8 times the null expectation (95% CI 1.6–2.0; Fig. 2b).

**Exploratory** (rung: *suggests*, post hoc):

> A post hoc split by interneuron subclass suggests that pairs involving basket-type
> cells carry most of the excess (64% of reciprocal pairs against 51% of possible pairs;
> Fig. 2c). This comparison was not prespecified and is reported as exploratory.

**Why this meets the rubric.** Each claim carries a number, an interval or an explicit
“no test,” a panel and the version (Minimum line 1). The three rungs are distinct and
named, and the strong claim is not weakened by the two below it (Strong lines 1 and 2).
The arithmetic: 1,247 / 12,891 = 9.67%; 1,247 / 2.1 = 593.8 expected pairs, 4.61% of
possible pairs; the excess is 653 pairs.

**A weak version, and what is missing.** “Reciprocal excitatory–inhibitory connectivity
is a striking and fundamental feature of layer 2/3 circuits (Fig. 2).” No count, no null,
no interval, no version, no rung. “Striking” is doing the work a number should do, and a
reviewer reads it as a warning sign.

### 2. Claim-evidence matrix

| Claim | Figure panel | Metric | Statistical test | Effect size | Dataset version | Caveat |
|---|---|---|---|---|---|---|
| Reciprocal E–I pairs are enriched in L2/3 | Fig. 2a | Reciprocal pairs / possible pairs: 1,247 / 12,891 | Observed count against 1,000 degree-preserving rewirings preserving in-degree, out-degree and class | 2.1× (95% CI 2.0–2.2); 653 excess pairs | T17, cleft score > 50 | A merge between an E and an I arbor manufactures reciprocity in the reported direction; the interval holds the null expectation fixed |
| Enrichment persists in the proofread subset | Fig. 2b | Same metric on pairs with both cells proofread: 241 / 2,960 | Same null on the subset | 1.8× (95% CI 1.6–2.0) | T17, proofread-status table | Proofread cells were not chosen at random; 23% of pairs; the drop from 2.1 is in the direction a merge artifact predicts |
| Basket-type pairs carry most of the excess | Fig. 2c | Share of reciprocal pairs by subclass against share of possible pairs | None: descriptive, post hoc, not corrected for the number of subclasses | 64% vs 51% (803 of 1,247) | T17, automated subclass labels | Post hoc; labels are automated and unvalidated here |

**Why this meets the rubric.** No cell is empty, including the test cell for the
exploratory row, which says “none” and why (Minimum line 1). Each row carries its own
version entry, which is the habit that stops a later reader assuming all numbers came
from one table.

### 3. Results subsection (300–400 words)

> **Reciprocal excitatory–inhibitory pairs are enriched in layer 2/3.** We asked whether
> excitatory and inhibitory neurons in layer 2/3 connect back to each other more often
> than their degrees predict. In release T17, 1,247 of 12,891 possible
> excitatory–inhibitory pairs (9.7%) were reciprocally connected, against 594 pairs
> (4.6%) expected under a degree-preserving null model that preserves each cell's
> in-degree, out-degree and class: an enrichment of 2.1 (95% CI 2.0–2.2; Fig. 2a). The
> interval reflects sampling variation in the observed count with the null expectation
> held fixed; the spread of the null draws themselves is shown in Fig. 2a and is
> narrower. Because a false merge between an excitatory and an inhibitory arbor
> manufactures reciprocity in exactly the reported direction, the count in the full
> volume may overestimate the true number of reciprocal pairs.
>
> The enrichment is consistent with a property of the circuit rather than of the
> reconstruction. In the subset of pairs in which both cells were proofread to axon and
> dendrite completeness (2,960 pairs, 23% of the total), reciprocal pairs were 1.8 times
> the null expectation (241 observed against 134 expected; 95% CI 1.6–2.0; Fig. 2b). The
> proofread subset was not chosen at random, and the smaller ratio is in the direction a
> merge artifact would predict, so with this design we cannot distinguish a modest merge
> contribution from sampling variation.
>
> A post hoc split by interneuron subclass suggests that pairs involving basket-type
> cells carry most of the excess: they account for 64% of reciprocal pairs (803 of 1,247)
> against 51% of all possible excitatory–inhibitory pairs (Fig. 2c). This comparison was
> not prespecified, uses the release's automated subclass labels, and is not corrected
> for the number of subclasses compared. We report it as exploratory and did not test it.
>
> All counts use the release's synapse table at a cleft score above 50. The enrichment
> ranges from 1.9 to 2.3 across thresholds from 30 to 70 and rises with the threshold
> (Supplementary Fig. S2), which is consistent with low-score false positives diluting
> the effect rather than producing it.

That is 344 words. The hardened legend that goes with it:

> **Figure 2. Reciprocal excitatory–inhibitory pairs in layer 2/3 exceed a
> degree-preserving null.** (a) Observed reciprocal pair count (1,247, vertical line)
> against the distribution of counts from 1,000 degree-preserving rewirings of the layer
> 2/3 excitatory–inhibitory graph (mean 594). (b) Enrichment in the full volume (12,891
> possible pairs) and in the proofread subset (2,960 pairs); error bars are 95% binomial
> intervals on the observed count with the null expectation held fixed. (c) Share of
> reciprocal pairs and of all possible pairs by interneuron subclass; descriptive, no
> test. Release T17; synapse table at cleft score > 50; excitatory/inhibitory identity
> and subclass from the release's automated cell-type table; analysis code tag v1.0.

**Why this meets the rubric.** Each paragraph leads with the finding, follows with the
evidence pointer and closes with the caveat. The rungs are *we measured*, *consistent
with* and *suggests*, and the caveats name alternatives (merges, non-random subset,
multiplicity) rather than hedging in general (Strong lines 1 and 2). The legend can be
read without the main text: version, method variant, parameters, n and the uncertainty
indicator are all in it (Minimum line 2).

**A weak version, and what is missing.** A paragraph that reports “p < 0.001” with no
effect size, moves the interval to the supplement, and closes with “these results
clearly demonstrate that reciprocal inhibition is a design principle of cortex.” The
number a reader needs to judge the headline is not in the sentence with the headline,
and the closing claim is functional; nothing in a synapse count tests it.

### 4. Methods paragraph with full provenance

Every value below is invented for the fictional release T17 (resolution, dates, cell
counts, seed, build number). The point is which fields are present, and the learner's
paragraph must carry real ones.

> **Dataset and provenance.** We analyzed release T17 of a serial-section electron
> microscopy volume of adult mouse primary visual cortex (one animal; strain, age and
> preparation as documented in the release), imaged at 8 × 8 × 40 nm; the analyzed
> subvolume spans layer 2/3 over 250 × 250 × 150 µm. Neurons were segmented by the
> release's automated pipeline (build 3.1) and proofread by the release team. We used the
> segmentation, synapse table and cell-type table as materialized in release T17 (frozen
> 2026-01-15); every root ID in this paper is valid at that materialization only.
> Synapses were taken from the release's synapse table at a cleft score above 50 on its
> 0–255 scale, the release's documented default; results at 30, 40, 60 and 70 are in
> Supplementary Fig. S2. Excitatory/inhibitory identity and interneuron subclass came
> from the release's automated cell-type table. Cells whose soma lay within 15 µm of the
> volume boundary were excluded; counts by class are in Supplementary Table S1. The
> proofread subset comprises pairs in which both cells were proofread to axon and
> dendrite completeness at T17. The degree-preserving null rewired the
> excitatory–inhibitory graph 1,000 times, preserving each cell's in-degree, out-degree
> and class, with random seed 17. Analysis code is at [repository URL], tag v1.0,
> commit [hash]; the conda environment file and every parameter, including the ones
> above, are in `config/t17_reciprocity.yml` at that commit.

**Why this meets the rubric.** Dataset identifier and version, pipeline and build,
proofreading state, code tag and commit, environment, all parameters, exclusion criteria
with their justification location: the Concept 5 checklist is complete (Minimum line 3,
Strong line 3). The paragraph was drafted before the results, which is why the results
subsection can cite the threshold and the subset without defining them.

**A weak version, and what is missing.** The run-of-show's deliberately incomplete
section: “Synapses were obtained from the CAVE synapse table and filtered by cleft
score. Motifs were counted in Python and compared with a random null model.” A reader
cannot pick the dataset, the version, the threshold, the null's constraints, the code or
the exclusions. Asked to reproduce it, they could do nothing.

### 5. Two mock reviewer comments

**Reviewer A.**

> *Reviewer:* “The cleft score threshold of 50 seems arbitrary. How sensitive are results
> to this choice?”
>
> *Response:* We agree that the threshold needed justification and a sensitivity analysis,
> and we have added both. The value 50 is the release's documented default for its 0–255
> score, and we now show the score histogram (new Supplementary Fig. S2a). We reran the
> full analysis at thresholds of 30, 40, 60 and 70 (Supplementary Fig. S2b). The
> enrichment is 1.9, 2.0, 2.1, 2.2 and 2.3 at 30, 40, 50, 60 and 70 respectively, with
> 1,612, 1,398, 1,247, 1,061 and 842 reciprocal pairs. The direction of the change,
> rising with the threshold, is consistent with low-score false-positive synapses
> diluting the enrichment rather than producing it, and we say so with that hedge.
>
> *Manuscript changes:* Methods, “Dataset and provenance,” sentence 5 (threshold
> justification and pointer). Results, paragraph 4, new (the sensitivity sentence).
> Supplementary Fig. S2 (new). Discussion, paragraph 2, one sentence noting that no
> threshold in the range reverses the finding.

**Reviewer B.**

> *Reviewer:* “The authors should compare their findings to FlyWire data to demonstrate
> generality.”
>
> *Response:* We thank the reviewer for raising generality, and we have not run the
> comparison, for three reasons we now state in the manuscript. First, the manuscript
> makes no claim of generality: the result is from one volume of one animal, and the
> Discussion now says so explicitly. Second, the classes compared here, layer 2/3
> excitatory neurons and cortical interneuron subclasses, have no counterpart in an
> insect brain, so a matched comparison would require a different question rather than
> the same analysis on a second dataset. Third, a cross-dataset comparison of a
> null-model enrichment depends on matched cell-type definitions, synapse detection and
> null constraints; that is a separate study, and we identify it as future work.
>
> *Manuscript changes:* Discussion, paragraph 3, new sentence: “This result describes a
> single volume of one animal; whether reciprocal excitatory–inhibitory enrichment
> generalizes across regions or species requires matched cell-type definitions and null
> models, which we have not attempted.” No change to Results.

**Why this meets the rubric.** Both responses quote, respond with evidence or a stated
reason, and name the location of every change (Minimum line 4, Strong line 4).
Reviewer B's request is declined without calling it wrong: the response gives the reason
a comparison would not answer the question and adds a sentence bounding the claim.

**A weak version, and what is missing.** “We disagree with Reviewer A; 50 is the
standard threshold in the field. Reviewer B's suggestion is outside the scope of this
paper.” No new analysis, no location, no reason a reader could check. It is persuasive
to the authors and to nobody else.

## Working checklist

Evidence inventory: the three claims and the matrix (sections 1 and 2). Methods first:
section 4 was drafted before section 3. Results: section 3. Legend hardening: the
Figure 2 legend. Limitation pass: the caveat column and the closing sentence of each
results paragraph. Peer-review simulation: section 5. No step skipped.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | Reciprocal E–I pairs are enriched 2.1× over a degree-preserving null. | 1,247 observed against 594 expected; 95% CI 2.0–2.2 (Fig. 2a). | The interval holds the null expectation fixed. A null whose draws spread widely would widen it; the draws are shown so a reader can judge. |
| 2 | The enrichment is not mainly a merge artifact. | 1.8× in the proofread subset (Fig. 2b). | The subset is not random and the ratio dropped in the artifact's direction. A merge-injection test at a known rate would settle how much of the drop merges explain. |
| 3 | The sensitivity to the threshold is monotone and does not reverse the finding. | 1.9–2.3× across 30–70 (Fig. S2). | The sweep covers one score scale of one release. A different detector would need its own sweep. |

**Confidence:** Medium. The headline rests on one null model in one volume; the proofread
subset supports it but shares the same synapse table and detector.

**Alternative considered and rejected:** reporting the subclass split as a finding with
a test. Rejected because it was chosen after seeing the data, and a p-value on a post hoc
split among several subclasses would overstate the evidence.

## Misconception self-check

Feedback for each error:

- **The methods section is a formality to write last.** Ask: “Which threshold does your
  results paragraph cite, and where is it defined?” If the answer is “nowhere yet,” the
  methods were written last.
- **Stronger language makes weak evidence more convincing.** Replace “striking” with the
  number and ask whether the sentence lost anything.
- **Stating uncertainty makes a paper look weak.** Point to the proofread-subset
  paragraph: naming the merge mechanism is what makes the 2.1 believable.
- **Readers will know which dataset version you used.** Ask: “Would the count be 1,247 at
  the next release?” No one can say, which is why T17 is in the legend.
- **A link to the code repository makes the analysis reproducible.** Ask for the tag and
  the commit. A link without them points at code that changes.
- **Confidence intervals can live in the supplement as long as the main text reports
  p-values.** Ask which sentence a reader uses to decide whether to trust the headline;
  the interval belongs in that sentence.
- **Citing the original EM paper covers all required attributions.** List the separate
  contributions in the exemplar's methods: imaging, segmentation, proofreading, cell
  typing, synapse detection. Each has its own citation request on a real release.
- **A firm, defensive reply shows confidence in the work.** Compare the weak reply in
  section 5 with the exemplar's Reviewer A response. One added an analysis; the other
  added an adjective.

## Session timing (facilitator reference)

This section has no learner task. Values below come from the
[Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }}) tables, computed
with Python's standard library, for classes that use the kit's three figures as the mock
figure set.

- **08:00–18:00, matrix construction.** A defensible first row from the kit's Figure 1
  heatmap. Claim: the ten L2/3 excitatory types send about a quarter of their synapses
  onto the ten interneuron types. Panel: Fig. 1. Metric: synapse share by postsynaptic
  group, 7,151 of 26,471 synapses (27.0%), against 50.4% onto other L2/3 types. Test:
  none, descriptive. Version: the kit as listed in `assets/kits/manifest.json`. Caveat:
  907 of the 2,500 matrix cells have fewer than 10 connected pairs and are hatched, so no
  claim about an individual hatched cell is supported. The reverse share, interneuron
  types onto L2/3 types, is 7,053 of 42,950 (16.4%).
- **28:00–38:00, methods and provenance.** The incomplete section is reproduced in
  section 4 above with what it fails to let a reader do.
- **38:00–50:00, reviewer responses.** Comment 2 (“847 connections is too small for any
  statistical conclusion”) is the partially mistaken one. The shape of a good response:
  sample size has no meaning apart from effect size and test; the reported interval on
  the 3.2× effect (2.8–3.6 in the run-of-show's invented example) already states the
  precision 847 connections buy; what the reviewer may rightly be asking is whether the
  null's own variance is in that interval, and the response should say whether it is.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** the matrix, because every results sentence was checked against a
  row before it was written, and the exploratory row says “no test” rather than
  inventing one.
- **Weakest part:** the intervals hold the null expectation fixed, which understates
  uncertainty if the null draws spread widely. **Next action:** report an interval that
  includes the null distribution's spread, from the 1,000 draws already run.

## Exit prompt

One results paragraph from the kit's Figure 3 (input synapses by layer, 160 synthetic
excitatory neurons, 40 per layer), with values computed from
`input_synapses_by_layer.csv`:

> Layer 5 excitatory neurons in this synthetic set received a mean of 1,246 input
> synapses against 773 for layer 6 neurons, a difference of 473 synapses (95% bootstrap
> CI 279–665, 10,000 resamples, seed 0; Fig. 3). The counts depend on dendritic
> completeness, and this table carries no per-neuron completeness estimate, so each count
> is a lower bound and the layer difference could partly reflect uneven reconstruction.
> All values are from the Module 16 kit at the version recorded in the site's kit
> manifest, computed with the analysis script at tag v1.0, commit [hash]. Legend
> sentence: n = 40 neurons per layer; violins show the distribution, dots individual
> neurons, and horizontal bars the mean with its 95% bootstrap interval.

## Peer review (swap worksheets)

A reviewer of this exemplar should check that every number in the results subsection
appears in a matrix row with the same panel and caveat. A good question to ask its
author: “If the null draws in Fig. 2a spread from 540 to 650, does your interval of
2.0–2.2 still hold?”

## Feedback guide

This key follows the kit's own tiers rather than a numeric score. In this key,
**Proficient** means every Minimum line met and at least half the Strong lines met, with
the remaining Strong lines named in the self-assessment as next actions.

- **Minimum pass:** claims map to explicit evidence with panel references; legends
  readable without the main text; methods with dataset version, pipeline and key
  parameters; reviewer responses specific and technically grounded.
- **Strong performance:** established findings separated from tentative ones with named
  rungs; limitation language that does not weaken the valid claim; concrete method
  details added; reviewer responses with evidence and manuscript locations.
- **Common failure modes:** narrative claims with no panel; missing versions in captions
  or methods; persuasive but non-technical replies; methods written last with missing
  parameters.

Do not reward a results subsection for hitting 400 words. Do not reward a reviewer
response that agrees with everything; a declined request with a stated reason and a
bounding sentence is the harder skill. Do not penalize a learner whose interval method
differs from the exemplar's when the paragraph says what the interval is. Do reward an
exploratory claim that says “no test” over one with a p-value attached after the fact.
This is a local teaching rubric, not a validated assessment instrument.

For null-model choice see [Module 20]({{ '/modules/module20/' | relative_url }}) and
section 2 of [Technical Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }});
for version records see [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}).
Teaching material: CC BY 4.0, NeuroTrailblazers.
