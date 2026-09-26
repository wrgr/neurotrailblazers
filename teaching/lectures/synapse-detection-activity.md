---
layout: page
title: "Synapse Detection: learner worksheet"
permalink: /teaching/lectures/synapse-detection-activity/
slug: synapse-detection-activity
content_type: delivery
description: "Calculate detection metrics and audit a synapse table using synthetic counts."
---

[Lecture and slides]({{ '/teaching/lectures/synapse-detection/' | relative_url }}) · [Four-session block]({{ '/teaching/sequence/' | relative_url }})

**35 minutes plus peer review.** Work in pairs with a calculator. These are
**invented counts**, not H01 measurements. E and I are synthetic class labels whose
assignment is assumed correct. No sign-classification errors occur in this exercise.

## Validation sample

Independent exhaustive annotation of a selected region produces these counts.
Predictions and reference contacts are matched one-to-one under a fixed criterion:

- **E:** 80 true positives, 5 false positives, 20 false negatives.
- **I:** 40 true positives, 5 false positives, 40 false negatives.
- Of the 120 true-positive detections, 108 have both partners assigned correctly.

True positives are matched detections, false positives are unmatched predictions,
and false negatives are missed reference contacts. These counts describe detection;
partner correctness is evaluated separately. No count of true negatives is supplied.

## 1. Detection and partners (10 minutes)

For E and I separately, calculate precision, recall and F1. Show the denominators.
Can you compute accuracy from these inputs? What does 108/120 measure, and why is
it not an end-to-end partner-pair recall?

Use precision = TP/(TP+FP), recall = TP/(TP+FN), and
F1 = 2TP/(2TP+FP+FN).

## 2. Counts and correction (10 minutes)

The predicted table has 85 E rows and 45 I rows. Calculate the observed E fraction.
Then use **estimated count = predicted count × precision / recall** for each class
and recalculate the E fraction. Explain the direction of the change.

Why is recovering the reference totals here not evidence that the correction works
on another region? Name two assumptions needed to apply it to a separate table.

## 3. A claim to repair (5 minutes)

A colleague writes: “Our detector has high precision, so this table establishes
the true E/I balance and the circuit's physiological balance.” Write a defensible
replacement. Separate anatomical class counts from physiological effects.

## 4. A small audit plan (10 minutes)

Specify the table/reconstruction version, sampling unit, independent reference
annotation, matching rule, class-specific metrics, partner checks and uncertainty
reporting. Explain why reviewing only existing table rows cannot estimate recall.
Name one condition under which you would postpone the biological claim.

**Peer review:** exchange audits. Check whether missed contacts could enter the
sample. Ask whether several regions from one brain justify a claim about many brains.

**Exit ticket:** “The most consequential unknown in this table is ___; I would
measure it by ___.” Submit the calculations and revised claim with the audit plan.

**Carry forward (3 minutes, during the debrief):** add two or three sentences to your
Introduction study brief. Name the synapse table's version, its evaluation domain,
the detection or partner error that most threatens your endpoint, and the evidence
that would resolve it. Bring the revised brief and this audit to Session 3.

[Instructor model answers]({{ '/teaching/lectures/synapse-detection-answers/' | relative_url }})
are public. Attempt the worksheet first. Teaching activity: CC BY-SA 4.0, NeuroTrailblazers.
