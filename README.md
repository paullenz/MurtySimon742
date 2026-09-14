# Murty–Simon / Erdős Problem #742

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **Updated 14 September 2026 through the reconciled selected-excess and interval-tail budgets, research commits `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb` and `d1e20da87e8d8dcda3633e550b8b5556b6e7c9ee`.**

The canonical promoted finite frontier remains **1,971 exclusions / 3,607 survivors**, with **977 quantified whole-state closures**. The **2,655 recovered relational candidate exclusions remain unpromoted**. The unrestricted conjecture is **not claimed proved**. Independent mathematical review, novelty assessment and genuinely independent third-party computational reproduction remain OPEN.

**Canonical repository:** `paullenz/MurtySimon742`; see [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md). **Research restarts:** read [`CURRENT_STATE.md`](CURRENT_STATE.md), then inspect newer commits. The repository, not a chat transcript, is the durable source of truth.

**External reviewers:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The project welcomes hostile review, counterexamples, literature corrections and independent reproduction. GitHub Issues are the preferred place to report a suspected flaw.

Earlier navigation and evidence are retained verbatim in [`README_EARLIER_2026-09-14.md`](README_EARLIER_2026-09-14.md). The recovery account through the selected-loss checkpoint is [`README_RECOVERY_DETAILS_2026-09-14.md`](README_RECOVERY_DETAILS_2026-09-14.md). Their historical live-status statements are superseded by this page and the current handoff. The protected reviewer index below is retained unchanged.

## How this research develops general theory

Specific graph orders serve as laboratories for structural principles, not as a substitute for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates graph structure into selected/residual incidences, label demands, source loads, destination caps and missing-pair constraints:

```text
a=n-1-Delta, b=Delta, t=e(G)-b(a+1).
```

The working cycle is graph structure, exact constraints, finite experiments, structural theorem extraction, hostile counterexample search, separately structured verification, and return to the all-order inequality. Failed approaches, bugs, counterexamples and audit challenges remain preserved. Survival of a relaxation never implies graph realizability.

## Current structural route

### Exact q-stratified minimum and its scope

The [q-stratified minimum-cut theorem](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_MINCUT_EXACTNESS.md) derives, under its fixed-q cap monotonicity hypotheses,

```text
min_A[H(A)-D(A)] = min_A[U_q(A)-D(A)].
```

This is compatible with positive crossing statistic C_q on particular source sets, even the maximal minimizer. Proving C_q(M+)=0 is no longer a prerequisite for an exact q-stratified minimum. The [type-complete witness](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md) and [threshold normal form](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) replace target-by-target flow with complete types, cap tails, source order statistics and histogram rectangles.

High-q-tail sufficiency is still NOT a universal theorem. The preserved [red-team correction](https://github.com/paullenz/MurtySimon742/commit/93c9e8995c57e69c238396f20641a0dc84bb4754) rules out several weaker formulations. In particular z counts zero-demand labels and is not constrained by z<=E. The full type-complete threshold route remains available even if a narrower tail conjecture fails.

### Two defects and exact selected-excess losses

The [two-defect decomposition](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/BRIDGE_TWO_DEFECT_DECOMPOSITION.md) separates

```text
D0=S-r-2t>=0,  E=Esel=Q-S>=0,  Q=r+2t+D0+E.
```

Set k=b-a-1>=0 and N(h)=#{u:q_u>=h}. The [selected-excess tail-loss identity](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SELECTED_EXCESS_TAIL_LOSS_BUDGET.md) gives

```text
h_j=min(E,z)+floor(max(E-z,0)/j)+1,  j=1,...,k+1,
L_E=sum_j N(h_j),
P_u=rho_u+k-ell_E(q_u)-eta_u,
L_K=sum_u eta_u.
```

Here ell_E is selected-excess cap loss and eta is the additional, non-double-counted potential-pair cap loss. The exact global necessary budget is

```text
2t+D0+E+L_E+L_K<=bk.
```

For any source set A, with unused receiver capacity V(A) and demand q_out(A) outside A,

```text
H(A)-D(A)=bk-(2t+D0+E)-L_E-L_K+q_out(A)-V(A).
```

These are hand-usable coordinates for the existing cap and Hall screens, not new computational exclusions beyond those same screens. The [local audit](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/EXCESS_TAIL_LOSS_AUDIT.md) passed 179,375 pointwise identities, 171,504 exhaustive source-set checks and 10,000 deterministic random profiles. Code, frozen JSON, a harness-correction record and CI workflow are committed; local PASS is not remote CI completion or external review.

### New interval-tail synthesis

The concurrently developed [interval-budget package](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md) has been preserved and reconciled with the selected-loss identity in [`SELECTED_LOSS_SYNTHESIS.md`](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/SELECTED_LOSS_SYNTHESIS.md).

For the tail T_tau={u:q_u>=tau}, retain the upper compatibility threshold and diagonal deletion but temporarily drop reverse compatibility. Let Omega_tau be target capacity unfillable even by that interval relaxation. Let Xi_tau>=0 be its exact reverse-compatibility correction. Then

```text
V(T_tau)=Omega_tau+Xi_tau,
Delta_tau=Q_tau-H_tau
 =2t+D0+E+L_E+L_K+Omega_tau+Xi_tau-Q_<tau-bk.
```

Consequently

```text
2t+D0+E+L_E+L_K+Omega_tau-Q_<tau > bk
```

is a sufficient tail-failure criterion. **Universal existence of such a threshold remains OPEN.**

The newly committed [replay summary](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/REPLAY_SUMMARY.json) reports interval-tail detection of all **205,919** target-Hall failures in the original **201,493,148-profile, 15-state pilot**, with separately implemented arithmetic on the same exported profiles. It also retains **32 profiles with a strict reverse-correction gap**: interval detection is not universal pointwise exactness. This is local replay on shared generation and stopping rules, not a full-frontier scan, independent generation, third-party reproduction or an all-order theorem. The recovery session inspected this newly committed evidence; it did not itself independently rerun that full export.

An [exact three-profile certificate](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/FIXED_WEIGHT_OBSTRUCTION.json) now rules out one common nonnegative weighting that detects all three profiles; it does not rule out weights depending on E or the profile. The [summed-tail pressure note](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SUMMED_Q_TAIL_PRESSURE.md) remains the weighted-identity foundation.

## Frontier and audit gates

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 (NOT PROMOTED)
```

The final relational cross-audit `34854911792` remained queued with no conclusion when last fetched in this recovery. Promotion requires exact state-by-state agreement between the two relational implementations, zero unresolved cases, then a separate ledger-promotion step. N34 and N35 provenance must remain separate.

The dedicated high-q-tail and corrected minimum-cut remote jobs were also queued at the recovery's last checks. That is distinct from the newly committed local interval replay. See [`CURRENT_STATE.md`](CURRENT_STATE.md) for IDs and evidence boundaries.

The fixed-order candidate packages remain n=25 and n=27 through n=35, with extremal bounds 156,182,196,210,225,240,256,272,289,306 respectively and equality the balanced complete bipartite graph. The general candidate maximum-degree theorem remains: for n>=6, Delta(G)>=(7/12)n implies e(G)<floor(n^2/4). All retain external-review and novelty boundaries. The 3,607 scalar states are not surviving graphs or unresolved obligations in those fixed-order packages.

<!-- REVIEW-MATERIALS:START -->
## Papers and review materials

This reviewer-facing index is intentionally duplicated here as a protected navigation surface. The detailed canonical status remains [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md), and new editions must update both surfaces rather than deleting this section.

### Fixed-order papers and packages

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md) — [manuscript PDF](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf).
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md) — [manuscript PDF](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf).
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md) — [manuscript PDF](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf).
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md) — [manuscript PDF](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) and [verification companion PDF](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf).
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md) — [manuscript PDF](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) and [verification companion PDF](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf).
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/reviews/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md).
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md) — source-first proof/review package; [exact equality ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md).
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md).
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

## Next proof obligation and trust boundary

Find an adaptive threshold whose interval-unfillable capacity, together with selected-excess and potential-pair losses, exceeds the bridge headroom and omitted low-q demand. The 239 synthetic target-Hall passes in the interval package show that its listed scalar/incidence relaxations alone cannot force a deficient tail for every profile; further full-bridge structure is needed. Retain the exact type-complete q-layer route when a tail reduction is insufficient.

Hand derivation, finite checks, separately structured internal arithmetic, remote CI, external mathematical review and third-party reproduction are different statuses. No timeout, missing output, unsuccessful search or floating infeasibility is a certificate. The largest correlated dependency remains the graph-to-constraint bridge, especially quasi-edge selection/injection and forcing.

The independent maximum-cut/stability route remains open: e(G)=|X||Y|+I-M, so I<=M would suffice. Its failed direct matching shortcut and earlier structural routes remain preserved in the archived chronology. No frontier promotion was performed during this recovery.
