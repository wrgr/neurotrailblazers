---
marp: true
title: "03 EM Prep and Imaging"
paginate: true
---

# 03 EM Prep and Imaging
Technical Training: Nanoscale Connectomics

---

## Learning goals
- Understand prep-to-imaging chain.
- Identify artifact classes and downstream impact.

---

## Acquisition chain
Fixation -> Staining -> Sectioning/Block-face -> Imaging -> Stack assembly

---

## Artifact classes
- Physical: tears, folds, chatter, compression.
- Signal: charging, contrast drift.
- Geometric: misalignment and seam artifacts.

---

## Why artifacts matter
Acquisition defects propagate to segmentation merges/splits and topology errors.

---

## QA gates
- SNR and intensity drift checks.
- Seam residual monitoring.
- Missing/damaged section tracking.

---

## Pilot-first strategy
Run pilot segmentation before full-volume ingestion.

---

## Failure modes
- Late QA discovery.
- Missing acquisition metadata.
- Throughput-over-fidelity decisions without quantified cost.

---

## Activity
Create a risk register with 3 artifacts, metrics, and mitigation triggers.

---

## Bridge
Next unit: infrastructure that operationalizes this data at scale.
