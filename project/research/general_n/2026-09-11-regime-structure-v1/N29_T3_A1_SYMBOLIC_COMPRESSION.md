# n=29, t=3, A1 regime: symbolic-on-support compression

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite structural result inside the RX-Hall programme. Conditional on the graph-to-profile bridge, the 3-D potential-certificate lemma and the stated n=29 parameters. This is not a general-N Murty–Simon theorem. Independent review remains open.**

## 1. Headline

The `t=3` regime

```text
(h_res,J)=(4,14),
J=2 #{u:rho_u>=2}-#{i:s_i=1},
```

is the 11-profile regime certified by template `A1` for the fixed potential

```text
F = 6 B(3,0) + 4 B(3,5) + 3 B(3,9).
```

This regime can now be reduced much further than the original finite endpoint machinery.

Two exact standard-library replays establish:

1. a transparent necessary-condition core reduces **236,885** abstract histogram pairs to exactly the **11** audited A1 profiles using only charging, zero slack, `h=4`, `J=14`, the scalar supplement cutoff, total selected-incidence capacity and largest-demand-prefix Hall inequalities;
2. on the resulting support class, the A1 certificate gap is an explicit positive linear combination of three elementary tail slacks, with minimum exactly **1** and unique equality at profile 1.

No demand dual, threshold certificate, C++ residual-row scanner, LP/MIP solver, saved dual vector or floating-point arithmetic is needed in this compressed A1 argument.

## 2. Transparent core reduction

Start only with:

- twelve positive demand integers `s_i`;
- sixteen positive residual degrees `rho_u`;
- the exact charging inequality;
- zero slack `sum s = sum rho + 6`;
- `h_res(rho)=4`;
- `J=14`;
- the scalar supplement-cutoff lemma;
- total selected-incidence capacity;
- Hall on largest-demand prefixes.

The exact standard-library enumeration gives

```text
broad histogram pairs:          236,885
total-capacity rejections:      226,990
prefix-Hall rejections:           9,884
survivors:                           11
```

The initial `D1=#{s_i=1}` census is

```text
D1=0: 220,966
D1=2:  15,907
D1=4:      12
```

The eleven survivors have exactly

```text
s support:    {2,3,4}
rho support:  {1,3,4,5,6}
rho1:         9
scalar cutoff L: 6.
```

Their histogram set agrees exactly with the independently regenerated 11-profile `(h,J)=(4,14)` frontier cell.

Replay:

```text
n29_t3_a1_core_reduction_exact.py
```

Successful GitHub Actions run:

```text
34594956004
```

This is still a finite order-29 reduction, but it removes the opaque parts of the old preparation from this regime and exposes the small combinatorial core that must be parameterised.

## 3. A1 envelope values

The exact A1 template is

```text
lambda = 9/5,
c      = 16/3,
tau_2  = 23/3,
```

with all other scalar coefficients zero.

On the surviving support class the exact finite envelope minima are

```text
ell_2 = 32/3
ell_3 = 55
ell_4 = 1028/15

sigma_1 = 0
sigma_3 = -253/3
sigma_4 = -253/3
sigma_5 = -92
sigma_6 = -299/3.
```

The order of the argument matters. For rejected abstract states with very large `D4`, the source envelope at `rho=3` can change because `qmax(3)` falls. Those states are first eliminated structurally by the scalar-cutoff capacity argument. The stable A1 envelope is invoked only on the surviving `D4<=6` class.

That correction is enforced by the exact replay rather than hidden in exposition.

## 4. Exact three-slack identity

Define

```text
U = sum_{i:s_i>=3} s_i,
V = sum_{i:s_i>=4} s_i,
Z = sum_{u:rho_u>=4} rho_u.
```

For every survivor the exact A1 certificate gap is

\[
\boxed{
\operatorname{gap}_{A1}
=1+rac{1454}{135}(U-36)
 +\frac{125}{54}(24-V)
 +\frac{23}{9}(Z-16).
}
\]

All arithmetic is exact rational arithmetic.

Replay:

```text
n29_t3_a1_slack_identity_exact.py
```

Successful corrected GitHub Actions run:

```text
34594720253
```

## 5. Why the three slacks are nonnegative

Write the demand histogram as

```text
D2+D3+D4=12
```

and the non-unit residual histogram as

```text
R3+R4+R5+R6=7,
```

with nine residual ones.

### 5.1 Scalar cutoff forces `D4<=6`

Assume instead that `D4=k>=7`.

Because there are no unit demands in the surviving support class,

```text
C(1)=0.
```

There are only seven non-unit residual sources. Therefore the cutoff gate at level 7 cannot open: it would require eight supporters at threshold 6. Hence

```text
L<=6.
```

For a residual-3 source,

```text
C(3)=12-k<=5,
```

while residual degrees 4,5,6 have initial caps 8,7,6. Consequently the total terminal selected-degree cap obeys

\[
\sum_u q_u^*
\le R_3(12-k)+6(7-R_3)
\le 42-R_3.
\]

But `h=4` implies at least four of the seven non-unit residual degrees are at least 4, so

\[
\sum_u \rho_u
\ge 9+3R_3+4(7-R_3)
=37-R_3.
\]

Zero slack then gives

\[
\sum_i s_i=\sum_u\rho_u+6\ge43-R_3.
\]

Thus

\[
\sum_i s_i>\sum_u q_u^*,
\]

contradicting total selected incidence, because `x_i>=s_i` and `sum_i x_i=sum_u q_u`.

Therefore

\[
\boxed{D_4\le6},
\]

so

\[
V=4D_4\le24.
\]

### 5.2 `h=4` gives `Z>=16`

At least four residual degrees are at least 4. Hence immediately

\[
\boxed{Z\ge16}.
\]

### 5.3 Zero slack gives `U>=36`

Within the surviving support class, `h=4` gives

\[
\sum\rho\ge9+3\cdot3+4\cdot4=34,
\]

so zero slack gives

\[
\sum s\ge40.
\]

Now

\[
\sum s=36-D_2+D_4,
\]

hence

\[
D_4-D_2\ge4.
\]

Since `D4<=6`, this forces `D2<=2`. Also

\[
U=36-3D_2+D_4.
\]

Using `D4>=D2+4` and `D2<=2`,

\[
U\ge36+(4-2D_2)\ge36.
\]

Therefore

\[
\boxed{U\ge36}.
\]

## 6. Consequence

All three correction terms in the exact gap identity are nonnegative. Hence

\[
\boxed{\operatorname{gap}_{A1}\ge1}.
\]

Equality requires simultaneously

```text
U=36,
V=24,
Z=16.
```

These force

```text
(D2,D3,D4)=(2,4,6),
(R3,R4,R5,R6)=(3,4,0,0),
```

which is exactly audited frontier profile 1. Thus the margin-one extremal is unique inside this regime.

## 7. How much enumeration remains?

The certificate positivity itself is now essentially a hand argument once the support class is known.

The transparent core replay still uses finite histogram enumeration to show that the starting necessary conditions reduce to that support class. Even that enumeration is already much simpler than the historical preparation. Several parts admit immediate hand reductions:

1. the charging score of any demand is at most `5/2`, so charging plus `J=14` restricts `D1` to `0,2,4`;
2. the one-label Hall inequality plus `h=4` forces `max s_i<=4` (a demand at least 5 would require at least five residual sources of degree at least 5, contradicting `h=4`);
3. the `D1=4` branch is impossible without enumeration: `J=14` gives seven residual ones and nine non-unit residuals; `h=4` then forces residual sum at least 33 and demand sum at least 39, while four unit demands and `s_i<=4` give demand sum at most 36.

Therefore the only unresolved pre-support branch for a fully hand-written reduction is

```text
D1=2.
```

The exact core replay shows that every one of its 15,907 abstract histogram pairs is excluded by total capacity or prefix Hall. After total-capacity and the one-label Hall reduction, only a very small structured family remains. Compressing that family to one symbolic Hall contradiction is the current highest-value local target.

## 8. Significance for the general programme

This is the first current `t=3` scalar regime for which the finite template certificate has been converted into:

```text
simple necessary conditions
 -> scalar-cutoff Hall core
 -> explicit support class
 -> three nonnegative tail slacks
 -> exact positive certificate gap.
```

That is much closer to a parameterised theorem architecture than a table of finite certificates.

The obvious next tests are:

1. eliminate the remaining `D1=2` pre-support branch symbolically, removing the 236,885-state enumeration from the A1 derivation;
2. seek analogous slack decompositions for the adjacent `A530` regimes `(4,16)` and `(4,18)`;
3. determine which coefficients and thresholds can be written in terms of `(a,b,t,h,J)` rather than the fixed values `(12,16,3,4,14)`;
4. continue independent red-team of the graph-to-profile/RX-Hall bridge and the 3-D potential lemma.

The unrestricted conjecture remains open.