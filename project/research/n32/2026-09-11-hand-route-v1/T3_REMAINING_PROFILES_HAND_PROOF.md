# N32, Delta=17, m=258: hand exclusion of the remaining fourteen-label equality profiles

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate hand proof component. Independent mathematical review OPEN.** This note uses only selected-incidence forcing, supplement forcing, the exact selected-pair orientation, and the source indegree bound from the canonical bridge.

The fourteen-label theorem reduces `n=32, Delta=17, m=258` to three demand profiles. The separate note `T3_PROFILE_3_HAND_PROOF.md` excludes `3^14`. Here we exclude

\[
3\,4^{13}
\qquad\hbox{and}\qquad
4^{14}.
\]

Throughout

\[
a=14,\qquad b=17,\qquad t=3.
\]

For every source `u`, the canonical bridge gives

\[
p_u\le \rho_u+b-a-1=\rho_u+2.
\tag{0.1}
\]

For every selected pair `u->w`, supplement forcing gives

\[
\rho_w+q_w\ge q_u-1.
\tag{0.2}
\]

Also every selected incidence of a label of demand `s` must come from a source of residual degree at least `s`.

## 1. A core-pair deficit count

We will repeatedly use the following elementary count.

Let `C` be a set of eleven possible selected sources. Suppose every selected arc is sourced in `C`, and every source outside `C` has selected outdegree zero. Let `E` be the number of selected arcs whose supplement lies outside `C`.

The selected B-pairs form an orientation of a simple graph: each unordered pair supports at most one selected arc. Hence at most `C(11,2)=55` selected arcs can remain wholly inside `C`.

If a source `u in C` has selected outdegree `q_u`, inward selected degree `p_u`, and sends `e_u` arcs outside `C`, then the number of used unordered pairs inside `C` incident with `u` is

\[
(q_u-e_u)+p_u.
\]

Thus any upper bound on `q_u+p_u` turns directly into a lower bound on unused core-pair incidences.

## 2. Excluding 4^14

For the profile

\[
s=4^{14},
\]

we have `S=56`. Equality in the fourteen-label tail ledger fixes the residual source degrees as

\[
4^{11},1^6.
\tag{2.1}
\]

Let `C` be the eleven residual-degree-four sources. Selected-incidence forcing shows that **every selected arc is sourced in `C`**. The six degree-one sources have `q=0`.

Any selected arc from `u in C` to a degree-one source must, by (0.2), satisfy

\[
1\ge q_u-1,
\]

so

\[
q_u\le2.
\tag{2.2}
\]

Let `K` be the set of core sources with `q_u<=2`, put `k=|K|`, and let `E` be the number of selected arcs from `K` to the six degree-one sources. All external selected arcs are of this form, and

\[
E\le2k.
\tag{2.3}
\]

For `u in K`, (0.1) gives `p_u<=6`. Since the core has ten other vertices, the number of unused core-pair incidences at `u` is at least

\[
10-[(q_u-e_u)+p_u]
\ge10-(2-e_u+6)=2+e_u.
\]

Summing over `K`, there are at least

\[
2k+E
\]

unused core-pair incidences. An unused core pair is counted at most twice, so the number `U` of unused unordered pairs inside `C` satisfies

\[
U\ge \left\lceil\frac{2k+E}{2}\right\rceil
=k+\left\lceil\frac E2\right\rceil.
\]

Therefore the total number of selected arcs is at most

\[
q(C)
\le 55-U+E
\le55-k+\left\lfloor\frac E2\right\rfloor
\le55,
\]

using `E<=2k` in the last step.

But the fourteen labels require at least

\[
\sum_i x_i\ge\sum_i s_i=56
\]

selected incidences, and every selected incidence is sourced in `C`. Contradiction.

Hence `4^14` is impossible.

## 3. Excluding 3 4^13

Now take

\[
s=(3,4,4,\ldots,4),
\]

so

\[
S=55.
\]

Equality in the tail ledger fixes the residual source degrees as

\[
4^{10},3^1,1^6.
\tag{3.1}
\]

Let `H` be the ten degree-four sources and let `c` be the unique degree-three source. Put

\[
C=H\cup\{c\},
\]

so again `|C|=11`.

Selected-incidence forcing shows that all selected arcs are sourced in `C`; the six degree-one sources have `q=0`. Moreover the source `c`, having residual degree three, can serve only the **single** demand-three label. Simplicity of the cross graph therefore gives

\[
q_c\le1.
\tag{3.2}
\]

As before, any selected arc to a degree-one supplement must come from a source with `q_u<=2` by (0.2).

Let `K` consist of the degree-four sources in `H` with `q_u<=2`, and put `k=|K|`. The only sources in `C` which can send outside `C` are those in `K` together with `c`. Let `E` be the number of such external arcs. By (3.2),

\[
E\le2k+1.
\tag{3.3}
\]

For a source `u in K`, exactly the same calculation as above gives at least `2+e_u` unused core-pair incidences, because `p_u<=6`.

For the special source `c`, (0.1) and (3.2) give

\[
p_c\le5,
\qquad q_c\le1.
\]

Thus, if `e_c` of its selected arcs leave the core, the number of unused core-pair incidences at `c` is at least

\[
10-[(q_c-e_c)+p_c]
\ge10-(1-e_c+5)=4+e_c.
\]

Summing over `K` and `c`, the unused-incidence total is at least

\[
2k+4+E.
\]

Hence the number `U` of unused unordered pairs inside the eleven-vertex core obeys

\[
U\ge\left\lceil\frac{2k+4+E}{2}\right\rceil
=k+2+\left\lceil\frac E2\right\rceil.
\]

The total number of selected arcs is consequently at most

\[
q(C)
\le55-U+E
\le53-k+\left\lfloor\frac E2\right\rfloor.
\]

By (3.3), `floor(E/2)<=k`, so

\[
q(C)\le53.
\]

But the demand ledger requires at least

\[
\sum_i x_i\ge S=55
\]

selected incidences, all sourced in `C`. Contradiction.

Hence `3 4^13` is impossible.

## 4. Consequence

Together with `T3_PROFILE_3_HAND_PROOF.md`, all three equality profiles of the fourteen-label theorem are impossible. Therefore

\[
\boxed{n=32,\ \Delta=17,\ m=258\text{ is impossible}.}
\]

Since the scalar fourteen-label bound already excludes every `m>=259`, the only remaining positive-surplus case in the `Delta=17` branch is now

\[
\boxed{m=257\quad(t=2).}
\]
