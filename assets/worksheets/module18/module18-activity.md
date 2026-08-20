# Module 18 Activity Worksheet

**Module:** Module 18: Data Cleaning and Preprocessing  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module18.md`, not this file.*

---

## Capability target

Produce a reproducible preprocessing release that transforms raw or intermediate connectomics outputs into analysis-ready data, with explicit quality gates and full provenance. Students will be able to identify the specific cleaning operations that shape biological conclusions, justify every threshold decision, and document their preprocessing pipeline so that another researcher can audit and reproduce it.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Basic dataframe manipulation in Python
- [ ] Familiarity with segmentation/proofreading outputs

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. What preprocessing decisions materially change biological conclusions?
   - Your answer:
2. How do we separate data repair from data distortion?
   - Your answer:
3. What metadata is required to make preprocessing reproducible?
   - Your answer:

---

## The task

**Scenario:** Your team receives a connectomics export from MICrONS minnie65 (CAVE materialization v795) containing: a synapse table (4.2 million rows) with confidence scores, a segment table (120,000 segments) with volumes, and a cell-type annotation table (8,400 classified neurons). Initial inspection reveals: 12% of synapses have confidence scores below 30, 35,000 segments have fewer than 2 synapses, 847 segments intersect the volume bounding box, and 23 segment IDs appear in the synapse table but not in the segment table.

1. **Artifact triage:** classify each issue (low-confidence synapses, small segments, boundary neurons, orphan IDs) by likely biological impact and propose a cleaning policy for each.
2. **Threshold justification:** for synapse confidence and segment size thresholds, propose two candidate values each and argue for your preferred choice. Explain what biological signal you might lose at each threshold.
3. **Implement preprocessing pipeline:** write pseudocode or notebook-level steps for the full cleaning workflow, from ingest through release.
4. **QC comparison:** compute (or estimate) pre/post metrics: total synapse count, total segment count, mean degree, graph density, and the fraction of each cell type remaining after cleaning.
5. **Release note:** produce a one-page release note that includes: input dataset version, all thresholds and parameters, code reference, QC metrics with pass/fail calls, and known residual risks (e.g., "boundary neurons were excluded, which may underrepresent connectivity of neurons near volume edges").

### What you hand in

- Preprocessing decision table (one row per issue, columns: issue, policy, threshold, rationale, impact)
- QC metric summary with thresholds and pass/fail calls
- Release note (inputs, transforms, outputs, limitations)

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] **Ingest and integrity validation**
- [ ] **Artifact and anomaly screening**
- [ ] **Cleaning transforms**
- [ ] **QC and drift checks**
- [ ] **Release packaging**

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

- [ ] I did not assume: "raw data is always better." In connectomics, raw segmentation output contains systematic artifacts that will corrupt analysis if left uncleaned. The question is not whether to clean, but how to clean transparently.
- [ ] I did not assume: There is no single "correct" threshold. If your result depends on a specific threshold choice, it is fragile and should be reported with a sensitivity analysis.
- [ ] I did not assume: More filtering is not always better. Aggressive cleaning can create the appearance of clean results while actually removing biological signal.
- [ ] I did not assume: Version-control notes alone are insufficient without data lineage. Git tracks code changes, but you also need to track which data version was processed with which code version.
- [ ] I did not assume: Documenting preprocessing after the fact is unreliable. Document decisions in real time.
- [ ] I did not assume: Reporting metrics without thresholds is not quality control. Every metric needs an associated action.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-08:00 | Setup and target framing |
| 08:00-18:00 | Instructor modeling: ingest and anomaly screening |
| 18:00-32:00 | Team preprocessing design |
| 32:00-44:00 | QC pass |
| 44:00-54:00 | Cross-team review |
| 54:00-60:00 | Competency checkpoint |

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

Take one connectomics table (real or mock) and write:
1. Three cleaning rules with rationale tied to specific data artifacts.
2. Two QC thresholds with associated pass/fail actions and biological justification.
3. One sensitivity analysis: what happens to your key metric if you relax or tighten your primary threshold by 20%?
4. One limitation that remains after preprocessing, stated concretely enough to guide interpretation.

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

*Module page: `/modules/module18/` · Slides: `/modules/slides/module18/` · [Facilitator guide](/teaching/facilitator-guide/)*
