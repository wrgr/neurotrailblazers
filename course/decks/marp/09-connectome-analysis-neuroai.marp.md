---
marp: true
title: "09 Connectome Analysis and NeuroAI"
paginate: true
---

# 09 Connectome Analysis and NeuroAI
Technical Training: Nanoscale Connectomics

---

## Learning goals
- Define a motif hypothesis and executable query.
- Choose defensible null models.
- Interpret findings without overclaiming.

---

## Motivation
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S10-01.png)
- Use structure as a source of constrained AI priors.

---

## Brain-data framing
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S11-01.png)
- Clarify data representation before analysis.

---

## Reverse-engineering limits
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S12-01.png)
- Structure informs hypotheses but does not prove dynamics.

---

## Workflow overview
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S13-01.png)
Hypothesis -> Query -> Search -> Null comparison -> Interpretation

---

## Motif search framing
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S24-01.png)
- Treat motifs as candidate primitives requiring validation.

---

## Query syntax and tooling
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S42-01.png)
- Human-readable motif syntax improves reproducibility.

---

## Complexity constraints
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S31-01.png)
- Subgraph isomorphism cost shapes feasible analyses.

---

## Benchmark context (historical)
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S32-01.png)
- Treat performance values from 2021 decks as historical baselines.

---

## Throughput and scale caveats
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S33-01.png)
- Revalidate claims against current data/hardware stack.

---

## Comparative motif context
![w:900](../../../assets/images/technical-training/09-connectome-analysis-neuroai/FIG-SRC-21_02388_X_TECHTALK_-S44-01.png)
- Cross-dataset comparisons require aligned preprocessing assumptions.

---

## Failure modes
- Post-hoc hypothesis selection.
- Null-model mismatch.
- Cross-dataset overgeneralization.
- Untracked query/code versions.

---

## Activity
Define:
- 1 motif hypothesis.
- 1 null model.
- 1 success criterion.
- 1 explicit limitation.

---

## Attribution
NeuroAI and outreach visuals are used as historical/technical context; benchmark claims require current revalidation.
