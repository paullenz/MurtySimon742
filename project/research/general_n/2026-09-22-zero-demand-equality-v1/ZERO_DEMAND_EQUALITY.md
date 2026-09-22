# Zero-demand equality rigidity

22 September 2026. INTERNAL_CANDIDATE; same-project derivation, not external
review. This is an independent proof within the project's own residual route,
not a claim of novelty. Its Boolean orientation is consistent with the earlier
`project/papers/boolean-flow-d2c/MANUSCRIPT.md`, but all facts needed here are
proved below. No external e+disj+X theorem is used.

## Statement

Let G be a finite simple diameter-two-critical graph of order n>=3. Root it at
any maximum-degree vertex v, and choose any legal selected system as in
`../2026-09-22-raw-profile-bridge-v1/RAW_PROFILE_BRIDGE.md`. Let S be its total
positive demand. If S=0, then

    e(G) <= floor(n^2/4),

with equality if and only if G is the balanced complete bipartite graph.
The statement holds for every legal choice and every maximum-degree root.

## 1. Ledger reduction

Write B=N_G(v), A=V(G)\N_G[v], b=|B|, a=|A|, F=G[A], f=e(F),
t=e(G)-b(n-b), and r for residual cross-edge mass. The independently
reconstructed bridge gives f=r+t and S>=r+2t. Therefore S=0 implies
t<=-r/2<=0, proving the edge bound.

If equality holds, b(n-b)<=floor(n^2/4) forces t>=0. Hence t=r=f=0,
b(n-b)=floor(n^2/4), and C=A union {v} is an independent set.

If a=0, the graph is a star: any edge outside v can be deleted without losing
diameter at most two. Among stars of order n>=3, equality occurs only at n=3,
where the graph is K(1,2). Thus assume a>=1.

## 2. Exact Boolean orientation, with repeated codes allowed

For u in B set M_u={i in A: ui is not an edge of G}. Because r=0, every
missing cross-edge is selected. Orient each B-edge u->w according to its
selected quasi-edge ui->w, and give it label i. Thus outdegree(u)=|M_u|,
the outgoing labels are distinct, and each label in M_u occurs once.

For an arc u->w labelled i, the unique common G-neighbour of u and i is w.
In particular i belongs to M_u but not M_w. If j belongs to M_u\{i}, its
selected edge at u has a different supplement. Since uw is a G-edge, the
quasi-edge at label j forces j in M_w. Conversely, if j belongs to M_w,
the selected edge wj cannot have supplement u: the unordered pair {u,w}
has already been assigned to ui. The same quasi-edge property then forces
j in M_u. Consequently

    M_w = M_u \ {i}.                                      (BF)

The orientation is acyclic, since |M| falls by one along every arc. This does
not identify vertices with equal codes: distinct vertices remain distinct.

The degree formula is

    deg_G(u) = a+1-|M_u|+outdegree(u)+indegree(u)
             = a+1+indegree(u).

Maximum degree b therefore gives indegree(u)<=b-a-1=2b-n.

## 3. Even order

For n=2k equality forces b=k, a=k-1. Thus every indegree is zero; there are
no B-edges. Since r=0 also, all C-B edges are present. Hence G=K(k,k).

## 4. Odd order

Let n=2k+1. Equality and the maximum-degree bound force b=k+1 rather than k:
if b=k, then 2e(G)=2k(k+1)>nk, impossible. Thus a=k-1 and b=a+2.
Every directed indegree is at most one.

Suppose a B-edge exists. Follow an oriented path from an edge until it reaches
a sink w. Acyclicity ensures termination. This sink is triangle-active and
M_w is empty, since its outdegree is |M_w|. Thus w is adjacent to every C vertex.

Deleting vw leaves a length-two path between v and w through a B-neighbour
of w. Any newly distant pair must be one of the following:

* (v,i) for i in A whose only B-neighbour was w; or
* (w,z) for a nonadjacent z in B, with unique common neighbour v.

The first option is impossible. F is empty, so i would have degree one.
Diameter two would then make its neighbour w universal, contradicting that
v has maximum degree b<n-1. Hence the second option occurs. Since M_w is
empty, the absence of a common A-neighbour forces M_z=A.

If a>=2, vertex z has a outgoing neighbours, one for each missing label.
Their codes have size a-1. Each has a-1 outgoing neighbours with code size
a-2. These a(a-1) second-level vertices are all distinct, since directed
indegree is at most one; they also differ from z and its first-level
neighbours by code size. Therefore

    b >= 1+a+a(a-1) = a^2+1 > a+2=b,

a contradiction.

If a=1, then b=3. Every nonempty code has size one, each arc goes to an
empty code, and indegree is at most one. The underlying B graph is a
matching, with at most one edge. For its sink w, the required nonadjacent
antipode z with full code must be a source of an edge. There is only one
source, and it is adjacent to w. This too is impossible.

Thus no B-edge exists. All C-B edges are present, giving K(k,k+1).

## 5. Equality controls and exact trust boundary

For balanced K(p,q), a maximum-degree root is in a smaller part. Both F and
G[B] are empty, every C-B edge is present, and S=r=t=0. Deleting any edge
leaves its endpoints at distance greater than two, so these graphs are D2C.
This verifies both parities and K(1,2), without excluding the odd balanced
examples inside the live degree strip.

The proof closes only the zero-demand branch. It neither bounds all positive
demand profiles nor improves the 250/429 degree threshold. Any non-bipartite
graph at or above the conjectured bound must have positive demand for every
legal selection at every maximum-degree root. Actual-graph regression and a
separate hostile replay remain required before relying on this lemma broadly.
