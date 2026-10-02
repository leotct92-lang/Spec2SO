# Pipeline Execution Summary — R-Car V4M Public Reconstruction

## Counts

| Metric | Value |
|---|---:|
| Engineering revisions | 2 |
| Architecture revisions | 1 |
| RTL revisions | 0 |
| Checker runs | 19 |
| PASS / FAIL / WARN / BLOCKED | 5 / 0 / 5 / 9 |
| Failure-resolution iterations | 0 |
| Cross-domain cap | 3 |
| Cap consumed | 0 |
| Recorded checker runtime | 7.00 s |
| Pipeline wall window | 2026-10-02 17:33–18:50 UTC (4,620 s) |

## Runtime by recorded stage

| Stage | Seconds |
|---|---:|
| Framework validation | 6.76 |
| Product/system specification validation | 0.08 |
| Input reconstruction source check | 0.02 |
| Architecture evaluation | 0.01 |
| RTL design gate | 0.01 |
| Lint gate | 0.01 |
| Functional verification gate | 0.01 |
| Formal gate | 0.01 |
| CDC/RDC gate | 0.01 |
| Synthesis gate | 0.01 |
| Power/area scenario review | 0.01 |
| DFT gate | 0.01 |
| Physical-design gate | 0.01 |
| STA gate | 0.01 |
| SoC integration review | 0.01 |
| Firmware/software planning review | 0.01 |
| FPGA/prototype planning review | 0.01 |

Runtime records measure executed check/gate commands, not the human/research effort between
them. There were no retries, failure classes, or resolution durations because no checker ran
and failed. Exact commands, tool versions, timestamps and report paths are in
`design_state.json`.
