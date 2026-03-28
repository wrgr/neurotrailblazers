---
title: "Module 16: Scientific Visualization for Connectomics"
layout: module
permalink: /modules/module16/
description: "Create clear, truthful visualizations of connectomics structures, uncertainty, and analysis results for technical communication."
module_number: 16
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Select visualization forms aligned to analytical intent"
  - "Encode uncertainty and quality signals explicitly"
  - "Avoid misleading visual encodings in dense connectomics data"
  - "Produce publication-ready and presentation-ready figures"
prerequisites: "Modules 12-15"
merit_stage: "Dissemination"
compass_skills:
  - "Visualization Design"
  - "Scientific Communication"
  - "Interpretation Integrity"
ccr_focus:
  - "Skills - Visualization"
  - "Character - Transparency"

# Normalized metadata
slug: "module16"
short_title: "Scientific Visualization for Connectomics"
status: "active"
audience:
  - "students"
pipeline_stage: "Dissemination"
merit_row_focus: "Dissemination"
topics:
  - "visualization"
  - "uncertainty"
  - "communication"
summary: "Design truthful, high-clarity visualizations for structural and graph-level connectomics results."
key_questions:
  - "Which chart/visual form best matches each scientific claim?"
  - "How should uncertainty and data quality be shown visually?"
  - "What design choices commonly mislead interpretation?"
slides:
  - "/assets/slides/module16/module16-scientific-visualization-for-connectomics.pdf"
notebook:
  - "/assets/notebooks/module16/module16-scientific-visualization-for-connectomics.ipynb"
datasets:
  - "/datasets/workflow"
  - "/datasets/mouseconnects"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic plotting library familiarity"
  - "Understanding of analysis outputs"
next_modules:
  - "module17"
references:
  - "Visualization best-practice resources and connectomics exemplars."
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Produce a figure set that communicates connectomics findings accurately, including uncertainty and data-quality context, for both expert and mixed audiences. Students will leave this module able to choose the right visualization form for a given scientific claim, build publication-quality figures using standard tools, and defend every design choice in terms of clarity and honesty.

## Why this module matters
Poor visual design can create false confidence and hide limitations. In connectomics, visualizations are often used as primary evidence: a node-link diagram of a circuit motif, a heatmap of synaptic connectivity, or a 3D rendering of a reconstructed neuron may be the single most important piece of evidence for a paper's central claim. If that figure misleads --- through cluttered layout, inappropriate color scales, gratuitous 3D, or invisible uncertainty --- the science itself is compromised. Visualization is communication, not decoration.

## Concept set

### 1) Visualization as communication, not decoration
- **Technical:** every visual encoding (position, color, size, shape, opacity) carries information. Encodings that do not map to data dimensions are noise. The goal of a scientific figure is to make the reader's correct interpretation as effortless as possible.
- **Plain language:** a figure should help people understand your result, not impress them with complexity.
- **Misconception guardrail:** making a figure "look good" is not the same as making it truthful. A beautiful 3D rendering with no scale bar and no uncertainty indicators is worse than an ugly but complete 2D plot.

### 2) Choosing the right plot type for connectomics data
- **Technical:** connectomics generates diverse data types, each with preferred visual forms:
  - **Node-link diagrams** show circuit topology and are best for small networks (under ~100 nodes) where individual connections matter. Force-directed layouts can mislead if spatial position is not meaningful.
  - **Adjacency matrices** are better for dense networks and make reciprocal connections, blocks, and community structure visible. Row/column ordering matters enormously --- random ordering hides structure.
  - **Heatmaps** display quantitative connectivity (synapse counts, connection probabilities) across cell-type pairs. Color scale choice is critical; sequential scales for counts, diverging scales for deviations from expected.
  - **3D renderings** of reconstructed morphologies communicate spatial context but are hard to read quantitatively. Use them for orientation and context, not for making numerical arguments.
  - **Sholl plots** quantify dendritic/axonal arborization by counting intersections at increasing radii from the soma, revealing branching complexity in a single 2D chart.
  - **Histograms and violin plots** for distributions of synapse counts, segment sizes, and other scalar metrics.
- **Plain language:** match your chart type to the question you are answering. "What is the circuit topology?" calls for a node-link diagram. "How strong are connections between cell types?" calls for a heatmap.
- **Misconception guardrail:** there is no single "best" visualization. The best choice depends on the claim.

### 3) Common visualization mistakes in connectomics
- **Technical:**
  - **Cluttered graphs:** plotting a full connectome as a node-link diagram produces an unreadable hairball. Aggregate, filter, or use matrix representations instead.
  - **Misleading color scales:** rainbow/jet colormaps distort perceived magnitude because they are not perceptually uniform. Use viridis, inferno, or other perceptually uniform scales.
  - **3D when 2D suffices:** rotating 3D scatter plots look impressive but make quantitative comparison nearly impossible. Use 3D only when the third spatial dimension is genuinely necessary.
  - **Missing scale bars and axis labels:** a reconstruction rendering without a scale bar is uninterpretable. An adjacency matrix without labeled rows/columns is useless.
  - **Overplotting:** when thousands of synapses overlap, individual points disappear. Use density plots, transparency, or binning.
- **Plain language:** the most common mistakes are showing too much at once, using colors that lie about magnitude, and using 3D for flash rather than function.
- **Misconception guardrail:** complexity in a figure does not equal rigor. Simplicity with completeness is the standard.

### 4) Uncertainty must be visible
- **Technical:** confidence intervals, confidence classes, and missingness indicators should be explicit in every figure that supports a quantitative claim. Strategies include error bars, shaded confidence bands, hatching for uncertain regions, and explicit "data not available" markers for boundary neurons or unproofread segments.
- **Plain language:** show what is uncertain, not only what is central. If a synapse count could be off by 20%, the reader needs to know.
- **Misconception guardrail:** cleaner-looking plots are not always better. A plot that hides uncertainty is less honest than one that shows it.

### 5) Accessibility and colorblind-safe design
- **Technical:** approximately 8% of males and 0.5% of females have color vision deficiency. Figures that rely on red-green discrimination exclude these readers. Use colorblind-safe palettes (e.g., Okabe-Ito, ColorBrewer qualitative palettes) and redundant encoding (color + shape, color + pattern). Ensure sufficient contrast for printing in grayscale. Keep annotation density manageable --- overcrowded labels defeat the purpose.
- **Plain language:** if people cannot read it, they cannot evaluate it. Design for the widest possible audience.
- **Misconception guardrail:** aesthetics cannot replace methodological clarity. A beautiful figure that only some people can read is not a good figure.

## Tools for connectomics visualization

### Neuroglancer
Browser-based volumetric visualization for EM data, segmentation overlays, and mesh browsing. Ideal for exploring reconstructed volumes interactively, generating shareable view states, and verifying proofreading. Used extensively in MICrONS, FlyWire, and H01 projects.

### Matplotlib and Plotly
The workhorses of 2D figure generation in Python. Matplotlib excels at publication-quality static figures with fine-grained control. Plotly provides interactive figures useful for exploration and web-based sharing. Both support adjacency matrices, histograms, violin plots, Sholl plots, and scatter plots.

### Blender and ParaView
For high-quality 3D renderings of neuronal morphologies and circuit reconstructions. Blender produces photorealistic images suitable for journal covers and presentations. ParaView handles large-scale scientific datasets with built-in volume rendering. Both have steep learning curves but produce results unmatched by simpler tools.

### napari
Python-based multi-dimensional image viewer for volume data. Supports overlaying segmentation masks on EM imagery, annotating structures, and integrating with analysis pipelines through its plugin ecosystem. Lighter-weight than Neuroglancer for local exploration.

## Core workflow
1. **Map each claim to required visual evidence.** For every result sentence, identify what figure panel and what visual encoding will support it.
2. **Select the appropriate plot type.** Use the decision framework: topology questions get node-link diagrams or matrices; quantity questions get heatmaps or bar charts; spatial questions get renderings; distribution questions get histograms or violins.
3. **Draft candidate visuals with uncertainty layers.** Include error bars, confidence bands, or explicit missing-data indicators from the start --- do not plan to "add them later."
4. **Run critique for misinterpretation risk.** Show the draft to someone unfamiliar with the analysis and ask them what they conclude. If their conclusion differs from your intent, revise.
5. **Check accessibility.** Run the figure through a colorblind simulator (e.g., Coblis or the Matplotlib colorblind check). Verify grayscale legibility.
6. **Revise for clarity, accessibility, and reproducibility.** Add scale bars, axis labels, panel letters, and complete captions.
7. **Export figure package with caption metadata.** Include figure files at publication resolution (300+ DPI for raster, vector preferred), caption text, and a note on the dataset version and code used to generate each panel.

## 60-minute tutorial run-of-show

### Materials needed
- Projected examples: 3 good and 3 bad connectomics figures (prepared in advance from published papers or synthetic examples).
- Shared dataset: a small adjacency matrix (20x30 cell types) and one reconstructed neuron mesh.
- Software: Matplotlib/Plotly notebooks pre-loaded; Neuroglancer link ready.
- Colorblind simulation tool (browser-based).
- Printed or digital critique rubric (one per student).

### Timing and instructor script

**00:00-10:00 | Visual integrity gallery walk**
Instructor displays six figures (three strong, three weak) without labels. Students vote on which are "trustworthy" and which are "suspicious." Instructor reveals issues: missing scale bars, rainbow colormaps, cluttered node-link diagrams, hidden uncertainty, gratuitous 3D. Key script line: "Your first instinct about a figure's trustworthiness is often right. Let us learn why."

**10:00-20:00 | Claim-to-visual mapping exercise**
Instructor presents three scientific claims from a mock connectomics study:
1. "Excitatory neurons in layer 4 receive more synaptic input than those in layer 2/3."
2. "Reciprocal connections are enriched between Martinotti cells."
3. "Axonal arbors of chandelier cells are spatially restricted to a 100-micron radius."
Students work in pairs to select the best plot type for each claim and justify their choice. Instructor circulates, challenging choices: "Why not a node-link diagram for claim 1? What would you lose with a heatmap for claim 3?"

**20:00-35:00 | Figure draft build**
Students open the provided notebook and generate: (a) an adjacency heatmap for the cell-type connectivity matrix, (b) a Sholl plot for the reconstructed neuron. Instructor models adding axis labels, a perceptually uniform colormap, and a scale bar. Students replicate and customize.

**35:00-47:00 | Uncertainty and quality overlays**
Instructor demonstrates adding confidence intervals to the Sholl plot and a "data quality" overlay to the heatmap (hatching for cell-type pairs with fewer than 5 observed connections). Students add these to their own figures. Key script line: "If you cannot see the uncertainty, you cannot evaluate the claim."

**47:00-55:00 | Peer critique and revision**
Students swap figures with a neighbor and complete the critique rubric: Does the figure support the stated claim? Is uncertainty visible? Could it be misinterpreted? Is it colorblind-safe? Students revise based on feedback.

**55:00-60:00 | Competency check and wrap-up**
Each student submits one revised figure with a two-sentence caption. Instructor reviews one or two examples live, highlighting what works and what still needs improvement.

### Success criteria for this session
- Every student figure includes at least one uncertainty indicator.
- Captions specify dataset version and analysis parameters.
- No figure uses a rainbow/jet colormap.

## Studio activity: connectomics figure package

**Scenario:** You are preparing a three-figure package for a short connectomics paper reporting cell-type-specific connectivity patterns in a cortical volume. Your dataset includes a 50x50 cell-type adjacency matrix, morphological reconstructions for three example neurons, and synapse count distributions across layers.

**Figure 1 task:** Create an adjacency heatmap of the cell-type connectivity matrix. Choose an appropriate colormap, add a colorbar with units, order rows and columns by hierarchical clustering, and annotate the diagonal. Include hatching or transparency for cell-type pairs with fewer than 10 observed connections.

**Figure 2 task:** Generate Sholl plots for the three example neurons (one excitatory, one inhibitory basket cell, one inhibitory chandelier cell). Use distinct colorblind-safe colors with a legend. Add shaded confidence bands reflecting reconstruction uncertainty. Include a scale bar and soma marker.

**Figure 3 task:** Produce a synapse count distribution comparison across cortical layers using violin plots. Add individual data points as jittered dots. Include a statistical annotation (e.g., effect size with confidence interval, not just a p-value star).

**Outputs**
- Three-figure set exported at publication resolution with complete captions.
- Uncertainty annotation strategy document (one paragraph per figure explaining what uncertainty is shown and why).
- Revision log from peer critique (at least two specific changes made in response to feedback).
- Accessibility check report (colorblind simulation screenshot for each figure).

## Assessment rubric
- **Minimum pass:** visuals map clearly to claims, include uncertainty context, use perceptually uniform colormaps, and have complete axis labels and scale bars.
- **Strong performance:** high clarity across expert and non-expert audiences, minimal misinterpretation risk, colorblind-safe design, explicit documentation of dataset version and code used for each panel, and thoughtful caption language that narrows interpretation bounds.
- **Failure modes:** overloaded figures with too many overlapping elements, missing scale context, hidden uncertainty, rainbow colormaps, gratuitous 3D renderings, captions that do not mention data quality or limitations.

## Content library cross-references
- [Data formats]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) --- understanding the source formats (Zarr volumes, CSV synapse tables, SWC morphologies) that feed visualization workflows.
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}) --- adjacency matrices, edge lists, and graph objects that underlie node-link diagrams and heatmaps.

## Teaching resources
- [Technical Unit 09: Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- [Module 17: Scientific Writing for Connectomics]({{ '/modules/module17/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})
- [Workflow overview]({{ '/datasets/workflow' | relative_url }})

## Evidence anchors from connectomics practice

### Key papers
- [Tufte, E. (1983). *The Visual Display of Quantitative Information.*](https://www.edwardtufte.com/tufte/books_vdqi) --- foundational principles of data visualization integrity.
- [Borland, D. and Taylor, R.M. (2007). "Rainbow Color Map (Still) Considered Harmful."](https://doi.org/10.1109/MCG.2007.323435) --- why perceptually uniform colormaps matter.
- [Weissgerber, T.L. et al. (2015). "Beyond Bar and Line Graphs."](https://doi.org/10.1371/journal.pbio.1002128) --- showing distributions, not just summaries.
- [MICrONS Consortium (2025). Visual cortex reconstruction. *Nature.*](https://www.nature.com/articles/s41586-025-08790-w) --- exemplary connectomics figure design.
- [Shapson-Coe, A. et al. (2024). H01 human cortical fragment. *Science.*](https://www.science.org/doi/10.1126/science.adk4858) --- large-scale visualization of human connectomics data.

### Key tools and resources
- [Neuroglancer](https://github.com/google/neuroglancer) --- browser-based volumetric viewer.
- [napari](https://napari.org/) --- Python multi-dimensional image viewer.
- [ColorBrewer](https://colorbrewer2.org/) --- colorblind-safe palette selection.
- [Coblis Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/) --- test figure accessibility.

### Competency checks
- Can you justify why you chose each plot type for each claim?
- Can you identify the uncertainty indicator in each figure and explain what it represents?
- Can you pass each figure through a colorblind simulator without information loss?
- Can you regenerate each figure from the documented code and dataset version?

## Quick practice prompt
Take one existing connectomics figure (from a paper, a classmate, or your own work) and perform a full audit:
1. Identify the claim the figure is supposed to support.
2. Add one uncertainty cue (error bar, confidence band, or missing-data indicator).
3. Replace the colormap with a perceptually uniform alternative if needed.
4. Write a two-sentence caption that narrows interpretation bounds and specifies the dataset version.
5. Run the figure through a colorblind simulator and note any issues.
