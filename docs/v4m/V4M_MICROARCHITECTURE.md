# R-Car V4M Public Microarchitecture Model

Status: **WARN**. This is a black-box integration model derived from public software-visible
topology. It is not Renesas implementation documentation.

## Boundary model

| Block | Publicly modeled boundary | Parameters intentionally unresolved |
|---|---|---|
| A76 cluster | 4 cores; evidenced L1/L2/L3 capacities; GICv3-visible interrupt path | internal coherency fabric, clocks, reset, power states, debug, safety mechanisms |
| R52 domain | existence from public thermal naming | core count, lockstep, local memories, boot, clocks, interconnect |
| Vision/AI | instance inventory from UIO exposure | datapaths, precision, SRAM, throughput, scheduling, coherency |
| CSI/VIN/ISP | 2/16/2 public instances | lane/rate, pixel formats, buffering, exact routing and aggregate throughput |
| GPU/display | GSX plus DU/VSP/DSI nodes | pipelines, shader resources, clocks, bandwidth and codecs |
| Memory system | Gray Hawk address ranges and CPU cache hierarchy | DRAM type/rate/width/channels, ECC, QoS, firewalls, physical map completeness |
| I/O | controller counts/modes observable in DTS | product lane/rate limits, pinmux/package availability, safety qualification |
| Security | PSCI/SMC + ATF/OP-TEE integration | ROM chain, keys, lifecycle, HSM/root of trust and production policy |

## Interface policy

Public device-tree addresses, interrupt descriptions, clocks and resets may seed software and
integration manifests. They must not be reinterpreted as a complete hardware contract. An RTL
port, transaction ordering rule, CDC boundary, register semantic or safety response may be
declared only when an authoritative manual/specification supplies it.

## Clock, reset, memory and safety treatment

- The 500/1000 MHz at 0.825 V CPU OPP table is retained as BSP evidence, not the global clock
  plan or maximum frequency.
- Each public power/thermal domain is modeled as a named boundary; crossings remain unresolved.
- The DTS-visible address map is a software subset. Reserved/secure/internal regions remain
  unspecified.
- The R52 and safety mechanisms remain opaque. No lockstep, diagnostic coverage or ASIL claim
  is inferred.

## Regeneration trigger

New hardware manual, safety manual, memory-controller, clock/reset or interface evidence must
enter through Stage 0. If it changes partitioning or interfaces, create a new architecture
revision, regenerate the handoff, then rerun the dependent checker set.
