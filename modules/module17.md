---
title: "Module 17: Scientific Writing for Connectomics"
layout: module
permalink: /modules/module17/
description: "Write clear, evidence-grounded connectomics manuscripts, figure legends, and response letters for technical audiences."
module_number: 17
image: /assets/images/modules/module17.svg
image_alt: "Stylized vector art: a manuscript page gaining structure, with a margin note arrowed into the text."
difficulty: "Intermediate"
duration: "4-5 hours"
learning_objectives:
  - "Convert connectomics analyses into coherent claim-evidence writing"
  - "Write figure legends that are reproducible and interpretation-safe"
  - "Draft abstracts that distinguish result, uncertainty, and limitation"
  - "Respond to reviewer critiques with technically grounded revisions"
prerequisites: "Modules 12-16 or equivalent analysis experience"
merit_stage: "Dissemination"
compass_skills:
  - "Scientific Communication"
  - "Critical Reading"
  - "Revision Practice"
ccr_focus:
  - "Skills - Scientific Communication"
  - "Character - Precision"

# Normalized metadata
slug: "module17"
short_title: "Scientific Writing for Connectomics"
status: "active"
audience:
  - "students"
pipeline_stage: "Dissemination"
merit_row_focus: "Dissemination"
topics:
  - "writing"
  - "peer-review-response"
  - "figure-legend"
summary: "Translate technical connectomics outputs into clear, defensible manuscripts and reviewer responses."
key_questions:
  - "What is the exact evidence for each claim?"
  - "Where does uncertainty belong in the narrative?"
  - "How should reviewers' methodological concerns be answered?"
slides: []
notebook: []
datasets:
  - "/datasets/mouseconnects/"
  - "/datasets/workflow/"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
related_tools:
  - "/tools/ask-an-expert/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic statistical interpretation of connectomics outputs"
  - "Ability to read method sections in technical papers"
next_modules:
  - "module18"
  - "module19"
references:
  - "Gopen GD, Swan JA (1990) The science of scientific writing. American Scientist."
  - "Mensh B, Kording K (2017) Ten simple rules for structuring papers. PLOS Computational Biology 13(9):e1005619."
  - "Wasserstein RL, Lazar NA (2016) The ASA statement on p-values: context, process, and purpose. The American Statistician 70(2):129-133."
  - "White JG, Southgate E, Thomson JN, Brenner S (1986) The structure of the nervous system of the nematode Caenorhabditis elegans. Philosophical Transactions of the Royal Society of London B 314(1165):1-340."
  - "The MICrONS Consortium (2025) Functional connectomics spanning multiple areas of mouse visual cortex. Nature 640(8058):435-447."
  - "Dorkenwald S et al. (2024) Neuronal wiring diagram of an adult brain. Nature 634(8032):124-138."
videos: []
downloads: []
last_reviewed: 2026-09-28
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Produce a manuscript-ready results section (figures, legends, and claims) where each conclusion is traceable to explicit connectomics evidence and stated limitations. Students will also be able to write methods sections with the level of detail required for connectomics reproducibility and respond to peer review with technically precise, non-defensive language.

## Why this module matters
Connectomics results are often complex and high-dimensional. Weak writing can overstate conclusions, hide uncertainty, or make methods irreproducible. Clear writing is part of technical rigor. In connectomics the methods section carries unusual weight, because readers must judge data quality, reconstruction fidelity, and proofreading completeness before they can evaluate any biological claim. A methods section that omits the dataset version, segmentation pipeline, or proofreading state leaves every result in the paper unverifiable.

**Scope boundary with Module 22.** This module owns the written record: manuscript structure, methods provenance, figure legends, and the reviewer response. [Module 22: Scientific Presentation]({{ '/modules/module22/' | relative_url }}) owns the spoken version of the same result: the claim tree for a talk, the time budget, the one-line provenance statement on a slide, and Q&A. The evidentiary standard is the same in both. What differs is that a paper is read out of order and checked at leisure, while a talk is heard once, so the two need different structures.

## Concept set

### 1) Structure of a connectomics paper: methods are unusually important
- **Technical:** in most neuroscience papers, the methods section is a reference appendix. In connectomics, it is primary evidence. Readers need to assess: What volume was imaged? At what resolution? What species, age, and preparation? Which segmentation algorithm was used, and what was the merge/split error rate? What proofreading version was the analysis based on? Was CAVE materialization pinned to a specific timestamp? Without these details, no biological claim is evaluable.
- **Plain language:** in connectomics, how you got the data is as important as what the data shows. Skeptical readers spend the most time in your methods section.
- **Misconception guardrail:** the methods section is a formality to write last.
- **Why it fails:** in connectomics the methods constrain what you can legitimately claim, so draft them first.

### 2) Claim-evidence mapping
- **Technical:** each claim should map to a figure panel, metric, and method reference. Build a claim-evidence matrix before drafting prose: one row per claim, columns for figure panel, statistical test, effect size, dataset version, and caveat. This matrix becomes the skeleton of your results section.
- **Plain language:** no claim without visible evidence. If you cannot point to a specific figure panel and a specific number, the claim is unsupported.
- **Misconception guardrail:** stronger language makes weak evidence more convincing.
- **Why it fails:** adjectives like "striking," "remarkable," and "clearly" do not substitute for effect sizes and confidence intervals, and reviewers read them as a warning sign.

### 3) Writing about uncertainty and interpretation limits
- **Technical:** connectomics data has characteristic uncertainty sources: segmentation errors (false merges and splits), synapse detection false positives/negatives, incomplete proofreading, boundary effects from finite volumes, and sampling bias from studying one animal or one brain region. Each of these should be acknowledged in the results and discussion with specific language: "Given the estimated false merge rate of X%, this connection count may overestimate true connectivity by up to Y%." Confidence levels should use calibrated language: "consistent with," "suggestive of," "insufficient evidence to distinguish from chance."
- **Plain language:** show what you do not know yet, not just what you found. Readers respect honesty about limits more than they respect false confidence.
- **Misconception guardrail:** stating uncertainty makes a paper look weak.
- **Why it fails:** uncertainty statements tell a reader what would reproduce and what might not. A paper that states its limits is more credible than one that ignores them.

### 4) Describing datasets with full provenance
- **Technical:** every connectomics paper should specify: species and strain, animal age, tissue preparation method, EM imaging modality and resolution (e.g., "serial section TEM at 4x4x30 nm"), total volume dimensions, segmentation pipeline and version, proofreading version or CAVE materialization timestamp, and any filtering applied (e.g., "neurons with fewer than 5 synapses were excluded"). This information belongs in the methods section, not buried in supplementary materials.
- **Plain language:** describe your dataset the way you would describe a reagent: precisely enough that someone else could find it and use it.
- **Misconception guardrail:** readers will know which dataset version you used.
- **Why it fails:** within one project (MICrONS, for example), different materialization versions produce different connectivity tables.

### 5) The methods reproducibility checklist
- **Technical:** before submission, verify that your methods section includes:
  - Dataset identifier and version (e.g., "MICrONS minnie65_public, CAVE materialization v1300")
  - Segmentation pipeline name and version
  - Proofreading state and any manual corrections
  - Code repository URL with commit hash or release tag
  - All parameters for analysis scripts (thresholds, filter criteria, random seeds)
  - Hardware/software environment if compute-sensitive
  - Any data exclusion criteria with justification
- **Plain language:** if someone cannot rerun your analysis from your methods section alone, it is not complete.
- **Misconception guardrail:** a link to the code repository makes the analysis reproducible.
- **Why it fails:** without a tagged release or a named commit in the methods, the link points at code that keeps changing.

### 6) Uncertainty-forward reporting
- **Technical:** confidence intervals, error modes, and sampling limits belong in results and discussion, not only supplements. Report effect sizes alongside p-values. Use language that distinguishes statistical significance from biological significance. Separate confirmed findings from exploratory observations.
- **Plain language:** a p-value says whether an effect is distinguishable from chance; the effect size and interval say whether it matters.
- **Misconception guardrail:** confidence intervals can live in the supplement as long as the main text reports p-values.
- **Why it fails:** a reader deciding whether to trust the headline needs the interval in the same sentence as the number.

### 7) References and citation practices in connectomics
- **Technical:** connectomics has specific citation norms: cite the dataset paper (not just the project website), cite the segmentation method paper, cite proofreading tools used, and cite any community contributions (e.g., FlyWire community proofreaders). When using public datasets, follow the project's citation guidelines. Preprints should be cited as preprints, not as if they were peer-reviewed. When multiple versions of a dataset exist, cite the specific version used.
- **Plain language:** give credit accurately and specifically. Citing "the FlyWire dataset" without the version or the community contribution paper is incomplete.
- **Misconception guardrail:** citing the original EM paper covers all required attributions.
- **Why it fails:** segmentation, proofreading, and annotation are separate contributions with their own papers and citation requests.

### 8) Reviewer-response engineering
- **Technical:** responses should specify action taken, location of revision, and rationale when a request is declined. Use a structured format: quote the reviewer comment, state your response, and reference the specific manuscript location of any change. When you disagree with a reviewer, provide evidence rather than opinion.
- **Plain language:** answer critiques like an engineer debugging a system. Be specific, be evidence-based, and be respectful.
- **Misconception guardrail:** a firm, defensive reply shows confidence in the work.
- **Why it fails:** defensiveness costs credibility. Do not call a reviewer's comment "wrong"; give the evidence that supports your position.

## Worked example: from a kit table to a results sentence

The numbers here are computed from `input_synapses_by_layer.csv` in the [Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }}): 160 synthetic excitatory neurons, 40 per layer, generated from a fixed seed. They describe no real brain; the point is the shape of the sentence, and the numbers are there so you can check it.

The table gives a median of 861.5 input synapses per neuron in layer 2/3 and 1,125.5 in layer 4. The ratio of medians is 1.31. A bootstrap over neurons (10,000 resamples, seed 1) gives a 95% interval of 1.02 to 1.57. Layer 6 has the lowest median, 656.

**Draft 1, the overclaim.** "Layer 4 excitatory neurons receive dramatically more synaptic input than layer 2/3 neurons, consistent with their role as the primary thalamic recipient layer."

Four things are wrong. "Dramatically" stands where a number should be. There is no n, no interval and no version. "Consistent with their role" is a functional story imported from the literature; nothing in a synapse count tests it. And a reader who wants to check the sentence has nowhere to go.

**Draft 2, the calibrated version.** "Layer 4 excitatory neurons received more input synapses than layer 2/3 neurons (median 1,126 vs 862, n = 40 per layer; ratio of medians 1.31, bootstrap 95% CI 1.02 to 1.57; Fig. 3c). The lower bound of the interval is close to 1, so the difference is modest and the sample is small. Counts come from the automated synapse table at the stated version with no proofreading; incomplete reconstructions lower both medians, and would bias the ratio if truncation differed by layer, which we did not test."

Every clause now has a job. The number and the interval sit in the same sentence, so a reader judging the headline sees both at once. The caveat is specific and directional: it names the mechanism (truncation), the direction it would push, and the check that was not done.

**The methods paragraph that supports it.** "Input synapse counts per neuron were read from `input_synapses_by_layer.csv` (Module 16 kit, generated by `scripts/generate_kit_materials.rb` from a fixed seed; n = 40 neurons per layer). Medians were compared by the ratio of medians, with a 95% percentile interval from 10,000 bootstrap resamples of neurons within each layer (random seed 1). No synapses were excluded." Three sentences, and a stranger can rerun it.

**The legend sentence.** "Fig. 3c. Input synapses per excitatory neuron by layer (n = 40 per layer; points are neurons; bar is the median; whiskers are the bootstrap 95% interval of the median). Synthetic kit data at the version given in Methods; no proofreading applied."

**The reviewer comment, and the reply.** Reviewer: "The bootstrap interval nearly touches 1. Why is this claim in the abstract?" Reply, in the structured form: quote the comment; then "We agree the effect is modest. We have removed the claim from the abstract and rewritten it in the results (paragraph 3) with the interval in the same sentence as the ratio, as quoted above. We have added the untested layer-dependent truncation as a limitation (Discussion, paragraph 2)." The reply concedes the valid point, names the change, and gives the location. It does not argue that the reviewer misread the interval, because the reviewer did not.

**What this example does not establish.** That a ratio of medians is the right statistic. On another question a difference in means with a t-based interval, or a rank test, would be the honest choice; the sentence structure is the same either way. Which statistic belongs to which question is [Module 20]({{ '/modules/module20/' | relative_url }}).

## Core workflow: from analysis output to paper text
1. **Evidence inventory**
   - List candidate claims and required supporting figures/metrics.
   - Build a claim-evidence matrix: claim, figure panel, statistical test, effect size, dataset version, caveat.
2. **Methods drafting (first, not last)**
   - Write the dataset description with full provenance.
   - Document every preprocessing step, threshold, and parameter.
   - Complete the reproducibility checklist.
3. **Results drafting**
   - Write one paragraph per claim cluster with explicit evidence pointers.
   - Use calibrated uncertainty language throughout.
   - Separate confirmed findings from exploratory observations.
4. **Legend hardening**
   - Ensure legends include dataset version, method variant, key parameters, sample sizes, and uncertainty indicators.
   - Each legend should be interpretable without reading the main text.
5. **Limitation pass**
   - Add interpretation bounds (sampling, segmentation error, model assumptions, volume boundary effects).
   - Quantify uncertainty where possible rather than using vague qualifiers.
6. **Peer-review simulation**
   - Exchange sections and produce one methods-focused critique plus one interpretation critique.
   - Practice structured reviewer responses.

## Time budget
The declared 4 to 5 hours are: about 30 minutes reading the concept set before the meeting, the 90-minute meeting the [syllabus maps]({{ '/teaching/syllabi/' | relative_url }}) give this kit (the 60-minute run-of-show below plus the opening of the studio activity), and 2 to 3 hours outside class finishing the studio drafts, the quick practice prompt, and the linked readings.

## 60-minute tutorial run-of-show

### Materials needed
- One mock connectomics figure set (3 panels) with underlying data tables: each learner's Module 16 figure package, or three figures the instructor makes from the [Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }}) (synthetic).
- Claim-evidence matrix template (printed or digital): the seven columns in studio task 2.
- Methods reproducibility checklist (one per student): Concept 5 on this page.
- Two mock reviewer comments (one valid methodological concern, one partially mistaken interpretation critique), given in full in the 38:00-50:00 block.
- Timer visible to all students.

### Timing and instructor script

**00:00-08:00 | Good writing vs bad writing in connectomics**
Instructor displays two versions of the same results paragraph: one with vague claims and missing provenance ("We found strong connectivity between these cell types"), one with precise language and full evidence pointers ("Layer 4 excitatory neurons formed 3.2x more synapses onto PV+ interneurons than expected by the degree-preserving null model (95% CI: 2.8-3.6x, n=847 connections, release T17)"; invented figures from a fictional mouse cortex volume, not measured from any real dataset). Students identify what makes the second version stronger. Key script line: "Every sentence in a results section should be falsifiable. If a skeptic cannot check your claim against your data, it is not a scientific sentence."

**08:00-18:00 | Claim-evidence matrix construction**
Students receive the mock figure set and build a claim-evidence matrix. Instructor models the first row, then students complete three more rows independently. Instructor circulates, pushing students to be specific: "Which panel? What is the effect size? What is the caveat?"

**18:00-28:00 | Results paragraph drafting**
Students draft a 200-word results paragraph from their matrix. Instructor emphasizes: lead with the finding, follow with the evidence pointer, close with the caveat. Students read their paragraphs aloud to a partner, who checks each claim against the matrix.

**28:00-38:00 | Methods and provenance exercise**
Instructor presents a deliberately incomplete methods section (missing dataset version, no proofreading state, no code commit hash), for example: "Synapses were obtained from the CAVE synapse table and filtered by cleft score. Motifs were counted in Python and compared with a random null model." Students use the reproducibility checklist to identify gaps and rewrite the section. Key script line: "If I handed you this methods section and asked you to reproduce the analysis, what would you be unable to do?"

**38:00-50:00 | Reviewer response practice**
Students receive two mock reviewer comments. Comment 1: "The authors do not report the false merge rate for their segmentation. How can we trust the synapse counts?" (valid). Comment 2: "The sample size of 847 connections is too small for any statistical conclusion" (partially mistaken --- depends on effect size and test). Students draft structured responses: quote, response, manuscript reference. Instructor reviews two examples live.

**50:00-58:00 | Peer exchange and feedback**
Students swap their results paragraph and methods section with a neighbor. Each student writes one specific improvement suggestion for each document. Students revise based on feedback.

**58:00-60:00 | Competency check**
Students submit their claim-evidence matrix and one revised paragraph. Instructor collects and reviews after session.

### Success criteria for this session
- Every claim in the results paragraph maps to a specific figure panel and metric.
- Methods section passes the reproducibility checklist with no critical gaps.
- Reviewer responses are structured, specific, and non-defensive.

## Studio activity: claim-to-paragraph writing sprint
{: #studio-activity}

**Scenario:** You are preparing a short paper section on motif enrichment from a connectome analysis. Your team has identified that reciprocal connections between excitatory and inhibitory neurons in cortical layer 2/3 occur 2.1x more frequently than expected under a degree-preserving null model. The analysis used a fictional mouse cortex volume, release T17, with synapse detection via the release's synapse table (cleft score threshold > 50). A total of 1,247 reciprocal pairs were observed across 12,891 possible excitatory-inhibitory pairs. The volume, the release and every number here are synthetic, invented for this exercise; none describes a real dataset.

**Tasks**
1. Draft three result claims from the scenario above, each with different confidence levels (strong, moderate, exploratory).
2. Build a claim-evidence matrix (claim, figure panel, metric, statistical test, effect size, dataset version, caveat).
3. Write a 300-400 word results subsection with calibrated uncertainty language.
4. Write a methods paragraph with full dataset provenance and reproducibility details.
5. Respond to two mock reviewer comments:
   - Reviewer A: "The cleft score threshold of 50 seems arbitrary. How sensitive are results to this choice?"
   - Reviewer B: "The authors should compare their findings to FlyWire data to demonstrate generality."

**Expected outputs**
- Claim-evidence matrix (complete, with no empty cells).
- Results subsection draft (300-400 words, every claim traceable).
- Methods paragraph with full provenance.
- Reviewer response draft with revision notes (structured format: quote, response, manuscript location).

## Assessment rubric
- **Minimum pass**
  - Claims map to explicit evidence with figure panel references.
  - Legends contain enough detail for independent interpretation.
  - Methods include dataset version, pipeline, and key parameters.
  - Reviewer responses are specific and technically grounded.
- **Strong performance**
  - Separates established findings from tentative interpretations using calibrated language.
  - Uses limitation language without weakening valid conclusions.
  - Improves reproducibility via concrete method-detail additions.
  - Reviewer responses include evidence and specific manuscript revision locations.
- **Common failure modes**
  - Narrative claims that cannot be traced to figures.
  - Missing dataset/method versioning in captions or methods.
  - Reviewer replies that are persuasive but non-technical.
  - Methods section written as an afterthought with missing parameters.

## Common errors and how to recover

- **The results paragraph reads well and no sentence in it can be checked.** Recover by building the claim-evidence matrix after the fact: every sentence gets a figure panel and a number, or it gets cut. The sentences that survive are the results section.
- **The methods say "the latest release".** Recover by pinning the version, recomputing every number that depends on it, and putting the version in the methods and in every legend. If the numbers moved, that movement is reported, not hidden.
- **The confidence interval is in the supplement and the p-value is in the text.** Recover by moving the interval into the sentence that carries the number. If the claim then looks weaker, the claim was too strong; rewrite it, not the layout.
- **"Consistent with" is doing the work of a test you did not run.** Recover by separating what was measured from what it might mean: the measurement stays in the results, the mechanism moves to the discussion and is labeled untested.
- **A reviewer is partly wrong and your reply says so first.** Recover by conceding the valid part in the first sentence, giving the evidence for the rest, and citing the manuscript location of every change. The order matters more than the content.
- **The citation list names a project website and no papers.** Recover by citing the dataset paper, the segmentation method, the proofreading and annotation contributions, and the version, following the project's own citation guidance.
- **The methods were written last and the analysis cannot be described.** Recover by writing them from the provenance record, the five elements in [Module 21]({{ '/modules/module21/' | relative_url }}). If no record exists, the analysis has to be rerun with one before the paper can be finished.

## What this module does not cover

- **Designing the figures.** Plot choice, color, uncertainty encoding and accessibility are [Module 16]({{ '/modules/module16/' | relative_url }}); here the figures exist and the question is what the text may claim from them.
- **The talk.** Slides, the time budget and Q&A are [Module 22]({{ '/modules/module22/' | relative_url }}).
- **Abstracts, posters and conference conduct.** [Module 23]({{ '/modules/module23/' | relative_url }}).
- **Whether the statistics behind a sentence are sound.** Null models, multiplicity and the exploratory-confirmatory split are [Module 20]({{ '/modules/module20/' | relative_url }}); this module assumes the analysis is defensible and teaches how to say so.
- **Packaging the analysis for reuse.** The provenance record the methods section draws on is [Module 21]({{ '/modules/module21/' | relative_url }}).
- **Reviewing other people's papers, and authorship.** The reviewer's side of the exchange and credit rules are [Module 19]({{ '/modules/module19/' | relative_url }}).
- **Grant and fellowship writing.** Not covered by any module; the claim discipline here transfers, the genre does not.

## Content library cross-references
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) --- the versioning infrastructure that underlies reproducible methods reporting in connectomics.

## Teaching resources
- Writing context in technical track: [Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- Reading support: [Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Vocabulary support: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Mentorship and feedback context: [Ask an Expert]({{ '/ask-an-expert/' | relative_url }})

## Evidence anchors from connectomics practice

### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [FlyWire](https://flywire.ai/)
- [Workflow overview]({{ '/datasets/workflow/' | relative_url }})

### Competency checks
- Can you point each conclusion to a specific figure/metric pair?
- Can you rewrite one overclaim into a defensible interpretation with calibrated language?
- Can you answer a reviewer concern with concrete revision language and a manuscript reference?
- Does your methods section pass the reproducibility checklist with no critical gaps?
- Are all dataset versions, code commits, and parameters explicitly documented?

## Academic references
- Gopen GD, Swan JA (1990) "The science of scientific writing." *American Scientist*, 1990. Not registered on Crossref; verified against the reprint hosted at [usenix.org](https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf). Reader expectations: put the stress position at the end of the sentence.
- Mensh B, Kording K (2017) "Ten simple rules for structuring papers." *PLOS Computational Biology* 13(9):e1005619. doi:10.1371/journal.pcbi.1005619. One paper, one contribution; the claim-first structure behind Concept 2.
- Wasserstein RL, Lazar NA (2016) "The ASA statement on *p*-values: context, process, and purpose." *The American Statistician* 70(2):129-133. doi:10.1080/00031305.2016.1154108. Why Concept 6 puts the effect size and interval next to the p-value.
- White JG, Southgate E, Thomson JN, Brenner S (1986) "The structure of the nervous system of the nematode *Caenorhabditis elegans*." *Philosophical Transactions of the Royal Society of London B* 314(1165):1-340. doi:10.1098/rstb.1986.0056. The original connectome paper; read its methods as a model of what a reader needs.
- The MICrONS Consortium (2025) "Functional connectomics spanning multiple areas of mouse visual cortex." *Nature* 640(8058):435-447. doi:10.1038/s41586-025-08790-w. A methods section that states section counts, resolution, and proofreading state; the source of the v1300 example in Concept 5.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634(8032):124-138. doi:10.1038/s41586-024-07558-y. How community proofreading is credited in the author list, which is what Concept 7 asks you to cite.

## Quick practice prompt
Write one results paragraph from a connectomics figure and include:
1. one quantitative claim with effect size and confidence interval,
2. one explicit caveat tied to a known data limitation,
3. one sentence on reproducibility assumptions (dataset version, materialization, code),
4. one figure legend sentence that specifies sample size and uncertainty indicator.
