# Murty–Simon / Erdős #742 — live current state

> Read this first. The defect-one attack has yielded a parameterized critical-edge covering argument. The derivation is preserved below before its verification unit; no computational check of the new argument is claimed yet.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_CLIQUE_DEFECT_HAND_PROOF_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Theorem-first priority. One critical-edge covering derivation, not a survivor scan.

**INSPECTED PREDECESSOR:** `54f974fcff8acd85870deacc931da15ec4b11069`, tree `8aee1d0825d29ef22652b4a7ed7493a219092b17`, CURRENT_STATE blob `5cb8a19152dde50adfe4e6df9c73e0cec3a56405`; current file freshly re-read before this contents update. The full preceding handoff and zero-defect proof remain at that immutable commit.

**LAST VERIFIED RESULT:** new internal symbolic derivation, finite verification pending. For every actual exact d-by-d tight block with d>=3 and complete F[T], critical-edge covering forces L+beta>=(d-1)(d-2). If F[T] is not complete, 2mu>=2 already. Thus intrinsic defect one is excluded for every d>=3. No d=2 closure is claimed: beta=0 automatically there, and the L=1 singleton-label exception remains open. Full derivation below.

**IMPLICATIONS / LIMITS:** conditional on the full original graph construction. For a complete tight graph, W>=d+(d-1)m+(d-1)(d-2); for d=5 this gives W>=37, or W>=57 when E>0. Without the completeness assumption the new derived universal d>=3 increment is only two, not the quadratic term. The argument uses criticality of all original edges and full receiver pools. It does not establish that every counterexample has an exact block.

**CHECKS:** new local graph and incidence checks NOT_RUN at this checkpoint. No replay of prior tests is claimed. The older zero-defect proof and its 8601 graph records retain their recorded internal status. Both proof and prospective implementations are by the same assistant; external review and novelty assessment OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Prior 203-key candidate union, 41 strict/equality certificates and 170-candidate audit unchanged. State3349 unresolved. No catalogue application, q-enumeration, workflow launch or promotion.

**UNPRESERVED WORK:** no completed mathematical derivation remains only in session memory after remote confirmation; the new argument and its d=2 limitation are transcribed below. Existing raw-archive and older-attachment transfers remain pending.

**DEFERRED ADMIN:** older raw evidence transfers; root README/reviewer integration; unrelated CI/status work; independent review, literature novelty assessment and promotion.

**NEXT ACTION:** verify this same critical-edge covering theorem with explicit-path graph checks, separately structured incidence/defect arithmetic, and negative controls for full-pool saturation, singleton marks, completeness and d=2. Preserve exact decisions, proof and honest coverage limits. Do not treat checking the local lemma as enumerating original canonical graphs. After verification, choose between the d=2 exceptional branch and a separately proved extension to incomplete F[T]; do not silently apply the clique bound to mu>0.

**PROCESS RULE:** one bounded unit, preservation and one remote confirmation; no background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Preserved derivation: critical-edge covering and clique defect

Use the complete canonical selected/residual construction of the recovered interface theorem at `4cb18222e4c0f56c2a5278f424c8414a09c469f7`. Let G be diameter-two edge-critical, J its complement, p a minimum-degree pivot, A its J-neighbourhood and B the remaining vertices. F=G[A]. Assume T={i:s_i=d}, H={v:rho_v>=d}, |T|=|H|=d>=3. Put K=N_F(T) minus T. Every high vertex selects T and carries K residually; every low vertex has residual degree at most d-1 and selects no tight label. The full pools are V_t={v outside H:R_v=T minus {t}}, p_t=|V_t|>=1, m=sum p_t>=d. At any actual exact block, each K-weight is d at zero demand and d-1 at positive demand: the d forced full receivers make the requisite low residual order statistics d-1. Put ell_k=|N_F(k) intersect T|, L=sum_K(w_k-ell_k), beta_t=R_t-(m-p_t)>=0, beta=sum beta_t, and mu=binom(d,2)-e(F[T]). The existing exact identity is W-d-(d-1)m=P+L+beta+2mu with P>=0.

Assume now mu=0, so T is a clique.

### 1. Full-pool adjacency and redundant edges

If k in K is adjacent in F to t, then k is adjacent in G to every vertex x of V_t. Indeed k cannot be residual at x, since R_x=T minus {t}. If k were selected there, its quasi-edge would have to dominate t in J, but both k and x miss t in J. Thus kx is absent in J and present in G.

Define Z={t in T: some k in K has N_F(k) intersect T={t}}, U=T minus Z, z=|Z| and u=|U|. These marks record singleton tight neighbourhoods, not all private witnesses of the original graph.

Suppose t,s are distinct vertices of U and have a common K-neighbour k. Delete ts. Its endpoints retain a length-two path through a third tight vertex (d>=3). For an exclusive neighbour x of s, with x nonadjacent to t, consider its type. If x lies in A, it lies in K; because s is unmarked, x has another tight neighbour r different from s and t, giving t-r-x. If x lies in B and has at least two tight neighbours, the same path works. If x in B has only s as a tight neighbour, it has all d-1 other tight labels residual, so its low residual ceiling forces x in V_s; then t-k-x is a path by the full-pool adjacency fact. A high B vertex has no tight G-neighbour. The pivot and A-labels outside T union K have no tight G-neighbour. Reverse t and s for the other exclusive neighbours. This covers every formerly length-at-most-two path destroyed by ts; thus ts would be noncritical, a contradiction.

Consequently every k in K has at most one tight neighbour in U.

### 2. Counting distinct labels, not repeated incidences

Write e_U=e_F(U,K), kappa=|K|, p_Z=sum_(t in Z)p_t and beta_U=sum_(t in U)beta_t. Each K-label meeting U contributes exactly one edge to e_U. In addition there are at least z DISTINCT singleton labels witnessing the z distinct marks, none of which meets U. Therefore

    kappa >= e_U+z.                                      (C1)

Each tight row satisfies e_F(t,K)=1+m-p_t+beta_t, since its full F-degree is d+R_t and its internal tight degree is d-1. Summing over U gives

    e_U=u+(u-1)m+p_Z+beta_U.                            (C2)

Every K weight is at least d-1, and e_F(T,K)=d+(d-1)m+beta. Hence

    L+beta >= (d-1)kappa-d-(d-1)m
           >= d(d-2)+(d-1)[(u-2)m+p_Z+beta_U].          (C3)

If u>=2, the bracket is nonnegative, so L+beta>=d(d-2). If u<=1, there are z>=d-1 distinct singleton labels; each has ell=1 and weight at least d-1, hence contributes at least d-2 to L. Therefore L+beta>=(d-1)(d-2). Together these prove the parameterized clique bound.

If equality L+beta=(d-1)(d-2) holds, the inequalities force u=1, z=d-1, beta=0, exactly one singleton label at each mark, all those labels of positive demand, and zero weight loss at every other K-label. These are necessary equality conditions, not an existence claim.

### 3. Scope and the small exception

For d>=3, mu=0 gives L+beta>=(d-1)(d-2)>=2; mu>=1 gives L+beta+2mu>=2 immediately. Thus intrinsic defect one is closed for every d>=3, without a positive-surplus assumption or restriction on m.

For d=2, every K-label has zero demand. Also beta=0: any tight residual occurrence at a low vertex already fills its one residual slot and places it in a full pool. L=1 therefore means exactly one zero-demand K-label is adjacent to just one tight vertex, while all other K-labels are common. The only tight edge may use that singleton as a private witness. The preceding quadratic statement and d>=3 edge argument do not close this case. No counterexample graph is claimed, and no exceptional class is silently declared absent.

A preliminary, weaker count used only singleton costs and row balance; the distinct-label count (C1)-(C3) strengthens it. No computational or literature-priority claim is attached to the derivation.

## Earlier evidence

- Zero-defect proof: `project/research/general_n/2026-09-16-zero-defect-closure-v1/ZERO_DEFECT_CLOSURE.md`.
- Its exact preceding operational handoff is preserved at `54f974fcff8acd85870deacc931da15ec4b11069:CURRENT_STATE.md`.
- Complete graph-to-interface proof is preserved at `4cb18222e4c0f56c2a5278f424c8414a09c469f7:CURRENT_STATE.md`.
