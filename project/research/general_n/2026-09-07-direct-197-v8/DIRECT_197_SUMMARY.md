# Direct197 result and candidate order-28 assembly

7 September 2026. Research directed by Paul Lenz; derivations, implementation and internal checking by ChatGPT/Geeps. **Candidate mathematics; independent mathematical review OPEN.** Full proof, source and exact certificates are in the 90-payload v8 archive pinned in [README.md](README.md). This is a readable summary, not a replacement for that evidence.

## A fresh scope, not extrapolation from 196

The target is (n,Delta,m)=(28,15,197), a=12,b=15,t=m-b(n-b)=2. Let H complement G, choose its minimum-degree root v, put A=N_H(v) and B=V(H) minus N_H[v], and let F complement H[A]. Select exactly one cross quasi-edge for each missing B-pair. All other existing cross edges are residual.

Write rho_u,R_i for residual row/column degrees, r=sum rho=sum R, q_u,p_u for outgoing/incoming selected-pair degrees, x_i for the actual selected degree of label i, d_i=d_F(i), s_i=max(0,d_i-R_i), and S=sum s. The ledger gives e(F)=r+t, sum d=2(r+t), x_i>=s_i, and S>=r+2t. Positive surplus forces all rho_u>=1 by the inherited residual injection.

Every hypothetical graph therefore gives a demand tuple satisfying

    sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t.

At a=12, b=15, t=2 the right side is 19. Every nondecreasing length-12 tuple from 0..11 in this domain is generated. The separate checker independently counts the unpruned domain, verifies membership/uniqueness of every tuple, and checks all source/support/dual exclusions. It does not use the older equality-only verify_scope wrapper.

There are 12,012 tuples; 1,229 retained intervals expand into 8,216,928 residual rows. A separate C++ multiplicity enumeration and generating-product count reconstruct every row classification, each demand-band count and all survivor bytes. The source-capacity/refinement screen leaves 5,154 rows. Explicit t=2 slack and degree-pair tests leave 2,959. The joint-column checker reconstructs every disposition and the surviving column domains, caps and forced labels, leaving 1,584.

| Stage | Input rows | Exact exclusions | Remaining |
|---|---:|---:|---:|
| Complete residual expansion | 8,216,928 | 8,211,774 | 5,154 |
| t=2 slack and projected pair cuts | 5,154 | 2,195 | 2,959 |
| Joint columns and one-source constraints | 2,959 | 1,375 | 1,584 |
| Shared adjacency model | 1,584 | 787 | 797 |
| Source-degree-type model | 797 | 790 | 7 |
| Actual endpoint-degree model | 7 | 7 | **0** |

These are numerical necessary-condition rows, not graphs. The new direct route does not consume a t=1 survivor list and has no unclosed branch tree.

## Why the final constraints are necessary

For a selected ui with unique B-exception w, the A-label i must neighbour u and every missing-B-pair neighbour of u except w. Hence its actual B-neighbourhood satisfies

    R_i+x_i >= q_u+p_u.

The final model records both actual degree types at each selected incidence. Source degrees, column choices, selected/residual/missing status and their shared marginals must agree. The source degree-conditioned ledgers include sum R=r and sum d=2(r+t) conditional on each type, rather than only in aggregate.

One extra local inequality needs full criticality. Partition A relative to a source u into selected S, residual T and missing M. Selected quasi-edges prohibit F-edges S-M. Distinct supplements of F-edges within S force 2e_F(S) residual edges with A-endpoints in S. Missing H-pairs within M miss u; their quasi-edge auxiliaries lie in T or B. At most e_C(T,M) use T; the others give distinct residual cross edges with A-endpoints in M. Together with u's rho_u edges ending in T this gives

    rho_u+2e_F(S)+e_F(M)-e_C(T,M) <= r.

It implies

    sum_{i in S} d_i <= rho_u(2a-rho_u-3+q_u)-2t,
    sum_{i in S} R_i <= r-rho_u.

The direct calculation applies these to the original 197-edge critical graph. It does not assume that this local lemma survives the other workstream's weakening to B-quasi-edge cores.

Symmetry coordinates are averages of indicators under relabelling within identical label/source classes. They can be fractional for a real graph. The models respect that fact; they do not impose integrality on those averages. The exact certificates already reject the fractional relaxations, so no complete integral graph search is needed.

## Exact arithmetic and complete replay

If a reconstructed system is Ay<=b,Ey=f,y>=0, a certificate has nonnegative integer inequality multipliers lambda and signed integer equality multipliers mu. It proves lambda A+mu E is coefficientwise nonnegative while lambda b+mu f is strictly negative. That is an exact contradiction. Floating-point optimisation only proposes weights; no solver status alone counts.

Every one of the 1,584 final certificates is checked against a separately reconstructed named-variable model. The new checker also independently regenerates the initial domain, residual domain, projected partition and every joint state, and checks all handoffs. It imports no discovery model or optimisation library. The thirteen damaged-evidence controls reject wrong t/edge scope, omitted or duplicate demand/LP records, a zero initial dual, wrong LP input row, forged RHS, unknown constraint, negative inequality multiplier, duplicate multiplier and empty alleged contradiction. The projected checker adds two more controls.

The complete clean-copy replay passed. The original v6 and LocalIncidence-v7 complete separate checks also passed again, as did the v3 Delta=16 equality scope. No fresh full replay of every earlier v3/v4/v5 equality-level stage is asserted.

## Every maximum degree at 197 is covered

Delta<=14 gives at most 196 edges by the degree sum. Delta=15 is excluded above. At Delta=16, a=11 and t=5, so the charging sum must be at least 26. But for every integer 0<=s<=10,

    s(12-2s)/(11-s) <= 16/7.

The difference is 2(s-4)(7s-22)/[7(11-s)], nonnegative for those integers. Eleven labels therefore permit at most 176/7<26, a contradiction.

For 17<=Delta<=26, the inherited h-index charging gives

    b+2t <= floor((28-b)^2/4),

violated in every case: at b=17 it already requires 37<=30. The full ten-case exact table is in ALL_DEGREES_AND_FAN.json. Delta=27 forces a star, which has 27 edges. Thus no maximum degree is possible at 197.

Fan's strict bound for n>=25, as reported by Tao Wang, On Murty-Simon Conjecture, arXiv:1205.4397 p. 2, is

    m < n^2/4 + (n^2-(81/5)n+56)/320.

At n=28 it is 78883/400=197.2075, hence m<=197 by integrality. The new direct197 exclusion gives the candidate upper bound 196. Fan's original proof has not been re-audited here; that theorem is an explicit input to the full upper-bound assembly, not the fixed 197-edge calculation.

Equality at 196 uses the separately preserved LocalIncidence-v7/upstream chain at Delta=15 and v3 at Delta=16, the degree-sum/regular-graph argument at Delta<=14, and the h-index/star reductions above. Consequently this supplies a complete **candidate** order-28 route with equality only K(14,14), without the weak-core density reduction. It remains subject to the universal structural and upstream-coverage review obligations.

No order above 28, all-order proof, improved uniform coefficient, novelty, independent researcher endorsement or formal-kernel verification is claimed. The saved actual-graph samples contain no positive-surplus graph; those tests cannot empirically establish the dense-case contradiction.
