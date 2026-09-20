# Surviving one-witness branch: all-F reduction for y>=2

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

Assume in this note that `y>=2`.

## 2. Every X'--Y edge must be core-certified

Fix `x in X'`, `y_0 in Y`. The edge `xy_0` lies in a triangle because C and d agree at the coordinate `i_0`. Apply raw triangle-edge criticality.

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

## 3. Head saturation

The core-head map `W_0 -> X` is injective and `|W_0|=k`. Since all N=x-1 vertices of X' must be heads,

> `k>=x-1`.

But `k=x-g` and `g>=0`, so

> `g<=1`, and `k in {x-1,x}`.                           `(F-GATE)`

Thus the surviving `m=1`, `y>=2` branch is not a broad g-range: it is confined to the two head-saturated cases g=1 and g=0.

## 4. z misses the entire common core

If a core vertex w has head `x in X'`, then `wx in E`. The outside buffer certificate gives `N(x) cap N(z)={b}`. Therefore `wz` must be a nonedge, otherwise w is a second common neighbour.

If `k=x-1` (g=1), every core head lies in X', so z misses all k core vertices.

If `k=x` (g=0), injectivity makes the core-head map a bijection onto X: x-1 core vertices head X', and the remaining core vertex heads `a_0`. The forward funnel has `N(z) cap N(a_0)={q_{i_0}}`; hence the remaining core vertex also misses z, otherwise it is another common neighbour of z and `a_0`.

Therefore in both head-saturated cases

> `z--W_0` is empty.                                    `(F-ZCORE)`

Since z is already anticomplete to A, direct degree counting gives

> `epsilon_z>=p+k`.                                     `(F-ZPAY)`

and the rooted triangle ceiling gains k physical U--U holes:

> `q<=binom(u,2)-binom(k+1,2)-k`.                       `(F-Q)`

## 5. Current surviving one-witness geometry

Combining the all-R collapse with this theorem, every `m=1` first-strict survivor satisfies the exact all-F Hamming bill

`r >= x + y[p-1-floor((p-2)/x)] >= a+y`,

and when `y>=2` it additionally satisfies

- `g in {0,1}`;
- every X' vertex is a distinct common-core head;
- `z--W_0` is empty;
- `epsilon_z>=p+k`;
- the strengthened q ceiling `(F-Q)`.

The separate `y=1` all-F slice remains live because the unique Y-head allows a differing-fibre matched endpoint to certify X->Y edges; it should be handled separately rather than importing the y>=2 argument.

## 6. Next attack

For y>=2 the branch has collapsed to two explicit head-saturated regimes. The highest-value next calculation is to combine `(F-GATE)/(F-ZPAY)/(F-Q)` with exact pair-local score and the all-F Hamming-slot lower bound, looking for a direct residual contradiction. The y=1 slice needs its own matched-foot analysis.