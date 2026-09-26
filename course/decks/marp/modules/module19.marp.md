---
marp: true
theme: neurotrailblazers
paginate: true
footer: "Module 19 · NeuroTrailblazers"
title: "Module 19: Peer Review and Scientific Ethics"
---

<!-- _class: title nanoscale -->
<img class="cover-image" src="../../../../assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg" alt="H01 electron microscopy with object segmentation and original 2 µm scale bar">
<span class="eyebrow">NeuroTrailblazers · Module 19</span>

# Peer Review and Scientific Ethics
Teaching Deck

<p class="cover-label">Human cortex · H01<br>Object segmentation over electron microscopy</p>
<p class="source">H01 release · Lichtman Lab / Harvard &amp; Connectomics at Google · CC BY 4.0<br>Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858</p>

---

## Learning Objectives
- Evaluate connectomics manuscripts for methodological and interpretive rigor
- Identify ethics risks in data handling, authorship, and reporting
- Draft constructive, technically specific peer-review feedback
- Make transparent integrity decisions in ambiguous collaboration scenarios

---

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Capability Target
Produce a technically rigorous manuscript review and an ethics-risk decision memo for a connectomics study, including actionable recommendations and integrity safeguards. Students will be able to distinguish constructive criticism from destructive criticism, identify the specific ethical challenges that arise in large-scale connectomics collaborations, and make documented decisions when facing ambiguous integrity situations.

---

## Concept Focus
### 1) What peer reviewers look for in connectomics papers
- **Technical:** effective peer review of connectomics manuscripts requires evaluating several domain-specific dimensions:
  - **Data quality documentation:** does the paper report the segmentation error rate (merge/split metrics), synapse detection precision/recall, and proofreading completeness? Without these, no biological claim is evaluable.

---

## Concept Focus (continued)
- **Statistical rigor:** are null models appropriate for the graph structure? Are multiple comparisons handled? Are effect sizes reported alongside p-values? Is there sensitivity analysis for key thresholds?
- **Interpretation boundaries:** does the paper distinguish confirmed findings from exploratory observations? Are conclusions limited to what the data can actually support (e.g., one brain region in one animal at one developmental time point)?

---

## Concept Focus (continued)
- **Data availability:** are the dataset version, CAVE materialization, code repository, and parameters sufficient for reproduction? Can a reader trace every claim to a specific data artifact?
- **Plain language:** a good reviewer checks whether the methods can actually support the claims, whether the statistics are honest, and whether someone else could reproduce the work.
- **Misconception guardrail:** an interesting result can make up for thin methods.

---

## Concept Focus (continued)
- **Why it fails:** a novel finding with inadequate methods documentation cannot be checked, and is worth less than an incremental finding reported transparently.

---

## Core Workflow
- **Pre-review framing**
- Identify manuscript claim types (descriptive, predictive, explanatory).
- Note the dataset, methods pipeline, and stated limitations.
- **Methods-evidence audit**
- Check dataset versioning, preprocessing transparency, QC thresholds, and statistical controls.
- Verify that each claim maps to a specific figure panel and statistical test.

---

## Core Workflow (continued)
- **Interpretation audit**
- Flag overclaiming, underreported uncertainty, and missing limitations.
- Check whether conclusions are bounded by the data (one brain region, one species, one time point).

---

## Core Workflow (continued)
- **Ethics-risk scan**
- Evaluate authorship clarity, disclosure statements, data-governance assumptions, and consent coverage.
- Check for signs of selective reporting (missing negative results, single-threshold analyses).

---

## Core Workflow (continued)
- **Actionable response package**
- Write revision requests prioritized by scientific impact and integrity risk.
- Use constructive language: problem, evidence, suggestion.

---

## Run of Show (60 min)
- 00:00-08:00 | Constructive vs destructive criticism
- 08:00-12:00 | What reviewers look for in connectomics
- 12:00-28:00 | Methods-evidence audit exercise
- 28:00-38:00 | Ethics-risk scan
- 38:00-50:00 | Decision memo drafting
- 50:00-58:00 | Peer review of reviews
- 58:00-60:00 | Competency check

<!--
Materials needed
  One mock connectomics preprint (2-3 pages: abstract, key methods paragraph, two result figures with legends, and discussion excerpt): `mock-preprint.md` in the [Module 19 kit](/assets/kits/module19/README.md). Pre-seeded with 4 issues: one methods gap, one overclaim, one ethics concern (ambiguous authorship), and one example of selective reporting.
  Structured review form template (one per student): `review-form.md` in the [Module 19 kit](/assets/kits/module19/README.md).
  Ethics-risk checklist (human tissue, attribution, data sharing, selective reporting), in the same review form.
  Two example reviewer comments, one constructive and one destructive, in the review form. They were written for this session, not taken from a real review.
  Timing and instructor script

00:00-08:00 | Constructive vs destructive criticism
  Instructor displays the two example reviewer comments from the review form, both written about the mock preprint. One is specific, evidence-based, and actionable; the other is vague and dismissive. Students identify which is which and explain why. Key script line: "The most rigorous reviewer is not the harshest one. Rigor means specificity. Vague criticism is lazy, not tough."

08:00-12:00 | What reviewers look for in connectomics
  Instructor presents a checklist of connectomics-specific review criteria: data quality metrics, appropriate null models, reproducibility metadata, interpretation boundaries, and data availability. Brief discussion of how these differ from standard neuroscience review criteria.

12:00-28:00 | Methods-evidence audit exercise
  Students read the mock preprint individually. Using the structured review form, each student identifies: (a) one methods gap with specific missing information, (b) one overclaim where the language exceeds the evidence, (c) one figure panel where uncertainty is insufficiently represented. Instructor circulates, prompting: "Can you point to the exact sentence that overclaims? What would the bounded version say?"

28:00-38:00 | Ethics-risk scan
  Students use the ethics-risk checklist to scan the mock preprint. They identify: (a) the authorship ambiguity (the mock paper lists "the consortium" as an author without specifying individual contributions), (b) the selective reporting concern (only one of three tested motifs is discussed in results). Students draft a one-paragraph ethics memo for each issue with a concrete mitigation recommendation.

38:00-50:00 | Decision memo drafting
  In pairs, students draft a complete review decision memo: (a) summary of the paper's contribution, (b) major concerns (methods, interpretation, ethics) with evidence, (c) minor concerns, (d) recommendation (accept with revisions, major revisions, or reject) with explicit rationale. Students must ensure their recommendation is consistent with their documented concerns.

50:00-58:00 | Peer review of reviews
  Pairs swap decision memos and evaluate: Is the review specific and evidence-based? Is the recommendation consistent with the concerns? Is the tone constructive? Each pair writes one improvement suggestion.

58:00-60:00 | Competency check
  Each student submits their structured review form and decision memo. Instructor collects for after-session review.
  Success criteria for this session
  Review comments reference specific manuscript locations (figure panels, paragraph numbers, methods details).
  Ethics concerns are tied to concrete workflow practices, not abstract principles.
  Recommendations are consistent with documented findings.
  All feedback uses constructive language (problem, evidence, suggestion).
-->

---

## Misconceptions to Watch
- **Misconception guardrail:** an interesting result can make up for thin methods.
- **Misconception guardrail:** ethics in connectomics is covered once the IRB or animal-care approval is in hand.
- **Misconception guardrail:** a review is mainly a judgment of how well the story is told.
- **Misconception guardrail:** the harshest review is the most rigorous one.
- **Misconception guardrail:** a completed compliance checklist guarantees integrity.
- **Misconception guardrail:** contribution volume alone decides authorship.

---

## Studio Activity
**Scenario:** Your team is acting as reviewers for a connectomics preprint claiming a novel circuit motif --- a specific three-neuron feed-forward inhibitory loop --- with translational implications for understanding epilepsy. The preprint uses a fictional mouse visual cortex volume (release T19) and reports 3.5x enrichment of this motif relative to a degree-preserving random graph null model (p < 0.001 after Bonferroni correction across 13 three-node motif classes). The methods section does not report the synapse confidence threshold, does not mention boundary neuron handling, and lists a data consortium as a co-author without individual contribution details. The full mock preprint is in the [Module 19 kit](/assets/kits/module19/README.md). The discussion section states that "this motif likely plays a causal role in seizure propagation."

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
**Minimum pass**

- Review comments are specific and evidence-linked (referencing figure panels, methods details, or specific sentences).
- Ethics risks are identified with concrete mitigations tied to workflow practices.
- Recommendation is consistent with documented findings.

---

## Assessment Rubric
**Strong performance**

- Distinguishes fixable technical issues from fundamental validity failures.
- Balances rigor with constructive tone and practical revision advice.
- Uses transparent criteria for authorship/integrity judgments.
- Anticipates author responses and pre-addresses potential objections.

---

## Assessment Rubric
**Common failure modes**

- Generic critique with no evidence references ("the statistics are weak").
- Ethics discussion disconnected from actual workflow practices.
- Inconsistent recommendation versus identified risks (e.g., listing major concerns but recommending accept with minor revisions).
- Destructive tone that undermines the credibility of valid criticisms.

---

## Exit Ticket
Choose a connectomics abstract (from a real paper or the mock preprint) and produce:
1. One high-priority methods concern (what is missing, why it matters, what should be added).
2. One interpretation concern (which sentence overclaims, what the bounded version would say).
3. One ethics/integrity concern (tied to a specific workflow practice, not an abstract principle).
4. One actionable revision request for each of the above, written in constructive language.

---

## References (Instructor)
- COPE Core Practices.
- ICMJE authorship recommendations.
- FAIR principles (Wilkinson et al., 2016).

---

## Teaching Materials
- Module page: /modules/module19/
- Session kit: /teaching/sessions/module19/
- Worksheet: /assets/worksheets/module19/module19-activity.md
