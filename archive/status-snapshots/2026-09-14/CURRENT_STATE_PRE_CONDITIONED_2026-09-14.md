# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. New checkpoint: demand-block and source-specific priced pressure. Proof `5616b33e452d62728f05a721b7fa5cb2724382ea`, verifier `56c8f230b7b0da6996a84392fa43d981fe65d964`, frozen output `479bc1faad29a4c95ebc4530238c46aabe08f0ea`, combined CI `82c544d9d8fc9ff991845adb9d7d74dacb1e715c`, all twelve retained profiles `e733028b9a60cb2d42e8db6dc7f3c88f11afaaa9`. Inspect newer commits and live CI before continuing.**

Canonical repository: `paullenz/MurtySimon742`, ID `1359206057`. The complete preceding capped-spill handoff remains preserved [at commit e0f2c0a5](https://github.com/paullenz/MurtySimon742/blob/e0f2c0a555c6e8e9902df615114d1cd73918b38e/CURRENT_STATE.md). Its predecessor, priced-tail and earlier archival handoffs retain every prior derivation, experiment, counterexample and audit gate. The repository, not a chat transcript, is the durable source of truth.

## Canonical frontier and external review — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — NOT PROMOTED
```

The fixed-order candidates n=25 and n=27 through n=35, plus the general 7/12 maximum-degree candidate, are unchanged. External mathematical review, novelty assessment and third-party reproduction remain OPEN. Synthetic profiles and generalisation scalar states are not graphs or unresolved obligations in those fixed-order packages. Preserve both reviewer navigation surfaces.

Promotion of the 2,655 recovered candidates still requires every candidate covered, both relational implementations agreeing state by state, zero unresolved cases, a successful aggregate and a separate ledger-promotion commit. Keep N34/N35 provenance separate. Candidate discovery SHA256 remains `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`.

## GitHub has made progress; do not trust old queue labels

The short-verifier kick `34883538561` is now COMPLETED/SUCCESS. Its downloaded artifact `10363664441`, `priority-proof-replay-and-queue-diagnostic`, has archive SHA256 `91eabcde27e8a1a79d8e40ecbcacf826cb33519899fc2589a0981e6755690a5c`. Both complete parsed actual/expected JSON objects were compared locally: localized and priced outputs agree exactly.

Its fully paginated snapshot was observed at **2026-09-14 19:17:44 UTC**:

```text
relational audit 34854911792:
  plan succeeded,
  audit shards succeeded: 116
  audit shards running:    11
  audit shards queued:    129
  total jobs:             257 (plan + 256 shards)
  accepted aggregate:     NONE
```

This is a timestamped snapshot, not a current completion claim. It supersedes the old first-page account of only 29 visible successes. No failed shard appeared in that snapshot. The run-level label still said queued despite active and completed shards.

The same snapshot records completed success for dedicated q-tail run `34876612516`, repaired mincut `34878019517` and original localized run `34880833888`. The current capped-spill run `34885163695` was directly rechecked and still queued. Previously verified frozen-ledger `34875592126` and threshold `34871045562` successes remain separate from relational promotion.

A fresh COMBINED capped-spill/block-pressure replay was triggered as **`34887492789`**, observed queued after creation. It regenerates the hash-pinned corpus, replays the complete prior capped-spill gate and new integer verifier, then records fully paginated before/after audit snapshots. It uses a single standard ARM runner, does not cancel or duplicate the 256-shard audit, and makes no scheduling-priority guarantee. Do not call the new proof remotely green before checking this run.

An hourly conditional GitHub check was also scheduled at the user's request to keep GH moving. It only retries individual confirmed transient-infrastructure failures once; queued/running/successful jobs, mathematical discrepancies, hash failures and computational timeouts are not blindly retried. It cannot promote the ledger and should stop after relevant scopes complete. This does not imply ongoing autonomous mathematical research between chat turns.

## Retained core notation and proof chain

```text
Q=r+2t+D0+Esel,
D0=S-r-2t>=0,
Esel=Q-S>=0,
x_i=s_i+e_i,
delta=b-a,
c_u=q_u+rho_u<=a,
rho_u>=1.
```

Structural surplus is t, q-threshold tau, label-demand threshold eta. z counts zero-demand labels; never assume z<=Esel. Selected ui has s_i<=rho_u, and a selected POSITIVE-demand label forces

```text
d_u=(p_u-rho_u+1)_+ <= e_i.
```

Retain all legitimate target caps P: residual/incoming, simple-degree, exact potential-pair, selected-excess, localized and all-source-spill. Negative caps reject a branch and must not be clipped to zero. Define source pressure ceiling D_u=(P_u-rho_u+1)_+; actual d_u<=D_u<=delta.

The capped-spill theorem, its 57>48 hand certificate, all 400,758 old inequality checks, 3,000 old independent prefix-DP comparisons and 812-case replay remain preserved in `2026-09-14-capped-spill-v1`. Those full old tests were NOT rerun locally during the new block-pressure session; the new combined CI explicitly reruns them.

## New hand inequality: exclude low-positive-demand excess from a high-label charge

Read [`project/research/general_n/2026-09-14-block-pressure-v1/README.md`](project/research/general_n/2026-09-14-block-pressure-v1/README.md).

For eta>=0 set

```text
L_eta={i:s_i<=eta}, m_eta=|L_eta|,
v_u(eta)=(q_u-m_eta)_+,
M_eta=sum_u(q_u-#{i:eta<s_i<=rho_u})_+,
S_eta=sum_{i:s_i<=eta}s_i,
B_eta=min(Esel,Esel+S_eta-M_eta).
```

Each source selects at least v_u(eta) labels above eta. All-source spill forces at least M_eta-S_eta excess onto low labels, so high-label excess is at most B_eta. B_eta<0 is infeasibility. With smax_eta=max high-label demand (zero for no high labels), the clean necessary inequality is

```text
sum_u v_u(eta)(p_u-rho_u+1)_+
 <= B_eta[smax_eta+min(B_eta,delta)].
```

This generalizes the preceding zero-label subtraction to LOW POSITIVE demands and retains the two-defect budget via Esel=Q-r-2t-D0.

For arbitrary alpha_u>=0 there is a sharper source-cap bound:

```text
sum_u alpha_u v_u(eta)d_u
 <= sum_{i:s_i>eta} sum_{u selected at i} alpha_u min(e_i,D_u).
```

For each candidate e_i, upper-bound the label contribution by the largest s_i+e_i values alpha_u min(e_i,D_u) among q_u>0,rho_u>=s_i. Maximize their sum over the previously justified integer total-excess, per-label and complete equal-demand-prefix constraints. This gives U(eta,alpha;P), a SAFE UPPER bound, exact only for that necessary projection. Top-source selections for different labels need not be jointly realizable; the relaxation direction is upper, not lower.

## Priced-tail coupling and the 209>190 certificate

For interval incoming J_w(tau)=#{u!=w:tau<=q_u<=c_w+1}, set

```text
A_w=min(P_w,J_w),
f_w=min(A_w,rho_w-1),
g_w=A_w-f_w,
w_w=alpha_w(q_w-m_eta)_+.
```

Every actual graph orientation must satisfy, for every theta>=0,

```text
theta(Q_tau-sum f_w)-sum_w(theta-w_w)_+g_w <= U(eta,alpha;P).
```

For alpha=1 the closed-form B_eta bound is another valid right side. All newly frozen certificates use the one-sided interval bound, not unproved exact reverse compatibility or tail-minimum equality.

Synthetic row 664 gives a short unweighted hand contradiction:

```text
a=24,b=30,t=1,D0=0,Esel=33,
eta=1,M_eta=15,S_eta=1,B_eta=19,
delta=6,smax_eta=4,
upper=19(4+6)=190.

tau=3,theta=8,Q_tau=100,sum A=101,sum f=51,
penalty=183,
required cost=8(100-51)-183=209>190.
```

Nominal interval capacity exceeds demand, but financing it is impossible. No optimizer or integer-DP optimum is needed for this particular certificate.

## Completed new verification and synthetic result

The new executed standard-library verifier imports no production C++ scanner. It reuses the preceding Python module only for old cap/baseline reconstruction. Its committed blob matches the locally executed file: `31973251dd7e3250f3ded9a3e3af903a35824020`.

```text
actual incidence configurations:              9,293
new inequality checks:                       33,356
independent labelled-subset/excess comparisons: 2,000
  nonempty / empty projections:            579 / 1,421
receiver box instances:                       1,000
receiver incoming vectors:                   14,806
standing hostile examples:                       3
```

The SAME 713-row corpus is used, SHA256 `157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572`. It first reproduces the preceding 694 exclusions and exact 19 remaining row IDs. All eta, tau and price breakpoints are tested for alpha=1 and for alpha=1 at q<=2 / alpha=3 at q>2. The latter is an inequality coefficient choice, NOT an extra graph hypothesis.

```text
additional rejected profiles: 7
combined rejected:          701 / 713
not rejected:                12 / 713
new rows: 39,76,119,406,664,682,688
```

All seven certificates, including capacity/demand, prices, penalties, upper envelopes and strict gaps, are in `BLOCK_PRESSURE_VERIFICATION.json`. All TWELVE unrejected arrays are committed in `REMAINDER_12.json`:

```text
108,160,240,258,295,338,342,347,365,471,570,586.
```

This is NOT a seven-state reduction of the 3,607 frontier. The corpus is a sampled scalar/incidence/pair-flow relaxation; passing gives no graph-realizability evidence. No new 812-profile or 205,931-export replay was performed locally in this block session. The preceding larger observations remain preserved with their own provenance.

## Failed extensions, red-team boundaries and next priority

Source ceilings alone reject only row 664; demand blocks give six new rejections; the tested source weighting adds row 688. A bounded multiblock-weight search gave no additional rejection. An exploratory row-incidence Lagrangian search tightened some bounds but gave no additional certified exclusion of the tested twelve. It used floating optimization only for discovery and does not certify infeasibility or optimality. All exploratory code/results are retained in the portable bundle and their scope is recorded in the proof note.

The standing hostile examples still have negative Hall minima and no deficient high-q tails. Their explicit bridge failures are residual/edge-ledger inconsistency, selected-demand infeasibility, and S<r+2t respectively. No z restriction was silently added.

Row 295 reaches equality 126=126 in a source-cap charge bound. Audit whether equality forces incompatible actual selected incidences; this is a sharper next target than fitting more weights. More broadly attack joint residual/selected realizability of the twelve. Preserve the exact q-layer/mincut, crossing-wall and maximum-cut/stability fallbacks. Check fixed-q monotonicity before transferring witness theorems to new capacity models.

Hand derivation, same-assistant independent implementation, local finite verification, remote CI, external mathematical review and third-party reproduction remain different statuses. Actual graph orientations satisfy Hall; a contradiction must be forced by OTHER canonical constraints. No timeout, queue label, missing output, failed search or floating status proves an exclusion. The canonical selected/residual bridge remains the principal correlated external-review dependency.
