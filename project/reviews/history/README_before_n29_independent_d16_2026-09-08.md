# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 8 September 2026. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication and internal replay are not external acceptance or a proof of the unrestricted conjecture.

## Fixed-order candidate results

### n=25

**Candidate:** `e(G) <= 156`, equality only `K(12,13)`. [Reviewer release](releases/n25-reviewer-v1/README.md) · [frozen proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md) · [8 September re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md). The complete finite domain has now been replayed again in 16 disjoint clean-runner shards: 543,578 outer states, 3,442,212 labelled columns and 1,959 independently reconstructed final equality certificates. Independent specialist review remains open.

### n=27

**Candidate:** `e(G) <= 182`, equality only `K(13,14)`. [Proof](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) · [evidence release](releases/n27-candidate-v1/README.md) · [8 September red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md). The hardened replay checks 80,978,546 canonical columns and independently reconstructs all 35,435 terminal source-cap vectors. Independent review remains open.

### n=28

**Candidate:** `e(G) <= 196`, equality only `K(14,14)`. [Reviewer release](releases/n28-reviewer-v1/README.md) · [direct 197-edge exclusion](project/research/general_n/2026-09-07-direct-197-v8/README.md) · [red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md). Independent review remains open.

### n=29 — new complete candidate

**Candidate:**

```text
e(G) <= 210 = floor(29^2/4),
with equality exactly K(14,15).
```

[Full proof and replay guide](project/reviews/n29/2026-09-08-candidate-v1/README.md) · [candidate manuscript](project/reviews/n29/2026-09-08-candidate-v1/PROOF.md).

The proof does **not** depend on the later general `293/500` candidate theorem. Fan's cited strict bound leaves only 211 edges to exclude. `Delta=15` is handled by a witness-deficit count, which also forces `K(14,15)` at 210. A fresh `Delta=16` direct calculation excludes both 211 and 210: its clean-runner replay examines 1,848,957 and 5,765,218 residual rows respectively, with two independent row scanners and exact integer Farkas certificates; final survivors are zero. `Delta=17` is excluded by a short pointwise charging bound, `Delta=18..27` by the residual h-index inequality, and a universal vertex gives a star. **Status: complete candidate; independent mathematical review OPEN.**

## General structural programme

### Profile-integral continuation — 293/500 candidate

The [profile-integral proof](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md) gives the candidate implication

```text
n >= 6 and Delta(G) >= (293/500)n  ==>  e(G) < floor(n^2/4).
```

It proves `t < a^2/24+a/8` by retaining the demand profile across thresholds. [Replay and audit](project/research/general_n/2026-09-08-profile-integral-v1/README.md). This remains a general structural candidate, not a dependency of the new n=29 proof.

### Layer-sum 13/22 and earlier structural checkpoints

The [13/22 layer-sum proof](project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md) and the preserved [v9](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md), [v10](project/research/general_n/2026-09-08-demand-tail-stability-v10/README.md), and [v11](project/research/general_n/2026-09-08-jensen-tail-v11/README.md) checkpoints document the preceding general-order programme. The local Lean slice checks ten scoped quasi-edge/edge-insertion lemmas; the complete universal theorems are not formally verified.

## Review-paper index

| Scope | Proof / paper | Evidence / review |
|---|---|---|
| n=25 | [Reviewer manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) | [Reviewer package](releases/n25-reviewer-v1/README.md) |
| n=27 | [Proof](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) | [Evidence](releases/n27-candidate-v1/README.md) |
| n=28 | [Mathematical manuscript](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/n28-reviewer-v1/N28_Verification_Companion_v1.pdf) |
| n=29 | [Candidate proof](project/reviews/n29/2026-09-08-candidate-v1/PROOF.md) | [Replay guide](project/reviews/n29/2026-09-08-candidate-v1/README.md) |
| General 293/500 | [Proof](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md) | [Audit](project/research/general_n/2026-09-08-profile-integral-v1/AUDIT.md) |

## Governance and limits

**No complete order above 29, proof through n=1,000, unrestricted all-order solution, novelty determination, full formal verification or external endorsement is claimed.** Numerical states are necessary-condition systems, not graphs. Saved actual-graph regressions contain no positive-surplus graph, so universal correctness depends on the written structural proofs, not extrapolation from samples.

Paul Lenz directed the project; ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. Frozen n=25/n=27/n=28 proofs, original archives and the governed theorem ledger remain unchanged by the n=29 work.

The README immediately preceding the n=29 publication is preserved verbatim at `project/reviews/history/README_before_n29_candidate_2026-09-08.md`. See [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [repository sync policy](project/REPO_SYNC_POLICY.md), and the [theorem ledger](repro-v1/ledger/theorem_ledger.json).
