# R-Car V4M Derived Estimates

Every calculation here states its operands. Results are `DERIVED_ESTIMATE` unless explicitly
marked `ENGINEERING_ASSUMPTION`; none is an official V4M specification.

## Gray Hawk fitted-memory estimate

The official board DTS (S2) describes 7.875 GiB usable/non-secure Linux memory and notes the
first 128 MiB as secure. `7.875 GiB + 0.125 GiB = 8.000 GiB`. Therefore the board is modeled as
approximately 8 GiB fitted memory. This says nothing about V4M controller maximum, DRAM type,
channel count, bus width, rate, or ECC.

## DRAM bandwidth scenarios

| Case | Explicit hypothetical organization | Arithmetic | Estimate |
|---|---|---|---:|
| CONSERVATIVE | 32 aggregate data bits at 4.266 GT/s | `4.266e9 × 32 / 8` | 17.1 GB/s |
| NOMINAL_EXPLORATORY | 64 aggregate data bits at 3.2 GT/s | `3.2e9 × 64 / 8` | 25.6 GB/s |
| AGGRESSIVE | 64 aggregate data bits at 4.266 GT/s | `4.266e9 × 64 / 8` | 34.1 GB/s |

The organization operands are ENGINEERING_ASSUMPTION. At an assumed 70% sustained
efficiency, available workload bandwidth is 12.0/17.9/23.9 GB/s. Camera, ISP, GPU and AI
throughput cannot be closed against these values until formats, resolutions, frame rates,
precision, reuse, compression and arbitration are specified.

## Cache capacity visible from public evidence

For four A76 cores (S1) and the cache hierarchy in S4:

- L1 instruction: `4 × 64 KiB = 256 KiB`.
- L1 data: `4 × 64 KiB = 256 KiB`.
- Private L2: `4 × 256 KiB = 1,024 KiB`.
- Shared L3: `512 KiB`.
- Publicly described A76 cache sum: `2,048 KiB`.

The sum is not total on-chip SRAM and excludes tags, buffers, R52 caches and every accelerator,
ISP, interconnect and peripheral memory.

## Timing sensitivity

| Frequency | Raw period | Reserved margin | Exploratory implementation allowance |
|---:|---:|---:|---:|
| 1.0 GHz | 1.000 ns | 15% | 0.850 ns |
| 1.8 GHz | 0.556 ns | 10% | 0.500 ns |
| 2.0 GHz | 0.500 ns | 5% | 0.475 ns |

Only the 1.0 GHz BSP operating point is official public evidence, and even that is not a
product-maximum claim. All implementation allowances are ENGINEERING_ASSUMPTION.

## Area and power

No defensible die calculation can be made without a scaled die image, die dimensions,
transistor count, process disclosure, floorplan, or implementation database. The
180/260/340 mm² and 15/25/40 W values are therefore ENGINEERING_ASSUMPTION envelopes, not
derived product estimates. Keeping this distinction prevents a guessed bound from acquiring
false authority through repetition.
