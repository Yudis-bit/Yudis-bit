# Yudistira Putra

Systems Software Engineer working across compilers, GPU drivers, Linux kernel, firmware, and virtualization. Focused on toolchain correctness, low-level ABI enforcement, GPU runtime validation, and memory safety.

`pyudistira519@gmail.com` · [GitHub](https://github.com/Yudis-bit) · [LinkedIn](https://www.linkedin.com/in/yudistira-putra-dev/)

---

## Current Focus

- **Compilers & Toolchains**: LLVM backend code generation, SelectionDAG, machine instruction pass optimizations (`SILoadStoreOptimizer`), and ABI constraint validation under dynamic tracing (`"patchable-function-entry"` / `ftrace`).
- **Graphics & GPU Drivers**: Vulkan API validation rules, descriptor set memory boundary checks, and AMDGPU vector memory instruction merging (TFE/LWE sampling flags).
- **Kernel & Firmware**: Linux kernel maintainer tree patches, dynamic tracing trampolines, and RISC-V OpenSBI Supervisor Binary Interface (`ecall`) handlers.
- **Virtualization**: QEMU instruction decoding and x86 long mode segment override prefix handling in 64-bit user mode.

---

## Verified Upstream Contributions

| Subsystem | Change Summary | Upstream Review & Architectural Detail | Status |
| :--- | :--- | :--- | :---: |
| **Khronos Vulkan Validation Layers** | Descriptor validation out-of-bounds crash fix | Fixed static descriptor set array index out-of-bounds access (`VVL-12294` / PR #12743). Added C++ regression tests to Khronos test suite. | **Merged** |
| **LLVM (AMDGPU Backend)** | TFE/LWE image-load merge rejection | Prevented invalid `SILoadStoreOptimizer` memory instruction merging on AMDGPU. Refactored into `collectMergeableInsts()` per reviewer feedback. Added `.ll` regression tests. | **Approved** *(Pending Merge)* |
| **Linux Kernel** | Kernel patch accepted into maintainer tree | Patch addressing kernel subsystem behavior accepted into maintainer tree. | **Accepted** |
| **OpenSBI (RISC-V Firmware)** | Extension buffer clamping boundary fix | Clamped string buffer boundaries in `sbi_ecall_get_extensions_str` (`0001-lib-sbi-clamp`) to prevent buffer overruns during SBI extension queries. | **Pending Review** |
| **QEMU (Virtualization)** | x86 long mode segment prefix decoding | Verified segment prefix override decoding in 64-bit user mode (`GitLab #3391`). Issued public `Tested-by`. | **Tested-by** |
| **Bitcoin Core `libsecp256k1`** | Dynamic regression testing & differential harness | Authored C/Python dynamic trace runner and differential testsuite (`ecc-audit-engine`) for EC math primitives. | **Contributor** |

---

## Architecture & Subsystem Touchpoints

<div align="center">
  <img src="./assets/systems-stack.svg" alt="Systems Software Execution & Toolchain Architecture" width="100%" />
</div>

---

## Upstream Engineering Progression

```
[2024 - 2025] Bitcoin Core (libsecp256k1)
              └── Dynamic differential testing & EC math regression harness
      │
      ▼
[2025 - 2026] Linux Kernel & QEMU
              └── Segment prefix decoding verification & maintainer patch submission
      │
      ▼
[2026]        LLVM (AMDGPU Backend)
              └── SILoadStoreOptimizer TFE/LWE merging & ABI patchable-function-entry
      │
      ▼
[2026]        Khronos Vulkan Validation Layers
              └── Descriptor set boundary checks & merged regression tests
      │
      ▼
[2026]        OpenSBI (RISC-V Firmware)
              └── SBI ecall extension string buffer safety patches
```

---

## Engineering Approach

- **Root Cause Isolation**: Bugs are isolated to precise machine instructions, compiler passes, or ABI specification mismatches before writing code.
- **Regression Testing First**: Every fix includes a target-specific test case (`.ll` assembly for LLVM, GoogleTest / C++ for Vulkan, C reproducers for kernel and OpenSBI).
- **Upstream Code Review**: Maintainer feedback is incorporated directly into pass architecture and interface design.
- **Correctness Over LOC**: Priority is placed on small, well-bounded patches that enforce hard system invariants without side effects.

---

## Primary Repositories

- **[`Yudis-bit/ecc-audit-engine`](https://github.com/Yudis-bit/ecc-audit-engine)** *(Original)* — Dynamic differential testing, failure minimization, and trace runner for `secp256k1` C primitives.
- **[`Yudis-bit/arkheionx`](https://github.com/Yudis-bit/arkheionx)** *(Original)* — Local-first review infrastructure and bytecode execution analyzer.
- **[`Yudis-bit/Vulkan-ValidationLayers`](https://github.com/Yudis-bit/Vulkan-ValidationLayers)** *(Fork)* — Upstream patch branch for Khronos VVL descriptor set boundary checks and validation test suite additions.
- **[`Yudis-bit/llvm-project`](https://github.com/Yudis-bit/llvm-project)** *(Fork)* — Upstream patch branch for LLVM AMDGPU `SILoadStoreOptimizer` refactoring and RISC-V ABI fixes.
- **[`Yudis-bit/opensbi`](https://github.com/Yudis-bit/opensbi)** *(Fork)* — Patch branch for RISC-V Supervisor Binary Interface extension buffer clamping.

---

## Technical Domain Overview

### Compilers & Toolchains
- **Frameworks**: LLVM Core, Clang, SelectionDAG, Target Lowering, MachineInstruction passes, `MachineVerifier`.
- **ABI & Dynamic Tracing Mismatches**: Analyzing interprocedural optimizations against dynamic tracing trampolines (`ftrace` / `"patchable-function-entry"`), caller-saved register clobbering (`x7`/`t2`), and stack alignment rules.
- **Architectures**: AMDGPU (RDNA / GFX9+), RISC-V (RV64GC), x86_64, AArch64.

### Graphics & GPU Drivers
- **Validation Layers**: Vulkan API validation rules, descriptor set index bounds checking, resource lifecycle checks, SPIR-V environment constraints.
- **GPU Memory & ISA**: AMDGPU vector memory instructions (`IMAGE_LOAD` / `IMAGE_SAMPLE`), TFE (Texture Fail Enable) and LWE (LOD Warning Enable) flag handling in optimizer passes.

### Kernel, Firmware & Hypervisors
- **Linux Kernel**: Tracing subsystem, syscall wrappers, memory safety invariants, maintainer tree submissions.
- **OpenSBI**: RISC-V Supervisor Binary Interface, SBI `ecall` dispatching, extension string buffer boundaries.
- **QEMU**: User-mode TCG translation, x86_64 64-bit segment override decoding (CS, DS, ES, SS).
