# Murty–Simon at n=29: candidate proof with complete finite Delta=16 arithmetic

8 September 2026. Research directed by Paul Lenz; mathematical development, implementation and internal checking by ChatGPT/Geeps.

**Status: candidate proof. The fixed-order arithmetic described below has been reproduced internally; independent mathematical review, external computational reproduction and novelty assessment remain OPEN. The graph-theoretic lemmas are not fully formalised.**

## 1. Statement

Let G be a finite simple diameter-two edge-critical graph on 29 vertices. The candidate statement is

\[
e(G)\le 210=\left\lfloor\frac{29^2}{4}\right\rfloor,
\]

with equality if and only if

\[
G\cong K_{14,15}.
\]

Deleting an edge is understood to increase the diameter, with disconnected pairs assigned infinite distance.

The proof does **not** use the later general `293/500` candidate theorem. It uses the same published reductions and residual/quasi-edge lemmas already isolated in the n=27/n=28 programme, one new fixed-order Delta=16 calculation, and a short witness argument for Delta=15.

## 2. Published reductions and the two edge counts

Fan's strict bound, in the form reported by Tao Wang,

\[
e(G)<\frac{n^2}{4}+\frac{n^2-(81/5)n+56}{320},
\]

has value

\[
\frac{42317}{200}=211.585
\]

at n=29. Thus a counterexample to the desired upper bound has exactly 211 edges. Equality at 210 edges must be treated separately; we never delete an edge and assume edge-criticality is preserved.

A bipartite graph of diameter two is complete bipartite, because a missing cross-part pair has odd distance at least three. Hence a bipartite graph on 29 vertices has at most 14*15=210 edges, with equality only K(14,15).

Assume henceforth that G is non-bipartite. The published dominating-edge result of Dailly, Foucaud and Hansberg gives at most floor(29^2/4)-2=208 edges for a non-bipartite diameter-two-critical graph with a dominating edge; its exceptional graph has order six. Consequently neither dense edge count has a dominating edge.

A universal vertex forces an edge-critical graph to be a star: any edge among the remaining vertices could be removed while every pair stayed at distance at most two. The star case is therefore sparse and is handled separately below.

If Delta<=14, the degree sum gives

\[
2e(G)\le 29\cdot14=406,
\]

so e(G)<=203. Thus only Delta>=15 can occur at 210 or 211 edges.

## 3. Witness lemma and the complete Delta=15 argument

A **direct witness** is an edge uv whose endpoints have no common neighbour. A **two-step witness** is a nonedge uv whose endpoints have exactly one common neighbour.

Every critical edge is covered by one of these witnesses. Indeed, delete a critical edge xy and choose a pair u,v whose distance becomes greater than two. In G their distance is at most two and every path of length at most two must use xy. If u,v are adjacent, their edge is xy and they have no common neighbour, giving a direct witness. If u,v are nonadjacent, their unique length-two path uses xy; a second common neighbour would give another length-two path after xy were deleted. Thus uv is a two-step witness. A direct witness covers its own edge; a two-step witness can cover at most the two edges of its unique length-two path.

Because there is no dominating edge, every witness pair uv satisfies

\[
d(u)+d(v)\le28. \tag{3.1}
\]

For a two-step witness, N(u) and N(v) lie among the other 27 vertices and have intersection one, so the degree sum is at most 27+1=28. For a direct witness, the neighbourhoods are disjoint; if their union were all 29 vertices, uv would be a dominating edge.

Now suppose Delta=15 and put

\[
\varepsilon_x=15-d(x),\qquad
L=\{x:\varepsilon_x\ge2\},\qquad
O=\{x:\varepsilon_x=1\}.
\]

Write h=|L| and o=|O|. By (3.1), every witness pair has deficit sum at least two. A witness entirely outside L must therefore have both endpoints in O. If

\[
T=29\cdot15-2e(G),
\]

then

\[
2h+o\le T. \tag{3.2}
\]

Let X=V(G)\setminus L. Count the edges having an endpoint in L directly, and cover the remaining X-X edges by witnesses. A witness with both endpoints in L covers no X-X edge. A missing cross pair between L and X covers at most one X-X edge. A witness within O covers at most two. If e(L,X) is the number of actual cross edges, the number of missing cross pairs is h(29-h)-e(L,X). Hence

\[
\begin{aligned}
e(G)
&\le \binom h2+e(L,X)
 +\bigl(h(29-h)-e(L,X)\bigr)+2\binom o2\\
&=\binom h2+h(29-h)+o(o-1). \tag{3.3}
\end{aligned}
\]

No injective assignment of witness pairs to edges is assumed: each edge is assigned one witness, while the displayed capacities are upper bounds on how many edges any witness type can cover.

### 3.1 Excluding 211 edges at Delta=15

At e(G)=211, T=13. For each integer h=0,...,6, (3.2) gives o<=13-2h. The right side of (3.3) is increasing in o>=1, so the largest possible bounds are

| h | o max | upper bound |
|---:|---:|---:|
| 0 | 13 | 156 |
| 1 | 11 | 138 |
| 2 | 9 | 127 |
| 3 | 7 | 123 |
| 4 | 5 | 126 |
| 5 | 3 | 136 |
| 6 | 1 | 153 |

Every value is below 211. Thus Delta=15 is impossible at 211 edges.

### 3.2 Equality at 210 edges and K(14,15)

At e(G)=210, T=15. The analogous table is

| h | o max | upper bound |
|---:|---:|---:|
| 0 | 15 | 210 |
| 1 | 13 | 184 |
| 2 | 11 | 165 |
| 3 | 9 | 153 |
| 4 | 7 | 148 |
| 5 | 5 | 150 |
| 6 | 3 | 159 |
| 7 | 1 | 175 |

Equality therefore forces h=0 and o=15. All witnesses lie inside O. We can now distinguish actual O-edges from O-nonedges: a direct witness edge covers one edge, while a two-step witness nonedge covers at most two. Consequently

\[
210\le e(G[O])+2\left(\binom{15}{2}-e(G[O])\right)
=210-e(G[O]).
\]

Thus O is independent. Its 15 vertices each have degree 14, and there are exactly 14 vertices outside O. Every vertex of O is therefore adjacent to every vertex outside O. Those 15*14=210 cross edges exhaust E(G). Hence

\[
G=K_{15,14}.
\]

Conversely K(14,15) is diameter-two edge-critical: after deleting a cross edge uv, its endpoints have no path of length two (the graph is bipartite) and do have a length-three path because both parts have size at least two. Thus the diameter increases to three.

This settles Delta=15 completely, without enumeration.

## 4. Complement residual setup for Delta=16

It remains to exclude Delta=16 at both 211 and 210 edges. Put H=complement(G), choose a minimum-degree vertex v of H, and set

\[
A=N_H(v),\qquad B=V(H)\setminus N_H[v].
\]

Then

\[
|A|=a=29-1-16=12,\qquad |B|=b=16.
\]

Let C=H[A], F=complement(C) on A, and d_i=d_F(i). For each missing unordered pair uw in H[B], edge-criticality of G implies that H+uw contains a new adjacent total-dominating pair. Because u,w both miss v, that pair is not {u,w}; after interchanging endpoints it is an existing cross edge ui whose open H-neighbourhoods cover every vertex except w. Write ui->w. Choose one such cross edge for every missing B-pair. Different missing pairs select different cross edges because the B-source and unique exception recover the pair. All other H[A,B] edges are residual.

Let rho_u and R_i be residual row/column degrees, q_u and p_u outgoing/incoming selected-pair degrees, and x_i the actual selected degree of label i. Put

\[
r=\sum_u\rho_u=\sum_iR_i,
\quad s_i=\max(0,d_i-R_i),
\quad S=\sum_i s_i,
\quad t=e(G)-b(29-b).
\]

For the two scopes

\[
(m,t)=(211,3)\quad\hbox{and}\quad(210,2).
\]

Counting H gives

\[
e(F)=r+t,\qquad \sum_i d_i=2(r+t),\qquad S\ge r+2t. \tag{4.1}
\]

Because t>0, the residual-activity lemma applies: every B-source has rho_u>=1. The selected-edge injection gives

\[
d_i\le\rho_u+R_i,\qquad d_i\le\rho_u+\rho_w,
\qquad \rho_w+q_w\ge q_u-1, \tag{4.2}
\]

whenever ui->w is selected. The actual selected neighbourhood also gives

\[
R_i+x_i\ge q_u+p_u. \tag{4.3}
\]

The source and supplement capacities are

\[
q_u+\rho_u\le a,
\qquad p_u\le\rho_u+(b-a-1)=\rho_u+3,
\qquad q_u+p_u\le b-1. \tag{4.4}
\]

These are the same graph lemmas used by the order-28 direct197 route, with b=16 and the displayed t supplied explicitly. The adapted programs infer a and b from the current demand/row lengths and do not retain a hard-coded b=15 assumption in the joint/LP stages.

The inherited charging inequality yields the necessary demand condition

\[
\sum_{i=1}^{12}\frac{s_i(13-2s_i)}{12-s_i}\ge16+2t. \tag{4.5}
\]

The finite calculation deliberately over-enumerates arithmetic systems satisfying these necessary conditions; a numerical survivor is never treated as a graph.

## 5. Complete Delta=16 finite calculation

The adaptation starts from the hash-pinned n=28 direct197 source archive. Only the fixed scope changes to a=12,b=16 and t in {3,2}. The demand generator independently checks its complete integer domain. Two separately compiled C++ residual-row implementations produce byte-identical survivor and band files. The projected pair screen is regenerated from the current t. The joint-column propagation is run twice: the discovery implementation and a separately compiled/set-valued checker agree on every surviving state. Final infeasibility is accepted only when an integer Farkas certificate is verified against a separately reconstructed named linear system.

A floating-point solver is used only to *propose* certificates. Solver status alone is never an exclusion. Every accepted certificate has nonnegative integer multipliers on inequalities and signed integer multipliers on equalities, and the checker verifies coefficientwise nonnegativity together with a strictly negative right-hand side.

### 5.1 The 211-edge scope: t=3

| Stage | Input / retained |
|---|---:|
| Complete demand tuples | 4,867 |
| Demand tuples retained | 339 |
| Residual rows enumerated | 1,848,957 |
| Residual row survivors | 206 |
| Projected survivors | 118 |
| Joint-column survivors | 36 |
| Shared-adjacency exact contradictions | 13 |
| Source-degree-typed exact contradictions | 23 |
| Endpoint-type contradictions needed | 0 |
| **Final survivors** | **0** |

The residual row implementations agree on all 1,848,957 rows. The projected stage excludes 47 zero-slack rows and 41 pair-threshold rows. The joint stage excludes 38 by source matching, two by source Hall, and 42 by joint total-source capacity, leaving 36. All 36 then have exact Farkas contradictions.

### 5.2 The 210-edge scope: t=2

| Stage | Input / retained |
|---|---:|
| Complete demand tuples | 9,251 |
| Demand tuples retained | 901 |
| Residual rows enumerated | 5,765,218 |
| Residual row survivors | 2,087 |
| Projected survivors | 1,225 |
| Joint-column survivors | 593 |
| Shared-adjacency exact contradictions | 213 |
| Source-degree-typed exact contradictions | 378 |
| Actual-endpoint-type exact contradictions | 2 |
| **Final survivors** | **0** |

The residual implementations agree on all 5,765,218 rows. The projected stage excludes 734 zero-slack rows and 128 pair-threshold rows. The independent joint checks agree on all 1,225 inputs and leave 593. Their exclusions are 311 source-matching, 29 source-Hall, six empty label domains, 58 total-source, 222 joint-total-source, and six pair-Hall contradictions. The exact LP stages reject all 593 remaining rows, including the last two only after the actual endpoint-degree model.

Thus Delta=16 is impossible at both 211 and 210 edges.

## 6. Delta=17 by the pointwise charging bound

For Delta=17 we have a=11. The same charging inequality requires

\[
17+2t\le\sum_{i=1}^{11}\frac{s_i(12-2s_i)}{11-s_i}.
\]

For every integer 0<=s<=10,

\[
\frac{s(12-2s)}{11-s}\le\frac{16}{7}.
\]

Indeed

\[
\frac{16}{7}-\frac{s(12-2s)}{11-s}
=\frac{2(s-4)(7s-22)}{7(11-s)}\ge0
\]

at every integer s=0,...,10. Hence the right side is at most

\[
11\cdot\frac{16}{7}=\frac{176}{7}<29.
\]

At 210 edges, t=210-17*12=6 and the required left side is 29. At 211 edges, t=7 and it is 31. Both are impossible.

## 7. Delta from 18 through 27 by residual h-index

Let h be the largest integer for which at least h residual rows have degree at least h. The source-demand injection implies s_i<=h for every label: a label demanding s_i selected sources requires s_i distinct sources with residual degree at least s_i.

Since t>0, every B-row is residual-active. Therefore

\[
r\ge h^2+(b-h)=b+h(h-1).
\]

On the other hand S<=ah and S>=r+2t. Consequently

\[
b+2t\le(a+1)h-h^2
\le\left\lfloor\frac{(a+1)^2}{4}\right\rfloor
=\left\lfloor\frac{(29-b)^2}{4}\right\rfloor. \tag{7.1}
\]

For m=210 and b=18,...,27 the left/right pairs begin with 42>30 and then become still more separated. For m=211 they begin with 44>30. The complete exact table is reproduced by the supplied arithmetic checker. Thus no b in 18,...,27 is possible at either dense edge count.

For Delta=28, the universal-vertex argument gives a star, which has only 28 edges.

## 8. Assembly

Fan's strict bound leaves only m<=211.

At m=211:

- Delta<=14 is impossible by degree sum;
- Delta=15 is excluded by the witness count in Section 3;
- Delta=16 is excluded by the complete direct calculation in Section 5;
- Delta=17 is excluded by Section 6;
- 18<=Delta<=27 is excluded by Section 7;
- Delta=28 gives a star.

Therefore e(G)<=210.

Suppose e(G)=210. Bipartite graphs already give equality only at K(14,15). In the non-bipartite case the same degree partition applies. Delta<=14, Delta=16, Delta=17, Delta>=18 and the star case are all excluded. Thus Delta=15, and Section 3.2 forces G=K(14,15), contradicting the assumption that it was non-bipartite. Hence globally equality occurs exactly for K(14,15).

This proves the stated **candidate** order-29 result, subject to the explicit external and universal-lemma review obligations below.

## 9. Audit boundaries and provenance

The Delta=16 source is an adaptation of `project/research/general_n/2026-09-07-direct-197-v8/MurtySimon_N28_197_Direct_v8.zip`, SHA-256 `b753076ffc755066a0c57756be91cc5b265c163d869244d3aa65e3943799347b`. The first hosted n=29 replay attempts exposed environment/setup issues (missing SciPy, then isolated Python hiding a user-site install, then missing Boost headers). Those failures are preserved as failed executions and are not mathematical counterexamples. The fourth hosted run, GitHub Actions run `34220977858` at commit `42954d3094860a218e6ba8a418c35b7061449b31`, completed successfully on Ubuntu 24.04 after pinning SciPy 1.17.0 in an isolated virtual environment and installing Boost headers. Its aggregate output is reproduced verbatim in the review package. The three earlier failed executions are retained as environment/setup failures rather than rewritten as mathematical runs.

The fixed-order arithmetic is exhaustive over its stated numerical relaxation, not over all labelled graphs. Actual-graph regressions elsewhere in the project contain no positive-surplus critical graph, so the universal graph-to-model implication rests on the written lemmas rather than empirical sampling. The solver-assisted discovery and exact checking implementations were written by the same assistant; clean-runner execution is not independent authorship or peer review.

Fan's and Dailly–Foucaud–Hansberg's published theorems are external inputs and are not re-proved here. The quasi-edge, residual-injection, activity, charging and h-index arguments are internal hand proofs with separate earlier audits and limited local formalisation, not a full Lean proof of this order-29 theorem.

No order above 29, unrestricted all-order Murty–Simon solution, novelty determination, priority claim or external endorsement is asserted by this manuscript.

## References

[1] Tao Wang, *On Murty-Simon Conjecture*, arXiv:1205.4397 (2012), especially page 2 for the strict Fan bound as reported there. https://arxiv.org/pdf/1205.4397

[2] Antoine Dailly, Florent Foucaud and Adriana Hansberg, *Strengthening the Murty-Simon conjecture on diameter 2 critical graphs*, arXiv:1812.08420 (2018), Theorem 4 for the non-bipartite dominating-edge bound. https://arxiv.org/pdf/1812.08420

[3] Project direct197-v8 proof and exact source package: `project/research/general_n/2026-09-07-direct-197-v8/`. The n=29 Delta=16 calculation uses its hash-pinned source archive as an implementation antecedent but generates fresh n=29 domains.

[4] Project n=27 candidate proof: `project/reviews/n27/2026-09-07-candidate-v1/PROOF.md`, for the earlier full written derivations of the residual-activity and h-index framework. The relevant arguments are restated above at the level needed for n=29.
