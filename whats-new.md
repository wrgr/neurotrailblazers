---
layout: page
title: "What's New"
permalink: /whats-new/
description: "What was added or changed on the site, by date. Entries come from the commit history; nothing is listed that is not on the site."
slug: whats-new
content_type: navigation
---

Each entry names what changed and where to find it. Dates are commit dates. Every
page that shows a "Last reviewed" line at the bottom gets that date from the same
history (`scripts/refresh_last_reviewed.rb` in the repository), so the line means
"last committed change", not "last read by a person".

## September 2026

### 2026-09-28

- **Finding your way.** Every page now has a breadcrumb at the top and, at the bottom, previous and next links where the page is one step in a sequence: the nine technical units and their lecture plans, the 25 modules with their session kits and model responses, the five sessions of the short lecture series, the ten Pathways workshops, and the hidden-curriculum pages. Pages outside a sequence show an "Up" link to their section. A "Last reviewed" date appears on pages that carry one, and this page lists what changed.
- **Beyond EM.** A content-library page on X-ray, expansion and light-sheet microscopy and barcoded sequencing: what each resolves, and which questions still need electron microscopy. [Read it]({{ '/content-library/imaging/beyond-em/' | relative_url }}).
- **More model responses.** Model responses for Modules 02, 08, 17, 19, 20, 21, 22 and 25 join those for 01, 07 and 18, and the index now lists every key that exists. [Model responses index]({{ '/teaching/answers/' | relative_url }}).
- **Funding and jobs.** A hidden-curriculum page on how trainees are paid, how to read a grant number, and how to find who funds a lab, with every figure quoted from a dated official source. [Read it]({{ '/hidden-curriculum/funding-and-jobs/' | relative_url }}).
- **For instructors.** An [instructor FAQ]({{ '/teaching/faq/' | relative_url }}) (35 questions), [46 practice items for the nine technical units]({{ '/teaching/assessment/units/' | relative_url }}), and a [two-day workshop map]({{ '/teaching/syllabi/two-day/' | relative_url }}) with pacing notes.
- **Reference pages expanded.** The [MICrONS case study]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }}) now covers how calcium imaging was matched to EM and what that data can support; [provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) and [neuron-type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) are rewritten, with worked examples from the MICrONS lab's real outputs.
- **Modules.** Every module page now says why it matters, what it does not cover, the common errors, and where its hours go; reference lists are checked against Crossref. Module 22 is now *Scientific Presentation*.
- **Concept Explorer.** Grown from 12 to 61 concepts across the units, library and teaching pages. [Open it]({{ '/concepts/' | relative_url }}).
- **Sources.** Claims the September audit left unsourced now cite a primary source, carry an explicit label such as "our arithmetic" or "rule of thumb", or were removed.

### 2026-09-26

- **Site audit for accuracy and voice.** Two fabrication audits and a verified registry of canonical facts, applied across the front door, Neuronauts, datasets and tools, the content library, the technical course, the hidden curriculum, teaching and Pathways. Invented figure captions were removed. A new page, [Comparative connectomics]({{ '/content-library/connectomics/comparative-connectomics/' | relative_url }}), covers what carries over between worm, fly, mouse and human connectomes.
- **Curriculum values corrected.** Invented results were moved off real datasets and versions onto labeled fictional releases across the 25 modules, their kits and their decks; dataset figures were aligned to the verified registry; timing tables and a 1,000x storage error were fixed. Worksheets, decks and session kits were regenerated. [Module Library]({{ '/modules/' | relative_url }}).
- **Journal club data corrected against Crossref.** Author lists, titles or journal names were rebuilt for 97 records, 117 publication years were corrected and one duplicate removed, in the [Journal Club]({{ '/technical-training/journal-club/' | relative_url }}) and the [journal paper corpus]({{ '/content-library/journal-papers/' | relative_url }}).
- **Model responses and an assessment bank.** Public model responses for Modules 01, 07 and 18 at [/teaching/answers/]({{ '/teaching/answers/' | relative_url }}), and a 20-item assessment bank for the four lecture sessions, with worked answers, per-error feedback and variant templates, at [/teaching/assessment/]({{ '/teaching/assessment/' | relative_url }}).
- **MICrONS Real-Data Lab.** A version-pinned notebook that reads static public MICrONS (minnie65_public v1507) exports with no account, verifies file hashes, applies counted inclusion rules to 2,070 proofread cells and compares reciprocity against three null models at two thresholds. Four clean-environment reruns were byte-identical; the outputs are archived. [Open the lab]({{ '/notebooks/microns-lab/' | relative_url }}).
- **Module kit materials.** An audit found 70 named materials missing across Modules 01 to 19. Thirty were published as labeled synthetic kits with a SHA-256 manifest, 35 were rewritten to point at what exists, and 5 were linked. CI now checks that every kit material resolves. [Session kits]({{ '/teaching/sessions/' | relative_url }}).
- **Ethics and Governance session; syllabus maps.** Ethics and Governance is packaged as the optional fifth session of the [short lecture series]({{ '/teaching/sequence/' | relative_url }}), with a 90-minute plan, a worksheet on an invented release and model responses. New [10-week and 16-week syllabus maps]({{ '/teaching/syllabi/' | relative_url }}) sequence the lecture sessions, technical units, module kits and Pathways workshops week by week.
- **Graduate deck claim audit.** 317 claims on the five graduate decks were checked against primary sources: 166 verified, 70 corrected, 47 qualified, 20 labeled as hypothetical and 14 listed for the owner. Matching errors on Units 01 and 02 and two reference pages were fixed and the decks re-rendered. [Presentation Decks]({{ '/technical-training/slides/' | relative_url }}).
- **Professional Pathways workshops.** The ten COMPASS workshops are packaged as 90-minute sessions, each with a timed plan, a learner worksheet built on an invented case and model responses with a 0-2 rubric, then reviewed as one series so cases, names and follow-through line up. [Pathways hub]({{ '/teaching/pathways/' | relative_url }}).
- **Four lectures packaged.** The four connectomics lectures each have a plan, slides, a learner worksheet and model responses, and the Teaching menu was simplified around them. [Short lecture series]({{ '/teaching/sequence/' | relative_url }}).
- **Neuronauts print files.** Service-ready color print exports and a two-inch edition of the Neuronauts models. [Neuronauts]({{ '/neuronauts/' | relative_url }}).

### 2026-09-25

- **Teaching decks redesigned.** The shared Marp theme, the 25 module decks and the ten technical decks adopt the nanoscale tissue design: H01 imagery, a charcoal and warm-paper palette, Source Sans type, with scale bars and attribution kept on covers. Dense generated content was repaginated without dropping text. [Presentation Decks]({{ '/technical-training/slides/' | relative_url }}).
- **Copy and layout scrub.** Site copy and the reading layouts on small screens were tidied, and the Journal Club's research synthesis panel now stays hidden until asked for.

### 2026-09-24

- **Two standalone graduate lectures.** Synapse Detection (39 slides) and Connectomics Ethics and Governance (31 slides), each built from one content-library page and ending with a slide on what it does not cover. Linked from their source pages and from a new section of the [decks index]({{ '/technical-training/slides/' | relative_url }}); they are not part of any course.
- **Technical units filled in.** Content gaps in the nine units were closed and the graduate decks linked in; the ten unit decks gained source lines, speaker notes and overflow fixes. [Technical Course]({{ '/technical-training/' | relative_url }}).

### 2026-09-15 to 2026-09-16

- **CI gates.** A check that every class JavaScript toggles has a CSS rule; the work plan restatused.

### 2026-09-07 to 2026-09-08

- **Start Here rebuilt.** The Persona Pathfinder on [Start Here]({{ '/start-here/' | relative_url }}) now runs on the site's four real personas.
- **Citation graph.** The [Citation Graph Explorer]({{ '/technical-training/journal-club/graph/' | relative_url }}) and its corpus tooling were brought into the site.
- **Navigation and naming.** One label per thing, a [Tools]({{ '/tools/' | relative_url }}) page that lists only what exists, no emoji in the chrome, and a stacking order for the dropdowns. The 25 slide-wrapper pages were folded into the [session kits]({{ '/teaching/sessions/' | relative_url }}). Decks render deterministically and carry speaker notes.
- **CI gate.** Site paths written in code spans are checked against the built site.

### 2026-09-05

- **About, license and citation.** New [About]({{ '/about/' | relative_url }}) and [License and reuse]({{ '/license/' | relative_url }}) pages name the HI-MC award, the contributors and how to cite the site; the site line settled on "Mapping connections. Making connections." and the brand adopted the synapse mark.
- **Datasets as a collection.** The [catalog]({{ '/datasets/' | relative_url }}) became a real Jekyll collection, one record per dataset, and gained FANC, MANC, BANC and larval zebrafish.
- **Content library.** New reference pages on [ethics and governance]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}) and [synapse detection as a method]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}), a domain map that works, and two generated banners.
- **Teaching.** Real practice content for every module, themed unit decks and a CI gate; the three graduate lecture decks surfaced; three resources that did not exist were replaced; the [Program Models]({{ '/models/' | relative_url }}) page collapses three pages that described one thing.
- **Journal papers.** `journal_papers.yml` is regenerated from the corpus and guarded in CI; the corpus page shows its allocation target against what shipped.
