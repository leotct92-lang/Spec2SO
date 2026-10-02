# R-Car V4M Downstream Implementation Plan

This artifact separates preparatory work completed from production execution blocked by
missing design or technology collateral.

| Stage | Status | Preparation completed | Exact production blocker |
|---|---|---|---|
| RTL design | BLOCKED | Handoff and black-box boundaries | Authoritative design behavior, RTL/IP rights and clock/reset/interface specifications. |
| Lint | BLOCKED | Checker record template | No product RTL/file list. |
| Functional verification | BLOCKED | Verification matrix | No RTL/models/requirements/coverage targets. |
| Formal | BLOCKED | Property categories identified | No RTL/properties/assumptions. |
| CDC/RDC | BLOCKED | Domain gaps identified | No RTL plus clock/reset/power intent. |
| Logic synthesis | BLOCKED | Scenario constraints identified | No RTL, Liberty, memory views or production SDC. |
| Power/area estimation | WARN | Scenario sensitivity and separation rules | No netlist/activity/PDK/physical evidence; only exploratory envelopes. |
| DFT | BLOCKED | Required collateral inventory | No RTL/netlist, scan/MBIST architecture, ATPG models or targets. |
| Physical design | BLOCKED | Floorplan inputs enumerated | No netlist, LEF, floorplan/package, RC tech or sign-off decks. |
| STA | BLOCKED | Corner/constraint inventory | No netlist, Liberty, SDC, SPEF/RC corners or derates. |
| SoC integration | WARN | Public controllers/board paths inventoried | Complete address/interrupt/pin/clock/reset/security maps and IP contracts absent. |

Open-source tools, if installed, cannot turn absent product sources or proprietary technology
views into sign-off evidence. Future exploratory runs must be explicitly named as such.
