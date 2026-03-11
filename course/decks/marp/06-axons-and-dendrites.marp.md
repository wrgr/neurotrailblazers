---
marp: true
title: "06 Axons and Dendrites"
paginate: true
---

# 06 Axons and Dendrites
Technical Training: Nanoscale Connectomics

---

## Learning goals
- Classify axons vs dendrites with multi-cue evidence.
- Handle ambiguity with confidence labels and adjudication.

---

## Why this matters
Process-type errors propagate into connectivity graphs and motif results.

---

## Morphology cues
![w:900](../../../assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S01-01.png)
- Start with branch geometry and process caliber trends.

---

## Dendritic feature context
![w:900](../../../assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S08-01.png)
- Evaluate local morphology in neighborhood context.

---

## Axon-related cue context
![w:900](../../../assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S11-01.png)
- Add organelle/synaptic-role information before final class call.

---

## Side-by-side comparison
![w:900](../../../assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S13-01.png)
- Use explicit criteria for each candidate label.

---

## Advanced ambiguity case
![w:900](../../../assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S14-01.png)
- Weighted evidence beats single-cue heuristics.

---

## Edge-case continuity check
![w:900](../../../assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S18-01.png)
- Verify along neighboring slices/branches.

---

## High-complexity cue
![w:900](../../../assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S22-01.png)
- Escalate low-confidence cases to adjudication.

---

## Late-stage synthesis
![w:900](../../../assets/images/technical-training/06-axons-and-dendrites/FIG-RIV-AXDEN-S23-01.png)
- Log alternate hypothesis when uncertainty remains.

---

## QC metrics
- Axon/dendrite confusion matrix.
- Rework fraction after secondary review.
- Impact check on downstream graph summaries.

---

## Activity
Classify 3 ambiguous processes with:
- primary label,
- confidence tier,
- one alternative hypothesis.

---

## Attribution
Figures derived from Pat Rivlin MICrONS proofreading training materials (111821).
