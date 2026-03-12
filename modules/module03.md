---
title: "Module 03: Python and Jupyter for Neuroscience"
layout: module
permalink: /modules/module03/
description: "Build practical Python/Jupyter skills for reproducible connectomics data exploration."
module_number: 3
difficulty: "Beginner to Intermediate"
duration: "4 hours"
learning_objectives:
  - "Set up a reproducible notebook workflow"
  - "Load and inspect connectomics data tables"
  - "Write basic analysis and visualization code blocks"
  - "Document assumptions and outputs for reuse"
prerequisites: "Modules 01-02"
merit_stage: "Foundations"
compass_skills:
  - "Programming"
  - "Data Handling"
  - "Reproducible Practice"
ccr_focus:
  - "Skills - Computational Foundations"
  - "Meta-Learning - Debugging"

# Normalized metadata
slug: "module03"
short_title: "Python and Jupyter for Neuroscience"
status: "active"
audience:
  - "students"
pipeline_stage: "Foundations"
merit_row_focus: "Foundations"
topics:
  - "python"
  - "jupyter"
  - "reproducibility"
summary: "Develop notebook-based analysis habits for connectomics datasets with explicit reproducibility discipline."
key_questions:
  - "How do we structure notebooks for reuse?"
  - "What metadata should accompany outputs?"
slides: []
notebook: []
datasets:
  - "/datasets/access"
  - "/datasets/workflow"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/ask-an-expert/"
related_frameworks:
  - "education-models"
prerequisites_list: []
next_modules:
  - "module04"
references: []
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Create a reproducible Jupyter notebook that ingests a connectomics dataset slice, performs one analysis, and exports documented outputs.

## Core concepts
- Notebook as executable lab notebook.
- Deterministic environments and version pinning.
- Readable code and explicit assumptions.

## Core workflow
1. Set environment and dependencies.
2. Load dataset and validate schema.
3. Run analysis cell sequence.
4. Save outputs + metadata.
5. Re-run from clean kernel.

## 60-minute tutorial run-of-show
1. 00:00-08: notebook anatomy.
2. 08:00-20: setup and loading.
3. 20:00-34: analysis coding sprint.
4. 34:00-46: plotting and export.
5. 46:00-56: clean rerun test.
6. 56:00-60: competency check.

## Studio activity
Build a mini notebook with one descriptive statistic and one plot from a sample connectomics table.

## Assessment rubric
- Minimum: runnable notebook, clear outputs, basic metadata.
- Strong: clean structure, robust error handling, repeatable rerun.
- Failure: hidden state dependencies, undocumented assumptions.

## Teaching resources
- [Dataset Access]({{ '/datasets/access/' | relative_url }})
- [Workflow]({{ '/datasets/workflow' | relative_url }})

## Quick practice prompt
Add one markdown cell documenting input version, processing steps, and output files.
