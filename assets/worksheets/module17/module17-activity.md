# Module 17 Activity Worksheet

**Module:** Module 17: Scientific Writing for Connectomics  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module17.md`, not this file.*

---

## Capability target

Produce a manuscript-ready results section (figures, legends, and claims) where each conclusion is traceable to explicit connectomics evidence and stated limitations. Students will also be able to write methods sections with the level of detail required for connectomics reproducibility and respond to peer review with technically precise, non-defensive language.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Basic statistical interpretation of connectomics outputs
- [ ] Ability to read method sections in technical papers

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. What is the exact evidence for each claim?
   - Your answer:
2. Where does uncertainty belong in the narrative?
   - Your answer:
3. How should reviewers' methodological concerns be answered?
   - Your answer:

---

## The task

**Scenario:** You are preparing a short paper section on motif enrichment from a connectome analysis. Your team has identified that reciprocal connections between excitatory and inhibitory neurons in cortical layer 2/3 occur 2.1x more frequently than expected under a degree-preserving null model. The analysis used MICrONS minnie65 data, CAVE materialization v795, with synapse detection via the CAVE synapse table (cleft score threshold > 50). A total of 1,247 reciprocal pairs were observed across 12,891 possible excitatory-inhibitory pairs.

1. Draft three result claims from the provided scenario, each with different confidence levels (strong, moderate, exploratory).
2. Build a claim-evidence matrix (claim, figure panel, metric, statistical test, effect size, dataset version, caveat).
3. Write a 300-400 word results subsection with calibrated uncertainty language.
4. Write a methods paragraph with full dataset provenance and reproducibility details.
5. Respond to two mock reviewer comments:

### What you hand in

- Claim-evidence matrix (complete, with no empty cells)
- Results subsection draft (300-400 words, every claim traceable)
- Methods paragraph with full provenance
- Reviewer response draft with revision notes (structured format: quote, response, manuscript location)

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] **Evidence inventory**
- [ ] **Methods drafting (first, not last)**
- [ ] **Results drafting**
- [ ] **Legend hardening**
- [ ] **Limitation pass**
- [ ] **Peer-review simulation**

---

## Evidence and reasoning

Fill one row per claim you make in your artifact. A claim without a limitation is
not finished.

| # | Claim | Evidence (what specifically) | Limitation / what would change my mind |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Confidence.** For your main claim, mark one and say why:

- [ ] **High** — two or more independent lines of evidence agree
- [ ] **Medium** — one strong line, or several that share a weakness
- [ ] **Uncertain** — the deciding evidence is not available to me

Why:

**One alternative I considered and rejected**, and the reason:

---

## Misconception self-check

These are the errors this module is designed to prevent. Confirm you did not make
them, or note where you nearly did:

- [ ] I did not assume: Treating the methods section as a formality to write last. In connectomics, draft the methods first because they constrain what you can legitimately claim.
- [ ] I did not assume: Writing stronger language does not strengthen weak evidence. Adjectives like "striking," "remarkable," and "clearly" do not substitute for effect sizes and confidence intervals.
- [ ] I did not assume: Uncertainty statements are not weakness; they are reproducibility signals. A paper that acknowledges its limits is more credible than one that ignores them.
- [ ] I did not assume: Assuming readers know which dataset version you used. Even within the same project (e.g., MICrONS), different materialization timestamps produce different connectivity tables.
- [ ] I did not assume: Linking to a GitHub repository is not sufficient if the repository has no tagged release and the methods do not specify which commit was used.
- [ ] I did not assume: Uncertainty statements are not weakness; they are reproducibility signals.
- [ ] I did not assume: Assuming that citing the original EM paper covers all required attributions. Segmentation, proofreading, and annotation are separate contributions that deserve separate citations.
- [ ] I did not assume: Defensive tone weakens technical credibility. Never characterize a reviewer's comment as "wrong" --- instead, provide the evidence that supports your position.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-08:00 | Frame the capability target |
| 08:00-20:00 | Model one worked example aloud |
| 20:00-38:00 | Guided learner activity |
| 38:00-50:00 | Debrief and misconception correction |
| 50:00-58:00 | Competency check |
| 58:00-60:00 | Exit prompt |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**
- **Strong performance**
- **Common failure modes**

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Write one results paragraph from a connectomics figure and include:
1. one quantitative claim with effect size and confidence interval,
2. one explicit caveat tied to a known data limitation,
3. one sentence on reproducibility assumptions (dataset version, materialization, code),
4. one figure legend sentence that specifies sample size and uncertainty indicator.

**Your answer:**

---

## Peer review (swap worksheets)

Reviewing someone else's reasoning is the fastest way to see the gaps in your own.
Assess the **evidence quality**, not whether you agree with the conclusion.

- Is every claim paired with specific evidence?
- Is at least one limitation stated, and is it a real one?
- Is the confidence level justified by the number of *independent* evidence lines?
- One thing this person did better than me:
- One question I would ask them:

---

*Module page: `/modules/module17/` · Slides: `/modules/slides/module17/` · [Facilitator guide](/teaching/facilitator-guide/)*
