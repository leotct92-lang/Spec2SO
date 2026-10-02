# Revision Progress — R-Car V4M Public Reconstruction

| Revision | Trigger | Checker | Result | Main change | Next revision | Recorded runtime |
|---|---|---|---|---|---|---:|
| REV-0001 | Stage 0 release | Input completeness gate | WARN | Qualified initial 70 inputs; public spec, provenance, gaps and scenarios | REV-0002 | Included in pipeline wall window |
| REV-0002 | Forward architecture pipeline | 20 linked runs | 6 PASS / 5 WARN / 9 BLOCKED | Evidence-preserving architecture, black-box microarchitecture and downstream handoffs | REV-0003 | 10.64 s recorded checker time |
| REV-0003 | Canonical inventory correction | RUN-0021 | PASS | Added explicit FlexRay UNKNOWN and pipeline-session linkage on every checker run | — (FINAL) | 3.48 s |

REV-0001 is recoverable at `f32ab22e422b45aacd664bd798daa41cd797e56b`, REV-0002 at
`3145238b53bebbc6bc0b4468722f2625766355b3`, and REV-0003 at
`2704b18dd7feda968af5cd89a9ee63c585855f94`. `design_state.json` is the machine-readable
source for the complete run list and bidirectional links.
