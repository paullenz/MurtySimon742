# Tight-antipode matching stability and the Boolean-pair normal form

17 September 2026. Research directed by Paul Lenz; derivation and finite regression by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The live target is the sufficiently-large/eventual second-extremal problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 strengthening is not assumed. The published order-12, size-32 D2C exception remains a mandatory hostile control.

This note starts from the current post-`Q=0` position: for an above-threshold non-bipartite graph, a maximum-degree root has rooted triangles, and for `n>=14` the preserved all-private theorem forces a disjoint-support antipode. The purpose here is to identify exactly what an antipode costs and to isolate the zero-error configuration. The resulting zero-error structure is the same Boolean-pair mechanism visible in the reconstructed `X_3` exception.

---

## 1. Setup

Let `G` be diameter-2-critical. Choose a maximum-degree root `v` and put

\[
B=N_G(v),\qquad A=V(G)\setminus N_G[v],
\]

with

\[
b=|B|=\Delta(G),\qquad a=|A|=n-1-b,
\qquad \lambda=2b-n=b-a-1.
\]

For every vertex `x`, write its maximum-degree slack as

\[
\varepsilon_x=b-d_G(x)\ge0.
\]

Call distinct `u,w in B` an **antipode pair at v** if

\[
uw\notin E(G),\qquad N_G(u)\cap N_G(w)=\{v\}. \tag{1.1}
\]

This is exactly the antipode supplied by the preserved root-edge dichotomy once a triangle-active root neighbour has no private `A`-foot.

For an antipode pair define

\[
U=N_A(u),\qquad W=N_A(w),
\]

and

\[
C=A\setminus(U\cup W).
\]

The antipode condition gives `U cap W=empty`. Similarly put

\[
X=N_B(u),\qquad Y=N_B(w),
\]

and

\[
Z=(B\setminus\{u,w\})\setminus(X\cup Y).
\]

Again `X cap Y=empty`. Write

\[
c=|C|,\qquad z=|Z|,
\qquad \eta(uw)=c+z. \tag{1.2}
\]

Thus `eta` is the number of vertices, apart from the root and the antipode endpoints, adjacent to neither endpoint.

---

## 2. Exact antipode slack identity

Because `u,w` have no common neighbour other than `v`,

\[
|U|+|W|=a-c,
\qquad
|X|+|Y|=b-2-z.
\]

Therefore

\[
d(u)+d(w)
 =2+(a-c)+(b-2-z)
 =n-1-c-z.
\]

Equivalently:

> **ANTIPODE SLACK IDENTITY.**
>
> \[
> \boxed{\varepsilon_u+\varepsilon_w
> =\lambda+1+\eta(uw).} \tag{AS}
> \]

In particular every antipode pays at least `lambda+1` units of endpoint degree slack.

Call an antipode **tight** when

\[
\eta(uw)=0. \tag{2.1}
\]

The following are equivalent:

1. `uw` is tight;
2. `d(u)+d(w)=n-1`;
3. every vertex outside `{u,w,v}` is adjacent to exactly one of `u,w`.

The third formulation makes the connection to the Boolean/cube mechanism explicit.

### Complement interpretation

Let `H=\overline G`. Since `uw` is a G-nonedge, it is an H-edge. The antipode condition says that every vertex other than `v` is H-adjacent to at least one of `u,w`, while `v` is adjacent in H to neither endpoint. Hence

\[
uw\to v
\]

in the standard quasi-edge notation. In particular the single H-edge `uw` is a quasi-edge for **both** missing H-edges `uv` and `wv`. This is the exact double-use mechanism hidden inside the antipode branch.

---

## 3. Tight antipodes form a matching

> **Theorem 3.1 (tight-antipode matching).** For a fixed root `v`, no vertex of `B` has two distinct tight antipode partners. Hence the graph on `B` whose edges are the tight antipode pairs is a matching.

### Proof

Suppose `w` had two tight antipode partners `u_1,u_2`.

Put

\[
R=V(G)\setminus(N_G(w)\cup\{w\}).
\]

Both `u_1,u_2` belong to `R`. Tightness says that every vertex outside `{v,w,u_i}` which is not adjacent to `w` must be adjacent to `u_i`, while no neighbour of `w` other than `v` can be adjacent to `u_i`. Consequently

\[
N_G(u_i)=\{v\}\cup(R\setminus\{u_i\}),
\]

so

\[
N_G[u_1]=N_G[u_2]=\{v\}\cup R. \tag{3.1}
\]

Thus `u_1,u_2` are adjacent true twins. The edge `u_1u_2` cannot be critical: after deleting it the endpoints still have the common neighbour `v`, and every other vertex adjacent to one of the twins is adjacent to the other as well. Hence the diameter remains at most two, contradicting D2C criticality.

So tight antipodes have maximum degree one in the antipode relation. `square`

### Strategic meaning

This is the first useful stability separation in the antipode branch:

- zero-error antipodes are forced into disjoint pairs;
- any attempted hub with two or more antipode partners must have positive error `eta` on all but at most one of those relations.

The order-12 hostile control lies exactly in the zero-error paired regime.

---

## 4. A matching cut for arbitrary antipodes

Let `J_v` be the antipode graph on `B`. For any matching `M` in `J_v`, summing `(AS)` over the disjoint endpoint pairs gives

\[
\sum_{x\in V(M)}\varepsilon_x
 =|M|(\lambda+1)+\sum_{e\in M}\eta(e). \tag{4.1}
\]

The canonical maximum-root ledger gives

\[
\sum_{x\in B}\varepsilon_x
 =b\lambda+r-Q, \tag{4.2}
\]

where `Q=e(G[B])` is the rooted triangle count and `r` is the residual cross count. Therefore

> **ANTIPODE MATCHING CUT.** For every matching `M subseteq J_v`,
>
> \[
> \boxed{
> b\lambda+r-Q
> \ge |M|(\lambda+1)+\sum_{e\in M}\eta(e).
> } \tag{AMC}
> \]

At exact balance (`lambda=0`) this becomes

\[
r-Q\ge |M|+\sum_{e\in M}\eta(e). \tag{4.3}
\]

This does not by itself close the second-extremal defect, but it converts disjoint antipodes into an exact residual-load payment. The positive error `eta` is not a heuristic penalty: it is literally additional maximum-degree slack.

---

## 5. Full tight cover: a 2-lift of a complete graph

Assume now that the tight antipodes cover all of `B`. By Theorem 3.1 they form a perfect matching, so

\[
b=2k
\]

and we may write the pairs as

\[
P_i=\{u_i,w_i\},\qquad 1\le i\le k.
\]

Tightness has two immediate consequences.

### 5.1 Between two antipode pairs

Fix `i != j`. Every vertex of `P_j` is adjacent to exactly one endpoint of `P_i`, and every vertex of `P_i` is adjacent to exactly one endpoint of `P_j`. Therefore the `2 x 2` bipartite graph between `P_i` and `P_j` is a perfect matching.

Hence `G[B]` is a **2-lift of `K_k`**: after choosing a `0/1` label on each pair, every pair of fibres is joined by either the parallel or crossed perfect matching.

In particular

\[
d_{G[B]}(x)=k-1\quad(x\in B), \tag{5.1}
\]

and

\[
\boxed{Q=e(G[B])=k(k-1).} \tag{5.2}
\]

### 5.2 Every A-vertex is a transversal

For every `x in A` and every tight pair `P_i`, exactly one endpoint of `P_i` is adjacent to `x`. Thus

\[
d_B(x)=k. \tag{5.3}
\]

After choosing a `0/1` endpoint in each pair, every `A`-vertex receives a binary code

\[
c(x)\in\{0,1\}^k. \tag{5.4}
\]

This is the Boolean-pair normal form.

Exactly half of the `A-B` pairs are G-edges and half are H-edges. The total H-cross count is therefore

\[
Q+r=ak.
\]

Using (5.2):

> \[
> \boxed{r=k(a-k+1).} \tag{5.5}
> \]

Consequently

\[
\boxed{\delta=r-e(F)=k(a-k+1)-e(F).} \tag{5.6}
\]

Maximum degree also gives, for every `x in A`,

\[
k+d_F(x)\le2k,
\]

so

\[
d_F(x)\le k,
\qquad
 e(F)\le \frac{ak}{2}. \tag{5.7}
\]

The coarse consequence

\[
\delta\ge \frac{b(1-\lambda)}4
\]

is not strong enough to solve the eventual problem, but (5.2)--(5.6) reduce the zero-error antipode branch to a much more rigid coded object.

---

## 6. Selected edges acquire forced binary codes

The canonical selected/quasi-edge system becomes especially rigid in the full tight-cover normal form.

Take an edge `pq` of `G[B]`, where `p in P_i`, `q in P_j`, `i != j`. Suppose the canonical representative is oriented at source `q`:

\[
qx\to p
\]

in the complement, with `x in A`. Equivalently in `G`,

\[
qx\notin E(G),\qquad px\in E(G),
\qquad N_G(q)\cap N_G(x)=\{p\}. \tag{6.1}
\]

Then the binary code of `x` is completely determined by the ordered B-edge `q -> p`:

1. in fibre `P_j`, `x` chooses the mate of `q`;
2. in fibre `P_i`, `x` chooses `p`;
3. in every other fibre `P_ell`, `x` chooses the endpoint **not** adjacent to `q`.

Indeed any other choice would create a second common B-neighbour of `q` and `x`, contradicting (6.1).

Moreover, if

\[
S_q=N_A(q),
\]

then (6.1) also forces

\[
N_F(x)\cap S_q=\varnothing. \tag{6.2}
\]

Thus every oriented rooted-triangle edge carries both

- a **forced Boolean code type**, and
- an **F-separation condition**.

At a fixed source `q`, its different B-neighbours lie in different fibres, so the forced code types are different. This is the precise bridge back to the selected/Hall machinery: in the tight zero-error branch, the selected labels are no longer arbitrary capacities but prescribed binary witnesses.

---

## 7. The order-12 hostile control is exactly the zero-error normal form

For the reconstructed `X_3` graph:

\[
a=3,\qquad b=8,\qquad k=4,
\qquad \lambda=4,
\]

and the four cube-antipodal pairs form a perfect tight-antipode matching.

The B-graph is

\[
Q_3\cong K_{4,4}-M,
\]

a 3-regular 2-lift of `K_4`. Formula (5.2) gives

\[
Q=4\cdot3=12.
\]

The three A-vertices are binary transversals of the four antipode pairs. Formula (5.5) gives

\[
r=4(3-4+1)=0,
\]

and `F` is empty, so

\[
\delta=0.
\]

The deterministic reconstruction has

\[
n=12,\qquad m=32>M(12)=31.
\]

Every one of the 12 B-edges has exactly one canonical A-witness in the reconstruction. Thus the known finite exception is not merely compatible with the theorem: it sits exactly at its zero-error Boolean-pair boundary.

---

## 8. What this changes strategically

The antipode branch should no longer be treated as one undifferentiated case.

It has a natural stability split:

### Errorful antipodes

If `eta(uw)>0`, identity `(AS)` charges that failure of exact complementarity directly to maximum-degree slack. Matchings of such pairs give the quantitative cut `(AMC)`.

### Tight antipodes

They cannot branch: Theorem 3.1 says they form a matching. If they cover `B`, the entire rooted B-layer collapses to a 2-lift of a complete graph and the A-layer becomes a binary transversal system. Selected witnesses then have forced code types and F-separation constraints.

This is substantially closer to the requested stability theorem whose error vanishes only in a cube/Boolean-flow configuration. The next high-value unit should attack the **full or near-full tight matching branch** through the forced-code orientation system in Section 6, while using `(AMC)` to price the unmatched/errorful part.

No eventual second-extremal theorem is claimed here.
