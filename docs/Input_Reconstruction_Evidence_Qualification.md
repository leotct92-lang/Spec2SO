# Input Reconstruction & Evidence Qualification

This reusable Spec2SO Stage 0 runs before product/system specification and re-enters whenever
a downstream consumer discovers a missing, weak, contradictory, or under-qualified input.
The executable contract lives in the [skill](../plugins/input-reconstruction/skills/input-reconstruction/SKILL.md),
[orchestrator](../plugins/input-reconstruction/agents/input-reconstruction-orchestrator.md),
and [design-state schema](design_state.schema.json).

Every input record carries name, definition, unit, datatype, requirement, consuming stages,
current value, missing/evidence status, estimation policy, acceptable form, and provenance.
Evidence is exactly one of `OFFICIAL_DISCLOSED`, `PUBLIC_CORROBORATED`, `DERIVED_ESTIMATE`,
`ENGINEERING_ASSUMPTION`, or `UNKNOWN`. Numeric provenance includes context, bounds,
confidence, derivation, and usage classification. Corrections append a superseding record;
they never overwrite history.

Downstream gaps use `stage0_feedback_requests[]`. Proprietary-only gaps block only affected
production sign-off. Independent exploratory/preparatory work continues with explicit labels.
Critical uncertainties use `CONSERVATIVE`, `NOMINAL_EXPLORATORY`, and `AGGRESSIVE` scenarios.
