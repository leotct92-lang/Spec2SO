# R-Car V4M → Spec2SO End-to-End Task Packet

## Objective
Use public, citable information about Renesas R-Car V4M to build a structured product/system specification at the abstraction level expected by this repository, then execute the repository's end-to-end flow as far as the available evidence and tools allow.

The goal is NOT to recreate a confidential User Manual or invent undocumented implementation details.

## Source policy
1. Prefer Renesas official public sources first:
   - R-Car V4M product page
   - product briefs / datasheets / block diagrams
   - R-Car SDK / software pages
   - safety and security pages
   - evaluation board / GrayHawk pages
   - toolchain and ecosystem pages
2. Secondary public sources may be used only to fill context, and must be clearly labeled as secondary.
3. Every extracted fact must preserve provenance: source URL, document/page title, publication/revision date when available.
4. Never promote an inference into a confirmed fact.
5. Never fabricate register maps, address maps, clocks, reset trees, internal buses, PDK/process details, die area, power budget, or timing constraints.

## Required abstraction level
The input to Spec2SO is a structured PRODUCT / SYSTEM specification, not a raw customer wish and not a register-level user manual.

Expected chain:
Customer / use-case requirements
→ Product/System Specification
→ Architecture Evaluation
→ Microarchitecture Specification
→ RTL handoff
→ Verification / Formal / Synthesis / DFT / PD / STA
→ Sign-off artifacts where tools and evidence permit.

## Build the V4M public spec pack
Create:
- docs/v4m/V4M_PUBLIC_PRODUCT_SPEC.md
- docs/v4m/V4M_PUBLIC_PRODUCT_SPEC.json
- docs/v4m/V4M_SOURCE_LEDGER.md
- docs/v4m/V4M_GAPS_AND_ASSUMPTIONS.md
- docs/v4m/V4M_TRACEABILITY_MATRIX.md

The structured spec should cover, where public evidence exists:
- intended automotive / ADAS use cases
- CPU subsystem
- real-time / safety CPU subsystem
- AI / CV accelerators
- GPU / display / graphics
- ISP / camera / image processing
- DSP / media accelerators
- memory subsystem and public bandwidth/capacity limits
- PCIe / Ethernet / CAN / FlexRay / serial and automotive I/O
- safety features / ISO 26262 claims
- security features
- software / SDK / OS / hypervisor support
- development boards / reference platforms
- package / thermal / process information if publicly disclosed
- measurable public performance figures
- any published power figures, with exact operating context

## Constraint discipline
The architecture orchestrator in this repo requires:
- constraints.clock.clk_mhz
- constraints.area.area_um2
- constraints.power.power_mw

If a required value is not publicly disclosed:
- keep it null;
- record it as a spec_gap;
- do not invent a value;
- explain what source or engineering decision would be needed to unblock architecture sign-off.

A workload-specific power number must not be treated as whole-SoC power budget unless the source explicitly says so.

## Architecture execution
Run the repository's architecture flow:
spec_analysis
→ arch_exploration
→ perf_modelling
→ power_area_estimation
→ risk_assessment
→ arch_signoff

Produce:
- V4M-derived architecture baseline
- alternative architecture candidates only where justified
- assumptions and confidence level for each decision
- microarchitecture document
- RTL handoff package
- architecture sign-off report OR an explicit gated/spec-gap report

## Downstream end-to-end flow
If architecture handoff passes:
1. RTL Design
2. HLS for algorithmic blocks where appropriate
3. Functional Verification
4. Formal Verification
5. Logic Synthesis
6. DFT
7. Physical Design
8. STA
9. SoC IP Integration
10. Memory-IP planning
11. Firmware / BSP planning
12. FPGA emulation planning

Use the repo orchestrators and their loop-back rules. Never mark a stage PASS unless the required tool/evidence actually ran and passed.

## Sign-off truthfulness
For proprietary sign-off items requiring unavailable PDK, standard-cell libraries, macro views, SDC, IP views, licensed EDA tools, or confidential implementation collateral:
- do not simulate success;
- mark the stage BLOCKED / ESCALATE with exact missing inputs;
- still produce all preparatory collateral possible (scripts, constraints templates, manifests, checklists, expected outputs, handoff package).

## Deliverables
At minimum:
- complete public-source V4M spec pack
- architecture report
- traceability matrix source → requirement → architecture decision → downstream artifact
- design_state.json updated consistently
- list of all assumptions and unresolved gaps
- all generated source/config/test artifacts
- test logs and command history
- final END_TO_END_STATUS.md with:
  - PASS / WARN / BLOCKED per stage
  - evidence for each status
  - exact missing inputs for blocked stages
  - recommended next action

## Git workflow
Work on a dedicated branch derived from the current fork.
Commit in logical increments.
Do not overwrite upstream history.
Open a PR back to the fork's default branch when the task reaches a coherent review point.

## Completion condition
The task is complete only when:
1. public V4M information has been exhaustively harvested from reasonable public sources;
2. the structured product/system spec and provenance ledger are committed;
3. the Spec2SO flow has been executed as far as evidence/tools permit;
4. all blocked stages identify concrete missing inputs instead of inventing results;
5. an end-to-end status report and PR are available for review.
