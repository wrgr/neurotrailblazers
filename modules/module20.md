---
title: "Module 20: Statistical Models and Inference for Connectomics"
layout: module
permalink: /modules/module20/
description: "Build defensible statistical inference workflows for connectomics analyses, from null models to uncertainty reporting."
module_number: 20
image: /assets/images/modules/module20.svg
image_alt: "Stylized vector art: two overlapping distributions with the effect gap bracketed."
difficulty: "Advanced"
duration: "4-6 hours"
learning_objectives:
  - "Choose statistical models aligned to connectomics question types"
  - "Construct and justify appropriate null models for graph analyses"
  - "Control multiplicity and uncertainty in high-dimensional motif tests"
  - "Report inferential claims with explicit assumptions and limits"
prerequisites: "Modules 12-19, including graph-analysis familiarity"
merit_stage: "Analysis"
compass_skills:
  - "Statistical Reasoning"
  - "Model Critique"
  - "Reproducible Analysis"
ccr_focus:
  - "Skills - Statistical Inference"
  - "Character - Epistemic Humility"

# Normalized metadata
slug: "module20"
short_title: "Statistical Models and Inference"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "inference"
  - "null-models"
  - "uncertainty"
  - "multiple-testing"
summary: "Design and critique statistical inference pipelines for connectomics with clear assumptions and reproducible outputs."
key_questions:
  - "Which null model is valid for this connectome hypothesis?"
  - "How should multiplicity be handled across motif families?"
  - "What claims are robust versus exploratory?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow/"
  - "/datasets/mouseconnects/"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic probability/statistics"
  - "Graph representation concepts"
next_modules:
  - "module21"
references:
  - "Bassett, Zurn, and Gold (2018) - model use in network neuroscience."
  - "Januszewski et al. (2018) - segmentation performance and uncertainty context."
  - "MICrONS/FlyWire/H01 analyses for cross-dataset inference constraints."
videos:
  - "https://www.neurotrailblazers.org/technical-training/09-connectome-analysis-neuroai/"
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Design and execute a connectomics inference plan that includes null-model choice, multiplicity control, uncertainty reporting, and explicit claim boundaries.

## Why this module matters
Connectomics analyses can produce thousands of statistically testable patterns. Without disciplined inference, teams risk publishing artifacts from preprocessing bias, multiple comparisons, or misaligned null assumptions.

## Concept set
### 1) Null models encode scientific assumptions
- **Technical:** null models should preserve relevant graph constraints (degree sequence, spatial limits, cell-class composition) while randomizing the tested structure.
- **Plain language:** your "chance baseline" must reflect biology and data collection realities.
- **Misconception guardrail:** a generic random graph is an adequate null for a connectome.

### 2) Multiplicity is structural, not optional
- **Technical:** motif families and subgroup analyses require correction strategies and predeclared test hierarchies.
- **Plain language:** if you test many patterns, some will look significant by accident.
- **Misconception guardrail:** a small p-value speaks for itself, regardless of how many tests were run.

### 3) Exploratory and confirmatory analyses must be separated
- **Technical:** hypothesis generation and hypothesis testing should have different reporting labels and evidence standards.
- **Plain language:** be clear about what you discovered versus what you validated.
- **Misconception guardrail:** a hypothesis found in the data can be confirmed by the same data.

### 4) Statistical challenges unique to connectomics
Connectomics datasets present several statistical difficulties that are uncommon in other fields. Massive multiple comparisons arise when testing thousands of motifs, cell-type pairs, or connection patterns simultaneously. Spatial autocorrelation is pervasive because nearby neurons share arbor overlap, creating non-independent edges that violate standard test assumptions. The threshold problem is particularly acute: choosing a minimum synapse count (e.g., 3 vs. 5 synapses to define a "real" connection) changes the resulting graph and all downstream statistics, yet no universally accepted threshold exists.

Researcher degrees of freedom in null model selection further compound these issues. Different null models that preserve different graph properties (degree sequence, spatial distance distribution, cell-type composition) can yield contradictory conclusions from the same data. Best practices include using permutation tests over parametric alternatives when distributional assumptions are uncertain, reporting effect sizes alongside p-values to distinguish statistical significance from biological relevance, and performing sensitivity analyses across multiple thresholds and null model variants to confirm that findings are robust rather than artifacts of a single analytical choice.

## Worked example: the motif that survived the null and died in the error band

The numbers below are illustrative — they show the shape of the reasoning, not results from a specific dataset. The companion example — the same reciprocity count yielding 2.9x enrichment, 1.4x, or no effect depending on the null — is worked line by line in [Technical Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}); read it first. This example starts where that one ends: the null is already chosen well, and the claim still falls apart.

You run a triad census on a 300-neuron subgraph: 16 directed three-node classes. The feedforward-loop triad looks enriched.

**Step 1: choose the null from the hypothesis, not the toolbox.** The hypothesis is "feedforward structure beyond what degree and distance explain," so the null must preserve each node's in- and out-degree and the empirical connection-probability-versus-distance curve. Rewiring 10,000 times gives a null mean of 350 feedforward loops, sd 20, against an observed 402: enrichment 1.15x, z = 2.6, nominal p = 0.009. So far this looks publishable.

**Step 2: count the tests you actually ran.** You tested all 16 triad classes, and before settling you looked at the graph under two synapse-count thresholds (at least 3 and at least 5 synapses per edge). That is 32 tests, not 1. Bonferroni at α = 0.05 requires p below 0.0016; your 0.009 does not clear it. Benjamini-Hochberg is more forgiving but depends on the other 31 results — and its verdict must be reported either way.

**Step 3: respect the dependence between tests.** Triad counts move together — adding one edge changes many triads at once — so treating the 16 tests as independent overstates confidence in both directions. Permutation inference over the whole census, using the maximum-enrichment statistic, respects the dependence; here it gives a family-wise p of 0.06 for the feedforward loop. Borderline, honestly computed.

**Step 4: run the error-sensitivity check.** Your validation work gives measured error rates: 2% merge, 6% split. Perturb the graph at those rates 200 times and recompute enrichment each time: the band spans 0.97 to 1.28 — it crosses 1.0. Worse, the bias is directional: merges manufacture dense motifs, so reconstruction error pushes the statistic toward exactly the result you are hoping for.

**Step 5: check threshold sensitivity.** At threshold 3 synapses, enrichment is 1.15x; at threshold 5 it drops to 1.04x. The effect is concentrated in weak edges — which is also where synapse-detection false positives concentrate.

**What gets reported.** An exploratory finding: "feedforward-loop counts are 1.15x the degree-and-distance null (permutation p = 0.06, family-wise), not robust to measured reconstruction error rates or to the edge threshold." The confirmatory path is written in the same paragraph: preregister the null, the threshold, and this single test, then run it on the next data release or a held-out region.

**What this example does not establish:** that the motif is absent. It shows only that this dataset, at these error rates, cannot support the enrichment claim — which is itself a result worth stating plainly.

## Core workflow: connectomics inference protocol
1. **Question-to-test mapping**
   - Convert biological question into estimand(s), test set, and effect-size target.
2. **Null-model design**
   - Define null constraints and why they preserve key confounders.
3. **Inference execution**
   - Run model/tests with preregistered thresholds and multiplicity controls.
4. **Robustness checks**
   - Test sensitivity to preprocessing variant, sampling region, and parameter choice.
5. **Claim calibration**
   - Report supported, uncertain, and unsupported claims in separate blocks.

## 60-minute tutorial run-of-show

### Pre-class preparation (15 min async)
- Read Technical Unit 09, section 2 — the worked reciprocity example across three null models.
- Bring one motif or connectivity claim from a paper you have read, with its stated null.

### Minute-by-minute plan
1. **00:00-06:00 | Framing: the null is the scientific step**
   - Prompt: "Same graph, same motif, three null models, three different conclusions. Which one is right?"
   - Establish that the answer depends on what the hypothesis treats as uninteresting.
2. **06:00-18:00 | Worked example: reciprocity across nulls**
   - Instructor works the Unit 09 example live: 100 neurons, 1,200 edges, 210 reciprocal pairs.
   - Erdos-Renyi gives 2.9x. Degree-preserving gives 1.4x. Degree-and-distance gives 1.14x, not significant.
   - Think aloud about which null matches which hypothesis, not which gives the nicer number.
3. **18:00-30:00 | Guided practice: write the uninteresting explanation**
   - In pairs, learners take their brought-in claim and write, in words, the sentence "this result would be uninteresting if ___".
   - Then name the null that preserves exactly that.
   - Instructor circulates asking "what does your null preserve, and what does it randomize?"
4. **30:00-40:00 | Multiplicity**
   - Count the tests actually run, including unreported ones. Choose a correction and justify it.
   - Surface the dependence problem: triad counts move together, so analytic p-values overstate confidence. Permutation inference respects the dependence.
5. **40:00-50:00 | Robustness and error sensitivity**
   - Each learner names one preprocessing choice (synapse threshold, inclusion criteria, boundary handling) and states how they would test sensitivity to it.
   - Introduce the error-simulation check: perturb the graph at measured merge and split rates, report the band.
6. **50:00-57:00 | Competency check**
   - Each learner submits: estimand, null model with what it preserves, correction strategy, one robustness check, and one claim they will not make.
7. **57:00-60:00 | Exit ticket**
   - "One result I now doubt, and the null model that would settle it."

### Formative checkpoints
- **At 30 minutes:** every pair can state their null in terms of what it preserves, not just its name. If not, re-teach before proceeding.
- **At 50 minutes:** learners distinguish an exploratory finding from a confirmatory one in their own write-up.

## Studio activity: motif inference challenge
{: #studio-activity}
**Scenario:** A team reports motif enrichment in one dataset and asks whether the claim generalizes.

**Tasks**
1. Propose at least two candidate null models and justify each.
2. Run or outline multiplicity-aware testing strategy across motif set.
3. Draft a results summary separating exploratory and confirmatory findings.
4. Add one robustness check for cross-dataset comparability.

**Expected outputs**
- Inference design sheet (estimand, null, tests, correction).
- One-page claim calibration summary.
- Robustness plan with pass/fail criteria.

## Assessment rubric
- **Minimum pass**
  - Null model is justified and the constraints it preserves are listed explicitly, in terms of what the hypothesis treats as uninteresting.
  - Total test count — including tests run and not reported — is documented, and a named correction is applied against it.
  - Claims are partitioned into exploratory and confirmatory blocks with different language in each.
- **Strong performance**
  - Sensitivity analysis spans at least two preprocessing choices (synapse threshold, inclusion criteria), with results reported for each variant.
  - Effect sizes with uncertainty intervals appear alongside every significance statement.
  - Error-sensitivity band computed at measured merge and split rates, with the direction of merge bias named.
  - Generalization boundary stated: which dataset, version, and region the claim covers, and what it says nothing about.
- **Common failure modes**
  - Null model choice disconnected from the biological question.
  - Selective reporting: significant outcomes shown, the full test count uncounted.
  - Exploratory signal conflated with validated inference.
  - Analytic p-values used where dependence between tests calls for permutation.

## Common errors and how to recover

- **You used an Erdos-Renyi null because it was one line of code.** Nearly every motif comes out "enriched," because degree heterogeneity alone produces that. Recover by rerunning under degree-preserving and degree-plus-distance nulls and reporting all three; the collapse in effect size across nulls is a finding, not a failure.
- **You forgot the tests you did not report.** Threshold trials, subgroup peeks, and abandoned motif families all count toward multiplicity. Recover by reconstructing the full test count from your notebook history and correcting against that number; whatever exploration cannot be reconstructed gets labeled exploratory, permanently.
- **Your p-values assume independent tests.** Triad counts are strongly correlated, so analytic corrections mislead in both directions. Recover by switching to permutation inference over the whole test family, which respects the dependence structure by construction.
- **The result flips with the synapse threshold.** Recover by reporting the statistic across thresholds (2, 3, 5) rather than picking the favorable one. If the effect lives only in weak edges, say so — that localization is informative, because weak edges are where detection error concentrates.
- **An exploratory find became confirmatory in the abstract.** Recover by relabeling honestly and writing the confirmatory path: preregistered null, threshold, and test, executed on a held-out region or the next data release. The same data cannot both generate and confirm the hypothesis.

## What this module does not cover

- **Graph construction choices.** Thresholding, direction, weights, and what each choice commits you to are [Technical Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}) and [graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}).
- **Null-model mechanics in detail.** The full reciprocity worked example and the null-model table live in [Technical Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}) and [motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }}); this module teaches when to reach for them, not their internals.
- **Measuring the error rates the sensitivity check needs.** Merge and split rates come from segmentation validation: [Module 14]({{ '/modules/module14/' | relative_url }}), [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}), and [metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}).
- **ML validity — leakage, splits, and base rates.** That is [Module 13]({{ '/modules/module13/' | relative_url }}), and it applies whenever a model produces the labels you test on.
- **Packaging the analysis for reuse.** Versioning, environments, and provenance are [Module 21]({{ '/modules/module21/' | relative_url }}).
- **Bayesian and generative model comparison.** Fitting competing generative models and comparing them with complexity penalties is relevant and out of scope here; the module handles null-based testing operationally.

## Content library references
- [Motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }}) — Null models and statistical testing for motifs
- [Network analysis methods]({{ '/content-library/connectomics/network-analysis-methods/' | relative_url }}) — Graph metrics requiring statistical interpretation
- [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) — Quality metrics with statistical properties

## Teaching resources
- Core unit context: [Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- Reading support: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dataset workflow context: [Workflow overview]({{ '/datasets/workflow/' | relative_url }})
- Quality controls context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## Evidence anchors from connectomics practice
### Key papers to use in this module
- [Bassett, Zurn, and Gold (2018)](https://doi.org/10.1038/s41583-018-0038-8)
- [Januszewski et al. (2018)](https://doi.org/10.1038/s41592-018-0049-4)
- [MICrONS visual cortex reconstruction (Nature, 2025)](https://www.nature.com/articles/s41586-025-08790-w)

### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [FlyWire](https://flywire.ai/)
- [neuPrint Hemibrain](https://neuprint.janelia.org/)

### Competency checks
- Can you defend your null-model assumptions in one paragraph?
- Can you report one finding with effect size, uncertainty, and limitation?
- Can you identify which result remains exploratory?

## Quick practice prompt
Write a 6-8 sentence inference note that includes:
1. hypothesis and estimand,
2. null-model assumptions,
3. multiplicity strategy,
4. one robust conclusion and one unresolved uncertainty.
