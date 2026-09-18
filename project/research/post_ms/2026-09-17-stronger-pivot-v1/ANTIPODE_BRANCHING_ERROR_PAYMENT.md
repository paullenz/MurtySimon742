# Antipode branching pays quadratic error

18 September 2026. Research directed by Paul Lenz; derivation and finite regression by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted.** This note is independent of the false all-order 2019 second-extremal conjecture. It is a local D2C statement about the antipode relation at a rooted vertex.

Let `G` be diameter-2-critical, let `v` be any root, and put `B=N(v)`. Call distinct `u,w in B` antipodes at `v` when

`uw notin E(G)` and `N(u) cap N(w)={v}`.

For an antipode edge `uw`, let

`eta(uw)`

be the number of vertices outside `{u,w,v}` adjacent to neither endpoint. This is the same error variable used in the antipode slack identity.

Fix `w in B` and let

`S=N_{J_v}(w)`

be its set of antipode partners. Put `d=|S|` and

`E_w=sum_{y in S} eta(yw)`.

---

## 1. Nonedges among partners consume error twice

If `y,z in S` are nonadjacent, then both are nonadjacent to `w` by definition of `S`.

Thus `z` is adjacent to neither `y` nor `w`, so it is counted by `eta(yw)`. Symmetrically `y` is counted by `eta(zw)`.

Therefore every nonedge in `G[S]` consumes two error incidences, and

> `binom(d,2)-e(G[S]) <= E_w/2`.                     (1.1)

Equivalently,

> `e(G[S]) >= binom(d,2)-E_w/2`.                    (1.2)

---

## 2. Edges among partners inject into error incidences

Take an edge `yz in E(G[S])`.

Because `G` is D2C, deleting `yz` raises the diameter. As in the preserved B-edge criticality argument, after orienting the edge if necessary there exists a vertex `x in N(y)\{z}` such that

`x not~ z` and `N(x) cap N(z)={y}`.                  (2.1)

The witness cannot be `v`, because `vz` is still an edge after deleting `yz`.

Since `y` is antipodal to `w`, every neighbour of `y` other than `v` is nonadjacent to `w`. Hence the witness `x` is nonadjacent to `w`. Together with `x not~z`, this means that `x` is one of the vertices counted by `eta(zw)`.

Charge the edge `yz` to the ordered error incidence `(x,z)`.

This charge is injective: for fixed `(x,z)`, condition (2.1) says that `y` is the unique common neighbour of `x` and `z`.

Therefore

> `e(G[S]) <= E_w`.                                  (2.2)

---

## 3. Quadratic branching-error inequality

Combine (1.2) and (2.2):

`binom(d,2)-E_w/2 <= E_w`.

Hence

> **ANTIPODE BRANCHING ERROR THEOREM.**
>
> `E_w >= d(d-1)/3`.                                 (ABE)

Equivalently,

> `3 sum_{y in N_J(w)} eta(yw) >= d_J(w)(d_J(w)-1)`.  (3.1)

Thus the zero-error matching theorem is the first endpoint of a quantitative stability statement: branching is allowed only by paying quadratic antipode error.

Since `eta` is integer-valued, a useful local corollary is

> `max_{y in N_J(w)} eta(yw) >= ceil((d_J(w)-1)/3)`.   (3.2)

In particular, a high-degree antipode hub necessarily contains a substantially errorful relation.

---

## 4. Global error curvature

Sum (3.1) over all `w in B`. Each antipode edge contributes its error to the two endpoint sums, so

`2 sum_{e in E(J_v)} eta(e)
 >= (1/3) sum_{w in B} d_J(w)(d_J(w)-1)`.

Therefore

> `sum_{e in E(J_v)} eta(e)
> >= (1/6) sum_{w in B} d_J(w)(d_J(w)-1)`.             (4.1)

This is a convexity penalty on the antipode degree sequence. Concentrating many root-edge witnesses through a small number of antipode hubs is not free.

---

## 5. Interaction with a near-full tight matching

Suppose the tight antipodes form `p` pairs and leave `u` vertices unmatched, as in `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`, with `p>=2`.

The no-private-foot lemma there shows that every unmatched vertex has at least one antipode partner, and every such incident antipode is errorful.

Hence the errorful antipode edges cover the whole unmatched set. In particular there are at least

`ceil(u/2)`

distinct errorful antipode edges, and therefore

> `sum_{e errorful} eta(e) >= ceil(u/2)`.              (5.1)

This elementary bound is sometimes sharper than the curvature term when the errorful relation is matching-like; (4.1) becomes stronger when the relation branches.

The remaining difficulty is that `(AMC)` directly prices **matchings** of antipode edges, while (4.1) prices total error across a possibly branching antipode graph. The next stability target should therefore be a weighted-matching extraction lemma converting the error curvature into a large-weight antipode matching, with edge weight

`lambda+1+eta(e)=epsilon_x+epsilon_y`.

Such a lemma would plug directly into `(AMC)` and is a more focused target than trying to classify arbitrary errorful antipode graphs.

---

## 6. Finite regression

The companion checker

`check_antipode_branching_error_payment.py`

scans every NetworkX graph-atlas D2C graph through order seven, every possible root, and every antipode centre. It verifies both the local integer form

`3 E_w >= d(d-1)`

and the global curvature inequality.

Frozen summary:

- D2C isomorphism classes through order seven: `21`;
- rooted vertices tested: `126`;
- roots with at least one antipode edge: `43`;
- antipode centres of positive degree: `125`;
- branching centres (`d>=2`): `50`;
- maximum antipode degree observed: `5`;
- local violations: `0`;
- global violations: `0`;
- minimum local integer margin: `0`.

The finite scan is regression evidence only. The proof above is the mathematical basis.
