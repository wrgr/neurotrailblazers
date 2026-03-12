---
title: "Module 09: Neuron Morphology and Skeletonization"
layout: module
permalink: /modules/module09/
description: "Extract and interpret morphology and skeleton features to support connectomics analysis and cell-type reasoning."
module_number: 9
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Generate skeleton representations from reconstructed neurites"
  - "Compute core morphology descriptors"
  - "Relate morphology metrics to biological interpretation"
  - "Report morphology uncertainty and classification limits"
prerequisites: "Modules 01-08"
merit_stage: "Experiment"
compass_skills:
  - "Morphological Analysis"
  - "Feature Extraction"
  - "Interpretive Reporting"
ccr_focus:
  - "Skills - Morphometrics"
  - "Knowledge - Neuronal Structure"

# Normalized metadata
slug: "module09"
short_title: "Neuron Morphology & Skeletonization"
status: "active"
audience:
  - "students"
pipeline_stage: "Experiment"
merit_row_focus: "Experiment"
topics:
  - "morphology"
  - "skeletonization"
summary: "Extract and interpret neurite morphology features with uncertainty-aware reporting."
key_questions:
  - "Which morphology features are robust across reconstructions?"
  - "How should skeleton uncertainty be communicated?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow"
personas:
  - "/avatars/gradstudent"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
prerequisites_list: []
next_modules:
  - "module10"
references: []
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Produce a skeleton-based morphology summary with at least three descriptors and one explicit limitation.

## Core workflow
1. Build skeleton from reconstruction.
2. Compute descriptors (path length, branching, etc.).
3. Compare against reference patterns.
4. Report interpretation confidence.

## 60-minute tutorial run-of-show
1. 00:00-10: morphology overview.
2. 10:00-24: skeleton extraction demo.
3. 24:00-38: descriptor calculation.
4. 38:00-50: interpretation and caveats.
5. 50:00-60: competency check.

## Studio activity
Extract one skeleton and submit a morphology descriptor table with interpretation notes.

## Assessment rubric
- Minimum: valid skeleton and descriptor set.
- Strong: robust interpretation with uncertainty framing.
- Failure: descriptor list without biological context.

## Teaching resources
- [Technical Unit 05]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }})
- [Technical Unit 06]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }})

## Quick practice prompt
Explain one morphology feature that could be confounded by reconstruction quality.
