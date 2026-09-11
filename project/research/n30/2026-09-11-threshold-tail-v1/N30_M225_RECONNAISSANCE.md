# n=30, Delta=16, m=225: next analytic frontier

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: reconnaissance only. No theorem-status promotion.**

This note records the next target after the hand reduction of the `m=226` endpoint. It also records one rejected exploratory tightening so that it is not accidentally reused.

## 1. Current preserved endpoint

For

```text
n=30, Delta=16, a=13, b=16, m=225, t=1,
```

the current candidate proof reduces the exact row-threshold frontier to 272 rows and rejects all 272 with the historical corrected grouped LP plus exact integer Farkas certificates. The relevant preserved workflow runs are

```text
row-threshold: 34287440190
final exact:   34287739057.
```

Those exact certificates remain the current proof route for this branch.

## 2. Demand-only reconstruction

A fresh exact reconstruction of the threshold-tail functional gives

```text
Q(s) >= 16+2t = 18.
```

Across the complete nondecreasing thirteen-label demand domain, the `Q>=18` frontier contains exactly 100 profiles, distributed as

```text
Q=18: 64 profiles
Q=19: 29 profiles
Q=20:  6 profiles
Q=21:  1 profile
```

with no profile above 21. This agrees with the already-established `Q<=21` upper bound from the new `m=226` hand profile reduction.

The 272 historical row-threshold survivors use exactly those 100 demand profiles.

This reconstruction is theorem-discovery / audit evidence at present; unlike the `Q>=20` classification in `N30_M226_HAND_PROFILE_REDUCTION.md`, the complete `Q>=18` list has not yet been replaced by a hand classification.

## 3. A free hand reduction: ledger slack

Write

```text
S=sum_i s_i,
r=sum_u rho_u,
lambda=S-r-2.
```

The 272 historical rows split as

```text
lambda=0: 211 rows
lambda=1:  52 rows
lambda=2:   8 rows
lambda=3:   1 row.
```

Equivalently by `(Q,lambda)`:

```text
(Q,lambda)   rows
(18,0)         64
(19,0)         96
(19,1)         29
(20,0)         42
(20,1)         18
(20,2)          6
(21,0)          9
(21,1)          5
(21,2)          2
(21,3)          1.
```

All 61 rows with `lambda>0` have all thirteen demands positive.

But by definition

```text
s_i=max(0,d_i-R_i).
```

If every `s_i>0`, then `s_i=d_i-R_i` for every label. Therefore

```text
S = sum_i d_i - sum_i R_i
  = 2e(F)-r
  = 2(r+t)-r
  = r+2t
  = r+2.
```

Hence every all-positive graph-realizable row has

```text
lambda=0.                                         (1)
```

So the 61 historical rows with `lambda>0` are analytically impossible before any grouped LP/Farkas model is built.

This leaves 211 ledger-tight rows as the genuine `m=225` target.

A useful companion observation is that if a ledger-tight row contains a zero demand, then equality of

```text
sum_i max(0,d_i-R_i) >= sum_i(d_i-R_i)=r+2
```

forces every zero-demand negative part also to vanish. Thus on every one of the 211 tight rows one has

```text
d_i=R_i+s_i
```

for every label, including a zero-demand label when present. This is the exact identity needed by the selected-incidence / excess arguments used at `m=226`.

## 4. Rejected exploratory tightening

During the first attempt to port the `m=226` hand-Hall argument to `t=1`, the local supplement-degree bound was mistakenly tightened from

```text
p_u <= rho_u+2
```

to

```text
p_u <= rho_u+1.
```

**That tightening is not justified and must not be used.**

The `+2` comes from the fixed `(a,b)=(13,16)` local degree geometry, not from the surplus parameter `t`. The exploratory exclusions obtained under `p<=rho+1` were discarded before any repository proof claim was made.

This failed route is recorded deliberately so it cannot silently re-enter the argument later.

## 5. Correct-domain tests of the m=226 mechanism

With the correct bound

```text
p_u<=rho_u+2,
```

the present one-dimensional label-excess / supplement-Hall template does **not** close the 211 tight rows. A theorem-discovery LP over that template gives a positive separating margin for only 27 of the 211 rows.

The stronger `m=226` two-transport relaxation was also tested on the 211 tight rows with the correct `p<=rho+2` domain. It is infeasible for 39 rows but feasible for 172. Therefore that relaxation by itself cannot replace the historical `m=225` grouped-model certificates.

These two figures are reconnaissance diagnostics, not proof claims and not new dependencies of the candidate theorem.

## 6. Next analytic target

The remaining high-value problem is therefore sharply stated:

```text
replace the 211 tight m=225 rows, or a large uniform subclass of them,
by a stronger hand inequality that keeps p<=rho+2 exact.
```

The most promising sources of extra strength are:

1. demand-level selected-incidence Hall constraints, not just the scalar excess bound;
2. same-group / no-self supplement transport, which the simple Hall tails relax;
3. exploiting the very small threshold-tail slack `Q-18<=3` to classify residual tails symbolically;
4. structural analysis of the 211 historical exact Farkas rays to identify a small family of recurring dual potentials.

Until one of those succeeds, the historical exact `m=225` Farkas route remains the current candidate-proof dependency.
