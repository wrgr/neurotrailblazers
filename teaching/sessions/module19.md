---
layout: page
title: "Session Kit: Module 19: Peer Review and Scientific Ethics"
description: "Everything needed to run Module 19 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module19/
slug: session-module19
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module19.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Produce a technically rigorous manuscript review and an ethics-risk decision memo for a connectomics study, including actionable recommendations and integrity safeguards. Students will be able to distinguish constructive criticism from destructive criticism, identify the specific ethical challenges that arise in large-scale connectomics collaborations, and make documented decisions when facing ambiguous integrity situations. |
| **Learners leave with** | Structured review form (claims, methods audit, evidence gaps, interpretation audit) |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Ability to interpret methods/results sections
- Basic understanding of reproducibility and QC terms


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module19.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module19.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module19/module19-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module19/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | Constructive vs destructive criticism | |
| 08:00-12:00 | What reviewers look for in connectomics | |
| 12:00-28:00 | Methods-evidence audit exercise | |
| 28:00-38:00 | Ethics-risk scan | |
| 38:00-50:00 | Decision memo drafting | |
| 50:00-58:00 | Peer review of reviews | |
| 58:00-60:00 | Competency check | |

## The activity

**Scenario:** Your team is acting as reviewers for a connectomics preprint claiming a novel circuit motif --- a specific three-neuron feed-forward inhibitory loop --- with translational implications for understanding epilepsy. The preprint uses MICrONS minnie65 data (CAVE materialization v661) and reports 3.5x enrichment of this motif relative to a degree-preserving random graph null model (p < 0.001 after Bonferroni correction across 13 three-node motif classes). The methods section does not report the synapse confidence threshold, does not mention boundary neuron handling, and lists "MICrONS Consortium" as a co-author without individual contribution details. The discussion section states that "this motif likely plays a causal role in seizure propagation."

1. Write one methods critique (specific: what is missing, why it matters, what the authors should add) and one interpretation critique (specific: which sentence overclaims, what the bounded version would say).
2. Identify two ethics risks: (a) the authorship/attribution concern and (b) one additional concern (selective reporting, consent, data sharing, or responsible AI). For each, draft a concrete mitigation recommendation.
3. Draft a decision memo: accept with revisions, major revisions, or reject. Justify your recommendation by referencing your specific concerns.
4. Propose one concrete integrity policy improvement for the project team (e.g., a contribution tracking system, a preregistration requirement, a threshold sensitivity analysis mandate).

**What learners hand in**

- Structured review form (claims, methods audit, evidence gaps, interpretation audit)
- Ethics-risk memo with two identified risks and concrete mitigations
- Decision memo with recommendation and traceable rationale
- One-paragraph integrity policy proposal

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** "interesting result" is not a substitute for methodological soundness. A novel finding reported with inadequate methods documentation is worse than an incremental finding reported transparently.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Ethics in connectomics is not just about IRB approval. It extends to data sharing, attribution, responsible AI, and honest reporting throughout the research lifecycle.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** "interesting result" is not a substitute for methodological soundness.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Being harsh is not the same as being rigorous. The most rigorous reviews are also the most specific and constructive.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Compliance checklists alone do not ensure good practice. Integrity requires ongoing attention to workflow transparency.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Contribution volume alone does not define authorship role. A person who proofread 10,000 segments may deserve authorship; a person who ran one analysis script may not. The criteria must be explicit and agreed upon in advance.
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
  - Review comments are specific and evidence-linked (referencing figure panels, methods details, or specific sentences).
  - Ethics risks are identified with concrete mitigations tied to workflow practices.
  - Recommendation is consistent with documented findings.
- **Strong performance**
  - Distinguishes fixable technical issues from fundamental validity failures.
  - Balances rigor with constructive tone and practical revision advice.
  - Uses transparent criteria for authorship/integrity judgments.
  - Anticipates author responses and pre-addresses potential objections.
- **Common failure modes**
  - Generic critique with no evidence references ("the statistics are weak").
  - Ethics discussion disconnected from actual workflow practices.
  - Inconsistent recommendation versus identified risks (e.g., listing major concerns but recommending accept with minor revisions).
  - Destructive tone that undermines the credibility of valid criticisms.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

Choose a connectomics abstract (from a real paper or the mock preprint) and produce:
1. One high-priority methods concern (what is missing, why it matters, what should be added).
2. One interpretation concern (which sentence overclaims, what the bounded version would say).
3. One ethics/integrity concern (tied to a specific workflow practice, not an abstract principle).
4. One actionable revision request for each of the above, written in constructive language.

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
