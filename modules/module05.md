---

title: "Module 05: From Pixels to Proofreading: Image Segmentation and Quality Control"
layout: module
description: "Discover how neural structures are segmented from raw EM images and how humans proofread to ensure accuracy."
module\_number: 5
difficulty: "Intermediate"
duration: "3-4 hours"
learning\_objectives:

* "Explain the concept of image segmentation in connectomics"
* "Understand the role of neural networks in segmenting EM volumes"
* "Learn how human proofreading improves segmentation accuracy"
* "Perform basic proofreading tasks using Neuroglancer"
  prerequisites: "Module 4 and familiarity with EM imaging"
  merit\_stage: "Experiment"
  compass\_skills: \["Scientific Visualization", "Attention to Detail", "Collaboration"]
  ccr\_focus: \["Skills - Data Integrity", "Character - Grit"]

---

<div class="main-content">
  <div class="hero">
    <div class="hero-content">
      <span class="module-number">Module 05</span>
      <h1>{{ page.title }}</h1>
      <p class="hero-subtitle">{{ page.description }}</p>
    </div>
  </div>

  <section class="section">
    <h2>🧠 What is Segmentation?</h2>
    <p>Segmentation is the process of identifying and labeling structures in an image. In connectomics, this means separating each neurite (axon or dendrite) and assigning it a unique label. Most current approaches rely on deep learning to automate this step.</p>
    <ul>
      <li>Flood-filling networks</li>
      <li>U-Net and 3D CNNs</li>
      <li>Segmentation errors: mergers and splits</li>
    </ul>
  </section>

  <section class="section">
    <h2>🛠️ Proofreading 101</h2>
    <p>No segmentation algorithm is perfect. Humans review and correct the machine-generated output, a process known as proofreading. Tools like Neuroglancer allow users to inspect 3D reconstructions slice-by-slice and validate continuity.</p>
    <ul>
      <li>Common proofreading errors and their consequences</li>
      <li>Using visual cues to spot mergers/splits</li>
      <li>Basic workflow: select, inspect, edit</li>
    </ul>
  </section>

  <section class="section">
    <h2>🔬 Quality Metrics and Feedback Loops</h2>
    <p>Segmentation quality can be quantified using metrics like Rand score and edge accuracy. Proofread corrections can also be used to retrain models, creating a virtuous cycle of improvement.</p>
    <ul>
      <li>Manual vs. automated QA</li>
      <li>Using corrections to improve models</li>
      <li>Tracking proofreading contributions</li>
    </ul>
  </section>

  <section class="section">
    <h2>🎯 COMPASS Integration</h2>
    <ul>
      <li><strong>Knowledge:</strong> Understanding EM segmentation outputs</li>
      <li><strong>Skills:</strong> Visual discrimination, 3D spatial reasoning, data quality assessment</li>
      <li><strong>Character:</strong> Persistence, humility, teamwork</li>
      <li><strong>Meta-Learning:</strong> Adapting to evolving tools and methods</li>
    </ul>
  </section>

  <section class="section">
    <h2>📚 References & Resources</h2>
    <ul>
      <li>Januszewski et al., 2018. <em>High-precision automated reconstruction of neurons with flood-filling networks</em>. Nature Methods.</li>
      <li>Neuroglancer: <a href="https://github.com/google/neuroglancer">github.com/google/neuroglancer</a></li>
      <li>SNEMI3D Benchmark: <a href="https://cremi.org">cremi.org</a></li>
    </ul>
  </section>

  <section class="section">
    <h2>✅ Assessment</h2>
    <ul>
      <li>Define and explain the purpose of segmentation in connectomics</li>
      <li>Correct a sample proofreading task using Neuroglancer</li>
      <li>Describe how proofreading improves final circuit reconstructions</li>
    </ul>
  </section>
</div>
