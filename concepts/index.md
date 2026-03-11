---
layout: page
title: "Concept Explorer"
permalink: /concepts/
slug: concept-explorer
summary: "Find content by concept and learner need rather than module number."
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Concept Explorer</h1>
      <p class="hero-subtitle">Explore NeuroTrailblazers by concept, not module numbers.</p>
    </div>
  </div>

  <section class="section">
    <p>Use this page to navigate by what you need right now: a method, a workflow challenge, or professional-development support. Modules remain available as delivery objects, but discovery is concept-first.</p>
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
      <label for="need-filter"><strong>User need:</strong></label>
      <select id="need-filter">
        <option value="all">All needs</option>
      </select>
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
    if (!cards.length || !needSelect) return;

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
  })();
</script>
