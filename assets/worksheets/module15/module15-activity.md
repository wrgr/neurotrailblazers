# Module 15 Activity Worksheet

**Module:** Module 15: LLMs for Patch Analysis  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module15.md`, not this file.*

---

## Capability target

Implement an LLM-assisted patch-analysis workflow with verification gates, confidence labeling, and explicit human override policies. Concretely: classify every output your workflow produces into named output classes, attach a verification method and a numeric acceptance threshold to each class before any output is used, measure whether the gate costs less than the task it replaces, and log model version, prompt, output, reviewer, and decision so a reader can reconstruct which claims a model touched.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Segmentation and proofreading basics
- [ ] Basic scripting and data-table handling
- [ ] Read [proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) so you know what the human-in-the-loop workflow currently is.
- [ ] Bring one real task from your own work you were considering handing to an LLM.
- [ ] Be ready to estimate how long that task takes you by hand.

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

**Scenario:** Build an LLM-assisted triage helper for proofreading queues. Reviewers can inspect about 500 segments per week; the current heuristic ranks candidates by segment size and produces roughly 40% true errors in the top 500. Your team wants to know whether an LLM-assisted ranker, drawing on segment statistics and free-text QC notes, should replace it. You have a labeled holdout of 300 segments and one expert available for four hours.

1. Enumerate the output classes this helper will produce and name the one that carries the most risk.
2. Write the verification gate and numeric acceptance threshold for each class, before generating any output.
3. Estimate the cost of each gate and compare it with the cost of the task it replaces; mark any class where the gate loses.
4. Design the pilot: how many items per class, who adjudicates, and what result would cause you to abandon the helper.
5. Specify the logging schema and the human override policy, including the interface rule that prevents anchoring.
6. Write the risk register: for each output class, the failure mode, its detection method, and the fallback if the gate fails.

### What you hand in

- prompt + schema pack
- verification rubric with numeric thresholds per output class
- gate-cost comparison table
- risk register and override policy

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Enumerate the candidate LLM tasks in your project and sort them into named output classes.
- [ ] For each class, write the verification method and a numeric acceptance threshold that can fail, before generating any output.
- [ ] Estimate, then measure, the cost of the gate against the cost of doing the task directly; drop any class where the gate costs more.
- [ ] Create prompt templates with an explicit output schema, and include the fields that gates depend on — for code, the version pin; for summaries, the citation list.
- [ ] Define the human override policy and the interface rule that prevents anchoring: independent human call recorded before the suggestion is shown.
- [ ] Pilot on a small set — 20 to 50 items per class — and log every failure with its cause.
- [ ] Set the logging fields: model name and version, prompt, raw output, verification result, reviewer, decision, timestamp.
- [ ] Refine prompts and thresholds from the pilot, then state in your methods which output classes were LLM-assisted.

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

- [ ] I did not assume: Fluent output means correct output.
- [ ] I did not assume: Spot-checking is enough when the output looks unusual.
- [ ] I did not assume: LLM assistance saves time on every task it can perform.
- [ ] I did not assume: Chat history is sufficient traceability.
- [ ] I did not assume: Showing the model's answer first speeds annotators up without changing their judgment.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| | 00:00-08:00 scope boundaries and failure examples. Show the unpinned-query failure first, because it is the one that looks like a success. |
| | 08:00-20:00 prompt template design, including the schema fields each gate depends on. |
| | 20:00-34:00 run sample outputs and score reliability against a known answer; record agreement counts rather than impressions. |
| | 34:00-46:00 define verification and override rules per output class, and estimate the cost of each gate. |
| | 46:00-56:00 produce governance checklist and risk register, with one class explicitly marked as not yet usable. |
| 56:00-60:00 competency check | each learner states one output class they would refuse to gate, and why. |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass:** clear task boundaries, verification logic with thresholds that can fail, and logging fields including model version and prompt.
- **Strong performance:** robust failure-mode handling, an actionable governance plan, a measured or defensibly estimated gate cost for each output class, and at least one class explicitly declared not yet usable.
- **Failure modes:** unbounded scope, no confidence policy, missing audit trail, thresholds written after seeing the outputs, and gates whose cost was never compared with the task they replace.

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
