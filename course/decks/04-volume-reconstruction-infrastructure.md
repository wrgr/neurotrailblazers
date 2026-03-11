# Deck Spec: 04 Volume Reconstruction Infrastructure

## Session
- Duration: 80 + 10 min
- Outcome: architecture and rollback plan
- Figure source: `course/units/figures/04-volume-reconstruction-infrastructure-selected-v1.md`

## Slide plan
1. Title and systems view
   - Content: connectomics as data-platform engineering.
2. Reference architecture
   - Content: ingest, transform, inference, post-process, serving.
3. Data contracts
   - Content: stage I/O schemas and validation.
4. Orchestration
   - Content: queues, retries, idempotent outputs.
5. Versioning and lineage
   - Content: model hash, params, code revision, source IDs.
6. Storage strategy
   - Content: multiscale chunks for proofreading vs analysis.
7. API and query layer
   - Content: serving large volumes and graph queries.
8. Release engineering
   - Content: candidate builds, promotion gates.
9. Reliability metrics
   - Content: throughput, failure rate, MTTR, quality SLOs.
10. Cost envelope
    - Content: compute/storage cost per processed volume.
11. Failure modes
    - Content: non-determinism, provenance drift, bottlenecks.
12. Case + bridge
    - Content: rollback scenario; bridge to ultrastructure interpretation.

## Assessment
- Prompt: produce a staged pipeline with three mandatory lineage fields per stage.
- Rubric: traceability, resilience, and operational realism.
