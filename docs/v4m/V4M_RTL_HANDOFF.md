# R-Car V4M RTL Handoff

Status: **BLOCKED** for product RTL design; **PASS** for the public black-box handoff package.

## Available handoff material

- Qualified product/system specification and field inventory.
- Selected evidence-preserving architecture and black-box microarchitecture.
- Public instance counts and software-visible integration references.
- Three explicitly exploratory clock/voltage/bandwidth/power/area/thermal scenarios.
- Exact list of unresolved interface, clock/reset, memory, safety, security and test inputs.

## Product RTL entry criteria not met

1. Authoritative block behavior and register/interface specifications.
2. Complete clock/reset/power-domain and CDC/RDC intent.
3. Complete memory architecture, address map, QoS, ECC and protection behavior.
4. Accelerator/ISP/GPU functional and performance contracts.
5. Safety mechanisms, lockstep/diagnostics and security lifecycle requirements.
6. Verification requirements and acceptance coverage.
7. Implementable timing, power, area, physical and DFT constraints.
8. Rights to implement or use the proprietary Renesas/IP functionality.

Generating plausible internal V4M RTL without these facts would invent fundamental design
behavior. Therefore no misleading product RTL was created. A future owner can use the public
model to build mocks or software emulators, but those artifacts must be named and classified
as non-product prototypes.
