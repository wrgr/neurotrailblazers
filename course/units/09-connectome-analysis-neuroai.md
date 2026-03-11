---
unit_slug: "09-connectome-analysis-neuroai"
unit_title: "Connectome Analysis and NeuroAI"
status: draft_ready
primary_sources:
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/neuroAI/metadata/figure_registry.csv
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/assets_outreach/metadata/figure_registry.csv
secondary_sources:
  - course/source-ingest/21-02388_X_techtalk_v2_final_review.md
  - course/source-ingest/module13-lesson3.pptx.md
mapped_modules:
  - module10
  - module13
  - module14
  - module15
  - module20
selected_figures_file: course/units/figures/09-connectome-analysis-neuroai-selected-v1.md
last_updated: 2026-03-10
---

# Unit: Connectome Analysis and NeuroAI

## Learning goals
- Explain why connectome analysis is a core bridge between neuroscience and AI.
- Describe the motif-search workflow from hypothesis to query to interpretation.
- Compare practical tool choices for motif queries and subgraph isomorphism.
- Evaluate how analysis scale and compute constraints shape scientific conclusions.

## Scope boundaries
- In scope:
  - graph/motif-centric connectome analysis
  - NeuroAI motivation and analysis pipeline
  - practical tooling examples (DotMotif/GrandIso-style workflows)
- Out of scope:
  - full cell segmentation methods (covered in Unit 08)
  - wet-lab imaging/acquisition detail (Units 02/03)

## Source synthesis
- Core claims to preserve:
  - biological networks motivate new AI priors and architectures
  - motif search is a practical lens for candidate computational primitives
  - scalable query tooling is required for realistic connectome-scale analysis
- Historical context to reframe:
  - neuroAI deck framing from July 12, 2021 should be labeled historical baseline
  - outreach examples used as context, not as current-state authority
- Needs verification:
  - benchmark claims and speed comparisons before publication-ready copy
  - current status of specific repositories/tools

## Website draft blocks
### Hero framing
Connectome analysis asks a direct question: can biological circuit structure reveal reusable computational motifs that improve AI? This unit introduces the analysis workflow that links graph theory, query languages, and large-scale neural datasets.

### Core concepts
- From connectome graph to candidate motif hypotheses.
- Subgraph search and isomorphism as scientific instruments.
- Why data scale, storage models, and query overhead matter.

### Practical workflow
1. Define motif hypothesis from neuroscience literature.
2. Express query in a readable motif language.
3. Run motif search over connectome graph(s).
4. Compare prevalence to null models / control datasets.
5. Interpret motifs as candidate functional primitives.

### Tools and methods
- DotMotif-style motif specification.
- Cypher-translation and graph backends.
- GrandIso-style accelerated subgraph search.

### Output and impact
- Candidate circuit primitives for hypothesis generation.
- Structured comparisons across regions/species/development.
- NeuroAI design cues for architecture constraints.

## Slide draft sequence (v1)
1. Why connectome analysis for NeuroAI? (motivation)
2. Where current ML falls short (problem framing)
3. What brain data looks like at analysis level
4. Reverse-engineering analogy and limits
5. NeuroAI pipeline overview
6. Motif hypothesis and subgraph framing
7. Query language design (human-readable -> executable)
8. GrandIso/subgraph isomorphism mechanics
9. Performance and scale tradeoffs
10. Atlas-style motif scan examples
11. Developmental/connectome comparison example
12. Interpretation limits and verification checklist
13. Current applications and integration points
14. Summary + reading/resources

## Figure candidates
See: `course/units/figures/09-connectome-analysis-neuroai-selected-v1.md`

## Cross-links
- Related modules: `module10`, `module13`, `module14`, `module15`, `module20`
- Related tools: `/tools/ask-an-expert/`, `/tools/connectome-quality/`
- Related frameworks: `/models/`, `/education/models/`

## Open issues
- Confirm citation/attribution text for selected figures before web integration.
- Decide how many historical figures to keep vs replace with newer references.
- Add one hands-on notebook activity aligned to motif query practice.

## Scope check (expert pass)
- Distinguish motif prevalence from causal mechanism; include null-model comparisons.
- Require statistical controls for multiple comparisons and dataset bias.
- Frame NeuroAI transfer as constrained inspiration, not direct biological equivalence.

## Technical anchors to preserve
- Query language usability is part of scientific throughput.
- Subgraph isomorphism complexity drives practical design tradeoffs.
- Cross-dataset comparability requires standardized preprocessing and annotation assumptions.
