# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. Latest research checkpoint inspected: `449a268f93600d78660e02b09d65e5304a2ca0bf`.** Inspect newer commits before resuming. This page supersedes older live-status statements elsewhere, including the root README's account through the selected-loss checkpoint.

Canonical repository: `paullenz/MurtySimon742`, ID `1359206057`. See `CANONICAL_REPOSITORY.md`. The repository, not a chat transcript, is the durable source of truth. No whole-state exclusion or unrestricted proof is promoted by this handoff.

## Recovery and concurrent commits

The failed-chat checkpoint was `0e6546e8947b43896d0c8f5eebde8335b8d95f11`; main initially stood five commits later at `81560e92698d07992df4a53976ee1ea8efaaeb4d`. This session derived, verified and pushed `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb`, the selected-excess tail-loss identity.

Main continued to receive concurrent research:

- `de82393062163dc2ffab10b90ba68ce4a0f7a741`: interval-tail receiver-loss budget;
- `d1e20da87e8d8dcda3633e550b8b5556b6e7c9ee`: verifier, fixed-weight certificate, frozen replay summary and synthesis with the selected-loss identity;
- `d6c818440c736367dae68bd425ce7e6df7fa0bed`: preservation of replay instrumentation and hostile searches;
- `449a268f93600d78660e02b09d65e5304a2ca0bf`: localized selected-excess cap and two specific pilot-profile exclusions.

Two non-fast-forward documentation updates were correctly rejected. This synchronization uses the later research tree and preserves its files. Never force a stale update over concurrent work. No uncommitted text from the failed chat was recovered; do not invent it.

Earlier detailed records are preserved verbatim in `CURRENT_STATE_EARLIER_2026-09-14.md`, `RECOVERY_STATE_DETAILS_2026-09-14.md`, `INTERVAL_RECONCILIATION_DETAILS_2026-09-14.md` and `README_EARLIER_2026-09-14.md`. Their old priorities and queued-job observations are historical.

## Canonical promoted frontier — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered candidate exclusions: 2,655 (NOT PROMOTED)
```

The final two-implementation audit `34854911792` was directly fetched in this recovery and remained queued with conclusion null. Promotion requires exact state-by-state agreement between `scan_post_pair_relational.cpp` and `scan_post_pair_relational_types.cpp`, zero unresolved cases, then a separate ledger-promotion commit. Preserve N34/N35 provenance and the closure-ledger check. Do not subtract 2,655 from 3,607 before that gate passes.

The fixed-order candidate packages n=25 and n=27 through n=35 and the general 7/12 maximum-degree candidate theorem are unchanged. External mathematical review and novelty assessment remain OPEN. These packages are distinct from the scalar generalisation frontier. Preserve reviewer navigation at both root README and `releases/REVIEW_READY_INDEX.md`.

## Exact q-stratified route

In `project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`, read `Q_STRATIFIED_MINCUT_EXACTNESS.md`, `Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md` and `Q_LAYER_THRESHOLD_NORMAL_FORM.md`.

Under their stated hypotheses,

```text
min_A[H(A)-D(A)]=min_A[U_q(A)-D(A)].
```

Pointwise equality is false in general, and C_q(M+) can be positive. Proving C_q(M+)=0 is no longer a prerequisite. The full exact type-complete threshold route does not depend on high-q-tail sufficiency.

The correction at `93c9e8995c57e69c238396f20641a0dc84bb4754` preserves failures of several overbroad tail conjectures. z counts zero-demand LABELS and is not constrained by z<=E. The two defects D0=S-r-2t and Esel=Q-S must not be conflated. Q=r+2t+D0+Esel.

## Selected-loss result actually verified in this recovery

Let k=b-a-1>=0, E=Esel, N(h)=#{u:q_u>=h}, and

```text
h_j=min(E,z)+floor(max(E-z,0)/j)+1, j=1,...,k+1,
ell_E(q)=sum_j 1_{q>=h_j},
eta_u=max(0,c_u+k-d_K(u)-ell_E(q_u)),
L_E=sum_j N(h_j), L_K=sum_u eta_u.
```

`SELECTED_EXCESS_TAIL_LOSS_BUDGET.md` proves the exact old cap identity P_u=rho_u+k-ell_E(q_u)-eta_u and the necessary global budget

```text
2t+D0+E+L_E+L_K<=bk.
```

For any source set A, with unused receiver capacity V(A) and outside demand q_out(A),

```text
H(A)-D(A)=bk-(2t+D0+E)-L_E-L_K+q_out(A)-V(A).
```

This reformulates existing cap/Hall screens and is not stronger computationally than those same screens. Negative computed caps reject the branch; they must not be clipped to zero.

The standard-library verifier was run and rerun with identical frozen JSON values: 179,375 pointwise identities, 6,381 exhaustive profiles, 171,504 exhaustive source sets and 10,000 random profiles (93,010 nonnegative-cap source-set checks), PASS. `EXCESS_TAIL_LOSS_AUDIT.md` preserves a corrected regression-fixture expectation [2,3,3,0]. Local PASS is not external review or remote CI completion.

## Concurrent interval synthesis: inspected committed evidence

Read `project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md`, `SELECTED_LOSS_SYNTHESIS.md`, `REPLAY_SUMMARY.json` and `FIXED_WEIGHT_OBSTRUCTION.json`.

For T_tau={u:q_u>=tau}, the exact vacancy decomposes as V(T_tau)=Omega_tau+Xi_tau: interval-unfillable capacity plus the nonnegative reverse-compatibility correction. The combined exact tail deficiency is

```text
Delta_tau=2t+D0+E+L_E+L_K+Omega_tau+Xi_tau-Q_<tau-bk.
```

Dropping Xi gives a sufficient interval-tail test. Universal existence of a successful threshold is OPEN.

The newly committed local replay summary reports interval detection of 205,919/205,919 target-Hall failures from the original 201,493,148-profile, 15-state pilot, and separately implemented arithmetic on 205,931 exports including 12 Hall passes. It preserves 32 strict interval/exact gaps. All 812 difficult profiles are interval-detected. The exact three-profile certificate rules out one common nonnegative weighting in the OLD cap model, not adaptive weights or the newer localized cap.

These were concurrent-session computations inspected as committed evidence here, NOT independently rerun in this recovery. Shared generation and existing early stopping are not full-frontier coverage, independent generation or external reproduction. The dedicated high-q-tail run `34876612516` and corrected minimum-cut run `34878019517` were queued at this recovery's last direct checks; their remote status is separate from the local interval replay.

## Latest localized cap: new mathematical priority

Read `project/research/general_n/2026-09-14-localized-excess-v1/README.md`, added at `449a268...`. Its hand derivation was inspected here; its listed finite checks were not independently rerun in this recovery. Do not assume future evidence files exist until fetching them.

For a residual threshold eta, define

```text
U_eta={u:rho_u<=eta}, L_eta={i:s_i<=eta},
m_eta=|L_eta|, S_eta=sum_{i in L_eta}s_i,
Q_eta=sum_{u in U_eta}q_u,
C_eta=Esel+S_eta-Q_eta.
```

C_eta must be nonnegative. For a source w OUTSIDE U_eta, put kstar=min(m_eta,q_w,C_eta). When q_w>kstar the candidate canonical consequence is

```text
p_w<=rho_w-1+floor((C_eta-kstar)/(q_w-kstar)).
```

Eta=0 recovers the existing zero-demand cap. Positive eta locates excess already forced into low-positive-demand labels, preventing the same excess being reused independently elsewhere. The source-outside-U condition and zero-demand handling are essential review targets.

Unlike the old-cap loss identity, this can strengthen P itself. The new note displays two specific old feasible PROFILE witnesses: state-1626's Q=51 against localized sum P=50, and state-2984's Q=57 against localized sum P=52. These are not whole-state exclusions. Its reported finite verification and 812-profile reconnaissance remain internal evidence, not external acceptance. Its full-pilot attempt timed out without a complete table and is explicitly not a certificate.

The next priority is to audit this localized-cap proof and its new verifier, then assess its selection-quantified reach, retaining all previous legitimate cap terms and the interval/exact-tail decomposition. Do not transfer the old fixed-weight obstruction automatically to the smaller localized capacities. Any scalar-state closure still needs every admissible profile addressed and the project's promotion gate.

## Trust boundary

Actual graph orientations satisfy Hall. An exclusion proof must show OTHER hypothetical-counterexample bridge constraints force a negative margin somewhere. Preserved scalar/incidence relaxations admit Hall passes; they do not themselves supply an all-order contradiction.

Preserve derivations, rejected lemmas, hostile examples, verifier code, exact outputs and harness corrections. Distinguish hand derivation, local finite checks, independently structured internal arithmetic, remote CI, external review and third-party reproduction. The canonical quasi-edge/selected-residual bridge remains a correlated external-review dependency. No force push, frontier promotion or graph-realizability claim was made by this synchronization.
