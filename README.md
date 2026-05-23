<div align="center">
  <h1>Yudistira Putra</h1>
  <p><b>Smart Contract Security Researcher · EVM / SVM / MoveVM</b></p>
  <p><i>Manual, opcode-level analysis. Deterministic PoCs. Invariant-driven validation.</i></p>

  <p>
    <a href="https://github.com/Yudis-bit"><img src="https://img.shields.io/badge/GitHub-Yudis--bit-181717?style=flat-square&logo=github" /></a>
    <a href="https://www.linkedin.com/in/yudistira-putra-dev/"><img src="https://img.shields.io/badge/LinkedIn-yudistira--putra--dev-0A66C2?style=flat-square&logo=linkedin" /></a>
    <img src="https://img.shields.io/badge/Foundry-Invariant_Fuzzing-ff6633?style=flat-square" />
    <img src="https://img.shields.io/badge/Halmos-Formal_Verification-7c3aed?style=flat-square" />
  </p>
</div>

---

## What I Do

I work on three classes of problems: (1) re-engineering historical DeFi exploits as deterministic, assertion-hardened PoCs that survive regression; (2) auditing live protocols at the state-transition and account-model level — EVM, Solana/Anchor, and Move; (3) building executable enforcement layers where governance and human review are not enough. The common thread is treating security as a property to be proven, not asserted — through invariants, hard assertions, and reproducible traces rather than surface-level checks.

---

## Research Archive — Arkheionx Vault

[`Yudis-bit/DeFi-Exploit-PoCs`](https://github.com/Yudis-bit/DeFi-Exploit-PoCs) — independent archive of historical DeFi exploits, re-engineered with reproducibility, assertion quality, and root-cause analysis as first-class concerns. Every entry is gated through a maturity model so that "a PoC exists" is not the same claim as "a PoC is verified."

**Maturity model (L0 → L5):** raw replay → structured metadata → assertion-hardened → public-RPC smoke-tested → archival-verified → research-grade case study. Promotion between levels is gated by [`scripts/poc_maturity_index.py`](https://github.com/Yudis-bit/DeFi-Exploit-PoCs/blob/main/scripts/poc_maturity_index.py), not by self-attestation.

**Current corpus** ([`reports/research_dashboard.md`](https://github.com/Yudis-bit/DeFi-Exploit-PoCs/blob/main/reports/research_dashboard.md)):

| Metric | Value |
|---|---|
| Total PoCs | 18 |
| Assertion-hardened (medium / strong) | 11 |
| Maturity distribution | L1: 7 · L2: 10 · L3: 1 |
| Severity coverage | Critical: 10 · High: 8 |
| Categories represented | 11 (access-control, AMM-invariant, flash-loan price manipulation, reentrancy, oracle manipulation, governance, initialization, accounting mismatch, arithmetic precision, invariant bypass, unsafe external call) |
| Public-RPC smoke attempted | 2 |

Sample entries: Parity Multisig (2017), SpankChain (2018), BeautyChain (2018), Bancor (2020), Uniswap V1 reentrancy (2020), Harvest Finance (2020), Yearn v1 DAI (2021), SushiSwap (2021), Indexed Finance (2021), Moonwell (2025), yETH (2025).

The repository is structured for three execution targets: EVM (Foundry, active), SVM (Anchor scaffold), MoveVM (Aptos scaffold). CI enforces metadata schema validation, EVM compilation, and dashboard regeneration.

---

## Validated Findings

External findings on live, in-scope bug bounty programs. Listed without disclosure of payout details.

- **Variational — Oracle Registry Bypass.** State-transition flaw in oracle registration logic permitting registry assumptions to be bypassed under specific call paths. Validated by the protocol team.
- **Hyperbridge — GET Timeout Prefix Mismatch.** Inconsistency between encoded request prefix and timeout-handler prefix on GET requests, breaking the symmetry the timeout path relied on. Validated by the protocol team.

---

## Technical Range

**EVM (Ethereum & L2s)**
- State transition dynamics; pre/post-condition reasoning at the storage-slot level
- Yul / opcode-level analysis; gas-refund and delegatecall abuse
- Proxy patterns: UUPS, Transparent, Diamond — initialization and upgrade-path bypasses
- Cross-contract state manipulation, callback-driven invariant violation
- Invariant fuzzing campaigns (Foundry, Echidna, Medusa); symbolic execution (Halmos)

**SVM (Solana)**
- Account-model validation: missing signer / owner / discriminator checks
- PDA derivation security; seed-collision and authority confusion
- CPI instruction ordering, re-entry through cross-program invocation
- Anchor-based audit workflow; Trident fuzzing

**MoveVM (Sui / Aptos)**
- Resource safety invariants; ability-graph reasoning (`key`, `store`, `copy`, `drop`)
- Integer truncation and arithmetic precision in liquidity math
- Type-reflection and generic-instantiation exploits
- Module-publishing and capability-leak patterns

---

## Tools & Infrastructure

- **Languages:** Solidity, Yul, Rust (Anchor), Move, Python, Bash
- **Frameworks:** Foundry, Hardhat, Solana CLI, Anchor, Sui CLI, Aptos CLI
- **Security:** Echidna, Halmos (FV), Medusa, Slither, Trident
- **CI/CD:** GitHub Actions for metadata schema validation, EVM compilation, and dashboard regeneration

---

## Other Projects

- **[`arkheoinx`](https://github.com/Yudis-bit/arkheoinx)** — Deterministic EVM execution firewall for Safe treasuries. Immutable `ArkheionxGuard` / `ArkheionxModuleGuard` cores with timelocked `PolicyRegistry` and `AdapterRegistry` adapters bound by codehash pinning. Foundry invariant suite survived 512,000+ adversarial calls with zero ghost violations against guard removal, module mutation, owner mutation, fallback handler mutation, unlimited approvals, delegatecall, gas-refund abuse, and value drains.

- **[`Cognitive-Routing-Protocol`](https://github.com/Yudis-bit/Cognitive-Routing-Protocol)** — Prototype routing protocol for DePIN networks combining a reinforcement-learning simulator (Python) with on-chain trust and incentive primitives (Solidity). Comparative simulation showed ~22% lower average latency on successful packet deliveries against the baseline, with the cognitive router using a congested link <0.1% of the time.

---

## Contact

- LinkedIn — [`yudistira-putra-dev`](https://www.linkedin.com/in/yudistira-putra-dev/)
- GitHub — [`Yudis-bit`](https://github.com/Yudis-bit)

Open to: protocol audit engagements, bug bounty collaboration, security research roles.
