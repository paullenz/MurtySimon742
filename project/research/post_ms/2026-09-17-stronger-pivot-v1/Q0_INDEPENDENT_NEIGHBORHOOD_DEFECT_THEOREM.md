# Independent-neighbourhood defect theorem for the Q=0 branch

17 September 2026. Research directed by Paul Lenz; derivation and regression by ChatGPT/Geeps.

**Status:** internal candidate hand theorem; not promoted. External mathematical and novelty review remain open.

The live target is the eventual / sufficiently-large second-extremal problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 Dailly--Foucaud--Hansberg strengthening is not assumed. The published 12-vertex, 32-edge D2C graph remains a mandatory hostile control.

This note closes the entire maximum-root `Q=0` branch developed in `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` and `Q0_CRITICAL_ARM_ORIENTATION.md`. The previous saturated-source obstruction remains useful diagnostic structure, but is no longer needed for the closure.

---

## 1. Setup

Let `G` be a **non-bipartite** diameter-2-critical graph. Choose a maximum-degree vertex `v` and put

\[
B=N_G(v),\qquad A=V(G)\setminus N_G[v],\qquad b=|B|=\Delta(G).
\]

Assume

\[
Q=e(G[B])=0,
\]

so `B` is independent. Let

\[
F=G[A],\qquad f=e(F).
\]

For `x in A`, write

\[
R_x=b-|N_G(x)\cap B|,
\qquad d_x=d_F(x),
\qquad e_x=R_x-d_x=b-d_G(x)\ge0.
\]

Since every missing `A-B` incidence is residual in the `Q=0` branch,

\[
r=\sum_xR_x=2f+\sum_xe_x.
\]

With

\[
\delta:=b(n-b)-m=r-f,
\]

we therefore have the exact identity

\[
\boxed{\delta=f+\sum_{x\in A}e_x.} \tag{1.1}
\]

In particular

\[
\delta\ge f. \tag{1.2}
\]

Because `G` is non-bipartite while `B` is independent, `F` is nonempty. Otherwise

\[
B\quad\text{and}\quad \{v\}\cup A
\]

would be a bipartition of `G`.

The theorem to prove is

> **INDEPENDENT-NEIGHBOURHOOD DEFECT THEOREM (Q0-IN).**
>
> If `G` is non-bipartite D2C and a maximum-degree vertex `v` has independent neighbourhood, then
>
> \[
> \boxed{\delta\ge b-1.} \tag{IN}
> \]
>
> Equivalently,
>
> \[
> m\le b(n-b)-(b-1)
>   =b((n-1)-b)+1
>   \le M(n).
> \]

Thus no graph with `m>=M(n)+1` can lie in the maximum-root `Q=0` branch.

---

## 2. Preserved local payment: a triangle-free F-edge already closes the bound

The predecessor `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` proved:

> **Triangle-free F-edge payment.** If `xy in E(F)` lies in no triangle of `G`, then
>
> \[
> \delta\ge b-1. \tag{2.1}
> \]

For completeness, the proof is one line in the present notation. Since `xy` has no common neighbour in `B`,

\[
R_x+R_y\ge b.
\]

Since `x,y` have no common neighbour in `A` either,

\[
f\ge d_x+d_y-1.
\]

Using (1.1),

\[
\delta\ge d_x+d_y-1+e_x+e_y
       =R_x+R_y-1
       \ge b-1.
\]

Hence any counterexample to `(IN)` must satisfy

\[
\delta\le b-2, \tag{2.2}
\]

and then **every edge of `F` lies in a triangle of `G`**.

---

## 3. General source-foot lemma

The decisive improvement over the previous saturated-source attack is that the cross-edge criticality argument works for **every** source in `B`.

For `u in B`, put

\[
S_u=N_A(u),\qquad T_u=A\setminus S_u,
\qquad t_u=|T_u|.
\]

Let

\[
I_u=\{x\in S_u:d_{F[S_u]}(x)>0\}
\]

be the vertices of `S_u` which are nonisolated in the induced graph `F[S_u]`.

> **Lemma 3.1 (general source-foot lemma).** Assume `delta<=b-2`. Then for every `u in B` there is an injection
>
> \[
> I_u\hookrightarrow T_u.
> \]
>
> In particular,
>
> \[
> \boxed{|I_u|\le t_u.} \tag{3.1}
> \]

### Proof

Take `x in I_u`. There is some `z in S_u` with `xz in E(F)`, so the cross edge `ux` lies in the triangle `u-x-z`.

Delete `ux`. Since `u` and `x` remain at distance two through `z`, the pair `(u,x)` itself cannot witness criticality. Any destroyed path of length at most two using `ux` gives, after choosing the appropriate orientation, one of the following two alternatives.

### Type I

There is `p in N(u)\setminus{x}` such that

\[
p\not\sim x,
\qquad N(p)\cap N(x)=\{u\}. \tag{3.2}
\]

Because `B` is independent,

\[
N(u)=\{v\}\cup S_u.
\]

If `p=v`, then `x` has exactly one neighbour in `B`, namely `u`, so

\[
R_x=b-1.
\]

Since `f>=d_x`, (1.1) gives

\[
\delta\ge d_x+e_x=R_x=b-1,
\]

contrary to `delta<=b-2`.

If `p in S_u`, then `p,x` are nonadjacent and their `B`-neighbourhoods intersect only in `u`. Hence

\[
R_p+R_x\ge b-1. \tag{3.3}
\]

Their incident `F`-edge sets are disjoint because `px` is not an edge, so

\[
f\ge d_p+d_x.
\]

Again using (1.1),

\[
\delta\ge d_p+d_x+e_p+e_x
       =R_p+R_x
       \ge b-1,
\]

a contradiction.

Thus Type I is impossible under (2.2).

### Type II

There is `y in N(x)\setminus{u}` such that

\[
y\not\sim u,
\qquad N(y)\cap N(u)=\{x\}. \tag{3.4}
\]

The vertex `y` cannot lie in `B`, because two vertices of `B` have the root `v` as a common neighbour. It cannot be `v`, because `v` has no neighbours in `A`. Hence

\[
y\in A\setminus S_u=T_u.
\]

Moreover (3.4) gives

\[
N_F(y)\cap S_u=\{x\}. \tag{3.5}
\]

Thus `y` is a private `T_u`-foot for `x`.

Two distinct vertices `x,x' in I_u` cannot receive the same foot `y`, because (3.5) would give two different unique neighbours of `y` in `S_u`. Hence the feet are automatically injective. This proves (3.1). `square`

---

## 4. Every B-source must miss an A-vertex

Continue under the counterexample assumption `delta<=b-2`.

If some source `u` had

\[
t_u=0,
\]

then `S_u=A`. Since `F` is nonempty, `F[S_u]=F` has at least two nonisolated vertices, contradicting (3.1).

Therefore

\[
\boxed{t_u\ge1\quad\text{for every }u\in B.} \tag{4.1}
\]

Now the total number of missing `A-B` incidences is

\[
\sum_{u\in B}t_u=r=f+\delta. \tag{4.2}
\]

By (1.2) and `delta<=b-2`,

\[
r=f+\delta
 \le2\delta
 \le2b-4
 <2b. \tag{4.3}
\]

There are exactly `b` sources, all with positive integer `t_u`. Hence (4.3) forces at least one source `u` with

\[
\boxed{t_u=1.} \tag{4.4}
\]

Let

\[
T_u=\{c\}.
\]

Then (3.1) gives

\[
|I_u|\le1.
\]

But a nonempty graph has at least two nonisolated vertices. Therefore

\[
F[S_u]=F[A\setminus\{c\}]
\]

is edgeless.

Consequently every edge of `F` is incident with `c`:

> \[
> \boxed{F\text{ is a nonempty star (with possible isolated vertices), centred at }c.} \tag{4.5}
> \]

This star reduction is the entire global counting step.

---

## 5. The star contradicts triangularity

Take any edge

\[
cx\in E(F).
\]

By Section 2, every `F`-edge is triangular under the counterexample assumption.

Because `F` is a star, no vertex of `A` other than `c,x` is adjacent to both `c` and `x`. The root `v` is adjacent to no `A`-vertex. Therefore the third vertex of a triangle containing `cx` must lie in `B`.

Choose

\[
w\in B
\]

with

\[
w\sim c,
\qquad w\sim x. \tag{5.1}
\]

Thus `c,x in S_w`, and the leaf `x` is nonisolated in `F[S_w]`. Apply Lemma 3.1 to the source `w` and the vertex `x`.

Under `delta<=b-2`, Type I is impossible, so `x` must have a private foot

\[
y\in T_w
\]

with

\[
yx\in E(F). \tag{5.2}
\]

But `x` is a leaf of the star `F`: its **only** `F`-neighbour is `c`, and `c in S_w` by (5.1). No such `y in T_w` exists.

This contradiction eliminates (2.2).

Therefore

\[
\boxed{\delta\ge b-1.}
\]

This proves `(IN)`. `square`

---

## 6. Second-extremal consequence

The identity

\[
b(n-b)-(b-1)=b((n-1)-b)+1
\]

and the elementary quadratic bound

\[
b((n-1)-b)
\le\left\lfloor\frac{(n-1)^2}{4}\right\rfloor
\]

give

\[
\boxed{
 m\le M(n)
}
\]

for every non-bipartite D2C graph possessing a maximum-degree vertex whose neighbourhood is independent.

Thus the `Q=0` maximum-root branch is completely closed. In particular, the false-twin peeling reduction from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md` is no longer needed as an unresolved branch: any above-threshold graph must have

\[
Q=e(G[N(v)])>0
\]

for **every** maximum-degree root `v`.

Equivalently:

> **Maximum-triangle-root corollary.** If a non-bipartite D2C graph satisfies
>
> \[
> m\ge M(n)+1,
> \]
>
> then every maximum-degree vertex lies in a triangle.

This is stronger than the scope statement previously sought, and it is obtained indirectly through the defect theorem rather than by raw degree comparison.

---

## 7. Mandatory controls

### Expanded C5 equality family

The expanded-`C5` equality models have maximum-root `Q=0` and

\[
\delta=b-1.
\]

Thus `(IN)` is sharp at the comparison threshold.

### Published 12-vertex / 32-edge obstruction

The mandatory hostile control is not touched. The independent `X_3` reconstruction has

\[
n=12,\qquad m=32,\qquad M(12)=31,
\]

and its unique maximum-degree root has

\[
Q=12>0.
\]

Therefore it lies outside the hypothesis of `(IN)`, exactly as required.

### Bipartite graphs

The non-bipartite hypothesis is essential. A complete bipartite graph has a maximum root with independent neighbourhood but `delta=0`; it is excluded because `F=empty` and the star reduction starts from non-bipartiteness.

---

## 8. Verification and trust boundary

The companion checker `check_q0_independent_neighborhood_defect.py` directly verifies on every D2C graph in the NetworkX graph atlas through order 7:

- the exact `Q=0` defect identity;
- the triangle-free `F`-edge payment;
- the cross-edge critical-arm dichotomy;
- the Type-I defect payment whenever that arm occurs;
- the private-foot conclusion whenever Type I is absent;
- the final bound `delta>=b-1` for every non-bipartite maximum-root `Q=0` instance.

The atlas contains 17 such maximum-root instances and no violation. The finite check is regression evidence only; the hand proof above is the mathematical basis.

No novelty claim is made. No eventual second-extremal theorem is claimed yet: the remaining live branch is the maximum-degree triangle-root / disjoint-support antipode branch, and it must continue to preserve the order-12 hostile control.
