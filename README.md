<div align="center">Yudistira Putra

Systems Software Engineer

<img
src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=19&duration=2800&pause=900&color=58A6FF&center=true&vCenter=true&repeat=true&width=760&lines=C+%2F+C%2B%2B+%2F+Rust+Systems;Compiler+%26+GPU+Validation;Virtualization+%26+x86;RISC-V+Firmware;Cryptographic+Correctness;Reproducible+Debugging"
alt="Systems Engineering Focus"
/>

<br/>Correctness-focused systems engineer working across
compilers · GPU validation · virtualization · firmware · cryptographic software

<br/>""Email" (https://img.shields.io/badge/Email-Contact-24292f?style=for-the-badge&logo=gmail&logoColor=white)" (mailto:pyudistira519@gmail.com)
""LinkedIn" (https://img.shields.io/badge/LinkedIn-Yudistira_Putra-24292f?style=for-the-badge&logo=linkedin&logoColor=white)" (https://www.linkedin.com/in/yudistira-putra-dev/)
""GitHub" (https://img.shields.io/badge/GitHub-Yudis--bit-24292f?style=for-the-badge&logo=github&logoColor=white)" (https://github.com/Yudis-bit)

</div>---

"> whoami"

I work on correctness-critical systems software, with an emphasis on reproducing difficult failures, understanding root causes, building regression coverage, and contributing narrowly scoped fixes upstream.

My current work spans C, C++, and Rust across compiler backends, GPU and graphics validation, virtualization, RISC-V firmware, and cryptographic testing infrastructure.

$ focus

systems correctness
reproducible debugging
compiler behavior
GPU validation
virtualization / x86
firmware safety
cryptographic testing

---

"> upstream --selected"

Selected Upstream Engineering

<table>
<tr>
<td width="50%" valign="top">Khronos · Vulkan Validation Layers

GPU Validation · C++

Static descriptor validation could reach an out-of-bounds access path and crash.

Contribution

- Root-cause investigation
- Defensive correctness fix
- C++ regression coverage
- Upstream review iteration

Status: "MERGED ✓"

"PR #12743 →" (https://github.com/KhronosGroup/Vulkan-ValidationLayers/pull/12743)

</td><td width="50%" valign="top">LLVM · AMDGPU

Compiler Backend · C++ / MIR

TFE/LWE image loads could incorrectly enter "SILoadStoreOptimizer" merge candidates.

Contribution

- Correctness guard
- MIR regression coverage
- Rebase and upstream review iteration

Status: "OPEN · REVIEWER APPROVED ◉"

"PR #210583 →" (https://github.com/llvm/llvm-project/pull/210583)

</td>
</tr><tr>
<td width="50%" valign="top">QEMU · x86_64

Virtualization · ISA Validation

Independently validated a fix for incorrect long-mode handling of legacy segment override prefixes.

Contribution

- Regression validation
- Upstream testing feedback
- Permanent upstream testing credit

Status: "MERGED UPSTREAM ✓"

"Tested-by: Yudistira Putra"

"Upstream commit →" (https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a)

</td><td width="50%" valign="top">bitcoin-core · secp256k1

Cryptographic Software · C

Missing constant-time test coverage around "schnorrsig_sign_custom".

Contribution

- Extended "ctime_tests.c"
- Custom nonce callback coverage
- Auxiliary-data coverage
- Variable-message coverage
- Valgrind / CHECKMEM validation

Status: "UNDER REVIEW ◉"

"PR #1893 →" (https://github.com/bitcoin-core/secp256k1/pull/1893)

</td>
</tr><tr>
<td width="50%" valign="top">OpenSBI · RISC-V

Firmware · C

Fixed-size firmware queue-name storage could receive an unbounded copy.

Contribution

- Length clamp
- Explicit null termination
- Minimal bounds-safety patch

Status: "OPEN · AWAITING REVIEW ○"

"PR #423 →" (https://github.com/riscv-software-src/opensbi/pull/423)

</td><td width="50%" valign="top">Linux

Tracing / ftrace

Small upstream cleanups in Linux tracing documentation and samples.

Contribution

- 2 upstream commits

Status: "MERGED ×2 ✓"

"e5d8524 →" (https://github.com/torvalds/linux/commit/e5d8524)
"8a66c09 →" (https://github.com/torvalds/linux/commit/8a66c09)

</td>
</tr>
</table>---

"> ls flagship/"

Flagship Engineering Projects

<table>
<tr>
<td width="50%" valign="top">"ecc-audit-engine" (https://github.com/Yudis-bit/ecc-audit-engine)

Cryptographic differential-testing infrastructure

A research-oriented engine for reproducible investigation of secp256k1 implementations.

deterministic corpus
        ↓
target execution
        ↓
behavior comparison
        ↓
failure detection
        ↓
minimization
        ↓
replay + report

Engineering focus

- Differential testing
- Deterministic reproduction
- Synthetic corrupted targets
- Failure minimization
- Structured reporting
- CI-backed regression coverage

30 tests · 3 releases · Active CI

"Latest release →" (https://github.com/Yudis-bit/ecc-audit-engine/releases/latest)
"Quick demo →" (https://github.com/Yudis-bit/ecc-audit-engine/blob/main/examples/quick-demo.sh)

</td><td width="50%" valign="top">"ArkheionX" (https://github.com/Yudis-bit/arkheionx)

Local-first security review infrastructure

Infrastructure for creating structured and reproducible security evidence without requiring sensitive repositories to leave the local environment.

source / findings
        ↓
deterministic evidence
        ↓
portable review pack
        ↓
offline inspection

Engineering focus

- Deterministic fixtures
- Evidence packaging
- Local-first workflows
- Reproducibility
- Privacy-preserving output
- Automated testing

44 releases · CI-backed

"Explore repository →" (https://github.com/Yudis-bit/arkheionx)

</td>
</tr>
</table>---

"> cat case-studies/*"

Engineering Case Files

<details>
<summary><b>01 / Vulkan Validation Layers — Out-of-Bounds Crash</b></summary><br/>SYMPTOM
validation path crashes on malformed pipeline state

        ↓

INVESTIGATION
trace descriptor validation execution

        ↓

ROOT CAUSE
unsafe static descriptor validation path
reaches an out-of-bounds access

        ↓

FIX
terminate safely before invalid state is consumed

        ↓

VERIFICATION
dedicated C++ regression coverage

        ↓

UPSTREAM
KhronosGroup/Vulkan-ValidationLayers
MERGED ✓

"Read full case study →" (https://github.com/Yudis-bit/opencode/blob/main/case-studies/vulkan-validation-crash-fix.md)

</details><br/><details>
<summary><b>02 / QEMU x86_64 — Segment Prefix Regression Validation</b></summary><br/>Independent validation of an x86_64 long-mode decoding fix involving legacy segment override prefixes.

The resulting upstream QEMU commit permanently records:

Tested-by: Yudistira Putra

This work focused on behavioral validation and regression confidence, not authorship of the underlying patch.

"View upstream commit →" (https://github.com/qemu/qemu/commit/3589cd995b4facf34071e944fd8ec2294524e25a)

</details><br/><details>
<summary><b>03 / ECC Differential Testing</b></summary><br/>"ecc-audit-engine" explores reproducible techniques for comparing cryptographic implementations, constructing controlled failure cases, minimizing mismatches, and producing replayable evidence.

generate
   ↓
execute
   ↓
compare
   ↓
detect mismatch
   ↓
minimize
   ↓
replay

"Explore ecc-audit-engine →" (https://github.com/Yudis-bit/ecc-audit-engine)

</details>---

"> stack --systems"

<div align="center">"C" (https://img.shields.io/badge/C-Systems-24292f?style=flat-square&logo=c&logoColor=white)
"C++" (https://img.shields.io/badge/C%2B%2B-Systems-24292f?style=flat-square&logo=cplusplus&logoColor=white)
"Rust" (https://img.shields.io/badge/Rust-Systems-24292f?style=flat-square&logo=rust&logoColor=white)
"LLVM" (https://img.shields.io/badge/LLVM-Compiler-24292f?style=flat-square&logo=llvm&logoColor=white)
"Vulkan" (https://img.shields.io/badge/Vulkan-GPU-24292f?style=flat-square&logo=vulkan&logoColor=white)
"QEMU" (https://img.shields.io/badge/QEMU-Virtualization-24292f?style=flat-square)
"RISC-V" (https://img.shields.io/badge/RISC--V-Firmware-24292f?style=flat-square&logo=riscv&logoColor=white)
"Linux" (https://img.shields.io/badge/Linux-Systems-24292f?style=flat-square&logo=linux&logoColor=white)
"Git" (https://img.shields.io/badge/Git-Upstream-24292f?style=flat-square&logo=git&logoColor=white)

</div>Technical Focus

┌──────────────────────┬──────────────────────────┐
│ Compilers            │ correctness / backends   │
│ GPU / Graphics       │ validation / debugging   │
│ Virtualization       │ ISA / x86 behavior       │
│ Firmware             │ bounds safety / RISC-V   │
│ Cryptographic code   │ differential testing     │
│ Regression systems   │ reproduction / CI        │
└──────────────────────┴──────────────────────────┘

---

"> ps --active"

Current Focus

- LLVM AMDGPU correctness work
- secp256k1 constant-time assurance
- RISC-V / OpenSBI firmware safety
- ECC differential-testing infrastructure
- Regression-test design for difficult systems failures
- Reproducible debugging workflows

---

"> methodology"

How I Approach Systems Bugs

observe
   │
   ▼
reproduce
   │
   ▼
reduce
   │
   ▼
understand
   │
   ▼
patch
   │
   ▼
regression test
   │
   ▼
upstream review

I prefer small, reviewable changes backed by reproducible evidence.

The goal is not simply to make a failure disappear.

The goal is to understand why it happened, demonstrate the failure reliably, and leave behind coverage that makes the same class of regression harder to reintroduce.

---

"> github --activity"

<div align="center"><img
height="165"
src="https://github-readme-stats.vercel.app/api?username=Yudis-bit&show_icons=true&hide_border=true&bg_color=00000000&title_color=58A6FF&text_color=8B949E&icon_color=58A6FF&include_all_commits=true&count_private=true"
alt="GitHub Stats"
/>

<img
height="165"
src="https://github-readme-stats.vercel.app/api/top-langs/?username=Yudis-bit&layout=compact&hide_border=true&bg_color=00000000&title_color=58A6FF&text_color=8B949E&langs_count=8"
alt="Top Languages"
/>

</div>---

"> status --availability"

Open to Engineering Opportunities

I'm interested in full-time, contract, and scoped engineering opportunities involving:

- Systems software
- Low-level C / C++ / Rust
- Compiler and toolchain engineering
- GPU / graphics infrastructure
- Virtualization
- RISC-V / firmware
- Correctness and validation
- Regression-testing infrastructure
- Security-critical software
- Difficult cross-layer debugging

Particularly interested in problems where the failure is subtle, reproducibility matters, and correctness has to be demonstrated rather than assumed.

<div align="center">Let's build reliable systems.

""Email" (https://img.shields.io/badge/Email-Let's_Talk-58A6FF?style=for-the-badge&logo=gmail&logoColor=white)" (mailto:pyudistira519@gmail.com)
""LinkedIn" (https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)" (https://www.linkedin.com/in/yudistira-putra-dev/)

</div>---

<div align="center">$ ./engineer --mode=correctness

reproduce.
understand.
test.
upstream.

█

<sub>
Systems · Compilers · GPU · Virtualization · Firmware · Cryptographic Software
</sub></div>