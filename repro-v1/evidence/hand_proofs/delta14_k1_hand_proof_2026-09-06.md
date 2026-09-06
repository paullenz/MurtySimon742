# Erdős Problem #742 at n=25: elimination of the Δ(G)=14, k=1 branch

Date: 6 September 2026

## Status

This note records a short project-level hand elimination of the local branch

\[
\Delta(G)=14,\qquad k=\delta(C)=1,
\]

within the existing audited complement/quasi-edge framework. It uses the exact Δ=14 ledger, Haynes–Henning–van der Merwe–Yeo Claims A and B, and the already audited residual-component and residual-label lemmas.

## Setup

Let H be the complement of a hypothetical 25-vertex, 157-edge diameter-2-critical counterexample with \(\Delta(G)=14\). Then \(\delta(H)=10\). Choose v of degree ten and put

\[
A=N_H(v),\quad |A|=10,\qquad B=V(H)\setminus N_H[v],\quad |B|=14.
\]

Let \(C=H[A]\), let \(F=\overline C\) on A, and let r be the number of residual A-B edges after the Claim-A quasi-clique assignment on B. The exact ledger is

\[
e(C)+r=42,\qquad e(F)=r+3.
\]

Assume \(k=\delta(C)=1\). Choose \(x\in A\) with \(d_C(x)=1\), and write y for its unique C-neighbour. Put

\[
X=A\setminus\{x,y\}=A\setminus N_C[x],\qquad |X|=8,
\]

and define \(s=d_C(y,X)\), \(0\le s\le 8\). Since x has no C-neighbour in X, \(x\cup X\) is a connected 9-vertex subgraph of F. If \(s\le7\), F is connected; if \(s=8\), y is isolated in F and the other nine vertices form the unique nontrivial component.

## Lemma 1

Because \(e(C)=1+s+e(C[X])\), the number M of missing C-edges inside X is

\[
M=\binom82-e(C[X])=r-13+s. \tag{1}
\]

Haynes et al. Claim B makes X a quasi-clique. Let q be the number of its associated quasi-edges whose auxiliary endpoint is y. Then \(q\le s\). The remaining \(M-q\) Claim-B quasi-edges are A-B edges and cannot simultaneously be Claim-A quasi-edges, so they are residual.

For each such relation \(uz\to w\), domination forces xz to be an H-edge, and xz cannot be selected for Claim A; therefore xz is residual. If R is the set of residual-active B-vertices and \(t=|R|\), distinct B-vertices require distinct residual cross-edges outside the Claim-B family. Hence

\[
t\le r-(M-q)=13-s+q\le13. \tag{2}
\]

## Lemma 2: connected case

If \(s\le7\), F is connected. A residual-inactive B-vertex would then have \(N_A(b)=A\), and the audited residual-label lemma would give \(r\ge2e(F)=2(r+3)\), impossible. Thus all fourteen B-vertices are residual-active, so \(t=14\), contradicting (2).

## Lemma 3: disconnected 9+1 case

If \(s=8\), y is isolated and the other nine A-vertices form the unique nontrivial F-component L. Here an internal Claim-B quasi-edge using y is impossible, so q=0 and (2) sharpens to \(t\le5\).

If a residual-inactive B-vertex met L, the residual-label lemma would again give \(r\ge2e(L)=2(r+3)\), impossible. Thus every inactive B-vertex can meet only the singleton \(\{y\}\). In particular every B-neighbour of x is residual-active. Since x has H-neighbours v and y and total H-degree at least ten,

\[
d_B(x)\ge8,
\]

so \(t\ge8\), contradicting \(t\le5\).

## Conclusion

Both possibilities for F are impossible. Therefore, within the current audited quasi-edge framework,

\[
\boxed{\Delta(G)=14,\quad k=\delta(C)=1\text{ is impossible}.}
\]

The proof is uniform in r and requires no fixed-core enumeration or SAT search.

The arithmetic companion `verify_delta14_k1_counts.py` is only a sanity check; it does not independently verify the published Claim B or project residual lemmas.
