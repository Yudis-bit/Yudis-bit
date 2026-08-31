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

## Engineering Snapshot

A compact view of the engineering work represented across this profile.

| System | Layer | Problem Class | Engineering Artifact | State |
|:---|:---|:---|:---|:---:|
| **LLVM / AMDGPU** | Compiler backend | Unsafe image-load merge candidate involving TFE/LWE result semantics | C++ fix + MIR regression coverage | `LANDED` |
| **Vulkan Validation Layers** | GPU validation | Out-of-bounds descriptor access during static validation | C++ guard + regression coverage | `LANDED` |
| **QEMU / x86_64** | Virtualization / ISA | Long-mode segment-prefix decoding correctness | Independent emulator validation | `TESTED-BY` |
| **OpenSBI · SBI ecall** | RISC-V firmware | Extension-list buffer could advance past caller-provided capacity | C bounds guard + SBIUNIT redzone regression | `LANDED` |
| **OpenSBI · RPMI mailbox** | RISC-V firmware | Fixed-size queue-name buffer boundary | Bounded-copy patch | `OPEN` |
| **secp256k1** | Cryptographic software | Constant-time coverage gap | C test-coverage extension | `OPEN` |
| **Linux / ftrace** | Kernel tooling | Documentation / sample correctness | Focused upstream cleanups | `LANDED ×2` |
| **Code4rena / Swafe** | Protocol security | Replayable authenticated recovery state | Security analysis + reproducible finding | `M-04 CO-FINDER` |

The systems are different.

The engineering questions are often the same:

```text
What assumption is being made?
            │
            ▼
Where is that assumption enforced?
            │
            ▼
What happens at the boundary?
            │
            ▼
Can the failure be reproduced?
            │
            ▼
Can the cause be reduced?
            │
            ▼
Can the correction be made narrowly?
            │
            ▼
What evidence prevents regression?
```

---

## Verified Upstream Engineering

> Production codebases. Reproducible failures. Reviewable changes.

| Project | Area | Contribution | Upstream State |
|:---|:---|:---|:---:|
| [**Khronos Vulkan Validation Layers**](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743) | GPU Validation · C++ | Fixed an out-of-bounds crash in static descriptor validation and added regression coverage | `MERGED ✓` |
| [**LLVM · AMDGPU**](https://github.com/llvm/llvm-project/pull/210583) | Compiler Backend · C++ / MIR | Prevented TFE/LWE image loads from entering invalid `SILoadStoreOptimizer` merge candidates | `MERGED ✓` |
| [**OpenSBI · SBI ecall**](https://github.com/riscv-software-src/opensbi/commit/f95648d3955d72f77e13315a990a6135303978a5) | RISC-V Firmware · C / SBIUNIT | Fixed an out-of-bounds write in `sbi_ecall_get_extensions_str()` and added redzone regression coverage | `MERGED ✓` |
| [**QEMU · x86_64**](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a) | Virtualization · ISA Validation | Independently validated the x86 long-mode segment-prefix decoding fix | `MERGED · TESTED-BY ✓` |
| [**bitcoin-core/secp256k1**](https://github.com/bitcoin-core/secp256k1/pull/1893) | Cryptographic Software · C | Extended constant-time test coverage for `schnorrsig_sign_custom` | `OPEN · REVIEW COMMENTS ◉` |
| [**OpenSBI · RPMI mailbox**](https://github.com/riscv-software-src/opensbi/pull/423) | RISC-V Firmware · C | Proposed bounded handling for RPMSI shared-memory queue names at the fixed firmware buffer boundary | `OPEN · AWAITING REVIEW ○` |
| **Linux · tracing / ftrace** | Kernel Documentation / Samples | Two small upstream documentation and sample cleanups — [e5d8524](https://github.com/torvalds/linux/commit/e5d8524) · [8a66c09](https://github.com/torvalds/linux/commit/8a66c09) | `MERGED ×2 ✓` |

<sub>Upstream states last reviewed: 31 August 2026.</sub>

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

### Failure path

```text
shader-declared descriptor array
              │
              ▼
pipeline-layout binding count
              │
              ▼
           mismatch
              │
              ▼
static descriptor validation
              │
              ▼
binding.descriptors[index]
              │
              ▼
        out-of-range access
```

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

TFE/LWE image loads carry additional status-result semantics.

The image-load merge path cannot safely reconstruct those status lanes, which means such instructions should never become ordinary merge candidates.

### Failure boundary

```text
MIMG instruction
      │
      ├── ordinary image load
      │        │
      │        └── eligible for merge analysis
      │
      └── TFE / LWE image load
               │
               └── additional status-result semantics
                            │
                            ▼
                  merge path cannot preserve
                  the required result shape
                            │
                            ▼
                     reject before
                  candidate collection
```

**Contribution**

- Added a guard rejecting TFE/LWE image loads before merge-candidate collection
- Covered the asymmetric ordinary → TFE/LWE failure ordering
- Added MIR-level regression coverage
- Preserved existing status-free positive merge behavior
- Iterated on AMDGPU reviewer feedback
- Rebased against upstream during review
- Passed focused LLVM lit coverage and upstream CI
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

The work focused on validating whether emulator behavior matched the expected architectural semantics.

The final QEMU commit permanently records:

```text
Tested-by: Yudistira Putra
```

This is **independent testing and validation credit**, not authorship of the underlying patch.

I keep that distinction explicit because authorship and independent validation are different engineering contributions.

<p>
<a href="https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a">
  <img src="https://img.shields.io/badge/QEMU-Upstream_Commit-FF6600?style=for-the-badge&logo=github&logoColor=white" alt="QEMU Commit">
</a>
</p>

---

### 04 · OpenSBI · RISC-V

**Caller-buffer boundary handling in `sbi_ecall_get_extensions_str()`**

The extension-string helper advanced its offset using the nominal extension-name length without first ensuring that the next entry would fit in the caller-provided buffer.

With a sufficiently small destination, the offset could move beyond `exts_str_size`, making the remaining-size calculation invalid and potentially allowing an out-of-bounds write.

### Failure boundary

```text
registered SBI extensions
          │
          ▼
caller-provided buffer
          │
          ▼
next extension does not fit
          │
          ▼
offset advances past capacity
          │
          ▼
invalid remaining-size calculation
          │
          ▼
potential out-of-bounds write
```

**Contribution**

- Identified the caller-buffer boundary failure
- Added a guard before appending the next extension name
- Added SBIUNIT regression coverage
- Used a 16-byte destination with a redzone to detect writes past the supplied boundary
- Added a larger-buffer control case
- Iterated through upstream review
- Reviewed by Anup Patel
- Landed in OpenSBI `master`
- Closed upstream issue #416

<p>
<a href="https://github.com/riscv-software-src/opensbi/commit/f95648d3955d72f77e13315a990a6135303978a5">
  <img src="https://img.shields.io/badge/OpenSBI-Upstream_Commit-238636?style=for-the-badge&logo=github&logoColor=white" alt="OpenSBI Commit">
</a>
<a href="https://lore.kernel.org/r/20260719101125.190314-1-pyudistira519@gmail.com">
  <img src="https://img.shields.io/badge/lore.kernel.org-Patch_Thread-58A6FF?style=for-the-badge" alt="OpenSBI lore thread">
</a>
</p>

---

## Failure → Fix → Evidence

I prefer work that can be reduced to a verifiable chain.

```text
unexpected behavior
        │
        ▼
reproducer
        │
        ▼
reduced failure
        │
        ▼
root-cause boundary
        │
        ▼
narrow correction
        │
        ▼
regression artifact
        │
        ▼
review
        │
        ▼
upstream result
```

A code change by itself is weak evidence.

A change becomes more useful when another engineer can inspect:

- what failed
- how to reproduce it
- which invariant was violated
- why the correction is scoped correctly
- what regression coverage preserves the behavior
- what happened during upstream review

This is the standard I try to apply whether the target is a compiler backend, validation layer, emulator, firmware component, cryptographic library, or protocol state machine.

---

## Technical Surface Area

My current work spans several layers of the software stack.

```text
┌───────────────────────────────────────────────────────────────┐
│                  SECURITY-CRITICAL PROTOCOLS                  │
│          invariants · freshness · state transitions           │
├───────────────────────────────────────────────────────────────┤
│                    CRYPTOGRAPHIC SOFTWARE                     │
│       secp256k1 · constant-time testing · differential tests  │
├───────────────────────────────────────────────────────────────┤
│                  COMPILER / MACHINE BACKEND                   │
│            LLVM · AMDGPU · MIR · machine transforms           │
├───────────────────────────────────────────────────────────────┤
│                     GPU VALIDATION LAYER                      │
│        Vulkan · descriptor state · pipeline correctness       │
├───────────────────────────────────────────────────────────────┤
│                    VIRTUALIZATION / ISA                       │
│             QEMU · x86_64 · decoder validation                │
├───────────────────────────────────────────────────────────────┤
│                           FIRMWARE                            │
│       OpenSBI · RISC-V · caller buffers · fixed boundaries    │
├───────────────────────────────────────────────────────────────┤
│                     KERNEL / TOOLING                          │
│                 Linux · tracing · ftrace                      │
└───────────────────────────────────────────────────────────────┘
```

Across those layers, I am primarily interested in places where correctness depends on subtle assumptions that are easy to miss during normal execution.

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

## Small Systems Tools

Not every useful engineering artifact needs to become a large framework.

### [`bitpeek`](https://github.com/Yudis-bit/bitpeek)

**Local-first byte inspector**

A small browser utility for inspecting raw byte representations without sending data to a backend.

```text
DE AD BE EF
     │
     ├── hex
     ├── binary
     ├── ASCII / UTF-8
     ├── signed integer
     ├── unsigned integer
     ├── big endian
     ├── little endian
     └── individual bits
```

Core behavior:

- Hex, binary, decimal-byte, and UTF-8 input
- Byte-range selection
- Signed and unsigned integer interpretation
- Big-endian and little-endian interpretation
- Interactive bit mutation
- Exact handling of 64-bit integer values
- Fully client-side execution
- No backend and no uploads

<p>
<a href="https://bitpeek-seven.vercel.app/">
  <img src="https://img.shields.io/badge/Live-bitpeek-238636?style=for-the-badge" alt="bitpeek live">
</a>
<a href="https://github.com/Yudis-bit/bitpeek">
  <img src="https://img.shields.io/badge/Source-bitpeek-181717?style=for-the-badge&logo=github&logoColor=white" alt="bitpeek source">
</a>
</p>

Its scope is intentionally narrow:

> Paste bytes. Inspect what they mean under a specific representation.

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

## Engineering Evidence

Claims on this profile are intentionally linked to primary engineering artifacts.

| Work | Primary Evidence |
|:---|:---|
| **LLVM / AMDGPU backend fix** | [llvm-project #210583](https://github.com/llvm/llvm-project/pull/210583) |
| **Vulkan validation crash fix** | [Vulkan-ValidationLayers #12743](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743) |
| **OpenSBI ecall buffer-boundary fix** | [Upstream commit f95648d](https://github.com/riscv-software-src/opensbi/commit/f95648d3955d72f77e13315a990a6135303978a5) |
| **QEMU independent validation** | [QEMU commit 3589cd9](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a) |
| **secp256k1 constant-time coverage** | [secp256k1 #1893](https://github.com/bitcoin-core/secp256k1/pull/1893) |
| **OpenSBI RPMI queue-name bounds patch** | [OpenSBI #423](https://github.com/riscv-software-src/opensbi/pull/423) |
| **Linux upstream work** | [e5d8524](https://github.com/torvalds/linux/commit/e5d8524) · [8a66c09](https://github.com/torvalds/linux/commit/8a66c09) |
| **Competitive security finding** | [Code4rena S-855](https://code4rena.com/audits/2025-11-swafe/submissions/S-855) |
| **Differential-testing infrastructure** | [ecc-audit-engine](https://github.com/Yudis-bit/ecc-audit-engine) |
| **Local-first review infrastructure** | [ArkheionX](https://github.com/Yudis-bit/arkheionx) |
| **Byte-inspection utility** | [bitpeek](https://github.com/Yudis-bit/bitpeek) |

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
PATCH / VALIDATE
   ↓
REGRESSION TEST
   ↓
UPSTREAM REVIEW
```

I prefer **small, reviewable changes backed by reproducible evidence**.

The goal is not simply to make a failure disappear.

The goal is to understand **why it happened**, demonstrate the failure reliably, identify the violated invariant or boundary, and leave behind evidence that makes the same class of regression harder to reintroduce.

---

## Review Discipline

Before considering a correctness change complete, I generally want to answer:

```text
Can I reproduce the failure?
        │
        ├── no  → evidence is incomplete
        │
        └── yes
              │
              ▼
Can I reduce the triggering case?
        │
        ├── no  → continue isolating
        │
        └── yes
              │
              ▼
Do I understand the violated invariant?
        │
        ├── no  → continue investigating
        │
        └── yes
              │
              ▼
Can the correction stay narrowly scoped?
        │
        ▼
Can a regression artifact preserve the behavior?
        │
        ▼
Submit for review
```

This matters in systems code because a locally plausible fix can still violate assumptions in another layer.

---

## What I Work On

| Domain | Current Engineering Focus |
|:---|:---|
| **Compilers** | LLVM backend correctness · machine-level optimization · MIR regression testing |
| **GPU / Graphics** | Vulkan validation · crash debugging · descriptor and pipeline boundary correctness |
| **Virtualization** | QEMU · x86_64 ISA behavior · instruction-decoder validation |
| **Firmware** | RISC-V · OpenSBI · caller-buffer and fixed-boundary safety |
| **Cryptographic Software** | secp256k1 · constant-time testing · differential testing |
| **Regression Infrastructure** | reproduction · minimization · deterministic replay · CI |
| **Security-Critical Software** | invariants · state transitions · freshness · replay protection |
| **Open Source** | focused fixes · regression coverage · review iteration · independent validation |

---

## Current Engineering Direction

### Compiler correctness

- Machine-level transformations
- Backend optimization
- MIR-based regression testing
- Cases where an optimization is structurally legal but semantically unsafe

### GPU infrastructure

- Validation-layer behavior
- Pipeline and descriptor state
- Boundary-condition crashes
- Safe handling of invalid application state

### Architecture and virtualization

- ISA semantics
- Instruction decoding
- Hardware / emulator behavior
- Small architectural edge cases with downstream effects

### RISC-V firmware

- Caller-provided buffer boundaries
- Fixed-size firmware interfaces
- SBI extension handling
- Regression coverage for boundary conditions

### Cryptographic software

- Constant-time test coverage
- Differential testing
- Deterministic corpora
- Failure minimization
- Reproducible evidence

### Security-critical state machines

- Freshness
- Replay resistance
- State-transition invariants
- Evidence-driven protocol review

---

## Engineering Priorities

The properties I optimize for are straightforward:

```text
correctness
reproducibility
reviewability
evidence
regression resistance
```

A useful engineering artifact should make it possible for another engineer to independently inspect both:

1. **what failed**
2. **why the proposed correction is sufficient**

That standard applies whether the target is a compiler backend, validation layer, emulator, firmware component, cryptographic library, or protocol.

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