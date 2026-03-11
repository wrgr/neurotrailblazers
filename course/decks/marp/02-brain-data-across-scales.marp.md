---
marp: true
title: "02 Brain Data Across Scales"
paginate: true
---

# 02 Brain Data Across Scales
Technical Training: Nanoscale Connectomics

---

## Learning goals
- Distinguish acquisition scale from analysis scale.
- Select representation and compute plan by hypothesis.

---

## Scale ladder
Mesoscale -> microscale -> ultrastructure

Each level changes what can be reliably measured.

---

## Representation transitions
Volume -> Segmentation -> Skeleton/Mesh -> Graph

Track what is lost or preserved at each conversion.

---

## Registration and uncertainty
- Declare transform class.
- Report residuals by region.
- Propagate uncertainty downstream.

---

## Anisotropy risks
Unequal z-resolution can induce false continuity and boundary errors.

---

## Compute constraints
- Storage growth with resolution.
- I/O bottlenecks.
- Query latency tradeoffs.

---

## Failure modes
- Scale leakage in interpretation.
- Overconfidence in warped alignment.
- Graph-only analyses that drop critical geometry.

---

## Activity
Choose one question and justify minimal sufficient scale + representation.

---

## Bridge
Next unit: acquisition decisions that set data quality limits.
