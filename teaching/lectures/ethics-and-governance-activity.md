---
layout: page
title: "Ethics and Governance: learner worksheet"
permalink: /teaching/lectures/ethics-and-governance-activity/
slug: ethics-and-governance-activity
content_type: delivery
description: "Audit licenses, human-tissue questions and proofreading credit for an invented data release."
---

[Lecture and slides]({{ '/teaching/lectures/ethics-and-governance/' | relative_url }}) · [Four-session block]({{ '/teaching/sequence/' | relative_url }})

**34 minutes plus peer review.** Work in pairs. The team, project, startup and
contributors below are **invented**. The dataset licenses are real and are stated on
slide 16 and the [reference page]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}).
This is a planning exercise, not legal advice.

## The hypothetical scenario

A small, invented lab group plans a public release in six months. It has three parts:

- **A. Derived tables:** cleaned edge lists and per-cell summary tables computed from
  MICrONS, H01, the FlyWire public release (v783) and the hemibrain v1.0 deposit.
- **B. A connectivity-constrained model** built from FlyWire and hemibrain tables.
  An invented startup has asked to license it for a paid product.
- **C. A segmentation model** trained on H01 and MICrONS imagery, released openly.

A draft README lists the H01 donor's age, sex, procedure, hospital and surgery year
“for completeness.” Twelve people proofread for the project: two postdocs, one
graduate student, six undergraduates in a course and three outside volunteers.

## 1. License and terms audit (10 minutes)

Copy and complete this table for each dataset: MICrONS, H01, FlyWire v783, hemibrain.

| Dataset | Data license and where stated | May part A redistribute it? | May the startup use part B? | What must the release include? |
|---|---|---|---|---|

Which instrument governs a figure copied from the FlyWire *Nature* paper? The hemibrain
sources disagree. Mark that row **unresolved** and write what you would do before
release. Do not choose a license by guesswork.

## 2. Human tissue before reuse (8 minutes)

Answer briefly. Where is H01's consent and approval information, and how will you
record where you found it? Can an EM volume imaged at 4 nm pixels identify the donor? Which README
fields would you remove, and what would a reuser lose? Does consent to “research use”
clearly extend to part C's model training? Who would you ask? Rewrite this sentence
from the draft paper: “Our model learns how the human cortex is organized.”

## 3. Credit plan for proofreaders (8 minutes)

Choose one of the four credit models on slide 25 for the twelve contributors, or a
stated combination. Which CRediT role will you map proofreading onto, given that
CRediT has no proofreading term? Write the authorship threshold, how effort will be
measured and when contributors are told. Say what the volunteers lose under your rule.

## 4. A governance note (8 minutes)

Draft a data-use statement of no more than 150 words for the release README. Include
source licenses and versions, required citations, the commercial-use position of each
part, the human-tissue provenance and its limits, and one open question for the
institution's compliance office.

**Peer review:** exchange notes. Check whether a reader could tell which license
governs each part, whether any uncertainty was written as a settled fact, and whether
the credit rule is dated before the work.

**Exit ticket:** “One obligation this team must meet is ___; one question it cannot
settle alone is ___, and it would ask ___.”

**Success criteria:** data and article licenses are distinguished; the hemibrain
conflict is recorded with both sources and handled under the more restrictive terms; human-tissue claims name the single donor; the
credit rule is written before the work and names what each contributor loses.

**Carry forward (optional, 3 minutes):** if you have a study brief from the four-session
block, add your dataset's data license and version, where its ethics statement is
(for human tissue) and how its proofreaders were credited.

[Instructor model answers]({{ '/teaching/lectures/ethics-and-governance-answers/' | relative_url }})
are public. Attempt the worksheet first. Teaching activity: CC BY-SA 4.0, NeuroTrailblazers.
