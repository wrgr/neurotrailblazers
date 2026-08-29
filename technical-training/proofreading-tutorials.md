---
layout: default
title: "EM Proofreading Tutorials & Community Practice Guide"
description: "Master volume electron microscopy proofreading: false merge/split diagnosis, dendrite/axon tracing in Neuroglancer & CAVE, synapse validation, and curated community resources."
permalink: /technical-training/proofreading-tutorials/
track: core-concepts-methods
pathways:
  - proofreading
  - data quality
  - workflows
content_type: core
---

<div class="main-content">

  <div class="hero hero-spaced hero-rounded" style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #31104b 100%); color: #fff; padding: 3rem 2rem; border-radius: 12px; margin-bottom: 2rem;">
    <div class="hero-content" style="max-width: 900px;">
      <span class="pill" style="background: rgba(124, 58, 237, 0.35); color: #c4b5fd; border: 1px solid rgba(167, 139, 250, 0.4); font-weight: 700; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.25rem 0.6rem; border-radius: 999px;">Technical Guide &amp; Practice Suite</span>
      <h1 style="font-size: 2.4rem; font-weight: 800; line-height: 1.2; margin: 0.75rem 0 0.5rem 0; color: #ffffff;">EM Proofreading Tutorials &amp; Community Practice</h1>
      <p style="font-size: 1.1rem; color: #cbd5e1; line-height: 1.5; margin: 0;">
        How human annotators fix machine segmentation errors, validate synaptic connections, and transform raw AI predictions into ground-truth connectomes.
      </p>
    </div>
  </div>

  <!-- Table of Contents / Fast Navigation -->
  <div class="card" style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 1.25rem; margin-bottom: 2.5rem;">
    <h3 style="margin: 0 0 0.75rem 0; font-size: 1rem; color: #1e293b; display: flex; align-items: center; gap: 0.4rem;">
      <span>📑</span> Table of Contents &amp; Learning Flow
    </h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem; font-size: 0.88rem;">
      <a href="#core-errors" style="color: #1a56db; text-decoration: none; font-weight: 600;">1. Diagnosing Segmentation Errors &rarr;</a>
      <a href="#synapse-validation" style="color: #1a56db; text-decoration: none; font-weight: 600;">2. Synapse Verification Criteria &rarr;</a>
      <a href="#tooling-guides" style="color: #1a56db; text-decoration: none; font-weight: 600;">3. Platform Workflows (CAVE, Neuroglancer) &rarr;</a>
      <a href="#step-by-step" style="color: #1a56db; text-decoration: none; font-weight: 600;">4. Step-by-Step Tracing SOP &rarr;</a>
      <a href="#community-resources" style="color: #1a56db; text-decoration: none; font-weight: 600;">5. Canonical Community Portals &rarr;</a>
    </div>
  </div>

  <!-- Section 1: Diagnosing Segmentation Errors -->
  <section class="section" id="core-errors" style="margin-bottom: 3rem;">
    <div class="section-header">
      <h2 style="font-size: 1.6rem; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
        1. Diagnosing Segmentation Errors
      </h2>
      <p style="color: #475569; font-size: 0.95rem;">Automated 3D convolutional models (FFNs, 3D U-Nets) produce two fundamental topological errors. Your first job as a proofreader is rapidly distinguishing them.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
      
      <!-- False Merges Card -->
      <div class="card" style="border: 2px solid #fca5a5; border-radius: 10px; padding: 1.5rem; background: #fff;">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
          <span style="background: #fee2e2; color: #b91c1c; font-size: 1.2rem; padding: 0.35rem 0.6rem; border-radius: 6px; font-weight: 800;">⚡ Merge</span>
          <h3 style="margin: 0; font-size: 1.15rem; color: #991b1b;">False Merges (Over-Segmentation)</h3>
        </div>
        <p style="font-size: 0.88rem; color: #475569; line-height: 1.5;">
          Occurs when the AI connects two distinct biological neurons into a single object ID. <strong>Why it happens:</strong> thin membrane boundaries, poor staining contrast, or vesicle clouds that blur cell membranes.
        </p>
        <h4 style="font-size: 0.82rem; text-transform: uppercase; color: #991b1b; letter-spacing: 0.05em; margin: 1rem 0 0.4rem 0;">Key Diagnostic Signatures:</h4>
        <ul style="margin: 0; padding-left: 1.2rem; font-size: 0.85rem; color: #334155; line-height: 1.5;">
          <li><strong>Multiple Somas:</strong> A single object contains two cell bodies or two primary neurite stalks.</li>
          <li><strong>Impossible Branch Angles:</strong> Axons making acute &lt;60° hairpins across fascicles without cytoskeletal continuity.</li>
          <li><strong>Discordant Myelination:</strong> A myelinated axon suddenly jumping into an unmyelinated dendritic shaft.</li>
          <li><strong>Membrane Discontinuity:</strong> Follow the slice sequence: at least one cross-section will show a clear lipid bilayer separating the two paths.</li>
        </ul>
        <div style="margin-top: 1rem; background: #fef2f2; border-left: 4px solid #ef4444; padding: 0.6rem 0.8rem; font-size: 0.8rem; color: #991b1b;">
          <strong>Correction Action:</strong> In Neuroglancer / CAVE, place a <em>Split Point</em> on the false bridge to separate the component supervoxels.
        </div>
      </div>

      <!-- False Splits Card -->
      <div class="card" style="border: 2px solid #93c5fd; border-radius: 10px; padding: 1.5rem; background: #fff;">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
          <span style="background: #dbeafe; color: #1d4ed8; font-size: 1.2rem; padding: 0.35rem 0.6rem; border-radius: 6px; font-weight: 800;">✂️ Split</span>
          <h3 style="margin: 0; font-size: 1.15rem; color: #1e40af;">False Splits (Under-Segmentation)</h3>
        </div>
        <p style="font-size: 0.88rem; color: #475569; line-height: 1.5;">
          Occurs when a single continuous biological neuron is severed into two or more detached pieces. <strong>Why it happens:</strong> knife chatter, staining folds, missing sections, or ultra-thin spine necks.
        </p>
        <h4 style="font-size: 0.82rem; text-transform: uppercase; color: #1e40af; letter-spacing: 0.05em; margin: 1rem 0 0.4rem 0;">Key Diagnostic Signatures:</h4>
        <ul style="margin: 0; padding-left: 1.2rem; font-size: 0.85rem; color: #334155; line-height: 1.5;">
          <li><strong>Orphan Dendritic Spines:</strong> A spine head floating unattached within 100nm of a dendritic shaft with matching postsynaptic density.</li>
          <li><strong>Abrupt Terminal Stubs:</strong> An axon terminates abruptly in the middle of a continuous bundle with no growth cone morphology.</li>
          <li><strong>Artifact Crossings:</strong> An open terminal points directly across a fold or knife chatter mark at another open terminal with identical cross-sectional diameter and mitochondrial trajectory.</li>
        </ul>
        <div style="margin-top: 1rem; background: #eff6ff; border-left: 4px solid #3b82f6; padding: 0.6rem 0.8rem; font-size: 0.8rem; color: #1e40af;">
          <strong>Correction Action:</strong> Select both fragment IDs in CAVE / PyChunkedGraph and execute a <em>Merge Operation</em>.
        </div>
      </div>

    </div>
  </section>

  <!-- Section 2: Synapse Validation -->
  <section class="section" id="synapse-validation" style="margin-bottom: 3rem;">
    <div class="section-header">
      <h2 style="font-size: 1.6rem; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
        2. Synapse Verification Criteria
      </h2>
      <p style="color: #475569; font-size: 0.95rem;">Automated synapse detectors find millions of connections, but have false positive rates of 5–15%. Use this 4-point checklist to confirm true chemical synapses.</p>
    </div>

    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 1.5rem; margin-top: 1rem;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
        
        <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem;">
          <h4 style="margin: 0 0 0.35rem 0; color: #1e293b; font-size: 0.92rem; display: flex; align-items: center; gap: 0.35rem;">
            <span style="color: #059669;">1.</span> Presynaptic Vesicle Cloud
          </h4>
          <p style="margin: 0; font-size: 0.82rem; color: #475569; line-height: 1.45;">
            Cluster of clear, spherical 30–50nm lipid vesicles docked within 100nm of the presynaptic active zone membrane. In flies, look for the electron-dense <strong>T-bar</strong> ribbon structure.
          </p>
        </div>

        <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem;">
          <h4 style="margin: 0 0 0.35rem 0; color: #1e293b; font-size: 0.92rem; display: flex; align-items: center; gap: 0.35rem;">
            <span style="color: #059669;">2.</span> Synaptic Cleft Rigid Spacing
          </h4>
          <p style="margin: 0; font-size: 0.82rem; color: #475569; line-height: 1.45;">
            Strictly parallel extracellular space (15–25nm width) maintained across at least 3–4 consecutive EM sections, containing electron-dense adhesion protein matrix.
          </p>
        </div>

        <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem;">
          <h4 style="margin: 0 0 0.35rem 0; color: #1e293b; font-size: 0.92rem; display: flex; align-items: center; gap: 0.35rem;">
            <span style="color: #059669;">3.</span> Postsynaptic Density (PSD)
          </h4>
          <p style="margin: 0; font-size: 0.82rem; color: #475569; line-height: 1.45;">
            Thick, dark proteinaceous thickening lining the intracellular face of the recipient membrane (pronounced in asymmetric/excitatory synapses; thinner in symmetric/inhibitory synapses).
          </p>
        </div>

        <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem;">
          <h4 style="margin: 0 0 0.35rem 0; color: #1e293b; font-size: 0.92rem; display: flex; align-items: center; gap: 0.35rem;">
            <span style="color: #059669;">4.</span> Multi-Section Continuity
          </h4>
          <p style="margin: 0; font-size: 0.82rem; color: #475569; line-height: 1.45;">
            A genuine synapse spans a disc of 200–500nm diameter. If an apparent junction appears on only a single 30nm section without neighboring vesicles, flag as artifact.
          </p>
        </div>

      </div>
    </div>
  </section>

  <!-- Section 3: Tooling Workflows -->
  <section class="section" id="tooling-guides" style="margin-bottom: 3rem;">
    <div class="section-header">
      <h2 style="font-size: 1.6rem; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
        3. Platform-by-Platform Proofreading Workflows
      </h2>
      <p style="color: #475569; font-size: 0.95rem;">Master the standard tool stacks used across FlyWire, MICrONS, and the Mouse Connectome Project.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
      
      <!-- CAVE & Neuroglancer -->
      <div class="card" style="border: 1px solid #cbd5e1; border-radius: 10px; padding: 1.5rem; background: #fff;">
        <h3 style="margin: 0 0 0.5rem 0; color: #1a56db; font-size: 1.15rem;">🖥️ CAVE &amp; Neuroglancer Workflow</h3>
        <p style="font-size: 0.85rem; color: #475569; line-height: 1.45;">
          The primary production backend for <strong>FlyWire</strong> and <strong>MICrONS</strong>. Uses a dynamic chunked graph (`PyChunkedGraph`) to record edits without re-segmenting the petascale volume.
        </p>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; font-size: 0.8rem; margin: 0.75rem 0;">
          <p style="margin: 0 0 0.35rem 0;"><strong>Essential Keybindings:</strong></p>
          <ul style="margin: 0; padding-left: 1.1rem; color: #334155; line-height: 1.4;">
            <li><code>Double-Click</code>: Center view on point in 3D</li>
            <li><code>Shift + Click</code>: Toggle segment ID selection</li>
            <li><code>Ctrl / Cmd + Scroll</code>: Step through Z-sections</li>
            <li><code>Alt + Click</code>: Place split/merge graph annotation</li>
            <li><code>Space</code>: Toggle 3D mesh visibility</li>
          </ul>
        </div>
        <p style="font-size: 0.8rem; color: #64748b; margin: 0;">
          <strong>Materialization Rule:</strong> Never run analysis on live unpinned IDs. Always pin to an explicit <code>materialization_version</code> to guarantee reproducible results.
        </p>
      </div>

      <!-- webKnossos -->
      <div class="card" style="border: 1px solid #cbd5e1; border-radius: 10px; padding: 1.5rem; background: #fff;">
        <h3 style="margin: 0 0 0.5rem 0; color: #7e22ce; font-size: 1.15rem;">🌐 webKnossos &amp; Skeletonization</h3>
        <p style="font-size: 0.85rem; color: #475569; line-height: 1.45;">
          Optimized for high-speed volumetric skeleton tracing (Max Planck / scalable minds). Features "Flight Mode" allowing annotators to fly through axons at up to 1 mm/hour.
        </p>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; font-size: 0.8rem; margin: 0.75rem 0;">
          <p style="margin: 0 0 0.35rem 0;"><strong>Core Features:</strong></p>
          <ul style="margin: 0; padding-left: 1.1rem; color: #334155; line-height: 1.4;">
            <li><strong>Flight Mode:</strong> Velocity-based Z-stepping for rapid long-range axon tracking</li>
            <li><strong>Node &amp; Edge Graphs:</strong> Hierarchical SWC / NML skeleton export</li>
            <li><strong>Task Queues:</strong> Distributed consensus tracing with automated inter-annotator agreement scoring</li>
          </ul>
        </div>
        <p style="font-size: 0.8rem; color: #64748b; margin: 0;">
          <strong>Best For:</strong> Fast topological proofreading, cell-type census, and dense volume bounding-box annotations.
        </p>
      </div>

    </div>
  </section>

  <!-- Section 4: Canonical Community Resources -->
  <section class="section" id="community-resources" style="margin-bottom: 3rem;">
    <div class="section-header">
      <h2 style="font-size: 1.6rem; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
        4. Canonical Community Proofreading Resources
      </h2>
      <p style="color: #475569; font-size: 0.95rem;">Jump straight into official academies, interactive simulators, and documentation produced by global connectomics consortia.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
      
      <!-- FlyWire Academy -->
      <div class="card" style="border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; background: #fff;">
        <h4 style="margin: 0 0 0.35rem 0; font-size: 1.05rem;"><a href="https://codex.flywire.ai/" target="_blank" rel="noopener" style="color: #1a56db; text-decoration: none;">🏆 FlyWire Academy &amp; Codex &rarr;</a></h4>
        <p style="font-size: 0.82rem; color: #475569; line-height: 1.45; margin: 0 0 0.5rem 0;">
          Official community portal for whole-brain Drosophila connectomics (Nature 2024). Includes comprehensive video tutorials, proofreading certification exercises, and interactive cell search.
        </p>
        <span class="jc-tag" style="background: #dbeafe; color: #1e40af; font-size: 0.72rem; font-weight: 600;">Drosophila &bull; Whole Brain &bull; CAVE</span>
      </div>

      <!-- EyeWire -->
      <div class="card" style="border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; background: #fff;">
        <h4 style="margin: 0 0 0.35rem 0; font-size: 1.05rem;"><a href="https://eyewire.org/" target="_blank" rel="noopener" style="color: #1a56db; text-decoration: none;">🎮 EyeWire Training Camp &rarr;</a></h4>
        <p style="font-size: 0.82rem; color: #475569; line-height: 1.45; margin: 0 0 0.5rem 0;">
          The pioneering gamified citizen-science platform developed by the Seung Lab (Princeton). Superb interactive introductory onboarding to 3D branch tracing and merge spotting.
        </p>
        <span class="jc-tag" style="background: #fef3c7; color: #92400e; font-size: 0.72rem; font-weight: 600;">Retina &bull; Citizen Science &bull; Gamified</span>
      </div>

      <!-- CAVEclient Docs -->
      <div class="card" style="border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; background: #fff;">
        <h4 style="margin: 0 0 0.35rem 0; font-size: 1.05rem;"><a href="https://caveclient.readthedocs.io/" target="_blank" rel="noopener" style="color: #1a56db; text-decoration: none;">📖 CAVEclient Python Docs &rarr;</a></h4>
        <p style="font-size: 0.82rem; color: #475569; line-height: 1.45; margin: 0 0 0.5rem 0;">
          Official API documentation for programmatically querying proofread root IDs, synapse tables, cell taxonomies, and ID edit lineages in Python.
        </p>
        <span class="jc-tag" style="background: #ede9fe; color: #6d28d9; font-size: 0.72rem; font-weight: 600;">Python &bull; CAVE API &bull; Provenance</span>
      </div>

      <!-- SynapseWeb -->
      <div class="card" style="border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; background: #fff;">
        <h4 style="margin: 0 0 0.35rem 0; font-size: 1.05rem;"><a href="https://synapseweb.clm.utexas.edu/" target="_blank" rel="noopener" style="color: #1a56db; text-decoration: none;">🔬 SynapseWeb EM Neurocytology Atlas &rarr;</a></h4>
        <p style="font-size: 0.82rem; color: #475569; line-height: 1.45; margin: 0 0 0.5rem 0;">
          The Kristen Harris lab's canonical visual EM atlas (UT Austin). The standard reference for spine morphologies, active zones, PSD variations, and organelle ultrastructure.
        </p>
        <span class="jc-tag" style="background: #d1fae5; color: #065f46; font-size: 0.72rem; font-weight: 600;">Ultrastructure &bull; Anatomy &bull; Spines</span>
      </div>

      <!-- webKnossos Docs -->
      <div class="card" style="border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; background: #fff;">
        <h4 style="margin: 0 0 0.35rem 0; font-size: 1.05rem;"><a href="https://webknossos.org/docs" target="_blank" rel="noopener" style="color: #1a56db; text-decoration: none;">🌐 webKnossos User Guide &rarr;</a></h4>
        <p style="font-size: 0.82rem; color: #475569; line-height: 1.45; margin: 0 0 0.5rem 0;">
          Step-by-step guides for setting up volume layers, sharing collaborative annotations, flight-mode tracing, and skeleton mesh exports.
        </p>
        <span class="jc-tag" style="background: #fce7f3; color: #9d174d; font-size: 0.72rem; font-weight: 600;">Skeletons &bull; Flight Mode &bull; Tooling</span>
      </div>

      <!-- VAST Manual -->
      <div class="card" style="border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; background: #fff;">
        <h4 style="margin: 0 0 0.35rem 0; font-size: 1.05rem;"><a href="https://software.rc.fas.harvard.edu/lichtman/vast/" target="_blank" rel="noopener" style="color: #1a56db; text-decoration: none;">🖌️ Harvard Lichtman Lab VAST Guide &rarr;</a></h4>
        <p style="font-size: 0.82rem; color: #475569; line-height: 1.45; margin: 0 0 0.5rem 0;">
          The Volume Annotation and Segmentation Tool created by Daniel Berger. Ideal for high-precision manual voxel painting and proofreading dense mammalian neuropil.
        </p>
        <span class="jc-tag" style="background: #f1f5f9; color: #334155; font-size: 0.72rem; font-weight: 600;">Manual Painting &bull; Mammalian &bull; Harvard</span>
      </div>

    </div>
  </section>

  <!-- Section 5: Related Modules & Resources -->
  <section class="section" style="margin-top: 2rem; border-top: 2px solid #e2e8f0; padding-top: 1.5rem;">
    <h3 style="font-size: 1.2rem; color: #0f172a; margin-bottom: 1rem;">🔗 Related Curriculum &amp; Research Surfaces</h3>
    <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
      <a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}" class="btn btn-secondary" style="font-size: 0.82rem;">📘 Technical Unit 08: Segmentation &amp; Proofreading</a>
      <a href="{{ '/content-library/proofreading/error-taxonomy/' | relative_url }}" class="btn btn-secondary" style="font-size: 0.82rem;">📑 Content Library: Error Taxonomy</a>
      <a href="{{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}" class="btn btn-secondary" style="font-size: 0.82rem;">📊 Content Library: Metrics &amp; QA</a>
      <a href="{{ '/initiatives/outreach/' | relative_url }}" class="btn btn-primary" style="font-size: 0.82rem;">🌐 Global Outreach &amp; Citizen Science &rarr;</a>
    </div>
  </section>

</div>
