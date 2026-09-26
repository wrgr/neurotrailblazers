---
marp: true
theme: neurotrailblazers
paginate: true
footer: "Module 17 · NeuroTrailblazers"
title: "Module 17: Scientific Writing for Connectomics"
---

<!-- _class: title nanoscale -->
<img class="cover-image" src="../../../../assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg" alt="H01 electron microscopy with object segmentation and original 2 µm scale bar">
<span class="eyebrow">NeuroTrailblazers · Module 17</span>

# Scientific Writing for Connectomics
Teaching Deck

<p class="cover-label">Human cortex · H01<br>Object segmentation over electron microscopy</p>
<p class="source">H01 release · Lichtman Lab / Harvard &amp; Connectomics at Google · CC BY 4.0<br>Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858</p>

---

## Learning Objectives
- Convert connectomics analyses into coherent claim-evidence writing
- Write figure legends that are reproducible and interpretation-safe
- Draft abstracts that distinguish result, uncertainty, and limitation
- Respond to reviewer critiques with technically grounded revisions

---

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Capability Target
Produce a manuscript-ready results section (figures, legends, and claims) where each conclusion is traceable to explicit connectomics evidence and stated limitations. Students will also be able to write methods sections with the level of detail required for connectomics reproducibility and respond to peer review with technically precise, non-defensive language.

---

## Concept Focus
### 1) Structure of a connectomics paper: methods are unusually important
- **Technical:** in most neuroscience papers, the methods section is a reference appendix. In connectomics, it is primary evidence. Readers need to assess: What volume was imaged? At what resolution? What species, age, and preparation? Which segmentation algorithm was used, and what was the merge/split error rate? What proofreading version was the analysis based on? Was CAVE materialization pinned to a specific timestamp? Without these details, no biological claim is evaluable.

---

## Concept Focus (continued)
- **Plain language:** in connectomics, how you got the data is as important as what the data shows. Your methods section is not boilerplate --- it is where skeptical readers will spend the most time.
- **Misconception guardrail:** treating the methods section as a formality to write last. In connectomics, draft the methods first because they constrain what you can legitimately claim.

---

## Core Workflow
- **Evidence inventory**
- List candidate claims and required supporting figures/metrics.
- Build a claim-evidence matrix: claim, figure panel, statistical test, effect size, dataset version, caveat.

---

## Core Workflow (continued)
- **Methods drafting (first, not last)**
- Write the dataset description with full provenance.
- Document every preprocessing step, threshold, and parameter.
- Complete the reproducibility checklist.

---

## Core Workflow (continued)
- **Results drafting**
- Write one paragraph per claim cluster with explicit evidence pointers.
- Use calibrated uncertainty language throughout.
- Separate confirmed findings from exploratory observations.

---

## Core Workflow (continued)
- **Legend hardening**
- Ensure legends include dataset version, method variant, key parameters, sample sizes, and uncertainty indicators.
- Each legend should be interpretable without reading the main text.

---

## Core Workflow (continued)
- **Limitation pass**
- Add interpretation bounds (sampling, segmentation error, model assumptions, volume boundary effects).
- Quantify uncertainty where possible rather than using vague qualifiers.

---

## Core Workflow (continued)
- **Peer-review simulation**
- Exchange sections and produce one methods-focused critique plus one interpretation critique.
- Practice structured reviewer responses.

---

## Run of Show (60 min)
- 00:00-08:00 | Good writing vs bad writing in connectomics
- 08:00-18:00 | Claim-evidence matrix construction
- 18:00-28:00 | Results paragraph drafting
- 28:00-38:00 | Methods and provenance exercise
- 38:00-50:00 | Reviewer response practice
- 50:00-58:00 | Peer exchange and feedback
- 58:00-60:00 | Competency check

<!--
Materials needed
  One mock connectomics figure set (3 panels) with underlying data tables: each learner's Module 16 figure package, or three figures the instructor makes from the [Module 16 kit](/assets/kits/module16/README.md) (synthetic).
  Claim-evidence matrix template (printed or digital): the seven columns in studio task 2.
  Methods reproducibility checklist (one per student): Concept 5 on this page.
  Two mock reviewer comments (one valid methodological concern, one partially mistaken interpretation critique), given in full in the 38:00-50:00 block.
  Timer visible to all students.
  Timing and instructor script

00:00-08:00 | Good writing vs bad writing in connectomics
  Instructor displays two versions of the same results paragraph: one with vague claims and missing provenance ("We found strong connectivity between these cell types"), one with precise language and full evidence pointers ("Layer 4 excitatory neurons formed 3.2x more synapses onto PV+ interneurons than expected by the degree-preserving null model (95% CI: 2.8-3.6x, n=847 connections, MICrONS v795)"; illustrative figures, not measured from a MICrONS release). Students identify what makes the second version stronger. Key script line: "Every sentence in a results section should be falsifiable. If a skeptic cannot check your claim against your data, it is not a scientific sentence."

08:00-18:00 | Claim-evidence matrix construction
  Students receive the mock figure set and build a claim-evidence matrix. Instructor models the first row, then students complete three more rows independently. Instructor circulates, pushing students to be specific: "Which panel? What is the effect size? What is the caveat?"

18:00-28:00 | Results paragraph drafting
  Students draft a 200-word results paragraph from their matrix. Instructor emphasizes: lead with the finding, follow with the evidence pointer, close with the caveat. Students read their paragraphs aloud to a partner, who checks each claim against the matrix.

28:00-38:00 | Methods and provenance exercise
  Instructor presents a deliberately incomplete methods section (missing dataset version, no proofreading state, no code commit hash), for example: "Synapses were obtained from the CAVE synapse table and filtered by cleft score. Motifs were counted in Python and compared with a random null model." Students use the reproducibility checklist to identify gaps and rewrite the section. Key script line: "If I handed you this methods section and asked you to reproduce the analysis, what would you be unable to do?"

38:00-50:00 | Reviewer response practice
  Students receive two mock reviewer comments. Comment 1: "The authors do not report the false merge rate for their segmentation. How can we trust the synapse counts?" (valid). Comment 2: "The sample size of 847 connections is too small for any statistical conclusion" (partially mistaken --- depends on effect size and test). Students draft structured responses: quote, response, manuscript reference. Instructor reviews two examples live.

50:00-58:00 | Peer exchange and feedback
  Students swap their results paragraph and methods section with a neighbor. Each student writes one specific improvement suggestion for each document. Students revise based on feedback.

58:00-60:00 | Competency check
  Students submit their claim-evidence matrix and one revised paragraph. Instructor collects and reviews after session.
  Success criteria for this session
  Every claim in the results paragraph maps to a specific figure panel and metric.
  Methods section passes the reproducibility checklist with no critical gaps.
  Reviewer responses are structured, specific, and non-defensive.
-->

---

## Misconceptions to Watch
- **Misconception guardrail:** treating the methods section as a formality to write last. In connectomics, draft the methods first because they constrain what you can legitimately claim.
- **Misconception guardrail:** writing stronger language does not strengthen weak evidence. Adjectives like "striking," "remarkable," and "clearly" do not substitute for effect sizes and confidence intervals.

---

## Misconceptions to Watch (continued)
- **Misconception guardrail:** uncertainty statements are not weakness; they are reproducibility signals. A paper that acknowledges its limits is more credible than one that ignores them.
- **Misconception guardrail:** assuming readers know which dataset version you used. Even within the same project (e.g., MICrONS), different materialization timestamps produce different connectivity tables.
- **Misconception guardrail:** linking to a GitHub repository is not sufficient if the repository has no tagged release and the methods do not specify which commit was used.

---

## Misconceptions to Watch (continued)
- **Misconception guardrail:** uncertainty statements are not weakness; they are reproducibility signals.
- **Misconception guardrail:** assuming that citing the original EM paper covers all required attributions. Segmentation, proofreading, and annotation are separate contributions that deserve separate citations.
- **Misconception guardrail:** defensive tone weakens technical credibility. Never characterize a reviewer's comment as "wrong" --- instead, provide the evidence that supports your position.

---

## Studio Activity
**Scenario:** You are preparing a short paper section on motif enrichment from a connectome analysis. Your team has identified that reciprocal connections between excitatory and inhibitory neurons in cortical layer 2/3 occur 2.1x more frequently than expected under a degree-preserving null model. The analysis used MICrONS minnie65 data, CAVE materialization v795, with synapse detection via the CAVE synapse table (cleft score threshold > 50). A total of 1,247 reciprocal pairs were observed across 12,891 possible excitatory-inhibitory pairs. These are illustrative figures, not measured from a MICrONS release.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
**Minimum pass**

- Claims map to explicit evidence with figure panel references.
- Legends contain enough detail for independent interpretation.
- Methods include dataset version, pipeline, and key parameters.
- Reviewer responses are specific and technically grounded.

---

## Assessment Rubric
**Strong performance**

- Clearly separates robust findings from tentative interpretations using calibrated language.
- Uses limitation language without weakening valid conclusions.
- Improves reproducibility via concrete method-detail additions.
- Reviewer responses include evidence and specific manuscript revision locations.

---

## Assessment Rubric
**Common failure modes**

- Narrative claims that cannot be traced to figures.
- Missing dataset/method versioning in captions or methods.
- Reviewer replies that are persuasive but non-technical.
- Methods section written as an afterthought with missing parameters.

---

## Exit Ticket
Write one results paragraph from a connectomics figure and include:
1. one quantitative claim with effect size and confidence interval,
2. one explicit caveat tied to a known data limitation,
3. one sentence on reproducibility assumptions (dataset version, materialization, code),
4. one figure legend sentence that specifies sample size and uncertainty indicator.

---

## References (Instructor)
- Gopen and Swan (1990) - The science of scientific writing.
- White et al. (1986) - foundational connectome reporting style.
- Januszewski et al. (2018) - modern method reporting and performance framing.

---

## Teaching Materials
- Module page: /modules/module17/
- Session kit: /teaching/sessions/module17/
- Worksheet: /assets/worksheets/module17/module17-activity.md
