---
marp: true
theme: neurotrailblazers
paginate: true
footer: "Module 03 · NeuroTrailblazers"
title: "Module 03: Python and Jupyter for Neuroscience"
---

<!-- _class: title nanoscale -->
<img class="cover-image" src="../../../../assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg" alt="H01 electron microscopy with object segmentation and original 2 µm scale bar">
<span class="eyebrow">NeuroTrailblazers · Module 03</span>

# Python and Jupyter for Neuroscience
Teaching Deck

<p class="cover-label">Human cortex · H01<br>Object segmentation over electron microscopy</p>
<p class="source">H01 release · Lichtman Lab / Harvard &amp; Connectomics at Google · CC BY 4.0<br>Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858</p>

---

## Learning Objectives
- Set up a reproducible notebook workflow
- Load and inspect connectomics data tables
- Write basic analysis and visualization code blocks
- Document assumptions and outputs for reuse


---

## Capability Target
Create a reproducible Jupyter notebook that ingests a connectomics dataset slice, performs one analysis, and exports documented outputs. Demonstrate familiarity with the core Python libraries used in connectomics research: CAVEclient, CloudVolume, NetworkX, pandas, and matplotlib.


---

## Concept Focus
### 1) Python as the lingua franca of connectomics
- **Technical:** the connectomics ecosystem is built on Python.
- **Plain language:** if connectomics has a common language, it is Python.

<!--
Further teaching detail from the module:
**Technical:** the connectomics ecosystem is built on Python. CAVEclient queries the CAVE database for synapses, segments, and annotations. CloudVolume accesses volumetric data (EM images, segmentation volumes). NetworkX and igraph construct and analyze circuit graphs. NumPy and pandas handle numerical and tabular data. Matplotlib and Plotly produce publication-quality visualizations. Familiarity with these libraries is not optional --- it is the baseline for participation.
-->

---

## Concept Focus (continued)
- **Misconception:** you need to be an expert programmer to do connectomics.
- **In practice:** Most analyses use a small set of patterns (query, filter, aggregate, plot) applied to different datasets.


---

## Core Workflow
- Set environment and dependencies (`requirements.txt` with pinned versions).
- Initialize clients (CAVEclient, CloudVolume) and record dataset/materialization version.
- Load dataset and validate schema (check column names, data types, row counts).
- Run analysis cell sequence (filter, aggregate, compute metrics).


---

## Core Workflow (continued)
- Visualize results (at least one plot with labeled axes, title, and caption).
- Save outputs + metadata (CSV/Parquet for data, PNG/SVG for figures, JSON for parameters).
- Re-run from clean kernel to verify reproducibility.


---

## Run of Show (90 min)
- Block 1: Notebook anatomy (00:00-12:00)
- Block 2: Environment setup and library tour (12:00-28:00)
- Block 3: Guided analysis sprint (28:00-50:00)
- Block 4: Visualization and export (50:00-65:00)
<!--
Block 1: Notebook anatomy (00:00-12:00)
  Instructor script: "Open the sample notebook I have shared. Before we write any code, let's understand the structure." Walk through the five sections of a well-organized notebook:
  Header: title, author, date, dataset version, materialization version.
  Setup: imports and environment configuration.
  Data loading: queries and schema validation.
  Analysis: computation cells with markdown explanations.
  Export: saving outputs with metadata.
  Show a bad notebook (out-of-order cells, no markdown, hidden state) and a good notebook side by side. Ask: "Which one would you trust for a paper?"

Block 2: Environment setup and library tour (12:00-28:00)
  Instructor script: "Let's set up our environment. Everyone run the first cell." Walk through installing and importing the core libraries:
  `pip install caveclient cloud-volume networkx pandas matplotlib`
  Demonstrate `pip freeze > requirements.txt` for version pinning.
  Live demo of each library (2-3 minutes each):
  CAVEclient: initialize client, query a synapse table, show resulting DataFrame.
  CloudVolume: open a volume, download a small image cutout, display it.
  NetworkX: build a tiny graph from 10 synapses, visualize it.
  pandas: filter the synapse DataFrame by brain region, compute mean synapse count per cell type.
  matplotlib: plot a histogram of synapse counts.

Block 3: Guided analysis sprint (28:00-50:00)
  Instructor script: "Now you build. Your task: query synapses for a specific brain region, count connections between cell types, and plot the result. I will walk you through step by step, but you write the code."
  Step-by-step guided coding:
  Initialize CAVEclient and set materialization version (3 min).
  Query synapse table filtered by brain region (5 min).
  Group by pre/post cell type and count synapses (5 min).
  Build a NetworkX graph from the grouped data (5 min).
  Plot a bar chart of top 10 connections by synapse count (4 min).
  Instructor circulates and helps with errors. Common issues: authentication tokens, version mismatches, column name typos.

Block 4: Visualization and export (50:00-65:00)
  Instructor script: "A plot without labels is not a figure --- it is a sketch. Let's make yours publication-ready."
  Learners add: axis labels, title, legend, caption in a markdown cell below the figure.
  Export figure as PNG and SVG. Export data table as CSV with a header comment recording the query parameters and materialization version.
  Demonstrate saving a metadata JSON file: `{"dataset": "...", "materialization_version": ..., "query_date": "...", "parameters": {...}}`.

Block 5: Clean rerun test (65:00-80:00)
  Instructor script: "The moment of truth. Restart your kernel and run all cells. If anything breaks, that is a reproducibility bug --- fix it now."
  Learners restart kernel and run all cells. Instructor helps debug common issues:
  Cells that depend on variables defined out of order.
  Cells that depend on interactive state (e.g., widget selections).
  Missing imports that were run in a previous session.
  Discuss: "Why does this matter? Because six months from now, you will need to regenerate this figure for a revision, and you will not remember what you did."

Block 6: Competency check and exit ticket (80:00-90:00)
  Learners submit their completed notebook.
  Instructor script: "Your notebook should pass three tests: (1) it runs from clean kernel without errors, (2) every output has a markdown explanation, (3) someone who has never seen your code can understand what it does and reproduce it."
  Exit ticket: (1) link to submitted notebook; (2) one sentence describing the most useful library you learned today and why.
-->

---

## Run of Show (90 min) (continued)
- Block 5: Clean rerun test (65:00-80:00)
- Block 6: Competency check and exit ticket (80:00-90:00)


---

## Misconceptions to Watch
- **Misconception:** you need to be an expert programmer to do connectomics.
- **Misconception:** if the code runs on my machine, it is reproducible.
- **Misconception:** version control is only for software engineers.
- **Misconception:** code comments are sufficient documentation.


---

<!-- _class: visual-lesson -->
## A notebook is a repeatable chain
<p class="visual-lead">Treat the saved result as the output of a declared process.</p>
<ol class="visual-steps"><li><span class="step-number" aria-hidden="true">1</span><h3>Inputs</h3><p>Table + version + units</p></li><li><span class="step-number" aria-hidden="true">2</span><h3>Method</h3><p>Run code in a stated order</p></li><li><span class="step-number" aria-hidden="true">3</span><h3>Outputs</h3><p>Labeled result + parameters</p></li><li><span class="step-number" aria-hidden="true">4</span><h3>Clean rerun</h3><p>Restart; run all; compare</p></li></ol>
<p class="visual-question"><strong>Discuss:</strong> Which link in this chain is missing from your notebook?</p>
<p class="source">Illustrative teaching scenario; see this module’s lesson and worked example.</p>
<!--
Visual description and discussion guidance:
The sequence represents dependencies, not a guarantee of reproducibility. A clean rerun checks hidden interactive state. A picture alone does not record the inputs or code that produced it.
-->


---

<!-- _class: visual-lesson -->
## A tiny result you can verify by hand
<p class="visual-lead">Synthetic counts, not a biological finding. No account or download needed.</p>
<div class="visual-code"><div><h3>Input and code</h3><pre><code>counts = {&quot;A&quot;: 4, &quot;B&quot;: 1, &quot;C&quot;: 0}
total = sum(counts.values())
print(total)
print(total / len(counts))
</code></pre></div><div><h3>Interpret the output</h3><pre class="output">Total: 5
Mean across A, B, C: 1.666…
</pre></div></div>
<p class="visual-question"><strong>Discuss:</strong> What changes if the zero-count row is omitted?</p>
<p class="source">Synthetic example; arithmetic checked by scripts/check_visual_design.rb.</p>
<!--
Visual description and discussion guidance:
All three rows give total 5 and mean 5/3. Omitting the zero-count row keeps the total but changes the mean to 5/2 = 2.5. Declare the population represented by the denominator. These are synthetic teaching values.
-->


---

## Studio Activity
**Scenario:** Learners produce a complete, reproducible Jupyter notebook that queries a connectomics dataset, performs a descriptive analysis, and exports documented results. The work runs in four parts: setup and data loading (20 minutes), analysis (20 minutes), visualization and export (15 minutes), and a reproducibility check (5 minutes).


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
- Session kit: /teaching/sessions/module03/
- Worksheet: /assets/worksheets/module03/module03-activity.md


---

<!-- _class: closing -->
## Read, review, or teach
[Read these slides as a page](module03.reader.html)

[Open the complete lesson](https://www.neurotrailblazers.org/modules/module03/)

The reading version includes figure descriptions and discussion guidance.

<p class="source">NeuroTrailblazers text: CC BY 4.0. Scientific figures retain their individual credits.</p>

