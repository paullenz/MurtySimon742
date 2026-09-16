# Exact tight blocks: interface capacity and critical-edge rigidity

**17 September 2026 · Internal candidate theorem; external review open.**
Research directed by Paul Lenz. Mathematical development and implementations by ChatGPT/Geeps.

## Theorem and scope

Let G be a finite simple diameter-two edge-critical graph. Construct the full selected-representative system defined below. Suppose that for some integer d>=5 its whole levels

    T={i in A:s_i=d},  H={u in B:rho_u>=d}

both have size d. With the full receiver pools, intrinsic defect D and scalar capacity W defined below,

    D >= 2 floor(d/2)+2,
    W >= d+(d-1)m+2 floor(d/2)+2.                 (1)

In particular W>=d^2+2 floor(d/2)+2. If a high source has an additional selection beyond T, then

    W >= d(2d-1)+2 floor(d/2)+2.                  (2)

For d=5 these say D>=6 and W>=31, or W>=51 with additional selections. There is no restriction on graph order or pool size and no positive-surplus assumption. **Existence of the exact block is a hypothesis, not a conclusion.** This is not a proof of the unrestricted Murty–Simon conjecture, a sharpness assertion, or a new finite-catalogue exclusion.

The proof below assembles the graph bridge, exact accounting, universal-core argument and two boundary closures. The first boundary reconstructs the previously reported star-forest argument; the one-defect closure is a new extension in this continuation. Older attachment bytes are not claimed recovered.

## 1. From the original graph to representatives

Write J for the complement of G. Choose a minimum-degree vertex p of J and put A=N_J(p), B=V(J) minus N_J[p], a=|A|, and F=G[A]. For each edge uv of G[B], choose exactly one cross-edge ui of J, reversing u,v when necessary, such that

    N_J(u) union N_J(i)=V(J) minus {v}; write (u,i)->v.

This representative exists by criticality. Adding uv to J creates an adjacent total-dominating pair: a pair at distance greater than two after deleting uv in G supplies it. No such pair existed in J. The new pair uses u or v, is not {u,v} because both miss p, and its other endpoint must lie in A to dominate p. Its pre-existing cross-edge therefore has exactly the other B-endpoint as its unique exception.

Select one representative per unordered B-edge. A selected cross-edge has a unique exception, so distinct labels at one source have distinct destinations; opposite orientations of the same B-pair are not both selected. At u in B partition its J-neighbours in A into selected S_u and residual R_u; put rho_u=|R_u|. At i in A, x_i and R_i count selected and residual incidences. Thus R_i is a number, whereas R_u is a set. Put delta_i=deg_F(i) and s_i=max(0,delta_i-R_i). Minimum pivot degree gives

    deg_J(i)=a-delta_i+R_i+x_i>=a, hence x_i>=s_i.

For (u,i)->v, another selection (u,j)->w has w!=v. Its quasi-edge dominates v, forcing jv in J. A selection at v cannot have exception u, so it dominates u. Consequently

    S_u minus {i} subset N_J(v),  S_v subset N_J(u).

For j in N_F(i), domination forces uj in J. If it is residual, charge j at u. Otherwise j is selected at u and jv is present by the first containment. Both j and v miss i in J, so jv cannot be selected; it is residual. Therefore

    N_F(i) subset R_u union R_v.                       (3)

For the scalar injection, let w be the destination of a selected j in N_F(i). Domination by (u,i) forces iw in J. Both i and w miss j, so iw is residual. Distinct j have distinct w. Charge the other neighbours at u to obtain

    delta_i<=rho_u+R_i, hence s_i<=rho_u.               (4)

These are facts about the actual graph and actual representatives, not arbitrary numerical routings.

## 2. Exact block and interface accounting

Each tight label has at least d selected sources by x_i>=s_i and exactly d eligible sources by (4). Thus every high vertex selects all T and no low vertex selects a tight label. A tight destination omits its selected label t and contains the other d-1 tight labels residually. It is low, and its complete residual set is T minus {t}.

Define the **full**, possibly partly unused pools

    V_t={v outside H:R_v=T minus {t}}, p_t=|V_t|,
    V=union_t V_t, m=sum_t p_t.

Every p_t>=1, the pools are disjoint, and m>=d. Let K=N_F(T) minus T and c=min_H rho. Domination puts every K-label in every high J-neighbourhood. None can be selected there: its destination would contain all T, impossible if low; if high, the K-label is already present, contradicting exception absence. Hence K is residual at H, |K|<=c, and R_k>=d.

If s_k>0 for k in K, choose a selected occurrence. Both its endpoints are low. Equation (3) gives delta_k<=2d-2, so s_k<=d-2. Its ell_k=|N_F(k) intersect T| tight neighbours must all be residual at the low source, so ell_k<=d-1. At zero demand use ell_k<=d. Assign every label i outside T the scalar weight

    w_i=d if s_i=0; d-1 if 1<=s_i<=d-2; 0 otherwise.

Define W as the sum of the largest min(c,|A minus T|) weights. For k in K, ell_k<=w_k and its weight is at least d-1. This agrees with the earlier low-degree order-statistic definition because the d nonempty pools supply at least d low vertices of residual degree d-1.

Put Q=F[T], mu=binom(d,2)-e(Q), nu_t=d-1-deg_Q(t), and

    beta_t=R_t-(m-p_t), beta=sum_t beta_t,
    L=sum_K(w_k-ell_k), P=W-sum_K w_k, D=L+beta+2mu.

All are nonnegative integers. The exact row and its sum are

    e_F(t,K)=1+m-p_t+beta_t+nu_t,
    sum_K w_k=d+(d-1)m+D,
    W-d-(d-1)m=P+D.                                    (5)

For the stronger threshold (2), an extra selection at a high source has a high destination: otherwise all T would be residual at a low vertex. Its endpoints cannot share a tight receiver. If v were shared, forward containment would put the extra label at v; since R_v is contained in T, that label would be selected at v. Reverse containment from the other high endpoint would then put it at its own exception, a contradiction. Thus an extra edge needs two different vertices in every pool: m>=2d.

## 3. The universal-core lower bound

Let C_Q be the g universal vertices of Q. Mark t in C_Q if some K-label has tight support exactly {t}. Write Z for the marked vertices, U=C_Q minus Z, z=|Z|, u=|U|. Each K-label meets at most one vertex of U.

To prove this, suppose k meets distinct t,s in U and delete ts. The endpoints retain t-k-s. For an exclusive neighbour x of s, if x lies in A outside T, it belongs to K and has another tight neighbour r because s is unmarked. Universality of t gives t-r-x. A B-vertex with at least two tight neighbours has the same replacement. A B-vertex with exactly s as tight neighbour belongs to the full pool V_s: its other d-1 tight incidences are residual and exhaust its low residual degree. Then kx is an edge of G. It is not residual in J because R_x=T minus {s}; it cannot be selected because k and x both miss s in J. Use t-k-x. The pivot and high vertices have no tight G-neighbours; no other tight vertex is exclusive because t is universal. Reverse t,s. All potentially destroyed short paths are covered, contradicting criticality.

Let kappa=|K| and e_U=e_F(U,K). Distinct labels are required for its e_U incidences and the z marked singletons, so kappa>=e_U+z. The rows in (5), with nu_t=0 on U, give

    e_U=u+(u-1)m+sum_(t outside U)p_t+sum_(t in U)beta_t.

If u<=1, at least g-1 marked singletons each cost at least d-2 in L. If u>=2, use w_k>=d-1 and m>=d to obtain

    D >= (d-1)g-d+(d-1)[(u-2)m+sum_(t outside U)p_t
                                      +sum_(t in U)beta_t]
      >= (d-1)(g+d-2)-d.

All missing tight edges lie outside C_Q, hence 2mu<=(d-g)(d-g-1). Subtracting gives

    L+beta >= (g-1)(d-2)+g(2d-g)-2d
             > (g-1)(d-2)              when u>=2.

Here g>=2 and the extra term is at least 2(d-2). Together with the first case,

    L+beta >= (d-2)max(0,g-1),
    D >= 2mu+(d-2)max(0,d-2mu-1).                      (6)

The second line uses g>=d-2mu. Write r=2 floor(d/2). If 2mu>=d-1, its even value is at least r. Otherwise (6) gives D>=2(d-2)>=r for d>=5. Thus D>=r.

## 4. A reusable bounded-hole deletion lemma

Suppose a vertex c0 outside T neighbours every tight vertex. Every other external vertex either has no tight neighbour, misses at most h tight vertices, or has one tight neighbour and is adjacent to c0. **Any edge ts of Q whose endpoint degrees are both at least h+1 is noncritical.**

Indeed t,s retain t-c0-s. An affected pair t,x has x an exclusive neighbour of s. If x is tight, use t-c0-x. If x is a protected singleton neighbour, use that same path. Otherwise x misses t and at most h-1 other tight vertices. At least h vertices lie in N_Q(t) minus {s}, so one, r0, neighbours x; use t-r0-x. Reverse t,s. Any destroyed path of length at most two uses ts and has one of these forms. Arbitrary edges among external vertices do not affect the argument.

When L=beta=0, all K-labels have full or one-hole tight support. All residual tight incidences outside H are exhausted in V; remaining B-vertices therefore neighbour all T. Any common K-label c0 neighbours every pool vertex: it cannot be selected at H, and cannot be selected at a low vertex because domination would force all d tight labels into fewer than d residual slots. It is not residual in a full pool either.

Consequently, if a common label exists, the lemma with h=1 says every Q-edge has a degree-one endpoint. Each nontrivial component is a star; a shortest path between two vertices of degree at least two would otherwise contain a forbidden edge. Hence

    e(Q)<=d-1, 2mu>=(d-1)(d-2).                         (7)

A common label is required here; it is forced at the following boundaries, not asserted for every zero-loss configuration.

## 5. Closing both lowest numerical boundaries

Suppose D is r or r+1. Since 2mu is even and at most r, either 2mu=r or 2mu<=r-2. In the latter case (6) is at least 2d-4 for even d>=6, or 3d-7 for odd d>=5. Both exceed r+1. Thus

    2mu=r, L+beta=D-r.                                 (8)

For D=r, L=beta=0. Let a0 be the number of zero-demand K-labels. Equation (5) gives

    (d-1)kappa+a0=d+(d-1)m+D.                           (9)

At zero loss a0 equals the common-label count. For odd d, (9) gives a0=1 modulo d-1; for even d it gives a0=2 modulo d-1. A common label exists, so (7) contradicts 2mu=r< (d-1)(d-2). Therefore D>=r+1.

Now suppose D=r+1, so L+beta=1. From (6), g<=1. The missing-edge graph on T has d-g nonisolated vertices and total degree r. Each nonisolated vertex has degree at most r-(d-g-1): at most one for odd d, and at most two for even d. Therefore every Q-degree is at least d-2 in the odd case or d-3 in the even case, and in either case at least three.

Equation (9) now gives a0=2 modulo d-1 for odd d and a0=3 modulo d-1 for even d. Since L<=1, at most one zero-demand K-label fails to be common. Thus at least one common label c0 exists and, as above, protects every singleton pool.

Each K-label has ell_k>=w_k-L>=d-2. Every B-vertex outside H union V selects no tight label; each missing tight neighbour there is a residual incidence counted in beta. It therefore misses at most one tight vertex. High vertices, the pivot, and A-labels outside T union K have no tight neighbours. Pool vertices are protected singletons. The **entire graph** consequently satisfies the h=2 lemma. Every tight edge has endpoint degrees at least three and is noncritical, a contradiction. Hence D>=r+2. Equations (5), m>=d and the extra-selection implication m>=2d prove (1) and (2).

## 6. Verification, provenance and remaining obligations

The general proof is the argument above. Fresh finite checks support its two local deletion steps; they do not replace it. Python bitset reachability and C++ explicit intermediate-vertex search agree on **324,554 h=1 records** and **407,741 h=2 records**. The positive families exhaust all labelled distinguished-edge tight graphs with the relevant endpoint degrees through d=6, and every allowed single-probe support. Only pairs touching the deleted edge can lose a short path, which explains the probe design. These are not full canonical exact-block graph censuses.

Each family includes five diameter-two controls where dropping an essential premise destroys a short path. Integer boundary calculations were checked for d=5,...,1000. Both implementations and the proof are by the same assistant, not independent external reviewers. The older 11,357-record universal-core replay was not rerun in this package.

Run `python3 check_star_forest.py` and `python3 check_hole_budget.py` in this directory. Python 3.10+ and a C++17 compiler suffice. Both commands regenerate complete inputs, per-record decisions, gzip copies and summaries. Published summary hashes identify the exact streams; the downloadable package includes those generated streams. No old recovery bundle is needed for these new tests.

The graph bridge and original capacity proof are pinned at `4cb18222e4c0f56c2a5278f424c8414a09c469f7:CURRENT_STATE.md`. The universal-core proof is pinned at `3353576e458b1ccfd025a38bfb06eb3b5c6e5dc5:project/research/general_n/2026-09-16-universal-core-defect-v1/UNIVERSAL_CORE_DEFECT.md`. The reconstructed star proof and first checks are at `072b24bfbd256b0d941725460e944da7cb402eae`; the new one-defect derivation was preserved before testing at `d9cbdec625fb841cac47a435bd409b60ab077e1f`.

Classical background: Tao Wang, Ping Wang and Qinglin Yu, *On Murty-Simon Conjecture II*, arXiv:1301.0460 (2013), https://arxiv.org/abs/1301.0460. This reference supplies background, not a claim of priority for this argument. A full novelty investigation remains open.

**Next mathematical obligation:** determine the actual-graph structure at d=5,D=6 without assuming away L or beta. More broadly, configurations without the exact-block hypothesis still require a justified structural treatment. Independent review should first challenge representative existence, the two residual injections, full-pool coverage, the universal-core distinct-label count, and the exhaustive external-neighbour classification in the one-defect closure. Canonical counts and all promotion gates are unchanged.
