# Yudistira Putra

Systems software and correctness engineer focused on reproducible debugging, C/C++/Rust systems, compiler and GPU validation, firmware safety, and cryptographic differential-testing infrastructure.

`pyudistira519@gmail.com` · [GitHub](https://github.com/Yudis-bit) · [LinkedIn](https://www.linkedin.com/in/yudistira-putra-dev/)

---

## Verified Contributions

| Project | Problem | Contribution | Status | Evidence |
|:---|:---|:---|:---:|:---|
| **Khronos Vulkan Validation Layers** | Out-of-bounds crash in static descriptor validation | 6-line fix + 64-line C++ regression test | **MERGED** | [PR #12743](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743) |
| **LLVM** | TFE/LWE image loads entering SILoadStoreOptimizer merge candidates | 10-line guard + 35-line MIR regression | **APPROVED, NOT MERGED** | [PR #210583](https://github.com/llvm/llvm-project/pull/210583) |
| **Linux** | Two comment typos in ftrace samples and tracing docs | Typo corrections | **MERGED** | [e5d8524](https://github.com/torvalds/linux/commit/e5d8524), [8a66c09](https://github.com/torvalds/linux/commit/8a66c09) |
| **bitcoin-core/secp256k1** | Missing constant-time test coverage for schnorrsig_sign_custom | Test-only `ctime_tests.c` extension | **UNDER REVIEW** | [PR #1893](https://github.com/bitcoin-core/secp256k1/pull/1893) |

---

## Flagship Projects

### [ecc-audit-engine](https://github.com/Yudis-bit/ecc-audit-engine)
Independent secp256k1 differential-testing research engine. Deterministic corpus, synthetic corrupted targets, failure minimization, replay, and structured reporting. 30 tests, 3 releases, active CI.
- [v0.2.1 release](https://github.com/Yudis-bit/ecc-audit-engine/releases/latest)
- [Quick demo](https://github.com/Yudis-bit/ecc-audit-engine/blob/main/examples/quick-demo.sh)

### [arkheionx](https://github.com/Yudis-bit/arkheionx)
Local-first smart contract review infrastructure. Structured evidence packs, deterministic fixtures, privacy-preserving portable output. Extensive Python test suite, CI, 44 releases.
- [Portable review packs case study](https://github.com/Yudis-bit/arkheionx)

### [Cognitive Routing Protocol](https://github.com/Yudis-bit/Cognitive-Routing-Protocol)
Research simulation exploring adaptive routing tradeoffs with Multi-Armed Bandit RL. 23.8% delivery ratio honestly documented alongside latency analysis.
- [Simulation methodology](https://github.com/Yudis-bit/Cognitive-Routing-Protocol)

---

## Case Studies

- [Vulkan Validation Layers — Out-of-Bounds Crash Fix](https://github.com/Yudis-bit/opencode/blob/main/case-studies/vulkan-validation-crash-fix.md)
- [ArkheionX — Portable Private Review Packs](https://github.com/Yudis-bit/opencode/blob/main/case-studies/arkheionx-portable-private-review-packs.md)

---

## Available For

Scoped systems debugging, regression-test development, C/C++/Rust correctness work, compiler and Vulkan investigations, cryptographic differential-testing integrations, and repository reproducibility rescue.

[Contact for scoped engagement →](mailto:pyudistira519@gmail.com)

---

## Current Focus

- ECC differential-testing adapter SDK
- Compiler and cryptographic test infrastructure
- Local-first review tooling
- Upstream LLVM and secp256k1 contributions