# One-code residual dimension one: corrected forward-only boundary obstruction

Date: 2026-09-21

Status: **strengthened correction.** For a repeated one-code outside block (`y>=2`), the X-reverse boundary arm is impossible. The earlier same-session gamma/U tradeoff section that treated reverse-only coordinates as live is superseded. The residual-one branch is much more rigid than first recorded.

## 1. Residual-one normal form

Assume residual matched-coordinate dimension

`r=p-m=1`.

Let j be the unique residual coordinate. Then

`H={h_i:i!=j}`, `|H|=p-1`,

with `c(h_i)=d xor e_i`.

The residual X-head class K has size

`k=x-(p-1)=u-c+1`,

when nonempty, and code `d xor e_j`.

The minimum-source escape population is exactly

> **`e=u-k=c-1`.**                                      `(1.1)`

Assume `p>=4`, so `m=p-1>=2` and the full-boundary theorem applies.

## 2. Full exposure

Every tight coordinate is exposed:

> **`I(d,X)=[p]`.**                                      `(2.1)`

At a private coordinate i another private head agrees with d; at residual coordinate j every private head agrees with d.

For private coordinates, h_i itself shows nonuniversality. At j:

- if `k>=1`, a K-head differs from d, so `C=empty`;
- if `k=0`, j is the only possible universal coordinate, so `C subseteq {j}`.

## 3. Repeated outside code forces forward-only routing

Assume

> **`y>=2`.**                                             `(3.1)`

The corrected boundary theorem makes X-reverse certification impossible at every coordinate. Thus every one of the p exposed coordinates must use either U-forward or matched-forward support.

Only the escape reservoir `e=c-1` can populate U-forward one-match classes, because the selected complementary class `U_bar d` is disjoint from all codes `bar d xor e_i`.

### Theorem 3.1 — residual-one repeated-code obstruction

For every residual-one one-code realization with `p>=4,y>=2`,

> **`p<=c+1`, hence `c>=p-1`.**                          `(3.2)`

This uses only the global bound of at most two matched-forward heads.

If `k>=1`, then `C=empty`, so matched-forward support vanishes completely and

> **`p<=c-1`, hence `c>=p+1`.**                          `(3.3)`

If `k=0`, then `C subseteq {j}` and at most one matched-forward head is possible, giving the intermediate bound

> **`p<=c`, hence `c>=p`.**                              `(3.4)`

These are literal graph-realizability restrictions, not score inequalities.

## 4. Intermediate half-ray closes immediately

The corrected diagnostic half-ray has

`p=2t`, `c=t`, `r=1`, `y=t>=4`, and `k=2>=1`.

The strong bound `(3.3)` would require

`2t<=t-1`,

which is impossible for every positive t. Hence the half-ray has no actual realization for any of its stated values `t>=4`.

All later H--U carrier, equality-face and superconstant analyses on this ray are therefore strategically subordinate diagnostics rather than a necessary route to its closure.

## 5. What remains in residual dimension one

For repeated outside code (`y>=2`), a residual-one one-code survivor must drive the rooted gap to essentially the full tight dimension:

- `c>=p+1` if the residual K class is present;
- `c>=p` if it is absent.

The former “large residual-class reverse-capacity” escape does **not** exist: even an arbitrarily large X reverse class cannot certify a boundary edge when there is a second same-code outside vertex, because source and witness would share both outside vertices.

The only qualitatively different residual-one case is

> **`y=1`,**

where X-reverse certification may still be possible and gamma multiplicity remains relevant.

Thus the correct next residual-one split is not “small-U versus large residual X-class”; it is

1. repeated outside code `y>=2` with `c` forced to `p+O(1)` or larger; versus
2. singleton outside code `y=1`.

## 6. Scope

This theorem remains conditional on the rigid complete one-code interface. It bypasses the audit-sensitive source-tuple capacity theorem. Bounded actual-D2C regression still has no positive rigid complete pair-family cut with `x>=3`; X_3 remains the mandatory negative control.
