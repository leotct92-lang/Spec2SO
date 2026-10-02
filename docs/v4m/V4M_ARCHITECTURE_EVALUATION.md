# R-Car V4M Architecture Evaluation and Trade-off

Status: **WARN** — public architecture reconstruction completed; production architecture
sign-off requires confidential manuals and acceptance criteria.

## Product intent reconstructed from public evidence

The defensible system intent is a heterogeneous ADAS-oriented SoC/software platform: four
Cortex-A76 application CPUs, an R52-class real-time domain, GSX graphics, public vision/AI
accelerator instances, camera/ISP ingress, display/video paths, automotive/network interfaces,
and a Linux/Yocto + trusted-execution software stack. This is a reconstruction of exposed
blocks, not a claim about undisclosed performance or safety scope.

## Candidates

| Candidate | Description | Benefits | Risks | Result |
|---|---|---|---|---|
| A: evidence-preserving heterogeneous model | Preserve every publicly exposed block and unknown boundary; treat accelerators as black boxes. | Highest traceability; supports BSP/integration planning without inventing internals. | Cannot predict peak performance or physical QoR. | **Selected**. |
| B: CPU-centric emulation | Model cameras/AI on A76 software and omit undocumented accelerators. | Easier generic prototyping. | Contradicts the public hardware topology and distorts bandwidth/power. | Rejected as product architecture; allowed only as a host prototype. |
| C: inferred accelerator implementation | Invent internal CNN/IMP/CVE/VDSP microarchitecture to meet assumed TOPS. | Could enable synthetic RTL experiments. | No authoritative throughput, precision, interfaces, clocks or behavior; false product claim. | Rejected. |

## Selected partition

- Application island: four A76 cores and their evidenced cache hierarchy.
- Safety/real-time island: R52-class black box pending topology and safety manual.
- Vision/AI island: 2 IMP, 4 CVE, 1 CNN and 2 VDSP software-visible domains as black boxes.
- Imaging island: two CSI-2, sixteen VIN and two ISP instances; throughput remains a variable.
- Graphics/display island: GSX GPU, DU, VSP and MIPI DSI public nodes.
- I/O island: three Ethernet controllers, four CAN-FD channels, one PCIe controller, eMMC,
  RPC flash and public board peripherals.
- Security/system island: GICv3, IPMMUs, PSCI/SMC, ATF and OP-TEE software integration.

## Consistency checks

| Check | Result | Resolution |
|---|---|---|
| TOPS vs accelerator topology/frequency | WARN | Instance counts alone cannot yield TOPS; retain TOPS/precision as UNKNOWN. |
| Compute vs memory bandwidth | WARN | No public controller organization or workload arithmetic; use three explicit bandwidth scenarios only. |
| ISP vs eight board camera links | WARN | Eight links do not establish concurrent format/frame rate; parameterize traffic. |
| Power vs process/frequency | WARN | Neither chip power nor process is official; no closure claim. |
| Area vs process/IP | WARN | No scaled die/process evidence; area envelopes remain assumptions. |
| Thermal vs power | WARN | Sensor domains exist but ratings/model do not; do not equate scenario temperatures to limits. |
| Clock vs interface limit | WARN | Controller existence does not establish line rates; integration uses unknown rate fields. |
| Channel count vs bandwidth | PASS | Counts are kept distinct from throughput, so no unsupported multiplication is presented as fact. |

## Architecture decision

Proceed with Candidate A for public specification, firmware planning, test-plan preparation and
integration inventories. Do not generate product-representative internal accelerator, clock,
reset, safety or memory-controller RTL. Any such implementation needs a genuine product
decision or proprietary specification and would create a new architecture revision.
