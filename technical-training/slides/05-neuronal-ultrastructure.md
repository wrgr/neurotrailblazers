---
layout: page
title: "Lecture Plan: Neuronal Ultrastructure"
permalink: /technical-training/slides/05-neuronal-ultrastructure/
slug: slides-05-neuronal-ultrastructure
content_type: delivery
---

## What this document is

This page is a **build plan for an instructor assembling a lecture** on this unit. It gives the
slide sequence, per-slide timing, the points at which figures belong, and the speaker notes that
carry the argument. It is a design document, not a rendered deck: there are no slides on this
page to project, and nothing here is written to be shown to learners as it stands.

A separately maintained Marp deck for this unit does exist, and it is linked at the foot of this
page under *Rendered deck artifacts*. That deck was authored in its own right and does not follow
this plan slide for slide, so treat this page as the teaching design and the Marp file as one
existing implementation of it. The learner-facing material is the unit page linked under
*Connections*.

## Session profile
- Audience: annotators, proofreaders, and analysts needing ultrastructure fluency.
- Duration: 75 minutes lecture + 20 minutes image annotation drill.
- Output: labeled cue sheet with confidence scores and ambiguity notes.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and practical stakes
2. Slide 2 (5 min): Ultrastructure as operational language
3. Slide 3 (6 min): Compartment refresher
   - Soma, dendrite, axon, boutons, spines.
4. Slide 4 (6 min): Synapse architecture essentials
   - Vesicles, active zone, PSD, cleft context.
5. Slide 5 (6 min): Organelle cues
   - Mitochondria, ER, microtubules in context.
6. Slide 6 (6 min): Multi-slice evidence protocol
7. Slide 7 (7 min): Worked example I
   - Easy compartment call with converging evidence.
8. Slide 8 (7 min): Worked example II
   - Ambiguous case and confidence annotation.
9. Slide 9 (6 min): Annotation disagreement analysis
10. Slide 10 (5 min): Frequent error modes
11. Slide 11 (5 min): QC metrics for ultrastructure calls
12. Slide 12 (5 min): Standardized decision log template
13. Slide 13 (7 min): Hands-on labeling prompt
14. Slide 14 (7 min): Debrief and bridge to process classification.

## Sixty-minute tutorial: run-of-show

### Pre-class (10–15 min, async)

- Read §1 and §2 of the unit page. Bring the organelle table.
- Open the unit page figure panel and preview at least three figures.
- Bring one cue you find ambiguous.

### Materials

- [Neuronal Ultrastructure lecture plan]({{ '/technical-training/slides/05-neuronal-ultrastructure/' | relative_url }})
- The figure panel above (RIV-ULTRA shortlist)
- A shared annotation sheet with columns: patch ID | compartment call | synapse call |
  confidence tier | cue family 1 | cue family 2 | what would change my mind

The last column is the one that produces learning. Insist on it.

### Minute by minute

| Time | Activity | Instructor focus |
|---|---|---|
| 00:00–05:00 | **Framing.** Prompt: "What goes wrong if we force a label too early?" | Set the capability target; state that "uncertain" is a passing answer |
| 05:00–12:00 | **Expert modeling.** Work one patch aloud, following the §3 protocol | Think aloud about *uncertainty*, not just conclusions. Name each cue's family explicitly |
| 12:00–20:00 | **Guided practice 1.** Two easy patches, in pairs | Circulate; ask "which family is that cue from?" rather than "is that right?" |
| 20:00–30:00 | **Public debrief.** Compare calls openly | Target the three misconceptions below |
| 30:00–42:00 | **Guided practice 2.** Two borderline patches, independently | Require two independent cues plus one uncertainty statement per patch |
| 42:00–52:00 | **Consensus round.** Groups reconcile using the tier definitions | Classify each disagreement: cue conflict / missing context / vocabulary mismatch |
| 52:00–58:00 | **Competency check.** One fully justified call each | Label + confidence + evidence chain + one alternative considered and rejected |
| 58:00–60:00 | **Exit ticket.** "One cue I trust more now; one I still mistrust" | Collect these — they are your calibration data for next session |

### The three misconceptions to target explicitly

1. **"Small process = axon."** Size alone is unreliable; thin dendritic branches and
   spine necks are small too. Counter with a ribosome-bearing thin process.
2. **"Dark contrast = synapse."** Counter with a tangentially sectioned membrane and
   with an adherens junction.
3. **"Every patch must end in a hard label."** Counter by praising a well-justified
   "uncertain" in the public debrief. Learners calibrate to what gets rewarded, so
   reward it visibly, once, early.

### Formative checkpoints

- **At 20 min:** ≥ 80% of pairs cite two cues from *different families*. If not, stop
  and re-teach §4 — proceeding without this makes the rest of the session unproductive.
- **At 42 min:** the disagreement log distinguishes cue conflict from missing context.
- **At 58 min:** each learner justifies one call with explicit uncertainty language.

### Post-class (20–30 min)

Annotate three new patches; submit call, confidence, cue rationale by family, and one
unresolved ambiguity with an escalation note.

## Figure integration points
- Primary shortlist: `course/units/figures/05-neuronal-ultrastructure-selected-v1.md`.
- Use at least three cue-comparison panels and one ambiguity panel.

## Speaker notes (expert-level)
- Require cue triangulation (morphology + organelle + context) before hard labels.
- Keep uncertain labels explicit; uncertainty is signal, not failure.

## Assessment and artifacts
- Deliverable: cue-based annotation sheet with confidence tiers.
- Rubric dimensions: evidence quality, consistency, and uncertainty handling.

## Connections
- Unit page: [Neuronal Ultrastructure]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module04]({{ '/modules/module04/' | relative_url }}), [module09]({{ '/modules/module09/' | relative_url }}), [module11]({{ '/modules/module11/' | relative_url }})

## Rendered deck artifacts
<div class="resource-card">
  <p>These are the separately maintained Marp deck artifacts for this unit. They are not generated from the plan above, so their sequence and timing differ from it.</p>
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/' | append: page.slug | remove: 'slides-' | append: '.html' | relative_url }}">Open HTML Deck</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/{{ page.slug | remove: 'slides-' }}.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/technical-training/' | append: page.slug | remove: 'slides-' | append: '/' | relative_url }}">Open Unit Page</a>
  </div>
  <p><small>The HTML deck presents directly in a browser. The Markdown source is the one to
  take if you want to adapt it &mdash; it renders with <a href="https://marp.app/">Marp</a>.
  For PowerPoint, run <code>./scripts/render_marp.sh --pptx</code>; the exports are not
  committed because 35 of them came to 88&nbsp;MB.</small></p>
  <p><strong>Batch render helper:</strong> <code>./scripts/render_marp.sh</code></p>
</div>