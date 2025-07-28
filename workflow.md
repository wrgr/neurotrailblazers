---
layout: default
title: "Connectomics Workflow"
description: "Learn the complete pipeline for nanoscale connectomics research, from sample preparation to circuit analysis"
---

<div class="hero-section">
  <div class="hero-content">
    <div class="hero-text">
      <h1>Nanoscale Connectomics Workflow</h1>
      <p class="hero-subtitle">From Mouse Brain to Circuit Maps</p>
      <p class="hero-description">
        Discover the cutting-edge pipeline used in the MouseConnects project to create 
        the first synapse-level connectome of a mammalian brain region.
      </p>
    </div>
    <div class="hero-visual">
      <div class="workflow-preview">
        <div class="pipeline-step">Sample</div>
        <div class="pipeline-arrow">→</div>
        <div class="pipeline-step">Image</div>
        <div class="pipeline-arrow">→</div>
        <div class="pipeline-step">Segment</div>
        <div class="pipeline-arrow">→</div>
        <div class="pipeline-step">Analyze</div>
      </div>
    </div>
  </div>
</div>

<div class="container">
  <div class="workflow-overview">
    <h2>The MouseConnects Pipeline</h2>
    <p>
      The MouseConnects project represents the most ambitious connectomics effort to date, 
      aiming to reconstruct 10 mm³ of mouse hippocampal formation at nanometer resolution. 
      This workflow demonstrates how modern neuroscience combines advanced imaging, 
      machine learning, and massive computational resources.
    </p>
    
    <div class="workflow-stats">
      <div class="stat-card">
        <div class="stat-number">10 mm³</div>
        <div class="stat-label">Brain Volume</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">10 PB</div>
        <div class="stat-label">Data Generated</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">8 nm</div>
        <div class="stat-label">Resolution</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">50x</div>
        <div class="stat-label">Larger than Previous</div>
      </div>
    </div>
  </div>

  <div class="workflow-steps">
    <h2>Complete Workflow Pipeline</h2>
    
    <div class="step-container">
      <div class="step-number">1</div>
      <div class="step-content">
        <h3>Sample Preparation & Staining</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              Whole mouse brains are fixed and stained with heavy metals (osmium tetroxide) 
              to create contrast for electron microscopy. The new ODeCO protocol ensures 
              uniform staining across large volumes.
            </p>
            <ul>
              <li>Transcardiac perfusion with specialized fixatives</li>
              <li>ODeCO staining protocol for whole brains</li>
              <li>MicroCT imaging for quality control</li>
              <li>Registration to Allen Brain Atlas</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Heavy Metal Staining</span>
            <span class="tech-tag">MicroCT Imaging</span>
            <span class="tech-tag">Atlas Registration</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">2</div>
      <div class="step-content">
        <h3>Serial Sectioning & Mounting</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              Stained brains are cut into semithin sections (200-1000 nm thick) and 
              mounted on silicon wafers using magnetic collection technology.
            </p>
            <ul>
              <li>Precision ultramicrotomy for consistent sections</li>
              <li>MagC magnetic collection onto silicon wafers</li>
              <li>Light microscopy mapping of sections</li>
              <li>ROI selection for high-resolution imaging</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Ultramicrotomy</span>
            <span class="tech-tag">MagC Collection</span>
            <span class="tech-tag">Wafer Mapping</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">3</div>
      <div class="step-content">
        <h3>High-Resolution EM Imaging</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              Novel mSEM-IBEAM systems combine multibeam scanning electron microscopy 
              with ion beam milling to image at 8 nm isotropic resolution.
            </p>
            <ul>
              <li>91-beam scanning electron microscopes</li>
              <li>Ion beam etching and milling (IBEAM)</li>
              <li>Automated imaging across multiple sites</li>
              <li>Real-time quality monitoring</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">mSEM-IBEAM</span>
            <span class="tech-tag">Multibeam SEM</span>
            <span class="tech-tag">Ion Beam Milling</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">4</div>
      <div class="step-content">
        <h3>Data Processing & Management</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              Massive datasets are transferred to Google Cloud, aligned, and prepared 
              for automated segmentation using advanced compression techniques.
            </p>
            <ul>
              <li>Lossless compression and cloud transfer</li>
              <li>3D alignment and stitching</li>
              <li>Denoising and lossy compression</li>
              <li>Quality monitoring pipeline</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Google Cloud</span>
            <span class="tech-tag">Image Compression</span>
            <span class="tech-tag">3D Alignment</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">5</div>
      <div class="step-content">
        <h3>Automated Segmentation</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              Machine learning algorithms trace every neuron and identify all synapses 
              to create the connectome. Flood-filling networks achieve state-of-the-art accuracy.
            </p>
            <ul>
              <li>Flood-filling networks for neuron tracing</li>
              <li>Semantic segmentation for tissue types</li>
              <li>Automated synapse detection</li>
              <li>3D reconstruction and validation</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Deep Learning</span>
            <span class="tech-tag">Flood-Filling Networks</span>
            <span class="tech-tag">Synapse Detection</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">6</div>
      <div class="step-content">
        <h3>Proofreading & Validation</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              Human experts and community contributors validate and correct automated 
              reconstructions using collaborative web-based tools.
            </p>
            <ul>
              <li>ChunkedGraph collaborative editing</li>
              <li>CAVE proofreading interface</li>
              <li>Community-driven validation</li>
              <li>Version control for reconstructions</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">ChunkedGraph</span>
            <span class="tech-tag">CAVE Interface</span>
            <span class="tech-tag">Web Collaboration</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">7</div>
      <div class="step-content">
        <h3>Integration & Cell Typing</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              Connectomic data is integrated with transcriptomic, physiological, and 
              morphological data to define comprehensive cell types.
            </p>
            <ul>
              <li>Patch-seq physiological recordings</li>
              <li>fMOST whole-brain morphology</li>
              <li>Cross-modal cell type matching</li>
              <li>Multi-modal data integration</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Patch-seq</span>
            <span class="tech-tag">fMOST</span>
            <span class="tech-tag">Multi-modal Integration</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">8</div>
      <div class="step-content">
        <h3>Circuit Analysis & Discovery</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              The complete connectome enables unprecedented analysis of hippocampal 
              circuits, revealing new insights into memory and spatial navigation.
            </p>
            <ul>
              <li>Local microcircuit motif analysis</li>
              <li>Long-range connectivity patterns</li>
              <li>Circuit mechanism discovery</li>
              <li>Computational model validation</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Graph Analysis</span>
            <span class="tech-tag">Circuit Modeling</span>
            <span class="tech-tag">Network Science</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">9</div>
      <div class="step-content">
        <h3>Open Data Sharing</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              All data, tools, and discoveries are made freely available to the global 
              research community through advanced web interfaces and APIs.
            </p>
            <ul>
              <li>Neuroglancer visualization platform</li>
              <li>Science API for data access</li>
              <li>Educational outreach programs</li>
              <li>Community tool development</li>
            </ul>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Neuroglancer</span>
            <span class="tech-tag">Science API</span>
            <span class="tech-tag">Open Science</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="learning-pathways">
    <h2>Learn This Workflow</h2>
    <p>
      Ready to dive deeper? Our educational modules guide you through each step 
      of the connectomics pipeline with hands-on exercises and real data.
    </p>
    
    <div class="pathway-cards">
      <div class="pathway-card">
        <h3>👁️ Module 2: Sample Preparation</h3>
        <p>Learn tissue processing and staining techniques for EM</p>
        <a href="/modules/module02.md" class="btn btn-primary">Start Learning</a>
      </div>
      
      <div class="pathway-card">
        <h3>🔬 Module 5: EM Imaging</h3>
        <p>Understand electron microscopy and acquisition methods</p>
        <a href="/modules/module05.md" class="btn btn-primary">Start Learning</a>
      </div>
      
      <div class="pathway-card">
        <h3>🤖 Module 8: AI Segmentation</h3>
        <p>Explore machine learning for neuron reconstruction</p>
        <a href="/modules/module08.md" class="btn btn-primary">Start Learning</a>
      </div>
      
      <div class="pathway-card">
        <h3>🧠 Module 12: Circuit Analysis</h3>
        <p>Analyze connectivity patterns and discover circuits</p>
        <a href="/modules/module12.md" class="btn btn-primary">Start Learning</a>
      </div>
    </div>
  </div>

  <div class="next-steps">
    <h2>Ready to Get Started?</h2>
    <div class="cta-grid">
      <div class="cta-card">
        <h3>🚀 Begin Your Journey</h3>
        <p>Start with Module 0 to understand the big picture and find your path</p>
        <a href="/modules/inspiration" class="btn btn-primary">Module 0: Inspiration</a>
      </div>
      
      <div class="cta-card">
        <h3>📊 Explore Real Data</h3>
        <p>Dive into actual connectomics datasets from leading research projects</p>
        <a href="/datasets/" class="btn btn-secondary">Browse Datasets</a>
      </div>
      
      <div class="cta-card">
        <h3>👥 Find Your Archetype</h3>
        <p>See how students like you navigate connectomics research</p>
        <a href="/archetypes/" class="btn btn-secondary">Student Stories</a>
      </div>
    </div>
  </div>
</div>

<style>
.workflow-preview {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.1) 0%, rgba(124, 58, 237, 0.1) 100%);
  border-radius: 1rem;
  border: 2px solid rgba(37, 99, 235, 0.2);
}

.pipeline-step {
  background: var(--neural-blue);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-weight: 600;
  white-space: nowrap;
}

.pipeline-arrow {
  color: var(--neural-blue);
  font-size: 1.5rem;
  font-weight: bold;
}

.workflow-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin: 3rem 0;
}

.stat-card {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  color: var(--neural-blue);
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #6b7280;
  font-weight: 500;
}

.workflow-steps {
  margin: 4rem 0;
}

.step-container {
  display: flex;
  gap: 2rem;
  margin-bottom: 3rem;
  padding: 2rem;
  background: white;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border-left: 4px solid var(--neural-blue);
}

.step-number {
  flex-shrink: 0;
  width: 3rem;
  height: 3rem;
  background: var(--neural-blue);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.25rem;
}

.step-content {
  flex: 1;
}

.step-content h3 {
  color: var(--neural-blue);
  margin-bottom: 1rem;
}

.step-details {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.step-description ul {
  margin-top: 1rem;
  color: #6b7280;
}

.step-tech h4 {
  color: var(--cerebral-purple);
  margin-bottom: 1rem;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.tech-tag {
  display: inline-block;
  background: rgba(124, 58, 237, 0.1);
  color: var(--cerebral-purple);
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  margin: 0.25rem 0.25rem 0.25rem 0;
  border: 1px solid rgba(124, 58, 237, 0.2);
}

.pathway-cards, .cta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.pathway-card, .cta-card {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.pathway-card:hover, .cta-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.pathway-card h3, .cta-card h3 {
  color: var(--neural-blue);
  margin-bottom: 1rem;
}

.next-steps {
  background: linear-gradient(135deg, var(--brain-gray) 0%, white 100%);
  padding: 3rem;
  border-radius: 1rem;
  margin-top: 4rem;
  text-align: center;
}

@media (max-width: 768px) {
  .workflow-preview {
    flex-direction: column;
    text-align: center;
  }
  
  .step-container {
    flex-direction: column;
    gap: 1rem;
  }
  
  .step-details {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .workflow-stats {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>