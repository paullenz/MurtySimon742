# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. Synchronized through `57d7c1e7f7f786bcb77f15c7957765970901715d`, the priced-tail derivation, fixed-tau localized reconstruction and exact 80>77 certificate. Inspect newer commits and recheck CI before resuming.**

Canonical repository: `paullenz/MurtySimon742`, ID `1359206057`. The full immediately preceding handoff is preserved verbatim in [`CURRENT_STATE_PRE_PRICED_2026-09-14.md`](CURRENT_STATE_PRE_PRICED_2026-09-14.md). It retains the detailed interval, selected-loss, localized-cap, exact q-layer and recovery chronology. Earlier archival files and Git history remain intact. No force push, whole-state promotion or unrestricted proof is asserted.

## Promoted frontier and audit gate — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

Final audit `34854911792` remains incomplete on direct recheck: final indexed shard `audit (255)`, job `104025296865`, is queued, with 257 jobs total and no accepted aggregate. The plan and first visible 29 shards had passed. Promotion requires full coverage of all 2,655 inputs, state-by-state agreement of `scan_post_pair_relational.cpp` and `scan_post_pair_relational_types.cpp`, zero unresolved states, successful aggregate, then a SEPARATE ledger promotion. Preserve the N34/N35 split and `tools/check_n34_whole_state_ledger.py`.

Frozen candidate SHA256: `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`. Never subtract 2,655 from 3,607 before promotion. The fixed-order candidate packages n=25 and n=27 through n=35, and the general 7/12 candidate theorem, are unchanged and externally unreviewed. These scalar states are not graphs or unfinished obligations in those fixed-order packages.

## Live CI: later observations supersede old queues

- `34875592126`, frozen ledger: directly rechecked, completed SUCCESS, including combined survivor coverage.
- `34871045562`, q-layer threshold: completed SUCCESS, including frozen totals.
- `34868771056`, original mincut: mathematical verifier succeeded; raw JSON comparison failed only on formatting. Historical failure retained and classified as a workflow comparison bug.
- `34878019517`, corrected mincut: directly rechecked, now completed SUCCESS, including frozen JSON value equality and evidence upload. Repair commit `81560e9` did not change mathematical totals.
- `34859094097`, q-stratified pilot: completed artifact downloaded and replayed; finite summary records C_q=0 on all 205,919 Hall failures.
- New priced-tail workflow: `.github/workflows/verify-priced-q-tail.yml`, committed at `57d7c1e7`; local verifier PASS is not itself remote CI completion. Recheck its run before calling it green.
- The dedicated q-tail and localized-cap workflows have separate gates. Their earlier statuses are in the archived handoff; do not infer their completion from a different green run.

The corrected mincut and frozen-ledger successes do not complete the 2,655-state relational audit.

## Notation and retained exact routes

```text
r=sum rho=sum R, S=sum s, Q=sum q,
D0=S-r-2t=sum_{s_i=0}(R_i-d_i)>=0,
Esel=Q-S>=0,
Q=r+2t+D0+Esel,
delta=b-a,
G=b(delta-1)-(2t+D0+Esel)>=0.
```

`t` is structural surplus, `tau` a q threshold, `eta` a residual/demand-block threshold. z counts ZERO-DEMAND LABELS, and is not constrained by z<=Esel. Positive-surplus residual activity gives rho>=1; c=q+rho<=a.

The exact q-stratified minimum theorem and q-layer threshold normal form in `2026-09-14-type-compressed-orientation-hall-v1/` remain fallbacks. Equality of minima does not mean pointwise equality or C_q(M+)=0. Before transferring an old canonical-witness theorem to new caps, check its monotonicity and other hypotheses; direct tail evaluation does not require that transfer.

For a tail, interval incoming J_w(tau)=#{u!=w:tau<=q_u<=c_w+1} drops only reverse compatibility. With a legitimate cap P,

```text
Lambda=sum_w(rho_w+delta-1-P_w),
Omega_tau=sum_w(P_w-J_w(tau))_+,
Q_<tau=sum_{q_u<tau}q_u,
Delta_tau=-F_tau >= Lambda+Omega_tau-Q_<tau-G.
```

The explicit nonnegative reverse correction Xi_tau makes this equality. Universal interval exactness is false: 32 of the old exported failure profiles have strict gaps at some threshold. All useful counterexamples are retained.

## Localized excess: the extra canonical constraint

The concurrent localized package `2026-09-14-localized-excess-v1/` is preserved and integrated. It defines

```text
U_eta={u:rho_u<=eta}, L_eta={i:s_i<=eta},
C_eta=Esel+sum_{i in L_eta}s_i-sum_{u in U_eta}q_u>=0.
```

For rho_w>eta put kstar=min(|L_eta|,q_w,C_eta). When q_w>kstar the canonical endpoint-excess argument gives

```text
p_w<=rho_w-1+floor((C_eta-kstar)/(q_w-kstar)).
```

Take the minimum with ALL legitimate old caps. Eta=0 recovers the zero-demand cap; positive eta prevents reusing excess forced into low-positive-demand labels. The source-outside-U condition is essential. Negative caps are infeasibility, never silently clipped.

The concurrent complete local checks and incomplete wider generation experiment remain distinct. Our new reconstruction below reads the OLD exported stream; it does not claim to have completed that interrupted regenerated search.

## New main proof target: priced tails, not necessarily deficient Hall tails

Read [`PRICED_TAIL_BUDGET.md`](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md) first, then its verifier and frozen output.

For x_i=s_i+e_i, every selected POSITIVE-demand label i at u satisfies p_u<=rho_u-1+e_i. Define v_u=(q_u-z)_+. Distinct selected labels imply the shared charge bound

```text
sum_u v_u(p_u-rho_u+1)_+
 <= sum_i e_i(s_i+e_i)
 <= Esel(Esel+smax),   smax=max s_i.
```

For tail T_tau and a legitimate cap P, set

```text
A_w=min(P_w,J_w(tau)),
f_w=min(A_w,rho_w-1),
g_w=A_w-f_w.
```

Every graph-derived orientation necessarily obeys, for ALL tau>=1 and prices theta>=0,

```text
theta*(Q_tau-sum_w f_w)
 -sum_w(theta-v_w)_+ g_w <= Esel(Esel+smax).
```

Its right side can equivalently use Esel=Q-r-2t-D0. The proof sums a pointwise free/paid receiver inequality and the canonical selected-incidence charge bound. It is hand-derived under explicit bridge hypotheses; external mathematical review and novelty assessment remain open.

For theta>=max v the left side is

```text
theta*(Q_tau-sum A_w)+sum_w v_w g_w.
```

Thus a deficient interval tail is one way to contradict the budget, but a TIGHT tail can also force too much excess cost. This broadens the research goal and avoids assuming a deficient Hall tail always exists.

## New frozen evidence: a fixed tau=3 Hall-or-price certificate

Independent localized-cap reconstruction on the 812 difficult profiles:

```text
fixed tau=3 detects:          812 / 812
minimum / maximum deficit:     1 / 15
cap vectors tightened:            748
uniform weights detect:           773
first deficient tau:        1:630, 2:117, 3:65
```

The OLD-cap fixed-weight obstruction remains valid for OLD caps. It must NOT be transferred to the strengthened localized model: the common integer weighting (0,0,1,0,0,0,0,0) now works on all 812. This is finite evidence, not a universal tau=3 theorem.

On all 205,931 old exported rows, localized fixed tau=3 detects 205,930, including all 205,919 old Hall failures and 11 of 12 old Hall passes. Cap vectors tighten on 43,113. The remaining state-4073 profile has r=56,S=58,Q=65,t=1,D0=0,Esel=7,smax=4. At tau=3 its tail demand and capacity both equal 56. Filling the tail needs excess cost at least 80, while Esel(Esel+smax)=77. Theta=7 gives an exact strict certificate 80>77. All arrays and arithmetic are frozen in `PRICED_TAIL_VERIFICATION.json`.

This last profile was already rejected by the old cost screen. The new result is a short scalar hand certificate explaining it. A Hall-or-priced-tail explanation therefore covers all OLD exports, not every possible profile or whole scalar state. The old scanner stopped at two surviving witnesses; eliminating them requires resuming omitted continuations before any whole-state claim.

Shared-generator independent arithmetic is not external reproduction. Source TSV SHA256: `4b183b899127f4f9e05faed0cb23a11c6962c854f077d0e3ad209d09b386fb67`. Original artifact IDs, hashes and reproduction commands are retained in the interval package. The evidence ZIP includes original inputs, compressed raw rows and detailed outputs; those large rows are not claimed uploaded to Git.

## Verification, hostile boundaries and next work

`verify_priced_tail.py` independently checks 1,329 receiver profiles / 5,109 feasible demand values, 9,293 selected-incidence configurations including zero demands, localized-cap reconstruction and the exact 80>77 fixture. `verify_localized_fixed_tail.py` checks the 812 fixed-threshold certificate without an optimizer. `replay_localized_export.py` reconstructs the full old stream; `recheck_synthetic_priced.py` preserves its negative boundary.

The earlier 713 sampled scalar/incidence/pair-flow relaxations now have 652 localized/priced rejections but **61 not rejected**. Passing is not graph realization, and these 61 prohibit claiming universal closure from the tested relaxation. No additional priced-only rejection occurred in that synthetic sample. Preserve the explicit unrejected example.

The three older hostile q-tail examples, old-cap exact fixed-weight obstruction, abstract interval misses, frozen strict gaps, and all generator/workflow corrections remain preserved. The a=4,b=7 cap-only case fails selected demand feasibility; the all-zero-demand case fails the canonical ledger. No counterexample is excluded by an unstated z restriction.

Next: seek a structurally forced violating pair (tau,theta) from FULL canonical selected/residual and endpoint constraints, or sharpen the excess envelope and localized block budgets on the 61 synthetic survivors. Keep exact q-layer and crossing-wall/saturation routes as fallbacks, and the independent maximum-cut/stability route. Complete source-state continuations with coverage certificates separately from this hand attack. External review of the canonical graph bridge remains the central correlated dependency. No timeout, missing output or unreviewed discovery is proof.
