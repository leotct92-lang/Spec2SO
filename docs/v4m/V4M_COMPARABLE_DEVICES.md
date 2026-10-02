# R-Car V4M Comparable-Device Policy and Record

No related-device numeric value is copied into the V4M normalized specification. The final
accessible-source sweep searched R-Car Gen4 family terminology in official Renesas Linux and
Yocto repositories, but those software trees do not establish comparable product power,
process, package, die, TOPS, memory-rate, or safety values.

| Related evidence | Relevance | Material difference | Permitted use | V4M result |
|---|---|---|---|---|
| R-Car Gen4 common Linux driver/binding support | Helps identify shared software interfaces and compatible strings. | A common driver does not prove equal instance count, rate, lanes, clocks, safety features, or physical implementation. | Public corroboration of interface family only. | No numeric value imported. |
| Gray Hawk evaluation platform | Official software/board realization of R8A779H0. | Board population, memory capacity, bridges, PHYs, rail power, and connectors are not SoC maxima. | Confirm enabled board paths and derive fitted memory only. | Board facts remain scoped to Gray Hawk. |
| Cortex-A76 architectural family | Explains ISA/toolchain compatibility. | Core integration, cache hierarchy, frequency, voltage and safety configuration are SoC-specific. | Compiler/software planning only. | Core count/cache use direct V4M sources S1/S4 instead. |

If later research uses an exact sibling device, Stage 0 must add a record naming the sibling,
source, relevance, difference, derivation, bounds and `DERIVED_ESTIMATE` or
`ENGINEERING_ASSUMPTION` classification. A sibling data sheet alone can never establish a V4M
fact.
