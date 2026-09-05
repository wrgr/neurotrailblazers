# Module 12 Activity Worksheet

**Module:** Module 12: Big Data in Connectomics  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module12.md`, not this file.*

---

## Capability target

Produce a scalable, reproducible query-and-analysis plan for a large connectomics dataset, including storage assumptions, indexing strategy, and provenance capture. Concretely: size a dataset from its imaging parameters before anyone quotes you a price, choose a chunk and shard layout from your actual access pattern rather than from the format everyone else uses, predict which query will dominate your bill, and pin every published number to a segmentation version a stranger can re-query a year from now.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Basic SQL/Python dataframe proficiency
- [ ] Familiarity with EM volume structure
- [ ] Read the [data formats](/content-library/infrastructure/data-formats/) and [provenance and versioning](/content-library/infrastructure/provenance-and-versioning/) library pages.
- [ ] Bring one query you have actually run, with its runtime and its data source.
- [ ] Have a calculator or notebook open; the first exercise is arithmetic, not code.

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. How do we architect data systems for petascale connectomics?
   - Your answer:
2. Which indexing/query decisions drive analysis speed and reliability?
   - Your answer:
3. How do we preserve provenance at scale?
   - Your answer:

---

## The task

**Scenario:** Your team delivers a weekly motif-analysis report from a store holding a ~5 x 10^8-row synapse table, a 120,000-row segment table, and cell-type annotations for about 8,400 neurons. The volume is ~1 mm³, the bytes live in cloud object storage, and your analysis cluster is on-premises. The report is regenerated every Monday and will be cited in a manuscript. Last week's run took nine hours and produced numbers that do not match the report from three weeks ago; nobody knows why.

1. Propose a storage and index layout for the expected query patterns: chunk shape, sharding decision, and which products you mirror locally, with a byte estimate for each.
2. Outline the two queries that will dominate cost, estimate runtime from a sampled measurement, and name the operation you expect to be the bottleneck.
3. Define the minimum provenance fields for the weekly output and state what happens operationally when one is missing.
4. Diagnose the three-week discrepancy: list candidate causes in the order you would check them and the evidence that distinguishes them.
5. Produce one optimization proposal with an expected speedup and its cost, and one reproducibility safeguard someone else could execute without you.

### What you hand in

- Query architecture sketch with byte and object-count estimates
- Baseline vs optimized query plan with measured or sampled runtimes
- Provenance checklist with a stated failure action for each field
- A one-paragraph diagnosis of the version discrepancy naming the most likely cause first

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Write the analysis question as a sentence naming the table, the filter, and the unit of the answer — for example, "count synapses between layer 2/3 pyramidal cells and basket cells, per neuron pair, at cleft score above threshold."
- [ ] Estimate the working set: how many rows, how many objects, how many bytes must move, and whether that fits in memory on the machine you have.
- [ ] Choose storage and index strategy from the access pattern — chunk shape for volumetric reads, sharding if object counts exceed roughly 10^6, a pre-joined extract if the same join recurs.
- [ ] Pin the segmentation: record the materialization version or timestamp, and refuse to proceed if it is unknown.
- [ ] Prototype on a 0.1% sample, profile, and extrapolate the full runtime before running it once at full scale.
- [ ] Add provenance fields to the output artifact itself, not to the surrounding notebook.
- [ ] Validate reproducibility by having a second person re-run the query package from the recorded version and compare row counts and summary statistics.

---

## Evidence and reasoning

Fill one row per claim you make in your artifact. A claim without a limitation is
not finished.

| # | Claim | Evidence (what specifically) | Limitation / what would change my mind |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Confidence.** For your main claim, mark one and say why:

- [ ] **High** — two or more independent lines of evidence agree
- [ ] **Medium** — one strong line, or several that share a weakness
- [ ] **Uncertain** — the deciding evidence is not available to me

Why:

**One alternative I considered and rejected**, and the reason:

---

## Misconception self-check

These are the errors this module is designed to prevent. Confirm you did not make
them, or note where you nearly did:

- [ ] I did not assume: The format everyone else uses is automatically the right layout for your access pattern.
- [ ] I did not assume: Storage cost is the storage line on the invoice.
- [ ] I did not assume: The dataset size is the petabyte figure quoted for the raw imagery.
- [ ] I did not assume: An object ID refers to the same neuron next month.
- [ ] I did not assume: "it runs eventually" is acceptable for iterative science.
- [ ] I did not assume: Notebook history is sufficient provenance.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-08:00 | Architecture framing and failure examples |
| 08:00-20:00 | Access-pattern to index mapping exercise |
| 20:00-34:00 | Query profiling and bottleneck diagnosis |
| 34:00-46:00 | Provenance logging implementation |
| 46:00-56:00 | Team review of reproducibility gaps |
| 56:00-60:00 | Competency check and next-step assignment |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**
  - Query design matches analysis goal and data shape, with at least one quantitative estimate.
  - Provenance requirements are explicit, actionable, and attached to the artifact rather than the notebook.
  - Bottlenecks are identified with one realistic mitigation.
- **Strong performance**
  - Separates exploratory and production query paths and says which rules apply to each.
  - Quantifies tradeoffs across latency, dollar cost, and reproducibility, and names the assumption behind each number.
  - Identifies version drift as the first hypothesis for the discrepancy, before code bugs.
  - Anticipates failure recovery and rollback needs, including what happens when a materialization is superseded mid-analysis.
- **Common failure modes**
  - Index choices disconnected from query workload.
  - Missing version metadata in outputs.
  - Optimization attempts without a benchmark baseline.
  - Sizing that counts only the raw volume and ignores derived products and egress.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Document one query you use with:
1. data source/version,
2. expected runtime class,
3. one provenance field you currently miss.

**Your answer:**

---

## Peer review (swap worksheets)

Reviewing someone else's reasoning is the fastest way to see the gaps in your own.
Assess the **evidence quality**, not whether you agree with the conclusion.

- Is every claim paired with specific evidence?
- Is at least one limitation stated, and is it a real one?
- Is the confidence level justified by the number of *independent* evidence lines?
- One thing this person did better than me:
- One question I would ask them:

---

*Module page: `/modules/module12/` · Slides: `/modules/slides/module12/` · [Facilitator guide](/teaching/facilitator-guide/)*
