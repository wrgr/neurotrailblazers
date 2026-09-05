---
layout: avatar
title: "Amir, AI scientist"
role: AI Scientist
permalink: /avatars/researcher/
slug: researcher
track: career-and-community
pathways:
  - professional growth
  - research workflow
experience: Expert (industry)
epistemic_orientation: Mechanistic, systems optimization
motivation: Solve big problems, bring vision science into AI
student_name: "Amir Khan"
education_level: "PhD in Computer Science"
background: "Industry AI researcher bridging vision and neuroscience"
major: "Computer Science"
interests: ["Edge devices", "Object tracking", "Connectomics"]
challenges: ["Interpreting neuroscience literature", "Adapting pace from industry", "Collaborating across fields"]
strengths: ["Deep ML expertise", "Systems thinking", "Problem solving"]
goals: ["Apply ML to neural data", "Collaborate with academics", "Understand circuitry"]
summary: "Industry AI scientist translating machine learning expertise into neuroscience collaboration and connectomics discovery."
recommended_modules:
  - module05
  - module07
  - module08
  - module10
  - module13
  - module14
recommended_datasets:
  - mouseconnects
  - workflow
recommended_tools:
  - connectome-quality
  - ask-an-expert
last_reviewed: 2026-03-09
maintainer: NeuroTrailblazers Team
use_layout_hero: false
content_type: core
---

<div class="main-content">
<div class="hero hero-spaced hero-rounded">
  <div class="hero-content">
    <div class="avatar-header">
      <div>
        <h1>{{ page.title }}</h1>
        <p class="hero-subtitle">{{ page.role }}</p>
      </div>
    </div>
  </div>
</div>

<nav class="avatar-nav">
  <a href="#story">Story</a>
  <a href="#decisions">Decisions</a>
  <a href="#path">How the Site Helps</a>
  <a href="#insights">Insights</a>
  <a href="{{ '/avatars/' | relative_url }}">All Avatars</a>
</nav>

<section class="section" id="story">
  <h2>Amir's Story</h2>
  <div style="background: var(--brain-gray); padding: 2rem; border-radius: 12px; margin: 1rem 0;">
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--synapse-black); margin: 0;">
      Amir came from the world of edge devices and object tracking. But when he saw a 3D fly brain reconstructed by a global team, he knew: this was the next frontier. He’s fluent in models and metrics, but unsure what a dendrite <em>means</em>. And he’s learning that science doesn’t move like startups do. But the challenge—that's the hook.
    </p>
  </div>
  <div class="cards-grid" style="margin: 2rem 0;">
    <div class="card" style="border-left: 4px solid var(--neural-blue);">
      <h3 style="color: var(--neural-blue);">Background</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>PhD in computer vision</li>
        <li>Five years in industry building ML systems</li>
        <li>Contributor to several open-source projects</li>
        <li>Minimal formal neuroscience training</li>
        <li>Passionate about interdisciplinary work</li>
      </ul>
    </div>
    <div class="card" style="border-left: 4px solid var(--cerebral-purple);">
      <h3 style="color: var(--cerebral-purple);">Current Situation</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Industry researcher exploring neuroscience collaborations</li>
        <li>Self-studying neuro literature and attending seminars</li>
        <li>Building models for large neural datasets</li>
        <li>Balancing corporate objectives with academic curiosity</li>
        <li>Expanding network with university labs</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="decisions" markdown="1">

## The Decisions in Front of Amir

**Where to enter the material.** Amir does not need another machine learning
course, and sitting through one disguised as "computational neuroscience"
would waste the asset he brings. His actual gap is biological: he can tune a
segmentation model but cannot yet say what a dendrite means, which cues
distinguish an axon from a glial process, or why a particular merge error is
scientifically expensive. The right entry point is
[Unit 05]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}),
[Unit 06]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}),
and [Unit 07]({{ '/technical-training/07-glia/' | relative_url }}) — the
ultrastructure, neurites, and glia units — followed by
[Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}),
which connects that biology back to the pipeline vocabulary he already speaks.
The [Neuroanatomy for Proofreaders side quest]({{ '/side-quests/neuroanatomy-for-proofreaders/' | relative_url }})
trains the same identification skill hands-on.

**Prototype first, or scope first?** Industry habit says grab the data and
start training. In this field that habit has a specific failure mode: root IDs
and tables change between proofreading versions, so two files pulled a week
apart can silently disagree. Before building anything, Amir should climb the
ladder in [Getting Started with Data]({{ '/datasets/getting-started/' | relative_url }})
— snapshot tables load in an afternoon with no authentication — and adopt its
version-pinning rule from the first notebook. For choosing what to build, the
[Open Problems]({{ '/open-problems/' | relative_url }}) ramps state questions
the field actually has, each with a defined on-ramp, which is a faster route
to a real collaboration than pitching a tool nobody asked for.

</section>

<section class="section" id="path" markdown="1">

## How the Site's Material Serves Him

Amir's stated struggle is reading dense neuroscience papers.
[Reading and judging]({{ '/hidden-curriculum/reading-and-judging/' | relative_url }})
addresses it directly: the order experts actually read a paper in, how to read
methods for what is absent, and how to tell a solid result from a fragile one.
Paired with the [Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
paper list, it converts his self-study from coverage into calibration — the
same move he would make when learning a new ML subfield.

His expertise becomes most useful to collaborators when it is expressed in the
field's own quality vocabulary. The
[Connectome Quality]({{ '/tools/connectome-quality/' | relative_url }}) page
and the [Metrics and QA reference]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }})
explain what VI, ERL, and synapse precision/recall each measure and — more
importantly for a model builder — what each is blind to. A benchmark Amir
proposes that ignores the field's split/merge asymmetry will be politely
ignored; one that reports the components separately will be read. This is the
concrete version of his "when to push his tech, when to adapt it" question.

Finally, the pace mismatch he feels is partly a norms mismatch, and the
[hidden curriculum]({{ '/hidden-curriculum/' | relative_url }}) pages describe
the academic operating system — authorship, credit, escalation, how meetings
work — that his industry experience does not transfer to. The
[Career and Community track]({{ '/tracks/career-and-community/' | relative_url }})
sequences that material; the
[lab norms]({{ '/hidden-curriculum/lab-norms/' | relative_url }}) page alone
would have saved him his first two months of cross-cultural confusion.

There is also a contribution path sized for him right now. The
[getting-started page]({{ '/datasets/getting-started/' | relative_url }})
states that corrections to its own drifting command snippets are a welcome
first contribution, and the
[proofreading side quest]({{ '/side-quests/proofreading/' | relative_url }})
ends in an artifact a lab can read — both are ways to demonstrate seriousness
to academic collaborators in their own currency before proposing anything
larger.

</section>

<section class="section" id="insights">
  <h2>Key Insights</h2>
  <div class="cards-grid" style="margin: 2rem 0;">
    <div class="card" style="border-left: 4px solid var(--neural-blue);">
      <h3 style="color: var(--neural-blue);">Inner Conflict</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Struggles to read dense neuro papers</li>
        <li>Unsure when to push his tech or adapt it</li>
        <li>Wants to contribute but not overstep</li>
      </ul>
    </div>
    <div class="card" style="border-left: 4px solid var(--cerebral-purple);">
      <h3 style="color: var(--cerebral-purple);">Journey Markers</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Tuned a transformer model for segment consistency</li>
        <li>Co-created a dashboard with a neuro postdoc to evaluate proofread merges</li>
        <li>Gave a talk that helped PIs understand model bias</li>
      </ul>
    </div>
    <div class="card" style="border-left: 4px solid var(--axon-cyan);">
      <h3 style="color: var(--axon-cyan);">Growth Path</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Learns from questions, not just answers</li>
        <li>Redefines “impact” from speed to depth</li>
        <li>Bridges cultures without diluting either</li>
      </ul>
    </div>
  </div>
</section>

</div>
