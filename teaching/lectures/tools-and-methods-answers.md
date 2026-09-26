---
layout: page
title: "Tools and Methods: instructor model responses"
permalink: /teaching/lectures/tools-and-methods-answers/
slug: tools-and-methods-answers
content_type: delivery
description: "Worked snapshot queries, a provenance record and a raw-capacity estimate."
---

[Learner worksheet]({{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }})
· [Lecture plan]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}#teach-a-90-minute-session)

These responses use **synthetic** data. This is a public, formative answer key.

## 1. Query results

**Snapshot A:** s1 and s2, **2 rows**. Exclude s3 for score, s4 for region and s5
for postsynaptic identity. **Snapshot B:** s1, s2, s3 and s6, **4 rows**. Exclude
s4 and s5. The change consists of a score revision for s3 and a newly listed row s6.

With a strict `score > 0.80` rule, s2 is excluded and the counts become **1 and 3**.
An undocumented boundary convention can therefore change both results without
any dataset revision. The fixture has no evidence of tissue change: new or revised
annotations do not establish biological growth.

## 2. Model methods record

“For the synthetic teaching dataset in the archived query source, I selected
`snapshot-a`, postsynaptic label 101, region label `core`, and score ≥ 0.80.
The endpoint was the number of qualifying rows, not distinct presynaptic partners
or physiological strength. The selected IDs were s1 and s2, giving n = 2 from five
input rows; three rows were excluded for the reasons recorded above.”

Append the **actual execution date**, exact command, saved output, Python version
and source SHA-256 emitted by the program. Archive the source itself; a hash alone
cannot recover a missing file. On the paper route, record the worksheet revision,
manual filtering procedure and peer re-run instead of claiming a code execution.
Do not copy a fabricated hash or environment from an exemplar.

For a real query, additionally record the datastack/table and schema, materialization
version and timestamp, segmentation state, version-appropriate object IDs, region
definition and coordinate units/frame, client/dependency versions, and restrictions
on access or redistribution. This fixture has region labels only and no coordinates
or segmentation graph; those fields are **not applicable**, not silently inferred.
No stochastic operation occurs here, so a seed is not applicable either.

If a prior version is missing, inspect archived outputs, notebook history, manifests
and query logs. A count alone does not uniquely identify its source version. If the
provenance cannot be established, label that result unreproduced and rerun a documented
analysis. Do not declare either count correct merely because both are plausible.

The [CAVEclient materialization guide](https://www.caveconnecto.me/CAVEclient/tutorials/materialization/)
describes versioned queries; the [MICrONS versioning tutorial](https://tutorial.microns-explorer.org/materialization-version.html)
shows the association between versions and timestamps. The toy snapshot labels are
not identifiers from either service.

## 3. Capacity and transfer

- Convert the volume to **100,000 × 100,000 × 40,000 nm**.
- Divide by voxel size: **10,000 × 10,000 × 1,000 voxels**.
- Product: **100,000,000,000 voxels**. At one byte per voxel: **100 GB** raw.
- Three total copies require **300 GB** before overhead.
- One ideal transfer: 100 × 10⁹ / (100 × 10⁶) = **1,000 seconds**, about
  **16.7 minutes**. This is not an acquisition-time estimate or a transfer guarantee.

Omissions include segmentation labels, image pyramids, chunk padding, metadata,
intermediate processing arrays, backups beyond the three copies, and retry/protocol
overhead. Compression can change storage and throughput; its ratio was not supplied.
Neither hardware price nor staff time can be inferred from this byte estimate.
Accept binary units only if explicitly labeled and converted correctly.

## Feedback guide

Score four dimensions **0–2 each**: exact filtering/counts, recoverable provenance,
capacity arithmetic/units, and interpretation/limitations. Two means explicit and
correct, one means a recoverable omission, and zero means absent or contradictory.
A proficient response has at least 6/8 and no zero in provenance or interpretation.
This is a local teaching rubric, not a validated assessment instrument.

Common feedback: “Which snapshot?” for a missing version; “Is 0.80 included?” for
an ambiguous threshold; “Where are the archived inputs?” for a hash without files;
and “What changed in the evidence?” for an unsupported biological explanation.

Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
