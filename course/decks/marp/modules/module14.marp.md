---
marp: true
theme: default
paginate: true
title: "Module 14: Computer Vision for EM"
---

# Module 14: Computer Vision for EM
Teaching Deck

---

## Learning Objectives
- Explain how classical and deep CV methods map to connectomics tasks
- Compare model outputs using biologically meaningful error criteria
- Design a validation plan for CV pipelines in EM data
- Report CV limitations with reproducibility safeguards

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
Design and evaluate a CV pipeline for EM imagery that is fit for a specific connectomics task and explicitly bounded by known failure modes.

---

## Concept Focus
### 1) Task-model fit
- **Technical:** detection, segmentation, denoising, and classification tasks require different objective functions and architectures.
- **Plain language:** pick models for the job, not by popularity.
- **Misconception guardrail:** one model can solve all EM tasks equally well.

---

## Core Workflow
- Define EM task and acceptable error envelope.
- Select baseline and candidate CV approaches.
- Run evaluation using biologically relevant metrics.
- Perform failure-case review on ambiguous regions.
- Publish model card with limitations and intended use.

---

## 60-Minute Run-of-Show
- **00:00-08:00** task framing + exemplar failure modes.
- **08:00-20:00** choose metrics tied to downstream biology.
- **20:00-34:00** evaluate baseline vs candidate model.
- **34:00-46:00** error taxonomy and triage discussion.
- **46:00-56:00** model card drafting.
- **56:00-60:00** competency check.

---

## Misconceptions to Watch
- **Misconception guardrail:** one model can solve all EM tasks equally well.
- **Misconception guardrail:** high benchmark score implies safe downstream use.
- **Misconception guardrail:** visual plausibility is sufficient validation.

---

## Studio Activity
**Scenario:** Compare two segmentation-support CV models for an EM subvolume.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass:** clear task-model rationale, biologically relevant metrics, explicit limitations.
- **Strong performance:** robust failure analysis and operational release criteria.
- **Failure modes:** metric-only reasoning, weak split design, no deployment boundaries.

---

## Exit Ticket
Document one CV result with one supported use case and one forbidden use case.

---

## References (Instructor)
- Januszewski et al. (2018) for segmentation model context.
- Recent MICrONS/FlyWire methods for practical CV constraints.

---

## Teaching Materials
- Module page: /modules/module14/
- Slide page: /modules/slides/module14/
- Worksheet: /assets/worksheets/module14/module14-activity.md
