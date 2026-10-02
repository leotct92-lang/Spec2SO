# R-Car V4M Firmware, Software and FPGA/Prototype Plan

Status: **WARN** — public BSP planning is actionable; production enablement needs controlled
documentation and hardware access.

## Firmware/software continuity

- Reproduce the Gray Hawk build from the pinned official `meta-renesas` revision and matching
  Linux BSP branch in an isolated build environment.
- Preserve the public DTS as the initial device inventory; treat it as a software view, not the
  complete hardware contract.
- Boot chain planning: ATF → OP-TEE integration → Linux, while leaving ROM secure-boot/key/HSM
  behavior unresolved until the security manual is available.
- Validate eMMC, PCIe/NVMe, Ethernet, CAN-FD, camera and display one interface at a time with
  board-specific logs and exact BSP versions.
- Keep Linux/Yocto evidence separate from AUTOSAR/hypervisor claims; neither latter product was
  established by the accessible sources.

## FPGA/prototyping

- Host-based software mocks may reproduce device discovery and buffer/control APIs.
- FPGA traffic generators may model parameterized CSI, memory or Ethernet load, but not claim
  V4M protocol/internal equivalence.
- Product RTL prototyping is **BLOCKED** because no authorized V4M RTL/IP or implementable
  interface contract is available.
- Any proxy design receives its own project/revision namespace and cannot be used as evidence
  that V4M timing, power, functionality or safety passes.

## Next executable action

Obtain the public/controlled evaluation-board documentation and approved manuals, reproduce the
official BSP, capture boot/device logs, and feed newly observed values through Stage 0 before
updating integration requirements.
