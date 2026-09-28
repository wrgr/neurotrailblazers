---
title: "Module 16: Scientific Visualization for Connectomics"
layout: module
permalink: /modules/module16/
description: "Create clear, truthful visualizations of connectomics structures, uncertainty, and analysis results for technical communication."
module_number: 16
image: /assets/images/modules/module16.svg
image_alt: "Stylized vector art: a clean chart with an uncertainty band on labeled axes."
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
notebook: []
datasets:
  - "/datasets/workflow/"
  - "/datasets/mouseconnects/"
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
  - "Borland D, Taylor RM (2007) Rainbow color map (still) considered harmful. IEEE Computer Graphics and Applications 27(2):14-17."
  - "Crameri F, Shephard GE, Heron PJ (2020) The misuse of colour in science communication. Nature Communications 11:5444."
  - "Rougier NP, Droettboom M, Bourne PE (2014) Ten simple rules for better figures. PLoS Computational Biology 10(9):e1003833."
  - "Weissgerber TL et al. (2015) Beyond bar and line graphs: time for a new data presentation paradigm. PLoS Biology 13(4):e1002128."
  - "Wong B (2011) Points of view: color blindness. Nature Methods 8(6):441."
  - "Birch J (2012) Worldwide prevalence of red-green color deficiency. Journal of the Optical Society of America A 29(3):313-320."
videos: []
downloads: []
last_reviewed: 2026-09-28
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Produce a figure set that communicates connectomics findings accurately, including uncertainty and data-quality context, for both expert and mixed audiences. Students will leave this module able to choose the right visualization form for a given scientific claim, build publication-quality figures using standard tools, and defend every design choice in terms of clarity and honesty.

## Why this module matters
Poor visual design can create false confidence and hide limitations. In connectomics, visualizations are often used as primary evidence: a node-link diagram of a circuit motif, a heatmap of synaptic connectivity, or a 3D rendering of a reconstructed neuron may be the single most important piece of evidence for a paper's central claim. If that figure misleads through cluttered layout, a distorting color scale, needless 3D, or hidden uncertainty, the reader draws the wrong conclusion from correct data.

## Concept set

### 1) Visualization as communication, not decoration
- **Technical:** every visual encoding (position, color, size, shape, opacity) carries information. Encodings that do not map to data dimensions are noise. The goal of a scientific figure is to make the reader's correct interpretation as effortless as possible.
- **Plain language:** a figure should help people understand your result, not impress them with complexity.
- **Misconception guardrail:** a figure that looks good is a figure that tells the truth.
- **Why it fails:** a polished 3D rendering with no scale bar and no uncertainty indicator tells the reader less than a plain but complete 2D plot.

### 2) Choosing the right plot type for connectomics data
- **Technical:** connectomics generates diverse data types, each with preferred visual forms:
  - **Node-link diagrams** show circuit topology and are best for small networks (under ~100 nodes) where individual connections matter. Force-directed layouts can mislead if spatial position is not meaningful.
  - **Adjacency matrices** are better for dense networks and make reciprocal connections, blocks, and community structure visible. Row/column ordering matters enormously --- random ordering hides structure.
  - **Heatmaps** display quantitative connectivity (synapse counts, connection probabilities) across cell-type pairs. Color scale choice is critical; sequential scales for counts, diverging scales for deviations from expected.
  - **3D renderings** of reconstructed morphologies communicate spatial context but are hard to read quantitatively. Use them for orientation and context, not for making numerical arguments.
  - **Sholl plots** quantify dendritic/axonal arborization by counting intersections at increasing radii from the soma, revealing branching complexity in a single 2D chart.
  - **Histograms and violin plots** for distributions of synapse counts, segment sizes, and other scalar metrics.
- **Plain language:** match your chart type to the question you are answering. "What is the circuit topology?" calls for a node-link diagram. "How strong are connections between cell types?" calls for a heatmap.
- **Misconception guardrail:** each data type has one best chart.
- **Why it fails:** the right form depends on the claim; the same matrix can need a heatmap for one sentence and a node-link diagram for another.

### 3) Common visualization mistakes in connectomics
- **Technical:**
  - **Cluttered graphs:** plotting a full connectome as a node-link diagram produces an unreadable hairball. Aggregate, filter, or use matrix representations instead.
  - **Misleading color scales:** rainbow/jet colormaps distort perceived magnitude because they are not perceptually uniform. Use viridis, inferno, or other perceptually uniform scales.
  - **3D when 2D suffices:** rotating 3D scatter plots look impressive but make quantitative comparison nearly impossible. Use 3D only when the third spatial dimension is genuinely necessary.
  - **Missing scale bars and axis labels:** a reconstruction rendering without a scale bar is uninterpretable. An adjacency matrix without labeled rows/columns is useless.
  - **Overplotting:** when thousands of synapses overlap, individual points disappear. Use density plots, transparency, or binning.
- **Plain language:** the most common mistakes are showing too much at once, using colors that lie about magnitude, and using 3D for flash rather than function.
- **Misconception guardrail:** a more complex figure shows a more rigorous analysis.
- **Why it fails:** complexity hides the claim. Aim for the simplest figure that is still complete.

### 4) Uncertainty must be visible
- **Technical:** confidence intervals, confidence classes, and missingness indicators should be explicit in every figure that supports a quantitative claim. Strategies include error bars, shaded confidence bands, hatching for uncertain regions, and explicit "data not available" markers for boundary neurons or unproofread segments.
- **Plain language:** show what is uncertain, not only what is central. If a synapse count could be off by 20%, the reader needs to know.
- **Misconception guardrail:** removing error bars makes a plot cleaner and therefore better.
- **Why it fails:** a plot that hides uncertainty is less honest than one that shows it.

### 5) Accessibility and colorblind-safe design
- **Technical:** in large population surveys of European populations, about 8% of men and about 0.4% of women have inherited red-green color deficiency (Birch 2012). Figures that rely on red-green discrimination exclude these readers. Use colorblind-safe palettes (e.g., Okabe-Ito, ColorBrewer qualitative palettes) and redundant encoding (color + shape, color + pattern). Ensure sufficient contrast for printing in grayscale. Keep annotation density manageable --- overcrowded labels defeat the purpose.
- **Plain language:** if people cannot read it, they cannot evaluate it. Design for the widest possible audience.
- **Misconception guardrail:** if the figure reads well on your screen, it reads well for everyone.
- **Why it fails:** red-green contrasts, thin lines, and low-contrast labels lock out readers with color vision deficiency or a grayscale printout.

## Worked example: the heatmap that hid its own sparsity

Every number here comes from the [Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }}), which is synthetic and generated from a fixed seed, so you can reproduce each step. Nothing below is a finding about a brain.

`celltype_synapses.csv` is a 50 x 50 matrix of synapse counts between cell types: 2,500 cells, median 36 synapses, maximum 1,089 (L5_09 onto L5_05), and 27 cells at zero. Its companion `celltype_connections.csv` gives the number of connected neuron pairs behind each cell. 907 of the 2,500 cells, 36%, rest on fewer than 10 pairs.

**Draft 1.** A linear color scale from 0 to 1,089, the jet colormap, rows and columns in file order. It looks like a heatmap and it says almost nothing. Three reasons. First, the scale: 90% of cells are at or below 146 synapses, the 90th percentile, so nine cells in ten fall into the bottom 13% of the color range and read as one flat color while three cells above 800 carry the whole image. Second, the colormap: jet is not perceptually uniform, so it draws bands where the data have none (Borland & Taylor 2007). Third, the sparsity is invisible. A cell built on 3 neuron pairs and a cell built on 433 pairs get the same visual weight, and the reader has no way to tell that a third of the matrix is thinly supported.

**Draft 2.** Color encodes log10(count + 1) on the viridis colormap, with the colorbar labeled "synapses (log scale)". Rows and columns are reordered by hierarchical clustering so blocks become visible. The 907 sparse cells are hatched. The 27 zero cells sit at the bottom of the scale and the caption says so. None of these changes touches the data; each one removes a way the first draft could be misread.

**The Sholl panel gets the same treatment.** `python3 morphometry.py --swc neurons/basket.swc --sholl 10` prints the shell crossings. At a 60 µm radius the basket arbor crosses 23 times, the excitatory arbor 12, the chandelier arbor 7. Those three curves need three colorblind-safe colors with a legend and a radius axis in µm. The uncertainty band comes from `neurons.csv`, which gives an estimated missing-cable fraction of 0.08 for the excitatory reconstruction, 0.15 for the basket and 0.22 for the chandelier, so the chandelier band must be the widest. The caption has to say what the band is: reconstruction incompleteness, not biological variability across cells of that type.

**The caption for Figure 1 after revision.** "Synapse counts between 50 cell types (rows presynaptic, columns postsynaptic), shown as log10(count + 1) and ordered by hierarchical clustering. Hatched cells rest on fewer than 10 connected neuron pairs (907 of 2,500). Synthetic data: Module 16 kit, `celltype_synapses.csv` and `celltype_connections.csv`, generated by `scripts/generate_kit_materials.rb` from a fixed seed." A reader can now check every claim the figure makes.

**What this example does not establish.** That clustering order is the right order for every claim. A sentence about laminar organization is served better by ordering rows by layer, even though the blocks become less crisp. The ordering, like the plot type, follows the claim, which is why the claim is written first.

## Tools for connectomics visualization

### Neuroglancer
Browser-based volumetric visualization for EM data, segmentation overlays, and mesh browsing. Ideal for exploring reconstructed volumes interactively, generating shareable view states, and verifying proofreading. Used extensively in MICrONS, FlyWire, and H01 projects.

### Matplotlib and Plotly
The workhorses of 2D figure generation in Python. Matplotlib excels at publication-quality static figures with fine-grained control. Plotly provides interactive figures useful for exploration and web-based sharing. Both support adjacency matrices, histograms, violin plots, Sholl plots, and scatter plots.

### Blender and ParaView
For high-quality 3D renderings of neuronal morphologies and circuit reconstructions. Blender produces photorealistic images suitable for journal covers and presentations. ParaView handles large-scale scientific datasets with built-in volume rendering. Both take time to learn; use them when a figure needs a rendering that Neuroglancer screenshots cannot give.

### napari
Python-based multi-dimensional image viewer for volume data. Supports overlaying segmentation masks on EM imagery, annotating structures, and integrating with analysis pipelines through its plugin ecosystem. Lighter-weight than Neuroglancer for local exploration.

## Core workflow
1. **Map each claim to required visual evidence.** For every result sentence, identify what figure panel and what visual encoding will support it.
2. **Select the appropriate plot type.** Use the decision framework: topology questions get node-link diagrams or matrices; quantity questions get heatmaps or bar charts; spatial questions get renderings; distribution questions get histograms or violins.
3. **Draft candidate visuals with uncertainty layers.** Include error bars, confidence bands, or explicit missing-data indicators from the start --- do not plan to "add them later."
4. **Run critique for misinterpretation risk.** Show the draft to someone unfamiliar with the analysis and ask them what they conclude. If their conclusion differs from your intent, revise.
5. **Check accessibility.** Run the figure through a colorblind simulator (e.g., Coblis, or a Python library such as colorspacious). Verify grayscale legibility.
6. **Revise for clarity, accessibility, and reproducibility.** Add scale bars, axis labels, panel letters, and complete captions.
7. **Export figure package with caption metadata.** Include figure files at publication resolution (300+ DPI for raster, vector preferred), caption text, and a note on the dataset version and code used to generate each panel.

## Time budget
The declared 4 hours are: about 30 minutes reading the concept set beforehand, a 90-minute meeting (the 60-minute run-of-show below plus the opening of the studio activity), and about 2 hours outside class finishing the studio figures, the quick practice prompt, and the linked readings. Neither [syllabus map]({{ '/teaching/syllabi/' | relative_url }}) schedules a meeting for this kit; the 16-week map offers it as a 4-hour take-home on the learner's own analysis card, in which case the run-of-show is read rather than run and the studio is done alone.

## 60-minute tutorial run-of-show

### Materials needed
- Projected examples: 3 good and 3 bad connectomics figures (prepared in advance from published papers or synthetic examples).
- Shared dataset: the [Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }}) (synthetic). Use a 20 x 30 block of its cell-type matrix and the `excitatory.swc` skeleton for the Sholl plot.
- Software: Matplotlib or Plotly in a notebook each learner starts; [MICrONS Explorer](https://www.microns-explorer.org/) open for the 3D context view.
- Colorblind simulation tool (browser-based), such as [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/).
- Printed or digital critique rubric (one per student): the four questions in the 47:00-55:00 block below.

### Timing and instructor script

**00:00-10:00 | Visual integrity gallery walk**
Instructor displays six figures (three strong, three weak) without labels. Students vote on which are "trustworthy" and which are "suspicious." Instructor reveals issues: missing scale bars, rainbow colormaps, cluttered node-link diagrams, hidden uncertainty, gratuitous 3D. Key script line: "Your first instinct about a figure's trustworthiness is often right. Now name the feature that triggered it."

**10:00-20:00 | Claim-to-visual mapping exercise**
Instructor presents three scientific claims from a mock connectomics study:
1. "Excitatory neurons in layer 4 receive more synaptic input than those in layer 2/3."
2. "Reciprocal connections are enriched between Martinotti cells."
3. "Axonal arbors of chandelier cells are spatially restricted to a 100-micron radius."
Students work in pairs to select the best plot type for each claim and justify their choice. Instructor circulates, challenging choices: "Why not a node-link diagram for claim 1? What would you lose with a heatmap for claim 3?"

**20:00-35:00 | Figure draft build**
Students open a notebook, load the kit files, and generate: (a) an adjacency heatmap for the cell-type connectivity matrix, (b) a Sholl plot for the kit's excitatory neuron. Instructor models adding axis labels, a perceptually uniform colormap, and a scale bar. Students replicate and customize.

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
{: #studio-activity}

**Scenario:** You are preparing a three-figure package for a short connectomics paper reporting cell-type-specific connectivity patterns in a cortical volume. Your dataset includes a 50x50 cell-type adjacency matrix, morphological reconstructions for three example neurons, and synapse count distributions across layers (all synthetic, in the [Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }})).

**Figure 1 task:** Create an adjacency heatmap of the cell-type connectivity matrix. Choose an appropriate colormap, add a colorbar with units, order rows and columns by hierarchical clustering, and annotate the diagonal. Include hatching or transparency for cell-type pairs with fewer than 10 observed connections.

**Figure 2 task:** Generate Sholl plots for the three example neurons (one excitatory, one inhibitory basket cell, one inhibitory chandelier cell). Use distinct colorblind-safe colors with a legend. Add shaded confidence bands reflecting reconstruction uncertainty. Label the radius axis in µm and mark radius zero as the soma.

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

## Common errors and how to recover

- **A reader says the heatmap "shows nothing".** The usual cause is a linear color scale on a heavy-tailed matrix, so most cells share one color. Recover by switching to a log or quantile scale, saying so on the colorbar label, and hatching the cells that rest on few observations.
- **Two panels of the same quantity give different impressions.** Their color ranges differ. Recover by fixing the same minimum and maximum across panels and stating the shared scale once in the caption.
- **A 3D rendering is the only evidence for a quantitative claim.** Recover by adding a 2D panel that carries the number (a Sholl plot, a histogram, a bar with an interval) and keeping the rendering for orientation, with a scale bar.
- **Error bars came off in the last revision "to clean it up".** Restore them. If the interval is too wide to show comfortably, that width is the finding; report n and say why the interval is wide.
- **The figure passes the colorblind simulator and fails in grayscale.** Two hues had similar luminance. Recover with redundant encoding (shape, line style or pattern in addition to color) and check the luminance contrast directly.
- **A node-link diagram of 2,000 nodes.** Nobody can read it. Recover by aggregating to cell types, or by switching to an adjacency matrix, and keep node-link diagrams for the small networks where individual edges matter.
- **You cannot regenerate the figure six months later.** Recover by treating each panel as the output of a script: the script, the dataset version and the seed go in the caption metadata, and the exported file is never edited by hand.

## What this module does not cover

- **Writing the paper the figures sit in.** Claim-evidence mapping, legends as part of the methods record, and reviewer responses are [Module 17]({{ '/modules/module17/' | relative_url }}).
- **Slides and spoken delivery.** What a figure has to do on a slide, in a room, in eight minutes, is [Module 22]({{ '/modules/module22/' | relative_url }}).
- **What the interval means.** Null models, multiplicity and the difference between an exploratory and a confirmatory result are [Module 20]({{ '/modules/module20/' | relative_url }}). This module shows the uncertainty; that one decides what it licenses.
- **Cleaning the table before plotting it.** Thresholds, duplicates and boundary neurons are [Module 18]({{ '/modules/module18/' | relative_url }}); a figure built on an uncleaned table inherits its defects.
- **The formats behind the figure.** What a Zarr volume, an SWC skeleton or a synapse table contains is [data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}).
- **Interactive dashboards and web viewers as software.** Building a Neuroglancer deployment or a web app is engineering outside this curriculum; here Neuroglancer is a tool you use, not one you build.

## Content library cross-references
- [Data formats]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) --- understanding the source formats (Zarr volumes, CSV synapse tables, SWC morphologies) that feed visualization workflows.
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}) --- adjacency matrices, edge lists, and graph objects that underlie node-link diagrams and heatmaps.

## Teaching resources
- [Technical Unit 09: Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- [Module 17: Scientific Writing for Connectomics]({{ '/modules/module17/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})
- [Workflow overview]({{ '/datasets/workflow/' | relative_url }})
- [Module 16 kit]({{ '/assets/kits/module16/README.md' | relative_url }}) — synthetic cell-type matrices, three example skeletons and layer counts

## Evidence anchors from connectomics practice

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

## Academic references
- Borland D, Taylor RM (2007) "Rainbow color map (still) considered harmful." *IEEE Computer Graphics and Applications* 27(2):14-17. doi:10.1109/MCG.2007.323435. Why the jet colormap draws bands the data do not have.
- Crameri F, Shephard GE, Heron PJ (2020) "The misuse of colour in science communication." *Nature Communications* 11:5444. doi:10.1038/s41467-020-19160-7. Perceptual uniformity and color-vision-deficient readers, with scientific colormaps that satisfy both.
- Rougier NP, Droettboom M, Bourne PE (2014) "Ten simple rules for better figures." *PLoS Computational Biology* 10(9):e1003833. doi:10.1371/journal.pcbi.1003833. The claim-first, audience-first rules behind the core workflow.
- Weissgerber TL, Milic NM, Winham SJ, Garovic VD (2015) "Beyond bar and line graphs: time for a new data presentation paradigm." *PLoS Biology* 13(4):e1002128. doi:10.1371/journal.pbio.1002128. Why Figure 3 shows the points, not only the summary.
- Wong B (2011) "Points of view: color blindness." *Nature Methods* 8(6):441. doi:10.1038/nmeth.1618. The eight-color palette this module calls Okabe-Ito.
- Birch J (2012) "Worldwide prevalence of red-green color deficiency." *Journal of the Optical Society of America A* 29(3):313-320. doi:10.1364/JOSAA.29.000313. The prevalence figures in Concept 5.

## Quick practice prompt
Take one existing connectomics figure (from a paper, a classmate, or your own work) and perform a full audit:
1. Identify the claim the figure is supposed to support.
2. Add one uncertainty cue (error bar, confidence band, or missing-data indicator).
3. Replace the colormap with a perceptually uniform alternative if needed.
4. Write a two-sentence caption that narrows interpretation bounds and specifies the dataset version.
5. Run the figure through a colorblind simulator and note any issues.
