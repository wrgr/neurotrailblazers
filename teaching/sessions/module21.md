---
layout: page
title: "Session Kit: Module 21: Reproducibility and FAIR Principles in Connectomics"
description: "Everything needed to run Module 21 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module21/
slug: session-module21
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module21.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4-5 hours |
| **Capability target** | Publish a reproducibility-ready connectomics package (data + methods + metadata + limitations) that an external group can audit and reuse. |
| **Learners leave with** | FAIR metadata form |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Basic data-processing workflow familiarity
- Basic manuscript methods section familiarity


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module21.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module21.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module21/module21-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module21/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-06:00 | Framing: the silent bug | |
| 06:00-16:00 | The five-element checklist, modeled | |
| 16:00-30:00 | Guided practice: audit your own work | |
| 30:00-40:00 | Clean-environment rerun | |
| 40:00-50:00 | Known limitations, written honestly | |
| 50:00-57:00 | Competency check | |
| 57:00-60:00 | Exit ticket | |

## The activity

**Scenario:** Your lab plans to release a connectomics analysis package to collaborators.

1. Build a FAIR metadata sheet for one analysis output.
2. Create a reproducibility checklist with pass/fail criteria.
3. Draft a "known limitations" section and one deprecation note.
4. Peer-test another team's package for reuse friction.

**What learners hand in**

- FAIR metadata form
- Reproducibility checklist + validation log
- Reuse friction report with remediation recommendations

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** Posting files online makes work FAIR.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A notebook that ran end-to-end once is proof of reproducible science.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Reproducibility norms are common sense that any careful trainee will infer without being taught.
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
  - All five provenance elements present: dataset release ID, materialization number, code commit hash, environment specification, parameter configuration.
  - Re-run instructions testable by a peer without contacting the author.
  - Limitations name concrete failure modes, excluded samples, and failed runs rather than generic hedges.
- **Strong performance**
  - Clean-environment rerun actually attempted, with a friction log and remediations ordered by cost.
  - Hidden norms made explicit: version identifiers in figure legends, a changelog, and a deprecation note.
  - ID churn quantified whenever identifiers cross versions, and reported in the methods.
  - Documentation is audit-friendly: an external reader can locate every provenance element from the README alone.
- **Common failure modes**
  - Missing version identifiers for data or code.
  - Methods that omit key parameters or the environment specification.
  - "Reproducible in principle" claims without a validation rerun.
  - Limitations sections written as boilerplate rather than as concrete guidance.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

Take one prior analysis output and add:
1. provenance metadata,
2. reproducibility instructions,
3. a 5-line limitations section.

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
