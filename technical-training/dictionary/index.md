---
layout: page
title: "Connectomics Dictionary"
permalink: /technical-training/dictionary/
slug: connectomics-dictionary
---

## Purpose
A shared vocabulary for learners, mentors, and journal clubs in the technical connectomics track.

<div class="cards-grid">
  {% assign terms = site.data.connectomics_dictionary.terms | sort: 'term' %}
  {% for item in terms %}
  <article class="card">
    <h3 class="card-title">{{ item.term }}</h3>
    <p><small><strong>Category:</strong> {{ item.category }}</small></p>
    <p class="card-description">{{ item.definition }}</p>
  </article>
  {% endfor %}
</div>
