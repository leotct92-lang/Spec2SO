# Design Revision & Verification Traceability

Design-state version 2.0 preserves all compatible 1.x fields and adds:

- `revisions[]`: Git-backed meaningful engineering states (`REV-NNNN`).
- `checker_runs[]`: immutable tool/checker executions (`RUN-NNNN`) tied to revisions.
- `iteration_history[]`: complete failure/fix/rerun cycles (`ITER-NNNN`).
- `input_records[]` and `stage0_feedback_requests[]`: evidence and feedback.

Use `python3 tools/design_traceability.py --help`. The utility rejects changed duplicate IDs,
unknown revision references, unlinked replacement evidence, and broken iteration references.
Its `add-revision` command verifies the recorded commit exists.

```text
REV-0004 → RUN-0021 FAIL → FR-0008 → REV-0005 → RUN-0024 PASS → ITER-0001 PASS
```

Historical records are not overwritten or deleted. Only resolution/supersession links and
revision status may be added later. Human-readable views live under `docs/revisions/`.
