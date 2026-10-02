# R-Car V4M Input-to-Stage Traceability Matrix

| Input group | Evidence artifacts | Consuming stages | Current disposition |
|---|---|---|---|
| Identity, CPU, cache | S1, S3, S4; public spec JSON | specification, architecture, firmware, compiler | Usable public baseline. |
| R52/safety | S1 thermal-domain evidence; gap ledger | architecture, verification, firmware, safety | Existence corroborated; topology/certification BLOCKED. |
| GPU/AI/CV | S1, S3, S7 | architecture, performance, software, verification | Topology usable; rates/precision WARN or UNKNOWN. |
| Camera/ISP/display/video | S1, S2 | architecture, integration, performance | Instance inventory usable; throughput/codec limits WARN. |
| PCIe/Ethernet/CAN/storage | S1, S2, S5 | integration, firmware, verification | Public path inventory usable; exact electrical/rate limits incomplete. |
| DRAM/cache/SRAM | S1, S2, S4; derived estimates | architecture, performance, firmware, PD | Board capacity and CPU cache usable; controller details BLOCKED. |
| Clock/reset/DVFS/voltage | S1; scenario file | RTL, CDC/RDC, synthesis, STA, firmware | Public CPU OPP only; implementation closure BLOCKED. |
| Power/thermal | S1 thermal nodes; power/area report | architecture sensitivity, power, PD | Exploratory scenarios only; sign-off BLOCKED. |
| Process/die/package | gap and power/area reports | synthesis, PD, STA, integration | UNKNOWN/assumption; sign-off BLOCKED. |
| Security/virtualization | S1, S3, S5, S6 | firmware, integration, verification | Software primitives usable; production chain/HSM UNKNOWN. |
| Linux/Yocto/toolchain | S3, S5, S6 | firmware/software planning | Usable public baseline. |
| RTL/IP/PDK/SDC/DFT collateral | exact blockers in gap ledger | RTL, formal, synthesis, DFT, PD, STA | Proprietary inputs absent; dependent stages BLOCKED. |

Value-level provenance is carried in `V4M_REQUIRED_INPUT_INVENTORY.md`, the normalized JSON and
`design_state.json`. Revision/checker/fix links are in `design_state.json` and the generated
reports under `docs/revisions/`; historical records are not replaced when evidence improves.
