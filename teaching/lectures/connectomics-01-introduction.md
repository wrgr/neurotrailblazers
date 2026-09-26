---
layout: page
title: "Lecture 1: Introduction to Connectomics"
description: "Why synapse-resolution structure needs electron microscopy, what a wiring diagram can and cannot establish, the three scales, and the state of the field through 2025."
permalink: /teaching/lectures/connectomics-01-introduction/
slug: lecture-connectomics-01-introduction
track: core-concepts-methods
content_type: delivery
pathways:
  - classroom delivery
  - graduate teaching
summary: "What a connectome is, what it can and cannot establish, and where the field stands."
---

*Lecture 1 of the [connectomics lecture series]({{ '/teaching/lectures/' | relative_url }}).
59 slides in three parts, about 150 minutes. Openly licensed under **CC BY-SA 4.0**.*

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/en585781/module07-introduction-to-connectomics.html' | relative_url }}">Open the deck (HTML)</a>
    <a class="resource-link" href="https://github.com/wrgr/neurotrailblazers/blob/main/course/decks/marp/en585781/module07-introduction-to-connectomics.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/teaching/lectures/' | relative_url }}">Series overview</a>
    <a class="resource-link" href="{{ '/teaching/lectures/introduction-activity/' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/teaching/lectures/introduction-answers/' | relative_url }}">Instructor model responses</a>
  </div>
  <p><small>The HTML deck presents directly in a browser. The Markdown source carries the
  speaker notes as HTML comments and is what to edit if you want to change wording.
  See <a href="{{ '/teaching/lectures/' | relative_url }}#formats">Formats</a> for PowerPoint and Google Slides.</small></p>
</div>

## Learning objectives

By the end of this lecture, participants will be able to:

1. **Explain** why synapse-resolution structure requires electron microscopy, using the resolution and data-volume arithmetic.
2. **Differentiate** acquisition, reconstruction, and analysis scale for a stated research question.
3. **Classify** a connectivity claim as supported by structure alone, by structure plus a declared assumption, or not by structure.
4. **Communicate** the current challenges and opportunities in connectomics without overclaiming.

## Teach a 90-minute session

This selected-slide route includes an activity and debrief. It is a shorter
alternative to the full 150-minute lecture below. Slide numbers include the cover.
Use the [four-session block]({{ '/teaching/sequence/' | relative_url }}) to follow
this session with Synapse Detection.

**Preparation:** open the deck, review the worksheet/key, and provide paper or a
text editor plus a calculator. No accounts or coding are needed. The worksheet
uses invented data and must not be presented as a real dataset result.

- **0–5 min, slides 1, 4, 10:** introduce the outcome and collect initial votes on
  the three claims. Ask for reasons; do not resolve the votes yet.
- **5–20 min, slides 7, 11–14, 18–22:** define the connectome and evidence needed
  for a contact, then teach the claim bins. Return to the votes. Distinguish a
  physiological inference from a directly counted anatomical contact.
- **20–30 min, slides 28–29, 35:** compare acquisition, reconstruction and analysis
  scale. Ask “What is the unit in your conclusion?” A cell-pair conclusion needs
  partner identity, not just a count of image features.
- **30–40 min, slides 23–24:** narrate the repaired research question. Make the
  denominator and non-claim explicit. Ask learners to suggest a result that would
  weaken the proposed explanation.
- **40–65 min:** pairs complete the [worksheet]({{ '/teaching/lectures/introduction-activity/' | relative_url }}).
  At minute 50, check whether anyone has mistaken mean count per connected pair
  for mean count per eligible pair. Do not require a significance test on four pairs.
- **65–80 min:** spend 10 minutes exchanging and revising briefs, then 5 minutes
  comparing answers using the [model responses]({{ '/teaching/lectures/introduction-answers/' | relative_url }}).
  Ask what new observation each rejected claim would require.
- **80–90 min, slides 25–26:** collect exit tickets and revised briefs. Preview
  Session 2: the count depends on which contacts the reconstruction missed.

The unselected slides are extension material for this route. Slides 58–59 carry
references and credit. The full-course assignment on slide 56 is **not** an extra
requirement for this short session; use the worksheet brief instead.

**Assessment:** use the key's four-dimension rubric. Prioritize evidence-matched
claims and explicit non-claims over polished prose. Permit a well-justified
“not yet known.”

## Structure

The full, approximately 150-minute route uses all three parts.

### Part A: The case for mapping

The resolution argument in numbers, the cost argument you can do in your head, and the three bins every connectivity claim falls into.

### Part B: Three scales that are not the same thing

Acquisition, reconstruction, and analysis scale; the modality chart and the tradeoff triangle; representations, registration, and scale leakage.

### Part C: The field as it stands

Forty years of milestones tagged by stream, the landmark datasets and what each actually delivered, open problems, and how to read a connectomics paper.

## What students produce

A one-page **study brief** on a question the student cares about: a measurable endpoint with units, a null model stated in words, and an explicit non-claim.

## The centerpiece

The claim-sorting framework in Part A. It is introduced here, used in every later lecture, and is what the lecture 3 lab is graded against. Students tend to treat lecture 1 as background and skip to the tools, so say out loud that the rest of the series depends on this part.

## Notes for whoever teaches it

**The cold open pays off twelve slides later.** Slide 10 puts three claims about the same circuit to the room and leaves them unresolved until slide 22. Take a show of hands on each. Expect the room to accept the first and split on the second. Anyone who accepts the third because it sounds like something they have read is the point of the exercise.

**Part A ends on a constructive turn, not a limitation.** Students hear "structure cannot establish this" as "connectomics cannot do anything interesting". The right reading is that it tells you exactly which additional experiment your question needs. MICrONS exists because someone decided to co-register two-photon physiology with the EM volume.

**The decision rule dislodges a common instinct.** Learners arrive assuming nanoscale is the serious scale. The rule is the *coarsest* acquisition scale that resolves the analysis unit. Choosing EM at 4 × 4 × 40 nm when 1 µm light microscopy answers the question multiplies the voxel count about 1.5 million times.

## License and credit

**CC BY-SA 4.0.** Teach from this lecture anywhere, including commercially; copy and
redistribute it in any medium; and re-cut, shorten, translate, or merge it into your own
material. No permission needed. Two conditions: credit the original and say if you
changed anything, and distribute your adapted version under
[the same license]({{ '/teaching/lectures/' | relative_url }}#license).

> Gray Roncal, W. (2026). *Introduction to Connectomics* (EN.585.781 Frontiers in Neuroengineering,
> Module 7). NeuroTrailblazers. CC BY-SA 4.0.
> https://neurotrailblazers.org/teaching/lectures/

For an adaptation, prefix with *"Adapted from"* and note what you changed.

The H01 cover image retains **CC BY 4.0**, with credit to Lichtman Lab / Harvard
and Connectomics at Google, Shapson-Coe et al. (2024), doi:10.1126/science.adk4858.
Preserve that separate attribution when adapting the deck.

Found something wrong or out of date, or built a version worth sharing back?
[Open an issue](https://github.com/wrgr/neurotrailblazers/issues).

## Related

- [Series overview]({{ '/teaching/lectures/' | relative_url }})
- [Lecture 2: Tools and Methods]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }})
- [Lecture 3: Algorithms and Applications]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }})
- [Technical training units]({{ '/technical-training/' | relative_url }}): the long-form material behind these slides
- [Journal club]({{ '/technical-training/journal-club/' | relative_url }}): papers and discussion prompts
