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
1. Define candidate LLM tasks (triage, summary, QA aid).
2. Create prompt templates and expected output schema.
3. Add verification gates and human adjudication rules.
4. Pilot on small patch set and log failure patterns.
5. Refine prompts/policies before wider use.

---

## 60-Minute Run-of-Show
1. **00:00-08:00** scope boundaries and failure examples.
2. **08:00-20:00** prompt template design.
3. **20:00-34:00** run sample outputs and score reliability.
4. **34:00-46:00** define verification and override rules.
5. **46:00-56:00** produce governance checklist.
6. **56:00-60:00** competency check.

---

## Studio Activity
**Scenario:** Build an LLM-assisted triage helper for proofreading queues.

---

## Assessment Rubric
- **Minimum pass:** clear task boundaries, verification logic, and logging fields.
- **Strong performance:** robust failure-mode handling and actionable governance plan.
- **Failure modes:** unbounded scope, no confidence policy, missing audit trail.

---

## Quick Practice Prompt
For one LLM output type, define: acceptance threshold, verification method, and human override trigger.

---

## Teaching Materials
- Module page: /modules/module15/
- Slide page: /modules/slides/module15/
- Worksheet: /assets/worksheets/module15/module15-activity.md
