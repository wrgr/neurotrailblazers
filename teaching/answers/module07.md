---
layout: page
title: "Module 07: model responses"
permalink: /teaching/answers/module07/
slug: module-answers-07
content_type: delivery
description: "Worked triage of the Module 07 kit's 45-flag error report, before/after metrics from qc_metrics.py, and an exemplar release memo that resolves a metric disagreement."
---

[Learner worksheet]({{ '/assets/worksheets/module07/module07-activity.md' | relative_url }}) · [Module 07 kit]({{ '/assets/kits/module07/README.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module07/' | relative_url }}) · [Module page]({{ '/modules/module07/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 07 worksheet in order. It uses the
[Module 07 kit]({{ '/assets/kits/module07/README.md' | relative_url }}): the 45-row
`error_report.csv`, the instructor-only `ground_truth.csv` and `qc_metrics.py`. The kit
is **synthetic teaching data**, not a real segmentation. Every metric value below was
produced by running `qc_metrics.py` from the kit folder with the fix list shown. This
page is public and suitable for formative assessment.

**Instructor note.** This key names which flags are real errors, using the kit's ground
truth. Learners should commit their rankings from the error report alone before they see
this page or the ground-truth file.

## Before you start

Modules 01–06 supply the vocabulary used here: merge, split, segment, synapse table and
materialization version. A learner missing those should read the
[error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }})
before the triage step.

## Questions this module answers

1. **Which errors most affect biological conclusions?** The ones that change the
   endpoint. For reciprocal connectivity among the 60 L2/3 pyramidal analysis cells,
   those are merges and splits on analysis cells inside the region of interest. In this
   kit, glial and out-of-region flags change the endpoint little or not at all.
2. **What thresholds justify release versus rework?** Thresholds written down before
   proofreading, on the metric that matches the endpoint. When two prespecified metrics
   disagree, the memo says which one the question depends on.

## The task

### 1. Review the automated error report

The report has 45 flags: 18 merges, 20 splits and 7 uncertain. Each row gives the
putative class, whether the segment is in the analysis region, its synapse count, a
detector score and a note. State what the report cannot tell you: the kit records 1,250
error sites that were never flagged (`unflagged_error_sites` in `kit.json`). The 45 rows
are flags, not the errors in the volume.

### 2. Triage

**Reasoning pattern.** For each flag, ask three questions. Is the segment an L2/3
pyramidal cell in the analysis region? Could the error create a false reciprocal pair
(a merge that gives one object synapses in both directions with another cell) or hide
a real one (a split that detaches an axon carrying synapses)? Does the note give
evidence of an error, or only a possibility?

Applied to the kit's 45 rows, using only what the report shows:

| Tier | Flags | Count | Reasoning from the report |
|---|---|---|---|
| High: fix | Merges E06, E08, E24, E26, E31, E32, E36, E38, E43 | 9 | Pyramidal, in region, 204–439 synapses; notes give direct evidence (two somata, smooth branch on a spiny arbor, soma count 2). Can create false reciprocal pairs. |
| High: fix | Splits E11, E16, E35, E37, E39, E45 | 6 | Pyramidal, in region; the main axon ends abruptly. A detached axon hides that cell's outputs, including reciprocal partners. |
| Review before editing | Uncertain E02, E03, E12, E13, E18, E21, E40 | 7 | Pyramidal, in region, high impact if real. Low detector scores (0.33–0.48) and ambiguous notes. Send to a second look; do not edit blind. |
| Medium | Splits E17, E22, E28 | 3 | Pyramidal, in region, but distal dendrite branches with 20–34 synapses. Fewer edges at stake than an axon. |
| Medium | Merges E04, E09, E42 | 3 | Interneuron merges. They do not enter the pyramidal-to-pyramidal graph but corrupt circuit context. |
| Low | E01, E15 (merges); E10, E14, E44 (splits) | 5 | Pyramidal but outside the analysis region, at the volume edge or corner. |
| Low | Glia: E05, E19, E20, E25, E27, E29, E33, E34, E41 | 9 | Glial objects. The three astrocytic-sheet merges fused to axons (E19, E20, E41) are the only ones worth a later look. |
| Low | Unknown fragments E07, E23, E30 | 3 | Orphan axon fragments with 3–5 synapses and no soma in the volume. |

The tiers sum to 45. Three example triage lines, as a learner would write them:

- **E06, merge, high.** Two somata in one pyramidal object in the region; the merged
  object could appear to both send to and receive from the same partner.
- **E11, split, high.** Main axon of an analysis cell ends in a low-contrast stretch
  with a continuation three sections on; its outputs are missing from the graph.
- **E05, split, low.** Glial sheet in pieces; no synapses; no effect on the endpoint.

### 3. Fix the top 15 errors

The 15 high-tier flags form a defensible ranking: **E06, E08, E11, E16, E24, E26, E31,
E32, E35, E36, E37, E38, E39, E43, E45**. None of them is a non-error, so no budget is
wasted (`fixes_spent_on_non_errors` is empty).

Example log entries (segment IDs from the report):

| Flag | Before | After | Rationale |
|---|---|---|---|
| E06 | 7955 (merged with 7389) | 7955 and 7389 as separate cells | Two somata in one object joined by a thin bridge near z = 259. |
| E11 | 9381 (axon ends at z = 523) | 9381 joined to its continuation | Axon resumes three sections on; the continuation's ID is recorded from the viewer. |
| E24 | 7064 (merged with 9734) | 7064 and 9734 separate | Soma count 2; caliber drops from 0.9 to 0.2 µm at z = 584. |

On paper, verification means saying what you would check: an orphan piece left after a
split, or an extra fragment absorbed by a merge, in two orthogonal views.

**What the ground truth shows (instructor only).** Of the seven uncertain flags, E02 and
E12 are not errors, and the other five are real (E03, E21 and E40 merges; E13 and E18
splits). The highest F1 any 15 fixes can reach is **0.952**. An exhaustive search of every
15-flag combination finds it: E03, E06, E11, E13, E16, E21, E24, E35, E36, E37, E38, E39,
E40, E43 and E45. That set trades four report-backed fixes for four uncertain flags that
turned out to be real. A learner could not have known that from the report. Do not
grade toward it. Do credit a learner who sent the uncertain flags to review and ranked
them next.

### 4. Compute before/after metrics

The thresholds were set before proofreading. They are the ones the run-of-show
introduces and the kit tells learners to test: **run length above 30 µm and edge F1 above
0.80**. Commands, run from the kit folder:

```bash
python3 qc_metrics.py
python3 qc_metrics.py --fixed E06,E08,E11,E16,E24,E26,E31,E32,E35,E36,E37,E38,E39,E43,E45
```

| Indicator | Before | After 15 fixes | Threshold | Call |
|---|---|---|---|---|
| Edge precision | 0.729 | 0.923 | — | — |
| Edge recall | 0.833 | 0.955 | — | — |
| Edge F1 | 0.777 | 0.939 | > 0.80 | **Pass** (failed before) |
| False edges / missed edges | 124 / 67 | 32 / 18 | — | — |
| Reciprocal pairs counted (true: 40) | 44 | 42 | — | — |
| of which spurious | 17 | 4 | — | — |
| Real pairs hidden by splits | 13 | 2 | — | — |
| Run-length proxy | 27.0 µm | 27.3 µm | > 30 µm | **Fail** |
| Flagged error sites on analysis cells | 23 | 8 | — | — |

**The disagreement is the point.** The run-length proxy divides 36,000 µm of
analysis-cell path by the number of runs: 60 cells plus 1,250 unflagged error sites plus
the flagged sites that remain. Before: 36,000/1,333 = 27.0 µm. After: 36,000/1,318 =
27.3 µm. Even with all 23 flagged sites fixed, 36,000/1,310 = 27.5 µm, so **no set of
flag fixes can pass 30 µm**. The proxy is dominated by errors the detector never
flagged. Edge F1 is measured on the connections the analysis uses, and the targeted
fixes moved it from 0.777 to 0.939.

Also note what the baseline hides: the count of 44 reciprocal pairs is close to the true
40, but 17 of the 44 are spurious and 13 real pairs are missing. A count that looks right
can be wrong in both directions at once. After the fixes, 4 spurious and 2 hidden pairs
remain.

The kit's run-length proxy is not the ERL of Funke et al.; `kit.json` says so. A
learner's memo should call it a proxy.

### 5. Release recommendation memo

> **Metrics.** After 15 fixes, edge F1 is 0.939 (threshold 0.80, pass; baseline 0.777).
> The run-length proxy is 27.3 µm (threshold 30 µm, fail; baseline 27.0). The analysis
> counts 42 reciprocal pairs, down from 44.
>
> **Corrections.** Nine merges and six axon splits, all on L2/3 pyramidal analysis cells in
> the region, each logged with segment IDs and the evidence in the flag note.
>
> **Remaining risks.** Seven uncertain flags on analysis cells are unreviewed. Three
> distal-dendrite splits and three interneuron merges remain. About 1,250 unflagged error
> sites remain in the volume, which is why the run-length proxy cannot pass.
>
> **Recommendation: go for the reciprocal-connectivity analysis only, conditional on
> review of the seven uncertain flags. No-go for any analysis that depends on long
> continuous reconstructions.** The question is about connections among the analysis
> cells. Edge F1 measures exactly that and passes. The run-length proxy fails because of
> errors the detector never flagged; that failure is a property of the whole volume, not
> of the connections being counted. Report both numbers, state which one the question
> depends on, and do not reuse this release for morphology.

A **rework** recommendation is also acceptable if the learner argues that a failed
prespecified threshold blocks release until the policy is revised, and says who revises
it. Grade the reasoning, not the verdict. Do not accept a memo that reports only the
passing metric.

## Working checklist

Classify and prioritize: the triage table. Apply: the 15-flag fix list and log. Verify:
the orphan and absorbed-fragment check. Record: the metrics table and memo. A rework
recommendation must name the error categories to work next, such as the seven uncertain
flags, and an effort estimate.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | The subvolume is fit for the reciprocal-connectivity analysis after review. | Edge F1 0.939 against a prespecified 0.80; spurious reciprocal pairs down from 17 to 4. | Any of the seven unreviewed uncertain flags could be real. Review might change the pair count. |
| 2 | The run-length failure does not bear on this endpoint. | The proxy moved only from 27.0 to 27.3 µm while F1 rose by 0.16. It is dominated by unflagged sites. | If the analysis depended on tracing whole arbors, this would be the deciding metric. |
| 3 | The reciprocal count is still not exact. | Four spurious pairs and two hidden pairs remain after the fixes. | Only the kit's ground truth shows this. In a real volume it would need an independent reference region. |

**Confidence:** Medium. The F1 call rests on one line of evidence, the script's
re-measurement, and unreviewed flags remain.

**Alternative considered and rejected:** fixing the seven uncertain flags first because
they are all on analysis cells. Rejected because two of them could be non-errors (the
notes say “membrane looks continuous”), and an edit without evidence can create an error.

## Misconception self-check

- **Proofreading ends when the data look right.** Feedback: “The baseline counted 44
  reciprocal pairs against a true 40. Did it look wrong?” It is an allocation problem
  under a budget of 15.
- **One aggregate score is enough.** Feedback: “Run length failed and F1 passed. Which
  one measures the connections your question counts?” A single score hides that
  disagreement.
- **Throughput measures annotator performance.** Feedback: “If two of your 15 fixes were on
  non-errors, how would you know without a second annotator?” Report agreement alongside
  counts.
- **A result can omit proofreading level.** Feedback: the memo must say which cells were
  corrected and which flags remain, or a reader cannot judge the pair count.

## Session timing (facilitator reference)

This section has no learner task. The run-of-show now uses the kit.

- **10:00–24:00, queue classification.** Pairs rank rows **E01–E12** only. A defensible
  top five from the report: E06, E08 and E11 (pyramidal, in region, direct evidence),
  then E03 (uncertain, high impact if real; review it) and one of the in-region
  interneuron merges, E04 or E09. E01 is outside the region, E05 is glia, E07 is an orphan
  fragment, E10 is at the edge, and E02 and E12 have notes saying the membrane looks
  continuous.
- **24:00–38:00, correction sprint.** With `--fixed E03,E06,E08,E09,E11`, edge F1 goes
  from 0.777 to **0.812** and the reciprocal count to 41 (12 spurious, 11 hidden). E09
  and E04 change nothing in this metric; E03 is a real merge. With only E06, E08 and E11,
  F1 is 0.803.
- **38:00–50:00, thresholds.** The warm-up already shows the disagreement: F1 passes 0.80
  after five fixes while the run-length proxy reads 27.1 µm.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** the triage ties each flag to reciprocal connectivity, and the memo
  resolves the metric disagreement against the question.
- **Weakest part:** seven uncertain flags are unreviewed. **Next action:** send them to a
  second annotator and rerun the script with any confirmed fixes.

## Exit prompt

> A merge error must be fixed before release when it joins two cells in the analysis
> population and the merged object has synapses in both directions with another analysis
> cell, because it can create a reciprocal pair that does not exist. In the kit, 17 of the
> baseline's 44 reciprocal pairs were of that kind.

Other acceptable rules name an axon split on an analysis cell, which can hide a real
pair. Reject a rule that names only error size or visual salience.

## Peer review (swap worksheets)

A reviewer should rerun the partner's fix list with `qc_metrics.py` and check that the
numbers match the memo. A good question: “If E03 and E21 turn out to be merges, does your
recommendation change?”

## Feedback guide

This key follows the kit's own tiers.

- **Minimum pass:** triage consistent by type and impact; a release decision justified
  by metric values; a correction log present.
- **Strong:** impact reasoning tied to reciprocal connectivity; uncertainty stated and
  carried into the decision; the metric disagreement named and resolved against the
  question.
- **Failure to flag:** ad hoc corrections without a policy; a recommendation with no
  metric values; thresholds changed after the metrics were seen.

Do not reward fixing glial flags because they are visually dramatic. Do not reward
editing E02 or E12 on the detector's word. Do not reward lowering the run-length
threshold to 27 µm after seeing 27.3 µm; that is moving the goalposts. Do not reward a
learner for matching the instructor-only best set. Do reward an honest “unreviewed”
entry. This is a local teaching rubric, not a validated assessment instrument.

For metric definitions see [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }})
and [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).
Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
