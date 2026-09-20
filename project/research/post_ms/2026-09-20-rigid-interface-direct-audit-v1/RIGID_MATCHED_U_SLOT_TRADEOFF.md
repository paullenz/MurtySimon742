# Rigid Hall cuts — matched-private-coordinate versus U-defect slot tradeoff

Date: 2026-09-20

Status: **same-session structural theorem** conditional on the exact rigid Hall event `M_X=E_X=0`, `x=|A_X|>=3`. This combines the corrected private-coordinate normal form with the exact rigid A_X degree identity and the local rooted Hamming-slot inequality.

The purpose is to price the two ways a fixed outside source can certify its x complete-cut edges **simultaneously**:

- a U-witness creates physical A--U nonedges/slack;
- a matched witness creates a private Boolean coordinate, and many such heads force Hamming load on internal A_X edges.

## 1. One fixed source

Fix `s in Y` with source code d. For its x crossing edges into A_X choose the already-fixed criticality witnesses.

Let

- H be the set of heads whose selected witness is a tight matched endpoint;
- K be the set of heads whose selected witness is in U;
- `m=|H|`, `k=|K|`, so `m+k=x`.

By `RIGID_PRIVATE_COORDINATE_NORMAL_FORM.md`, the m heads in H admit m distinct private coordinates relative to d. Hence any two distinct heads of H have

> `d_H(c(h),c(h'))>=2`.                                   `(MU-HD2)`

The k selected U-witnesses are distinct and each has exactly one A_X-neighbour, its certified head.

## 2. How many internal X edges must lie wholly inside H?

Let

`e_X:=e(G[A_X])`.

Deleting the k vertices of K can remove at most

`k(x-k)+binom(k,2)=kx-k(k+1)/2`

internal X edges. Therefore

> `e(H) >= [e_X-kx+k(k+1)/2]_+`.                          `(MU-EH)`

This is exact extremal bookkeeping: the right side is the number of internal edges that cannot all be incident to the k U-certified heads.

## 3. Private coordinates force rooted Hamming load

For each `z in A`, the local rooted slot theorem gives

`sum_{y in N_A(z)} d_H(c(y),c(z)) <= r_z d_A(z)`.

Sum this inequality over z in H. Every internal H-edge is counted at both endpoints, and by `(MU-HD2)` contributes at least 2 at each endpoint. Thus, with

`R_H:=sum_{z in H} r_z d_A(z)`, `R_X:=sum_{z in A_X} r_z d_A(z)`,

> `R_X >= R_H >= 4 e(H)`.                                `(MU-RH)`

Combining with `(MU-EH)` gives the first joint tradeoff:

> **`R_X >= 4[e_X-kx+k(k+1)/2]_+`.**                     `(MU-1)`

## 4. Substitute the exact rigid cut degree identity

Because `M_X=0`, the exact Hall-cut degree identity is

`2e_X=x(x-T0)-L_X+Z_X`.

Put

`g0=x-T0=p-y`.

Then `(MU-1)` becomes

> **`R_X >= 2[x g0-L_X+Z_X-2kx+k(k+1)]_+`.**             `(MU-2)`

This keeps the actual physical A_X--U deficit `Z_X` rather than replacing it prematurely.

The k U-witnesses selected by the fixed source are physically distinct and each misses `x-1` X-heads, so already

`Z_X>=k(x-1)`.

Substituting only that unavoidable contribution yields the convenient weaker form

> **`R_X >= 2[x g0-L_X-k(x-k)]_+`.**                      `(MU-3)`

Thus the two certificate channels cannot both be cheap:

- making k large pays at least `k(x-1)` physical X--U holes (plus source--U holes and U slack);
- making k small leaves a large matched-covered head set H, whose internal density forces rooted Hamming-slot resource through `(MU-3)`.

## 5. Code-specific matched scarcity

For source code d let `mu_d` be the total number of singleton matched endpoints with gamma d. Any d-coded source has

`k >= k_d:=[x-mu_d]_+`.

The function `k(x-k)` is concave and is maximized near x/2, so one should **not** blindly replace k by k_d in `(MU-3)` without checking the relevant range. The proof-safe statement is existential per actual source/witness selection: use its actual k.

Two safe corollaries are nevertheless immediate:

1. if a source has `k=0`, then

   > `R_X >= 2[xg0-L_X]_+`;                               `(MU-K0)`

2. if a source has `k=1`, then

   > `R_X >= 2[xg0-L_X-(x-1)]_+`.                         `(MU-K1)`

These are especially relevant when U is small and the singleton-gamma budget forces most crossing heads onto matched private coordinates.

## 6. Why this is a new route on the zero-fixture problem

The earlier rigid witness-deficit theorem priced U-heavy certification. The one-code pair purification priced matched traffic through `Ccap_P`. `(MU-2)` adds a missing bridge between them:

> **matched traffic has a rooted Hamming cost whenever it covers a dense collection of X-heads.**

The exact pair-local next step is to retain, for a one-code outside pair P,

- actual matched witness count per source;
- `Ccap_P` and `(ONE-P)`;
- `Z_X` from U witnesses;
- `R_X` from `(MU-2)`;
- `(CROWD)`;

and optimize those together. This is preferable to another total-score collapse and may expose why no actual D2C fixture realizes the rigid complete-cut interface.