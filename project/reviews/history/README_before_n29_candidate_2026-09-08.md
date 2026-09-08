# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research, organised by graph order and then by general structural work. **Updated 8 September 2026. Independent mathematical review, novelty assessment and external computational reproduction remain OPEN.** Internal replay, formal checking of selected local lemmas and repository publication are not independent acceptance or a proof of the full conjecture.

## n=25 — candidate proof

**Proposed result:** every simple diameter-two edge-critical graph on 25 vertices has at most **156 edges**, with equality only for **K(12,13)**.

**Review paper:** [PDF](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) · [readable manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.md) · [review guide](releases/n25-reviewer-v1/REVIEW_GUIDE.md).

The [complete reviewer package](releases/n25-reviewer-v1/README.md), [frozen proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md), [exact results](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RESULTS.md) and [internal red-team report](project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Report_2026-09-06.md) preserve the argument and checking record. **Status:** complete candidate; independent review OPEN.

## n=27 — candidate proof

**Proposed result:** at most **182 edges**, with equality only for **K(13,14)**.

**Review paper:** [full readable proof manuscript](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) · [proof and review guide](project/reviews/n27/2026-09-07-candidate-v1/README.md) · [complete evidence package](releases/n27-candidate-v1/README.md).

**Status:** complete candidate; internal arithmetic reproduced; independent review OPEN. The n=25 frozen edition is unchanged.

**8 September internal red-team audit:** [full report](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md) and [replay guide](project/reviews/n27/2026-09-08-redteam-v1/README.md). No blocking mathematical defect found. A clean-runner rebuild replayed all 80,978,546 canonical columns; a separate augmenting-path implementation rederived all 35,435 terminal source-cap vectors. Strict JSON validation covers 13,596,058 input rows. The audit records a permissive raw C++ digit parser, now guarded without changing frozen sources, and the initial audit-comparison failure caused by gzip timestamps, now explicitly reconciled. These are internal checks, not external acceptance or full formal verification; the original n=27 proof and evidence archive remain unchanged.

## n=28 — candidate proof and reviewer release

**Proposed result:** at most **196 edges**, with equality only for **K(14,14)**.

**Review papers:** [mathematical manuscript — PDF](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) · [verification companion — PDF](releases/n28-reviewer-v1/N28_Verification_Companion_v1.pdf) · [complete reviewer release](releases/n28-reviewer-v1/README.md).

The direct route treats the 196-edge equality case and the 197-edge exclusion separately. At 196 edges the degree-15 chain passes through [v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md), [v6](project/research/general_n/2026-09-07-shared-adjacency-v6/README.md) and [LocalIncidence-v7](project/research/general_n/2026-09-07-local-incidence-v7/README.md), reducing 6,918 necessary-condition rows to 388 and then zero. [Direct197-v8](project/research/general_n/2026-09-07-direct-197-v8/README.md) generates a fresh t=2 domain and excludes all 1,584 final rows. Other maximum degrees are covered explicitly; Fan's cited strict bound is an external theorem input.

The hardened reviewer driver checks the six original archives without modifying them. The [internal red-team audit](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md) found no blocking defect in the audited direct route. **Status:** complete candidate prepared for review; independent mathematical review OPEN.

The separate [degree-load-v7 route](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md) is an alternative workstream with an additional weak-core obligation. It is not a dependency of the direct reviewer manuscript and must not be conflated with LocalIncidence-v7.

## General structural programme

### Profile-integral continuation — current candidate for n>=6

The [completed profile-integral argument](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md) gives the candidate implication

```text
n >= 6 and Delta(G) >= (293/500)*n  ==>  e(G) < floor(n^2/4).
293/500 = 0.586 exactly.
```

It proves `t < a^2/24+a/8`, with `a=n-1-Delta` and `t=e(G)-Delta*(n-Delta)`, by retaining the individual demand profile across thresholds. A shifted midpoint estimate controls the finite sum-to-integral error; an exact scalar polynomial bound makes Jensen unnecessary. The old 13/22 cubic is not a dependency. A 640-case integer certificate closes the two small-a exceptions. This excludes the `n=29, Delta=17` 210-edge case, **not every maximum degree at n=29**. The strict statement still requires n>=6 because of K(2,3).

The [replay guide](project/research/general_n/2026-09-08-profile-integral-v1/README.md), [adversarial audit](project/research/general_n/2026-09-08-profile-integral-v1/AUDIT.md) and [exact output](project/research/general_n/2026-09-08-profile-integral-v1/evidence/RESULTS.json) preserve 478,192 abstract demand profiles, 4,215,632 threshold levels, 833,250 rational midpoint checks and 5,173,536 eligible degree-pair checks through n=5,000. These are not actual graph enumerations or a proof of all graphs through n=5,000. **Complete candidate hand argument; internal computations REPRODUCED; independent specialist review OPEN. The new profile-integral theorem is not formally verified or PROJECT-CERTIFIED.** Earlier frozen proofs and the governed theorem ledger are unchanged.

### Layer-sum continuation — retained 13/22 candidate for n>=6

The [layer-sum candidate proof](project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md) gives the exact rational implication

```text
n >= 6 and Delta(G) >= (13/22)*n  ==>  e(G) < floor(n^2/4).
13/22 = 0.59090909...
```

It derives `3*S^3 <= a^2*r*(2*r+1)` and `t < 4*a^2/81 + 1/8`, where `a=n-1-Delta`, `t=m-Delta*(n-Delta)`, `r` counts residual edges and `S` is total minimum label demand. The proof combines the exact threshold-pair count across all demand levels through a common residual budget. It has no large-a cutoff. **The n>=6 qualification is essential for strictness: K(2,3) is a small-order exception.** This is not a complete general-conjecture solution or a new whole-order proof.

The [replay guide](project/research/general_n/2026-09-08-layer-sum-v1/README.md) and [fresh evidence](project/research/general_n/2026-09-08-layer-sum-v1/RESULTS.md) preserve 1,059 checked selected systems, the full labelled-graph census through six vertices, 2,353 abstract demand multisets and 10,200 scalar identities. The two criticality implementations agree on all 33,864 graphs in that small domain. Only 12 systems have nonzero demand, and none has positive surplus; finite tests are not a proof of the dense case. **Candidate mathematics; internal finite replay REPRODUCED; independent review OPEN. Only a local quasi-edge/edge-insertion slice is formally checked; the full layer-sum result is not.**

The preceding [threshold-capacity note](project/research/general_n/2026-09-07-stability-spare-sources-v9/THRESHOLD_CAPACITY_CONTINUATION.md), with its 0.6129 candidate coefficient, remains unchanged. Its supplied regression has now actually run successfully: 99 rounding cases, 2,550 integer maximisations and 1,728,186 oriented-graph checks. The new graph-to-layer proof is self-contained and does not depend on the older charging-deficit constants. The concurrent demand-tail v10 and Jensen-tail v11 checkpoints are preserved in full; this layer-sum argument does not depend on their new constants. The unreferenced weighted-spare v10 blobs from the previous turn are a different workstream and are not silently adopted as evidence. Frozen papers and the theorem ledger remain untouched.

The publication was rebased onto the concurrent v11 checkpoint; see the [reconciliation note](project/research/general_n/2026-09-08-layer-sum-v1/RECONCILIATION.md). V11 retains its stated n>=4 scope; the stronger layer-sum threshold above is deliberately limited to n>=6.

### v9 — standalone structural paper

The [nine-page v9 paper](project/research/general_n/2026-09-07-stability-spare-sources-v9/General_Structural_Theorems_v9.pdf), [full proof](project/research/general_n/2026-09-07-stability-spare-sources-v9/PROOF.md), [review guide](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md) and [literature comparison](project/research/general_n/2026-09-07-stability-spare-sources-v9/literature/COMPARISON.md) isolate the charging and source-supplement mechanisms from finite-order computations. The complete standard-library replay passed locally and in a clean GitHub runner.

The local quasi-edge Lean slice now checks **ten** logical lemmas in Lean 4.19.0, including four local edge-insertion bridge lemmas. Global finite selection/injection, charging, threshold counting and the general theorems are not formally verified. The later [construction assurance record](project/research/general_n/2026-09-08-layer-sum-v1/evidence/CONSTRUCTION_ASSURANCE_2026-09-08.json) gives the exact scope and preserves the corrected first attempt.

### v10 — first explicit demand-tail improvement

The [v10 proof](project/research/general_n/2026-09-08-demand-tail-stability-v10/PROOF.md) derives the candidate fixed loss `1/750` for `a>=25` and the conservative maximum-degree implication `Delta>=0.6126n`. Its [exact rational checker](project/research/general_n/2026-09-08-demand-tail-stability-v10/check_v10.py) passed in a clean Ubuntu 24.04 runner. V10 also records the general demand-tail capacity inequality and all-k spare-source bound.

### v11 — Jensen-tail candidate (retained)

The [v11 Jensen-tail proof](project/research/general_n/2026-09-08-jensen-tail-v11/PROOF.md) adds an exact second stability identity centred at the **actual mean demand**, rather than only at `alpha=1-1/sqrt(2)`. Combining that Jensen defect with the same source-supplement pair capacity gives

```text
a = n-1-Delta,
t = e(G)-Delta(n-Delta),
c = (3-2*sqrt(2))/2,

a >= 50  ==>  t < (c-1/300) a^2.
```

Together with the original charging bound for `2<=a<=49` and a direct `a=1` observation, the v11 conservative candidate implication is

```text
n >= 4 and Delta(G) >= 0.6116 n
    ==> e(G) < floor(n^2/4).
```

The remaining algebra reduces to positivity of one explicit degree-seven polynomial on a rational interval. The [standard-library exact checker](project/research/general_n/2026-09-08-jensen-tail-v11/check_v11.py) uses a rational Sturm sequence and passed in a clean Ubuntu 24.04 GitHub runner; see the [verification record](project/research/general_n/2026-09-08-jensen-tail-v11/evidence/REMOTE_EXACT_CHECK.json). The first runner attempt exposed and corrected a checker-only strict-inequality encoding error; no theorem constant or proof inequality changed.

No finite-order enumeration, Fan bound, weak-core reduction or positive-surplus residual-activity lemma is used by v11. The universal graph-to-selected-system and demand-tail lemmas remain hand proofs awaiting specialist scrutiny. **No best-known, novelty or priority claim is made pending specialist review.** Paul is arranging that review; no new outreach has been sent by the assistant.

## Review-paper index

| Scope | Direct paper / proof | Companion / evidence |
|---|---|---|
| n=25 | [Reviewer manuscript — PDF](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) | [Review guide](releases/n25-reviewer-v1/REVIEW_GUIDE.md) |
| n=27 | [Full proof manuscript — Markdown](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) | [Evidence package](releases/n27-candidate-v1/README.md) |
| n=28 | [Mathematical manuscript — PDF](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) | [Verification companion — PDF](releases/n28-reviewer-v1/N28_Verification_Companion_v1.pdf) |
| General profile-integral | [293/500 candidate proof — Markdown](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md) | [Replay and audit](project/research/general_n/2026-09-08-profile-integral-v1/README.md) |
| General layer-sum | [Full candidate proof — Markdown](project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md) | [Replay and evidence](project/research/general_n/2026-09-08-layer-sum-v1/README.md) |
| General v9 | [Structural paper — PDF](project/research/general_n/2026-09-07-stability-spare-sources-v9/General_Structural_Theorems_v9.pdf) | [Proof and replay guide](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md) |
| General v10 | [Demand-tail proof — Markdown](project/research/general_n/2026-09-08-demand-tail-stability-v10/PROOF.md) | [Clean-runner arithmetic record](project/research/general_n/2026-09-08-demand-tail-stability-v10/README.md) |
| General v11 | [Jensen-tail proof — Markdown](project/research/general_n/2026-09-08-jensen-tail-v11/PROOF.md) | [Guide and exact Sturm record](project/research/general_n/2026-09-08-jensen-tail-v11/README.md) |

## Scope, evidence and governance

Earlier general stages remain preserved: [residual h-index v1](project/research/general_n/2026-09-07-residual-hindex-v1/README.md), [pair budgets v2](project/research/general_n/2026-09-07-pair-budgets-v2/README.md), [demand-support v3](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md), [demand-stability v3](project/research/general_n/2026-09-07-demand-stability-v3/README.md), [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md), and the [coupled-resource proof](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md).

The middle-degree region remains open. Degree-case exclusions at selected larger orders are not whole-order theorems. **No complete order above 28, proof through n=1,000, full all-order solution, novelty determination or full formal verification is claimed.** Saved actual-graph tests contain no positive-surplus graph, so universal correctness rests on the written structural proofs rather than extrapolation from samples.

Paul Lenz directed the project; ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. Frozen finite-order proofs, original archives and the governed theorem ledger remain unchanged by the general research programme.

The [README before the profile-integral update](project/reviews/history/README_before_profile_integral_2026-09-08.md), the [README immediately before the layer-sum update](project/reviews/history/README_before_layer_sum_2026-09-08.md) and the [README immediately before the v11 update](project/reviews/history/README_before_v11_2026-09-08.md) are preserved verbatim. See the [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [commit-completion policy](project/REPO_SYNC_POLICY.md), [canonical review](project/CANONICAL_N25_REVIEW_2026-09-06.md), [theorem ledger](repro-v1/ledger/theorem_ledger.json), [task backlog](project/CANONICAL_TASKS.json) and [evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json). Publication preserves evidence; it does not promote mathematical status.
