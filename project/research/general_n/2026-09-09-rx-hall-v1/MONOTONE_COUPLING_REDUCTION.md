# Finite monotone-coupling reduction of the stripped Hall core

9 September 2026. Research note inside the candidate selected/residual framework. This is an exact reduction of the stripped fractional incidence layer; it is **not** an unrestricted Murty–Simon theorem.

## 1. Common product-order coordinates

For a label state `(s,R,x)` define

\[
Y=(s,\ d,\ -h),\qquad d:=R+s,\qquad h:=R+x.
\]

For a source state `(rho,q,p)` define

\[
X=(\rho,\ \alpha,\ -\beta),\qquad
\alpha:=\rho+q-1,\qquad
\beta:=q+p.
\]

The three retained source-label compatibility conditions are exactly

\[
s\le \rho,\qquad d\le\alpha,\qquad h\ge\beta,
\]

or equivalently

\[
Y\le X
\]

coordinatewise.

Let the label-state mass be

\[
\mu(Y)=n_g x L_{g,R,x},
\]

and the source-state capacity mass be

\[
\nu(X)=n_k q W_{k,q,p}.
\]

The total-incidence equality is

\[
\sum_Y\mu(Y)=\sum_X\nu(X).
\tag{M0}
\]

The stripped `Z` layer asks whether this mass can be coupled so that every transported pair satisfies `Y <= X`.

## 2. Finite monotone-coupling lemma

**Lemma.** Assume (M0). A nonnegative transport from label states to source states supported only on pairs `Y <= X` exists if and only if, for every upper set `A` in the coordinatewise product order,

\[
\mu(A)\le\nu(A),
\tag{M(A)}
\]

where `mu(A)` sums label mass at label states in `A` and `nu(A)` sums source capacity mass at source states in `A`.

### Proof

If such a coupling exists and a label state `Y` lies in an upper set `A`, then every source state `X` receiving mass from it satisfies `X >= Y`, hence `X` also lies in `A`. Therefore all label mass in `A` must be absorbed by source capacity in `A`, proving `mu(A) <= nu(A)`.

Conversely, assume (M(A)) for every upper set. For any set `U` of label states, let `up(U)` be its upward closure in the common product order. The compatible source neighbourhood of `U` is exactly

\[
N(U)=\operatorname{up}(U)\cap S,
\]

where `S` is the source-state support. Since `U` is contained in `up(U)`,

\[
\mu(U)
\le \mu(\operatorname{up}(U))
\le \nu(\operatorname{up}(U))
= \nu(N(U)).
\]

Thus every weighted Hall inequality holds. By max-flow/min-cut (equivalently weighted Hall for finite bipartite transport), the required nonnegative transport exists. QED.

This is the finite-poset monotone-coupling / stochastic-dominance formulation of the stripped incidence problem, proved here directly from Hall.

## 3. Relation to the earlier neighbourhood closure

Given any Hall set `U`, replacing it by its ambient upward closure strengthens the label side while leaving its source neighbourhood unchanged:

\[
N(\operatorname{up}(U))=N(U).
\]

Hence a violated Hall cut always yields a violated upper-set inequality. The earlier support-specific closure

\[
\operatorname{cl}(U)=\{v:N(v)\subseteq N(U)\}
\]

can be stronger still when the finite source support has holes, but it is not needed for the exact theoretical characterisation: the complete family of ambient upper-set inequalities is already equivalent to existence of the monotone coupling.

## 4. Staircase geometry

In the dominant `BC` slice, omit the first coordinate `s <= rho`. The order reduces to the two coordinates

\[
(d,-h)\le(\alpha,-\beta),
\]

so every upper set is determined by a monotone staircase in the `(d,h)` plane. Restoring `s <= rho` makes the full problem a three-coordinate upper-set / antichain problem in

\[
(s,d,-h).
\]

Therefore the large incidence LP can be replaced exactly by:

1. the source and label state distributions;
2. exact residual/degree-mass identities and source threshold constraints;
3. the total incidence equality (M0);
4. upper-set stochastic-dominance inequalities (M(A)).

The active research problem is to compress the required upper-set family using the special graph-derived identities, rather than to retain the `Z` variables.

## 5. Status boundary

The reduction above is exact for the stated stripped fractional model. Universal correctness of the surrounding graph-to-state construction remains governed by the written selected/residual lemmas. The completed n=29 and n=30 candidate proofs do not depend on this post-hoc generalisation route.
