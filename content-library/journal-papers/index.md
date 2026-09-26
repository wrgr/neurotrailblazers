---
layout: page
title: "Journal Paper Corpus & Literature Hub"
permalink: /content-library/journal-papers/
description: "A 2,000-paper connectomics corpus in 12 research domains and 3 nested tiers (500, 1,000 and 2,000 papers), with published abstracts, a citation graph, and 95 hand-written paper summaries."
use_layout_hero: false
content_type: core
---

# Journal Paper Corpus & Literature Hub

The NeuroTrailblazers literature corpus holds **2,000 connectomics papers**, chosen by their place in the field's citation graph and sorted into 12 research domains. It covers the science, the tools, the applications and the training of nanoscale connectomics. Two layers sit on top of it: 95 papers with hand-written summaries on the topic pages below, and a browsable card for every paper in the journal club.

<div class="jc-hero-stats" style="display: flex; gap: 1rem; flex-wrap: wrap; margin: 1.25rem 0 1.5rem 0;">
  <span class="jc-hero-stat" style="background:#eff6ff; color:#1d4ed8; font-weight:700; padding:0.4rem 0.8rem; border-radius:6px; font-size:0.9rem;">2,000 Total Papers</span>
  <span class="jc-hero-stat" style="background:#f0fdf4; color:#15803d; font-weight:700; padding:0.4rem 0.8rem; border-radius:6px; font-size:0.9rem;">12 Canonical Domains</span>
  <span class="jc-hero-stat" style="background:#faf5ff; color:#7e22ce; font-weight:700; padding:0.4rem 0.8rem; border-radius:6px; font-size:0.9rem;">3 Nested Tiers (500 / 1000 / 2000)</span>
  <span class="jc-hero-stat" style="background:#fef3c7; color:#b45309; font-weight:700; padding:0.4rem 0.8rem; border-radius:6px; font-size:0.9rem;">5,460 Citation Links</span>
</div>

---

## Ways to explore the corpus

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin: 1.5rem 0;">

  <div style="border: 1px solid #e2e8f0; border-radius: 10px; padding: 1.25rem; background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0; color:#1a56db;">Citation Graph Explorer</h3>
    <p style="font-size:0.88rem; color:#475569; line-height:1.5;">
      See which papers in the corpus cite which, laid out by a force-directed graph. Filter by domain, organism and era, and copy a prompt that lists the papers in view for use with an AI assistant.
    </p>
    <a href="{{ '/technical-training/journal-club/graph/' | relative_url }}" style="font-weight:700; color:#1a56db; text-decoration:none;">Open Graph Explorer &rarr;</a>
  </div>

  <div style="border: 1px solid #e2e8f0; border-radius: 10px; padding: 1.25rem; background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0; color:#059669;">Journal Club &amp; Reading Paths</h3>
    <p style="font-size:0.88rem; color:#475569; line-height:1.5;">
      Browse a card for every paper, with its published abstract, filters by domain, era and tier, and seminar discussion prompts. The OCAR notes and three-level summaries on the cards are written per research domain, not per paper.
    </p>
    <a href="{{ '/technical-training/journal-club/' | relative_url }}" style="font-weight:700; color:#059669; text-decoration:none;">Browse Journal Club &rarr;</a>
  </div>

  <div style="border: 1px solid #e2e8f0; border-radius: 10px; padding: 1.25rem; background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0; color:#7c3aed;">Major Research Initiatives</h3>
    <p style="font-size:0.88rem; color:#475569; line-height:1.5;">
      Programs, consortia, datasets and open tools behind the papers, including NIH BRAIN CONNECTS, IARPA MICrONS, Janelia FlyEM, the Allen Institute, the Max Planck Society, BossDB and CIRCUIT.
    </p>
    <a href="{{ '/initiatives/' | relative_url }}" style="font-weight:700; color:#7c3aed; text-decoration:none;">Explore Major Initiatives &rarr;</a>
  </div>

</div>

---

## Twelve research domains

The corpus was built to a stratified allocation, so that no single axis &mdash;
experimental, computational, biological, pedagogical &mdash; could crowd out the others.
The **target** column is that design; the **in the corpus** column is what the shipped
data actually contains, counted from `_data/journal_papers.yml` at build time rather than
typed here.

{% assign rows = "circuit-structure|Circuit Structure &amp; Connectomes|15.0%|300|Dense synaptic wiring diagrams, circuit motifs, connectivity graphs;;pipeline|Pipeline &amp; Software Engineering|15.0%|300|Automated 3D segmentation, synapse detection, proofreading (CAVE/CATMAID);;physiology|Physiological Validation &amp; Function|12.0%|240|In vivo 2-photon imaging, electrophysiology, structure-function mapping;;behaviour|Behavior &amp; Circuit Dynamics|12.0%|240|Ring attractors, navigation, sensory-motor control, escape behaviour;;imaging|Volume EM &amp; Advanced Optics|8.0%|160|SBF-SEM, FIB-SEM, multibeam arrays, tissue prep, expansion microscopy;;cell-types|Cell Types &amp; Morphological Census|8.0%|160|Morphological clustering, synaptic fingerprints, multi-modal cell types;;neuroanatomy|Neuroanatomy &amp; Ultrastructure|8.0%|160|Synaptic active zones, spine density, organelle distributions, glia;;synthesis|Synthesis, Theory &amp; Reviews|5.0%|100|Canonical field reviews, graph theory principles, conceptual frameworks;;dataset|Benchmark Datasets &amp; Repositories|5.0%|100|Open petascale public volumes (FlyWire, MICrONS, H01, Kasthuri);;neuroai|NeuroAI, Biophysics &amp; Models|5.0%|100|Connectome-constrained artificial networks, biophysical simulations;;health|Health, Disease &amp; Translation|5.0%|100|Nanoscale connectopathies, Alzheimer's, Huntington's, epilepsy rewiring;;training-outreach|Workforce Training &amp; Outreach|2.0%|40|Traineeship design, undergraduate pedagogy, citizen science" | split: ";;" %}

| Research domain | Share | Target | In the corpus | Core research focus |
| :--- | :---: | :---: | :---: | :--- |
{% for row in rows -%}
{%- assign f = row | split: "|" -%}
{%- assign n = site.data.journal_papers.papers | where: "dimension", f[0] | size -%}
| [**{{ f[1] }}**]({{ '/technical-training/journal-club/' | relative_url }}?dimension={{ f[0] }}) | {{ f[2] }} | {{ f[3] }} | {{ n }} | {{ f[4] }} |
{% endfor %}

{% assign allocated = 0 %}{% for row in rows %}{% assign f = row | split: "|" %}{% assign n = site.data.journal_papers.papers | where: "dimension", f[0] | size %}{% assign allocated = allocated | plus: n %}{% endfor %}{% assign unallocated = site.data.journal_papers.papers.size | minus: allocated %}

**Where the two columns differ, the corpus is the truth.** Retrieval found more
synthesis and benchmark-dataset literature than the allocation anticipated, and less on
health and translation and on workforce training &mdash; which says something about the
field's published output rather than about curation. A further **{{ unallocated }}**
papers carry a label outside these domains and are not counted above.

---

## Hand-written paper summaries by topic

For courses and seminar series, these 11 pages each give a small set of papers, with citations checked against Crossref and summaries written for that paper at three levels:

| Category | Count | Focus |
| :--- | :---: | :--- |
| [Neuroanatomy]({{ '/content-library/journal-papers/neuroanatomy/' | relative_url }}) | 8 | Ultrastructural foundations, synapses, and organelles |
| [Imaging]({{ '/content-library/journal-papers/imaging/' | relative_url }}) | 8 | Volume EM, FIB-SEM, and serial sectioning |
| [Computer Vision &amp; ML]({{ '/content-library/journal-papers/computer-vision-ml/' | relative_url }}) | 10 | Automated segmentation, affinity graphs, and FFNs |
| [Data Storage &amp; Infrastructure]({{ '/content-library/journal-papers/data-storage/' | relative_url }}) | 8 | Petascale volumetric cloud stores and spatial indexing |
| [Proofreading &amp; Annotation]({{ '/content-library/journal-papers/proofreading/' | relative_url }}) | 8 | Human-in-the-loop proofreading and citizen science |
| [Cell Types &amp; Morphology]({{ '/content-library/journal-papers/cell-types/' | relative_url }}) | 8 | Morphological classification and synaptic fingerprints |
| [Connectomics]({{ '/content-library/journal-papers/connectomics/' | relative_url }}) | 8 | Saturated reference connectomes across species |
| [Network Analysis]({{ '/content-library/journal-papers/network-analysis/' | relative_url }}) | 9 | Graph theory, motifs, and topological invariance |
| [MRI &amp; Meso-Connectomics]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }}) | 10 | Diffusion MRI and macroscale tractography |
| [NeuroAI &amp; Biophysics]({{ '/content-library/journal-papers/neuroai/' | relative_url }}) | 8 | Connectome-constrained artificial neural networks |
| [Case Studies]({{ '/content-library/journal-papers/case-studies/' | relative_url }}) | 10 | Biological circuit discoveries and behavioral mechanisms |

**Total: 95 papers** across the 11 topic pages, counted as entries: a few papers, such as FlyWire and H01, appear on more than one page.

---

## Downloads

The three nested tiers are available as JSON files:

* **[500 Key Papers (`corpus_500.json`)]({{ '/data/corpus_500.json' | relative_url }})**:
  The 500 most central papers, with abstracts, domain-level OCAR notes and summaries, discussion prompts, and citation graph metrics.
* **[1000 Key Papers (`corpus_1000.json`)]({{ '/data/corpus_1000.json' | relative_url }})**:
  The 1,000-paper tier, with abstracts, domain-level OCAR notes, and in/out citation degrees.
* **[2000 Key Papers (`corpus_2000.json`)]({{ '/data/corpus_2000.json' | relative_url }})**:
  All 2,000 papers, with abstracts, domain-level OCAR notes and summaries, and per-paper in/out citation degrees. The 5,460 internal citation links are drawn in the [Citation Graph Explorer]({{ '/technical-training/journal-club/graph/' | relative_url }}).

**What is per paper and what is not.** The title, authors, year, venue, DOI, abstract and citation links are specific to each paper. The OCAR notes (Opportunity, Challenge, Resolution, Future Work), most of the three-level summaries and the discussion prompts were drafted per research domain, so every paper in a domain shares that text; the Action line fills in the paper's own title and authors. Read the abstract for what a given paper actually found. Author lists and titles were checked against Crossref in September 2026.
