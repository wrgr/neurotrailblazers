---
layout: avatar
title: "Maya, graduate student"
role: Graduate Student
permalink: /avatars/gradstudent/
slug: gradstudent
track: career-and-community
pathways:
  - professional growth
  - mentoring
experience: Intermediate
epistemic_orientation: "Hybrid - computational with curiosity"
motivation: Use ML to push neuroscience forward and lift others with her
student_name: "Maya Patel"
education_level: "PhD Student, Year 2"
background: "Blend of psychology and mathematics"
major: "Computational Neuroscience"
interests: ["Machine learning", "Segmentation models", "Mentoring"]
challenges: ["Balancing research directions", "Career uncertainty", "Bridging disciplines"]
strengths: ["Explaining complex ideas", "Collaboration", "Curiosity"]
goals: ["Advance segmentation methods", "Publish impactful papers", "Support younger students"]
summary: "Graduate student connecting computational methods and neuroscience while developing research identity and mentoring others."
recommended_modules:
  - module04
  - module05
  - module06
  - module07
  - module08
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
  <h2>Maya's Story</h2>
  <div style="background: var(--brain-gray); padding: 2rem; border-radius: 12px; margin: 1rem 0;">
    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--synapse-black); margin: 0;">
      Maya always straddled two worlds—equally at home in math class and psych lab. She’s now in year 2 of her PhD, building segmentation models and explaining PCA to undergrads. She loves when code makes neurons “pop” into clarity. She's not always sure her work counts when she’s not slicing brains or running gels—but she's finding her place.
    </p>
  </div>
  <div class="cards-grid" style="margin: 2rem 0;">
    <div class="card" style="border-left: 4px solid var(--neural-blue);">
      <h3 style="color: var(--neural-blue);">Background</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Majored in psychology and mathematics</li>
        <li>First in her family to pursue a PhD</li>
        <li>Volunteered at mental health clinics</li>
        <li>Passionate about machine learning since undergrad</li>
        <li>Enjoys mentoring fellow students</li>
      </ul>
    </div>
    <div class="card" style="border-left: 4px solid var(--cerebral-purple);">
      <h3 style="color: var(--cerebral-purple);">Current Situation</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Second-year PhD in computational neuroscience</li>
        <li>Developing segmentation models for EM data</li>
        <li>Mentors an undergraduate student</li>
        <li>Attends cross-lab reading groups</li>
        <li>Exploring career paths in academia and industry</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="decisions" markdown="1">

## The Decisions in Front of Maya

**How much proofreading and quality-control depth does a model builder need?**
Maya builds segmentation models, and the temptation is to treat proofreading as
someone else's downstream cleanup. The site's technical material argues the
opposite: [Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
shows how a segmentation can improve its total VI score while its merge errors
get worse, because the split component dominates — which means a model like
hers can ship a regression behind a better headline number. Deciding to learn
the error taxonomy and metric blind spots firsthand, through the
[proofreading side quest]({{ '/side-quests/proofreading/' | relative_url }})
and the [Connectome Quality]({{ '/tools/connectome-quality/' | relative_url }})
notebooks, is a direct investment in her first-author paper, not a detour from
it.

**Mentor by improvisation, or mentor by design?** Maya mentors an
undergraduate and is not sure her guidance counts as anything more than
availability. The [models-in-practice playbook]({{ '/models/' | relative_url }})
gives her a design: her mentee is in MERIT stage 3, where the failure modes
are symmetric — support withdrawn too fast reads as personal inadequacy,
support withdrawn too slowly produces dependence — and the signal to watch is
whether the mentee initiates questions or waits for tasks. That one page turns
"am I helping?" into a checkable question.

</section>

<section class="section" id="path" markdown="1">

## How the Site's Material Serves Her

On the technical side, Maya's models are only as good as her understanding of
the tissue they segment.
[Unit 05]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}),
[Unit 06]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}),
and [Unit 07]({{ '/technical-training/07-glia/' | relative_url }}) supply the
ultrastructural ground truth behind her training labels — including why
glia-neuron merges are both hard to detect and expensive, which is exactly the
error class her models need to be evaluated against. The
[Metrics and QA reference]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }})
works VI, ERL, and precision/recall in the mathematical detail her methods
section will need.

For the mentoring half of her life, the
[hidden curriculum]({{ '/hidden-curriculum/' | relative_url }}) pages give her
something concrete to hand Julian instead of vague reassurance: named norms,
stated as sentences. This also solves her own problem of being "the explainer"
— she can point to a page rather than reconstruct the explanation each time.
If she runs a session for her lab or reading group, the
[session kits]({{ '/teaching/sessions/' | relative_url }}) and
[Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}) are
built for exactly that: one page to open ten minutes beforehand, with timing,
misconceptions, and a rubric already assembled.

Her academia-versus-industry uncertainty is a stage question, not a character
flaw. [Career mechanics]({{ '/hidden-curriculum/career-mechanics/' | relative_url }})
describes how applications, funding, and references actually operate, and the
[Career and Community track]({{ '/tracks/career-and-community/' | relative_url }})
sequences that material so she can prepare for both paths at once instead of
stalling on the choice.

Her quiet doubt — that work counts only when it involves slicing brains or
running gels — is answered by the site's own structure. The
[Technical practice]({{ '/hidden-curriculum/technical-practice/' | relative_url }})
norms she can bake into her toolbox release (versions pinned, assumptions
named, exclusions reported) are what make a computational contribution one
that other scientists can actually build on, which is the working definition
of counting.

</section>

<section class="section" id="insights">
  <h2>Key Insights</h2>
  <div class="cards-grid" style="margin: 2rem 0;">
    <div class="card" style="border-left: 4px solid var(--neural-blue);">
      <h3 style="color: var(--neural-blue);">Inner Conflict</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Wants to help others but worries she’s still too new herself</li>
        <li>Torn between staying in academia or joining a neurotech startup</li>
        <li>Feels pressure to always be “the explainer” in cross-disciplinary settings</li>
      </ul>
    </div>
    <div class="card" style="border-left: 4px solid var(--cerebral-purple);">
      <h3 style="color: var(--cerebral-purple);">Journey Markers</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Published reusable Jupyter template for EM visualization</li>
        <li>Presented on model error modes at a neuroML workshop</li>
        <li>Started mentoring Julian—and learned as much as she taught</li>
      </ul>
    </div>
    <div class="card" style="border-left: 4px solid var(--axon-cyan);">
      <h3 style="color: var(--axon-cyan);">Growth Path</h3>
      <ul style="color: #4b5563; margin: 0; font-size: 0.9rem;">
        <li>Learns to embrace partial knowledge</li>
        <li>Gains feedback literacy through peer review</li>
        <li>Realizes her impact comes from enabling others as much as producing code</li>
      </ul>
    </div>
  </div>
</section>

</div>
