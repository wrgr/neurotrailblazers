---
title: "Module 03: Python and Jupyter for Neuroscience"
layout: module
permalink: /modules/module03/
description: "Build practical Python/Jupyter skills for reproducible connectomics data exploration."
module_number: 3
image: /assets/images/modules/module03.svg
image_alt: "Stylized vector art: notebook code cells with prompt chevrons and a result sparkline."
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
  - "/datasets/workflow/"
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
last_reviewed: 2026-09-26
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Create a reproducible Jupyter notebook that ingests a connectomics dataset slice, performs one analysis, and exports documented outputs. Demonstrate familiarity with the core Python libraries used in connectomics research: CAVEclient, CloudVolume, NetworkX, pandas, and matplotlib.

## Why this module matters
Python is the lingua franca of connectomics. CAVE (behind FlyWire and MICrONS) and neuPrint (behind the Janelia hemibrain) both have Python clients, and most published connectome analyses are shared as Python code. Jupyter notebooks are the common format for that sharing: they hold executable code, inline figures, and narrative in one document. Learn the notebook workflow now and later modules spend their time on the science instead of on tooling.

## Concept set

### 1) Python as the lingua franca of connectomics
- **Technical:** the connectomics ecosystem is built on Python. CAVEclient queries the CAVE database for synapses, segments, and annotations. CloudVolume accesses volumetric data (EM images, segmentation volumes). NetworkX and igraph construct and analyze circuit graphs. NumPy and pandas handle numerical and tabular data. Matplotlib and Plotly produce publication-quality visualizations. Every later module assumes you can use them.
- **Plain language:** if connectomics has a common language, it is Python.
- **Misconception:** you need to be an expert programmer to do connectomics.
- **In practice:** Most analyses use a small set of patterns (query, filter, aggregate, plot) applied to different datasets.

### 2) Jupyter notebooks for reproducible analysis
- **Technical:** a Jupyter notebook is an executable lab notebook that combines code cells, markdown narrative, and inline outputs. Reproducibility requires that notebooks run cleanly from top to bottom (no hidden state), document all dependencies (pinned package versions), and record the dataset version used. A notebook that cannot be re-run from a clean kernel records what happened once; it does not reproduce it.
- **Plain language:** your notebook should work for someone who has never seen it before.
- **Misconception:** if the code runs on my machine, it is reproducible.
- **In practice:** Without version pinning, environment specification, and dataset versioning, results may differ across machines and time.

### 3) Key libraries overview
- **CAVEclient:** the primary interface to the CAVE (Connectome Annotation Versioning Engine) database. Use it to query synapse tables, retrieve segment IDs, fetch cell type annotations, and access materialization versions. Example: `client.materialize.get_tables()` lists the tables in a datastack, and `client.materialize.query_table(table_name)` returns one of them as a DataFrame; a synapse table has one row per synapse with pre/post segment IDs and coordinates, plus whatever extra columns its schema defines.
- **CloudVolume:** access volumetric data stored in chunked cloud formats such as Neuroglancer Precomputed. Use it to download image cutouts, retrieve mesh data for 3D rendering, and access segmentation volumes. Example: `vol = CloudVolume('precomputed://gs://bucket/dataset')` opens a volume for random-access reads.
- **NetworkX / igraph:** construct directed graphs from synapse tables. Nodes represent neurons; edges represent synaptic connections weighted by synapse count. Use for computing degree distributions, shortest paths, motif detection, and community structure. NetworkX is easier to learn; igraph is faster for large graphs.
- **Matplotlib / Plotly:** visualization libraries. Matplotlib produces static publication figures. Plotly produces interactive plots suitable for exploration. Both integrate directly with Jupyter notebooks.
- **pandas:** tabular data manipulation. Most connectomics queries return DataFrames. pandas provides filtering, grouping, merging, and aggregation operations that nearly every analysis uses.

### 4) Best practices for connectomics code
- **Technical:** pin package versions in a `requirements.txt` or `environment.yml` file. Document every analysis step in markdown cells. Use git for version control of notebooks (consider pairing with `nbstripout` to avoid committing large outputs). Record the CAVE materialization version and dataset version in the notebook header. Structure notebooks linearly: setup, data loading, analysis, visualization, export.
- **Plain language:** future you (and your collaborators) will thank present you for being organized.
- **Misconception:** version control is only for software engineers.
- **In practice:** In research, version control is how you prove that your analysis produced the results you claim.

### 5) The notebook as a communication tool
- **Technical:** notebooks serve multiple audiences. For yourself: they are a record of what you tried and what worked. For collaborators: they are a reproducible protocol. For reviewers: they are evidence that your analysis is sound. Write markdown cells as if explaining to a knowledgeable colleague who has not seen your specific analysis before.
- **Plain language:** a good notebook tells a story that anyone in the field can follow.
- **Misconception:** code comments are sufficient documentation.
- **In practice:** Markdown cells provide the narrative context --- the *why* --- that code comments alone cannot convey.

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

**Where the 4 hours go.** The 90-minute session is the taught part, and the studio notebook is built inside it. The rest is preparation, installing the five libraries or downloading the [Module 03 kit]({{ '/assets/kits/module03/README.md' | relative_url }}) if you have no CAVE access, and follow-up: the three content-library readings at the end of the page, the quick practice prompt, and a second clean-kernel rerun of your notebook a day later, when you have forgotten what the cells do.

### Block 1: Notebook anatomy (00:00-12:00)
- **Instructor script:** "Open a new notebook with me. Before we write any code, we lay out its structure." Create the five sections of a well-organized notebook as empty markdown headings:
  1. **Header:** title, author, date, dataset version, materialization version.
  2. **Setup:** imports and environment configuration.
  3. **Data loading:** queries and schema validation.
  4. **Analysis:** computation cells with markdown explanations.
  5. **Export:** saving outputs with metadata.
- Then make a bad notebook from a copy of the good one while the class watches: run cells out of order, delete the markdown, and define a variable in a cell you then delete. Put the two side by side and ask: "Which one would you trust for a paper?"

### Block 2: Environment setup and library tour (12:00-28:00)
- **Instructor script:** "Set up your environment first. Everyone run the first cell." Walk through installing and importing the core libraries:
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
- **Instructor script:** "A plot without labels is a sketch. Make yours publication-ready."
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
{: #studio-activity}

**Scenario:** Learners produce a complete, reproducible Jupyter notebook that queries a connectomics dataset, performs a descriptive analysis, and exports documented results. The work runs in four parts: setup and data loading (20 minutes), analysis (20 minutes), visualization and export (15 minutes), and a reproducibility check (5 minutes).

**Task sequence:**
1. **Setup and data loading (Part A, 20 minutes):** create a new notebook with a header cell: title, your name, date, dataset name, materialization version.
2. Create a setup cell with all imports and version pinning.
3. Initialize CAVEclient, or, if CAVE access is unavailable, load the [offline synapse table]({{ '/assets/kits/module03/synapses_sample.csv' | relative_url }}) (synthetic; its [README]({{ '/assets/kits/module03/README.md' | relative_url }}) lists the columns and the version string to record).
4. Query or load a synapse table. Validate: print column names, data types, row count, and first 5 rows.
5. Add a markdown cell explaining what the dataset contains and what version you are using.
6. **Analysis (Part B, 20 minutes):** choose one descriptive analysis from the following options: a synapse count distribution (histogram of synapse counts per neuron); top connections (bar chart of the 10 most connected cell-type pairs); a degree distribution (in-degree vs. out-degree scatter plot for all neurons in a region); or a spatial distribution (scatter plot of synapse locations colored by cell type).
7. Write the analysis code with markdown cells explaining each step.
8. Compute at least one summary statistic (mean, median, max, or standard deviation) and report it in a markdown cell.
9. **Visualization and export (Part C, 15 minutes):** create at least one publication-quality figure with labeled axes, title, and legend.
10. Add a markdown caption below the figure explaining what it shows and what conclusions (if any) can be drawn.
11. Export your data table as CSV and your figure as PNG.
12. Create a metadata JSON cell recording dataset version, query parameters, and analysis date.
13. **Reproducibility check (Part D, 5 minutes):** restart the kernel and run all cells.
14. Verify all outputs regenerate correctly.
15. If any cell fails, fix it and re-run.

**Outputs:**
- A notebook that runs clean from a restarted kernel, with a header cell recording title, author, date, dataset, and materialization version.
- One descriptive analysis with at least one summary statistic reported in a markdown cell.
- One labeled figure exported as PNG, with a caption stating what it shows and what it does not license you to conclude.
- The underlying data table exported as CSV, plus a metadata JSON recording dataset version, query parameters, and analysis date.

## Assessment rubric
- **Minimum:** runnable notebook from clean kernel, clear outputs, basic metadata, at least one plot with labels.
- **Strong:** clean linear structure, error handling that says what failed, repeatable rerun, markdown narrative explaining every step, exported metadata JSON, version-pinned requirements file.
- **Failure:** hidden state dependencies, undocumented assumptions, plots without labels, no dataset version recorded.

## Common errors and how to recover

- **The notebook only runs in the order you wrote it.** Cell 12 works because cell 30 was run yesterday. Recover with Restart Kernel and Run All before every commit; anything that breaks is a hidden-state bug, and the fix is to move the definition above its first use, not to add a note saying "run cell 30 first."
- **You queried the live database with no version.** A query without a materialization version returns whatever the segmentation is today, so the numbers in your notebook cannot be reproduced next month. Recover by setting the version when you create the client, writing it in the header cell, and copying it into the metadata JSON that ships with the outputs.
- **Your access token is in the notebook.** A token pasted into a cell is a credential committed to git. Recover by revoking it, storing the replacement where the client library expects it or in an environment variable, and adding that file to `.gitignore` before the next commit.
- **The schema you assumed is not the schema you got.** Column names and types differ between tables and between dataset versions, and a wrong assumption often fails late: an empty DataFrame after a filter, or a KeyError three cells down. Recover by validating before analyzing (print columns, dtypes, row count and the first five rows, as in studio step 4) and by asserting the columns you rely on.
- **Your figure exists but the code that made it does not.** The plot came from an interactive session, and the notebook holds a different version of the query. Recover by regenerating the figure from the notebook's own cells and exporting figure, data table and metadata JSON in the same run, so a reader can trace the picture to the query.
- **Git holds a notebook full of cell outputs.** Every rerun produces a diff nobody can read, and the repository grows with each figure. Recover by pairing git with `nbstripout`, exporting data as CSV or Parquet outside the notebook, and keeping the notebook as code and narrative only.

## What this module does not cover

- **Python itself.** Syntax, functions, and the basics of pandas are assumed. The concept set names the libraries, and the session teaches the query, filter, aggregate, plot pattern, not the language.
- **Data at scale.** Chunked volumetric formats, storage cost, and what happens when the table does not fit in memory are [Module 12]({{ '/modules/module12/' | relative_url }}) and [Technical Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}).
- **How CAVE versions data.** The materialization model, what a version freezes, and how long versions last are [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}); here you only record the version.
- **Statistics and null models.** What to compute once the data is loaded is [Module 08]({{ '/modules/module08/' | relative_url }}) and [Module 20]({{ '/modules/module20/' | relative_url }}); this module's analysis is descriptive by design.
- **Cleaning a messy table.** Integrity checks, duplicates, and missing values are [Module 18]({{ '/modules/module18/' | relative_url }}).
- **Figure design and reproducible packaging.** Choosing a plot type and encoding uncertainty is [Module 16]({{ '/modules/module16/' | relative_url }}); environments, releases, and FAIR principles are [Module 21]({{ '/modules/module21/' | relative_url }}).
- **A worked analysis on real data.** The [MICrONS Real-Data Lab]({{ '/notebooks/microns-lab/' | relative_url }}) is the next step: a version-pinned notebook against MICrONS that needs no account and archives its outputs so you can check a rerun.

## Content library references
- [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }})
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }})

## Teaching resources
- [Dataset Access]({{ '/datasets/access/' | relative_url }})
- [Workflow]({{ '/datasets/workflow/' | relative_url }})
- [Module 03 kit]({{ '/assets/kits/module03/README.md' | relative_url }}) — a synthetic synapse table for learners without CAVE access

## Academic references
- Kluyver, T., et al. (2016). Jupyter Notebooks: a publishing format for reproducible computational workflows. *Proceedings of the 20th International Conference on Electronic Publishing*, 87-90.
- Dorkenwald, S., et al. (2025). CAVE: Connectome Annotation Versioning Engine. *Nature Methods*, 22, 1112-1120. https://doi.org/10.1038/s41592-024-02426-z
- Silversmith, W., et al. (2021). seung-lab/cloud-volume: Zenodo Release v1. *Zenodo*. https://doi.org/10.5281/zenodo.5671443
- Hagberg, A. A., Schult, D. A., & Swart, P. J. (2008). Exploring network structure, dynamics, and function using NetworkX. *Proceedings of the 7th Python in Science Conference*, 11-15.
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. *Nature*, 634, 124-138.
- Rule, A., et al. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks. *PLOS Computational Biology*, 15(7), e1007007.

## Quick practice prompt
Add one markdown cell documenting input version, processing steps, and output files. Then write a code cell that queries a synapse table and computes the mean number of synapses per neuron for one brain region.
