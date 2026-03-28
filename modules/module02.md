---
title: "Module 02: Research Foundations and the Hidden Curriculum"
layout: module
permalink: /modules/module02/
description: "Learn the unwritten norms of research practice while using real connectomics datasets responsibly."
module_number: 2
difficulty: "Beginner"
duration: "4 hours"
learning_objectives:
  - "Describe key hidden-curriculum norms in research settings"
  - "Navigate roles, expectations, and communication channels"
  - "Use dataset documentation to infer responsible analysis boundaries"
  - "Build a personal support/mentorship map"
prerequisites: "Module 01"
merit_stage: "Foundations"
compass_skills:
  - "Research Literacy"
  - "Professional Communication"
  - "Self-Advocacy"
ccr_focus:
  - "Meta-Learning - Hidden Curriculum"
  - "Character - Belonging and Agency"

# Normalized metadata
slug: "module02"
short_title: "Research Foundations & the Hidden Curriculum"
status: "active"
audience:
  - "students"
pipeline_stage: "Foundations"
merit_row_focus: "Foundations"
topics:
  - "hidden-curriculum"
  - "research-roles"
  - "dataset-orientation"
summary: "Make implicit research expectations explicit while building responsible dataset orientation habits."
key_questions:
  - "What norms are assumed but rarely taught?"
  - "How do I ask for help effectively in research spaces?"
slides: []
notebook: []
datasets:
  - "/datasets/access"
  - "/datasets/workflow"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/ask-an-expert/"
related_frameworks:
  - "education-models"
prerequisites_list: []
next_modules:
  - "module03"
references: []
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Create a personal research-navigation plan that includes role expectations, communication scripts, and mentor support pathways. Demonstrate understanding of research ethics norms specific to connectomics, including data attribution, responsible use of human tissue data, and collaborative proofreading etiquette.

## Why this module matters
Every research environment operates on two sets of rules: the official ones (written in handbooks and syllabi) and the unofficial ones (learned through trial, error, and observation). The "hidden curriculum" includes how to ask a question in lab meeting without sounding dismissive, how to credit a colleague who helped debug your code, how to admit you do not understand something without losing credibility, and how to navigate the hierarchy from undergraduate to PI. In connectomics, these norms are amplified by the field's inherently collaborative structure: the FlyWire whole-brain connectome was produced by 287 proofreaders across dozens of institutions. Knowing how to collaborate, attribute, and communicate is not a soft skill --- it is a core technical competency.

## Concept set

### 1) The "hidden curriculum" of research
- **Technical:** unwritten norms govern scientific research --- how to ask questions, how to admit uncertainty, how to give and receive feedback, how to navigate lab hierarchies. These norms vary by institution, lab, and PI, but common patterns exist: arrive at meetings prepared, version-control your work, attribute contributions explicitly, escalate problems early rather than late.
- **Plain language:** there are rules nobody writes down but everyone is expected to follow.
- **Misconception:** you will be taught everything you need to know. In practice, many critical skills (how to write a methods section, how to respond to a reviewer, how to push back on a senior colleague's suggestion) are learned by watching others, making mistakes, or asking directly.

### 2) Research ethics in connectomics
- **Technical:** connectomics raises specific ethical considerations. Data sharing norms require that datasets be made available for replication (e.g., FlyWire, MICrONS). Attribution must credit proofreaders, not just PIs. Human tissue data (e.g., from surgical resections for epilepsy studies) requires IRB oversight and careful de-identification. Provenance tracking ensures that analyses can be traced back to specific dataset versions.
- **Plain language:** know where the data came from, who did the work, and what rules govern its use.
- **Misconception:** if the data is publicly available, there are no ethical considerations. Public availability does not eliminate the need for proper attribution, version tracking, and responsible interpretation.

### 3) Collaboration norms in large-scale projects
- **Technical:** connectomics is inherently collaborative. The FlyWire project coordinated 287 proofreaders across time zones and institutions. MICrONS involved teams at the Allen Institute, Princeton, and Baylor. Effective collaboration requires shared conventions for naming, version control, conflict resolution, and communication channels. Disagreements about segment boundaries are resolved through consensus protocols, not authority.
- **Plain language:** you will work with many people; learn the rules of teamwork before you need them.
- **Misconception:** research is a solitary activity. Modern connectomics is closer to open-source software development than to the lone-genius model.

### 4) Failure as data
- **Technical:** in research, negative results and errors are informative, not shameful. A failed segmentation run reveals something about image quality, algorithm parameters, or tissue preparation. A proofreading error that is caught and corrected improves the dataset and trains the annotator. Labs that punish errors get fewer error reports, not fewer errors.
- **Plain language:** mistakes are information; hiding them helps nobody.
- **Misconception:** good researchers do not make mistakes. In practice, the best researchers make mistakes, document them, and learn from them systematically.

### 5) Communication scripts for common situations
- **Technical:** having pre-planned language for difficult situations reduces anxiety and improves outcomes. Key scripts include: asking for help ("I have been stuck on X for Y hours; here is what I have tried..."), admitting uncertainty ("I am not confident in this annotation because..."), giving feedback ("I noticed a potential issue with segment Z; could we review it together?"), and escalating problems ("This issue is beyond my current skill level; who should I consult?").
- **Plain language:** practice what you will say before you need to say it.
- **Misconception:** scripted communication is inauthentic. In reality, scripts are scaffolds that build confidence until the language becomes natural.

## Hidden curriculum scaffold
- Unspoken norms: meeting etiquette, version-control expectations, attribution etiquette, escalation paths.
- Explicit supports: script templates, expectation checklists, mentorship map.
- Ethics anchors: data provenance, attribution chains, human-tissue protocols.
- Collaboration patterns: shared naming conventions, conflict resolution, communication channels.

## Core workflow
1. Decode one research setting's unwritten rules.
2. Map roles and communication paths.
3. Practice help-seeking script.
4. Define personal support network.
5. Identify ethical considerations relevant to your dataset.
6. Draft attribution and collaboration norms for your team.

## Detailed run-of-show (90 minutes)

### Block 1: Hidden curriculum reveal (00:00-15:00)
- **Instructor script:** "Raise your hand if you have ever felt lost in a research setting --- not because the science was hard, but because you did not know the unwritten rules." (Expect most hands.) "Today we make those rules explicit."
- Present 5 hidden-curriculum scenarios (3 minutes each):
  1. You disagree with a senior lab member's interpretation at lab meeting. What do you do?
  2. You find a bug in shared analysis code. How do you report it?
  3. You need help but your mentor is busy. Who else can you ask?
  4. You are asked to proofread neurons outside your assigned region. Should you?
  5. A collaborator uses your annotation work in a paper without crediting you. How do you respond?
- For each scenario, collect 2-3 responses from learners, then present a recommended approach.

### Block 2: Role and expectation mapping (15:00-30:00)
- **Instructor script:** "Every research team has roles. Let's map them." Draw a role diagram on the board: PI, postdoc, graduate student, undergraduate, technician, proofreader, data manager. For each role, ask: "What does this person expect from you? What can you expect from them?"
- Learners fill in a role-expectation worksheet for their own research setting (or a hypothetical one).
- Discuss: where do expectations conflict? Where are they ambiguous?

### Block 3: Ethics in connectomics (30:00-45:00)
- **Instructor script:** "Connectomics data is not just pixels. It comes from real organisms, sometimes from human patients. Let's talk about what that means."
- Cover three ethics topics:
  1. **Data provenance:** every analysis should reference a specific dataset version. Show how CAVE materialization versions work.
  2. **Attribution:** the 287 FlyWire proofreaders were co-authors. Discuss what fair attribution looks like at scale.
  3. **Human tissue:** discuss IRB requirements, de-identification, and the responsibility that comes with working on data derived from surgical patients.
- Group discussion: "What ethical situation might you encounter in your work? How would you handle it?"

### Block 4: Communication script workshop (45:00-65:00)
- **Instructor script:** "We are going to practice the hardest part of research: talking to people." Distribute script templates for five common situations (asking for help, admitting uncertainty, giving feedback, receiving feedback, escalating problems).
- Learners customize scripts for their own context (10 min).
- Role-play in pairs: one person plays the mentor/colleague, the other practices the script (10 min, switch roles).

### Block 5: Personal navigation plan (65:00-85:00)
- **Instructor script:** "Now bring it all together. You are going to create a one-page document that you can actually use."
- Learners draft their "lab navigation playbook" including:
  1. Top 5 norms for their research setting.
  2. Role-expectation map for their team.
  3. Three communication scripts customized for their context.
  4. Mentor/support map: at least 3 people they can go to for different types of help.
  5. Ethical commitments: how they will handle attribution, data provenance, and error reporting.

### Block 6: Exit ticket (85:00-90:00)
- Submit: (1) your lab navigation playbook; (2) one reflection sentence on the most surprising hidden-curriculum norm you learned today.
- **Instructor script:** "Keep this playbook accessible. Revise it as you learn more about your research environment."

## Studio activity: "Build your lab navigation playbook"

### Overview
Learners produce a one-page research navigation document that serves as a practical reference throughout the program.

### Part A: Norms inventory (15 minutes)
1. List 5 unwritten norms you have encountered (or expect to encounter) in research settings.
2. For each norm, write: (a) what the norm is, (b) how you learned it (or how you think most people learn it), (c) what happens when someone violates it.
3. Star the 2 norms you find most challenging to follow.

### Part B: Communication scripts (20 minutes)
Write customized scripts for three situations:
1. **Asking for help:** "I have been working on [X] for [time]. Here is what I have tried: [list]. I am stuck on [specific point]. Could you [specific request]?"
2. **Giving feedback:** "I noticed [specific observation] in [specific work]. I wanted to flag it because [reason]. Would it help to [proposed action]?"
3. **Admitting uncertainty:** "I am not confident about [specific decision] because [reason]. My best guess is [guess], but I would like to [verify/discuss/get a second opinion]."

### Part C: Mentor and support map (15 minutes)
Create a table with columns: Name | Role | What I can ask them | How to reach them | Backup contact.
Fill in at least 3 rows. Include at least one peer, one senior person, and one person outside your immediate team.

### Part D: Ethics commitment (10 minutes)
Write 3-5 sentences describing your commitments regarding:
- How you will track data provenance in your work.
- How you will attribute contributions from collaborators.
- How you will handle errors (your own and others').

## Assessment rubric
- **Minimum:** clear norms list, help-seeking plan, and at least one communication script.
- **Strong:** realistic escalation paths, reflection on barriers, ethics commitment with specific practices, mentor map with backup contacts.
- **Failure:** generic advice without actionable steps; no personalization to learner's own context.

## Content library references
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
- [FlyWire whole-brain]({{ '/content-library/case-studies/flywire-whole-brain/' | relative_url }})

## Teaching resources
- [Start Here]({{ '/start-here/' | relative_url }})
- [Learner Personas]({{ '/avatars/' | relative_url }})
- [Dataset Access Guide]({{ '/datasets/access/' | relative_url }})

## Academic references
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. *Nature*, 634, 124-138.
- Cossell, L., et al. (2015). Functional organization of excitatory synaptic strength in primary visual cortex. *Nature*, 518(7539), 399-403.
- National Academies of Sciences, Engineering, and Medicine. (2018). *Graduate STEM Education for the 21st Century*. The National Academies Press.
- Margolis, E., & Romero, M. (2001). *The Hidden Curriculum in Higher Education*. Routledge.
- MICrONS Consortium. (2021). Functional connectomics spanning multiple areas of mouse visual cortex. *bioRxiv*. https://doi.org/10.1101/2021.07.28.454025
- Lichtman, J. W., Pfister, H., & Shavit, N. (2014). The big data challenges of connectomics. *Nature Neuroscience*, 17(11), 1448-1454.

## Quick practice prompt
Draft one email requesting clarification on an unclear lab expectation. Then write a 2-sentence ethics commitment explaining how you will handle attribution in a collaborative proofreading project.
