# R-Car V4M Gaps and Assumptions

## Engineering assumptions used only for exploration

- Process scenario: 7 nm nominal, 7 nm conservative-performance, 12 nm aggressive-area-cost
  sensitivity label. The naming is about scenario direction, not a manufacturing claim.
- SoC power scenarios: 15 W / 25 W / 40 W. These are chip-level exploratory envelopes, not
  measured idle, workload, peak, board power, or TDP.
- Die-area scenarios: 180 / 260 / 340 mm². These are model envelopes, never package area.
- CPU product-frequency sensitivity: 1.0 / 1.8 / 2.0 GHz. Only 0.5/1.0 GHz OPPs are official
  in the inspected BSP; higher values are not V4M facts.
- DRAM bandwidth scenarios: 17.1 / 25.6 / 34.1 GB/s theoretical, pending type/channel/rate.
- Junction-temperature planning points: 85 / 105 / 125 °C; actual ratings are unknown.
- Implementation utilization: 60 / 70 / 80%; timing margin: 15 / 10 / 5%.

## Exact proprietary or decision inputs required

1. Current V4M hardware, safety and security manuals and applicable certificates.
2. Orderable-part datasheet/package drawing and thermal characterization.
3. Product-level power definitions and measured rail data by workload/corner.
4. DRAM controller configuration, SI/PI constraints, ECC and bandwidth guarantees.
5. Implementation RTL/IP views, complete address map, clock/reset/DVFS intent.
6. PDK, standard-cell Liberty/LEF, memory compiler views, RC tech, DRC/LVS decks.
7. Sign-off SDC/modes/corners/derates and package/board SI/PI models.
8. DFT architecture, scan/MBIST collateral and production test targets.
9. Product verification plan, safety mechanisms/diagnostic coverage, and acceptance criteria.

These gaps block production RTL equivalence, synthesis, DFT, PD, STA and sign-off. They do not
block public architecture reconstruction, software planning, handoff preparation, or scenario
sensitivity analysis.
