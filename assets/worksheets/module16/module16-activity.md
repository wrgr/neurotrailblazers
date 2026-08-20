# Module 16 Activity Worksheet

**Module:** Module 16: Scientific Visualization for Connectomics  
**Duration:** 4 hours  
*Generated from the module page. Edit `modules/module16.md`, not this file.*

---

## Capability target

Produce a figure set that communicates connectomics findings accurately, including uncertainty and data-quality context, for both expert and mixed audiences. Students will leave this module able to choose the right visualization form for a given scientific claim, build publication-quality figures using standard tools, and defend every design choice in terms of clarity and honesty.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Basic plotting library familiarity
- [ ] Understanding of analysis outputs

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. Which chart/visual form best matches each scientific claim?
   - Your answer:
2. How should uncertainty and data quality be shown visually?
   - Your answer:
3. What design choices commonly mislead interpretation?
   - Your answer:

---

## The task

**Scenario:** You are preparing a three-figure package for a short connectomics paper reporting cell-type-specific connectivity patterns in a cortical volume. Your dataset includes a 50x50 cell-type adjacency matrix, morphological reconstructions for three example neurons, and synapse count distributions across layers.

1. **Map each claim to required visual evidence.** For every result sentence, identify what figure panel and what visual encoding will support it.
2. **Select the appropriate plot type.** Use the decision framework: topology questions get node-link diagrams or matrices; quantity questions get heatmaps or bar charts; spatial questions get renderings; distribution questions get histograms or violins.
3. **Draft candidate visuals with uncertainty layers.** Include error bars, confidence bands, or explicit missing-data indicators from the start --- do not plan to "add them later."
4. **Run critique for misinterpretation risk.** Show the draft to someone unfamiliar with the analysis and ask them what they conclude. If their conclusion differs from your intent, revise.
5. **Check accessibility.** Run the figure through a colorblind simulator (e.g., Coblis or the Matplotlib colorblind check). Verify grayscale legibility.
6. **Revise for clarity, accessibility, and reproducibility.** Add scale bars, axis labels, panel letters, and complete captions.
7. **Export figure package with caption metadata.** Include figure files at publication resolution (300+ DPI for raster, vector preferred), caption text, and a note on the dataset version and code used to generate each panel.

### What you hand in

- Three-figure set exported at publication resolution with complete captions
- Uncertainty annotation strategy document (one paragraph per figure explaining what uncertainty is shown and why)
- Revision log from peer critique (at least two specific changes made in response to feedback)
- Accessibility check report (colorblind simulation screenshot for each figure)

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] **Map each claim to required visual evidence.** For every result sentence, identify what figure panel and what visual encoding will support it.
- [ ] **Select the appropriate plot type.** Use the decision framework: topology questions get node-link diagrams or matrices; quantity questions get heatmaps or bar charts; spatial questions get renderings; distribution questions get histograms or violins.
- [ ] **Draft candidate visuals with uncertainty layers.** Include error bars, confidence bands, or explicit missing-data indicators from the start --- do not plan to "add them later."
- [ ] **Run critique for misinterpretation risk.** Show the draft to someone unfamiliar with the analysis and ask them what they conclude. If their conclusion differs from your intent, revise.
- [ ] **Check accessibility.** Run the figure through a colorblind simulator (e.g., Coblis or the Matplotlib colorblind check). Verify grayscale legibility.
- [ ] **Revise for clarity, accessibility, and reproducibility.** Add scale bars, axis labels, panel letters, and complete captions.
- [ ] **Export figure package with caption metadata.** Include figure files at publication resolution (300+ DPI for raster, vector preferred), caption text, and a note on the dataset version and code used to generate each panel.

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

- [ ] I did not assume: Making a figure "look good" is not the same as making it truthful. A beautiful 3D rendering with no scale bar and no uncertainty indicators is worse than an ugly but complete 2D plot.
- [ ] I did not assume: There is no single "best" visualization. The best choice depends on the claim.
- [ ] I did not assume: Complexity in a figure does not equal rigor. Simplicity with completeness is the standard.
- [ ] I did not assume: Cleaner-looking plots are not always better. A plot that hides uncertainty is less honest than one that shows it.
- [ ] I did not assume: Aesthetics cannot replace methodological clarity. A beautiful figure that only some people can read is not a good figure.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| | "Excitatory neurons in layer 4 receive more synaptic input than those in layer 2/3." |
| | "Reciprocal connections are enriched between Martinotti cells." |
| | "Axonal arbors of chandelier cells are spatially restricted to a 100-micron radius." |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass:** visuals map clearly to claims, include uncertainty context, use perceptually uniform colormaps, and have complete axis labels and scale bars.
- **Strong performance:** high clarity across expert and non-expert audiences, minimal misinterpretation risk, colorblind-safe design, explicit documentation of dataset version and code used for each panel, and thoughtful caption language that narrows interpretation bounds.
- **Failure modes:** overloaded figures with too many overlapping elements, missing scale context, hidden uncertainty, rainbow colormaps, gratuitous 3D renderings, captions that do not mention data quality or limitations.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Take one existing connectomics figure (from a paper, a classmate, or your own work) and perform a full audit:
1. Identify the claim the figure is supposed to support.
2. Add one uncertainty cue (error bar, confidence band, or missing-data indicator).
3. Replace the colormap with a perceptually uniform alternative if needed.
4. Write a two-sentence caption that narrows interpretation bounds and specifies the dataset version.
5. Run the figure through a colorblind simulator and note any issues.

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

*Module page: `/modules/module16/` · Slides: `/modules/slides/module16/` · [Facilitator guide](/teaching/facilitator-guide/)*
