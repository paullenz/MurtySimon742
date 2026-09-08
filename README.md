# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 9 September 2026. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication and internal replay are not external acceptance or a proof of the unrestricted conjecture.

**External reviewers:** please start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). The project actively welcomes hostile review, counterexamples, literature corrections and independent reproduction. GitHub Issues are the preferred place to report a suspected flaw.

## Public-review note

The repository intentionally preserves failed approaches and audit findings rather than silently rewriting them.

During the restarted hostile audit of the additional n=29 `Delta=16` cumulative-threshold verifier, a **real normalization bug** was found in its first version: a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are therefore **invalid as proof evidence** and the historical v1 source is retained only for auditability. The defect did not affect the original n=29 direct route or the separate fully fresh implementation.

A corrected `v2` model was then replayed cleanly and again produced zero survivors. The audit subsequently reduced the proof-critical `Delta=16` computation to a smaller trusted kernel, whose clean replay also produced zero survivors with every late exclusion rechecked by exact integer Farkas arithmetic. See the [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md) and [minimal-kernel report](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json).

## Fixed-order candidate results

### n=25

**Candidate:** `e(G) <= 156`, equality only `K(12,13)`. [Reviewer release](releases/n25-reviewer-v1/README.md) · [frozen proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md) · [8 September re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md). The complete finite domain has now been replayed again in 16 disjoint clean-runner shards: 543,578 outer states, 3,442,212 labelled columns and 1,959 independently reconstructed final equality certificates. Independent specialist review remains open.

### n=27

**Candidate:** `e(G) <= 182`, equality only `K(13,14)`. [Proof](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) · [evidence release](releases/n27-candidate-v1/README.md) · [8 September red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md). The hardened replay checks 80,978,546 canonical columns and independently reconstructs all 35,435 terminal source-cap vectors. Independent review remains open.

### n=28

**Candidate:** `e(G) <= 196`, equality only `K(14,14)`. [Reviewer release](releases/n28-reviewer-v1/README.md) · [direct 197-edge exclusion](project/research/general_n/2026-09-07-direct-197-v8/README.md) · [red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md). Independent review remains open.

### n=29 — complete candidate

**Candidate:**

```text
e(G) <= 210 = floor(29^2/4),
with equality exactly K(14,15).
```

[Full proof and replay guide](project/reviews/n29/2026-09-08-candidate-v1/README.md) · [candidate manuscript](project/reviews/n29/2026-09-08-candidate-v1/PROOF.md) · [standalone Delta=16 graph-to-model bridge](project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md) · [bridge hostile audit](project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md) · [restarted red-team audit](project/reviews/n29/2026-09-08-redteam-restart-v1/N29_RED_TEAM_RESTART.md) · [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md).

The proof does **not** depend on the later general `293/500` candidate theorem. Fan's cited strict bound leaves only 211 edges to exclude. `Delta=15` is handled by a witness-deficit count, which also forces `K(14,15)` at 210. `Delta=17` is excluded by a short pointwise charging bound, `Delta=18..27` by the residual h-index inequality, and a universal vertex gives a star.

The difficult `Delta=16` case has several same-assistant computational routes. The preferred proof-critical route is now the **minimal trusted kernel**:

```text
quasi-edge / selected-residual construction
  -> residual activity
  -> charging and threshold-capacity inequalities
  -> exact source-capacity dual pruning
  -> simple residual-row Hall/refinement scan
  -> corrected cumulative-threshold/source-q-flow LP
  -> exact integer Farkas verification
```

Its clean replay retains 72 demand profiles and 126 residual rows at 211 edges, and 367 demand profiles and 1,467 residual rows at 210 edges. All 1,593 late residual rows receive exact Farkas contradictions and final survivors are zero. This route does **not** use the old projected screen, joint propagator, shared LP, typed LP, old endpoint LP or older pair-capacity support formula.

**Status: complete candidate; independent mathematical review OPEN.**

## n=30 reconnaissance

A first symbolic parameterisation pass has been recorded at [`project/research/n30/2026-09-09-recon-v1/README.md`](project/research/n30/2026-09-09-recon-v1/README.md). It is **not** an n=30 candidate theorem. The hand reductions narrow the dense non-bipartite n=30 problem to four scopes only:

```text
m=226: Delta=16,17
m=225: Delta=16,17
```

The `Delta=17` scopes keep the same `a=12` label-side dimension as the difficult n=29 case and are therefore the preferred first test of whether the stripped trusted kernel genuinely parameterises.

## General structural programme

### Profile-integral continuation — 293/500 candidate

The [profile-integral proof](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md) gives the candidate implication

```text
n >= 6 and Delta(G) >= (293/500)n  ==>  e(G) < floor(n^2/4).
```

It proves `t < a^2/24+a/8` by retaining the demand profile across thresholds. [Replay and audit](project/research/general_n/2026-09-08-profile-integral-v1/README.md). This remains a general structural candidate, not a dependency of the n=29 proof.

### Layer-sum 13/22 and earlier structural checkpoints

The [13/22 layer-sum proof](project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md) and the preserved [v9](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md), [v10](project/research/general_n/2026-09-08-demand-tail-stability-v10/README.md), and [v11](project/research/general_n/2026-09-08-jensen-tail-v11/README.md) checkpoints document the preceding general-order programme. The local Lean slice checks ten scoped quasi-edge/edge-insertion lemmas; the complete universal theorems are not formally verified.

## Review-paper index

| Scope | Proof / paper | Evidence / review |
|---|---|---|
| n=25 | [Reviewer manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) | [Reviewer package](releases/n25-reviewer-v1/README.md) |
| n=27 | [Proof](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) | [Evidence](releases/n27-candidate-v1/README.md) |
| n=28 | [Mathematical manuscript](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/n28-reviewer-v1/N28_Verification_Companion_v1.pdf) |
| n=29 | [Candidate proof](project/reviews/n29/2026-09-08-candidate-v1/PROOF.md) | [Standalone bridge](project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md) |
| General 293/500 | [Proof](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md) | [Audit](project/research/general_n/2026-09-08-profile-integral-v1/AUDIT.md) |

## Governance and limits

**No complete order above 29, proof through n=1,000, unrestricted all-order solution, novelty determination, full formal verification or external endorsement is claimed.** Numerical states are necessary-condition systems, not graphs. Saved actual-graph regressions contain no positive-surplus graph, so universal correctness depends on the written structural proofs, not extrapolation from samples.

Paul Lenz directed the project; ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. Same-assistant independent implementations are explicitly **not** described as external independent review. Frozen n=25/n=27/n=28 proofs, original archives and the governed theorem ledger remain preserved.

The README immediately preceding the n=29 publication is preserved verbatim at `project/reviews/history/README_before_n29_candidate_2026-09-08.md`. See [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [repository sync policy](project/REPO_SYNC_POLICY.md), and the [theorem ledger](repro-v1/ledger/theorem_ledger.json).

## Review and corrections

Please use the [reviewer starting point](START_HERE_FOR_REVIEWERS.md) and open a GitHub Issue for suspected errors. The repository includes a mathematical-review issue template. Corrections should preserve the original failure evidence and state clearly which downstream claims are affected.

## Licence

MIT — see [`LICENSE`](LICENSE).
