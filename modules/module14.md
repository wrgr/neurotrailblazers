---

title: "Module 14: Neuron Classification and Morphology"
layout: module
permalink: /modules/module14/
description: "Learn how to identify neuron types using structural, morphological, and connectivity features in EM datasets."
module_number: 14
difficulty: "Intermediate"
duration: "3 hours"
learning_objectives:

- "Classify neurons based on morphology and known anatomical features"
- "Use tools to compute quantitative descriptors of neuron shape"
- "Interpret classifications in the context of network architecture"
prerequisites: "Modules 1-13, basic familiarity with neuroanatomy"
merit_stage: "Analysis"
compass_skills: ["Pattern Recognition", "Quantitative Analysis", "Critical Thinking"]
ccr_focus: ["Knowledge - Neuroanatomy", "Skills - Morphometrics"]

# Normalized metadata
slug: "module14"
short_title: "Computer Vision for EM"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "neuron-morphology"
  - "classification"
summary: "From filters to deep learning for image understanding and neuron classification from EM morphology."
key_questions: []
slides: []
notebook: []
datasets: []
personas: []
related_tools: []
related_frameworks: []
prerequisites_list: []
next_modules: []
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
    <h2>🔄 Neuron Classification Strategies</h2>
    <ul>
      <li>Taxonomies: excitatory vs. inhibitory, projection vs. interneuron</li>
      <li>Features: soma size, dendritic branching, axonal spread</li>
      <li>Tools: NBLAST, NeuroMorpho.org, mesh classifiers</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>🔄 Morphological Feature Extraction</h2>
    <ul>
      <li>Skeleton-based shape descriptors</li>
      <li>Sholl analysis, path length, bifurcation ratios</li>
      <li>Normalization and comparative metrics</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>🔄 Functional Implications</h2>
    <ul>
      <li>Linking morphology to electrophysiological role</li>
      <li>Comparing morphologically similar neurons across regions</li>
      <li>Implications for connectivity and computation</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>🌟 COMPASS Integration</h2>
    <ul>
      <li><strong>Knowledge:</strong> Cell type and morphology principles</li>
      <li><strong>Skills:</strong> Structural comparison, database tools</li>
      <li><strong>Character:</strong> Attention to detail, curiosity</li>
      <li><strong>Meta-Learning:</strong> Evaluating classification limits and biases</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>📚 References & Resources</h2>
    <ul>
      <li>Ascoli et al., 2007. <em>NeuroMorpho.Org: a central resource for neuronal morphologies</em>. Nat Neurosci.</li>
      <li>Colab: "Quantifying neuron shape using PyTorch and scikit-image"</li>
      <li>Allen Institute Cell Types Database</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>✅ Assessment</h2>
    <ul>
      <li>Extract morphology features from an EM-reconstructed neuron</li>
      <li>Classify neuron type using known anatomical criteria</li>
      <li>Submit justification and visualizations of your classification</li>
    </ul>
  </div>
</div>
</div>
