# R-Car V4M Source Ledger

Retrieval date: 2026-10-02 UTC. The execution environment denied direct access to
Renesas.com and general web search with HTTP 403. Official Renesas GitHub repositories were
accessible and are the primary evidence used below. The blocked product-page search is recorded
as a gap; no value was promoted merely because it is commonly repeated online.

| ID | Class | Organization | Document / exact revision | Reference | Material used |
|---|---|---|---|---|---|
| S1 | OFFICIAL_DISCLOSED | Renesas Electronics | Linux BSP `r8a779h0.dtsi`, commit `b03ecaf56b04744cfb4e61905fa25fd5bc820514` | https://github.com/renesas-rcar/linux-bsp/blob/b03ecaf56b04744cfb4e61905fa25fd5bc820514/arch/arm64/boot/dts/renesas/r8a779h0.dtsi | R8A779H0 identity; 4 Cortex-A76; exposed OPPs; GPU/ISP/CSI/VIN/display/PCIe/CAN-FD/Ethernet/storage/IOMMU/thermal blocks. |
| S2 | OFFICIAL_DISCLOSED | Renesas Electronics | Gray Hawk common DTS at S1 commit | https://github.com/renesas-rcar/linux-bsp/blob/b03ecaf56b04744cfb4e61905fa25fd5bc820514/arch/arm64/boot/dts/renesas/r8a779h0-gray-hawk-common.dtsi | Board memory map, three Ethernet PHYs, four CAN-FD pin groups, two CSI inputs fed by eight serializer links, DSI bridge, PCIe, eMMC HS200/HS400. |
| S3 | OFFICIAL_DISCLOSED | Renesas Electronics | `meta-renesas` Gray Hawk machine config, commit `9289a2c05dbc8d6deaaff49f33d81a0110bd8228` | https://github.com/renesas-rcar/meta-renesas/blob/9289a2c05dbc8d6deaaff49f33d81a0110bd8228/meta-rcar-bsp/conf/machine/grayhawk.conf | V4M/Gray Hawk mapping, Cortex-A76 tune, Linux/Yocto machine and SDK identity. |
| S4 | OFFICIAL_DISCLOSED | Renesas Electronics | Public BSP patch citing V4M HWUM rev.0.80 §5.1.1.1 | https://github.com/renesas-rcar/meta-renesas/blob/9289a2c05dbc8d6deaaff49f33d81a0110bd8228/meta-rcar-bsp/recipes-kernel/linux/linux-renesas/0001-arm64-dts-r8a779h0-Fix-CPU-cache-hierarchy-to-enable.patch | 64 KiB I + 64 KiB D L1 per A76, 256 KiB L2 per core, 512 KiB cluster L3. This is a public excerpt, not a substitute for the confidential HWUM. |
| S5 | OFFICIAL_DISCLOSED | Renesas Electronics | `rcar-image-adas.bb` at S3 commit | https://github.com/renesas-rcar/meta-renesas/blob/9289a2c05dbc8d6deaaff49f33d81a0110bd8228/meta-rcar-adas/recipes-core/images/rcar-image-adas.bb | ADAS Linux image includes OpenCV SDK, kernel, NVMe/PCIe utilities and OP-TEE client. |
| S6 | OFFICIAL_DISCLOSED | Renesas Electronics | Arm Trusted Firmware recipe at S3 commit | https://github.com/renesas-rcar/meta-renesas/blob/9289a2c05dbc8d6deaaff49f33d81a0110bd8228/meta-rcar-bsp/recipes-bsp/arm-trusted-firmware/arm-trusted-firmware_git.bb | V4M platform identifier, AArch64 ATF, OP-TEE dispatcher, mbedTLS integration. |
| S7 | OFFICIAL_DISCLOSED | Renesas Electronics | Linux BSP V4M UIO DTS at S1 commit | https://github.com/renesas-rcar/linux-bsp/blob/b03ecaf56b04744cfb4e61905fa25fd5bc820514/arch/arm64/boot/dts/renesas/r8a779h0-uio.dtsi | Public software-visible IMP (2), CVE (4), CNN (1), VDSP domains (2), ISP and video/vision accelerator register regions. Counts describe exposed instances in this BSP, not guaranteed peak performance. |
| S8 | PUBLIC_CORROBORATED | Linux kernel community + Renesas maintainers | DT bindings for R-Car CSI-2/VIN and R8A779H0 | https://github.com/renesas-rcar/linux-bsp/tree/b03ecaf56b04744cfb4e61905fa25fd5bc820514/Documentation/devicetree/bindings | Corroborates R-Car V4M compatible strings and Linux driver model. |
| S9 | SEARCH_ATTEMPT_ONLY | Renesas Electronics | R-Car V4M product page | https://www.renesas.com/en/products/automotive-products/automotive-system-chips-socs/r-car-v4m | Direct retrieval and text-mirror retrieval returned HTTP 403. No exact value in this pack relies solely on the unfetched page. |

## Search paths exhausted in this run

- Direct Renesas product URL and sitemap: proxy/server HTTP 403.
- General Google/Bing search endpoints: HTTP 403.
- GitHub code-search API without a user token: forbidden; native read-only Git access worked.
- Alternative official terminology searched in accessible repositories: `V4M`, `r8a779h0`,
  `grayhawk`, `cr52`, `IMP`, `CVE`, `CNN`, `VDSP`, `GSX`, `OPTEE`, `PCIe`, camera/CSI/VIN.

These limitations reduce confidence for marketing/performance, process, package, safety, and
power/area fields. They do not affect facts directly observable in the exact official commits.
