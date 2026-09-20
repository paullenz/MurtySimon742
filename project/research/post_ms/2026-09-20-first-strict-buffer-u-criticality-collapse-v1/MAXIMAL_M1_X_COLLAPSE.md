# Internal-X collapse in the maximal-selection one-witness branch

Date: 2026-09-20

Status: internal conditional structural theorem. Assumptions: maximal-witness selection, surviving m=1 all-F polarization, `y>=2`, and the independently audited same-code raw-criticality theorem.

By `MAXIMAL_SELECTION_GENERIC.md`, `U_o={z}`. By head saturation, `g in {0,1}`, every vertex of `X'=X\{a_0}` is the unique X-head of one core vertex, and when `g=0` the remaining core vertex has head `a_0`.

## 1. X' is independent

All vertices of `X'` have the same code C. Suppose `x_1x_2` is an edge in `G[X']`. The independently audited same-code theorem requires a witness of complementary code `bar C` in `A union U`.

In the present geometry:

- the only U-vertex of code `bar C` is z, and z is anticomplete to all of A, so it is not adjacent to the A-head of either orientation;
- the only possible A-vertex of code `bar C` is `a_0` (this can occur only when `S_0={i_0}`), but `a_0` and either X'-source share every vertex of the nonempty set Y as common neighbours. Hence `a_0` cannot give a singleton common neighbourhood with an X'-source.

No valid complementary-code witness exists. Therefore

> `G[X']` is edgeless.                                  `(M1-XP-INDEP)`

## 2. a0 has at most one X' neighbour

Suppose `a_0x in E` for `x in X'`. The edge lies in triangles through Y. Exhaust raw criticality.

### Source x, head a0 is impossible

- an A-witness in X shares all Y with x; a Y-witness is adjacent to x;
- z is not adjacent to a0; b is not adjacent to a0;
- a core witness with head a0 can occur only when g=0, but its `bar d` code shares tight matched neighbours with the C-source x;
- a matched witness distinguishing x from a0 either has b as an extra common neighbour (at `i_0`) or has Y as extra common neighbours (at any other differing coordinate).

Thus this orientation fails.

### Source a0, head x

A U-witness b or a core head of x shares a tight matched neighbour with a0 on the nonempty support `S_0`; z is not adjacent to x. An A-witness is excluded by the complete X--Y cut / X' independence.

A matched witness can work only at a coordinate `j notin S_0` (necessarily `j!=i_0`), where x selects the `bar d` endpoint and a0 selects d. That matched endpoint is adjacent to **every** X' vertex. Hence its common neighbourhood with a0 contains every X'-neighbour of a0. It can single out x only when x is the unique such neighbour.

Therefore

> `d_{X'}(a_0)<=1`.                                    `(M1-A0-XDEG)`

## 3. The g=0 case has no internal X-edge at all

When `g=0`, the k=x injective core heads cover all of X, so there is a unique core vertex `c_0` with head a0. For the only remaining possible matched orientation above, the matched `bar d` endpoint is also adjacent to `c_0`, while `a_0c_0 in E`. Thus `c_0` is an extra common neighbour and even the unique-X'-neighbour certificate fails.

Hence

> `g=0 => G[X] is edgeless`.                            `(M1-X0)`

When `g=1`, there is no core head at a0 and at most one edge `a_0x` can remain. Uniformly,

> `e(X)<=g<=1`.                                         `(M1-XEDGE)`

This is a graph-level structural collapse, not a score relaxation.

## 4. Exact X-score consequence

Put `t=e(X)`; by the theorem `0<=t<=g`. Every `x in X'` has exactly two U-neighbours: b and its unique core head. It is adjacent to all y vertices of Y and, since X' is independent, possibly only to a0 inside X. Therefore

`sum_{x in X'} epsilon_x=(x-1)(p+k-y)-t`.

The vertex a0 has U-degree `1-g` (its core head when g=0 and none when g=1), A-degree `y+t`, and hence

`epsilon_{a_0}=p+k+1+g-y-t`.

Thus

> `E_X=(x-1)(p+k-y)+p+k+1+g-y-2t`,                    `(M1-EX)`

with `t<=g`. In particular the score-minimizing possibilities are literal: `t=0` for g=0 and `t=1` for g=1.

Combined with the exact U-ledger and exact Y-degree (`Y--U` empty, so `epsilon_y=p-g+2`), the maximal-selection m=1 y>=2 branch now has a nearly complete degree ledger. The remaining uncertainty is only whether the single possible a0--X' edge exists in the g=1 case.
