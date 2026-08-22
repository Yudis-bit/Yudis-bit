<div align="center">

# Yudistira Putra

### Systems Software Engineer · Low-Level Engineering · Correctness

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2600&pause=900&color=58A6FF&center=true&vCenter=true&width=760&lines=C+%C2%B7+C%2B%2B+%C2%B7+Rust;Compilers+%C2%B7+GPU+Validation;Virtualization+%C2%B7+x86;RISC-V+Firmware;Cryptographic+Correctness;Reproduce+%E2%86%92+Understand+%E2%86%92+Test+%E2%86%92+Upstream" alt="Systems engineering focus" />

<br>

Correctness-focused systems engineer working across  
**compilers · GPU validation · virtualization · firmware · cryptographic software**

<br>

[![Email](https://img.shields.io/badge/EMAIL-CONTACT-24292F?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pyudistira519@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yudistira-putra-dev/)
[![GitHub](https://img.shields.io/badge/GITHUB-YUDIS--BIT-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Yudis-bit)

<br>

![C](https://img.shields.io/badge/C-Systems-555555?style=flat-square&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-Systems-555555?style=flat-square&logo=cplusplus&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-Systems-555555?style=flat-square&logo=rust&logoColor=white)
![LLVM](https://img.shields.io/badge/LLVM-Compiler-555555?style=flat-square&logo=llvm&logoColor=white)
![Vulkan](https://img.shields.io/badge/Vulkan-GPU-555555?style=flat-square&logo=vulkan&logoColor=white)
![QEMU](https://img.shields.io/badge/QEMU-x86__64-555555?style=flat-square)
![RISC-V](https://img.shields.io/badge/RISC--V-Firmware-555555?style=flat-square&logo=riscv&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Upstream-555555?style=flat-square&logo=linux&logoColor=white)

</div>

---

## `$ whoami`

I work on **correctness-critical systems software**, with an emphasis on reproducing difficult failures, isolating root causes, building regression coverage, and contributing narrowly scoped fixes or validation upstream.

My current work spans **C, C++, and Rust** across compiler backends, GPU and graphics validation, virtualization, RISC-V firmware, and cryptographic testing infrastructure.

```text
$ focus

systems correctness
reproducible debugging
compiler behavior
GPU validation
virtualization / x86
firmware safety
cryptographic testing
```

---

# Upstream Engineering

<div align="center">

### Production codebases · Reproducible failures · Reviewable changes

</div>

<table>
<tr>
<td width="50%" valign="top">

### Khronos · Vulkan Validation Layers

**GPU Validation · C++**

Out-of-bounds crash in static descriptor validation.

**Contribution**
- Root-cause investigation
- Defensive correctness fix
- Dedicated C++ regression test
- Upstream review iteration

**Status:** `MERGED ✓`

[**PR #12743 →**](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743)

</td>

<td width="50%" valign="top">

### LLVM · AMDGPU

**Compiler Backend · C++ / MIR**

TFE/LWE image loads entering invalid `SILoadStoreOptimizer` merge candidates.

**Contribution**
- Correctness guard
- MIR regression coverage
- Rebase against current upstream tree
- Upstream review iteration

**Status:** `OPEN · REVIEWED ◉`

[**PR #210583 →**](https://github.com/llvm/llvm-project/pull/210583)

</td>
</tr>

<tr>
<td width="50%" valign="top">

### QEMU · x86_64

**Virtualization · ISA Validation**

Independent regression validation for incorrect long-mode segment override decoding.

**Contribution**
- Behavioral validation
- Regression testing
- Upstream testing feedback
- Permanent upstream testing credit

**Status:** `MERGED UPSTREAM ✓`

```text
Tested-by: Yudistira Putra
```

[**Upstream commit →**](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a)

</td>

<td width="50%" valign="top">

### bitcoin-core · secp256k1

**Cryptographic Software · C**

Missing constant-time coverage for `schnorrsig_sign_custom`.

**Contribution**
- Extended `ctime_tests.c`
- Custom nonce callback coverage
- Auxiliary-data coverage
- Variable-message coverage
- Valgrind / CHECKMEM validation

**Status:** `UNDER REVIEW ◉`

[**PR #1893 →**](https://github.com/bitcoin-core/secp256k1/pull/1893)

</td>
</tr>

<tr>
<td width="50%" valign="top">

### OpenSBI · RISC-V

**Firmware · C**

Fixed-size firmware queue-name storage could receive an unbounded copy.

**Contribution**
- Length clamp
- Explicit null termination
- Minimal bounds-safety change

**Status:** `OPEN · AWAITING REVIEW ○`

[**PR #423 →**](https://github.com/riscv-software-src/opensbi/pull/423)

</td>

<td width="50%" valign="top">

### Linux

**Tracing · ftrace**

Small upstream documentation and sample cleanups.

**Contribution**
- 2 upstream commits

**Status:** `MERGED ×2 ✓`

[**e5d8524 →**](https://github.com/torvalds/linux/commit/e5d8524)

[**8a66c09 →**](https://github.com/torvalds/linux/commit/8a66c09)

</td>
</tr>
</table>

---

## `$ upstream --signal`

```text
Vulkan VVL     ████████████████████████  MERGED
LLVM AMDGPU    ███████████████████░░░░░  REVIEWED / OPEN
QEMU x86_64    ████████████████████████  MERGED · TESTED-BY
secp256k1      ████████████████░░░░░░░░  UNDER REVIEW
OpenSBI        ████████████░░░░░░░░░░░░  AWAITING REVIEW
Linux          ████████████████████████  MERGED ×2
```

---

# Selected Upstream Highlights

## 01 · Vulkan Validation Layers

```text
malformed pipeline state
        │
        ▼
static descriptor validation
        │
        ▼
unsafe validation path
        │
        ▼
out-of-bounds access
        │
        ▼
crash
        │
        ▼
root-cause fix
        │
        ▼
regression test
        │
        ▼
upstream review
        │
        ▼
MERGED ✓
```

**Contribution**
- Investigated the failing validation path
- Isolated the unsafe descriptor-validation behavior
- Added a narrowly scoped defensive fix
- Added dedicated C++ regression coverage
- Iterated through Khronos upstream review

[**View PR #12743 →**](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743)

---

## 02 · LLVM AMDGPU

```text
TFE / LWE image load
        │
        ▼
SILoadStoreOptimizer
        │
        ▼
invalid merge candidate
        │
        ▼
correctness guard
        │
        ▼
MIR regression coverage
```

**Contribution**
- Added a correctness guard
- Added MIR regression coverage
- Rebased against upstream changes
- Iterated through AMDGPU review

[**View PR #210583 →**](https://github.com/llvm/llvm-project/pull/210583)

---

## 03 · QEMU x86_64

Independent validation of an x86_64 long-mode decoding fix involving legacy segment override prefixes.

```text
legacy segment prefix
          │
          ▼
    x86_64 decoder
          │
          ▼
  incorrect behavior
          │
          ▼
     upstream fix
          │
          ▼
independent validation
          │
          ▼
      MERGED ✓
```

The final upstream commit permanently records:

```text
Tested-by: Yudistira Putra
```

This contribution is **testing and validation credit**, not authorship of the underlying QEMU patch.

[**View upstream commit →**](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a)

---

# Flagship Engineering

<table>
<tr>
<td width="50%" valign="top">

## [ecc-audit-engine](https://github.com/Yudis-bit/ecc-audit-engine)

### Cryptographic Differential Testing

Research-oriented infrastructure for reproducible investigation of secp256k1 implementations.

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
   minimization
        │
        ▼
 replay + report
```

**Engineering focus**
- Differential testing
- Deterministic reproduction
- Synthetic corrupted targets
- Failure minimization
- Replayable evidence
- Structured reporting
- CI regression coverage

**30 tests · 3 releases · Active CI**

[**Repository →**](https://github.com/Yudis-bit/ecc-audit-engine)

[**Latest release →**](https://github.com/Yudis-bit/ecc-audit-engine/releases/latest)

[**Quick demo →**](https://github.com/Yudis-bit/ecc-audit-engine/blob/main/examples/quick-demo.sh)

</td>

<td width="50%" valign="top">

## [ArkheionX](https://github.com/Yudis-bit/arkheionx)

### Local-First Review Infrastructure

Infrastructure for producing structured and reproducible security evidence without requiring sensitive repositories to leave the local environment.

```text
 source / findings
        │
        ▼
deterministic evidence
        │
        ▼
 portable review pack
        │
        ▼
 offline inspection
```

**Engineering focus**
- Deterministic fixtures
- Evidence packaging
- Local-first workflows
- Reproducibility
- Privacy-preserving output
- Automated testing

**44 releases · CI-backed**

[**Repository →**](https://github.com/Yudis-bit/arkheionx)

</td>
</tr>
</table>

---

# Engineering Case Files

<details>
<summary><b>01 — Vulkan Validation Layers / Out-of-Bounds Crash</b></summary>

<br>

### Symptom

Malformed pipeline state could drive static descriptor validation into an unsafe access path.

```text
malformed state
      │
      ▼
validation path
      │
      ▼
unsafe access
      │
      ▼
OOB crash
```

### Investigation

The failure was reduced to an unsafe path inside static descriptor validation.

### Fix

A narrowly scoped defensive change prevents invalid state from reaching the unsafe access.

### Verification

Dedicated C++ regression coverage reproduces the failure path and protects against reintroduction.

### Result

```text
UPSTREAM : KhronosGroup/Vulkan-ValidationLayers
STATUS   : MERGED ✓
```

[**Read case study →**](https://github.com/Yudis-bit/opencode/blob/main/case-studies/vulkan-validation-crash-fix.md)

[**View upstream PR →**](https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743)

</details>

<br>

<details>
<summary><b>02 — QEMU x86_64 / Segment Prefix Regression Validation</b></summary>

<br>

Independent validation of a QEMU x86_64 fix involving legacy segment override prefixes in long mode.

```text
legacy prefix
     │
     ▼
x86_64 decoder
     │
     ▼
incorrect behavior
     │
     ▼
upstream fix
     │
     ▼
validation
     │
     ▼
MERGED ✓
```

The resulting upstream commit records:

```text
Tested-by: Yudistira Putra
```

This work focused on behavioral validation and regression confidence rather than authorship of the underlying patch.

[**View upstream commit →**](https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a)

</details>

<br>

<details>
<summary><b>03 — ECC / Differential Testing Infrastructure</b></summary>

<br>

`ecc-audit-engine` explores reproducible testing of elliptic-curve implementations.

```text
generate inputs
      │
      ▼
execute targets
      │
      ▼
compare behavior
      │
      ▼
detect mismatch
      │
      ▼
minimize failure
      │
      ▼
replay evidence
```

The emphasis is not only on discovering mismatches, but on turning failures into deterministic and reviewable evidence.

[**Explore ecc-audit-engine →**](https://github.com/Yudis-bit/ecc-audit-engine)

</details>

---

# Systems Stack

<div align="center">

### Core Languages

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Systems & Toolchains

![LLVM](https://img.shields.io/badge/LLVM-Compiler-262D3A?style=for-the-badge&logo=llvm&logoColor=white)
![Vulkan](https://img.shields.io/badge/Vulkan-Validation-AC162C?style=for-the-badge&logo=vulkan&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Systems-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![RISC-V](https://img.shields.io/badge/RISC--V-Firmware-283272?style=for-the-badge&logo=riscv&logoColor=white)
![Git](https://img.shields.io/badge/Git-Upstream-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

---

# Technical Focus

| Domain | Focus |
|:---|:---|
| **Compilers** | Backend correctness · optimizer behavior · MIR regression testing |
| **GPU / Graphics** | Validation layers · crash debugging · correctness |
| **Virtualization** | ISA behavior · x86_64 validation · QEMU |
| **Firmware** | Bounds safety · RISC-V · OpenSBI |
| **Cryptographic Software** | Constant-time testing · differential testing |
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

The goal is to understand **why it happened**, reproduce it reliably, and leave behind coverage that makes the same class of regression harder to reintroduce.

---

# Current Work

```text
$ ps --engineering

PID   AREA                     STATE
001   LLVM / AMDGPU            upstream-review
002   secp256k1                constant-time-testing
003   OpenSBI / RISC-V         firmware-correctness
004   ecc-audit-engine         active-development
005   regression tooling       research
```

### Active Focus

- LLVM AMDGPU correctness work
- secp256k1 constant-time assurance
- RISC-V / OpenSBI firmware safety
- ECC differential-testing infrastructure
- Systems regression-test design
- Reproducible debugging workflows

---

# GitHub Activity

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Yudis-bit&show_icons=true&hide_border=true&bg_color=00000000&title_color=58A6FF&text_color=8B949E&icon_color=58A6FF" alt="GitHub statistics" />

<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Yudis-bit&layout=compact&hide_border=true&bg_color=00000000&title_color=58A6FF&text_color=8B949E&langs_count=8" alt="Top languages" />

</div>

---

# Open to Engineering Opportunities

I'm interested in **full-time, contract, and scoped engineering opportunities** involving:

```text
Systems Software
│
├── C / C++ / Rust
├── Compiler Engineering
├── GPU / Graphics Infrastructure
├── Virtualization
├── x86 / ISA Validation
├── RISC-V / Firmware
├── Correctness Engineering
├── Regression Testing
├── Security-Critical Software
└── Difficult Cross-Layer Debugging
```

Particularly interested in problems where failures are subtle, reproducibility matters, and correctness must be **demonstrated rather than assumed**.

<div align="center">

## Let's build reliable systems.

[![Email](https://img.shields.io/badge/EMAIL-LET'S_TALK-58A6FF?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pyudistira519@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yudistira-putra-dev/)

</div>

---

<div align="center">

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