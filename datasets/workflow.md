---
layout: dataset
title: "MouseConnects Connectomics Workflow"
description: "A step-by-step tour of the nanoscale connectomics pipeline — fixation through circuit analysis — using the MouseConnects HI-MC hippocampus project as the running example, with links into the units that teach each step."
permalink: /datasets/workflow/
slug: workflow
track: research-in-action
pathways:
  - research workflow
  - reproducibility
summary: "Seven pipeline steps from fixation to circuit analysis, with the HI-MC project's numbers and a depth link into the unit that teaches each step."
modality: "Electron microscopy pipeline"
species: "Mouse"
scale: "Whole-project operational workflow"
access_level: "Educational documentation"
use_cases:
  - Pipeline orientation
  - Methods training
  - Connectomics workflow teaching
recommended_modules:
  - module01
  - module02
  - module04
  - module05
  - module08
related_tools:
  - ask-an-expert
  - connectome-quality
related_frameworks:
  - research-incubator-model
  - education-models
resource_links: []
last_reviewed: 2026-03-09
maintainer: NeuroTrailblazers Team
use_layout_hero: false
content_type: core
---

<div class="main-content">
<div class="hero hero-spaced hero-rounded">
  <div class="hero-content">
    <div class="hero-text">
      <h1>MouseConnects Nanoscale Connectomics Workflow</h1>
      <p class="hero-subtitle">The pipeline, one step at a time</p>
      <p class="hero-description">
        A walkable tour of how a block of brain tissue becomes a synapse-level wiring
        diagram, using the MouseConnects HI-MC hippocampus project as the running
        example. Every step links to the training unit that teaches it in depth.
      </p>
    </div>
    <div class="hero-visual">
      <div class="workflow-preview">
        <div class="pipeline-step">Prep</div>
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
      MouseConnects, funded through the NIH BRAIN Initiative's BRAIN CONNECTS program
      from 2023 to 2028, aims to reconstruct the synaptic connectome of the mouse
      hippocampus — roughly 10 mm³ spanning CA1, CA3, and the dentate gyrus. That is
      about ten times the volume of MICrONS, the largest comparable reconstruction,
      and the expected dataset exceeds 10 petabytes of raw imagery. The project's
      center, HI-MC (the Center for High-throughput Integrative Mouse Connectomics),
      is led by Jeff Lichtman at Harvard and Viren Jain at Google Research, with
      collaborators across multiple institutions. The full scientific case — why the
      hippocampus, which theories the connectome can test — is in the
      <a href="{{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}">MouseConnects and HI-MC case study</a>.
    </p>
    <p>
      This page walks the pipeline that turns that tissue into a queryable wiring
      diagram. Each step below says what happens, what makes it hard, and what a
      failure there costs everyone downstream — because the defining property of this
      pipeline is that nothing is ever really fixed later. A staining defect becomes a
      segmentation error becomes a proofreading cost becomes a wrong number in an
      analysis. One caution before you quote anything: every count derived from a
      connectome is a property of a particular data release, not of the tissue.
      <a href="{{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}">Provenance and versioning</a>
      explains why, and the case study repeats the warning where the numbers live.
    </p>

    <div class="workflow-stats">
      <div class="stat-card">
        <div class="stat-number">10 mm³</div>
        <div class="stat-label">Target volume (hippocampus)</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">&gt;10 PB</div>
        <div class="stat-label">Expected raw imagery</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">10×</div>
        <div class="stat-label">The MICrONS volume (1 mm³)</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">2023–2028</div>
        <div class="stat-label">Funded project timeline</div>
      </div>
    </div>
  </div>

  <div class="workflow-steps">
    <h2>The Seven Steps</h2>

    <div class="step-container">
      <div class="step-number">1</div>
      <div class="step-content">
        <h3>Fixation and Staining</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              The tissue is fixed by transcardial perfusion with a buffered aldehyde
              mix — typically around 2–2.5% glutaraldehyde plus 2% paraformaldehyde —
              to arrest ultrastructure within seconds, before autolysis and osmotic
              swelling distort the fine processes you are about to spend years
              tracing. Then, because biological tissue is nearly transparent to
              electrons, contrast is created chemically: a sequence of heavy-metal
              stains (the rOTO protocol — reduced osmium, thiocarbohydrazide, a
              second osmium — followed by uranyl acetate and lead) deposits metal on
              membranes, which is what you actually see in an EM image.
            </p>
            <p>
              The hard part at HI-MC scale is uniformity. Stain has to penetrate the
              entire block, and a block that is well stained at the edges and pale in
              the center produces segmentation quality that varies systematically
              with position — which can masquerade as a biological gradient. Weak
              membrane contrast is the single most expensive prep failure, because it
              is the dominant cause of automated merge errors: the network cannot
              find a boundary that is barely there.
            </p>
            <p>
              One cost is unavoidable and worth knowing now: dehydration and resin
              embedding shrink tissue on the order of 5–20% linearly. Every absolute
              length, area, and volume measurement in EM connectomics inherits that
              distortion, which is why careful papers report ratios within a volume
              rather than absolute values compared across studies.
            </p>
            <p class="step-depth">
              <strong>Depth:</strong>
              <a href="{{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}">Unit 03: EM prep and imaging</a>
              — the full preparation chain, with the artifact catalog that pairs each
              step with its characteristic failure.
            </p>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Aldehyde Fixation</span>
            <span class="tech-tag">rOTO Staining</span>
            <span class="tech-tag">Resin Embedding</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">2</div>
      <div class="step-content">
        <h3>Serial Sectioning</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              An ultramicrotome with a diamond knife cuts the embedded block into
              sections 30–50 nm thick — around a thousand sections per 40 µm of
              depth — collected onto tape (ATUM) or a reinforced substrate. HI-MC
              uses this serial-section approach, building on the Lichtman lab's
              decades of experience with it, for a decisive reason: sectioning does
              not consume the block. Sections can be re-imaged if something goes
              wrong, and imaging can be parallelized across many microscopes, which
              is how petascale volumes get acquired in finite time.
            </p>
            <p>
              The price is section handling, and section handling has a signature
              artifact list: lost sections, folds, wrinkles, knife chatter,
              compression along the cutting axis, debris. Each is survivable in
              isolation; what matters is the downstream bill. A lost section is a gap
              the alignment stage must interpolate across and the segmentation model
              was never trained on. A fold makes a region of tissue simply
              untraceable. At 10 mm³ — hundreds of thousands of sections — even a
              small per-section failure rate is a large absolute number, so the
              operational discipline is catching problems while the block still
              exists to recut.
            </p>
            <p class="step-depth">
              <strong>Depth:</strong>
              <a href="{{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}">Unit 03 §1.4 and §2</a>
              — sectioning versus block-face approaches, and the artifact catalog
              with each defect's downstream cost.
            </p>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Ultramicrotomy</span>
            <span class="tech-tag">Tape Collection (ATUM)</span>
            <span class="tech-tag">Section QA</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">3</div>
      <div class="step-content">
        <h3>High-Throughput EM Imaging</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              The sections are imaged by scanning electron microscopes at nanometer
              resolution — voxels on the order of 4 × 4 × 40 nm are typical for
              volumes like this. The arithmetic is the whole story. An 800 µm cube
              at that resolution is 8 × 10¹⁴ pixels; at a sustained 0.2 gigapixels
              per second that is 46 days of continuous imaging, and roughly 77 days
              at a realistic 60% duty cycle — before sectioning, QA, or re-imaging
              failed sections. Multibeam SEM attacks that throughput term directly,
              scanning with 61 or 91 beams in parallel to aggregate on the order of
              a gigapixel per second; it is the technology that moved 1 mm³ from
              impossible to an eighteen-month project. HI-MC is a 10 mm³ target,
              which is why sustained multi-instrument operation over years is built
              into the plan.
            </p>
            <p>
              The core tradeoff is dose. Image quality improves roughly with the
              square root of electron dose, so doubling the signal-to-noise ratio
              costs about four times the acquisition time. At petascale, "just image
              it better" is rarely the answer; the honest move is usually to accept
              a noisier image and spend the savings on better segmentation and more
              proofreading. Failure at this step — drift, charging, defocus that
              nobody caught — is uniquely expensive because acquisition is the one
              stage you cannot rerun from disk: the QA has to happen while the
              instrument is still pointed at the section.
            </p>
            <p class="step-depth">
              <strong>Depth:</strong>
              <a href="{{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}">Unit 03 §1.5 and §3</a>
              — imaging parameters and the acquisition QA gates that decide when to
              stop the microscope.
            </p>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Multibeam SEM</span>
            <span class="tech-tag">Dose Budgeting</span>
            <span class="tech-tag">Live Acquisition QA</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">4</div>
      <div class="step-content">
        <h3>Alignment and Reconstruction Infrastructure</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              The microscope produces tiles; science needs one coherent 3D volume.
              First the raw tiles land in an immutable, checksummed archive — the
              only irreplaceable asset in the project, since everything downstream
              is recomputable from it, expensively. Then stitching places tiles
              within each section, and alignment registers each section to its
              neighbors. Alignment is the hard half, because sections deform
              non-rigidly — knife compression, folds, stretch — and because errors
              accumulate: a bias of 0.1 voxel per section across 20,000 sections is
              a 2,000-voxel drift. Modern pipelines use coarse-to-fine elastic
              registration with a global relaxation step that spreads residual
              error across the whole stack instead of letting it pile up in one
              direction.
            </p>
            <p>
              The infrastructure numbers explain why HI-MC is a cloud project. A
              single 1 mm³ volume at 4 × 4 × 40 nm is about 1.5 × 10¹⁵ voxels:
              roughly 1.5 PB of raw archive, another ~2 PB for the aligned image
              pyramid, and comparable transient volumes for the model predictions
              that feed segmentation. HI-MC is ten of those. At this scale, moving
              data is often more expensive than storing it — egress on a petabyte
              can cost more than a year of storage — so compute goes to the data,
              not the reverse.
            </p>
            <p>
              Failure here is subtle rather than dramatic: a misalignment does not
              destroy data, it quietly severs every neurite that crosses the bad
              seam, and the segmentation stage will faithfully turn that seam into
              a wall of split errors. And because every stored annotation
              coordinate is defined in the aligned space, revising an alignment
              later means re-mapping everything — which is why alignment revisions
              are rare and carefully planned.
            </p>
            <p class="step-depth">
              <strong>Depth:</strong>
              <a href="{{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}">Unit 04: Volume reconstruction infrastructure</a>
              — the eight-stage reference pipeline, storage layout, and the
              capacity-and-cost arithmetic worked in full.
            </p>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Elastic Registration</span>
            <span class="tech-tag">Cloud Storage</span>
            <span class="tech-tag">Immutable Archives</span>
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
              No human traces 10 mm³. Machine learning does the first pass, in two
              main families. In the affinity approach, a network predicts for every
              pair of neighboring voxels whether they belong to the same object;
              watershed then produces deliberately-too-small supervoxels, and an
              agglomeration step merges them into neurons. In flood-filling networks
              (FFNs) — developed at Google Research and the planned workhorse for
              HI-MC, as for FlyWire before it — a network grows one object at a time
              from a seed, repeatedly asking whether the next voxel belongs. A
              separate model detects synapses and assigns their partners.
            </p>
            <p>
              The compute is significant — on the order of 1,700 GPU-days per cubic
              millimeter at typical throughputs, and pipelines budget for three to
              five full inference passes because the first model version is never
              the last — but the deeper design decision is about error. The whole
              stack is deliberately tuned to over-segment: it prefers splits (one
              neuron in pieces) to merges (two neurons fused), because a split
              leaves visible evidence of itself while a merge produces an object
              that looks like a neuron and is not. Where segmentation fails is
              structural and predictable: thin spine necks that appear in only one
              or two sections, processes crossing sections at shallow angles,
              tightly apposed membranes with weak staining, and artifact regions
              the model never saw in training.
            </p>
            <p class="step-depth">
              <strong>Depth:</strong>
              <a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08 §1–2</a>
              for how the methods work and fail;
              <a href="{{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}">Unit 04</a>
              for the supervoxel architecture that makes the output editable at all.
            </p>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Flood-Filling Networks</span>
            <span class="tech-tag">Affinity + Watershed</span>
            <span class="tech-tag">Synapse Detection</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">6</div>
      <div class="step-content">
        <h3>Proofreading and Quality Control</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              Automated segmentation is good and wrong: wrong in ways that are
              individually small and collectively decisive. Humans correct it using
              CAVE — the Connectome Annotation Versioning Engine, built for FlyWire
              and MICrONS and serving as HI-MC's backend — which represents the
              segmentation as an editable graph over immutable supervoxels, so
              thousands of proofreaders can split and merge concurrently with every
              edit versioned. This is where NeuroTrailblazers connects most directly
              to the project: proofreading and annotation at this scale is a trained
              workforce problem, and trained contributors can work on real data.
            </p>
            <p>
              It is also the pipeline's dominant cost. Compute and storage are line
              items you can negotiate with a cloud vendor; proofreading is a hiring,
              training, and quality-management problem, at a few hours of skilled
              attention per fully proofread neuron. And complete manual proofreading
              of 10 mm³ is almost certainly infeasible — the case study is explicit
              about this — so HI-MC will need strategies that combine automated
              error detection with targeted human review of the circuits that
              matter most. That turns proofreading into an allocation problem under
              a fixed budget: which errors, on which cells, checked to what defined
              standard, with a stopping rule written down in advance.
            </p>
            <p>
              Failure at this step is the quietest in the pipeline, because its
              output looks identical to success. An unproofread merge does not
              crash anything; it just inflates a connectivity count in a paper two
              years later. This is why quality is reported per release, with
              metrics whose blind spots are stated alongside them.
            </p>
            <p class="step-depth">
              <strong>Depth:</strong>
              <a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08</a>
              for the production loop, triage, and metrics; the content library's
              <a href="{{ '/content-library/proofreading/error-taxonomy/' | relative_url }}">error taxonomy</a>,
              <a href="{{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}">strategies</a>, and
              <a href="{{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}">metrics and QA</a>
              entries for the reference material; and the
              <a href="{{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}">neuroanatomy entries</a>
              for the identification skills the work depends on.
            </p>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">CAVE</span>
            <span class="tech-tag">Neuroglancer</span>
            <span class="tech-tag">Versioned Editing</span>
          </div>
        </div>
      </div>
    </div>

    <div class="step-container">
      <div class="step-number">7</div>
      <div class="step-content">
        <h3>Analysis and Release</h3>
        <div class="step-details">
          <div class="step-description">
            <p>
              The deliverable is not the images — it is the graph, plus the tables
              that describe it: a synapse table on the order of 5 × 10⁸ rows per
              cubic millimeter, skeletons, meshes, and cell annotations. Building
              the graph is itself a sequence of consequential choices (which edges
              count, what synapse threshold, which release), and every analysis
              needs a null model before a claim: a motif count means nothing until
              you say what you are comparing it against. For HI-MC the target
              questions are the hippocampal classics — whether dentate gyrus wiring
              supports pattern separation, whether the CA3 recurrent network looks
              like an auto-associative memory, how the trisynaptic circuit is
              actually built at synaptic resolution.
            </p>
            <p>
              Failure at this step is the only kind the earlier pipeline cannot
              cause: a technically perfect reconstruction analyzed without regard
              to its error profile. Residual splits deflate degree; residual merges
              inflate it; both do so non-uniformly. The defensible habit is to run
              analyses at two proofreading versions and report what moved — which
              is also why the project's phased public releases, with versioned
              access for the community, are part of the pipeline rather than an
              afterthought.
            </p>
            <p class="step-depth">
              <strong>Depth:</strong>
              <a href="{{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}">Unit 09: Connectome analysis and NeuroAI</a>
              — graph construction, null models, motif analysis, and the
              error-sensitivity checks that keep a result honest.
            </p>
          </div>
          <div class="step-tech">
            <h4>Key Technologies:</h4>
            <span class="tech-tag">Graph Analysis</span>
            <span class="tech-tag">Null Models</span>
            <span class="tech-tag">Versioned Releases</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="next-steps">
    <h2>Where to Go Next</h2>
    <div class="cta-grid">
      <div class="cta-card">
        <h3>Learn the steps properly</h3>
        <p>
          The technical training units behind this tour:
          <a href="{{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}">Unit 03</a> (prep and imaging),
          <a href="{{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}">Unit 04</a> (alignment and infrastructure),
          <a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08</a> (segmentation and proofreading), and
          <a href="{{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}">Unit 09</a> (analysis).
        </p>
      </div>
      <div class="cta-card">
        <h3>Do the bottleneck skill</h3>
        <p>
          The <a href="{{ '/side-quests/proofreading/' | relative_url }}">Proofreading side quest</a>
          treats step 6 as what it is — an allocation problem under a budget — and
          ends with an artifact a lab can evaluate.
        </p>
      </div>
      <div class="cta-card">
        <h3>Get your hands on data</h3>
        <p>
          <a href="{{ '/datasets/getting-started/' | relative_url }}">Getting started with data</a>
          is the on-ramp from "the data is public" to a working DataFrame;
          <a href="{{ '/datasets/access/' | relative_url }}">the access guide</a>
          collects per-platform notebooks. The
          <a href="{{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}">HI-MC case study</a>
          has the project's scientific context and timeline.
        </p>
      </div>
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

.step-description p {
  margin-bottom: 1rem;
}

.step-depth {
  border-top: 1px solid #e5e7eb;
  padding-top: 0.75rem;
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

.cta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.cta-card {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
  text-align: left;
}

.cta-card h3 {
  color: var(--neural-blue);
  margin-bottom: 1rem;
}

.next-steps {
  background: linear-gradient(135deg, var(--brain-gray) 0%, white 100%);
  padding: 3rem;
  border-radius: 1rem;
  margin-top: 4rem;
}

@media (max-width: 768px) {
  .workflow-preview {
    flex-direction: column;
    text-align: center;
    padding: 1.25rem;
  }

  .step-container {
    flex-direction: column;
    gap: 1rem;
  }

  .step-details {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .next-steps {
    padding: 1.5rem 1.1rem;
    margin-top: 2.5rem;
  }

  .cta-grid {
    grid-template-columns: 1fr;
  }

  .cta-card {
    padding: 1.25rem;
  }

  .workflow-stats {
    grid-template-columns: 1fr;
    gap: 1rem;
    margin: 2rem 0;
  }

  .stat-card {
    padding: 1.25rem;
  }
}
</style>
