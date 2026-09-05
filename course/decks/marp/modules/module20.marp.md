---
marp: true
theme: default
paginate: true
title: "Module 20: Statistical Models and Inference for Connectomics"
---

# Module 20: Statistical Models and Inference for Connectomics
Teaching Deck

---

## Learning Objectives
- Choose statistical models aligned to connectomics question types
- Construct and justify appropriate null models for graph analyses
- Control multiplicity and uncertainty in high-dimensional motif tests
- Report inferential claims with explicit assumptions and limits

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
Design and execute a connectomics inference plan that includes null-model choice, multiplicity control, uncertainty reporting, and explicit claim boundaries.

---

## Concept Focus
### 1) Null models encode scientific assumptions
- **Technical:** null models should preserve relevant graph constraints (degree sequence, spatial limits, cell-class composition) while randomizing the tested structure.
- **Plain language:** your "chance baseline" must reflect biology and data collection realities.
- **Misconception guardrail:** a generic random graph is an adequate null for a connectome.

---

## Core Workflow
- **Question-to-test mapping**
- Convert biological question into estimand(s), test set, and effect-size target.
- **Null-model design**
- Define null constraints and why they preserve key confounders.
- **Inference execution**
- Run model/tests with preregistered thresholds and multiplicity controls.
- **Robustness checks**
- Test sensitivity to preprocessing variant, sampling region, and parameter choice.
- **Claim calibration**
- Report supported, uncertain, and unsupported claims in separate blocks.

---

## 60-Minute Run-of-Show
- Read Technical Unit 09, section 2 — the worked reciprocity example across three null models.
- Bring one motif or connectivity claim from a paper you have read, with its stated null.
- **00:00-06:00 | Framing: the null is the scientific step**
- Prompt: "Same graph, same motif, three null models, three different conclusions. Which one is right?"
- Establish that the answer depends on what the hypothesis treats as uninteresting.
- **06:00-18:00 | Worked example: reciprocity across nulls**
- Instructor works the Unit 09 example live: 100 neurons, 1,200 edges, 210 reciprocal pairs.
- Erdos-Renyi gives 2.9x. Degree-preserving gives 1.4x. Degree-and-distance gives 1.14x, not significant.
- Think aloud about which null matches which hypothesis, not which gives the nicer number.
- **18:00-30:00 | Guided practice: write the uninteresting explanation**
- In pairs, learners take their brought-in claim and write, in words, the sentence "this result would be uninteresting if ___".
- Then name the null that preserves exactly that.
- Instructor circulates asking "what does your null preserve, and what does it randomize?"
- **30:00-40:00 | Multiplicity**
- Count the tests actually run, including unreported ones. Choose a correction and justify it.
- Surface the dependence problem: triad counts move together, so analytic p-values overstate confidence. Permutation inference respects the dependence.
- **40:00-50:00 | Robustness and error sensitivity**
- Each learner names one preprocessing choice (synapse threshold, inclusion criteria, boundary handling) and states how they would test sensitivity to it.
- Introduce the error-simulation check: perturb the graph at measured merge and split rates, report the band.
- **50:00-57:00 | Competency check**
- Each learner submits: estimand, null model with what it preserves, correction strategy, one robustness check, and one claim they will not make.
- **57:00-60:00 | Exit ticket**
- "One result I now doubt, and the null model that would settle it."
- **At 30 minutes:** every pair can state their null in terms of what it preserves, not just its name. If not, re-teach before proceeding.
- **At 50 minutes:** learners distinguish an exploratory finding from a confirmatory one in their own write-up.

---

## Misconceptions to Watch
- **Misconception guardrail:** a generic random graph is an adequate null for a connectome.
- **Misconception guardrail:** a small p-value speaks for itself, regardless of how many tests were run.
- **Misconception guardrail:** a hypothesis found in the data can be confirmed by the same data.

---

## Studio Activity
**Scenario:** A team reports motif enrichment in one dataset and asks whether the claim generalizes.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
**Minimum pass**

- Null model is justified and the constraints it preserves are listed explicitly, in terms of what the hypothesis treats as uninteresting.
- Total test count — including tests run and not reported — is documented, and a named correction is applied against it.
- Claims are partitioned into exploratory and confirmatory blocks with different language in each.

---

## Assessment Rubric
**Strong performance**

- Sensitivity analysis spans at least two preprocessing choices (synapse threshold, inclusion criteria), with results reported for each variant.
- Effect sizes with uncertainty intervals appear alongside every significance statement.
- Error-sensitivity band computed at measured merge and split rates, with the direction of merge bias named.
- Generalization boundary stated: which dataset, version, and region the claim covers, and what it says nothing about.

---

## Assessment Rubric
**Common failure modes**

- Null model choice disconnected from the biological question.
- Selective reporting: significant outcomes shown, the full test count uncounted.
- Exploratory signal conflated with validated inference.
- Analytic p-values used where dependence between tests calls for permutation.

---

## Exit Ticket
Write a 6-8 sentence inference note that includes:
1. hypothesis and estimand,
2. null-model assumptions,
3. multiplicity strategy,
4. one robust conclusion and one unresolved uncertainty.

---

## References (Instructor)
- Bassett, Zurn, and Gold (2018) - model use in network neuroscience.
- Januszewski et al. (2018) - segmentation performance and uncertainty context.
- MICrONS/FlyWire/H01 analyses for cross-dataset inference constraints.

---

## Teaching Materials
- Module page: /modules/module20/
- Slide page: /modules/slides/module20/
- Worksheet: /assets/worksheets/module20/module20-activity.md
