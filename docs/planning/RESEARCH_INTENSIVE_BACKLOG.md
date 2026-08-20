# Research intensive: independent study projects

**Status: backlogged.** Captured so the shape is not re-derived later. Nothing in
this document is built, and `/modes/#research-intensive` must keep saying so until
it is.

## What this is for

The research intensive (`/modes/#research-intensive`, defined in `_data/modes.yml`) is the third mode of use: a longer,
contributory programme that draws on the core rather than treating it as a syllabus.
It is the only mode that requires work whose output somebody downstream actually
uses, and it is the mode that currently does not exist.

The user's framing: **significant open challenges, each with a starter and a success
gate, packaged as independent study projects.**

That triple is the unit of work:

| Part | What it has to do |
|---|---|
| **Open challenge** | A question that is genuinely unresolved, stated so a reader can tell what would count as progress. Not an exercise with a hidden answer. |
| **Starter** | Something concretely doable in a few weeks with public data and no lab affiliation. The point is a foothold, not a scoped-down version of the whole problem. |
| **Success gate** | What would make the result credible to a lab: the specific artifact, the check it has to survive, and who could evaluate it. This is what makes the mode contributory rather than aspirational. |

A project that cannot state all three honestly should not ship. In particular, a
success gate that amounts to "you did the exercise" is the failure mode this mode
exists to avoid.

## Two kinds of project, and both are needed

**Type A — open questions in the field.** Real research. The trainee may not resolve
it; the gate is whether the attempt is defensible.

**Type B — gaps in this site's own apparatus.** Contributory work whose output is
used here. Smaller, more tractable, and the only category where "somebody downstream
actually uses it" is guaranteed rather than hoped for. These are the ones that make
the mode real on day one.

A working programme probably pairs one of each: a Type B project that produces
something used, and a Type A project that produces something arguable.

## Candidate challenges

Drawn from what is verifiably in this repository — the expert seed corpus, the
technical units, and gaps measured during the content review. Each needs the
starter and gate written out properly; what follows is the seed, not the spec.

### Type A — open in the field

1. **What does a calibrated confidence tier actually buy?**
   The units argue throughout that calibration matters more than raw accuracy
   (Units 05–07). Whether a trainee's stated confidence carries information that
   improves a downstream reconstruction is, as far as the curriculum goes, asserted
   rather than measured. *Starter:* score your own high-confidence calls separately
   on a labelled public subvolume. *Gate:* a confusion matrix plus accuracy within
   your own top tier, and a statement of whether your confidence separated the two.

2. **Does automated proofreading change the shape of the allocation problem?**
   NEURD (Dorkenwald et al., *Nature Methods* 2024, `10.1038/s41592-024-02515-z`)
   removes a large share of errors before a human sees them. Every triage rule in
   the content library assumes the pre-automation error population. Whether
   priority-ranking still works on the residue is untested here. *Starter:* compare
   the error distribution before and after automated correction on one public
   volume. *Gate:* a revised triage rule with the evidence for why it differs.

3. **Which null model is defensible for a spatially embedded, degree-heterogeneous
   connectome?** Unit 09 argues Erdős–Rényi is inadequate and works three nulls, but
   the field has no settled answer. *Starter:* re-run one published motif result
   under distance-preserving and degree-preserving nulls. *Gate:* an effect size
   under each, with a pre-specified choice and the reason.

4. **Does a published motif result survive its own reconstruction error?**
   *Starter:* an error-injection simulation at the merge and split rates the source
   dataset reports. *Gate:* an error band on the headline number, and a statement of
   whether the claim survives.

5. **Does light-microscopy connectomics revise Unit 01's founding premise?**
   LICONN (`boyden/boyden-2025-liconn.json` in the seed corpus) is taught nowhere,
   and Unit 01 §1 rests on EM being *required* for synapse resolution. *Starter:* a
   modality memo comparing what each can and cannot establish. *Gate:* a defensible
   revision — or a defensible refusal to revise — of the premise as written.

6. **What does ML-guided acquisition do to the fixed-dose-budget framing?**
   SmartEM (`shavit/shavit-2025-smartem.json`) against Unit 03. Same shape as 5.

7. **Where does X-ray holographic nano-tomography sit on the modality chart?**
   `kuan/kuan-2020-xray-nanotomography.json` against Unit 02.

*Items 5–7 are the "curriculum lags its own reading list" findings from the content
review. They are Type A because the answer is not obvious, and Type B-adjacent
because the output patches a real gap here.*

### Type B — contributory, output used here

8. **Build the perceptual calibration corpus.** Several hundred native-resolution
   z-stack crops from MICrONS / H01 / FlyWire via CloudVolume, labels derived from
   the released segmentation. This is the blocker for the whole mode: it is the
   calibration gate, and `/side-quests/` currently lists it as not built.
   *Gate:* the drill runs through the existing interactive machinery and returns a
   populated confusion matrix from real labels.

9. **Establish a proofreading-level reporting convention.** No standard exists for
   stating what "proofread" means for a given cell. The side quest asks trainees to
   define levels; nothing collects or compares them. *Gate:* a convention two people
   apply to the same volume and broadly agree on.

10. **Measure inter-annotator agreement across trainees.** The site argues agreement
    statistics must accompany throughput and provides no way to collect them.
    *Gate:* an agreement number from more than one person on shared cases.

11. **Audit the figure corpus against its captions.** Partly done, unverified: the
    captions were rewritten by an agent that could not see the images. *Gate:* every
    caption confirmed by someone who opened the file, and the placeholders retired.

## What has to exist before any of this ships

From `/modes/`, unchanged:

1. **A calibration gate** a lab would trust — item 8 above.
2. **Real tasks with real consumers** — items 8–11 qualify; items 1–7 need a named
   reader.
3. **Structured review** — a named reviewer, a rubric, and a return path. The
   worksheets already carry peer-review sections; the exchange is what is missing.

Shipping projects without (3) turns the mode into self-study with harder homework,
which is the specific thing it is not.

## Open questions to settle first

- **Who reviews?** Without an answer, every success gate is self-assessed and the
  mode collapses back into self-study.
- **Do projects need a cohort, or can one person run one alone?** Items 10 and
  arguably 1 need more than one person by construction.
- **What is the artifact's home?** A portfolio page here, a repository, a
  submission somewhere. "Write it up" is not a destination.
