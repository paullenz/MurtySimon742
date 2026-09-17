# Root-edge stability dichotomy beyond the zero-residual boundary

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal hand theorem with small-order regression check; not promoted. External mathematical and novelty review remain open.

## 1. Why this is the right next perturbation

The exact boundary theorem in `ZERO_RESIDUAL_BOUNDARY.md` uses

`F=empty`, `r=0`

to turn every rooted triangle edge into an exact Boolean-coordinate flip. The first perturbative question is not yet how to repair the entire factorial path argument. Before doing that, one should identify exactly how root-edge criticality itself can fail to produce the disjoint-support antipode used in the zero-residual proof.

There is a clean answer: the only alternative is a **private A-neighbour**, and such alternatives are paid for by vertices incident with `F=G[A]`.

This gives a compact dichotomy coupling

- rooted triangle activity `Q=e(G[B])`;
- the residual mass `r`;
- the A-side graph `F`;
- the maximum-degree imbalance `lambda=2b-n`.

It is a stable extension of the root-criticality step used in the 12-vertex / Boolean-flow analysis.

## 2. Setup

Let `G` be a diameter-2-critical graph which is not a star. Choose a maximum-degree root `v` and put

`B=N_G(v)`, `A=V(G)\N_G[v]`,

`b=|B|=Delta(G)`, `a=|A|=n-1-b`.

Let

`F=G[A]`, `f=e(F)`,

and use the canonical complement-root selected/residual system. Thus

`Q=e(G[B])=sum_u q_u=sum_u p_u`,

`r=sum_u rho_u`,

`delta=r-f=b(n-b)-m`,

and

`lambda=2b-n=b-a-1`.

For `u in B`, every H-cross edge from u to A is either selected or residual, so

`h_u:=q_u+rho_u = # {x in A : ux notin E(G)}`.          (2.1)

Call `u in B` **triangle-active** if it has a neighbour in `B`; equivalently, `u` lies in a triangle containing `v`. Let

`T={u in B : d_{G[B]}(u)>0}`.

A vertex `x in A` is **B-private for u** if

`N_G(x) intersect B={u}`.                               (2.2)

## 3. Root-edge antipode-or-private lemma

> **Lemma 3.1.** For every triangle-active `u in T`, at least one of the following holds.
>
> **(P)** `u` has a B-private neighbour `x in A`.
>
> **(A)** there exists `w in B\{u}` such that
>
> `uw notin E(G)` and `N_G(u) intersect N_G(w)={v}`.    (3.1)

### Proof

Delete the critical edge `vu`.

Because `u` is triangle-active, it has some neighbour `y in B`. Hence after deleting `vu`, the vertices `v,u` remain at distance two through `y`. So `(v,u)` itself cannot witness the increase of diameter.

Any path of length at most two that uses the edge `vu` has one of the following endpoint forms:

1. `v` and a neighbour `x` of `u` other than `v`;
2. `u` and a neighbour `w` of `v` other than `u`.

Since deletion of `vu` increases the diameter, at least one such pair loses all length-at-most-two paths.

In case 1, `x` cannot lie in `B`, because then `vx` is still an edge. Thus `x in A`. For `v` and `x` to have distance greater than two after deleting `vu`, no other vertex of `B=N(v)` can be adjacent to `x`. Therefore

`N_G(x) intersect B={u}`,

which is (P).

In case 2, `w in B`. For `u,w` to have distance greater than two after deleting `vu`, they cannot be adjacent, and they can have no common neighbour other than `v`. Hence (A).

This proves the lemma. `square`

### Remark

No selected/residual machinery is used in Lemma 3.1. It is a direct consequence of diameter-2 edge-criticality. The canonical framework enters only when the alternatives are counted.

## 4. Private alternatives are paid for by F

Because `G` is a non-star D2C graph, it has no degree-one vertex. Indeed, if `x` were a leaf with unique neighbour `u`, diameter two would force `u` to be universal; but a D2C graph with a universal vertex cannot contain an edge away from that vertex, so it would be a star.

Consequently, if `x in A` is B-private for `u`, then `x` has some neighbour in `A`. Thus `x` is a nonisolated vertex of `F`.

Let

`nu(F)=# {x in A : d_F(x)>0}`.

If `P subseteq T` is the set of triangle-active B-vertices which possess a B-private A-neighbour, choosing one private neighbour for each `u in P` is injective: a B-private vertex has a unique B-neighbour. Therefore

> `|P| <= nu(F) <= 2f`.                                (4.1)

This is the first stability payment. In the exact boundary `F=empty`, private alternatives do not exist at all.

## 5. The antipode alternative forces large cross deficit

Assume some triangle-active `u` has no B-private A-neighbour. Lemma 3.1 supplies `w in B` with

`N_G(u) intersect N_G(w)={v}`.

In particular their A-neighbourhoods are disjoint:

`N_A(u) intersect N_A(w)=empty`.

Using (2.1),

`|N_A(u)|=a-h_u`, `|N_A(w)|=a-h_w`.

Disjointness therefore gives

`(a-h_u)+(a-h_w) <= a`,

so

> `h_u+h_w >= a`.                                      (5.1)

Since `h_x=q_x+rho_x`, and the global selected/residual sums are

`sum q_x=Q`, `sum rho_x=r`,

(5.1) immediately yields

> `Q+r >= a`.                                           (5.2)

This is the stable version of the large-zero-coordinate conclusion used in the exact Boolean boundary.

## 6. Convert to residual defect

The canonical source inequality is

`p_u <= rho_u+lambda`.

Summing over `B` gives

`Q <= r+b lambda`.                                      (6.1)

Combine (5.2) and (6.1):

`a <= Q+r <= 2r+b lambda`.

Hence

> `2r+b lambda >= a`.                                   (6.2)

Using `r=f+delta` gives the defect form

> `2 delta + 2f + b lambda >= a`.                       (6.3)

Equivalently,

`delta >= ceil((a-b lambda)/2)-f`,

with the ceiling understood only when an integer form is desired.

At exact balance (`lambda=0`), the antipode branch forces

`r=f+delta >= ceil(a/2)`.                               (6.4)

## 7. Global rooted-triangle dichotomy

If every active vertex belongs to `P`, then by (4.1)

`|T|<=nu(F)`.

All `Q=e(G[B])` rooted-triangle edges have both endpoints in `T`, so

`Q <= binom(|T|,2) <= binom(nu(F),2) <= binom(min(b,2f),2)`.   (7.1)

If not every active vertex belongs to `P`, then (6.3) holds.

Therefore:

> **Theorem 7.1 (root-edge stability dichotomy).** For a non-star D2C graph rooted at a maximum-degree vertex with `Q=e(G[B])>0`, at least one of
>
> `Q <= binom(nu(F),2) <= binom(min(b,2e(F)),2)`,       (D1)
>
> or
>
> `2 delta + 2e(F) + b(2b-n) >= a`                    (D2)
>
> must hold.

The first branch says that all rooted triangle activity can be supported by distinct A-side private witnesses, which forces the active B-set to fit inside the nonisolated vertex set of `F`.

The second branch says that once even one active root neighbour lacks such a private witness, root criticality forces an antipodal B-pair, and the combined selected/residual A-cross deficit must be large.

## 8. Important special cases

### 8.1 `F=empty`

If `F` is empty and `Q>0`, then `nu(F)=0`, so (D1) is impossible. Therefore

> `2 delta + b(2b-n) >= a`.                            (8.1)

Since here `r=delta`, this is also

`2r+b lambda>=a`.

This is a genuine one-layer extension of the exact `F=r=0` boundary: residual cross mass is allowed, but it must pay for the loss of exact coordinate flow.

When `r=delta=0`, (8.1) reduces to

`b lambda>=a`.                                         (8.2)

The hypercube-face negative control `X_3` has

`a=3`, `b=8`, `lambda=4`, `delta=f=0`,

so it satisfies (8.2) comfortably. The theorem therefore does not accidentally exclude the known 12-vertex/32-edge obstruction.

### 8.2 Balanced maximum degree

If `b=n/2`, then `lambda=0`. Thus either

`Q <= binom(nu(F),2)`,

or

> `delta+e(F)=r >= ceil(a/2)`.                         (8.3)

So a triangle-bearing balanced root cannot simultaneously have sparse `F`, small residual mass, and many rooted triangles.

## 9. Exact small-order regression

`check_root_edge_stability_atlas.py` checks the pure graph-theoretic dichotomy and the canonical-parameter corollaries for every D2C graph in NetworkX's graph atlas (all unlabeled graphs through order 7), at every maximum-degree root lying in a triangle.

Counts of D2C isomorphism classes are

`n=3:1, 4:2, 5:3, 6:5, 7:10`.

The checker examined all maximum-degree triangle-root instances among them and found no failure of:

- Lemma 3.1;
- the injection `|P|<=nu(F)<=2e(F)`;
- `Q+r>=a` in the antipode branch;
- `2r+b lambda>=a` in that branch.

This is only a regression check. The proof above is the mathematical basis.

## 10. Strategic consequence

The next perturbative step should split according to Theorem 7.1 rather than trying to repair Boolean factorial expansion uniformly.

1. **Private-foot branch:** all triangle-active B-vertices inject into nonisolated vertices of `F`. The natural next theorem is to classify how the corresponding private A-vertices can be connected inside `F`, using criticality of those F-edges and selected-pair uniqueness. Sparse `F` now means few possible active triangle vertices.
2. **Antipode branch:** (5.1) provides an actual disjoint-support pair. Here one should try to restart the Boolean/path expansion after deleting or charging the residual coordinates on this pair. The residual budget enters explicitly through `r`, not as an unstructured error term.

This decomposition is more informative than a blanket `r+e(F)` perturbation: it identifies the exact obstruction to the zero-boundary antipode argument and charges that obstruction to `F`.

No eventual second-extremal theorem is claimed yet.