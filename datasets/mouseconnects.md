---
layout: dataset
title: "MouseConnects: A Hippocampal Connectome in Progress"
permalink: /datasets/mouseconnects/
slug: mouseconnects
track: research-in-action
pathways:
  - research workflow
  - data fluency
summary: "What the MouseConnects HI-MC project is building: a 10 mm³ hippocampal connectome, its imaging method, collaborators, funding status and aims. No data is released yet."
modality: "Multibeam SEM with ion-beam milling of semithin sections"
species: "Mouse"
scale: "10 mm³ hippocampal formation, >10 PB expected"
access_level: "Not yet released"
use_cases:
  - Connectomics pipeline learning
  - Circuit analysis case studies
  - AI segmentation and proofreading exercises
recommended_modules:
  - module02
  - module04
  - module05
  - module06
  - module07
  - module08
  - module12
related_tools:
  - connectome-quality
  - ask-an-expert
related_frameworks:
  - research-incubator-model
  - education-models
resource_links: []
last_reviewed: 2026-09-26
maintainer: NeuroTrailblazers Team
use_layout_hero: false
content_type: core
---

<div class="hero">
    <div class="container">
        <div class="hero-content">
            <div class="hero-text">
                <div style="background: rgba(255,255,255,0.15); backdrop-filter: blur(10px); padding: 0.5rem 1rem; border-radius: 25px; font-size: 0.9rem; margin-bottom: 1rem; display: inline-block;">
                    NIH BRAIN CONNECTS • 2023–2028
                </div>
                <h1 class="hero-title-impact">
                    <span class="hero-title-main">MouseConnects</span>
                    <span class="hero-title-sub">A hippocampal connectome in progress</span>
                </h1>
                <div class="hero-description-box">
                    <p>A planned synapse-level reconstruction of 10 mm³ of the mouse hippocampal formation, the circuits of memory and spatial navigation.</p>
                </div>
                <div class="cta-buttons">
                    <a href="#dataset-access" class="btn btn-primary btn-large">Data status</a>
                    <a href="{{ '/datasets/workflow/' | relative_url }}" class="btn btn-secondary btn-large">View the pipeline</a>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="container">
    <div class="section">
        <h2 class="section-title">Ten cubic millimeters, about ten times MICrONS or H01</h2>
        <p>MouseConnects targets the mouse hippocampal formation, the region most closely tied to memory and spatial navigation. The NIH award abstract says the project "will image 10 cubic millimeters". That is roughly ten times the volume of MICrONS or H01 (our arithmetic), and the abstract describes it as a feasibility test for a whole mouse brain, which "is 50 times larger". The data size is a projection, and the published figures differ: "about 10,000 terabytes" in Harvard's announcement, "about 25,000 terabytes, or 25 petabytes" in Google's, and "may exceed tens of petabytes" in the NIH abstract. Google's post also gives the volume as "10–15 cubic mm". The <a href="{{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}">case study</a> covers the scientific rationale and pipeline in depth.</p>

        <div class="cards-grid mt-2">
            <div class="card dataset-card-blue text-center">
                <div style="font-size: 2.5rem; font-weight: 700; color: var(--neural-blue); margin-bottom: 0.5rem;">10 mm³</div>
                <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">Target volume</div>
                <div style="font-size: 0.9rem; color: #7f8c8d; font-style: italic;">about 10× MICrONS or H01</div>
            </div>
            <div class="card dataset-card-purple text-center">
                <div style="font-size: 2.5rem; font-weight: 700; color: var(--cerebral-purple); margin-bottom: 0.5rem;">2 × 91</div>
                <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">Electron beams</div>
                <div style="font-size: 0.9rem; color: #7f8c8d; font-style: italic;">two multibeam SEMs, Harvard and Princeton</div>
            </div>
            <div class="card dataset-card-cyan text-center">
                <div style="font-size: 2.5rem; font-weight: 700; color: var(--axon-cyan); margin-bottom: 0.5rem;">&gt;10 PB</div>
                <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">Projected raw imagery</div>
                <div style="font-size: 0.9rem; color: #7f8c8d; font-style: italic;">projection; published estimates run from ~10 PB to ~25 PB</div>
            </div>
            <div class="card dataset-card-orange text-center">
                <div style="font-size: 2.5rem; font-weight: 700; color: #f97316; margin-bottom: 0.5rem;">7</div>
                <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;">Institutions</div>
                <div style="font-size: 0.9rem; color: #7f8c8d; font-style: italic;">listed below</div>
            </div>
        </div>
    </div>

    <div class="section">
        <h2 class="section-title">The imaging method is new, not just bigger</h2>
        <ul>
            <li><strong>Sectioning and imaging:</strong> the block is cut into semithin sections. Each section is imaged by multibeam SEM, a few nanometers are milled away with an ion beam, and the surface is imaged again until the whole section is done. The award gives the aim as reducing the distortions of ultrathin sectioning.</li>
            <li><strong>Targeting:</strong> the volume of interest is chosen from a micro-CT scan of the whole brain.</li>
            <li><strong>Two imaging sites:</strong> one 91-beam SEM at Harvard and one at Princeton.</li>
            <li><strong>Automated reconstruction:</strong> flood-filling network segmentation from Google Research, the method used for H01, followed by labeling of neurons, glia, blood vessels, myelin, cell bodies and synapses.</li>
            <li><strong>Registration:</strong> the reconstruction is to be registered to the Allen Institute mouse brain atlas so it can be related to other data.</li>
            <li><strong>Open access:</strong> free online tools to render, proofread and analyze the volume, released as the project progresses.</li>
        </ul>

        <h3>Questions the project names</h3>
        <ul>
            <li>What cell types does the hippocampal formation contain, defined by morphology and connectivity, and how do they map onto transcriptomic types?</li>
            <li>What local and long-range circuit motifs does it contain?</li>
            <li>Which models of memory and spatial cognition do those circuits support, and which do they rule out?</li>
            <li>What would a whole-mouse-brain connectome cost, judged from the throughput this project achieves?</li>
        </ul>
    </div>

    <div class="section section-highlight">
        <h2 class="section-title">Method stack</h2>
        <div class="grid-md">
            <div class="card">
                <h3 class="card-title">EM imaging</h3>
                <p class="card-description">Multibeam SEM combined with ion-beam milling of semithin sections, building on the Lichtman lab's large-volume EM work.</p>
                <ul class="list-tight">
                    <li>Two 91-beam SEMs: Harvard and Princeton</li>
                    <li>Micro-CT to choose the volume</li>
                    <li>Image-quality monitoring and compression during acquisition</li>
                </ul>
            </div>

            <div class="card">
                <h3 class="card-title">Cloud processing</h3>
                <p class="card-description">Alignment, segmentation and analysis run on Google infrastructure, for a dataset expected to exceed 10 PB.</p>
                <ul class="list-tight">
                    <li>Flood-filling networks for neuron tracing</li>
                    <li>Automated synapse detection</li>
                    <li>Collaborative online proofreading</li>
                </ul>
            </div>

            <div class="card">
                <h3 class="card-title">Multimodal integration</h3>
                <p class="card-description">Planned links between the EM cell types and light-microscopy and single-cell gene-expression data. These are project aims, not released data.</p>
                <ul class="list-tight">
                    <li>Registration to the Allen mouse brain atlas</li>
                    <li>Connectivity types matched to transcriptomic types</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="section">
        <h2 class="section-title">Who is involved</h2>
        <p>Institutions as listed by Google Research when the award was announced in September 2023. Named people are those identified in public reporting; roles are not listed where no public source states them.</p>
        <div class="cards-grid">
            <div class="card dataset-card-blue">
                <h4>Harvard University</h4>
                <p><strong>Jeff Lichtman, principal investigator</strong><br>
                Leads the center; one of the two multibeam SEMs.</p>
            </div>

            <div class="card dataset-card-purple">
                <h4>Princeton University</h4>
                <p><strong>Sebastian Seung, collaborator</strong><br>
                Site of the second multibeam SEM.</p>
            </div>

            <div class="card dataset-card-cyan">
                <h4>Google Research</h4>
                <p><strong>Viren Jain</strong><br>
                Leads the machine-learning work, including flood-filling network segmentation.</p>
            </div>

            <div class="card dataset-card-orange">
                <h4>MIT</h4>
                <p><strong>Ila Fiete, investigator</strong></p>
            </div>

            <div class="card dataset-card-blue">
                <h4>Allen Institute</h4>
            </div>

            <div class="card dataset-card-purple">
                <h4>University of Cambridge</h4>
            </div>

            <div class="card dataset-card-cyan">
                <h4>Johns Hopkins University</h4>
                <p><strong>William Gray-Roncal</strong><br>
                Connectome quality assurance, community training, and data dissemination.</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2 class="section-title">Funding status</h2>
        <p>NIH award UM1NS132250 runs from September 2023 to August 2028. NIH RePORTER lists four budget-year awards, issued in September 2023, September 2024, August 2025 and August 2026 (checked 26 September 2026). Check <a href="https://reporter.nih.gov/project-details/UM1NS132250" target="_blank" rel="noopener">RePORTER</a> for the current record.</p>
    </div>

    <div class="section" id="dataset-access">
        <div class="checklist-box text-center">
            <h2>No data has been released yet</h2>
            <p>Data, browsers and analysis tools will be released as the project progresses. Until then, practice on the <a href="{{ '/datasets/' | relative_url }}">released public datasets</a>, follow the pipeline on the <a href="{{ '/datasets/workflow/' | relative_url }}">workflow tour</a>, and read the <a href="{{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}">case study</a> for what the project is building.</p>
        </div>
    </div>
</div>
