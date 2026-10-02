# R-Car V4M Verification and Formal Plan

Status: **WARN** for plan completeness; execution against product RTL is **BLOCKED**.

## Executable now

- Validate normalized JSON and design-state schema.
- Check public-source facts against the pinned official repository revisions.
- Check evidence taxonomy, provenance, scenario labels and unknown preservation.
- Check cross-parameter arithmetic used in derived estimates.

## Product checker matrix

| Checker | Required design/collateral | Current status | Exact unblocker |
|---|---|---|---|
| Compile/lint | Product RTL, file list, parameters, waivers | BLOCKED | Authorized RTL/IP sources and build manifest. |
| Functional simulation | RTL, executable requirements, models, tests | BLOCKED | RTL plus authoritative behavior/register/interface specs. |
| Functional coverage | Coverage model and closure targets | BLOCKED | Approved verification plan and acceptance criteria. |
| Formal properties | RTL, assumptions, reset/clock protocol, properties | BLOCKED | RTL and authoritative safety/protocol properties. |
| CDC/RDC | RTL/netlist, clocks, resets, power intent, waivers | BLOCKED | Complete clock/reset/UPF intent and sources. |
| Safety verification | Safety architecture, FMEDA/diagnostics, fault list | BLOCKED | Safety manual/certification scope and fault campaign criteria. |

No PASS will be recorded for an unexecuted product checker. When inputs arrive, each command,
version, duration, result, log/report and revision will be appended to `checker_runs[]`.
