---
marp: true
theme: default
paginate: true
title: "Module 18: Data Cleaning and Preprocessing"
---

# Module 18: Data Cleaning and Preprocessing
Teaching Deck

---

## Learning Objectives
- Diagnose common connectomics data-quality issues before analysis
- Apply reproducible preprocessing steps with documented decision rules
- Quantify preprocessing impact with auditable QC metrics
- Produce an analysis-ready dataset package with provenance metadata

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
Produce a reproducible preprocessing release that transforms raw or intermediate connectomics outputs into analysis-ready data, with explicit quality gates and full provenance. Students will be able to identify the specific cleaning operations that shape biological conclusions, justify every threshold decision, and document their preprocessing pipeline so that another researcher can audit and reproduce it.

---

## Concept Focus
### 1) Data cleaning in connectomics: what needs fixing and why
- **Technical:** connectomics datasets arrive with characteristic quality issues that must be addressed before analysis:
  - **Synapse table filtering:** automated synapse detection produces false positives (cleft detections at non-synaptic locations) and false negatives (missed synapses). Filtering typically uses a confidence score threshold (e.g., cleft score > 50 in CAVE synapse tables). The choice of threshold directly affects edge weights in the connectivity graph.
  - **Segment size thresholding:** automated segmentation produces many small fragments --- bits of neuropil, partial dendrites, glia misclassified as neurons. Including these in analysis adds noise. Common practice is to exclude segments below a volume or synapse count threshold (e.g., segments with fewer than 2 synapses as pre- or post-synaptic partner).
  - **Removing orphan fragments:** segments that have no synaptic connections to any other segment are orphans. They typically represent segmentation debris or incomplete reconstructions. Including them inflates node counts and distorts network metrics.
  - **Handling neurons at volume boundaries:** neurons whose arbors are truncated by the edge of the imaged volume have artificially low synapse counts and incomplete morphologies. These boundary neurons can be flagged (e.g., by checking whether the segment mesh intersects the volume bounding box) and either excluded or analyzed with explicit caveats.
  - **Duplicate and conflicting IDs:** merges and splits during proofreading can create duplicate entries or conflicting segment-to-cell-type mappings that must be resolved.
- **Plain language:** connectomics data is not "clean" when you receive it. Segmentation makes mistakes, synapse detection has false alarms, and the edges of the volume cut through neurons. You must fix these issues before analysis, but every fix is a decision that affects your results.
- **Misconception guardrail:** "raw data is always better." In connectomics, raw segmentation output contains systematic artifacts that will corrupt analysis if left uncleaned. The question is not whether to clean, but how to clean transparently.

---

## Core Workflow
- **Ingest and integrity validation**
- Confirm file completeness, schema conformance, and version compatibility.
- Log dataset identifiers, CAVE materialization version, and checksums.
- Verify that the synapse table, segment table, and cell-type annotations refer to the same materialization.
- **Artifact and anomaly screening**
- Compute segment size distribution and flag outliers (extremely large segments may be merge errors; extremely small segments may be debris).
- Compute synapse confidence score distribution and identify the threshold region.
- Check for duplicate segment IDs, conflicting cell-type labels, and missing foreign keys.
- Identify boundary neurons by mesh-bounding-box intersection.
- Triage issues by likely biological impact: high-impact issues block analysis; low-impact issues are documented and accepted.
- **Cleaning transforms**
- Apply synapse confidence threshold with documented rationale.
- Remove orphan segments (zero synapses as both pre and post).
- Apply segment size threshold with documented rationale.
- Flag or remove boundary neurons with documented policy.
- Resolve duplicate IDs and label conflicts.
- Normalize units (e.g., convert voxel coordinates to nanometers using dataset resolution metadata).
- **QC and drift checks**
- Compare pre/post distributions: synapse count per neuron, segment size, graph density, degree distribution.
- Verify that cleaning did not selectively remove a specific cell type or spatial region.
- Check that graph topology statistics (clustering coefficient, connected components) are consistent with expectations.
- **Release packaging**
- Publish analysis-ready tables plus: preprocessing decision log, transform code with commit hash, QC metric report with threshold justifications, known limitations and residual risks.

---

## 60-Minute Run-of-Show
- One noisy connectomics table (synapse table with low-confidence entries, duplicate IDs, and missing cell-type labels).
- Segment table with size distribution spanning 5 orders of magnitude.
- Shared preprocessing decision sheet (printed or digital template).
- QC dashboard template (pre/post metric comparison).
- Cleaning decisions are deterministic, justified, and documented in real time.
- QC thresholds are tied to operational actions (not just reported).
- Release note exposes at least one unresolved interpretation risk.

---

## Misconceptions to Watch
- **Misconception guardrail:** "raw data is always better." In connectomics, raw segmentation output contains systematic artifacts that will corrupt analysis if left uncleaned. The question is not whether to clean, but how to clean transparently.
- **Misconception guardrail:** there is no single "correct" threshold. If your result depends on a specific threshold choice, it is fragile and should be reported with a sensitivity analysis.
- **Misconception guardrail:** more filtering is not always better. Aggressive cleaning can create the appearance of clean results while actually removing biological signal.
- **Misconception guardrail:** version-control notes alone are insufficient without data lineage. Git tracks code changes, but you also need to track which data version was processed with which code version.
- **Misconception guardrail:** documenting preprocessing after the fact is unreliable. Document decisions in real time.
- **Misconception guardrail:** reporting metrics without thresholds is not quality control. Every metric needs an associated action.

---

## Studio Activity
{: #studio-activity}

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
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

---

## Exit Ticket
Take one connectomics table (real or mock) and write:
1. Three cleaning rules with rationale tied to specific data artifacts.
2. Two QC thresholds with associated pass/fail actions and biological justification.
3. One sensitivity analysis: what happens to your key metric if you relax or tighten your primary threshold by 20%?
4. One limitation that remains after preprocessing, stated concretely enough to guide interpretation.

---

## References (Instructor)
- Wilkinson et al., 2016. The FAIR Guiding Principles for scientific data management and stewardship.
- Peng, 2011. Reproducible Research in Computational Science.
- MICrONS and related connectomics workflow documentation.

---

## Teaching Materials
- Module page: /modules/module18/
- Slide page: /modules/slides/module18/
- Worksheet: /assets/worksheets/module18/module18-activity.md
