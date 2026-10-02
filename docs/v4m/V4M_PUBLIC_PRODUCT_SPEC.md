# R-Car V4M Public Product/System Specification

Status: **WARN — usable for exploratory architecture and software planning; not production
implementation/sign-off**. Target identity is Renesas R-Car V4M / R8A779H0, with Gray Hawk as
the official public BSP board. This specification deliberately separates SoC capability,
board implementation, public software exposure, estimates, and unknown proprietary details.

## Qualified public baseline

| Domain | Qualified statement | Evidence / use |
|---|---|---|
| CPU | Four Arm Cortex-A76 application CPUs are instantiated in one public cluster. | OFFICIAL_DISCLOSED, S1, HARD_CONSTRAINT for the public architecture model. |
| CPU frequency/voltage | The inspected BSP exposes 500 MHz and 1,000 MHz OPPs at 0.825 V. This is a software table, not proof of the product maximum. | OFFICIAL_DISCLOSED, S1, SOFT_CONSTRAINT. |
| Cache | Per A76: 64 KiB I + 64 KiB D L1 and 256 KiB L2; cluster L3 512 KiB. | OFFICIAL_DISCLOSED, S4, HARD_CONSTRAINT for public model. |
| Real-time CPU | A CR52 thermal zone proves an R52-class subsystem exists, but public accessible code inspected here does not prove core count, lockstep topology, cache, or frequency. | PUBLIC_CORROBORATED for existence; other fields UNKNOWN. |
| GPU | A Renesas GSX GPU node and binary-driver recipes exist. Public code does not disclose shader count or peak rate. | OFFICIAL_DISCLOSED existence, S1/S3. |
| AI/CV | Public UIO topology exposes 2 IMP cores, 4 CVE blocks, 1 CNN block, and 2 VDSP domains. Peak TOPS/precision are not established by these files. | OFFICIAL_DISCLOSED topology, S7; performance UNKNOWN. |
| Camera/ISP | 2 CSI-2 receivers, 16 VIN nodes, and 2 ISP nodes are represented. Gray Hawk routes eight serializer camera links into two CSI receivers. | OFFICIAL_DISCLOSED, S1/S2. |
| Display | One display unit, one VSP, and one MIPI DSI encoder are represented; Gray Hawk uses a DSI bridge. | OFFICIAL_DISCLOSED, S1/S2. |
| Ethernet | Three Ethernet AVB/TSN-class controller nodes; Gray Hawk enables three PHYs. Exact line-rate modes require the relevant manual/PHY design. | OFFICIAL_DISCLOSED count, S1/S2. |
| CAN | One CAN-FD controller with four channels; Gray Hawk exposes four CAN-FD pin groups. | OFFICIAL_DISCLOSED, S1/S2. |
| PCIe | One Gen4-family R-Car PCIe controller with root-complex and endpoint modes in public DTS. Lane count/rate is not inferred. | OFFICIAL_DISCLOSED existence/modes, S1. |
| Storage | One 8-bit SDHI/eMMC interface; Gray Hawk enables HS200/HS400 at 1.8 V. RPC flash and NVMe tooling are also present. | OFFICIAL_DISCLOSED board/software support, S1/S2/S5. |
| Memory capacity | Gray Hawk Linux map exposes 7.875 GiB non-secure DRAM plus a noted first 128 MiB secure area, consistent with 8 GiB fitted memory. This is board capacity, not a V4M controller maximum. | DERIVED_ESTIMATE from S2 address ranges, SOFT_CONSTRAINT. |
| Security | PSCI/SMC, Arm Trusted Firmware, OP-TEE, and mbedTLS integration are public. Secure-boot/HSM/root-of-trust production configuration is not proven. | OFFICIAL_DISCLOSED software support, S1/S5/S6. |
| Virtualization/protection | Armv8.2-A tuning, GICv3 and multiple IPMMUs are public; a specific production hypervisor is not established. | OFFICIAL_DISCLOSED primitives, S1/S3. |
| Software | Renesas Yocto layer supports Gray Hawk, Linux kernel/DT, Poky GCC AArch64 SDK, OpenCV SDK, OP-TEE, and PCIe/NVMe utilities. | OFFICIAL_DISCLOSED, S3/S5/S6. |
| Thermal | Separate public thermal zones exist for CA76 and CR52 domains. Limits and package thermal resistance are not public in inspected evidence. | OFFICIAL_DISCLOSED sensor topology, S1. |

## Inputs not established as official facts

Peak TOPS and precision, product-maximum CPU/R52/GPU/accelerator clocks, SRAM totals, DRAM
type/channels/rate/controller maximum, ECC topology, internal interconnect widths/QoS, ISP
pixel/s, video codecs/rates, USB/LIN/FlexRay counts, PLL/DVFS tables, SoC/subsystem/idle/peak/TDP power,
process/foundry, die dimensions/area, package/orderable-part dimensions, safety certification
scope/ASIL allocation/diagnostics, production secure boot/HSM/roots, AUTOSAR/hypervisor product
support, and all production physical/timing/DFT/verification constraints remain assumptions or
UNKNOWN as detailed in the inventory.

## Power and area discipline

No board power is relabeled as chip power. No workload figure is relabeled as peak or TDP. No
package dimension is relabeled as die size. Scenario values are engineering assumptions for
sensitivity analysis only and cannot satisfy production sign-off gates.
