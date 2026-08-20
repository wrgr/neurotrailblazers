# Module 15 Activity Worksheet

**Module:** Module 15: LLMs for Patch Analysis  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module15.md`, not this file.*

---

## Capability target

Implement an LLM-assisted patch-analysis workflow with verification gates, confidence labeling, and explicit human override policies.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Segmentation and proofreading basics
- [ ] Basic scripting and data-table handling

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. Where can LLMs help without introducing unacceptable risk?
   - Your answer:
2. How should outputs be verified before scientific use?
   - Your answer:
3. Which tasks must remain human-adjudicated?
   - Your answer:

---

## The task

**Scenario:** Build an LLM-assisted triage helper for proofreading queues.

1. Define candidate LLM tasks (triage, summary, QA aid).
2. Create prompt templates and expected output schema.
3. Add verification gates and human adjudication rules.
4. Pilot on small patch set and log failure patterns.
5. Refine prompts/policies before wider use.

### What you hand in

- prompt + schema pack
- verification rubric
- risk register and override policy

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Define candidate LLM tasks (triage, summary, QA aid).
- [ ] Create prompt templates and expected output schema.
- [ ] Add verification gates and human adjudication rules.
- [ ] Pilot on small patch set and log failure patterns.
- [ ] Refine prompts/policies before wider use.

---

## Evidence and reasoning

Fill one row per claim you make in your artifact. A claim without a limitation is
not finished.

| # | Claim | Evidence (what specifically) | Limitation / what would change my mind |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Confidence.** For your main claim, mark one and say why:

- [ ] **High** — two or more independent lines of evidence agree
- [ ] **Medium** — one strong line, or several that share a weakness
- [ ] **Uncertain** — the deciding evidence is not available to me

Why:

**One alternative I considered and rejected**, and the reason:

---

## Misconception self-check

These are the errors this module is designed to prevent. Confirm you did not make
them, or note where you nearly did:

- [ ] I did not assume: Fluent output equals correct output.
- [ ] I did not assume: Spot-checking only when output seems odd.
- [ ] I did not assume: Chat history alone is sufficient traceability.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| | 00:00-08:00 scope boundaries and failure examples. |
| | 08:00-20:00 prompt template design. |
| | 20:00-34:00 run sample outputs and score reliability. |
| | 34:00-46:00 define verification and override rules. |
| | 46:00-56:00 produce governance checklist. |
| | 56:00-60:00 competency check. |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass:** clear task boundaries, verification logic, and logging fields.
- **Strong performance:** robust failure-mode handling and actionable governance plan.
- **Failure modes:** unbounded scope, no confidence policy, missing audit trail.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

For one LLM output type, define: acceptance threshold, verification method, and human override trigger.

**Your answer:**

---

## Peer review (swap worksheets)

Reviewing someone else's reasoning is the fastest way to see the gaps in your own.
Assess the **evidence quality**, not whether you agree with the conclusion.

- Is every claim paired with specific evidence?
- Is at least one limitation stated, and is it a real one?
- Is the confidence level justified by the number of *independent* evidence lines?
- One thing this person did better than me:
- One question I would ask them:

---

*Module page: `/modules/module15/` · Slides: `/modules/slides/module15/` · [Facilitator guide](/teaching/facilitator-guide/)*
