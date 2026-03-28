---
title: "Module 17: Scientific Writing for Connectomics"
layout: module
permalink: /modules/module17/
description: "Write clear, evidence-grounded connectomics manuscripts, figure legends, and response letters for technical audiences."
module_number: 17
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
  - "/datasets/mouseconnects"
  - "/datasets/workflow"
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
  - "Gopen and Swan (1990) - The science of scientific writing."
  - "White et al. (1986) - foundational connectome reporting style."
  - "Januszewski et al. (2018) - modern method reporting and performance framing."
videos:
  - "https://www.neurotrailblazers.org/technical-training/journal-club/"
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Produce a manuscript-ready results section (figures, legends, and claims) where each conclusion is traceable to explicit connectomics evidence and stated limitations. Students will also be able to write methods sections with the level of detail required for connectomics reproducibility and respond to peer review with technically precise, non-defensive language.

## Why this module matters
Connectomics results are often complex and high-dimensional. Weak writing can overstate conclusions, hide uncertainty, or make methods irreproducible. Strong scientific writing is not presentation polish; it is part of technical rigor. In connectomics specifically, the methods section carries unusual weight because readers must assess data quality, reconstruction fidelity, and proofreading completeness before they can evaluate any biological claim. A methods section that omits the dataset version, segmentation pipeline, or proofreading state is not merely incomplete --- it is scientifically irresponsible.

## Concept set

### 1) Structure of a connectomics paper: methods are unusually important
- **Technical:** in most neuroscience papers, the methods section is a reference appendix. In connectomics, it is primary evidence. Readers need to assess: What volume was imaged? At what resolution? What species, age, and preparation? Which segmentation algorithm was used, and what was the merge/split error rate? What proofreading version was the analysis based on? Was CAVE materialization pinned to a specific timestamp? Without these details, no biological claim is evaluable.
- **Plain language:** in connectomics, how you got the data is as important as what the data shows. Your methods section is not boilerplate --- it is where skeptical readers will spend the most time.
- **Misconception guardrail:** treating the methods section as a formality to write last. In connectomics, draft the methods first because they constrain what you can legitimately claim.

### 2) Claim-evidence mapping
- **Technical:** each claim should map to a figure panel, metric, and method reference. Build a claim-evidence matrix before drafting prose: one row per claim, columns for figure panel, statistical test, effect size, dataset version, and caveat. This matrix becomes the skeleton of your results section.
- **Plain language:** no claim without visible evidence. If you cannot point to a specific figure panel and a specific number, the claim is unsupported.
- **Misconception guardrail:** writing stronger language does not strengthen weak evidence. Adjectives like "striking," "remarkable," and "clearly" do not substitute for effect sizes and confidence intervals.

### 3) Writing about uncertainty and interpretation limits
- **Technical:** connectomics data has characteristic uncertainty sources: segmentation errors (false merges and splits), synapse detection false positives/negatives, incomplete proofreading, boundary effects from finite volumes, and sampling bias from studying one animal or one brain region. Each of these should be acknowledged in the results and discussion with specific language: "Given the estimated false merge rate of X%, this connection count may overestimate true connectivity by up to Y%." Confidence levels should use calibrated language: "consistent with," "suggestive of," "insufficient evidence to distinguish from chance."
- **Plain language:** show what you do not know yet, not just what you found. Readers respect honesty about limits more than they respect false confidence.
- **Misconception guardrail:** uncertainty statements are not weakness; they are reproducibility signals. A paper that acknowledges its limits is more credible than one that ignores them.

### 4) Describing datasets with full provenance
- **Technical:** every connectomics paper should specify: species and strain, animal age, tissue preparation method, EM imaging modality and resolution (e.g., "serial section TEM at 4x4x30 nm"), total volume dimensions, segmentation pipeline and version, proofreading version or CAVE materialization timestamp, and any filtering applied (e.g., "neurons with fewer than 5 synapses were excluded"). This information belongs in the methods section, not buried in supplementary materials.
- **Plain language:** describe your dataset the way you would describe a reagent: precisely enough that someone else could find it and use it.
- **Misconception guardrail:** assuming readers know which dataset version you used. Even within the same project (e.g., MICrONS), different materialization timestamps produce different connectivity tables.

### 5) The methods reproducibility checklist
- **Technical:** before submission, verify that your methods section includes:
  - Dataset identifier and version (e.g., "MICrONS minnie65, CAVE materialization v795")
  - Segmentation pipeline name and version
  - Proofreading state and any manual corrections
  - Code repository URL with commit hash or release tag
  - All parameters for analysis scripts (thresholds, filter criteria, random seeds)
  - Hardware/software environment if compute-sensitive
  - Any data exclusion criteria with justification
- **Plain language:** if someone cannot rerun your analysis from your methods section alone, it is not complete.
- **Misconception guardrail:** linking to a GitHub repository is not sufficient if the repository has no tagged release and the methods do not specify which commit was used.

### 6) Uncertainty-forward reporting
- **Technical:** confidence intervals, error modes, and sampling limits belong in results and discussion, not only supplements. Report effect sizes alongside p-values. Use language that distinguishes statistical significance from biological significance. Separate confirmed findings from exploratory observations.
- **Plain language:** show what you do not know yet, not just what you found.
- **Misconception guardrail:** uncertainty statements are not weakness; they are reproducibility signals.

### 7) References and citation practices in connectomics
- **Technical:** connectomics has specific citation norms: cite the dataset paper (not just the project website), cite the segmentation method paper, cite proofreading tools used, and cite any community contributions (e.g., FlyWire community proofreaders). When using public datasets, follow the project's citation guidelines. Preprints should be cited as preprints, not as if they were peer-reviewed. When multiple versions of a dataset exist, cite the specific version used.
- **Plain language:** give credit accurately and specifically. Citing "the FlyWire dataset" without the version or the community contribution paper is incomplete.
- **Misconception guardrail:** assuming that citing the original EM paper covers all required attributions. Segmentation, proofreading, and annotation are separate contributions that deserve separate citations.

### 8) Reviewer-response engineering
- **Technical:** responses should specify action taken, location of revision, and rationale when a request is declined. Use a structured format: quote the reviewer comment, state your response, and reference the specific manuscript location of any change. When you disagree with a reviewer, provide evidence rather than opinion.
- **Plain language:** answer critiques like an engineer debugging a system. Be specific, be evidence-based, and be respectful.
- **Misconception guardrail:** defensive tone weakens technical credibility. Never characterize a reviewer's comment as "wrong" --- instead, provide the evidence that supports your position.

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

## 60-minute tutorial run-of-show

### Materials needed
- One mock connectomics figure set (3 panels) with underlying data tables.
- Claim-evidence matrix template (printed or digital).
- Methods reproducibility checklist (one per student).
- Two mock reviewer comments (one valid methodological concern, one partially mistaken interpretation critique).
- Timer visible to all students.

### Timing and instructor script

**00:00-08:00 | Good writing vs bad writing in connectomics**
Instructor displays two versions of the same results paragraph: one with vague claims and missing provenance ("We found strong connectivity between these cell types"), one with precise language and full evidence pointers ("Layer 4 excitatory neurons formed 3.2x more synapses onto PV+ interneurons than expected by the degree-preserving null model (95% CI: 2.8-3.6x, n=847 connections, MICrONS v795)"). Students identify what makes the second version stronger. Key script line: "Every sentence in a results section should be falsifiable. If a skeptic cannot check your claim against your data, it is not a scientific sentence."

**08:00-18:00 | Claim-evidence matrix construction**
Students receive the mock figure set and build a claim-evidence matrix. Instructor models the first row, then students complete three more rows independently. Instructor circulates, pushing students to be specific: "Which panel? What is the effect size? What is the caveat?"

**18:00-28:00 | Results paragraph drafting**
Students draft a 200-word results paragraph from their matrix. Instructor emphasizes: lead with the finding, follow with the evidence pointer, close with the caveat. Students read their paragraphs aloud to a partner, who checks each claim against the matrix.

**28:00-38:00 | Methods and provenance exercise**
Instructor presents a deliberately incomplete methods section (missing dataset version, no proofreading state, no code commit hash). Students use the reproducibility checklist to identify gaps and rewrite the section. Key script line: "If I handed you this methods section and asked you to reproduce the analysis, what would you be unable to do?"

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

**Scenario:** You are preparing a short paper section on motif enrichment from a connectome analysis. Your team has identified that reciprocal connections between excitatory and inhibitory neurons in cortical layer 2/3 occur 2.1x more frequently than expected under a degree-preserving null model. The analysis used MICrONS minnie65 data, CAVE materialization v795, with synapse detection via the CAVE synapse table (cleft score threshold > 50). A total of 1,247 reciprocal pairs were observed across 12,891 possible excitatory-inhibitory pairs.

**Tasks**
1. Draft three result claims from the provided scenario, each with different confidence levels (strong, moderate, exploratory).
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
  - Clearly separates robust findings from tentative interpretations using calibrated language.
  - Uses limitation language without weakening valid conclusions.
  - Improves reproducibility via concrete method-detail additions.
  - Reviewer responses include evidence and specific manuscript revision locations.
- **Common failure modes**
  - Narrative claims that cannot be traced to figures.
  - Missing dataset/method versioning in captions or methods.
  - Reviewer replies that are persuasive but non-technical.
  - Methods section written as an afterthought with missing parameters.

## Content library cross-references
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) --- the versioning infrastructure that underlies reproducible methods reporting in connectomics.

## Teaching resources
- Writing context in technical track: [Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- Reading support: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Vocabulary support: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Mentorship and feedback context: [Ask-an-Expert]({{ '/tools/ask-an-expert/' | relative_url }})

## Evidence anchors from connectomics practice

### Key papers to use in this module
- [Gopen, G.D. and Swan, J.A. (1990). "The Science of Scientific Writing." *American Scientist*, 78(6), 550-558.](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing) --- foundational principles of clear scientific prose.
- [White, J.G. et al. (1986). "The Structure of the Nervous System of the Nematode *Caenorhabditis elegans*." *Phil. Trans. R. Soc. Lond. B*, 314, 1-340.](https://doi.org/10.1098/rstb.1986.0056) --- the original connectome paper; study its methods section as a model of thoroughness.
- [Januszewski, M. et al. (2018). "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods*, 15, 605-610.](https://doi.org/10.1038/s41592-018-0049-4) --- modern method reporting with performance metrics.
- [Shapson-Coe, A. et al. (2024). H01 human cortical fragment. *Science.*](https://www.science.org/doi/10.1126/science.adk4858) --- exemplary dataset description and provenance reporting.
- [MICrONS Consortium (2025). Visual cortex reconstruction. *Nature.*](https://www.nature.com/articles/s41586-025-08790-w) --- large-scale connectomics paper with detailed methods.

### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [FlyWire](https://flywire.ai/)
- [Workflow overview]({{ '/datasets/workflow' | relative_url }})

### Competency checks
- Can you point each conclusion to a specific figure/metric pair?
- Can you rewrite one overclaim into a defensible interpretation with calibrated language?
- Can you answer a reviewer concern with concrete revision language and a manuscript reference?
- Does your methods section pass the reproducibility checklist with no critical gaps?
- Are all dataset versions, code commits, and parameters explicitly documented?

## Quick practice prompt
Write one results paragraph from a connectomics figure and include:
1. one quantitative claim with effect size and confidence interval,
2. one explicit caveat tied to a known data limitation,
3. one sentence on reproducibility assumptions (dataset version, materialization, code),
4. one figure legend sentence that specifies sample size and uncertainty indicator.
