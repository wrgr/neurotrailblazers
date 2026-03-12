---
title: "Module 20: Statistical Models and Inference for Connectomics"
layout: module
permalink: /modules/module20/
description: "Build defensible statistical inference workflows for connectomics analyses, from null models to uncertainty reporting."
module_number: 20
difficulty: "Advanced"
duration: "4-6 hours"
learning_objectives:
  - "Choose statistical models aligned to connectomics question types"
  - "Construct and justify appropriate null models for graph analyses"
  - "Control multiplicity and uncertainty in high-dimensional motif tests"
  - "Report inferential claims with explicit assumptions and limits"
prerequisites: "Modules 12-19, including graph-analysis familiarity"
merit_stage: "Analysis"
compass_skills:
  - "Statistical Reasoning"
  - "Model Critique"
  - "Reproducible Analysis"
ccr_focus:
  - "Skills - Statistical Inference"
  - "Character - Epistemic Humility"

# Normalized metadata
slug: "module20"
short_title: "Statistical Models and Inference"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "inference"
  - "null-models"
  - "uncertainty"
  - "multiple-testing"
summary: "Design and critique statistical inference pipelines for connectomics with clear assumptions and reproducible outputs."
key_questions:
  - "Which null model is valid for this connectome hypothesis?"
  - "How should multiplicity be handled across motif families?"
  - "What claims are robust versus exploratory?"
slides: []
notebook:
  - "/assets/notebooks/module12/module12-big-data-in-connectomics.ipynb"
datasets:
  - "/datasets/workflow"
  - "/datasets/mouseconnects"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic probability/statistics"
  - "Graph representation concepts"
next_modules:
  - "module21"
references:
  - "Bassett, Zurn, and Gold (2018) - model use in network neuroscience."
  - "Januszewski et al. (2018) - segmentation performance and uncertainty context."
  - "MICrONS/FlyWire/H01 analyses for cross-dataset inference constraints."
videos:
  - "https://www.neurotrailblazers.org/technical-training/09-connectome-analysis-neuroai/"
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Design and execute a connectomics inference plan that includes null-model choice, multiplicity control, uncertainty reporting, and explicit claim boundaries.

## Why this module matters
Connectomics analyses can produce thousands of statistically testable patterns. Without disciplined inference, teams risk publishing artifacts from preprocessing bias, multiple comparisons, or misaligned null assumptions.

## Concept set
### 1) Null models encode scientific assumptions
- **Technical:** null models should preserve relevant graph constraints (degree sequence, spatial limits, cell-class composition) while randomizing the tested structure.
- **Plain language:** your "chance baseline" must reflect biology and data collection realities.
- **Misconception guardrail:** a generic random graph is rarely an adequate connectomics null.

### 2) Multiplicity is structural, not optional
- **Technical:** motif families and subgroup analyses require correction strategies and predeclared test hierarchies.
- **Plain language:** if you test many patterns, some will look significant by accident.
- **Misconception guardrail:** reporting only p-values without multiplicity context is incomplete.

### 3) Exploratory and confirmatory analyses must be separated
- **Technical:** hypothesis generation and hypothesis testing should have different reporting labels and evidence standards.
- **Plain language:** be clear about what you discovered versus what you validated.
- **Misconception guardrail:** post-hoc storytelling is not confirmatory inference.

## Core workflow: connectomics inference protocol
1. **Question-to-test mapping**
   - Convert biological question into estimand(s), test set, and effect-size target.
2. **Null-model design**
   - Define null constraints and why they preserve key confounders.
3. **Inference execution**
   - Run model/tests with preregistered thresholds and multiplicity controls.
4. **Robustness checks**
   - Test sensitivity to preprocessing variant, sampling region, and parameter choice.
5. **Claim calibration**
   - Report supported, uncertain, and unsupported claims in separate blocks.

## Studio activity: motif inference challenge
**Scenario:** A team reports motif enrichment in one dataset and asks whether the claim generalizes.

**Tasks**
1. Propose at least two candidate null models and justify each.
2. Run or outline multiplicity-aware testing strategy across motif set.
3. Draft a results summary separating exploratory and confirmatory findings.
4. Add one robustness check for cross-dataset comparability.

**Expected outputs**
- Inference design sheet (estimand, null, tests, correction).
- One-page claim calibration summary.
- Robustness plan with pass/fail criteria.

## Assessment rubric
- **Minimum pass**
  - Null model is justified and constraints are explicit.
  - Multiplicity handling is documented and applied.
  - Claims are partitioned by confidence level.
- **Strong performance**
  - Demonstrates sensitivity analysis against preprocessing and sampling choices.
  - Reports effect sizes and uncertainty, not significance alone.
  - Provides clear boundaries on generalization.
- **Common failure modes**
  - Null model choice disconnected from biological question.
  - Selective reporting of significant outcomes.
  - Conflation of exploratory signal with validated inference.

## Teaching resources
- Core unit context: [Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- Reading support: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dataset workflow context: [Workflow overview]({{ '/datasets/workflow' | relative_url }})
- Quality controls context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## Evidence anchors from connectomics practice
### Key papers to use in this module
- [Bassett, Zurn, and Gold (2018)](https://doi.org/10.1038/s41583-018-0038-8)
- [Januszewski et al. (2018)](https://doi.org/10.1038/s41592-018-0049-4)
- [MICrONS visual cortex reconstruction (Nature, 2025)](https://www.nature.com/articles/s41586-025-08790-w)

### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [FlyWire](https://flywire.ai/)
- [neuPrint Hemibrain](https://neuprint.janelia.org/)

### Competency checks
- Can you defend your null-model assumptions in one paragraph?
- Can you report one finding with effect size, uncertainty, and limitation?
- Can you identify which result remains exploratory?

## Quick practice prompt
Write a 6-8 sentence inference note that includes:
1. hypothesis and estimand,
2. null-model assumptions,
3. multiplicity strategy,
4. one robust conclusion and one unresolved uncertainty.
