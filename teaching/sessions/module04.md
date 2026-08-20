---
layout: page
title: "Session Kit: Module 04: Neuroanatomy for Connectomics"
description: "Everything needed to run Module 04 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module04/
slug: session-module04
track: career-and-community
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module04.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Interpret a local EM region using correct anatomical context and document one confident and one uncertain structural call. |
| **Learners leave with** | Completed annotation table (patch ID, layer call, structure call, evidence, confidence) |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-03


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module04.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module04.pptx' | relative_url }}">Download deck (.pptx)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module04/module04-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module04/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-10:00 | Macro-to-micro bridge | |
| 10:00-24:00 | Guided structural identification | |
| 24:00-38:00 | Ambiguity case discussion | |
| 38:00-50:00 | Learner annotation round | |
| 50:00-60:00 | Debrief and competency check | |

## The activity

**Scenario:** You are given a set of 8 EM patches from a mouse cortex volume. The patches span different layers (L1 through L6) but are presented without layer labels.

1. For each patch, determine the likely cortical layer using soma density, neuropil texture, and cell-type signatures.
2. Identify the dominant cell type and compartment type in each patch.
3. For each call, record the evidence chain and confidence level.
4. Identify 2 patches where you are most uncertain and explain what additional information would help.
5. Compare your annotations with a partner and resolve disagreements.

**What learners hand in**

- Completed annotation table (patch ID, layer call, structure call, evidence, confidence)
- Two uncertainty notes with proposed resolution strategies
- One "lesson learned" about how context changed an interpretation

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** Cortical layer can be read off a single EM patch without soma density or neuropil context.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** The hippocampal laminar logic transfers to neocortex because both are cortex.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** An atlas coordinate is a ground-truth location rather than a registered estimate with a residual.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Annotation confidence should be uniform across a volume, when boundaries and volume edges are systematically harder.
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

- **Minimum pass**: Context-aware call and confidence note for each patch. Layer identification is reasonable (within ±1 layer).
- **Strong performance**: Clear rationale linking EM features to layer context. Uncertainty is explicit and well-reasoned. Cross-slice evidence cited.
- **Common failure to flag**: Isolated local cue overconfidence — making a definitive call from a single feature without checking layer context or neighboring slices.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behaviour within one session.

## Exit prompt

Describe one case where anatomy context changes your interpretation of an EM structure.

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
