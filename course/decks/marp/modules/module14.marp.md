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
1. Define EM task and acceptable error envelope.
2. Select baseline and candidate CV approaches.
3. Run evaluation using biologically relevant metrics.
4. Perform failure-case review on ambiguous regions.
5. Publish model card with limitations and intended use.

---

## 60-Minute Run-of-Show
1. **00:00-08:00** task framing + exemplar failure modes.
2. **08:00-20:00** choose metrics tied to downstream biology.
3. **20:00-34:00** evaluate baseline vs candidate model.
4. **34:00-46:00** error taxonomy and triage discussion.
5. **46:00-56:00** model card drafting.
6. **56:00-60:00** competency check.

---

## Studio Activity
**Scenario:** Compare two segmentation-support CV models for an EM subvolume.

---

## Assessment Rubric
- **Minimum pass:** clear task-model rationale, biologically relevant metrics, explicit limitations.
- **Strong performance:** robust failure analysis and operational release criteria.
- **Failure modes:** metric-only reasoning, weak split design, no deployment boundaries.

---

## Quick Practice Prompt
Document one CV result with one supported use case and one forbidden use case.

---

## Teaching Materials
- Module page: /modules/module14/
- Slide page: /modules/slides/module14/
- Worksheet: /assets/worksheets/module14/module14-activity.md
