# Orchestrator Flows & End-to-End Pipeline

This page describes how the domain orchestrators sequence their stages and how
Stage 0 plus the 14 design domains connect into a full chip design pipeline. For the complete
per-domain flow detail, see [`MASTER_INDEX.md`](MASTER_INDEX.md).

The standard flow starts with **Input Reconstruction & Evidence Qualification**, then
Product/System Specification → Architecture Evaluation → Microarchitecture → RTL →
Verification → Formal → Synthesis → DFT → Physical Design → STA → SoC Integration →
applicable firmware/software/FPGA planning.

Any downstream missing or under-qualified input opens a Stage 0 feedback request and reruns
the affected stage after qualification. Every meaningful state is a Git-backed `REV-NNNN`,
every checker execution a `RUN-NNNN`, and every failure/fix/rerun loop an `ITER-NNNN`. See
[`Input_Reconstruction_Evidence_Qualification.md`](Input_Reconstruction_Evidence_Qualification.md)
and [`Design_Revision_Traceability.md`](Design_Revision_Traceability.md).

## Orchestrator Flows

Each orchestrator enforces a strict stage sequence with loop-back rules.

**Physical Design** (example):
```
floorplan → placement → CTS → routing →
timing_opt → power_opt → area_opt → signoff
```
If routing DRC fails → retry routing (max 3×).
If signoff timing fails → loop back to timing_opt (max 2×).
If any loop exceeds its limit → escalate to you with full state + recommendations.

All 14 domain orchestrators follow the same pattern with domain-specific stages
and criteria. The rules above are an illustration; each flow's authoritative stage
sequence and loop-back rules are in its agent file, `plugins/<domain>/agents/*-orchestrator.md`.

## End-to-End Pipeline

The 14 design domains (+ the meta pipeline orchestrator) map to a complete chip
design pipeline:

```
[0. Input Reconstruction & Evidence Qualification]
      │
      ▼
[Product/System Specification]
      │
      ▼
[1. Architecture Evaluation] ──► microarch doc
      │
      ├──► [2. RTL Design]  ──► [3. HLS] (algorithm blocks)
      │           │
      │           │           ├──► [4. Functional Verification] ◄──┐
      │           └──► [5. Formal Verification]    ◄──┤
      │                       │ (bug found)           │ fix_request loop
      │                       │                    [Meta / Pipeline Orch.]
      │                       ▼                       │
      │              [6. Logic Synthesis]          ────┘
      │                       │
      │           ┌───────────┼───────────┐
      │           ▼           ▼           ▼
      │      [7. DFT]  [8. Physical  [9. STA]
      │                   Design]
      │                       │
      │                   [Tape-out]
      │
      ├──► [10. SoC IP Integration]  (if SoC-level work)
      ├──► [11. Memory IP Design]    ──► macros + views ──► DFT / PD / STA
      ├──► [12. Compiler Toolchain]  (if custom CPU)
      ├──► [13. Embedded Firmware]
      └──► [14. FPGA Emulation]      (pre-silicon SW dev)
```
