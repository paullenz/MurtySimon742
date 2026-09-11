# Threshold-slack reconstruction of the n=30, Delta=16, m=225 row frontier

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact analytic/combinatorial hardening. Independent mathematical review remains open.**

This note replaces the historical large residual-row scan and subsequent row-threshold screen by a tiny slack reconstruction, conditional on the preserved exact `Q>=18` demand frontier. It does **not** yet replace the exact 100-profile demand classification or the final exact exclusions of the remaining ledger-tight rows.

## 1. Setup

For

```text
n=30,
Delta=16,
a=13,
b=16,
m=225,
t=1,
```

let `s=(s_1,...,s_13)` be the demand multiset and put

```text
S=sum_i s_i.
```

For `h>=2`, define

```text
W_h=sum_{i:s_i>=h}s_i,
```

and let `g_h(W_h)` be the least threshold-compatible residual-tail size from the threshold-capacity lemma. Since `s_i<=12`, only `h=2,...,12` occur in the demand threshold score.

Write

```text
Q(s)=S-sum_{h=2}^{12} g_h(W_h).                  (1)
```

The bridge gives

```text
Q(s)>=16+2t=18.                                   (2)
```

The hand `m=226` profile reduction proves globally, for the same `(a,b)=(13,16)` parameter pair,

```text
Q(s)<=21.                                         (3)
```

Hence every `m=225` candidate has only

```text
0<=Q-18<=3                                        (4)
```

units of total threshold/ledger slack.

The preserved exact `Q>=18` frontier contains exactly 100 nondecreasing demand profiles:

```text
Q=18: 64 profiles
Q=19: 29 profiles
Q=20:  6 profiles
Q=21:  1 profile.
```

They are listed in [`N30_M225_QGE18_PROFILES.txt`](N30_M225_QGE18_PROFILES.txt).

## 2. Residual-tail identity

For a residual row `rho=(rho_1,...,rho_16)`, residual activity gives

```text
rho_u>=1
```

for all sixteen sources. Define

```text
z_h=#{u:rho_u>=h},  h=2,...,13.
```

Because every residual degree is at most `a=13`, the tail-sum identity is

```text
r=sum_u rho_u
 =16+sum_{h=2}^{13} z_h.                          (5)
```

Threshold capacity says

```text
z_h>=g_h(W_h), h=2,...,12,                        (6)
```

while `z_13>=0` has no demand-side threshold term.

The demand ledger at `t=1` is

```text
S>=r+2.                                           (7)
```

Define the nonnegative integer ledger slack

```text
lambda=S-r-2.                                     (8)
```

Substituting (5) into (8) and then into (1) gives the exact identity

```text
Q-18
 =lambda
  +sum_{h=2}^{12}(z_h-g_h(W_h))
  +z_13.                                          (9)
```

Every term on the right is a nonnegative integer.

Thus, once `s` is fixed, **every possible residual row is obtained by distributing exactly `Q-18` units** among:

```text
lambda,
z_2-g_2,
...,
z_12-g_12,
z_13,
```

subject only to the residual-tail monotonicity

```text
16>=z_2>=z_3>=...>=z_13>=0.                       (10)
```

Because of (4), at most three units are ever distributed.

Conversely, every such monotone tail sequence determines a unique sorted residual row: the number of residual degrees equal to `1` is `16-z_2`; for `2<=h<=12` the number equal to `h` is `z_h-z_{h+1}`; and the number equal to `13` is `z_13`.

So (9)--(10) give a complete finite reconstruction, not merely a necessary subfilter.

## 3. Exact reconstruction of the historical 272 rows

Applying (9)--(10) to the 100 preserved demand profiles produces exactly

```text
272
```

pairwise distinct `(s,rho)` rows.

Their `(Q,lambda)` distribution is

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

This is exactly the historical row-threshold frontier from workflow `34287440190`.

The historical normalized survivor list has SHA-256

```text
ac02b654d672062421a67e0b07a4f1cbebbc688e83ad4723ea37af2b0542f16e.
```

The solver-free checker [`verify_m225_tail_slack_reduction.py`](verify_m225_tail_slack_reduction.py) reconstructs the 272 rows from the 100 profiles and obtains the same SHA-256 exactly. No LP solver, floating point, residual-row scan, or graph enumeration is used.

Accordingly, conditional on the exact 100-profile `Q>=18` frontier, the historical route

```text
158,314,695 raw residual states
 -> 150,896 post-Hall/refinement rows
 -> 272 row-threshold survivors
```

is no longer a logical necessity for identifying the endpoint row frontier. Equations (9)--(10) recover the same 272 rows directly.

## 4. Sixty-one rows die immediately from ledger equality

Among the 272 reconstructed rows,

```text
211 have lambda=0,
 61 have lambda>0.
```

Every one of the 61 positive-slack rows has all thirteen demands strictly positive.

But when every `s_i>0`, the definition

```text
s_i=max(0,d_i-R_i)
```

reduces pointwise to

```text
s_i=d_i-R_i.
```

Therefore

```text
S=sum_i d_i-sum_i R_i
 =2e(F)-r.
```

The exact graph-to-model ledger has

```text
e(F)=r+t=r+1,
```

so

```text
S=2(r+1)-r=r+2.                                   (11)
```

Equation (11) says exactly

```text
lambda=0,
```

contradicting every one of those 61 rows.

Thus the genuine `m=225` endpoint target falls immediately from

```text
272 rows
```

to

```text
211 ledger-tight rows.                            (12)
```

## 5. What remains computational

This note does **not** claim a hand proof of the full `m=225, Delta=16` branch.

Two tasks remain before the historical final exact route can be removed completely:

1. replace the preserved exact classification of the 100 `Q>=18` demand profiles by a hand classification, or otherwise reduce its proof-critical role;
2. replace the historical exact Farkas exclusions of the 211 ledger-tight rows by a hand argument or a substantially smaller transparent certificate family.

Correct-domain reconnaissance shows that the stripped `m=226` two-transport relaxation is insufficient here: with the valid local bound `p<=rho+2`, it excludes only 39 of the 211 tight rows. The earlier exploratory tightening to `p<=rho+1` was invalid and is explicitly rejected in [`N30_M225_RECONNAISSANCE.md`](N30_M225_RECONNAISSANCE.md).

The next analytic target is therefore the structure of the 211 tight rows, not the historical 150-million-state row scan.
