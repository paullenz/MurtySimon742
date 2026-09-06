# Erdős Problem #742 at n=25: elimination of the Δ(G)=14, k=0 branch

Date: 6 September 2026

## Status

This note records a short project-level hand elimination of the local branch

\[
\Delta(G)=14,\qquad k=\delta(C)=0,
\]

within the existing audited complement/quasi-edge framework. It uses the exact ledger, Haynes–Henning–van der Merwe–Yeo Claims A and B, and the already audited residual-component lemma. It does not by itself re-audit those imported lemmas or constitute independent peer review.

## Setup

Let H be the complement of a hypothetical 25-vertex, 157-edge diameter-2-critical counterexample with \(\Delta(G)=14\). Then \(\delta(H)=10\). Choose \(v\in V(H)\) with \(d_H(v)=10\), put

\[
A=N_H(v),\quad |A|=10,\qquad B=V(H)\setminus N_H[v],\quad |B|=14.
\]

Let \(C=H[A]\), let \(F=\overline C\) on A, and let r be the number of residual A-B edges after the Claim-A quasi-clique assignment on B. The exact ledger is

\[
e(C)+r=42,\qquad e(F)=r+3.
\]

Assume \(k=\delta(C)=0\), and choose \(x\in A\) isolated in C. Put \(X=A\setminus\{x\}\), so \(|X|=9\).

## Lemma 1: Claim B leaves exactly six residual edges outside its family

Since x is isolated in C,

\[
e(C)=e(C[X]).
\]

Hence the number of missing C-edges inside X is

\[
\binom 92-e(C[X])=36-(42-r)=r-6.
\]

Thus \(r\ge6\). By Claim B, every missing edge \(uw\) of C[X] has a distinct associated quasi-edge \(uz\to w\), with \(z\in B\). Exactly as in the audited \(\Delta=15,k=0\) argument, such a Claim-B edge cannot also be a Claim-A edge for the B quasi-clique: its unique undominated vertex lies in X, whereas a Claim-A edge has its unique undominated vertex in B. Consequently all \(r-6\) Claim-B quasi-edges are residual A-B edges.

Let P be this set of \(r-6\) residual edges, and let Z be the set of their B-endpoints. For \(z\in Z\), take one Claim-B relation \(uz\to w\). Since x is nonadjacent in H to u and \(x\ne w\), domination by \(\{u,z\}\) forces \(xz\in E(H)\). Moreover xz cannot be selected for Claim A. If it were, the selected pair \(\{x,z\}\) would dominate every A-vertex; because x has no C-neighbour in X, z would have to be adjacent to every vertex of X. But \(uz\to w\) requires z to miss w. Therefore xz is residual.

The xz edges are outside P and are distinct for distinct z. Since P already contains \(r-6\) of the total r residual cross-edges, there are exactly six residual cross-edges outside P.

## Lemma 2: at most six B-vertices are residual-active

Call \(b\in B\) residual-active if it is incident with a residual A-B edge. Let R be the set of residual-active B-vertices.

If \(b\in Z\), then xb is a residual edge outside P by Lemma 1. If \(b\notin Z\) is residual-active, its residual edge cannot belong to P, since all B-endpoints of P lie in Z; hence b is again the B-endpoint of a residual edge outside P. Therefore every vertex of R occurs as the B-endpoint of one of the six residual edges outside P. Each such cross-edge has only one B-endpoint, so

\[
|R|\le6. \tag{1}
\]

In particular at least eight vertices of B are residual-inactive.

## Lemma 3: every residual-inactive B-vertex is A-complete

Because x is isolated in C, x is adjacent in F to every vertex of X. Hence F is connected.

The audited residual-component lemma says that if \(b\in B\) is residual-inactive, then \(N_A(b)\) is a union of components of F. Since F is connected, \(N_A(b)\) is either empty or all of A. But every B-vertex has an A-neighbour (distance two from v in H), so

\[
N_A(b)=A.
\]

Thus every residual-inactive b is A-complete. Equivalently, every non-A-complete B-vertex is residual-active.

## Contradiction

By (1), B contains a residual-inactive vertex b. By Lemma 3, b is A-complete. Since b has no residual A-B edge, all ten edges ba, \(a\in A\), are selected Claim-A quasi-edges.

The Claim-A bijection assigns these ten distinct selected cross-edges to ten distinct missing B-pairs \(bw_a\). For the assignment using ba, its supplement \(w_a\) is nonadjacent to a. Therefore each \(w_a\) is non-A-complete, and by Lemma 3 each \(w_a\) is residual-active. The ten supplements are distinct, so

\[
|R|\ge10. \tag{2}
\]

Equations (1) and (2) contradict each other. Therefore the branch

\[
\boxed{\Delta(G)=14,\quad k=0}
\]

is impossible within the audited project framework.

## Scope of the result

This proof eliminates all possible residual values at once; there is no remaining r-subcase for k=0. The only arithmetic input specific to this branch is the six-slack identity

\[
\#\overline{E(C[X])}=r-6.
\]
