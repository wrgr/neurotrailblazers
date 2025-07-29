---
title: "Module 02: From Pixels to Projects — Exploring Real Connectomics Datasets"
layout: module
permalink: /modules/module02/
description: "Dive into real-world brain mapping datasets and learn how EM images become 3D digital reconstructions of the brain."
module_number: 2
difficulty: "Beginner"
duration: "2–3 hours"
learning_objectives:
  - "Describe how raw EM data is acquired and prepared for analysis"
  - "Identify the stages in the connectomics data pipeline (imaging, alignment, segmentation, skeletonization)"
  - "Explore real connectomics datasets using interactive tools"
  - "Recognize different formats (volumes, segments, meshes, skeletons) in current datasets"
prerequisites: "Module 1 or equivalent understanding of basic connectomics"
merit_stage: "Orientation & Research Foundations"
compass_skills:
  - "Digital Literacy"
  - "Data Navigation"
ccr_focus:
  - "Knowledge - Data Acquisition"
  - "Skills - Dataset Exploration"
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
    <h2>Core Topics</h2>
    <ul>
      <li>🖼️ <strong>Volume Imaging:</strong> Acquiring nanoscale slices via serial-section EM</li>
      <li>🔗 <strong>Image Alignment:</strong> Stitching and registering slices to form coherent volumes</li>
      <li>🧩 <strong>Segmentation:</strong> Using AI to label pixels and define cell boundaries</li>
      <li>🕸️ <strong>Skeletonization:</strong> Creating simplified graphs to represent neuron paths</li>
      <li>🧠 <strong>Dataset Exploration:</strong> FlyWire, MICrONS, H01, FAFB, Kasthuri, and more</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>Sample Interactive Tools</h2>
    <ul>
      <li><a href="https://neuroglancer-demo.appspot.com/">Neuroglancer</a></li>
      <li><a href="https://flywire.ai">FlyWire Viewer</a></li>
      <li><a href="https://www.microns-explorer.org">MICrONS Explorer</a></li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>COMPASS Integration</h2>
    <ul>
      <li><strong>Knowledge:</strong> Understand how data is organized and labeled for analysis</li>
      <li><strong>Skills:</strong> Navigate viewers, identify structures, interpret metadata</li>
      <li><strong>Character:</strong> Patience, attention to detail, and openness to uncertainty</li>
      <li><strong>Meta-Learning:</strong> Learn how tools and pipelines evolve across datasets</li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>References & Resources</h2>
    <ul>
      <li><strong>Kasthuri et al., 2015</strong>, Cell – "Saturated reconstruction of neocortex"</li>
      <li><strong>Zheng et al., 2018</strong>, Nature – FlyWire / FAFB EM volume of adult fly brain</li>
      <li><strong>MICrONS dataset release</strong>, 2021 – V1 Layer 2/3 mouse volume</li>
      <li><a href="https://bossdb.org">Allen Institute / BossDB</a></li>
      <li><a href="https://bossdb.org">BossDB</a> Cookbook: <a href="https://github.com/aplbrain/bossdb_cookbook/blob/main/notebooks/Five-Minute-Jump-Start.ipynb">Five-Minute Jump Start</a></li>
      <li><a href="https://bossdb.org">BossDB</a> Cookbook: <a href="https://github.com/aplbrain/bossdb_cookbook/blob/main/notebooks/More-Advanced-Get-Started-Downloading-Data-with-Intern.ipynb">Advanced Data Downloading</a></li>
    </ul>
  </div>

  <div class="card module-card">
    <h2>Assessment</h2>
    <ul>
      <li>Match dataset types to pipeline stages (e.g., segmentation → labeled volume)</li>
      <li>Navigate a dataset and find one synapse, one neuron, and one glial cell</li>
      <li>Write a 3–4 sentence description of how segmentation is performed and why it matters</li>
    </ul>
  </div>

</div>
</div>
