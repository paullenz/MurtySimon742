# Residual-one k=2 coupled K-heavy / F0 minimum

Date: 2026-09-20

Status: **same-session analytic corollary**, conditional on the exception-conservation and sector-deficit theorems. No finite scan is used.

This note solves the simplest weighted endpoint exposed by the coefficient-sensitive exception theorem: an escape reservoir carried asymptotically only by K-heavy vertices R and fully K/W_s-free vertices F0. The result is stronger than the global five-class `tau` bound and shows that the R/F0 tradeoff itself is not the most permissive asymptotic geometry.

## 1. Setup

On the exact low-k ray

`c=p=lambda`, `y=p-1`, `u=x=p+1`, `k=2`,

let

- `r=|R|` be the K-heavy population;
- `f=|F0|` be the fully K/W_s-free population;
- `E_R=sum_R epsilon_w`, `E_F=sum_F0 epsilon_t`;
- `A=sum_{w in R}|H\N(w)|`;
- `S_F=Z_H(F0)+Z_Y(F0)+M_U(F0)`.

Assume `r+f=p-1-o(p)`; equivalently, all other escape classes have sublinear size. Define

`D_RF=E_R+E_F+A+S_F`.

Every term lies in the physical rooted/score currencies and no term is counted twice in this definition.

## 2. Two lower bounds

The F0 sector-deficit theorem gives

> `S_F >= [f(p-4)+E_F]/2 >= f(p-4)/2`.                  `(RF-SECT)`

The coefficient-sensitive exception conservation gives

`(1+2f/p)E_R+(2r/p)E_F+3A+yq >= r(r-1)`,                `(RF-CONS)`

where q is the number of X-anticomplete exceptional witnesses used by opposite-orientation Y-edge certificates.

Every such q-witness lies in F0 and contributes a full H/X hole block. In particular

`yq <= Z_H(F0) <= S_F`,

because here `|H|=y=p-1` and an X-anticomplete F0 witness misses all H-heads.

Also

`1+2f/p <=3`, `2r/p<=2<=3`.

Therefore the left side of `(RF-CONS)` is at most

`3E_R+3E_F+3A+S_F`
`=3D_RF-2S_F`.

Since `(RF-CONS)` says that same quantity is at least `r(r-1)`, we obtain

> **`3D_RF >= r(r-1)+2S_F`.**                            `(RF-C1)`

Using `(RF-SECT)`:

> **`D_RF >= [r(r-1)+f(p-4)]/3`.**                       `(RF-C2)`

Independently, `(RF-SECT)` itself gives

> **`D_RF >= f(p-4)/2`.**                                `(RF-C3)`

## 3. Asymptotic minimum is one quarter

Write `r/p -> alpha` and `f/p -> 1-alpha`. Divide `(RF-C2)` and `(RF-C3)` by `p^2` and pass to the limit:

`liminf D_RF/p^2 >= max{`
`  (alpha^2-alpha+1)/3,`
`  (1-alpha)/2`
`}`.                                                     `(RF-LIM)`

The two expressions agree exactly at `alpha=1/2`:

`(1/4-1/2+1)/3=1/4`,

`(1-1/2)/2=1/4`.

For `alpha<1/2`, the second term is greater than `1/4`; for `alpha>1/2`, the first term is increasing from `1/4`. Hence

> **`liminf D_RF/p^2 >= 1/4`.**                           `(RF-MAIN)`

Equality in this coarse asymptotic relaxation can occur only near the balanced split

> `r~f~p/2`.                                              `(RF-BAL)`

Thus an R/F0-dominant realization is substantially more expensive than the global five-class lower bound `tau p^2`, where `tau≈0.09387`. The coarse global minimizer must use the other escape classes at linear scale; it cannot hide solely in the K-heavy / fully-free exception tradeoff.

## 4. Strategic consequence

The live weighted problem has narrowed again. Any asymptotic configuration close to the global minimum must use a linear population from at least one of

- F1: K-free with exactly one W_s neighbour;
- S: W-heavy;
- M: mixed;
- D with one K-neighbour rather than the fully-free F0 subcase.

These classes have stronger literal local structure than the abstract five-way functional records: F1 and S are Y-anticomplete, M pays `epsilon>=p+1` vertexwise, and the one-K-neighbour D subclass is W_s-free but still carries a named K adjacency that can be attacked by raw B-edge criticality.

The next weighted optimization should therefore separate `D0=F0` from `D1={W_s-free, d_K=1}` and retain the exact `r--F1/S` missing U blocks already proved by the heavy-endpoint theorem. If the resulting coefficient rises enough, feed the currencies into the exact score/rooted inequalities; otherwise the optimizer identifies which of F1/S/M/D1 must be attacked next.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; this remains conditional downstream mathematics pending independent hostile replay.