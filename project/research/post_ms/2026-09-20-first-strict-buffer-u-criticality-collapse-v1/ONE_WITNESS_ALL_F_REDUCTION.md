# Surviving one-witness branch: all-F isolation and head saturation

Date: 2026-09-20

Status: internal conditional structural follow-up. `ONE_WITNESS_ALL_R_COLLAPSE.md` eliminates the all-R polarization, so this note analyzes the surviving all-F case. It remains conditional on the rigid first-strict hypotheses.

## 1. All-F setup

For `m=1` all-F:

- all vertices of `X'=X\{a_0}` have one common code C;
- relative to d, C has exactly one agreement coordinate `I_C={i_0}` and differs from d in the other `p-1` coordinates;
- the unique outside witness z has code `bar C`, is anticomplete to all of A, and `za_0` is a nonedge;
- for every `x in X'`, `N(x) cap N(z)={b}`;
- the forward funnel gives `N(z) cap N(a_0)={q_{i_0}}`, where `q_{i_0}` is the `bar d` matched endpoint.

The generic theorem `BUFFER_UO_Y_ANTICOMPLETENESS.md` gives `E(U_o,Y)=emptyset` and `U_o cap V_{bar d}=emptyset`.

## 2. z misses the entire common core — no y assumption

Every core vertex `w in W_0` has a graph-fixed unique X-head `h(w)`.

If `h(w) in X'`, then `wh(w) in E` while the buffer certificate gives `N(h(w)) cap N(z)={b}`. Hence `wz` would make w an illicit second common neighbour.

If `h(w)=a_0`, the forward funnel gives `N(z) cap N(a_0)={q_{i_0}}`; again `wz` would make w an illicit second common neighbour because `wa_0 in E`.

Therefore, without assuming y>=2,

> `z--W_0` is empty.                                    `(F-ZCORE)`

## 3. z has no second outside-U neighbour

Suppose `w in U_o\{z}` and `zw in E`.

- For every `x in X'`, `N(x) cap N(z)={b}` forces `xw` to be a nonedge.
- `N(z) cap N(a_0)={q_{i_0}}` forces `a_0w` to be a nonedge.
- `BUFFER_UO_Y_ANTICOMPLETENESS.md` forces `w--Y` to be empty.

Thus w is anticomplete to all of A. But z itself is also anticomplete to A.

The U--U edge zw lies in a triangle through the root. Raw triangle-edge criticality cannot use a root-neighbour witness: with a U-source the root would be an extra common neighbour distinct from the U-head. Hence any witness must lie in A. In either orientation the witness would have to be adjacent to the opposite endpoint, yet both z and w are A-anticomplete. No certificate exists, contradiction.

Therefore

> `N_U(z)={b}`.                                         `(F-ZISO)`

This is an exact physical statement, not a score relaxation.

Since z has exactly the root, p selected tight matched endpoints and b as neighbours,

> `d(z)=p+2`,
>
> `epsilon_z=p+u-2`.                                    `(F-ZEXACT)`

The internal independent set `U_-=W_0 dotcup {b}` contributes `binom(k+1,2)` missing U-pairs. The additional `u-2` missing pairs from z to every U-vertex except b are disjoint from those. Hence

> `q<=binom(u,2)-binom(k+1,2)-(u-2)`.                  `(F-QEXACT)`

This exact witness isolation holds for **all y>=1** in the all-F polarization.

## 4. For y>=2 every X'--Y edge must be core-certified

Now assume `y>=2`. Fix `x in X'`, `y_0 in Y`. The edge `xy_0` lies in a triangle because C and d agree at coordinate `i_0`. Apply raw triangle-edge criticality.

### Source x, head y_0

- A Y-witness is adjacent to x and therefore cannot be a nonadjacent witness.
- Any X-witness adjacent to the head shares all y>=2 Y-vertices with x, so the common neighbourhood cannot be the singleton `{y_0}`.
- A matched witness distinguishing C from d must be the d-selected endpoint in one of the p-1 differing fibres. That endpoint is adjacent to every Y-vertex, while x is also adjacent to every Y-vertex; again y>=2 forbids a singleton head.
- No `U_o` witness is adjacent to a Y-head by outside-U/Y anticompleteness.
- A core/buffer witness has code `bar d`. Since Type F C agrees with d only at i_0, C agrees with `bar d` in the other p-1>=2 fibres; source and witness then share matched neighbours distinct from the head.

So this orientation is impossible.

### Source y_0, head x

- Every X-vertex is adjacent to y_0 and cannot be a nonadjacent A-witness; another Y-vertex has the same code d and shares tight matched neighbours.
- A matched witness must be the C-selected endpoint in a fibre where C differs from d. Every vertex of X' has the same code C, so all N=x-1>=2 vertices of X' are common neighbours of y_0 and that matched endpoint. It cannot single out x.
- A U-witness must have complementary code `bar d`; there is no such vertex in `U_o` by the generic no-`bar d` theorem.
- The buffer b has code `bar d` but shares all of X' with y_0, so it cannot single out one x.
- A core vertex in W_0 may work only at its graph-fixed unique X-head.

Therefore the edge `xy_0` can be certified only by a core vertex whose unique X-head is x.

This conclusion holds for every y_0 in Y. Hence **every vertex of X' must occur as a core head.**

## 5. Head saturation for y>=2

The core-head map `W_0 -> X` is injective and `|W_0|=k`. Since all N=x-1 vertices of X' must be heads,

> `k>=x-1`.

But `k=x-g` and `g>=0`, so

> `g<=1`, and `k in {x-1,x}`.                           `(F-GATE)`

Thus the surviving `m=1`, `y>=2` branch is confined to the two head-saturated cases g=1 and g=0.

## 6. Current surviving one-witness geometry

Combining the all-R collapse with this theorem, every `m=1` first-strict survivor satisfies the exact all-F Hamming bill

`r >= x + y[p-1-floor((p-2)/x)] >= a+y`,

and for every y it has the exact witness isolation

- `z--W_0=empty`;
- `N_U(z)={b}`;
- `epsilon_z=p+u-2`;
- `q<=binom(u,2)-binom(k+1,2)-(u-2)`.

When `y>=2` it additionally has

- `g in {0,1}`;
- every X' vertex is a distinct common-core head.

The separate `y=1` all-F slice remains live because the unique Y-head allows a differing-fibre matched endpoint to certify X->Y edges; it should be handled separately rather than importing the head-saturation argument.

## 7. Next attack

The unique selected outside witness is now almost completely isolated, and its slack grows as `p+u-2`. The highest-value next calculation is to combine `(F-ZEXACT)/(F-QEXACT)`, the exact pair-local threshold and the all-F Hamming-slot lower bound. For `y>=2`, do this only in the two regimes g=0 and g=1. Keep y=1 separate and inspect its matched-foot certificates directly.