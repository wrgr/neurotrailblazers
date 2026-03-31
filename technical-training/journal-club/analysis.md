---
layout: default
title: "Bibliometric Analysis"
permalink: /technical-training/journal-club/analysis/
sitemap: false
robots: noindex
description: "Internal bibliometric analysis of the EM connectomics literature: citation graphs, community detection, paper lineage, and strategic audit results."
---

<div class="layout-content layout-page">

<section class="jc-hero">
  <h1>Bibliometric Analysis</h1>
  <p>Data-driven analysis of the EM connectomics literature. Built from 7,925 papers via OpenAlex, scored by composite metric (0.35 PageRank + 0.25 citations + 0.20 betweenness + 0.20 recent PageRank), organized into 30 Louvain communities.</p>
  <div class="jc-hero-stats">
    <span class="jc-hero-stat">7,925 papers in corpus</span>
    <span class="jc-hero-stat">Top 500 ranked</span>
    <span class="jc-hero-stat">200 with OCAR cards</span>
    <span class="jc-hero-stat">30 communities</span>
  </div>
</section>

<section class="section section-compact">
  <h2>Interactive Visualizations</h2>

  <h3>Field Map &mdash; Citation Network</h3>
  <p>Force-directed graph of the connectomics citation network. Nodes are papers; edges are citations. Color encodes community membership. Click nodes for details.</p>
  <iframe src="/assets/analysis/field_map.html" width="100%" height="700" style="border:1px solid #2a2a4a; border-radius:6px; background:#0a0a1a;" loading="lazy"></iframe>

  <h3 style="margin-top:2rem;">Research Evolution (2000&ndash;2025)</h3>
  <p>How research communities have grown over time. Toggle between stacked area, streamgraph, and line views.</p>
  <iframe src="/assets/analysis/evolution_graph.html" width="100%" height="700" style="border:1px solid #2a2a4a; border-radius:6px; background:#0a0a1a;" loading="lazy"></iframe>
</section>

<section class="section section-compact">
  <h2>Reading List Structure</h2>
  <p>The top 500 papers are organized into five reading phases, topologically sorted so that citation prerequisites appear before dependent papers.</p>

  <table style="width:100%; border-collapse:collapse; margin:1rem 0;">
    <thead>
      <tr style="border-bottom:2px solid #444;">
        <th style="text-align:left; padding:8px;">Phase</th>
        <th style="text-align:left; padding:8px;">Focus</th>
        <th style="text-align:right; padding:8px;">Papers</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="padding:6px 8px;">0 &mdash; Orientation</td><td style="padding:6px 8px;">Review papers; read first</td><td style="text-align:right; padding:6px 8px;">~88</td></tr>
      <tr><td style="padding:6px 8px;">1 &mdash; Foundations</td><td style="padding:6px 8px;">Pre-2010 landmark work</td><td style="text-align:right; padding:6px 8px;">~173</td></tr>
      <tr><td style="padding:6px 8px;">2 &mdash; Core Methods</td><td style="padding:6px 8px;">2010&ndash;2020 techniques</td><td style="text-align:right; padding:6px 8px;">~176</td></tr>
      <tr><td style="padding:6px 8px;">3 &mdash; Landmark Datasets</td><td style="padding:6px 8px;">Major connectome releases</td><td style="text-align:right; padding:6px 8px;">~4</td></tr>
      <tr><td style="padding:6px 8px;">4 &mdash; Frontiers</td><td style="padding:6px 8px;">2021+ recent advances</td><td style="text-align:right; padding:6px 8px;">~59</td></tr>
    </tbody>
  </table>
</section>

<section class="section section-compact">
  <h2>Scoring Methodology</h2>
  <p><strong>Composite score</strong> = 0.35 &times; PageRank + 0.25 &times; normalized citations + 0.20 &times; betweenness centrality + 0.20 &times; recent PageRank</p>
  <ul>
    <li><strong>PageRank</strong> captures influence through citation flow (not just raw count).</li>
    <li><strong>Betweenness</strong> highlights bridge papers connecting different subcommunities.</li>
    <li><strong>Recent PageRank</strong> boosts papers gaining traction in the last 5 years.</li>
    <li><strong>Normalized citations</strong> accounts for overall impact outside the corpus.</li>
  </ul>
  <p>Papers are drawn from three independent corpora seeded by expert-curated paper lists from 66+ researchers in the field, then merged and deduplicated.</p>
</section>

<section class="section section-compact">
  <h2>Strategic Audit Highlights</h2>
  <p>The strategic audit flags papers outside the top-200 OCAR list that warrant human review.</p>

  <h3>Expert-curated papers ranked below 500 (sample)</h3>
  <p>Papers that experts consider important but that fell below our quantitative cutoff:</p>
  <ul>
    <li><em>Functional connectome fingerprinting</em> (Finn et al., 2015) &mdash; 2,967 external citations</li>
    <li><em>Network-based statistic</em> (Zalesky et al., 2010) &mdash; 2,779 external citations</li>
    <li><em>The connectomics of brain disorders</em> (Fornito et al., 2015) &mdash; 1,757 external citations</li>
    <li><em>CATMAID</em> (Saalfeld et al.) &mdash; foundational annotation tool, not in corpus</li>
    <li><em>OME-Zarr</em> &mdash; cloud-optimized format standard, not in corpus</li>
  </ul>

  <h3>High in-degree omissions (most cited <em>within</em> corpus but outside top 500)</h3>
  <p>These papers are heavily cited by other papers in our corpus, suggesting structural importance:</p>
  <ul>
    <li><em>Large-volume en-bloc staining</em> (Hua et al., 2015) &mdash; 171 in-degree</li>
    <li><em>Whole-brain serial-section EM in larval zebrafish</em> (Hildebrand et al., 2017) &mdash; 154 in-degree</li>
    <li><em>The big data challenges of connectomics</em> (Lichtman et al., 2014) &mdash; 86 in-degree</li>
  </ul>

  <h3>Known noise in corpus</h3>
  <p>The automated corpus construction pulls in some off-topic highly-cited papers (cancer statistics, pharmacology tools, etc.) via broad citation chains. These are identified in audit section C1 and filtered from the curated reading list.</p>
</section>

<section class="section section-compact">
  <h2>Recent Reviews Not Yet Ranked</h2>
  <p>Major 2025 reviews identified but too new for citation-based ranking:</p>
  <ul>
    <li>Helmstaedter, <em>Synaptic-resolution connectomics: towards large brains and connectomic screening</em> (Nat. Rev. Neurosci., 2025)</li>
    <li>Bock, <em>Synaptic connectomics: status and prospects</em> (Nat. Rev. Neurosci., 2025)</li>
    <li>Khajeh &amp; Lee, <em>Connectomics beyond electron microscopy</em> (Nat. Methods, 2025)</li>
    <li>Beaudoin, Rheault et al., <em>Rethinking scale in network neuroscience</em> (arXiv, 2025)</li>
    <li>Kasthuri et al., <em>Big data in nanoscale connectomics, and the greed for training labels</em> (Curr. Opin. Neurobiol., 2019)</li>
    <li>Lichtman, Pfister &amp; Shavit, <em>The big data challenges of connectomics</em> (Nat. Neurosci., 2014) &mdash; 86 in-degree, structural gap</li>
  </ul>
</section>

<section class="section section-compact">
  <h2>Quality Audit Summary</h2>

  <h3>Preprint/Published Duplicates</h3>
  <p><strong>65 duplicate pairs</strong> detected in the top 2000. Key impacts:</p>
  <ul>
    <li><strong>11 pairs</strong> where both versions occupy top-500 slots (wasting capacity)</li>
    <li><strong>8 papers</strong> that would enter the top 500 if their preprint + published citations were merged</li>
    <li><strong>~147,000 citations</strong> split across duplicates instead of consolidated</li>
    <li><strong>3 off-topic duplicates</strong> (cancer statistics) inflated by having multiple DOIs</li>
  </ul>

  <h3>Author Name Variants</h3>
  <p><strong>25 name variant groups</strong> detected, 6 involving prolific authors. Mix of true duplicates (Hayworth, Barab&aacute;si, Albert) and false positives (Stephen J Smith &ne; Stephen M Smith). Affects co-authorship metrics and community detection.</p>

  <h3>QA Checklist</h3>
  <p>A structured human-review checklist covering corpus integrity, coverage validation, ranking accuracy, dimension assignment, content quality, and noise monitoring is in <code>strategic_audit.md</code> Section H.</p>
</section>

<section class="section section-compact">
  <h2>Source Data</h2>
  <p>Full analysis outputs are in <code>scripts/bibliometrics/output/</code>:</p>
  <ul>
    <li><code>reading_list.json</code> / <code>.md</code> &mdash; Top 500 ranked papers</li>
    <li><code>ocar_entries.json</code> &mdash; Top 200 with OCAR framework cards</li>
    <li><code>paper_rankings.json</code> &mdash; Full 2,000-paper ranking</li>
    <li><code>strategic_audit.md</code> &mdash; Human review flags</li>
    <li><code>high_indegree_omissions.json</code> &mdash; Structurally central papers outside top 500</li>
    <li><code>graphs/citation_graph.json</code> &mdash; Full citation network</li>
  </ul>
</section>

</div>
