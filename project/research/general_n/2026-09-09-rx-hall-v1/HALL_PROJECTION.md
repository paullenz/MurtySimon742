# Exact Hall projection of the stripped R+Z transport core

9 September 2026. Research note; this is a polyhedral reduction inside the candidate selected/residual framework, **not** an unrestricted Murty–Simon theorem.

## 1. Setting

After deleting the per-demand-group source-capacity inequalities, the remaining `Z` layer is an ordinary fractional bipartite transportation problem.

A source-state node has type

\[
u=(k,q,p),
\]

where source group `k` has residual degree \(\rho_k\), multiplicity \(n_k\), and state density \(W_u\). Its required outgoing incidence mass is

\[
c_u=n_k q W_u.
\]

A label-state node has type

\[
v=(g,R,x),
\]

where demand group `g` has demand \(s_g\), multiplicity \(n_g\), and state density \(L_v\). Its required incoming incidence mass is

\[
d_v=n_g x L_v.
\]

There is a compatibility edge \(u\sim v\) exactly when the retained graph-derived edge conditions hold. In the full stripped model these are

\[
s_g\le \rho_k,
\]

\[
R+s_g\le \rho_k+q-1,
\]

and

\[
R+x\ge q+p.
\]

The original grouped variable \(Z_{uv}\) rescales to ordinary flow

\[
y_{uv}=n_k n_g Z_{uv}.
\]

The source-total equations become

\[
\sum_{v\sim u}y_{uv}=c_u,
\]

and the label-incidence equations become

\[
\sum_{u\sim v}y_{uv}=d_v.
\]

Thus the remaining `Z` variables have no role beyond routing nonnegative mass through this compatibility graph.

## 2. Exact elimination

By the standard max-flow/min-cut theorem, such a nonnegative transportation exists if and only if

\[
\sum_u c_u=\sum_v d_v
\tag{H0}
\]

and, for every set \(U\) of label-state nodes,

\[
\sum_{v\in U}d_v
\le
\sum_{u:\,N(u)\cap U\ne\varnothing}c_u.
\tag{H(U)}
\]

Equivalently, after substituting the grouped state masses,

\[
\sum_{(g,R,x)\in U} n_g x L_{g,R,x}
\le
\sum_{(k,q,p):\,N(k,q,p)\cap U\ne\varnothing}
 n_k q W_{k,q,p}.
\tag{H}
\]

Therefore **all stripped `Z` variables can be projected out exactly** and replaced by the total-mass equality (H0) plus the Hall family (H).

This is an exact equivalence at the relaxation level; it is not an approximation and does not depend on floating-point infeasibility.

## 3. Why this matters

The exact n=30 equality-frontier ablation `N30_RZ_NO_GROUP_CAP_RUN_34344223209.json` removes every per-demand-group source-capacity inequality yet still rejects all seven residual-budget survivors by exact integer Farkas certificates. Hence, on those seven decisive states, the only additional force supplied by `Z` is ordinary compatibility transport and can in principle be expressed entirely through (H0) and (H).

The next task is therefore not to preserve a large incidence LP. It is to exploit the threshold structure of compatibility to compress the Hall family. The three compatibility coordinates are being ablated separately:

- A: \(s\le\rho\);
- B: \(R+s\le\rho+q-1\);
- C: \(R+x\ge q+p\).

If one or two of these coordinates carry essentially all of the n=30 obstruction, the neighbourhoods in (H) may become nested or staircase-shaped, making a small explicit Hall/majorization inequality plausible.

## 4. Status boundary

This note proves only the exact projection statement for the stated fractional transport layer. Universal correctness of the surrounding selected/residual graph model remains governed by the written graph-to-model lemmas. The n=29 and n=30 complete candidate proofs do not depend on this post-hoc generalisation experiment.
