---

title: "Module 06: Hypothesis Testing in Connectomics"
layout: module
permalink: /modules/module06/
description: "Learn how to formulate, test, and refine scientific hypotheses using nanoscale brain circuit data."
module_number: 6
difficulty: "Intermediate"
duration: "3-4 hours"
learning_objectives:

- "Formulate testable scientific questions based on circuit data"
- "Design a simple experimental plan using connectomics resources"
- "Differentiate between correlation and causation in structural data"
- "Understand limitations and ethical considerations in EM-based research"
prerequisites: "Modules 1-5, or background in neuroscience methods"
merit_stage: "Scientific Question / Experiment"
compass_skills: ["Analytical Thinking", "Curiosity", "Scientific Reasoning"]
ccr_focus: ["Knowledge - Scientific Method", "Character - Integrity"]

# Normalized metadata
slug: "module06"
short_title: "Segmentation 101"
status: "active"
audience:
  - "students"
pipeline_stage: "Question"
merit_row_focus: "Question"
topics:
  - "hypothesis-design"
  - "connectomics-experiments"
summary: "Understanding segmentation, labels, sources of error, and how to formulate and test questions with connectomics data."
key_questions: []
slides: []
notebook: []
datasets:
  - mouseconnects
personas:
  - gradstudent
  - researcher
related_tools:
  - connectome-quality
  - ask-an-expert
related_frameworks:
  - research-incubator-model
  - education-models
prerequisites_list: []
next_modules:
  - module07
  - module08
references: []
videos: []
downloads: []
last_reviewed: 2026-03-09
maintainer: "NeuroTrailblazers Team"
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
    <h2>🧠 From Curiosity to Question</h2>
    <p>Every scientific journey begins with a question. In connectomics, questions might concern the structure, connectivity, or variability of specific neural circuits. This module guides you through crafting meaningful and testable hypotheses.</p>
    <ul>
      <li>Observations from EM volumes</li>
      <li>Generating hypotheses from structure</li>
      <li>Choosing appropriate controls and comparisons</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>🔬 Designing Connectomic Experiments</h2>
    <p>Using large datasets like MICrONS or FlyWire, researchers can simulate experiments by analyzing connectivity motifs, synapse distributions, or circuit asymmetries. Experimental design involves framing a hypothesis, defining metrics, and selecting analysis techniques.</p>
    <ul>
      <li>Using existing data to ask new questions</li>
      <li>Metrics: synapse counts, partner diversity, path length</li>
      <li>Tools for analysis: Python, Neuroglancer, Jupyter</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>⚖️ Pitfalls and Ethics</h2>
    <p>Interpretation of structural data comes with challenges. Structure alone doesn’t reveal function. Hypothesis-driven work in connectomics must acknowledge these limits—and be grounded in ethical research practices.</p>
    <ul>
      <li>Limitations of inference from anatomy</li>
      <li>Responsible data use and attribution</li>
      <li>Working with animal and human brain data</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>🎯 COMPASS Integration</h2>
    <ul>
      <li><strong>Knowledge:</strong> Framing scientific questions in a connectomic context</li>
      <li><strong>Skills:</strong> Designing structured inquiry and controlled comparisons</li>
      <li><strong>Character:</strong> Scientific honesty and rigor</li>
      <li><strong>Meta-Learning:</strong> Learning from failed or ambiguous results</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>📚 References & Resources</h2>
    <ul>
      <li>Helmstaedter et al., 2013. <em>Connectomic reconstruction of the inner plexiform layer in the mouse retina</em>. Nature.</li>
      <li>FlyWire Tutorials: <a href="https://flywire.ai">flywire.ai</a></li>
      <li>Open Source Analysis: <a href="https://microns-explorer.org">microns-explorer.org</a></li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>✅ Assessment</h2>
    <ul>
      <li>Write a testable hypothesis based on a sample EM volume</li>
      <li>Describe a potential comparison or control</li>
      <li>Explain a challenge in interpreting structural findings</li>
    </ul>
  </div>
</div>
</div>
