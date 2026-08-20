# Module 10 Activity Worksheet

**Module:** Module 10: Network Science and Graph Representation  
**Duration:** 4 hours  
*Generated from the module page. Edit `modules/module10.md`, not this file.*

---

## Capability target

Build one connectome graph representation and justify two metric choices for a defined hypothesis.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] The module prerequisites listed on the module page

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. What information is lost or preserved by this graph abstraction?
   - Your answer:
2. Which metrics answer the biological question at hand?
   - Your answer:

---

## The task

**Scenario:** You have the connectivity graph of 500 neurons in a cortical column from the MICrONS dataset. Your PI asks: "Is this circuit small-world? Are there hub neurons? Are there communities?"

1. Load the graph and compute basic statistics (nodes, edges, density, components).
2. Compute: degree distribution, clustering coefficient, average path length.
3. Compare to degree-preserving random graph and Watts-Strogatz small-world reference.
4. Identify candidate hub neurons (top 5% by degree or betweenness centrality).
5. Run community detection (Louvain or Leiden). Do detected communities align with cell types?
6. Write a 1-page graph analysis report with figures, metrics, null comparisons, and biological interpretation.

### What you hand in

- Artifact produced during the activity
- One stated limitation or uncertainty
- One revision made in response to feedback

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Define node/edge schema: what are your nodes, what are your edges, what weighting scheme?
- [ ] Construct graph from synapse table (e.g., using CAVEclient + NetworkX). Inspect: number of nodes, edges, density, connected components.
- [ ] Compute candidate metrics: degree distribution, clustering, path length, reciprocity, modularity.
- [ ] Compare each metric to null-model expectation (degree-preserving random graph as minimum).
- [ ] Interpret metrics against hypothesis. Report which metrics are significant and which are not.
- [ ] Document abstraction limits: what information was lost in the graph construction?

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

- [ ] I have stated one thing I am still unsure about.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-08:00 | Graph abstraction choices |
| 08:00-20:00 | Graph build demo |
| 20:00-34:00 | Metric computation |
| 34:00-46:00 | Interpretation and null concerns |
| 46:00-60:00 | Competency check |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**: Coherent graph model and metric rationale. Null comparison included.
- **Strong performance**: Clear link between each metric and a biological question. Multiple null models tested. Community structure validated against external data.
- **Common failure to flag**: Metric dumping without hypothesis alignment — computing every metric available without explaining what question each answers.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

State one reason a graph metric might be misleading in your current dataset.

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

*Module page: `/modules/module10/` · Slides: `/modules/slides/module10/` · [Facilitator guide](/teaching/facilitator-guide/)*
