---
marp: true
title: "07 Glia"
paginate: true
---

# 07 Glia
Technical Training: Nanoscale Connectomics

---

## Learning goals
- Distinguish astrocyte, microglia, and oligodendrocyte cues.
- Reduce glia-neuron boundary errors in proofreading.

---

## Why glia matter operationally
Glia labels directly affect segmentation quality and downstream interpretation.

---

## Unit opener context
![w:900](../../../assets/images/technical-training/07-glia/FIG-RIV-GLIA-S01-01.png)
- Frame glia as central structural context, not background.

---

## Astrocyte context cues
![w:900](../../../assets/images/technical-training/07-glia/FIG-RIV-GLIA-S03-01.png)
- Combine morphology with neighborhood evidence.

---

## Microglia context cues
![w:900](../../../assets/images/technical-training/07-glia/FIG-RIV-GLIA-S09-01.png)
- Require multi-slice confirmation in ambiguous regions.

---

## Oligodendrocyte cue context
![w:900](../../../assets/images/technical-training/07-glia/FIG-RIV-GLIA-S15-01.png)
- Track myelin-related structural relationships.

---

## Myelin-producing glia context
![w:900](../../../assets/images/technical-training/07-glia/FIG-RIV-GLIA-S16-01.png)
- Use local architecture to disambiguate class identity.

---

## Ambiguity and escalation
- Tag uncertainty type before adjudication.
- Use second-pass review queue for low-confidence calls.

---

## QC metrics
- Glia-vs-neuron boundary error rate.
- Class-level agreement by region.
- Unresolved-case rate after secondary review.

---

## Failure modes
- Over-calling microglia from partial morphology.
- Under-prioritizing glia corrections in proofreading triage.

---

## Activity
Classify 2 ambiguous regions with:
- class label,
- key cues,
- uncertainty note.

---

## Attribution
Figures derived from Pat Rivlin MICrONS proofreading training materials (111821).
