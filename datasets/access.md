---
layout: dataset
title: "Accessing Public EM Datasets"
description: "Resources and notebooks for downloading and exploring connectomics data."
---

<div class="main-content">

# Getting Started with EM Connectomics Datasets

A guide to resources and example notebooks for accessing major public Electron Microscopy (EM) connectomics datasets.

<div class="grid-md mt-2 mb-2">
  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-icon">🧠</div>
      <div class="dataset-meta">
        <span class="dataset-type">Fly &amp; Human</span>
      </div>
    </div>
    <h3>Google Research (FAFB &amp; H01)</h3>
    <p>Access FlyWire and the H01 human cortex dataset using <code>caveclient</code>.</p>
    <ul class="dataset-facts">
      <li><code>pip install caveclient</code></li>
      <li><a href="https://colab.research.google.com/github/seung-lab/PyChunkedGraph/blob/master/notebooks/Introduction%20to%20CAVE.ipynb" target="_blank">CAVEclient Basics</a></li>
      <li><a href="https://colab.research.google.com/github/seung-lab/PyChunkedGraph/blob/master/notebooks/Queries.ipynb" target="_blank">Advanced Queries</a></li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-icon">🐭</div>
      <div class="dataset-meta">
        <span class="dataset-type">Mouse Cortex</span>
      </div>
    </div>
    <h3>Allen Institute MICrONS</h3>
    <p>Download the MICrONS dataset via the <code>allensdk</code> Python library.</p>
    <ul class="dataset-facts">
      <li><code>pip install allensdk</code></li>
      <li><a href="https://github.com/AllenInstitute/MicronsBinder/blob/main/notebooks/intro_to_microns_data.ipynb" target="_blank">MICrONS Data Access</a></li>
      <li><a href="https://github.com/AllenInstitute/MicronsBinder/blob/main/notebooks/meshing.ipynb" target="_blank">Visualizing Meshes</a></li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-icon">🪰</div>
      <div class="dataset-meta">
        <span class="dataset-type">Fly Brain</span>
      </div>
    </div>
    <h3>Janelia Hemibrain</h3>
    <p>Work with the hemibrain connectome using <code>neuprint-python</code>.</p>
    <ul class="dataset-facts">
      <li><code>pip install neuprint-python</code></li>
      <li><a href="https://github.com/connectome-neuprint/neuprint-python/blob/master/notebooks/Neuprint_Tutorial.ipynb" target="_blank">neuPrint Starter Guide</a></li>
      <li><a href="https://github.com/connectome-neuprint/neuprint-python/blob/master/notebooks/Neuprint_Recipes.ipynb" target="_blank">Common Recipes</a></li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-icon">💾</div>
      <div class="dataset-meta">
        <span class="dataset-type">Multiple Datasets</span>
      </div>
    </div>
    <h3>bossDB Resources</h3>
    <p>Explore a variety of EM volumes hosted on bossDB using the <code>intern</code> client.</p>
    <ul class="dataset-facts">
      <li><code>pip install intern</code></li>
      <li><a href="https://github.com/jhuapl-boss/intern/blob/master/notebooks/Boss_cutout_example.ipynb" target="_blank">bossDB Cutout Example</a></li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-icon">🚀</div>
      <div class="dataset-meta">
        <span class="dataset-type">Visualization</span>
      </div>
    </div>
    <h3>General Tools</h3>
    <p>Visualize data in-browser with Neuroglancer or analyze it locally with <a href="https://napari.org/" target="_blank">Napari</a>.</p>
  </div>
</div>

</div>
