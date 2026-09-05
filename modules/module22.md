---
title: "Module 22: Scientific Writing and Presentation"
layout: module
permalink: /modules/module22/
description: "Deliver clear scientific talks and written summaries for technical and mixed audiences without oversimplifying connectomics evidence."
module_number: 22
image: /assets/images/modules/module22.svg
image_alt: "Stylized vector art: speech arcs widening from a speaker to connected listeners."
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Design a coherent scientific talk from connectomics evidence"
  - "Adapt explanation depth for expert and non-expert audiences"
  - "Handle audience questions without overclaiming"
  - "Make hidden presentation norms explicit for trainees"
prerequisites: "Modules 17-21"
merit_stage: "Dissemination"
compass_skills:
  - "Scientific Communication"
  - "Audience Adaptation"
  - "Presentation Practice"
ccr_focus:
  - "Skills - Presentation"
  - "Character - Intellectual Honesty"

# Normalized metadata
slug: "module22"
short_title: "Scientific Writing & Presentation"
status: "active"
audience:
  - "students"
pipeline_stage: "Dissemination"
merit_row_focus: "Dissemination"
topics:
  - "presentation"
  - "audience-adaptation"
  - "q-and-a"
summary: "Build and deliver defensible connectomics presentations with clear evidence, uncertainty, and audience-aware framing."
key_questions:
  - "How do we simplify without distorting?"
  - "Which uncertainties must be explicit in oral presentation?"
  - "What hidden expectations shape audience judgments?"
slides: []
notebook: []
datasets:
  - "/datasets/mouseconnects/"
  - "/datasets/workflow/"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/ask-an-expert/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic manuscript/figure familiarity"
  - "Experience presenting at least one technical result"
next_modules:
  - "module23"
references:
  - "Gopen and Swan (1990) - clarity principles for scientific prose."
  - "Technical Track Journal Club papers for evidence-backed slide narratives."
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Deliver a 10-minute connectomics talk with evidence-linked claims, explicit uncertainty, and audience-appropriate language, then respond to questions without overclaiming. Operationally: every slide carries one claim and names the dataset version behind it, you can write down in advance the two questions you are most likely to be asked, and you have a rehearsed answer to each that ends in a next test rather than a defense.

## Why this module matters
Many strong analyses fail to influence practice because communication is either too vague or too overloaded. The specific hazard in connectomics is that the data are visually spectacular and inferentially fragile at once. A rotating 3D reconstruction will hold a room; the same room will not notice that the connection counts behind it came from an unpinned segmentation that has since changed. Audiences reward the render and rarely audit the provenance, so the discipline has to come from you.

Presentation norms are also the clearest case of the hidden curriculum: strict, consequential, and almost never written down. Learners who grew up around working scientists absorbed by observation which minute may be spent on background, whether "I don't know" reads as failure or as calibration, and what a senior person's question is actually asking for. Learners who did not usually read their own confusion as lack of ability rather than lack of information. Stating the rules out loud costs one slide of session time.

## Concept set

### 1) Evidence-first narrative
- **Technical:** each major slide maps to one core claim and one evidence source: a named figure panel, a metric with an effect size, and the dataset version it came from. Build the claim tree before opening slide software. A claim with no evidence node is background and belongs in a sentence, not a slide.
- **Plain language:** do not ask the audience to infer your logic. A listener reconstructing why slide 5 follows slide 4 is not listening to slide 6.
- **Misconception guardrail:** a compelling narrative arc can carry a claim the evidence does not support.

### 2) Audience adaptation without distortion
- **Technical:** adapt vocabulary, analogy, and background depth; never the evidentiary standard. The invariant set is what was measured, on what data, at what version, and what the result does not establish. Write the caveat twice, for a specialist and a non-specialist, and check the two are logically identical rather than merely both present.
- **Plain language:** "neurons that fire together wire together" is a simplification that changes the claim; "we counted synapses between two cell types and found more than chance predicts" is one that does not.
- **Misconception guardrail:** caveats can be dropped for a general audience because they would not understand them anyway.

### 3) Q&A as scientific reasoning
- **Technical:** a response names the assumption the question targets, the limit of what you tested, and the observation that would resolve it. Classify before answering; most bad answers are correct answers to a different question type.
- **Plain language:** "I don't know" stops the conversation. "I don't know, and the check is to rerun this against the degree-preserving null on the proofread subset" continues it.
- **Misconception guardrail:** answering confidently is what makes an answer credible.

### 4) Connectomics-specific presentation challenges
Presenting connectomics research poses unique difficulties that require deliberate design choices. Explaining electron microscopy to non-expert audiences demands analogies and visual scaffolding: show the scale progression from brain region to neuropil to individual synapses. Visualizing inherently 3D data on 2D slides requires showing both the raw EM cross-section and the 3D reconstruction of the same structure side by side so viewers can connect what is imaged to what is reconstructed. Every microscopy image should include scale bars and arrows pointing to key features, since EM images are visually unfamiliar to most audiences.

Apply the "so what?" test to every slide: if a viewer cannot articulate why a particular image, graph, or diagram matters to the argument after 15 seconds, the slide needs revision. Pair morphological images with quantitative summaries rather than relying on visual impression alone. When showing network diagrams, indicate what nodes and edges represent, how many are shown versus exist in the full dataset, and what thresholds or filters produced the visualization.

### 5) The time budget is fixed, so the cut list is the design
- **Technical:** a 10-minute slot is about 8 minutes of speech plus a hard stop. Budget it before drafting (60s question and stake, 90s data and method, 4 min result, 60s limitation, 30s next step) and delete slides until rehearsal fits.
- **Plain language:** a talk that runs long is a scoping decision nobody made, not a pacing problem.
- **Misconception guardrail:** speaking faster is a legitimate way to fit more material into a fixed slot.

### 6) Uncertainty language is a graded scale
- **Technical:** use one ladder and say which rung you are on. Strongest to weakest: "we measured" (direct observation from the data as reconstructed); "consistent with" (alternatives remain); "suggests" (survived one null model, not a sensitivity analysis); "we cannot distinguish"; "we did not test". Keep the same rung in slide text, spoken claim, and prepared answer.
- **Plain language:** marking which findings are tentative is what makes the strong ones believable.
- **Misconception guardrail:** hedging weakens a talk and should be minimized.

### 7) Question types and their answer shapes
- **Technical:** *clarification* wants one sentence and no elaboration. *Methods challenge* wants the mechanism, whether you checked, and the result or the plan. *Alternative explanation* wants to know whether your null model already controls for it; if it does not, concede and name a test. *Scope* wants an explicit boundary, not optimistic extrapolation. *Positioning* ("have you seen our lab's work?") is usually a request for citation; thank them, ask for the reference, move on.
- **Plain language:** each kind of question has a different correct length of answer.
- **Misconception guardrail:** every question in Q&A is an attack that must be rebutted.

## Hidden curriculum scaffold
Give these to trainees in writing before the first practice talk.

- Unspoken norms in talks and conference Q&A:
  - The opening minute states question, why it matters, and what is new. A talk that opens with field history has spent its most valuable minute on material nobody needed.
  - Methods depth matches the expected critique audience. In a connectomics room, reconstruction and proofreading state is challenged first, so put it on a slide; in a general neuroscience room, one sentence plus a backup slide is correct.
  - "I don't know yet" is acceptable when paired with a concrete next step, and not acceptable as a way to end a conversation you would rather not have.
  - Answer to the level asked, then stop. Continuing past the answer reads as insecurity and costs the next questioner their turn.
  - The chair owns the clock. If they signal, stop mid-sentence and offer to continue offline.
- How to support trainees:
  - Provide model Q&A transcripts, strong and weak, for the same question. The contrast teaches faster than the rule.
  - Share the rubric before the practice talk. Revealed afterwards it is assessment; revealed beforehand it is instruction.
  - Rehearse the hardest question in private, as the MERIT stage-4 guidance in [Education Models]({{ '/models/' | relative_url }}) describes.

## Core workflow: technical talk preparation
1. Build the claim tree on paper: question at the root, two or three claims, one evidence item and one caveat under each, deleting any claim you cannot attach evidence to.
2. Write the time budget for your slot, then select the minimal slide set that preserves the inferential logic; every surviving slide must answer "which node of the claim tree is this?"
3. Draft the one-line provenance statement for the data slide: species and region, imaging modality and resolution, segmentation pipeline, proofreading or materialization version, and any exclusion criterion.
4. Rehearse against a timer with no audience and cut to the budget, then rehearse again with transitions spoken aloud, because the sentence carrying slide 4 into slide 5 is the one people improvise badly.
5. Run peer critique with one narrow brief: mark every sentence where the spoken claim is stronger than the slide's evidence.
6. Write the two most likely questions and a three-sentence answer to each, choosing the answer shape from the question-type taxonomy.
7. Revise with explicit uncertainty statements, checking the rung is identical in slide, speech, and prepared answer.

## Choosing the depth: talk-format decision table
The same result becomes six different talks. Choose the row before drafting, because the cut list follows from it.

| Format | Who is in the room | Methods depth to show | What you cut | What it costs you |
|---|---|---|---|---|
| Lab meeting, 30-60 min | People who know the dataset better than you | Everything, including QC plots and the analysis that failed | Nothing; the mess is the point here | One prep session, plus exposure to people who can actually check you |
| Departmental seminar, 45 min | Neuroscientists, mostly not connectomics | One slide on reconstruction and proofreading state | Parameter sweeps and alternative nulls, moved to backup | Several rehearsals and a real reframing, not a trim of the specialist version |
| Contributed talk, 10-12 min | Specialists who challenge the null model first | Null model and its constraints, on the result slide | All background beyond 90 seconds | Highest prep cost per delivered minute, against a hard stop |
| Poster pitch, 90 s | Whoever stops walking | Dataset name and version only | Everything except claim, evidence, limitation | Low prep, high repetition: dozens of deliveries that must each sound like the first |
| Public or outreach talk | Non-scientists | None; scale analogies instead of protocols | All numbers except one memorable anchor | Largest rewrite cost of any row; reuse from the research talk is near zero |

## 60-minute tutorial run-of-show
1. **00:00-08:00 | Framing and exemplar**
   - Instructor demonstrates one evidence-linked opening slide.
   - Show two versions of the same opener, one starting with field history and one with the question. Script line: "You have sixty seconds before the audience decides how hard to listen."
2. **08:00-18:00 | Claim tree workshop**
   - Learners draft question-claim-evidence-caveat map, capped at three claims.
   - Circulate asking one question only: "what is the evidence node under this claim, and which dataset version?"
3. **18:00-30:00 | Slide drafting sprint**
   - Build 4-slide mini-talk (problem, method, result, limitation).
   - Require the provenance line and a named uncertainty rung. Early finishers draft backup slides, not more main slides.
4. **30:00-42:00 | Peer critique round**
   - Review for clarity, caveat visibility, and claim discipline, under one narrow brief: mark every place the spoken claim outruns the slide's evidence.
5. **42:00-54:00 | Q&A simulation**
   - Each learner answers two critique questions.
   - Assign types so everyone gets one methods challenge and one alternative-explanation question. Name the type before judging the answer.
6. **54:00-60:00 | Debrief and competency check**
   - Submit revised claim language and one uncertainty statement, then name the question you most fear. That list is next session's material.

## Worked example: repairing an opener, then surviving the question
Maya has a reciprocity result from a cortical dataset and a 10-minute slot. Her first opener:

> "Connectomics is revolutionizing our understanding of the brain. Today I'll be talking about my work on network motifs in cortical circuits."

**Move 1, replace the field claim with a question.** It is about the field, not her work, it is unfalsifiable, and every other speaker will use it. In its place: "Do excitatory and inhibitory neurons in layer 2/3 connect back to each other more often than chance?"

**Move 2, add the stake.** A question without a stake makes the audience wonder why they should care. "Reciprocal excitatory-inhibitory pairs are the substrate most circuit models assume, and almost nobody has counted them at synapse resolution."

**Move 3, state the news.** "My work on network motifs" names a topic, not a finding, and the audience calibrates how hard to listen on whether there is news to hear. "We counted them, and we find about twice as many as a degree-preserving null model predicts."

**Move 4, pre-empt the first challenge inside the opener.** Anyone working on reconstruction will wonder whether false merges manufactured those pairs. Naming it first converts a challenge into evidence of competence: "The number moves with proofreading state, so I will show the enrichment on the proofread subset as well as the full volume."

The repaired opener runs about 35 seconds. The effect is still described as enrichment relative to a named null model, not as the circuit "preferring" reciprocity.

**Then the question.** A senior person asks: "Isn't your enrichment just a segmentation artifact? Merge errors create spurious reciprocal pairs."

*Defensive:* "The segmentation is state of the art and error rates are low." This asserts authority instead of evidence, names no mechanism, and invites a follow-up she cannot answer because she quoted no number.

*Capitulating:* "That's a really good point, it might well be an artifact." This abandons a result she has evidence for, and it teaches the room to discount everything else she said. Over-conceding is as much a calibration failure as overclaiming.

*The answer that works:* "It could be, and the mechanism is real: a merge between an excitatory and an inhibitory arbor manufactures reciprocity in exactly the direction I'm reporting. Two things make me think it isn't the whole story. The enrichment is present in the proofread subset, where those merges are corrected, though the interval is wider because n is smaller. And an artifact of that kind should also inflate reciprocity between cell-type pairs where I see none. What I have not done is a merge-injection simulation, adding merges at a known rate to measure how much reciprocity that buys. That is the test that would settle it, and it is next."

That answer classifies the question as a methods challenge, concedes the mechanism, offers two independent pieces of counter-evidence, states what was not done, and ends on a specific test. It runs about forty seconds, and it leaves her better off than silence: the room now knows she understands her own failure mode.

## Studio activity: mini-talk and critique loop
{: #studio-activity}
**Scenario:** You are presenting one connectomics result to mixed audience members (domain experts + trainees). Use your own result if you have one. Otherwise: in a cortical EM volume, layer 4 excitatory neurons form 3.2x more synapses onto PV+ interneurons than a degree-preserving null model predicts, from 847 connections at a specific materialization version, with roughly a third of the relevant arbors proofread. Two people in the room work on segmentation; one is a physiologist who has never opened an EM volume.

**Tasks**
1. Create a 4-slide mini-talk with a provenance line on the method slide and a named uncertainty rung on the result slide.
2. Deliver it in 3 minutes against a timer you can see.
3. Answer two audience questions, naming the question type aloud before answering each.
4. Revise one slide and one spoken claim from the feedback, recording what changed and why.

**Expected outputs**
- 4-slide deck.
- Speaker notes with claim boundaries.
- Revision log after Q&A.
- Two prepared answers, each ending in a next test.

## Assessment rubric
- **Minimum pass:** claims are evidence-linked and caveats visible; language is audience-appropriate without technical distortion; Q&A responses include limits and follow-up tests; the deck names dataset and version.
- **Strong performance:** anticipates likely critiques and addresses them proactively; balances accessibility with methodological precision; concedes the valid part of a challenge while defending the rest; keeps the same uncertainty rung in slide, speech, and answer.
- **Common failure to flag:** overcompressed methods leading to overclaiming, jargon-heavy explanation with missing context, and defensive Q&A that asserts authority instead of citing evidence. Flag over-conceding too: abandoning a supported result under mild challenge is a calibration failure, not modesty.

## Common errors and how to recover
- **Out of time on slide 6 of 12.** Do not accelerate. Say "I'll skip to the result and the limitation," jump there, and deliver both fully. A complete argument on two slides is remembered; an incomplete one on six is not. Fix it at rehearsal next time by cutting to the budget.
- **You made a claim on stage stronger than your data.** Correct it in the same session, out loud: "Earlier I said X causes Y; what I can support is that they co-occur more than the null predicts." A voluntary correction reads as calibration; one extracted from you in Q&A does not.
- **You do not know the answer.** Use the three-part form: what you know, what you did not test, what would settle it. Then stop. Filling the silence turns an acceptable answer into a bad one.
- **A questioner will not yield the floor.** Say "I'd rather work through this properly than badly in thirty seconds; can we continue after the session?" and look at the chair. If the chair misses the cue, you have still done the correct thing.

## What this module does not cover
- **Writing the paper.** Manuscript structure, written methods provenance, and reviewer responses are [Module 17]({{ '/modules/module17/' | relative_url }}).
- **Figure design itself.** Colormaps, axis conventions, and accessible visual encodings are [Module 18]({{ '/modules/module18/' | relative_url }}); here your figures already exist and the only question is what claim each carries.
- **Posters, abstracts, and conference navigation.** Those are [Module 23]({{ '/modules/module23/' | relative_url }}).
- **The statistics behind the claims.** Null-model choice, multiplicity, and the exploratory-confirmatory split are [Module 20]({{ '/modules/module20/' | relative_url }}). This module assumes the analysis is already defensible.
- **Authorship and who gets to give the talk.** See [Module 19]({{ '/modules/module19/' | relative_url }}). Terms used here without definition are in the [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }}).

## Content library references
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) — What to cite in methods sections, and what belongs on your one provenance line

## Teaching resources
- Public-engagement companion: [Module 22 companion for public audiences]({{ '/teaching/module22-public-engagement/' | relative_url }}) — the evidence-badge exercise and outreach framing for running this material outside a research audience
- Technical context: [Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- Evidence set: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Vocabulary support: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Coaching support: [Ask-an-Expert]({{ '/tools/ask-an-expert/' | relative_url }})
- Differentiation guidance: [Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }})

## Quick practice prompt
Write your 60-second talk opener with the core question, one evidence-backed finding, one explicit caveat, and one sentence pre-empting the challenge you most expect. Read it aloud against a timer; if it runs past 60 seconds, cut the background sentence first.
