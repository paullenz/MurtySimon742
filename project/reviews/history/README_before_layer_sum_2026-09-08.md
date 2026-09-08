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

## n=28 — candidate proof and reviewer release

**Proposed result:** at most **196 edges**, with equality only for **K(14,14)**.

**Review papers:** [mathematical manuscript — PDF](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) · [verification companion — PDF](releases/n28-reviewer-v1/N28_Verification_Companion_v1.pdf) · [complete reviewer release](releases/n28-reviewer-v1/README.md).

The direct route treats the 196-edge equality case and the 197-edge exclusion separately. At 196 edges the degree-15 chain passes through [v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md), [v6](project/research/general_n/2026-09-07-shared-adjacency-v6/README.md) and [LocalIncidence-v7](project/research/general_n/2026-09-07-local-incidence-v7/README.md), reducing 6,918 necessary-condition rows to 388 and then zero. [Direct197-v8](project/research/general_n/2026-09-07-direct-197-v8/README.md) generates a fresh t=2 domain and excludes all 1,584 final rows. Other maximum degrees are covered explicitly; Fan's cited strict bound is an external theorem input.

The hardened reviewer driver checks the six original archives without modifying them. The [internal red-team audit](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md) found no blocking defect in the audited direct route. **Status:** complete candidate prepared for review; independent mathematical review OPEN.

The separate [degree-load-v7 route](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md) is an alternative workstream with an additional weak-core obligation. It is not a dependency of the direct reviewer manuscript and must not be conflated with LocalIncidence-v7.

## General structural programme

### v9 — standalone structural paper

The [nine-page v9 paper](project/research/general_n/2026-09-07-stability-spare-sources-v9/General_Structural_Theorems_v9.pdf), [full proof](project/research/general_n/2026-09-07-stability-spare-sources-v9/PROOF.md), [review guide](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md) and [literature comparison](project/research/general_n/2026-09-07-stability-spare-sources-v9/literature/COMPARISON.md) isolate the charging and source-supplement mechanisms from finite-order computations. The complete standard-library replay passed locally and in a clean GitHub runner.

The local quasi-edge Lean slice now checks **six** logical lemmas in Lean 4.19.0, including the supplement-forcing fact used by the demand-tail proof. Quasi-edge existence, cardinality injections, charging, demand-tail counting and the general theorem are not formally verified.

### v10 — first explicit demand-tail improvement

The [v10 proof](project/research/general_n/2026-09-08-demand-tail-stability-v10/PROOF.md) derives the candidate fixed loss `1/750` for `a>=25` and the conservative maximum-degree implication `Delta>=0.6126n`. Its [exact rational checker](project/research/general_n/2026-09-08-demand-tail-stability-v10/check_v10.py) passed in a clean Ubuntu 24.04 runner. V10 also records the general demand-tail capacity inequality and all-k spare-source bound.

### v11 — current candidate maximum-degree threshold

The [v11 Jensen-tail proof](project/research/general_n/2026-09-08-jensen-tail-v11/PROOF.md) adds an exact second stability identity centred at the **actual mean demand**, rather than only at `alpha=1-1/sqrt(2)`. Combining that Jensen defect with the same source-supplement pair capacity gives

```text
a = n-1-Delta,
t = e(G)-Delta(n-Delta),
c = (3-2*sqrt(2))/2,

a >= 50  ==>  t < (c-1/300) a^2.
```

Together with the original charging bound for `2<=a<=49` and a direct `a=1` observation, the current conservative candidate implication is

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
| General v9 | [Structural paper — PDF](project/research/general_n/2026-09-07-stability-spare-sources-v9/General_Structural_Theorems_v9.pdf) | [Proof and replay guide](project/research/general_n/2026-09-07-stability-spare-sources-v9/README.md) |
| General v10 | [Demand-tail proof — Markdown](project/research/general_n/2026-09-08-demand-tail-stability-v10/PROOF.md) | [Clean-runner arithmetic record](project/research/general_n/2026-09-08-demand-tail-stability-v10/README.md) |
| General v11 | [Current Jensen-tail proof — Markdown](project/research/general_n/2026-09-08-jensen-tail-v11/PROOF.md) | [Guide and exact Sturm record](project/research/general_n/2026-09-08-jensen-tail-v11/README.md) |

## Scope, evidence and governance

Earlier general stages remain preserved: [residual h-index v1](project/research/general_n/2026-09-07-residual-hindex-v1/README.md), [pair budgets v2](project/research/general_n/2026-09-07-pair-budgets-v2/README.md), [demand-support v3](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md), [demand-stability v3](project/research/general_n/2026-09-07-demand-stability-v3/README.md), [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md), and the [coupled-resource proof](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md).

The middle-degree region remains open. Degree-case exclusions at selected larger orders are not whole-order theorems. **No complete order above 28, proof through n=1,000, full all-order solution, novelty determination or full formal verification is claimed.** Saved actual-graph tests contain no positive-surplus graph, so universal correctness rests on the written structural proofs rather than extrapolation from samples.

Paul Lenz directed the project; ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. Frozen finite-order proofs, original archives and the governed theorem ledger remain unchanged by the general research programme.

The [README immediately before the v11 update](project/reviews/history/README_before_v11_2026-09-08.md) is preserved verbatim. See the [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [commit-completion policy](project/REPO_SYNC_POLICY.md), [canonical review](project/CANONICAL_N25_REVIEW_2026-09-06.md), [theorem ledger](repro-v1/ledger/theorem_ledger.json), [task backlog](project/CANONICAL_TASKS.json) and [evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json). Publication preserves evidence; it does not promote mathematical status.
