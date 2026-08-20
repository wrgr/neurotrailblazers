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
- **Misconception guardrail:** a generic random graph is rarely an adequate connectomics null.

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
- **Misconception guardrail:** a generic random graph is rarely an adequate connectomics null.
- **Misconception guardrail:** reporting only p-values without multiplicity context is incomplete.
- **Misconception guardrail:** post-hoc storytelling is not confirmatory inference.

---

## Studio Activity
{: #studio-activity}
**Scenario:** A team reports motif enrichment in one dataset and asks whether the claim generalizes.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass**
- Null model is justified and constraints are explicit.
- Multiplicity handling is documented and applied.
- Claims are partitioned by confidence level.
- **Strong performance**
- Demonstrates sensitivity analysis against preprocessing and sampling choices.
- Reports effect sizes and uncertainty, not significance alone.
- Provides clear boundaries on generalization.
- **Common failure modes**
- Null model choice disconnected from biological question.
- Selective reporting of significant outcomes.
- Conflation of exploratory signal with validated inference.

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
