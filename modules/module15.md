---

title: "Module 15: Connectome Proofreading and Quality Control"
layout: module
description: "Learn how to identify and correct errors in segmentation and connectivity, improving the reliability of connectomics data."
module\_number: 15
difficulty: "Intermediate"
duration: "3 hours"
learning\_objectives:

* "Identify common segmentation and synapse errors"
* "Use visualization tools for proofreading"
* "Assess connectome quality with metrics"
* "Propose and apply corrections to data"
  prerequisites: "Modules 1-14, familiarity with Neuroglancer"
  merit\_stage: "Analysis"
  compass\_skills: \["Attention to Detail", "Visual Reasoning", "Data Curation"]
  ccr\_focus: \["Skills - Quality Control", "Skills - Annotation"]

---

<div class="main-content">
  <div class="hero">
    <div class="hero-content">
      <span class="module-number">Module 15</span>
      <h1>{{ page.title }}</h1>
      <p class="hero-subtitle">{{ page.description }}</p>
    </div>
  </div>

  <section class="section">
    <h2>🔍 Common Error Types</h2>
    <p>Segmentation errors (splits, merges) and synapse mislabels affect downstream analysis. Learn to spot patterns in raw EM imagery and segment overlays.</p>
    <ul>
      <li>Split vs. merge errors</li>
      <li>Ghost synapses and missing links</li>
      <li>Boundary ambiguity and stitching artifacts</li>
    </ul>
  </section>

  <section class="section">
    <h2>📊 Visualization Tools</h2>
    <p>Interactive viewers like Neuroglancer enable efficient quality control. Understand how to use layers and cross-sections for visual checks.</p>
    <ul>
      <li>Configuring layers in Neuroglancer</li>
      <li>Using 3D mesh and skeleton modes</li>
      <li>Spotting errors across slices</li>
    </ul>
  </section>

  <section class="section">
    <h2>📈 Metrics and Fixes</h2>
    <p>Evaluate accuracy using F1 score, precision, recall, and consistency with ground truth or heuristics. Apply edits or flag errors for correction.</p>
    <ul>
      <li>Segment overlap metrics</li>
      <li>Topology-aware metrics</li>
      <li>Manual editing vs. AI-assisted correction</li>
    </ul>
  </section>

  <section class="section">
    <h2>🌟 COMPASS Integration</h2>
    <ul>
      <li><strong>Knowledge:</strong> Common connectomics error modes</li>
      <li><strong>Skills:</strong> Visual identification, annotation tools</li>
      <li><strong>Character:</strong> Persistence, accountability</li>
      <li><strong>Meta-Learning:</strong> Recognizing error patterns across datasets</li>
    </ul>
  </section>

  <section class="section">
    <h2>📚 References & Resources</h2>
    <ul>
      <li>Funke et al., 2018. <em>Large Scale Image Segmentation with Structured Loss Based Deep Learning for Connectomics</em>. ECCV.</li>
      <li>Motta et al., 2019. <em>Dense connectomic reconstruction in layer 4 of the somatosensory cortex</em>. Science.</li>
      <li>Colab: "Segmentation Proofreading with Neuroglancer"</li>
    </ul>
  </section>

  <section class="section">
    <h2>✅ Assessment</h2>
    <ul>
      <li>Locate and document at least 3 segmentation errors in a provided volume</li>
      <li>Use Neuroglancer to propose a correction</li>
      <li>Reflect on how quality control affects downstream analysis</li>
    </ul>
  </section>
</div>
