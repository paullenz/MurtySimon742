# n=30 threshold-tail endpoint attack

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate analytic hardening; the `n=30, Delta=16, m=226` endpoint now has a hand route after the universal bridge. The `m=225` equality branch has also been reduced sharply, but still retains exact finite dependencies. Independent mathematical review remains open.**

## Target

For `n=30, Delta=16`, put

```text
a=13,
b=16,
t=m-224.
```

The threshold-tail construction gives the necessary inequality

```text
Q_{13,16}(s) >= 16+2t.
```

Historically, an exact full-domain check over all

```text
C(25,13)=5,200,300
```

nondecreasing demand multisets `0<=s_i<=12` found

```text
max Q_{13,16}=21,
```

uniquely at `(3^13)`, and exactly seven profiles with `Q>=20`.

That exhaustive classification is no longer a logical dependency at the upper endpoint. [`N30_M226_HAND_PROFILE_REDUCTION.md`](N30_M226_HAND_PROFILE_REDUCTION.md) proves by hand that

```text
Q<=21,
Q=21 only at (3^13),
```

and that `Q>=20` holds exactly for

```text
(2^2,3^11),
(2,3^12),
(3^13),
(3^4,4^9),
(3^2,4^11),
(3,4^12),
(4^13).
```

The proof uses a monotone clipping chain and a two-variable tail calculation. It also derives by hand the exact nine residual rows below. The small standard-library audit [`verify_hand_profile_reduction.py`](verify_hand_profile_reduction.py) checks only the local clipping obligations, 105 cap-four tail pairs, cap-five preimages and the nine-row reconstruction; it does **not** perform the historical 5,200,300-profile sweep.

Hence `t<=2`, so every `Delta=16` scope with `m>=227` is excluded by the hand threshold-tail bound.

The sole upper-bound endpoint is

```text
m=226,
t=2,
Q>=20.
```

## Exact nine m=226 rows

```text
s=(2,2,3^11), rho=(1^7,2,3^8), r=33
s=(2,3^12),   rho=(1^7,3^9),   r=34
s=(3^13),     rho=(1^7,3^9),   r=34
s=(3^13),     rho=(1^7,3^8,4), r=35
s=(3^13),     rho=(1^6,2,3^9), r=35
s=(3^4,4^9),  rho=(1^6,3^2,4^8), r=44
s=(3^2,4^11), rho=(1^5,2,3,4^9), r=46
s=(3,4^12),   rho=(1^5,2,4^10), r=47
s=(4^13),     rho=(1^5,3,4^10), r=48
```

[`N30_M226_HAND_ENDPOINT_REDUCTION.md`](N30_M226_HAND_ENDPOINT_REDUCTION.md) then excludes these rows by hand: one dies immediately from demand-ledger equality and the remaining eight by a label-excess versus supplement-Hall contradiction. [`verify_hand_endpoint_table.py`](verify_hand_endpoint_table.py) checks the tiny integer endpoint table without a solver.

Thus, conditional on the universal graph-to-model / threshold-tail lemmas already used by the project, the complete `n=30, Delta=16, m=226` endpoint no longer logically depends on:

- the 5,200,300-demand maximisation;
- the residual-row enumeration;
- the final grouped LP / exact Farkas certificates.

All historical exact evidence remains preserved as independent corroboration and regression material.

## m=225: direct threshold-slack reconstruction

The equality branch remains the important computational frontier, but its row-generation stage has now been simplified substantially.

The preserved exact `Q>=18` frontier consists of exactly 100 demand profiles, listed in [`N30_M225_QGE18_PROFILES.txt`](N30_M225_QGE18_PROFILES.txt), with

```text
Q=18: 64
Q=19: 29
Q=20:  6
Q=21:  1.
```

[`N30_M225_THRESHOLD_SLACK_REDUCTION.md`](N30_M225_THRESHOLD_SLACK_REDUCTION.md) uses the exact identity

```text
Q-18 = lambda
       + sum_{h=2}^{12}(z_h-g_h)
       + z_13,
```

where `lambda>=0` is ledger slack and `z_h` are the residual-degree tail counts. Since the hand upper bound gives `Q<=21`, at most three nonnegative integer slack units must be distributed. Monotone tail reconstruction from the 100 profiles produces exactly the historical 272 row-threshold survivors.

The standard-library checker [`verify_m225_tail_slack_reduction.py`](verify_m225_tail_slack_reduction.py) reproduces the historical normalized survivor SHA-256

```text
ac02b654d672062421a67e0b07a4f1cbebbc688e83ad4723ea37af2b0542f16e
```

without an LP solver, graph enumeration, or the historical 158,314,695-state residual-row scan.

The 272 rows split as

```text
ledger slack lambda=0: 211
lambda>0:                61.
```

All 61 positive-slack rows have all thirteen demands positive. Positivity gives `s_i=d_i-R_i` pointwise, so `S=r+2t=r+2` exactly; hence `lambda=0`, a contradiction. Thus only the 211 ledger-tight rows survive analytically.

## The four zero-demand tight rows

Of the 211 tight rows, 207 have all demands positive and four contain one zero demand. [`N30_M225_ZERO_DEMAND_RCORE.md`](N30_M225_ZERO_DEMAND_RCORE.md) observes that ledger tightness actually forces

```text
d_i=R_i+s_i
```

for **every** label, including a zero-demand label. Therefore the residual-budget Hall model extends to these four rows without the earlier positivity restriction.

All four are exactly Farkas-rejected. Their preserved rays are in [`N30_M225_ZERO_DEMAND_RCORE_CERTS.json`](N30_M225_ZERO_DEMAND_RCORE_CERTS.json), and [`verify_m225_zero_demand_rcore_exact.py`](verify_m225_zero_demand_rcore_exact.py) reconstructs the integer models and verifies all four certificates without a solver or floating point.

This leaves the 207 positive ledger-tight rows as the substantive `m=225` endpoint sector.

## The 207 positive tight rows

The preserved residual-budget RX-Hall core already treats exactly these 207 rows. Its necessary-condition model uses:

- grouped source types with the correct local supplement geometry `p<=rho+2`;
- nested source/supplement transport;
- grouped `(s,R,y)` label types;
- the exact residual-column budget;
- total selected-incidence balance;
- RX1/RX2/RX3 compatibility;
- Hall capacities for one or two source neighborhoods.

It exactly rejects 200 of the 207 rows and leaves seven hard states. All seven have residual maximum three. The later exact 3-D potential programme rejects those seven with two fixed rational scalar templates.

This is a much smaller and more structured endpoint dependency than the original full grouped model, but it remains computational/certificate-based. The current analytic target is to replace the 200 residual-budget Hall rejections, or a large uniform subclass of them, with one or a small family of explicit hand inequalities. A secondary target is a hand classification of the 100 `Q>=18` demand profiles.

[`N30_M225_RECONNAISSANCE.md`](N30_M225_RECONNAISSANCE.md) also records and rejects an invalid exploratory tightening `p<=rho+1`; the correct local bound remains `p<=rho+2`.

This analytic hardening does **not** promote the project beyond candidate status. Independent specialist review remains open, and the exact finite work at `m=225, Delta=16` remains a proof-critical dependency until the positive tight sector and the 100-profile classification are replaced analytically.
