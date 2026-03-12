---
marp: true
theme: default
paginate: true
title: "Module 20: Statistical Models and Inference for Connectomics"
---

# Module 20: Statistical Models and Inference for Connectomics
Teaching Deck

---

## Learning Objectives
- Choose statistical models aligned to connectomics question types
- Construct and justify appropriate null models for graph analyses
- Control multiplicity and uncertainty in high-dimensional motif tests
- Report inferential claims with explicit assumptions and limits

---

## Capability Target
Design and execute a connectomics inference plan that includes null-model choice, multiplicity control, uncertainty reporting, and explicit claim boundaries.

---

## Concept Focus
### 1) Null models encode scientific assumptions
- **Technical:** null models should preserve relevant graph constraints (degree sequence, spatial limits, cell-class composition) while randomizing the tested structure.
- **Plain language:** your "chance baseline" must reflect biology and data collection realities.
- **Misconception guardrail:** a generic random graph is rarely an adequate connectomics null.

---

## Core Workflow


---

## 60-Minute Run-of-Show
- See module page for timed delivery flow.

---

## Studio Activity


---

## Assessment Rubric
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

---

## Quick Practice Prompt
Write a 6-8 sentence inference note that includes:
1. hypothesis and estimand,
2. null-model assumptions,
3. multiplicity strategy,
4. one robust conclusion and one unresolved uncertainty.

---

## Teaching Materials
- Module page: /modules/module20/
- Slide page: /modules/slides/module20/
- Worksheet: /assets/worksheets/module20/module20-activity.md
