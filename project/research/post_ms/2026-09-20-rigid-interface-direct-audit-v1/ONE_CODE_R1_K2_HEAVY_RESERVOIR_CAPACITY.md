# Residual-one k=2 heavy-reservoir capacity

Date: 2026-09-20

Status: **same-session candidate structural theorem**, conditional on the residual-one hub package and the predecessor k=2 one-sided/heavy normal form. No finite scan is used as proof. Rigid-interface reachability remains unresolved and the 20 September daily red-team gate remains binding.

This note attacks the remaining cheap `k=2` endpoint by raw criticality of the heavy reservoir itself. The main conclusion is that the predecessor scalar equality endpoint is not physically cheap: a heavy-only escape reservoir already carries a quadratic slack bill, and its K-heavy side is almost anticomplete to Y.

## 1. Setup and hostile replay of the predecessor heavy theorem

Let

`K={a,b}`, `W_s={z_a,z_b}`, `E=U\W_s`.

The beta map swaps a and b. Thus

`N_A(z_a)={a}`, `N_A(z_b)={b}`,

`N_Y(z_a)=N_Y(z_b)=empty`.

Call an escape

- **K-heavy** if it is complete to K and anticomplete to W_s;
- **W-heavy** if it is complete to W_s and anticomplete to K.

The predecessor theorem `ONE_CODE_R1_K2_HEAVY_ENDPOINT_CRITICALITY.md` was replayed directly before the arguments below. Its orientation exhaustion survives: for a W-heavy w and h in K,

`N(w) cap N(h)={z_h}`,

so every W-heavy escape is Y-anticomplete and every W-heavy/K-heavy pair is a nonedge.

The arguments below use only these literal consequences, the complete X--Y cut, the private matched endpoints `q_i`, and raw D2C edge criticality.

## 2. K-heavy escapes have at most one Y-neighbour

Assume the escape reservoir is one-sided heavy: every escape is K-heavy or W-heavy. Fix a K-heavy escape w and suppose `wy` is an edge for some `y in Y`.

The edge `wy` has at least the two common neighbours a,b, so the edge itself cannot be the direct critical pair. Raw edge criticality therefore needs one of the two singleton orientations.

### Orientation with source y is impossible

A witness r adjacent to w and nonadjacent to y with

`N(y) cap N(r)={w}`

cannot exist:

- an X-vertex is adjacent to y because X--Y is complete;
- a Y-vertex shares all of X, in particular a,b, with y;
- a K-heavy escape shares a,b with y;
- a W-heavy escape is nonadjacent to w by the predecessor heavy theorem;
- a selected witness is nonadjacent to w;
- a private endpoint `q_i` has the common X-head `h_i` with y;
- the residual endpoint `q_j` has the common K-heads a,b with y;
- the root is not adjacent to w.

### The other orientation can only use H

Now let r be adjacent to y and nonadjacent to w with

`N(w) cap N(r)={y}`.

The root fails because w has the additional A-neighbours a,b. K fails because w is K-heavy. Another Y-vertex or a K-heavy escape again creates the common pair a,b; W-heavy escapes and selected witnesses have no Y-neighbours; no `q_i` is adjacent to Y. Hence r must lie in H.

But every H-vertex is adjacent to every Y-vertex. Therefore `N(w) cap N(r)` contains **all** Y-neighbours of w. For it to be the singleton `{y}`, w can have only one Y-neighbour.

> **K-heavy Y-degree lemma:**
>
> `d_Y(w)<=1` for every K-heavy escape in a heavy-only reservoir. `(HR-Y1)`

Consequently, if there are `r_K` K-heavy and `r_W` W-heavy escapes,

> `Z_{Y,E} >= r_W y + r_K (y-1)`                       `(HR-ZY)`

located Y--escape nonedges, in addition to the already-known selected-witness holes `2y`.

## 3. Criticality of a K-heavy--K-heavy edge has only H/q_i witnesses

Let w,e be adjacent K-heavy escapes. They share a,b, so direct criticality is impossible. Orient the edge from source w, so a witness r must be adjacent to e, nonadjacent to w and satisfy

`N(w) cap N(r)={e}`.

The possibilities exhaust as follows.

- K and another K-heavy escape fail because of the common pair a,b.
- Y fails for the same reason.
- W-heavy escapes are anticomplete to e.
- selected witnesses are anticomplete to e.
- `q_j` fails because a,b are common neighbours with w.
- the root is not adjacent to e.
- an H-head `h_i` is possible only if `w h_i` is a nonedge;
- a private endpoint `q_i` is possible only if `w h_i` is a nonedge, since otherwise `h_i` is an extra common neighbour of w and `q_i`.

Thus every oriented K-heavy internal edge consumes a private index i for which w misses `h_i`. For fixed source w and fixed i, the witness `h_i` can certify at most one outgoing edge, and the witness `q_i` can certify at most one outgoing edge.

There is a refinement when `d_Y(w)=1`: an H-witness is then impossible, because its unique Y-neighbour is an extra common neighbour of w and every H-head. Therefore, writing

`alpha_w=|H\N(w)|`,

an oriented K-heavy edge sourced at w has capacity at most

`2 alpha_w` if `d_Y(w)=0`,

and at most

`alpha_w` if `d_Y(w)=1`.                                `(HR-KCAP)`

This is an edge-criticality capacity, not a score relaxation.

## 4. All-K-heavy reservoir: quadratic excess slack

First take the pure K-heavy endpoint, with `r=|E|=c-1` and no W-heavy escapes. Put

`eta_w=d_Y(w) in {0,1}`,

`beta_w=|(E\{w})\N(w)|`,

and write `epsilon_w=2+delta_w`, `delta_w>=0`; the universal orientation-covering theorem supplies the floor `epsilon_w>=2`.

The exact U-degree identity

`d_{A union U}(w)=p+u-1-epsilon_w`

and `u=c+1`, together with K-heavy adjacency to a,b and nonadjacency to W_s, give

> `alpha_w+beta_w=1+delta_w+eta_w`.                      `(HR-KDEF)`

Let `E_0,E_1` split the K-heavy escapes by `eta_w=0,1`; put `A_i=sum alpha_w`, `D_i=sum delta_w` on the two parts.

Every internal K-heavy edge must be oriented to one endpoint. By `(HR-KCAP)` the total number of such edges is at most

`2A_0+A_1`.

On the other hand, summing `(HR-KDEF)` gives its exact missing-edge count. Eliminating the missing-edge sum yields

`4D_0+2D_1 >= r(r-1)-4r`.

Hence, with `D=D_0+D_1`,

> **`D >= max{0, ceil(r(r-5)/4)}`.**                    `(HR-KEX)`

Equivalently

> **`sum_{w in E} epsilon_w >= 2r + max{0,ceil(r(r-5)/4)}`.** `(HR-KSLACK)`

In particular the formerly scalar-sharp endpoint `epsilon_w=2` for every K-heavy escape is possible only when

> **`r<=5`, hence `c<=6`.**                              `(HR-KCHEAP)`

Thus an all-K-heavy reservoir cannot realize the old linear-cost equality endpoint at unbounded size.

## 5. W-heavy internal edges are even more rigid

Now let R be the K-heavy set of size r and S the W-heavy set of size s, with no mixed escapes. The predecessor theorem gives `R--S=empty` and `N_Y(S)=empty`.

Fix `w in S`. Write

`alpha_w=|H\N(w)|`,

`beta_w=|(S\{w})\N(w)|`.

The exact U-degree identity gives

> `alpha_w+beta_w=epsilon_w-r-1`.                        `(HR-WDEF)`

For an edge between two W-heavy escapes, direct criticality is impossible because the two vertices have the common neighbours `z_a,z_b`. In an oriented certificate, every possible witness except H fails:

- K and Y are not adjacent to the W-heavy head;
- a K-heavy escape is cross-anticomplete;
- another W-heavy escape has the common pair `z_a,z_b` with the source;
- `z_a,z_b` are adjacent to both endpoints;
- `q_i` also has both `z_a,z_b` as common neighbours with the source;
- `q_j` is absent from every W-heavy escape;
- the root is absent.

Hence an outgoing W-heavy internal edge consumes an H-nonneighbour of its source, and a fixed H-witness can certify only one such edge. Therefore

`e(S)<=sum_{w in S} alpha_w`.

Combining this with the exact missing-edge count from `(HR-WDEF)` yields

> **`sum_{w in S}(epsilon_w-r-1) >= binom(s,2)`.**       `(HR-WCAP)`

Thus

> **`sum_{w in S} epsilon_w >= s(r+1)+binom(s,2)`.**     `(HR-WSLACK)`

For the pure W-heavy endpoint (`r=0`) this is

`sum epsilon_w >= s+binom(s,2)=s(s+1)/2`,

in addition to the universal pointwise floor `epsilon_w>=2`. In particular an all-W-heavy reservoir with every escape at slack two has `s<=3`.

## 6. Heavy-only low-k ray gets simultaneous quadratic prices

On the exact preserved low-k/high-y ray

`c=p=lambda=t`, `y=t-1`, `u=x=t+1`, `k=2`,

one has

`|E|=p-1`.

Let `r+s=p-1` be the K-heavy/W-heavy split. The Y-degree results give, just on the escape reservoir,

`Z_{Y,E} >= s(p-1)+r(p-2)`

`             =(p-1)^2-r`

and hence

> **`Z_{Y,E}>=(p-1)(p-2)`.**                            `(HR-RAY-Z)`

This is disjoint from the selected-witness A--U holes already used in the predecessor rooted-Q floor.

The internal-edge capacity estimates also show that a heavy-only reservoir cannot retain the predecessor's merely linear U-slack cost. A safe split-independent consequence is

> **`E_E >= (p-1)(p-2)/4`**                              `(HR-RAY-E)`

(up to the harmless integral ceiling), obtained from the K-heavy internal-edge capacity together with `(HR-WSLACK)` and minimizing over `r+s=p-1`; the continuous lower envelope is concave in r and is minimized at the pure K-heavy endpoint.

Thus the old scalar equality value `E_E=2(p-1)` is not physically realizable for large p: heavy-only realizations acquire quadratic cost simultaneously in the located Y--U defect and in U-slack.

This does **not** yet close the full low-k ray, because mixed escapes can act as exceptional neighbours/witnesses. They already cost `epsilon_w>=p+1` individually, but an exception-budget version of the present edge-capacity argument is still needed before the heavy-only quadratic bill can be promoted to the whole ray.

## 7. J2=0 residual-hub spoke refinement

At the especially permissive all-radius-one endpoint `J2=empty`, the residual endpoint `q_j` has A-neighbourhood exactly K. If a K-heavy escape w is adjacent to `q_j`, criticality of the B-edge `w q_j` has only one possible type:

- the orientation whose witness is adjacent to `q_j` fails because every such A-witness lies in K and w is complete to K;
- in the opposite orientation, K is excluded by the `q_j` edge, Y creates the common pair a,b, and the witness is forced into H.

Hence there is `h_i in H` with

> `N(q_j) cap N(h_i)={w}`.                               `(HR-JHUB)`

Distinct K-heavy `q_j`-neighbours require distinct H-heads. This does not by itself close the endpoint, but it records the correct next local structure if the exception-budget attack leaves a J2=0 tail.

## 8. Evidence status and next move

The substantive consequences of this note are:

1. hostile replay of the W-heavy forced-orientation theorem passed at its stated conditional scope;
2. K-heavy escapes in a heavy-only reservoir satisfy `d_Y<=1`;
3. internal K-heavy edges can be certified only through H/q_i, with the source-capacity refinement `(HR-KCAP)`;
4. a pure K-heavy reservoir has quadratic excess slack `(HR-KSLACK)`, and the all-slack-two endpoint has `c<=6`;
5. internal W-heavy edges can be certified only through H, giving `(HR-WSLACK)`;
6. on the exact low-k ray, every heavy-only split pays the simultaneous quadratic bills `(HR-RAY-Z)` and `(HR-RAY-E)`;
7. at J2=0, every K-heavy `q_j` spoke injects into H through `(HR-JHUB)`.

The highest-value continuation is now an **exception-budget theorem for mixed escapes**. Each mixed escape already pays `p+1` slack; the issue is to bound how much K-heavy/W-heavy edge-criticality capacity one mixed vertex can restore. If a small exceptional set cannot repair more than linearly many heavy-heavy obligations, the heavy-only quadratic bill will extend to the entire low-k ray and may finally make the rooted residual ledger finite-order.

Global caveat: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; all results here remain conditional on reaching that interface.