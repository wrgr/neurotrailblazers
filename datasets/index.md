---
layout: default
title: "Connectomics Datasets - Learning with Real Scientific Data"
description: "Explore curated connectomics datasets from landmark studies including Kasthuri, MICrONS, FlyWire, and more. Learn with the same data used by leading researchers."
---

<div class="main-content">
    <div class="hero" style="margin: -2rem -2rem 4rem -2rem; padding: 4rem 2rem;">
        <div class="hero-content">
            <h1>Connectomics Datasets</h1>
            <p class="hero-subtitle">Learn with real scientific data from groundbreaking research</p>
            <p class="hero-description">
                Explore carefully curated datasets from landmark connectomics studies. Each dataset represents years of cutting-edge research and offers unique insights into neural circuit organization.
            </p>
        </div>
    </div>

    <section class="section">
        <h2>Featured Datasets</h2>
        <p>These datasets represent milestones in connectomics research and provide excellent learning opportunities for students at all levels.</p>

        <div class="cards-grid" style="margin-top: 2rem;">
            <div class="card dataset-card" style="background: linear-gradient(135deg, #eff6ff, #dbeafe); border-left: 4px solid var(--neural-blue);">
                <div class="dataset-meta">
                    <span class="dataset-year">2015</span>
                    <span class="dataset-type">Mouse Cortex</span>
                </div>
                <h3 class="card-title">Kasthuri et al. - Visual Cortex</h3>
                <p class="card-description">
                    The first high-resolution connectome of mammalian cortex. This groundbreaking dataset revealed the complexity of cortical wiring and established many methods still used today.
                </p>
                <div style="margin: 1rem 0;">
                    <strong>Key Features:</strong>
                    <ul style="margin: 0.5rem 0 0 1rem; font-size: 0.9rem;">
                        <li>1,676 synapses mapped</li>
                        <li>Mouse visual cortex tissue</li>
                        <li>Serial electron microscopy</li>
                        <li>Detailed synapse analysis</li>
                    </ul>
                </div>
                <a href="{{ '/datasets/kasthuri2015' | relative_url }}" class="btn btn-primary" style="margin-top: 1rem;">Explore Dataset</a>
            </div>

            <div class="card dataset-card" style="background: linear-gradient(135deg, #f3e8ff, #ede9fe); border-left: 4px solid var(--cerebral-purple);">
                <div class="dataset-meta">
                    <span class="dataset-year">2024</span>
                    <span class="dataset-type">Complete Brain</span>
                </div>
                <h3 class="card-title">FlyWire - Adult Fly Brain</h3>
                <p class="card-description">
                    The first complete connectome of an adult animal brain. All 140,000 neurons and 50 million synapses mapped with unprecedented detail and accuracy.
                </p>
                <div style="margin: 1rem 0;">
                    <strong>Key Features:</strong>
                    <ul style="margin: 0.5rem 0 0 1rem; font-size: 0.9rem;">
                        <li>Complete adult brain mapping</li>
                        <li>Collaborative proofreading</li>
                        <li>Cell type classification</li>
                        <li>Interactive exploration tools</li>
                    </ul>
                </div>
                <a href="{{ '/datasets/flywire2024' | relative_url }}" class="btn btn-primary" style="margin-top: 1rem;">Explore Dataset</a>
            </div>

            <div class="card dataset-card" style="background: linear-gradient(135deg, #ecfeff, #cffafe); border-left: 4px solid var(--axon-cyan);">
                <div class="dataset-meta">
                    <span class="dataset-year">2025</span>
                    <span class="dataset-type">Structure + Function</span>
                </div>
                <h3 class="card-title">MICrONS - Mouse Visual Cortex</h3>
                <p class="card-description">
                    Revolutionary dataset combining structural connectomics with functional recordings. Links neural connectivity to actual brain activity during vision.
                </p>
                <div style="margin: 1rem 0;">
                    <strong>Key Features:</strong>
                    <ul style="margin: 0.5rem 0 0 1rem; font-size: 0.9rem;">
                        <li>100,000+ neurons mapped</li>
                        <li>Simultaneous functional data</li>
                        <li>Visual stimulus responses</li>
                        <li>AI-assisted analysis</li>
                    </ul>
                </div>
                <a href="{{ '/datasets/microns2025' | relative_url }}" class="btn btn-primary" style="margin-top: 1rem;">Explore Dataset</a>
            </div>
        </div>
    </section>

    <section class="section">
        <h2>Historical Foundations</h2>
        <p>These classical datasets laid the groundwork for modern connectomics research and remain valuable for understanding fundamental principles.</p>

        <div class="cards-grid">
            <div class="card">
                <div class="dataset-meta">
                    <span class="dataset-year">1986</span>
                    <span class="dataset-type">Complete Worm</span>
                </div>
                <h3 class="card-title">C. elegans Connectome</h3>
                <p class="card-description">
                    The first complete nervous system ever mapped. White et al.'s pioneering work on the nematode worm established the field of connectomics.
                </p>
                <a href="{{ '/datasets/white1986' | relative_url }}" class="btn btn-secondary" style="margin-top: 1rem;">Learn More</a>
            </div>

            <div class="card">
                <div class="dataset-meta">
                    <span class="dataset-year">2011</span>
                    <span class="dataset-type">Mouse Retina</span>
                </div>
                <h3 class="card-title">Bock et al. - Retinal Circuits</h3>
                <p class="card-description">
                    Detailed mapping of mouse retinal circuits that process visual information. Revealed how retinal neurons are wired to detect motion and other features.
                </p>
                <a href="{{ '/datasets/bock2011' | relative_url }}" class="btn btn-secondary" style="margin-top: 1rem;">Learn More</a>
            </div>

            <div class="card">
                <div class="dataset-meta">
                    <span class="dataset-year">2020</span>
                    <span class="dataset-type">Fly Brain</span>
                </div>
                <h3 class="card-title">Hemibrain - Fly Central Brain</h3>
                <p class="card-description">
                    Comprehensive mapping of the Drosophila central brain, providing insights into neural circuits for learning, memory, and behavior.
                </p>
                <a href="{{ '/datasets/hemibrain2020' | relative_url }}" class="btn btn-secondary" style="margin-top: 1rem;">Learn More</a>
            </div>
        </div>
    </section>

    <section class="section">
        <h2>🔍 Dataset Categories</h2>
        <p>Connectomics datasets vary in scope, species, and methodology. Understanding these categories helps you choose the right data for your learning goals.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: var(--brain-gray); padding: 1.5rem; border-radius: 12px;">
                <h3 style="color: var(--neural-blue); margin-bottom: 1rem;">🧠 By Species</h3>
                <ul style="color: #4b5563; margin: 0; line-height: 1.8;">
                    <li><strong>C. elegans:</strong> Simple, complete nervous system (302 neurons)</li>
                    <li><strong>Drosophila:</strong> Complex invertebrate brain (~140,000 neurons)</li>
                    <li><strong>Mouse:</strong> Mammalian cortical circuits (millions of neurons)</li>
                    <li><strong>Human:</strong> Small cortical samples (thousands of neurons)</li>
                </ul>
            </div>

            <div style="background: var(--brain-gray); padding: 1.5rem; border-radius: 12px;">
                <h3 style="color: var(--cerebral-purple); margin-bottom: 1rem;">🔬 By Resolution</h3>
                <ul style="color: #4b5563; margin: 0; line-height: 1.8;">
                    <li><strong>Synaptic:</strong> Individual synapses and connections</li>
                    <li><strong>Cellular:</strong> Complete neuronal morphologies</li>
                    <li><strong>Circuit:</strong> Functional neural networks</li>
                    <li><strong>Regional:</strong> Large-scale brain organization</li>
                </ul>
            </div>

            <div style="background: var(--