---
layout: page
title: "Connectomics Dictionary"
description: "A working glossary of connectomics terms with definitions, typical values, why each term matters in practice, and the confusions it commonly causes."
permalink: /technical-training/dictionary/
slug: connectomics-dictionary
track: core-concepts-methods
pathways:
  - technical foundation
  - shared vocabulary
use_layout_hero: false
content_type: core
---

<div class="main-content">

<section class="section">
<h1>Connectomics Dictionary</h1>
<p>A shared vocabulary for learners, mentors, and journal clubs in the technical
connectomics track. Entries carry more than a definition: where a term has a
characteristic magnitude, a <strong>typical value</strong>; where it drives a practical
decision, <strong>why it matters</strong>; and where it is routinely confused with
something else, <strong>the confusion</strong>.</p>
</section>

<section class="section">
<h2>How to use this dictionary</h2>
<ul>
  <li><strong>Before a unit:</strong> pick the unit number in the filter below and review the terms tagged with it.</li>
  <li><strong>During annotation or journal club:</strong> require every definition to be tied to a concrete example from the data in front of you. A term someone can define but not point at has not been learned.</li>
  <li><strong>Treat the "why it matters" line as the real content.</strong> Terms such as <em>null model</em>, <em>materialization</em>, <em>proofreading level</em>, and <em>merge error</em> are operational requirements. Each one implies something you must do or report.</li>
  <li><strong>Self-test:</strong> cover the definition and try to produce it from the term, then check. Recognition is much easier than recall, and only recall transfers to practice.</li>
</ul>
</section>

<section class="section">
<h2>Starter sets by unit</h2>
<ul class="list-tight">
  <li><strong>Units 01–02:</strong> connectome, completeness, anisotropy, voxel, Peters' rule, null model, Bin A/B/C claim, non-claim</li>
  <li><strong>Units 03–04:</strong> rOTO, fold, lost section, contrast-to-noise ratio, supervoxel, ChunkedGraph, root ID, materialization, provenance</li>
  <li><strong>Units 05–07:</strong> ultrastructure, postsynaptic density, synaptic vesicle, Gray type I/II, polyribosome, glycogen granule, axon initial segment, cue family, confidence tier</li>
  <li><strong>Units 08–09:</strong> merge error, split error, Variation of Information, Expected Run Length, proofreading level, stopping rule, endpoint metric, configuration model, triad census, synapse threshold</li>
</ul>
</section>

<section class="section">
  <h2>Browse all terms</h2>
  <p>
    <input type="search" id="dict-search" placeholder="Search terms and definitions…"
           aria-label="Search dictionary"
           style="width:100%;max-width:32rem;padding:.6rem .8rem;border:1px solid #d1d5db;border-radius:8px;font-size:1rem;">
  </p>
  <p id="dict-filters" style="margin-top:.5rem;">
    <button type="button" class="tech-tag dict-cat is-active" data-cat="all" style="cursor:pointer;border:none;">All</button>
    {% assign cats = site.data.connectomics_dictionary.terms | map: 'category' | uniq | sort %}
    {% for c in cats %}
    <button type="button" class="tech-tag dict-cat" data-cat="{{ c | escape }}" style="cursor:pointer;border:none;">{{ c }}</button>
    {% endfor %}
  </p>
  <p id="dict-unit-filters" style="margin-top:.25rem;" aria-label="Filter by unit">
    <small><strong>Unit:</strong></small>
    <button type="button" class="tech-tag dict-cat is-active" data-unit="all" style="cursor:pointer;border:none;">All units</button>
    {% assign dict_units = site.data.connectomics_dictionary.terms | map: 'units' | join: ',' | split: ',' | uniq | sort %}
    {% for u in dict_units %}
    <button type="button" class="tech-tag dict-cat" data-unit="{{ u }}" style="cursor:pointer;border:none;">{{ u }}</button>
    {% endfor %}
  </p>
  <p><small id="dict-count"></small></p>

  <div class="cards-grid" id="dict-list">
    {% assign terms = site.data.connectomics_dictionary.terms | sort: 'term' %}
    {% for item in terms %}
    <article class="card dict-entry"
             data-cat="{{ item.category | escape }}"
             data-units=" {{ item.units | join: ' ' }} "
             data-text="{{ item.term | downcase | escape }} {{ item.definition | downcase | escape }} {{ item.typical | downcase | escape }} {{ item.matters | downcase | escape }} {{ item.confuse | downcase | escape }}">
      <h3 class="card-title">{{ item.term }}</h3>
      <p><small><strong>{{ item.category }}</strong>{% if item.units %} &middot; Units {{ item.units | join: ', ' }}{% endif %}</small></p>
      <p class="card-description">{{ item.definition }}</p>
      {% if item.typical %}<p><small><strong>Typical:</strong> {{ item.typical }}</small></p>{% endif %}
      {% if item.matters %}<p><small><strong>Why it matters:</strong> {{ item.matters }}</small></p>{% endif %}
      {% if item.confuse %}<p><small><strong>Often confused with:</strong> {{ item.confuse }}</small></p>{% endif %}
    </article>
    {% endfor %}
  </div>
</section>

<section class="section">
  <h2>Contributing a term</h2>
  <p>Terms live in <code>_data/connectomics_dictionary.yml</code>. A complete entry has:</p>
  <ul class="list-tight">
    <li><code>term</code>, <code>category</code>, <code>definition</code> — required</li>
    <li><code>typical</code> — a representative value or range, where the term has one</li>
    <li><code>matters</code> — the practical consequence: what you must do, report, or avoid because of this term</li>
    <li><code>confuse</code> — the term or concept it is routinely mistaken for</li>
    <li><code>units</code> — the technical-training units where it is used</li>
  </ul>
  <p>The <code>matters</code> field is the one worth the effort. A glossary of definitions
  is a lookup table; a glossary of consequences is a checklist. If a term genuinely has no
  characteristic magnitude, leave out <code>typical</code> and add the term, with the reason,
  to the <code>NO_TYPICAL</code> list in <code>scripts/validate_dictionary.rb</code>.</p>
</section>

</div>

<script>
(function () {
  var search = document.getElementById('dict-search');
  var list = document.getElementById('dict-list');
  if (!search || !list) return;
  var entries = Array.prototype.slice.call(list.querySelectorAll('.dict-entry'));
  var buttons = Array.prototype.slice.call(document.querySelectorAll('.dict-cat[data-cat]'));
  var unitButtons = Array.prototype.slice.call(document.querySelectorAll('.dict-cat[data-unit]'));
  var counter = document.getElementById('dict-count');
  var activeCat = 'all';
  var activeUnit = 'all';

  function apply() {
    var q = search.value.trim().toLowerCase();
    var shown = 0;
    entries.forEach(function (el) {
      var catOk = activeCat === 'all' || el.getAttribute('data-cat') === activeCat;
      var unitOk = activeUnit === 'all' || el.getAttribute('data-units').indexOf(' ' + activeUnit + ' ') !== -1;
      var textOk = q === '' || el.getAttribute('data-text').indexOf(q) !== -1;
      var visible = catOk && unitOk && textOk;
      el.style.display = visible ? '' : 'none';
      if (visible) shown++;
    });
    counter.textContent = shown + ' of ' + entries.length + ' terms shown';
  }

  search.addEventListener('input', apply);
  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      activeCat = b.getAttribute('data-cat');
      buttons.forEach(function (x) { x.classList.remove('is-active'); });
      b.classList.add('is-active');
      apply();
    });
  });
  unitButtons.forEach(function (b) {
    b.addEventListener('click', function () {
      activeUnit = b.getAttribute('data-unit');
      unitButtons.forEach(function (x) { x.classList.remove('is-active'); });
      b.classList.add('is-active');
      apply();
    });
  });
  apply();
})();
</script>
