# High-demand star: criticality forces quadratic pair-deficit slack

23 September 2026. Status: **proved internal graph-structural lemma**, conditional on the assigned-witness obstruction already reduced from the exact-H interface. It uses actual diameter-two-criticality of B-edges; it is not an abstract profile statement.

Fix a maximum-degree root `v`, write `B=N(v)`, `A=V\(B union {v})`, `Delta=|B|`, `rho=2Delta-n`, and `delta_z=Delta-d(z)`. Fix one demand-positive label `i in A` in an exact-H attaining assigned-witness graph `W*`. Let

- `T=N_{W*}(i) subset B`, `x=|T|`;
- `h=h_i`, so `i` misses exactly `h` vertices of `B`;
- `R=N_G(i) intersect A`, so `|R|=h-delta_i` (because `d_B(i)=Delta-h` and `d(i)=Delta-delta_i`);
- `C=N_G(i) intersect B`, `|C|=Delta-h`;
- `M=B minus C`, so `|M|=h` and `T subset M`;
- `Z=A minus (R union {i})`.

For every `t in T`, its assigned certificate has a source `u_t in C` and

`N(i) intersect N(t)={u_t}`.

Hence `t` is adjacent to exactly one vertex of `C`, to no vertex of `R`, and of course to the root `v`. Its only remaining possible neighbours lie in `(M minus {t}) union Z`.

Define the pair-deficit slack

`epsilon_t = delta_i+delta_t-(rho+1) >= 0`.

## Lemma 1: exact slack interpretation

`epsilon_t` is exactly the number of non-neighbours of `t` inside

`(M minus {t}) union Z`.

Proof. The allowed set has size

`(h-1)+|Z| = (h-1)+(a-1-(h-delta_i)) = a+delta_i-2`,

where `a=|A|=n-1-Delta`. The degree of `t` already contains `v` and the unique source `u_t`, so it has exactly

`Delta-delta_t-2`

neighbours in the allowed set. Their difference is

`a+delta_i-2-(Delta-delta_t-2)
 = delta_i+delta_t-(Delta-a)
 = delta_i+delta_t-(rho+1)`.

QED.

Thus equality in the old pair-deficit inequality means that a witness endpoint is universal on every locally allowed vertex.

## Lemma 2: every B-edge inside T needs a Z-certificate

Let `tt'` be an edge of `G[T]`. Because `G` is diameter-two-critical, deleting `tt'` must destroy all paths of length at most two for a pair involving one endpoint of the deleted edge. Equivalently, one orientation has a certificate vertex `z` adjacent to one of `t,t'`, nonadjacent to the other, with the adjacent endpoint as their unique common neighbour.

Such a `z` cannot lie in `B`: both `z` and the nonadjacent endpoint are neighbours of the root `v`, which would give an additional common neighbour. It cannot be `i` or lie in `R`, since the defining witness relation for every member of `T` makes every vertex of `R union {i}` nonadjacent to every `t in T`. Therefore every B-edge inside `T` has a critical certificate `z in Z`.

For a fixed `z in Z`, write `S_z=N(z) intersect T`, `k_z=|S_z|`, and `l_z=x-k_z`. If `z` certifies an oriented edge `tt'` with `t` nonadjacent to `z` and `t'` adjacent, then `t` has **exactly one** neighbour in `S_z`, namely `t'`; otherwise another member of `S_z` would be a second common neighbour of `t,z`. Consequently a fixed `z` can certify at most one T-edge for each vertex of `T minus S_z`, hence at most `l_z` edges of `G[T]`.

## Theorem: quadratic star-slack bound

For the `x` assigned witnesses of label `i`,

`sum_{t in T} epsilon_t >= binom(x,2)`.

Proof. Let `e=e(G[T])`. Let

- `alpha` be the number of ordered missing incidences from `T` to `T minus {t}`. Then `alpha=2(binom(x,2)-e)`.
- `beta` be the number of missing incidences between `T` and `Z`, so `beta=sum_{z in Z} l_z`.

By Lemma 1, every such missing incidence is counted among the `epsilon_t`, therefore

`sum epsilon_t >= alpha+beta`.

By Lemma 2 and the capacity bound for each `z`, every one of the `e` B-edges of `G[T]` must be certified by some `z in Z`, while `z` can certify at most `l_z` of them. Hence

`e <= sum_z l_z = beta`.

Therefore

`sum epsilon_t >= 2(binom(x,2)-e)+beta
                  >= 2 binom(x,2)-e
                  >= binom(x,2)`.

QED.

Equivalently,

`x delta_i + sum_{t in T} delta_t
 >= x(rho+1)+binom(x,2)`.

This is strictly stronger than summing the old edgewise pair-deficit inequalities, which supplied only the first term on the right.

A coarse but sometimes useful corollary for the total degree-deficit budget `D` is

`D >= rho+1+(x-1)/2`,

because `xD` is at least the left side. With integrality one may take the ceiling of the right side.

## Why this attacks the remaining concentration

The assigned-witness cover reduction left a star-like loophole: one label could carry many assigned certificates while the witness graph had matching number one. The new theorem shows that such a star is not free. Its D2C edge-criticality forces **quadratically many units of pair-deficit slack** across the centre/endpoints before that slack is collapsed back to the global `D` budget.

The mechanism is genuinely graph-realizability based. If all pair-deficit inequalities were tight, each witness endpoint would be universal on `(M minus {t}) union Z`; then `T` would be a clique whose B-edges have no possible critical `Z`-certificate, contradicting diameter-two-criticality as soon as `x>=2`.

## Bounded scalar stress

An independent fresh greedy-deletion D2C screen was run while deriving this lemma: 2,000 graphs on orders 17--36 (seeds 1000--1099) yielded 154 live-strip maximum-root states. The largest single-label graph-level margin `2s_i-h_i` was 8 and the largest exact Hall envelope was 8. A second disjoint 1,440-graph batch (orders 17--34, seeds 2000--2079) produced 131 live-strip root states; its largest single-label margin was 9. These generated graphs are far from the strict-counterexample deficit budget, so the nonappearance is diagnostic only and is **not** used in the theorem.

A scalar feasibility check using only the new star-slack inequality plus the strict deficit budget excludes a single-label demand 15 at all live-strip parameter rows through `n=25`, but permits abstract rows from `n=26` onward. Thus this lemma is a real structural strengthening but not a standalone closure of `H<15`.

## Next target

Do not collapse the quadratic slack immediately to the coarse global bound `D >= rho+1+(x-1)/2`. Instead retain

`sum_{t in T} epsilon_t >= binom(x,2)`

inside a multi-label exact-H obstruction. Assigned physical edges are disjoint, while high-demand centres may share supplement endpoints. The next useful question is whether quadratic star slacks from several demand-positive labels can be charged with bounded multiplicity to the global degree-deficit budget, or whether overlap itself creates an additional crossed-certificate charge. That is the shortest route from this lemma toward `H<15`.
