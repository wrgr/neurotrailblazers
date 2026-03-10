---
title: "Module 08: Hypothesis Testing in Connectomics"
layout: module
permalink: /modules/module08/
description: "Learn how to generate and test scientific hypotheses using circuit-level data from EM volumes."
module_number: 8
difficulty: "Intermediate"
duration: "3-4 hours"

# Normalized metadata (pilot)
slug: "module08"
short_title: "Hypothesis Testing in Connectomics"
status: "active"
audience:
  - "students"
pipeline_stage: "Experiment"
merit_row_focus: "Experiment"
topics:
  - "hypothesis-testing"
  - "statistics"
  - "connectomics"
summary: "Defining and testing hypotheses using statistical tools in connectomics."
learning_objectives:
  - "Define and identify testable hypotheses in connectomics"
  - "Apply statistical methods to compare neural features"
  - "Design experiments to validate hypotheses using segmented data"
  - "Critically interpret analysis results"
key_questions: []
slides: []
notebook: []
datasets:
  - mouseconnects
  - workflow
personas:
  - gradstudent
  - researcher
  - mentor
related_tools:
  - connectome-quality
  - ask-an-expert
related_frameworks:
  - research-incubator-model
  - education-models
prerequisites:
  - "Modules 1-7"
  - "Basic statistics"
next_modules:
  - module09
  - module10
references: []
videos: []
downloads: []
last_reviewed: 2026-03-09
maintainer: "NeuroTrailblazers Team"
merit_stage: "Analysis"
compass_skills:
  - "Scientific Reasoning"
  - "Experimental Design"
  - "Critical Thinking"
ccr_focus:
  - "Knowledge - Scientific Inquiry"
  - "Skills - Statistical Analysis"
---

<div class="main-content">
  <div class="hero">
    <div class="hero-content">
      <h1>{{ page.title }}</h1>
      <p class="hero-subtitle">{{ page.description }}</p>
    </div>
  </div>

  <div class="cards-grid module-cards">
<div class="card module-card">
    <h2>🔬 Scientific Hypotheses in Circuit Neuroscience</h2>
    <p>Hypothesis testing is the foundation of experimental science. In connectomics, hypotheses may concern the structure, function, or variability of brain circuits. These must be formalized in ways that support measurement and comparison.</p>
    <ul>
      <li>What makes a hypothesis testable?</li>
      <li>Generating predictions from data models</li>
      <li>Null vs. alternative hypotheses</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>📊 Statistical Tools</h2>
    <p>Proper testing requires selecting appropriate methods based on sample size, distribution, and effect size. Familiarity with statistical tests is key to avoiding false positives or negatives.</p>
    <ul>
      <li>t-tests, ANOVA, and non-parametric alternatives</li>
      <li>Multiple comparisons and correction</li>
      <li>Visualizing distributions and error bars</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>🔍 Hypothesis-Driven Experiments</h2>
    <p>Analysis should be guided by the scientific question, not just exploratory metrics. This section emphasizes how to match your analysis pipeline to your hypothesis.</p>
    <ul>
      <li>Operationalizing hypotheses in code</li>
      <li>Power analysis and sample size estimation</li>
      <li>Reporting significance and effect size</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>🌟 COMPASS Integration</h2>
    <ul>
      <li><strong>Knowledge:</strong> Hypothesis formulation and statistical testing</li>
      <li><strong>Skills:</strong> Experimental design, statistical computation, error estimation</li>
      <li><strong>Character:</strong> Scientific integrity, curiosity, patience</li>
      <li><strong>Meta-Learning:</strong> Reflecting on analysis limitations and next steps</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>📚 References & Resources</h2>
    <ul>
      <li>Ghasemi & Zahediasl, 2012. <em>Normality tests for statistical analysis: A guide for non-statisticians</em>. Int J Endocrinol Metab.</li>
      <li>Field et al., 2012. <em>Discovering Statistics Using R</em>. Sage.</li>
      <li>Colab: "Statistical Tests in Python with SciPy"</li>
      <li><a href="https://bossdb.org">BossDB</a> Cookbook: <a href="https://github.com/aplbrain/bossdb_cookbook/blob/main/notebooks/Accessing-Lower-Resolution-Versions-Of-Data-From-BossDB.ipynb">Accessing Lower Resolution Data</a></li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>✅ Assessment</h2>
    <ul>
      <li>Identify a testable hypothesis from a neural network dataset</li>
      <li>Use Python to perform a statistical test (e.g. t-test) and interpret the result</li>
      <li>Explain the significance and limitations of the findings</li>
    </ul>
  </div>
</div>
</div>
