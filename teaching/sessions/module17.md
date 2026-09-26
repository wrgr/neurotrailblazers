---
layout: page
title: "Session Kit: Module 17: Scientific Writing for Connectomics"
description: "Everything needed to run Module 17 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module17/
slug: session-module17
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module17.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4-5 hours |
| **Capability target** | Produce a manuscript-ready results section (figures, legends, and claims) where each conclusion is traceable to explicit connectomics evidence and stated limitations. Students will also be able to write methods sections with the level of detail required for connectomics reproducibility and respond to peer review with technically precise, non-defensive language. |
| **Learners leave with** | Claim-evidence matrix (complete, with no empty cells) |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Basic statistical interpretation of connectomics outputs
- Ability to read method sections in technical papers


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module17.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module17.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module17/module17-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module17/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | Good writing vs bad writing in connectomics | |
| 08:00-18:00 | Claim-evidence matrix construction | |
| 18:00-28:00 | Results paragraph drafting | |
| 28:00-38:00 | Methods and provenance exercise | |
| 38:00-50:00 | Reviewer response practice | |
| 50:00-58:00 | Peer exchange and feedback | |
| 58:00-60:00 | Competency check | |

## The activity

**Scenario:** You are preparing a short paper section on motif enrichment from a connectome analysis. Your team has identified that reciprocal connections between excitatory and inhibitory neurons in cortical layer 2/3 occur 2.1x more frequently than expected under a degree-preserving null model. The analysis used a fictional mouse cortex volume, release T17, with synapse detection via the release's synapse table (cleft score threshold > 50). A total of 1,247 reciprocal pairs were observed across 12,891 possible excitatory-inhibitory pairs. The volume, the release and every number here are synthetic, invented for this exercise; none describes a real dataset.

1. Draft three result claims from the scenario above, each with different confidence levels (strong, moderate, exploratory).
2. Build a claim-evidence matrix (claim, figure panel, metric, statistical test, effect size, dataset version, caveat).
3. Write a 300-400 word results subsection with calibrated uncertainty language.
4. Write a methods paragraph with full dataset provenance and reproducibility details.
5. Respond to two mock reviewer comments:

**What learners hand in**

- Claim-evidence matrix (complete, with no empty cells)
- Results subsection draft (300-400 words, every claim traceable)
- Methods paragraph with full provenance
- Reviewer response draft with revision notes (structured format: quote, response, manuscript location)

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** The methods section is a formality to write last.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Stronger language makes weak evidence more convincing.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Stating uncertainty makes a paper look weak.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Readers will know which dataset version you used.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A link to the code repository makes the analysis reproducible.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Confidence intervals can live in the supplement as long as the main text reports p-values.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Citing the original EM paper covers all required attributions.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A firm, defensive reply shows confidence in the work.
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
  - Claims map to explicit evidence with figure panel references.
  - Legends contain enough detail for independent interpretation.
  - Methods include dataset version, pipeline, and key parameters.
  - Reviewer responses are specific and technically grounded.
- **Strong performance**
  - Separates established findings from tentative interpretations using calibrated language.
  - Uses limitation language without weakening valid conclusions.
  - Improves reproducibility via concrete method-detail additions.
  - Reviewer responses include evidence and specific manuscript revision locations.
- **Common failure modes**
  - Narrative claims that cannot be traced to figures.
  - Missing dataset/method versioning in captions or methods.
  - Reviewer replies that are persuasive but non-technical.
  - Methods section written as an afterthought with missing parameters.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

Write one results paragraph from a connectomics figure and include:
1. one quantitative claim with effect size and confidence interval,
2. one explicit caveat tied to a known data limitation,
3. one sentence on reproducibility assumptions (dataset version, materialization, code),
4. one figure legend sentence that specifies sample size and uncertainty indicator.

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
