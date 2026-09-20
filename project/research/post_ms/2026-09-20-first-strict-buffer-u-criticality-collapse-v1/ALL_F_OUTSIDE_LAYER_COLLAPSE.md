# All-F outside-U layer collapse

Date: 2026-09-20

Status: internal conditional structural theorem inside the audited first-strict unloaded `m=1` all-F branch. It uses only the already-preserved outside-U/Y anticompleteness, reverse-fan code collapse, all-F code geometry, and raw triangle-edge criticality. It does not assert realizability of the rigid complete-cut hypotheses.

## Setup

Write `X'=X\{a_0}` and `u_o=|U_o|=u-k-1`. In the surviving one-witness all-F polarization:

- every vertex of `X'` has one code `C`;
- `C` agrees with `d` only at the unique coordinate `i_0`;
- every vertex of `U_o` has code `bar C` by `BUFFER_UO_REVERSE_FAN.md`;
- `U_o--Y` is empty by `BUFFER_UO_Y_ANTICOMPLETENESS.md`;
- `G[U_o]` is edgeless by the same-code/buffer obstruction in `BUFFER_UO_REVERSE_FAN.md`;
- `b` is complete to `X'` and `U_o`;
- `i_0 in S_0`, so `a_0` and every `bar C` outside vertex select the `bar d` endpoint at `i_0`.

## 1. An outside vertex has at most one X' neighbour

Fix `w in U_o` and suppose `wx in E` for `x in X'`. The edge lies in the triangle `w-b-x`. Apply raw criticality.

### Orientation source x, head w is impossible

A witness must be nonadjacent to `x`, adjacent to `w`, and have singleton common neighbourhood with `x` equal to `{w}`.

- another outside-U vertex cannot be adjacent to `w` because `G[U_o]` is edgeless;
- `b` is adjacent to `x`, so cannot be a nonadjacent witness;
- a core witness has code `bar d`, while `C` agrees with `bar d` in the `p-1` coordinates other than `i_0`, producing a tight matched common neighbour;
- a Y witness is adjacent to `x`, and an X witness shares all nonempty Y with `x`; `a_0` likewise shares all Y with `x`;
- a matched witness adjacent to `w` and not `x` is the `w`-selected endpoint. At `i_0` the buffer `b` is an extra common neighbour of `x` and that endpoint; away from `i_0`, every Y-vertex is an extra common neighbour;
- the root is adjacent to `w` but shares the tight matched neighbours of `x`, so cannot give a singleton.

Hence this orientation cannot certify `wx`.

### Orientation source w, head x

A witness in U is impossible because the root is then an extra common neighbour distinct from the A-head. An X witness has `b` as an extra common neighbour; `a_0` shares the `i_0` tight endpoint with `w`; and a Y witness shares the `p-1` d-coordinates away from `i_0` with `w`.

For a matched witness, away from `i_0` the x-selected endpoint has code `bar d`, so `b` is an extra common neighbour. At `i_0`, however, the x-selected endpoint is the d-endpoint. Its common neighbours with `w` inside A are exactly the X'-neighbours of `w`: Y selects d there but is anticomplete to w, while `a_0`, b, the core and U_o select the opposite endpoint.

Therefore the only possible certificate for `wx` is the d-selected matched endpoint at `i_0`, and it works only if x is the unique X'-neighbour of w. Thus

> `d_{X'}(w)<=1` for every `w in U_o`.                  `(F-UO-XDEG)`

Equivalently,

> `e_bar(X',U_o)>=(x-2)u_o`.                            `(F-UO-XHOLES)`

## 2. The outside layer is anticomplete to a0

Suppose `wa_0 in E` for `w in U_o`. The edge lies in a triangle through the common `bar d` matched endpoint at `i_0`.

For source `w`, head `a_0`:

- a Y witness shares the `p-1` d-coordinates away from `i_0` with w;
- an X' witness has b as an extra common neighbour with w;
- a U witness has the root as an extra common neighbour;
- a matched witness distinguishing `a_0` from w can occur only at a coordinate where `a_0` selects `bar d` and w selects d, and then b is an extra common neighbour.

For source `a_0`, head w:

- no Y vertex is adjacent to w;
- an X' witness shares every Y-vertex with `a_0`;
- another outside vertex is not adjacent to w; b and any core candidate share a tight matched neighbour with `a_0` on the nonempty support `S_0`;
- a matched witness distinguishing w from `a_0` away from `i_0` selects d and therefore has every Y-vertex as an extra common neighbour with `a_0`;
- the root shares tight matched neighbours with `a_0`.

Both orientations fail, contradiction. Hence

> `E(a_0,U_o)=emptyset`.                                `(F-UO-A0)`

Together with Y-anticompleteness and `(F-UO-XDEG)`, every outside vertex has at most one A-neighbour:

> `d_A(w)<=1` for every `w in U_o`.                     `(F-UO-ADEG)`

## 3. Quadratic outside-score floor

For a U-vertex the standard deficit identity may be read as the baseline `p-a` plus its missing A- and U-incidences. Every `w in U_o` misses at least `a-1` vertices of A by `(F-UO-ADEG)`, and at least `u_o-1` vertices of U because `G[U_o]` is edgeless. Therefore

> `epsilon_w >= p+u_o-2`.                               `(F-UO-PAY)`

Summing over the entire outside layer gives

> `E_{U_o} >= u_o(p+u_o-2)`.                            `(F-UO-SCORE)`

This is a physical-population bill, not a selected-witness multiplicity count.

## 4. Linear triangle ceiling

Since both `U_-=W_0 dotcup {b}` and `U_o` are independent,

`q<=|U_-||U_o|=(k+1)u_o`.

The distinguished selected witness z lies in U_o and misses every core vertex while retaining zb, so k cross pairs are also absent. Hence

> `q <= (k+1)u_o-k`.                                    `(F-Q-LINEAR)`

With `T=u-k-2`, so `u_o=T+1`, this is

> `q <= (k+1)T+1`.

Thus the previous quadratic-in-u triangle allowance collapses to a linear function of the outside-reservoir length.

## 5. Consequence for the live attack

The unresolved all-F asymptotic family is no longer merely constrained by the isolation of the selected witness z. The entire outside population is independent, has A-degree at most one, pays quadratic total slack in `u_o`, and contributes only linearly to q. Any residual/score analysis that still uses the older `Q_F=binom(u,2)-binom(k+1,2)-(u-2)` is now strictly obsolete on this branch.
