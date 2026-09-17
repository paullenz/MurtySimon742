# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live graph-theory problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The 2019 Dailly–Foucaud–Hansberg all-order strengthening is false: the published 2024 order-12, size-32 D2C graph remains a mandatory hostile control. Existing Murty–Simon / Erdős #742 work and the standalone-paper programme remain preserved, but they are not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `DENSE_MAX_TRIANGLE_OR_TWIN_REDUCTION_CHECKED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit critically reconsidered the previous instruction to prove a blanket maximum-triangle-root lemma. A cleaner route emerged: price the `Q=0` maximum-root branch directly. The resulting theorem replaces the root-scope gate by an explicit false-twin reduction.

**INSPECTED PREDECESSOR:** `450d5e1c3d97e3b45f67a1e8868e2db385e942b7`, whose substantive result is the all-private edge-witness pricing theorem and the conditional dense-root antipode theorem. No intervening mathematical commit was found before this unit.

## New result — exact `Q=0` defect coordinates

Let `v` be a maximum-degree root with

`B=N(v)`, `A=V(G)\N[v]`, `b=Delta(G)`, `F=G[A]`, `f=e(F)`, `Q=e(G[B])`.

Assume `Q=0`, so `B` is independent. For `x in A` put

`R_x=b-|N_B(x)|`, `d_x=d_F(x)`, `e_x=R_x-d_x`.

Maximum degree gives the exact identity

`e_x=b-d_G(x)>=0`.

Since every missing `A-B` incidence is residual when `Q=0`,

`r=2f+sum_x e_x`,

hence the residual defect

> `delta=b(n-b)-m=r-f=f+sum_x e_x`.                    (Q0)

Thus `delta` is literally the internal `A`-edge count plus total degree slack below the maximum.

## Triangle-free `F`-edge payment

If `xy in E(F)` lies in no triangle of `G`, then its `B`-neighbourhoods are disjoint, so

`R_x+R_y>=b`.

The endpoints also have no common `A`-neighbour, so

`f>=d_x+d_y-1`.

Using (Q0),

> `delta>=b-1`.                                        (TF)

This is exactly the defect needed for the second-extremal comparison because

`b(n-b)-(b-1)=b((n-1)-b)+1<=M(n)`.

Consequently, whenever

`m>=M(n)+1`,

one has `delta<=b-2`, and therefore **every edge of `F` must lie in a triangle**.

## Maximum-triangle-or-twin reduction

Call `x in A` tight when `e_x=0`, equivalently `d_G(x)=b`.

If a tight `x` is incident with an `F`-edge, that edge is triangular by (TF), so `x` itself is a maximum-degree triangle vertex. Therefore, if **no** maximum-degree vertex lies in a triangle, every tight `A`-vertex is isolated in `F`.

For such a tight isolated `x`, `R_x=0`, so

`N_G(x)=B=N_G(v)`.

Hence all tight isolated vertices together with `v` form a false-twin class `W` with common independent neighbourhood `B`.

Let `D={x in A:e_x>0}`. Then `F=F[D]`, `|D|<=sum e_x=delta-f`, and in the triangle-bearing branch `f>=1`. At `m>=M(n)+1` this implies

> `|W|>=3`.                                             (TW)

Thus any above-threshold triangle-containing graph with no maximum-degree triangle vertex has at least three maximum-degree, triangle-free false twins.

## False-twin peeling

If `x,y` are nonadjacent twins with common independent neighbourhood `B`, deleting one twin preserves diameter at most two because every path `p-y-q` can be replaced by `p-x-q`.

For edge criticality, any witness avoiding the deleted twin survives. A witness `(y,z)` transfers to `(x,z)` by the twin automorphism unless the surviving edge under test is `xu`, `u in B`; in that case deleting `xu` leaves `x,u` with no common neighbour because `B` is independent. Hence every surviving edge remains critical, provided the reduced graph is noncomplete.

Applying this repeatedly to the dense class `W` produces a smaller D2C core `G_0` with one twin root `w`, the same maximum degree `b`, all triangles preserved, and

`A_0=D`, `n_0=b+|D|+1`.

Every removed twin deletes exactly `b` edges while decreasing the order by one, so the residual defect is invariant:

> `delta_0=delta`.                                      (PEEL)

Every nonroot `A_0` vertex has positive degree slack `e_x>=1`.

## Main structural reduction — internal candidate

For a triangle-containing D2C graph with

`m>=M(n)+1`,

at least one of the following holds:

1. **maximum-triangle branch:** some maximum-degree vertex lies in a triangle;
2. **twin-core branch:** there is a false-twin class `W` of at least three maximum-degree, triangle-free vertices with a common independent neighbourhood, and all but one can be peeled to a smaller D2C core preserving `b`, all triangles, and `delta`.

So the previous blanket “maximum-triangle-root” question is no longer the correct main gate. Its only dense obstruction has been compressed to an explicit twin expansion.

Full proof:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/MAX_TRIANGLE_OR_TWIN_REDUCTION.md`

## Verification

`check_max_triangle_or_twin_reduction.py` has been executed successfully and records

`PASS_MAX_TRIANGLE_OR_TWIN_REDUCTION`.

Exact regression counts:

- 21 D2C graph-atlas classes through order 7;
- 5 triangle-bearing classes;
- 41 maximum-root `Q=0` instances;
- 18 triangle-free `F`-edge payment records;
- 82 direct false-twin peel operations;
- 12,497,497 threshold/twin-class arithmetic records through `n=5000`;
- 285 expanded-`C5` equality controls through order 30;
- the explicit `X_3` hostile control `n=12,m=32,M(12)=31,delta=0,Q=12`.

Summary:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/MAX_TRIANGLE_OR_TWIN_CHECK_SUMMARY.json`

These are regression checks only; the hand proof is the mathematical basis.

## Mandatory controls and preserved predecessor

The 2024 order-12/size-32 exception remains untouched. The reconstructed `X_3` has its unique maximum root in the **maximum-triangle branch** (`Q=12`) and is not excluded.

The expanded-`C5` equality family remains a useful boundary control: at maximum roots it has `delta=b-1` and exactly `M(n)` edges.

The predecessor all-private edge-witness theorem remains intact: for `n>=14`, `m>=M(n)+1`, once a maximum-degree triangle root exists, the all-private branch is excluded and a disjoint-support antipode is forced.

## Fallback with a nonmaximum triangle root

If the twin-core route stalls, rerooting at a triangle vertex with

`epsilon=Delta(G)-d(v)`

produces the candidate all-private inequality

`3 delta_v + epsilon(2a-t) >= binom(t,2)+2s+2t(b-t)`.

This is preserved as a fallback, not the primary route; it does not by itself close `epsilon=1`.

## Trust boundary

The maximum-triangle-or-twin reduction, false-twin peeling lemma, and nonmaximum-root epsilon formula are internal hand mathematics with finite regression. External mathematical and novelty review remain open. **No eventual second-extremal theorem is claimed.**

The two live branches are now:

1. **`Q=0` peeled core:** prove the stronger independent-neighbourhood defect theorem `delta>=b-1` for a non-bipartite D2C graph with a maximum root whose neighbourhood is independent;
2. **maximum-triangle / antipode branch:** after a maximum-degree triangle root is obtained, convert the forced disjoint-support antipode into the required defect contradiction while preserving the order-12 control.

**UNPRESERVED WORK:** None after this current-state commit.

**NEXT ACTION:** Prioritize the peeled `Q=0` core before further antipode sharpening. In that core,

`N(v)=B` is independent, `A=D`, every `e_x>=1`, `delta=f+sum e_x`, and every `F`-edge must be triangular in any above-threshold candidate.

Try to prove

`delta>=b-1`

by pricing criticality of the triangular `F`-edges. Split a critical arm according to whether its witness lies in `A` or `B`; an `A`-side witness appears capable of forcing a full `b`-scale endpoint payment, while the genuine unresolved case is when all necessary arms can be routed through `B`. If this target fails, preserve an explicit incidence-level obstruction. Do not return to the closed mixed `{4,5}` ladder and do not revert to the obsolete blanket maximum-triangle-root goal.
<!-- CURRENT-STATUS:END -->
