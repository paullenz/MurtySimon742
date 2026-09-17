# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The 2019 all-order second-extremal strengthening is false because of a published 12-vertex, 32-edge D2C graph. The live problem is the sufficiently-large / eventual second-extremal classification around `M(n)=floor((n-1)^2/4)+1`. Existing Murty–Simon / Erdős #742 work remains preserved, but the project is not optimizing for first-proof priority there.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `ROOT_EDGE_STABILITY_DICHOTOMY_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Returned from the dependency-audit transaction to the perturbative Boolean-flow problem. Rather than trying to repair the factorial path argument immediately, this unit isolates the exact way root-edge criticality can fail to produce the disjoint-support antipode used in the zero-residual proof.

**INSPECTED PREDECESSOR:** `7bb7cc9a409d59455fead1042e0eecead5a8930c` on `main`, which synchronized the eventual-D2C target and audited the false 2019 conjecture out of the proof dependency chain. The zero-residual `n<=294` theorem at `32a5d27...` remains preserved.

**LAST VERIFIED RESULT:** `project/research/post_ms/2026-09-17-stronger-pivot-v1/ROOT_EDGE_STABILITY_DICHOTOMY.md` plus `check_root_edge_stability_atlas.py`.

Use a maximum-degree root `v`, with

`B=N_G(v)`, `A=V(G)\N_G[v]`, `b=|B|`, `a=|A|`, `F=G[A]`, `f=e(F)`,

and canonical residual variables

`Q=e(G[B])`, `r=sum rho_u`, `delta=r-f=b(n-b)-m`, `lambda=2b-n`.

Call `u in B` **triangle-active** when it has a neighbour in `B`.

**ROOT-EDGE ANTIPODE-OR-PRIVATE LEMMA.** For every triangle-active `u`, criticality of the root edge `vu` forces one of two alternatives:

1. **private-foot alternative:** there is `x in A` with `N_G(x) intersect B={u}`;
2. **antipode alternative:** there is `w in B\{u}` with `uw` a nonedge and `N_G(u) intersect N_G(w)={v}`.

The proof is direct: after deleting `vu`, `(v,u)` stays at distance two through a rooted triangle neighbour. Any newly distant pair whose old path used `vu` must therefore be either `(v,x)` or `(u,w)`, giving exactly the two alternatives above.

Because a non-star D2C graph has no leaf, every private `x in A` is incident with an `F`-edge. Hence the set `P` of triangle-active B-vertices possessing a private A-neighbour injects into the nonisolated vertex set of `F`:

`|P| <= nu(F) <= 2e(F)`.

If some triangle-active source has no private foot, the antipode pair has disjoint A-neighbourhoods. Writing

`h_u=q_u+rho_u=# {x in A: ux notin E(G)}`,

this gives

`h_u+h_w>=a`,

and therefore the global cross-deficit bound

`Q+r>=a`.

The canonical source inequality `Q<=r+b lambda` then yields

`2r+b lambda>=a`,

or equivalently

`2 delta + 2e(F) + b(2b-n) >= a`.                    (RSD)

If instead **every** triangle-active source has a private foot, all rooted-triangle edges lie inside at most `nu(F)` active B-vertices, so

`Q <= binom(nu(F),2) <= binom(min(b,2e(F)),2)`.       (PRIVATE)

Thus every maximum-degree triangle root satisfies the compact dichotomy `(PRIVATE)` or `(RSD)`.

**IMPORTANT SPECIAL CASE `F=empty`:** if `Q>0`, the private branch is impossible, so

`2 delta + b(2b-n) >= a`.

This is a genuine one-layer extension of the exact `F=r=0` Boolean boundary: positive residual cross mass is allowed, but it must pay for the loss of exact coordinate flow. At exact balance `b=n/2`, the antipode branch forces

`r=delta+e(F) >= ceil(a/2)`.

**12-VERTEX NEGATIVE CONTROL:** the reconstructed `X_3` profile has `a=3,b=8,lambda=4,delta=f=0` and satisfies the new inequality comfortably; the theorem does not accidentally exclude the published-order obstruction. Direct authoritative isomorphism between `X_3` and the published Figure 1 remains uncertified.

**FINITE REGRESSION:** the atlas checker covers every D2C isomorphism class through order 7 and every maximum-degree root lying in a triangle. It found no failure of the root-edge dichotomy, the private-foot injection, `Q+r>=a`, or `2r+b lambda>=a`. This is regression evidence only; the hand proof is the basis of the theorem.

**INTERPRETATION:** the first perturbative obstruction is now explicit. The zero-boundary antipode argument is not destroyed arbitrarily by `F` and residual mass. It fails only when rooted triangle-active vertices are supported by distinct private A-feet, and those feet must sit on `F`. Otherwise an actual disjoint-support antipode survives and immediately forces a quantitative residual/defect payment.

**STATUS / TRUST BOUNDARY:** internal hand theorem, not promoted; external mathematical and novelty review open. No eventual second-extremal theorem is claimed. The maximum-triangle-root scope issue also remains open: a triangle-containing D2C graph is not yet proved to have a maximum-degree vertex in a triangle.

**OLD LINE PRESERVED:** fixed-order candidates, audits, exact-block work, residual h-index/receiver theory, selected-incidence Hall, the complete mixed `{4,5}` all-E closure, the 12-vertex hypercube-face reconstruction, and the zero-residual `n<=294` cutoff remain available. Canonical ledger remains **4626 exclusions / 952 survivors / 3632 whole-state closures**; no catalogue promotion changes.

**UNPRESERVED WORK:** None after this checkpoint.

**DEFERRED ADMIN:** authoritative Figure-1 adjacency/isomorphism certification; fresh independent Lean recompilation of `Erdos742/Erdos742`; older archive transfers; PR #2; unrelated CI/root historical narrative maintenance; full novelty search for the hypercube-face construction / Boolean-flow / root-edge stability formulation.

**NEXT ACTION:** MATH: split the eventual triangle-bearing attack along the new dichotomy instead of treating residual corruption uniformly. First attack the **all-private branch**, because it is now the only way to avoid the explicit antipode defect payment: classify the private A-feet inside `F`, use criticality of their incident F-edges and selected-pair uniqueness, and seek either a forced small cyclic/twin quotient or an additional residual charge. In parallel, retain `(RSD)` as the starting inequality for the antipode branch and only return to factorial/path expansion once the all-private obstruction is understood. Do not return to the closed mixed `{4,5}` ladder.
<!-- CURRENT-STATUS:END -->
