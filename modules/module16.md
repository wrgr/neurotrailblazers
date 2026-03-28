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
Produce a figure set that communicates connectomics findings accurately, including uncertainty and data-quality context, for both expert and mixed audiences.

## Why this module matters
Poor visual design can create false confidence and hide limitations. In connectomics, visualizations are often used as primary evidence --- a node-link diagram or adjacency matrix may be the single artifact a reviewer uses to evaluate a circuit claim. Unlike many fields where figures illustrate text, connectomics figures frequently *are* the argument. This means visualization is not decoration; it is communication infrastructure. Every design choice (color scale, layout algorithm, threshold cutoff) encodes an interpretive decision that readers will absorb, often unconsciously. This module teaches you to make those decisions deliberately and transparently.

## Concept set

### 1) Visualization as communication, not decoration
- **Technical:** every visual encoding carries implicit claims. A force-directed layout implies that spatial proximity reflects connectivity strength; a color gradient implies that the mapped variable is continuous. Designers must ensure that the visual grammar matches the scientific claim.
- **Plain language:** a figure is an argument, not an illustration. If the picture says something your data does not, you have miscommunicated.
- **Misconception guardrail:** "making it look nice" is not the same as making it accurate. A polished but misleading figure is worse than a rough but honest one.

### 2) Choosing the right plot type for connectomics data
Connectomics produces diverse data types, and each calls for different visual forms:

| Data type | Recommended forms | When to avoid |
|---|---|---|
| **Connectivity graphs** | Node-link diagrams (small networks), adjacency matrices (dense networks), chord diagrams (inter-region flow) | Node-link for >200 nodes without aggregation --- becomes unreadable |
| **Synaptic distributions** | Histograms, kernel density plots, violin plots | Pie charts for continuous distributions |
| **Spatial morphology** | 3D mesh renderings (Neuroglancer, Blender), Sholl plots for branching analysis, skeleton overlays | 3D when 2D projections suffice and depth adds no information |
| **Heatmaps** | Cell-type-by-cell-type connectivity matrices, gene expression overlays | Heatmaps without dendrograms when cluster structure matters |
| **Volume data** | Orthogonal slice views, maximum intensity projections, napari interactive exploration | Static screenshots of 3D volumes without orientation markers |

- **Technical:** node-link diagrams excel at showing topology and path structure but collapse visually at high density. Adjacency matrices scale better for dense graphs and make reciprocal connections immediately visible as symmetric entries. Sholl plots quantify branching complexity as a function of distance from the soma. 3D renderings are essential for morphological context but should be accompanied by quantitative summaries.
- **Plain language:** pick the chart that answers your question most directly. If you are showing "who connects to whom," use a matrix. If you are showing "what the neuron looks like," use a 3D rendering with scale bar.
- **Misconception guardrail:** 3D renderings look impressive but often obscure quantitative patterns. Use them for morphological context, not for statistical arguments.

### 3) Common visualization mistakes in connectomics
- **Cluttered graphs:** plotting all 100,000+ edges of a connectome on a single node-link diagram produces a "hairball" that communicates nothing. Always threshold, filter, or aggregate before plotting.
- **Misleading color scales:** rainbow (jet) colormaps distort perception of magnitude --- the yellow band appears brighter than it should, creating false peaks. Use perceptually uniform colormaps (viridis, cividis, inferno).
- **3D when 2D suffices:** rotating 3D scatter plots in presentations prevent the audience from extracting exact values. If the third dimension does not carry biological meaning, project to 2D.
- **Missing scale bars and units:** a synapse density heatmap without a colorbar scale is uninterpretable. Always include axis labels, units, scale bars, and colorbar ranges.
- **Cherry-picked examples:** showing one "beautiful" neuron reconstruction without indicating how representative it is misleads readers about reconstruction quality.

### 4) Uncertainty must be visible
- **Technical:** confidence intervals, confidence classes, and missingness indicators should be explicit in every figure. For connectomics, this includes: reconstruction confidence (automated vs. proofread segments), synapse detection confidence scores, and boundary effects (neurons truncated at volume edges). Use transparency, hatching, or explicit annotations to mark uncertain regions.
- **Plain language:** show what is uncertain, not only what is central. A connectivity matrix should indicate which entries are well-supported and which come from poorly proofread neurons.
- **Misconception guardrail:** cleaner-looking plots are not always better. Removing error bars or confidence indicators to reduce clutter removes scientific content.

### 5) Accessibility: colorblind-safe palettes and universal design
- **Technical:** approximately 8% of males have red-green color vision deficiency. Figures that rely on red-green contrast exclude these readers. Use colorblind-safe palettes (e.g., Okabe-Ito, viridis family, Color Universal Design guidelines). Beyond color: ensure sufficient contrast, use redundant encoding (color + shape + label), provide alt-text for screen readers, and test figures in grayscale.
- **Plain language:** if people cannot read your figure, they cannot evaluate your science. Accessibility is a scientific obligation, not a courtesy.
- **Misconception guardrail:** aesthetics and personal color preferences should never override accessibility requirements.

## Visualization tools for connectomics

### Neuroglancer
Browser-based viewer for volumetric EM data and mesh overlays. Use for: browsing raw imagery, inspecting segmentation quality, creating shareable visualization states via URL. Essential for verifying that downstream analyses correspond to real biological structures.

### Matplotlib and Plotly
Python plotting libraries for publication figures. Matplotlib provides fine-grained control for static figures (adjacency matrices, histograms, Sholl plots). Plotly adds interactivity for exploratory analysis and presentations. Both support colorblind-safe palettes and export to vector formats (SVG, PDF).

### Blender and ParaView
3D rendering tools for publication-quality morphological visualizations. Blender excels at photorealistic neuron renderings with controlled lighting and camera angles. ParaView handles large-scale scientific visualization with built-in volume rendering. Use when morphological context is essential to the scientific argument.

### napari
Python-based multi-dimensional image viewer. Integrates with NumPy arrays and supports layers for segmentation overlays, point annotations, and surface meshes. Ideal for interactive exploration of volume data within a Python analysis pipeline.

## Core workflow
1. **Claim inventory:** list each scientific claim and identify the required visual evidence.
2. **Form selection:** for each claim, choose the plot type that most directly supports interpretation (use the table above as a guide).
3. **Draft with uncertainty:** build candidate visuals that include confidence indicators, quality annotations, and boundary markers.
4. **Accessibility check:** verify colorblind safety, contrast, scale bars, and units. Test in grayscale.
5. **Peer critique:** exchange figures with a colleague and document misinterpretation risks.
6. **Revision and export:** revise based on critique, export figure package with caption metadata, source data references, and code to regenerate each panel.

## 60-minute tutorial run-of-show

### Materials
- Example figure set: one good and one misleading connectomics figure pair.
- Sample adjacency matrix dataset (e.g., MICrONS layer 2/3 excitatory subnetwork).
- Colorblind simulation tool (e.g., Coblis or matplotlib colorblind preview).
- Shared critique rubric template.

### Timing and flow
1. **00:00-08:00 | Visual integrity warm-up**
   - *Instructor script:* "I am going to show you two figures from real connectomics papers. One earned a reviewer compliment; the other triggered a major revision request. Your job: identify what makes the difference." Show side-by-side examples. Discuss: misleading color scale, missing uncertainty, hairball graph vs. aggregated matrix.

2. **08:00-15:00 | Concept lecture: visualization as communication**
   - Walk through the plot-type selection table. Emphasize: "The question determines the figure, not the other way around." Show a Sholl plot example and explain when it communicates more than a 3D rendering.

3. **15:00-22:00 | Claim-to-visual mapping exercise**
   - Students receive three scientific claims (e.g., "Layer 4 neurons receive more inhibitory synapses than layer 2/3 neurons"). For each claim, they propose a figure type and justify their choice. Brief share-out.

4. **22:00-36:00 | Figure building workshop**
   - Using provided data, students build one figure in Matplotlib or Plotly. Requirements: appropriate plot type, colorblind-safe palette, scale bars, uncertainty annotation. Instructor circulates and flags common errors in real time.

5. **36:00-46:00 | Accessibility and critique pass**
   - Students run their figure through a colorblind simulator. Exchange figures with a partner. Each partner writes two critique items: one about potential misinterpretation and one about accessibility.

6. **46:00-54:00 | Revision sprint**
   - Students revise their figure based on critique. Document changes in a revision log.

7. **54:00-60:00 | Competency checkpoint**
   - Each student submits: (a) revised figure with caption, (b) one-sentence statement of what the figure does and does not show, (c) revision log.

### Instructor notes
- Common pitfall: students default to whatever plot they have made before rather than selecting the form that matches the claim. Push back on this explicitly.
- If time is short, the accessibility pass (step 5) can be shortened but should never be skipped entirely.

## Studio activity: connectomics figure package

### Scenario
You are preparing a three-figure package for a short report on cell-type-specific connectivity in a cortical column. Your data includes: (1) a connectivity matrix between five cell types, (2) synapse count distributions for each cell type, and (3) a morphological reconstruction of one example neuron per type.

### Tasks
1. **Figure 1 --- Connectivity matrix:** Design an adjacency heatmap showing connection strengths between cell types. Include: colorblind-safe diverging colormap, row/column labels, synapse count scale bar, and annotations for entries based on fewer than 10 synapses (low-confidence flag).

2. **Figure 2 --- Synapse distributions:** Create violin or box plots comparing synapse counts across cell types. Include: individual data points overlaid, sample sizes per group, and a note about neurons truncated at volume boundaries.

3. **Figure 3 --- Morphological examples:** Render one example neuron per cell type using Neuroglancer screenshots or napari. Include: scale bar (micrometers), orientation axes, and a caption noting that these are representative examples selected by [stated criterion].

4. **Caption writing:** For each figure, write a caption that includes: what is shown, how it was generated (dataset version, filtering criteria), what uncertainty or limitation applies, and what the figure does *not* show.

5. **Peer critique round:** Exchange your figure package with another team. Provide written feedback on: (a) one potential misinterpretation risk, (b) one accessibility issue, (c) one missing piece of context.

### Expected outputs
- Three-figure set with publication-ready captions.
- Uncertainty annotation strategy document (one paragraph per figure).
- Revision log from peer critique with before/after notes.

## Assessment rubric
- **Minimum pass:**
  - Each figure maps clearly to a stated claim.
  - Uncertainty context is present (error bars, confidence flags, or boundary notes).
  - Captions include dataset version and key parameters.
  - Colorblind-safe palette is used throughout.
- **Strong performance:**
  - Figure types are well-matched to claim types (not default choices).
  - Accessibility has been tested and documented.
  - Captions distinguish what is shown from what is inferred.
  - Revision log demonstrates substantive response to critique.
- **Failure modes:**
  - Hairball node-link diagrams with no filtering or aggregation.
  - Rainbow colormaps or red-green-only encoding.
  - Missing scale bars, units, or colorbars.
  - Figures that overstate certainty by omitting reconstruction quality context.
  - Captions that describe the figure but not its limitations.

## Content library cross-references
- [Data formats]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) --- understanding the data structures that underlie visualization choices.
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}) --- how connectivity data is stored and accessed for plotting.

## Teaching resources
- [Technical Unit 09: Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- [Module 17: Scientific Writing]({{ '/modules/module17/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})
- [Neuroglancer documentation](https://github.com/google/neuroglancer)
- [napari documentation](https://napari.org/)

## Evidence anchors from connectomics practice

### Key papers and resources
- [Tufte, E. (1983). *The Visual Display of Quantitative Information*](https://www.edwardtufte.com/tufte/books_vdqi) --- foundational principles of honest data graphics.
- [Crameri, F., Shephard, G. E., & Heron, P. J. (2020). The misuse of colour in science communication. *Nature Communications*, 11, 5444](https://doi.org/10.1038/s41467-020-19160-7) --- evidence for abandoning rainbow colormaps.
- [Dorkenwald, S. et al. (2024). Neuronal wiring diagram of an adult brain. *Nature*, 634, 124-138](https://doi.org/10.1038/s41586-024-07558-y) --- FlyWire whole-brain connectome, exemplar of large-scale visualization.
- [MICrONS Consortium (2025). Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*](https://www.nature.com/articles/s41586-025-08790-w) --- large-scale cortical connectome visualization.
- [Shapson-Coe, A. et al. (2024). A petavoxel fragment of human cerebral cortex. *Science*, 384, eadk4858](https://www.science.org/doi/10.1126/science.adk4858) --- H01 human cortex dataset with Neuroglancer-based exploration.

### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/) --- mouse visual cortex with Neuroglancer integration.
- [FlyWire](https://flywire.ai/) --- whole adult *Drosophila* brain.
- [Workflow overview]({{ '/datasets/workflow' | relative_url }})

### Competency checks
- Can you justify why you chose this specific plot type for this specific claim?
- Can you demonstrate that your figure is interpretable in grayscale and by colorblind readers?
- Can a reader reconstruct the filtering/thresholding decisions from your caption alone?
- Can you point to where uncertainty is encoded in each panel?

## Quick practice prompt
Take one existing connectomics figure and:
1. Replace any rainbow colormap with a perceptually uniform alternative.
2. Add one uncertainty cue (error bars, confidence shading, or a low-confidence annotation).
3. Write one caption sentence that states what the figure does *not* show.
4. Test the revised figure with a colorblind simulator and note any remaining issues.
