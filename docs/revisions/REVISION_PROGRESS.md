# Revision Progress — R-Car V4M Public Reconstruction

| Revision | Trigger | Checker | Result | Main change | Next revision | Recorded runtime |
|---|---|---|---|---|---|---:|
| REV-0001 | Stage 0 release | Input completeness gate | WARN | Qualified 70 inputs; public spec, provenance, gaps and scenarios | REV-0002 | Included in pipeline wall window |
| REV-0002 | Forward architecture pipeline | 19 linked runs | 5 PASS / 5 WARN / 9 BLOCKED | Evidence-preserving architecture, black-box microarchitecture and downstream handoffs | — (FINAL) | 7.00 s recorded checker time |

REV-0001 is recoverable at `f32ab22e422b45aacd664bd798daa41cd797e56b` and REV-0002 at
`3145238b53bebbc6bc0b4468722f2625766355b3`. `design_state.json` is the machine-readable
source for the complete run list and bidirectional links.
