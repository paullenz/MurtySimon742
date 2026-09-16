# Critical-edge covering and a quadratic clique-defect bound

**16 September 2026. Internal hand proof and finite verification; not promoted. External review and novelty assessment remain open.**

Research directed by Paul Lenz; mathematical derivation and implementations by ChatGPT/Geeps. Canonical repository: `paullenz/MurtySimon742`. The inspected starting head was `54f974fcff8acd85870deacc931da15ec4b11069`; the derivation was preserved before verification at `80a783799a9a671e9b29356284515bad0402a3ce`.

## Result and scope

The defect-one question admits a more general answer for tight blocks of size at least three. In the full canonical representative system of a diameter-two edge-critical graph, assume

    T={i:s_i=d}, H={v:rho_v>=d}, |T|=|H|=d>=3.

Let L be the tight-neighbour capacity loss, beta the extra tight residual count outside the full receiver pools, and mu the number of missing edges in F[T], as defined below. Then

    F[T] complete  ==>  L+beta >= (d-1)(d-2).             (1)

Consequently, without assuming F[T] complete,

    L+beta+2mu >= 2.                                     (2)

Thus intrinsic defect one is excluded for **every d>=3 and every full-pool size**, not merely for the examples retained in a finite catalogue. The proof does not require positive pivot surplus. It uses criticality of all original graph edges, not just local representative feasibility.

For the weighted capacity W and full-pool count m from the preceding theorem, (1) gives

    W >= d+(d-1)m+(d-1)(d-2) when F[T] is complete.       (3)

In particular W>=d^2+(d-1)(d-2); if extra high-source selections exist, W>=d(2d-1)+(d-1)(d-2). At d=5 these bounds are **37 and 57**. Without completeness, (2) instead gives the smaller bounds **27 and 47** at d=5. The quadratic increment must not be applied to an incomplete tight graph.

The d=2, L=1 exception remains unresolved in the full graph class. Nor does this theorem assert that all graphs of interest have an exact block, or that larger-defect blocks are impossible. It is a structural necessary-condition theorem with a complete proof of its stated scope, not a proof of the unrestricted Murty–Simon conjecture.

## 1. Setup and inherited facts, with their role made explicit

Let G be a finite simple diameter-two graph whose every edge deletion increases the diameter. Write J for its complement. Choose a minimum-degree vertex p of J, let A=N_J(p), and put B=V(J) minus N_J[p] and F=G[A]. For every unordered edge uv of G[B], choose exactly one cross-edge ui of J satisfying

    N_J(u) union N_J(i)=V(J) minus {v},                   (4)

after orienting uv as necessary. This exists because deleting uv creates a pair at distance greater than two; in the complement the corresponding new adjacent total-dominating pair must use an endpoint and a label in A. Write (u,i)->v for the chosen representative. Distinct labels at one source have distinct destinations, and opposite orientations of one B-pair are not both chosen.

At a B-vertex u, partition its A-neighbours in J into selected S_u and residual R_u, and put rho_u=|R_u|. At an A-label i, let R_i and x_i be its residual and selected incidence counts. Define

    delta_i=deg_F(i), s_i=max(0,delta_i-R_i).

The scalar R_i and set R_u are different objects. The graph-to-interface proof at the preserved predecessor derives

    x_i>=s_i;  i in S_u implies s_i<=rho_u;
    N_F(i) subset N_J(u);
    N_F(i) subset R_u union R_v for (u,i)->v.             (5)

The last inclusion follows by charging a residual F-neighbour at u there, and charging a selected F-neighbour at u to a forced residual occurrence at v. Such a cross-edge at v cannot be selected because both its endpoints miss i in J. Minimum degree of p gives the first inequality. The separate injection into source residual incidences and residual occurrences of label i gives eligibility. These full proofs remain in the base theorem; no freely invented or demand-thinned routing is substituted.

Under the exact whole-level hypothesis, every tight label is selected at all d high vertices and nowhere else. Put

    K=N_F(T) minus T.

Every k in K is residual at every high vertex: tight-label domination puts it in every high neighbourhood, while selecting it there would require a destination both containing all T and omitting k, which neither a low nor a high vertex can supply. Hence R_k>=d. A selected k has both endpoints low; (5) gives delta_k<=2d-2 and therefore s_k<=d-2.

Define the **full** pools

    V_t={v outside H:R_v=T minus {t}}, p_t=|V_t|,
    V=union_t V_t, m=sum_t p_t.

The actual tight destinations force every p_t>=1 and m>=d. Each low vertex has rho<=d-1 and selects no tight label. The preceding order-statistic weights consequently simplify on an actual block to

    w_k=d if s_k=0, and w_k=d-1 if s_k>0, for k in K.    (6)

There are at least d low vertices of degree d-1, so all required low-degree order statistics equal d-1. In particular w_k>=d-1. Let ell_k=|N_F(k) intersect T| and define

    L=sum_K(w_k-ell_k),
    beta_t=R_t-(m-p_t), beta=sum_t beta_t,
    mu=binom(d,2)-e(F[T]).

All are nonnegative integers. With W the top-c weighted capacity, c=min_H rho, the earlier exact identity is

    W-d-(d-1)m=P+L+beta+2mu, P=W-sum_K w_k>=0.           (7)

Only the original graph construction and these stated consequences are used below.

## 2. An edge-covering restriction from original criticality

Assume F[T] is complete. First note a useful saturation consequence:

> If k in K is adjacent to t in F, then k is adjacent in G to every vertex of V_t.

Indeed k cannot be residual at such a vertex x, since R_x=T minus {t}. It cannot be selected there either: both k and x miss t in J, contradicting domination of every A-label by a selected cross-edge. Thus kx is absent in J and present in G.

Mark a tight vertex when some interface label has it as its only tight neighbour:

    Z={t in T: N_F(k) intersect T={t} for some k in K},
    U=T minus Z, z=|Z|, u=|U|.

**Covering lemma.** Every k in K has at most one neighbour in U.

Suppose otherwise, and choose distinct t,s in U with a common K-neighbour k. Delete the tight edge ts. Its endpoints retain a two-step path through a third tight vertex, since d>=3. An exclusive neighbour x of s, not adjacent to t, is handled as follows.

If x lies in A, it lies in K. Since s is unmarked, x has a second tight neighbour r. This r differs from s and t, and t-r-x is a replacement path. If x lies in B with at least two tight neighbours, the same argument applies. A B-vertex with only s as a tight G-neighbour cannot be high. All d-1 other tight labels must be residual there, so its low degree ceiling forces its residual set to be exactly T minus {s}; it lies in V_s. The saturation consequence gives the replacement path t-k-x. High vertices, the pivot, and A-labels outside T union K have no tight G-neighbours and cannot be exclusive neighbours of s.

Reverse t and s for the other exclusive neighbours. Every destroyed path of length at most two using ts has one endpoint t or s; the preceding cases and the endpoint pair cover them all. Thus deletion preserves all distances that were at most two, contradicting edge-criticality. This proves the lemma. It does not assert that the listed marks are all possible private witnesses of G.

## 3. Count distinct labels rather than repeated incidences

Write kappa=|K|, e_U=e_F(U,K), p_Z=sum_(t in Z)p_t and beta_U=sum_(t in U)beta_t. By the covering lemma, each label meeting U contributes exactly one edge to e_U. At least z further, distinct singleton labels witness the z different marks. None meets U. Therefore

    kappa>=e_U+z.                                       (8)

The exact tight-row equation, using completeness of F[T], is

    e_F(t,K)=delta_t-(d-1)=1+m-p_t+beta_t.

Summing over U yields

    e_U=u+(u-1)m+p_Z+beta_U.                             (9)

Also e_F(T,K)=d+(d-1)m+beta and every w_k>=d-1. Substituting (8) and (9) gives

    L+beta = sum_K w_k-d-(d-1)m
           >=(d-1)kappa-d-(d-1)m
           >=d(d-2)+(d-1)[(u-2)m+p_Z+beta_U].           (10)

If u>=2, the bracket is nonnegative; thus L+beta>=d(d-2). If u<=1, then z>=d-1, and each of the z distinct singleton labels has ell=1 and contributes at least d-2 to L. Hence L+beta>=(d-1)(d-2). These two cases prove (1).

If mu>=1, its contribution 2mu already proves (2); if mu=0, (1) is at least two for d>=3. Combining with (7) proves (3) and the unqualified two-unit bound. Extra high-source selections still force at least two vertices in every pool by the previously proved actual-destination colouring argument; that is the sole additional input in the E>0 thresholds.

## 4. Equality gives a precise remaining structure

Equality in (1) is possible only if u=1, z=d-1, beta=0, there is exactly one singleton K-label at each marked tight vertex, each such label has positive demand, and every other K-label has zero weight loss. Indeed u>=2 or u=0 would cost at least d(d-2), which is strictly larger. With u=1, all permitted loss is already consumed by the d-1 required singleton labels.

This is not an arithmetic contradiction. An explicit **incidence-only** equality family exists. Choose one unmarked tight vertex a and arbitrary positive pool sizes p_t. Use one common label; one positive-demand singleton label for each t different from a; p_t positive-demand one-hole labels missing t for each t different from a; and p_a-1 such one-hole labels missing a. These incidence tables satisfy the exact rows with beta=0 and have L=(d-1)(d-2). They are not canonical graph constructions: the remaining F-neighbours, full representative identities, residual incidences and all-edge criticality are not supplied. This prevents overstating the reach of the arithmetic portion of the proof.

## 5. The d=2 exception is retained, not discarded

For d=2 all K-labels have zero demand. Also beta=0 automatically: any tight residual occurrence at a low vertex fills its sole residual slot and places it in one of the full pools. Thus the putative intrinsic-defect-one case has exactly one singleton K-label and all remaining K-labels common; F[T] is complete.

Writing the common-label count as c and orienting the singleton towards s, the exact rows force p_t=c and p_s=c-1, so c>=2. The only tight edge may have that singleton as a private witness. A diameter-two **local graph control** and a matching incidence table preserve precisely this possibility; neither is asserted to provide a full canonical edge-critical graph. The actual d=2 exception remains an explicit next proof obligation.

## 6. Verification and limitations

Python reachable-within-two sets and separately structured C++ explicit-path checks agree on 10,333 graph records. These comprise 10,088 exhaustive local completions, 240 seeded varied completions and five controls. There are 9,712 eligible edge deletions, exercised by 4,316 graphs, with no lost previously short pair. Of all records, 6,643 have diameter two before deletion. Four negative controls show destructive deletions when the common-label, singleton-mark, full-pool adjacency or tight-clique premise is dropped. The fifth retains the d=2 private-witness exception.

The independent incidence calculations agree on 496,070 records, including 496,028 feasible row/pool assignments from the exhaustive d=3 support-multiset search, 39 equality controls for d=3 through 15, the d=2 boundary and two malformed-hypothesis controls. In total the two implementations agree on **506,403 exact records**. Input and decision digests, complete compressed streams and executable sources are preserved. Replay uses `python3 check_covering.py --replay-only`; omitting that flag regenerates the finite cases.

These are checks of the local deletion lemma and the incidence relaxation, not an enumeration of original canonical graphs or a survivor census. Both implementations and the proof are by the same assistant. Early bounded combined-driver invocations expired; a separate complete replay, followed by the delivered replay command, succeeded. Interrupted invocations are not counted as successful checks. No catalogue count, promotion, independent acceptance, graph-realisation claim or literature novelty is inferred.

## Sources and continuation

The graph-to-interface theorem is preserved at `4cb18222e4c0f56c2a5278f424c8414a09c469f7:CURRENT_STATE.md`. The zero-defect predecessor is `project/research/general_n/2026-09-16-zero-defect-closure-v1/ZERO_DEFECT_CLOSURE.md` at `54f974fcff8acd85870deacc931da15ec4b11069`. For classical background, Tao Wang, Ping Wang and Qinglin Yu, *On Murty-Simon Conjecture II*, arXiv:1301.0460 (2013), describes the complement/quasi-edge framework: https://arxiv.org/abs/1301.0460. It is not claimed to contain the present argument; no literature-priority determination has been made.

The next bounded unit should resolve the isolated d=2 exception using full representative identities and original criticality, or characterise the remaining graph family precisely. The broader next route is to quantify which additional private witnesses become possible when F[T] is incomplete. The clique theorem cannot be exported to that regime without a new argument.
