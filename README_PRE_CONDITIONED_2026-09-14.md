# Murty–Simon / Erdős Problem #742

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **Updated 14 September 2026 through the demand-block/source-pressure checkpoint: proof `5616b33e452d62728f05a721b7fa5cb2724382ea`, frozen verification `479bc1faad29a4c95ebc4530238c46aabe08f0ea`.**

The promoted finite frontier remains **1,971 exclusions / 3,607 survivors**, with **977 quantified whole-state closures**. The **2,655 recovered relational candidates remain unpromoted**. The unrestricted conjecture is **not claimed proved**. External mathematical review, novelty assessment and third-party reproduction remain OPEN.

**Canonical repository:** `paullenz/MurtySimon742`; see [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md). **Restarts:** read [`CURRENT_STATE.md`](CURRENT_STATE.md), then inspect newer commits and live CI. The repository, not a chat transcript, is the durable source of truth.

**External reviewers:** begin with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). Hostile review, counterexamples, literature corrections and independent reproduction are welcome.

The full preceding capped-spill overview remains permanently preserved [at commit e0f2c0a5](https://github.com/paullenz/MurtySimon742/blob/e0f2c0a555c6e8e9902df615114d1cd73918b38e/README.md). Its links and the earlier archived handoffs retain all prior derivations, failed approaches, code and evidence. The protected reviewer index below is retained.

## How this research develops general theory

Specific graph orders are laboratories for structural principles, not a substitute for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates hypothetical graph structure into selected quasi-edge representatives, residual incidences, demands, missing-pair loads and target capacities. We retain a=n-1-Delta, b=Delta and structural surplus t=e(G)-b(a+1).

The cycle is exact constraints, finite experiments, hand-theorem extraction, immediate hostile tests, separately structured verification, then return to the symbolic inequality. Failed approaches, bugs, counterexamples and audit challenges remain part of the result. Surviving a relaxation never implies graph realizability.

## New demand-block and source-specific pressure inequality

Read the [new derivation, verifier and exact certificates](project/research/general_n/2026-09-14-block-pressure-v1/README.md). It extends [capped positive excess and all-source spill](project/research/general_n/2026-09-14-capped-spill-v1/README.md) in two ways: excess committed to LOW POSITIVE-demand labels is removed from a high-label charge, and each source keeps its own legitimate pressure ceiling rather than being assigned the global maximum.

Keep the two defects distinct:

```text
D0=S-r-2t>=0,
Esel=Q-S>=0,
Q=r+2t+D0+Esel,
delta=b-a.
```

For eta>=0 define

```text
m_eta=#{i:s_i<=eta},
M_eta=sum_u(q_u-#{i:eta<s_i<=rho_u})_+,
S_eta=sum_{i:s_i<=eta}s_i,
B_eta=min(Esel,Esel+S_eta-M_eta).
```

Every source must choose at least (q_u-m_eta)_+ high-demand labels. Low-label spill leaves at most B_eta excess for those high labels. The new closed-form necessary inequality is

```text
sum_u(q_u-m_eta)_+(p_u-rho_u+1)_+
 <= B_eta[smax_eta+min(B_eta,delta)],
```

where smax_eta is the maximum demand above eta. Negative B_eta means infeasibility, not a quantity to clip to zero. Eta=0 recovers the preceding positive-label budget; positive eta adds information.

Retaining source ceilings D_u=(P_u-rho_u+1)_+ yields a stronger integer upper bound. For arbitrary nonnegative source weights alpha_u, each high label with selected degree s_i+e_i can receive charge from only that many distinct eligible sources. Bound it by the largest s_i+e_i values alpha_u min(e_i,D_u), then maximize over the justified total-excess, per-label and complete-prefix constraints. This is a SAFE UPPER bound, exact for the stated necessary projection, not for graph realization.

### A short hand contradiction: 209 > 190

One of the preceding 19 unrejected synthetic profiles, row 664, has Esel=33. At eta=1, M_eta=15 and S_eta=1, so B_eta=19. With delta=6 and smax_eta=4, its permissible high-label charge is at most

```text
19(4+6)=190.
```

At q-threshold tau=3 the interval capacity is 101 and demand is only 100. Nevertheless price theta=8 forces charge

```text
8(100-51)-183=209>190.
```

The tail has enough nominal interval capacity but cannot finance its pressure. This certificate needs neither an optimizer nor the stronger integer-envelope calculation. It is a profile exclusion conditional on the canonical bridge, not an all-order theorem forcing a violating threshold.

### Completed synthetic reconnaissance: 19 remaining -> 12

The new verifier reads the same hash-pinned 713-row synthetic corpus, reproduces the preceding baseline, and checks exact integer block/price certificates:

| Necessary screens on the same sampled profiles | Rejected | Not rejected |
|---|---:|---:|
| Previous localized/priced screen | 652 | 61 |
| All-source spill and capped integer envelope | 694 | 19 |
| Demand-block/source-cap pressure, retaining prior screens | **701** | **12** |

Seven new rows are rejected: 39,76,119,406,664,682,688. Every certificate is frozen in [`BLOCK_PRESSURE_VERIFICATION.json`](project/research/general_n/2026-09-14-block-pressure-v1/BLOCK_PRESSURE_VERIFICATION.json). All twelve remaining arrays are explicitly retained in [`REMAINDER_12.json`](project/research/general_n/2026-09-14-block-pressure-v1/REMAINDER_12.json). This is NOT a seven-state reduction of the canonical 3,607 frontier.

Completed new local checks cover 9,293 actual incidence configurations / 33,356 inequalities, 2,000 independent labelled-subset/excess-vector comparisons, 1,000 receiver boxes / 14,806 incoming vectors, all three standing hostile q-tail examples and the complete 713-row corpus. Source weights are chosen coefficients of valid inequalities, not hidden new graph assumptions. The verifier uses integer arithmetic and no optimizer. Same-assistant independent implementation is not external acceptance.

Several extensions gave no further certified exclusions: source ceilings alone, bounded multiblock weighting, and a row-incidence Lagrangian search. Their code/results and limitations are preserved. The latter used floating optimization only for discovery, never as a mathematical certificate. A remaining equality case, row 295 with 126=126, is a concrete next target for joint incidence rigidity.

## Retained capped-spill and priced-tail foundations

The [capped-spill package](project/research/general_n/2026-09-14-capped-spill-v1/README.md) retains the 57>48 hand certificate, 400,758 pressure/cap/envelope checks, 3,000 independent prefix-DP comparisons and its full 812 difficult-profile replay. The all-source-spill cap counts forced selections from every source and removes a source's own lower bound before counting its actual selections again. Its double-counting counterexample remains preserved. Every cap is combined with exact potential-pair degrees and all previously legitimate caps.

The [priced-tail derivation](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md) combines [interval capacities](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md) with [localized selected excess](project/research/general_n/2026-09-14-localized-excess-v1/README.md). At a tail, write A_w for capped interval incoming, f_w=min(A_w,rho_w-1), g_w=A_w-f_w and w_w=alpha_w(q_w-m_eta)_+. The necessary price inequality is

```text
theta(Q_tau-sum f_w)-sum_w(theta-w_w)_+g_w <= shared charge upper bound.
```

The earlier localized-cap replay has fixed tau=3 detection of all 812 difficult profiles. Its Hall-or-price explanation covers all 205,931 OLD exported profiles, including the tight state-4073 tail with the exact 80>77 certificate. These larger observations retain their original provenance; they were NOT regenerated locally in the new block-pressure session. Old exports have shared generation and early stopping, not complete regenerated state coverage. Eliminating stopping witnesses still requires exploring omitted continuations before any whole-state claim.

## Retained exact routes and negative results

The [q-stratified minimum theorem](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_MINCUT_EXACTNESS.md), [type-complete witness corollary](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md) and [q-layer threshold normal form](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) remain exact fallbacks under their stated hypotheses. Equality of minima is not pointwise equality or a requirement that C_q(M+)=0. Check fixed-q monotonicity before transferring old witness theorems to new caps.

The [selected-excess tail-loss identity](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SELECTED_EXCESS_TAIL_LOSS_BUDGET.md) rewrites old cap losses; later localization adds stronger bridge information. The [hostile q-tail cases](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/MURTY_Q_TAIL_HALL_CONJECTURE.md), old-cap fixed-weight obstruction, 32 frozen interval strict gaps, abstract interval misses, synthetic non-rejections and incomplete wider scans remain preserved. Never silently constrain z by z<=Esel.

The completed original q-stratified artifact records C_q=0 on all 205,919 old Hall failures, a finite observation only. Crossing-wall and saturation-wall arguments remain fallbacks. The independent maximum-cut/stability route remains open: e(G)=|X||Y|+I-M, so I<=M for some cut would suffice, but the naive edge-to-missing-pair matching shortcut is false.

## Finite frontier and GitHub audit gates

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

The short-verifier kick `34883538561` has now succeeded. Its downloaded actual/expected localized and priced JSON objects match completely. Its fully paginated audit snapshot, observed at **14 September 2026 19:17:44 UTC**, records plan success plus **116 successful audit shards, 11 running and 129 queued**. This is a timestamped snapshot, not a claim that the audit has completed. The earlier first-page account of only 29 visible successful shards is superseded.

The final relational audit `34854911792` still needs all 2,655 inputs covered, both implementations agreeing, zero unresolved cases, a successful aggregate and a separate ledger-promotion commit. No successful shard was restarted and the 256-shard audit was not duplicated. Scalar states are not graphs or unresolved obligations in the fixed-order candidate packages.

New combined capped/block-pressure replay **`34887492789`** is queued after creation. It regenerates the pinned corpus, rechecks both complete frozen outputs and collects before/after paginated queue snapshots on one standard ARM runner. It is a fresh bounded execution request, not a scheduling-priority guarantee. Capped-spill run `34885163695` was still queued at direct recheck. An hourly conditional GitHub check has been scheduled for confirmed infrastructure retries and meaningful completion/blocker updates, not mathematical promotion.

The successful diagnostic also records green dedicated q-tail `34876612516`, original localized `34880833888` and repaired mincut `34878019517` runs. Frozen-ledger `34875592126` and threshold `34871045562` were previously directly checked green. The old mincut failure `34868771056` was JSON formatting after its mathematical verifier passed; the repair retained all frozen values. Each remote replay, local proof check and external review remains a separate evidence class.

## Fixed-order and general candidate status

| Scope | Preserved candidate result; external review open |
|---|---|
| n=25 | e(G)<=156, equality exactly K(12,13); reviewer-v2 |
| n=27 | e(G)<=182, equality exactly K(13,14); reviewer-v2 |
| n=28 | e(G)<=196, equality exactly K(14,14); reviewer-v2 plus analytic hardening |
| n=29 | e(G)<=210, equality exactly K(14,15); reviewer-v4; difficult Delta=16 branch hand-closed |
| n=30 | e(G)<=225, equality exactly K(15,15); reviewer-v3 |
| n=31 | e(G)<=240, equality exactly K(15,16); source-first reviewer-v1 |
| n=32 | e(G)<=256, equality exactly K(16,16); source-first reviewer-v1 |
| n=33 | e(G)<=272, equality exactly K(16,17); source-first reviewer-v1 |
| n=34 | e(G)<=289, equality exactly K(17,17); reviewer-v2; final heavy certificate hand-replaced |
| n=35 | e(G)<=306, equality exactly K(17,18); reviewer-v1 |
| General maximum-degree result | For n>=6, Delta(G)>=(7/12)n implies e(G)<floor(n^2/4); candidate theorem, external review and novelty assessment open |

<!-- REVIEW-MATERIALS:START -->
## Papers and review materials

This reviewer-facing index is intentionally duplicated here as a protected navigation surface. The detailed canonical status remains [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md), and new editions must update both surfaces rather than deleting this section.

### Fixed-order papers and packages

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md) — [manuscript PDF](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf).
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md) — [manuscript PDF](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf).
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md) — [manuscript PDF](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf).
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md) — [manuscript PDF](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) and [verification companion PDF](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf).
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md) — [manuscript PDF](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) and [verification companion PDF](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf).
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md).
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md) — source-first proof/review package; [exact equality ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md).
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/research/n33/2026-09-12-candidate-v1/AUDIT.md).
- [`n=34 reviewer-v2`](releases/n34-reviewer-v2/README.md) — complete candidate package; [normalization audit and hand replacement](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md).
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md) — complete candidate package; [internal audit](project/research/n35/2026-09-12-candidate-v1/AUDIT.md).

### General-theory papers and reviewer packages

- [`7/12` maximum-degree reviewer-v1](releases/general-7-12-reviewer-v1/README.md) — [manuscript PDF](releases/general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf).
- [`13/22` retained maximum-degree reviewer-v1](releases/general-13-22-reviewer-v1/README.md) — [manuscript PDF](releases/general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf).
- [`293/500` retained maximum-degree reviewer-v1](releases/general-293-500-reviewer-v1/README.md) — [manuscript PDF](releases/general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf).
- [General step-back structural package](releases/general-stepback-v1/README.md) — balanced-degree theorem candidate, `a=14`, fifteen-label and sixteen-label results.
- [Joint-clipping reviewer-v1](releases/general-joint-clipping-reviewer-v1/README.md) — sharp scalar tail bounds and tight-threshold obstruction.
- [Heavy-load / routing reviewer-v1](releases/general-heavy-load-reviewer-v1/README.md).
- [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md).
- [Demand/tail projection reviewer-v1](releases/general-routing-tail-reviewer-v1/README.md).
- [Compatible-destination routing reviewer-v1](releases/general-compatible-routing-reviewer-v1/README.md).
- [Compatible-routing full-catalogue reviewer-v1](releases/general-compatible-catalogue-reviewer-v1/README.md).
- [Closed-compatible-potential reviewer-v1](releases/general-closed-compatible-reviewer-v1/README.md).
- [Fixed-neighbourhood / arc-realisation reviewer-v1](releases/general-arc-realisation-reviewer-v1/README.md).
- [Whole-type orientation Hall research package](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md) — exact type/cut structure, canonical moving staircase, compatible-copy exactness, exterior residual expansion and q-stratified correlation programme; internal audits green where explicitly marked, external review/novelty open.

### Reviewer entry points, audits and corrections

- [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) — reviewer orientation and high-value review targets.
- [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md) — canonical theorem-level manuscript/package index.
- [Canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
- [General-foundations audit](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md).
- [N29 public-release / normalization audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md).
- [Source-degree display erratum](project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md).
- [Alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md).
- [q-stratified crossing-gap audit](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_CROSSING_GAP_AUDIT.md).

Superseded reviewer editions and failed/corrected research remain preserved in Git history and the linked package histories; they are not silently deleted.
<!-- REVIEW-MATERIALS:END -->

## Next research priority and trust boundary

Attack the twelve explicit synthetic non-rejections using joint selected/residual geometry. In particular, determine whether the 126=126 pressure equality in row 295 forces incompatible actual incidences. Additional exploratory weight searches have not been proved exhaustive. The desired general theorem must force a violating block/tail/price from full canonical structure, not infer universal existence from these samples.

Retain exact q-layer, crossing-wall and independent maximum-cut routes. Hand derivation, finite tests, separately structured internal implementations, remote CI, external review and third-party reproduction are different statuses. No timeout, missing output, failed search or floating infeasibility is proof. The canonical selected/residual bridge remains the central correlated external-review dependency. Preserve reviewer navigation and every audit gate during future updates.
