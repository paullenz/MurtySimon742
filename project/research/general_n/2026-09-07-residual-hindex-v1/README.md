# General-order residual h-index attack

7 September 2026. Prepared by ChatGPT/Geeps for Paul Lenz in response to: “Can you find a generalised attack approach for N>27”.

**Status:** explicit candidate mathematical derivations; arithmetic REPRODUCED; independent mathematical and computational review OPEN. Nothing is promoted to PROJECT-CERTIFIED. Frozen n=25 and n=27 editions and the governed theorem ledger are unchanged. No novelty or priority is claimed. No complete order above 27 is claimed resolved.

## Main result derived in this session

Candidate theorem: for n>=4, a diameter-two edge-critical graph with maximum degree

    Delta >= alpha*n,  alpha=(3+sqrt(2))/7 = 0.630601937...

has strictly fewer than floor(n^2/4) edges.

This is an order-independent mathematical argument, not extrapolation from finite enumeration. The exact inequality is

    b+2t <= floor((n-b)^2/4),                 (H)

where b=Delta and t=m-b(n-b)>0. The near-half-degree region remains open. A second consequence extends the local k=0,1 residual argument to every k.

## Attribution and dependencies

Source project manuscript: `project/reviews/n27/2026-09-07-candidate-v1/PROOF.md`, Git blob SHA `83e09e02918adf461470bf7e70177bad275b57d9`. Sections 4–8 supply the residual ledger, activity argument, selected-edge inequalities and h-index observation; Sections 9–11 supply subset and pair cuts. These were read and rederived here. The new step aggregates the h-index and activity bounds into an all-order inequality.

Published sources:

- Haynes, Henning, van der Merwe and Yeo, *A maximum degree theorem for diameter-2-critical graphs* (2014), Theorems 3.1–3.2 and Observation 3.4: https://d-nb.info/1372516379/34
- Dailly, Foucaud and Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs* (2019), dominating-edge reduction: https://arxiv.org/abs/1812.08420
- Fan's strict edge bound, as reproduced on page 2 of Wang, *On Murty-Simon Conjecture*: https://arxiv.org/pdf/1205.4397 . Fan's original full proof was not re-audited here. The new high-degree theorem does not depend on this bound.

The 2014 paper gives a published 0.7n degree result; a 2016 preprint states a 0.6756n result in its theorem, https://arxiv.org/html/1610.00360v2 . Neither is needed to derive (H). Searches did not locate the 0.630601937... statement, but no comprehensive novelty determination has been completed.

## 1. Residual setup

Let G have order n, m edges and maximum degree b. A universal vertex forces G to be a star, since any edge between other vertices would be redundant. Bipartite diameter-two graphs are complete bipartite. Handle those cases separately. For remaining non-bipartite G, H=complement(G) is 3-total-domination-edge-critical by the published correspondence.

Choose v of minimum H-degree a=n-1-b. Put A=N_H(v), B=V(H) minus N_H[v], C=H[A], F=complement(C) on A. Then |A|=a, |B|=b. Write d_i for degrees in F.

For an H-nonedge uw whose endpoints fail to dominate a third vertex, criticality supplies an existing edge uz (after possibly exchanging u,w) whose endpoints dominate every vertex except w. Write uz -> w. Its exception is unique, and uw and zw are absent. To see this, a total dominating adjacent pair in H+uw must use the new edge for a domination not available in H, cannot be exactly {u,w}, and must have the opposite endpoint of the added edge as its only exception in H.

For every missing unordered B-pair choose exactly one quasi-edge ui -> w or wi -> u. The auxiliary i must be in A to dominate v. Different pairs select different cross-edges, since a cross-edge's B-endpoint and exception identify its pair. Call all other A–B edges residual. At one B-source, selected supplements are distinct.

Let r be the residual count, rho_u its B-degrees, R_i its A-degrees, and Q the selected count. Put t=m-b(n-b) and L=choose(a,2)-t. The selected cross-edges and existing B-edges account for choose(b,2), so

    e(C)+r=L, e(F)=r+t,
    sum_i d_i=2(r+t), sum_i R_i=sum_u rho_u=r.       (1)

Minimum H-degree gives d_B(i)>=d_i, since the total degree of i is a-d_i+d_B(i). Thus its selected degree is at least max(0,d_i-R_i).

## 2. Positive surplus forces all B-vertices residual-active

Assume t>0 and rho_u=0. Write S=N_A(u), T=A minus S. Every ui for i in S is selected. There are no F-edges between S and T: otherwise a selected edge ui would miss an A-vertex in addition to its B-exception.

Let w_i be the supplement of ui. These are distinct. For each F-edge ij within S, selected uj must dominate w_i, forcing jw_i; similarly iw_j exists. Both edges are residual: j and w_i miss i, and i and w_j miss j. The 2e(F[S]) edges are distinct by their A-endpoints and distinct supplement labels.

For each F-edge pq within T, the H-nonedge pq misses u, so has a quasi-edge. Its auxiliary must dominate u. It cannot be v or u. An auxiliary in A would lie in S, but all S–T pairs are C-edges, so it would dominate the supposed exception in T. The auxiliary must lie in B. This gives a residual cross-edge whose A-endpoint lies in T and whose exception is in A. Distinct F-edges give distinct such edges: their A-endpoint and unique exception identify the pair. They are disjoint from the S-endpoint family.

Therefore r>=2e(F[S])+e(F[T])>=e(F)=r+t, impossible. Hence

    rho_u>=1 for every u in B; r>=b.              (2)

This handles empty S and does not assume diameter(H)=2.

## 3. Selected-edge inequality and h-index aggregation

For every selected ui -> w,

    d_i <= rho_u+R_i.                            (3)

Each F-neighbour j of i must be adjacent to u. At most rho_u such uj are residual. Each remaining uj is selected, with distinct supplement w_j different from w. The selected ui must dominate w_j, forcing iw_j. That edge is residual because i and w_j both miss j. Distinct w_j give at least d_i-rho_u residual edges at i, proving (3).

Put s_i=max(0,d_i-R_i), and let h be the largest integer q such that at least q residual B-degrees are at least q. Label i needs at least s_i distinct selected sources. By (3), each such source has rho_u>=s_i when s_i>0. Thus s_i<=h. From (1),

    r+2t=sum_i(d_i-R_i)<=sum_i s_i<=a*h.           (4)

At least h residual degrees are >=h; all remaining b-h are >=1 by (2). Thus

    r>=h^2+(b-h)=b+h(h-1).                       (5)

Combining (4) and (5),

    b+2t<=(a+1)h-h^2<=floor((a+1)^2/4).

Since a+1=n-b, this proves (H). The dependencies are the explicit quasi-edge, activity, distinct-supplement and selected-edge arguments above. No numerical infeasibility solver is used.

## 4. Maximum-degree consequence

Let alpha=(3+sqrt(2))/7, the larger root of 7x^2-6x+1=0. Suppose n>=4, b>=alpha*n and m>=floor(n^2/4). Integer b is beyond the balanced part size, so t>0. Inequality (H) gives

    2m<=2b(n-b)+floor((n-b)^2/4)-b.

Dropping a floor upward and multiplying by four gives

    8floor(n^2/4)<=n^2+6nb-7b^2-4b.

For even n this requires 7b^2-6nb+n^2+4b<=0; for odd n it requires 7b^2-6nb+n^2+4b-2<=0. But b>=alpha*n makes the first three terms nonnegative, and 4b-2>0. Contradiction.

Complete bipartite graphs and stars at this degree threshold are unbalanced for n>=4 and have strictly fewer than floor(n^2/4) edges. Excluding n=3 matters: K1,2 attains equality with degree ratio 2/3.

The exact finite inequality (H), including floors and its linear b term, is stronger than just rounding alpha*n. The coefficient can be tested without floating point using 7b-3n>=0 and (7b-3n)^2>=2n^2.

## 5. All-k local inequality

Assume every B-vertex is residual-active. For x in A set k=d_C(x), Y=N_C(x), X=A minus ({x} union Y). A missing H-pair in X has a quasi-edge auxiliary in Y or B. At most e_C(X,Y) such pairs use Y, since their quasi-edges are distinct X–Y edges. If p pairs use B, then

    p>=choose(a-k-1,2)-e(C[X])-e_C(X,Y)
     =choose(a-k-1,2)-e(C)+k+e(C[Y]).

The p cross-edges are residual since their exceptions lie in A. Every B-endpoint z used by them also forces xz. This is residual: if selected, it would miss the original A-exception. It is outside the p edges since its A-endpoint is x rather than in X. At each unused B-vertex choose an arbitrary residual edge. These supply b distinct additional residual edges. Thus

    L=e(C)+r>=b+k+choose(a-k-1,2)+e(C[Y]).        (K)

For a minimum-C-degree vertex, e(C)>=ceil(ak/2). Combining this with the h-index budget yields the scalar screen

    L>=b+k+choose(a-k-1,2),
    b+h(h-1)<=r<=min(L-ceil(ak/2),a*h-2t).       (B)

The scanner drops the nonnegative e(C[Y]) term. These are necessary conditions, not graph-realizability criteria.

## 6. General near-half witness reduction

At n>27, the published dominating-edge result excludes non-bipartite dense graphs with a dominating edge. Every remaining witness pair uv has d_G(u)+d_G(v)<=n-1. A witness is an edge with no common neighbour, or a nonedge with exactly one common neighbour; every critical edge belongs to the unique path of length at most two of some witness. A direct witness with degree sum n would be dominating.

For n=2s, Delta<=s gives m<=s^2; equality would make every degree s and leave no witness pair in the no-dominating-edge case.

For n=2s+1 and Delta=s+1, write epsilon_u=s+1-d_G(u), P={u:epsilon_u>=2}, O={u:epsilon_u=1}, p=|P|, o=|O|. At m>=s(s+1), total deficit T=n(s+1)-2m<=s+1, so 2p+o<=s+1. Witnesses outside P have both endpoints in O. Counting edge coverage gives

    m<=choose(p,2)+p(n-p)+2choose(o,2)
     <=choose(p,2)+p(n-p)+(s+1-2p)(s-2p).        (W)

Cross-part nonedge witnesses cover at most one edge outside P; O–O witnesses cover at most two. Adding the cross-part edges cancels their subtraction from possible cross-part nonedges. Thus no unjustified injective assignment is required. The right side is convex in p, equals s(s+1) at p=0, and is strictly smaller at p=floor((s+1)/2) for s>=2. Equality forces p=0 and o=s+1. All witnesses then lie in O, and the sharper count m<=2choose(s+1,2)-e(G[O]) forces O independent. Its s+1 vertices each have degree s, forcing K_{s,s+1}. Delta<=s is trivial. Hence the unresolved non-bipartite dense degrees exceed ceil(n/2).

## 7. Exact diagnostic and limits

`screen.py` applies (B) at m=floor(n^2/4). Increasing m increases t and decreases L, so every scalar interval only shrinks. Degrees excluded at equality by this screen are excluded at all larger m too. This is inequality monotonicity, not preservation of criticality under edge deletion.

Remaining degrees after the witness and scalar screens:

| n | Target | Remaining degrees |
|---:|---:|---|
|27|182|15,16|
|28|196|15,16|
|29|210|16,17|
|30|225|16,17|
|31|240|17,18|
|32|256|17,18,19|
|33|272|18,19|
|34|289|18,19,20|
|35|306|19,20,21|
|40|400|21,22,23,24|
|50|625|26,27,28,29,30|
|100|2500|51 through 62|

These are unresolved scalar survivors, not actual graphs or completed new orders. The pre-existing n=27 candidate uses additional tests.

The strict Fan bound is m<n^2/4+(n^2-(81/5)n+56)/320. Orders 28–32 each have one possible above-target edge count; n=33 has two (273,274), and n=100 has 26. Future exact work must cover every count or justify a simultaneous reduction.

Arithmetic tests passed: 1,500 integer quadratic maxima, 63,248 odd witness endpoint cases, 183,386 high-degree integer checks through n=1000. These are finite algebra regressions, not universal graph proofs.

`test_small_graphs.py` exhaustively examined all 33,864 labelled graphs of orders 3 through 6. There were 608 diameter-two-critical graphs, 552 non-bipartite. All minimum-degree complement roots and all selected-quasi-edge choices gave 780 selections; 420 had every B-vertex residual-active and supplied 840 checks of (K). No failures occurred. No positive-surplus graph occurred, so these tests do not empirically prove the positive-surplus contradiction. All implementations are from the same assistant, not external reviewers.

## 8. General attack on the remaining window

The remaining target is ceil(n/2)<Delta<alpha*n. Parameterise by n, degree offset j and edge excess e=m-floor(n^2/4). For even n=2s, Delta=s+j gives t=e+j^2. For odd n=2s+1, Delta=s+1+j gives t=e+j(j+1). After the witness reduction j>=1; residual activity applies to both equality and exclusion.

Apply (H), (K), (B) before profile enumeration. Then enforce the n=27 subset and pair cuts as universal rules. Each selected incidence carries an A-label i, a B-source u, and a supplement w, and consumes the unordered pair {u,w} at most once globally. Couple label, source and supplement capacities in one integer model rather than granting independent optimistic capacities repeatedly.

The n=27 four-column endgame trapped all selected pairs among seven B-vertices: only 21 pairs for demand 37 or 39. The next mathematical target is a uniform forced-support or subset-capacity inequality generalising that phenomenon across n. A surviving numeric relaxation is not a counterexample; shared-adjacency and full criticality constraints may still rule it out.

A proof-producing integer/pseudo-Boolean engine for this next stage is proposed, NOT implemented here. It must retain complete domain coverage, justified symmetry, and checked certificates. Timeouts, infeasibility messages and floating-point LP results do not prove exclusion. Raw graph search is a fallback for small unresolved cores. No bounded-core or fixed-parameter tractability theorem is claimed.

The concrete results here are the h-index inequality, its candidate all-order high-degree consequence, the all-k local bound, and the exact first-stage scanner.

## 9. Replay, provenance and preservation

    python3 screen.py --output RESULTS.json
    python3 test_small_graphs.py

The downloadable working package also contains an expanded ATTACK.md, SUMMARY.json and full RESULTS.json (all 7,371 scalar bands). Full numeric bands are deterministically reconstructable with the source and parameters retained here; no solver or third-party library is required. The full RESULTS.json generated in this session has SHA256 `752737cbf82a4e62feac7e7c0070f1d975266770aef585bb3e476bbb329abde5`; its environment records CPython 3.11.8, so another Python version may change environment metadata without changing the mathematical output. See REPORT.json for exact test results and file hashes.

External reviewers should prioritise the two residual injections, distinct supplements, the selected-demand-to-h step, and the b additional residual edges in (K). Arithmetic replay, universal lemma validity, novelty and external endorsement remain separate questions.
