# Residual support obstruction and the first positive-demand gap

22 September 2026. INTERNAL_CANDIDATE, awaiting external review.
All statements quantify over every legal selected system at every maximum-
degree root of a finite simple D2C graph. Notation and the raw selected-
residual injection are from the independently reconstructed bridge.

Write f=e(G[A]), r=sum_i R_i, t=f-r=e(G)-b(n-b), X_i for selected B-sources
at label i, and Z_i for residual B-sources there. Thus |Z_i|=R_i and
M_i=X_i disjoint-union Z_i is the set of B-vertices missing i in G.
For every F-edge ij, X_i is a subset of M_j. Moreover, if ui is selected
and uj is also selected, the bridge's distinct-supplement injection produces
a residual edge at label i. Finally |X_i|>=d_F(i)-R_i.

## 1. No residual-(0,1) edge

**Lemma.** Every F-edge ij satisfies R_i+R_j>=2.

If R_i=0, every selected source u at i must have uj residual: if uj were
selected, the injection just recalled would produce a residual at i.
Consequently X_i is a subset of Z_j. Since |X_i|>=d_F(i)>=1, R_j cannot
be zero. Suppose R_j=1, with Z_j={u}. Then X_i={u} and d_F(i)=1.
Also X_j is a subset of M_i=X_i={u}, but uj is residual, so X_j is empty.
The degree bound gives d_F(j)<=R_j=1. Therefore i and j have no other
F-neighbours and have the identical B-neighbour set B\{u}.

The adjacent vertices i,j are true twins. They have at least one common
B-neighbour because b>=2 in a D2C graph of order at least three. Deleting
ij preserves their distance at two, and any other path of length at most
two using ij can be shortened using their identical outside neighbours.
Thus ij is not critical, a contradiction. If both residual degrees are
positive, their sum is already at least two. This proves the lemma.

In particular the positive-residual labels cover every F-edge, and a label
of residual degree one cannot have a zero-residual F-neighbour.

## 2. A single residual label cannot saturate the product bound

**Theorem.** If r>0 and every residual cross-edge has the same A endpoint c,
then f<=r-1. Hence e(G)<=b(n-b)-1.

By the lemma, every F-edge is incident to c: F is a star with k=f leaves,
plus isolated vertices. If k=0 the claim is immediate. Let U=Z_c, |U|=r.
For each leaf i, the proof of the lemma gives the nonempty set

    M_i=X_i subset U.

Also X_c subset M_i subset U; all c-edges from U are residual, so X_c is
empty. Thus M_c=U, and k=d_F(c)<=R_c=r.

Suppose k=r. Then f=r and e(G)=b(n-b). Maximum degree gives
2b(n-b)<=nb, hence b>=n/2 and b>=a+1. Since the star uses r+1 A-vertices,
a>=r+1 and b>=r+2. Thus B\U is nonempty, and all its vertices are common
neighbours of c and every leaf, and of any two leaves.

Consider deleting the F-edge ci. Its endpoints still have a common neighbour
in B\U, and every leaf pair still has one there. The only possible newly
distant pair is (c,u_i), where u_i belongs to U, is adjacent to leaf i but
to no other leaf, and has no B-neighbour in B\U. This follows by enumerating
the two types of two-path using ci: neighbours of i are c and B\M_i;
neighbours of c are its leaves and B\U. The latter B-neighbours are also
neighbours of i, so they produce no newly distant pair on the i side.

Distinct leaves require distinct u_i, because u_i is adjacent to exactly
that one leaf. There are r leaves and r vertices in U, so these witnesses
exhaust U. Consequently

    M_i=U\{u_i},  and  N_G(u_i) intersect (B\U) is empty.

If r=1, M_i is empty, contradicting |X_i|>=d_F(i)=1.
If r>=2, take different leaves i,j. The missing cross-edge u_j i is selected.
Its only possible B-supplement is u_i: u_j has no B-neighbour outside U,
while leaf i meets only u_i inside U. Therefore u_j i -> u_i selects the
unordered B-pair {u_i,u_j}. Similarly u_i j -> u_j selects the same pair a
second time. This contradicts the injectivity of the selected construction.
Thus k=r is impossible, proving f<=r-1.

## 3. Complete r<=2 consequence

If r=1, there is one residual label, so f=0. If r=2, either there is one
residual label (then f<=1 by the theorem), or there are two residual labels,
each of degree one. In the latter case neither can meet a zero-residual
label by Lemma 1; therefore the only possible F-edge joins those two labels,
again giving f<=1.

Hence, for r in {1,2},

    f<=r-1,  t<=-1,  e(G)<=b(n-b)-1.                  (LR2)

For r=0, a positive demand would require a selected source with positive
residual degree, impossible. Thus S=0 and the zero-demand equality theorem
applies. Combining the branches, any graph at or above floor(n^2/4) whose
selected system has r<=2 is balanced complete bipartite and has r=0.

## 4. Demand gap for a hypothetical obstruction

Put D=floor(n^2/4)-b(n-b)>=0 and epsilon=e(G)-floor(n^2/4).
Then t=D+epsilon and S>=r+2D+2epsilon. A non-bipartite graph with epsilon>=0
must therefore satisfy, for every maximum root and every legal selection,

    r>=3,   S>=3+2D+2epsilon.

In particular S<=2 forces the Murty-Simon bound with equality only balanced
complete bipartite. A strict counterexample requires S>=5+2D.

These are structural necessary conditions, not graph existence claims.
They close a bounded-demand branch but do not settle the remaining positive-
demand strip or improve the maximum-degree threshold. The r=2,f=1 pattern
is realized by C5 (below the target density), so LR2 cannot be strengthened
to f=0 at r=2. A separate exact graph regression is required for these new
local conditions; absence of an r=1 fixture alone was not used as proof.
