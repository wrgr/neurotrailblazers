---
title: "Module 16: Scientific Visualization for Connectomics"
layout: module
permalink: /modules/module16/
description: "Create clear, truthful visualizations of connectomics structures, uncertainty, and analysis results for technical communication."
module_number: 16
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Select visualization forms aligned to analytical intent"
  - "Encode uncertainty and quality signals explicitly"
  - "Avoid misleading visual encodings in dense connectomics data"
  - "Produce publication-ready and presentation-ready figures"
prerequisites: "Modules 12-15"
merit_stage: "Dissemination"
compass_skills:
  - "Visualization Design"
  - "Scientific Communication"
  - "Interpretation Integrity"
ccr_focus:
  - "Skills - Visualization"
  - "Character - Transparency"

# Normalized metadata
slug: "module16"
short_title: "Scientific Visualization for Connectomics"
status: "active"
audience:
  - "students"
pipeline_stage: "Dissemination"
merit_row_focus: "Dissemination"
topics:
  - "visualization"
  - "uncertainty"
  - "communication"
summary: "Design truthful, high-clarity visualizations for structural and graph-level connectomics results."
key_questions:
  - "Which chart/visual form best matches each scientific claim?"
  - "How should uncertainty and data quality be shown visually?"
  - "What design choices commonly mislead interpretation?"
slides:
  - "/assets/slides/module16/module16-scientific-visualization-for-connectomics.pdf"
notebook:
  - "/assets/notebooks/module16/module16-scientific-visualization-for-connectomics.ipynb"
datasets:
  - "/datasets/workflow"
  - "/datasets/mouseconnects"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic plotting library familiarity"
  - "Understanding of analysis outputs"
next_modules:
  - "module17"
references:
  - "Visualization best-practice resources and connectomics exemplars."
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Produce a figure set that communicates connectomics findings accurately, including uncertainty and data-quality context, for both expert and mixed audiences.

## Why this module matters
Poor visual design can create false confidence and hide limitations. In connectomics, visualizations are often used as primary evidence and must be interpretation-safe.

## Concept set
### 1) Representation follows question
- **Technical:** geometry, topology, and statistical uncertainty require different visual encodings.
- **Plain language:** choose visuals that match what you are trying to prove.
- **Misconception guardrail:** one figure type can serve every claim.

### 2) Uncertainty must be visible
- **Technical:** confidence intervals, confidence classes, and missingness indicators should be explicit.
- **Plain language:** show what is uncertain, not only what is central.
- **Misconception guardrail:** cleaner-looking plots are always better.

### 3) Accessibility and integrity
- **Technical:** color choices, annotation density, and scale bars affect interpretability and fairness.
- **Plain language:** if people cannot read it, they cannot evaluate it.
- **Misconception guardrail:** aesthetics can replace methodological clarity.

## Core workflow
1. Map each claim to required visual evidence.
2. Draft candidate visuals with uncertainty layers.
3. Run critique for misinterpretation risk.
4. Revise for clarity, accessibility, and reproducibility.
5. Export figure package with caption metadata.

## 60-minute tutorial run-of-show
1. **00:00-08:00** visual integrity examples (good/bad).
2. **08:00-20:00** claim-to-visual mapping.
3. **20:00-34:00** figure draft build.
4. **34:00-46:00** uncertainty and quality overlays.
5. **46:00-56:00** peer critique and revision.
6. **56:00-60:00** competency check.

## Studio activity
**Scenario:** Prepare a 3-figure package for a connectomics result summary.

**Outputs**
- figure set with captions,
- uncertainty annotation strategy,
- revision log from critique.

## Assessment rubric
- **Minimum pass:** visuals map clearly to claims and include uncertainty context.
- **Strong performance:** high clarity across audiences with minimal misinterpretation risk.
- **Failure modes:** overloaded figures, missing scale context, hidden uncertainty.

## Teaching resources
- [Technical Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- [Module 17]({{ '/modules/module17/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## Quick practice prompt
Take one existing figure and add one uncertainty cue plus one caption sentence that narrows interpretation bounds.
