# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live graph-theory problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The 2019 Dailly–Foucaud–Hansberg all-order strengthening is false: the published 2024 order-12, size-32 D2C graph remains a mandatory hostile control. Existing Murty–Simon / Erdős #742 work and the standalone-paper programme remain preserved, but they are not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `ZERO_RESIDUAL_FULL_TIGHT_COVER_SWITCHING_CLASSIFIED_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit critically reassessed the full/near-full tight-antipode branch from predecessor `b745a8a6500deb22eb5117c206befd6071cd32ea`. Rather than immediately applying a generic Hall inequality, it isolated the exact `r=0` boundary and converted the Boolean witness system into a switching/factorization problem on the antipode fibres. That boundary is now classified: apart from the trivial Q=0 endpoint, only fibre counts `k=2` and `k=4` survive. These are exactly the six-vertex `H5` mechanism and the independent twelve-vertex `X_3` Boolean/cube mechanism.

## Preserved entry point

For a non-bipartite D2C graph above `M(n)`, the preserved Q0 theorem forces every maximum-degree root `v` to have

`Q=e(G[N(v)])>0`.

For `n>=14`, the preserved all-private edge-witness theorem then forces an antipode pair

`u,w in B=N(v)`, `uw notin E(G)`, `N(u) intersect N(w)={v}`.

The tight-antipode matching theorem from the predecessor says zero-error antipodes form a matching. If they cover `B`, write

`B=P_1 dotcup ... dotcup P_k`, `|P_i|=2`, `b=2k`.

Then `G[B]` is a 2-lift of `K_k`, every A-vertex is a Boolean transversal, and

`Q=k(k-1)`,

`r=k(a-k+1)`,

`delta=k(a-k+1)-e(F)`.

The order-12 hostile control `X_3` sits exactly in this full-tight normal form.

## New theorem — residual-zero full tight cover is finite

Assume the full tight cover and

`r=0`.

Then the exact residual formula gives

`a=k-1`.

The H-cross total is `ak=k(k-1)=Q`, so **every H-cross edge is selected**. Hence every source residual degree and label residual degree is zero. The preserved selected-edge inequality

`d_F(x) <= rho_u + R_x`

therefore forces

`F=empty`, `delta=0`.

Choose 0/1 endpoint labels on each antipode fibre. Encode the 2-lift by signs `sigma_ij`. Each `x in A` has a code `c(x) in {0,1}^k`. Define a graph `L_x` on the fibre indices by

`ij in E(L_x)` iff `sigma_ij xor c_i(x) xor c_j(x)=1`.

For the H-cross source in fibre `j`, its common B-neighbours with `x` are exactly the neighbours of `j` in `L_x`. Since every H-cross edge is selected and `F` is empty, that nonedge must have exactly one common neighbour. Thus every vertex of `L_x` has degree one:

> each `L_x` is a perfect matching of `K_k`.

Because all H-cross edges are selected and the selected system is in bijection with the rooted B-edges, two distinct labels cannot reuse a fibre edge. Therefore the `k-1` matchings `L_x` are pairwise edge-disjoint and form a **1-factorization of `K_k`**.

For two labels `x,y`, the switched graphs satisfy

`E(L_x) symmetric_difference E(L_y) = delta(S)`,

where `S` is the set of coordinates on which their Boolean codes differ. Since the matchings are edge-disjoint, the left side is a 2-regular spanning graph. A nontrivial cut of `K_k` is 2-regular only when both sides have size two. Hence, as soon as there are two labels,

`k=4`.

The remaining one-label case is `k=2`.

> **ZERO-RESIDUAL FULL-TIGHT-COVER CLASSIFICATION — internal candidate.** In the triangle-bearing range `k>=2`, a D2C full tight-antipode cover with `r=0` has
>
> `k in {2,4}`,
>
> with `a=k-1`, `F=empty`, `delta=0`.

No residual-zero full-tight Boolean mechanism exists for `k>=6`.

Full hand note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/ZERO_RESIDUAL_TIGHT_COVER_CLASSIFICATION.md`

## Identification of the two surviving normal forms

### k=2

`b=4`, `a=1`, `n=6`, `m=8`.

The normal form is exactly `T_6` in Dailly–Foucaud–Hansberg (2019), and their paper states `T_6 ~= H5`. The companion checker verifies the explicit isomorphism.

### k=4

`b=8`, `a=3`, `n=12`, `m=32`, while `M(12)=31`.

The three A-labels give the three 1-factors of `K_4`. After gauge fixing, the B-layer is the 3-regular bipartite 2-lift

`K_{4,4}-M ~= Q_3`.

There are four finite code-representative choices after gauge; the checker verifies that every resulting normal form is D2C and isomorphic to the project's independent `X_3` construction. Thus the new switching theorem explains the exact Boolean/cube mechanism of the 12/32 negative control.

**Published-figure trust boundary:** direct adjacency-list certification that `X_3` is literally the graph drawn in Radosavljević–Stanić–Živković Figure 1 remains open. The project does not promote that identity from coarse invariants alone.

## Verification

Companion replay:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/check_zero_residual_tight_cover_classification.py`

Recorded summary:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/ZERO_RESIDUAL_TIGHT_COVER_CHECK_SUMMARY.json`

Finite evidence:

- cut-degree obstruction replayed through `k=5000`;
- `k=2` normal form: D2C, order 6, size 8, exact isomorphism to `T_6 ~= H5`;
- `k=4`: all four gauge representatives are D2C, order 12, size 32, and isomorphic to `X_3`;
- the canonical selected-witness map has exactly `Q` records in both surviving normal forms.

Finite checks are regression evidence only. The switching/factorization proof is the mathematical basis.

## Strategic consequence

The exact zero-residual obstruction is now finite. The 12/32 graph is not the first member of an infinite zero-error Boolean family at second-extremal density: the switching class itself blocks continuation beyond four antipode fibres.

The full-cover formula also creates a discrete jump. For `k>=6`, `a=k-1` is impossible, so any full tight cover must have

`a>=k`,

hence

`r=k(a-k+1)>=k`.

For arbitrary positive residual full cover, each A-label `x` still defines a switched graph `L_x`. If `ell_x` is the number of degree-one vertices of `L_x`, then only leaf coordinates can support selected H-cross incidences. Since label `x` has exactly `k-R_x` selected cross edges,

`k-ell_x <= R_x`.

Summing gives the new stability budget

`sum_x (k-ell_x) <= r`.

Thus residual mass measures aggregate departure from the perfect-matching switching boundary.

## Mandatory negative control

The order-12/32 graph remains mandatory. The new theorem **does not exclude it**; it isolates it as the unique `k=4` residual-zero full-tight normal form (up to the internal finite isomorphism check). Likewise the classical six-vertex `H5` is the `k=2` member.

No all-order 2019 Conjecture-3 claim is revived.

## Trust boundary

The residual-zero classification is internal hand mathematics with exact finite replay. External mathematical review and novelty assessment remain open. No eventual second-extremal theorem is claimed.

**UNPRESERVED WORK:** None after this current-state commit.

**NEXT ACTION:** Continue with the **first positive-residual full-tight layer**, not a broad scalar scan. Use the switched graphs `L_x` and the leaf-deficiency budget

`sum_x (k-ell_x) <= r`.

Prove a switching-stability lemma for two switching-equivalent graphs with many degree-one vertices. The key local fact to exploit is: if a vertex is degree one in both switched graphs, then its degree in their symmetric-difference cut is 0 or 2. For `k>4`, two near-perfect switching states can therefore differ only by a small cut whose small side must be paid for by non-leaf coordinates. Convert that payment into a lower bound on `r` (and ultimately `delta`). Use the antipode matching cut `(AMC)` for any unmatched/errorful part. Preserve `H5` and `X_3` as exact finite boundary models.
<!-- CURRENT-STATUS:END -->
