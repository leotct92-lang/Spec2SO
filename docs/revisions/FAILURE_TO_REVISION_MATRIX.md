# Failure-to-Revision Matrix — R-Car V4M Public Reconstruction

No checker returned `FAIL`; therefore this execution created no V4M fix request, fixing
revision or failure-resolution iteration. Nine checks returned `BLOCKED` before execution
because product RTL or proprietary collateral was absent. `BLOCKED` is not relabeled `FAIL`.

| Failed run | Failed revision | Failure class | Fix request | Fixing revision | Rerun | Result |
|---|---|---|---|---|---|---|
| _None_ | — | — | — | — | — | — |

The reusable failure → fix → revision → rerun behavior is exercised by
`tests/test_stage0_traceability.py::test_failure_fix_revision_rerun_and_iteration_chain`.
Future real failures append rows; they never replace the failed revision or run.
