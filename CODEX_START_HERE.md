# CODEX START HERE — Spec2SO Framework Upgrade + R-Car V4M End-to-End

> **Canonical restart / continuation instruction for Codex.**
>
> This file is the single source of truth for resuming this work from GitHub.
> When this file conflicts with older task packets, prompts, or chat history, **this file wins**.
> Important user feedback must be reflected into the reusable repository framework, not left only in chat.

## 0. Current handoff

Repository: `leotct92-lang/Spec2SO`

Working baseline branch: `chatgpt-enterprise-pilot`

Existing V4M packet:
`docs/V4M_CODEX_TASK_PACKET.md`

Verified handoff commit containing that packet:
`20c9b449e6eb8a23add64b970739bb9bcb9084e6`

Before doing new work:

1. Inspect the entire repository.
2. Read this file completely.
3. Read `docs/V4M_CODEX_TASK_PACKET.md` completely.
4. Inspect current Git branch, HEAD, working tree, open branches/PRs, and latest state artifacts.
5. Inspect all pipeline/domain agents, skills, orchestrators, schemas, tests, validators, state-management logic, loop-back rules, fix-request logic, and plugin registrations.
6. Resume from the latest verified repository state. Do not redo useful completed work without a reason.
7. If chat history is unavailable, reconstruct project state from GitHub and repository artifacts.

## 1. Governing rule: user feedback must change the repo

The requirements below are **not one-off manual instructions only for R-Car V4M**.

Implement them as reusable standard behavior of Spec2SO by updating the actual canonical repository components where appropriate:

- agents
- skills
- orchestrators
- shared workflow sections
- schemas
- state-management logic
- validators
- tests
- examples
- documentation
- plugin registrations

If some files are generated from canonical shared templates, update the canonical source rather than patching generated copies only.

Do not merely document a desired process. Implement, test, and use it.

---

# PART A — STANDARD STAGE 0

## 2. Add reusable Stage 0

Create a mandatory reusable capability:

`Input Reconstruction & Evidence Qualification`

The intended standard flow becomes:

`Input Reconstruction & Evidence Qualification`
→ `Product/System Specification`
→ `Architecture Evaluation`
→ `Microarchitecture`
→ `RTL`
→ `Verification`
→ `Formal`
→ `Synthesis`
→ `DFT`
→ `Physical Design`
→ `STA`
→ `SoC Integration`
→ firmware/software/FPGA planning where applicable.

It must be generic and reusable for future projects, not hard-coded for V4M.

## 3. Discover all required inputs

Stage 0 must scan the whole repository and determine every input required or materially useful by downstream stages.

Inspect at least:

- schemas
- templates
- examples
- validators
- stage gates
- agents
- skills
- orchestrators
- design state
- architecture
- microarchitecture
- RTL
- verification
- formal
- CDC/RDC
- synthesis
- DFT
- PD
- STA
- integration
- firmware/software
- tests
- scripts

Build a complete required-input inventory.

For each field record:

- field name
- definition
- unit
- datatype
- required/optional
- consuming stage(s)
- current value
- missing status
- evidence status
- whether estimation is allowed
- acceptable form/range/bounds
- provenance
- confidence
- usage classification

Do not assume the supplied product spec is complete.

## 4. Active research and evidence qualification

When a required input is missing or weakly supported, Stage 0 must proactively research it.

Prioritize:

1. original manufacturer documentation
2. official product pages
3. datasheets
4. public manuals/manual excerpts
5. application notes
6. official presentations
7. evaluation-board documentation
8. SDK/BSP/Linux/Yocto documentation
9. partner documentation
10. foundry/IP/EDA ecosystem disclosures
11. standards documentation
12. automotive OEM/Tier-1 public material
13. conference presentations
14. academic papers
15. independent semiconductor analysis
16. teardown/die analysis
17. reputable engineering publications
18. related-product evidence
19. engineering derivation

Do not stop after one failed search. Try alternate terminology, subsystem names, package identifiers, related products, board/BSP material, conference material, partner disclosures, and credible engineering sources.

## 5. Evidence classes

Every material technical input must be classified as exactly one of:

- `OFFICIAL_DISCLOSED`
- `PUBLIC_CORROBORATED`
- `DERIVED_ESTIMATE`
- `ENGINEERING_ASSUMPTION`
- `UNKNOWN`

Every important numeric value must preserve enough provenance to answer:

`Where did this exact input value come from?`

Record where applicable:

- value
- unit
- source
- URL/reference
- source organization
- document title
- page/section
- publication/revision date
- retrieval date
- evidence classification
- confidence: HIGH / MEDIUM / LOW
- derivation method
- uncertainty
- lower bound
- upper bound
- usage classification:
  - `HARD_CONSTRAINT`
  - `SOFT_CONSTRAINT`
  - `EXPLORATORY_ONLY`

## 6. Missing-input resolution policy

Do not immediately leave a required field blank just because an official value is unavailable.

Attempt in order:

1. additional primary-source search
2. independent corroboration
3. related-family evidence
4. engineering derivation
5. defensible bounded range
6. scenario construction
7. explicit engineering assumption
8. `UNKNOWN` only as final fallback

Never present an estimate or assumption as an official specification.

This rule **supersedes any older instruction that forced missing public power/area or other fields to remain null**. Bounded engineering estimates are allowed when clearly classified and never misrepresented as official or production sign-off data.

## 7. Scenario analysis

For uncertain critical parameters support at least:

- `CONSERVATIVE`
- `NOMINAL_EXPLORATORY`
- `AGGRESSIVE`

At minimum support scenarios where relevant for:

- power
- area
- process
- frequency
- voltage
- memory bandwidth
- thermal
- utilization
- timing margin

## 8. Cross-parameter consistency

Check reconstructed inputs against one another and report contradictions.

Examples:

- TOPS vs accelerator architecture/frequency
- compute throughput vs memory bandwidth
- ISP throughput vs camera requirements
- power vs process/frequency
- area vs process/IP assumptions
- thermal vs power
- clock vs interface limits
- channel count vs bandwidth

Resolve inconsistencies where defensible, otherwise preserve the uncertainty explicitly.

## 9. Active Stage-0 feedback loop

Stage 0 is not a one-time pre-processing step.

When any downstream stage discovers a missing or weak constraint:

`Downstream stage`
→ missing input detected
→ invoke Stage 0
→ research/derive/classify
→ update normalized spec
→ update provenance
→ rerun affected stage
→ continue pipeline

Integrate this into actual pipeline behavior.

---

# PART B — DESIGN REVISION & VERIFICATION TRACEABILITY

## 10. Add reusable traceability capability

Create a reusable capability:

`Design Revision & Verification Traceability`

Preserve compatibility with existing state constructs where possible, including:

- `history[]`
- `fix_requests[]`
- `archive_fix_requests[]`
- `pipeline_session_id`
- `cross_domain_iteration_count`
- `pending_approval`

Enhance existing mechanisms instead of replacing them unnecessarily.

## 11. Revision IDs

Every meaningful released engineering state must have a unique revision ID, for example:

- `REV-0001`
- `REV-0002`
- `REV-0003`

Create a new revision for meaningful changes to areas such as:

- architecture
- microarchitecture
- RTL
- constraints
- interfaces
- clock/reset
- memory architecture
- verification-relevant implementation
- synthesis-driven RTL
- timing-driven design
- power/area-driven architecture
- formal fixes
- CDC/RDC fixes
- DFT-related logic
- PD-driven logical changes
- STA-driven architecture/RTL changes

## 12. Git checkpoint for every meaningful revision

A released engineering revision must never exist only as overwritten workspace files.

For each meaningful revision:

1. save the changed files
2. create a Git commit
3. record the commit SHA
4. record parent revision
5. record reason for revision
6. record triggering failure/checker when applicable
7. record affected domains/files
8. preserve previous revision history

Git is the recoverable snapshot of every meaningful engineering revision.

## 13. Revision metadata

Implement repository-native machine-readable revision storage, for example in `design_state.revisions[]` or an equivalent dedicated artifact.

Each revision should capture information equivalent to:

```json
{
  "revision_id": "REV-0007",
  "parent_revision_id": "REV-0006",
  "git_commit_sha": "...",
  "created_at": "...",
  "created_by": "...",
  "change_domain": ["architecture", "rtl"],
  "trigger_type": "verification_failure",
  "trigger_id": "FR-0012",
  "trigger_stage": "functional_verification",
  "trigger_checker": "verification-orchestrator",
  "trigger_failure_class": "functional",
  "trigger_summary": "...",
  "change_summary": "...",
  "affected_files": ["..."],
  "status": "ACTIVE|SUPERSEDED|FINAL"
}
```

## 14. Record every checker/tool run

Every checker/tool execution against a design revision must be traceable.

Include where applicable:

- compile
- lint
- functional simulation
- functional verification
- formal verification
- CDC
- RDC
- synthesis
- timing
- power
- area
- DFT
- physical design
- STA
- integration tests

Each run should record:

- run ID
- revision ID
- pipeline session ID
- stage
- checker/tool
- tool version
- command/config
- relevant constraints
- start time
- end time
- duration
- `PASS|FAIL|WARN|BLOCKED`
- failure class
- key metrics
- summary
- log path
- report path
- fix-request ID when applicable

## 15. Failure → fix → revision mapping

For each checker failure:

1. record the failed run
2. identify the failed revision
3. create/update a fix request
4. record failure class
5. record suspected/confirmed root cause
6. apply the fix
7. create a new revision
8. Git commit the new revision
9. link fixing revision to original failure
10. rerun relevant checker(s)
11. record rerun results

The history must visibly support chains such as:

`REV-0004`
→ `RUN-0021 verification FAIL`
→ `FR-0008`
→ RTL fix
→ `REV-0005`
→ `RUN-0024 verification PASS`

and cross-domain cases such as:

`REV-0005`
→ synthesis FAIL
→ fix request
→ architecture/RTL refinement
→ `REV-0006`
→ synthesis PASS

## 16. Bidirectional traceability

The system must answer both:

`For this revision, what checker runs executed and what were their results?`

and:

`For this failure, which revision failed, what fix was applied, and which later revision resolved it?`

Maintain links for:

- revision → checker runs
- run → revision
- failure → failed revision
- failure → fixing/resolving revision
- fix request → failed revision
- fix request → resolved revision

## 17. Iteration records

Every loop-back cycle must have an iteration record including:

- iteration ID
- pipeline session ID
- input revision
- failed run
- fix request
- output revision
- rerun ID
- result
- start time
- end time
- duration

A full fail/fix/rerun cycle must be visible as one traceable iteration.

## 18. Architecture backtracking

Do not assume every checker failure is an RTL-only problem.

When evidence points to architecture or microarchitecture:

checker FAIL
→ root-cause analysis
→ architecture/microarchitecture loop-back
→ new architecture revision
→ update/regenerate RTL
→ new RTL revision where appropriate
→ rerun checker

Record relationships between architecture revisions and RTL revisions.

## 19. Progress and runtime metrics

Track at least:

- total revisions
- architecture revisions
- RTL revisions
- total checker runs
- PASS count
- FAIL count
- WARN count
- BLOCKED count
- failures by class
- retries per checker
- loop-back cycles
- runtime per checker
- runtime per stage
- runtime per iteration
- total pipeline runtime
- average failure-resolution time
- stages requiring most retries
- most common failure classes

## 20. Human-readable and machine-readable reports

Create repository-native equivalents of:

- `docs/revisions/REVISION_PROGRESS.md`
- `docs/revisions/FAILURE_TO_REVISION_MATRIX.md`
- `docs/revisions/PIPELINE_EXECUTION_SUMMARY.md`

Maintain machine-readable equivalents of:

- revision history
- checker runs
- iteration history

Historical records are immutable except for additive resolution/status links. Do not silently overwrite past evidence.

---

# PART C — FRAMEWORK INTEGRATION & TESTS

## 21. Update the actual reusable framework

Inspect and modify as needed:

- pipeline orchestrator
- architecture orchestrator and skill
- RTL orchestrator and skill
- verification orchestrator and skill
- formal orchestrator and skill
- synthesis orchestrator and skill
- DFT orchestrator and skill
- PD orchestrator and skill
- STA orchestrator and skill
- SoC integration orchestrator and skill
- shared state/schema definitions
- validators
- tests
- examples
- shared sections
- plugin registrations

If repository paths differ from older task descriptions, follow the current repository structure and conventions.

## 22. Required validation

Add/update tests demonstrating at least:

1. Stage 0 detects missing input
2. official vs estimate classification remains distinct
3. provenance is preserved
4. downstream constraint gaps can invoke Stage 0
5. verification failure creates a fix request
6. a fix creates a new revision
7. revision gets Git/state traceability
8. checker rerun points to the new revision
9. failed revision remains historically visible
10. fixing revision links back to the failure
11. loop duration is recorded
12. cross-domain iteration cap still works
13. existing design-state compatibility is preserved
14. pipeline can still converge
15. historical evidence cannot be silently overwritten

Run all available relevant tests and fix regressions.

---

# PART D — APPLY THE UPGRADED FLOW TO R-CAR V4M

## 23. Do not stop after framework work

After implementing and validating the framework upgrades, immediately apply the new flow to Renesas R-Car V4M.

Use existing V4M artifacts and continue from the latest verified repo state.

Do not restart useful completed work unnecessarily.

## 24. V4M input reconstruction scope

Determine **all** inputs Spec2SO requires, not only power and area.

Research and reconstruct where relevant:

- intended use cases
- CPU architecture
- CPU core count
- CPU frequency
- real-time/safety CPUs
- lockstep
- GPU
- AI accelerators
- TOPS
- AI precision
- caches
- SRAM
- DRAM type
- DRAM channels
- memory rate
- memory bandwidth
- ECC
- interconnect
- ISP
- camera inputs/count
- pixel throughput
- video
- display
- PCIe
- Ethernet
- CAN/CAN-FD
- LIN
- FlexRay where applicable
- USB
- storage
- CSI/DSI
- clock/reset
- PLL
- DVFS
- voltage
- power
- subsystem power
- total SoC power
- board power
- thermal
- process node
- foundry clues
- die dimensions
- die area
- package
- package dimensions
- safety
- ISO 26262 / ASIL claims
- diagnostics
- security
- secure boot
- HSM
- root of trust
- virtualization
- memory protection
- OS support
- Linux
- AUTOSAR
- hypervisors
- SDK
- BSP
- compiler/toolchain
- software stack
- physical constraints
- timing constraints
- DFT constraints
- verification constraints
- integration constraints

## 25. V4M source strategy

Search reasonably exhaustively and prefer:

1. Renesas official product pages
2. Renesas datasheets
3. public Renesas manuals/manual excerpts
4. Renesas application notes
5. Renesas technical presentations
6. Renesas press releases
7. evaluation-board documentation
8. R-Car SDK/BSP/Linux/Yocto documentation
9. Renesas partner documentation
10. foundry/IP/EDA ecosystem disclosures
11. automotive OEM/Tier-1 public material
12. conference papers
13. academic papers
14. independent semiconductor analysis
15. public teardown/die analysis
16. technical journalism
17. credible engineering sites
18. closely related R-Car Gen4 devices

Do not stop at the main V4M product page.

## 26. Related-device policy

Related products may be used only for comparison or bounded inference.

For each use:

- identify the exact related product
- explain relevance
- explain differences
- do not copy values directly as V4M facts
- classify the resulting value correctly as estimate/assumption

## 27. Power rules

Always distinguish:

- chip power
- subsystem power
- board power
- idle
- typical workload
- peak
- thermal-design number

Never use board power as SoC power.

Never use workload power as worst-case power unless evidence supports it.

## 28. Area rules

Research where possible:

- die photos
- die dimensions
- process node
- package
- transistor clues
- public floorplan/micrograph clues
- related Gen4 implementation evidence

Never use package area as die area.

Calculated die/logic area must be clearly labeled `DERIVED_ESTIMATE`.

## 29. Required V4M artifacts

Create/update at least:

- `docs/v4m/V4M_REQUIRED_INPUT_INVENTORY.md`
- `docs/v4m/V4M_PUBLIC_PRODUCT_SPEC.md`
- `docs/v4m/V4M_PUBLIC_PRODUCT_SPEC.json`
- `docs/v4m/V4M_SOURCE_LEDGER.md`
- `docs/v4m/V4M_GAPS_AND_ASSUMPTIONS.md`
- `docs/v4m/V4M_TRACEABILITY_MATRIX.md`
- `docs/v4m/V4M_POWER_AREA_RESEARCH.md`
- `docs/v4m/V4M_DERIVED_ESTIMATES.md`
- `docs/v4m/V4M_COMPARABLE_DEVICES.md`
- `docs/v4m/V4M_SENSITIVITY_SCENARIOS.md`
- `docs/v4m/V4M_INPUT_COMPLETENESS_REPORT.md`
- `docs/v4m/END_TO_END_STATUS.md`
- `docs/PROJECT_STATUS.md`

Use repository-native equivalent paths if there is a clearly better convention.

## 30. Input completeness gate

Classify V4M inputs as:

- `AVAILABLE_OFFICIAL`
- `AVAILABLE_CORROBORATED`
- `AVAILABLE_ESTIMATED`
- `ENGINEERING_ASSUMPTION`
- `UNKNOWN`

Report completeness separately for:

- functional
- compute
- performance
- memory
- interconnect
- interfaces
- clock/reset
- power
- area
- thermal
- physical
- safety
- security
- software
- verification
- DFT
- integration

Do not wait for 100% official information. Continue using clearly marked, defensible exploratory values where appropriate.

## 31. Execute V4M end-to-end

After input reconstruction, continue through every executable stage:

Specification
→ Architecture Evaluation
→ Architecture Trade-off
→ Microarchitecture
→ RTL handoff
→ RTL Design
→ Lint
→ Functional Verification
→ Formal Verification
→ CDC/RDC where supported
→ Logic Synthesis
→ Power/Area Estimation
→ DFT
→ Physical Design
→ STA
→ SoC Integration
→ Firmware/Software Planning
→ FPGA/Prototyping Planning where applicable

Use the upgraded Stage-0 and revision-traceability mechanisms throughout.

Every meaningful design revision must have a recoverable Git commit.

Every checker run must map to the revision it checked.

## 32. Proprietary-data policy

Missing proprietary data must not terminate unrelated work.

Examples:

- confidential Renesas User Manual details
- PDK
- Liberty
- LEF
- RC technology files
- memory compiler views
- proprietary IP views
- production timing corners
- voltage tables
- confidential thermal data
- DFT collateral
- package SI/PI models
- unavailable licensed EDA tools

When proprietary input is missing:

1. finish public research
2. create all preparatory artifacts
3. use explicitly labeled exploratory assumptions where defensible
4. execute every independent stage possible
5. mark only the affected stages `BLOCKED` or `ESCALATE`
6. record the exact missing input needed to unblock

Never fabricate production sign-off data.

## 33. Stage statuses

Use only:

- `PASS`
- `WARN`
- `BLOCKED`
- `ESCALATE`
- `NOT_EXECUTED`

Never claim production-grade sign-off unless actual required tools and real technology collateral were available.

Generic/open-tool results must be explicitly labeled exploratory.

---

# PART E — AUTONOMY, CONTINUITY, AND RECOVERY

## 34. Autonomous execution

Do not ask routine implementation questions.

Do not stop after:

- documentation
- framework changes
- research
- architecture
- a single checker pass/fail
- discovery that some inputs are estimated

Make the most defensible engineering decision supported by available evidence and continue.

Escalate only when:

- a genuine product/business decision is required
- continuing would require inventing a fundamental design fact
- proprietary credentials/input are absolutely required
- an irreversible/destructive external action requires approval

Otherwise proceed autonomously.

## 35. Final UNKNOWN / ASSUMPTION sweep

Before declaring completion, perform another research pass for remaining:

- `UNKNOWN`
- `ENGINEERING_ASSUMPTION`

Search alternate terminology, related chips, subsystem names, partner documentation, conference material, academic papers, board/BSP information, and industry analysis.

If stronger evidence is found:

- update the input
- update provenance
- update confidence
- update normalized spec
- rerun affected stages

## 36. Business continuity

All important knowledge must live in GitHub, not only in Codex conversation history.

Maintain `docs/PROJECT_STATUS.md` with at least:

- current branch
- latest verified commit
- current/final revision ID
- completed stages
- work in progress
- blockers
- required proprietary inputs
- next recommended action
- latest relevant checker run IDs
- latest pipeline session ID

Keep `design_state.json`, revision history, checker-run history, iteration history, V4M status, and repository documentation current.

The repository must contain enough information that a completely new Codex account/environment can reconnect to GitHub, read this file and the status artifacts, reconstruct the state, and continue from the latest verified revision without relying on chat history.

## 37. Future user feedback rule

Whenever the user gives a new process/flow requirement:

1. determine whether it is project-specific or framework-generic
2. if framework-generic, update the reusable agents/skills/orchestrators/schemas/tests
3. update this `CODEX_START_HERE.md` if it changes canonical restart behavior
4. update project/status artifacts
5. commit the change
6. continue execution

Do not leave important workflow changes only inside a Codex conversation.

---

# PART F — FINAL REPORT AND STOPPING CONDITION

## 38. Final executive report

At the coherent end state report at least:

1. all required inputs
2. official inputs
3. corroborated inputs
4. derived estimates
5. engineering assumptions
6. remaining unknowns
7. total architecture revisions
8. total RTL revisions
9. total engineering revisions
10. total checker runs
11. PASS/FAIL/WARN/BLOCKED counts
12. most common failure classes
13. failure → fixing revision mapping
14. total loop-back cycles
15. runtime per iteration
16. runtime per stage
17. total pipeline runtime
18. final revision ID
19. final Git commit SHA
20. final PASS/WARN/BLOCKED matrix
21. remaining proprietary inputs required for real production sign-off

## 39. Completion condition

Do not declare the task complete until all applicable items below are true:

1. Stage 0 `Input Reconstruction & Evidence Qualification` exists as reusable repo behavior.
2. Stage 0 is integrated into the actual pipeline.
3. `Design Revision & Verification Traceability` is implemented.
4. Revision/checker/failure mapping is integrated into orchestrators/state.
5. Tests validate the new behaviors.
6. Existing flow compatibility is preserved.
7. All V4M-required inputs are identified.
8. Missing inputs have been actively researched.
9. Provenance exists for all material inputs.
10. Estimates/assumptions are clearly marked.
11. V4M Product/System Specification is usable.
12. Architecture evaluation has run.
13. Every executable downstream stage has run.
14. Blocked stages have exact documented blockers.
15. Every meaningful revision has a recoverable Git commit.
16. Every checker run maps to a revision.
17. Every failure maps to the failing and fixing/resolving revisions.
18. Loop/runtime metrics exist.
19. `design_state.json` and related state artifacts are current.
20. `docs/v4m/END_TO_END_STATUS.md` is current.
21. `docs/PROJECT_STATUS.md` is current.
22. Tests/validation have run.
23. Changes are committed logically.
24. A coherent PR is opened toward the fork default branch when appropriate.

Do not merely describe how the upgraded process should work.

**Implement the framework changes, validate them, then use the upgraded framework to execute the R-Car V4M project end-to-end.**

## 40. Codex resume command

When Codex receives a short instruction such as:

`Read CODEX_START_HERE.md and continue autonomously from the latest verified repo state.`

it must perform the restart/recovery procedure in Section 0 and continue from the next unresolved step without waiting for routine confirmation.
