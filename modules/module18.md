---
title: "Module 18: Data Cleaning and Preprocessing"
layout: module
permalink: /modules/module18/
description: "Build reproducible preprocessing workflows for connectomics data, from integrity checks through analysis-ready releases."
module_number: 18
image: /assets/images/modules/module18.svg
image_alt: "Stylized vector art: scattered noisy points passing a sieve into aligned clean rows."
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
notebook: []
datasets:
  - "/datasets/workflow/"
  - "/datasets/mouseconnects/"
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
  - "Wilkinson MD et al. (2016) The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data 3:160018."
  - "Peng RD (2011) Reproducible research in computational science. Science 334(6060):1226-1227."
  - "Dorkenwald S et al. (2025) CAVE: Connectome Annotation Versioning Engine. Nature Methods 22(5):1112-1120."
  - "The MICrONS Consortium (2025) Functional connectomics spanning multiple areas of mouse visual cortex. Nature 640(8058):435-447."
  - "Januszewski M et al. (2018) High-precision automated reconstruction of neurons with flood-filling networks. Nature Methods 15(8):605-610."
videos: []
downloads: []
last_reviewed: 2026-09-26
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Produce a reproducible preprocessing release that transforms raw or intermediate connectomics outputs into analysis-ready data, with explicit quality gates and full provenance. Students will be able to identify the specific cleaning operations that shape biological conclusions, justify every threshold decision, and document their preprocessing pipeline so that another researcher can audit and reproduce it.

## Why this module matters
Most downstream failures in connectome analysis start in the data and its preprocessing, before any model is fitted. A synapse table with unfiltered false positives inflates connectivity estimates. A neuron table that includes tiny orphan fragments skews degree distributions. A graph built without handling volume-boundary neurons misrepresents the network. Every preprocessing decision --- what to filter, what threshold to set, what to include or exclude --- directly shapes the biological conclusions that follow. This module teaches how to clean data without erasing signal, and how to document each transformation so conclusions remain defensible.

## Concept set

### 1) Data cleaning in connectomics: what needs fixing and why
- **Technical:** connectomics datasets arrive with characteristic quality issues that must be addressed before analysis:
  - **Synapse table filtering:** automated synapse detection produces false positives (cleft detections at non-synaptic locations) and false negatives (missed synapses). Filtering typically uses a confidence score threshold (e.g., a minimum cleft score; check the dataset's documentation for the recommended value). The choice of threshold directly affects edge weights in the connectivity graph.
  - **Segment size thresholding:** automated segmentation produces many small fragments --- bits of neuropil, partial dendrites, glia misclassified as neurons. Including these in analysis adds noise. Common practice is to exclude segments below a volume or synapse count threshold (e.g., segments with fewer than 2 synapses as pre- or post-synaptic partner).
  - **Removing orphan fragments:** segments that have no synaptic connections to any other segment are orphans. They typically represent segmentation debris or incomplete reconstructions. Including them inflates node counts and distorts network metrics.
  - **Handling neurons at volume boundaries:** neurons whose arbors are truncated by the edge of the imaged volume have artificially low synapse counts and incomplete morphologies. These boundary neurons can be flagged (e.g., by checking whether the segment mesh intersects the volume bounding box) and either excluded or analyzed with explicit caveats.
  - **Duplicate and conflicting IDs:** merges and splits during proofreading can create duplicate entries or conflicting segment-to-cell-type mappings that must be resolved.
- **Plain language:** connectomics data is not "clean" when you receive it. Segmentation makes mistakes, synapse detection has false alarms, and the edges of the volume cut through neurons. You must fix these issues before analysis, but every fix is a decision that affects your results.
- **Misconception guardrail:** "raw data is always better."
- **Why it fails:** raw segmentation output contains systematic artifacts that corrupt analysis if left in. You will clean; the question is how to clean transparently.

### 2) Threshold decisions that shape analysis
- **Technical:** two of the most consequential preprocessing decisions in connectomics are:
  - **Minimum synapse count for edges:** should a connection between two neurons count if it involves only 1 synapse? Or require 2, 3, or 5? This threshold changes the graph density, affects motif counts, and can alter community detection results. There is no universally correct answer --- the choice depends on the scientific question and the false-positive rate of synapse detection.
  - **Minimum segment size for inclusion:** should a segment be included if it has only 10 voxels? 1,000? 100,000? Small segments are often noise, but aggressive size filtering can remove real small neurons (e.g., some interneuron types have compact morphologies).
  - **Confidence score thresholds for synapses:** higher thresholds reduce false positives but increase false negatives. The optimal threshold depends on the downstream analysis: motif detection may be more sensitive to false positives, while connectivity strength estimation may be more sensitive to false negatives.
- **Plain language:** every threshold you set changes your results. There is no "neutral" threshold. The responsible approach is to justify your choice, report it explicitly, and test whether your conclusions change if you move the threshold.
- **Misconception guardrail:** there is one correct threshold, and finding it settles the question.
- **Why it fails:** if your result depends on one threshold value, it is fragile. Report it with a sensitivity analysis across plausible values.

### 3) Cleaning vs distortion
- **Technical:** preprocessing should reduce known artifacts and noise while preserving biologically meaningful structure. The distinction is not always clean: removing small segments removes noise but might also remove small neurons. Filtering low-confidence synapses removes false positives but also removes some true synapses. The key principle is that every cleaning step should have a stated rationale tied to a known data artifact, not to making results "look better."
- **Plain language:** fix mistakes, do not "polish away" the biology.
- **Misconception guardrail:** more filtering always gives cleaner, better data.
- **Why it fails:** aggressive cleaning can make results look clean while removing biological signal, such as compact interneurons below a size cut.

### 4) Provenance as a scientific requirement
- **Technical:** every transform should be traceable: input version (e.g., CAVE materialization timestamp), parameters (thresholds, filter criteria), code version (git commit hash), timestamp, operator, and output hash. Reproducibility requires it. If you cannot explain how the analysis-ready dataset was made from the raw data, no one can evaluate whether your preprocessing introduced bias.
- **Plain language:** if you cannot explain how the file was made, you cannot trust the result.
- **Misconception guardrail:** git history is enough provenance.
- **Why it fails:** git tracks code changes. You also need data lineage: which data version was processed with which code version.

### 5) Documenting cleaning decisions for reproducibility
- **Technical:** maintain a preprocessing decision log that records, for each cleaning step: (a) what was done, (b) why it was done (which artifact it addresses), (c) the exact parameters, (d) the impact on data dimensions (how many rows/segments/synapses were removed), and (e) any known risks (what biological signal might have been lost). This log should be a deliverable alongside the cleaned data, not an afterthought.
- **Plain language:** write down every decision as you make it. Future-you and your collaborators will need this record.
- **Misconception guardrail:** preprocessing can be documented after the analysis is finished.
- **Why it fails:** a log reconstructed afterwards usually lacks the row counts and parameters. Record each decision as you make it.

### 6) QC metrics must be decision-linked
- **Technical:** metrics (missingness rates, merge/split error estimates, synapse count distributions, segment size distributions, consistency checks) should trigger concrete accept/rework decisions. Define quality gates before preprocessing: "If more than 5% of synapses fall below the confidence threshold, investigate detection quality before proceeding." A dashboard that displays metrics without thresholds is monitoring, not quality control.
- **Plain language:** a dashboard is useful only if it changes what you do.
- **Misconception guardrail:** reporting QC metrics is quality control.
- **Why it fails:** a metric without a threshold and an associated action is monitoring. Quality control changes what you do.

## Worked example: placing one threshold, and showing your work

The numbers here are from the [Module 18 kit]({{ '/assets/kits/module18/README.md' | relative_url }}), which is synthetic and generated from a fixed seed, and they match the published [model responses]({{ '/teaching/answers/module18/' | relative_url }}) for this module. Nothing below describes a real dataset. The scenario in the studio uses larger, invented figures; this example shows the reasoning on the small table you can open.

**Start with the integrity steps, not the threshold.** `noisy_synapses.csv` has 30,450 rows. Removing the 447 exact duplicate rows, the rows whose endpoints are missing from `segments.csv`, and the autapses (pre equals post) leaves 29,589 rows. Thresholding before these steps would have counted duplicates twice and scored rows that have no partner.

**Look at the distribution before choosing a number.** The cleft-score histogram (0 to 255) is bimodal. A low mode peaks at scores 32 to 39 (962 rows), a high mode peaks at 144 to 151 (2,288 rows), and the trough sits at 64 to 71 (428 rows). The studio scenario's candidate values of 30 and 50 both fall inside the low mode: only 6.8% and 14.4% of rows sit below them, and most of the low mode survives either cut.

**Two candidates, one decision.** At 64, the trough, 5,315 rows are removed (18.0%), and the graph among the 407 neurons with a soma keeps 2,231 directed edges. The rows that touch a segment smaller than 1 µm³, which is the debris tail, drop from 2,905 to 178, so the low mode is mostly detections onto fragments. At 96, a conservative cut, 7,638 rows go (25.8%) and 2,013 edges remain, 9.8% fewer than at 64, because the cut now reaches into the high mode and removes true synapses with moderate scores. The preferred value is 64, placed at the trough with the histogram shown, and 96 is reported as a sensitivity run. A learner who prefers 96 for a motif analysis, where false positives do the most damage, is also right, as long as the reason is written down.

**The decision-log entry.** What: cleft-score threshold at 64. Why: the trough of a bimodal score distribution, separating a low mode concentrated on debris from a high mode of plausible synapses. Parameters: score >= 64 on the 0 to 255 scale, applied after duplicate removal, endpoint validation and autapse removal. Impact: 29,589 rows to 24,274; 2,231 directed edges among 407 neurons. Risk: true synapses with scores in the low mode are lost, and the size of that loss is not known from this table alone.

**The sensitivity statement.** Moving the threshold 20% either way changes the edge count by a few percent: 2,284 edges at 51 (+2.4%), 2,165 at 77 (-3.0%). A conclusion that survives that range does not depend on the exact number; one that flips inside it is a conclusion about the threshold.

**What this example does not establish.** That 64 is right for any other table. A threshold does not transfer between synapse tables with different score scales or detectors. The method transfers: integrity first, histogram second, a value at the trough, and a sensitivity run on either side of it.

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
{: #studio-activity}

**Scenario:** Your team receives a connectomics export from a fictional mouse cortex volume, release T18, containing: a synapse table (4.2 million rows) with confidence scores, a segment table (120,000 segments) with volumes, and a cell-type annotation table (8,400 classified neurons). Initial inspection reveals: 12% of synapses have confidence scores below 30, 35,000 segments have fewer than 2 synapses, 847 segments intersect the volume bounding box, and 23 segment IDs appear in the synapse table but not in the segment table. The volume, the release and every number here are synthetic, invented for this exercise; none describes a real dataset.

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

## Common errors and how to recover

- **You applied a threshold from another dataset's documentation.** Score scales and detectors differ, so the number means nothing here. Recover by plotting this table's score histogram, placing the cut at its trough, and reporting the histogram with the threshold.
- **Cleaning removed one cell type faster than the others.** Recover by tabulating retention per cell type. If any type sits more than a few points from the overall rate, flag rather than drop, and report the composition change; uneven loss changes the population being studied.
- **Duplicate synapse rows reached the graph.** Deduplicating on the synapse ID alone misses rows that repeat with a new ID. Recover by deduplicating on the full row, reporting the count removed, and adding a zero-duplicates gate.
- **Synapse endpoints are missing from the segment table.** The two tables came from different materializations. Recover by stopping, re-querying both at one version, and treating a nonzero count of unmatched endpoints as a gate failure, not a row to drop.
- **The decision log was written after the analysis and has no row counts.** Recover by rerunning the pipeline with logging on, so every step emits its before and after counts, and replacing the reconstructed log with the emitted one.
- **Boundary neurons were dropped, and a degree-by-position analysis followed.** Recover by flagging instead of dropping, keeping the flag in the released table, and stating that flagged degrees are underestimates; compare degree by position only after excluding the flagged cells and saying so.
- **The QC dashboard is full and nobody acted on it.** Recover by attaching a gate and an action to every metric. A metric that has neither is removed from the dashboard, because it was monitoring, not control.

## What this module does not cover

- **The upstream pipeline that produces the artifacts.** Segmentation, synapse detection and their error rates are [Module 14]({{ '/modules/module14/' | relative_url }}), [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}) and the [reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) page. This module cleans the tables those produce.
- **Proofreading.** Correcting merges and splits in the segmentation itself is [Module 07]({{ '/modules/module07/' | relative_url }}); a cleaning step never repairs a segmentation error, it only decides how to treat its trace in the table.
- **Imaging artifacts in the raw EM.** Folds, section loss and staining defects are [Technical Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}) and the [artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}); here they appear only as their downstream effects on tables.
- **Inference on the cleaned graph.** Null models, multiplicity and threshold sensitivity as a statistical question are [Module 20]({{ '/modules/module20/' | relative_url }}).
- **The release itself.** FAIR packaging, identifiers and the clean-room rerun are [Module 21]({{ '/modules/module21/' | relative_url }}); the release note written here is its input.
- **Storage and query cost.** Sizing tables and pinning materializations at scale are [Module 12]({{ '/modules/module12/' | relative_url }}).

## Content library cross-references
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}) --- the graph structures that preprocessing feeds into, and how cleaning decisions affect them.
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) --- the infrastructure for tracking dataset versions, materializations, and transform lineage.
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) --- understanding the upstream pipeline (imaging, alignment, segmentation, synapse detection) that produces the artifacts preprocessing must address.

## Teaching resources
- Lesson context: [Volume Reconstruction Infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
- QC context: [Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
- Slides: [Infrastructure lecture plan]({{ '/technical-training/slides/04-volume-reconstruction-infrastructure/' | relative_url }})
- Practice dataset workflow: [Workflow overview]({{ '/datasets/workflow/' | relative_url }})
- Quality framework: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})
- [Module 18 kit]({{ '/assets/kits/module18/README.md' | relative_url }}) — a synthetic noisy export and the QC dashboard template

## Time budget
The declared 4 to 5 hours are: about 30 minutes reading the concept set beforehand, a 90-minute meeting (the 60-minute run-of-show below plus the opening of the studio activity), and 2 to 3 hours outside class finishing the studio release note, the quick practice prompt, and the linked readings. Neither [syllabus map]({{ '/teaching/syllabi/' | relative_url }}) schedules this kit; the 16-week map leaves Kits 12 to 16 and 18 out for time, so run it as a lab meeting or a take-home between the proofreading work of Technical Unit 08 and the inference work of Module 20.

## 60-minute tutorial run-of-show

### Materials
- One noisy connectomics table (synapse table with low-confidence entries, duplicate IDs, and missing cell-type labels): `noisy_synapses.csv` and `cell_types.csv` in the [Module 18 kit]({{ '/assets/kits/module18/README.md' | relative_url }}), a synthetic stand-in of about 30,000 rows.
- Segment table with size distribution spanning 5 orders of magnitude: `segments.csv` in the kit.
- Shared preprocessing decision sheet (printed or digital template), with the studio's columns: issue, policy, threshold, rationale, impact.
- QC dashboard template (pre/post metric comparison), in the kit README.

### Timing and instructor script

**00:00-08:00 | Setup and target framing**
Instructor presents the scenario: "You have received a connectomics export. Before you can analyze it, you must clean it. But every cleaning decision changes your results. Today we learn to clean responsibly." Display the raw data summary statistics. Define the release objective: an analysis-ready synapse table and neuron table with documented provenance. Define non-negotiable quality gates: no duplicate IDs, no unresolved foreign keys, all thresholds documented.

**08:00-18:00 | Instructor modeling: ingest and anomaly screening**
Live demonstration: load the synapse table, compute the confidence score distribution, identify the bimodal peak (true synapses vs false positives). Show the segment size distribution on a log scale, point out the debris tail. Check for orphan IDs. Key script line: "Before you touch the data, understand its shape. The distribution plot is your first diagnostic tool."

**18:00-32:00 | Team preprocessing design**
Teams of 3-4 draft cleaning rules for each identified issue. Each team must produce a preprocessing decision table with columns: issue, proposed action, threshold, rationale, estimated impact. Instructor circulates, challenging threshold choices: "Why 50 and not 40? What do you lose at 50 that you keep at 40?"

**32:00-44:00 | QC pass**
Teams compute (or estimate from the distributions in the kit) pre/post metrics: total synapse count, total segment count, mean synapses per neuron, fraction of each cell type remaining. Teams make a release/no-release decision based on their quality gates. Instructor asks: "Did cleaning change the relative representation of cell types? If it did, that is a bias you must report."

**44:00-54:00 | Cross-team review**
Teams swap preprocessing decision tables and QC reports. Each team audits the other's transform log for: missing rationale, unjustified thresholds, potential biological signal loss, and reproducibility gaps. Teams write two specific improvement suggestions.

**54:00-60:00 | Competency checkpoint**
Each team submits one release note with: dataset version, all thresholds and parameters, QC metrics with pass/fail, and at least one documented residual risk. Instructor reviews one example live.

### Success criteria for this session
- Cleaning decisions are deterministic, justified, and documented in real time.
- QC thresholds are tied to operational actions (not just reported).
- Release note exposes at least one unresolved interpretation risk.

## Evidence anchors from connectomics practice

### Key datasets to practice on
- [NeuroTrailblazers workflow overview]({{ '/datasets/workflow/' | relative_url }})
- [MouseConnects (HI-MC)]({{ '/datasets/mouseconnects/' | relative_url }})
- [MICrONS Explorer](https://www.microns-explorer.org/)

### Competency checks
- Can you trace every preprocessing transform from input version to release artifact?
- Can you justify your QC thresholds and explain their operational consequences?
- Can you state one unresolved data-risk that could still affect downstream interpretation?
- Can you explain what biological signal might have been lost at each filtering step?
- If you changed your synapse confidence threshold by 10 points, would your main conclusion still hold?

## Academic references
- Wilkinson MD et al. (2016) "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data* 3:160018. doi:10.1038/sdata.2016.18. The metadata standard the release package is written to.
- Peng RD (2011) "Reproducible research in computational science." *Science* 334(6060):1226-1227. doi:10.1126/science.1213847. The reproducibility spectrum: why a decision log with code and data beats a description of the method.
- Dorkenwald S et al. (2025) "CAVE: Connectome Annotation Versioning Engine." *Nature Methods* 22(5):1112-1120. doi:10.1038/s41592-024-02426-z. Materialization versions, which is why the ingest step checks that every table comes from the same one.
- The MICrONS Consortium (2025) "Functional connectomics spanning multiple areas of mouse visual cortex." *Nature* 640(8058):435-447. doi:10.1038/s41586-025-08790-w. Reports synapse-detection precision of 96% and recall of 89%, the kind of number a confidence-threshold decision has to be read against.
- Januszewski M et al. (2018) "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods* 15(8):605-610. doi:10.1038/s41592-018-0049-4. Where merges and splits come from, so that the debris tail and the oversized segments in Concept 1 have a cause.

## Quick practice prompt
Take one connectomics table (real or mock) and write:
1. Three cleaning rules with rationale tied to specific data artifacts.
2. Two QC thresholds with associated pass/fail actions and biological justification.
3. One sensitivity analysis: what happens to your key metric if you relax or tighten your primary threshold by 20%?
4. One limitation that remains after preprocessing, stated concretely enough to guide interpretation.
