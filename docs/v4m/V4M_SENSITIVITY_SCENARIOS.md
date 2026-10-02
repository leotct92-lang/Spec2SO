# R-Car V4M Sensitivity Scenarios

These scenarios keep architecture work moving while public evidence is incomplete. They are
not Renesas specifications. `NOMINAL_EXPLORATORY` is the reference case; `CONSERVATIVE`
protects margin/capacity; `AGGRESSIVE` stresses performance or implementation density. A
scenario label does not imply likelihood.

| Parameter | CONSERVATIVE | NOMINAL_EXPLORATORY | AGGRESSIVE | Evidence / use |
|---|---:|---:|---:|---|
| CPU frequency | 1.0 GHz | 1.8 GHz | 2.0 GHz | 1.0 GHz is an OFFICIAL_DISCLOSED BSP OPP (S1); 1.8/2.0 are ENGINEERING_ASSUMPTION. SOFT/EXPLORATORY only. |
| CPU OPP voltage | 0.825 V | 0.900 V | 1.000 V | 0.825 V is OFFICIAL_DISCLOSED at public OPPs (S1); others are ENGINEERING_ASSUMPTION. Never use as rail limits. |
| Process model | 12 nm equivalent | 7 nm equivalent | 7 nm high-performance | ENGINEERING_ASSUMPTION; foundry and actual node remain UNKNOWN. |
| SoC power envelope | 15 W | 25 W | 40 W | ENGINEERING_ASSUMPTION chip envelope; not idle, measured workload, board power, peak, or TDP. |
| Bare-die area envelope | 180 mm² | 260 mm² | 340 mm² | ENGINEERING_ASSUMPTION bounds; no public scaled die evidence. Never package area. |
| Theoretical DRAM bandwidth | 17.1 GB/s | 25.6 GB/s | 34.1 GB/s | DERIVED_ESTIMATE from explicit hypothetical bus/rate combinations; not V4M controller claims. |
| Planning junction point | 85 °C | 105 °C | 125 °C | ENGINEERING_ASSUMPTION; not a rated limit. |
| Placeable utilization | 60% | 70% | 80% | ENGINEERING_ASSUMPTION for floorplan sensitivity only. |
| Timing margin | 15% | 10% | 5% | ENGINEERING_ASSUMPTION relative to the selected exploratory period. |

## Scenario formulas

- Clock period is `1 / frequency`; 1.0, 1.8, and 2.0 GHz correspond to 1.000, 0.556,
  and 0.500 ns before margin.
- Effective exploratory periods after reserving margin are 0.850, 0.500, and 0.475 ns.
- DRAM bandwidth is `transfers/s × aggregate bus width / 8`. The three illustrative cases
  are respectively 4.266 GT/s × 32 bits, 3.2 GT/s × 64 bits, and 4.266 GT/s × 64 bits.
- A workload allowance of 70% of theoretical bandwidth gives 12.0, 17.9, and 23.9 GB/s.
  The 70% factor is an ENGINEERING_ASSUMPTION, not a measured efficiency.

## Decision policy

Architecture and software planning may use the scenarios with `EXPLORATORY_ONLY` usage.
RTL, safety, DFT, package, PD, STA, and production power/thermal sign-off may not silently
promote them to hard constraints. When official collateral arrives, Stage 0 adds a new input
record that supersedes the scenario; history remains visible and affected stages rerun.
