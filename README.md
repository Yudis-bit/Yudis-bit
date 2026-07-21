# Yudistira Putra

Systems Software Engineer

Compilers, GPU drivers, Linux kernel, firmware, and virtualization.

`pyudistira519@gmail.com` · [GitHub](https://github.com/Yudis-bit) · [LinkedIn](https://www.linkedin.com/in/yudistira-putra-dev/)

---

## Verified Upstream Contributions

| Project | Area | Status | Contribution |
| :--- | :--- | :---: | :--- |
| **Khronos Vulkan Validation Layers** | Validation Layers | **Merged** | Fixed static descriptor set array index out-of-bounds crash (`VVL-12294` / PR #12743) and added C++ regression tests. |
| **LLVM** | AMDGPU Backend | **Approved (Pending Merge)** | Prevented invalid `SILoadStoreOptimizer` memory instruction merging on TFE/LWE image loads (`collectMergeableInsts()`). |
| **Linux Kernel** | Kernel Subsystems | **Accepted** | Upstream patch accepted into maintainer tree. |
| **OpenSBI** | RISC-V Firmware | **Pending Review** | Clamped string buffer boundaries in `sbi_ecall_get_extensions_str` (`0001-lib-sbi-clamp`). |
| **QEMU** | x86_64 Emulation | **Tested-by** | Functional testing and bug isolation for x86 long mode segment prefix decoding (`#3391`). |
| **Bitcoin Core `libsecp256k1`** | Crypto Primitives | **Contributor** | Authored dynamic differential testing harness (`ecc-audit-engine`) for EC math primitives. |

---

## Current Focus

- **Compilers**: LLVM backend code generation, `SelectionDAG`, machine instruction pass optimizations (`SILoadStoreOptimizer`), and ABI enforcement.
- **Graphics & GPU Drivers**: Vulkan API validation rules, descriptor set memory boundaries, and AMDGPU vector memory instruction constraints.
- **Kernel & Firmware**: Linux kernel maintainer tree patches, dynamic tracing (`ftrace`), and RISC-V OpenSBI `ecall` handlers.
- **Virtualization**: QEMU instruction decoding and x86 long mode segment override prefix handling.

---

## Engineering Approach

- Understand root causes before proposing fixes.
- Target-specific regression tests (`.ll` assembly, GoogleTest, C reproducers) are part of the fix.
- Small, reviewable patches are preferred over large architectural rewrites.

---

## Engineering Timeline

Bitcoin Core (`libsecp256k1`)
↓
Linux Kernel & QEMU
↓
LLVM (`AMDGPU`)
↓
Khronos Vulkan Validation Layers
↓
OpenSBI (`RISC-V`)

---

## Repositories

- **[`Yudis-bit/ecc-audit-engine`](https://github.com/Yudis-bit/ecc-audit-engine)** — Dynamic differential testing, failure minimization, and trace runner for `secp256k1` C primitives.
- **[`Yudis-bit/arkheionx`](https://github.com/Yudis-bit/arkheionx)** — Local-first review infrastructure and bytecode execution analyzer.
- **[`Yudis-bit/Vulkan-ValidationLayers`](https://github.com/Yudis-bit/Vulkan-ValidationLayers)** — Fork containing descriptor set validation fixes and validation test suite additions.
- **[`Yudis-bit/llvm-project`](https://github.com/Yudis-bit/llvm-project)** — Fork containing LLVM AMDGPU `SILoadStoreOptimizer` refactoring and RISC-V ABI fixes.
- **[`Yudis-bit/opensbi`](https://github.com/Yudis-bit/opensbi)** — Fork containing RISC-V Supervisor Binary Interface extension buffer clamping.
