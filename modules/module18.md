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
Produce a reproducible preprocessing release that transforms raw or intermediate connectomics outputs into analysis-ready data, with explicit quality gates and full provenance.

## Why this module matters
Most downstream failures in connectome analysis are not model failures first; they are data-quality and preprocessing failures. This module teaches how to clean data without erasing signal, and how to document each transformation so conclusions remain defensible.

## Concept set
### 1) Cleaning vs distortion
- **Technical:** preprocessing should reduce known artifacts/noise while preserving biologically meaningful structure.
- **Plain language:** fix mistakes, do not "polish away" the biology.
- **Misconception guardrail:** more filtering is not always better.

### 2) Provenance as a scientific requirement
- **Technical:** every transform should be traceable (input version, parameters, timestamp, owner, output hash).
- **Plain language:** if you cannot explain how the file was made, you cannot trust the result.
- **Misconception guardrail:** version-control notes alone are insufficient without data lineage.

### 3) QC metrics must be decision-linked
- **Technical:** metrics (missingness, merge/split rates, consistency checks) should trigger concrete accept/rework decisions.
- **Plain language:** a dashboard is useful only if it changes what you do.
- **Misconception guardrail:** reporting metrics without thresholds is not quality control.

## Core workflow: preprocessing for connectomics
1. **Ingest and integrity validation**
   - Confirm file completeness, schema conformance, and version compatibility.
   - Log dataset identifiers and checksums.
2. **Artifact and anomaly screening**
   - Identify missing values, label conflicts, geometric outliers, and suspicious connectivity spikes.
   - Triage issues by likely biological impact.
3. **Cleaning transforms**
   - Apply deterministic corrections (schema normalization, unit harmonization, explicit missing-value policy).
   - Isolate heuristic transforms for extra review.
4. **QC and drift checks**
   - Compare pre/post distributions and topology statistics.
   - Verify no unacceptable biological-signal loss.
5. **Release packaging**
   - Publish analysis-ready tables/volumes plus transform log, metric report, and known limitations.

## Studio activity: preprocessing release simulation
**Scenario:** Your team receives a mixed-quality connectomics export with missing labels, duplicated IDs, and inconsistent units.

**Tasks**
1. Define cleaning policy for each issue category.
2. Implement a preprocessing pipeline (pseudocode or notebook-level steps).
3. Run pre/post QC metrics and justify any tradeoffs.
4. Produce a release note that includes lineage metadata and known residual risks.

**Expected outputs**
- Preprocessing decision table.
- QC metric summary with thresholds and pass/fail calls.
- Release note (inputs, transforms, outputs, limitations).

## Assessment rubric
- **Minimum pass**
  - Cleaning decisions are explicit and reproducible.
  - QC metrics include thresholds tied to actions.
  - Release package includes provenance metadata.
- **Strong performance**
  - Distinguishes low-risk cleanup from biologically sensitive transforms.
  - Quantifies and explains pre/post changes clearly.
  - Documents limitations and unresolved risks transparently.
- **Common failure modes**
  - Silent ad-hoc edits with no transform log.
  - Aggressive filtering that removes biologically meaningful variation.
  - Metrics reported without operational thresholds.

## Teaching resources
- Lesson context: [Volume Reconstruction Infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
- QC context: [Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
- Slides: [Infrastructure deck draft]({{ '/technical-training/slides/04-volume-reconstruction-infrastructure/' | relative_url }})
- Practice dataset workflow: [Workflow overview]({{ '/datasets/workflow' | relative_url }})
- Quality framework: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## Quick practice prompt
Take one connectomics table (real or mock) and write:
1. Three cleaning rules with rationale.
2. Two QC thresholds and associated actions.
3. One limitation that remains after preprocessing.
