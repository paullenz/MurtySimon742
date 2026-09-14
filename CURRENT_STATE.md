# Murty–Simon / Erdős #742 — current state handoff

**Synchronized 14 September 2026 through research commit `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb` (selected-excess tail losses and Hall slack budget).** This documentation update carries no frontier promotion. Inspect commits newer than that research checkpoint before resuming.

Canonical repository: `paullenz/MurtySimon742`, repository ID `1359206057`. See `CANONICAL_REPOSITORY.md`. Do not use the legacy repository name. The repository, not any chat transcript, is the durable source of truth.

The pre-recovery handoff is preserved verbatim in `CURRENT_STATE_EARLIER_2026-09-14.md`. It is a HISTORICAL snapshot, including old audit statuses and a superseded emphasis on proving C_q(M+)=0. Current state follows.

## 1. Recovery and exact synchronization point

The interrupted chat's supplied checkpoint was `0e6546e8947b43896d0c8f5eebde8335b8d95f11`, the universal two-defect decomposition. On recovery main was five commits ahead, at `81560e92698d07992df4a53976ee1ea8efaaeb4d`.

Those five commits added high-q-tail pilot instrumentation, fixed its TSV generator, launched the full frozen pilot, added `SUMMED_Q_TAIL_PRESSURE.md`, and repaired the minimum-cut audit's whitespace-sensitive JSON comparison. The repair preserves JSON values and array ordering rather than weakening the mathematical baseline.

New research in the recovery: `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb`. It adds a proof note, standard-library verifier, frozen JSON, explicit audit/harness-correction record, and CI workflow. No uncommitted content from the failed chat was recoverable here; do not invent any.

## 2. Canonical promoted frontier — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered candidate exclusions: 2,655 (NOT PROMOTED)
```

Protect the closure ledger with `tools/check_n34_whole_state_ledger.py`. Preserve N34/N35 provenance separately. The 943-state potential-pair family is part of the canonical whole-state ledger, not a fresh recovery exclusion.

The layer/state-safe discovery run `34820187136` and long-budget recovery `34844403328` were recorded complete in the preceding handoff. The recovered 2,655-candidate aggregate is pinned by SHA256 `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`.

The final cross-implementation audit `34854911792` was fetched directly in this recovery: status queued, conclusion null. Its earlier workflow-output bug and relaunch remain documented in the archived handoff. Promotion requires exact state-by-state agreement of `scan_post_pair_relational.cpp` and `scan_post_pair_relational_types.cpp`, zero unresolved cases, then a separate ledger-promotion commit. Do not subtract 2,655 from 3,607 before that gate passes.

## 3. Fixed-order candidates and external review

The preserved candidate frontier is unchanged: n=25 and n=27 through n=35, with extremal bounds 156,182,196,210,225,240,256,272,289,306 respectively and equality the balanced complete bipartite graph. n=29's difficult Delta=16 branch and n=34's final heavy branch have hand-proof replacements. These are candidate proofs; external mathematical acceptance is OPEN.

The general candidate maximum-degree theorem remains: n>=6 and Delta(G)>=(7/12)n imply e(G)<floor(n^2/4). The reviewer index and root README protected materials section remain authoritative navigation surfaces and must not be removed.

These fixed-order packages are separate from the 3,607 scalar states. No current unpromoted relational candidate is being used to claim a fixed-order proof upgrade.

## 4. Correct current exact Hall route

Package: `project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`.

The preserved chain includes whole-type compression, quotient flow, sharp dominance, canonical antichain/staircase, compatible-copy exactness and exterior residual expansion. Read the associated audit files for their exact completed internal scopes; this recovery did not re-audit every earlier theorem.

The materially newer step is `Q_STRATIFIED_MINCUT_EXACTNESS.md`:

```text
min_S[H(S)-D(S)] = min_S[U_q(S)-D(S)]
```

under fixed-q target-cap monotonicity and the stated numerical compatibility hypotheses. Pointwise U_q(S)=H(S) is false in general. Positive C_q(M+) is compatible with equality of the minima. Consequently proving C_q(M+)=0 is not a prerequisite for the current exact reduction.

`Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md` restricts the q-stratified minimization to complete types. `Q_LAYER_THRESHOLD_NORMAL_FORM.md` writes the receiver layers through cap c-tails, selected-source order statistics and rectangle counts. Its local frozen totals were 46,800 profiles, 666,600 source sets and 30,000 random trials. Local checks and repository derivation are not external acceptance.

The repaired minimum-cut CI replay is run `34878019517`; its verify job `104089980265` was fetched in this recovery and remained queued. Do not call this corrected remote replay PASS until it completes and its evidence is inspected.

## 5. High-q-tail conjecture: narrowed, not promoted

The frozen 812 difficult profiles have deficient high-q tails. First deficient thresholds are 2:426, 3:191, 4:195. This is a frozen empirical fact, not a universal theorem.

Commit `93c9e8995c57e69c238396f20641a0dc84bb4754` preserves counterexamples to several overbroad statements. Arbitrary monotone capacities are insufficient. The current cap formula alone is insufficient. Selected-incidence feasibility without the global bridge ledger is also insufficient. z counts zero-demand labels and must not be restricted by z<=E. Some earlier tests imposed that false restriction and are not accepted as evidence for the narrowed conjecture.

The surviving question is whether an appropriate ledger-current class admits a high-q-tail minimum witness. The full q-layer exact reduction remains available if that conjecture fails. Do not state that a full graph bridge counterexample has been found: the preserved hostile profiles fail bridge ledger conditions.

The broader 201,493,148-profile/205,919-Hall-failure frozen pilot is run `34876612516`. Job `104085266949` was fetched in this recovery and remained queued. Do not claim 205,919/205,919 tail detection, exact tail minima, or zero inversions from a queued run. The older q-crossing and zero-inversion workflows were not freshly certified here.

## 6. Two defects, weighted pressure, and new exact tail losses

Bridge parameters:

```text
a=n-1-Delta, b=Delta, t=e(G)-b(a+1),
D0=S-r-2t>=0, E=Esel=Q-S>=0,
Q=r+2t+D0+E.
```

`BRIDGE_TWO_DEFECT_DECOMPOSITION.md` separates D0 from E; do not conflate the older uses of the letter E. `SUMMED_Q_TAIL_PRESSURE.md` gives weighted tail identities and the exact top-compatible quadratic consequence. Its reported 812-profile quadratic detection is 476/812; that is reconnaissance, not an all-order theorem or a new frontier count.

NEW: `SELECTED_EXCESS_TAIL_LOSS_BUDGET.md`. Put k=b-a-1>=0, z=#{i:s_i=0}, and

```text
h_j=min(E,z)+floor(max(E-z,0)/j)+1,  j=1,...,k+1,
ell_E(q)=sum_j 1_{q>=h_j},
eta_u=max(0,c_u+k-d_K(u)-ell_E(q_u)),
L_E=sum_j #{u:q_u>=h_j},  L_K=sum_u eta_u.
```

The exact current target cap is

```text
P_u=rho_u+k-ell_E(q_u)-eta_u.
```

The simple-degree cap is redundant only under c_u<=a. Negative computed P rejects the branch; do not clip it to zero. Every legal orientation must obey

```text
2t+D0+E+L_E+L_K<=bk.
```

For any source set A0, define V(A0)=sum_w(P_w-y_w(A0))_+ and q_out as total q outside A0. Then

```text
H(A0)-D(A0)
 = bk-(2t+D0+E)-L_E-L_K+q_out(A0)-V(A0).
```

This is the existing aggregate cap screen and exact Hall margin in structural loss coordinates, NOT a new computational screen stronger than those same conditions. In particular the frozen 812 profiles already passed the aggregate screen, so this scalar budget alone cannot newly eliminate them.

### New local audit

`EXCESS_TAIL_LOSS_VERIFICATION.json` records PASS:

```text
pointwise cap-loss identities: 179,375
exhaustive small profiles:       6,381
exhaustive source-set checks:  171,504
random profiles:               10,000
random nonnegative-cap cuts:   93,010
```

`verify_excess_tail_loss.py` is standalone and standard-library-only. `EXCESS_TAIL_LOSS_AUDIT.md` retains the corrected local regression-fixture expectation [2,3,3,0] for the old non-tail example. No theorem formula was patched to fit a failing mathematical case.

`.github/workflows/verify-excess-tail-loss.yml` is committed for remote replay, with strict parsed-JSON value equality. Local PASS is not remote CI PASS, independent third-party reproduction or external mathematical review.

## 7. Next mathematical priority

Use the exact source-cut identity to lower-bound V(A0)-q_out(A0) beyond the remaining cap budget on the branches being targeted. An adaptive high-q tail is the first candidate, not an assumed sufficient family. Retain the complete-type q-layer threshold minimization as the fallback exact route.

A focused diagnostic should decompose the frozen 812 profiles by selected-excess loss, additional pair loss, and cut vacancy; then identify which part admits an all-order lower bound. Do not rerun or relabel the already-passed aggregate screen as new progress.

Logical direction matters: actual graph orientations satisfy Hall. An exclusion theorem must show OTHER counterexample-branch bridge constraints force a negative Hall margin somewhere. Proving all relaxed profiles Hall-feasible would not prove Murty-Simon.

In parallel, inspect the queued tail/minimum-cut replays and the independent relational audit when results exist. Do not duplicate costly runs merely because they are queued. Do not promote fixed-order, general, empirical or CI claims beyond inspected evidence.

## 8. Preservation and trust boundaries

Preserve proofs, rejected lemmas, counterexamples, harness bugs, verifier code, exact outputs and audit challenges. Distinguish derivation, finite checks, separately structured internal audit, remote replay, external mathematical review and third-party reproduction. Preserve reviewer links and update both review navigation surfaces for any actual new reviewer edition.

The canonical bridge remains a correlated external-review dependency, especially quasi-edge selection/injection, forcing, endpoint loads and target/source caps. The unrestricted conjecture remains unproved by this project. No new frontier promotion was performed in this recovery.
