---
layout: default
title: "Start Here"
description: "Choose a path through nanoscale connectomics: what to read, what to build, and in what order, whether you are starting out or already in a lab."
permalink: /start-here/
track: career-and-community
pathways:
  - professional growth
  - hidden curriculum
content_type: navigation
---

<div class="main-content">
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
        <h2>Two questions, not one</h2>
        <p>Getting oriented here means answering two separate questions, and most people only think to ask the first. <strong>What</strong> you are learning is the track. <strong>How</strong> you are using it &mdash; alone, in a session someone is running, or inside a research group &mdash; is the mode. They are independent, and the second one changes what you should be reading as much as the first does.</p>

        <div class="axis-head">
          <span class="axis-eyebrow">Question 1</span>
          <h3>How are you using this?</h3>
        </div>
        {% include ui/mode-picker.html %}
        <p class="mt-1"><a href="{{ '/modes/' | relative_url }}">What each mode assumes, gives, and does not give &rarr;</a></p>

        <div class="axis-head">
          <span class="axis-eyebrow">Question 2</span>
          <h3>What are you learning?</h3>
        </div>
        <div class="arch-grid">
            <article class="arch-card" style="--accent: var(--layer-path); --accent-tint: var(--layer-path-tint);">
                <span class="arch-chip" aria-hidden="true">&#129504;</span>
                <h3 class="arch-title">Core Concepts &amp; Methods</h3>
                <p class="arch-meta"><span class="pill pill-layer">topic track</span></p>
                <p class="arch-body">Build technical fluency in connectomics from motivation and imaging through analysis methods. The default answer if you are new, whatever your career stage.</p>
                <div class="arch-actions">
                    <a href="{{ '/tracks/core-concepts-methods/' | relative_url }}" class="btn btn-primary">Open Core Track</a>
                </div>
            </article>
            <article class="arch-card" style="--accent: var(--layer-path); --accent-tint: var(--layer-path-tint);">
                <span class="arch-chip" aria-hidden="true">&#128736;</span>
                <h3 class="arch-title">Research in Action</h3>
                <p class="arch-meta"><span class="pill pill-layer">topic track</span></p>
                <p class="arch-body">Apply methods through workflows, quality control, tools, and research execution practice. Works best alongside a live project rather than instead of one.</p>
                <div class="arch-actions">
                    <a href="{{ '/tracks/research-in-action/' | relative_url }}" class="btn btn-primary">Open Practice Track</a>
                </div>
            </article>
            <article class="arch-card" style="--accent: var(--layer-path); --accent-tint: var(--layer-path-tint);">
                <span class="arch-chip" aria-hidden="true">&#129309;</span>
                <h3 class="arch-title">Career &amp; Community</h3>
                <p class="arch-meta"><span class="pill pill-layer">topic track</span></p>
                <p class="arch-body">Navigate mentorship, the hidden curriculum, and professional growth. Relevant from week one, not only at the end.</p>
                <div class="arch-actions">
                    <a href="{{ '/tracks/career-and-community/' | relative_url }}" class="btn btn-primary">Open Community Track</a>
                </div>
            </article>
        </div>

        <h3>Or neither</h3>
        <p>The tracks are a convenience, not a gate. If you have a specific question rather than a curriculum-sized one, go straight to <a href="{{ '/core/' | relative_url }}">the core</a> &mdash; the dictionary, content library, journal club, atlas, hidden curriculum and datasets are written to be looked things up in, and none of them requires you to have started anywhere.</p>
    </section>

    <section class="section">
        <h2 id="your-first-hour">Your first hour</h2>
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
                    <span><strong>10-25 min &mdash; Find out why it looks like that.</strong> Read <a href="{{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}">Unit 03, section 1</a>, on the preparation chain. Then go back to the volume and find one thing from the artifact catalog in section 2.</span>
                </label>
                <label class="checklist-item">
                    <input type="checkbox">
                    <span><strong>25-45 min &mdash; Make a judgment and test it.</strong> Read <a href="{{ '/technical-training/01-why-map-the-brain/' | relative_url }}">Unit 01, section 3</a>, on what structure can and cannot establish. Attempt its &ldquo;Check yourself&rdquo; questions <em>before</em> opening the answers &mdash; opening them first turns a test into re-reading, which feels productive and is not.</span>
                </label>
                <label class="checklist-item">
                    <input type="checkbox">
                    <span><strong>45-60 min &mdash; Write the artifact.</strong> Do the Unit 01 lab: a one-page study brief with a biological question, three measurements with units, a null model, and one sentence you will refuse to write. The last item is the one that matters, and it is the one most people leave blank.</span>
                </label>
            </div>
            <p class="mt-1"><small>If you finish with a brief you are willing to show someone, you are oriented. If you finish with an empty step 4, that is also information &mdash; it means you have not yet found the boundary of your evidence, which is exactly what Unit 01 exists to teach.</small></p>
        </div>
    </section>


    {% include ui/technical-track-roadmap.html %}

    <section class="section">
        <h2>Understanding Our Structure</h2>

        <h3>Core with tracks</h3>
        <p>The site has two layers, and telling them apart saves a lot of wandering.</p>
        <ul class="mb-2" style="margin-left: 2rem;">
            <li><strong><a href="{{ '/core/' | relative_url }}">The core</a> is reference.</strong> Content library, dictionary, journal club, atlas, hidden curriculum, datasets. No order, not meant to be finished, consulted rather than worked through.</li>
            <li><strong><a href="{{ '/tracks/' | relative_url }}">Tracks are paths through it.</strong> Each selects from the core, sequences it, and adds labs that end in an artifact. Three of them, aligned to the Fadel dimensions of Knowledge, Skills, Character and Meta-learning.</li>
            <li><strong><a href="{{ '/modes/' | relative_url }}">Modes are how you walk a track.</strong> Self-study and hosted workshop both exist today. A third &mdash; a research-intensive, contributory program built on the same core &mdash; is named on that page but is not built yet.</li>
        </ul>
        <p>Technical units and modules are path content; session kits, decks and worksheets are delivery material for whoever is running a session. If you are studying alone you can ignore the latter entirely.</p>

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
                <h3>Julian, first-generation undergraduate</h3>
            </a>
            <a href="{{ '/avatars/gradstudent/' | relative_url }}" class="avatar-card avatar-card-purple">
                <h3>Maya, graduate student</h3>
            </a>
            <a href="{{ '/avatars/researcher/' | relative_url }}" class="avatar-card avatar-card-cyan">
                <h3>Amir, AI scientist</h3>
            </a>
            <a href="{{ '/avatars/mentor/' | relative_url }}" class="avatar-card avatar-card-orange">
                <h3>Dr. Linh Nguyen, assistant professor</h3>
            </a>
        </div>

        <p>Each avatar includes a backstory, visible successes, and a noble failure—offering a relatable entry point for diverse learners.</p>
        <p><em>Inspired by stories like those described in <a href="https://www.molbiolcell.org/doi/10.1091/mbc.E24-09-0416">When Life Gets in the Way of Science</a></em></p>
    </section>

    <section class="section">
        <h2>Our Educational Framework</h2>
        <p>The program is built on three evidence-based models &mdash; the MERIT mentoring stages, the Professional Pathways workshops, and the CCR development dimensions. The <a href="{{ '/models/' | relative_url }}">program models page</a> summarizes them, and the <a href="{{ '/education/models/' | relative_url }}">models-in-practice playbook</a> shows what each stage looks like when it is working and the failure mode it exists to prevent.</p>
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
                    <td>Anyone, at any stage</td>
                    <td><a href="{{ '/hidden-curriculum/' | relative_url }}">The hidden curriculum</a></td>
                    <td>The unwritten norms &mdash; how to read a paper, what a PI expects but won&rsquo;t say, how funding and authorship really work, how to disagree with someone senior. Not a track; read it alongside whatever else you are doing.</td>
                </tr>
                <tr>
                    <td>Wanting one concrete, valuable skill rather than a curriculum</td>
                    <td><a href="{{ '/side-quests/proofreading/' | relative_url }}">The proofreading side quest</a></td>
                    <td>Off every track&rsquo;s critical path, and the skill most likely to get you taken seriously by a connectomics lab, because it is the bottleneck and competence at it is checkable. Twenty to thirty hours, ending in a document someone can disagree with.</td>
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
                <div class="card-icon" aria-hidden="true">&#128172;</div>
                <h3>A technical answer</h3>
                <p>The <a href="{{ '/ask-an-expert/' | relative_url }}">Ask-an-Expert</a> route is for questions where you have already tried something and can say what you tried. Before using it, check the <a href="{{ '/technical-training/dictionary/' | relative_url }}">dictionary</a> &mdash; a large share of apparent difficulty in this field is vocabulary, and it is fixable in a week.</p>
            </div>
            <div class="card">
                <div class="card-icon" aria-hidden="true">&#128100;</div>
                <h3>Calibration against other people</h3>
                <p>You cannot calibrate your own judgment alone. The units' drills are built to be run with a partner, and comparing calls with one other person is worth more than three rounds of self-review. A journal club or a community proofreading effort supplies the same thing at larger scale.</p>
            </div>
            <div class="card">
                <div class="card-icon" aria-hidden="true">&#128218;</div>
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
