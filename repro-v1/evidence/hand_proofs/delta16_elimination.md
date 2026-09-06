# Elimination of the Δ(G)=16 branch

**Project:** Erdős Problem #742 / Murty–Simon, n=25  
**Status:** PROJECT-CERTIFIED  
**Source audit:** comprehensive audit through Δ=15, k=3, 5 September 2026

## Setup

Let \(G\) be a hypothetical 25-vertex diameter-2-critical counterexample with \(e(G)=157\), and let \(H=\overline G\). Assume

\[
\Delta(G)=16.
\]

Then \(\delta(H)=8\). Choose \(v\in V(H)\) with \(d_H(v)=8\), put

\[
A=N_H(v),\quad |A|=8,
\qquad
B=V(H)\setminus N_H[v],\quad |B|=16,
\]

and write \(C=H[A]\), \(F=\overline C\) on \(A\). Let \(r\) be the residual \(A\)-\(B\) edge count after the audited quasi-edge assignment. The exact ledger gives

\[
e(C)+r=15.
\]

Let \(k=\delta(C)\). The local quasi-clique lower bound excludes \(k=0,1\). The case \(k=3\) is also impossible: then \(e(C)\ge12\), while the residual-component bound gives \(r\ge\Delta(F)=4\), so \(e(C)+r\ge16\), contradicting the ledger. Hence

\[
k=2,
\qquad
\Delta(F)=5.
\]

Since \(e(F)=\binom82-e(C)=13+r\) and \(\Delta(F)\le r\), handshaking gives

\[
e(F)\le \frac{8r}{2}=4r,
\]

so \(13+r\le4r\) and therefore \(r\ge5\). Also \(k=2\) implies \(e(C)\ge8\), hence \(r\le7\). Thus

\[
r\in\{5,6,7\}.
\]

## Proposition

The \(\Delta(G)=16\) branch is impossible.

## Proof

For \(r=5\) and \(r=6\), the graph \(F\) has respectively 18 and 19 edges and maximum degree at most five. A disconnected graph on eight vertices with maximum degree at most five has at most 17 edges: the extremal split is \(7+1\), and a seven-vertex component with maximum degree five has at most \(\lfloor7\cdot5/2\rfloor=17\) edges. Hence \(F\) is connected in both cases.

For \(r=7\), the ledger gives \(e(C)=8\). Since \(C\) has eight vertices, minimum degree two and eight edges, its degree sum is exactly 16; therefore every vertex has degree two and \(C\) is 2-regular. Consequently \(F\) is 5-regular, in particular connected.

Thus in every admissible case \(F\) is one connected component of order eight, while \(r\le7\).

The audited residual-component lemma says that a residual-inactive vertex \(b\in B\) can meet only \(F\)-components of order at most \(r\). Since the unique component of \(F\) has order eight and \(r\le7\), every residual-inactive \(b\) has no neighbour in \(A\).

At most \(r\le7\) of the sixteen vertices of \(B\) can be residual-active. Hence at least one residual-inactive vertex exists. That vertex has no neighbour in \(A\), contradicting the diameter-two requirement in \(H\).

Therefore no counterexample can have \(\Delta(G)=16\). ∎

## Audit note

The comprehensive audit marks this proof LOCKED. It deliberately uses only the exact edge ledger, the residual-component lemma and connectivity, avoiding the more delicate supplement-count argument used in earlier exploratory work.
