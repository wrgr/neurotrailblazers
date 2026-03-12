---
marp: true
theme: default
paginate: true
title: "Module 13: Machine Learning in Neuroscience"
---

# Module 13: Machine Learning in Neuroscience
Teaching Deck

---

## Learning Objectives
- Build feature pipelines for neuron and synapse-level analyses
- Compare supervised and unsupervised methods for connectomics tasks
- Evaluate model quality with biologically meaningful metrics
- Detect data leakage and distribution-shift risks in connectomics ML

---

## Capability Target
Design and critique an ML analysis pipeline for connectomics that includes feature rationale, evaluation plan, leakage controls, and interpretation limits.

---

## Concept Focus
### 1) Feature engineering defines the hypothesis space
- **Technical:** feature choices encode assumptions about what variation is biologically meaningful.
- **Plain language:** your model can only learn what your features allow.
- **Misconception guardrail:** adding more features always improves science.

---

## Core Workflow


---

## 60-Minute Run-of-Show
1. **00:00-08:00 | Task framing and leakage examples**
2. **08:00-20:00 | Feature rationale workshop**
3. **20:00-34:00 | Split strategy and baseline modeling**
4. **34:00-46:00 | Error analysis and biologically relevant metrics**
5. **46:00-56:00 | Model-card limitation writing**
6. **56:00-60:00 | Competency checkpoint**

---

## Studio Activity


---

## Assessment Rubric
- **Minimum pass**
  - Feature and split decisions are justified.
  - Metrics include at least one biologically targeted criterion.
  - Limitation statement is specific and actionable.
- **Strong performance**
  - Identifies and mitigates likely leakage channels.
  - Uses error analysis to propose next data improvements.
  - Distinguishes exploratory model from deployment-ready model.
- **Common failure modes**
  - Leakage-prone random splits for spatially correlated data.
  - Overfocus on aggregate accuracy.
  - Claims of biological insight unsupported by model diagnostics.

---

## Quick Practice Prompt
For one candidate model, write:
1. one plausible leakage pathway,
2. one metric blind spot,
3. one limitation you would report publicly.

---

## Teaching Materials
- Module page: /modules/module13/
- Slide page: /modules/slides/module13/
- Worksheet: /assets/worksheets/module13/module13-activity.md
