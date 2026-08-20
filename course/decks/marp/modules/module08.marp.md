---
marp: true
theme: default
paginate: true
title: "Module 08: Hypothesis Testing in Connectomics"
---

# Module 08: Hypothesis Testing in Connectomics
Teaching Deck

---

## Learning Objectives
- Translate biological questions into testable hypotheses
- Select metrics and null models for structural data
- Interpret outcomes with uncertainty discipline
- Separate supported claims from exploratory signals

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
Design one hypothesis test with metric, null model, and interpretation boundary statement.

---

## Concept Focus
### 1) What makes a connectomics hypothesis testable?
A testable connectomics hypothesis must specify: (a) a structural feature that can be measured from the reconstructed data (e.g., synapse count, motif frequency, path length), (b) a comparison or null expectation (e.g., "more frequent than in a degree-preserving random graph"), and (c) an interpretation boundary (what the result does and does not prove). Many fascinating biological questions ("How does the cortex generate consciousness?") are not directly testable with connectomics because they lack measurable structural endpoints.

---

## Core Workflow
- Define question and estimand: what structural feature would constrain or inform the biological question?
- Choose measurable outputs: specific metric(s) computed from the connectome graph.
- Select null model: the most stringent null relevant to the claim.
- Test and interpret results: compute metric, compare to null distribution, compute z-score and p-value.
- Document supported vs unsupported claims: what the result proves, what it doesn't, and what additional evidence would be needed.

---

## 60-Minute Run-of-Show
- Read the motif analysis content library entry (focus on null models section)
- Draft one biological question you'd like to test with connectomics data
- **00:00-08:00 | Framing: good vs bad hypotheses**
- Show 4 example hypotheses (2 good, 2 poor). Group identifies which are testable and why.
- Key criteria: measurable endpoint, specified null, interpretation boundary.
- **08:00-20:00 | Hypothesis drafting**
- Each learner drafts a hypothesis using a template:
- "In [dataset/region], [structural feature] is [comparison] compared to [null model]."
- "This would support [interpretation] but would NOT prove [over-claim]."
- Peer review: partner evaluates whether the hypothesis is testable.
- **20:00-34:00 | Metric and null model selection**
- For each drafted hypothesis, select the appropriate metric and null model.
- Instructor walks through one example end-to-end: hypothesis → metric → null → expected result → interpretation.
- Discussion: "What happens if you use the wrong null model?" Show how the same data looks significant or non-significant depending on null choice.
- **34:00-46:00 | Interpretation workshop**
- Present 3 pre-computed results (with p-values and z-scores). For each, learners write:
- Supported claim (what the data shows)
- Explicit non-claim (what the data does NOT show)
- One confound that could explain the result
- Group discussion of each result.
- **46:00-60:00 | Competency check**
- Each learner submits their final hypothesis with metric, null model, and interpretation boundaries.
- Exit ticket: "Write one claim and one explicit non-claim from the same test outcome."

---

## Misconceptions to Watch
- **Misconception guardrail:** a significant result against a random-graph null is evidence of biological structure.
- **Misconception guardrail:** the statistical test is the scientific step, when the choice of null model is.
- **Misconception guardrail:** a metric can be chosen after seeing the data without cost to the inference.
- **Misconception guardrail:** reporting the tests that worked is sufficient without reporting how many were run.

---

## Studio Activity
**Scenario:** Your lab is planning a study of feedforward vs feedback connectivity in mouse visual cortex using the MICrONS dataset. You need to design three testable hypotheses about the circuit architecture.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass**: Coherent hypothesis/metric/null trio for at least 2 of 3 hypotheses.
- **Strong performance**: Clear uncertainty and non-claim statements. Null model choice justified. Peer critique identifies genuine issues.
- **Common failure to flag**: Vague hypothesis without measurable endpoint ("we will study connectivity patterns") or missing null model.

---

## Exit Ticket
Write one claim and one explicit non-claim from the same test outcome.

---

## References (Instructor)
- Use module references listed on the module page.

---

## Teaching Materials
- Module page: /modules/module08/
- Slide page: /modules/slides/module08/
- Worksheet: /assets/worksheets/module08/module08-activity.md
