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
Design and evaluate a CV pipeline for EM imagery that is fit for a specific connectomics task and explicitly bounded by known failure modes. Concretely: choose an architecture from the shape of the task rather than from the benchmark leaderboard, decompose error into merges and splits instead of reporting one score, convert that decomposition into a downstream cost using a ratio your team has actually measured, and write a release gate that says in advance what result would stop the model from shipping.

---

## Concept Focus
### 1) Task-model fit
- **Technical:** detection, instance segmentation, denoising, and classification need different objectives, and in EM they also need different data geometry. Affinity prediction with watershed and agglomeration is modular: the dense network runs once over the volume and agglomeration can be re-run cheaply with a new threshold or a learned merge model. Flood-filling networks produce instance labels directly with fewer post-processing stages, at substantially higher compute per volume and less ability to re-run one stage in isolation. Anisotropic data — 4 x 4 x 40 nm is 10:1 — makes z-context weak and pushes some pipelines toward 2D prediction with explicit cross-section linking.
- **Plain language:** pick the model for the job and for the voxel shape, not by popularity.
- **Misconception guardrail:** one architecture solves all EM tasks equally well.

---

## Core Workflow
- Write the EM task as a sentence naming the input, the output, and the downstream consumer of that output.
- Define the acceptable error envelope in decomposed terms: maximum merge rate, minimum ERL, and the region in which those numbers must hold.
- Select a baseline and at most two candidate approaches, using the approach table and the voxel geometry of your data.
- Assemble evaluation data that includes at least one deliberately hard region, and keep clean-region and hard-region metrics separate.
- Evaluate with VI decomposed, ERL, and a connectivity-level metric; never report a single aggregate score alone.
- Convert the error counts into downstream cost using a merge-to-split ratio your team measured rather than assumed.
- Review 20-30 failure cases by eye in ambiguous regions and classify each by cause: weak stain, section loss, fold, thin neurite, or genuine ambiguity.
- Publish a model card with intended use, unsupported uses, the evaluation regions, the metrics with their region breakdown, and the release gate the model passed.

---

## 60-Minute Run-of-Show
- **00:00-08:00** task framing + exemplar failure modes. Show one split and one merge in the viewer and ask which is worse; collect reasons before giving the answer.
- **08:00-20:00** choose metrics tied to downstream biology. Each learner writes the metric they would gate on and the threshold, before seeing any model output.
- **20:00-34:00** evaluate baseline vs candidate model. Learners compute or are given VI components, ERL, and error counts for two models, then solve for the break-even merge-to-split ratio.
- **34:00-46:00** error taxonomy and triage discussion. Sample failure cases, classify each by cause, and identify which causes augmentation could have addressed.
- **46:00-56:00** model card drafting, including at least one unsupported use and the region breakdown of the metrics.
- **56:00-60:00** competency check: each learner states their release gate as a sentence that could fail.

---

## Misconceptions to Watch
- **Misconception guardrail:** one architecture solves all EM tasks equally well.
- **Misconception guardrail:** a higher benchmark score means safer downstream use.
- **Misconception guardrail:** visual plausibility is sufficient validation.
- **Misconception guardrail:** the held-out ground truth is representative of the volume.
- **Misconception guardrail:** more augmentation is always better than less.

---

## Studio Activity
{: #studio-activity}
**Scenario:** Compare two segmentation-support CV models for an EM subvolume. You are given the model outputs, a proofread ground-truth subvolume of roughly 40 mm of traced path drawn from a clean region, and a second, smaller ground-truth patch from a region containing a partial fold and two lost sections. Your team maintains the production segmentation and must recommend one model.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass:** clear task-model rationale, biologically relevant metrics reported with merge and split separated, explicit limitations naming at least one unsupported use.
- **Strong performance:** robust failure analysis by cause, a release gate written before the result was known, and a downstream cost argument that names the merge-to-split ratio as a measured quantity rather than an assumption.
- **Failure modes:** metric-only reasoning, pooling clean and artifact-heavy regions into one number, weak split design, no deployment boundaries, thresholds chosen after seeing which model they would favor.

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
