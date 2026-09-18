# Rooted B-edge witness-slot saturation and Hamming defect

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

The published order-12, size-32 graph `X_3` remains a mandatory negative control. No all-order or eventual second-extremal theorem is claimed.

## 1. Reassessment

The preceding scalar synthesis showed that globally replacing complementary-pair slack by total `S=E_U+L_A` leaves too much room. A first attempt in this session was therefore to localize the matched-B channel further by complementary gamma pairs. That does give a valid pairwise refinement, but its aligned-code radius has a large zero-slack baseline and a conservative finite test does not improve the forced-`f` region. The more useful object is one level earlier in the rooted structure: **criticality of the rooted triangle edges themselves**.

Every edge of `G[B]` lies in a triangle with the root `v`. Edge criticality therefore injects the rooted triangle set into the set of missing `B--A` incidences. The unused incidences are not merely bounded by the old residual variable `r`: they are **exactly** `r`. This gives a direct combinatorial meaning to

`delta=r-f`,

explains the saturation mechanism of the `12/32` exception, and yields a new Hamming-energy lower bound on `r` that prices the direct A-edge channel before any global channel maximization.

## 2. Rooted witness slots

Let `v` be the live maximum-degree root, with

- `B=N(v)`, `b=|B|`;
- `A=V\N[v]`, `a=|A|`;
- `Q=e(G[B])`;
- `f=e(G[A])`.

For `z in A`, put `epsilon_z=b-d(z)` and `L_A=sum_{z in A} epsilon_z`.

Define the set of **rooted witness slots**

> `Omega={(x,z) in B x A : xz notin E(G)}`.              `(WS0)`

Since

`sum_{z in A} d(z)=e(A,B)+2f`,

we have

> `|Omega|=ab-e(A,B)=L_A+2f`.                            `(WS1)`

The preserved rooted identity is

> `r+Q=L_A+2f`.                                           `(RQ1)`

Hence already

> `|Omega|=Q+r`.                                          `(WS2)`

The point of the next theorem is that this equality has a direct criticality interpretation.

## 3. Every rooted triangle edge consumes one slot

### Theorem 3.1 — rooted B-edge witness-slot injection

For every edge `xy in E(G[B])`, one can orient the edge, say from source `x` to head `y`, and choose `z in A` such that

> `N(x) cap N(z)={y}`.                                    `(WS3)`

Consequently the map

> `xy -> (x,z)`                                            `(WS4)`

is an injection from `E(G[B])` into `Omega`.

#### Proof

The edge `xy` lies in the triangle `vxy`, so after deleting `xy` the endpoints `x,y` remain at distance two through `v`. Since the graph is D2C, the deletion must destroy a different distance-at-most-two relation. The standard triangle-edge criticality lemma therefore gives an orientation with a vertex `z` satisfying `(WS3)`.

The witness cannot lie in `B`: if `z in B`, then `v` is a second common neighbour of the source `x` and `z`. It cannot be `v` itself, since the damaged pair in the triangle-edge certificate is nonadjacent while `xv` is an edge. Thus `z in A`.

The source is not adjacent to `z`, so `(x,z) in Omega`. A fixed ordered pair `(x,z)` can certify at most one rooted B-edge because its singleton common neighbourhood fixes the head. Hence `(WS4)` is injective. `square`

Choose one such slot for every rooted B-edge and let

> `W subseteq Omega`                                      `(WS5)`

be the image. Then `|W|=Q`. Put

> `Upsilon=Omega\W`.                                      `(WS6)`

### Corollary 3.2 — exact unused-slot interpretation of the residual

> `|Upsilon|=r`.                                          `(WS7)`

Therefore

> `delta=|Upsilon|-f`.                                    `(WS8)`

In particular the second-extremal target `delta>=D_M` is exactly

> `|Upsilon|>=f+D_M`.                                     `(WS9)`

An above-`M(n)` candidate is a graph in which the rooted B-edge criticality assignment leaves **fewer than `f+D_M` unused B--A witness slots**.

This is a structural, rather than purely algebraic, interpretation of the live residual defect.

## 4. Exact saturation is a hypercube-type representation

For `x in B`, define its A-neighbourhood code

> `phi(x)=(1_{xz in E})_{z in A} in {0,1}^A`.             `(HC0)`

This is different from the preserved tight-fibre Boolean code on `A`; it is a new rooted code on `B` whose coordinates are the A-vertices themselves.

### Theorem 4.1 — saturation theorem

If `r=0`, then all of the following hold.

1. `A` is independent, so `f=0` and `delta=0`.
2. Every slot `(x,z) in Omega` satisfies
   
   > `N(x) cap N(z)={y}`
   
   for a unique `y in B`.
3. Every edge `xy in E(G[B])` is separated by exactly one A-coordinate:
   
   > `d_H(phi(x),phi(y))=1`.                              `(HC1)`
4. Hence `G[B]` is bipartite under the parity of `phi`.
5. For every `z in A`, writing `S_z=N_B(z)` and `C_z=B\S_z`, every `x in C_z` has exactly one neighbour in `S_z` inside `B`:
   
   > `d_{S_z}^{G[B]}(x)=1`.                               `(HC2)`

Thus every A-neighbourhood cut is a one-sided perfect-domination cut, and every rooted B-edge crosses exactly one such cut.

#### Proof

If `r=0`, then `W=Omega`, so every B--A nonedge slot is used by a rooted B-edge certificate.

First suppose `yz in E(G[A])`. If some `x in N_B(y)\N_B(z)`, then `(x,z) in Omega` and `y` is already a common A-neighbour of `x,z`. But every slot is used by a rooted B-edge and therefore must have a singleton common neighbourhood whose unique member lies in `B`, contradiction. Hence `N_B(y)=N_B(z)`.

The edge `yz` lies in a triangle because every A-vertex has a B-neighbour and the two B-neighbourhoods are equal. Apply triangle-edge criticality to `yz`. A B-witness is impossible because equal B-neighbourhoods cannot distinguish the source from the head. An A-witness `w` would be adjacent to the head, so `zw` (or `yw`) is another A-edge; the preceding paragraph then gives `N_B(w)=N_B(y)=N_B(z)`. The source and witness would therefore share a B-neighbour, contradicting their required unique common neighbourhood. Thus no A-edge exists. This proves (1).

Statements (2)--(3) follow from bijectivity `E(B) <-> Omega`: a used slot separates the source and head, so every B-edge has at least one separating A-coordinate. If a second A-vertex also separated the same edge, its corresponding slot would have the same edge forced by its unique common neighbour, contradicting the bijection. Hence the Hamming distance is exactly one. Parity gives (4). Finally each `x in C_z` is a used slot with witness `z`, so its unique common neighbour with `z` is exactly one B-neighbour in `S_z`, giving (5). `square`

### Corollary 4.2 — the published `X_3` mechanism

At the canonical root of the published order-12 graph,

`a=3`, `b=8`, `Q=12`, `r=f=0`.

The map `phi:B->{0,1}^3` is bijective, and `G[B]` is exactly `Q_3`; the three A-vertices are the three coordinate-zero faces. Thus the published exception is an **exact witness-slot saturation model**: all twelve B--A nonedges are consumed by the twelve cube edges, one coordinate per edge.

This explains the exception in the same variables used by the eventual programme rather than treating it as an unrelated small graph.

## 5. Near-saturation identities

Keep the chosen injection `W` and unused slots `Upsilon` for arbitrary `r`.

For `(x,z) in Omega`, define

> `c_B(x,z)=|N(x) cap N(z) cap B|`,
>
> `c_A(x,z)=|N(x) cap N(z) cap A|`.                       `(COL0)`

Every used slot has

> `c_B=1`, `c_A=0`.                                       `(COL1)`

Define the rooted B-edge A-Hamming mass

> `H_B=sum_{xy in E(B)} |N_A(x) triangle N_A(y)|`,        `(HB0)`

and the A-edge B-asymmetry mass

> `H_A=sum_{yz in E(A)} |N_B(y) triangle N_B(z)|`.        `(HA0)`

### Theorem 5.1 — exact collision identities

> `H_B=Q+sum_{(x,z) in Upsilon} c_B(x,z)`,                `(HB1)`
>
> `H_A=  sum_{(x,z) in Upsilon} c_A(x,z)`.                `(HA1)`

#### Proof

For `(HB1)`, count triples `(xy,z)` where `xy` is a B-edge and `z in A` is adjacent to exactly one endpoint. Such a triple is equivalently a slot `(x,z)` together with a common B-neighbour `y`, so the total is `sum_Omega c_B`. Used slots contribute exactly one each by `(COL1)`, giving `(HB1)`.

For `(HA1)`, count triples `(yz,x)` where `yz` is an A-edge and `x in B` is adjacent to exactly one endpoint. Equivalently, orient the A-edge toward the nonadjacent endpoint `z`; then `(x,z) in Omega` and the other A-endpoint is a common A-neighbour. Thus the total is `sum_Omega c_A`. Used slots have `c_A=0`, yielding `(HA1)`. `square`

### Corollary 5.2 — quantitative hypercube stability

In the live partial-Boolean branch every A-vertex has at most `p+u` B-neighbours. Therefore

> `H_B-Q <= r(p+u)`.                                      `(HB2)`

So if `r` is small, the rooted B-edge representation is close, in total edge-Hamming mass, to the exact hypercube model `d_H=1`.

## 6. A-edge Hamming energy forces unused slots

In the live partial-Boolean branch an A-vertex has

> `d_A(z)=p+u-epsilon_z-d_U(z)`.

Hence

> `d_A(z)<=K_A:=min(p+u,a-1)`.                            `(KA)`

Using `(HA1)`, every unused slot has `c_A(x,z)<=d_A(z)<=K_A`, so

> `H_A<=r K_A`.                                           `(HA2)`

Let `c(z) in {0,1}^p` be the preserved tight-fibre Boolean code on `A`. For an A-edge `yz`, differing in `h=d_H(c(y),c(z))` tight coordinates changes two matched endpoints per coordinate, so

> `|N_B(y) triangle N_B(z)| >= 2h`.                       `(HAM0)`

Define the A-edge tight-code Hamming energy

> `J_A=sum_{yz in E(A)} d_H(c(y),c(z))`.                  `(HAM1)`

### Theorem 6.1 — residual Hamming-energy bound

> `r K_A >= H_A >= 2J_A`.                                 `(HAM2)`

Equivalently,

> `r >= ceil(2J_A/K_A)`                                  `(HAM3)`

when `K_A>0`.

This prices **all** A-edges according to how far they move in the tight Boolean cube, before any criticality-channel split is used.

### Corollary 6.2 — direct A-edges are residually expensive

Let `D` be the number of direct A-edges. A direct A-edge has complementary tight codes, hence Hamming distance `p`. Therefore

> `r K_A >= 2pD`,                                         `(DIR-R)`

and

> `D <= K_A r/(2p)=K_A(f+delta)/(2p)`.                   `(DIR-C)`

This is independent of the previous direct-fan slack inequalities.

## 7. Forced non-direct traffic

Let `P_B` and `C` be the matched-B and A/U witness channels, so

> `f=D+P_B+C`.                                             `(CH)`

Combining `(DIR-C)` with `r=f+delta` gives

> `P_B+C`
> ` >= [((2p-K_A)f-K_A delta)/(2p)]_+`.                  `(ND1)`

Now use the exact residual split

> `f=G-delta`,
>
> `G=(p-lambda)(p+u)+q+E_U`.                              `(ND2)`

The delta terms collapse:

### Theorem 7.1 — residual-to-nondirect demand

> `P_B+C`
> ` >= [(1-K_A/(2p)) G-delta]_+`.                        `(ND3)`

For an above-`M(n)` candidate,

> `P_B+C`
> ` >= [(1-K_A/(2p))((p-lambda)(p+u)+q+E_U)`
> `      -(D_M-1)]_+`.                                    `(ND4)`

Thus a small residual defect cannot be paid predominantly by direct A-edges whenever `K_A<2p`: a definite part of the rooted-triangle-forced A-edge mass must enter the matched-B or A/U witness channels.

This is the first direct bridge from the **unused rooted B-edge witness slots** to the existing complete non-direct criticality machinery.

For comparison, the preserved capacities imply, for `lambda>=0`,

> `P_B<=a R_A(L_A)`,
>
> `(lambda+1)C<=R_code(S)S`.                              `(ND5)`

Hence every survivor also obeys the actual-slack feasibility inequality

> `[(1-K_A/(2p))G-delta]_+`
> ` <= aR_A(L_A)+R_code(S)S/(lambda+1)`.                 `(ND6)`

The useful feature of `(ND6)` is not a global scalar closure; it is that the direct channel has already been removed by residual geometry before the matched/A-U pair allocation is optimized.

## 8. External eventual reduction: a C5 is mandatory

A relevant published result should now be treated as part of the strategic boundary. Qiao Lin and Xiaolin Wang, *Discrete Applied Mathematics* 375 (2025), 332--337, DOI `10.1016/j.dam.2025.06.025`, prove that for sufficiently large `n`, every **C5-free** D2C graph with at least

`floor((n-1)^2/4)+1`

edges is complete bipartite.

Therefore any sufficiently-large **non-bipartite** survivor at or above the live second-extremal threshold must contain a `C5`. The current live branch is already triangle-containing, so an eventual counterexample to the desired classification would have to contain **both a triangle and a C5**.

This does not solve the branch: the `X_3` negative control itself has the saturation mechanism above and contains odd-cycle structure compatible with the small-order exception. But it removes C5-free triangle-containing graphs from the eventual target and strengthens the case for studying the rooted witness-slot/hypercube stability together with odd-cycle structure.

## 9. Audit

The companion checker independently tests the witness-slot identities on every graph-atlas D2C isomorphism class through order seven and every maximum-degree root, and separately reconstructs `X_3`.

Recorded results:

- 21 D2C graph-atlas classes through order seven;
- 50 maximum-degree roots;
- 14 rooted B-edges checked for A-witness certificates;
- 91 B--A nonedge slots;
- 77 unused slots in total;
- 27 saturated (`r=0`) roots;
- zero failures of `(HB1)`, `(HA1)`, the saturation consequences, or the `X_3` reconstruction;
- `X_3`: `Q=12`, `|Omega|=12`, `r=0`, `H_B=12`, `H_A=0`.

The finite checks are audit support only. The promoted claims are the hand arguments above.

## 10. Strategic consequence

The residual variable is no longer just a numerical remainder. It counts **unused rooted triangle criticality slots**. The two important regimes are now:

1. **near saturation:** `r` small forces `G[B]` toward a hypercube-like A-cut representation and forces A-edges to have low tight-code Hamming energy;
2. **large Hamming/direct mass:** `(HAM2)--(ND4)` converts it into unused slots and therefore into residual defect, forcing the remaining A-edge demand into matched-B/A-U channels.

The next high-value move is to combine `(ND4)` with the existing complementary-pair capacities **without globalizing the pair slack**, and separately to exploit the Lin--Wang C5 reduction inside the near-saturation hypercube regime. The published `X_3` graph should be kept as the exact `r=0` hostile model throughout.