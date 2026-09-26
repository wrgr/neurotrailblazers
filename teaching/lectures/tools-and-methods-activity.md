---
layout: page
title: "Tools and Methods: learner worksheet"
permalink: /teaching/lectures/tools-and-methods-activity/
slug: tools-and-methods-activity
content_type: delivery
description: "An offline exercise in query provenance, changing snapshots and storage estimation."
---

[Lecture plan and slides]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}#teach-a-90-minute-session)
· [Four-session block]({{ '/teaching/sequence/' | relative_url }})

**35 minutes plus peer review.** Work in pairs. Every value and identifier here is
**invented teaching data**, not MICrONS, H01 or a real materialization version.
The paper route requires only a calculator. The optional code route needs Python 3,
with no additional packages, network access or credentials.

## 1. Reproduce a count (15 minutes)

Count rows with **post = 101**, **region = core**, and **score ≥ 0.80**. Treat the
score as a toy filter, not a calibrated probability. Each ID appears once per snapshot.

Snapshot A contains these five rows, written as `(id, post, region, score)`:

```text
(s1, 101, core,    0.95)
(s2, 101, core,    0.80)
(s3, 101, core,    0.60)
(s4, 101, outside, 0.99)
(s5, 102, core,    0.90)
```

Snapshot B retains all five IDs, changes s3's score to **0.90**, and adds
`(s6, 101, core, 0.85)`. For this exercise the target and region labels have the
same meaning in both snapshots. Real reconstruction IDs require version-aware checking.

List the included IDs and excluded rows for each snapshot. Explain each difference.
Would changing `≥` to `>` affect the result? Can the change establish biological growth?

**Optional runnable route:** save [the teaching query]({{ '/assets/worksheets/lectures/tools-and-methods-query.py' | relative_url }})
as `tools-and-methods-query.py` in a working folder, then run:

```bash
python3 tools-and-methods-query.py --version snapshot-a
python3 tools-and-methods-query.py --version snapshot-b
```

The program embeds the exact rows printed above and reports the filters, IDs,
counts, Python version and a SHA-256 hash of its source. It refuses an unspecified
version or `latest`. Save each output with the exact command and execution date.
This is an offline teaching fixture, not a public-volume query or a CAVE client.

## 2. Repair the methods record (10 minutes)

A colleague's methods say: “We downloaded the latest synapses for cell 101 and
counted the high-confidence inputs.” Rewrite this as a reproducible record for
Snapshot A. Include dataset/snapshot, object and region scope, exact filter, query
code identity, execution environment/date, returned IDs and one limitation.

For a real dataset, what would you additionally record about segmentation state,
coordinate units/frame, table schema and access? What could you check if an earlier
run's version was missing? Distinguish evidence you can recover from what you would
have to label unknown.

## 3. Estimate capacity (10 minutes)

For a separate hypothetical acquisition, assume a **100 × 100 × 40 µm** volume,
**10 × 10 × 40 nm** voxels, one channel, **8-bit unsigned** samples and no compression.

Calculate the voxel dimensions, total voxels, raw bytes and decimal GB. Estimate
capacity for **three total copies of that raw image**. If sustained payload transfer
were 100 MB/s, what is the ideal transfer time for one copy? Use 1 GB = 10⁹ bytes
and 1 MB = 10⁶ bytes. Name at least three things omitted from this estimate.

## Peer review and exit ticket

Exchange methods records and reproduce the selected IDs without asking the author
what they meant. Circle any missing decision. Record the result of this re-run,
including mismatches rather than silently correcting them.

Submit the two counts, repaired methods record and capacity estimate. Finish:
“If this count changes next month, the first evidence I would compare is ___.”
Then add one line to your study brief from Session 1: the version, filter and query
identity your own endpoint would need recorded. Bring the brief to Session 4.

[Instructor model responses]({{ '/teaching/lectures/tools-and-methods-answers/' | relative_url }})
are public; attempt the exercise first. Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
