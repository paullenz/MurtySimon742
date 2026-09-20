# Residual-one k=2 heavy-reservoir exception budget

Date: 2026-09-20

Status: **same-session candidate continuation**, conditional on the residual-one hub and k=2 orientation-covering packages plus `ONE_CODE_R1_K2_HEAVY_RESERVOIR_CAPACITY.md`. It is not a graph-level closure.

The heavy-only theorem shows that saturated K-heavy/W-heavy reservoirs acquire quadratic cost. This note asks exactly what kind of exceptional escape can repair that edge-criticality capacity.

## 1. Only K-free U-vertices can repair a K-heavy internal-edge certificate

Let R be a set of K-heavy escapes, `|R|=r`. For an oriented edge `w e` inside R, a certificate has the form

`N(w) cap N(t)={e}`

with t adjacent to e and nonadjacent to w.

The heavy-reservoir theorem already classified the native witnesses: an H-head or a private endpoint `q_i`, in either case tied to an H-nonneighbour of w.

Suppose instead that t is another U-vertex. If t has **any** neighbour in `K={a,b}`, then that K-neighbour is also adjacent to w, because w is K-heavy. It is therefore an extra common neighbour of w and t, contradicting the singleton equation.

Hence:

> **Any U-vertex used as an exceptional witness for a K-heavy--K-heavy edge is K-free.** `(EX-KFREE)`

Let F be the set of K-free non-W-heavy escape vertices which can supply such exceptional certificates, and put `f=|F|`. (A W-heavy vertex cannot certify a K-heavy edge because the predecessor theorem makes the two heavy sides anticomplete.)

For a fixed source w and a fixed exceptional witness t, the singleton `N(w) cap N(t)` determines at most one head e. Therefore F restores at most f outgoing internal-edge certificates at each K-heavy source.

## 2. The same exceptional class is the only way to give a K-heavy vertex many Y-neighbours

Fix K-heavy w and an edge `wy`, `y in Y`.

If a U-vertex t appears in either singleton orientation and t has a K-neighbour, then w or y shares that K-neighbour with t: w is complete to K and every Y-vertex is complete to X, hence to K. Thus a U-witness for `wy` must again be K-free.

The heavy-reservoir proof showed that an H-witness is possible only when y is the **unique** Y-neighbour of w. Consequently, if `d_Y(w)>=2`, every edge from w to Y must use a K-free exceptional U-witness. A fixed physical witness t can certify at most one such edge for the fixed source w.

Therefore

> **`d_Y(w)<=max{1,f}` for every K-heavy w.**             `(EX-YCAP)`

The W-heavy vertices do not enlarge f for this purpose: they are Y-anticomplete and K-heavy/W-heavy anticomplete.

## 3. Edge-capacity inequality with f exceptional K-free witnesses

For `w in R`, write

`alpha_w=|H\N(w)|`,

`beta_w=|(R\{w})\N(w)|`.

Let

`A=sum alpha_w`, `B=sum beta_w`,

`E_R=sum_{w in R} epsilon_w`,

`eta=sum_{w in R} d_Y(w)`.

The exact degree identity, with all additional nonneighbours outside R simply discarded in the favourable direction, gives

> `B <= E_R+eta-r-A`.                                    `(EX-B)`

Every edge of `G[R]` must be oriented to one endpoint. Native H/q_i certificates provide at most `2A` orientations, while F adds at most `rf`. Thus

`e(R)<=2A+rf`.                                            `(EX-EUP)`

On the other hand

`e(R)=binom(r,2)-B/2`.

Combining with `(EX-B)` gives the physical exception-budget inequality

> **`E_R+3A >= r^2-eta-2rf`.**                            `(EX-MAIN)`

Using `(EX-YCAP)`:

- if `f=0`, then `eta<=r` and

  > **`E_R+3A >= r(r-1)`;**                              `(EX-0)`

- if `f>=1`, then `eta<=rf` and

  > **`E_R+3A >= r(r-3f)`.**                            `(EX-F)`

Thus a small exceptional K-free set cannot repair a quadratic K-heavy reservoir for free.

## 4. Score interpretation

The quantity A is not bookkeeping-only: every H--R nonedge counted by A is an additional X--U hole. In the exact rigid identity

`2e_X=x g0-L_X+Z_X`,

those holes raise the X-slack floor one-for-one once the predecessor upper bound on `e_X` is retained. Meanwhile `E_R` is literal U-slack.

Hence the two terms in `(EX-MAIN)` live in the score on disjoint physical sides. A coarse but safe consequence when `f>=1` and `r>3f` is

> **`E_R+A >= r(r-3f)/3`.**                              `(EX-SCORE)`

For `f=0`, the heavy-only theorem is stronger and should be used instead.

Every vertex of F is also K-free, so F itself contributes at least `2f` additional X--U nonedges beyond the selected-witness baseline. This is only a linear price and is not, by itself, enough to close the low-k ray.

## 5. Strategic consequence

The remaining escape from the heavy-reservoir quadratic theorem is now much more specific:

> a large family of **K-free, non-W-heavy** U-vertices must be present if one wants to restore enough witness capacity to a large K-heavy reservoir without paying the quadratic term in `(EX-F)`.

Mixed escapes touching both K and W_s do **not** provide this repair: they already pay `epsilon_w>=p+1`, and because they have a K-neighbour they fail `(EX-KFREE)`.

So the next raw-criticality target is no longer an arbitrary mixed exception. It is the **K-free deficient W-side escape**: a vertex with no K-neighbour and fewer than two W_s-neighbours, especially one that also has Y-neighbours or is used to certify K-heavy internal edges.

A useful next theorem would show that such K-free deficient vertices either have large slack / large X-hole cost, or have too little adjacency to serve many K-heavy edge certificates. That is the exact missing bridge from the heavy-only quadratic bill to the full low-k ray.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; the present argument is conditional downstream mathematics.