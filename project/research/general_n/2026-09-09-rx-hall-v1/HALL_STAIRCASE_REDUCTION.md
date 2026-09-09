# Hall neighbourhood closure and staircase reduction

9 September 2026. Research note inside the stripped selected/residual transport framework.

## Lemma 1: neighbourhood closure

Let the projected Hall compatibility graph have label-state side \(L\) and source-state side \(S\). For \(U\subseteq L\), define

\[
N(U)=\bigcup_{v\in U}N(v)
\]

and the neighbourhood closure

\[
\operatorname{cl}(U)=\{v\in L:N(v)\subseteq N(U)\}.
\]

Then

\[
N(\operatorname{cl}(U))=N(U).
\]

Consequently the Hall right-hand side is unchanged while the nonnegative label-demand left-hand side can only increase:

\[
\sum_{v\in U}d_v
\le
\sum_{v\in\operatorname{cl}(U)}d_v.
\]

Thus it is enough to test neighbourhood-closed Hall sets. Any violated Hall inequality has a violated closed representative.

## Lemma 2: only a frontier determines the neighbourhood

For any finite \(U\), remove every label state \(v\) for which another state \(w\in U\) satisfies

\[
N(v)\subseteq N(w).
\]

The union neighbourhood \(N(U)\) is unchanged. Hence every Hall set is represented by the antichain of its inclusion-maximal label neighbourhoods.

## Threshold geometry

In the stripped full compatibility model a source state \(u=(\rho,q,p)\) is adjacent to a label state \(v=(s,R,x)\) when

\[
s\le\rho,
\qquad d:=R+s\le \alpha:=\rho+q-1,
\qquad h:=R+x\ge \beta:=q+p.
\]

If the first condition is temporarily omitted, as in the `BC` ablation, compatibility is the two-dimensional dominance relation

\[
d\le\alpha,\qquad h\ge\beta.
\]

Therefore

\[
d_1\ge d_2\ \hbox{and}\ h_1\le h_2
\quad\Longrightarrow\quad
N(v_1)\subseteq N(v_2).
\]

The inclusion-maximal neighbourhoods of a closed Hall set are consequently a monotone staircase / Pareto antichain in the \((d,h)\)-plane. Restoring \(s\le\rho\) adds one monotone coordinate, so the full `ABC` frontier is an antichain in the hardness coordinates

\[
(s,d,-h).
\]

## n=30 evidence

The exact compatibility ablation checkpoint `N30_RZ_COMPAT_ABLATION_RUN_34344452015.json` shows:

- `BC` rejects 6 of the 7 residual-budget hard states exactly;
- `ABC` rejects all 7 exactly;
- deleting C (`AB`) rejects none;
- deleting B (`AC`) rejects only 2.

The Z-free Hall cut-generation v2 run closes all seven exactly. Post-processing its proof-active Hall cuts shows that the inclusion-maximal-neighbourhood frontier of an active cut is typically 4--6 label states; across the seven exact contradictions the observed maximum frontier size is 10. This is empirical structure of the current finite proof, not yet a universal frontier-size bound.

## Research target

The large incidence system has therefore been reduced to the problem of controlling weighted Hall inequalities indexed by small monotone staircases. The next useful questions are:

1. whether bounded-frontier Hall cuts already suffice for the n=30 seven-state contradiction;
2. whether the weighted sum of staircase cuts in the exact Farkas certificates collapses to a single layer-sum / majorization inequality;
3. whether the exceptional state requiring condition A can be handled by a separate one-dimensional \(s\le\rho\) correction.

This note is a combinatorial projection/reduction inside the candidate framework. It does not by itself prove the unrestricted Murty--Simon conjecture.
