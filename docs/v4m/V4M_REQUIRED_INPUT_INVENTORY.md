# R-Car V4M Required Input Inventory

Legend: requirement `R`/`O`; missing `NO`, `WEAK`, `YES`; evidence `OD` official disclosed,
`PC` public corroborated, `DE` derived estimate, `EA` engineering assumption, `U` unknown.
Every row is material to at least one enabled Spec2SO stage. `Current value` is normalized;
source IDs resolve in `V4M_SOURCE_LEDGER.md`. Units marked `—` are categorical.

| Field | Definition / acceptable form | Unit/type | Req. | Consumers | Current value | Missing | Evidence | Estimate allowed | Provenance |
|---|---|---|---|---|---|---|---|---|---|
| identity.product | Exact product | string | R | all | R-Car V4M / R8A779H0 | NO | OD | no | S1/S3 |
| use_case | Product role | string[] | R | spec, architecture, verification | ADAS-oriented Linux platform | WEAK | PC | yes | S5; marketing unavailable |
| cpu.architecture | Application ISA/core | enum | R | architecture, firmware, compiler | Arm Cortex-A76 / Armv8.2-A tune | NO | OD | no | S1/S3 |
| cpu.core_count | Application core count | cores/int | R | architecture, verification | 4 | NO | OD | no | S1 |
| cpu.max_frequency | Product maximum | MHz/number | R | perf, power, timing, firmware | UNKNOWN; BSP OPPs 500/1000 | WEAK | U | yes, exploratory | S1 |
| cpu.realtime_family | Real-time CPU type | string | R | safety, firmware | Cortex-R52-class domain exists | WEAK | PC | no | S1 thermal label |
| cpu.realtime_count | Real-time core count | cores/int | R | safety, firmware | UNKNOWN | YES | U | scenario only | final sweep |
| cpu.lockstep | Lockstep topology | object | R | safety, verification | UNKNOWN | YES | U | no | confidential/manual needed |
| cache.l1 | I/D per core | KiB/object | R | perf, area | 64 I + 64 D | NO | OD | no | S4 |
| cache.l2 | Per-core L2 | KiB/int | R | perf, area | 256 | NO | OD | no | S4 |
| cache.l3 | Cluster L3 | KiB/int | R | perf, area | 512 | NO | OD | no | S4 |
| gpu.architecture | Public GPU identity | string | O | graphics, integration | Renesas GSX | WEAK | OD | no | S1/S3 |
| gpu.performance | Execution resources/rate | object | O | perf, power | UNKNOWN | YES | U | yes | product brief needed |
| ai.topology | Accelerator instances | object | R | architecture, verification | 2 IMP, 4 CVE, 1 CNN, 2 VDSP domains exposed | NO | OD | no | S7 |
| ai.peak_tops | Peak AI throughput with precision | TOPS/number | R | architecture, perf | UNKNOWN | YES | U | yes | official brief needed |
| ai.precision | INT8/FP16/etc. basis | enum[] | R | perf, verification | UNKNOWN | YES | U | no | accelerator manual needed |
| memory.onchip_sram | Total/banked SRAM | bytes/object | R | architecture, firmware, DFT | UNKNOWN | YES | U | yes | HWUM/implementation needed |
| memory.dram_type | Supported DRAM standard | enum | R | architecture, SI, firmware | UNKNOWN | YES | U | yes | datasheet needed |
| memory.channels_width | Channels and bus width | object | R | perf, PD, package | UNKNOWN | YES | U | yes | datasheet/package needed |
| memory.rate | Supported data rate | MT/s/number | R | perf, SI | UNKNOWN | YES | U | yes | datasheet needed |
| memory.bandwidth | Sustained/theoretical context | GB/s/number | R | perf, camera, AI | 17.1/25.6/34.1 scenario | WEAK | EA | yes | V4M_DERIVED_ESTIMATES |
| memory.board_capacity | Gray Hawk fitted capacity | GiB/number | O | software/integration | about 8; 7.875 non-secure + 128 MiB secure | NO | DE | yes | S2 address arithmetic |
| memory.ecc | Coverage/granularity | object | R | safety, verification | UNKNOWN | YES | U | no | manual needed |
| interconnect.fabric | Topology/QoS/coherency | object | R | architecture, perf | QoS + IPMMU existence only | WEAK | PC | yes | S1 |
| camera.csi2_receivers | CSI-2 controller count | count/int | R | integration, verification | 2 | NO | OD | no | S1 |
| camera.inputs_board | Gray Hawk camera links | count/int | O | integration | 8 serializer links | NO | OD | no | S2 |
| camera.vin_instances | Video input instances | count/int | O | architecture | 16 nodes | NO | OD | no | S1 |
| camera.pixel_throughput | Aggregate/context | Gpixel/s/number | R | perf, power | UNKNOWN | YES | U | yes | product brief needed |
| isp.instances | ISP block count | count/int | R | architecture, integration | 2 | NO | OD | no | S1 |
| isp.throughput | Aggregate/context | Gpixel/s/number | R | perf | UNKNOWN | YES | U | yes | manual/brief needed |
| video.codecs | Formats/resolution/streams | object | O | architecture, software | UNKNOWN | YES | U | yes | multimedia docs needed |
| display | Controllers/outputs/limits | object | O | integration | 1 DU, 1 VSP, 1 MIPI DSI node | WEAK | OD | no | S1/S2 |
| pcie | Count/generation/lanes/modes | object | O | integration | 1 controller; RC+EP; gen/lanes UNKNOWN | WEAK | OD | no | S1 |
| ethernet | Controller count/rates/TSN | object | O | integration | 3 AVB controllers; exact rates UNKNOWN | WEAK | OD | no | S1/S2 |
| can_fd | Channel count | channels/int | O | integration, firmware | 4 | NO | OD | no | S1/S2 |
| lin | Channel count | channels/int | O | integration | UNKNOWN | YES | U | no | manual needed |
| flexray | Channel count/capability if implemented | channels/int | O | integration, safety | UNKNOWN | YES | U | no | manual/package data needed |
| usb | Controllers/modes/rates | object | O | integration | UNKNOWN in inspected DTS | YES | U | no | manual needed |
| storage | eMMC/flash/NVMe | object | O | firmware | 8-bit eMMC HS200/400 board; RPC; NVMe tools | WEAK | OD | no | S1/S2/S5 |
| clock.tree | Sources/PLLs/domains | object | R | RTL, CDC, synthesis, STA | Public module clocks only; topology UNKNOWN | YES | U | no | manual/constraints needed |
| reset.tree | Reset domains/sequencing | object | R | RTL, CDC/RDC, verification | Controller/reset IDs only; sequencing UNKNOWN | YES | U | no | manual needed |
| dvfs.opps | Product OPP/transition policy | object | R | power, firmware | BSP 500/1000 MHz @0.825 V | WEAK | OD | yes | S1; not max claim |
| voltage.rails | Min/nom/max by domain | V/object | R | power, PD, STA | CPU BSP OPP 0.825 V only | YES | OD | yes | S1 |
| power.soc_idle | Chip idle context | W/number | R | power, thermal | UNKNOWN | YES | U | yes | measurement/datasheet |
| power.soc_typical | Workload-defined SoC | W/number | R | power, thermal | 25 nominal exploratory | WEAK | EA | yes | scenario only |
| power.soc_peak_tdp | Peak/TDP distinction | W/number | R | power, thermal, PD | 15/25/40 scenario bounds; not TDP | WEAK | EA | yes | scenario only |
| power.subsystems | CPU/GPU/AI/ISP/IO | W/object | O | power optimization | UNKNOWN | YES | U | yes | power model needed |
| power.board | Board rail/input context | W/object | O | lab planning | UNKNOWN | YES | U | yes | board measurement needed |
| thermal.limits | Tj/ambient/Rθ/package | object | R | thermal, PD | 85/105/125 °C scenarios only | WEAK | EA | yes | package data needed |
| process.node_foundry | Process/node/variants | nm/string | R | area, power, PD | 7/7/12 nm scenarios; foundry UNKNOWN | WEAK | EA | yes | manufacturing disclosure needed |
| die.dimensions_area | Bare die dimensions/area | mm/mm² | R | area, PD | 180/260/340 mm² scenarios | WEAK | DE | yes | no public die photo/scale found |
| package | Orderable package/dimensions/balls | object | R | PD, SI/PI, integration | UNKNOWN | YES | U | no | package drawing needed |
| safety.iso26262 | Certification/scope | object | R | safety, verification | UNKNOWN in accessible evidence | YES | U | no | safety manual/certificate needed |
| safety.diagnostics | Coverage/latent metrics | object | R | verification, DFT | UNKNOWN | YES | U | no | safety manual needed |
| security.boot | Secure boot chain/policy | object | R | security, firmware | ATF+OP-TEE public; production chain UNKNOWN | WEAK | OD | no | S1/S5/S6 |
| security.hsm_rot | HSM/root-of-trust/key storage | object | R | security | UNKNOWN | YES | U | no | security manual needed |
| virtualization | EL2/hypervisor/products | object | O | software, safety | Armv8.2/GICv3/IPMMU primitives; product UNKNOWN | WEAK | PC | no | S1/S3 |
| memory_protection | IOMMU/firewalls/access | object | R | security, integration | multiple IPMMUs; firewall details UNKNOWN | WEAK | OD | no | S1 |
| software.linux_yocto | Supported BSP | object | R | firmware | Linux/Yocto scarthgap Gray Hawk | NO | OD | no | S3/S5 |
| software.autosar | Vendor/package/version | object | O | firmware/safety | UNKNOWN | YES | U | no | official ecosystem data needed |
| software.hypervisor | Supported products | string[] | O | virtualization | UNKNOWN | YES | U | no | partner docs needed |
| software.sdk_toolchain | SDK/compiler | object | R | compiler, firmware | Poky GCC AArch64 SDK | NO | OD | no | S3 |
| software.cv_stack | AI/CV libraries | object | O | AI/software | OpenCV SDK image; proprietary accelerator stack UNKNOWN | WEAK | OD | no | S5 |
| physical.floorplan | Die/core/IO/macro constraints | object | R | PD | UNKNOWN/proprietary | YES | U | no | floorplan + LEF needed |
| physical.pdk_views | PDK/LEF/RC/DRC/LVS | files | R | synthesis, PD, STA | unavailable | YES | U | no | proprietary collateral |
| timing.sdc | Clocks/IO/exceptions/modes | files | R | synthesis, STA | unavailable | YES | U | no | implementation SDC needed |
| timing.liberty | Corner libraries | files | R | synthesis, STA | unavailable | YES | U | no | characterized .lib needed |
| dft.requirements | Scan/modes/compression/ATPG | object | R | DFT | generic scenario only | YES | EA | yes, planning | DFT owner/manual needed |
| verification.plan | Requirements/assertions/coverage | object | R | verification/formal | public-feature plan only | WEAK | EA | yes, planning | normalized public spec |
| integration.address_map | Complete non-confidential map | object | R | SoC integration, firmware | DTS-visible subset only | WEAK | OD | no | S1; HWUM needed |
| package.si_pi_models | IBIS/S-parameter/rail models | files | R | integration/sign-off | unavailable | YES | U | no | proprietary models |

UNKNOWN is used only after the accessible-source sweep documented in the source ledger. Rows
with engineering scenarios support exploration, never real production sign-off.
