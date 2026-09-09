---
title: "Murty-Simon at n=25: Fan-free candidate proof"
subtitle: "Reviewer edition 2 - historical v1 preserved"
author: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"
date: "9 September 2026"
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
---

\begin{abstract}
This reviewer edition removes G. Fan's 1987 theorem as a logical dependency of the fixed-order candidate proof while retaining Fan's result as historical attribution. Every larger edge count formerly excluded only by Fan is now covered directly by the project's witness/residual necessary conditions and exact finite arithmetic. The historical reviewer-v1 package and frozen proof remain preserved. Independent mathematical and computational review remain open.
\end{abstract}

**Canonical claim.** `e(G) <= 156, equality exactly K(12,13)`.

**Logical source.** `project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md`.

**History rule.** Reviewer v1 is not overwritten; edition 2 is a new proof surface.

---

# N=25 Murty–Simon: Fan-free reviewer proof, edition 2

9 September 2026. Built deterministically from the frozen 6 September candidate proof.

**Status:** complete candidate argument with internally checked exact arithmetic; independent mathematical and computational review OPEN. This edition removes Fan's theorem as a logical dependency while preserving and citing the historical Fan-based v1 proof.

**Historical source preserved:** `project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md` (SHA-256 `9f4daa246f794ab9e2de29fb968911ecdbb7b8698982dc6af234db6ba18b2aa9`).

**Fan-free replacement component:** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`.

---

## 1. Statement and scope

The target statement is: every simple diameter-2 edge-critical graph G on 25 vertices satisfies

\[
e(G)\le156,
\]

with equality exactly for the complete bipartite graph K_{12,13}. Diameter-2 edge-critical means that G has diameter two and deleting any edge increases its diameter, with disconnected pairs assigned infinite distance.

Both the upper-bound and equality chains are complete as candidate arguments. The equality chain uses the new subset-capacity certificates described below; all required cases have been eliminated and cross-checked, with exact numerical records in RESULTS.md. No mathematical conclusion is inferred merely from a program terminating successfully.

## 2. Published reductions and their exact numerical effect

### Fan-free upper-range reduction

Historically, the v1 proof used G. Fan's 1987 theorem (*On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235–240, DOI 10.1016/0012-365X(87)90174-9) to reduce an above-target graph to 157 edges. Fan is retained here for attribution, but **his theorem is not a logical dependency of this edition**.

The replacement is proved in `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`. Briefly: the degree sum excludes `Delta<=12`; the existing complement maximum-degree theorem excludes `Delta>=17`; the Section 3 witness inequality at `Delta=13` is monotone stronger as `m=e(G)` increases and therefore excludes every `m>=157`; the frozen residual proof below excludes `m=157` for `Delta=14,15,16`; and a new exact necessary-condition scan covers every larger degree-sum-possible edge count, namely `m=158..175` at `Delta=14`, `158..187` at `Delta=15`, and `158..200` at `Delta=16`. Across those 91 scopes it enumerates 128,754 outer numerical states and leaves **zero** survivors. Hence every above-target graph has exactly 157 edges before the original dense-case analysis below is invoked.

The old Fan-based reduction remains available in the frozen v1 proof for historical comparison.

A bipartite graph of diameter two must be complete bipartite: a missing cross-part edge would have odd distance at least three. Therefore such graphs have at most 12 times 13 = 156 edges, with equality only for K_{12,13}.

Henceforth, when considering 156 or 157 edges, assume G is non-bipartite. By Theorem 4 of [Dailly, Foucaud and Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*](https://arxiv.org/pdf/1812.08420), a non-bipartite diameter-2-critical graph with a dominating edge has at most floor(n²/4)-2 edges, except for their six-vertex graph H5. At order 25 the exception is irrelevant and the bound is 154. Consequently our G has **no dominating edge**.

Let H be the complement of G. A universal vertex in a diameter-2-critical graph forces the graph to be a star, since any edge between other vertices could be deleted while retaining diameter at most two. This sparse case is excluded. The complement correspondence now gives that H is 3-total-domination-edge-critical, or 4-total-domination-supercritical. The latter case is the disjoint union of two nontrivial cliques, already covered by complete bipartite G. We use the former case. Theorem 3.6(a) of [Haynes, Henning, van der Merwe and Yeo, *A maximum degree theorem for diameter-2-critical graphs*](https://d-nb.info/1372516379/34) states that minimum degree δ(H) at most 0.3n implies e(H)>ceil(n(n-2)/4). At n=25, δ(H) at most 7 implies e(H) at least 145 and e(G) at most 155. Thus maximum degree Δ(G) at least 17 is excluded. The complement correspondence and exceptional characterization are that paper's Theorems 3.1 and 3.2. For the odd-order complement-diameter-three case mentioned in its proof, Wang's Theorem 2.1 explicitly supplies the strict bound for odd as well as even orders.

Finally, Δ(G) at most 12 implies 2e(G) at most 25 times 12 = 300. For either dense edge count, it remains to consider **Δ(G)=13,14,15,16**.

## 3. A direct witness proof for Δ(G)=13, including equality

Call an edge a direct witness if its endpoints have no common neighbour. Call a nonedge a two-step witness if its endpoints have exactly one common neighbour. Every critical edge is either a direct witness itself or belongs to the unique length-two path of a two-step witness. Indeed, choose a vertex pair whose distance becomes greater than two on deleting the edge. If that pair was adjacent, it is the deleted edge and has no common neighbour. Otherwise every length-two path between the pair used the deleted edge, and there is exactly one such path. A two-step witness can account for at most two critical edges.

Each witness pair uv satisfies d_G(u)+d_G(v) at most 24. For a two-step witness, its neighbourhood union lies in the other 23 vertices and their intersection has size one. For a direct witness, the neighbourhoods are disjoint; a union of all 25 vertices would make uv a dominating edge, already excluded.

Write ε_u=13-d_G(u). Set L={u:ε_u at least 2}, O={u:ε_u=1}, and R=V(G) minus L; let h=|L| and o=|O|. A witness pair lying wholly in R must have both endpoints in O, because ε_u+ε_v must be at least two. If T=325-2e(G), then

\[
2h+o\le T.
\]

Let a=e(G[L]), b=e_G(L,R), and c=e(G[R]). Any edge counted by c can have one of only three sorts of witnesses: a direct witness within O; a two-step witness within O, whose path accounts for at most two R-edges; or a two-step witness with one endpoint in each of L and R, whose path accounts for at most one R-edge. A pair within L cannot witness an R-edge. There are at most h(25-h)-b cross-part nonedges. Hence

\[
c\le 2\binom{o}{2}+h(25-h)-b,
\qquad
e(G)\le \binom h2+h(25-h)+2\binom o2. \tag{3.1}
\]

The estimates deliberately overcount direct witnesses in O and need no injective assignment between different witness classes.

For 157 edges T=11. For 156 edges T=13. The right side of (3.1) increases with o, so substitute o=T-2h:

| h | Upper bound when e=157 | Upper bound when e=156 |
|---:|---:|---:|
| 0 | 110 | 156 |
| 1 | 96 | 134 |
| 2 | 89 | 119 |
| 3 | 89 | 111 |
| 4 | 96 | 110 |
| 5 | 110 | 116 |
| 6 | impossible | 129 |

This excludes 157 edges. At 156 edges it forces h=0, o=13. Every witness lies within the 13-vertex set O, so the sharper direct count gives

\[
156=e(G)\le |D[O]|+2|S[O]|
\le e(G[O])+2\bigl(\binom{13}{2}-e(G[O])\bigr)
=156-e(G[O]).
\]

Thus O is independent. Each of its vertices has degree 12 and must be adjacent to all the other 12 vertices. These cross edges already number 156, leaving no edges within the other part. Therefore G=K_{12,13}. Under our non-bipartite assumption this is a contradiction, completing this degree case.

## 4. Complement notation and the general residual ledger

For Δ(G) in {14,15,16}, put a=δ(H)=24-Δ(G), b=Δ(G), M=e(H)=300-e(G). Choose v of H-degree a, put A=N_H(v), B=V(H) minus N_H[v], C=H[A], and F the complement of C on A. Thus |A|=a, |B|=b. Let k=δ(C), and write d_i=d_F(i).

For a nonedge uw of H whose endpoints miss some third vertex, 3-total-domination-edge-criticality gives an existing edge uz, after possibly interchanging u,w, whose endpoints dominate every vertex except w. Write uz→w. Its exception w is unique, and both uw and zw are absent. To derive this, choose an adjacent total dominating pair after adding uw. It must use an endpoint of the new edge; it cannot be exactly {u,w}, which misses a third vertex. Its other edge already existed and the only newly dominated vertex is the opposite endpoint of the added edge.

For each missing **unordered** pair {b,w} in H[B], this observation applies because the pair misses v. Fix that unordered pair first, and designate exactly one corresponding cross-edge bi→w after interchanging b and w if necessary; i lies in A because the edge must dominate v. If both orientations happen to be available as possible quasi-edges, only one is designated selected for this unordered pair. Thus the map from selected edges to missing unordered B-pairs is injective by construction: a selected edge fixes its B-source and its unique B-exception, and opposite orientations of the same pair can never both be selected. Call these designated edges selected and all other A–B edges residual. At a fixed B-source, supplements of different selected edges are distinct, since there is only one selected representative for each unordered B-pair.

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

The exact parameters are:

| e(G) | Δ(G) | a | b | L | t |
|---:|---:|---:|---:|---:|---:|
| 157 | 14 | 10 | 14 | 42 | 3 |
| 156 | 14 | 10 | 14 | 43 | 2 |
| 157 | 15 | 9 | 15 | 29 | 7 |
| 156 | 15 | 9 | 15 | 30 | 6 |
| 157 | 16 | 8 | 16 | 15 | 13 |
| 156 | 16 | 8 | 16 | 16 | 12 |

## 5. All B-vertices are residual-active

This is the dimension-independent form of the attachment's inactive-vertex lemma. Suppose ρ_b=0, and write S=N_A(b), T=A minus S. Every bi with i in S is selected. An F-edge from S to T would leave an A-vertex undominated by a selected edge whose unique exception belongs to B. Thus F has no S–T edge.

For i in S, let w_i be the supplement of bi. These w_i are distinct. For each F-edge ij within S, the selected edge bj must dominate w_i, since its exception w_j is different. Since bw_i is absent, jw_i is an edge. It is residual: j and w_i both miss the A-vertex i, so jw_i cannot be one of the selected representatives of a missing B–B pair, because every selected edge has its unique exception in B and therefore must dominate every A-vertex. Similarly iw_j is residual. All 2e(F[S]) such edges are distinct, determined by their A-endpoints and distinct supplement labels.

For each F-edge uw within T, the pair misses b, so a quasi-edge uz→w or wz→u exists. Its auxiliary z must dominate b. It cannot be v or b; if in A it would be in S, but every S–T pair is a C-edge, contradicting its failure to dominate the exception in T. Thus z lies in B. The quasi-edge is residual, since its exception belongs to A. Distinct F-edges give distinct cross-edges, their A-endpoint and unique exception identifying the missing F-edge. These e(F[T]) edges have A-endpoints in T and are disjoint from the first family.

Therefore

\[
r\ge2e(F[S])+e(F[T])=e(F)+e(F[S])\ge r+t.
\]

All six rows above have t>0, a contradiction. Consequently every B-vertex has ρ_b≥1, so **r≥b**. This proof also covers S empty and assumes no diameter bound on H.

## 6. Small and large k, and Δ(G)=16

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

For Δ=16 and e=157, Section 5 gives r≥16 while the ledger gives r≤15, impossible. For Δ=16 and e=156 it forces r=16 and e(C)=0; now k=0 and (6.3) gives 16≤16-21=-5, again impossible.

For Δ=15, (6.3) and (6.4) exclude k=0,1 at both edge counts. Equation (6.1) excludes k≥4. Remaining bands are k=2 with r=15,...,20 and k=3 with r=15 at 157 edges; and k=2 with r=15,...,21 and k=3 with r=15,16 at 156 edges.

For Δ=14 at 157 edges the same inequalities exclude k=0,1 and k≥6, leaving k=2,...,5 with 14≤r≤42-5k, exactly the attachment's domain. At 156 edges they exclude k=0 and k≥6, leaving **k=1,...,5 with 14≤r≤43-5k**. In particular the k=1 equality case must be scanned; the old k=1 contradiction would only give 14≤14 and must not be reused.

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

For Δ=15 this bound alone eliminates every remaining numerical state: 108 states at 157 edges and 211 at 156 edges. Both separately implemented enumerators give the same complete state sets and per-band counts. No old Delta=15 exceptional-column hand argument is needed for this new route.

## 8. Exhaustive finite relaxation for Δ(G)=14

Enumerate every nondecreasing A-degree list d of length a, with entries between zero and D=a-1-k, maximum exactly D, and sum 2(r+t). Independently enumerate every nondecreasing positive B-residual list ρ of length b, entries at most a and sum r. Sorting is justified by independent relabelling of A and B. Nongraphical degree lists are retained; this is a necessary-condition relaxation, not a graph catalogue.

First apply (7.2). Next, for each B-source b and trial q from 1 through a-ρ_b, allow labels satisfying d_i≤ρ_b+q-1. Its q selected labels must match distinct supplements w≠b satisfying d_i≤ρ_b+ρ_w. Let c_b be the largest possible q in this relaxed matching problem, including q=0. Then q_b≤c_b, and sum c_b must reach r+2t. The primary verifier uses the q easiest labels and strongest suppliers; the second uses augmenting-path maximum matching with separate copies for repeated values. Both are safe upper bounds on the same requirement.

For each S_j, apply the matching bound again, using label eligibility d_i≤ρ_b+c_b-1. At most c_b such labels can be selected at source b. The sum of these source upper bounds must reach ℓ_j. All supplier identities within each matching are distinct, although consistency between different sources is deliberately relaxed.

Set

\[
h_ρ=\max\{j:|\{b:ρ_b\ge j\}|\ge j\}.
\]

If i has R_i residual incidences, it needs at least d_i-R_i selected incidences whenever this is positive. Their distinct B-sources each have residual degree at least d_i-R_i by (7.1). Hence R_i≥max(0,d_i-h_ρ). Reject if these lower bounds sum to more than r. Otherwise enumerate **all labelled** integer column vectors R satisfying those lower bounds, R_i≤b and sum R_i=r. Positions with equal d_i are not identified.

For fixed R, repeat the source-capacity calculation, additionally requiring d_i≤ρ_b+R_i. The selected total now has the lower bound

\[
Q_{\min}(R)=\sum_i\max(0,d_i-R_i).
\]

One further necessary refinement is used. If b selects q labels, the supplement of any selected label is adjacent to the other q-1 labels: each of those other selected edges must dominate that supplement. Thus b needs q distinct supplements with d_A(w)≥q-1. Since d_A(w)≤ρ_w+c_w, reduce c_b to the largest q≤c_b having at least q distinct w≠b with ρ_w+c_w≥q-1. Use the previous bounds for all sources simultaneously. The refined sum must still reach Q_min(R).

At 157 edges, these tests already eliminate all 59,264 outer states in 46 bands and all 1,480 labelled columns reached. These are the attachment's unchanged computations, fully reproduced in the preceding document review. Its two final patterns also have the hand contradiction printed in the attachment. The reconstructed source and fresh evidence are preserved with this package.

At 156 edges, the same general tests are applied to k=1,...,5 with the changed ledger and surplus. Their separately enumerated outputs, state-set hashes, band counts and every labelled-column capacity are compared. Surviving numerical columns are passed to the following additional necessary test. They are never interpreted as actual graphs.

## 9. New subset-capacity test for the equality columns

Fix a labelled R and any already justified upper bounds c_b on q_b, such as the refined bounds above. For a nonempty subset S of A define

\[
E_b(S)=\{i\in S:d_i\leρ_b+c_b-1\text{ and }d_i\leρ_b+R_i\}.
\]

The number of selected incidences with A-endpoint in S is at least

\[
\sum_{i\in S}\max(0,d_i-R_i).
\]

At source b, every selected label in S belongs to E_b(S), by the closure and column bounds (7.1) and q_b≤c_b. There is at most one selected edge to each label, and at most c_b in total. Consequently every real configuration satisfies

\[
\boxed{\quad
\sum_{i\in S}\max(0,d_i-R_i)
\le \sum_b\min\bigl(c_b,|E_b(S)|\bigr).
\quad} \tag{9.1}
\]

The program column_hall.py enumerates the 1,023 nonempty subsets of the ten A-labels and records the first strict violation for each surviving column. Each certificate contains the original outer-state key, labelled R, prior source caps, subset, selected demand and every source's upper bound. The separate check_column_certificates.py imports neither the search nor either scanner; it checks input identity, exact coverage of all previously surviving columns, the provenance of the caps, and every strict integer inequality. The prior caps themselves were compared against the second arithmetic implementation.

For k=2,...,5 at 156 edges, the first-stage scan has 82,452 outer states, 188,520 labelled column vectors, and 28 surviving outer states containing 171 labelled columns. All 171 violate (9.1), and the separate certificate check confirms complete coverage. The k=1 boundary has 401,543 outer states and 3,252,212 labelled columns. Its 130 surviving outer states contain 1,788 surviving labelled columns; all 1,788 also violate (9.1). A separate comparison confirms every state key, band disposition and column capacity against the second implementation, and the separate certificate checker verifies all 1,788 inequalities and complete coverage. Thus the entire k=1,...,5 equality domain is excluded.

## 10. Assembly, attainment and review obligations

The Fan-free upper-range reduction above excludes every edge count `m>=158`, while the dense-case analysis in this manuscript excludes `m=157`. The degree-sum bound covers Δ≤12; Section 3 covers Δ=13; the original reviewed finite argument covers Δ=14; Sections 4–7 cover Δ=15,16; and the published complement maximum-degree input covers Δ≥17. The bipartite and star cases were settled before taking complements. Thus these candidate deductions imply e(G)≤156 for every 25-vertex diameter-2-critical graph.

The analogous equality exclusions use the same degree partition: Section 3 yields K_{12,13} for Δ=13; Sections 4–7 exclude Δ=15,16 at 156 edges; and the complete k=1,...,5 scan and the certificates in Section 9 and RESULTS.md exclude Δ=14. Equality is therefore restricted to K_{12,13}. This graph has diameter two, and deleting any cross edge makes its endpoints have distance three, so it attains the bound and is critical.

The argument's graph-theoretic premises and necessary directions were read and rederived internally. Two implementations agreeing is computational corroboration, not independent mathematical authorship. External mathematical scrutiny should concentrate on the witness classification in Section 3, the residual injections in Sections 5–6, the generalized parameter domain and the source-capacity arguments in Sections 7–9. No graph catalogue, SAT encoding, DRAT/LRAT certificate, floating-point optimization, or old residual-component lemma is a dependency of this route. No novelty or priority claim is made.
