---
layout: dataset
title: "Accessing Public EM Datasets"
description: "Resources and notebooks for downloading and exploring connectomics data."
permalink: /datasets/access/
slug: access
track: research-in-action
pathways:
  - research workflow
  - data fluency
summary: "Starter notebooks and clients for FlyWire, H01, MICrONS, neuPrint and BossDB, with each platform's license."
modality: "Electron microscopy"
species: "Mixed"
scale: "Multiple public datasets"
access_level: "Public and account-based portals"
use_cases:
  - Data onboarding
  - Notebook setup
  - Dataset access workflows
recommended_modules:
  - module02
  - module03
related_tools:
  - ask-an-expert
related_frameworks:
  - education-models
resource_links: []
last_reviewed: 2026-09-26
maintainer: NeuroTrailblazers Team
content_type: core
---

<div class="main-content" markdown="1">

## Each platform has its own client and starter notebooks

The links below go to the
providers' own material, checked on 26 September 2026. When a notebook and this page
disagree, the provider's documentation wins.

<p><strong>New to the data?</strong> Start with <a href="{{ '/datasets/getting-started/' | relative_url }}">Getting Started with Data</a>. It tells you <em>which</em> of these platforms your question needs, walks through token setup, and lists the common failures. This page collects the per-platform examples behind it.</p>

<div class="grid-md mt-2 mb-2">
  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-meta">
        <span class="dataset-type">Fly brain</span>
      </div>
    </div>
    <h3>FlyWire (CAVE)</h3>
    <p>Browse and download tables in Codex with no install. For live, versioned queries, use <code>caveclient</code> with a free token from a Google account that has accepted FlyWire's terms. The data are licensed CC BY-NC 4.0.</p>
    <ul class="dataset-facts">
      <li><code>pip install caveclient</code></li>
      <li><a href="https://codex.flywire.ai/" target="_blank" rel="noopener">FlyWire Codex</a> (browser and downloads)</li>
      <li><a href="https://www.caveconnecto.me/CAVEclient/tutorials/authentication/" target="_blank" rel="noopener">CAVEclient authentication tutorial</a></li>
      <li><a href="https://flywire.ai/guidelines" target="_blank" rel="noopener">FlyWire data guidelines and license</a></li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-meta">
        <span class="dataset-type">Human cortex</span>
      </div>
    </div>
    <h3>H01 (Google Cloud)</h3>
    <p>H01 is served from Google Cloud Storage in Neuroglancer's precomputed format, not through CAVE or BossDB. Read it with TensorStore or CloudVolume. The data are CC BY 4.0.</p>
    <ul class="dataset-facts">
      <li><code>pip install tensorstore</code></li>
      <li><a href="https://h01-release.storage.googleapis.com/data.html" target="_blank" rel="noopener">H01 data page</a> (paths, formats, license)</li>
      <li><a href="https://colab.sandbox.google.com/gist/jbms/1ec1192c34ec816c2c517a3b51a8ed6c/h01_data_access.ipynb" target="_blank" rel="noopener">H01 data-access Colab</a> (linked from the data page)</li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-meta">
        <span class="dataset-type">Mouse cortex</span>
      </div>
    </div>
    <h3>MICrONS (CAVE and static exports)</h3>
    <p>Query the MICrONS cubic millimeter with <code>caveclient</code> on the <code>minnie65_public</code> datastack, or read the public CSV exports with no account at all. The data are CC BY 4.0.</p>
    <ul class="dataset-facts">
      <li><code>pip install caveclient</code></li>
      <li><a href="https://tutorial.microns-explorer.org/quickstart_notebooks/01-caveclient-setup.html" target="_blank" rel="noopener">MICrONS CAVEclient setup</a></li>
      <li><a href="https://github.com/AllenInstitute/MicronsBinder/blob/master/notebooks/mm3_intro/MeshAccess.ipynb" target="_blank" rel="noopener">Visualizing meshes (MicronsBinder)</a></li>
      <li><a href="{{ '/notebooks/microns-lab/' | relative_url }}">This site's MICrONS real-data lab</a> (version-pinned, no account)</li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-meta">
        <span class="dataset-type">Fly brain and nerve cord</span>
      </div>
    </div>
    <h3>Janelia hemibrain and MANC (neuPrint)</h3>
    <p>Query the hemibrain, MANC and the other Janelia connectomes with <code>neuprint-python</code>, using the token from your neuPrint account page.</p>
    <ul class="dataset-facts">
      <li><code>pip install neuprint-python</code></li>
      <li><a href="https://connectome-neuprint.github.io/neuprint-python/docs/quickstart.html" target="_blank" rel="noopener">neuprint-python quickstart</a></li>
      <li><a href="https://github.com/connectome-neuprint/neuprint-python/blob/master/examples/skeleton-with-synapses.ipynb" target="_blank" rel="noopener">Example: a skeleton with its synapses</a></li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-meta">
        <span class="dataset-type">Many datasets</span>
      </div>
    </div>
    <h3>BossDB</h3>
    <p>BossDB hosts dozens of EM and light-microscopy volumes, including MICrONS, Kasthuri 2015, Witvliet 2020, BANC and the larval zebrafish. Read cutouts with the <code>intern</code> client. Public data need no account.</p>
    <ul class="dataset-facts">
      <li><code>pip install intern</code></li>
      <li><a href="https://bossdb.org/projects" target="_blank" rel="noopener">BossDB project list</a> (each page shows its <code>bossdb://</code> path)</li>
      <li><a href="https://github.com/jhuapl-boss/intern/wiki/Boss-Download-Cutout-Tutorial" target="_blank" rel="noopener">intern cutout tutorial</a></li>
    </ul>
  </div>

  <div class="dataset-card">
    <div class="dataset-header">
      <div class="dataset-meta">
        <span class="dataset-type">Viewing</span>
      </div>
    </div>
    <h3>Viewers</h3>
    <p>Every platform above opens its data in <a href="https://github.com/google/neuroglancer" target="_blank" rel="noopener">Neuroglancer</a> in the browser. To look at a downloaded cutout on your own machine, use <a href="https://napari.org/" target="_blank" rel="noopener">napari</a>.</p>
  </div>
</div>

<p>Next: pick a dataset from the <a href="{{ '/datasets/' | relative_url }}">catalog</a>, or go straight to the <a href="{{ '/datasets/getting-started/' | relative_url }}">60-minute first contact</a>.</p>

</div>
