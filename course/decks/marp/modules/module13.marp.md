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
Design and critique an ML analysis pipeline for connectomics that includes feature rationale, evaluation plan, leakage controls, and interpretation limits. Concretely: choose a split strategy from the leakage channels present in your data rather than from convention, pick metrics from the decision the model will support, quantify how much of your reported performance survives a harder split, and write a limitation statement specific enough that a reader knows which uses of your model you would refuse.

---

## Concept Focus
### 1) Feature engineering defines the hypothesis space
- **Technical:** feature choices encode assumptions about what variation is biologically meaningful. For a neurite-fragment classifier a defensible starting set is skeleton path length, mean and variance of caliber, branch count, tortuosity, synapse count as presynaptic and as postsynaptic partner, and mitochondrial volume fraction — each of which corresponds to a cue a human annotator actually uses. Every feature you add also adds a way for the model to identify the *dataset* rather than the *biology*: raw intensity statistics, for instance, encode staining batch almost perfectly.
- **Plain language:** your model can only learn what your features allow, and it will learn the easiest thing they allow.
- **Misconception guardrail:** adding more features always improves science.

---

## Core Workflow
- Write the biological decision the model will support, naming who acts on the output and what they do differently as a result.
- Enumerate leakage channels present in your data — fragment duplication, spatial adjacency, annotator provenance, label circularity — and choose the split that blocks the strongest one.
- Construct the feature set with a one-line rationale per feature, and record the segmentation version the features were computed from.
- Fit all preprocessing (scaling, imputation, feature selection) inside the training fold only.
- Train a trivial baseline first — majority class, or a single-feature threshold — and report it alongside every later model.
- Evaluate with the metric that matches the decision from step 1, plus per-class recall and prevalence.
- Run error analysis on the failures: sample 20-30 misclassified examples and classify the failure reason by hand.
- Write the model card: intended use, unsupported uses, evaluation splits, metrics with intervals, and the domain in which the numbers hold.

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
- **Misconception guardrail:** a random split always gives a valid generalization estimate.
- **Misconception guardrail:** a 99% accurate classifier is a useful classifier.
- **Misconception guardrail:** the training labels are the truth the model is failing to reach.

---

## Studio Activity
**Scenario:** You must classify neurite fragments into coarse categories to prioritize a proofreading queue. You have roughly 4,000 labeled fragments drawn from about 600 neurons in one dataset, five classes with prevalences of approximately 38%, 27%, 19%, 12%, and 4%, and a reviewer team that can inspect 500 segments per week. A second, differently stained dataset is available as a held-out domain.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass**
- Feature and split decisions are justified against a named leakage channel.
- Metrics include at least one biologically targeted criterion tied to a real capacity or threshold.
- Limitation statement is specific and actionable.
- **Strong performance**
- Quantifies how much performance each successive split control removes.
- Uses error analysis to propose the next data improvement rather than the next model.
- Names the assumption behind the chosen block size or grouping in the same sentence as the number.
- Distinguishes an exploratory model from a deployment-ready one and states what would have to change.
- **Common failure modes**
- Leakage-prone random splits on spatially correlated data.
- Overfocus on aggregate accuracy with prevalence unreported.
- Claims of biological insight unsupported by model diagnostics.
- Features computed against an unpinned segmentation version.

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
