# Residual-one k=2 exception orientation conservation

Date: 2026-09-20

Status: **same-session candidate structural continuation**, conditional on the rigid residual-one identities and the preceding k=2 heavy-endpoint / exception-budget packages. No finite scan is used as proof. Rigid-interface reachability remains unresolved, and the 20 September daily red-team gate remains binding.

This note closes a loophole left by the crude exceptional-witness count. A K-free escape that touches even one selected witness cannot repair the K-heavy reservoir at all. After removing those inert exceptions, the remaining U--U singleton certificates for internal K-heavy edges and K-heavy--Y edges share one physical source/witness incidence budget. On the preserved low-k ray this yields a quadratic physical bill for the K-heavy reservoir **independent of how many exceptional witnesses are introduced**.

## 1. Hostile replay of the singleton degree-sum price

For every `z in U`, retain the exact identity

`d_{A union U}(z)=p+u-1-epsilon_z`.                       `(OC-UDEG)`

If nonadjacent `w,t in U` satisfy the literal singleton equation

`N(w) cap N(t)={e}`

with `e in A union U`, then inside `A union U` their neighbourhood union has size at most

`|A|+u-2=x+y+u-2`,

because neither w nor t belongs to either neighbourhood, while their intersection has size one. Hence

`d_{A union U}(w)+d_{A union U}(t)<=x+y+u-1`.

Using `x=p+u-c` gives

> **`epsilon_w+epsilon_t>=p+c-y-1`.**                    `(OC-UU)`

This independently reproduces `(SC-UU)` from the predecessor singleton-cost note. On the exact low-k ray

`c=p=lambda`, `y=p-1`,

it becomes

> **`epsilon_w+epsilon_t>=p`.**                           `(OC-RAY-UU)`

No orientation or code language is used in this degree-sum step.

## 2. A K-free escape touching `W_s` is inert for K-heavy repair

Keep `K={a,b}`, `W_s={z_a,z_b}` and let R be the K-heavy escape set. Thus every `w in R` is adjacent to a,b and anticomplete to `W_s`.

Take an escape t with

`N(t) cap K=empty`

and suppose `t z_h` is an edge for `h in K`.

The already-preserved heavy-endpoint raw-criticality theorem applies without requiring t to be W-heavy. Its reverse orientation is impossible and the forward orientation is forced through h:

> **`N(t) cap N(h)={z_h}`.**                              `(OC-FWD)`

Immediate consequences are:

1. every `Y`-vertex is adjacent to h, so `N_Y(t)=empty`;
2. `q_j` is adjacent to h, so `t q_j` is absent;
3. every K-heavy escape w is adjacent to h, so `t w` is absent.

Therefore:

> **If a K-free escape sees even one selected witness, it is anticomplete to both Y and the entire K-heavy reservoir R.** `(OC-INERT)`

Such a vertex cannot certify a K-heavy internal edge in either U--U orientation because it is not adjacent to the K-heavy head, and it cannot certify a K-heavy--Y edge in either orientation because it is adjacent to neither the K-heavy endpoint nor the Y endpoint.

Consequently every U-witness that actually repairs a K-heavy internal edge or a K-heavy--Y edge must lie in the smaller class

> `F0={t in E : N_K(t)=empty and N_{W_s}(t)=empty}`.      `(OC-F0)`

The K-free deficient vertices with exactly one `W_s` neighbour are not capacity; they are physical defect vertices. If their number is `f1`, they contribute at least

- `y f1` located Y--U nonedges, and
- `r f1` missing U--U pairs between themselves and R.

These blocks should be retained in the rooted ledger rather than hidden in an undifferentiated exception count.

## 3. Internal and Y-edge U--U certificates share one incidence budget

Write

- `r=|R|`, `f=|F0|`;
- `E_R=sum_{w in R} epsilon_w`;
- `E_F=sum_{t in F0} epsilon_t`;
- `A=sum_{w in R}|H\N(w)|`;
- `eta=sum_{w in R} d_Y(w)`.

Let I be the number of K-heavy internal-edge certificates using an exceptional witness in F0 in the U--U orientation

`N(w) cap N(t)={e}`, with `w,e in R`, `t in F0`.

Let `J_U` be the number of K-heavy--Y edge certificates using the U--U orientation

`N(w) cap N(t)={y0}`, with `w in R`, `y0 in Y`, `t in F0`.

For a fixed ordered physical pair `(w,t)`, the set `N(w) cap N(t)` is graph-fixed. Hence the same pair cannot support two different singleton heads, whether the head lies in R or Y. Therefore the I and `J_U` incidences are disjoint source/witness pairs.

Applying `(OC-UU)` to all of them gives

> `(p+c-y-1)(I+J_U) <= f E_R+r E_F`.                     `(OC-IJ)`

On the exact low-k ray, `p+c-y-1=p` and `r,f<=p-1`, hence

> **`I+J_U <= E_R+E_F`.**                                 `(OC-RAY-IJ)`

This is stronger than pricing internal-edge exceptions and Y-edge exceptions separately: they compete for the same physical source/witness incidence reservoir.

## 4. The opposite Y-edge orientation is controlled by X-anticomplete witnesses

For a K-heavy--Y edge, the predecessor criticality exhaustion gives the following safe statement: apart from at most one native Y-edge per K-heavy source, the edge must use an exceptional K-free witness. Thus if `J_X` counts exceptional Y-edge certificates in the opposite orientation, then

> `J_U+J_X >= eta-r`.                                    `(OC-YNEED)`

In the opposite orientation one has

`N(y0) cap N(t)={w}`.

Because every `y0 in Y` is complete to X, this forces

> **`N_X(t)=empty`.**                                     `(OC-X0)`

Let q be the number of distinct witnesses in F0 that are X-anticomplete and are used in such opposite-orientation certificates.

For fixed `(y0,t)`, the singleton `N(y0) cap N(t)` has at most one head w. Hence ordered-pair injectivity at this literal graph level gives

> **`J_X<=y q`.**                                         `(OC-XCAP)`

Combining `(OC-YNEED)` and `(OC-XCAP)` yields

> `eta <= r+J_U+yq`.                                      `(OC-ETA)`

Each of the q witnesses also contributes the full located block of x X--U nonedges. Denote that block size by `Z_X^0`; then

> **`Z_X^0>=xq`.**                                        `(OC-ZX0)`

## 5. Exception-independent quadratic conservation on the low-k ray

The predecessor exception-budget derivation has the exact pre-substitution inequality

> `E_R+3A+2I >= r^2-eta`.                                `(OC-EDGE)`

Now specialize to the preserved low-k ray. Put

`B=E_R+E_F`.

From `(OC-RAY-IJ)`,

`I+J_U<=B`.

From `(OC-ETA)`,

`eta<=r+J_U+yq<=r+B-I+yq`.

Insert this into `(OC-EDGE)`:

`r^2`
` <= E_R+3A+2I+eta`
` <= E_R+3A+2I+r+B-I+yq`
` <= E_R+3A+r+2B+yq`.

Therefore

> **`3E_R+2E_F+3A+yq >= r(r-1)`.**                       `(OC-MAIN)`

This is the main conservation theorem. The exceptional-set size f has disappeared. Adding more K-free witnesses does not remove the quadratic bill: it can only move the cost between

- U-slack on the K-heavy side,
- U-slack on the fully K/W-free witness side,
- H--R X--U holes A,
- or X-anticomplete exceptional witnesses q.

Since on the ray `x=p+1>y=p-1`, `(OC-ZX0)` gives `Z_X^0>=yq`. The A block and `Z_X^0` are pair-disjoint because their U endpoints lie in R and F0 respectively. Thus a coarse but completely physical corollary is

> **`E_R+E_F+A+Z_X^0 >= r(r-1)/3`.**                     `(OC-PHYS)`

No abstract survivor count enters this bound.

## 6. What this removes, and what remains

`(OC-PHYS)` eliminates the main loophole in the predominantly-K-heavy endpoint: a linear-size K-heavy reservoir carries a quadratic physical bill **even after arbitrary K-free exceptional witnesses are admitted**. The predecessor heavy-only theorem no longer needs the assumption that the escape reservoir contains only the two saturated heavy types in order to obtain a quadratic obstruction on R.

The remaining asymptotic escape therefore has to suppress the K-heavy population itself. On the exact low-k ray, any parameter-level family avoiding a quadratic R-bill must move a linear fraction of the `p-1` escape vertices into the non-K-heavy classes. The most permissive unresolved class is now the fully four-hole class F0: K-free and `W_s`-free. The one-selected-witness K-free class is inert and pays the additional Y/R defect blocks in Section 2; mixed vertices already pay `epsilon>=p+1`; W-heavy vertices retain their predecessor Y-anticompleteness and internal-edge capacity bill.

So the next structural target should be the literal F0-dominant geometry, not another optimization of the old heavy-only scalar endpoint. In particular, combine the exact identity

`d_{A union U}(t)=2p-epsilon_t`

on the low-k ray with F0's four forced holes to H/Y/U sector deficits, and apply raw criticality to its incident H, Y and U edges. The objective is either a quadratic bill for a linear F0 reservoir or a small explicit normal form that can be fed back into the rooted Q/residual ledger.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; every result here remains conditional downstream mathematics pending independent hostile replay.