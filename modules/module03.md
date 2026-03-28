---
title: "Module 03: Python and Jupyter for Neuroscience"
layout: module
permalink: /modules/module03/
description: "Build practical Python/Jupyter skills for reproducible connectomics data exploration."
module_number: 3
difficulty: "Beginner to Intermediate"
duration: "4 hours"
learning_objectives:
  - "Set up a reproducible notebook workflow"
  - "Load and inspect connectomics data tables"
  - "Write basic analysis and visualization code blocks"
  - "Document assumptions and outputs for reuse"
prerequisites: "Modules 01-02"
merit_stage: "Foundations"
compass_skills:
  - "Programming"
  - "Data Handling"
  - "Reproducible Practice"
ccr_focus:
  - "Skills - Computational Foundations"
  - "Meta-Learning - Debugging"

# Normalized metadata
slug: "module03"
short_title: "Python and Jupyter for Neuroscience"
status: "active"
audience:
  - "students"
pipeline_stage: "Foundations"
merit_row_focus: "Foundations"
topics:
  - "python"
  - "jupyter"
  - "reproducibility"
summary: "Develop notebook-based analysis habits for connectomics datasets with explicit reproducibility discipline."
key_questions:
  - "How do we structure notebooks for reuse?"
  - "What metadata should accompany outputs?"
slides: []
notebook: []
datasets:
  - "/datasets/access"
  - "/datasets/workflow"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/ask-an-expert/"
related_frameworks:
  - "education-models"
prerequisites_list: []
next_modules:
  - "module04"
references: []
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Create a reproducible Jupyter notebook that ingests a connectomics dataset slice, performs one analysis, and exports documented outputs. Demonstrate familiarity with the core Python libraries used in connectomics research: CAVEclient, CloudVolume, NetworkX, pandas, and matplotlib.

## Why this module matters
Python is the lingua franca of connectomics. Every major connectomics platform --- CAVE, FlyWire, MICrONS, NeuPrint --- provides Python client libraries. Jupyter notebooks have become the standard medium for sharing reproducible analyses: they combine executable code, inline visualizations, and narrative explanations in a single document. Mastering the notebook workflow early means that every subsequent module builds on a solid technical foundation rather than fighting tooling issues.

## Concept set

### 1) Python as the lingua franca of connectomics
- **Technical:** the connectomics ecosystem is built on Python. CAVEclient queries the CAVE database for synapses, segments, and annotations. CloudVolume accesses volumetric data (EM images, segmentation volumes). NetworkX and igraph construct and analyze circuit graphs. NumPy and pandas handle numerical and tabular data. Matplotlib and Plotly produce publication-quality visualizations. Familiarity with these libraries is not optional --- it is the baseline for participation.
- **Plain language:** if connectomics has a common language, it is Python.
- **Misconception:** you need to be an expert programmer to do connectomics. In practice, most analyses use a small set of patterns (query, filter, aggregate, plot) applied to different datasets.

### 2) Jupyter notebooks for reproducible analysis
- **Technical:** a Jupyter notebook is an executable lab notebook that combines code cells, markdown narrative, and inline outputs. Reproducibility requires that notebooks run cleanly from top to bottom (no hidden state), document all dependencies (pinned package versions), and record the dataset version used. A notebook that cannot be re-run from a clean kernel is not reproducible --- it is a screenshot.
- **Plain language:** your notebook should work for someone who has never seen it before.
- **Misconception:** if the code runs on my machine, it is reproducible. Without version pinning, environment specification, and dataset versioning, results may differ across machines and time.

### 3) Key libraries overview
- **CAVEclient:** the primary interface to the CAVE (Connectome Annotation Versioning Engine) database. Use it to query synapse tables, retrieve segment IDs, fetch cell type annotations, and access materialization versions. Example: `client.materialize.query_table('synapses_nt_v1')` returns a DataFrame of synapses with pre/post segment IDs, coordinates, and neurotransmitter predictions.
- **CloudVolume:** access volumetric data stored in cloud-optimized formats (Precomputed, Neuroglancer). Use it to download image cutouts, retrieve mesh data for 3D rendering, and access segmentation volumes. Example: `vol = CloudVolume('precomputed://gs://bucket/dataset')` opens a volume for random-access reads.
- **NetworkX / igraph:** construct directed graphs from synapse tables. Nodes represent neurons; edges represent synaptic connections weighted by synapse count. Use for computing degree distributions, shortest paths, motif detection, and community structure. NetworkX is easier to learn; igraph is faster for large graphs.
- **Matplotlib / Plotly:** visualization libraries. Matplotlib produces static publication figures. Plotly produces interactive plots suitable for exploration. Both integrate directly with Jupyter notebooks.
- **pandas:** tabular data manipulation. Most connectomics queries return DataFrames. pandas provides filtering, grouping, merging, and aggregation operations essential for every analysis pipeline.

### 4) Best practices for connectomics code
- **Technical:** pin package versions in a `requirements.txt` or `environment.yml` file. Document every analysis step in markdown cells. Use git for version control of notebooks (consider pairing with `nbstripout` to avoid committing large outputs). Record the CAVE materialization version and dataset version in the notebook header. Structure notebooks linearly: setup, data loading, analysis, visualization, export.
- **Plain language:** future you (and your collaborators) will thank present you for being organized.
- **Misconception:** version control is only for software engineers. In research, version control is how you prove that your analysis produced the results you claim.

### 5) The notebook as a communication tool
- **Technical:** notebooks serve multiple audiences. For yourself: they are a record of what you tried and what worked. For collaborators: they are a reproducible protocol. For reviewers: they are evidence that your analysis is sound. Write markdown cells as if explaining to a knowledgeable colleague who has not seen your specific analysis before.
- **Plain language:** a good notebook tells a story that anyone in the field can follow.
- **Misconception:** code comments are sufficient documentation. Markdown cells provide the narrative context --- the *why* --- that code comments alone cannot convey.

## Core concepts
- Notebook as executable lab notebook.
- Deterministic environments and version pinning.
- Readable code and explicit assumptions.
- Library ecosystem: CAVEclient, CloudVolume, NetworkX, pandas, matplotlib.
- Dataset versioning via CAVE materialization versions.

## Core workflow
1. Set environment and dependencies (`requirements.txt` with pinned versions).
2. Initialize clients (CAVEclient, CloudVolume) and record dataset/materialization version.
3. Load dataset and validate schema (check column names, data types, row counts).
4. Run analysis cell sequence (filter, aggregate, compute metrics).
5. Visualize results (at least one plot with labeled axes, title, and caption).
6. Save outputs + metadata (CSV/Parquet for data, PNG/SVG for figures, JSON for parameters).
7. Re-run from clean kernel to verify reproducibility.

## Detailed run-of-show (90 minutes)

### Block 1: Notebook anatomy (00:00-12:00)
- **Instructor script:** "Open the sample notebook I have shared. Before we write any code, let's understand the structure." Walk through the five sections of a well-organized notebook:
  1. **Header:** title, author, date, dataset version, materialization version.
  2. **Setup:** imports and environment configuration.
  3. **Data loading:** queries and schema validation.
  4. **Analysis:** computation cells with markdown explanations.
  5. **Export:** saving outputs with metadata.
- Show a bad notebook (out-of-order cells, no markdown, hidden state) and a good notebook side by side. Ask: "Which one would you trust for a paper?"

### Block 2: Environment setup and library tour (12:00-28:00)
- **Instructor script:** "Let's set up our environment. Everyone run the first cell." Walk through installing and importing the core libraries:
  - `pip install caveclient cloud-volume networkx pandas matplotlib`
  - Demonstrate `pip freeze > requirements.txt` for version pinning.
- Live demo of each library (2-3 minutes each):
  - **CAVEclient:** initialize client, query a synapse table, show resulting DataFrame.
  - **CloudVolume:** open a volume, download a small image cutout, display it.
  - **NetworkX:** build a tiny graph from 10 synapses, visualize it.
  - **pandas:** filter the synapse DataFrame by brain region, compute mean synapse count per cell type.
  - **matplotlib:** plot a histogram of synapse counts.

### Block 3: Guided analysis sprint (28:00-50:00)
- **Instructor script:** "Now you build. Your task: query synapses for a specific brain region, count connections between cell types, and plot the result. I will walk you through step by step, but you write the code."
- Step-by-step guided coding:
  1. Initialize CAVEclient and set materialization version (3 min).
  2. Query synapse table filtered by brain region (5 min).
  3. Group by pre/post cell type and count synapses (5 min).
  4. Build a NetworkX graph from the grouped data (5 min).
  5. Plot a bar chart of top 10 connections by synapse count (4 min).
- Instructor circulates and helps with errors. Common issues: authentication tokens, version mismatches, column name typos.

### Block 4: Visualization and export (50:00-65:00)
- **Instructor script:** "A plot without labels is not a figure --- it is a sketch. Let's make yours publication-ready."
- Learners add: axis labels, title, legend, caption in a markdown cell below the figure.
- Export figure as PNG and SVG. Export data table as CSV with a header comment recording the query parameters and materialization version.
- Demonstrate saving a metadata JSON file: `{"dataset": "...", "materialization_version": ..., "query_date": "...", "parameters": {...}}`.

### Block 5: Clean rerun test (65:00-80:00)
- **Instructor script:** "The moment of truth. Restart your kernel and run all cells. If anything breaks, that is a reproducibility bug --- fix it now."
- Learners restart kernel and run all cells. Instructor helps debug common issues:
  - Cells that depend on variables defined out of order.
  - Cells that depend on interactive state (e.g., widget selections).
  - Missing imports that were run in a previous session.
- Discuss: "Why does this matter? Because six months from now, you will need to regenerate this figure for a revision, and you will not remember what you did."

### Block 6: Competency check and exit ticket (80:00-90:00)
- Learners submit their completed notebook.
- **Instructor script:** "Your notebook should pass three tests: (1) it runs from clean kernel without errors, (2) every output has a markdown explanation, (3) someone who has never seen your code can understand what it does and reproduce it."
- Exit ticket: (1) link to submitted notebook; (2) one sentence describing the most useful library you learned today and why.

## Studio activity: "Build a connectomics analysis notebook"

### Overview
Learners produce a complete, reproducible Jupyter notebook that queries a connectomics dataset, performs a descriptive analysis, and exports documented results.

### Part A: Setup and data loading (20 minutes)
1. Create a new notebook with a header cell: title, your name, date, dataset name, materialization version.
2. Create a setup cell with all imports and version pinning.
3. Initialize CAVEclient (or load a provided sample CSV if CAVE access is unavailable).
4. Query or load a synapse table. Validate: print column names, data types, row count, and first 5 rows.
5. Add a markdown cell explaining what the dataset contains and what version you are using.

### Part B: Analysis (20 minutes)
1. Choose one descriptive analysis from the following options:
   - **Synapse count distribution:** histogram of synapse counts per neuron.
   - **Top connections:** bar chart of the 10 most connected cell-type pairs.
   - **Degree distribution:** in-degree vs. out-degree scatter plot for all neurons in a region.
   - **Spatial distribution:** scatter plot of synapse locations colored by cell type.
2. Write the analysis code with markdown cells explaining each step.
3. Compute at least one summary statistic (mean, median, max, or standard deviation) and report it in a markdown cell.

### Part C: Visualization and export (15 minutes)
1. Create at least one publication-quality figure with labeled axes, title, and legend.
2. Add a markdown caption below the figure explaining what it shows and what conclusions (if any) can be drawn.
3. Export your data table as CSV and your figure as PNG.
4. Create a metadata JSON cell recording dataset version, query parameters, and analysis date.

### Part D: Reproducibility check (5 minutes)
1. Restart kernel and run all cells.
2. Verify all outputs regenerate correctly.
3. If any cell fails, fix it and re-run.

## Assessment rubric
- **Minimum:** runnable notebook from clean kernel, clear outputs, basic metadata, at least one plot with labels.
- **Strong:** clean linear structure, robust error handling, repeatable rerun, markdown narrative explaining every step, exported metadata JSON, version-pinned requirements file.
- **Failure:** hidden state dependencies, undocumented assumptions, plots without labels, no dataset version recorded.

## Content library references
- [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }})
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }})

## Teaching resources
- [Dataset Access]({{ '/datasets/access/' | relative_url }})
- [Workflow]({{ '/datasets/workflow' | relative_url }})

## Academic references
- Kluyver, T., et al. (2016). Jupyter Notebooks: a publishing format for reproducible computational workflows. *Proceedings of the 20th International Conference on Electronic Publishing*, 87-90.
- Dorkenwald, S., et al. (2023). CAVE: Connectome Annotation Versioning Engine. *bioRxiv*. https://doi.org/10.1101/2023.07.26.550598
- Silversmith, W., et al. (2021). cloud-volume: Serverless client for arbitrary volumetric data. *Zenodo*. https://doi.org/10.5281/zenodo.3956205
- Hagberg, A. A., Schult, D. A., & Swart, P. J. (2008). Exploring network structure, dynamics, and function using NetworkX. *Proceedings of the 7th Python in Science Conference*, 11-15.
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. *Nature*, 634, 124-138.
- Rule, A., et al. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks. *PLOS Computational Biology*, 15(7), e1007007.

## Quick practice prompt
Add one markdown cell documenting input version, processing steps, and output files. Then write a code cell that queries a synapse table and computes the mean number of synapses per neuron for one brain region.
