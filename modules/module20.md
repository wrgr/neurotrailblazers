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
  - "Bassett DS, Zurn P, Gold JI (2018) On the nature and use of models in network neuroscience. Nature Reviews Neuroscience 19(9):566-578."
  - "Milo R et al. (2002) Network motifs: simple building blocks of complex networks. Science 298(5594):824-827."
  - "Artzy-Randrup Y, Fleishman SJ, Ben-Tal N, Stone L (2004) Comment on Network motifs: simple building blocks of complex networks and Superfamilies of evolved and designed networks. Science 305(5687):1107."
  - "Song S, Sjostrom PJ, Reigl M, Nelson S, Chklovskii DB (2005) Highly nonrandom features of synaptic connectivity in local cortical circuits. PLoS Biology 3(3):e68."
  - "Benjamini Y, Hochberg Y (1995) Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal Statistical Society Series B 57(1):289-300."
  - "Nosek BA, Ebersole CR, DeHaven AC, Mellor DT (2018) The preregistration revolution. Proceedings of the National Academy of Sciences 115(11):2600-2606."
videos:
  - "https://www.neurotrailblazers.org/technical-training/09-connectome-analysis-neuroai/"
downloads: []
last_reviewed: 2026-09-28
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Design and execute a connectomics inference plan that includes null-model choice, multiplicity control, uncertainty reporting, and explicit claim boundaries.

## Why this module matters
Connectomics analyses can produce thousands of statistically testable patterns. Without disciplined inference, teams risk publishing artifacts from preprocessing bias, multiple comparisons, or misaligned null assumptions.

**Scope boundary with Module 08.** [Module 08]({{ '/modules/module08/' | relative_url }}) teaches the design of one test: a measurable outcome, one null model, and an interpretation boundary for one claim. This module starts where that ends and handles inference at scale: many tests at once, the dependence between them, reconstruction error as a directional bias, threshold sensitivity, and the separation of exploratory from confirmatory claims. If you have one hypothesis and one null, Module 08 is enough. If you have a census, you need this one.

## Concept set
### 1) Null models encode scientific assumptions
- **Technical:** null models should preserve relevant graph constraints (degree sequence, spatial limits, cell-class composition) while randomizing the tested structure.
- **Plain language:** your "chance baseline" must reflect biology and data collection realities.
- **Misconception guardrail:** a generic random graph is an adequate null for a connectome.
- **Why it fails:** a null that ignores degree and distance is beaten by almost any real graph, so the enrichment is a fact about the null, not the circuit. Preserve the constraints your hypothesis takes for granted and randomize only the structure you are testing.

### 2) Multiplicity is structural, not optional
- **Technical:** motif families and subgroup analyses require correction strategies and predeclared test hierarchies.
- **Plain language:** if you test many patterns, some will look significant by accident.
- **Misconception guardrail:** a small p-value speaks for itself, regardless of how many tests were run.
- **Why it fails:** at a 0.05 threshold, a census of 16 motif classes with nothing in it is expected to produce about one significant class (16 x 0.05 = 0.8). A p-value means what its family lets it mean, so report the family size and the correction with it.

### 3) Exploratory and confirmatory analyses must be separated
- **Technical:** hypothesis generation and hypothesis testing should have different reporting labels and evidence standards.
- **Plain language:** be clear about what you discovered versus what you validated.
- **Misconception guardrail:** a hypothesis found in the data can be confirmed by the same data.
- **Why it fails:** the data that suggested the hypothesis were selected for it, so a test on them is circular. Confirmation needs data the hypothesis has not seen: a held-out region reserved before the exploration, or the next release.

### 4) Statistical challenges unique to connectomics
Connectomics datasets present several statistical difficulties that are uncommon in other fields. Massive multiple comparisons arise when testing thousands of motifs, cell-type pairs, or connection patterns simultaneously. Spatial autocorrelation is pervasive because nearby neurons share arbor overlap, creating non-independent edges that violate standard test assumptions. The threshold problem is particularly acute: choosing a minimum synapse count (e.g., 3 vs. 5 synapses to define a "real" connection) changes the resulting graph and all downstream statistics, yet no universally accepted threshold exists.

Researcher degrees of freedom in null model selection further compound these issues. Different null models that preserve different graph properties (degree sequence, spatial distance distribution, cell-type composition) can yield contradictory conclusions from the same data. Best practices include using permutation tests over parametric alternatives when distributional assumptions are uncertain, reporting effect sizes alongside p-values to distinguish statistical significance from biological relevance, and performing sensitivity analyses across multiple thresholds and null model variants to confirm that a finding survives rather than depends on a single analytical choice.

- **Misconception guardrail:** if the result holds at one synapse threshold, it holds.
- **Why it fails:** the threshold changes the graph, so a result that appears at only one threshold is a result about that threshold. Report the statistic across the plausible range and say where it lives.

### 5) Reconstruction error is a directional bias, not noise
- **Technical:** merge errors join separate arbors, so they add edges between neurons that were already near each other and inflate dense motifs; split errors remove edges and deflate them. The two do not cancel, because they act on different motifs at different rates. The error-sensitivity check in the worked example below therefore reports a band with a direction: perturb the graph at the measured merge and split rates, recompute the statistic, and say which way the band moved relative to the observed value.
- **Plain language:** reconstruction mistakes push motif counts one way, and it is usually the way the enrichment claim points. Measure the push before you trust the claim.
- **Misconception guardrail:** segmentation errors add random noise that averages out over a large graph.
- **Why it fails:** merges and splits bias motif counts in opposite and unequal directions, and merges push toward denser motifs, which is the direction most enrichment claims point. Averaging over more of the graph averages the bias in, not out.

## Choosing a multiplicity correction: decision table

The correction follows from how the tests were generated and how much dependence they share. Choose the row before running the census, and write it down.

| Situation | Correction | What it gives you | What it costs you |
|---|---|---|---|
| A few tests declared in advance, and any single false positive is unacceptable | Bonferroni | Family-wise control that needs no assumption about dependence | Power falls with every test added; conservative when tests are dependent, which motif counts are |
| Many tests, and a stated fraction of false discoveries is acceptable | Benjamini-Hochberg false discovery rate | More discoveries at large test counts | The verdict on each test depends on the other tests' p-values, so a changed census changes every result; assumes independence or positive dependence |
| Tests are strongly dependent, as in a triad census where one edge moves many counts | Permutation inference on the maximum statistic across the family | Family-wise control that respects the dependence by construction | Compute cost; you need the null generator anyway, so this is usually the honest default |
| One hypothesis that survived exploration and now needs confirming | A preregistered single test on a held-out region or the next release | The only route from exploratory to confirmatory | A second dataset or a held-out region, which has to be reserved before the exploration starts |

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

## Time budget
The declared 4 to 6 hours are: the 15-minute pre-class reading below and about 30 minutes on the concept set, the 90-minute meeting the [16-week syllabus map]({{ '/teaching/syllabi/16-week/' | relative_url }}) gives this kit in week 10 (the 60-minute run-of-show below plus the opening of the studio activity; the 10-week map leaves this kit out), and 2 to 4 hours outside class running the studio's null models and finishing its write-up, the quick practice prompt, and the linked readings.

## 60-minute tutorial run-of-show

### Pre-class preparation (15 min async)
- Read section 2 of [Technical Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}), the worked reciprocity example across three null models.
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
**Scenario:** A team reports that E-to-I-to-E feedback loops are enriched in one dataset and asks whether the claim generalizes. Use the synthetic 200-neuron subgraph in the [Module 11 kit]({{ '/assets/kits/module11/README.md' | relative_url }}) as their dataset: it has cell types and soma positions, so degree, distance and cell-type nulls can all be built. Use the synthetic 500-neuron column graph in the [Module 10 kit]({{ '/assets/kits/module10/README.md' | relative_url }}) as the second dataset for the generalization check. Both are invented for teaching; no result from them describes a real brain.

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
- Reading support: [Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dataset workflow context: [Workflow overview]({{ '/datasets/workflow/' | relative_url }})
- Quality controls context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## Evidence anchors from connectomics practice
### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [FlyWire](https://flywire.ai/)
- [neuPrint Hemibrain](https://neuprint.janelia.org/)

### Competency checks
- Can you defend your null-model assumptions in one paragraph?
- Can you report one finding with effect size, uncertainty, and limitation?
- Can you identify which result remains exploratory?

## Academic references
- Bassett DS, Zurn P, Gold JI (2018) "On the nature and use of models in network neuroscience." *Nature Reviews Neuroscience* 19(9):566-578. doi:10.1038/s41583-018-0038-8. What a null model is a model of; the framing behind Concept 1.
- Milo R, Shen-Orr S, Itzkovitz S, Kashtan N, Chklovskii D, Alon U (2002) "Network motifs: simple building blocks of complex networks." *Science* 298(5594):824-827. doi:10.1126/science.298.5594.824. The motif census against a degree-preserving null that the worked example runs.
- Artzy-Randrup Y, Fleishman SJ, Ben-Tal N, Stone L (2004) "Comment on 'Network motifs: simple building blocks of complex networks' and 'Superfamilies of evolved and designed networks'." *Science* 305(5687):1107. doi:10.1126/science.1099334. Motif enrichment that vanishes under a null with spatial structure; why Concept 1 says the null encodes the hypothesis.
- Song S, Sjöström PJ, Reigl M, Nelson S, Chklovskii DB (2005) "Highly nonrandom features of synaptic connectivity in local cortical circuits." *PLoS Biology* 3(3):e68. doi:10.1371/journal.pbio.0030068. The reciprocity and motif result the run-of-show's reciprocity example is modeled on.
- Benjamini Y, Hochberg Y (1995) "Controlling the false discovery rate: a practical and powerful approach to multiple testing." *Journal of the Royal Statistical Society Series B* 57(1):289-300. doi:10.1111/j.2517-6161.1995.tb02031.x. The correction in the second row of the decision table.
- Nosek BA, Ebersole CR, DeHaven AC, Mellor DT (2018) "The preregistration revolution." *Proceedings of the National Academy of Sciences* 115(11):2600-2606. doi:10.1073/pnas.1708274114. Why the confirmatory path in Concept 3 is preregistered on new data.

## Quick practice prompt
Write a 6-8 sentence inference note that includes:
1. hypothesis and estimand,
2. null-model assumptions,
3. multiplicity strategy,
4. one conclusion that survives your checks and one unresolved uncertainty.
