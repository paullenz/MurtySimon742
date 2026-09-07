# A complete candidate proof at order 28

7 September 2026. Paul Lenz directed the research; ChatGPT/Geeps developed the argument, computations and internal checks.

**Status: complete candidate mathematical route with internally checked finite evidence; independent mathematical review, independent researcher reproduction and formal verification OPEN.** This is not an announcement that the full Murty–Simon conjecture has been settled. The earlier n=25 and n=27 editions remain unchanged.

## Candidate theorem

Every simple diameter-two edge-critical graph G on 28 vertices has at most 196 edges. Equality holds exactly for the complete bipartite graph K(14,14).

A graph is diameter-two edge-critical when it has diameter two and removing any one edge increases its diameter, allowing disconnected distance to be infinite. The proof uses the two published reductions identified below and the replayable finite core exclusion in the accompanying v3–v7 evidence. The computational portion is part of the proof, not an empirical graph sample.

## 1. Exceptional classes and degrees at most 14

A bipartite graph of diameter two must be complete bipartite: opposite-part vertices cannot be joined by a path of length two. Its edge count is k(28-k)<=196, with equality only at k=14. Conversely, K(14,14) is diameter-two critical: deleting a cross edge leaves its endpoints at distance three.

If G has a universal vertex, no edge between two other vertices can be critical, since their route through the universal vertex remains. Hence G is a star and has only 27 edges. From now on G is non-bipartite and not a star.

Dailly–Foucaud–Hansberg, Theorem 4 [2], says that a non-bipartite diameter-two-critical graph with a dominating edge, other than their graph H5, has at most floor(n²/4)-2 edges. Their H5 has six vertices, so it is irrelevant at n=28. Consequently a graph of interest with m>=196 has no dominating edge.

If Delta<=13, the degree sum gives m<=28*13/2=182. If Delta=14 and m>=196, the degree sum forces m=196 and every degree to be 14. This is impossible in the no-dominating-edge case, as follows.

For every critical edge e there is a pair of vertices whose distance was at most two and becomes greater than two upon deleting e. If the pair was adjacent, e joined the pair and they had no common neighbour; otherwise they had exactly one common neighbour and e lay on their unique length-two path. Two distinct length-two paths of a nonadjacent pair cannot both contain the same edge, so these cases cover every critical edge.

An adjacent pair with no common neighbour has disjoint open neighbourhoods; their union has at most 27 vertices if the edge is not dominating. Its endpoint degree sum is therefore at most 27. For a nonadjacent pair with exactly one common neighbour, neither endpoint lies in the union of the open neighbourhoods, so the degree sum is at most 26+1=27. But every pair in a 14-regular graph has degree sum 28. There is no witness pair for any edge: contradiction.

It remains to exclude m>=196 for Delta>=15.

## 2. Complement decomposition and residual activity

By Haynes–Henning–van der Merwe–Yeo, Theorems 3.1–3.2 [1], the complement H of a non-bipartite diameter-two-critical graph without the star exception is 3-total-domination-edge-critical. The other complement class, 4-supercritical graphs, consists of two disjoint nontrivial cliques and corresponds to the complete-bipartite case already handled. In particular, when an H-nonedge uw fails to dominate a third vertex, adding uw supplies an existing edge ui whose endpoint open neighbourhoods cover every vertex except w, after possibly exchanging u,w. This is the published quasi-edge observation [1, Observation 3.4]. The exception is unique.

Choose v with minimum H-degree a=27-b, where b=Delta(G). Let A=N_H(v), B=V(H) minus N_H[v], so |A|=a and |B|=b. Put C=H[A], F=the complement of C on A. For each missing B-pair choose one cross quasi-edge: its auxiliary must lie in A to dominate v. Different B-pairs cannot choose the same cross edge, because the B-endpoint and unique exception identify the pair. Selected labels and exceptions at a source are distinct.

Call the other A-B edges residual, with total r and B-degrees rho. Counting the existing B-edges and selected cross edges gives

    e(F)=r+t,   t=m-b(28-b).

For b>=15 and m>=196, t>0. We need the all-active lemma: every B-vertex has rho>=1.

Suppose instead that a vertex u has rho_u=0. Let S=N_H(u) intersect A and T=A minus S. Every ui for i in S is selected. There are no F-edges between S and T: a selected ui would otherwise miss an A-vertex in addition to its B-exception.

Let w_i be the exception of ui; these exceptions are distinct. If ij is an F-edge inside S, the selected uj must dominate w_i and selected ui must dominate w_j. Thus jw_i and iw_j exist. They are residual because each misses the other A-endpoint of ij. These give 2e(F[S]) distinct residual edges, with A-endpoints in S.

For an F-edge pq inside T, the H-nonedge pq fails to dominate u. Its quasi-edge auxiliary cannot be v or u; an auxiliary in A would have to be in S to dominate u, but every S–T pair is a C-edge, so it would also dominate the supposed exception in T. Hence the auxiliary is in B. The resulting cross quasi-edge is residual because its exception is in A. Distinct F-edges give distinct cross edges: their A-endpoint and unique exception identify the original pair. These e(F[T]) edges have A-endpoints in T and are disjoint from the first family.

Therefore

    r>=2e(F[S])+e(F[T])>=e(F)=r+t,

a contradiction. Thus all rho_u>=1. Empty S or T causes no exception to the count.

## 3. Degrees at least 17: direct h-index exclusion

Let d_i=d_F(i), R_i be the residual degree at label i, and x_i its selected degree. Minimum H-degree gives R_i+x_i>=d_i. For a selected ui -> w the residual charging argument gives d_i<=rho_u+R_i; see PROOF.md Section 2 and CORE_SCOPE_AUDIT.md for the explicit injection. Hence a label of positive demand s_i=max(0,d_i-R_i) requires at least s_i distinct selected sources with rho>=s_i.

Let h be the h-index of the residual degrees: the largest integer for which at least h entries are at least h. Then s_i<=h. Also

    r+2t=sum_i(d_i-R_i)<=sum_i s_i<=a h.

Activity gives r>=h²+(b-h)=b+h(h-1). Combining,

    b+2t <= (a+1)h-h² <= floor((a+1)²/4)
           =floor((28-b)²/4).                           (3.1)

At m>=196 this fails for every integer b=17,...,26. The exact endpoint values are:

| b | minimum t=196-b(28-b) | b+2t | floor((28-b)²/4) |
|---:|---:|---:|---:|
|17|9|35|30|
|18|16|50|25|
|19|25|69|20|
|20|36|92|16|
|21|49|119|12|
|22|64|150|9|
|23|81|185|6|
|24|100|224|4|
|25|121|267|2|
|26|144|314|1|

The left side only increases with a larger m. Degree 27 was the universal-vertex/star case. This branch needs no published numerical edge cap and does not use the project's uniform 0.6132704598 coefficient.

## 4. Degree 16: the previously preserved exact exclusion

Here a=11, b=16 and t>=4. The demand-support v3 argument gives, at t=4, 39 possible charging-demand multisets. Of these, 34 fail its threshold-support bound, one fails the source-count bound, three have exact weighted dual contradictions, and the final multiset has all 604 residual row profiles excluded by exact prefix/source-capacity inequalities.

The complete domain and every rejection were independently recomputed in this session by the preserved standard-library checker. `evidence/V3_N28_D16_CHECK_REPORT.json` records 39 demand profiles, 604 residual profiles, complete arithmetic coverage and rejected corrupted controls.

For higher t, the initial charging condition becomes stronger and each allowed r-interval becomes smaller. The support and dual upper budgets cannot increase; the residual-row certificates are independent of t once the row is fixed. Thus the v3 proof's own explicit monotonicity argument covers all t>=4, and therefore all m>=196. This is monotonicity of necessary inequalities, not deletion-preserves-criticality. No later exact-column test is granted this property without proof.

This branch depends on the mathematical necessity of the v3 counting inequalities as written in its unchanged PROOF.md. Exact arithmetic checks do not replace review of those arguments.

## 5. Degree 15: complete finite core exclusion and density reduction

Here a=12, b=15, and t=m-195>=1. Section 2 gives activity. Moreover C=H[A] has no isolated vertex. If x were isolated, every missing pair pq inside X=A minus {x} would fail to dominate x. Its quasi-edge auxiliary must be in B: v is adjacent to the supposed A-exception, and no A-vertex can dominate x. These give e(F[X]) distinct residual cross edges. Each B-endpoint used also forces a residual x-edge, outside that family; unused B-endpoints supply residual edges by activity. Thus

    r>=e(F[X])+15=r+t-11+15,

forcing t<=-4, a contradiction.

The original graph consequently produces an active B-quasi-edge core with positive C-minimum degree in the sense of PROOF.md Section 6. The finite v4–v7 route excludes EVERY such core at t=1, not just critical graphs. The exact chain is:

| Stage | Complete checked scope | Remaining |
|---|---:|---:|
| Charging-demand domain and initial cuts | 18,645 demand patterns | 1,976 demand patterns |
| Residual-row expansion and source/supplement bounds | 17,669,896 rows | 24,411 rows |
| Exact slack and projected pair restrictions | 24,411 rows | 13,196 rows |
| v5 individual columns, matching and one-source projections | 13,196 rows | 7,725 rows |
| v5 supplement activation | 7,725 rows | 6,918 rows |
| v6 shared fractional columns, F and pair incidences | 6,918 rows | 4,617 rows |
| v6 outgoing-degree types and pair flow | 4,617 rows | 479 rows |
| v6 checked integer-count branching | 479 rows | 388 rows |
| v7 joint arc / option / endpoint-degree events | 388 rows | 215 rows |
| v7 source (q,p) / label x consistency | 215 rows | **0** |

The residual enumeration does not count graphs. It covers a proved necessary numerical domain; every actual core maps into that domain. Later stages only remove rows through proved necessary constraints. All adjacent frontier files were compared, and all rows are accounted for by the independent checking route.

For t>1, remove t-1 edges from F, equivalently add them to H[A], keeping every cross edge, every B-edge and the selected assignment fixed. This does NOT preserve diameter-two criticality, and it is not claimed to do so. It DOES preserve exactly the weaker core axioms: each chosen B-quasi-edge still dominates every vertex except its unchanged B-exception, activity is unchanged, minimum H-degree is maintained, and positive C-minimum degree is maintained. Its new surplus is t'=1. Recompute its d and s. It must then lie somewhere in the completely excluded target core domain, an impossibility.

The closure lemma and its numerical-scope audit are written out separately because this is the new obligation that allows the 196-edge calculation to cover all higher m. No unproved assertion about the old column tests' monotonicity is used.

Thus degree 15 also admits no graph with m>=196.

## 6. Conclusion and trust boundary

Every non-bipartite diameter-two-critical graph of order 28 has strictly fewer than 196 edges in this candidate route. The only graphs attaining 196 are therefore the balanced complete-bipartite graphs already handled in Section 1, completing both the proposed upper bound and equality characterization.

The finite computations were reproduced by separately written exact checkers, including complete branch trees where used, and the new graph-to-model maps were tested with rational arithmetic. The full v7 certificate checker imports neither optimisation software nor discovery builders. None of this is independent expert mathematical review or formal-kernel verification. In particular, the original residual injections, every model's necessity for a weak core, the scope audit, and the published dependencies remain explicit mathematical trust boundaries.

No sampled positive-surplus critical graph was found. That does not constitute evidence of complete graph enumeration; universal validity rests on the proof plus complete necessary-domain exclusion. No new order other than 28 is concluded by this document, and no all-order theorem is claimed.

## Primary dependencies and exact evidence

[1] Haynes, Henning, van der Merwe and Yeo, *A maximum degree theorem for diameter-2-critical graphs* (2014), Theorems 3.1–3.2 and Observation 3.4. Primary full text: https://d-nb.info/1372516379/34 .

[2] Dailly, Foucaud and Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs* (2019), Theorem 4. Primary preprint: https://arxiv.org/pdf/1812.08420 .

[3] Original demand-support v3 archive, n=28/Delta16 scope; original label-tail v4, column-propagation v5, shared-adjacency v6 archives; this degree-load v7 package. `DEPENDENCIES.json` pins their hashes. `replay_chain.py` in the complete audit bundle verifies cross-stage identity and reruns the full required arithmetic route. Fresh reports are preserved in this checkpoint, separately from every unchanged historical archive.
