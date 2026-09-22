# Unit residual columns, cycle saturation, and the r<=3 closure

22 September 2026. INTERNAL_CANDIDATE; no external verification or novelty
claim. Dependencies: the raw graph bridge and LOW_RESIDUAL_OBSTRUCTION.md.

## 1. Unit-column theorem

**Theorem.** If every A-label has residual degree R_i in {0,1} and r>0,
then f=e(F)<=r-1. In particular e(G)<=b(n-b)-1.

The no-(0,1)-edge lemma implies that every nonisolated F-vertex has R_i=1.
Let such a vertex i have F-degree d. At a selected source u at i, the
source-demand injection sends selected F-neighbours of i to distinct residual
edges at i. There is at most one such neighbour, since R_i=1. Consequently
at least d-1 F-neighbours are residual labels at u.

Sum these residual incidences over the x_i distinct selected sources at i.
They are distinct physical cross-edges. Every F-neighbour j has R_j=1, so
the total available residual incidences at those neighbours is exactly d.
Therefore

    x_i(d-1)<=d,  and  x_i>=d-1.

For d>=3, (d-1)^2>d, a contradiction. Hence maximum F-degree is at most two,
all its edges lie on the r positive-residual labels, and f<=r.

Suppose f=r. Every one of those r labels then has degree two, and F is a
disjoint union of cycles plus isolated zero-residual labels. Also t=f-r=0,
so maximum degree applied to e(G)=b(n-b) gives b>=a+1>=r+1.

Let U be the B-sources of all residual edges; |U|<=r. At a degree-two label,
every selected source has at least one residual F-neighbour, by the incidence
argument above. Thus every selected source at a cycle label lies in U.
Every B-vertex outside U is consequently adjacent to every cycle label.
The set B\U is nonempty.

Delete any F-edge ij. Its endpoints and all A-pairs whose old two-path used
ij retain a common neighbour in B\U: the relevant A-vertices are all cycle
labels. Hence the deletion must create a newly distant cross pair (i,u) or
(j,u), u in B. If (i,u) is such a pair, its unique original common neighbour
is j in A. It cannot be selected, because a selected cross-edge has its
unique common neighbour in B. Thus it is a residual edge at i.

Assign one such residual witness to each F-edge. The assignment is injective:
a residual cross pair with a unique common neighbour determines its F-edge.
Since there are f=r edges and r residual pairs, the assignment is bijective.
Orient each F-edge from its witness label to its other endpoint. Every cycle
vertex has exactly one outgoing edge, because it has exactly one residual
edge and every residual edge is used. Each cycle is therefore a directed cycle.

On a directed cycle write prev(i), next(i) for predecessor and successor,
and z_i for the unique residual source at i. The assigned witness implies
z_i is adjacent to next(i) in G and has unique common neighbour next(i) with i.

The earlier selected-source incidence argument gives

    X_i subset {z_prev(i), z_next(i)}.

But z_prev(i) is adjacent to i, so it cannot belong to X_i. Since x_i>=1,
we obtain X_i={z_next(i)} and z_next(i)!=z_i. In particular

    M_prev(i) = {z_prev(i), z_i}.

The selected source z_next(i) at label i must miss its F-neighbour prev(i),
so it lies in M_prev(i). It cannot equal z_prev(i), which is adjacent to i,
and it cannot equal z_i, whose edge to i is residual, not selected. This is
a contradiction. Thus f=r is impossible and f<=r-1.

Repeated residual sources and repeated codes are explicitly permitted in
this proof. The contradiction does not assume all z_i are distinct.

## 2. A two-label support with a unit column

Suppose the residual support is {p,q}, with R_p=k>=1 and R_q=1. Every zero-
residual F-vertex can meet only p, by the no-(0,1)-edge lemma. Thus all
F-edges form a star at p, possibly including pq.

If there is a zero-residual leaf i, then X_i subset Z_p, and X_p subset
M_i=X_i. Since X_p is disjoint from Z_p, X_p is empty. The maximum-degree
inequality gives d_F(p)<=R_p=k, so f<=k=r-1. If there is no such leaf,
f<=1<=r-1. This proves strict product deficit for this whole support family.

## 3. Residual mass at most three

For r=3 the positive-column partitions are (3), (2,1), and (1,1,1).
They are excluded from f>=r by, respectively, the single-column theorem,
Section 2, and the unit-column theorem. The earlier note treats r=1,2.
Consequently

    1<=r<=3  implies  f<=r-1.                         (LR3)

If r=0, positive demand is impossible by the source-demand injection, so the
zero-demand equality theorem applies. Let
D=floor(n^2/4)-b(n-b), epsilon=e(G)-floor(n^2/4).
Any non-bipartite graph with epsilon>=0 must have, under EVERY legal choice,

    r>=4,  S>=4+2D+2epsilon.

Therefore S<=3 satisfies the conjectured edge bound with equality exactly
balanced complete bipartite. A strict counterexample needs S>=6+2D.

## 4. The next bounded core

At r=4, the partitions (4), (3,1), and (1,1,1,1) are already excluded by the
preceding theorems. For (2,1,1), zero-residual vertices can meet only the
degree-two residual label p. If any such leaf occurs, X_p is empty and
d_F(p)<=2; the other two residual labels support at most one further edge,
giving f<=3. If none occurs, F lies on three vertices and again f<=3.
Thus a possible f>=r core at r=4 must have residual partition (2,2).

This is only a necessary residual-profile reduction, not a graph realization
and not a proof that the remaining (2,2) core exists. That case is the exact
next obstruction. The all-order positive-demand strip remains open.
