# Exact second-strict mixed y=1 — x=4 singleton-support tail is finite-order

Date: 2026-09-20

Status: **same-session internal structural/algebraic reduction**. This checks that the large-head R/Fx/Fz proof uses `x>=5` only to obtain `|S_0|=1`; once singleton support is assumed explicitly, the classification and rooted-margin bounds transfer to `x=4`.

## 1. Setup

Assume the exact mixed second-strict y=1 geometry with

- `x=4`;
- `p>=2`;
- `S_0={j}`.

The raw edge `a_0y` has the same exhaustive three certificate types as in `SECOND_STRICT_MIXED_Y1_CLASSIFICATION.md`:

- R: `z_0` witnesses `y -> a_0`;
- Fz: `z_0` witnesses `a_0 -> y`;
- Fx: one complementary X-vertex t witnesses `a_0 -> y`.

Reviewing the subsequent proofs, no step needs `x>=5` once `S_0={j}` is supplied:

1. R: all three buffer heads are outside-certified Type R; the radius>=2 exclusion uses only the unique coordinate j and the fixed z_0 certificate.
2. Fx: exactly `x-2=2` heads are outside-certified Type R and the complementary head t is the unique reverse-buffer head. The no-higher-radius argument uses only the fixed singleton `N(b) cap N(z_0)={t}` and the unique coordinate j.
3. Fz: all three buffer heads are outside-certified Type R; at most one is higher-radius by ordered-pair injectivity at `(q_j,z_0)`, leaving at least two radius-one C-heads, enough for the same-code and h--C exclusions.

Thus the R/Fx/Fz code classifications, `G[X]=emptyset` conclusions and case-specific physical rooted margins transfer unchanged to `x=4,S_0={j}`.

## 2. Rooted-margin optimization

Write `k=x-g=4-g`, so `g in {1,2,3}`.

### R and no-exception Fz

The exact real-omega maximum of twice the rooted margin is

`2B_max=eps+4g-k^2-2kp+6k-p^2+2p-4`.

For integers `p>=2`, `g=1,2,3`, direct symbolic comparison of this quadratic in p gives `B_max>=0` only when

> **`p<=3`.**                                             `(X4-R-P3)`

More explicitly, the only `(p,g)` pairs surviving this necessary maximized test are

`(2,2)`, `(2,3)`, `(3,3)`.

Completing the omega square gives centre

`omega_*=x-p+2=6-p`

and maximum `2B_max<=10`, so every integer survivor has

> **`omega<=7`.**                                         `(X4-R-W7)`

### Exceptional Fz

Here

`2B_max=eps+4g-k^2-2kp+4k-p^2+2p-6`.

Again `B_max>=0` forces

> **`p<=3`,**

and the largest square maximum is 6, with the same centre `6-p`. Hence

> **`omega<=6`.**                                         `(X4-FZ-W6)`

### Fx

Using the safe rooted-floor relaxation `r_low>=x+p-1`,

`2B_max<=eps+2g-k^2-2kp+4k-p^2+2p+1`.

The only possible p values again satisfy

> **`p<=3`.**

The omega-square centre is

`x-p+1=5-p`,

and the maximum is at most 7, giving

> **`omega<=5`.**                                         `(X4-FX-W5)`

## 3. Order bound

For mixed y=1,

`n=x+2p+k+omega+3`.

With x=4, p<=3, k<=2 in the R/Fz survivors that maximize the order, and omega<=7, a uniform safe bound is

> **`n<=19`.**                                            `(X4-S1-N19)`

Therefore:

> **the x=4, |S_0|=1 mixed-y1 tail is impossible for n>=20.**

No finite graph enumeration is used. The finite list of `(p,g)` values above is merely evaluation of an explicit quadratic necessary condition over the three possible values of g.

## 4. Remaining x=4 geometry

The earlier exceptional-capacity inequality

`(H-1)(|S_0|-1)<=1`, with `H>=x-2=2`,

shows that the only x=4 geometry not covered here is the exact corner

> **`H=2`, `|S_0|=2`.**                                  `(X4-CORNER)`

Thus x=4 has been reduced to one literal support/certificate pattern. The next attack should reconstruct that corner directly rather than retain an unconstrained x=4 parameter family.