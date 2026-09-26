---
layout: page
title: "Synapse Detection: instructor model responses"
permalink: /teaching/lectures/synapse-detection-answers/
slug: synapse-detection-answers
content_type: delivery
description: "Worked detection metrics, conditional count correction and a synapse-table audit exemplar."
---

[Learner worksheet]({{ '/teaching/lectures/synapse-detection-activity/' | relative_url }}) · [Lecture plan]({{ '/teaching/lectures/synapse-detection/' | relative_url }})

All calculations below use the worksheet's **synthetic counts**, not a published dataset.

## 1. Metrics

- **E precision:** 80/85 = **94.1%**. Recall: 80/100 = **80.0%**.
  F1: 160/185 = **86.5%**.
- **I precision:** 40/45 = **88.9%**. Recall: 40/80 = **50.0%**.
  F1: 80/125 = **64.0%**.
- **Accuracy cannot be computed:** true negatives and a defined negative universe
  are absent. F1 is not accuracy.
- **108/120 = 90%** is partner correctness conditional on successful detection.
  It omits the 60 missed reference contacts. Under the exercise's one-to-one matching
  and requirement that both partners be correct, end-to-end partner-pair recall is
  **108/180 = 60%**. Do not use 90% as the full pipeline's recall.

## 2. Count correction

Observed E fraction: **85/(85+45) = 65.4%**. Using unrounded fractions:

- E estimate: 85 × (80/85) / (80/100) = **100**.
- I estimate: 45 × (40/45) / (40/80) = **80**.
- Corrected E fraction: 100/(100+80) = **55.6%**, down **9.8 percentage points**.

More I contacts were missed proportionally. Correcting the lower I recall adds
relatively more I contacts, reducing the E fraction. This is an anatomical count
exercise, not a physiological E/I measurement.

Recovery of the totals is algebraic here: the same reference counts generated both
the table and its precision/recall estimates. It is **not an independent validation**.
Transfer to another table assumes representative class-specific error estimates,
consistent matching/threshold rules and stable class labels. Estimates also have
sampling uncertainty. Sign misclassification would require a richer error model.

## 3. Repaired claim

“In the reviewed region, the predicted table's E fraction is 65.4%. Under the
exercise's validated class labels and measured detection errors, the reference
fraction is 55.6%. These counts do not establish physiological balance or performance
in other regions.”

Accept other wording that makes the population and assumptions explicit. Reject a
claim that a corrected point estimate eliminates uncertainty.

## 4. Example audit plan

Record the release/materialization identifier, reconstruction version, detection
threshold, query date and region boundaries before sampling. Prespecify spatially
distributed validation regions, including difficult image conditions. Annotate all
reference contacts in them independently of the predictions, adjudicate ambiguous
contacts, and retain the adjudication record.

Match predictions one-to-one under a documented distance and identity rule. Report
TP, FP and FN separately by class and region. Check both partners, reporting
conditional assignment performance separately from end-to-end performance. Keep
training/tuning regions separate from evaluation regions.

Report denominators and uncertainty, accounting for clustering within regions or
neurons rather than treating every contact as independent. State which tissues and
regions the validation represents. A convenience sample can support a pilot audit,
not a universal error bound. Multiple regions from one brain are not independent brains.

Inspecting existing rows can find false positives and partner mistakes. It cannot
discover missing rows without an independent search of the tissue. Postpone an E/I
claim if class-specific recall is unmeasured or the conclusion changes under plausible
error rates. A defensible “not yet known” is a successful audit outcome.

## Feedback guide

Score **0–2 each** for metric denominators, correction and assumptions, claim scope,
and an audit capable of finding misses. Two means explicit and correct, one means a
recoverable omission, zero means absent or contradictory. A proficient response has
at least 6/8 and no zero in claim scope or the ability to measure misses. This is a
teaching rubric, not a validated instrument. Accept sensible alternative sampling
plans when their limits are stated.

For the distinction between contact and connection evaluation, see
[Staffler et al., Table 3](https://elifesciences.org/articles/26414). For a concrete
partner matching convention, see [CREMI metrics](https://cremi.org/metrics/).
Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
