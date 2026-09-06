# Elimination of the Δ(G)=17 branch

**Project:** Erdős Problem #742 / Murty–Simon, n=25  
**Status:** PROJECT-CERTIFIED reduction using a published theorem  
**Source audit:** comprehensive audit of 5 September 2026

## Proposition

There is no 25-vertex diameter-2-critical counterexample with

\[
e(G)=157,\qquad \Delta(G)=17.
\]

## Proof

Let \(H=\overline G\). Since \(G\) has order 25 and 157 edges,

\[
e(H)=\binom{25}{2}-157=300-157=143.
\]

If \(\Delta(G)=17\), then

\[
\delta(H)=24-17=7.
\]

The complement \(H\) is 3-total-domination-critical. Haynes, Henning, van der Merwe and Yeo prove that a 3-total-domination-critical graph of order \(n\) with minimum degree \(\delta\le 0.3n\) has more than

\[
\left\lceil\frac{n(n-2)}4\right\rceil
\]

edges.

Here \(n=25\) and \(\delta(H)=7\le7.5=0.3n\). Therefore

\[
e(H)>\left\lceil\frac{25\cdot23}{4}\right\rceil
=\lceil143.75\rceil
=144.
\]

Because \(e(H)\) is an integer, this gives \(e(H)\ge145\), contradicting \(e(H)=143\).

Hence the \(\Delta(G)=17\) branch is impossible. ∎

## Dependency

T. W. Haynes, M. A. Henning, L. C. van der Merwe and A. Yeo, **“A maximum degree theorem for diameter-2-critical graphs,”** *Open Mathematics* 12(12) (2014), 1882–1889. DOI: 10.2478/s11533-014-0449-3.

## Audit note

The comprehensive project audit records this branch as LOCKED. The proof is a direct integer-boundary application of the published theorem; no computational search is used.
