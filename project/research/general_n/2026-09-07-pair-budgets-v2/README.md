# General-order pair budgets, continuation v2

7 September 2026. Directed by Paul Lenz; mathematical development, code and internal checking by ChatGPT/Geeps.

**Candidate mathematical derivations; finite arithmetic REPRODUCED; independent mathematical and computational review OPEN. No complete order above 27 is claimed resolved. No novelty or priority claim. No theorem-ledger promotion.** Frozen n=25/n=27 artifacts and general-n v1 are unchanged.

This continues `project/research/general_n/2026-09-07-residual-hindex-v1`, preservation commit `4bd48b12c6f5953af92adcb614f509b2aa06391a`. The earlier candidate maximum-degree threshold 0.630601937...n is unchanged. These new arguments address the remaining near-half-degree window.

## Results

The continuation derives an incoming supplement-capacity bound, a supplement-support inequality, and a source pair-degree/excess-selection inequality. It implements a coupled weighted-cover certificate finder and an exact integer Q-bound refinement. The standalone checker imports neither the search program nor third-party modules.

A deliberately constructed profile at (n,Delta,m)=(64,33,1031) passes the earlier tested cuts but fails 162<=160. Another profile at (44,23,485) admits an integral witness to the coupled static-capacity relaxation, but the new pair-degree lemma excludes the whole profile, including all extra-selection possibilities. Two infinite families of residual profiles are excluded symbolically. A further profile at (64,33,1025) remains unresolved by these tests.

**A profile is a necessary-condition relaxation, not an actual graph. Excluding these profiles does not settle all graphs at those orders.**

## 1. Inherited setup

For a non-bipartite diameter-two edge-critical graph G, put H=complement(G), n=|V(G)|, m=e(G), b=Delta(G), a=n-1-b. Stars and complete bipartite graphs are handled separately. Choose v of minimum H-degree a. Set A=N_H(v), B=V(H) minus N_H[v], C=H[A], F=complement(C) on A, with F-degrees d_i.

For each missing unordered pair {u,w} of H[B], select exactly one cross quasi-edge ui -> w, or wi -> u. The selected edge's endpoints totally dominate every vertex except its unique supplement. All other A-B edges are residual. Let r be their number, rho_u their B-degrees and R_i their A-degrees. The n=27 argument supplies

    t=m-b(n-b), e(F)=r+t,
    sum d_i=2(r+t), sum R_i=sum rho_u=r,
    d_H(i,B)>=d_i.

For each selected ui -> w it also supplies

    d_i<=rho_u+R_i,
    d_i<=rho_u+rho_w,
    d_i<=rho_u+q_u-1.

Here q_u is the number selected at source u. Selected labels and supplements at a source are distinct. At positive t every rho_u>=1, although the new counting lemmas below do not themselves require that activity conclusion.

Dependencies: n=27 `PROOF.md` Sections 4-8, blob `83e09e02918adf461470bf7e70177bad275b57d9`; published complement/quasi-edge correspondence in Haynes, Henning, van der Merwe and Yeo (2014), Theorems 3.1-3.2 and Observation 3.4, https://d-nb.info/1372516379/34 . This published dependency was not re-audited in this continuation. The broader dominating-edge reduction is Dailly, Foucaud and Hansberg (2019), https://arxiv.org/abs/1812.08420 .

## 2. Incoming capacity and support budget

Let P be the graph on B consisting of all missing pairs of H[B]. Orient each pair from its selected source to its supplement. Write q_u=outdegree, p_u=indegree and sigma_u=q_u+p_u. P is simple, has Q selected pairs, and sum q_u=sum p_u=Q, sum sigma_u=2Q.

Since u has rho_u+q_u A-neighbours, b-1-q_u-p_u neighbours in H[B], and no edge to v,

    d_H(u)=b-1+rho_u-p_u >= a.

Therefore, with ell=b-a-1=2b-n,

    p_u<=rho_u+ell.                                      (1)

The checker also uses p_u<=b-1. Define s_i=max(0,d_i-R_i), Q0=sum s_i. Actual selected label degrees x_i satisfy x_i>=s_i, so Q>=Q0>=r+2t.

If every possible supplement lies in W subset B, then

    Q0<=sum_{w in W} min(b-1,rho_w+ell).

In particular,

    sum_{u outside W}rho_u+2t<=ell|W|.                    (S)

Proof: r+2t<=Q<=sum_{w in W}(rho_w+ell)=r-sum_outside rho+ell|W|. For even n and Delta=n/2+1, ell=2. Thus inactive supplement vertices cannot carry arbitrary residual mass: it must fit a linear budget 2|W|-2t.

For a subset I of labels, the analogous inequality is sum_{i in I}s_i<=sum_{w in W_I}pbar_w, using a safe superset W_I of their permitted supplements.

## 3. Source pair-degree and excess selections

For every selected ui -> w,

    R_i+x_i>=sigma_u.                                    (2)

Proof: for z in N_P(u) minus {w}, uz is missing in H, so the quasi-edge ui must dominate z through iz. In addition iu is an edge. These are sigma_u distinct B-neighbours of i. This uses the total pair-degree q_u+p_u, not only the outgoing degree.

Put D_i^0=R_i+s_i=max(R_i,d_i), D0=max_i D_i^0, e_i=x_i-s_i>=0 and E=sum e_i=Q-Q0. If sigma_u>D0, all q_u distinct labels selected at u require e_i>=sigma_u-D0. Hence q_u(sigma_u-D0)<=E. For any proved incoming cap pbar_u,

    (sigma_u-pbar_u)_+ (sigma_u-D0)_+ <= E.              (D)

The E budget is used separately for each source; summing it across sources would double-count labels and is not justified.

### Exact monotone refinement

Let c_u be safe source caps and J the permitted unordered-pair graph. Every actual P is a subgraph of J. Set incoming capacity to zero outside the permitted supplement support. Initially bound Q by total source capacity, total incoming capacity, |E(J)| and the sum of label upper bounds min(b-R_i,eligible_source_count_i).

Given Q<=U, E<=U-Q0. For each u let g_u be the largest integer sigma satisfying sigma<=degree_J(u), sigma<=c_u+pbar_u and (D) with E replaced by U-Q0. Then

    Q<=floor(sum_u g_u/2).

Replace U by the minimum of itself and this quantity. Every iteration preserves an upper bound. A decrease below Q0 is an exact contradiction. The code also checks every integer Q in the original interval as an alternative certificate.

## 4. Coupled weighted-cover certificates

Each permitted triple (i,u,w) consumes source capacity c_u, supplement capacity pbar_w, source-label capacity one, and unordered-pair capacity one. Choose nonnegative integer label weights y_i and resource weights A_u,B_w,C_iu,D_{uw}. If every permitted triple satisfies

    y_i<=A_u+B_w+C_iu+D_{unordered {u,w}},

then

    sum_i y_i s_i <= sum_u A_u c_u+sum_w B_w pbar_w
                     +sum_{i,u}C_iu+sum_{unordered pairs}D_{uw}.

This follows by summing over actual selected triples and applying capacities. The search uses SciPy to discover weights; only rationalised integer weights whose every covering condition and strict final inequality pass exact checks are accepted. A solver status alone is never a certificate.

The static-capacity relaxation does NOT enforce all actual source-degree values, complete residual adjacency, or full criticality. An integral witness to it is not a graph.

## 5. Explicit checked profiles

Repeated-value notation below gives multiplicities.

### Profile A: (64,33,1031)

    a=30, t=8, ell=2,
    d=(10 repeated 22,11 repeated 8),
    R=(4 repeated 4,5 repeated 26),
    rho=(2 repeated 13,6 repeated 20).

Here r=146 and Q0=162. Every label needs at least five selected incidences, so a rho=2 vertex cannot select it. Since d_i>=10>6+2, none of those thirteen vertices can be a supplement either. The twenty usable supplements have incoming capacity 6+2=8 each. Thus 162<=160 is impossible, even though the support offers 190 unordered pairs.

### Profile B: (44,23,485)

    a=20, t=2, ell=2,
    d=(6 repeated 6,7 repeated 14),
    R=(3 repeated 15,4 repeated 5),
    rho=(1 repeated 9,4 repeated 14).

Here r=65, Q0=69, D0=7. Every pair endpoint lies among fourteen rho=4 vertices. They offer 91 pairs and incoming capacity 84, so support counting alone passes. An integral 69-selection witness to the static-capacity model is stored and checked; it does not satisfy all actual-degree conditions.

Nevertheless Q<=84 gives E<=15. Degree sigma>=11 would require (sigma-6)(sigma-7)>=20>15. Hence sigma<=10 and Q<=70. Then E<=1. Degree sigma>=8 would require at least 2 excess, so sigma<=7 and Q<=49<69. This rejects the entire profile, not only the minimum-selection case. All sixteen Q=69,...,84 are separately checked.

Both profiles pass the saved earlier source, pair, subset, h-index and local-k tests, as well as F-degree graphicality and residual bipartite-degree graphicality. These are two deliberate test inputs, not an exhaustive sweep.

## 6. Infinite excluded profile families

Let bal(a,M) be the sorted length-a integer list whose entries differ by at most one and sum to M.

Family I, every integer s>=2:

    n=60s+4, a=30s, b=30s+3, t=2,
    rho=((2s) repeated (10s+3),(6s) repeated 20s),
    r=140s^2+6s, R=bal(a,r), d=bal(a,2r+4).

Every label has d_i-R_i>2s, and min d_i>8s, so all supplements lie among the 20s high vertices. Demand is r+4; incoming capacity is 20s(6s+2). The difference is 20s^2-34s+4>0 for all s>=2. Explicit representatives s=2,3,4 also pass the earlier tests before this rejection.

Family II, every integer s>=1:

    n=40s+4, a=20s, b=20s+3, t=2,
    rho=(1 repeated (6s+3),(4s) repeated 14s),
    r=56s^2+6s+3, R=bal(a,r), d=bal(a,2r+4).

Every label has d_i-R_i>1 and min d_i>4s+1, so every selected-pair endpoint is among the 14s high vertices. Here Q0=56s^2+6s+7, Q<=56s^2+28s, E<=22s-7, pbar=4s+2 and D0<=6s+1.

For s>=3, degree sigma>=8s+1 would require excess at least (4s-1)(2s)=8s^2-2s>22s-7. Thus sigma<=8s, giving 2Q<=112s^2<2Q0. At s=2, D0=13, pbar=10 and E<=37 exclude degree 18, giving 2Q<=28*17=476<486. At s=1 use Profile B. This symbolically excludes the whole family.

These are families of residual patterns at Delta=n/2+1 and m=floor(n^2/4)+1. They do NOT settle all graphs at the displayed orders.

## 7. Retained frontier

The following pattern is not rejected by the tests in this continuation:

    n=64, a=30, b=33, t=2, m=1025,
    d=(15 repeated 4,16 repeated 26),
    R=(7 repeated 4,8 repeated 26),
    rho=(1 repeated 4,8 repeated 29).

It has r=236, Q0=240, 29 possible pair endpoints, 406 permitted pairs and incoming capacity 290. It passes the implemented old cuts, support bound and source-degree tests. Weighted search produced no rejection certificate; that absence is not a proof of feasibility. No actual graph or full dynamic construction is claimed.

The next target is to retain each D_i=R_i+x_i, rather than replacing them all by D0: sources of degree sigma may use only labels with D_i>=sigma, and each label's incidence demand competes for the same sources. This must then be coupled with residual/selected adjacency and F-neighbourhood closure. That stronger dynamic model is not implemented here.

## 8. Audit and preservation

`check_pack.py` and `EXPERIMENTS.json` provide a standard-library-only replay of the core certificates: run `python3 check_pack.py`. It checks seven certificate/witness objects and rejects three deliberately corrupted versions. It uses a different threshold-matching implementation from the search, but is still by the same assistant, not an external reviewer.

Actual-graph falsification checks inspected all 1,253 NetworkX Graph Atlas entries, with all selections on its ten non-bipartite critical graphs, plus 54 seeded larger critical graphs up to order 44 with at most five selections per root. Totals: 378 selected systems, 3,922 vertex checks, 3,540 selected-edge checks, no failures. No positive-surplus actual graph occurred. The catalogue is an imported dependency, not independently regenerated: https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html .

The complete downloadable `General_Order_Pair_Budgets_2026-09-07_v2.zip` contains the expanded PROOF.md, source programs, profiles, exact certificates, retained relaxation witness and frontier, sampled graph edge lists, environment and manifest. Repository preservation records identify these files and their hashes. The research package and core replay do not change frozen theorem editions or the governed ledger. Universal lemma validity, internal arithmetic, artifact availability, novelty and external review remain separate questions.
