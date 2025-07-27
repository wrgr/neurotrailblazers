TASK: Build a complete GitHub Pages-compatible Jekyll site titled NeuroTrailblazers. This is a curriculum and mentorship platform aligned with the HI-MC grant and the NIH CONNECTS program. It supports undergraduates and graduate students learning nanoscale connectomics, with a focus on discovery, merit-based training, and open science.

🔧 Core Technical Requirements
✅ Jekyll-based for GitHub Pages (wrgr/neurotrailblazers)

✅ Responsive layout, modern typography (Inter)

✅ Custom CSS (site-styles.css) inspired by neuroscience and discovery

✅ Animated hero banner on homepage

✅ Collections: modules, archetypes, datasets

✅ Fully deployable site with _config.yml, index.html, and markdown content

✅ All modules and pages should use real front matter and Markdown

🧠 Thematic Identity
Style evokes scientific discovery: neurons, EM data, connectomes

Color palette:

Neural Blue: #2563eb

Cerebral Purple: #7c3aed

Axon Cyan: #06b6d4

Brain Gray: #f3f4f6

Synapse Black: #111827

📁 Required Folder Structure
pgsql
Copy
Edit
neurotrailblazers/
├── _config.yml
├── index.html
├── start-here.md
├── models.md
├── workflow.md
├── README.md
├── archetypes/
│   ├── index.md
│   ├── undergrad-firstgen.md
│   ├── grad-student.md
│   └── postdoc-ai.md
├── modules/
│   ├── module-0-inspiration/index.md
│   ├── module-1-intro/index.md
│   └── [modules 2-15]/index.md
├── datasets/
│   ├── index.md
│   ├── kasthuri2015.md
│   ├── bock2011.md
│   ├── microns2025.md
│   ├── flywire2024.md
│   ├── hemibrain2020.md
│   └── white1986.md
├── assets/
│   ├── css/site-styles.css
│   └── images/
└── scripts/
    ├── course-generator.js
    └── chatbot.js
📚 Content Requirements
🔹 Modules 0–15:
For each module:

SMART learning objectives

Overall training goal

Representative image or placeholder

Key reference papers with inline citations

Public content (e.g., videos, talks, press)

🔹 models.md:
Full explanation of:

MERIT framework (6 stages, scientific method alignment)

COMPASS workshops (10 total)

CCR dimensions (Knowledge, Skills, Character, Meta-Learning)

Inline citations:

Lopatto (2007)

Duckworth (2007)

Fadel (2015)

Cervantes (2022)

🔹 workflow.md:
Step-by-step guide to the HI-MC nanoscale connectomics pipeline

Align each pipeline stage with relevant MERIT/COMPASS stages

🔹 datasets/:
Each dataset page should include:

Visual image (EM screenshot, neuron segmentation, etc.)

Title, author/year (e.g., Kasthuri et al. 2015)

Claims and highlights

DOI or direct link to data

Link to any public explorer (e.g., FlyWire, MICrONS, neuPrint)

🧑‍🔬 Archetypes
Include three profiles in /archetypes/:

Julian – First-gen undergrad just starting research

Layla – Grad student navigating dissertation and publishing

Elias – Postdoc with AI experience trying to merge disciplines

Each should include:

Bio/story

Challenges

Successes

Chatbot mentor placeholder script

🧩 Technical Features
Animated landing page hero banner

Grid layout for module and dataset cards

Subtle hover transitions on cards

Navigation with dropdown menus

Search (basic Jekyll search)

Mobile-first design

🎯 NIH CONNECTS / HI-MC Integration
Must reflect the goals of the HI-MC grant

Emphasize open science, pipeline learning, and equitable opportunity

Position NeuroTrailblazers as a national training and mentorship tool

📝 Summary
You are generating a deployable Jekyll site with curriculum, datasets, and mentoring tools tailored to nanoscale connectomics. The design, layout, and educational content must reflect the rigor and vision of an NIH-funded scientific initiative.

