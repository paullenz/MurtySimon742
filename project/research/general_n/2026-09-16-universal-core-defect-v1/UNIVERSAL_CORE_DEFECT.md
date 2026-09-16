# Missing tight edges and the surviving universal core

16 September 2026. Research directed by Paul Lenz; internal derivation by ChatGPT/Geeps.

**Status: internal hand proof with completed finite checks; not promoted. External review remains open.**
The inspected starting head of `paullenz/MurtySimon742` was
`6c5c979ea636316f3ad078b313314692e2ea1bbc`.

## 1. Statement and precise scope

Use the full canonical representative system of a finite diameter-two edge-critical graph G. With the notation below, assume the whole levels

    T={i:s_i=d}, H={v:rho_v>=d}, |T|=|H|=d>=3.

Let Q=G[T]. Let g be the number of vertices of T adjacent in Q to every other tight vertex, and let mu be the number of missing Q-edges. For the established nonnegative capacity loss L and extra tight residual count beta, the new necessary inequality is

    L+beta >= (d-2) max(0,g-1).                         (UC)

It follows that the intrinsic defect D=L+beta+2mu satisfies

    D >= 2mu+(d-2) max(0,g-1)
      >= 2mu+(d-2) max(0,d-2mu-1).                    (1)

The second form needs only the number of missing edges, since each can affect at most two vertices. This is a parameterized extension, not an application of the old clique bound to an incomplete graph.

For exactly one missing edge, g=d-2 and

    D >= 2+(d-2) max(0,d-3).                           (2)

For arbitrary Q, integer minimization in (1) gives

    D >= 2 floor(d/2), d>=3.                           (3)

The prior separately proved d=2 closure supplies (3) at d=2 as well; this note does not reprove that exceptional case.

In the weighted capacity notation of the base theorem,

    W >= d+(d-1)m+2mu+(d-2)max(0,g-1).                 (4)

In particular the uniform increment is 2 floor(d/2). Extra high-source selections imply m>=2d, as before. At d=5 the increments for arbitrary Q, exactly one missing edge, and complete Q are respectively 4, 8, and 12. The W thresholds are respectively 29/49, 33/53, and 37/57, where the second entry requires extras. These are necessary conditions, not catalogue exclusions or graph realizations.

## 2. Construction, weights and exact rows

Write J for the complement of G. Choose a minimum-degree pivot p of J, set A=N_J(p), B=V(J) minus N_J[p], and F=G[A]. For every edge uv of G[B], choose exactly one cross-edge ui of J whose endpoints together dominate every vertex of J except v, orienting uv when necessary. Write (u,i)->v. At u, partition its A-neighbours in J into selected S_u and residual R_u, with rho_u=|R_u|. At i in A let R_i and x_i count residual and selected incidences, and put s_i=max(0,deg_F(i)-R_i).

The canonical construction gives x_i>=s_i, source eligibility s_i<=rho_u at a selected incidence, different destinations for different selections at one source, domination of every A-label, and the residual-union implication N_F(i) subset R_u union R_v. These are actual graph representatives, not arbitrary numerical routings. Minimum pivot degree gives the demand inequality; the endpoint residual injection gives eligibility and the union implication. The complete prior derivations are pinned under Sources.

Every tight label is selected at all d high vertices and nowhere else. Let K=N_F(T) minus T. Tight-label domination puts K in every high neighbourhood. No high vertex can select k in K: its destination would have to contain all T while omitting k, impossible both low and high. Hence K is residual at every high vertex and R_k>=d. A selected k has both endpoints low, so deg_F(k)<=2d-2 and s_k<=d-2.

Define the full pools

    V_t={v outside H:R_v=T minus {t}}, p_t=|V_t|,
    V=union_t V_t, m=sum_t p_t.

The actual tight destinations force every p_t>=1. A low vertex selects no tight label and has at most d-1 residual incidences. For k in K write ell_k=|N_F(k) intersect T| and w_k=d if s_k=0, otherwise w_k=d-1. Then ell_k<=w_k: a selected positive-demand k needs all its tight neighbours residual at a low source. Define

    L=sum_K(w_k-ell_k),
    beta_t=R_t-(m-p_t), beta=sum_t beta_t,
    mu=binom(d,2)-e(Q), nu_t=d-1-deg_Q(t).

These quantities are nonnegative integers. The exact tight row is

    e_F(t,K)=1+m-p_t+beta_t+nu_t.                        (5)

Indeed deg_F(t)=d+R_t and deg_Q(t)=d-1-nu_t. Summing gives

    e_F(T,K)=d+(d-1)m+beta+2mu,
    D=L+beta+2mu=sum_K w_k-d-(d-1)m.                    (6)

For completeness, W is the sum of the largest min(c,|A minus T|) scalar weights, where c=min_H rho; the outside-T weights are d at demand zero, d-1 at demands 1 through d-2, and zero otherwise. This simplification is used only after the actual block supplies at least d degree-(d-1) low vertices. It agrees with the earlier order-statistic definition there. Since |K|<=c and all K labels have permitted demands, P=W-sum_K w_k>=0. Thus

    W-d-(d-1)m=P+D.                                    (7)

## 3. Cover only the tight vertices untouched by missing edges

Let C be the g universal vertices of Q. Mark t in C when some k in K has tight neighbourhood exactly {t}. Write Z for the marked vertices and U=C minus Z, with z=|Z| and u=|U|.

**Local covering lemma.** Each k in K neighbours at most one vertex of U.

Suppose k neighbours distinct t,s in U. Both endpoints are adjacent to all other tight vertices. Delete ts. Its endpoints retain a two-step path through k (or a third tight vertex). Any destroyed path of length at most two has one endpoint t or s. Consider an exclusive neighbour x of s which is not adjacent to t.

If x is in A outside T, it lies in K. As s is unmarked, x has another tight neighbour r. This r is neither t nor s, and t-r-x is a replacement path because t is universal. If x lies in B and has at least two tight neighbours, the same path works. If a B-vertex has exactly s as a tight neighbour, it is low and all other d-1 tight labels are residual there. The degree ceiling therefore places it in the FULL pool V_s.

For x in V_s, kx is an edge of G. It cannot be residual in J because R_x=T minus {s}; and it cannot be selected in J because both k and x miss s there, contrary to domination of all A-labels. Thus t-k-x is a replacement. The pivot, high vertices and labels outside T union K have no tight G-neighbours. No other tight vertex is an exclusive neighbour, since t is universal. Reverse t and s for the other direction. Every potentially destroyed short path is accounted for, so ts was not critical: a contradiction.

This proof does not assume Q complete. It uses universality only at the two endpoints being tested. Missing edges among the other tight vertices are unrestricted.

## 4. Distinct-label accounting

Let kappa=|K| and e_U=e_F(U,K). The lemma shows that each K-label meeting U contributes exactly one incidence to e_U. At least z further distinct singleton labels witness Z, and none meets U. Therefore

    kappa>=e_U+z.                                      (8)

For universal t, nu_t=0. Summing (5) over U gives

    e_U=u+(u-1)m+p_(T minus U)+beta_U.                  (9)

If u<=1, then z>=g-1 whenever g>=1. The z distinct singleton labels each cost at least d-2 in L. This proves (UC) in this case; g=0 is trivial.

Suppose u>=2. As w_k>=d-1 and u+z=g, equations (6), (8), (9) yield

    D >= (d-1)g-d
         +(d-1)[(u-2)m+p_(T minus U)+beta_U].           (10)

Since m>=d and every pool is nonempty, the bracket is at least d-2. Consequently

    D >= (d-1)(g+d-2)-d.                               (11)

All missing edges have both endpoints outside C, so 2mu<=(d-g)(d-g-1). Subtracting this upper bound from (11) gives

    L+beta >= (g-1)(d-2)+g(2d-g)-2d.

For 2<=g<=d, the last term is at least 2(d-2)>0: the expression g(2d-g) increases on this integer interval and is smallest at g=2. This proves (UC), with strict surplus in this branch. No label incidence or residual pool is charged twice.

## 5. Scalar corollaries and equality information

Since g>=max(0,d-2mu), equation (1) follows. Exactly one missing edge affects exactly two tight vertices, giving (2).

For (3), if 2mu>=d-1, its even integer value is at least 2 floor(d/2). Otherwise 2mu<=d-2 and (1) gives

    D >= (d-2)(d-1)-(d-3)2mu >= 2(d-2).

For d>=4 this is at least 2 floor(d/2). At d=3, (1) directly gives D>=2. The claimed minimum of this numerical envelope is attained at mu=floor(d/2), but no graph attainability follows.

When g>=2, equality in (UC) forces u=1, z=g-1, beta=0, exactly one positive-demand singleton label at each marked universal vertex, and zero weight loss on all other K-labels. This follows because the u>=2 branch is strictly more expensive and the g-1 singleton labels consume the entire remaining allowance. These are necessary consequences only.

For d=5, equality at the UNIFORM defect bound D=4 would force mu=2, g=1, L=beta=0, and the two missing edges to be disjoint. The clique and one-missing-edge cases cost more; two missing edges sharing an endpoint give g=2 and cost at least seven. Thus the new lower-bound equality has a precise structural target, Q=K5 minus a two-edge matching, not an unspecified list of scalar survivors.

## 6. Executed verification and the next target

The full symbolic derivation was committed before this verification at `963ae4ac78ca0a48a1cbc782b3ab160cc0bbfb59:CURRENT_STATE.md`.

Python bitset reachability and a separately structured C++ explicit-path implementation agree on all **11,357 exact records**. Graph inputs comprise 1,126 eligible exhaustive completions, 270 seeded larger completions, and three destructive negative controls. Exhaustive generation inspected all 33,856 labelled graphs of orders 4 through 6 with fixed distinguished roles. The 1,396 eligible deletions include **431 incomplete tight graphs**, **498 cases requiring singleton-pool protection**, and **259 cases exercising both at once**. Thus the extension beyond complete tight graphs is actually tested. Of the 1,399 graph records, 1,071 have diameter two; the lemma more generally preserves all pairs previously within distance two.

The incidence stream contains 9,958 records. Of these, **9,957 satisfy the row and covering premises**, including **7,072 incomplete tight graphs** and **334 with at least two unmarked universal vertices**, exercising the less immediate counting branch. The generator exhausts 27,027 support/weight multisets of sizes three through six for d=3, all tight graphs there, and beta_t in {0,1}; only feasible row/pool records are retained. It adds 780 seeded row systems for d=3 through 15. One feasible-row control deliberately violates the covering premise and the claimed conclusion, demonstrating that the row equations alone are insufficient.

The three graph controls keep diameter two and exhibit a destructive deletion after dropping, separately, universality of the first endpoint, universality of the second, or protection of singleton-support vertices. They are controls, not counterexamples to the proved lemma. Both implementations agree on every per-record decision, not merely aggregate counts. The numerical envelope and strict-surplus inequality were additionally checked for d=3 through 99.

Input SHA256: `ab9ed63d9caa99b5fbd237fc6b238f77b69a8dc893ff17a764f96ff5cc9ab4bb`.
Decision SHA256, in both languages: `c4859538b56444860b26fdc46e40f68bf21b4c65b68dce2e394b531c621ba82a`.

These are finite checks of a local graph lemma and an incidence relaxation, NOT an original canonical graph census, a survivor replay or independent expert acceptance. Both implementations and the proof are by the same assistant. They do not validate inherited bridge claims by a fresh graph census, certify scalar graph realization, establish literature priority or prove the bound sharp.

Run `python3 check_universal_core.py` to regenerate and cross-check. Run `python3 check_universal_core.py --replay-only` to replay the stored input stream; the latter automatically expands its preserved gzip files. Python 3.10+ and a C++17 compiler are sufficient; no external Python package is needed.

The next mathematical target is the equality boundary, especially d=5, D=4: two disjoint missing tight edges and L=beta=0. The zero-loss neighbourhood partition makes K consist of common and positive-demand one-hole labels. If a common label is forced by exact counting, replacement paths may exclude that configuration despite Q being incomplete. This is an explicitly preserved proof target, not a further conclusion claimed here.

Configurations without an exact tight block, larger-defect closures, independent review, novelty, sharpness and catalogue promotion remain open.

## Sources and provenance

The immediate repository predecessor is `6c5c979ea636316f3ad078b313314692e2ea1bbc:CURRENT_STATE.md`. The verified clique covering theorem is `cf718afcba303618f2231b95d452b9af5671c8d8:project/research/general_n/2026-09-16-critical-edge-covering-v1/CRITICAL_EDGE_COVERING.md`. The graph-to-interface statement is at `4cb18222e4c0f56c2a5278f424c8414a09c469f7:CURRENT_STATE.md`. The zero-defect proof is at `54f974fcff8acd85870deacc931da15ec4b11069:project/research/general_n/2026-09-16-zero-defect-closure-v1/ZERO_DEFECT_CLOSURE.md`.

Classical background only: Tao Wang, Ping Wang and Qinglin Yu, *On Murty-Simon Conjecture II*, arXiv:1301.0460 (2013), https://arxiv.org/abs/1301.0460. It is not claimed to contain this argument. No literature-priority determination has been performed.
