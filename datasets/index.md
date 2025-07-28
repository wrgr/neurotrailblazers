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
    <h2>HI-MC Spotlight</h2>
    <div class="dataset-card featured spotlight">
      <div class="dataset-header">
        <div class="dataset-icon">🚀</div>
        <div class="dataset-meta">
          <span class="dataset-type">Whole Mouse Brain</span>
          <span class="dataset-status">In Progress</span>
        </div>
      </div>
      <h3><a href="/hi-mc">High-throughput Imaging for Mouse Connectomics (HI-MC)</a></h3>
      <p>A flagship NIH CONNECTS effort to generate a scalable, synapse-resolution map of the entire mouse brain.</p>
      <ul class="dataset-facts">
        <li><strong>Species:</strong> Mouse</li>
        <li><strong>Planned Volume:</strong> Whole brain</li>
        <li><strong>Estimated Size:</strong> &gt;20 PB</li>
      </ul>
      <div class="dataset-actions">
        <a href="/hi-mc" class="btn btn-primary">Project Details</a>
        <a href="/workflow" class="btn btn-secondary">View Pipeline</a>
      </div>
    </div>
  </section>

  <section class="section">
    <h2>Connectomics Timeline</h2>
    <div class="timeline">
      <div class="timeline-item">
        <div class="timeline-year">1986</div>
        <div class="timeline-content">
          <h3 class="card-title">C. elegans Connectome</h3>
          <p class="card-description">The first complete nervous system ever mapped, establishing the field of connectomics.</p>
          <ul class="dataset-facts">
            <li><strong>Species:</strong> C. elegans</li>
            <li><strong>Neurons:</strong> 302</li>
            <li><strong>Size:</strong> &lt;1 GB</li>
          </ul>
          <a href="{{ '/datasets/white1986' | relative_url }}" class="btn btn-secondary">Learn More</a>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-year">2011</div>
        <div class="timeline-content">
          <h3 class="card-title">Bock et al. - Retinal Circuits</h3>
          <p class="card-description">Mapping of mouse retinal circuits for visual motion detection.</p>
          <ul class="dataset-facts">
            <li><strong>Species:</strong> Mouse</li>
            <li><strong>Volume:</strong> ~250 μm³</li>
            <li><strong>Size:</strong> ~2 TB</li>
          </ul>
          <a href="{{ '/datasets/bock2011' | relative_url }}" class="btn btn-secondary">Learn More</a>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-year">2015</div>
        <div class="timeline-content">
          <h3 class="card-title">Kasthuri et al. - Visual Cortex</h3>
          <p class="card-description">First high-resolution connectome of mammalian cortex.</p>
          <ul class="dataset-facts">
            <li><strong>Species:</strong> Mouse</li>
            <li><strong>Region:</strong> Visual cortex (exact area unspecified)</li>
            <li><strong>Size:</strong> ~1 TB</li>
          </ul>
          <a href="{{ '/datasets/kasthuri2015' | relative_url }}" class="btn btn-primary">Explore Dataset</a>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-year">2020</div>
        <div class="timeline-content">
          <h3 class="card-title">Hemibrain - Fly Central Brain</h3>
          <p class="card-description">Comprehensive mapping of the Drosophila central brain.</p>
          <ul class="dataset-facts">
            <li><strong>Species:</strong> Drosophila</li>
            <li><strong>Neurons:</strong> ~25,000</li>
            <li><strong>Size:</strong> ~30 TB</li>
          </ul>
          <a href="{{ '/datasets/hemibrain2020' | relative_url }}" class="btn btn-secondary">Learn More</a>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-year">2024</div>
        <div class="timeline-content">
          <h3 class="card-title">FlyWire - Adult Fly Brain</h3>
          <p class="card-description">First complete connectome of an adult animal brain.</p>
          <ul class="dataset-facts">
            <li><strong>Species:</strong> Drosophila</li>
            <li><strong>Neurons:</strong> 140,000</li>
            <li><strong>Size:</strong> 50 TB</li>
          </ul>
          <a href="{{ '/datasets/flywire2024' | relative_url }}" class="btn btn-primary">Explore Dataset</a>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-year">2025</div>
        <div class="timeline-content">
          <h3 class="card-title">MICrONS - Mouse Visual Cortex</h3>
          <p class="card-description">Links structural connectomics with functional recordings.</p>
          <ul class="dataset-facts">
            <li><strong>Species:</strong> Mouse</li>
            <li><strong>Volume:</strong> ~1 mm³</li>
            <li><strong>Size:</strong> ~100 TB</li>
          </ul>
          <a href="{{ '/datasets/microns2025' | relative_url }}" class="btn btn-primary">Explore Dataset</a>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-year">2023–2028</div>
        <div class="timeline-content">
          <h3 class="card-title">MouseConnects</h3>
          <p class="card-description">A complete synapse-level reconstruction of mouse hippocampal formation.</p>
          <ul class="dataset-facts">
            <li><strong>Species:</strong> Mouse</li>
            <li><strong>Volume:</strong> 10 mm³</li>
            <li><strong>Size:</strong> 10 PB</li>
          </ul>
          <a href="/datasets/mouseconnects" class="btn btn-primary">Explore Project</a>
        </div>
      </div>
    </div>
  </section>
</div>
