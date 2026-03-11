---
marp: true
title: "08 Segmentation and Proofreading"
paginate: true
---

# 08 Segmentation and Proofreading
Technical Training: Nanoscale Connectomics

---

## Learning goals
- Classify merge/split/boundary/identity errors.
- Prioritize high-impact corrections.
- Link corrections to QC metrics and logs.

---

## Why proofreading is scientific QC
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S03-01.png)
- Reconstruction quality bounds analysis validity.

---

## Error taxonomy overview
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S08-01.png)
- Track error classes explicitly in correction logs.

---

## Ultrastructure cues for correction
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S06-01.png)
- Local structure guides boundary decisions.

---

## Synapse-aware review
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S09-01.png)
- Avoid corrections that break plausible synaptic context.

---

## Organelle-assisted disambiguation
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S11-01.png)
- Organellar cues reduce false split/merge decisions.

---

## Comparative ambiguity case
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S17-01.png)
- Similar textures can require different corrections.

---

## Boundary failure case
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S23-01.png)
- Preserve unresolved uncertainty instead of over-correction.

---

## Identity checks (axon/dendrite)
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-AXDEN-S13-01.png)
- Identity errors can distort motif and degree statistics.

---

## Edge-case morphology
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-AXDEN-S18-01.png)
- Escalate difficult calls to adjudication queue.

---

## QC metrics and release gates
![w:900](../../../assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S13-01.png)
- Report VI, edge precision/recall, ERL, synapse-centric F1.

---

## Activity
Write one correction log with:
- Error type.
- Before/after rationale.
- Metric delta and confidence note.

---

## Attribution
Frompat figures from Pat Rivlin proofreading decks; outreach figures used for processing context.
