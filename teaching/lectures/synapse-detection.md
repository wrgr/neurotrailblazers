---
layout: page
title: "Synapse Detection: lecture package"
permalink: /teaching/lectures/synapse-detection/
slug: lecture-synapse-detection
content_type: delivery
description: "A 90-minute taught session with slides, instructor cues, a synthetic audit exercise and model answers."
---

**90 minutes including activity.** The existing 39-slide deck supports a longer
discussion or a 50–60 minute talk without the activity. This plan selects slides
rather than asking an instructor to rush through all 39.

- [Open presentation]({{ '/course/decks/marp/out/lectures/synapse-detection.html' | relative_url }})
- [Editable slide source and embedded speaker notes]({{ site.deck_source_base }}/lectures/synapse-detection.marp.md)
- [Learner worksheet]({{ '/teaching/lectures/synapse-detection-activity/' | relative_url }})
- [Instructor model answers]({{ '/teaching/lectures/synapse-detection-answers/' | relative_url }})
- [Short teaching sequence]({{ '/teaching/sequence/' | relative_url }})

## Outcomes and preparation

Learners distinguish localization, partner assignment and sign inference; calculate
precision and recall with explicit denominators; explain why class-dependent misses
bias counts; and write a defensible audit plan for a released table.

Before class, read [Synapse Detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }})
and review the worksheet/key. Learners need the Introduction session's claim framework
and arithmetic with fractions. Provide paper or a text editor and a calculator.
**No accounts, downloads of real volumes, or coding are required.**

## Timed plan and instructor cues

- **0–10 min, slides 1–3, 9:** ask what can fail between finding a cleft and adding
  a directed graph edge. Collect localization and partner errors separately. A
  correct cleft location does not certify the assigned cells.
- **10–20 min, slides 13–15:** compare evaluation units. Ask learners to name the
  denominator before quoting any performance number. SynEM's published operating
  thresholds and connection rule matter; aggregation does not guarantee improvement.
- **20–30 min, slides 17–18, 21–23:** discuss evaluation domain and sign. Ask which
  error could change a class ratio even when precision is high. Expected response:
  unequal recall. Keep the published H01 example separate from today's invented data.
- **30–40 min, slides 26–29:** narrate the count correction and its assumptions.
  Ask “Where did recall come from, and does it apply here?” If that is unknown, a
  corrected number is a conditional estimate, not recovered truth.
- **40–65 min:** pairs complete worksheet sections 1–3. Pause the deck so learners
  can see the input counts. At minute 55, check that misses appear in the recall
  denominator, not the precision denominator.
- **65–80 min, slides 33–34:** pairs draft section 4 and exchange audits. A sample
  of predictions alone cannot measure missed synapses. Require independently
  annotated regions, matching rules and a version record.
- **80–90 min, slides 35–37:** debrief with the key, then collect the exit ticket.
  Ask for one claim the audit supports and one it leaves unresolved.

Slides 4–8, 10–12, 16, 19–20, 24–25 and 30–32 are optional extension material;
38–39 hold references and credit. Slide numbers include the cover. Allow additional
time if using the method-history tables or detailed cross-species discussion.

## Instructor cautions

Do not call an F1 score “accuracy.” Do not transfer a paper's performance estimate
to a new tissue without validation. Distinguish a binary connection from its number
of contacts. Multiple contacts may change edge-level recall as well as precision,
depending on thresholding and correlated errors.

The worksheet intentionally assumes perfect sign labels and known validation
counts. Ask which assumption fails in real work before interpreting the corrected
ratio. The reference page and deck cover additional sign and domain-shift issues.

## Assessment and next session

Use the model key's four-dimension rubric. Collect both arithmetic and the written
audit. Learners revise the study brief from Introduction to name the table's version,
its evaluation domain and the error that most threatens their endpoint.

Continue with [Tools and Methods]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }})
for acquisition and reproducibility, then [Algorithms and Applications]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }})
for graph inference. This standalone session is not EN.585.781 Module 8.

## Sources and credit

The deck carries its scientific references. The performance-unit comparison is
grounded in [Staffler et al., SynEM, Table 3 and Figure 5](https://elifesciences.org/articles/26414)
and the [CREMI evaluation definitions](https://cremi.org/metrics/).

Lecture and teaching activity: **CC BY-SA 4.0**, NeuroTrailblazers. H01 cover image:
Lichtman Lab / Harvard and Connectomics at Google, **CC BY 4.0**, Shapson-Coe et al.
(2024), doi:10.1126/science.adk4858. Preserve the separate image attribution.
