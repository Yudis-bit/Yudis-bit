<div align="center">

# Yudistira Putra

### Systems Software Engineer · Low-Level Engineering · Correctness

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2600&pause=900&color=58A6FF&center=true&vCenter=true&width=820&lines=C+%C2%B7+C%2B%2B+%C2%B7+Rust;Compilers+%C2%B7+GPU+Validation;Virtualization+%C2%B7+x86;RISC-V+Firmware;Cryptographic+Correctness;Reproduce+%E2%86%92+Understand+%E2%86%92+Test+%E2%86%92+Upstream" alt="Systems Engineering Focus" />

<br>

**Correctness-focused systems engineer working across compilers, GPU validation,  
virtualization, firmware, and security-critical software.**

<br>

[![Email](https://img.shields.io/badge/Email-Contact-24292F?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pyudistira519@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yudistira-putra-dev/)
[![GitHub](https://img.shields.io/badge/GitHub-Yudis--bit-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Yudis-bit)

<br>

![C](https://img.shields.io/badge/C-Systems-00599C?style=flat-square&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-Systems-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-Systems-000000?style=flat-square&logo=rust&logoColor=white)
![LLVM](https://img.shields.io/badge/LLVM-AMDGPU-262D3A?style=flat-square&logo=llvm&logoColor=white)
![Vulkan](https://img.shields.io/badge/Vulkan-Validation-AC162C?style=flat-square&logo=vulkan&logoColor=white)
![QEMU](https://img.shields.io/badge/QEMU-x86__64-FF6600?style=flat-square)
![RISC-V](https://img.shields.io/badge/RISC--V-Firmware-283272?style=flat-square&logo=riscv&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Upstream-FCC624?style=flat-square&logo=linux&logoColor=black)

</div>

---

## `$ whoami`

I work on **correctness-critical systems software**.

My focus is reproducing difficult failures, isolating root causes, designing regression coverage, and contributing narrowly scoped fixes or independent validation upstream.

I currently work primarily with **C, C++, and Rust** across:

```text
┌────────────────────────┬───────────────────────────────────┐
│ Compiler Backends      │ LLVM / AMDGPU                     │
│ GPU Validation         │ Vulkan Validation Layers          │
│ Virtualization         │ QEMU / x86_64                     │
│ Firmware               │ OpenSBI / RISC-V                  │
│ Cryptographic Software │ secp256k1                         │
│ Security Research      │ Protocol / State-Machine Analysis │
│ Test Infrastructure    │ Differential + Regression Testing │
└────────────────────────┴───────────────────────────────────┘
```

---

# Upstream Engineering

> Production codebases. Reproducible failures. Reviewable changes.

| Project | Area | Contribution | Upstream State |
|:---|:---|:---|:---:|
| [**Khronos Vulkan Validation Layers**](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743) | GPU Validation · C++ | Fixed an out-of-bounds crash in static descriptor validation and added regression coverage | `MERGED ✓` |
| [**LLVM · AMDGPU**](https://github.com/llvm/llvm-project/pull/210583) | Compiler Backend · C++ / MIR | Prevented TFE/LWE image loads from entering invalid `SILoadStoreOptimizer` merge candidates | `OPEN · APPROVED BY REVIEWER ◉` |
| [**QEMU · x86_64**](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a) | Virtualization · ISA Validation | Independently validated the x86 long-mode segment-prefix decoding fix | `MERGED · TESTED-BY ✓` |
| [**bitcoin-core/secp256k1**](https://github.com/bitcoin-core/secp256k1/pull/1893) | Cryptographic Software · C | Extended constant-time testing for `schnorrsig_sign_custom` | `OPEN · UNDER REVIEW ◉` |
| [**OpenSBI**](https://github.com/riscv-software-src/opensbi/pull/423) | RISC-V Firmware · C | Clamped RPMSI shared-memory queue names to the fixed firmware buffer limit | `OPEN · AWAITING REVIEW ○` |

### Additional upstream work

**Linux tracing / ftrace**

Two small upstream documentation and sample cleanups:

[![Linux Commit](https://img.shields.io/badge/Linux-e5d8524-Merged-FCC624?style=flat-square&logo=linux&logoColor=black)](https://github.com/torvalds/linux/commit/e5d8524)
[![Linux Commit](https://img.shields.io/badge/Linux-8a66c09-Merged-FCC624?style=flat-square&logo=linux&logoColor=black)](https://github.com/torvalds/linux/commit/8a66c09)

---

## `$ upstream --status`

```text
Khronos VVL     [████████████████████████]  MERGED
LLVM AMDGPU     [███████████████████░░░░░]  OPEN · REVIEWER APPROVED
QEMU x86_64     [████████████████████████]  MERGED · TESTED-BY
secp256k1       [████████████████░░░░░░░░]  UNDER REVIEW
OpenSBI         [████████████░░░░░░░░░░░░]  AWAITING REVIEW
Linux           [████████████████████████]  MERGED ×2
```

---

# Selected Upstream Highlights

## 01 · Khronos Vulkan Validation Layers

**Out-of-bounds crash in static descriptor validation**

```text
malformed pipeline state
          │
          ▼
static descriptor validation
          │
          ▼
pipeline binding count < shader array length
          │
          ▼
binding.descriptors[index]
          │
          ▼
out-of-bounds access
          │
          ▼
crash
          │
          ▼
safe early termination
          │
          ▼
C++ regression coverage
          │
          ▼
upstream review + CI
          │
          ▼
MERGED ✓
```

### What I contributed

- Investigated the failing validation path
- Isolated the out-of-bounds descriptor access
- Added a narrowly scoped defensive correctness fix
- Added dedicated C++ regression coverage
- Iterated on maintainer review feedback
- Passed upstream CI
- Landed in `KhronosGroup:main`

[![View PR](https://img.shields.io/badge/View_PR-%2312743-238636?style=for-the-badge&logo=github)](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743)
[![Case Study](https://img.shields.io/badge/Read-Case_Study-58A6FF?style=for-the-badge&logo=markdown&logoColor=white)](https://github.com/Yudis-bit/opencode/blob/main/case-studies/vulkan-validation-crash-fix.md)

---

## 02 · LLVM · AMDGPU

**`SILoadStoreOptimizer` correctness**

```text
TFE / LWE image load
        │
        ▼
collectMergeableInsts()
        │
        ▼
invalid merge candidate
        │
        ▼
correctness guard
        │
        ▼
MIR regression test
        │
        ▼
AMDGPU review
```

### What I contributed

- Added a guard preventing invalid TFE/LWE image-load merging
- Added MIR-level regression coverage
- Iterated on LLVM AMDGPU review feedback
- Rebased the change against upstream
- Received reviewer approval / LGTM
- PR remains open pending the remaining upstream review path

[![View PR](https://img.shields.io/badge/View_PR-%23210583-58A6FF?style=for-the-badge&logo=github)](https://github.com/llvm/llvm-project/pull/210583)

---

## 03 · QEMU · x86_64

**Long-mode segment override prefix decoding**

```text
legacy segment prefix
          │
          ▼
x86_64 instruction decoder
          │
          ▼
incorrect long-mode behavior
          │
          ▼
upstream patch
          │
          ▼
independent functional validation
          │
          ▼
regression confidence
          │
          ▼
MERGED ✓
```

I independently tested and validated the fix.

The final upstream QEMU commit permanently records:

```text
Tested-by: Yudistira Putra
```

This is **testing and validation credit**, not authorship of the underlying patch.

[![QEMU](https://img.shields.io/badge/QEMU-Upstream_Commit-FF6600?style=for-the-badge)](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a)

---

## 04 · bitcoin-core/secp256k1

**Constant-time test coverage for `schnorrsig_sign_custom`**

```text
schnorrsig_sign_custom
          │
          ▼
constant-time test gap
          │
          ▼
ctime_tests.c extension
          │
          ├── default path
          ├── custom nonce callback
          ├── auxiliary data
          └── variable-length messages
          │
          ▼
CHECKMEM / Valgrind validation
```

### What I contributed

- Extended `ctime_tests.c`
- Added coverage for the custom nonce callback path
- Added non-null auxiliary-data coverage
- Added variable-length message coverage
- Exercised secret-tainted inputs through constant-time instrumentation
- Validated through the existing test infrastructure

[![View PR](https://img.shields.io/badge/View_PR-%231893-58A6FF?style=for-the-badge&logo=github)](https://github.com/bitcoin-core/secp256k1/pull/1893)

---

## 05 · OpenSBI · RISC-V Firmware

**Fixed-size RPMSI queue-name buffer safety**

```text
extension name
      │
      ▼
fixed-size firmware buffer
      │
      ▼
unbounded copy risk
      │
      ▼
length clamp
      │
      ▼
explicit null termination
```

### What I contributed

- Clamped the copied queue-name length to `RPMI_NAME_CHARS_MAX`
- Preserved explicit null termination
- Kept the patch minimal and localized to the firmware boundary

[![View PR](https://img.shields.io/badge/View_PR-%23423-58A6FF?style=for-the-badge&logo=github)](https://github.com/riscv-software-src/opensbi/pull/423)

---

# Flagship Engineering

## [`ecc-audit-engine`](https://github.com/Yudis-bit/ecc-audit-engine)

### Cryptographic Differential-Testing Infrastructure

Research-oriented tooling for reproducible investigation of secp256k1 implementations.

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

### Engineering focus

- Differential testing
- Deterministic reproduction
- Synthetic corrupted targets
- Failure minimization
- Replayable evidence
- Structured reporting
- Cryptographic implementation testing
- CI-backed regression coverage

**30 tests · 3 releases · Active CI**

[![Repository](https://img.shields.io/badge/Repository-ecc--audit--engine-181717?style=for-the-badge&logo=github)](https://github.com/Yudis-bit/ecc-audit-engine)
[![Release](https://img.shields.io/badge/Latest-Release-238636?style=for-the-badge&logo=github)](https://github.com/Yudis-bit/ecc-audit-engine/releases/latest)
[![Demo](https://img.shields.io/badge/Quick-Demo-58A6FF?style=for-the-badge&logo=gnubash&logoColor=white)](https://github.com/Yudis-bit/ecc-audit-engine/blob/main/examples/quick-demo.sh)

---

## [`ArkheionX`](https://github.com/Yudis-bit/arkheionx)

### Local-First Security Review Infrastructure

Infrastructure for producing structured and reproducible security evidence without requiring sensitive repositories to leave the local environment.

```text
source / findings
       │
       ▼
deterministic analysis
       │
       ▼
structured evidence
       │
       ▼
portable review pack
       │
       ▼
offline inspection
```

### Engineering focus

- Deterministic fixtures
- Local-first review workflows
- Evidence packaging
- Reproducibility
- Privacy-preserving output
- Automated testing
- Security-review infrastructure

**44 releases · CI-backed**

[![Repository](https://img.shields.io/badge/Repository-ArkheionX-181717?style=for-the-badge&logo=github)](https://github.com/Yudis-bit/arkheionx)

---

# Competitive Security Research

<div align="center">

### Protocol Correctness · Adversarial Reasoning · State-Machine Analysis

[![Code4rena](https://img.shields.io/badge/Code4rena-Swafe-24292F?style=for-the-badge)](https://code4rena.com/audits/2025-11-swafe/submissions/S-855)
![Severity](https://img.shields.io/badge/Severity-Medium-F59E0B?style=for-the-badge)
![Placement](https://img.shields.io/badge/Placement-%2330-58A6FF?style=for-the-badge)

</div>

## Swafe · Code4rena

### M-04 · Replayable recovery requests allow attacker to permanently block account recovery

A recovery request was authenticated, but lacked sufficient freshness or state binding.

That allowed an old valid recovery request to be replayed against later recovery state.

```text
valid signed recovery request
            │
            ▼
request remains replayable
            │
            ▼
state changes / later recovery attempt
            │
            ▼
old request replayed
            │
            ▼
recovery state disrupted
            │
            ▼
legitimate account recovery blocked
```

### Security impact

- Persistent recovery denial of service
- Replay of previously valid authenticated state transitions
- Critical account-recovery functionality can be blocked
- State-machine freshness / replay-protection weakness

### Result

```text
PLATFORM    Code4rena
AUDIT       Swafe
FINDING     M-04 / S-855
SEVERITY    Medium
PLACEMENT   #30
```

The issue was included in Code4rena's final Swafe report and the mitigation was later confirmed.

[![Finding](https://img.shields.io/badge/View-Finding_S--855-58A6FF?style=for-the-badge)](https://code4rena.com/audits/2025-11-swafe/submissions/S-855)
[![Final Report](https://img.shields.io/badge/Code4rena-Final_Report-24292F?style=for-the-badge)](https://code4rena.com/reports/2025-11-swafe)

---

## `$ security --methodology`

My security work follows the same correctness-first approach I use in systems engineering.

```text
identify invariant
       │
       ▼
map state transitions
       │
       ▼
inspect trust boundaries
       │
       ▼
search edge conditions
       │
       ▼
construct adversarial path
       │
       ▼
reproduce impact
       │
       ▼
document evidence
```

Whether the target is a compiler pass, validation layer, firmware boundary, cryptographic primitive, or protocol state machine, the underlying questions are similar:

> **What assumptions does the system make, where can those assumptions break, and how can the failure be demonstrated reproducibly?**

---

# Engineering Case Files

<details>
<summary><b>CASE 01 — Vulkan Validation Layers / Out-of-Bounds Crash</b></summary>

<br>

### Symptom

Malformed pipeline state could reach static descriptor validation and trigger an out-of-bounds access.

### Root cause

The shader's statically declared descriptor array length could exceed the pipeline-layout binding count.

If an invalid pipeline reached draw-time validation, the validator could access:

```cpp
binding.descriptors[index]
```

with `index >= binding.count`.

### Resolution

The validation path now terminates safely before consuming inconsistent descriptor state.

### Verification

A dedicated C++ regression test exercises the failure scenario and protects against reintroduction.

```text
ROOT CAUSE   isolated
FIX          upstreamed
REGRESSION   added
REVIEW       approved
CI           passed
STATUS       MERGED ✓
```

[**Read full case study →**](https://github.com/Yudis-bit/opencode/blob/main/case-studies/vulkan-validation-crash-fix.md)

[**View upstream PR →**](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743)

</details>

<br>

<details>
<summary><b>CASE 02 — QEMU x86_64 / Segment Prefix Validation</b></summary>

<br>

### Problem

QEMU's x86_64 decoding behavior around legacy segment override prefixes required validation against long-mode semantics.

### Contribution

I independently exercised the fix and provided testing confidence before it landed upstream.

### Result

```text
UPSTREAM    QEMU
ARCH        x86_64
ROLE        Independent validation
CREDIT      Tested-by: Yudistira Putra
STATUS      MERGED ✓
```

[**View upstream commit →**](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a)

</details>

<br>

<details>
<summary><b>CASE 03 — ECC / Differential Testing Infrastructure</b></summary>

<br>

`ecc-audit-engine` explores reproducible testing of elliptic-curve implementations.

```text
generate
   │
   ▼
execute
   │
   ▼
compare
   │
   ▼
detect mismatch
   │
   ▼
minimize
   │
   ▼
replay
   │
   ▼
report
```

The goal is not simply to detect differences.

The goal is to reduce them into deterministic, inspectable, replayable evidence.

[**Explore ecc-audit-engine →**](https://github.com/Yudis-bit/ecc-audit-engine)

</details>

<br>

<details>
<summary><b>CASE 04 — Swafe / Recovery Request Replay</b></summary>

<br>

### Invariant

A recovery request should only be valid for the recovery state it was created for.

### Failure mode

Previously valid authenticated recovery requests were replayable because the signed message lacked sufficient freshness/state binding.

### Impact

An attacker could repeatedly interfere with the recovery process and prevent legitimate account recovery.

### Resolution

The protocol mitigation added counters/state binding so each recovery request is valid only for the state version it targets.

```text
DOMAIN      Account Recovery
CLASS       Replay / State-Machine Correctness
SEVERITY    Medium
RESULT      Validated Finding
MITIGATION  Confirmed
```

[**View Code4rena finding →**](https://code4rena.com/audits/2025-11-swafe/submissions/S-855)

</details>

---

# Systems Stack

<div align="center">

### Core Languages

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Systems / Toolchains

![LLVM](https://img.shields.io/badge/LLVM-262D3A?style=for-the-badge&logo=llvm&logoColor=white)
![Vulkan](https://img.shields.io/badge/Vulkan-AC162C?style=for-the-badge&logo=vulkan&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![RISC-V](https://img.shields.io/badge/RISC--V-283272?style=for-the-badge&logo=riscv&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

---

# Technical Focus

| Domain | Focus |
|:---|:---|
| **Compilers** | Backend correctness · optimizer behavior · MIR regression testing |
| **GPU / Graphics** | Vulkan validation · crash debugging · boundary correctness |
| **Virtualization** | ISA behavior · x86_64 decoding · QEMU validation |
| **Firmware** | Bounds safety · RISC-V · OpenSBI |
| **Cryptographic Software** | Constant-time assurance · differential testing |
| **Security Research** | Invariants · replay protection · protocol state machines |
| **Regression Infrastructure** | Reproduction · minimization · replay · CI |
| **Open Source** | Upstream review · focused fixes · independent validation |

---

# How I Debug

```text
                     ┌─────────────┐
                     │   OBSERVE   │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │  REPRODUCE  │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │   REDUCE    │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │ UNDERSTAND  │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │    PATCH    │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │ REGRESSION  │
                     │    TEST     │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │  UPSTREAM   │
                     │   REVIEW    │
                     └─────────────┘
```

> I prefer small, reviewable changes backed by reproducible evidence.

The goal is not simply to make a failure disappear.

The goal is to understand **why it happened**, demonstrate it reliably, and leave behind coverage that makes the same class of regression harder to reintroduce.

---

# Engineering Activity

```text
UPSTREAM
├── Vulkan VVL
│   └── merged
│
├── LLVM AMDGPU
│   └── open · reviewer approved
│
├── QEMU x86_64
│   └── merged · Tested-by
│
├── secp256k1
│   └── open · under review
│
├── OpenSBI
│   └── open · awaiting review
│
└── Linux
    └── merged ×2


RESEARCH / TOOLING
├── ecc-audit-engine
│   └── cryptographic differential testing
│
├── ArkheionX
│   └── reproducible security-review infrastructure
│
└── Code4rena / Swafe
    └── Medium severity recovery replay finding
```

---

# Current Focus

```text
$ ps --engineering

PID   AREA                      STATE
001   LLVM / AMDGPU             upstream-review
002   secp256k1                 constant-time-testing
003   OpenSBI / RISC-V          firmware-correctness
004   ecc-audit-engine          active-development
005   regression tooling        research
006   systems debugging         active
```

- LLVM AMDGPU correctness
- secp256k1 constant-time assurance
- RISC-V / OpenSBI firmware safety
- Cryptographic differential testing
- Regression-test design
- Reproducible systems debugging
- Upstream open-source engineering

---

# Open to Engineering Opportunities

I'm interested in **full-time, contract, and scoped engineering opportunities** involving:

```text
Systems Software
│
├── C / C++ / Rust
│
├── Compiler Engineering
│   └── LLVM / backend correctness
│
├── GPU / Graphics Infrastructure
│   └── Vulkan / validation
│
├── Virtualization
│   └── QEMU / x86
│
├── Firmware
│   └── RISC-V / OpenSBI
│
├── Cryptographic Software
│   └── testing / correctness
│
├── Regression Infrastructure
│   └── reproduce / minimize / replay
│
├── Security-Critical Software
│
└── Difficult Cross-Layer Debugging
```

Particularly interested in problems where failures are subtle, reproducibility matters, and correctness must be **demonstrated rather than assumed**.

---

<div align="center">

## Let's build reliable systems.

[![Email](https://img.shields.io/badge/Email-Let's_Talk-58A6FF?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pyudistira519@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yudistira-putra-dev/)

<br><br>

```text
$ ./engineer --mode=correctness

[+] reproduce
[+] understand
[+] test
[+] upstream

ready.
```

### Systems · Compilers · GPU · Virtualization · Firmware · Cryptographic Software

</div>