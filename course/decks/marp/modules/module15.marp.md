---
marp: true
theme: default
paginate: true
title: "Module 15: LLMs for Patch Analysis"
---

# Module 15: LLMs for Patch Analysis
Teaching Deck

---

## Learning Objectives
- Identify realistic LLM use cases in connectomics patch workflows
- Design prompt/evaluation loops with reliability checks
- Detect hallucination and unsupported inference risks
- Integrate LLM outputs into human-in-the-loop QC

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
Implement an LLM-assisted patch-analysis workflow with verification gates, confidence labeling, and explicit human override policies.

---

## Concept Focus
### 1) Assistive, not autonomous
- **Technical:** LLMs should support prioritization, summarization, and protocol guidance, not final biological adjudication.
- **Plain language:** use LLMs to help, not to decide alone.
- **Misconception guardrail:** fluent output equals correct output.

---

## Core Workflow
- Define candidate LLM tasks (triage, summary, QA aid).
- Create prompt templates and expected output schema.
- Add verification gates and human adjudication rules.
- Pilot on small patch set and log failure patterns.
- Refine prompts/policies before wider use.

---

## 60-Minute Run-of-Show
- **00:00-08:00** scope boundaries and failure examples.
- **08:00-20:00** prompt template design.
- **20:00-34:00** run sample outputs and score reliability.
- **34:00-46:00** define verification and override rules.
- **46:00-56:00** produce governance checklist.
- **56:00-60:00** competency check.

---

## Misconceptions to Watch
- **Misconception guardrail:** fluent output equals correct output.
- **Misconception guardrail:** spot-checking only when output seems odd.
- **Misconception guardrail:** chat history alone is sufficient traceability.

---

## Studio Activity
**Scenario:** Build an LLM-assisted triage helper for proofreading queues.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass:** clear task boundaries, verification logic, and logging fields.
- **Strong performance:** robust failure-mode handling and actionable governance plan.
- **Failure modes:** unbounded scope, no confidence policy, missing audit trail.

---

## Exit Ticket
For one LLM output type, define: acceptance threshold, verification method, and human override trigger.

---

## References (Instructor)
- LLM reliability and evaluation literature (task-specific).
- Internal patch-analysis workflow guidance.

---

## Teaching Materials
- Module page: /modules/module15/
- Slide page: /modules/slides/module15/
- Worksheet: /assets/worksheets/module15/module15-activity.md
