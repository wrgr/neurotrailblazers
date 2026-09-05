---
marp: true
theme: default
paginate: true
title: "Module 16: Scientific Visualization for Connectomics"
---

# Module 16: Scientific Visualization for Connectomics
Teaching Deck

---

## Learning Objectives
- Select visualization forms aligned to analytical intent
- Encode uncertainty and quality signals explicitly
- Avoid misleading visual encodings in dense connectomics data
- Produce publication-ready and presentation-ready figures

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
Produce a figure set that communicates connectomics findings accurately, including uncertainty and data-quality context, for both expert and mixed audiences. Students will leave this module able to choose the right visualization form for a given scientific claim, build publication-quality figures using standard tools, and defend every design choice in terms of clarity and honesty.

---

## Concept Focus
### 1) Visualization as communication, not decoration
- **Technical:** every visual encoding (position, color, size, shape, opacity) carries information. Encodings that do not map to data dimensions are noise. The goal of a scientific figure is to make the reader's correct interpretation as effortless as possible.
- **Plain language:** a figure should help people understand your result, not impress them with complexity.
- **Misconception guardrail:** making a figure "look good" is not the same as making it truthful. A beautiful 3D rendering with no scale bar and no uncertainty indicators is worse than an ugly but complete 2D plot.

---

## Core Workflow
- **Map each claim to required visual evidence.** For every result sentence, identify what figure panel and what visual encoding will support it.
- **Select the appropriate plot type.** Use the decision framework: topology questions get node-link diagrams or matrices; quantity questions get heatmaps or bar charts; spatial questions get renderings; distribution questions get histograms or violins.
- **Draft candidate visuals with uncertainty layers.** Include error bars, confidence bands, or explicit missing-data indicators from the start --- do not plan to "add them later."
- **Run critique for misinterpretation risk.** Show the draft to someone unfamiliar with the analysis and ask them what they conclude. If their conclusion differs from your intent, revise.
- **Check accessibility.** Run the figure through a colorblind simulator (e.g., Coblis or the Matplotlib colorblind check). Verify grayscale legibility.
- **Revise for clarity, accessibility, and reproducibility.** Add scale bars, axis labels, panel letters, and complete captions.
- **Export figure package with caption metadata.** Include figure files at publication resolution (300+ DPI for raster, vector preferred), caption text, and a note on the dataset version and code used to generate each panel.

---

## 60-Minute Run-of-Show
- Projected examples: 3 good and 3 bad connectomics figures (prepared in advance from published papers or synthetic examples).
- Shared dataset: a small adjacency matrix (20x30 cell types) and one reconstructed neuron mesh.
- Software: Matplotlib/Plotly notebooks pre-loaded; Neuroglancer link ready.
- Colorblind simulation tool (browser-based).
- Printed or digital critique rubric (one per student).
- "Excitatory neurons in layer 4 receive more synaptic input than those in layer 2/3."
- "Reciprocal connections are enriched between Martinotti cells."
- "Axonal arbors of chandelier cells are spatially restricted to a 100-micron radius."
- Every student figure includes at least one uncertainty indicator.
- Captions specify dataset version and analysis parameters.
- No figure uses a rainbow/jet colormap.

---

## Misconceptions to Watch
- **Misconception guardrail:** making a figure "look good" is not the same as making it truthful. A beautiful 3D rendering with no scale bar and no uncertainty indicators is worse than an ugly but complete 2D plot.
- **Misconception guardrail:** there is no single "best" visualization. The best choice depends on the claim.
- **Misconception guardrail:** complexity in a figure does not equal rigor. Simplicity with completeness is the standard.
- **Misconception guardrail:** cleaner-looking plots are not always better. A plot that hides uncertainty is less honest than one that shows it.
- **Misconception guardrail:** aesthetics cannot replace methodological clarity. A beautiful figure that only some people can read is not a good figure.

---

## Studio Activity
**Scenario:** You are preparing a three-figure package for a short connectomics paper reporting cell-type-specific connectivity patterns in a cortical volume. Your dataset includes a 50x50 cell-type adjacency matrix, morphological reconstructions for three example neurons, and synapse count distributions across layers.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass:** visuals map clearly to claims, include uncertainty context, use perceptually uniform colormaps, and have complete axis labels and scale bars.
- **Strong performance:** high clarity across expert and non-expert audiences, minimal misinterpretation risk, colorblind-safe design, explicit documentation of dataset version and code used for each panel, and thoughtful caption language that narrows interpretation bounds.
- **Failure modes:** overloaded figures with too many overlapping elements, missing scale context, hidden uncertainty, rainbow colormaps, gratuitous 3D renderings, captions that do not mention data quality or limitations.

---

## Exit Ticket
Take one existing connectomics figure (from a paper, a classmate, or your own work) and perform a full audit:
1. Identify the claim the figure is supposed to support.
2. Add one uncertainty cue (error bar, confidence band, or missing-data indicator).
3. Replace the colormap with a perceptually uniform alternative if needed.
4. Write a two-sentence caption that narrows interpretation bounds and specifies the dataset version.
5. Run the figure through a colorblind simulator and note any issues.

---

## References (Instructor)
- Visualization best-practice resources and connectomics exemplars.

---

## Teaching Materials
- Module page: /modules/module16/
- Slide page: /modules/slides/module16/
- Worksheet: /assets/worksheets/module16/module16-activity.md
