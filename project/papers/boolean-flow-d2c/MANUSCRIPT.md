# Boolean coordinate flow and root-edge stability in near-extremal diameter-2-critical graphs

**Status:** working paper. Core statements are internal candidate theorems; external mathematical and novelty review remain open. The paper does not claim an eventual second-extremal classification.

## Abstract — provisional

Root a diameter-2-critical graph `G` at a maximum-degree vertex `v`, with `B=N(v)` and `A=V(G)\N[v]`. In the exact zero-residual boundary, the `A`-neighbourhood of each `B`-vertex becomes a Boolean word: every `B`-edge changes one coordinate and admits a canonical increasing orientation, with a unique outgoing flip for each zero coordinate. A factorial path count combined with root criticality yields an order cutoff `n<=294` at the comparison density `m>=floor((n-1)^2/4)+1`.

Away from the exact boundary, root-edge criticality gives an antipode-or-private-foot dichotomy. The antipode branch forces explicit residual mass. In the all-private branch, if `t` is the number of triangle-active `B` vertices, we prove the stability inequality

`t(b-t)<=2delta`,

where `delta=b(n-b)-m=r-e(F)`. In particular the exact-defect all-private branch `delta=0`, `Q=e(G[B])>0`, is impossible: equality would force a rigid pair of cliques linked by a matching, in which a `B`-edge is not diameter-critical. For small positive defect the same argument gives quantitative near-clique/degree-slack control.

## 1. Scope and notation

Let `v` be a maximum-degree root,

`B=N_G(v)`, `A=V(G)\N_G[v]`, `b=|B|`, `a=|A|`,

`F=G[A]`, `f=e(F)`, `Q=e(G[B])`.

Retain the canonical selected/residual construction, restating every bridge fact used in the finished paper. Use residual mass `r`, defect

`delta=r-f=b(n-b)-m`,

and `lambda=2b-n`.

## 2. Exact zero-residual Boolean coding

Assume `F=empty` and `r=0`, and `Q>0`. Encode each `u in B` by its `A`-neighbourhood word `c(u) in {0,1}^a`.

**Theorem 2.1.** Every `B`-edge joins codes at Hamming distance exactly one.

**Theorem 2.2.** Orient the edge from 0 to 1 in its changed coordinate. Every zero coordinate of a code has exactly one outgoing flip and there are no other outgoing `B`-edges.

Repeated-code fibres must be treated explicitly in the final proof.

## 3. Factorial path growth and the cutoff

If a code has `z` zero coordinates, all `z!` orders of coordinate flips give monotone directed paths. Maximum degree bounds directed indegree by `lambda`, hence

`z!<=b lambda^z`.

Root-edge criticality supplies a pair with disjoint `A`-support, forcing some code with

`z>=ceil(a/2)`.

Combined with the second-extremal comparison density and an exact finite arithmetic check:

> **Boundary cutoff (internal candidate).** A non-bipartite D2C graph in `F=empty,r=0` with `m>=floor((n-1)^2/4)+1` has `n<=294`.

The `n=294` arithmetic point is not a claimed graph.

## 4. Hypercube-face model family

For `k>=3`, let `X_k` have a root adjacent to all cube vertices of `Q_k`, coordinate vertices `a_i` adjacent to the zero face in coordinate `i`, and the cube edges themselves. The elementary edge-type proof gives D2C with

`n=2^k+k+1`, `m=(k+1)2^k`.

`X_3` has the coarse invariants of the known 12/32 obstruction; authoritative isomorphism remains uncertified. For `k>=4` the family falls below the comparison threshold. No novelty claim is authorised.

## 5. Root-edge antipode/private-foot dichotomy

Call `u in B` triangle-active when it has a neighbour in `B`.

> **Root-edge dichotomy.** Every triangle-active `u` has either
> 1. a private foot `x in A` with `N(x) cap B={u}`, or
> 2. an antipode `w in B\{u}` with `uw` a nonedge and `N(u) cap N(w)={v}`.

The proof comes directly from deleting `vu`: `(v,u)` still has a two-path through the rooted triangle, so a newly distant pair must occur on one of the two other sides of an old path using `vu`.

## 6. Antipode payment

Private-supported active vertices inject into the nonisolated vertices of `F`, hence there are at most `2f` of them.

If an active vertex has no private foot, the antipode has disjoint `A`-support. With canonical cross deficit `h_u=q_u+rho_u`,

`h_u+h_w>=a`,

and globally

`Q+r>=a`.

Using `Q<=r+b lambda` gives

`2r+b lambda>=a`,

or

`2delta+2f+b(2b-n)>=a`.                                (RSD)

## 7. All-private gap theorem

Suppose every triangle-active `B` vertex has a private foot. Let `T` be the active set and `t=|T|`.

Each distinct private foot misses `b-1` cross edges, so

`Q+r>=t(b-1)`.                                          (7.1)

Maximum degree of the root gives, after summing degrees over `A`,

`2f<=Q+r`,

hence with `r=f+delta`,

`f<=Q+delta`,

and therefore

`Q+r<=2Q+2delta`.                                       (7.2)

All `B`-edges lie inside `T`, so `Q<=binom(t,2)`. Combining (7.1)-(7.2):

> **All-private gap theorem (internal candidate).**
>
> `t(b-t)<=2delta`.                                     (APG)

This supersedes the earlier private-branch edge bound as the main scalar constraint.

## 8. Exact all-private exclusion

If `delta=0` and `Q>0`, APG forces `t=b`. Equality throughout its proof then forces

`G[B]=K_b`, `f=Q=binom(b,2)`,

all missing A-B incidences to come from the `b` private feet, and equality in every A-side maximum-degree constraint. Consequently the private feet induce `K_b`, each is joined to its unique matched vertex of `B`, and every nonprivate A-vertex is B-complete and F-isolated.

Delete any edge `uw` of `B`. The endpoints remain at distance two through `v`, while the potentially asymmetric private vertices are repaired by the two-paths

`u-x_u-x_w` and `w-x_w-x_u`.

All other pairs remain within distance two. Thus `uw` is not critical, contradiction.

> **Exact all-private exclusion.** No non-bipartite all-private maximum-root D2C branch with `Q>0` has `delta=0`.

## 9. Near-exact rigidity

When APG forces `t=b`, write `Q=binom(b,2)-s`. Then

`s<=delta`,

so `B` is missing at most `delta` clique edges. Moreover

`binom(b,2)+s-delta <= f <= binom(b,2)-s+delta`,

and total A-side maximum-degree slack is at most

`2(delta-s)<=2delta`.

The number of missing A-B incidences beyond those forced by the private feet is also at most `2(delta-s)`.

This suggests the next structural step: each surviving `B`-edge must obtain a criticality witness from a defect in an otherwise noncritical rigid model. Pricing those witnesses against the `O(delta)` available defects may force a positive lower bound on `delta` growing with `b`.

## 10. Regression

The existing zero-boundary and root-edge atlas checks remain preserved. A new standalone checker `check_all_private_stability_atlas.py` tests APG and the exact exclusion on every D2C graph-atlas isomorphism class through order 7 and every maximum-degree triangle root. It finds 3 all-private roots, no APG violation, and no `delta=0` all-private root.

Finite testing is regression evidence only.

## 11. Current frontier

Two tasks now matter most:

1. **all-private branch:** price criticality of `B`-edges against the small defect budget quantified in Section 9;
2. **scope:** resolve or explicitly quarantine the possibility that a triangle-containing D2C graph has no maximum-degree vertex in a triangle.

The antipode branch retains (RSD) as its starting inequality; factorial expansion should only be reintroduced after these structural obstructions are understood.

## 12. Literature and trust boundary

The final paper must compare the construction and stability results against classical D2C/Murty–Simon work, the recent primitive-D2C/counterexample literature, the sufficiently-large `C5`-free second-extremal results, and known Boolean/product constructions.

All theorems above are internal candidates. No eventual classification, novelty claim, authoritative 12-vertex identification, or first-solution priority is asserted.
