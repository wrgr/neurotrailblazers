---
layout: page
title: "Modes of Use"
description: "The same material, three situations: working alone, running a hosted session, or inside a research programme."
permalink: /modes/
slug: modes
content_type: navigation
track: career-and-community
pathways:
  - program design
  - professional growth
---

## Why there is a mode axis at all

The tracks answer *what* you are learning. They do not answer *how you are using
it*, and that turns out to change almost everything about what the material needs
to be.

A person working alone at midnight needs the answer to a self-check to be
available and needs to be told not to open it yet. A facilitator standing in front
of eleven people needs a run of show, a rubric visible before the activity starts,
and a list of misconceptions to fish for in the debrief. A trainee inside a lab
needs neither: they need work whose output somebody downstream actually uses, and
a reviewer who will tell them it is not good enough.

Those are three different products built from one body of material. Treating them
as one surface is why sites like this one usually end up serving none of them
well: the units read as both self-study and lecture notes, and the facilitator
material sits orphaned from the content it supports.

Mode is **independent of track**. Any [track]({{ '/tracks/' | relative_url }}) can
be worked in any available mode, and each track page states what it looks like in
each.

{% include ui/mode-picker.html %}

{% for m in site.data.modes.modes %}{% include ui/mode-panel.html mode=m %}{% endfor %}

## Choosing

If you are unsure, you are almost certainly in **self-study**, and the question
that matters more is which track. Pick that on the [tracks page]({{ '/tracks/' | relative_url }}),
or ignore the tracks and follow a question through [the core]({{ '/core/' | relative_url }}).
