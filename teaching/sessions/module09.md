---
layout: page
title: "Session Kit: Module 09: Neuron Morphology and Skeletonization"
description: "Everything needed to run Module 09 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module09/
slug: session-module09
track: career-and-community
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module09.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Produce a skeleton-based morphology summary with at least three descriptors and one explicit limitation. |
| **Learners leave with** | Morphology descriptor table (10 neurons × 5 descriptors) |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-08


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module09.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module09.pptx' | relative_url }}">Download deck (.pptx)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module09/module09-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module09/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-10:00 | Morphology overview | |
| 10:00-24:00 | Skeleton extraction demo | |
| 24:00-38:00 | Descriptor calculation | |
| 38:00-50:00 | Interpretation and caveats | |
| 50:00-60:00 | Competency check | |

## The activity

**Scenario:** You have skeletons for 10 neurons in L2/3 of mouse visual cortex. Your task is to classify them as pyramidal vs interneuron based on morphology alone, then validate against synapse-based classification (excitatory vs inhibitory output synapses).

1. Compute morphological descriptors for all 10 neurons (cable length, branch points, spine density, Strahler number, arbor volume).
2. Create a summary table and scatter plot (e.g., spine density vs cable length).
3. Classify each neuron as pyramidal or interneuron based on morphological criteria.
4. Compare your morphological classification to the synapse-based classification (provided). Do they agree?
5. For any mismatches, investigate: was the morphological measurement affected by reconstruction quality?

**What learners hand in**

- Morphology descriptor table (10 neurons × 5 descriptors)
- Scatter plot with proposed classification boundary
- Classification comparison table (morphology call vs synapse call)
- Brief report on any mismatches and their likely cause

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** A skeleton is a lossless summary of a neuron rather than a representation that discards surface geometry and spine shape.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Morphological measurements are comparable across cells that were proofread to different levels.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Total dendritic length is a property of the neuron rather than a property of the reconstruction of that neuron.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A cell type assigned from morphology alone needs no corroboration from connectivity or molecular identity.
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

- **Minimum pass**: Valid skeleton and descriptor set for all neurons. At least 3 descriptors.
- **Strong performance**: Robust interpretation linking descriptors to cell-type identity. Explicit uncertainty framing for borderline cases. Investigation of mismatches.
- **Common failure to flag**: Descriptor list without biological context — reporting numbers without explaining what they mean for the neuron's identity.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behaviour within one session.

## Exit prompt

Explain one morphology feature that could be confounded by reconstruction quality.

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
