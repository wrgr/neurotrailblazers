# Module 12 Activity Worksheet

**Module:** Module 12: Big Data in Connectomics  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module12.md`, not this file.*

---

## Capability target

Produce a scalable, reproducible query-and-analysis plan for a large connectomics dataset, including storage assumptions, indexing strategy, and provenance capture.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Basic SQL/Python dataframe proficiency
- [ ] Familiarity with EM volume structure

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. How do we architect data systems for petascale connectomics?
   - Your answer:
2. Which indexing/query decisions drive analysis speed and reliability?
   - Your answer:
3. How do we preserve provenance at scale?
   - Your answer:

---

## The task

**Scenario:** Your team must deliver a weekly motif-analysis report from a multi-terabyte connectomics store.

1. Propose storage/index layout for expected query patterns.
2. Write or outline two critical queries and estimate performance risk.
3. Define minimum provenance fields for outputs.
4. Produce one optimization proposal and one reproducibility safeguard.

### What you hand in

- Query architecture sketch
- Baseline vs optimized query plan
- Provenance checklist

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Define analysis question and required data granularity.
- [ ] Select storage/index strategy aligned to access pattern.
- [ ] Prototype baseline query and profile bottlenecks.
- [ ] Add provenance logging and version controls.
- [ ] Validate reproducibility and publish query package.

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

- [ ] I did not assume: Compute scale alone does not solve poor data design.
- [ ] I did not assume: "it runs eventually" is not acceptable for iterative science.
- [ ] I did not assume: Notebook history alone is insufficient provenance.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-08:00 | Architecture framing and failure examples |
| 08:00-20:00 | Access-pattern to index mapping exercise |
| 20:00-34:00 | Query profiling and bottleneck diagnosis |
| 34:00-46:00 | Provenance logging implementation |
| 46:00-56:00 | Team review of reproducibility gaps |
| 56:00-60:00 | Competency check and next-step assignment |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**
- **Strong performance**
- **Common failure modes**

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Document one query you use with:
1. data source/version,
2. expected runtime class,
3. one provenance field you currently miss.

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

*Module page: `/modules/module12/` · Slides: `/modules/slides/module12/` · [Facilitator guide](/teaching/facilitator-guide/)*
