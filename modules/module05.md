---
title: "Module 05: Electron Microscopy and Image Basics"
layout: module
permalink: /modules/module05/
description: "Understand EM image formation, artifacts, and interpretation basics for reliable connectomics analysis."
module_number: 5
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Describe core EM acquisition concepts relevant to connectomics"
  - "Identify common image artifacts and likely downstream impact"
  - "Interpret image quality for segmentation readiness"
  - "Document uncertainty and QA decisions"
prerequisites: "Modules 01-04"
merit_stage: "Foundations"
compass_skills:
  - "Imaging Literacy"
  - "Quality Assessment"
  - "Interpretive Discipline"
ccr_focus:
  - "Knowledge - EM Foundations"
  - "Skills - QA Screening"

# Normalized metadata
slug: "module05"
short_title: "Electron Microscopy and Image Basics"
status: "active"
audience:
  - "students"
pipeline_stage: "Foundations"
merit_row_focus: "Foundations"
topics:
  - "em"
  - "image-quality"
  - "artifacts"
summary: "Foundational EM image interpretation and artifact-aware quality control for connectomics workflows."
key_questions:
  - "Which artifacts critically affect reconstruction quality?"
  - "What minimum image quality supports downstream segmentation?"
slides:
  - "/assets/slides/module05/module05-electron-microscopy-and-image-basics.pdf"
notebook:
  - "/assets/notebooks/module05/module05-electron-microscopy-and-image-basics.ipynb"
datasets:
  - "/datasets/workflow"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
prerequisites_list: []
next_modules:
  - "module06"
  - "module07"
references: []
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Evaluate EM image patches for artifact risk and issue a justified pass/rework recommendation.

## Concept set
- Image quality as a scientific constraint.
- Artifact taxonomy linked to downstream error.
- QA gates and escalation logic.

## Core workflow
1. Inspect image quality and artifact signatures.
2. Classify severity and likely impact.
3. Decide pass/rework with rationale.
4. Log findings for reproducibility.

## 60-minute tutorial run-of-show
1. 00:00-08: EM basics refresher.
2. 08:00-20: artifact recognition walkthrough.
3. 20:00-34: learner triage round.
4. 34:00-46: QA threshold debate.
5. 46:00-56: decision logging practice.
6. 56:00-60: competency check.

## Studio activity
Classify 6 patches by artifact type/severity and propose action.

## Assessment rubric
- Minimum: accurate major artifact calls + action decision.
- Strong: clear impact reasoning and consistent thresholds.
- Failure: artifact labels without downstream implications.

## Teaching resources
- [Technical Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## Quick practice prompt
Pick one artifact and explain how it could create a merge or split error later.
