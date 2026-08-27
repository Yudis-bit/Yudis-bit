<div align="center">

<h1>Yudistira Putra</h1>

<h3>Systems Software Engineer · Compilers · GPU Validation · Firmware · Correctness</h3>

<p>
<strong>C · C++ · Rust</strong><br>
LLVM / AMDGPU · Vulkan · QEMU / x86_64 · RISC-V · secp256k1
</p>

<p>
Correctness-focused systems engineer working on difficult failures across
compilers, GPU validation, virtualization, firmware, cryptographic software,
and regression infrastructure.
</p>

<p>
<a href="mailto:pyudistira519@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contact-24292F?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
</a>
<a href="https://www.linkedin.com/in/yudistira-putra-dev/">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
<a href="https://github.com/Yudis-bit">
  <img src="https://img.shields.io/badge/GitHub-Yudis--bit-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>
</p>

<p>
<img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white" alt="C">
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++">
<img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
<img src="https://img.shields.io/badge/LLVM-AMDGPU-262D3A?style=flat-square&logo=llvm&logoColor=white" alt="LLVM AMDGPU">
<img src="https://img.shields.io/badge/Vulkan-Validation-AC162C?style=flat-square&logo=vulkan&logoColor=white" alt="Vulkan">
<img src="https://img.shields.io/badge/RISC--V-Firmware-283272?style=flat-square&logo=riscv&logoColor=white" alt="RISC-V">
</p>

</div>

---

## `$ whoami`

I work on **correctness-critical systems software**.

My focus is reproducing difficult failures, reducing them to understandable root causes, designing regression coverage, and contributing narrowly scoped fixes or independent validation upstream.

I currently work primarily with **C, C++, and Rust** across compiler backends, GPU validation, virtualization, firmware, cryptographic software, and test infrastructure.

> **Reproduce → Reduce → Understand → Test → Upstream**

---

## Verified Upstream Engineering

> Production codebases. Reproducible failures. Reviewable changes.

| Project | Area | Contribution | Upstream State |
|:---|:---|:---|:---:|
| [**Khronos Vulkan Validation Layers**](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743) | GPU Validation · C++ | Fixed an out-of-bounds crash in static descriptor validation and added regression coverage | `MERGED ✓` |
| [**LLVM · AMDGPU**](https://github.com/llvm/llvm-project/pull/210583) | Compiler Backend · C++ / MIR | Prevented TFE/LWE image loads from entering invalid `SILoadStoreOptimizer` merge candidates | `MERGED ✓` |
| [**QEMU · x86_64**](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a) | Virtualization · ISA Validation | Independently validated the x86 long-mode segment-prefix decoding fix | `MERGED · TESTED-BY ✓` |
| [**bitcoin-core/secp256k1**](https://github.com/bitcoin-core/secp256k1/pull/1893) | Cryptographic Software · C | Extended constant-time test coverage for `schnorrsig_sign_custom` | `OPEN · UNDER REVIEW ◉` |
| [**OpenSBI**](https://github.com/riscv-software-src/opensbi/pull/423) | RISC-V Firmware · C | Proposed a bounded copy for RPMSI shared-memory queue names at the fixed firmware buffer boundary | `OPEN · AWAITING REVIEW ○` |
| **Linux · tracing / ftrace** | Kernel Documentation / Samples | Two small upstream documentation and sample cleanups — [e5d8524](https://github.com/torvalds/linux/commit/e5d8524) · [8a66c09](https://github.com/torvalds/linux/commit/8a66c09) | `MERGED ×2 ✓` |

<sub>Upstream states last reviewed: 27 August 2026.</sub>

---

## Selected Upstream Work

### 01 · Khronos Vulkan Validation Layers

**Out-of-bounds crash in static descriptor validation**

An invalid pipeline could reach draw-time static descriptor validation with a shader-declared descriptor array larger than the pipeline-layout binding count.

That allowed validation to reach:

```cpp
binding.descriptors[index]
```

with an out-of-range `index`.

**Contribution**

- Reproduced and isolated the failing validation path
- Identified the descriptor-array / binding-count mismatch
- Added a narrowly scoped early-termination guard
- Added dedicated C++ regression coverage
- Iterated on maintainer review feedback
- Passed upstream CI
- Landed in `KhronosGroup:main`

<p>
<a href="https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743">
  <img src="https://img.shields.io/badge/View_PR-%2312743-238636?style=for-the-badge&logo=github&logoColor=white" alt="Vulkan PR">
</a>
<a href="https://github.com/Yudis-bit/opencode/blob/main/case-studies/vulkan-validation-crash-fix.md">
  <img src="https://img.shields.io/badge/Read-Case_Study-58A6FF?style=for-the-badge&logo=markdown&logoColor=white" alt="Case Study">
</a>
</p>

---

### 02 · LLVM · AMDGPU

**`SILoadStoreOptimizer` image-load merge correctness**

TFE/LWE image loads require semantics that make certain load combinations unsafe to treat as ordinary merge candidates.

**Contribution**

- Added a guard rejecting invalid TFE/LWE image-load merge candidates
- Added MIR-level regression coverage
- Iterated on AMDGPU review feedback
- Rebased the patch against upstream
- Received reviewer approval / LGTM
- Passed upstream CI
- Landed in `llvm:main`

<p>
<a href="https://github.com/llvm/llvm-project/pull/210583">
  <img src="https://img.shields.io/badge/View_PR-%23210583-238636?style=for-the-badge&logo=github&logoColor=white" alt="LLVM PR">
</a>
</p>

---

### 03 · QEMU · x86_64

**Long-mode segment override prefix decoding**

I independently tested an upstream fix for x86 long-mode handling of legacy segment override prefixes.

The final QEMU commit permanently records:

```text
Tested-by: Yudistira Putra
```

This is **independent testing and validation credit**, not authorship of the underlying patch.

<p>
<a href="https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a">
  <img src="https://img.shields.io/badge/QEMU-Upstream_Commit-FF6600?style=for-the-badge&logo=github&logoColor=white" alt="QEMU Commit">
</a>
</p>

---

## Flagship Engineering

### [`ecc-audit-engine`](https://github.com/Yudis-bit/ecc-audit-engine)

**Reproducible differential-testing infrastructure for secp256k1 implementations**

```text
deterministic corpus
        │
        ▼
target execution
        │
        ▼
behavior comparison
        │
        ▼
failure detection
        │
        ▼
failure minimization
        │
        ▼
deterministic replay
        │
        ▼
structured evidence
```

Engineering focus:

- Differential testing
- Deterministic reproduction
- Correct / corrupted / synthetic target harnesses
- Failure minimization
- Replayable evidence
- Structured corpora and reporting
- Dynamic-trace experiments
- CI-backed regression verification

The project is designed around a simple requirement:

> A mismatch is only useful if it can be **reproduced, reduced, inspected, and replayed**.

<p>
<a href="https://github.com/Yudis-bit/ecc-audit-engine">
  <img src="https://img.shields.io/badge/Repository-ecc--audit--engine-181717?style=for-the-badge&logo=github&logoColor=white" alt="ecc-audit-engine">
</a>
<a href="https://github.com/Yudis-bit/ecc-audit-engine/releases/latest">
  <img src="https://img.shields.io/badge/Latest-Release-238636?style=for-the-badge&logo=github&logoColor=white" alt="Latest Release">
</a>
<a href="https://github.com/Yudis-bit/ecc-audit-engine/blob/main/examples/quick-demo.sh">
  <img src="https://img.shields.io/badge/Quick-Demo-58A6FF?style=for-the-badge&logo=gnubash&logoColor=white" alt="Quick Demo">
</a>
</p>

---

### [`ArkheionX`](https://github.com/Yudis-bit/arkheionx)

**Local-first security-review infrastructure**

ArkheionX builds structured review artifacts from local repositories so reviewers can reason about scope, value flow, protocol behavior, assumptions, evidence, and unresolved review gaps without requiring sensitive source code to leave the local environment.

Engineering focus:

- Local-first review workflows
- Deterministic review artifacts
- Schema-backed evidence
- Scope and value-flow mapping
- Protocol invariants and review lanes
- Evidence packaging
- Reproducibility
- Automated verification

The project deliberately keeps strong boundaries:

```text
no RPC
no live-chain scanning
no auto-submit
no automatic vulnerability confirmation
human review required
```

<p>
<a href="https://github.com/Yudis-bit/arkheionx">
  <img src="https://img.shields.io/badge/Repository-ArkheionX-181717?style=for-the-badge&logo=github&logoColor=white" alt="ArkheionX">
</a>
<a href="https://github.com/Yudis-bit/arkheionx/releases">
  <img src="https://img.shields.io/badge/View-Releases-238636?style=for-the-badge&logo=github&logoColor=white" alt="ArkheionX Releases">
</a>
</p>

---

## Competitive Security Research

<div align="center">

### Code4rena · Swafe

<img src="https://img.shields.io/badge/Finding-M--04_Co--finder-F59E0B?style=for-the-badge" alt="M-04 Co-finder">
<img src="https://img.shields.io/badge/Severity-Medium-F59E0B?style=for-the-badge" alt="Medium Severity">
<img src="https://img.shields.io/badge/Placement-Tied_%2330-58A6FF?style=for-the-badge" alt="Tied #30">

</div>

### M-04 · Replayable recovery requests can block account recovery

My submission **S-855** was credited in Code4rena's final Swafe report as a **co-finding of M-04**.

The recovery request was authenticated but lacked sufficient freshness or account-state binding. A previously valid request could therefore be replayed against later recovery state.

```text
authenticated recovery request
            │
            ▼
insufficient freshness / state binding
            │
            ▼
old request remains replayable
            │
            ▼
later recovery state overwritten
            │
            ▼
legitimate recovery disrupted
```

**Security impact**

- Replay of previously valid authenticated state transitions
- Persistent interference with account recovery
- Recovery denial of service
- Protocol state-machine / freshness failure

Code4rena's mitigation review later marked **M-04 as mitigated**.

<p>
<a href="https://code4rena.com/audits/2025-11-swafe/submissions/S-855">
  <img src="https://img.shields.io/badge/View-Submission_S--855-58A6FF?style=for-the-badge" alt="Code4rena Submission">
</a>
<a href="https://code4rena.com/reports/2025-11-swafe">
  <img src="https://img.shields.io/badge/Final-Swafe_Report-24292F?style=for-the-badge" alt="Swafe Final Report">
</a>
</p>

---

## How I Debug

```text
OBSERVE
   ↓
REPRODUCE
   ↓
REDUCE
   ↓
UNDERSTAND
   ↓
PATCH
   ↓
REGRESSION TEST
   ↓
UPSTREAM REVIEW
```

I prefer **small, reviewable changes backed by reproducible evidence**.

The goal is not simply to make a failure disappear. The goal is to understand **why it happened**, demonstrate the failure reliably, and leave behind coverage that makes the same class of regression harder to reintroduce.

---

## What I Work On

| Domain | Current Engineering Focus |
|:---|:---|
| **Compilers** | LLVM backend correctness · machine-level optimization · MIR regression testing |
| **GPU / Graphics** | Vulkan validation · crash debugging · boundary correctness |
| **Virtualization** | QEMU · x86_64 ISA behavior · instruction-decoder validation |
| **Firmware** | RISC-V · OpenSBI · fixed-buffer and boundary safety |
| **Cryptographic Software** | secp256k1 · constant-time testing · differential testing |
| **Regression Infrastructure** | reproduction · minimization · replay · CI |
| **Security-Critical Software** | invariants · state transitions · replay protection |
| **Open Source** | focused fixes · regression coverage · review iteration · independent validation |

---

## Open to Engineering Opportunities

I'm interested in **full-time, contract, and scoped engineering opportunities** involving:

- Systems software in **C, C++, or Rust**
- Compiler engineering and backend correctness
- GPU / graphics infrastructure and validation
- Virtualization and ISA-level debugging
- RISC-V firmware
- Cryptographic software testing
- Regression and verification infrastructure
- Security-critical systems
- Difficult cross-layer debugging

Particularly interested in problems where failures are subtle, reproducibility matters, and correctness must be **demonstrated rather than assumed**.

---

<div align="center">

<h2>Let's build reliable systems.</h2>

<p>
<a href="mailto:pyudistira519@gmail.com">
  <img src="https://img.shields.io/badge/Email-Let's_Talk-58A6FF?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
</a>
<a href="https://www.linkedin.com/in/yudistira-putra-dev/">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
</p>

</div>

```text
$ ./engineer --mode=correctness

[+] reproduce
[+] reduce
[+] understand
[+] test
[+] upstream

ready.
```

<div align="center">

<strong>Systems · Compilers · GPU · Virtualization · Firmware · Cryptographic Software</strong>

</div>