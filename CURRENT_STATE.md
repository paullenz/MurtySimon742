# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The 2019 all-order second-extremal strengthening is false because of a published 12-vertex, 32-edge D2C graph. The live problem is the sufficiently-large / eventual second-extremal classification around `M(n)=floor((n-1)^2/4)+1`. Existing Murty–Simon / Erdős #742 work remains preserved.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `ZERO_RESIDUAL_BOUNDARY_CODING_CUTOFF_294_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Continued from the independently reconstructed hypercube-face exception. The exact zero-residual boundary has now been converted into a binary coding theorem and a finite-order obstruction.

**INSPECTED PREDECESSOR:** `510281fe61fb754008492a6a86c6867c93a02372` on `main`, containing the `X_k` hypercube-face D2C family and the k=3 canonical profile.

**LAST VERIFIED RESULT:** `project/research/post_ms/2026-09-17-stronger-pivot-v1/ZERO_RESIDUAL_BOUNDARY.md` plus `check_zero_residual_cutoff.py`.

Assume the canonical maximum-degree-root system satisfies

`t=0`, `F=empty`, hence `r=0`,

and the graph is non-bipartite (equivalently here `Q=e(G[B])>0`). For each `u in B`, encode its G-neighbourhood in A by

`c(u) in {0,1}^a`, `c_i(u)=1 iff u a_i is an edge of G`.

Because every H-cross edge is selected and every missing H[B] pair has exactly one selected representative:

1. every edge `uw` of `G[B]` joins codes of Hamming distance exactly one;
2. orient that edge from the endpoint with `0` in the changed coordinate to the endpoint with `1`;
3. for every vertex u and every zero coordinate of c(u), there is **exactly one** outgoing edge flipping that coordinate;
4. there are no other B-edges.

Thus the occupied codes form an upward-closed subset of the Boolean cube (with multiplicities), and the selected representatives are a directed coordinate-flow system.

Put

`lambda=2b-n=b-a-1`.

For `u in B`, its directed indegree is exactly `p_u`, and maximum-degree of the root gives

`p_u<=lambda`.

Since `Q>0`, necessarily `lambda>=1`.

**FACTORIAL PATH LEMMA:** if a B-vertex has z zero coordinates, then it generates `z!` monotone directed paths to the all-ones fibre, while each endpoint can receive at most `lambda^z` such length-z paths. Hence

`z! <= b lambda^z`.                                    (FP)

**ROOT-CRITICALITY FORCES A LARGE-Z VERTEX:** choose a B-vertex u with at least one zero coordinate. Its root edge `ru` cannot be certified by `(r,u)` because u has a B-neighbour. It cannot be certified by `(r,a_i)` because every A-vertex has degree at least 2 in a non-star D2C graph. Therefore deleting `ru` forces a pair `(u,w)` whose only common neighbour was r. In particular the A-supports of c(u) and c(w) are disjoint. If u has z zeros, w has at least `a-z` zeros, so some B-vertex has

`z>=ceil(a/2)`.

Combining with (FP) gives a necessary arithmetic condition for every non-bipartite zero-residual boundary realization.

**SECOND-EXTREMAL CUTOFF:** in this boundary

`b=a+1+lambda`, `n=2a+2+lambda`, `m=b(a+1)`.

Assume also `m>=M(n)`. A hand estimate rules out `a>=1296`: the density inequality gives `lambda<=3 sqrt(a)`; the standard integral bound `z! >= (z/e)^z` with `e<3`, together with `z>=a/2`, makes `z!/(lambda^z)>2^z`, contradicting `b<=2a` once `a>=1296`.

The remaining finite integer range `a<1296` is checked exactly (integer factorials, no floating-point acceptance criterion). The strongest surviving necessary arithmetic point is

`a=134, lambda=24, z=67, b=159, n=294`.

Therefore:

> **Any non-bipartite D2C graph in the exact canonical boundary `t=0, F=empty, r=0` with `m>=floor((n-1)^2/4)+1` must have `n<=294`.**

This is an internally proved, partly computer-assisted structural theorem. The arithmetic survivor at n=294 is only a necessary-conditions survivor; no graph realization is claimed.

**RELATION TO THE 12-VERTEX EXCEPTION:** the hypercube-face graph `X_3` has `a=3,b=8,lambda=4,n=12` and lies inside this boundary. The family `X_k` for k>=4 remains D2C but falls below the second-extremal density. The new cutoff formalizes the broader phenomenon: this exact residual-zero mechanism cannot threaten the sufficiently-large problem beyond order 294.

**IDENTITY / NOVELTY BOUNDARY:** direct isomorphism between `X_3` and the published Figure 1 remains uncertified from authoritative adjacency data, although the published enumeration plus matching invariants make it strongly likely. No novelty claim is made for the `X_k` family or the Boolean-flow lemma pending a dedicated literature comparison.

**OLD LINE PRESERVED:** fixed-order candidates, audits, exact-block work, residual h-index/receiver theory, selected-incidence Hall and the complete mixed `{4,5}` all-E closure remain available. Canonical ledger remains **4626 exclusions / 952 survivors / 3632 whole-state closures**; no promotion changes.

**AUTOMATION STATUS:** hourly task is `Eventual D2C Research`; it must retain the published 12-vertex exception and `X_3` as hostile controls and not revert to the false all-order conjecture.

**UNPRESERVED WORK:** None after this checkpoint.

**DEFERRED ADMIN:** authoritative Figure-1 adjacency/isomorphism certification; fresh Lean recompilation of `Erdos742/Erdos742`; reviewer-facing README synchronization; older archive transfers; PR #2; unrelated CI/root narrative maintenance; full novelty search for the hypercube-face construction and Boolean-flow formulation.

**NEXT ACTION:** MATH: move one layer outward from the exact boundary. Treat small positive residual defect / small `r+e(F)` as perturbations of the Boolean coordinate-flow system. Seek a stability version: delete or charge a bounded number of exceptional cross incidences/F-edges so that most of `G[B]` still admits the coordinate orientation, then combine factorial expansion with the existing Hall/residual inequalities. The immediate target is an inequality of the form `n <= N(delta,e(F),...)` for triangle-containing graphs at second-extremal density, with the zero-residual theorem recovered at `(delta,e(F))=(0,0)`.
<!-- CURRENT-STATUS:END -->
