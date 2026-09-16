# Murty–Simon / Erdős #742 — live current state

> Read this first. The incomplete-tight-graph attack has produced a universal-core defect bound. Its complete derivation is preserved below before graph and incidence verification. No catalogue application or promotion.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_UNIVERSAL_CORE_DEFECT_NOT_PROMOTED`.

**WORK MODE:** `MATH`. One parameterized extension of critical-edge covering to incomplete F[T], not a survivor scan.

**INSPECTED PREDECESSOR:** `6c5c979ea636316f3ad078b313314692e2ea1bbc`, tree `337de865b24e6de30fee2bb9190888af13098bca`, CURRENT_STATE blob `fd46115a5139c1ac3827e451b1bcc327698bd9b7`; current contents freshly re-read before this update. The entire preceding d=2 proof/check handoff remains at that immutable commit. No earlier artifact is overwritten.

**LAST VERIFIED RESULT:** internal symbolic derivation. For an actual exact d-by-d block with d>=3, let g count tight vertices adjacent to every other tight vertex. Then L+beta >= (d-2)max(0,g-1). Since g>=d-2mu, intrinsic defect D=L+beta+2mu is at least 2mu+(d-2)max(0,d-2mu-1), and hence at least 2floor(d/2). One missing tight edge gives D>=2+(d-2)max(0,d-3). The proof preserves the original covering argument only on unmarked universal vertices; missing-edge endpoints are not treated as universal.

**SCOPE / CONSEQUENCES:** no positive-surplus, graph-order or pool-size restriction. For d=5, generic / one-missing-edge / clique increments are 4 / 8 / 12; W thresholds are 29/49, 33/53, 37/57 respectively, with the second entry requiring extras. This does not claim every counterexample has an exact block. The earlier d=2 closure separately supplies the same uniform expression at d=2. Equality at D=4 for d=5 forces exactly two disjoint missing tight edges and L=beta=0; graph attainability is not asserted.

**CHECKS:** only the new numerical envelope and strict-surplus inequality have been checked for d=3,...,99. New local graph and incidence verification NOT_RUN at this checkpoint. Earlier tests retain their inherited scope and were not replayed. External mathematical review and novelty assessment OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Prior 203-key candidate union, 41 strict/equality certificates, 170-candidate audit and state3349 retain their earlier boundaries. No workflow launch, q-enumeration or promotion.

**UNPRESERVED WORK:** no completed mathematical derivation remains only in session memory after remote confirmation: the complete proof and useful equality target are below. A separate expanded local Markdown file is being prepared for the verification package; no byte-identical separate-file GitHub upload is claimed. Older source/raw transfers remain pending.

**DEFERRED ADMIN:** older source/raw transfers; root README/reviewer integration; unrelated CI/status work; independent review, novelty and promotion.

**NEXT ACTION:** verify THIS universal-core theorem with explicit graph-deletion checks that include incomplete tight graphs and actually used singleton-pool replacement paths, plus a separately structured incidence/row checker and negative controls. Preserve exact outputs and honest coverage limits. After verification, investigate the L=beta=0, matching-hole equality target, rather than reverting to a scalar survivor scan. That further closure is not yet claimed.

**PROCESS RULE:** one bounded unit then preservation and one remote confirmation. No background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Complete preserved derivation: missing tight edges and the surviving universal core

### Definitions and canonical inputs

Let G be a finite diameter-two edge-critical graph, J its complement, and p a minimum-degree pivot of J. Put A=N_J(p), B=V(J) minus N_J[p], F=G[A]. Use exactly one actual quasi-edge representative (u,i)->v for each unordered edge uv of G[B]: ui is an edge of J and its endpoints together dominate J except for v. At a B-vertex u, S_u and R_u partition its A-neighbours in J into selected and residual edges, with rho_u=|R_u|. At an A-label i, R_i and x_i count its residual and selected incidences; s_i=max(0,deg_F(i)-R_i).

Assume the WHOLE levels T={i:s_i=d}, H={u:rho_u>=d} satisfy |T|=|H|=d>=3. The canonical bridge gives x_i>=s_i, selection eligibility s_i<=rho_u, distinct destinations at a source, domination of every A-label, and N_F(i) subset R_u union R_v for a selected (u,i)->v. The preceding canonical and interface proofs derive these from original graph criticality; they are not arbitrary numerical routing assumptions.

Every tight label is selected at all d high vertices and nowhere else. Define K=N_F(T) minus T. Tight-label domination puts every k in K in every high neighbourhood. Selecting k at a high source would need a destination containing all T while omitting k, impossible either low or high. Thus K is residual at every high source, and R_k>=d. A selected k has both endpoints low and satisfies deg_F(k)<=2d-2. In particular s_k<=d-2 for all k in K.

Let Q=F[T] and define FULL pools V_t={v outside H:R_v=T minus {t}}, sizes p_t>=1, m=sum_t p_t>=d. The actual tight destinations force these nonempty pools. For k in K write ell_k=|N_F(k) intersect T| and w_k=d at demand zero, otherwise d-1. The latter bound is valid because all its tight neighbours must be residual at a low selecting source. Let

    L=sum_K(w_k-ell_k),
    beta_t=R_t-(m-p_t), beta=sum_t beta_t,
    mu=binom(d,2)-e(Q), nu_t=d-1-deg_Q(t),
    D=L+beta+2mu.

These are nonnegative integers. Since deg_F(t)=d+R_t, the exact tight row is

    e_F(t,K)=1+m-p_t+beta_t+nu_t.                       (R1)

Summing gives

    e_F(T,K)=d+(d-1)m+beta+2mu,
    D=sum_K w_k-d-(d-1)m.                              (R2)

The inherited top-c weighted capacity W, c=min_H rho, has P=W-sum_K w_k>=0, and hence

    W-d-(d-1)m=P+D.                                    (R3)

On an actual block, its order-statistic weights simplify to d at outside-T demand zero, d-1 at demands 1,...,d-2, and zero otherwise: there are at least d low vertices of residual degree d-1. No simultaneous attainability of weights is asserted.

### Local covering restricted to untouched vertices

Let C={t in T:deg_Q(t)=d-1}, g=|C|. Mark t in C if some k in K has tight neighbourhood exactly {t}. Let Z be the marked vertices and U=C minus Z, with z=|Z| and u=|U|.

CLAIM: every K-label neighbours at most one vertex of U.

Suppose k neighbours distinct t,s in U. Both t and s are adjacent to every other tight vertex. Delete ts. Its endpoints keep the path t-k-s. Any destroyed path of length at most two has one endpoint t or s. Consider an exclusive neighbour x of s not adjacent to t.

If x is an A-label outside T, it lies in K. Since s is unmarked, x has another tight neighbour r. This r differs from t,s; t-r-x remains because t is universal in Q. If x is a B-vertex with two or more tight neighbours, the same argument works. A B-vertex with tight neighbourhood exactly {s} cannot be high, cannot select T, and must carry the other d-1 tight labels residually. Its low residual ceiling therefore puts it in V_s.

At x in V_s, kx is an edge of G. It cannot be residual in J because R_x=T minus {s}. It cannot be selected in J because both k and x miss the A-label s, violating domination of every A-label. Thus t-k-x remains. No other tight vertex can be an exclusive neighbour because t is universal. The pivot, high vertices and A-labels outside T union K have no tight G-neighbours. Reverse t and s to cover the other direction. These cases account for every possibly destroyed short path, contradicting edge-criticality.

This argument needs universality only at the two tested endpoints. Missing tight edges elsewhere are unrestricted. It is not the old clique assertion with its hypothesis removed.

### Count distinct labels and charge the missing edges

Put kappa=|K| and e_U=e_F(U,K). The claim makes every K-label meeting U count exactly once in e_U. At least z further distinct singleton labels witness the different marks and do not meet U. Thus

    kappa>=e_U+z.                                      (R4)

On U, nu_t=0. Sum (R1) to obtain

    e_U=u+(u-1)m+p_(T minus U)+beta_U.                  (R5)

If u<=1, at least g-1 universal vertices are marked when g>=1. Each distinct singleton label contributes at least d-2 to L. Therefore

    L+beta >= (d-2)max(0,g-1).                          (UC)

For g=0 this is simply nonnegativity.

If u>=2, use w_k>=d-1, u+z=g and (R2), (R4), (R5):

    D >= (d-1)g-d
         +(d-1)[(u-2)m+p_(T minus U)+beta_U].           (R6)

Since m>=d and each pool is nonempty, the bracket is at least (u-2)d+d-u >= d-2. Hence

    D >= (d-1)(g+d-2)-d.                               (R7)

All missing edges are confined to the d-g nonuniversal vertices, so 2mu <= (d-g)(d-g-1). Subtracting from (R7),

    L+beta >= (g-1)(d-2)+g(2d-g)-2d.

For 2<=g<=d, the final term is at least 2(d-2)>0: g(2d-g) is minimized on this interval at g=2. This proves (UC), strictly stronger in this case. The counting uses distinct labels and disjoint charged incidences, not repeated copies of an interface edge.

### Parameterized and uniform consequences

Each missing edge touches at most two vertices, so g>=max(0,d-2mu). Therefore

    D >= 2mu+(d-2)max(0,g-1)
      >= 2mu+(d-2)max(0,d-2mu-1).                     (R8)

For exactly one missing edge, g=d-2, giving

    D >= 2+(d-2)max(0,d-3).                            (R9)

To obtain D>=2floor(d/2), first consider 2mu>=d-1. Its even integer value is already at least 2floor(d/2). Otherwise 2mu<=d-2, and (R8) yields

    D >= (d-2)(d-1)-(d-3)2mu >= 2(d-2).

For d>=4 this is at least 2floor(d/2). At d=3, (R8) directly gives D>=2. The earlier d=2 singleton proof supplies that case separately. The numerical envelope achieves its minimum at mu=floor(d/2); this is not a graph construction or a sharpness claim.

Insert (R8) in (R3). For d=5 the generic increment is four, the exactly-one-missing-edge increment eight, and the clique increment twelve. The W lower bounds are respectively 29,33,37 using m>=d; when extras exist, m>=2d gives 49,53,57. No scalar state has been newly screened.

### Equality structure and the next mathematical target

For g>=2, equality in (UC) forces u=1, z=g-1, beta=0, exactly one positive-demand singleton label for each marked universal vertex, and zero weight loss on all other K-labels. The u>=2 case is strictly more expensive; the required singleton labels consume the whole equality allowance. These are necessary conditions, not realizations.

For d=5, equality at D=4 must have mu=2 and L=beta=0. Two missing edges sharing an endpoint leave g=2 and force D>=7. Therefore the two holes must be disjoint: Q=K5 minus a two-edge matching, with one universal vertex. This is a precise target for original criticality, not an unclassified scalar survivor.

A further possible route, NOT proved as a conclusion here, is to reuse the zero-loss neighbourhood partition at L=beta=0. Then K consists of common and positive-demand one-hole labels. If a common label is forced by exact counting, replacement paths may exclude the matching-hole boundary despite Q being incomplete. This candidate route must be separately checked and preserved after the present verification unit.

### Evidence and limitations

The new strict-surplus expression and numerical envelope were checked for d=3,...,99. New graph and incidence verification remains pending at this WIP checkpoint. The proof and both eventual implementations are by the same assistant; external acceptance, novelty, sharpness and coverage of configurations without an exact tight block remain open.

Sources: the canonical interface theorem at `4cb18222e4c0f56c2a5278f424c8414a09c469f7:CURRENT_STATE.md`; the clique theorem at `cf718afcba303618f2231b95d452b9af5671c8d8:project/research/general_n/2026-09-16-critical-edge-covering-v1/CRITICAL_EDGE_COVERING.md`; the zero-defect proof at `54f974fcff8acd85870deacc931da15ec4b11069:project/research/general_n/2026-09-16-zero-defect-closure-v1/ZERO_DEFECT_CLOSURE.md`; and the immediate d=2 predecessor at `6c5c979ea636316f3ad078b313314692e2ea1bbc`. Classical background only: Tao Wang, Ping Wang and Qinglin Yu, On Murty-Simon Conjecture II, arXiv:1301.0460 (2013). No literature-priority determination was performed.
