---
layout: page
title: "Module 01: model responses"
permalink: /teaching/answers/module01/
slug: module-answers-01
content_type: delivery
description: "An exemplar question-to-hypothesis sheet, motivation statement, peer feedback and exit prompt for Module 01, with misconception feedback."
---

[Learner worksheet]({{ '/assets/worksheets/module01/module01-activity.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module01/' | relative_url }}) · [Module page]({{ '/modules/module01/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 01 worksheet in order. The worksheet
asks learners to write about their own question and their own motivation, so there is
no single correct answer. The responses below are one **invented learner's** work,
written to show the level of the kit's **Strong** criteria. They are examples, not the
only acceptable wording. This page is public and suitable for formative assessment.

The exemplar uses the fly olfactory pathway on purpose. The module's own worked
example uses mouse CA3, and a key that repeated it would reward copying.

## Before you start

Nothing is required. An acceptable question to bring is “How does a fly tell two
smells apart?” It is broad on purpose. The worksheet narrows it.

## Questions this module answers

1. **What can connectomics answer today?** It can answer structural questions within
   a reconstructed, versioned volume: which cells contact which, with how many
   synapses, and how that compares with a stated baseline.
2. **What claims require additional evidence beyond structure?** Claims about activity,
   synaptic strength, sign in a given state, causation and behavior. They need
   physiology, perturbation or behavioral measurement in addition to the wiring.

## The task

### Question-to-hypothesis sheet (Part A)

1. **Broad curiosity question.** How does a fly's brain turn an odor into a behavior?
2. **Narrowed target.** In the adult fly brain, uniglomerular olfactory projection
   neurons (PNs) from one chosen glomerulus, and their targets in the lateral horn of
   one hemisphere.
3. **Structural measurement.** For two lateral horn cell types, called L1 and L2 here,
   the **connected fraction**: ordered PN-to-target cell pairs with at least one
   synapse, divided by all eligible ordered pairs. Units: connected pairs per eligible
   pair. Secondary: synapses per connected pair. The learner names L1 and L2 from the
   dataset's cell-type annotations; this key does not prejudge which types or which
   result.
4. **Dataset.** FlyWire, queried at one pinned public release. The release identifier
   and query date are recorded with every count.
5. **Non-claim.** A higher connected fraction onto L1 would not show that L1 responds
   to the odor, that the connection is physiologically stronger, or that this pathway
   drives any behavior. Those claims need recording or perturbation.
6. **Falsification condition.** The hypothesis “PNs from this glomerulus preferentially
   contact L1 over L2” fails if the difference in connected fraction is no larger than a
   comparison that holds axon–dendrite overlap fixed would predict. That comparison is
   written down before the counts are inspected. Building it honestly is
   [Module 20]({{ '/modules/module20/' | relative_url }}).

The sheet is scoped for a first milestone within a week: pull all PN-to-L1 and PN-to-L2
pairs for one glomerulus in one hemisphere, record the release version, and inspect
ten pairs in the viewer by Friday.

### Motivation statement (Part B)

An invented exemplar of 216 words:

> I came to connectomics through a smell. My grandmother could name every herb in her
> garden with her eyes closed, and I wanted to know how a nose turns molecules into
> something you recognize. The fly's olfactory pathway is small enough to trace and
> reconstructed well enough in FlyWire to ask a real question: which lateral horn cells
> does each projection neuron actually contact?
>
> My daily work will be proofreading and writing queries. Most of it will not feel like
> discovery. Each merge I fix on a projection neuron axon changes which partners it
> appears to contact, so each correction changes the numerator of the fraction I care
> about. That link is why the tedious part matters.
>
> My plan for the slow weeks has three parts. First, milestones: five projection neurons
> proofread and one pair query running by Friday, then one glomerulus per week. Second,
> rotation: when I have proofread for more than 90 minutes and my error log shows two
> misses in a row, I will switch to writing query code for 30 minutes. Third,
> accountability: every Monday I will send my lab partner the week's count and one error
> that taught me something. If I miss two Mondays in a row, I will ask my mentor to
> rescope the question rather than quietly stop.

This meets the Strong criterion because it names two strategies with triggers (“when …
two misses in a row, I will switch”; “if I miss two Mondays, I will ask”) and ties one
daily task, fixing merges, to the specific measurement.

### Peer review

Example written feedback on a partner's statement:

- **Specificity:** “You name the hippocampus and ‘memory,’ but no measurement or
  first milestone. What would you have finished by Friday?”
- **Sustainability:** “‘I will stay motivated’ is an intention, not a plan. Name what
  you will do and when. For example: when your weekly count falls below a number you
  set, whom will you tell?”

Feedback addresses the statement, not the person, and asks a question the author can
act on.

### What you hand in: the revision

Example revision after feedback: the original falsification condition read “the
hypothesis fails if PNs do not connect to L1.” A partner pointed out that almost any
PN will contact some L1 cell. The revised condition compares the two types against a
prespecified overlap-matched baseline, as written in item 6 above.

## Working checklist

All five steps are complete in the sheet above. Curiosity question: item 1.
Measurable structural hypothesis: items 2–3 and 6. One metric and one limitation:
connected fraction and the non-claim in item 5. First dataset touchpoint: the
one-glomerulus query at a pinned FlyWire release. Motivation statement: Part B.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | FlyWire contains reconstructed PNs and lateral horn neurons with synapse predictions. | The whole-brain reconstruction reported by Dorkenwald et al. (2024), cited on the module page. | Synapses are detected automatically. Low-count edges may be false positives; check a sample by eye. |
| 2 | Connected fraction can be measured for each type pair. | The measurement uses only partner identities and synapse counts within the release. | Types with truncated or unproofread arbors would bias the denominator. Record eligibility rules first. |
| 3 | The first milestone fits in one week. | One glomerulus and two types is a bounded query. | My own speed is unknown. Revise the milestone after the first day's log. |

**Confidence:** Medium. The feasibility claims rest on one strong line of evidence, the
published dataset description, and have not yet been checked by a first query.

**Alternative considered and rejected:** “Map how the whole olfactory system supports
learning.” Rejected because it has no single structural measurement and learning is a
functional claim structure alone cannot carry.

## Misconception self-check

Accept a response that names where the learner nearly made an error. That is more
useful than seven unexplained ticks. Feedback for each error:

- **Tools generate good questions automatically.** “You chose FlyWire first. What would
  you measure in it?” Ask for the measurement before the tool.
- **A completed connectome is a full explanation of behavior.** “Which part of your
  claim would still be true if every synapse were silent?” The non-claim should name the
  functional gap.
- **Broad vision statements are sufficient project plans.** “What will exist on Friday
  that does not exist today?”
- **Excitement at the start is enough.** “What will you do in week six, when the novelty
  is gone?” Point to the trigger-and-action form.
- **Tedium means you chose the wrong field.** “What did the last boring error teach you
  about the segmentation?” Tedium is predictable, not diagnostic.
- **Good annotators never make errors.** Ask the learner to plan an error log rather than
  a promise of accuracy. Expert proofreaders disagree on a share of decisions.
- **My contribution is too small to matter.** Connect one correction to one count, as the
  exemplar does with the numerator.

## Session timing (facilitator reference)

This section has no learner task. It lists the case studies used in the landscape
segment.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** the falsification condition, because it names a comparison and
  was written before any data were seen.
- **Weakest part:** the eligibility rule for truncated arbors is not yet written.
  **Next action:** draft it before running the first query on Monday.

## Exit prompt

> PNs from my chosen glomerulus contact a larger fraction of lateral horn type L1 cells
> than type L2 cells in one hemisphere of the FlyWire adult fly brain. The metric is the
> connected fraction: ordered pairs with at least one synapse over eligible ordered
> pairs, at one pinned release. The caveat is that this is a structural preference; it
> does not show that L1 responds to the odor or drives behavior.
>
> This matters to me because I grew up watching someone recognize plants by smell.
> Tracing how one odor channel fans out is the smallest version of that question I can
> actually answer.

## Peer review (swap worksheets)

A reviewer of this exemplar should note that every claim has evidence and a real
limitation. A good question to ask its author: “How will you decide which L1 and L2
cells are eligible before you see their counts?”

## Feedback guide

This key follows the kit's own tiers rather than a numeric score.

- **Minimum:** organism, region, and a measurement with units (item 3); metric,
  dataset and non-claim consistent with each other (items 3–5); a motivation statement
  that says both why and how.
- **Strong:** a falsification condition naming a specific result (item 6); a first
  milestone that fits in a week; two sustainability strategies with triggers; a
  non-claim that names a functional inference structure cannot support.
- **Failure:** motivation without a measurable output, a question no result could
  contradict, a generic statement (“I like brains”), or claim language beyond the
  measurement's evidence class.

Do not reward polish or length. A plain statement with a trigger-and-action plan
outranks an eloquent one without it. Do not penalize a learner for saying a step is
uncertain when they name what would resolve it. This is a local teaching rubric, not a
validated assessment instrument.

Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
