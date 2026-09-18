<div align="center">

# Yudistira Putra

**Systems Software Engineer -
Compilers · GPU · Firmware · Correctness**

`C` · `C++` · `Rust`  
LLVM / AMDGPU · Vulkan · QEMU / x86_64 · RISC-V / OpenSBI · secp256k1

[Email](mailto:pyudistira519@gmail.com) · [LinkedIn](https://www.linkedin.com/in/yudistira-putra-dev/) · [GitHub](https://github.com/Yudis-bit)

</div>

---

I work where small mistakes become real failures: compiler backends, validation layers, emulators, firmware, and cryptographic code. I reproduce the bug, reduce it, fix the boundary, and leave a regression test behind.

`reproduce → reduce → understand → fix → test → upstream`

## Upstream Work

| Project | Contribution | Status |
|---|---|:---:|
| [LLVM / AMDGPU](https://github.com/llvm/llvm-project/pull/210583) | Stopped TFE/LWE image loads from entering `SILoadStoreOptimizer` merge candidates; added MIR regressions. | `MERGED` |
| [Vulkan Validation Layers](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743) | Added a bounds guard to static descriptor validation, preventing an out-of-bounds access; added C++ regression coverage. | `MERGED` |
| [heroiclabs / nakama](https://github.com/heroiclabs/nakama/pull/909) | Fixed tournament reset timer and session cleanup edge condition in distributed runtime. | `MERGED` |
| [OpenSBI / SBI ecall](https://github.com/riscv-software-src/opensbi/commit/f95648d3955d72f77e13315a990a6135303978a5) | Bounded `sbi_ecall_get_extensions_str()` to caller capacity; added an SBIUNIT redzone test. | `MERGED` |
| [bitcoin-core / secp256k1](https://github.com/bitcoin-core/secp256k1/pull/1893) | Added CHECKMEM coverage for `schnorrsig_sign_custom`, including a custom nonce callback. | `MERGED` |
| [OpenSBI / RPMI](https://github.com/riscv-software-src/opensbi/pull/423) | Proposed bounded copying for fixed-size shared-memory queue names. | `OPEN` |
| [QEMU / x86_64](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a) | Independently validated long-mode handling of legacy segment override prefixes. | `TESTED-BY` |
| [Code4rena / Swafe](https://code4rena.com/reports/2025-11-swafe) | Credited co-finder of M-04: replayable recovery requests could block later recovery; mitigation confirmed. | `CO-FINDER` |

## Featured Flagships

| Flagship | Stack | Purpose |
|---|---|---|
| [`why-ui`](https://github.com/Yudis-bit/why-ui) | TypeScript, Node, MCP | Developer tool & Model Context Protocol daemon providing runtime browser visual/DOM evidence for coding agents. |
| [`bitpeek`](https://github.com/Yudis-bit/bitpeek) | React, TypeScript, Vite | Client-side binary workbench for inspecting, editing, comparing, and interpreting raw bytes with zero telemetry. |
| [`ecc-audit-engine`](https://github.com/Yudis-bit/ecc-audit-engine) | Rust, C ABI, Valgrind | Reproducible secp256k1 differential testing, failure minimization, replay, and dynamic-trace research engine. |

## Research & Private Systems

| Project | Domain | Status |
|---|---|---|
| [`Cognitive-Routing-Protocol`](https://github.com/Yudis-bit/Cognitive-Routing-Protocol) | Multi-Armed Bandit RL vs Dijkstra simulation for DePIN routing with on-chain trust staking. | `PUBLIC RESEARCH` |
| **ArkheionX** | Local-first smart contract security review infrastructure and deterministic vulnerability workbench. | `PRIVATE PRODUCT` |

## Focus

Compiler backends · GPU validation · virtualization · RISC-V firmware · cryptographic software · regression infrastructure

Open to full-time, contract, and scoped systems work in **C, C++, and Rust**.