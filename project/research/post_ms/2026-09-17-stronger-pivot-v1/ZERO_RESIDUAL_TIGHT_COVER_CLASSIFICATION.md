# Residual-zero full tight-antipode covers: switching-factorization classification

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The live problem is the sufficiently-large/eventual second-extremal problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 Dailly--Foucaud--Hansberg Conjecture 3 is not assumed. The published 2024 order-12, size-32 D2C graph remains a mandatory hostile control.

This note sharpens the full tight-antipode Boolean normal form from `ANTIPODE_TIGHT_MATCHING_STABILITY.md` at its extreme boundary `r=0`. The result is unexpectedly rigid: apart from the trivial `Q=0` endpoint, the only possible fibre counts are `k=2` and `k=4`. The `k=2` normal form is exactly the six-vertex graph `H5`; the `k=4` normal form is the independently reconstructed `X_3` twelve-vertex, 32-edge graph.

The theorem therefore explains why the exact zero-residual Boolean obstruction does **not** scale to arbitrarily large order.

---

## 1. Entry point: full tight cover

Let `G` be D2C. Choose a maximum-degree root `v` and put

\[
B=N_G(v),\qquad A=V(G)\setminus N_G[v].
\]

Assume the tight antipodes at `v` cover all of `B`. By the preserved tight-antipode matching theorem they form a perfect matching. Write

\[
B=P_1\dot\cup\cdots\dot\cup P_k,
\qquad P_i=\{(i,0),(i,1)\},
\qquad b=|B|=2k.
\]

Between every two fibres `P_i,P_j`, `G[B]` induces a perfect matching. Thus `G[B]` is a 2-lift of `K_k`. Encode that lift by bits

\[
\sigma_{ij}\in\{0,1\},\qquad 1\le i<j\le k,
\]

where

\[
(i,t)(j,t\oplus\sigma_{ij})\in E(G).
\]

Every `A`-vertex is a transversal of the antipode pairs, so it has a binary code

\[
c(x)=(c_1(x),\ldots,c_k(x))\in\{0,1\}^k,
\]

with `x` adjacent to `(i,c_i(x))` and nonadjacent to `(i,1-c_i(x))`.

The preserved full-cover identities are

\[
Q=e(G[B])=k(k-1),
\]

and

\[
r=k(a-k+1),\qquad a=|A|. \tag{1.1}
\]

We now impose the exact boundary

\[
\boxed{r=0}. \tag{1.2}
\]

Since `k>0`, (1.1) gives

\[
\boxed{a=k-1}. \tag{1.3}
\]

---

## 2. Residual zero forces `F=G[A]` to be empty

The total number of H-cross edges is `ak`. Under (1.3),

\[
ak=k(k-1)=Q.
\]

The selected system contains exactly `Q` cross edges, one for each edge of `G[B]`. Therefore **every** H-cross edge is selected.

Equivalently:

- every source residual degree `rho_u` is zero;
- every label residual degree `R_x` is zero;
- every H-cross edge incident with every `x in A` is a selected quasi-edge.

For a selected incidence `ux -> w`, the preserved selected-edge inequality is

\[
d_F(x)\le \rho_u+R_x.
\]

Both terms on the right vanish. Hence

\[
\boxed{F=\varnothing}. \tag{2.1}
\]

Consequently

\[
\delta=r-e(F)=0. \tag{2.2}
\]

This already shows that the residual-zero tight-cover boundary is an exact zero-defect mechanism.

---

## 3. Each A-code produces a switched graph on the fibre indices

Fix `x in A`. Define a graph `L_x` on vertex set `[k]={1,...,k}` by

\[
ij\in E(L_x)
\quad\Longleftrightarrow\quad
\sigma_{ij}\oplus c_i(x)\oplus c_j(x)=1. \tag{3.1}
\]

Thus `L_x` is obtained from the signed edge set encoded by `sigma` by Seidel switching with the vertex subset

\[
S_x=\{i:c_i(x)=1\}.
\]

For fibre `j`, the unique H-neighbour of `x` in `P_j` is

\[
q_j(x)=(j,1-c_j(x)).
\]

A direct check of the 2-lift shows:

> the common B-neighbours of `q_j(x)` and `x` are in one-to-one correspondence with the neighbours of `j` in `L_x`.

Indeed, in fibre `P_i`, the B-neighbour of `q_j(x)` is

\[
(i,(1-c_j(x))\oplus\sigma_{ij}),
\]

which equals the endpoint `(i,c_i(x))` chosen by `x` exactly when (3.1) holds.

Because `F` is empty, there are no A-side common neighbours of `q_j(x)` and `x`. Also `v` is not adjacent to `x`. Hence the G-common neighbours of the nonedge `q_j(x)x` are exactly those encoded by `N_{L_x}(j)`.

But every H-cross edge `q_j(x)x` is selected. Its corresponding G-nonedge therefore has exactly one common neighbour, namely its B-exception. Thus

\[
d_{L_x}(j)=1
\qquad\text{for every }j. \tag{3.2}
\]

Therefore:

> **PERFECT-MATCHING SWITCHING LEMMA.** For every `x in A`, `L_x` is a perfect matching of `K_k`.

In particular, unless `k=0`, the residual-zero full-cover branch requires `k` to be even.

---

## 4. The matchings from distinct A-labels form a 1-factorization

Because all H-cross edges are selected and their number equals `Q`, the chosen selected cross edges are in bijection with the `Q` rooted B-edges.

Fix `x in A`. If `ij` is an edge of the perfect matching `L_x`, then the selected incidences sourced in fibres `i` and `j` map to the two distinct G-edges between `P_i` and `P_j`. Thus `x` accounts for **both** B-edges lying over every matching edge `ij in L_x`.

Consequently, if two distinct labels `x,y` had

\[
ij\in E(L_x)\cap E(L_y),
\]

then their selected H-cross edges would have to reuse the same two rooted B-edges over `ij`, contradicting the bijection between selected cross edges and rooted B-edges.

Hence the perfect matchings

\[
\{L_x:x\in A\}
\]

are pairwise edge-disjoint.

There are `a=k-1` such matchings, each with `k/2` edges. Their total number of edges is therefore

\[
(k-1)\frac{k}{2}=\binom{k}{2}.
\]

So they partition `E(K_k)`:

> **FACTORIZATION LEMMA.** The graphs `L_x`, `x in A`, form a 1-factorization of `K_k`.

This is already much stronger than the generic Boolean-code statement.

---

## 5. Switching-equivalent disjoint perfect matchings force `k=4`

For `x,y in A`, let

\[
S=S_x\triangle S_y
 =\{i:c_i(x)\ne c_i(y)\}.
\]

By (3.1), switching from `x` to `y` toggles exactly the cut `delta(S)` of `K_k`. Thus

\[
E(L_x)\triangle E(L_y)=\delta(S). \tag{5.1}
\]

The factorization lemma says the two perfect matchings are edge-disjoint, so their symmetric difference is simply their union. Every vertex has degree exactly two in that union.

On the other hand, in the cut `delta(S)`:

- each vertex of `S` has degree `k-|S|`;
- each vertex outside `S` has degree `|S|`.

For a nonempty proper cut to be 2-regular we must therefore have simultaneously

\[
|S|=2,
\qquad
k-|S|=2.
\]

Hence

\[
\boxed{k=4}. \tag{5.2}
\]

This argument applies whenever there are at least two A-labels, i.e. `k-1>=2`.

The remaining small case `k=2` has only one A-label and therefore no pair of distinct switching matchings to compare.

We obtain:

> **ZERO-RESIDUAL FULL-TIGHT-COVER CLASSIFICATION — internal candidate.**  
> Let a D2C graph admit a maximum-degree root whose tight antipodes cover `B=N(v)`, with `b=2k`, and suppose the canonical residual count is `r=0`. In the triangle-bearing range `k>=2`, one must have
>
> \[
> \boxed{k\in\{2,4\}}.
> \]
>
> Moreover `a=k-1`, `F=empty`, and `delta=0`.

Thus there is **no residual-zero full tight-antipode mechanism for `k>=6`**.

---

## 6. The `k=2` normal form is exactly `H5`

When `k=2`:

\[
b=4,\qquad a=1,\qquad n=6.
\]

The B-layer consists of two antipode pairs joined by a perfect matching. The single A-vertex chooses one endpoint from each pair. The edge count is

\[
m=b(n-b)-\delta=4\cdot2=8.
\]

This is exactly the graph `T_6` in Dailly--Foucaud--Hansberg (2019), and their Section 3 states that `T_6` is isomorphic to their exceptional graph `H5`.

An explicit mapping is immediate from their definition of `T_6`: choosing their degree-four vertex `u` as the root, its four neighbours form our B-layer, their remaining vertex `v` is our single A-label, the two `a_i b_i` edges are the B matching, and `v` chooses the two `b_i` endpoints.

Thus the first residual-zero tight-cover exception is the already-classical six-vertex exception.

---

## 7. The `k=4` normal form is the twelve-vertex Boolean/cube mechanism

When `k=4`:

\[
b=8,\qquad a=3,\qquad n=12,
\]

and

\[
m=8\cdot4=32.
\]

The three A-labels supply the three perfect matchings in the unique 1-factorization of `K_4`.

After switching the fibre labels by one A-code, we may take one of the three matchings as the signed edge set of the 2-lift. A 2-lift of `K_4` whose negative edges form a perfect matching is bipartite and 3-regular on eight vertices; equivalently it is

\[
K_{4,4}-M\cong Q_3.
\]

The remaining two A-codes correspond to the other two 1-factors. Up to the endpoint-switching and factor-permuting automorphisms of the cube, this is the coordinate-face incidence construction preserved in `HYPERCUBE_FACE_EXCEPTION.md`.

The companion exact checker enumerates the finite representative choices after gauge-fixing and verifies that every resulting normal form is isomorphic to the independently constructed `X_3`.

Therefore the residual-zero `k=4` normal form has

\[
n=12,\qquad m=32,
\qquad M(12)=31,
\]

and is exactly the project's independent twelve-vertex hostile control `X_3`.

**Trust boundary on the published 2024 figure.** The project still does not claim a direct adjacency-list certification that `X_3` is the graph drawn in Figure 1 of Radosavljević--Stanić--Živković (2024). The published graph and `X_3` share the decisive reported invariants, and small-order enumeration would force isomorphism if its completeness premise is accepted, but the present theorem is an internal structural classification of the canonical full-tight `r=0` mechanism, not a new primary-source identification of the drawing.

---

## 8. Why this matters for the eventual problem

The two residual-zero cases are exactly the two exceptional mechanisms that one would want a sufficiently-large theorem to isolate:

- `k=2`: the six-vertex `H5`;
- `k=4`: the twelve-vertex, 32-edge Boolean/cube obstruction.

There is no larger member of this exact zero-residual full-tight family.

This gives a concrete explanation of why the `12/32` obstruction fails to scale: the Boolean witness system at `r=0` would require `k-1` pairwise edge-disjoint perfect matchings lying in one switching class. Two such matchings already force the fibre set to have size four.

The full-cover formula

\[
r=k(a-k+1)
\]

also shows there is a discrete jump after this boundary. If `k>=6`, the classification rules out `a=k-1`, so any full tight cover must have

\[
a\ge k,
\qquad
r\ge k.
\]

That is only a first stability payment, but it is exact and structural rather than a scalar scan.

---

## 9. Next structural target

The right continuation is not another generic survivor enumeration. It is the **first positive-residual tight-cover layer**.

For arbitrary full tight cover, each A-label `x` still defines the switched graph `L_x`. If the label has residual degree `R_x`, then only `k-R_x` of its H-cross incidences are selected. Every selected source coordinate must be a degree-one vertex of `L_x`. Therefore

\[
\boxed{k-\ell_x\le R_x}, \tag{9.1}
\]

where `ell_x` is the number of degree-one vertices of `L_x`.

Summing,

\[
\sum_x (k-\ell_x)\le r. \tag{9.2}
\]

So positive residual mass measures exactly how far the family of switched graphs can deviate, in aggregate, from the perfect-matching boundary used above.

A useful next theorem would be a switching-stability version of Section 5: if two switching-equivalent graphs each have all but a small number of vertices of degree one, then either `k=4` or their combined leaf deficiency pays a quantitative amount. Combined with (9.2), that would turn deviation from the finite `H5/X_3` mechanisms directly into residual defect.

That is now the highest-value continuation of the full-tight branch.
