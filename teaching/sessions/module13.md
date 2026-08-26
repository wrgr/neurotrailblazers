---
layout: page
title: "Session Kit: Module 13: Machine Learning in Neuroscience"
description: "Everything needed to run Module 13 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module13/
slug: session-module13
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module13.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4-5 hours |
| **Capability target** | Design and critique an ML analysis pipeline for connectomics that includes feature rationale, evaluation plan, leakage controls, and interpretation limits. Concretely: choose a split strategy from the leakage channels present in your data rather than from convention, pick metrics from the decision the model will support, quantify how much of your reported performance survives a harder split, and write a limitation statement specific enough that a reader knows which uses of your model you would refuse. |
| **Learners leave with** | Feature and split design sheet with the leakage channel named for each split choice |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Basic scikit-learn workflow familiarity
- Feature matrix handling in Python

Pre-class preparation set for learners:

- Read [neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) so you know what the labels mean before you model them.
- Bring a small labeled table of your own, or use the supplied fragment set.
- Be ready to state, in one sentence, the decision your model would support.

## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module13.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module13.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module13/module13-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module13/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | Task framing and leakage examples | |
| 08:00-20:00 | Feature rationale workshop | |
| 20:00-34:00 | Split strategy and baseline modeling | |
| 34:00-46:00 | Error analysis and biologically relevant metrics | |
| 46:00-56:00 | Model-card limitation writing | |
| 56:00-60:00 | Competency checkpoint | |

## The activity

**Scenario:** You must classify neurite fragments into coarse categories to prioritize a proofreading queue. You have roughly 4,000 labeled fragments drawn from about 600 neurons in one dataset, five classes with prevalences of approximately 38%, 27%, 19%, 12%, and 4%, and a reviewer team that can inspect 500 segments per week. A second, differently stained dataset is available as a held-out domain.

1. Propose a feature set with a one-line rationale per feature, and flag any feature that could encode dataset identity.
2. Design the split, naming the leakage channel each choice blocks and the cost you accept for it.
3. Train one baseline and one improved model, or write the pseudocode plan if compute is unavailable.
4. Report two standard metrics, one biologically targeted metric tied to the 500-segment review capacity, and per-class recall with prevalence.
5. Sample 20 misclassified fragments, classify the failure reason by hand, and propose the one data improvement that would fix the largest group.
6. Draft a model limitation statement naming at least three unsupported uses.

**What learners hand in**

- Feature and split design sheet with the leakage channel named for each split choice
- Metric table including per-class recall, prevalence, and precision at *k* = 500
- Error-analysis tally of 20 hand-classified failures
- Limitation statement with supported and unsupported uses

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** Adding more features always improves science.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** One summary metric is enough.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A random split always gives a valid generalization estimate.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A 99% accurate classifier is a useful classifier.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** The training labels are the truth the model is failing to reach.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"

## Naming the norm

Every session is a chance to make one piece of the hidden curriculum explicit.
Pick a moment where you would normally just *do* the professional thing, and say
out loud why you are doing it — then ask whether anyone was taught that.

For this session, the candidate is whichever norm the activity most depends on:
stating an assumption in the same sentence as the claim, recording the version a
number came from, or saying "uncertain" and having it count as a real answer.
See [the hidden curriculum]({{ '/hidden-curriculum/' | relative_url }}) for the
collected set and why naming them is a fairness intervention rather than etiquette.

## Assessment

- **Minimum pass**
- **Strong performance**
- **Common failure modes**

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

For one candidate model, write:
1. one plausible leakage pathway,
2. one metric blind spot,
3. one limitation you would report publicly.

## If this session goes wrong

- **Nobody talks in the debrief.** You asked "any questions?" Ask instead: "Which
  cue would you drop first if the data got worse?"
- **Everyone finishes early.** They are pattern-matching, not judging. Give an
  ambiguous case where the answer is "uncertain" and see what happens.
- **Nobody finishes.** The scaffolding came off too fast. Work the next case
  together rather than pressing on.
- **A learner is silently lost.** The most likely cause is unstated vocabulary.
  Point them at the [dictionary]({{ '/technical-training/dictionary/' | relative_url }}) and check back.

---

*[All session kits]({{ '/teaching/sessions/' | relative_url }}) · [Facilitator guide]({{ '/teaching/facilitator-guide/' | relative_url }})*
