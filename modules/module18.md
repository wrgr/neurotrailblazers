---
title: "Module 18: Data Cleaning and Preprocessing"
layout: module
permalink: /modules/module18/
description: "Build reproducible preprocessing workflows for connectomics data, from integrity checks through analysis-ready releases."
module_number: 18
difficulty: "Intermediate"
duration: "4-5 hours"
learning_objectives:
  - "Diagnose common connectomics data-quality issues before analysis"
  - "Apply reproducible preprocessing steps with documented decision rules"
  - "Quantify preprocessing impact with auditable QC metrics"
  - "Produce an analysis-ready dataset package with provenance metadata"
prerequisites: "Modules 12-16 or equivalent Python/data-handling experience"
merit_stage: "Analysis"
compass_skills:
  - "Data Quality"
  - "Workflow Design"
  - "Reproducibility"
ccr_focus:
  - "Skills - Data Processing"
  - "Character - Scientific Rigor"

# Normalized metadata
slug: "module18"
short_title: "Data Cleaning and Preprocessing"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "data-cleaning"
  - "preprocessing"
  - "quality-control"
  - "reproducibility"
summary: "Detect artifacts, clean and standardize connectomics tables/volumes, and release analysis-ready data with documented provenance."
key_questions:
  - "What preprocessing decisions materially change biological conclusions?"
  - "How do we separate data repair from data distortion?"
  - "What metadata is required to make preprocessing reproducible?"
slides: []
notebook:
  - "/assets/notebooks/module12/module12-big-data-in-connectomics.ipynb"
datasets:
  - "/datasets/workflow"
  - "/datasets/mouseconnects"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic dataframe manipulation in Python"
  - "Familiarity with segmentation/proofreading outputs"
next_modules:
  - "module19"
  - "module20"
references:
  - "Wilkinson et al., 2016. The FAIR Guiding Principles for scientific data management and stewardship."
  - "Peng, 2011. Reproducible Research in Computational Science."
  - "MICrONS and related connectomics workflow documentation."
videos:
  - "https://www.neurotrailblazers.org/technical-training/03-em-prep-and-imaging/"
  - "https://www.neurotrailblazers.org/technical-training/04-volume-reconstruction-infrastructure/"
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Produce a reproducible preprocessing release that transforms raw or intermediate connectomics outputs into analysis-ready data, with explicit quality gates and full provenance. Students will be able to identify the specific cleaning operations that shape biological conclusions, justify every threshold decision, and document their preprocessing pipeline so that another researcher can audit and reproduce it.

## Why this module matters
Most downstream failures in connectome analysis are not model failures first; they are data-quality and preprocessing failures. A synapse table with unfiltered false positives inflates connectivity estimates. A neuron table that includes tiny orphan fragments skews degree distributions. A graph built without handling volume-boundary neurons misrepresents the network. Every preprocessing decision --- what to filter, what threshold to set, what to include or exclude --- directly shapes the biological conclusions that follow. This module teaches how to clean data without erasing signal, and how to document each transformation so conclusions remain defensible.

## Concept set

### 1) Data cleaning in connectomics: what needs fixing and why
- **Technical:** connectomics datasets arrive with characteristic quality issues that must be addressed before analysis:
  - **Synapse table filtering:** automated synapse detection produces false positives (cleft detections at non-synaptic locations) and false negatives (missed synapses). Filtering typically uses a confidence score threshold (e.g., cleft score > 50 in CAVE synapse tables). The choice of threshold directly affects edge weights in the connectivity graph.
  - **Segment size thresholding:** automated segmentation produces many small fragments --- bits of neuropil, partial dendrites, glia misclassified as neurons. Including these in analysis adds noise. Common practice is to exclude segments below a volume or synapse count threshold (e.g., segments with fewer than 2 synapses as pre- or post-synaptic partner).
  - **Removing orphan fragments:** segments that have no synaptic connections to any other segment are orphans. They typically represent segmentation debris or incomplete reconstructions. Including them inflates node counts and distorts network metrics.
  - **Handling neurons at volume boundaries:** neurons whose arbors are truncated by the edge of the imaged volume have artificially low synapse counts and incomplete morphologies. These boundary neurons can be flagged (e.g., by checking whether the segment mesh intersects the volume bounding box) and either excluded or analyzed with explicit caveats.
  - **Duplicate and conflicting IDs:** merges and splits during proofreading can create duplicate entries or conflicting segment-to-cell-type mappings that must be resolved.
- **Plain language:** connectomics data is not "clean" when you receive it. Segmentation makes mistakes, synapse detection has false alarms, and the edges of the volume cut through neurons. You must fix these issues before analysis, but every fix is a decision that affects your results.
- **Misconception guardrail:** "raw data is always better." In connectomics, raw segmentation output contains systematic artifacts that will corrupt analysis if left uncleaned. The question is not whether to clean, but how to clean transparently.

### 2) Threshold decisions that shape analysis
- **Technical:** two of the most consequential preprocessing decisions in connectomics are:
  - **Minimum synapse count for edges:** should a connection between two neurons count if it involves only 1 synapse? Or require 2, 3, or 5? This threshold changes the graph density, affects motif counts, and can alter community detection results. There is no universally correct answer --- the choice depends on the scientific question and the false-positive rate of synapse detection.
  - **Minimum segment size for inclusion:** should a segment be included if it has only 10 voxels? 1,000? 100,000? Small segments are often noise, but aggressive size filtering can remove real small neurons (e.g., some interneuron types have compact morphologies).
  - **Confidence score thresholds for synapses:** higher thresholds reduce false positives but increase false negatives. The optimal threshold depends on the downstream analysis: motif detection may be more sensitive to false positives, while connectivity strength estimation may be more sensitive to false negatives.
- **Plain language:** every threshold you set changes your results. There is no "neutral" threshold. The responsible approach is to justify your choice, report it explicitly, and test whether your conclusions change if you move the threshold.
- **Misconception guardrail:** there is no single "correct" threshold. If your result depends on a specific threshold choice, it is fragile and should be reported with a sensitivity analysis.

### 3) Cleaning vs distortion
- **Technical:** preprocessing should reduce known artifacts and noise while preserving biologically meaningful structure. The distinction is not always clean: removing small segments removes noise but might also remove small neurons. Filtering low-confidence synapses removes false positives but also removes some true synapses. The key principle is that every cleaning step should have a stated rationale tied to a known data artifact, not to making results "look better."
- **Plain language:** fix mistakes, do not "polish away" the biology.
- **Misconception guardrail:** more filtering is not always better. Aggressive cleaning can create the appearance of clean results while actually removing biological signal.

### 4) Provenance as a scientific requirement
- **Technical:** every transform should be traceable: input version (e.g., CAVE materialization timestamp), parameters (thresholds, filter criteria), code version (git commit hash), timestamp, operator, and output hash. This is not just good practice --- it is a requirement for scientific reproducibility. If you cannot explain how the analysis-ready dataset was made from the raw data, no one can evaluate whether your preprocessing introduced bias.
- **Plain language:** if you cannot explain how the file was made, you cannot trust the result.
- **Misconception guardrail:** version-control notes alone are insufficient without data lineage. Git tracks code changes, but you also need to track which data version was processed with which code version.

### 5) Documenting cleaning decisions for reproducibility
- **Technical:** maintain a preprocessing decision log that records, for each cleaning step: (a) what was done, (b) why it was done (which artifact it addresses), (c) the exact parameters, (d) the impact on data dimensions (how many rows/segments/synapses were removed), and (e) any known risks (what biological signal might have been lost). This log should be a deliverable alongside the cleaned data, not an afterthought.
- **Plain language:** write down every decision as you make it. Future-you and your collaborators will need this record.
- **Misconception guardrail:** documenting preprocessing after the fact is unreliable. Document decisions in real time.

### 6) QC metrics must be decision-linked
- **Technical:** metrics (missingness rates, merge/split error estimates, synapse count distributions, segment size distributions, consistency checks) should trigger concrete accept/rework decisions. Define quality gates before preprocessing: "If more than 5% of synapses fall below the confidence threshold, investigate detection quality before proceeding." A dashboard that displays metrics without thresholds is monitoring, not quality control.
- **Plain language:** a dashboard is useful only if it changes what you do.
- **Misconception guardrail:** reporting metrics without thresholds is not quality control. Every metric needs an associated action.

## Core workflow: preprocessing for connectomics
1. **Ingest and integrity validation**
   - Confirm file completeness, schema conformance, and version compatibility.
   - Log dataset identifiers, CAVE materialization version, and checksums.
   - Verify that the synapse table, segment table, and cell-type annotations refer to the same materialization.
2. **Artifact and anomaly screening**
   - Compute segment size distribution and flag outliers (extremely large segments may be merge errors; extremely small segments may be debris).
   - Compute synapse confidence score distribution and identify the threshold region.
   - Check for duplicate segment IDs, conflicting cell-type labels, and missing foreign keys.
   - Identify boundary neurons by mesh-bounding-box intersection.
   - Triage issues by likely biological impact: high-impact issues block analysis; low-impact issues are documented and accepted.
3. **Cleaning transforms**
   - Apply synapse confidence threshold with documented rationale.
   - Remove orphan segments (zero synapses as both pre and post).
   - Apply segment size threshold with documented rationale.
   - Flag or remove boundary neurons with documented policy.
   - Resolve duplicate IDs and label conflicts.
   - Normalize units (e.g., convert voxel coordinates to nanometers using dataset resolution metadata).
4. **QC and drift checks**
   - Compare pre/post distributions: synapse count per neuron, segment size, graph density, degree distribution.
   - Verify that cleaning did not selectively remove a specific cell type or spatial region.
   - Check that graph topology statistics (clustering coefficient, connected components) are consistent with expectations.
5. **Release packaging**
   - Publish analysis-ready tables plus: preprocessing decision log, transform code with commit hash, QC metric report with threshold justifications, known limitations and residual risks.

## Studio activity: preprocessing release simulation

**Scenario:** Your team receives a connectomics export from MICrONS minnie65 (CAVE materialization v795) containing: a synapse table (4.2 million rows) with confidence scores, a segment table (120,000 segments) with volumes, and a cell-type annotation table (8,400 classified neurons). Initial inspection reveals: 12% of synapses have confidence scores below 30, 35,000 segments have fewer than 2 synapses, 847 segments intersect the volume bounding box, and 23 segment IDs appear in the synapse table but not in the segment table.

**Tasks**
1. **Artifact triage:** classify each issue (low-confidence synapses, small segments, boundary neurons, orphan IDs) by likely biological impact and propose a cleaning policy for each.
2. **Threshold justification:** for synapse confidence and segment size thresholds, propose two candidate values each and argue for your preferred choice. Explain what biological signal you might lose at each threshold.
3. **Implement preprocessing pipeline:** write pseudocode or notebook-level steps for the full cleaning workflow, from ingest through release.
4. **QC comparison:** compute (or estimate) pre/post metrics: total synapse count, total segment count, mean degree, graph density, and the fraction of each cell type remaining after cleaning.
5. **Release note:** produce a one-page release note that includes: input dataset version, all thresholds and parameters, code reference, QC metrics with pass/fail calls, and known residual risks (e.g., "boundary neurons were excluded, which may underrepresent connectivity of neurons near volume edges").

**Expected outputs**
- Preprocessing decision table (one row per issue, columns: issue, policy, threshold, rationale, impact).
- QC metric summary with thresholds and pass/fail calls.
- Release note (inputs, transforms, outputs, limitations).

## Assessment rubric
- **Minimum pass**
  - Cleaning decisions are explicit, justified, and reproducible.
  - QC metrics include thresholds tied to concrete actions.
  - Release package includes provenance metadata (dataset version, code commit, parameters).
- **Strong performance**
  - Distinguishes low-risk cleanup from biologically sensitive transforms with explicit reasoning.
  - Includes sensitivity analysis: "If we move the synapse threshold from 50 to 30, X% more edges appear and Y motifs change significance."
  - Documents limitations and unresolved risks transparently, including what biological signal may have been lost.
- **Common failure modes**
  - Silent ad-hoc edits with no transform log.
  - Aggressive filtering that removes biologically meaningful variation without acknowledgment.
  - Metrics reported without operational thresholds.
  - Missing dataset version or code commit in the release note.

## Content library cross-references
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}) --- the graph structures that preprocessing feeds into, and how cleaning decisions affect them.
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) --- the infrastructure for tracking dataset versions, materializations, and transform lineage.
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) --- understanding the upstream pipeline (imaging, alignment, segmentation, synapse detection) that produces the artifacts preprocessing must address.

## Teaching resources
- Lesson context: [Volume Reconstruction Infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
- QC context: [Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
- Slides: [Infrastructure deck draft]({{ '/technical-training/slides/04-volume-reconstruction-infrastructure/' | relative_url }})
- Practice dataset workflow: [Workflow overview]({{ '/datasets/workflow' | relative_url }})
- Quality framework: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## 60-minute tutorial run-of-show

### Materials
- One noisy connectomics table (synapse table with low-confidence entries, duplicate IDs, and missing cell-type labels).
- Segment table with size distribution spanning 5 orders of magnitude.
- Shared preprocessing decision sheet (printed or digital template).
- QC dashboard template (pre/post metric comparison).

### Timing and instructor script

**00:00-08:00 | Setup and target framing**
Instructor presents the scenario: "You have received a connectomics export. Before you can analyze it, you must clean it. But every cleaning decision changes your results. Today we learn to clean responsibly." Display the raw data summary statistics. Define the release objective: an analysis-ready synapse table and neuron table with documented provenance. Define non-negotiable quality gates: no duplicate IDs, no unresolved foreign keys, all thresholds documented.

**08:00-18:00 | Instructor modeling: ingest and anomaly screening**
Live demonstration: load the synapse table, compute the confidence score distribution, identify the bimodal peak (true synapses vs false positives). Show the segment size distribution on a log scale, point out the debris tail. Check for orphan IDs. Key script line: "Before you touch the data, understand its shape. The distribution plot is your first diagnostic tool."

**18:00-32:00 | Team preprocessing design**
Teams of 3-4 draft cleaning rules for each identified issue. Each team must produce a preprocessing decision table with columns: issue, proposed action, threshold, rationale, estimated impact. Instructor circulates, challenging threshold choices: "Why 50 and not 40? What do you lose at 50 that you keep at 40?"

**32:00-44:00 | QC pass**
Teams compute (or estimate from the provided distributions) pre/post metrics: total synapse count, total segment count, mean synapses per neuron, fraction of each cell type remaining. Teams make a release/no-release decision based on their quality gates. Instructor asks: "Did cleaning change the relative representation of cell types? If it did, that is a bias you must report."

**44:00-54:00 | Cross-team review**
Teams swap preprocessing decision tables and QC reports. Each team audits the other's transform log for: missing rationale, unjustified thresholds, potential biological signal loss, and reproducibility gaps. Teams write two specific improvement suggestions.

**54:00-60:00 | Competency checkpoint**
Each team submits one release note with: dataset version, all thresholds and parameters, QC metrics with pass/fail, and at least one documented residual risk. Instructor reviews one example live.

### Success criteria for this session
- Cleaning decisions are deterministic, justified, and documented in real time.
- QC thresholds are tied to operational actions (not just reported).
- Release note exposes at least one unresolved interpretation risk.

## Evidence anchors from connectomics practice

### Key papers to use in this module
- [Januszewski, M. et al. (2018). "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods*, 15, 605-610.](https://doi.org/10.1038/s41592-018-0049-4) --- understanding the segmentation artifacts that preprocessing must address.
- [Shapson-Coe, A. et al. (2024). H01 human cortical fragment. *Science.*](https://www.science.org/doi/10.1126/science.adk4858) --- dataset description and quality documentation practices.
- [MICrONS Consortium (2025). Visual cortex reconstruction. *Nature.*](https://www.nature.com/articles/s41586-025-08790-w) --- large-scale preprocessing decisions and their documentation.
- [Wilkinson, M.D. et al. (2016). "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data*, 3, 160018.](https://doi.org/10.1038/sdata.2016.18) --- provenance and metadata standards.
- [Peng, R.D. (2011). "Reproducible Research in Computational Science." *Science*, 334, 1226-1227.](https://doi.org/10.1126/science.1213847) --- why preprocessing documentation matters for reproducibility.

### Key datasets to practice on
- [NeuroTrailblazers workflow overview]({{ '/datasets/workflow' | relative_url }})
- [MouseConnects (HI-MC)]({{ '/datasets/mouseconnects' | relative_url }})
- [MICrONS Explorer](https://www.microns-explorer.org/)

### Competency checks
- Can you trace every preprocessing transform from input version to release artifact?
- Can you justify your QC thresholds and explain their operational consequences?
- Can you state one unresolved data-risk that could still affect downstream interpretation?
- Can you explain what biological signal might have been lost at each filtering step?
- If you changed your synapse confidence threshold by 10 points, would your main conclusion still hold?

## Quick practice prompt
Take one connectomics table (real or mock) and write:
1. Three cleaning rules with rationale tied to specific data artifacts.
2. Two QC thresholds with associated pass/fail actions and biological justification.
3. One sensitivity analysis: what happens to your key metric if you relax or tighten your primary threshold by 20%?
4. One limitation that remains after preprocessing, stated concretely enough to guide interpretation.
