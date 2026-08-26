---
marp: true
theme: default
paginate: true
title: "Module 03: Python and Jupyter for Neuroscience"
---

# Module 03: Python and Jupyter for Neuroscience
Teaching Deck

---

## Learning Objectives
- Set up a reproducible notebook workflow
- Load and inspect connectomics data tables
- Write basic analysis and visualization code blocks
- Document assumptions and outputs for reuse

---

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Agenda (60 min)
- 0-10 min: Frame and model
- 10-35 min: Guided practice
- 35-50 min: Debrief and misconception correction
- 50-60 min: Competency check + exit ticket

---

## Capability Target
Create a reproducible Jupyter notebook that ingests a connectomics dataset slice, performs one analysis, and exports documented outputs. Demonstrate familiarity with the core Python libraries used in connectomics research: CAVEclient, CloudVolume, NetworkX, pandas, and matplotlib.

---

## Concept Focus
### 1) Python as the lingua franca of connectomics
- **Technical:** the connectomics ecosystem is built on Python. CAVEclient queries the CAVE database for synapses, segments, and annotations. CloudVolume accesses volumetric data (EM images, segmentation volumes). NetworkX and igraph construct and analyze circuit graphs. NumPy and pandas handle numerical and tabular data. Matplotlib and Plotly produce publication-quality visualizations. Familiarity with these libraries is not optional --- it is the baseline for participation.
- **Plain language:** if connectomics has a common language, it is Python.
- **Misconception:** you need to be an expert programmer to do connectomics.
- **In practice:** Most analyses use a small set of patterns (query, filter, aggregate, plot) applied to different datasets.

---

## Core Workflow
- Set environment and dependencies (`requirements.txt` with pinned versions).
- Initialize clients (CAVEclient, CloudVolume) and record dataset/materialization version.
- Load dataset and validate schema (check column names, data types, row counts).
- Run analysis cell sequence (filter, aggregate, compute metrics).
- Visualize results (at least one plot with labeled axes, title, and caption).
- Save outputs + metadata (CSV/Parquet for data, PNG/SVG for figures, JSON for parameters).
- Re-run from clean kernel to verify reproducibility.

---

## 60-Minute Run-of-Show
- **Instructor script:** "Open the sample notebook I have shared. Before we write any code, let's understand the structure." Walk through the five sections of a well-organized notebook:
- **Header:** title, author, date, dataset version, materialization version.
- **Setup:** imports and environment configuration.
- **Data loading:** queries and schema validation.
- **Analysis:** computation cells with markdown explanations.
- **Export:** saving outputs with metadata.
- Show a bad notebook (out-of-order cells, no markdown, hidden state) and a good notebook side by side. Ask: "Which one would you trust for a paper?"
- **Instructor script:** "Let's set up our environment. Everyone run the first cell." Walk through installing and importing the core libraries:
- `pip install caveclient cloud-volume networkx pandas matplotlib`
- Demonstrate `pip freeze > requirements.txt` for version pinning.
- Live demo of each library (2-3 minutes each):
- **CAVEclient:** initialize client, query a synapse table, show resulting DataFrame.
- **CloudVolume:** open a volume, download a small image cutout, display it.
- **NetworkX:** build a tiny graph from 10 synapses, visualize it.
- **pandas:** filter the synapse DataFrame by brain region, compute mean synapse count per cell type.
- **matplotlib:** plot a histogram of synapse counts.
- **Instructor script:** "Now you build. Your task: query synapses for a specific brain region, count connections between cell types, and plot the result. I will walk you through step by step, but you write the code."
- Step-by-step guided coding:
- Initialize CAVEclient and set materialization version (3 min).
- Query synapse table filtered by brain region (5 min).
- Group by pre/post cell type and count synapses (5 min).
- Build a NetworkX graph from the grouped data (5 min).
- Plot a bar chart of top 10 connections by synapse count (4 min).
- Instructor circulates and helps with errors. Common issues: authentication tokens, version mismatches, column name typos.
- **Instructor script:** "A plot without labels is not a figure --- it is a sketch. Let's make yours publication-ready."
- Learners add: axis labels, title, legend, caption in a markdown cell below the figure.
- Export figure as PNG and SVG. Export data table as CSV with a header comment recording the query parameters and materialization version.
- Demonstrate saving a metadata JSON file: `{"dataset": "...", "materialization_version": ..., "query_date": "...", "parameters": {...}}`.
- **Instructor script:** "The moment of truth. Restart your kernel and run all cells. If anything breaks, that is a reproducibility bug --- fix it now."
- Learners restart kernel and run all cells. Instructor helps debug common issues:
- Cells that depend on variables defined out of order.
- Cells that depend on interactive state (e.g., widget selections).
- Missing imports that were run in a previous session.
- Discuss: "Why does this matter? Because six months from now, you will need to regenerate this figure for a revision, and you will not remember what you did."
- Learners submit their completed notebook.
- **Instructor script:** "Your notebook should pass three tests: (1) it runs from clean kernel without errors, (2) every output has a markdown explanation, (3) someone who has never seen your code can understand what it does and reproduce it."
- Exit ticket: (1) link to submitted notebook; (2) one sentence describing the most useful library you learned today and why.

---

## Misconceptions to Watch
- **Misconception:** you need to be an expert programmer to do connectomics.
- **Misconception:** if the code runs on my machine, it is reproducible.
- **Misconception:** version control is only for software engineers.
- **Misconception:** code comments are sufficient documentation.

---

## Studio Activity
{: #studio-activity}

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum:** runnable notebook from clean kernel, clear outputs, basic metadata, at least one plot with labels.
- **Strong:** clean linear structure, robust error handling, repeatable rerun, markdown narrative explaining every step, exported metadata JSON, version-pinned requirements file.
- **Failure:** hidden state dependencies, undocumented assumptions, plots without labels, no dataset version recorded.

---

## Exit Ticket
Add one markdown cell documenting input version, processing steps, and output files. Then write a code cell that queries a synapse table and computes the mean number of synapses per neuron for one brain region.

---

## References (Instructor)
- Use module references listed on the module page.

---

## Teaching Materials
- Module page: /modules/module03/
- Slide page: /modules/slides/module03/
- Worksheet: /assets/worksheets/module03/module03-activity.md
