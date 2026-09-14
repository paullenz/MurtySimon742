# Murty–Simon / Erdős Problem #742

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **Updated 14 September 2026 through the capped positive-excess and all-source-spill checkpoint: proof `f1f9ea055233bf5bff4499f3f7981591a2f20765`, frozen verification `18cafdf20c5ab0d31c4c79f767f721b2064efa88`.**

The promoted finite frontier remains **1,971 exclusions / 3,607 survivors**, with **977 quantified whole-state closures**. The **2,655 recovered relational candidates remain unpromoted**. The unrestricted conjecture is **not claimed proved**. Independent mathematical review, novelty assessment and third-party computational reproduction remain OPEN.

**Canonical repository:** `paullenz/MurtySimon742`; see [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md). **Restarts:** read [`CURRENT_STATE.md`](CURRENT_STATE.md), then inspect newer commits and live CI. The repository, not a chat transcript, is the durable source of truth.

**External reviewers:** begin with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). Hostile review, counterexamples, literature corrections and independent reproduction are welcome.

The preceding priced-tail overview remains permanently available [at commit 0b8ba460](https://github.com/paullenz/MurtySimon742/blob/0b8ba460064f7441a8f92cc6f7434193039b7db5/README.md). [`README_PRE_PRICED_2026-09-14.md`](README_PRE_PRICED_2026-09-14.md) preserves the detailed exact q-layer, interval, selected-loss and localized-cap chronology. Earlier archives and Git history remain intact. The protected reviewer index below is retained.

## How this research develops general theory

Specific graph orders are laboratories for structural principles, not a substitute for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates a hypothetical graph into selected quasi-edge representatives, residual incidences, demands, missing-pair loads and target capacities. We retain the exact notation a=n-1-Delta, b=Delta and structural surplus t=e(G)-b(a+1).

The cycle is exact constraints, finite experiments, hand-theorem extraction, immediate hostile tests, separately structured verification, then return to the symbolic inequality. Failed approaches, bugs, counterexamples and audit challenges are preserved. Surviving any relaxation never implies graph realizability.

## New capped-excess inequality and all-source spill

The [new proof and verification package](project/research/general_n/2026-09-14-capped-spill-v1/README.md) strengthens both the shared charge budget and the localized receiver caps. Put delta=b-a, z=#{i:s_i=0}, and

```text
M0=sum_u(q_u-#{i:0<s_i<=rho_u})_+,
B=Esel-M0>=0, smax=max_i s_i.
```

M0 is selected excess unavoidably spent on zero-demand labels. Positive-demand endpoint forcing and the canonical incoming cap give

```text
sum_u(q_u-z)_+(p_u-rho_u+1)_+
 <= sum_{i:s_i>0}(s_i+e_i)min(e_i,delta)
 <= B[smax+min(B,delta)].
```

For B>=delta, the closed-form upper bound is linear in B, replacing the older quadratic envelope Esel(Esel+smax). It uses Esel=Q-r-2t-D0, so the two bridge defects remain explicitly coupled. Its graph application inherits the canonical bridge's external-review boundary.

The all-source-spill cap counts selections forced into each low-demand block by EVERY source, not just low-residual sources. It explicitly subtracts the target source's own contribution before recounting its actual selected labels. This avoids a preserved double-counting trap. The cap is combined with all previous caps, especially exact potential-pair degrees. A prefix integer dynamic programme further bounds how much positive-label charge the shared excess can finance; its exactness is for a specified necessary projection, not graph realization.

### New exact hand certificate and finite reach

A previously unrejected synthetic profile has Esel=34, forced zero-label excess M0=26, B=8 and delta=smax=3. Its upper cost is 8(3+3)=48. At tau=1 and price theta=4, even the preceding localized caps force cost at least 4(96-31)-203=57. Thus **57>48**, a nine-unit contradiction without an optimizer. The profile has no deficient interval tail after the new spill cap; pricing adds information beyond interval-tail deficiency.

The original 100,000-trial synthetic generator was regenerated with pinned source and scanner. Its 713-row output reproduces the earlier counts exactly. New separately implemented arithmetic gives:

| Necessary screen on the same 713 sampled profiles | Rejected |
|---|---:|
| Previous localized/priced screen | 652 |
| All-source spill with previous quadratic envelope | 654 |
| Spill with new closed-form capped envelope | 672 |
| Spill with integer prefix envelope | 694 |

**42 of the former 61 sampled survivors are newly rejected; 19 remain.** Their row IDs and all newly rejected IDs are preserved, and the corpus is hash-pinned and reproducible. This is not a 42-state frontier reduction or an independently generated exhaustive graph search.

The local verifier checks 133,586 exhaustive incidence configurations at delta=1,2,4, giving 400,758 pressure/cap/envelope checks, plus 3,000 independent brute-force comparisons of the prefix optimum. All standing hostile examples remain tested. On the frozen 812 difficult profiles, one further cap vector tightens and total-capacity contradictions increase from 630 to 631; adaptive interval detections remain 812. The committed CI regenerates the synthetic corpus and requires complete parsed equality of every frozen result. Local PASS is not remote CI completion or external acceptance.

## Priced-tail foundation: a tail can be feasible but too expensive

The [priced-tail hand derivation and certificate](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md) combines the [interval budget](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md) with the [localized selected-excess cap](project/research/general_n/2026-09-14-localized-excess-v1/README.md).

Keep the bridge quantities distinct:

```text
D0=S-r-2t>=0,
Esel=Q-S>=0,
Q=r+2t+D0+Esel.
```

For z zero-demand labels, put v_w=(q_w-z)_+. The earlier shared budget was

```text
sum_w v_w(p_w-rho_w+1)_+ <= Esel(Esel+smax).
```

It remains valid, but the new capped bound above can be materially stronger. At q-threshold tau, let Q_tau be the tail demand and A_w the available interval incoming capacity after all legitimate target caps. Put f_w=min(A_w,rho_w-1) and g_w=A_w-f_w. Every graph-derived orientation necessarily satisfies, for every theta>=0,

```text
theta*(Q_tau-sum_w f_w)
 -sum_w(theta-v_w)_+ g_w <= shared charge upper bound.
```

A strict violation is a contradiction even when capacity alone does not expose one. A universal theorem forcing such a violation from full canonical structure remains open; high-q-tail sufficiency is not assumed.

### Earlier fixed-threshold evidence and the 80>77 certificate

With the preceding localized caps, the single threshold tau=3 detects all 812 difficult profiles, with minimum deficiency 1 and maximum 15. This is a finite certificate, not a universal tau=3 theorem. The exact obstruction to common nonnegative weights remains preserved for the OLD cap model; it does not transfer to stronger caps.

The earlier reconstruction on all 205,931 OLD exported profiles made tau=3 deficient in 205,930. The remaining profile, associated with state 4073, had a tight tail: demand and capacity both 56. Filling it requires selected-excess cost at least 80, while the older budget permits only 77. Price theta=7 gives an exact hand certificate. This profile was already rejected by the old cost screen; the advance was the short explanation.

These are old exported rows with shared generation and early stopping, not regenerated complete state searches. The larger old export was NOT regenerated in the new capped-spill session. Rejecting old stopping witnesses requires exploring omitted continuations before a whole-state claim. All earlier code, frozen outputs, source hashes and reproduction instructions remain preserved.

## Retained exact routes and negative results

The [q-stratified minimum theorem](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_MINCUT_EXACTNESS.md), [type-complete witness corollary](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md) and [q-layer threshold normal form](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) remain exact fallbacks under their stated hypotheses. Equality of minima is not pointwise equality or a requirement that C_q(M+)=0. Check fixed-q monotonicity before transferring old canonical-witness results to modified caps.

The [selected-excess tail-loss budget](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SELECTED_EXCESS_TAIL_LOSS_BUDGET.md) rewrites old cap losses exactly; localized and all-source-spill caps add stronger bridge information. The [hostile q-tail cases](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/MURTY_Q_TAIL_HALL_CONJECTURE.md), old fixed-weight obstruction, 32 frozen interval strict gaps, abstract interval misses, synthetic non-rejections and failed wider scans remain part of the result. The zero-demand count z is never silently bounded by Esel.

The original completed q-stratified artifact records C_q=0 on all 205,919 old Hall failures. This remains finite reconnaissance. Crossing-wall charge and saturation-wall arguments are retained, not discarded.

## Finite frontier and CI gates

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

The final relational audit `34854911792` remains incomplete, but is making progress. Newly downloaded shard 90 evidence records all 11 assigned states audited and no unresolved cases. The final indexed shard 255 is still queued; no accepted aggregate has been observed. Promotion requires all 2,655 inputs, both implementations agreeing state by state, zero unresolved, successful aggregate and then a separate ledger update. Scalar states are not graphs or unresolved obligations in fixed-order candidate packages.

The user-requested GitHub kick created fresh read-only short-verifier replay `34883538561` on a standard ARM runner, with paginated queue diagnostics. It was still queued at recheck; this does not guarantee scheduling priority. The new capped-spill replay is run `34885163695`, also queued when inspected. The progressing 256-shard audit was not cancelled or duplicated. See `CURRENT_STATE.md` for exact observations and the downloaded shard hash.

Frozen-ledger CI `34875592126`, q-layer threshold CI `34871045562`, and repaired mincut CI `34878019517` were previously directly checked green. The old failed mincut run `34868771056` passed mathematics but failed on JSON formatting; its repair retained every frozen value. These successes do not complete the relational audit. Local proof verification, remote replay and external review remain separate gates.

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
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md) — complete candidate package; [internal audit](project/reviews/n35/2026-09-12-candidate-v1/AUDIT.md).

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

Seek a violating pair (tau,theta) forced by FULL canonical structure, using all-source spill, capped positive-label excess, exact pair losses and joint residual/selected realization. Attack the 19 remaining explicit synthetic profiles without claiming that passing a screen realizes a graph. Complete omitted source-state continuations with independent coverage certificates separately from the hand argument.

Retain exact q-layer and crossing-wall/saturation routes. The independent maximum-cut/stability programme is also preserved: e(G)=|X||Y|+I-M, so I<=M for some cut would suffice, but the naive edge-to-missing-pair matching shortcut is false.

Hand derivation, finite tests, separate internal implementations, remote CI, external review and third-party reproduction are distinct. No timeout, missing output, failed search or floating infeasibility is proof. The canonical quasi-edge/selected-residual bridge remains the central correlated external-review dependency. Preserve reviewer navigation and audit gates during every update.
