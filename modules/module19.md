---
title: "Module 19: Peer Review and Scientific Ethics"
layout: module
permalink: /modules/module19/
description: "Apply peer-review practice and research-ethics decision making to real connectomics workflows, claims, and collaborations."
module_number: 19
image: /assets/images/modules/module19.svg
image_alt: "Stylized vector art: two manuscripts exchanging annotated review passes."
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Evaluate connectomics manuscripts for methodological and interpretive rigor"
  - "Identify ethics risks in data handling, authorship, and reporting"
  - "Draft constructive, technically specific peer-review feedback"
  - "Make transparent integrity decisions in ambiguous collaboration scenarios"
prerequisites: "Modules 17-18 or equivalent writing/workflow experience"
merit_stage: "Dissemination"
compass_skills:
  - "Ethical Reasoning"
  - "Critical Review"
  - "Research Integrity"
ccr_focus:
  - "Character - Scientific Ethics"
  - "Meta-Learning - Reflective Practice"

# Normalized metadata
slug: "module19"
short_title: "Peer Review and Scientific Ethics"
status: "active"
audience:
  - "students"
pipeline_stage: "Dissemination"
merit_row_focus: "Dissemination"
topics:
  - "peer-review"
  - "research-ethics"
  - "authorship"
  - "reproducibility"
summary: "Run method-focused peer review and resolve ethics decisions in connectomics research with explicit documentation."
key_questions:
  - "What makes a review technically useful instead of opinion-based?"
  - "Where do integrity risks appear in large-scale connectomics projects?"
  - "How should authorship and credit be managed in consortium settings?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow/"
  - "/datasets/mouseconnects/"
personas:
  - "/avatars/gradstudent"
  - "/avatars/mentor"
related_tools:
  - "/tools/ask-an-expert/"
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Ability to interpret methods/results sections"
  - "Basic understanding of reproducibility and QC terms"
next_modules:
  - "module20"
  - "module21"
references:
  - "Bourne PE, Korngreen A (2006) Ten simple rules for reviewers. PLoS Computational Biology 2(9):e110."
  - "Brand A, Allen L, Altman M, Hlava M, Scott J (2015) Beyond authorship: attribution, contribution, collaboration, and credit. Learned Publishing 28(2):151-155."
  - "Simmons JP, Nelson LD, Simonsohn U (2011) False-positive psychology. Psychological Science 22(11):1359-1366."
  - "Dorkenwald S et al. (2024) Neuronal wiring diagram of an adult brain. Nature 634(8032):124-138."
  - "Shapson-Coe A et al. (2024) A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. Science 384(6696):eadk4858."
videos: []
downloads: []
last_reviewed: 2026-09-28
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Produce a technically rigorous manuscript review and an ethics-risk decision memo for a connectomics study, including actionable recommendations and integrity safeguards. Students will be able to distinguish constructive criticism from destructive criticism, identify the specific ethical challenges that arise in large-scale connectomics collaborations, and make documented decisions when facing ambiguous integrity situations.

## Why this module matters
Connectomics projects are collaborative, data-heavy, and method-sensitive. A single MICrONS or FlyWire paper may involve dozens to hundreds of contributors spanning multiple institutions, with data collected from human or animal tissue, processed by automated pipelines, proofread by community volunteers, and analyzed by computational teams. Errors in interpretation, reporting, or credit assignment can undermine both scientific validity and team trust. Here ethics is a set of daily practices: how you log, credit, share, and report.

## Concept set

### 1) What peer reviewers look for in connectomics papers
- **Technical:** effective peer review of connectomics manuscripts requires evaluating several domain-specific dimensions:
  - **Data quality documentation:** does the paper report the segmentation error rate (merge/split metrics), synapse detection precision/recall, and proofreading completeness? Without these, no biological claim is evaluable.
  - **Statistical rigor:** are null models appropriate for the graph structure? Are multiple comparisons handled? Are effect sizes reported alongside p-values? Is there sensitivity analysis for key thresholds?
  - **Interpretation boundaries:** does the paper distinguish confirmed findings from exploratory observations? Are conclusions limited to what the data can actually support (e.g., one brain region in one animal at one developmental time point)?
  - **Data availability:** are the dataset version, CAVE materialization, code repository, and parameters sufficient for reproduction? Can a reader trace every claim to a specific data artifact?
- **Plain language:** a good reviewer checks whether the methods can actually support the claims, whether the statistics are honest, and whether someone else could reproduce the work.
- **Misconception guardrail:** an interesting result can make up for thin methods.
- **Why it fails:** a novel finding with inadequate methods documentation cannot be checked, and is worth less than an incremental finding reported transparently.

### 2) Ethical issues specific to connectomics
- **Technical:** connectomics raises several domain-specific ethical concerns:
  - **Human tissue consent:** datasets like H01 use surgically resected human brain tissue. Consent processes must cover not only the initial use but also open data sharing, potential re-identification risks (from unique anatomical features), and downstream computational analyses not anticipated at the time of consent. The ethical review must address whether broad consent covers AI/ML applications.
  - **Data sharing obligations:** large publicly funded connectomics projects have data sharing mandates. Balancing open science with privacy, intellectual property for junior researchers, and responsible use requires explicit policies.
  - **Attribution for proofreaders:** in community proofreading projects (e.g., FlyWire, Eyewire), many volunteers contribute proofreading labor that is essential for data quality. Fair attribution practices must go beyond a blanket acknowledgment --- contribution tracking systems should inform authorship decisions, and community members should be credited proportionally.
  - **Responsible AI use:** using connectomics data to train AI models (for segmentation, synapse detection, or circuit prediction) raises questions about model bias, appropriate validation, and downstream applications. Models trained on one species or brain region may not generalize, and overclaiming generality is an ethical as well as scientific problem.
  - **Selective reporting:** the complexity of connectomics data creates many opportunities for selective reporting --- highlighting motifs that are enriched while ignoring those that are not, reporting only the threshold at which results are significant, or presenting one analysis variant while hiding others that gave different results.
- **Plain language:** connectomics has unique ethical challenges because it involves human tissue, massive collaborations with community contributors, and data complex enough to support many different stories depending on how you analyze it.
- **Misconception guardrail:** ethics in connectomics is covered once the IRB or animal-care approval is in hand.
- **Why it fails:** approval covers tissue collection. Data sharing, attribution, AI use, and honest reporting run through the whole project.

### 3) Technical peer review is an engineering audit
- **Technical:** reviews should test evidence-method alignment, not just narrative quality. For each major claim, check: (a) Is the evidence shown in a figure panel? (b) Is the statistical test appropriate for the data structure? (c) Are the preprocessing decisions documented and justified? (d) Are alternative interpretations acknowledged? (e) Could the result be an artifact of a known data limitation (segmentation errors, boundary effects, incomplete proofreading)?
- **Plain language:** ask whether the methods can really support the claims. Read the methods section first, not the abstract.
- **Misconception guardrail:** a review is mainly a judgment of how well the story is told.
- **Why it fails:** a well-told story can rest on a method that cannot support it. Audit the method against each claim.

### 4) Constructive criticism vs destructive criticism
- **Technical:** constructive criticism is specific, evidence-based, actionable, and focused on improving the science. It identifies the problem, explains why it matters, and suggests a concrete path to resolution. Destructive criticism is vague, opinion-based, dismissive, or focused on the authors rather than the work. Examples:
  - **Constructive:** "The null model preserves degree sequence but not spatial constraints. Since connection probability between nearby cortical neurons falls with distance, a spatially constrained null would be more appropriate. The authors could test whether their motif enrichment holds under a distance-dependent null model."
  - **Destructive:** "The statistics are unconvincing and the claims are overblown."
  - **Constructive:** "Figure 3 shows a 2x enrichment of reciprocal connections, but the confidence interval overlaps 1.5x. The authors should report the effect size with the CI and discuss whether this enrichment is biologically meaningful at the lower bound."
  - **Destructive:** "The enrichment is probably not real."
- **Plain language:** good criticism tells the authors what is wrong, why it matters, and what they can do about it. Bad criticism just says "this is not good enough."
- **Misconception guardrail:** the harshest review is the most rigorous one.
- **Why it fails:** rigor is specificity. The most rigorous reviews name the problem, the evidence, and the fix.

### 5) Integrity risks are workflow-linked
- **Technical:** risks include silent preprocessing changes (modifying thresholds after seeing results), undocumented QC exceptions (excluding outliers without reporting), selective reporting (showing only the analysis variant that "works"), and ambiguous authorship criteria (adding or removing authors based on politics rather than contribution).
- **Plain language:** ethics problems often start as process shortcuts. The researcher who silently changes a threshold "just to see" and then forgets to report it has created an integrity problem.
- **Misconception guardrail:** a completed compliance checklist guarantees integrity.
- **Why it fails:** most integrity problems start as small workflow shortcuts that no checklist asks about.

### 6) Authorship and credit need explicit rules
- **Technical:** large connectomics projects should use contribution tracking (e.g., CRediT taxonomy) and written authorship criteria established before the project produces results. In consortium settings, define: what level of proofreading contribution qualifies for authorship vs acknowledgment? How are computational contributions weighed against experimental ones? Who decides authorship order? These decisions should be documented in a project governance document, not resolved ad hoc when the paper is nearly submitted.
- **Plain language:** decide credit rules before conflicts happen. Put them in writing. Revisit them when roles change.
- **Misconception guardrail:** contribution volume alone decides authorship.
- **Why it fails:** volume is one input. A person who proofread 10,000 segments may deserve authorship and a person who ran one script may not, or the reverse; the criteria must be written and agreed in advance.

## Worked example: one review comment, written three times

The case is invented for this page and is not the mock preprint in the kit, so working it here spoils nothing. A fictional preprint reports that a three-neuron motif is enriched 2.4-fold over a degree-preserving null (p = 0.003, 16 motif classes tested, one reported). The methods give no merge or split rate for the segmentation. The author list ends with "the Cortical Wiring Consortium" and the contributions section does not say who in it did what.

**Version 1, destructive.** "The statistics are not convincing and the enrichment is probably a segmentation artifact." Two opinions, no mechanism, no location, nothing the authors can act on. An editor cannot weigh it, and the authors will read it as hostility rather than as a finding about their paper.

**Version 2, vague but polite.** "The authors should address possible segmentation errors and consider alternative null models." Better tone, same problem. "Address" and "consider" name no test, so the authors can satisfy the comment with a sentence in the discussion, and the paper does not improve.

**Version 3, constructive.** "Merge errors join separate arbors and create spurious three-node connections, so they inflate exactly the motif the paper reports. Section 2.3 gives no merge or split rate. Please (a) report the measured merge rate on the proofread subset, and (b) either show the enrichment on the proofread subset alone, or perturb the graph at the measured merge and split rates and report the resulting band of enrichment values. If that band includes 1.0, the claim should be stated as exploratory. Separately, the results discuss one of the 16 motif classes tested; please report all 16 with the correction applied, so readers can see the one reported in context."

What makes the third version rigorous is not its length. It names the mechanism, so the authors know why the concern matters. It names the location. It gives two acceptable fixes and a decision rule for what the result means if the fix fails. And it flags selective reporting with a specific, checkable request rather than an accusation.

**The ethics memo, one paragraph.** "The author list includes a consortium without individual contributions. Authorship criteria (ICMJE) apply to people, not organizations, and readers cannot tell who takes responsibility for the segmentation and proofreading this result depends on. Recommendation: list the consortium members who meet the criteria as authors, with CRediT roles, and acknowledge the rest by name. This is a correctable attribution gap, not evidence of misconduct."

**The recommendation, and why it follows.** Major revision. The top-tier concern, an unreported error rate that could produce the headline result, blocks the claim as written but is fixable with data the authors already have. Recommending acceptance with minor revisions would contradict the concern; recommending rejection would ignore that the fix is available. The recommendation has to be the one the concerns imply.

## Core workflow: review and ethics decision process
1. **Pre-review framing**
   - Identify manuscript claim types (descriptive, predictive, explanatory).
   - Note the dataset, methods pipeline, and stated limitations.
2. **Methods-evidence audit**
   - Check dataset versioning, preprocessing transparency, QC thresholds, and statistical controls.
   - Verify that each claim maps to a specific figure panel and statistical test.
3. **Interpretation audit**
   - Flag overclaiming, underreported uncertainty, and missing limitations.
   - Check whether conclusions are bounded by the data (one brain region, one species, one time point).
4. **Ethics-risk scan**
   - Evaluate authorship clarity, disclosure statements, data-governance assumptions, and consent coverage.
   - Check for signs of selective reporting (missing negative results, single-threshold analyses).
5. **Actionable response package**
   - Write revision requests prioritized by scientific impact and integrity risk.
   - Use constructive language: problem, evidence, suggestion.

## Time budget
The declared 4 hours are: about 30 minutes reading the concept set before the meeting, the 90-minute meeting the [syllabus maps]({{ '/teaching/syllabi/' | relative_url }}) give this kit (the 60-minute run-of-show below plus the opening of the studio activity), and about 2 hours outside class finishing the studio memos, the quick practice prompt, and the linked readings.

## 60-minute tutorial run-of-show

### Materials needed
- One mock connectomics preprint (2-3 pages: abstract, key methods paragraph, two result figures with legends, and discussion excerpt): `mock-preprint.md` in the [Module 19 kit]({{ '/assets/kits/module19/README.md' | relative_url }}). Pre-seeded with 4 issues: one methods gap, one overclaim, one ethics concern (ambiguous authorship), and one example of selective reporting.
- Structured review form template (one per student): `review-form.md` in the [Module 19 kit]({{ '/assets/kits/module19/README.md' | relative_url }}).
- Ethics-risk checklist (human tissue, attribution, data sharing, selective reporting), in the same review form.
- Two example reviewer comments, one constructive and one destructive, in the review form. They were written for this session, not taken from a real review.

### Timing and instructor script

**00:00-08:00 | Constructive vs destructive criticism**
Instructor displays the two example reviewer comments from the review form, both written about the mock preprint. One is specific, evidence-based, and actionable; the other is vague and dismissive. Students identify which is which and explain why. Key script line: "The most rigorous reviewer is not the harshest one. Rigor means specificity. Vague criticism is lazy, not tough."

**08:00-12:00 | What reviewers look for in connectomics**
Instructor presents a checklist of connectomics-specific review criteria: data quality metrics, appropriate null models, reproducibility metadata, interpretation boundaries, and data availability. Brief discussion of how these differ from standard neuroscience review criteria.

**12:00-28:00 | Methods-evidence audit exercise**
Students read the mock preprint individually. Using the structured review form, each student identifies: (a) one methods gap with specific missing information, (b) one overclaim where the language exceeds the evidence, (c) one figure panel where uncertainty is insufficiently represented. Instructor circulates, prompting: "Can you point to the exact sentence that overclaims? What would the bounded version say?"

**28:00-38:00 | Ethics-risk scan**
Students use the ethics-risk checklist to scan the mock preprint. They identify: (a) the authorship ambiguity (the mock paper lists "the consortium" as an author without specifying individual contributions), (b) the selective reporting concern (only one of three tested motifs is discussed in results). Students draft a one-paragraph ethics memo for each issue with a concrete mitigation recommendation.

**38:00-50:00 | Decision memo drafting**
In pairs, students draft a complete review decision memo: (a) summary of the paper's contribution, (b) major concerns (methods, interpretation, ethics) with evidence, (c) minor concerns, (d) recommendation (accept with revisions, major revisions, or reject) with explicit rationale. Students must ensure their recommendation is consistent with their documented concerns.

**50:00-58:00 | Peer review of reviews**
Pairs swap decision memos and evaluate: Is the review specific and evidence-based? Is the recommendation consistent with the concerns? Is the tone constructive? Each pair writes one improvement suggestion.

**58:00-60:00 | Competency check**
Each student submits their structured review form and decision memo. Instructor collects for after-session review.

### Success criteria for this session
- Review comments reference specific manuscript locations (figure panels, paragraph numbers, methods details).
- Ethics concerns are tied to concrete workflow practices, not abstract principles.
- Recommendations are consistent with documented findings.
- All feedback uses constructive language (problem, evidence, suggestion).

## Studio activity: connectomics review board simulation
{: #studio-activity}

**Scenario:** Your team is acting as reviewers for a connectomics preprint claiming a novel circuit motif --- a specific three-neuron feed-forward inhibitory loop --- with translational implications for understanding epilepsy. The preprint uses a fictional mouse visual cortex volume (release T19) and reports 3.5x enrichment of this motif relative to a degree-preserving random graph null model (p < 0.001 after Bonferroni correction across 13 three-node motif classes). The methods section does not report the synapse confidence threshold, does not mention boundary neuron handling, and lists a data consortium as a co-author without individual contribution details. The full mock preprint is in the [Module 19 kit]({{ '/assets/kits/module19/README.md' | relative_url }}). The discussion section states that "this motif likely plays a causal role in seizure propagation."

**Tasks**
1. Write one methods critique (specific: what is missing, why it matters, what the authors should add) and one interpretation critique (specific: which sentence overclaims, what the bounded version would say).
2. Identify two ethics risks: (a) the authorship/attribution concern and (b) one additional concern (selective reporting, consent, data sharing, or responsible AI). For each, draft a concrete mitigation recommendation.
3. Draft a decision memo: accept with revisions, major revisions, or reject. Justify your recommendation by referencing your specific concerns.
4. Propose one concrete integrity policy improvement for the project team (e.g., a contribution tracking system, a preregistration requirement, a threshold sensitivity analysis mandate).

**Expected outputs**
- Structured review form (claims, methods audit, evidence gaps, interpretation audit).
- Ethics-risk memo with two identified risks and concrete mitigations.
- Decision memo with recommendation and traceable rationale.
- One-paragraph integrity policy proposal.

## Assessment rubric
- **Minimum pass**
  - Review comments are specific and evidence-linked (referencing figure panels, methods details, or specific sentences).
  - Ethics risks are identified with concrete mitigations tied to workflow practices.
  - Recommendation is consistent with documented findings.
- **Strong performance**
  - Distinguishes fixable technical issues from fundamental validity failures.
  - Balances rigor with constructive tone and practical revision advice.
  - Uses transparent criteria for authorship/integrity judgments.
  - Anticipates author responses and pre-addresses potential objections.
- **Common failure modes**
  - Generic critique with no evidence references ("the statistics are weak").
  - Ethics discussion disconnected from actual workflow practices.
  - Inconsistent recommendation versus identified risks (e.g., listing major concerns but recommending accept with minor revisions).
  - Destructive tone that undermines the credibility of valid criticisms.

## Common errors and how to recover

- **Your review lists everything you noticed, in the order you noticed it.** Recover by sorting into three tiers: blocks the claim, weakens the claim, cosmetic. Lead with the first tier and say which tier each comment is in; an editor reads the first paragraph most carefully.
- **You wrote "the authors should address" without saying how.** Recover by naming the test, the figure or the sentence. If you cannot name one, the comment is an impression, and it belongs in the confidential note to the editor or nowhere.
- **You listed a validity problem and recommended minor revisions.** Recover by rereading your top-tier concern and choosing the recommendation it implies. If the concern is fixable with data the authors have, that is major revision; if it is not fixable, say so.
- **You reviewed the story and skipped the methods.** Recover by reading the methods first on the next pass and building the claim-to-method map before the discussion. Most overclaims are visible only from the methods side.
- **An ethics concern is raised as a principle rather than a practice.** "The authors should consider attribution" changes nothing. Recover by tying the concern to a workflow step and a concrete fix: a contribution statement with roles, a preregistered test, a sensitivity analysis.
- **The authorship dispute surfaced the week of submission.** Recover by applying the written criteria if the project has them. If it does not, draft them now with CRediT roles, apply them to everyone including yourself, and state each person's contribution in the paper; the drafting is late, but the alternative is deciding by seniority.
- **You found a silent threshold change in your own group's workflow.** Recover by logging it, rerunning from the documented threshold, and reporting both results. Earlier is cheaper; the decision log in [Module 18]({{ '/modules/module18/' | relative_url }}) exists so this is caught before submission, not after.

## What this module does not cover

- **Ethics and governance as a field.** Consent for human tissue, data licenses, dual use and credit for proofreading labor have their own page, [ethics and governance]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}); this module teaches the reviewer's and collaborator's daily practice and links there for the substance.
- **Writing your own reviewer response.** The author's side of the exchange is [Module 17]({{ '/modules/module17/' | relative_url }}).
- **Judging the statistics.** Whether a null model or a correction is right is [Module 20]({{ '/modules/module20/' | relative_url }}); a reviewer applies that module, this one says how to write the comment.
- **Reproducibility packaging.** What a release must contain for a reviewer to rerun it is [Module 21]({{ '/modules/module21/' | relative_url }}).
- **Institutional procedure.** IRB and animal-care processes, misconduct investigations, and journal-specific policies are set by institutions and publishers and change; raise them with your institution's office, not this page.
- **Legal protections for people who report problems.** Jurisdiction-specific and outside this curriculum.

## Content library cross-references
- [Ethics and governance]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}) --- consent, licenses, dual use and credit for proofreading labor; this module links here rather than owning the material.
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) --- the versioning infrastructure that reviewers should expect papers to document.
- [H01 human cortex]({{ '/content-library/case-studies/h01-human-cortex/' | relative_url }}) --- a case study raising ethical questions about human tissue consent, open data sharing, and attribution in large collaborations.

## Teaching resources
- Review practice context: [Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Workflow integrity context: [Workflow overview]({{ '/datasets/workflow/' | relative_url }})
- QC context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})
- Mentorship/escalation context: [Ask an Expert]({{ '/ask-an-expert/' | relative_url }})
- [Module 19 kit]({{ '/assets/kits/module19/README.md' | relative_url }}) — the fictional mock preprint and the review form
- Workshops that continue this module: [The Savvy Researcher]({{ '/teaching/pathways/savvy-researcher/' | relative_url }}) (authorship and credit) and [Professional Conduct in STEM]({{ '/teaching/pathways/professional-conduct/' | relative_url }})

## Evidence anchors from connectomics practice

### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [H01 dataset](https://h01-release.storage.googleapis.com/landing.html)
- [FlyWire](https://flywire.ai/)
- [Workflow overview]({{ '/datasets/workflow/' | relative_url }})

### Competency checks
- Can you identify one overclaim in a connectomics abstract and rewrite it with evidence boundaries?
- Can you map one ethics risk to a concrete workflow control (not just a policy statement)?
- Can you justify your editorial recommendation with traceable criteria referenced to specific manuscript locations?
- Can you distinguish constructive from destructive criticism in your own review draft?
- Can you articulate the specific ethical obligations associated with using community-proofread data?

## Academic references
- Bourne PE, Korngreen A (2006) "Ten simple rules for reviewers." *PLoS Computational Biology* 2(9):e110. doi:10.1371/journal.pcbi.0020110. The reviewer's obligations that Concept 4 turns into a comment format.
- Brand A, Allen L, Altman M, Hlava M, Scott J (2015) "Beyond authorship: attribution, contribution, collaboration, and credit." *Learned Publishing* 28(2):151-155. doi:10.1087/20150211. The CRediT contributor-role taxonomy named in Concept 6.
- Simmons JP, Nelson LD, Simonsohn U (2011) "False-positive psychology." *Psychological Science* 22(11):1359-1366. doi:10.1177/0956797611417632. Researcher degrees of freedom: why a threshold changed after seeing the result is an integrity problem, not a preference.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634(8032):124-138. doi:10.1038/s41586-024-07558-y. The FlyWire author list, where community proofreaders appear by name; the attribution model Concept 2 refers to.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384(6696):eadk4858. doi:10.1126/science.adk4858. H01, the human-tissue case the consent discussion in Concept 2 draws on.

Guidelines, not papers: [COPE Core Practices](https://publicationethics.org/core-practices) for editors and reviewers, and the [ICMJE Recommendations](https://www.icmje.org/recommendations/) for authorship criteria.

## Quick practice prompt
Choose a connectomics abstract (from a real paper or the mock preprint) and produce:
1. One high-priority methods concern (what is missing, why it matters, what should be added).
2. One interpretation concern (which sentence overclaims, what the bounded version would say).
3. One ethics/integrity concern (tied to a specific workflow practice, not an abstract principle).
4. One actionable revision request for each of the above, written in constructive language.
