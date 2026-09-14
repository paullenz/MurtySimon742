# Murty–Simon / Erdős Problem #742

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **Updated 14 September 2026 through the interval-tail budget and localized selected-excess cap, including proof `449a268f93600d78660e02b09d65e5304a2ca0bf`, frozen evidence `cbe1076c87b1cb1eccff409a14dcac7839fd9de6` and replay workflow `e7618ca2caa6438beea5b613638d9fa45297705b`.**

The canonical promoted finite frontier remains **1,971 exclusions / 3,607 survivors**, with **977 quantified whole-state closures**. The **2,655 recovered relational candidate exclusions remain unpromoted**. The unrestricted conjecture is **not claimed proved**. Independent mathematical review, novelty assessment and genuinely independent third-party computational reproduction remain OPEN.

**Canonical repository:** `paullenz/MurtySimon742`; see [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md). **Research restarts:** read [`CURRENT_STATE.md`](CURRENT_STATE.md), then inspect newer commits. The repository, not a chat transcript, is the durable source of truth.

**External reviewers:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The project welcomes hostile review, counterexamples, literature corrections and independent reproduction. GitHub Issues are the preferred place to report a suspected flaw.

The earlier README is preserved verbatim in [`README_EARLIER_2026-09-14.md`](README_EARLIER_2026-09-14.md), including historical statistics, older priorities and route chronology. Its live-status statements are superseded by this page and the current handoff. The protected reviewer index below is retained unchanged.

## How this research develops general theory

Specific graph orders serve as laboratories for structural principles, not as a substitute for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates graph structure into selected/residual incidences, label demands, source loads, destination caps and missing-pair constraints.

```text
a=n-1-Delta,
b=Delta,
t=e(G)-b(a+1).
```

The working cycle is graph structure, exact constraints, finite experiments, structural theorem extraction, hostile counterexample search, separately structured verification, and return to the all-order inequality. Failed approaches, bugs, counterexamples and audit challenges remain preserved. Survival of a relaxation never implies graph realizability.

## Current mathematical route

### 1. Exact q-stratified minimum, not pointwise crossing elimination

The [q-stratified minimum-cut theorem](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_MINCUT_EXACTNESS.md) derives, under its fixed-q cap monotonicity hypotheses,

```text
min_S [H(S)-D(S)] = min_S [U_q(S)-D(S)].
```

This is compatible with positive crossing statistic C_q on particular source sets, even the maximal minimizer. The old requirement to prove C_q(M+)=0 is no longer a prerequisite for an exact q-stratified minimum. Do not conflate pointwise equality with equality of minima.

The [type-complete witness corollary](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md) and [q-layer threshold normal form](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) express that minimum through type sets, cap tails, source order statistics and two-dimensional histogram rectangle counts. Their exact scope remains the target-Hall relaxation, not graph realizability.

These are preserved hand derivations with local finite verification. Threshold CI `34871045562` is green. The corrected minimum-cut CI replay `34878019517` was still queued at recheck. Its predecessor `34868771056` completed the mathematical verifier but failed on JSON list formatting in a raw text comparison; this is a workflow-comparison problem, not a mathematical counterexample. The fix retains all frozen value checks.

### 2. High-q tails and interval budgets: useful, not a universal theorem

The frozen 812 difficult profiles all have deficient high-q tails. However, the [preserved red-team correction](https://github.com/paullenz/MurtySimon742/commit/93c9e8995c57e69c238396f20641a0dc84bb4754) shows that arbitrary monotone caps, the current cap formula alone, and even selected-incidence feasibility without the global bridge ledger do not imply tail sufficiency. The zero-demand count z must not be incorrectly restricted by z<=E.

The [interval-tail package](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md) now gives a sufficient adaptive threshold inequality, with exact reverse-compatibility correction. Its committed replay detects all 205,919 old target-Hall failures in the original 15-state pilot using the interval bound; 32 profiles have a strict interval/exact gap at some threshold. This is finite reconnaissance with shared generation and independently implemented arithmetic, not a universal interval-exactness or tail-sufficiency theorem.

The original q-stratified artifact from run `34859094097` has also been retrieved: all 205,919 failures have C_q=0. This finite observation is separate from pointwise or minimum-cut theorems. The dedicated q-tail CI run `34876612516` must still be checked independently; its queued status must not erase the separately preserved completed local replay evidence.

The interval package preserves an exact three-profile certificate showing that no common nonnegative weighting detects every one of the 812 profiles with the OLD capacities. Adaptive thresholds remain viable. Its synthetic scalar/incidence relaxation also has target-Hall passes, proving that those weaker hypotheses alone cannot force a deficient tail on every profile.

The narrowed full-bridge q-tail question remains OPEN. The full q-layer threshold representation and crossing-wall route remain available.

### 3. Exact two-defect bridge and weighted pressure

The [two-defect decomposition](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/BRIDGE_TWO_DEFECT_DECOMPOSITION.md) separates two historically conflated quantities:

```text
D0 = S-r-2t >= 0,       zero-demand bridge deficit,
Esel = Q-S >= 0,        selected excess,
Q = r+2t+D0+Esel.
```

The [summed high-q-tail pressure note](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SUMMED_Q_TAIL_PRESSURE.md) gives exact weighted layer-cake inequalities. A single quadratic projection is not a substitute for adaptive thresholds. Structural surplus is t; q-thresholds are tau.

### 4. Selected-excess tail-loss budget

The [hand derivation](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SELECTED_EXCESS_TAIL_LOSS_BUDGET.md) converts the selected-excess receiver cap into an exact short sum of high-q tail losses. Put k=b-a-1>=0, E=Esel, z=#{i:s_i=0}, and N(h)=#{u:q_u>=h}. Define

```text
h_j(E,z)=min(E,z)+floor(max(E-z,0)/j)+1,
L_E=sum_{j=1}^{k+1} N(h_j(E,z)).
```

With L_K the additional, non-double-counted potential-pair cap loss,

```text
2t+D0+E+L_E+L_K <= bk
```

is necessary. For every source set A0 the exact Hall margin is

```text
H(A0)-D(A0)
 = bk-(2t+D0+E)-L_E-L_K+q_out(A0)-V(A0),
```

where V is receiver capacity unused by A0 and q_out is demand outside A0.

This turns the existing aggregate cap screen into a hand-usable threshold budget and identifies exactly what additional cut-specific shortage is needed. **It is not an extra computational exclusion beyond the existing sum-P screen.**

The [local audit](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/EXCESS_TAIL_LOSS_AUDIT.md) passed 179,375 pointwise identities, 171,504 exhaustive source-set checks, and 10,000 deterministic random profiles. A reproducible verifier, frozen JSON and CI workflow are committed. Local PASS is not remote CI completion or external review.

### 5. New localized selected-excess cap — additional bridge strength

The [localized-excess package](project/research/general_n/2026-09-14-localized-excess-v1/README.md) strengthens the target caps rather than merely rewriting them. For a residual threshold eta>=0 define

```text
U_eta={u:rho_u<=eta},  L_eta={i:s_i<=eta},
C_eta=Esel+sum_{i in L_eta}s_i-sum_{u in U_eta}q_u.
```

All selections from U_eta must land in L_eta. For a source w with rho_w>eta, let k count its selected labels in L_eta. Canonical endpoint forcing yields

```text
C_eta >= k+(q_w-k)(p_w-rho_w+1)  when p_w>=rho_w.
```

This gives an explicit floor cap after maximizing over feasible k. Eta=0 recovers the existing zero-demand cap exactly; positive eta captures excess already forced into positive-demand labels. In particular,

```text
q_w>C_eta and rho_w>eta => p_w<=rho_w-1.
```

If Z collects sources certified this way and delta=b-a, the two-defect budget strengthens to

```text
2t+D0+Esel+delta*|Z| <= b(delta-1).
```

Retain all other caps, especially exact potential-pair degrees. Two old surviving PROFILE witnesses associated with states 1626 and 2984 now fail: their required loads are 51 and 57, while localized total target capacities are 50 and 52. **This does not exclude either entire scalar state.**

On the frozen 812 difficult profiles, cap vectors tighten on 748, uniform-weight detections increase from 476 to 773, and 630 now fail already at tau=1. All 812 remain detectable by adaptive exact tails. The independent implementation passes 133,586 exhaustive incidence configurations, 6,880 floor cases and 3,000 ledger-preserving incidence mutations. These are necessary-condition/incidence tests, not realized Murty graphs or external acceptance.

The [experiment log](project/research/general_n/2026-09-14-localized-excess-v1/EXPERIMENT_LOG.md) preserves the standing hostile examples, a rejected marginal-exactness shortcut and an incomplete wider scanner run. No timeout result is promoted. The new cap is the current priority for combining localized bridge information with adaptive threshold losses.

## Finite frontier and audit gates

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 (NOT PROMOTED)
```

The final relational cross-audit `34854911792` remains incomplete: the plan and first visible audit shards passed, but a paginated recheck still found shard 255 queued. Promotion requires full coverage of all 2,655 candidates, exact agreement between `scan_post_pair_relational.cpp` and `scan_post_pair_relational_types.cpp`, zero unresolved cases, a successful aggregate and then a separate ledger-promotion step. N34 and N35 provenance remain separate.

Frozen-ledger CI `34875592126` has now passed, including combined survivor coverage. That is not the separate relational promotion audit. These scalar states are not surviving graphs and are not unresolved obligations in the fixed-order candidate proofs.

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

## Immediate research priorities

Use localized selected excess to strengthen target capacities, then combine the exact two-defect budget with adaptive interval-tail loss or the exact q-layer histogram formulation. The two old surviving profile witnesses expose a joint selected-incidence/endpoint-forcing obstruction; complete scalar-state searches and independent replay are still required. Uniform weighting improves materially but does not cover all 812 profiles.

Complete the independent localized-cap CI and bounded, checkpointed broader tests. Separately finish the 2,655-candidate relational audit and successful aggregate before any ledger promotion. Preserve failures and harness corrections. External review remains focused on quasi-edge selection/injection, bridge forcing, endpoint loads, incoming/source caps, and the exact Hall reductions. Fixed-q monotonicity requirements must be checked before applying an old canonical-witness theorem to any newly modified capacity model.

The independent maximum-cut/stability route remains open: for a cut X|Y, e(G)=|X||Y|+I-M, so finding I<=M would suffice. The failed one-internal-edge/one-cross-nonedge matching shortcut remains preserved in the earlier route record. Crossing-wall charge and saturation-wall arguments remain retained fallbacks.

## Trust boundary

Hand derivation, finite verification, a separately structured internal implementation, remote CI replay, external mathematical review and third-party reproduction are different statuses. No timeout, missing output, unsuccessful search, floating infeasibility report or unreviewed discovery is a certificate. The largest correlated mathematical dependency remains the canonical graph-to-constraint bridge. The localized cap changes the structural strength and profile-level evidence, not the promoted whole-state frontier.
