# Murty–Simon / Erdős #742 — current state handoff

**Synchronized 14 September 2026 through `d1e20da87e8d8dcda3633e550b8b5556b6e7c9ee`, reconciling concurrent selected-excess and interval-tail research.** Inspect newer commits before resuming. Canonical repository: `paullenz/MurtySimon742`, ID `1359206057`; see `CANONICAL_REPOSITORY.md`.

The repository, not chat text, is the durable source of truth. This reconciliation does not promote any finite exclusion or assert an all-order proof.

## 1. Recovery and concurrent-write handling

The interrupted-chat checkpoint was `0e6546e8947b43896d0c8f5eebde8335b8d95f11`. Main was initially five commits ahead, at `81560e92698d07992df4a53976ee1ea8efaaeb4d`: high-q-tail instrumentation, TSV repair, pilot launch, summed pressure identity and a whitespace-safe minimum-cut JSON comparison.

This session derived, locally verified and pushed `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb`, the exact selected-excess tail-loss budget. It then prepared a documentation commit, `ff0a59d023264e221a9ed93135a13dbc9b2de929`. Its non-forced main update was correctly rejected because main had advanced through:

- `de82393062163dc2ffab10b90ba68ce4a0f7a741`: interval-tail receiver-loss budget and exact fixed-weight obstruction;
- `d1e20da87e8d8dcda3633e550b8b5556b6e7c9ee`: verifier, frozen replay summaries and explicit synthesis with the selected-loss result.

Those newer research files are retained unchanged. The synchronization is based on their tree, not on the stale pre-interval tree. No force push or rollback is allowed. Recheck main before any future write.

Detailed pre-interval recovery notes are preserved verbatim in `RECOVERY_STATE_DETAILS_2026-09-14.md` and `README_RECOVERY_DETAILS_2026-09-14.md`. The older crossing-gap-era handoff and README are preserved in `CURRENT_STATE_EARLIER_2026-09-14.md` and `README_EARLIER_2026-09-14.md`. Their status statements are historical, not current. No uncommitted failed-chat content was recovered; do not invent it.

## 2. Canonical promoted frontier — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered candidate exclusions: 2,655 (NOT PROMOTED)
```

Protect `tools/check_n34_whole_state_ledger.py` and preserve separate N34/N35 provenance. The 943-state potential-pair family is already part of the canonical closure ledger.

The recovered aggregate SHA256 is `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`. The final two-implementation audit `34854911792` was directly fetched in this recovery and remained queued with conclusion null. Promotion requires exact state-by-state agreement between `scan_post_pair_relational.cpp` and `scan_post_pair_relational_types.cpp`, zero unresolved cases, then a separate ledger-promotion commit. Do not subtract 2,655 from 3,607 before that gate passes.

Fixed-order candidates n=25 and n=27 through n=35, and the general 7/12 maximum-degree candidate theorem, are unchanged; external review remains OPEN. These packages are separate from the 3,607 scalar states. Reviewer navigation must be retained at both root README and `releases/REVIEW_READY_INDEX.md`.

## 3. Exact q-stratified route and false shortcuts

Package A: `project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`.

The earlier whole-type/quotient-flow, sharp dominance, canonical staircase, compatible-copy and exterior-expansion chain remains preserved. The important newer theorem is `Q_STRATIFIED_MINCUT_EXACTNESS.md`:

```text
min_A[H(A)-D(A)]=min_A[U_q(A)-D(A)]
```

under its stated fixed-q cap monotonicity and compatibility assumptions. Pointwise equality is false in general; C_q(M+) can be positive. Proving C_q(M+)=0 is no longer a prerequisite. Complete types suffice (`Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md`), and `Q_LAYER_THRESHOLD_NORMAL_FORM.md` gives exact histogram/order-statistic formulas.

The high-q-tail sufficiency conjecture is NOT proved. The correction at `93c9e8995c57e69c238396f20641a0dc84bb4754` preserves failures under arbitrary monotone caps, the current cap formula alone and selected-incidence feasibility without the global bridge ledger. z is the zero-demand LABEL count; z<=E is an invalid restriction. D0 and Esel are different quantities. The full exact q-layer route survives failure of a tail conjecture.

The dedicated high-q-tail remote pilot `34876612516` (job `104085266949`) and repaired minimum-cut replay `34878019517` (job `104089980265`) were queued at this recovery's last direct checks. No completed remote PASS is asserted for them. The local interval replay below is separate evidence and must not be confused with those jobs.

## 4. Exact selected-excess loss result from this recovery

Use

```text
a=n-1-Delta, b=Delta, t=e(G)-b(a+1), k=b-a-1>=0,
D0=S-r-2t>=0, E=Esel=Q-S>=0, Q=r+2t+D0+E,
z=#{i:s_i=0}, N(h)=#{u:q_u>=h}.
```

`SELECTED_EXCESS_TAIL_LOSS_BUDGET.md` defines

```text
h_j=min(E,z)+floor(max(E-z,0)/j)+1, j=1,...,k+1,
ell_E(q)=sum_j 1_{q>=h_j},
eta_u=max(0,c_u+k-d_K(u)-ell_E(q_u)),
L_E=sum_j N(h_j), L_K=sum_u eta_u.
```

The exact current cap is P_u=rho_u+k-ell_E(q_u)-eta_u. The simple-degree cap is redundant only under c_u<=a. Negative P rejects the branch and must not be clipped to zero.

The global necessary budget is

```text
2t+D0+E+L_E+L_K<=bk.
```

For any source set A, let V(A)=sum_w(P_w-y_w(A))_+ and q_out(A) be demand outside A. Then

```text
H(A)-D(A)=bk-(2t+D0+E)-L_E-L_K+q_out(A)-V(A).
```

This is a structural reformulation of the existing aggregate cap and Hall screens, not a new screen stronger than them. In particular, the 812 difficult profiles already passed the aggregate cap check; that scalar check alone cannot newly exclude them.

Local exact verification was run and rerun in this session with identical parsed JSON values:

```text
pointwise identities:         179,375
exhaustive small profiles:      6,381
exhaustive source-set checks: 171,504
random profiles:              10,000
random nonnegative-cap cuts:  93,010
result: PASS
```

See `verify_excess_tail_loss.py`, `EXCESS_TAIL_LOSS_VERIFICATION.json` and `EXCESS_TAIL_LOSS_AUDIT.md`. The audit retains a corrected local fixture expectation [2,3,3,0] for an archived non-tail example; no theorem formula was patched. The GitHub replay workflow is committed, but local PASS is not remote CI PASS or external reproduction.

## 5. Newer concurrent interval package and the synthesis

Package B: `project/research/general_n/2026-09-14-q-tail-interval-budget-v1/`.

Its README, `SELECTED_LOSS_SYNTHESIS.md` and `REPLAY_SUMMARY.json` were fetched and reviewed during reconciliation. The core definitions are:

```text
T_tau={u:q_u>=tau},
J_w(tau)=max(0,N_tau-N_{c_w+2})-1_{q_w>=tau},
I_w(tau)=#{u:q_u>=tau and c_u<q_w},
y_w=J_w-I_w,
Omega_tau=sum_w(P_w-J_w)_+,
Xi_tau=sum_w[I_w-(J_w-P_w)_+]_+.
```

J drops reverse compatibility only. The exact vacancy is V(T_tau)=Omega_tau+Xi_tau. Combining the two research lines gives

```text
Delta_tau=Q_tau-H_tau
 =2t+D0+E+L_E+L_K+Omega_tau+Xi_tau-Q_<tau-bk.
```

Dropping nonnegative Xi gives a sufficient interval-tail obstruction. The current proof target is a theorem guaranteeing an appropriate tau with

```text
2t+D0+E+L_E+L_K+Omega_tau-Q_<tau>bk
```

on the particular full-bridge counterexample branches targeted. Universal threshold existence is OPEN.

### Newly committed empirical evidence: reported local replay, not rerun here

`REPLAY_SUMMARY.json` reports:

```text
original pilot scalar states:                     15
profiles generated with original stopping rules: 201,493,148
exact target-Hall failures:                         205,919
interval-tail detections:                          205,919
all thresholds interval-exact:                     205,887
profiles with a reverse-correction gap:                  32
exported profiles checked by separate arithmetic:  205,931
```

The latter count is 205,919 failures plus 12 Hall passes. All 812 difficult profiles and all 6,667 of their tested threshold rows are interval-exact. Provenance identifiers and hashes are in the summary; original pilot run `34859094097`, artifact `10356424619`.

These data were produced by the concurrent session and inspected as committed evidence here. The full profile export and original artifacts were NOT independently regenerated or redownloaded during this reconciliation. Shared profile generation, original early stopping, local replay and independent arithmetic are different from independent generation, full-frontier coverage, remote CI completion or third-party reproduction. No new whole-state count is promoted from them.

The preserved strict-gap state-226 example has tau=1 exact H=26 versus interval U=28. Thus do not upgrade 205,919/205,919 detection to universal interval equality.

The exact fixed-weight certificate uses three diagnostic deficiency vectors A,B,C with 7A+12B+10C coordinatewise nonpositive. It rules out a common nonnegative weighting that is strictly positive on all three, not weights depending on E or on the profile.

The synthetic audit's listed scalar/incidence domain has 239 target-Hall passes. Therefore those relaxed hypotheses alone cannot force a deficient tail for every profile. The full graph/quasi-edge bridge is not realized in that experiment and remains a distinct potential source of stronger constraints.

## 6. Next priority and audit boundaries

Exploit the combined loss budget to bound interval-unfillable capacity or exact vacancy minus omitted low-q demand, using FULL bridge structure beyond the already-tested scalar and incidence conditions. Adaptive thresholds are the leading simple witness family, not an assumed complete family. Preserve the exact complete-type q-layer route as the fallback.

Logical direction matters: actual graph orientations satisfy Hall. Exclusion requires OTHER hypothetical-counterexample constraints to force negative Hall margin somewhere. Proving every relaxed profile Hall-feasible would not prove Murty-Simon.

Preserve all proofs, failed generalizations, verifier code, counterexamples, fixture corrections and evidence. Distinguish internal derivation, local finite checks, separately structured arithmetic, remote replay, external mathematical review and third-party reproduction. The quasi-edge selection/injection and forcing bridge remains a high-value correlated external-review dependency. No force pushes, unreviewed frontier promotion or graph-realizability claims are authorized by this synchronization.
