# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. Synchronized through localized proof `449a268f93600d78660e02b09d65e5304a2ca0bf`, verifier `4e6af044adad9af0e3146772ccdcda62f39851d0`, frozen evidence `cbe1076c87b1cb1eccff409a14dcac7839fd9de6`, experiment log `d887f7d31f81054f501b5d6d4de08f6ce89b17fa`, CI workflow `e7618ca2caa6438beea5b613638d9fa45297705b` and root synchronization `391ca91416ad45b2c6e665f1371f992c33effabd`. Inspect newer commits before resuming.**

Canonical repository: `paullenz/MurtySimon742`, ID `1359206057`. See `CANONICAL_REPOSITORY.md`. The repository, not a chat transcript, is the durable source of truth. No whole-state exclusion or unrestricted proof is promoted by this handoff.

## Recovery and concurrent commits

The requested failed-chat checkpoint was `0e6546e8947b43896d0c8f5eebde8335b8d95f11`; main initially stood five commits later at `81560e92698d07992df4a53976ee1ea8efaaeb4d`. Later concurrent work was fetched and preserved:

- `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb`: selected-excess tail-loss identity;
- `de82393062163dc2ffab10b90ba68ce4a0f7a741`: interval-tail receiver-loss budget;
- `d1e20da87e8d8dcda3633e550b8b5556b6e7c9ee`: interval verifier, exact fixed-weight certificate and frozen replay summary;
- `d6c818440c736367dae68bd425ce7e6df7fa0bed`: replay instrumentation and hostile searches;
- the localized-cap sequence listed above: a new canonical necessary condition, independent implementation, complete local checks, incomplete wider experiment and remote replay workflow.

Never force a stale update over concurrent work. Earlier detailed records remain in `CURRENT_STATE_EARLIER_2026-09-14.md`, `RECOVERY_STATE_DETAILS_2026-09-14.md`, `INTERVAL_RECONCILIATION_DETAILS_2026-09-14.md`, `README_EARLIER_2026-09-14.md` and Git history. Their old priorities and queue observations are historical.

## Canonical promoted frontier — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered candidate exclusions: 2,655 (NOT PROMOTED)
```

The final two-implementation audit `34854911792` remains incomplete. The plan and first visible 29 audit shards passed, but a later paginated read returned 257 jobs total and the final shard `audit (255)` still queued. There is no accepted aggregate/full-coverage pass. Promotion requires all 2,655 candidates covered, exact state-by-state agreement between `scan_post_pair_relational.cpp` and `scan_post_pair_relational_types.cpp`, zero unresolved cases, a successful aggregate, then a separate ledger-promotion commit. Preserve N34/N35 provenance and the closure-ledger check. Do not subtract 2,655 from 3,607 prematurely.

The fixed-order candidate packages n=25 and n=27 through n=35 and the general 7/12 maximum-degree candidate theorem are unchanged. External mathematical review and novelty assessment remain OPEN. They are distinct from the scalar generalisation frontier. Preserve reviewer navigation at both root README and `releases/REVIEW_READY_INDEX.md`.

## Exact q-stratified route

In `project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`, read `Q_STRATIFIED_MINCUT_EXACTNESS.md`, `Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md` and `Q_LAYER_THRESHOLD_NORMAL_FORM.md`.

Under their stated hypotheses,

```text
min_A[H(A)-D(A)]=min_A[U_q(A)-D(A)].
```

Pointwise equality is false in general, and C_q(M+) can be positive. Proving C_q(M+)=0 is no longer a prerequisite. The exact type-complete threshold route does not depend on high-q-tail sufficiency. Before applying an old canonical-witness theorem to NEW caps, check its fixed-q monotonicity and other hypotheses afresh; direct Hall/tail evaluation does not require that transfer.

The correction at `93c9e8995c57e69c238396f20641a0dc84bb4754` preserves failures of overbroad tail conjectures. z counts zero-demand LABELS and is not constrained by z<=Esel. Keep

```text
D0=S-r-2t>=0,
Esel=Q-S>=0,
Q=r+2t+D0+Esel.
```

Structural surplus is t; q-thresholds are tau. The localized cap uses residual/demand threshold eta.

## Selected-loss result — exact old-cap coordinates

Let k=b-a-1>=0, E=Esel, N(h)=#{u:q_u>=h}, and

```text
h_j=min(E,z)+floor(max(E-z,0)/j)+1, j=1,...,k+1,
ell_E(q)=sum_j 1_{q>=h_j},
eta_u=max(0,c_u+k-d_K(u)-ell_E(q_u)),
L_E=sum_j N(h_j), L_K=sum_u eta_u.
```

Here the indexed eta_u is the older potential-pair loss notation, not the residual threshold eta of the localized theorem. `SELECTED_EXCESS_TAIL_LOSS_BUDGET.md` proves

```text
P_u=rho_u+k-ell_E(q_u)-eta_u,
2t+D0+E+L_E+L_K<=bk.
```

For any source set A, with unused receiver capacity V(A) and outside demand q_out(A),

```text
H(A)-D(A)=bk-(2t+D0+E)-L_E-L_K+q_out(A)-V(A).
```

This reformulates the existing cap/Hall screens; it is not computationally stronger than those screens. Negative caps reject the branch and must not be clipped to zero.

The committed standard-library verification reports 179,375 pointwise identities, 6,381 exhaustive profiles, 171,504 exhaustive source sets and 10,000 random profiles, with 93,010 nonnegative-cap source-set checks. `EXCESS_TAIL_LOSS_AUDIT.md` preserves its regression-fixture correction. This evidence came from the concurrent selected-loss work; it is distinct from the newly executed localized verifier.

## Interval synthesis — committed evidence inspected

Read `project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md`, `SELECTED_LOSS_SYNTHESIS.md`, `REPLAY_SUMMARY.json` and `FIXED_WEIGHT_OBSTRUCTION.json`.

For T_tau={u:q_u>=tau}, exact vacancy is V(T_tau)=Omega_tau+Xi_tau: interval-unfillable capacity plus reverse-compatibility correction. Thus

```text
Delta_tau=2t+D0+E+L_E+L_K+Omega_tau+Xi_tau-Q_<tau-bk.
```

Dropping Xi gives a sufficient interval-tail test, not a universal threshold-existence theorem.

The committed local replay detects 205,919/205,919 old target-Hall failures in the original 201,493,148-profile, 15-state pilot. A separately implemented arithmetic audit covers 205,931 exports including 12 Hall passes. There are 32 profiles with a strict interval/exact gap at some threshold. All 812 difficult profiles are interval-detected. The exact three-profile certificate rules out a common nonnegative weighting in the OLD cap model, not adaptive weights or the newer localized cap.

These full-replay computations were inspected as concurrent committed evidence, not independently regenerated by the localized run. Shared generation and early stopping are not full-frontier coverage or external reproduction. The original q-stratified artifact from run `34859094097` was downloaded and inspected: all 205,919 Hall failures have C_q=0. This remains a finite observation.

## Localized selected excess — completed new checkpoint

Read `project/research/general_n/2026-09-14-localized-excess-v1/README.md`, `verify_localized_excess.py`, `LOCALIZED_EXCESS_VERIFICATION.json` and `EXPERIMENT_LOG.md`. These files are now committed and the local verifier completed successfully; they are no longer merely promised evidence files.

For a residual threshold eta>=0 define

```text
U_eta={u:rho_u<=eta}, L_eta={i:s_i<=eta},
m_eta=|L_eta|, S_eta=sum_{i in L_eta}s_i,
Q_eta=sum_{u in U_eta}q_u,
C_eta=Esel+S_eta-Q_eta.
```

Every U_eta selection lies in L_eta, so C_eta>=0 is necessary. For a source w OUTSIDE U_eta, if k of its distinct selected labels lie in L_eta, canonical endpoint forcing gives

```text
C_eta >= k+(q_w-k)(p_w-rho_w+1) when p_w>=rho_w.
```

Put kstar=min(m_eta,q_w,C_eta). When q_w>kstar,

```text
p_w<=rho_w-1+floor((C_eta-kstar)/(q_w-kstar)).
```

Eta=0 exactly recovers the zero-demand cap. Positive eta locates excess forced into positive-demand labels. The source-outside-U condition prevents double counting, and labels outside L_eta have positive demand. These are essential review targets.

In particular, q_w>C_eta implies p_w<=rho_w-1. If Z collects such certified sources and delta=b-a,

```text
2t+D0+Esel+delta*|Z|<=b(delta-1).
```

Retain the minimum with every other legitimate cap, especially exact potential-pair degrees. This strengthens P itself and can be substituted into the interval and exact-tail identities.

Two specific old feasible PROFILE witnesses now fail: state-1626's Q=51 against localized sum P=50, and state-2984's Q=57 against localized sum P=52. Independent selected-incidence and old target-flow checks pass on both. They are NOT whole-state exclusions. In the first example the simple exposed-source inequality is only an equality; the potential-pair cap is essential for the strict full-source contradiction.

Completed local verification:

```text
exhaustive selected-incidence configurations: 133,586
integer floor-optimization cases:                6,880
seeded incidence/source-cap/ledger mutations:     3,000
standing hostile examples rechecked:                 3
frozen difficult profiles replayed:                812
  cap vectors tightened:                          748
  uniform detections, old -> new:            476 -> 773
  deficient already at tau=1:                      630
  detected by some exact tail:                     812
```

The 3,000 mutations preserve the positive-surplus scalar ledger but are not realized F-graphs, residual matrices or complete quasi-edge systems. The implementation is separately structured Python with no imports from the C++ verifiers. It is same-assistant internal evidence, not external reproduction.

The attempted instrumented wider C++ pilot exited at its 240-second limit with code 124. Its buffered TSV was empty; one stderr progress line is retained. NO complete wider replay or new whole-state certificate follows. The two profile exclusions and all completed finite tests are independent of that interrupted run.

The preserved hostile examples remain failures of weaker tail conjectures. Esel=5,z=2 is rejected by selected-demand feasibility; Esel=19,z=4,s=0 is rejected by S>=r+2t. No counterexample was removed by silently restricting z.

## Live CI observations and separate gates

| Run | Last direct observation in this synchronization |
|---|---|
| `34854911792` relational candidates | Incomplete; final shard 255 queued; no accepted aggregate. |
| `34875592126` frozen ledger | Rechecked after queue: completed success, including combined survivor coverage. |
| `34871045562` q-layer threshold | Completed success, including independent verifier and frozen totals. |
| `34868771056` old mincut | Verifier succeeded; raw JSON text comparison failed only on list formatting. Workflow bug, not mathematical failure. |
| `34878019517` corrected mincut | Still queued. Parsed-JSON fix preserves every frozen value. |
| `34859094097` q-stratified pilot | Completed artifact retrieved and its full finite summary inspected. |
| New localized-cap CI | Workflow `.github/workflows/verify-localized-excess.yml` committed at e7618ca; do not claim remote PASS without fetching its run. |

The dedicated older high-q-tail CI `34876612516` was queued at the earlier recovery check; recheck it as needed. Remote queues do not negate separately completed local arithmetic, but local arithmetic is not a remote green run.

## Next mathematical priority and trust boundary

The strongest current hand target is localized selected-excess forcing combined with the two-defect budget and adaptive threshold receiver losses. Red-team the source-disjoint count and integer cap, then explore selection-quantified reach with bounded, checkpointed state scans and independent replay. The 39 remaining uniform-weight misses make adaptive tails or the exact q-layer formulation preferable to declaring a universal quadratic potential. The crossing-wall and maximum-cut/stability routes remain retained fallbacks.

Actual graph orientations satisfy Hall. An exclusion proof must show OTHER hypothetical-counterexample bridge constraints force a negative margin. Scalar/incidence relaxations alone admit Hall passes and cannot supply that implication. The localized inequality adds a genuine joint constraint but is not yet an all-order contradiction.

Preserve derivations, rejected lemmas, hostile examples, code, exact outputs and harness corrections. Distinguish hand proof, finite verification, separately structured internal arithmetic, remote CI, external review and third-party reproduction. The canonical quasi-edge/selected-residual bridge remains a correlated external-review dependency. No force push, whole-state promotion or graph-realizability claim is made here.
