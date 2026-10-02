"""Stage 0 and design revision/checker traceability contract tests."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


def _module():
    path = ROOT / "tools" / "design_traceability.py"
    spec = importlib.util.spec_from_file_location("design_traceability", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def trace():
    return _module()


def provenance(classification="OFFICIAL_DISCLOSED", source="Renesas"):
    return {
        "source": source,
        "reference": "https://example.invalid/source",
        "source_organization": source,
        "document_title": "Public product brief",
        "page_or_section": "Features",
        "publication_date": None,
        "retrieval_date": "2026-10-03",
        "evidence_classification": classification,
        "confidence": "HIGH" if classification == "OFFICIAL_DISCLOSED" else "LOW",
        "derivation_method": None if classification == "OFFICIAL_DISCLOSED" else "bounded estimate",
        "uncertainty": None,
        "lower_bound": None,
        "upper_bound": None,
        "usage_classification": "HARD_CONSTRAINT" if classification == "OFFICIAL_DISCLOSED" else "EXPLORATORY_ONLY",
    }


def input_record(input_id="IN-0001", classification="OFFICIAL_DISCLOSED", value=4):
    return {
        "input_id": input_id,
        "field_name": "compute.cpu_core_count",
        "definition": "Application CPU core count",
        "unit": "cores",
        "datatype": "integer",
        "requirement": "REQUIRED",
        "consuming_stages": ["architecture", "verification"],
        "current_value": value,
        "missing_status": "AVAILABLE",
        "evidence_status": classification,
        "estimation_allowed": False,
        "acceptable_range_or_form": ">=1",
        "provenance": provenance(classification),
    }


def revision(revision_id, parent, sha, domain="rtl"):
    return {
        "revision_id": revision_id,
        "parent_revision_id": parent,
        "git_commit_sha": sha,
        "created_at": "2026-10-03T01:00:00Z",
        "created_by": "test",
        "change_domain": [domain],
        "trigger_type": "verification_failure" if parent else "baseline",
        "trigger_id": "FR-0001" if parent else None,
        "trigger_stage": "functional_verification" if parent else "stage0",
        "trigger_checker": "verification-orchestrator" if parent else None,
        "trigger_failure_class": "functional" if parent else "none",
        "trigger_summary": "failure" if parent else "baseline",
        "change_summary": "fix" if parent else "initial baseline",
        "affected_files": ["rtl/top.sv"] if domain == "rtl" else ["docs/spec.md"],
        "status": "ACTIVE",
    }


def run(run_id, revision_id, result, fix_request_id=None, start=0, duration=2):
    return {
        "run_id": run_id,
        "revision_id": revision_id,
        "stage": "functional_verification",
        "checker": "pytest-model",
        "tool_version": "1.0",
        "command_or_config": "pytest model",
        "start_time": f"2026-10-03T01:00:{start:02d}Z",
        "end_time": f"2026-10-03T01:00:{start + duration:02d}Z",
        "duration_seconds": duration,
        "result": result,
        "failure_class": "functional" if result == "FAIL" else "none",
        "relevant_constraint": "compute.cpu_core_count",
        "key_metrics": {"tests": 1},
        "summary": result.lower(),
        "log_path": "logs/run.log",
        "report_path": "reports/run.json",
        "fix_request_id": fix_request_id,
    }


def fix_request():
    return {
        "id": "FR-0001",
        "created_at": "2026-10-03T01:00:02Z",
        "updated_at": "2026-10-03T01:00:02Z",
        "created_by": "verification-orchestrator",
        "failure_class": "functional",
        "retry_strategy": "refine",
        "test_name": "directed_test",
        "property_or_assertion": None,
        "seed": 1,
        "waveform_path": None,
        "log_path": "logs/run.log",
        "suspected_rtl": {"module": "top", "signal": None, "file": "rtl/top.sv", "line_range": [1, 2]},
        "summary": "bad response",
        "expected_behavior": "good",
        "observed_behavior": "bad",
        "session_id": "ps_test",
        "status": "fixed",
        "rtl_response": {},
        "history": [],
        "failed_revision_id": "REV-0001",
        "failed_run_id": "RUN-0001",
        "resolved_revision_id": None,
        "resolution_run_id": None,
    }


def test_stage0_detects_missing_input(trace):
    state = {}
    trace.add_stage0_feedback_request(state, {
        "request_id": "S0-0001", "created_at": "2026-10-03T00:00:00Z",
        "requesting_stage": "synthesis", "field_name": "pvt.liberty",
        "reason": "missing production library", "status": "OPEN",
    })
    assert state["stage0_feedback_requests"][0]["status"] == "OPEN"


def test_official_and_estimate_remain_distinct_and_provenance_is_preserved(trace):
    state = {}
    trace.append_input_record(state, input_record())
    estimate = input_record("IN-0002", "DERIVED_ESTIMATE", 6)
    estimate["supersedes_input_id"] = "IN-0001"
    trace.append_input_record(state, estimate)
    assert [r["evidence_status"] for r in state["input_records"]] == [
        "OFFICIAL_DISCLOSED", "DERIVED_ESTIMATE"
    ]
    assert state["input_records"][0]["provenance"]["document_title"] == "Public product brief"


def test_historical_evidence_cannot_be_silently_overwritten(trace):
    state = {}
    trace.append_input_record(state, input_record())
    changed = input_record(value=8)
    with pytest.raises(trace.TraceabilityError, match="immutable"):
        trace.append_input_record(state, changed)
    unlinked = input_record("IN-0002", "DERIVED_ESTIMATE", 8)
    with pytest.raises(trace.TraceabilityError, match="supersedes_input_id"):
        trace.append_input_record(state, unlinked)


def test_downstream_gap_contract_invokes_stage0():
    shared = (ROOT / "tools" / "agent_shared_sections.md").read_text(encoding="utf-8")
    assert "stage0_feedback_requests[]" in shared
    assert "`input-reconstruction-orchestrator`" in shared


def test_failure_fix_revision_rerun_and_iteration_chain(trace):
    state = {"fix_requests": [fix_request()]}
    trace.append_revision(state, revision("REV-0001", None, "1" * 40))
    trace.record_checker_run(state, run("RUN-0001", "REV-0001", "FAIL", "FR-0001"))
    trace.append_revision(state, revision("REV-0002", "REV-0001", "2" * 40))
    trace.add_revision_resolution(state, "REV-0001", status="SUPERSEDED", superseded_by="REV-0002")
    trace.record_checker_run(state, run("RUN-0002", "REV-0002", "PASS", start=3))
    trace.link_fix_request(
        state, "FR-0001", failed_revision_id="REV-0001", failed_run_id="RUN-0001",
        resolved_revision_id="REV-0002", rerun_id="RUN-0002",
    )
    trace.record_iteration(state, {
        "iteration_id": "ITER-0001", "pipeline_session_id": "ps_test",
        "input_revision_id": "REV-0001", "failed_run_id": "RUN-0001",
        "fix_request_id": "FR-0001", "output_revision_id": "REV-0002",
        "rerun_id": "RUN-0002", "result": "PASS",
        "start_time": "2026-10-03T01:00:00Z", "end_time": "2026-10-03T01:00:05Z",
        "duration_seconds": 5,
    })
    assert state["checker_runs"][1]["revision_id"] == "REV-0002"
    assert state["revisions"][0]["revision_id"] == "REV-0001"
    assert state["fix_requests"][0]["resolved_revision_id"] == "REV-0002"
    assert state["iteration_history"][0]["duration_seconds"] == 5
    assert trace.calculate_metrics(state)["loop_back_cycles"] == 1


def test_checker_requires_known_revision(trace):
    with pytest.raises(trace.TraceabilityError, match="unknown revision"):
        trace.record_checker_run({}, run("RUN-0001", "REV-9999", "BLOCKED"))


def test_cross_domain_cap_still_applies():
    agent = (ROOT / "plugins/meta/agents/pipeline-orchestrator.md").read_text(encoding="utf-8")
    assert "cross_domain_iteration_count >= max_cross_domain_iterations" in agent


def test_existing_design_state_compatibility_and_new_schema_chain(trace):
    schema = json.loads((ROOT / "docs/design_state.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    legacy = json.loads((ROOT / "plugins/meta/skills/pipeline-orchestration/examples/design_state.fix_request.json").read_text(encoding="utf-8"))
    assert not list(validator.iter_errors(legacy))

    state = {"format_version": "2.0", "fix_requests": [fix_request()], "history": []}
    trace.append_revision(state, revision("REV-0001", None, "1" * 40))
    trace.record_checker_run(state, run("RUN-0001", "REV-0001", "FAIL", "FR-0001"))
    trace.append_revision(state, revision("REV-0002", "REV-0001", "2" * 40))
    trace.record_checker_run(state, run("RUN-0002", "REV-0002", "PASS"))
    trace.link_fix_request(state, "FR-0001", failed_revision_id="REV-0001", failed_run_id="RUN-0001", resolved_revision_id="REV-0002", rerun_id="RUN-0002")
    trace.record_iteration(state, {
        "iteration_id": "ITER-0001", "pipeline_session_id": "ps_test",
        "input_revision_id": "REV-0001", "failed_run_id": "RUN-0001",
        "fix_request_id": "FR-0001", "output_revision_id": "REV-0002",
        "rerun_id": "RUN-0002", "result": "PASS", "start_time": "x",
        "end_time": "y", "duration_seconds": 1,
    })
    assert not list(validator.iter_errors(state))


def test_stage0_plugin_is_registered():
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    assert any(p["name"] == "chip-design-input-reconstruction" for p in marketplace["plugins"])
