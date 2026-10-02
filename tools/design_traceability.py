#!/usr/bin/env python3
"""Append-only design revision and verification traceability helpers.

The orchestration prompts define *when* records are required; this module defines
how they are written without silently replacing historical evidence.  It uses only
the Python standard library so every Spec2SO checkout can use it before optional
EDA dependencies are installed.
"""

from __future__ import annotations

import argparse
import copy
import fcntl
import json
import os
import subprocess
import tempfile
from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EVIDENCE_CLASSES = {
    "OFFICIAL_DISCLOSED",
    "PUBLIC_CORROBORATED",
    "DERIVED_ESTIMATE",
    "ENGINEERING_ASSUMPTION",
    "UNKNOWN",
}
CONFIDENCE_LEVELS = {"HIGH", "MEDIUM", "LOW"}
USAGE_CLASSES = {"HARD_CONSTRAINT", "SOFT_CONSTRAINT", "EXPLORATORY_ONLY"}
RUN_RESULTS = {"PASS", "FAIL", "WARN", "BLOCKED"}
REVISION_STATUSES = {"ACTIVE", "SUPERSEDED", "FINAL"}
ITERATION_RESULTS = {"PASS", "FAIL", "WARN", "BLOCKED", "ESCALATE"}


class TraceabilityError(ValueError):
    """Raised when a write would violate a traceability invariant."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"format_version": "2.0"}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TraceabilityError("design state root must be an object")
    return data


def atomic_write(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = utc_now()
    version = state.get("format_version")
    if version in {None, "1.0", "1.1", "1.2", "1.3", "1.4", "1.5"}:
        state["format_version"] = "2.0"
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(state, stream, indent=2, sort_keys=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


@contextmanager
def locked_state(path: Path):
    """Serialize a complete CLI read-modify-write transaction across processes."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_name(f".{path.name}.lock")
    with lock_path.open("a+", encoding="utf-8") as lock_stream:
        fcntl.flock(lock_stream.fileno(), fcntl.LOCK_EX)
        try:
            yield load_state(path)
        finally:
            fcntl.flock(lock_stream.fileno(), fcntl.LOCK_UN)


def _require(record: dict[str, Any], fields: set[str], kind: str) -> None:
    missing = sorted(field for field in fields if field not in record)
    if missing:
        raise TraceabilityError(f"{kind} missing required fields: {', '.join(missing)}")


def _by_id(records: list[dict[str, Any]], key: str, value: str) -> dict[str, Any] | None:
    return next((item for item in records if item.get(key) == value), None)


def _append_unique(
    state: dict[str, Any], collection: str, key: str, record: dict[str, Any]
) -> None:
    records = state.setdefault(collection, [])
    existing = _by_id(records, key, record[key])
    if existing is not None:
        if existing == record:
            return
        raise TraceabilityError(
            f"immutable {collection} record {record[key]!r} already exists with different content"
        )
    records.append(copy.deepcopy(record))


def append_input_record(state: dict[str, Any], record: dict[str, Any]) -> None:
    required = {
        "input_id",
        "field_name",
        "definition",
        "unit",
        "datatype",
        "requirement",
        "consuming_stages",
        "current_value",
        "missing_status",
        "evidence_status",
        "estimation_allowed",
        "acceptable_range_or_form",
        "provenance",
    }
    _require(record, required, "input record")
    provenance = record["provenance"]
    _require(
        provenance,
        {
            "source",
            "reference",
            "source_organization",
            "document_title",
            "page_or_section",
            "publication_date",
            "retrieval_date",
            "evidence_classification",
            "confidence",
            "derivation_method",
            "uncertainty",
            "lower_bound",
            "upper_bound",
            "usage_classification",
        },
        "input provenance",
    )
    if provenance["evidence_classification"] not in EVIDENCE_CLASSES:
        raise TraceabilityError("invalid evidence classification")
    if provenance["confidence"] not in CONFIDENCE_LEVELS:
        raise TraceabilityError("invalid evidence confidence")
    if provenance["usage_classification"] not in USAGE_CLASSES:
        raise TraceabilityError("invalid usage classification")

    records = state.setdefault("input_records", [])
    existing_id = _by_id(records, "input_id", record["input_id"])
    if existing_id is not None:
        if existing_id == record:
            return
        raise TraceabilityError(
            f"immutable input_records record {record['input_id']!r} already exists with different content"
        )
    prior = [item for item in records if item.get("field_name") == record["field_name"]]
    if prior:
        supersedes = record.get("supersedes_input_id")
        if not supersedes or not _by_id(prior, "input_id", supersedes):
            raise TraceabilityError(
                "a new value for an existing field must name supersedes_input_id; "
                "historical input evidence is append-only"
            )
    records.append(copy.deepcopy(record))


def add_stage0_feedback_request(state: dict[str, Any], request: dict[str, Any]) -> None:
    _require(
        request,
        {
            "request_id",
            "created_at",
            "requesting_stage",
            "field_name",
            "reason",
            "status",
        },
        "Stage 0 feedback request",
    )
    if request["status"] not in {"OPEN", "RESOLVED", "BLOCKED"}:
        raise TraceabilityError("invalid Stage 0 feedback status")
    _append_unique(state, "stage0_feedback_requests", "request_id", request)


def append_revision(state: dict[str, Any], revision: dict[str, Any]) -> None:
    required = {
        "revision_id",
        "parent_revision_id",
        "git_commit_sha",
        "created_at",
        "created_by",
        "change_domain",
        "trigger_type",
        "trigger_id",
        "trigger_stage",
        "trigger_checker",
        "trigger_failure_class",
        "trigger_summary",
        "change_summary",
        "affected_files",
        "status",
    }
    _require(revision, required, "revision")
    if revision["status"] not in REVISION_STATUSES:
        raise TraceabilityError("invalid revision status")
    revisions = state.setdefault("revisions", [])
    parent_id = revision["parent_revision_id"]
    if parent_id is not None and _by_id(revisions, "revision_id", parent_id) is None:
        raise TraceabilityError(f"unknown parent revision {parent_id!r}")
    if parent_id is None and revisions:
        raise TraceabilityError("only the first revision may have a null parent")
    _append_unique(state, "revisions", "revision_id", revision)
    state["current_revision_id"] = revision["revision_id"]


def add_revision_resolution(
    state: dict[str, Any], revision_id: str, *, status: str, superseded_by: str | None = None
) -> None:
    """Apply the only permitted mutation to a historical revision: resolution metadata."""
    if status not in REVISION_STATUSES:
        raise TraceabilityError("invalid revision status")
    revision = _by_id(state.get("revisions", []), "revision_id", revision_id)
    if revision is None:
        raise TraceabilityError(f"unknown revision {revision_id!r}")
    if superseded_by and _by_id(state.get("revisions", []), "revision_id", superseded_by) is None:
        raise TraceabilityError(f"unknown superseding revision {superseded_by!r}")
    revision["status"] = status
    if superseded_by:
        if revision.get("superseded_by") not in {None, superseded_by}:
            raise TraceabilityError("revision already has a different superseded_by link")
        revision["superseded_by"] = superseded_by


def record_checker_run(state: dict[str, Any], run: dict[str, Any]) -> None:
    required = {
        "run_id",
        "revision_id",
        "stage",
        "checker",
        "tool_version",
        "command_or_config",
        "start_time",
        "end_time",
        "duration_seconds",
        "result",
        "failure_class",
        "relevant_constraint",
        "key_metrics",
        "summary",
        "log_path",
        "report_path",
        "fix_request_id",
    }
    _require(run, required, "checker run")
    if run["result"] not in RUN_RESULTS:
        raise TraceabilityError("invalid checker result")
    if _by_id(state.get("revisions", []), "revision_id", run["revision_id"]) is None:
        raise TraceabilityError(f"checker run references unknown revision {run['revision_id']!r}")
    _append_unique(state, "checker_runs", "run_id", run)


def link_fix_request(
    state: dict[str, Any], fix_request_id: str, *, failed_revision_id: str,
    failed_run_id: str, resolved_revision_id: str | None = None,
    rerun_id: str | None = None,
) -> None:
    request = _by_id(state.get("fix_requests", []), "id", fix_request_id)
    if request is None:
        raise TraceabilityError(f"unknown fix request {fix_request_id!r}")
    for field, value in {
        "failed_revision_id": failed_revision_id,
        "failed_run_id": failed_run_id,
        "resolved_revision_id": resolved_revision_id,
        "resolution_run_id": rerun_id,
    }.items():
        if value is None:
            continue
        if request.get(field) not in {None, value}:
            raise TraceabilityError(f"fix request already links {field} to a different record")
        request[field] = value


def record_iteration(state: dict[str, Any], iteration: dict[str, Any]) -> None:
    required = {
        "iteration_id",
        "pipeline_session_id",
        "input_revision_id",
        "failed_run_id",
        "fix_request_id",
        "output_revision_id",
        "rerun_id",
        "result",
        "start_time",
        "end_time",
        "duration_seconds",
    }
    _require(iteration, required, "iteration")
    if iteration["result"] not in ITERATION_RESULTS:
        raise TraceabilityError("invalid iteration result")
    revisions = state.get("revisions", [])
    for field in ("input_revision_id", "output_revision_id"):
        if _by_id(revisions, "revision_id", iteration[field]) is None:
            raise TraceabilityError(f"iteration references unknown {field}")
    runs = state.get("checker_runs", [])
    for field in ("failed_run_id", "rerun_id"):
        if _by_id(runs, "run_id", iteration[field]) is None:
            raise TraceabilityError(f"iteration references unknown {field}")
    _append_unique(state, "iteration_history", "iteration_id", iteration)


def calculate_metrics(state: dict[str, Any]) -> dict[str, Any]:
    revisions = state.get("revisions", [])
    runs = state.get("checker_runs", [])
    iterations = state.get("iteration_history", [])
    results = Counter(run.get("result") for run in runs)
    failures = Counter(
        run.get("failure_class") for run in runs if run.get("result") == "FAIL"
    )
    retries = Counter(run.get("checker") for run in runs)
    stage_runtime: defaultdict[str, float] = defaultdict(float)
    checker_runtime: defaultdict[str, float] = defaultdict(float)
    for run in runs:
        duration = float(run.get("duration_seconds") or 0)
        stage_runtime[str(run.get("stage"))] += duration
        checker_runtime[str(run.get("checker"))] += duration
    resolution_times = [
        float(item.get("duration_seconds") or 0)
        for item in iterations
        if item.get("result") == "PASS"
    ]
    architecture_revisions = sum(
        bool({"architecture", "microarchitecture"} & set(revision.get("change_domain", [])))
        for revision in revisions
    )
    rtl_revisions = sum("rtl" in revision.get("change_domain", []) for revision in revisions)
    return {
        "total_revisions": len(revisions),
        "architecture_revisions": architecture_revisions,
        "rtl_revisions": rtl_revisions,
        "total_checker_runs": len(runs),
        "checker_results": {key: results.get(key, 0) for key in sorted(RUN_RESULTS)},
        "failures_by_class": dict(sorted(failures.items())),
        "retries_per_checker": {
            key: max(value - 1, 0) for key, value in sorted(retries.items())
        },
        "loop_back_cycles": len(iterations),
        "runtime_per_checker_seconds": dict(sorted(checker_runtime.items())),
        "runtime_per_stage_seconds": dict(sorted(stage_runtime.items())),
        "runtime_per_iteration_seconds": {
            item["iteration_id"]: item["duration_seconds"] for item in iterations
        },
        "total_pipeline_runtime_seconds": sum(stage_runtime.values()),
        "average_failure_resolution_seconds": (
            sum(resolution_times) / len(resolution_times) if resolution_times else None
        ),
        "stages_requiring_most_retries": sorted(
            ((key, max(value - 1, 0)) for key, value in retries.items()),
            key=lambda pair: (-pair[1], pair[0]),
        ),
        "most_common_failure_classes": failures.most_common(),
    }


def verify_git_commit(repo: Path, sha: str) -> None:
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{sha}^{{commit}}"], cwd=repo, capture_output=True, text=True
    )
    if result.returncode:
        raise TraceabilityError(f"git commit {sha!r} is not recoverable in {repo}")


def _load_record(path: Path) -> dict[str, Any]:
    record = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(record, dict):
        raise TraceabilityError("record JSON must be an object")
    return record


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=Path("design_state.json"))
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("add-input", "add-feedback", "add-revision", "record-run", "record-iteration"):
        command = sub.add_parser(name)
        command.add_argument("record", type=Path)
    metrics = sub.add_parser("metrics")
    metrics.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    with locked_state(args.state) as state:
        if args.command == "add-input":
            append_input_record(state, _load_record(args.record))
        elif args.command == "add-feedback":
            add_stage0_feedback_request(state, _load_record(args.record))
        elif args.command == "add-revision":
            record = _load_record(args.record)
            verify_git_commit(Path.cwd(), record["git_commit_sha"])
            append_revision(state, record)
        elif args.command == "record-run":
            record_checker_run(state, _load_record(args.record))
        elif args.command == "record-iteration":
            record_iteration(state, _load_record(args.record))
        elif args.command == "metrics":
            result = calculate_metrics(state)
            payload = json.dumps(result, indent=2) + "\n"
            if args.output:
                args.output.write_text(payload, encoding="utf-8")
            else:
                print(payload, end="")
            return 0
        atomic_write(args.state, state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
