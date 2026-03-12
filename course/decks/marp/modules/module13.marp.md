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

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Agenda (60 min)
- 0-10 min: Frame and model
- 10-35 min: Guided practice
- 35-50 min: Debrief and misconception correction
- 50-60 min: Competency check + exit ticket

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
- See module page for details.

---

## 60-Minute Run-of-Show
- **00:00-08:00 | Task framing and leakage examples**
- **08:00-20:00 | Feature rationale workshop**
- **20:00-34:00 | Split strategy and baseline modeling**
- **34:00-46:00 | Error analysis and biologically relevant metrics**
- **46:00-56:00 | Model-card limitation writing**
- **56:00-60:00 | Competency checkpoint**

---

## Misconceptions to Watch
- **Misconception guardrail:** adding more features always improves science.
- **Misconception guardrail:** one summary metric is enough.
- **Misconception guardrail:** random split always gives valid generalization estimates.

---

## Studio Activity


---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

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

## Exit Ticket
For one candidate model, write:
1. one plausible leakage pathway,
2. one metric blind spot,
3. one limitation you would report publicly.

---

## References (Instructor)
- Januszewski et al. (2018) for segmentation ML context.
- UMAP paper (McInnes et al., 2018) for embedding interpretation caveats.
- MICrONS/FlyWire analyses for realistic distribution-shift context.

---

## Teaching Materials
- Module page: /modules/module13/
- Slide page: /modules/slides/module13/
- Worksheet: /assets/worksheets/module13/module13-activity.md
