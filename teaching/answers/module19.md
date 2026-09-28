---
layout: page
title: "Module 19: model responses"
permalink: /teaching/answers/module19/
slug: module-answers-19
content_type: delivery
description: "A worked review of the Module 19 kit's fictional mock preprint: methods and interpretation critiques, two ethics risks with mitigations, a decision memo and an integrity policy, with misconception feedback."
---

[Learner worksheet]({{ '/assets/worksheets/module19/module19-activity.md' | relative_url }}) · [Module 19 kit]({{ '/assets/kits/module19/README.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module19/' | relative_url }}) · [Module page]({{ '/modules/module19/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 19 worksheet in order. It reviews the
[Module 19 kit]({{ '/assets/kits/module19/README.md' | relative_url }})'s
`mock-preprint.md`, using the paragraph labels ([M1], [R2], [D1]) its review form asks
for. The preprint is **fictional**: its authors, its volume, its release T19, its
consortium and every number in it were written for this exercise, and nothing in it is
a finding about any dataset. The review below treats it as a submitted manuscript
because that is the exercise. This page is public and suitable for formative
assessment.

**Instructor note.** The kit's README lists the four seeded issues. Learners should
complete the review form before reading the README's key or this page.

## Before you start

The prerequisites are reading a methods section and knowing the QC vocabulary from
Modules 17–18: merge, split, synapse confidence threshold, boundary neuron,
materialization version. A learner missing those should read
[Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
before the audit step.

## Questions this module answers

1. **What makes a review technically useful instead of opinion-based?** Each comment
   names a location ([M1], Figure 2), says what is missing or wrong, says why it
   changes the claim, and says what the authors should do. The kit's Comment 1 has all
   four parts; Comment 2 has none.
2. **Where do integrity risks appear in large-scale connectomics projects?** In the
   workflow, not the approval file: a threshold chosen after seeing results, a motif
   tested and not reported, a contributor list that names a group and no people.
3. **How should authorship and credit be managed in consortium settings?** With
   written criteria agreed before results exist, a contribution record kept from the
   start, and individual contributions stated in the paper for every author,
   including the members of any group author.

## The task

### 1. Methods critique and interpretation critique

**Methods critique.**

> [M1] states that synapses “were taken from the public synapse table” and that an
> edge is one or more synapses, but gives no synapse confidence threshold and no rule
> for neurons whose arbors leave the volume. Both change the edge list the motif count
> is built on. Low-confidence synapse predictions concentrate in exactly the
> one-synapse edges that an “at least one” rule admits, and a neuron cut by the
> boundary loses partners on one side, which changes its in- and out-degree and so
> the degree-preserving null itself. Please state the confidence threshold used,
> re-run the count at a second threshold (at least two synapses per edge is the usual
> choice) and report both, and state how many of the 2,114 neurons touch the boundary
> and whether they were kept, flagged or excluded.

Three further gaps a strong review adds, in priority order:

- [M2] gives one null. A degree-preserving null does not preserve cell-type
  composition or distance. Because E-to-I and I-to-E edges are common, a loop with an
  interneuron in the middle can look enriched from type composition alone, and
  because interneuron arbors overlap their neighbors densely, from proximity alone.
  Ask for the count under a cell-type-stratified null and a distance-preserving null.
- No proofreading status, merge or split rate, or synapse-detection precision and
  recall is reported. Without them, the reader cannot judge whether 1,812 loops are
  wiring or reconstruction.
- No version identifier beyond “release T19,” no code, no derived edge list. A reader
  cannot reproduce Figure 1.

**Interpretation critique.**

> [D2] reads: “Given that disruption of feed-forward inhibition is observed in
> epilepsy, this motif likely plays a causal role in seizure propagation.” The study
> counted a wiring pattern in one volume from one healthy animal. It measured no
> activity, no seizure and no perturbation, so no causal claim is available from it.
> The bounded version: “Feed-forward inhibitory loops are more frequent in this
> volume than a degree-preserving null predicts. Whether their frequency or
> distribution differs in epileptic tissue, and whether they contribute to seizure
> propagation, would require comparison tissue and functional measurement.”

[D1] overclaims in the same way one sentence earlier: “establish” and “a dominant
organizing principle of visual cortex” from one motif in one volume. The bounded
version replaces “establish” with “find” and “visual cortex” with “this volume.”
The abstract's last sentence repeats [D2] and adds “candidate target for
anti-epileptic therapy,” which has no support in the paper at all.

### 2. Two ethics risks and mitigations

**(a) Authorship and attribution.** The author list includes “the Data Release
Consortium,” and the contributions section says only that the consortium
“contributed to this work.” A reader cannot tell who did what, whether the consortium
members meet authorship criteria, or whether the people who proofread the 2,114
neurons are among them. *Mitigation:* require a contributions statement that lists
every individual author with their roles in a standard taxonomy such as CRediT, and
for the group author, a linked list of its members and the contribution each made
(data generation, proofreading, curation). If the consortium's role was providing the
release, the journal's convention is usually an acknowledgment and a data citation,
not authorship; the authors should say which applies and why.

**(b) Selective reporting.** [M3] says three motifs were tested: the feed-forward
inhibitory loop, the reciprocal excitatory pair and the disinhibitory chain. The
results discuss one. The other two are not mentioned again, in any direction. The
abstract compounds this: it reports Bonferroni correction “across 13 motif classes,”
which does not match the three tests [M3] declares. Either 13 tests were run and
three were declared “of prior interest” afterwards, or the correction was miscounted;
the paper cannot have it both ways. *Mitigation:* report all tested motifs in one
table with observed count, null mean, sd, effect size and corrected p, whatever the
result, and state the true number of tests, including thresholds tried. Going
forward, preregister the motif list and the threshold before the count is run.

The checklist's other two items: **human tissue** does not apply (the volume is
mouse), though the animal-care approval is not stated and should be; **data sharing**
fails as written (no version, code or derived tables), which is the third methods gap
above and belongs in the revision request.

### 3. Decision memo

> **Summary of contribution.** The manuscript counts three-node motifs among 2,114
> neurons in a fictional cortical EM volume (release T19) and reports that a
> feed-forward inhibitory loop occurs 1,812 times against a degree-preserving null
> mean of 518 (SD 41), a ratio of 3.5. If the count holds up, a motif census at this
> scale with a stated null is a useful contribution.
>
> **Major concerns.**
> 1. *Methods, fixable.* No synapse confidence threshold and no boundary rule [M1];
>    no proofreading status, error rates or detection precision and recall; no
>    version, code or edge list. Each is a reporting gap the authors can close.
> 2. *Validity, potentially fundamental.* [R2] and Figure 2 show twelve interneurons
>    carrying more than half of all 1,812 loops. A merge error on an interneuron
>    fuses two cells' partner lists and manufactures exactly this signature. The
>    authors should report soma counts and a morphology check for those twelve cells,
>    and recount with them excluded. If the enrichment depends on them, the headline
>    result may be a reconstruction artifact, and no amount of rewriting fixes that.
> 3. *Null model, fixable but decisive.* A single degree-preserving null [M2] does not
>    separate loop-specific wiring from cell-type composition or proximity. The 3.5
>    ratio may shrink substantially under a type-stratified or distance-preserving
>    null; the paper's claim depends on which survives.
> 4. *Interpretation, fixable.* [D1] and [D2] and the abstract's last sentence claim
>    establishment, dominance and causation from a count in one volume. The bounded
>    versions are given above.
> 5. *Integrity, fixable.* Three motifs tested, one reported [M3]; the “13 motif
>    classes” in the abstract does not match; the group author has no individual
>    contributions.
>
> **Minor concerns.** Figure 2 has no error bars or uncertainty of any kind. “p <
> 0.001” with 1,000 rewirings is the floor of a permutation test, not a measured
> value; report the observed z and the number of rewirings. The abstract's therapy
> sentence should be removed.
>
> **Recommendation: major revisions.** The counting method is sound in outline and
> the reporting gaps can be closed. Concern 2 is the one that could turn this into a
> reject: if the loop count collapses without the twelve interneurons, or if the
> ratio falls to near 1 under a type- or distance-preserving null, the central claim
> does not stand and a resubmission would need a different framing. The
> recommendation is conditional on the authors reporting those two analyses, not on
> their outcome. I would expect the authors to reply that the degree-preserving null
> is standard; the answer is that it is the minimum, and the module's own examples
> show a threefold ratio under it falling to near 1 under a type-stratified null.

**Consistency check.** Five major concerns and a “major revisions” verdict are
consistent. “Accept with revisions” would not be, because concern 2 could invalidate
the result. “Reject” would also be defensible if the reviewer argues that a paper
missing threshold, boundary handling, error rates and a version has not yet reported a
checkable analysis; grade the reasoning, not the verdict.

### 4. Integrity policy proposal

> Before any motif count is run, the team files a one-page preregistration in the
> project repository: the data release and version, the synapse confidence threshold
> and the edge rule, the boundary policy, the full list of motifs to be tested, the
> null models with what each preserves, and the correction that will be applied
> across that list. Every count reported in a paper links to that file, and any
> analysis not in it is labeled exploratory. In the same repository, a contribution
> log records who did what from the first proofreading edit, using a fixed role
> taxonomy, and the paper's contributions section is generated from it. The
> preregistration removes the threshold-after-results and motif-after-results paths
> this manuscript walked; the log removes the anonymous group author.

### What good looks like

- **Strong:** every comment cites a label or a figure and has problem, evidence and
  fix in that order; the memo separates what the authors can fix by reporting (a
  threshold, a version) from what could sink the result (the twelve interneurons, the
  null); the verdict follows from the concerns; the reviewer says what the authors
  will answer and answers it first.
- **Weak:** “the statistics are weak,” “the claims are overblown,” “the authors should
  do more”; a list of everything wrong with no priority; a verdict that does not
  match the list (five major concerns, “accept with minor revisions”); a review that
  argues with the authors' conclusion rather than auditing their method.

## Working checklist

Pre-review framing: the claim types are one descriptive claim (the count and ratio)
and two explanatory claims ([D1], [D2]); the dataset is a fictional release T19 with
no version detail. Methods-evidence audit: section 1 and major concerns 1–3.
Interpretation audit: the [D1] and [D2] rewrites. Ethics-risk scan: section 2.
Actionable response package: the memo and the policy.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | The methods as written cannot support the enrichment claim. | [M1] states no confidence threshold or boundary rule; [M2] uses one null; no error rates or version are reported. | If the authors supply these and the ratio survives a type- and distance-preserving null, the claim stands at its bounded size. |
| 2 | The loop count may be a merge artifact. | [R2]: twelve interneurons carry more than half of 1,812 loops; a merged interneuron inherits two partner lists. | Twelve cells could be real high-degree interneurons. Soma counts and morphology for those twelve decide it. |
| 3 | The paper selectively reports. | [M3] declares three tests; the results discuss one; the abstract corrects across 13. | The other two motifs may appear in a supplement not included in the excerpt. If so, the abstract's count still needs reconciling with [M3]. |

**Confidence:** Medium. All three claims rest on the text of the excerpt alone;
nothing was recomputed, and the excerpt may omit a supplement.

**Alternative considered and rejected:** recommending reject on the strength of
concern 2. Rejected because the manuscript does not yet show whether the twelve
interneurons are merges; asking for the check is the review's job, and the verdict
should not assume its result.

## Misconception self-check

Feedback for each:

- **An interesting result can make up for thin methods.** Ask: “Could you check the
  3.5 from what [M1] and [M2] give you?” No threshold, no boundary rule, no version:
  the result cannot be checked, so its interest is not yet evidence.
- **Ethics in connectomics is covered once the IRB or animal-care approval is in
  hand.** The mock paper's ethics problems are a contributions section and a missing
  motif table. Neither is on any approval form.
- **A review is mainly a judgment of how well the story is told.** The story here is
  told well: clear motif, clean figure, a disease link. Ask which sentence of the
  methods the reviewer read first. It should be [M1].
- **The harshest review is the most rigorous one.** Compare the kit's Comment 1 and
  Comment 2. The harsh one contains no location, no evidence and no action.
- **A completed compliance checklist guarantees integrity.** The four-item checklist
  in the review form is a starting point; the “13 motif classes” mismatch is found
  only by reading [M3] against the abstract.
- **Contribution volume alone decides authorship.** Ask: “If the consortium
  proofread all 2,114 neurons, are its members authors?” The answer depends on the
  criteria written in advance, which this paper does not have.

## Session timing (facilitator reference)

This section has no learner task.

- **00:00–08:00.** Comment 1 could be acted on tomorrow: it names [M1], says why the
  two gaps change the edge count, and asks for three specific additions. Comment 2
  lacks a location, a reason and a request; the authors could not begin.
- **12:00–28:00.** The three items the audit asks for: (a) methods gap, [M1], no
  confidence threshold and no boundary rule; (b) overclaim, [D2] (or [D1]); (c) the
  figure panel with insufficient uncertainty, Figure 2, which by its own legend shows
  no error bars. Figure 1 shows the null histogram, which is the right way to show
  uncertainty for that count.
- **28:00–38:00.** The two ethics items: the group author without contributions, and
  three motifs tested with one discussed. Strong learners also catch the 3-versus-13
  mismatch and the twelve-interneuron merge check; neither is required.
- **Arithmetic learners may want.** 1,812 / 518 = 3.50; z = (1,812 − 518) / 41 =
  31.6; Bonferroni at 0.05 across 13 tests is 0.0038, across 3 tests 0.017. With
  1,000 rewirings the smallest permutation p is 1/1,001, so “p < 0.001” is the
  resolution limit, not a measurement.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** the memo separates fixable reporting gaps from the one check
  (the twelve interneurons) that could invalidate the result, and the verdict is
  conditioned on that check being reported rather than on its outcome.
- **Weakest part:** the review asks for a distance-preserving null without saying
  what distance data the fictional release provides. **Next action:** ask the authors
  whether soma positions or skeletons are available at T19, and name the null that
  matches.

## Exit prompt

Using the mock preprint:

1. **High-priority methods concern.** [M1] gives no synapse confidence threshold and
   no boundary rule. It matters because both change the edge list and, through
   degrees, the null. Add the threshold, a second-threshold rerun and the boundary
   policy with counts.
2. **Interpretation concern.** [D2], “likely plays a causal role in seizure
   propagation.” Bounded version: “is more frequent than a degree-preserving null
   predicts in this volume; its relevance to seizure propagation is untested.”
3. **Ethics and integrity concern.** [M3] declares three tested motifs and the
   results report one; the abstract corrects across 13. The practice at fault is
   reporting after seeing which test worked.
4. **Revision requests, in constructive form.**
   - “Please state the synapse confidence threshold and boundary policy in [M1],
     rerun the loop count at a second threshold, and report the number of boundary
     neurons kept or excluded.”
   - “Please rewrite [D1] and [D2] to describe the result as an enrichment in this
     volume relative to the stated null, and move the epilepsy link to a clearly
     marked speculation paragraph or remove it.”
   - “Please add a table reporting all three motifs named in [M3] under the same
     null, with corrected p-values, and reconcile the number of tests with the
     correction reported in the abstract.”

## Peer review (swap worksheets)

A reviewer of this review should check that every concern cites a label and that the
verdict follows from the concern list. A good question for its author: “If the
authors report that the twelve interneurons each have one soma and clean morphology,
does your recommendation change, and to what?”

## Feedback guide

This key follows the kit's own tiers.

- **Minimum pass:** review comments cite figure panels, methods details or specific
  sentences; ethics risks come with mitigations tied to workflow practices; the
  recommendation is consistent with the documented findings.
- **Strong performance:** fixable technical issues are distinguished from
  fundamental validity failures; rigor is paired with a constructive tone and
  practical revision advice; authorship and integrity judgments use transparent
  criteria; author responses are anticipated and answered.
- **Common failure modes:** generic critique with no evidence references; ethics
  discussion disconnected from workflow practice; a recommendation inconsistent with
  the risks listed; a destructive tone that undermines valid criticisms.

Do not reward finding all four seeded issues if none has a location and a fix. Do not
reward “reject” as the rigorous verdict by default, or “accept with revisions” as the
kind one; grade whether the verdict follows from the concerns. Do not reward a review
that argues the motif is “probably not real”; the review's job is to name what would
show it. Do reward a learner who marks the human-tissue item not applicable and says
why. This is a local teaching rubric, not a validated assessment instrument.

See [H01 human cortex]({{ '/content-library/case-studies/h01-human-cortex/' | relative_url }})
for the consent and attribution questions a human-tissue paper would raise, and
[Motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }})
for the null models the revision asks for. Teaching material: CC BY 4.0,
NeuroTrailblazers.
