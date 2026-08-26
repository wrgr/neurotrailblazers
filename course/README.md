# Technical Connectomics Course Workspace

This directory is the working area for building the canonical open connectomics course
("Technical Training: Nanoscale Connectomics") in iterative passes.

## Structure
- `source-ingest/`
  - Raw source assessments and mapping notes from PPT/PDF/doc inputs.
- `units/`
  - Canonical unit source docs used to produce both website and presentation outputs.

Planning boards, authoring templates, reviews, and editorial rules
(`workboard.md`, `templates/`, `reviews/`, `decision-rules.md`,
`capability-development-plan.md`, `instructional-framework.md`) live on the
`holding/internal-planning` branch, off the deployed branch.

## Execution model
1. Ingest source files and manifests.
2. Build/maintain one canonical unit doc per topic.
3. Derive website copy and slide outline from the unit doc.
4. Validate links/assets/attribution.
5. Mark unit status and move to next.
