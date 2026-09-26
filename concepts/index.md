---
layout: page
title: "Concept Explorer"
permalink: /concepts/
slug: concept-explorer
track: career-and-community
pathways:
  - professional growth
  - hidden curriculum
summary: "Find content by concept and learner need rather than module number."
use_layout_hero: false
content_type: navigation
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Concept Explorer</h1>
      <p class="hero-subtitle">Find material by the skill you need, not by module number.</p>
    </div>
  </div>

  <section class="section">
    <p>Each card is one skill, such as framing a hypothesis, calling an axon versus a dendrite, or budgeting proofreading. It lists the unit that teaches it, the lab that practices it, and the slides for teaching it. Filter by track or by what you are trying to do. If you already know the module you want, the <a href="{{ '/modules/' | relative_url }}">module library</a> is faster.</p>
  </section>

  <section class="section">
    <h2>Filter Concepts</h2>
    <div class="cta-buttons">
      <button class="btn btn-secondary concept-filter-btn" data-track="all">All Tracks</button>
      {% for tr in site.data.track_catalog.tracks %}
      <button class="btn btn-secondary concept-filter-btn" data-track="{{ tr.slug }}">{{ tr.short_title }}</button>
      {% endfor %}
    </div>
    <div class="mt-1">
      <label for="need-filter"><strong>What you are trying to do:</strong></label>
      <select id="need-filter">
        <option value="all">All needs</option>
      </select>
    </div>
    <div class="mt-1">
      <h3>Start with these</h3>
      <ul id="recommended-list"></ul>
    </div>
  </section>

  {% assign all = site.data.concepts.concepts %}
  {% assign tracks = site.data.track_catalog.tracks %}

  {% for tr in tracks %}
  <section class="section">
    <h2>{{ tr.title }}</h2>
    <div class="cards-grid">
      {% for item in all %}
        {% if item.track == tr.slug %}
          {% assign primary = item.resources | first %}
          {% include cards/concept-card.html item=item primary_url=primary.url %}
        {% endif %}
      {% endfor %}
    </div>
  </section>
  {% endfor %}
</div>

<script>
  (function () {
    const cards = Array.from(document.querySelectorAll('.concept-card-item'));
    const trackButtons = Array.from(document.querySelectorAll('.concept-filter-btn'));
    const needSelect = document.getElementById('need-filter');
    const recommendedList = document.getElementById('recommended-list');
    if (!cards.length || !needSelect || !recommendedList) return;

    const needsSet = new Set();
    cards.forEach((card) => {
      const raw = (card.getAttribute('data-needs') || '').split('|').map((v) => v.trim()).filter(Boolean);
      raw.forEach((n) => needsSet.add(n));
    });

    Array.from(needsSet).sort().forEach((need) => {
      const opt = document.createElement('option');
      opt.value = need;
      opt.textContent = need;
      needSelect.appendChild(opt);
    });

    let currentTrack = 'all';
    let currentNeed = 'all';

    function applyFilters() {
      cards.forEach((card) => {
        const track = card.getAttribute('data-track');
        const needs = (card.getAttribute('data-needs') || '').split('|');
        const matchTrack = currentTrack === 'all' || track === currentTrack;
        const matchNeed = currentNeed === 'all' || needs.includes(currentNeed);
        card.style.display = (matchTrack && matchNeed) ? '' : 'none';
      });

      const visible = cards.filter((card) => card.style.display !== 'none');
      const seen = new Set();
      const picks = [];
      visible.forEach((card) => {
        const link = card.querySelector('.card-title a');
        if (!link) return;
        const key = `${link.getAttribute('href')}|${link.textContent.trim()}`;
        if (seen.has(key)) return;
        seen.add(key);
        picks.push({ href: link.getAttribute('href'), label: link.textContent.trim() });
      });

      recommendedList.innerHTML = '';
      if (!picks.length) {
        const li = document.createElement('li');
        li.textContent = 'No matches for this filter combination.';
        recommendedList.appendChild(li);
        return;
      }
      picks.slice(0, 5).forEach((item) => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = item.href;
        a.textContent = item.label;
        li.appendChild(a);
        recommendedList.appendChild(li);
      });
    }

    trackButtons.forEach((btn) => {
      btn.addEventListener('click', () => {
        currentTrack = btn.getAttribute('data-track') || 'all';
        applyFilters();
      });
    });

    needSelect.addEventListener('change', () => {
      currentNeed = needSelect.value || 'all';
      applyFilters();
    });

    const params = new URLSearchParams(window.location.search);
    const qTrack = (params.get('track') || 'all').toLowerCase();
    const qNeed = (params.get('need') || 'all').toLowerCase();
    const validTrack = trackButtons.some((b) => (b.getAttribute('data-track') || '').toLowerCase() === qTrack);
    const validNeed = qNeed === 'all' || Array.from(needSelect.options).some((o) => (o.value || '').toLowerCase() === qNeed);

    if (validTrack) currentTrack = qTrack;
    if (validNeed) {
      currentNeed = qNeed;
      needSelect.value = qNeed;
    }
    applyFilters();
  })();
</script>
