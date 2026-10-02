# R-Car V4M Power and Area Research

## Result

The accessible official source set did not disclose chip idle power, workload power, subsystem
power, peak power, thermal-design power, process/foundry, die dimensions, or die area. The
result is **WARN** for exploratory planning and **BLOCKED** for production power, thermal and
physical sign-off.

## Search record

The sweep covered the Renesas V4M product URL, official Linux BSP, Gray Hawk DTS, official
Yocto layer, V4M/HWUM patch excerpts, board names, SoC identifier `R8A779H0`, accelerator
names, OPP/thermal nodes, package/process/die/power terminology, and R-Car Gen4 family terms.
The product page and general search routes returned HTTP 403; exact accessible commits and the
failure boundary are recorded in `V4M_SOURCE_LEDGER.md`.

## Power separation

| Quantity | Public value | Classification | Disposition |
|---|---:|---|---|
| SoC idle power | UNKNOWN | UNKNOWN | Requires defined state and rail measurement. |
| SoC workload power | UNKNOWN | UNKNOWN | Requires workload, temperature, OPP and rail scope. |
| SoC peak power | UNKNOWN | UNKNOWN | Requires vendor electrical/thermal definition. |
| SoC thermal-design number | UNKNOWN | UNKNOWN | Requires package/thermal collateral. |
| Subsystem power | UNKNOWN | UNKNOWN | Requires domain rail/model data. |
| Gray Hawk board power | UNKNOWN | UNKNOWN | Requires input/rail measurement; would remain board-scoped. |
| Exploratory SoC envelope | 15/25/40 W | ENGINEERING_ASSUMPTION | Sensitivity only; not any row above. |

Board input power includes regulators, DRAM, storage, PHYs, bridges and losses and must never
be relabeled as chip power. A measured workload point is not peak or TDP unless the source
defines it that way.

## Area separation

| Quantity | Public value | Classification | Disposition |
|---|---:|---|---|
| Package dimensions/area | UNKNOWN | UNKNOWN | Requires orderable-part package drawing. |
| Bare-die dimensions | UNKNOWN | UNKNOWN | Requires scaled photo or vendor disclosure. |
| Bare-die area | UNKNOWN | UNKNOWN | Cannot be inferred from package area. |
| Process/foundry | UNKNOWN | UNKNOWN | Software compatible strings do not establish manufacturing. |
| Exploratory area envelope | 180/260/340 mm² | ENGINEERING_ASSUMPTION | Floorplan sensitivity only. |

No public die photograph with a trustworthy scale, package-to-die ratio, transistor count or
floorplan was found in the accessible evidence. Consequently the scenario area is intentionally
not labeled a `DERIVED_ESTIMATE`.

## Exact unblocking evidence

An orderable-part data sheet/package drawing, vendor power definition and measured rail table,
package thermal model, process disclosure, scaled die evidence, and implementation floorplan
are required. PDK/LEF/Liberty/RC data are additionally required for implementation sign-off.
