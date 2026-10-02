---
name: input-reconstruction
description: >
  Reconstructs and qualifies all product/system inputs needed by downstream chip-design
  stages, actively researches gaps, preserves value-level provenance, builds bounded
  scenarios, and resolves constraint feedback without confusing estimates with facts.
version: 1.0.0
author: chuanseng-ng
license: MIT
allowed-tools: Read, Write, Bash, WebSearch, WebFetch
---

# Skill: Input Reconstruction & Evidence Qualification

## Purpose

This is reusable Stage 0 of Spec2SO. It turns incomplete public, private, or mixed source
material into a normalized product/system input inventory before architecture begins, and it
can be re-entered whenever a downstream stage discovers a missing or weak constraint. It is
product-neutral: project-specific evidence belongs in project artifacts, never in this skill.

The standard pipeline is:

`input_reconstruction → product_system_specification → architecture_evaluation →
microarchitecture → rtl → verification → formal → synthesis → dft → physical_design → sta →
soc_integration → firmware/software/fpga planning (where applicable)`.

## Stage: repository_input_discovery

### Domain Rules

1. Inspect the complete project repository and every enabled Spec2SO schema, template,
   validator, skill, agent, stage gate, example, test, script, and handoff contract.
2. Create one inventory record for every required or materially useful input. Each record has:
   `input_id`, `field_name`, `definition`, `unit`, `datatype`, `requirement` (`REQUIRED` or
   `OPTIONAL`), `consuming_stages[]`, `current_value`, `missing_status`, `evidence_status`,
   `estimation_allowed`, `acceptable_range_or_form`, and `provenance`.
3. Include functional, compute, performance, memory, interconnect, interface, clock/reset,
   voltage/process, power, area, thermal, physical/package, safety, security, software,
   verification, DFT, integration, firmware, compiler, and FPGA inputs where applicable.
4. Do not infer completeness from the supplied specification. Compare it with all downstream
   consumers and record gaps explicitly.

### QoR Metrics to Evaluate

- Downstream consumers inspected: 100% of enabled domains.
- Inventory records with owner/consumer and acceptable form: 100%.
- Duplicate field meanings: 0 unresolved.

### Common Issues & Fixes

| Issue | Fix |
|---|---|
| Same field uses different units | Select one normalized unit and retain source units in provenance. |
| A downstream prompt embeds a literal default | Inventory the value and label the default as an assumption unless sourced. |
| Proprietary input is unavailable | Record the exact artifact/view needed; continue independent stages. |

### Output Required

- Machine-readable `input_records[]` in `design_state.json`.
- Project required-input inventory with all fields listed above.

## Stage: active_evidence_research

### Domain Rules

1. Research every missing or weakly supported material field. Use this priority:
   manufacturer documents; official product pages; datasheets; public manuals/excerpts;
   application notes; official presentations; evaluation-board material; SDK/BSP/Linux/Yocto
   material; partner documentation; foundry/IP/EDA disclosures; standards; OEM/Tier-1 public
   material; conference presentations; academic papers; independent semiconductor analysis;
   teardown/die analysis; reputable engineering publications; related-product evidence; then
   engineering derivation.
2. One failed query is not exhaustion. Search alternative terminology, block names, ordering
   codes, package identifiers, software repositories, presentations, partner disclosures, and
   closely related products.
3. Resolve gaps in order: more primary-source search, independent corroboration,
   related-family evidence, engineering derivation, bounded range, scenarios, explicit
   assumption, then `UNKNOWN` as the final fallback.
4. Related-product evidence must name the exact product, relevance, differences, and why the
   result is not a fact about the target product.
5. Never copy or reconstruct confidential material and never invent sign-off collateral.

### QoR Metrics to Evaluate

- Search attempts and source classes recorded for every unresolved material field.
- Important facts with a stable URL/reference and retrieval date: 100%.
- `UNKNOWN` count reduced without promoting inference to fact.

### Common Issues & Fixes

| Issue | Fix |
|---|---|
| Main product page is sparse | Search product briefs, board manuals, BSP/device trees, SDK releases, and presentations. |
| Board power is published | Keep it as board power; never relabel it as chip power. |
| Package dimensions are known | Do not infer die area from package area. |

### Output Required

- Source ledger including unsuccessful search paths relevant to remaining gaps.
- Updated immutable input records; changes supersede earlier records rather than overwriting them.

## Stage: evidence_qualification

### Domain Rules

1. Classify every material value as exactly one of `OFFICIAL_DISCLOSED`,
   `PUBLIC_CORROBORATED`, `DERIVED_ESTIMATE`, `ENGINEERING_ASSUMPTION`, or `UNKNOWN`.
2. Every important numeric value records value, unit, source, URL/reference, source
   organization, document title, page/section, publication date, retrieval date,
   classification, `HIGH|MEDIUM|LOW` confidence, derivation method, uncertainty, lower bound,
   upper bound, and `HARD_CONSTRAINT|SOFT_CONSTRAINT|EXPLORATORY_ONLY` usage.
3. A value derived from official facts remains `DERIVED_ESTIMATE`; source authority does not
   turn arithmetic or modeling into disclosure.
4. Estimates and assumptions cannot be used as production sign-off constraints. They may
   enable clearly labeled exploratory work.
5. Historical source/value records are append-only. A corrected value names the record it
   supersedes, and the old record stays visible.

### QoR Metrics to Evaluate

- Material inputs with one valid evidence class: 100%.
- Important numeric values with complete provenance: 100%.
- Silent source/value overwrites: 0.

### Common Issues & Fixes

| Issue | Fix |
|---|---|
| Multiple sources repeat the same press release | Treat as one source lineage, not independent corroboration. |
| Value has no operating context | Reduce confidence and usage class; record the missing context. |
| Official and estimated ranges disagree | Preserve both and open a consistency finding. |

### Output Required

- Qualified input ledger and normalized product/system specification.
- Gaps and assumptions register.

## Stage: scenario_construction

### Domain Rules

1. For uncertain critical parameters create `CONSERVATIVE`, `NOMINAL_EXPLORATORY`, and
   `AGGRESSIVE` scenarios.
2. At minimum cover power, area, process, frequency, voltage, memory bandwidth, thermal,
   utilization, and timing margin when relevant.
3. Each scenario cites the input records it uses and stays within their bounds. Scenarios do
   not create new facts.
4. Keep chip, subsystem, board, idle, workload, peak, and thermal-design power distinct.

### QoR Metrics to Evaluate

- Critical uncertain parameters represented in all three scenarios: 100%.
- Scenario values outside evidence bounds: 0.

### Common Issues & Fixes

| Issue | Fix |
|---|---|
| Nominal is mistaken for official typical | Name it `NOMINAL_EXPLORATORY` everywhere. |
| Power contexts are mixed | Split records and scenarios by scope and workload. |

### Output Required

- Scenario table and machine-readable `input_reconstruction.scenarios`.

## Stage: cross_parameter_consistency

### Domain Rules

1. Check throughput against architecture/frequency, compute against memory bandwidth, ISP
   throughput against camera demand, power against process/frequency/voltage, area against
   process/IP assumptions, thermal against power, clocks against interface limits, and channel
   counts against aggregate bandwidth.
2. Record each check with equation/logic, input IDs, result, uncertainty, and disposition.
3. Resolve contradictions through better evidence or corrected derivation. If unresolved,
   downgrade confidence/usage and keep the contradiction visible.

### QoR Metrics to Evaluate

- Applicable cross-parameter checks executed: 100%.
- Unexplained contradictions in hard constraints: 0.

### Common Issues & Fixes

| Issue | Fix |
|---|---|
| Peak units use incompatible precision | Normalize operation definition and precision before comparing TOPS. |
| Interface theoretical rate is used as payload | Apply encoding/protocol/utilization efficiency explicitly. |

### Output Required

- Consistency-check ledger and resolution links.

## Stage: completeness_gate

### Domain Rules

1. Report completeness separately for functional, compute, performance, memory, interconnect,
   interfaces, clock/reset, power, area, thermal, physical, safety, security, software,
   verification, DFT, and integration.
2. Map evidence classes to project availability labels without losing the original class:
   official→`AVAILABLE_OFFICIAL`, corroborated→`AVAILABLE_CORROBORATED`, estimate→
   `AVAILABLE_ESTIMATED`, assumption→`ENGINEERING_ASSUMPTION`, unknown→`UNKNOWN`.
3. A hard constraint may pass only with adequate evidence for its intended use. Exploratory
   stages may proceed on bounded estimates/assumptions; affected production sign-off remains
   `BLOCKED` with the exact missing proprietary or business input.
4. Emit `PASS`, `WARN`, `BLOCKED`, `ESCALATE`, or `NOT_EXECUTED` in project stage reports.

### QoR Metrics to Evaluate

- Completeness by category and evidence class.
- Exact unblock requirement recorded for every blocked stage: 100%.

### Common Issues & Fixes

| Issue | Fix |
|---|---|
| Waiting for 100% official data stalls all work | Proceed with bounded exploratory inputs where allowed and block only dependent sign-off. |
| Fundamental product choice is unknown | Escalate that decision; continue unrelated preparation. |

### Output Required

- Input-completeness report and normalized spec handoff.
- `design_state.input_reconstruction` status and open feedback requests.

## Stage: downstream_feedback_resolution

### Domain Rules

1. A downstream missing/weak constraint opens `stage0_feedback_requests[]` with requesting
   stage, field, reason, current revision, and required evidence/use level.
2. Re-enter discovery/research/qualification for the requested fields, update the normalized
   spec and provenance append-only, resolve the request, and rerun only affected stages.
3. Record the loop as an `iteration_history[]` entry when it changes a released engineering
   revision. Do not reset the cross-domain iteration counter.
4. If public research cannot supply production collateral, mark the dependent stage `BLOCKED`
   and name the exact artifact; do not fabricate it and do not block unrelated stages.

### QoR Metrics to Evaluate

- Open feedback requests without a disposition: 0 at pipeline completion.
- Affected-stage reruns linked to the updated input record/revision: 100%.

### Common Issues & Fixes

| Issue | Fix |
|---|---|
| Downstream stage edits its own missing constraint | Route to Stage 0; the consumer must not invent upstream intent. |
| Research finds only a range | Record bounds, construct scenarios, and preserve production-signoff block. |

### Output Required

- Resolved feedback request with new input record IDs.
- Rerun checker record against the correct revision.
