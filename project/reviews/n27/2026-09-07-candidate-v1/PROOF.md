# Murty–Simon at n=27: candidate proof with complete finite arithmetic

7 September 2026. Prepared by ChatGPT/Codex for Paul Lenz.

**Status: complete candidate argument with internally replayed arithmetic; independent mathematical and computational review OPEN.** The programs do not formally verify the graph-theoretic lemmas. The same assistant developed and checked this work. No novelty, priority or external endorsement is claimed. The n=25 manuscript and its governed ledger remain unchanged.

## 1. Statement

The candidate statement is that every simple diameter-two edge-critical graph G on 27 vertices satisfies e(G)≤182, with equality exactly for K13,14. Deleting an edge must increase the diameter, with disconnected pairs assigned infinite distance.

The proof strategy extends the candidate n=25 residual method. It includes new fixed-column pair and forced-supplement inequalities. All exceptional numerical columns are retained and then rejected by checked integer inequalities. A surviving relaxation is never treated as an actual graph.

## 2. Published reductions

Fan's strict bound, as stated on page 2 of [Wang, On Murty-Simon Conjecture](https://arxiv.org/pdf/1205.4397), gives

\[
e(G)<\frac{n^2}{4}+\frac{n^2-16.2n+56}{320}.
\]

At n=27 the right side is exactly 146669/800=183.33625. Thus an upper-bound counterexample has exactly 183 edges. We separately examine equality at 182 edges. We do not delete edges and assume criticality is preserved. Fan's original source is [On diameter 2-critical graphs, Discrete Mathematics 67 (1987), 235–240](https://www.sciencedirect.com/science/article/pii/0012365X87901749); its full proof was not re-audited here.

Every bipartite graph of diameter two is complete bipartite, since a missing cross-part edge would have odd distance at least three. Its edge count is at most 182, with equality only for K13,14. Hence assume G non-bipartite. Theorem 4 of [Dailly, Foucaud and Hansberg](https://arxiv.org/pdf/1812.08420) bounds a non-bipartite diameter-two-critical graph with a dominating edge by floor(n²/4)−2, except for a six-vertex graph. At n=27 this gives 180. The dense cases therefore have no dominating edge.

A universal vertex forces a diameter-two-critical graph to be a star: an edge between other vertices could be deleted while all pairs remain at distance at most two. This sparse case is excluded. Write H for the complement. The complement correspondence and supercritical characterization (Theorems 3.1–3.2 of [Haynes, Henning, van der Merwe and Yeo](https://d-nb.info/1372516379/34)) leave H 3-total-domination-edge-critical; the alternative, two disjoint nontrivial cliques, corresponds to complete bipartite G.

For Δ(G)≥18, the complement has 1≤δ(H)=26−Δ(G)≤8≤0.3·27. Their Theorem 3.6(a) gives e(H)>ceil(27·25/4)=169, so e(G)≤351−170=181. Wang's Theorem 2.1 supplies the strict complement-diameter-three bound for odd orders used within this dependency. Thus Δ≥18 cannot occur at either dense edge count.

If Δ≤13, the degree sum gives 2e(G)≤351, also insufficient. It remains to examine Δ=14,15,16,17.

## 3. Witness counting for Δ=14

A direct witness is an edge whose endpoints have no common neighbour. A two-step witness is a nonedge whose endpoints have exactly one common neighbour. Every critical edge is either a direct witness or belongs to the unique length-two path of a two-step witness: choose a vertex pair whose distance exceeds two when the edge is deleted. Two different paths of length two between that pair cannot both use the deleted edge.

Every witness pair uv satisfies d(u)+d(v)≤26. For a two-step witness the neighbourhood union lies among the other 25 vertices and the intersection has size one. For a direct witness the neighbourhoods are disjoint; a union of all 27 vertices would make the edge dominating, already excluded.

Put εu=14−d(u), L0={u:εu≥2}, O={u:εu=1}, and R0=V(G)\L0. Write h=|L0| and o=|O|. A witness within R0 must have both endpoints in O. With T=378−2e(G), we have 2h+o≤T. Counting witnesses for R0–R0 edges as in the candidate n=25 argument gives

\[
e(G)\le\binom h2+h(27-h)+2\binom o2
\le\binom h2+h(27-h)+(T-2h)(T-2h-1).
\]

Indeed, a witness within L0 accounts for no R0–R0 edge, a cross-part witness accounts for at most one, and a witness within O accounts for at most two. Existing cross-part edges are subtracted when counting cross-part nonedges; adding all edge classes cancels that subtraction. These are upper bounds on covered edges and require no injective choice across witness classes.

| h | Upper bound at e=183, T=12 | Upper bound at e=182, T=14 |
|---:|---:|---:|
| 0 | 132 | 182 |
| 1 | 116 | 158 |
| 2 | 107 | 141 |
| 3 | 105 | 131 |
| 4 | 110 | 128 |
| 5 | 122 | 132 |
| 6 | 141 | 143 |
| 7 | impossible | 161 |

This excludes 183 edges. At 182 it forces h=0 and o=14 (smaller o gives a strict bound). Every witness lies within O. The sharper count is

\[
182\le e(G[O])+2\bigl(\binom{14}{2}-e(G[O])\bigr)=182-e(G[O]).
\]

Thus O is independent. Each of its 14 vertices has degree 13, forcing every edge to the other 13 vertices. Those 182 cross edges exhaust the graph, giving K13,14.

## 4. Complement notation and the general residual ledger

For Δ(G) in {15,16,17}, put a=δ(H)=26-Δ(G), b=Δ(G), M=e(H)=351-e(G). Choose v of H-degree a, put A=N_H(v), B=V(H) minus N_H[v], C=H[A], and F the complement of C on A. Thus |A|=a, |B|=b. Let k=δ(C), and write d_i=d_F(i).

For a nonedge uw of H whose endpoints miss some third vertex, 3-total-domination-edge-criticality gives an existing edge uz, after possibly interchanging u,w, whose endpoints dominate every vertex except w. Write uz→w. Its exception w is unique, and both uw and zw are absent. To derive this, choose an adjacent total dominating pair after adding uw. It must use an endpoint of the new edge; it cannot be exactly {u,w}, which misses a third vertex. Its other edge already existed and the only newly dominated vertex is the opposite endpoint of the added edge.

For each missing unordered pair bw in H[B], this observation applies because the pair misses v. Choose one cross-edge bi→w, where i is in A since it must dominate v. Different missing B-pairs select different cross-edges: a cross-edge fixes its B-endpoint and its unique exception. Call these edges selected and all other A–B edges residual. At a fixed B-source, supplements of different selected edges are distinct, since only one edge was selected for each unordered B-pair.

Write r for the number of residual edges, ρ_b for their B-degrees, R_i for their A-degrees, q_b for the selected degree at a B-source, and Q for the total selected edges. Define

\[
L=M-a-\binom b2,\qquad t=\binom a2-L.
\]

Selected cross-edges and existing B-edges together number binom(b,2). Consequently

\[
e(C)+r=L,\quad e(F)=r+t,\quad
\sum_i d_i=2(r+t),\quad \sum_bρ_b=\sum_iR_i=r. \tag{4.1}
\]

Minimum degree a in H gives a≤1+d_C(i)+d_B(i)=a-d_i+d_B(i), hence

\[
d_B(i)\ge d_i,\qquad Q\ge r+2t. \tag{4.2}
\]

The definitions make sense at general order n=a+b+1. Direct simplification gives

\[
t=e(G)-b(n-b)=e(G)-\Delta(G)(n-\Delta(G)).
\]

Thus every above-bound counterexample has t>0 at any order. For the present dense rows:

| e(G) | Δ(G) | a | b | L | t |
|---:|---:|---:|---:|---:|---:|
| 183 | 15 | 11 | 15 | 52 | 3 |
| 182 | 15 | 11 | 15 | 53 | 2 |
| 183 | 16 | 10 | 16 | 38 | 7 |
| 182 | 16 | 10 | 16 | 39 | 6 |
| 183 | 17 | 9 | 17 | 23 | 13 |
| 182 | 17 | 9 | 17 | 24 | 12 |

## 5. All B-vertices are residual-active

This argument requires t>0 and the selected-pair convention of Section 4; it does not fix n. Suppose ρ_b=0, and write S=N_A(b), T=A minus S. Every bi with i in S is selected. An F-edge from S to T would leave an A-vertex undominated by a selected edge whose unique exception belongs to B. Thus F has no S–T edge.

For i in S, let w_i be the supplement of bi. These w_i are distinct. For each F-edge ij within S, the selected edge bj must dominate w_i, since its exception w_j is different. Since bw_i is absent, jw_i is an edge. It is residual because j and w_i both miss the A-vertex i. Similarly iw_j is residual. All 2e(F[S]) such edges are distinct, determined by their A-endpoints and distinct supplement labels.

For each F-edge uw within T, the pair misses b, so a quasi-edge uz→w or wz→u exists. Its auxiliary z must dominate b. It cannot be v or b; if in A it would be in S, but every S–T pair is a C-edge, contradicting its failure to dominate the exception in T. Thus z lies in B. The quasi-edge is residual, since its exception belongs to A. Distinct F-edges give distinct cross-edges, their A-endpoint and unique exception identifying the missing F-edge. These e(F[T]) edges have A-endpoints in T and are disjoint from the first family.

Therefore

\[
r\ge2e(F[S])+e(F[T])=e(F)+e(F[S])\ge r+t.
\]

All six rows above have t>0, a contradiction. Consequently every B-vertex has ρ_b≥1, so **r≥b**. This proof also covers S empty and assumes no diameter bound on H.

## 6. Small and large k, and Δ(G)=17

Since e(C)≥ceil(ak/2), the ledger implies

\[
b\le r\le L-\lceil ak/2\rceil. \tag{6.1}
\]

For small k choose x in A with C-degree k, write Y=N_C(x), and X=A minus ({x} union Y). Any missing pair uw inside X misses x. Its quasi-edge auxiliary lies in Y or B: it must dominate x, and v is adjacent to the exception and hence cannot serve as auxiliary. A B auxiliary yields a distinct residual cross-edge with A-endpoint in X.

Let P be the family of these B-auxiliary edges, of size m. Each B-endpoint z used by P forces an edge xz to dominate x. This edge is residual: if selected, it would miss the exceptional X-vertex of the original member of P. The edge xz is outside P. For every unused B-vertex choose an incident residual edge, available by Section 5 and also outside P. Distinct B-endpoints distinguish these b extra edges. Thus

\[
b\le r-m. \tag{6.2}
\]

For k=0, all missing pairs in X have B auxiliaries, so

\[
m=\binom{a-1}{2}-L+r,
\qquad b\le L-\binom{a-1}{2}. \tag{6.3}
\]

For k=1 let Y={y} and s=e_C(y,X). There are binom(a-2,2)-L+1+s+r missing X-pairs, and at most s can have auxiliary y: the relevant y–X edges are distinct quasi-edges. Hence

\[
b\le L-1-\binom{a-2}{2}. \tag{6.4}
\]

For Δ=17, r≥17 and r≤L−ceil(9k/2), with L=23 or 24. Hence k≥2 is impossible. At k=0 the right side of (6.3) is −5 or −4; at k=1 the right side of (6.4) is 1 or 2. Neither can reach b=17. This excludes Δ=17 at both edge counts.

For Δ=16, k=0,1 are excluded by (6.3)–(6.4); k≥5 is excluded by (6.1). For Δ=15, k=0 is excluded and k≥7 is excluded. The k=1 case is retained at both edge counts: (6.4) gives 15≤15 or 15≤16, not a contradiction.

The full retained bands are generated from the following table, including any zero-cardinality numerical bands:

| Δ | e | k | r range |
|---:|---:|---:|---|
| 16 | 183 | 2,3,4 | 16≤r≤38−5k |
| 16 | 182 | 2,3,4 | 16≤r≤39−5k |
| 15 | 183 | 1,…,6 | 15≤r≤52−ceil(11k/2) |
| 15 | 182 | 1,…,6 | 15≤r≤53−ceil(11k/2) |

## 7. Necessary bounds for selected edges

For every selected bi→w,

\[
d_i\le ρ_b+ρ_w,\qquad d_i\le ρ_b+R_i,
\qquad d_i\le ρ_b+q_b-1,\qquad q_b+ρ_b\le a. \tag{7.1}
\]

For the first bound, each F-neighbour u of i must be adjacent to b. If bu is residual, charge it at b. Otherwise bu is selected with a supplement different from w, so it must dominate w; thus uw exists. It is residual since u and w both miss i. Distinct u give distinct charges at b or w.

For the second, again at most ρ_b F-neighbours u of i yield residual bu. Every remaining selected bu has a distinct supplement w_u, different from w. Selected bi must dominate w_u, forcing iw_u. This edge is residual because i and w_u miss u. The distinct supplements give at least d_i-ρ_b residual edges at i.

The third bound follows because b is adjacent to i and all its F-neighbours, and d_A(b)=ρ_b+q_b. The fourth is the size of A.

Let S_j={i:d_i≥j}. From d_B(i)≥d_i, at least

\[
\ell_j=\sum_{i\in S_j}d_i-\sum_b\min(ρ_b,|S_j|)
\]

selected incidences have labels in S_j. Each uses a distinct unordered B-pair with residual sum at least j. Therefore

\[
\ell_j\le |\{\{b,w\}:b\ne w,\ ρ_b+ρ_w\ge j\}|. \tag{7.2}
\]

For Δ=16, (7.2) eliminates all 5,802 numerical outer states at 183 edges and all 8,970 at 182 edges. Two Python implementations independently enumerate the finite domains and agree on every state key and disposition. Thus only Δ=15 needs the later capacity tests. Both implementations share the mathematical lemmas.

## 8. Finite domains, source capacities and column symmetry

For each retained (k,r), enumerate every nondecreasing degree list d of length a with entries 0,…,D=a−1−k, maximum exactly D, and sum 2(r+t). Independently enumerate every nondecreasing positive residual list ρ of length b, entries at most a and sum r. Sorting uses independent relabellings of A and B. Nongraphical degree sequences are retained, so this is a necessary-condition relaxation.

Apply (7.2) first. For a B-source b and trial q≤min(a−ρb,|B|−1), its q selected labels satisfy di≤ρb+q−1 and must match distinct supplements w≠b satisfying di≤ρb+ρw. Let cb be the largest feasible q in this relaxed matching problem, or zero. Then qb≤cb, so sum cb must reach r+2t. For each threshold j apply the same matching bound to labels in Sj, using eligibility di≤ρb+cb−1; the sum of source bounds must reach the lower bound in (7.2).

Put hρ=max{j: at least j residual entries are at least j}. A label i needs at least di−Ri selected sources when positive. Each of those distinct sources has ρb≥di−Ri by (7.1). Hence

\[
R_i\ge\max(0,d_i-h_\rho).
\]

Reject if these lower bounds sum to more than r. Otherwise the residual columns obey those bounds, Ri≤b and sum Ri=r.

**Column symmetry lemma.** Within a block of equal di, permuting the A-labels permutes Ri and the selected incidences while preserving every condition used here. Each possible graph therefore has a representative with Ri nondecreasing within each equal-degree block. Enumerating those representatives is sufficient. No order is imposed between blocks of different degrees.

For a block of m equal degree labels with residual-value multiplicities m1,…,ms, its representative accounts for m!/(m1!···ms!) labelled columns. Multiplying over blocks gives the orbit weight. The sum of these weights is checked against the coefficient of x^r in

\[
\prod_{i\in A}\bigl(x^{\ell_i}+x^{\ell_i+1}+\cdots+x^b\bigr),
\qquad \ell_i=\max(0,d_i-h_\rho).
\]

A separate dynamic program counts the canonical representatives themselves. Every representative is generated once in lexicographic order. The labelled-weight count is a coverage check; it does not mean every labelled column is individually visited.

For a fixed R, repeat the source-cap calculation with additional eligibility di≤ρb+Ri. The selected demand is

\[
Q_{\min}(R)=\sum_i\max(0,d_i-R_i).
\]

A selected edge at source b has a supplement adjacent to its other qb−1 selected A-labels: those selected edges have distinct exceptions and must dominate that supplement. Thus its supplement w has dA(w)≥qb−1. Since dA(w)=ρw+qw≤ρw+cw, source b needs qb distinct supplements with ρw+cw≥qb−1.

Reduce each cb to the largest q≤cb with at least q such other vertices, using the previous caps simultaneously. Repeat until stable. Every iteration preserves qb≤cb by induction. The caps are nonnegative integers and decrease, so the process terminates. Reject whenever their sum is below Qmin.

## 9. Subset-capacity cuts

For a nonempty S⊆A and already justified caps c, define

\[
E_b(S)=\{i\in S:d_i\le\rho_b+c_b-1,\ d_i\le\rho_b+R_i\}.
\]

Each real configuration satisfies

\[
\sum_{i\in S}\max(0,d_i-R_i)\le
\sum_{b\in B}\min(c_b,|E_b(S)|). \tag{9.1}
\]

The left side is a lower bound on selected incidences in S. At source b, each selected label lies in Eb(S), and simplicity permits at most one selected edge per source/label pair, with at most cb altogether.

The search uses an integer flow network: source-to-label arcs have the demands max(0,di−Ri), eligible label-to-B-source arcs have capacity one, and B-source-to-sink arcs have capacity cb. A failed flow yields a subset S; its strict violation of (9.1) is recorded. The checker does not trust the flow outcome and does not run the flow algorithm: it rederives the caps and checks the recorded strict integer inequality directly. A zero mask preserves the column for the next stage.

The source-cap replay uses threshold cuts for matching. If labels have requirements d and suppliers have capacities s, every matching has size at most

\[
\#\{d<t\}+\#\{s\ge t\}
\]

for each threshold t, and at most the number of labels or suppliers. For nested threshold neighbourhoods the minimum of these bounds is the matching number. This can also be seen by greedily matching the easiest remaining label to the weakest adequate supplier. In the checker only the upper-bound direction is needed for sound capacity bounds; it reproduces the search's capacities exactly. A six-state Python check separately uses augmenting paths, fully labelled enumeration and exhaustive subsets.

## 10. Fixed-column pair inequality

With R fixed, the lower bound for selected labels in Sj can be strengthened to

\[
\boxed{\sum_{i:d_i\ge j}\max(0,d_i-R_i)
\le\#\{\{b,w\}\subset B:\rho_b+\rho_w\ge j\}.} \tag{10.1}
\]

Proof: every selected edge with such a label satisfies the pair bound in (7.1). Its unordered source/supplement pair is different from every other selected edge's pair, by Section 4. This gives the stated injection. The fixed R supplies the left side; no graph-realizability assumption is made about other retained columns.

At 183 edges, all 190 columns remaining after Section 9 violate (10.1). At 182 edges, 35,241 of 35,245 remaining columns violate it. The four others are treated next. Every strict violation and complete survivor coverage is checked independently by check_final.py.

## 11. Forced labels and the supplement-pair budget

Write Di=max(0,di−Ri) and let Ei be the set of sources permitted for label i by the two eligibility inequalities in Section 9. If Di>|Ei|, the column is impossible. If Di=|Ei|>0, every source in Ei must select label i. Let fb count the labels thereby forced at source b. Then qb≥fb.

If bi is selected with supplement w, necessarily

\[
q_b\ge\lambda_{bi}:=\max(1,f_b,d_i-\rho_b+1),
\qquad
\rho_w+c_w\ge q_b-1\ge\lambda_{bi}-1. \tag{11.1}
\]

The first bound combines forced labels and source closure. The second is the supplement's required adjacency to the other selected labels, proved in Section 8.

Call an unordered pair {b,w} permitted if at least one orientation and label i satisfy: b∈Ei, di≤ρb+ρw, λbi≤cb, and ρw+cw≥λbi−1. Every actual selected edge maps injectively to a permitted pair. Therefore

\[
\boxed{Q_{\min}(R)\le\#\{\text{permitted unordered pairs}\}.} \tag{11.2}
\]

For the final four columns this becomes an elementary count. All have eight B-vertices with ρ=1 and c=0, and seven other B-vertices. No selected edge can start at the eight zero-cap sources. At a remaining source with ρ=3, every available label has d≥5, so any selected edge forces qb≥3 by closure. The remaining sources have at least four forced labels each (six in the two k=1 columns; five or four in the k=2 columns). Hence every selected source has qb≥3.

Each supplement must consequently have at least two A-neighbours. The eight vertices with ρ=1,c=0 have at most one, so none can be a supplement. Every selected unordered pair lies among the other seven vertices, leaving at most binom(7,2)=21 pairs. But Qmin is 39 for the two k=1 columns and 37 for the two k=2 columns. Thus all four are impossible.

The exact d,ρ,R,c arrays, forced-label counts and 21 permitted pairs are printed in d15_182_supplement_certificates.json. The checker reconstructs the sets and inequalities from those arrays. Caps used here are the already replayed Section 8 bounds.

## 12. Complete computation and assembly

| Scope | Outer states | Canonical columns | Labelled columns represented | After subset cuts | After fixed-column pair cuts | Final survivors |
|---|---:|---:|---:|---:|---:|---:|
| Δ16, e183 | 5,802 | 0 | 0 | 0 | 0 | 0 |
| Δ16, e182 | 8,970 | 0 | 0 | 0 | 0 | 0 |
| Δ15, e183 | 5,547,774 | 8,495,391 | 130,442,305 | 190 | 0 | 0 |
| Δ15, e182 | 7,047,851 | 72,483,155 | 1,320,569,120 | 35,245 | 4 | 0 |

The outer-domain checker counts bounded multisets by generating functions, checks membership and strict ordered-key uniqueness for every stored state, and verifies every pruning inequality. It matches each retained state to the complete column frontier. The column replay rederives all source caps, checks all 782,933 strict subset certificates (20,344 at 183 edges and 762,589 at 182 edges), and matches every per-state column digest. It preserves 35,435 columns for final checking, all rejected by Sections 10–11. The details and commands are in README.md and RESULTS.json.

Fan leaves only 183 edges above the target. The degree sum covers Δ≤13; Section 3 covers Δ14; Sections 4–11 cover Δ15,16,17; the published complement bound covers Δ≥18. The same partition at 182 edges leaves only K13,14. This graph has diameter two, and removing any cross edge increases its endpoints' distance to three. It attains 182 edges.

Thus the stated lemmas and the checked finite calculations together give a complete candidate proof of the order-27 upper bound and equality characterization.

## 13. Audit limits and provenance

The complete arithmetic checks passed internally. The graph-theoretic statements were read and rederived, and actual-graph falsification tests passed on all labelled graphs through order six (after reduction to representatives) and seeded examples through order 27. Such samples do not prove universal lemmas; in particular no positive-surplus actual graph occurred. The strict-surplus contradiction remains a mathematical argument.

A full column replay uses the same C++ domain generator with a different capacity calculation and direct certificate checking. Its domain counts are checked by separate recurrences and orbit weights; a six-state cross-language test also fully enumerates 2,071 labelled columns. This is not a second independently authored full graph-proof verification. The outer checker imports no search source. All implementations were produced by the same assistant.

In the C++ production scopes a=11 and b=15. Even the unrestricted labelled column box has only 16^11=2^44 elements, so its per-domain counts fit the 64-bit unsigned counters. The recorded aggregate counts also fit that type. The capacities, degree sums and inequality comparisons use exact integers, not floating point.

The additional actual-graph checks cover the fixed-column pair bound, forced-source lower bounds and the supplement-pair filter, using actual selected degrees and looser upper bounds. The original matching-helper length defect is corrected in the new generic Python copy; frozen n=25 sources are unchanged. No SAT solver, floating-point infeasibility claim, or unpreserved historical certificate is used.

External reviewers should focus on the residual injections, the equal-degree column symmetry, preservation of upper bounds during repeated refinement, the distinct-pair injection in (10.1), and the forced-source/supplement argument in (11.1)–(11.2). Independent mathematical review, reproduction by another researcher and any formal verification remain open. This document does not establish novelty or priority.
