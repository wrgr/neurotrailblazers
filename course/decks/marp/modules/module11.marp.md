---
marp: true
theme: default
paginate: true
title: "Module 11: Synapses and Circuit Logic"
---

# Module 11: Synapses and Circuit Logic
Teaching Deck

---

## Learning Objectives
- Identify synaptic patterns relevant to circuit hypotheses
- Relate synapse-level observations to local motif logic
- Differentiate robust motifs from annotation artifacts
- Communicate circuit-level claims with explicit limits

---

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Agenda (60 min)
- 0-10 min: Frame and model
- 10-35 min: Guided practice
- 35-50 min: Debrief and misconception correction
- 50-60 min: Competency check + exit ticket

---

## Capability Target
Generate one synapse-to-motif interpretation with explicit evidence chain and one alternative explanation.

---

## Concept Focus
### 1) Synaptic organization as circuit logic
Synapses are not randomly placed. Their location on the postsynaptic neuron (soma, proximal dendrite, distal dendrite, spine, axon initial segment) determines their functional impact:
- **Perisomatic synapses** (on soma and proximal dendrites): typically inhibitory (basket cells), powerful because they're close to the spike initiation zone. These synapses can veto spiking.
- **Dendritic spine synapses**: typically excitatory, the workhorses of cortical computation. Each spine receives one (usually) excitatory synapse. Spine size correlates with synapse strength — larger mushroom spines have larger PSDs and more AMPA receptors.
- **AIS synapses**: exclusively from chandelier cells. The only inhibitory input at the axon initial segment, positioned to control spike generation directly.
- **Shaft synapses on smooth dendrites**: typically inhibitory-to-inhibitory connections (disinhibition circuits) or excitatory inputs onto aspiny interneurons.

---

## Core Workflow
- Identify synapse candidates: find synapses in the region of interest with correct pre/post assignment.
- Build local connectivity motif: extract the subgraph connecting the pre and post neurons and their immediate neighbors.
- Classify the motif: reciprocal pair, feed-forward loop, feedback inhibition, convergent input, etc.
- Evaluate against null: is this motif more common than expected?
- State supported claim (what the data shows) + caveat (what it doesn't prove and what could confound it).

---

## 60-Minute Run-of-Show
- Review the synapse classification content library entry (Gray Type I/II)
- Review the motif analysis content library entry (key motif types section)
- **00:00-10:00 | Synapse cue recap**
- Quick review: asymmetric (Type I, excitatory) vs symmetric (Type II, inhibitory) synapses.
- Show 3 synapses in EM: spine synapse, perisomatic synapse, AIS synapse. "Where the synapse lands tells you about circuit function."
- **10:00-24:00 | Motif construction examples**
- Walk through 3 motifs in the MICrONS dataset:
- Reciprocal pair between two L2/3 pyramidal cells (mutual excitation)
- Feed-forward loop: L4 stellate → L2/3 pyramidal → L5 pyramidal, with L4 also connecting directly to L5
- Feedback inhibition: pyramidal → basket cell → same pyramidal
- For each: show the EM evidence (synapses), draw the circuit diagram, discuss functional implication.
- **24:00-38:00 | Learner motif analysis**
- Learners receive a small subgraph (15 neurons, 50 synapses) and identify all 3-node motifs.
- Count each motif type. Which are most common?
- Compare to expectations: "If these were randomly connected with the same degree distribution, how many of each motif would you expect?"
- **38:00-50:00 | Alternative explanation challenge**
- For each enriched motif, learners must propose one alternative (non-functional) explanation:
- "Reciprocal connections are enriched because nearby neurons are more likely to connect" (spatial proximity)
- "Feed-forward loops are enriched because of cell-type structure" (E→I and I→E are common)
- Group discussion: how would you test whether the spatial explanation is sufficient?
- **50:00-60:00 | Competency check**
- Each learner writes a motif claim/caveat pair:
- "In this circuit, [motif] is enriched [X]× compared to [null model]. This is consistent with [functional interpretation]. However, [alternative explanation] could also account for this enrichment."
- Exit ticket: "One motif claim and one plausible confound."

---

## Misconceptions to Watch
- **Misconception guardrail:** asymmetric morphology means a synapse is excitatory, rather than putatively excitatory under a stated assumption.
- **Misconception guardrail:** reconstruction errors add symmetric noise to motif counts, when merges bias them toward denser motifs.
- **Misconception guardrail:** a motif observed more often than expected is a functional building block.
- **Misconception guardrail:** synapse count is a direct measure of connection strength rather than a proxy for it.

---

## Studio Activity
{: #studio-activity}

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass**
- The motif count table reports observed, expected, and z-score for every motif class examined, not only the enriched ones.
- At least one motif carries a complete evidence chain: detection method, count, null comparison, and interpretation, in that order.
- Each claim in the circuit logic brief is paired with an explicit caveat stating what it does not prove.
- The synapse threshold and data version used to build the subgraph are stated in the brief.
- **Strong performance**
- Every enriched motif has at least one non-functional alternative explanation (spatial proximity, cell-type composition, reconstruction error) named and, where possible, tested.
- A second null model or a stratified analysis is applied to at least one motif, with the change in effect size reported.
- Synapse-level evidence — compartment targeting, Gray type — is used to subdivide or qualify at least one motif class rather than treating graph edges as interchangeable.
- Sensitivity to reconstruction quality is quantified: the headline count is re-run at a second synapse threshold or across proofreading versions, and the difference is reported.
- **Common failure to flag**
- Motif claim without error-awareness — treating every enriched pattern as a functional circuit without considering artifacts or spatial confounds.
- Functional language ("this circuit gates," "this loop amplifies") presented as a finding rather than as a consistency statement.
- Enrichment reported against a single weak null with no statement of what it fails to control.

---

## Exit Ticket
Write one motif claim and one plausible confound.

---

## References (Instructor)
- Use module references listed on the module page.

---

## Teaching Materials
- Module page: /modules/module11/
- Slide page: /modules/slides/module11/
- Worksheet: /assets/worksheets/module11/module11-activity.md
