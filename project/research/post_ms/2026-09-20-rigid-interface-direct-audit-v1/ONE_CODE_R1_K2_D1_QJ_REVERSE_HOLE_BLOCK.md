# Residual-one k=2 reverse-D1 hub-spoke hole block

Date: 2026-09-20

Status: **same-session hostile replay and strengthening** of `ONE_CODE_R1_K2_D1_QJ_SPOKE.md`, conditional on `J2=empty`. No finite scan is used.

## 1. Hostile replay of the D1 q_j dichotomy

Let `t` be W_s-free with `N_K(t)={a}` and suppose `tq_j` is an edge.

At `J2=empty`, `N_A(q_j)=K={a,b}`.

- In the orientation whose A-witness is adjacent to q_j, a is unavailable because `ta` is an edge, so b is forced. This gives `N(t) cap N(b)={q_j}` and therefore `N_Y(t)=empty` and `E(t,R)=empty` for the K-heavy reservoir R.
- In the opposite orientation the A-witness is adjacent to t and nonadjacent to q_j. K is unavailable; Y is impossible because every Y-vertex has the two extra common neighbours a,b with q_j. Hence the witness is a matched head `h_i in H`, giving `N(q_j) cap N(h_i)={t}`.

No missing A-location or orientation was found in this replay.

## 2. Reverse spokes create an almost-complete H--D1 hole rectangle

Let T be the set of all D1 vertices adjacent to q_j. Split

`T=T_F disjoint_union T_R`

by the two orientations above, and write

`tau=|T|`, `v=|T_R|`.

For each reverse vertex `t in T_R`, choose its forced matched head `h(t)` with

`N(q_j) cap N(h(t))={t}`.                                `(DR-SING)`

The map `t -> h(t)` is injective: one fixed graph pair `(q_j,h_i)` has one common-neighbour set and therefore cannot have two different singleton heads.

Now every vertex `t' in T` is adjacent to q_j. Therefore `(DR-SING)` forces

`h(t)t' notin E`

for every `t'!=t`. Consequently the v distinct matched heads `H_R={h(t):t in T_R}` have at most the v matching edges to T and miss every other pair:

> **`Z_{H_R,T} >= v(tau-1)`.**                            `(DR-RECT)`

This is a located H--U hole block. It is quadratic whenever both v and tau are linear.

There is a second disjoint block. The residual hub q_j is adjacent to both selected witnesses `z_a,z_b`. Hence `(DR-SING)` also forces every `h(t)` to miss both selected witnesses. Thus

> **`Z_{H_R,W_s} >= 2v`.**                                `(DR-WS)`

## 3. Forward/reverse population tradeoff

Every forward vertex in `T_F` is Y-anticomplete and anticomplete to R. Therefore the q_j-neighbour population alone contributes the following disjoint located defects:

> **`Z_Y >= |T_F| y`,**
>
> **`M_U >= |T_F| r`,**
>
> **`Z_X >= v(tau-1)+2v`**                               `(DR-BILL)`

from these three blocks, before any sector-deficit or U-slack price is added.

Thus a large D1 q_j-neighbour population cannot remain cheap in both orientations simultaneously:

- many forward vertices pay Y and K-heavy cross holes;
- many reverse vertices create an almost-complete H--T missing rectangle.

The remaining genuinely permissive D1 endpoint must therefore either have many q_j-nonneighbours, or a highly unbalanced q_j-neighbour orientation split. Both are now explicit located-hole alternatives for the exact rooted ledger.

## 4. Next move

Retain three D1 counts: q_j-nonneighbours, forward q_j-neighbours, and reverse q_j-neighbours. Combine `(DR-BILL)` with the exact D1 sector identity `alpha+beta+gamma=p-3+epsilon` and the K-heavy exception conservation. The next optimization should determine whether the D1 population can still realize the additive coefficient `(7-sqrt(33))/8`; if not, the global low-k coefficient rises again. If the optimizer concentrates on q_j-nonneighbours, attack those vertices by their missing residual-hub edge and private-coordinate criticality rather than returning to aggregate slack.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; this remains conditional downstream mathematics pending independent hostile replay.