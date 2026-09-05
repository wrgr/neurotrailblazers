# Module 11 Activity Worksheet

**Module:** Module 11: Synapses and Circuit Logic  
**Duration:** 4 hours  
*Generated from the module page. Edit `modules/module11.md`, not this file.*

---

## Capability target

Generate one synapse-to-motif interpretation with explicit evidence chain and one alternative explanation.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Modules 01-10

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. Which synaptic patterns support specific circuit hypotheses?
   - Your answer:
2. How do annotation errors alter motif conclusions?
   - Your answer:

---

## The task

**Scenario:** You are analyzing a 200-neuron subgraph from the MICrONS dataset, spanning L2/3 and L4 of mouse visual cortex. Your goal: characterize the local circuit motif profile and identify any enriched patterns that suggest specific wiring rules.

1. Enumerate all 2-node and 3-node motifs in the subgraph (use DotMotif or equivalent tool).
2. Generate 1,000 degree-preserving random rewirings. Count motifs in each.
3. Compute z-scores for each motif type.
4. Identify the top 3 most enriched motifs. For each: draw the circuit diagram, propose a functional interpretation, and state one alternative explanation.
5. Write a 1-page "circuit logic brief" summarizing the motif profile of this circuit.

### What you hand in

- Motif count table (observed vs expected vs z-score for each motif type)
- Circuit diagrams for top 3 enriched motifs
- 1-page circuit logic brief with interpretations and caveats

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Identify synapse candidates: find synapses in the region of interest with correct pre/post assignment.
- [ ] Build local connectivity motif: extract the subgraph connecting the pre and post neurons and their immediate neighbors.
- [ ] Classify the motif: reciprocal pair, feed-forward loop, feedback inhibition, convergent input, etc.
- [ ] Evaluate against null: is this motif more common than expected?
- [ ] State supported claim (what the data shows) + caveat (what it doesn't prove and what could confound it).

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

- [ ] I did not assume: Asymmetric morphology means a synapse is excitatory, rather than putatively excitatory under a stated assumption.
- [ ] I did not assume: Reconstruction errors add symmetric noise to motif counts, when merges bias them toward denser motifs.
- [ ] I did not assume: A motif observed more often than expected is a functional building block.
- [ ] I did not assume: Synapse count is a direct measure of connection strength rather than a proxy for it.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-10:00 | Synapse cue recap |
| 10:00-24:00 | Motif construction examples |
| 24:00-38:00 | Learner motif analysis |
| 38:00-50:00 | Alternative explanation challenge |
| 50:00-60:00 | Competency check |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**
  - The motif count table reports observed, expected, and z-score for every motif class examined, not only the enriched ones.
  - At least one motif carries a complete evidence chain: detection method, count, null comparison, and interpretation, in that order.
  - Each claim in the circuit logic brief is paired with an explicit caveat stating what it does not prove.
  - The synapse threshold and data version used to build the subgraph are stated in the brief.
- **Strong performance**
  - Every enriched motif has at least one non-functional alternative explanation (spatial proximity, cell-type composition, reconstruction error) named and, where possible, tested.
  - A second null model or a stratified analysis is applied to at least one motif, with the change in effect size reported.
  - Synapse-level evidence — compartment targeting, Gray type — is used to subdivide or qualify at least one motif class rather than treating graph edges as interchangeable.
  - Sensitivity to reconstruction quality is quantified: the headline count is re-run at a second synapse threshold or across proofreading versions, and the difference is reported.
- **Common failure to flag**
  - Motif claim without error-awareness — treating every enriched pattern as a functional circuit without considering artifacts or spatial confounds.
  - Functional language ("this circuit gates," "this loop amplifies") presented as a finding rather than as a consistency statement.
  - Enrichment reported against a single weak null with no statement of what it fails to control.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Write one motif claim and one plausible confound.

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

*Module page: `/modules/module11/` · Slides: `/modules/slides/module11/` · [Facilitator guide](/teaching/facilitator-guide/)*
