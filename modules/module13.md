---
title: "Module 13: Machine Learning in Neuroscience"
layout: module
permalink: /modules/module13/
description: "Apply machine-learning workflows to connectomics features, with explicit controls for data leakage, bias, and interpretability."
module_number: 13
difficulty: "Advanced"
duration: "4-5 hours"
learning_objectives:
  - "Build feature pipelines for neuron and synapse-level analyses"
  - "Compare supervised and unsupervised methods for connectomics tasks"
  - "Evaluate model quality with biologically meaningful metrics"
  - "Detect data leakage and distribution-shift risks in connectomics ML"
prerequisites: "Modules 1-12 and Python ML basics"
merit_stage: "Analysis"
compass_skills:
  - "Quantitative Reasoning"
  - "Model Evaluation"
  - "Bias Detection"
ccr_focus:
  - "Skills - Machine Learning"
  - "Character - Responsible Inference"

# Normalized metadata
slug: "module13"
short_title: "Machine Learning in Neuroscience"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "machine-learning"
  - "feature-engineering"
  - "model-evaluation"
summary: "Build and evaluate ML workflows for connectomics with biological interpretability and reproducibility safeguards."
key_questions:
  - "Which ML task framing matches this connectomics question?"
  - "How do we avoid leakage and overfitting in structural data?"
  - "Which metrics matter scientifically, not only computationally?"
slides: []
notebook: []
datasets:
  - "/datasets/mouseconnects"
  - "/datasets/workflow"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
related_tools:
  - "/tools/connectome-quality/"
  - "/tools/ask-an-expert/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic scikit-learn workflow familiarity"
  - "Feature matrix handling in Python"
next_modules:
  - "module14"
  - "module15"
references:
  - "Januszewski et al. (2018) for segmentation ML context."
  - "UMAP paper (McInnes et al., 2018) for embedding interpretation caveats."
  - "MICrONS/FlyWire analyses for realistic distribution-shift context."
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Design and critique an ML analysis pipeline for connectomics that includes feature rationale, evaluation plan, leakage controls, and interpretation limits.

## Why this module matters
ML can accelerate connectomics analysis, but naive workflows produce misleading biological claims. This module emphasizes model validity, not just model performance.

## Concept set
### 1) Feature engineering defines the hypothesis space
- **Technical:** feature choices encode assumptions about what variation is biologically meaningful.
- **Plain language:** your model can only learn what your features allow.
- **Misconception guardrail:** adding more features always improves science.

### 2) Evaluation must match biological use
- **Technical:** metrics should align with downstream decisions (for example, class-specific recall for rare but critical cell types).
- **Plain language:** high overall accuracy can still fail where it matters most.
- **Misconception guardrail:** one summary metric is enough.

### 3) Leakage and shift are endemic in connectomics
- **Technical:** spatial adjacency, reconstruction provenance, and shared preprocessing can leak signal across train/test splits.
- **Plain language:** your model may be "cheating" without obvious signs.
- **Misconception guardrail:** random split always gives valid generalization estimates.

## Hidden curriculum scaffold
- Unspoken ML norms trainees need explicitly:
  - justify split strategy before training.
  - report failure cases with examples, not only aggregate metrics.
  - include model-card style limitations and intended use.
- Mentoring supports:
  - provide leakage checklist template.
  - require one "where model fails" figure.
  - review scientific usefulness, not just benchmark score.

## Core workflow: connectomics ML protocol
1. Define task and biological decision context.
2. Construct feature set with rationale and preprocessing log.
3. Choose split strategy that blocks leakage pathways.
4. Train baseline + candidate models and compare error profiles.
5. Report metrics, limitations, and deployment constraints.

## 60-minute tutorial run-of-show
1. **00:00-08:00 | Task framing and leakage examples**
2. **08:00-20:00 | Feature rationale workshop**
3. **20:00-34:00 | Split strategy and baseline modeling**
4. **34:00-46:00 | Error analysis and biologically relevant metrics**
5. **46:00-56:00 | Model-card limitation writing**
6. **56:00-60:00 | Competency checkpoint**

## Studio activity: leakage-resistant ML mini-pipeline
**Scenario:** You need to classify neurite fragments into coarse categories for downstream proofreading prioritization.

**Tasks**
1. Propose feature set and leakage-safe split design.
2. Train one baseline and one improved model (or pseudocode plan).
3. Report two standard metrics and one biologically targeted metric.
4. Draft a model limitation statement with non-supported use cases.

**Expected outputs**
- Feature + split design sheet.
- Metric table with interpretation notes.
- Limitation statement.

## Assessment rubric
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

## ML in the connectomics pipeline

Machine learning is embedded at every stage of the reconstruction pipeline:

| Stage | ML task | Key methods | Training data source |
|-------|---------|-------------|---------------------|
| **Segmentation** | Predict voxel affinities/boundaries | U-Net, FFN (Januszewski et al. 2018) | Manual ground-truth annotations |
| **Synapse detection** | Identify cleft locations + pre/post partners | 3D CNN on local patches | Expert-annotated synapse sets |
| **Cell-type classification** | Assign neuron type from morphology/connectivity | Random forest, GNN, clustering | Morphologically typed neurons |
| **Error detection** | Flag likely merge/split errors for proofreading | Classifier on segment features | Proofreading correction logs |
| **Automated proofreading** | Suggest corrections | Reinforcement learning, heuristic models | Before/after correction pairs |

**Domain shift is the central challenge:** A model trained on well-stained MICrONS data may fail on under-stained H01 regions, on different species (mouse → fly), or on tissue with pathology (near epileptic foci). Always evaluate on held-out data from the target domain, not just the training domain.

## Content library references
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) — Where ML fits in the pipeline
- [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}) — Error types ML must handle
- [NeuroAI bridge]({{ '/content-library/connectomics/neuroai-bridge/' | relative_url }}) — Bidirectional exchange between neuroscience and AI
- [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) — Morphological and connectivity-based classification

## Teaching resources
- Upstream data context: [Module 12]({{ '/modules/module12/' | relative_url }})
- Downstream morphology/classification: [Module 14]({{ '/modules/module14/' | relative_url }})
- Technical track context: [Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- Quality context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## References
- Januszewski M et al. (2018) "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods* 15(8):605-610.
- Lee K et al. (2019) "Superhuman accuracy on the SNEMI3D connectomics challenge." *arXiv:1706.00120*.
- McInnes L et al. (2018) "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction." *arXiv:1802.03426*.
- Ronneberger O et al. (2015) "U-Net: Convolutional Networks for Biomedical Image Segmentation." *MICCAI* 2015.

## Quick practice prompt
For one candidate model, write:
1. one plausible leakage pathway,
2. one metric blind spot,
3. one limitation you would report publicly.
