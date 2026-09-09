# Pairwise staircase reduction of the n=30 hard frontier

9 September 2026. Research note inside the candidate selected/residual framework. This records an exact finite reduction of the stripped necessary-condition model; it is **not** an unrestricted Murty–Simon theorem.

## 1. Three compatibility coordinates

The full stripped source-label compatibility order is

\[
(s,d,-h)\le(\rho,\alpha,-\beta),
\]

where

\[
d=R+s,\qquad h=R+x,\qquad \alpha=\rho+q-1,\qquad \beta=q+p.
\]

A genuine full monotone coupling implies stochastic dominance in every coordinate projection. In particular it implies the two pairwise families

\[
(d,-h)\preceq(\alpha,-\beta)
\tag{BC}
\]

and

\[
(s,-h)\preceq(\rho,-\beta).
\tag{SH}
\]

Each family is exactly a two-dimensional upper-set / staircase family.

## 2. BC staircase family

As derived in `BC_STAIRCASE_FORM.md`, for every nondecreasing staircase function `H`,

\[
\sum_{g,R,x:\ R+x\le H(R+s)}n_gxL_{g,R,x}
\le
\sum_{k,q,p:\ q+p\le H(\rho_k+q-1)}n_kqW_{k,q,p}.
\tag{BC-H}
\]

On the seven preserved n=30 equality-frontier residual-budget states, this pairwise family rejects exactly hard positions 1 through 6 and leaves hard position 0.

## 3. SH staircase family

The same finite monotone-coupling argument in the coordinates `(s,-h)` gives, for every nondecreasing staircase function `K`,

\[
\boxed{
\sum_{g,R,x:\ R+x\le K(s_g)} n_gxL_{g,R,x}
\le
\sum_{k,q,p:\ q+p\le K(\rho_k)} n_kqW_{k,q,p}
}
\tag{SH-K}
\]

This is another direct necessary condition of the full source-label compatibility transport. It contains the interaction between the demand coordinate `s` and the lower threshold `h`, without retaining the degree-like coordinate `d`.

## 4. Exact n=30 separation

The exact pairwise ablation tests four models on top of the same W/L master and exact residual/source constraints:

- BC alone: 6/7 exact rejections;
- BC plus `(s,d)` pairwise dominance: still 6/7;
- **BC plus SH: 7/7 exact rejections**;
- BC plus both `(s,d)` and SH: 7/7.

Thus genuine three-dimensional upper-set inequalities are unnecessary for this finite hard frontier. The missing correction to BC is specifically the `s`--`h` interaction, not the `s` marginal by itself and not the `s`--`d` pair.

For the unique BC survivor (hard position 0, demand profile id 2094), the generated BC+SH exact contradiction uses four SH upper-set cuts. Their minimal generator antichains in `(s,-h)` are

\[
\{(2,-2),(3,-6)\},
\]

\[
\{(1,-1),(2,-5),(3,-6)\},
\]

\[
\{(1,-1),(2,-7)\},
\]

and

\[
\{(1,-1),(2,-2),(3,-11)\}.
\]

Their generator sizes are therefore 2, 3, 2 and 3. All four receive nonzero multipliers in one independently checked integer-Farkas contradiction. Subset-minimality is tested separately; nonzero multiplier in one certificate is not by itself a necessity statement.

## 5. Symbolic target

The active structural target can now be stated without `Z`, without full 3D Hall sets, and without exact supplement transport:

1. exact residual/degree-mass identities and source threshold constraints;
2. the two-dimensional BC staircase family (BC-H);
3. the two-dimensional SH staircase family (SH-K).

Equivalently, weighted combinations of these inequalities test increasing potentials of the additive pairwise form

\[
\Phi(s,d,h)=F(d,h)+G(s,h).
\]

The next useful question is whether the exact finite duals point to simple analytic choices of `F` and `G` that yield a parameteric positive-surplus contradiction below the existing `293/500` degree threshold.

## 6. Status boundary

BC+SH sufficiency is currently a finite exact fact for the seven preserved n=30 relaxation states, not a theorem that those two pairwise families replace full 3D compatibility for all parameter values. Every actual graph image satisfying the full compatibility construction necessarily satisfies BC-H and SH-K, so any contradiction derived from these two families would nevertheless be valid within the candidate graph-to-state framework. The fixed n=29 and n=30 candidate proofs do not depend on this post-hoc reduction.
