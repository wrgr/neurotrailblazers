# Module 03 Activity Worksheet

**Module:** Module 03: Python and Jupyter for Neuroscience  
**Duration:** 4 hours  
*Generated from the module page. Edit `modules/module03.md`, not this file.*

---

## Capability target

Create a reproducible Jupyter notebook that ingests a connectomics dataset slice, performs one analysis, and exports documented outputs. Demonstrate familiarity with the core Python libraries used in connectomics research: CAVEclient, CloudVolume, NetworkX, pandas, and matplotlib.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Modules 01-02

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. How do we structure notebooks for reuse?
   - Your answer:
2. What metadata should accompany outputs?
   - Your answer:

---

## The task

**Scenario:** {: #studio-activity}

1. Create a new notebook with a header cell: title, your name, date, dataset name, materialization version.
2. Create a setup cell with all imports and version pinning.
3. Initialize CAVEclient (or load a provided sample CSV if CAVE access is unavailable).
4. Query or load a synapse table. Validate: print column names, data types, row count, and first 5 rows.
5. Add a markdown cell explaining what the dataset contains and what version you are using.
6. Choose one descriptive analysis from the following options:
7. Write the analysis code with markdown cells explaining each step.
8. Compute at least one summary statistic (mean, median, max, or standard deviation) and report it in a markdown cell.
9. Create at least one publication-quality figure with labeled axes, title, and legend.
10. Add a markdown caption below the figure explaining what it shows and what conclusions (if any) can be drawn.
11. Export your data table as CSV and your figure as PNG.
12. Create a metadata JSON cell recording dataset version, query parameters, and analysis date.
13. Restart kernel and run all cells.
14. Verify all outputs regenerate correctly.
15. If any cell fails, fix it and re-run.

### What you hand in

- A notebook that runs clean from a restarted kernel, with a header cell recording title, author, date, dataset, and materialization version
- One descriptive analysis with at least one summary statistic reported in a markdown cell
- One labeled figure exported as PNG, with a caption stating what it shows and what it does not license you to conclude
- The underlying data table exported as CSV, plus a metadata JSON recording dataset version, query parameters, and analysis date
- If any cell fails, fix it and re-run

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Set environment and dependencies (`requirements.txt` with pinned versions).
- [ ] Initialize clients (CAVEclient, CloudVolume) and record dataset/materialization version.
- [ ] Load dataset and validate schema (check column names, data types, row counts).
- [ ] Run analysis cell sequence (filter, aggregate, compute metrics).
- [ ] Visualize results (at least one plot with labeled axes, title, and caption).
- [ ] Save outputs + metadata (CSV/Parquet for data, PNG/SVG for figures, JSON for parameters).
- [ ] Re-run from clean kernel to verify reproducibility.

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

- [ ] I did not assume: You need to be an expert programmer to do connectomics.
- [ ] I did not assume: If the code runs on my machine, it is reproducible.
- [ ] I did not assume: Version control is only for software engineers.
- [ ] I did not assume: Code comments are sufficient documentation.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| | Header: title, author, date, dataset version, materialization version. |
| | Setup: imports and environment configuration. |
| | Data loading: queries and schema validation. |
| | Analysis: computation cells with markdown explanations. |
| | Export: saving outputs with metadata. |
| | Initialize CAVEclient and set materialization version (3 min). |
| | Query synapse table filtered by brain region (5 min). |
| | Group by pre/post cell type and count synapses (5 min). |
| | Build a NetworkX graph from the grouped data (5 min). |
| | Plot a bar chart of top 10 connections by synapse count (4 min). |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum:** runnable notebook from clean kernel, clear outputs, basic metadata, at least one plot with labels.
- **Strong:** clean linear structure, robust error handling, repeatable rerun, markdown narrative explaining every step, exported metadata JSON, version-pinned requirements file.
- **Failure:** hidden state dependencies, undocumented assumptions, plots without labels, no dataset version recorded.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Add one markdown cell documenting input version, processing steps, and output files. Then write a code cell that queries a synapse table and computes the mean number of synapses per neuron for one brain region.

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

*Module page: `/modules/module03/` · Slides: `/modules/slides/module03/` · [Facilitator guide](/teaching/facilitator-guide/)*
