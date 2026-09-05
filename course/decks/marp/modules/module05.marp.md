---
marp: true
theme: default
paginate: true
title: "Module 05: Electron Microscopy and Image Basics"
---

# Module 05: Electron Microscopy and Image Basics
Teaching Deck

---

## Learning Objectives
- Describe core EM acquisition concepts relevant to connectomics
- Identify common image artifacts and likely downstream impact
- Interpret image quality for segmentation readiness
- Document uncertainty and QA decisions

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
Evaluate EM image patches for artifact risk and issue a justified pass/rework recommendation.

---

## Concept Focus
EM image quality is not merely an aesthetic concern — it is the single most consequential variable that determines segmentation accuracy and, by extension, the validity of every connectomic claim built on that segmentation. A 20% reduction in membrane contrast can double the split error rate in automated reconstruction, because the segmentation model loses the luminance gradient it relies on to delineate adjacent neurites. Every downstream analysis result — synapse counts, path lengths, circuit motifs — inherits the quality ceiling set at acquisition. This means that the person evaluating image quality is making a decision that propagates through the entire pipeline. Treating QA as a clerical step rather than a scientific judgment is one of the most common and costly mistakes in connectomics projects.

---

## Core Workflow
- Inspect image quality and artifact signatures.
- Classify severity and likely impact on segmentation.
- Decide pass/flag/rework with documented rationale.
- Log findings in a structured QA record for reproducibility.

---

## 60-Minute Run-of-Show
- Review the EM principles content library entry, focusing on the section on image formation and contrast mechanisms.
- Preview the three sample image patches posted to the course portal: one clean image, one with moderate knife chatter, and one with a tissue fold. For each, note initial impressions of quality.
- Projected EM image gallery (8-10 patches at varying quality levels)
- Printed or digital QA decision worksheet (one per student)
- Timer visible to the class
- Artifact reference card (single page, double-sided)
- *Instructor cue*: "We are going to start with a fast review. I will show four images — tell me which modality produced each one and why you think so."
- Show four images (ssTEM, SBEM, FIB-SEM, and one intentionally ambiguous). Cold-call students for modality identification and reasoning.
- Briefly review how contrast arises from heavy metal staining and electron scattering. Emphasize that membrane visibility depends on staining protocol, not microscope settings alone.
- *Instructor cue*: "Now I am going to show you the five artifacts that cause 90% of segmentation failures. For each one, I want you to predict: will this cause a merge error, a split error, or a topology break?"
- Walk through knife chatter, charging, folds, missing sections, and staining gradients with annotated example images.
- For each artifact, show the segmentation output on the same region so students can see the predicted error type realized in practice.
- *Formative check*: After the third artifact, pause and ask students to classify the next one independently before revealing the answer.
- *Instructor cue*: "You have 14 minutes. Work in pairs. Each pair receives six image patches. For each patch, fill in the QA worksheet: artifact type, severity (1-3), predicted segmentation impact, and your pass/flag/rework decision."
- Circulate and listen for common misconceptions. Note which artifact types cause the most disagreement.
- *Formative check*: At 30:00, ask one pair to share their most difficult call and explain their reasoning.
- *Instructor cue*: "Pair A said this patch is a pass. Pair B said rework. Both of you, defend your position."
- Facilitate structured debate on 2-3 patches where pairs disagreed. Push students to articulate the cost tradeoff: what is the cost of re-acquiring versus the cost of proofreading the resulting errors?
- Introduce the concept of escalation levels (hard stop, flag and monitor, pass) and ask students to re-classify their six patches using this framework.
- *Instructor cue*: "A QA decision that is not logged does not exist. You are now going to write a QA log entry for your hardest patch."
- Students write a structured QA entry: image ID, artifact type, severity, decision, rationale, and any conditions (e.g., "pass if proofreading budget is allocated to rows 12-18").
- Show an example of a well-written and a poorly-written QA entry for comparison.
- *Instructor cue*: "Final check. I am showing one new patch. You have two minutes to write your QA verdict on an index card. Include artifact type, severity, decision, and one sentence of rationale."
- Collect index cards. Review after class to identify students who need follow-up.
- **08:00**: Can students distinguish EM modalities from image appearance?
- **20:00**: Can students predict segmentation error type from artifact type?
- **34:00**: Can students apply severity ratings consistently across patches?
- **46:00**: Can students articulate cost tradeoffs in QA decisions?
- **56:00**: Can students write a structured QA log entry?

---

## Misconceptions to Watch
- **Misconception guardrail:** you can proofread your way out of a bad image.
- **Misconception guardrail:** a noisy image is worse for segmentation than a clean image with faint membranes.
- **Misconception guardrail:** artifact severity can be judged from a count, when the spatial distribution matters more.
- **Misconception guardrail:** quality assessment is a clerical checkpoint rather than a scientific judgment that propagates through every downstream claim.

---

## Studio Activity
**Scenario:** Your team has received pilot images from a new ssTEM acquisition of mouse visual cortex. The imaging facility reports that initial sections looked good, but they encountered intermittent knife chatter starting around section 200 and a possible staining gradient in the lateral third of the field of view. Before the facility commits to imaging the remaining 800 sections, your team must evaluate the pilot data and deliver a go/no-go recommendation with conditions.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum (pass)**: Accurate identification of major artifacts across all patches, correct mapping to segmentation error type, and a defensible pass/flag/rework decision for each patch.
- **Strong (merit)**: Clear articulation of cost tradeoffs, consistent severity thresholds across patches, spatially aware analysis, and a well-structured recommendation memo with specific conditions.
- **Failure**: Artifact labels assigned without reference to downstream segmentation implications, or QA decisions made without documented rationale.

---

## Exit Ticket
Pick one artifact and explain how it could create a merge or split error later. Then estimate: if this artifact appears on 5% of sections, how many additional proofreading hours would it add to a 1000-section volume?

---

## References (Instructor)
- Use module references listed on the module page.

---

## Teaching Materials
- Module page: /modules/module05/
- Slide page: /modules/slides/module05/
- Worksheet: /assets/worksheets/module05/module05-activity.md
