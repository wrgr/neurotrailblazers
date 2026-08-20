---
layout: default
title: "Start Here - Your Journey into Nanoscale Connectomics"
description: "Begin your adventure in computational neuroscience with our structured pathway through nanoscale connectomics research and discovery."
permalink: /start-here/
track: career-and-community
pathways:
  - professional growth
  - hidden curriculum
---

<div class="main-content">
    {% assign concepts_base = '/concepts/' | relative_url %}
    <div class="hero hero-spaced hero-rounded">
        <div class="hero-content">
            <h1>Start Your NeuroTrailblazing Journey</h1>
        </div>
    </div>

    <section class="section">
        <h2>Welcome to NeuroTrailblazers!</h2>
        <p>Whether you're an undergraduate student curious about the brain, a graduate student diving into research, or a mentor looking to guide the next generation, you're in the right place. Our platform is designed to support learners at every stage of their journey into nanoscale connectomics.</p>
    </section>

    <section class="section">
        <h2>Choose Your Path</h2>
        <div class="cards-grid">
            <div class="card">
                <div class="card-icon">🧠</div>
                <h3 class="card-title">Core Concepts & Methods</h3>
                <p class="card-description">Build technical fluency in connectomics from motivation and imaging through analysis methods.</p>
                <div class="mt-1">
                    <a href="{{ '/tracks/core-concepts-methods/' | relative_url }}" class="btn btn-primary">Open Core Track</a>
                </div>
            </div>
            <div class="card">
                <div class="card-icon">🔬</div>
                <h3 class="card-title">Research in Action</h3>
                <p class="card-description">Apply methods through workflows, quality control, tools, and research execution practice.</p>
                <div class="mt-1">
                    <a href="{{ '/tracks/research-in-action/' | relative_url }}" class="btn btn-primary">Open Practice Track</a>
                </div>
            </div>
            <div class="card">
                <div class="card-icon">🤝</div>
                <h3 class="card-title">Career & Community</h3>
                <p class="card-description">Navigate mentorship, hidden curriculum, and professional growth pathways.</p>
                <div class="mt-1">
                    <a href="{{ '/tracks/career-and-community/' | relative_url }}" class="btn btn-primary">Open Community Track</a>
                </div>
            </div>
        </div>
    </section>

    {% include ui/technical-track-roadmap.html %}

    <section class="section">
        <h2>Understanding Our Structure</h2>

        <h3>Three Track Architecture</h3>
        <p>We organize learning around three tracks aligned to the Fadel dimensions:</p>
        <ul class="mb-2" style="margin-left: 2rem;">
            <li><strong>Core Concepts & Methods:</strong> Knowledge + skills foundations</li>
            <li><strong>Research in Action:</strong> Applied workflows and reproducible practice</li>
            <li><strong>Career & Community:</strong> Character + meta-learning, mentorship, hidden curriculum</li>
        </ul>
        <p><a href="{{ '/tracks/' | relative_url }}">Explore all tracks</a></p>

        <h3>Key Datasets</h3>
        <p>Learn with real scientific data from landmark studies:</p>
        <div class="grid-sm mt-1 mb-1">
            <div class="card-gray">
                <strong>Kasthuri et al. 2015</strong><br>
                <small>Mouse visual cortex</small>
            </div>
            <div class="card-gray">
                <strong>MICrONS 2025</strong><br>
                <small>Large-scale mouse brain</small>
            </div>
            <div class="card-gray">
                <strong>FlyWire 2024</strong><br>
                <small>Complete fly brain</small>
            </div>
        </div>

        <div class="hero hero-spaced hero-rounded">
            <div class="hero-content">
                <h2 class="hero-title-impact">Meet the Trailblazers<span>: Inspiring paths into connectomics</span></h2>
                <p class="hero-subtitle">Stories of students, researchers, and mentors finding their way</p>
            </div>
        </div>

        <div class="cards-grid">
            <a href="{{ '/avatars/undergradstudent/' | relative_url }}" class="avatar-card avatar-card-blue">
                <h3>Julian: Undergraduate Student</h3>
            </a>
            <a href="{{ '/avatars/gradstudent/' | relative_url }}" class="avatar-card avatar-card-purple">
                <h3>Maya: Graduate Student</h3>
            </a>
            <a href="{{ '/avatars/researcher/' | relative_url }}" class="avatar-card avatar-card-cyan">
                <h3>Amir: Researcher</h3>
            </a>
            <a href="{{ '/avatars/mentor/' | relative_url }}" class="avatar-card avatar-card-orange">
                <h3>Dr. Nguyen: Mentor/PI</h3>
            </a>
        </div>

        <p>Each avatar includes a backstory, visible successes, and a noble failure—offering a relatable entry point for diverse learners.</p>
        <p><em>Inspired by stories like those described in <a href="https://www.molbiolcell.org/doi/10.1091/mbc.E24-09-0416">When Life Gets in the Way of Science</a></em></p>
    </section>

    <section class="section">
        <h2>Explore by Concept</h2>
        <p>If module numbering feels heavy, use concept-first discovery based on your immediate learning need.</p>
        <div class="cta-buttons">
            <a href="{{ '/concepts/' | relative_url }}" class="btn btn-primary">Open Concept Explorer</a>
            <a href="{{ concepts_base }}?track=core-concepts-methods&need=matching%20method%20to%20question" class="btn btn-secondary">Match Method to Question</a>
            <a href="{{ concepts_base }}?track=research-in-action&need=prioritizing%20corrections" class="btn btn-secondary">Prioritize QC Corrections</a>
            <a href="{{ concepts_base }}?track=career-and-community&need=finding%20mentorship%20support" class="btn btn-secondary">Find Mentorship Support</a>
            <a href="{{ '/tracks/' | relative_url }}" class="btn btn-secondary">Browse Tracks</a>
        </div>
    </section>

    <section class="section">
        <h2>Our Educational Framework</h2>
        <p>NeuroTrailblazers is built on evidence-based educational models:</p>
        
        <div class="cards-grid">
            <div class="card">
                <h3>MERIT Framework</h3>
                <p>Six stages aligned with the scientific method:</p>
                <ol class="list-tight">
                    <li>Motivation & Inspiration</li>
                    <li>Exploration & Discovery</li>
                    <li>Research & Investigation</li>
                    <li>Implementation & Practice</li>
                    <li>Testing & Validation</li>
                    <li>Sharing & Impact</li>
                </ol>
            </div>
            <div class="card">
                <h3>Professional Pathways</h3>
                <p>Structured support across:</p>
                <ul class="list-tight">
                    <li>Research fundamentals</li>
                    <li>Data analysis skills</li>
                    <li>Communication & presentation</li>
                    <li>Career development</li>
                </ul>
            </div>
            <div class="card">
                <h3>CCR Dimensions</h3>
                <p>Four key areas of development:</p>
                <ul class="list-tight">
                    <li><strong>Knowledge:</strong> Content mastery</li>
                    <li><strong>Skills:</strong> Technical abilities</li>
                    <li><strong>Character:</strong> Research ethics</li>
                    <li><strong>Meta-Learning:</strong> Learning how to learn</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="section">
        <h2>Your first hour</h2>
        <p>Reading about connectomics and doing connectomics are different skills, and only the second one transfers. So rather than a reading list, here is a first hour that ends with something you have made. You need a browser and, for step 3, nothing else.</p>

        <div class="checklist-box">
            <h3>Sixty minutes, one artifact</h3>
            <div class="checklist">
                <label class="checklist-item">
                    <input type="checkbox">
                    <span><strong>0-10 min &mdash; Look at real data.</strong> Open any public volume in Neuroglancer via the <a href="{{ '/datasets/access/' | relative_url }}">dataset access guide</a>. Navigate somewhere arbitrary, not a curated view. Scroll through twenty consecutive sections and watch how structures appear and disappear.</span>
                </label>
                <label class="checklist-item">
                    <input type="checkbox">
                    <span><strong>10-25 min &mdash; Find out why it looks like that.</strong> Read <a href="{{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}">Unit 03, section 1</a>, on the preparation chain. Then go back to the volume and find one thing from the artifact catalogue in section 2.</span>
                </label>
                <label class="checklist-item">
                    <input type="checkbox">
                    <span><strong>25-45 min &mdash; Make a judgement and test it.</strong> Read <a href="{{ '/technical-training/01-why-map-the-brain/' | relative_url }}">Unit 01, section 3</a>, on what structure can and cannot establish. Attempt its &ldquo;Check yourself&rdquo; questions <em>before</em> opening the answers &mdash; opening them first turns a test into re-reading, which feels productive and is not.</span>
                </label>
                <label class="checklist-item">
                    <input type="checkbox">
                    <span><strong>45-60 min &mdash; Write the artifact.</strong> Do the Unit 01 lab: a one-page study brief with a biological question, three measurements with units, a null model, and one sentence you will refuse to write. The last item is the one that matters, and it is the one most people leave blank.</span>
                </label>
            </div>
            <p class="mt-1"><small>If you finish with a brief you are willing to show someone, you are oriented. If you finish with an empty step 4, that is also information &mdash; it means you have not yet found the boundary of your evidence, which is exactly what Unit 01 exists to teach.</small></p>
        </div>
    </section>

    <section class="section">
        <h2>Which track, and when</h2>
        <p>Most people should start with <strong>Core Concepts &amp; Methods</strong> and layer the others in as their research practice develops. The exceptions are worth naming:</p>
        <table>
            <thead>
                <tr><th>If this describes you</th><th>Start here</th><th>Why</th></tr>
            </thead>
            <tbody>
                <tr>
                    <td>New to the field, whatever your level</td>
                    <td><a href="{{ '/tracks/core-concepts-methods/' | relative_url }}">Core Concepts &amp; Methods</a>, at Unit 01</td>
                    <td>The perceptual units 05&ndash;07 are the slowest part and everything downstream depends on them. Starting anywhere else means coming back.</td>
                </tr>
                <tr>
                    <td>Strong engineering or ML background, new to neuroscience</td>
                    <td><a href="{{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}">Unit 04</a> or <a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08</a>, then back to 05&ndash;07</td>
                    <td>Your systems intuitions transfer directly and give you a foothold. Skipping 05&ndash;07 entirely does not work: a model trained on annotations from people who cannot tell an astrocytic process from a dendrite learns to make that mistake at scale.</td>
                </tr>
                <tr>
                    <td>Already working on a connectomics project</td>
                    <td><a href="{{ '/tracks/research-in-action/' | relative_url }}">Research in Action</a></td>
                    <td>It is organized around the decisions a live project forces: proofreading budgets, version pinning, and defensible analysis.</td>
                </tr>
                <tr>
                    <td>Teaching or mentoring others</td>
                    <td><a href="{{ '/teaching/facilitator-guide/' | relative_url }}">Facilitator Guide</a>, then the <a href="{{ '/teaching/' | relative_url }}">teaching kits</a></td>
                    <td>What you need is the assessment instrument and the run-of-show, not the reading.</td>
                </tr>
                <tr>
                    <td>Here for the professional side</td>
                    <td><a href="{{ '/tracks/career-and-community/' | relative_url }}">Career &amp; Community</a></td>
                    <td>Relevant from week one, not only at the end. Deferring it until the technical work is finished is the most common mistake on this track.</td>
                </tr>
            </tbody>
        </table>
        <p>Each track page carries a time estimate, an ordered sequence with per-step outcomes, and a description of what &ldquo;done&rdquo; means as a capability rather than as a set of pages visited.</p>
    </section>

    <section class="section">
        <h2>Getting unstuck</h2>
        <p>Two things a page cannot give you, and where to find them:</p>
        <div class="cards-grid">
            <div class="card">
                <div class="card-icon">&#128172;</div>
                <h3>A technical answer</h3>
                <p>The <a href="{{ '/ask-an-expert/' | relative_url }}">Ask-an-Expert</a> route is for questions where you have already tried something and can say what you tried. Before using it, check the <a href="{{ '/technical-training/dictionary/' | relative_url }}">dictionary</a> &mdash; a large share of apparent difficulty in this field is vocabulary, and it is fixable in a week.</p>
            </div>
            <div class="card">
                <div class="card-icon">&#128100;</div>
                <h3>Calibration against other people</h3>
                <p>You cannot calibrate your own judgement alone. The units' drills are built to be run with a partner, and comparing calls with one other person is worth more than three rounds of self-review. A journal club or a community proofreading effort supplies the same thing at larger scale.</p>
            </div>
            <div class="card">
                <div class="card-icon">&#128218;</div>
                <h3>Depth on a specific topic</h3>
                <p>The <a href="{{ '/content-library/' | relative_url }}">content library</a> holds the long-form reference material behind every unit &mdash; instructor-level detail on ultrastructure, imaging, proofreading metrics, and analysis, with worked examples and reading lists.</p>
            </div>
        </div>
    </section>

    <div class="text-center mt-4 mb-2">
        <h2>Ready to Begin?</h2>
        <p class="mt-1 mb-1" style="font-size: 1.2rem;">Choose your starting point and embark on your neuroscience adventure!</p>
        <div class="flex-center mt-2">
            <a href="{{ '/tracks/' | relative_url }}" class="btn btn-primary">View Learning Tracks</a>
            <a href="{{ '/datasets/' | relative_url }}" class="btn btn-secondary">Explore Datasets</a>
            <a href="{{ '/datasets/workflow/' | relative_url }}" class="btn btn-secondary">See Our Workflow</a>
        </div>
    </div>
</div>
