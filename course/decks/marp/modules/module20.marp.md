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
Design and execute a connectomics inference plan that includes null-model choice, multiplicity control, uncertainty reporting, and explicit claim boundaries.

---

## Concept Focus
### 1) Null models encode scientific assumptions
- **Technical:** null models should preserve relevant graph constraints (degree sequence, spatial limits, cell-class composition) while randomizing the tested structure.
- **Plain language:** your "chance baseline" must reflect biology and data collection realities.
- **Misconception guardrail:** a generic random graph is rarely an adequate connectomics null.

---

## Core Workflow
- See module page for details.

---

## 60-Minute Run-of-Show
- See module page for details.

---

## Misconceptions to Watch
- **Misconception guardrail:** a generic random graph is rarely an adequate connectomics null.
- **Misconception guardrail:** reporting only p-values without multiplicity context is incomplete.
- **Misconception guardrail:** post-hoc storytelling is not confirmatory inference.

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

## Exit Ticket
Write a 6-8 sentence inference note that includes:
1. hypothesis and estimand,
2. null-model assumptions,
3. multiplicity strategy,
4. one robust conclusion and one unresolved uncertainty.

---

## References (Instructor)
- Bassett, Zurn, and Gold (2018) - model use in network neuroscience.
- Januszewski et al. (2018) - segmentation performance and uncertainty context.
- MICrONS/FlyWire/H01 analyses for cross-dataset inference constraints.

---

## Teaching Materials
- Module page: /modules/module20/
- Slide page: /modules/slides/module20/
- Worksheet: /assets/worksheets/module20/module20-activity.md
