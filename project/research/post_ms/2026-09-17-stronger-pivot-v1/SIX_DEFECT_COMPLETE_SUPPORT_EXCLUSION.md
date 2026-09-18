# Complete six-defect switching layer is support-impossible from k >= 9

18 September 2026. Research directed by Paul Lenz; structural reduction and finite certificates by ChatGPT/Geeps.

**Status: internal finite-certificate structural theorem; not promoted. External mathematical review and hand compression of the six-vertex core certificate remain open.**

This note combines the general leaf package, the new coordinatewise residual-monotonicity lemma, the separately classified lopsided six-defect ray, and a finite proof-producing residual matching audit. The result is stronger than expected: **every** six-defect switched state is support-impossible once `k>=9`.

The active objective is the eventual/sufficiently-large second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The published order-12/32 `X_3` graph is the separate `k=4,r=0` zero-defect mechanism and remains the mandatory negative control.

## 1. Setup

Let a switched state on the `k` antipode fibres have exactly six non-leaf exceptional coordinates. Let

\[
p_1\le\cdots\le p_6
\]

be its sorted pendant-group sizes, let `t` be the number of isolated leaf-leaf `K_2` components, and let `g` be the number of positive `p_i`. Then

\[
k=6+\sum_i p_i+2t.
\]

The exact general leaf package is

\[
B_6=2\sum_i(p_i-1)_++2\sum_{i<j}\min(p_i,p_j),
\]

and, for `t>=1`,

\[
L_6=B_6+4tg+2t(t-1)+1.
\]

An above-`M(n)` full-tight graph requires `tau(Omega)<=a<=2k`, so any possible state must satisfy

\[
L_6\le2k. \tag{1}
\]

For `t>=1`, the general necessary inequality becomes

\[
2\sum_{i=1}^6(6-i)p_i +(4t-2)g+2t^2-6t-11\le0. \tag{2}
\]

In particular `t>=5` is impossible even when `g=0`.

## 2. Coordinatewise monotonicity makes the frontier finite

By `COORDINATEWISE_RESIDUAL_RAY_MONOTONICITY.md`, once any pendant group has size at least two, enlarging that group cannot decrease

\[
L_6+\tau(R)-2k,
\]

where `R` is the residual orientation-code graph outside the exact leaf-package code vertices.

Therefore every attachment vector with `k>=9` reduces to the coordinatewise-minimal representative of its status pattern

\[
p_i\in\{0,1,\ge2\},
\]

with each `>=2` replaced by `2`, except that the unique lopsided no-pair status `(0,0,0,0,0,>=2)` first enters the range `k>=9` at size `3`.

After imposing (1), sorting the attachment statuses, and using `t<=4`, there are exactly

\[
\boxed{31}
\]

boundary patterns at `k>=9`.

They split by isolated-pair count as follows:

- `t=0`: 14 patterns, including the lopsided `(0,0,0,0,0,3)` ray;
- `t=1`: 8 patterns;
- `t=2`: 5 patterns;
- `t=3`: 3 patterns;
- `t=4`: 1 pattern.

There are no surviving `t>=5` patterns.

Thus the infinite six-defect pendant geometry has been reduced completely to 31 finite attachment-status boundaries and the `2^15` possible labelled exceptional cores.

## 3. The lopsided boundary

The lopsided no-pair pattern

\[
(0,0,0,0,0,3),\qquad k=9,
\]

is handled in `SIX_DEFECT_LOPSIDED_SUPPORT_EXCLUSION.md`.

At `z=3`, all `15572` valid labelled exceptional cores are audited. The disjoint leaf-package/residual cover is already strict except for 15 labelled cores, all one rooted isomorphism class

\[
K_2\vee2K_2.
\]

That class has an explicit all-`z` orientation-code decomposition giving

\[
\tau(\Omega)=2k+2.
\]

Coordinatewise residual monotonicity propagates all other strict base certificates. Hence the lopsided status is support-impossible for all `k>=9`.

## 4. The other 30 status patterns: residual matching certificates

For each of the remaining 30 boundary patterns, enumerate every labelled graph on the six exceptional coordinates and discard any core for which an allegedly exceptional coordinate has total switched degree one.

Delete the exact leaf-package code vertices from `Omega`, giving the residual graph `R`. A vertex-disjoint matching of size `s` in `R` certifies

\[
\tau(\Omega)\ge L_6+s. \tag{3}
\]

A deterministic proof-producing rule was used: repeatedly choose a minimum-positive-degree live residual vertex and match it to a minimum-degree live neighbour, deleting both endpoints. The resulting matching itself is the certificate; optimality is neither assumed nor needed.

For **29 of the 30** nonlopsided boundary patterns, for every valid exceptional core this explicit greedy matching already yields

\[
\boxed{L_6+|M|\ge2k+1}. \tag{4}
\]

The minimum certified margin is exactly `+1` in each of those pattern rows.

The number of valid exceptional cores varies with the attachment status, from `13757` to `25460`; the companion audit records each row separately.

### The sole matching-certificate miss

The only boundary where the deterministic matching rule is insufficient is the fixed state

\[
t=2,\qquad(p_1,\ldots,p_6)=(0,0,0,0,0,0),\qquad k=10. \tag{5}
\]

For every valid exceptional core except the empty core, the same matching rule still proves strict support excess. For the empty exceptional core the exact residual graph has the transparent decomposition

\[
\boxed{R\cong 8K_{1,6}\ \dot\cup\ 2K_6}. \tag{6}
\]

Therefore

\[
\tau(R)=8+2\cdot5=18. \tag{7}
\]

Here the isolated-pair leaf package has

\[
L_6=5,
\]

so

\[
\tau(\Omega)\ge L_6+\tau(R)=23>20=2k. \tag{8}
\]

Thus the unique finite miss of the generic matching certificate is closed by a two-line component calculation.

## 5. Complete six-defect support theorem

Every six-defect state with `k>=9` is either:

1. discarded immediately by `L_6>2k`;
2. coordinatewise above one of the 31 finite boundary patterns;
3. on the lopsided ray, closed by Section 3;
4. above one of the 29 generically matching-certified boundaries; or
5. the sole fixed exceptional case (5), closed by (6)--(8).

Coordinatewise residual monotonicity preserves every strict boundary certificate under enlargement of any established pendant group. Hence:

> **COMPLETE SIX-DEFECT SUPPORT EXCLUSION — internal candidate.** If a full tight-antipode switching class contains a state with exactly six non-leaf coordinates and
>
> \[
> \boxed{k\ge9},
> \]
>
> then
>
> \[
> \boxed{\tau(\Omega)>2k}.
> \]
>
> Consequently such a state cannot occur in an above-`M(n)` full-tight graph.

No F-separation or residual-defect cleanup is required.

## 6. Sharp switching-level boundary

The theorem cannot simply be moved down to `k=8` by the same support statement. In the lopsided status with two pendant leaves and empty exceptional core,

\[
\tau(\Omega)=16=2k.
\]

No D2C realization is claimed. This is a genuine switching-level support equality and explains the stated threshold.

## 7. Significance

The fixed-defect hierarchy now contains a qualitative run:

- four defects: eventual closure still needs F-separation on a small lopsided family;
- five defects: support-impossible from `k>=8`;
- **six defects: support-impossible from `k>=9`.**

The six-defect proof is more reusable than a direct 31-pattern census suggests: the coordinatewise monotonicity theorem means the census concerns only the finite `{0,1,2}` boundary of pendant geometry. The remaining finite difficulty is entirely in the exceptional core.

This strengthens the case for a defect-count-independent theorem for all `d>=5`. The next structural target should be a general lower bound on the residual exceptional-core contribution after ternary reduction, rather than a seventh one-off unbounded scan.

## 8. Trust boundary

- The leaf package and coordinatewise monotonicity are hand structural arguments.
- The six-coordinate core step is presently a finite proof-producing certificate: explicit matchings for all but one finite core instance, plus the exact component decomposition (6) for that instance.
- The lopsided dangerous core has a separate explicit all-ray component formula.
- The finite certificate has not been compressed into a short isomorphism-class proof and remains open to external mathematical review.
- The published `12/32` `X_3` counterexample is outside theorem scope and unaffected.
- No all-order second-extremal statement is claimed.
