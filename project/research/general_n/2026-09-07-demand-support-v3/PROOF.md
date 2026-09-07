# General-order demand–support cuts for the Murty–Simon programme

**Dated:** 7 September 2026. Developed by ChatGPT/Geeps for Paul Lenz in the continuation chat requested on this date.

**Status:** candidate mathematical arguments, with complete internally reproduced exact arithmetic for three specified degree cases. Independent mathematical review and independent computational reproduction by another researcher are **OPEN**. This is not formal verification, a novelty claim, a resolution of the general conjecture, or a complete resolution of any new order. No governed theorem-ledger entry is promoted.

## 1. Results and scope

The new result is an order-independent demand–support pair inequality, used before enumeration of the full degree and residual-column data. Combining it with exact source-capacity cuts gives candidate exclusions of:

| Order n | Maximum degree b | All excluded edge counts |
|---:|---:|---:|
| 28 | 16 | m ≥ 196 |
| 30 | 17 | m ≥ 225 |
| 33 | 19 | m ≥ 272 |

The calculations are performed at the smallest displayed edge count. Section 9 proves why the same exclusions apply at every larger count. No deletion-preserves-criticality assumption is made.

After incorporating the previous general-order reductions, the unresolved degree sets at these orders are respectively {15}, {16}, and {18}. Those remaining sets are inherited-plus-new necessary-condition frontiers, not lists of constructed graphs. The frozen n=25 and n=27 candidate proofs remain unchanged. The previous coefficient (10−√2)/14 ≈ 0.6132704598 is not improved in this note.

The programme uses three distinct levels: a universal graph-theoretic derivation; a finite relaxation whose domain contains every hypothetical graph in the specified case; and arithmetic certificates rejecting that whole relaxation. Software checks establish the last level and domain coverage, not the first level by themselves.

## 2. Graph setup and inherited inputs, rederived here

Let G be a simple diameter-two edge-critical graph: deleting any edge makes some distance exceed two, with disconnected pairs assigned infinite distance. Write n=|V(G)|, m=e(G), and b=Δ(G).

A universal vertex forces G to be a star: any edge between two other vertices could be removed without destroying diameter at most two. A bipartite diameter-two graph is complete bipartite, because an absent cross-part edge would have odd distance at least three. Handle these cases separately. For the three degree cases above, a complete bipartite graph has b(n−b) edges, strictly below the displayed target.

For the remaining non-bipartite case, let H be the complement of G. The published complement correspondence and characterization of 4-total-domination-supercritical graphs imply that H is 3-total-domination-edge-critical [1, Theorems 3.1–3.2]. The isolated-complement/star exception has already been removed. This published correspondence is an external mathematical dependency, not a new claim.

Choose v of **minimum** H-degree a=n−1−b. Put A=N_H(v), B=V(H)\N_H[v], C=H[A], and F=complement(C) on A. Thus |A|=a and |B|=b. Let d_i=d_F(i).

For a nonedge uw of H whose endpoints miss a third vertex, adding uw creates an adjacent total dominating pair. That pair cannot be {u,w}, which still misses the third vertex. It therefore uses an existing edge incident with one endpoint, say ui, that dominates every vertex of H except w. Write ui→w. The exception w is unique, and uw and iw are absent. This is the quasi-edge observation also used in [1, Observation 3.4].

For every missing **unordered** B-pair choose exactly one quasi-edge ui→w. Its auxiliary i belongs to A to dominate v. Distinct B-pairs select distinct cross-edges, because the B-endpoint and unique exception identify the pair. At a fixed source u, selected quasi-edges have distinct supplements w. Call all other H-edges between A and B **residual**.

Let r be the residual count, ρ_u its degrees at B, and R_i its degrees at A. Let q_u be the number of selected edges at source u, and Q=Σq_u. Set

\[
t=m-b(n-b),\qquad L=\binom a2-t.
\]

Selected edges and existing H[B]-edges together number binom(b,2). Counting all H-edges therefore gives

\[
e(C)+r=L,\qquad e(F)=r+t,\qquad
\sum_i d_i=2(r+t),\qquad \sum_iR_i=\sum_u\rho_u=r. \tag{2.1}
\]

Minimum H-degree is essential: d_H(i)=a−d_i+d_B(i)≥a, hence d_B(i)≥d_i. Define the **demand**

\[
s_i=\max(0,d_i-R_i),\qquad S=\sum_i s_i.
\]

Label i needs at least s_i selected sources, and

\[
S\ge \sum_i(d_i-R_i)=r+2t. \tag{2.2}
\]

### Selected-source and supplement constraints

For a selected ui→w, each F-neighbour j of i must be adjacent to u. At most ρ_u such uj edges are residual. Every remaining uj is selected with a distinct supplement w_j≠w. Since ui must dominate w_j, iw_j is an H-edge. It is residual: i and w_j both miss the A-vertex j, whereas a selected edge's unique exception belongs to B. Distinct w_j give distinct residual edges at i. Consequently

\[
d_i\le \rho_u+R_i,\qquad s_i\le\rho_u. \tag{2.3}
\]

Simplicity gives

\[
q_u+\rho_u\le a,\qquad q_u\le b-1. \tag{2.4}
\]

Every other selected uj at u has a supplement different from w and must dominate w. Since uw is absent, w is adjacent to each of those q_u−1 other A-labels. Therefore

\[
\rho_w+q_w\ge q_u-1. \tag{2.5}
\]

Globally, selected arcs u→w use each unordered B-pair at most once. Constraints (2.3)–(2.5) and this pair injection are the essential inputs to the new cut.

### Positive surplus and residual activity

We use the strict hypothesis t>0. Suppose ρ_u=0. Put U=N_A(u) and T=A\U. Every ui with i∈U is selected. There is no F-edge from U to T: otherwise ui would fail to dominate an A-vertex in addition to its B-exception.

Write w_i for the distinct supplements of selected ui. An F-edge ij inside U forces both jw_i and iw_j to exist, by domination of the other selected edge's supplement. These edges are residual, because each misses an A-vertex with its partner. Their A-endpoints and distinct supplement labels distinguish all 2e(F[U]) edges.

An F-edge pq inside T misses u and has a quasi-edge whose auxiliary must dominate u. The auxiliary cannot be u or v. If it belonged to A, it would be in U and hence adjacent in C to both p and q, contradicting the required exception. Thus it lies in B and gives a residual cross-edge with A-endpoint in T. Distinct F-edges give distinct such cross-edges: the A-endpoint and unique A-exception determine pq. This family is disjoint from the U-endpoint family.

It follows that r≥2e(F[U])+e(F[T])≥e(F)=r+t, a contradiction. Thus

\[
\rho_u\ge1\quad\hbox{for all }u\in B. \tag{2.6}
\]

This proof covers empty U. It does not assume any diameter bound on H. Replacing t>0 by t≥0 would be invalid.

## 3. The demand-only finite domain

A positive s_i has a selected source u with ρ_u≥s_i and q_u≥1. By (2.4), s_i≤a−1. Thus 0≤s_i≤a−1 for every label.

For each i choose exactly s_i actual selected incidences. A source of residual degree ρ<a can distribute cost (ρ−1)/(a−ρ) to each chosen incidence; its total cost is at most ρ−1. A source with ρ=a has no selected incidences and need distribute nothing. Because (x−1)/(a−x) is increasing on [1,a), each chosen incidence of label i receives cost at least (s_i−1)/(a−s_i). Summing gives the inherited charging inequality

\[
r-b\ge \sum_i g_a(s_i),\qquad
 g_a(s)=\frac{s(s-1)}{a-s}. \tag{3.1}
\]

Terms with s=0 contribute zero. Combining (2.2) with (3.1), and writing

\[
f_a(s)=s-g_a(s)=\frac{s(a+1-2s)}{a-s},
\]

gives the necessary domain condition

\[
\sum_i f_a(s_i)\ge b+2t. \tag{3.2}
\]

Every hypothetical graph yields a sorted demand multiset satisfying (3.2). Sorting here is only a relabelling of A. We do not independently sort the jointly labelled d and R arrays; those arrays are not enumerated at this stage.

For a fixed demand multiset, every feasible residual total belongs to the exact interval

\[
r_{\min}=b+\left\lceil\sum_i g_a(s_i)\right\rceil,
\qquad
r_{\max}=\min\left(S-2t,\binom a2-t\right). \tag{3.3}
\]

The second upper bound uses e(C)≥0. Nongraphical demand and residual data are deliberately retained. An empty interval is an immediate rejection.

## 4. New universal demand–support pair inequality

Choose an integer 2≤h≤a−1. Put

\[
I=\{i:s_i\ge h\},\quad k=|I|,\quad D=\sum_{i\in I}s_i,
\qquad Z=\{u:\rho_u\ge h\},\quad z=|Z|.
\]

Every selected source for an I-label lies in Z by (2.3). By residual activity,

\[
z\le z_{\max}:=\min\left(b,\left\lfloor\frac{r_{\max}-b}{h-1}\right\rfloor\right). \tag{4.1}
\]

If I is nonempty, its largest demand cannot exceed z_max: that label needs that many distinct sources in Z.

A vertex outside Z can select only the a−k labels outside I, and has ρ≤h−1. Its total A-degree is therefore at most

\[
\rho_w+q_w\le a-k+h-1=K-1,\qquad K=a-k+h. \tag{4.2}
\]

Call a source u∈Z **large** when q_u≥K+1, and let p be the number of such sources. By (2.5), every supplement of a large source has A-degree at least K, so lies in Z. Their selected arcs use distinct unordered pairs inside Z incident with the large-source set. There are only

\[
P(z,p)=\binom z2-\binom{z-p}2=pz-\frac{p(p+1)}2 \tag{4.3}
\]

such pairs. If p>0, feasibility therefore requires

\[
a-h\ge K+1,\qquad p(K+1)\le P(z,p). \tag{4.4}
\]

The first bound follows from q_u≤a−ρ_u≤a−h. A non-large source in Z contributes at most min(k,K,a−h) selected I-incidences. The large sources contribute at most both p min(k,a−h) and P(z,p). Therefore

\[
\boxed{
D\le C(a,k,h,z):=
\max_{\substack{0\le p\le z\\
p=0\;\text{or}\;[a-h\ge K+1,\ p(K+1)\le P(z,p)]}}
\left[(z-p)\min(k,K,a-h)+\min\{p\min(k,a-h),P(z,p)\}\right].
} \tag{4.5}
\]

The p=0 alternative is always admitted. When z is unknown, maximize (4.5) over all integers 0≤z≤z_max. A strict violation rejects the demand multiset without knowing F, R, or the individual residual degrees.

This is an all-order inequality, not an extrapolation from n=28. Its source/supplement coupling supplies a profile-dependent obstruction near the earlier charging maximum. No uniform stability constant or improved asymptotic degree coefficient is claimed.

## 5. Demand-only source cuts and exact dual certificates

Sort the demands in nonincreasing order, denoted s_(1),…,s_(a), and let D_k=Σ_{i≤k}s_(i). A source with residual degree j can contribute at most

\[
A_{kj}=\min\left(a-j,\#\{i\le k:s_{(i)}\le j\}\right)
\]

selected incidences in this prefix. If x_j is the number of B-vertices with residual degree j, necessary conditions are

\[
D_k\le\sum_{j=1}^a A_{kj}x_j,\quad
\sum_jx_j=b,\quad \sum_j(j-1)x_j=r-b. \tag{5.1}
\]

These constraints allow extra selected incidences beyond the minimum demands. They are upper bounds, not a claim that each label has exactly its demand.

For nonnegative integer weights y_k, integer μ, and positive integer scale Λ, suppose

\[
\mu+\sum_k y_kA_{kj}\le\Lambda(j-1)\quad(1\le j\le a).
\]

Multiply by x_j and sum. Equation (5.1) gives

\[
\boxed{b\mu+\sum_k y_kD_k\le\Lambda(r-b)
\le\Lambda(r_{\max}-b).} \tag{5.2}
\]

The saved certificate records weights giving the strict reverse of (5.2), while satisfying every residual-type constraint. The checker uses exact integer arithmetic throughout.

SciPy linear programming is used only to propose weights. The discovery code rationalizes them, repairs μ downwards, scales to integers, and checks the strict contradiction exactly. Solver failure, an infeasibility message, or floating-point feasibility is never accepted as a proof. The arithmetic checker does not import SciPy or the discovery code.

## 6. Residual-row refinement, without d/R column enumeration

For the remaining demand multisets, enumerate every sorted residual list ρ of length b, with 1≤ρ_u≤a and sum in [r_min,r_max]. An initial valid upper bound on the actual selected degree is

\[
c_u^{(0)}=\min\left(a-\rho_u,b-1,\#\{i:s_i\le\rho_u\}\right). \tag{6.1}
\]

Labels with s_i=0 must be included: they may still carry actual selected incidences. Omitting them would incorrectly restrict extra incidences.

Given simultaneous valid caps c, replace c_u by the largest q≤c_u for which at least q other vertices w satisfy ρ_w+c_w≥q−1. Each real source has q_u distinct supplements, and (2.5) proves that its actual q_u remains allowed. Each iteration uses the old caps for every source. Thus induction preserves validity, and monotone integer decrease terminates.

At the final caps, every prefix obeys

\[
\boxed{D_k\le\sum_u\min\left(c_u,\#\{i\le k:s_{(i)}\le\rho_u\}\right).} \tag{6.2}
\]

A saved prefix with a strict violation is the rejection certificate. The checker recomputes all caps, all iterations, and both sides of the inequality. This refinement adapts the earlier project supplement-capacity method to the smaller demand-only relaxation; the refinement itself is not claimed as a new project invention.

## 7. Exact completed scopes

| n | b | a | t | Charging demand multisets | Support/source-count rejections | Exact dual rejections | Demand multisets requiring rows | Residual rows checked | Survivors |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 28 | 16 | 11 | 4 | 39 | 35 | 3 | 1 | 604 | 0 |
| 30 | 17 | 12 | 4 | 1,155 | 921 | 216 | 18 | 13,545 | 0 |
| 33 | 19 | 13 | 6 | 630 | 553 | 77 | 0 | 0 | 0 |

All 1,824 demand multisets and 14,149 residual rows in the last stage are covered. These are relaxation-profile counts, not counts of actual graphs searched.

The checker establishes demand-domain coverage by direct enumeration of every nondecreasing sequence in {0,…,a−1}^a, followed by an exact integer-scaled test of (3.2). This examines 6,905,094 unfiltered multisets across the three dimensions. Saved lists must be valid and unique, and their cardinalities must match. The discovery generator instead uses branch pruning, so coverage is not simply accepted from its own totals.

For residual lists, the checker uses coefficients of

\[
\prod_{j=1}^a(1-XY^j)^{-1}
\]

to count each length-b, sum-r multiset domain. Membership, uniqueness, and equality with those counts prove full numerical coverage. This differs from the discovery recursion.

The support checker directly enumerates feasible (z,p) pairs, rather than using the discovery code's closed-form p upper bound. The row-cap checker sorts supplement capacities and checks each trial q; it does not import the discovery decrement routine. Deliberately zeroed dual weights, an omitted residual row, forged caps, and an omitted demand multiset are all rejected.

These are separate implementations written by the same assistant. They are not independent research authorship or an external assessment.

## 8. A short hand endgame for n=28, b=16

Here a=11, t=4. The exact charging/support screen leaves only these four sorted demand multisets:

| Demands | S | r_max |
|---|---:|---:|
| 2,2,3,3,4,4,4,4,4,4,4 | 38 | 30 |
| 2,2,3,4,4,4,4,4,4,4,4 | 39 | 31 |
| 2,3,3,4,4,4,4,4,4,4,4 | 40 | 32 |
| 3,3,4,4,4,4,4,4,4,4,4 | 42 | 34 |

For each list, direct checking of j=1,…,11 gives

\[
q_u\le\min(11-\rho_u,\#\{i:s_i\le\rho_u\})
\le\frac73(\rho_u-1).
\]

Since Q≥S, this forces r−16≥3S/7. The first three lists respectively require 114/7>14, 117/7>15, and 120/7>16, contradicting their residual budgets.

For the last list, equality is forced: S=Q=42 and r=34. Equality in the pointwise source bound permits only residual degrees 1 and 4. Thus there are six vertices with ρ=4, each with q=7, and ten with ρ=1, each with q=0.

A selected edge at one of the six sources requires a supplement with at least q−1=6 A-neighbours. None of the ten remaining vertices can provide one: each has only one A-neighbour. Each source would therefore need seven distinct supplements among the other five eligible vertices, impossible. Equivalently, 42 selected arcs would have to use only binom(6,2)=15 unordered pairs.

The production certificate also enumerates and rejects all 604 residual lists for the final demand pattern. The hand argument explains their common obstruction; the finite initial 39-profile coverage still uses the checked arithmetic screen.

## 9. Why all higher edge counts are covered

Fix n and b, and write t_0 for the value at m_0=floor(n²/4). For a larger edge count m, t≥t_0. Condition (3.2) is stronger, so the possible demand multisets form a subset of the recorded domain. For any fixed multiset, r_min is unchanged and r_max can only decrease.

An interval rejection remains valid. The support upper bound cannot increase, because z_max cannot increase. The right side of a dual certificate (5.2) cannot increase. Finally, a residual-row interval at larger t is a subset of the interval checked at t_0, and its row certificates do not depend on t.

Hence every certificate used at m_0 covers its retained data at larger m. This is monotonicity of necessary inequalities, not deletion of edges from a critical graph. Fan's finite edge bound is not a dependency of these three exclusions.

## 10. Falsification tests and their limits

The actual-adjacency test examines all 33,864 labelled graphs of orders 3 through 6, finds 608 diameter-two-critical graphs (552 non-bipartite), and checks all minimum-complement-degree roots and quasi-edge selections in that small domain. It additionally makes 192 seeded construction attempts at orders 7 through 22, yielding 89 critical outcomes; larger selections are sampled. Across these tests there are 916 root/selection instances, 1,190 selected triples, and 2,036 prefix checks, with no failed assertion.

**Important coverage limitation:** there are no positive-surplus graph instances and no nonempty high-demand support tests in this actual-graph sample. Thus these tests do not nonvacuously test the new h≥2 obstruction on actual critical graphs, and do not empirically establish the positive-surplus contradiction.

A separate abstract test constructs 9,427 accepted incidence systems from 12,000 seeded attempts. These systems satisfy the pair injection, distinct source labels, activity, row-size, source-demand, and supplement-degree premises of the abstract lemma. There are 15,737 nonempty threshold tests, including 2,976 with large sources. All assertions pass. The systems are **not** claimed to be diameter-critical graphs and do not impose the density ledger. This is a nonvacuous test of the combinatorial cut under its abstract premises, not a test of graph realizability or a substitute for the proof.

The argument remains subject to external mathematical review, especially the inherited residual injections and the new large-source pair accounting. No uniform stability theorem, bounded-core theorem, formal-kernel verification, or completed order beyond the pre-existing candidates is asserted.

## 11. References and provenance

[1] Teresa W. Haynes, Michael A. Henning, Lucas C. van der Merwe, and Anders Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12(12) (2014), 1882–1889. DOI: 10.2478/s11533-014-0449-3. Primary full text: https://d-nb.info/1372516379/34 . The published correspondence is a dependency; its entire original proof is not independently re-audited here.

[2] Project n=27 candidate, Sections 4–11, blob `83e09e02918adf461470bf7e70177bad275b57d9`: https://github.com/paullenz/MurtySimon25/blob/663992175fdedae3c77c87b2f80eb9e582adce27/project/reviews/n27/2026-09-07-candidate-v1/PROOF.md . Source of the inherited residual, selected-edge and supplement-refinement framework.

[3] Project general-order coupled-resource v2, blob `3d3b4ab5b2da8207f17a3a2afcce49e7119d78e2`: https://github.com/paullenz/MurtySimon25/blob/663992175fdedae3c77c87b2f80eb9e582adce27/project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md . Source of the inherited charging inequality and current general-degree baseline.

[4] Antoine Dailly, Florent Foucaud, and Adriana Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342(11) (2019), 3142–3159; https://arxiv.org/abs/1812.08420 . Dependency of the inherited low-degree frontier, not needed for the three fixed-degree exclusions proved here.

The repository baseline is commit `663992175fdedae3c77c87b2f80eb9e582adce27`. “New” means new to this project checkpoint, not a verified priority claim. Paul Lenz directed the project; ChatGPT/Geeps supplied the mathematical development, implementations and internal checks. See REVIEW_AND_RECONCILIATION.md for the limits of the cross-chat review and preservation status.
