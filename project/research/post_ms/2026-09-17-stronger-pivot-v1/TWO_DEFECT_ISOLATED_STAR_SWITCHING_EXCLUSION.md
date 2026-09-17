# Two-defect switching: isolated-star extremal normal form and eventual exclusion

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The active target is the sufficiently-large/eventual second-extremal diameter-2-critical problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 strengthening is not assumed. The published order-12, size-32 obstruction remains a mandatory hostile control. This note continues the full-tight Boolean switching branch after the perfect-matching and complete one-defect regimes have been eventually excluded.

---

## 1. Entry point

Assume a maximum-degree root `v` has a full tight-antipode cover

\[
B=P_1\dot\cup\cdots\dot\cup P_k,
\qquad |P_i|=2,
\qquad b=2k.
\]

Then `G[B]` is a 2-lift of `K_k`, every `A`-vertex is a Boolean transversal, and

\[
Q=k(k-1),\qquad
r=k(a-k+1),\qquad
\delta=r-e(F),
\]

where `a=|A|` and `F=G[A]`.

For any Boolean code `c`, write `L_c` for the switched graph on the `k` fibre coordinates. The orientation-code graph `Omega_sigma` has one vertex for each Boolean code and one edge for each physical rooted `B`-edge; the actual distinct `A`-code support is a vertex cover of `Omega_sigma`.

The above-`M(n)` density window already proved in this project gives

\[
 m>M(n)\quad\Longrightarrow\quad a\le2k. \tag{1.1}
\]

The perfect-matching switched states and both one-defect normal forms are already eventually excluded. We therefore move to the first genuinely two-defect state.

---

## 2. Structural reduction for an arbitrary two-defect state

Suppose some switched graph has exactly `k-2` leaves, hence exactly two non-leaf coordinates. Call those exceptional coordinates `a,b`, and put

\[
D=[k]\setminus\{a,b\}.
\]

Because every vertex of `D` has degree exactly one, the graph has the following canonical shape.

Partition `D` into

- `P`: leaves adjacent to `a`, of size `p`;
- `R`: leaves adjacent to `b`, of size `q`;
- `2t` further leaves paired into `t` disjoint `K_2` components.

The edge `ab` may or may not be present; write `epsilon in {0,1}` for its indicator. Thus

\[
p+q+2t=k-2,
\]

and the exceptional degrees are

\[
d(a)=p+\epsilon,\qquad d(b)=q+\epsilon,
\]

which are required to differ from one.

So **every two-defect switched state belongs to an explicit four-parameter family `(p,q,t,epsilon)`**. This is the correct finite structural target for a complete two-defect cover theorem; no broad signing enumeration is needed.

The present note closes the apparent extremal member of this family:

\[
(p,q,t,\epsilon)=(0,k-2,0,0)
\]

or symmetrically `(k-2,0,0,0)`. In words, one exceptional coordinate is isolated and the other is the centre of a `K_{1,k-2}`.

---

## 3. Gauge the isolated-star state

Write the isolated coordinate as `a`, the star centre as `b`, and

\[
D=[k]\setminus\{a,b\},\qquad |D|=k-2.
\]

Gauge the Boolean switching class so that the zero code gives

\[
L_0=K_1(a)\ \dot\cup\ K_{1,k-2}(b;D). \tag{3.1}
\]

Equivalently the signing has precisely the edges

\[
\{bd:d\in D\}. \tag{3.2}
\]

For `d in D` define the clique codes

\[
x_d=\{b,d\},\qquad \bar x_d=[k]\setminus\{b,d\}. \tag{3.3}
\]

Also define the four star-centre codes

\[
z_0=\varnothing,\qquad
z_1=\{a,b\},\qquad
\bar z_0=[k],\qquad
\bar z_1=D, \tag{3.4}
\]

and the antipodal pair

\[
y=\{b\},\qquad \bar y=[k]\setminus\{b\}=\{a\}\cup D. \tag{3.5}
\]

---

## 4. Exact orientation-code decomposition

Directly evaluating the forced orientation-witness code over each quotient pair gives the complete non-isolated orientation-code graph.

### 4.1 Pairs inside `D`

For each `d!=e in D`, the two physical `B`-edges over the quotient pair `{d,e}` give

\[
x_dx_e
\]

and

\[
\bar x_d\bar x_e.
\]

Thus the `x_d` form a `K_{k-2}`, and the complementary codes form another disjoint `K_{k-2}`.

### 4.2 Pairs `{b,d}`

For each `d in D`, the two physical edges give

\[
z_0\ --\ \{a,b,d\}
\]

and its complementary edge

\[
\bar z_0\ --\ D\setminus\{d\}.
\]

These form two stars `K_{1,k-2}` centred at `z_0` and `bar z_0`.

### 4.3 Pairs `{a,d}`

For each `d in D`, the two physical edges give

\[
z_1\ --\ \{d\}
\]

and its complementary edge

\[
\bar z_1\ --\ [k]\setminus\{d\}.
\]

These form two further stars `K_{1,k-2}` centred at `z_1` and `bar z_1`.

### 4.4 Pair `{a,b}`

Both physical `B`-edges over `{a,b}` join the same two code vertices

\[
y\ --\ \bar y.
\]

Thus this is one simple `K_2` component with physical multiplicity two.

Consequently, after deleting isolated code vertices,

> **ISOLATED-STAR TWO-DEFECT ORIENTATION-CODE NORMAL FORM — internal candidate.**
>
> \[
> \boxed{
> \Omega_\sigma\cong
> K_{k-2}\dot\cup K_{k-2}
> \dot\cup 4K_{1,k-2}
> \dot\cup K_2,
> }
> \tag{4.1}
> \]
>
> with the `K_2` edge carrying physical multiplicity two.

The quotient-pair accounting is exact and exhausts the `k(k-1)` physical rooted `B`-edges.

---

## 5. Exact cover number

Each `K_{k-2}` contributes vertex-cover number `k-3`. Each star contributes one, and the final `K_2` contributes one. Hence

\[
\boxed{
\tau(\Omega_\sigma)
=2(k-3)+4+1
=2k-1.
} \tag{5.1}
\]

This is one unit stronger than the `2k-2` cover number of the one-defect normal forms.

Therefore every actual distinct Boolean code support satisfies

\[
|C|\ge2k-1. \tag{5.2}
\]

Combined with the above-threshold density window (1.1), an above-`M(n)` graph in this switching class can only have

\[
a\in\{2k-1,2k\}. \tag{5.3}
\]

Equivalently, with

\[
\lambda=2k-a-1,
\]

only

\[
\lambda\in\{0,-1\} \tag{5.4}
\]

remain.

For `k>=5`, a code cover of size at most `2k` must contain all four star centres: replacing any star centre by all its leaves costs `k-3>=2` extra vertices. Each clique contributes at least `k-3` of its `k-2` vertices, and one endpoint of the doubled `K_2` must be present.

---

## 6. F-separation in the near-balanced support

Choose a minimum canonical core consisting of

- the four star centres;
- `k-3` codes from each `K_{k-2}` clique;
- one endpoint of the doubled `K_2`.

It has size `2k-1`.

Put

\[
q=a-(2k-1)=-\lambda\in\{0,1\}.
\]

Mark the four star-centre labels and the chosen doubled-edge label exceptional. Also mark every label in a duplicated core code class and every label outside the canonical core. Exactly as in the preceding one-defect closures, at most `2q` additional labels are needed to absorb one surplus label or one duplicated code class. Hence the exceptional set satisfies

\[
|E|\le5+2q=5-2\lambda. \tag{6.1}
\]

All remaining labels are clean singleton clique-code labels.

### 6.1 Same-clique clean labels are F-independent

For `d!=e`, `Omega_sigma` contains the clique edge `x_dx_e`. Since both corresponding actual labels are singleton code classes, the represented physical rooted `B`-edge must be selected at one endpoint. The selected source coordinate is one of `d,e`, exactly where the two Boolean codes disagree. The preserved F-separation rule therefore forbids an `F`-edge between them.

The same argument applies to the complementary clique.

### 6.2 Clean cross-clique F-edges force almost-total residuality

Take clean labels of codes `x_d` and `bar x_e`.

If `d!=e`, the two codes agree only in coordinates `d,e`. The switched graph at `x_d` has leaf set

\[
D\setminus\{d\}.
\]

Among the two agreement coordinates, only `e` is a leaf and hence can support a selected incidence. Therefore, if the two labels are adjacent in `F`, F-separation permits at most one selected coordinate at the `x_d` endpoint. Thus

\[
R_{x_d}\ge k-1.
\]

The same argument at `bar x_e` gives

\[
R_{\bar x_e}\ge k-1. \tag{6.2}
\]

If `d=e`, the two codes are complementary, so they agree in no coordinate and both endpoints have residual degree `k`.

Hence every clean-clean `F`-edge runs between the two clique layers and has both endpoints among labels of residual degree at least `k-1`.

Let `h` denote the number of such high-residual clean labels. Since

\[
\sum_{x\in A}R_x=r,
\]

we have

\[
h(k-1)\le r. \tag{6.3}
\]

The clean-clean `F` graph is bipartite, so

\[
e_F(\text{clean},\text{clean})\le
\left\lfloor\frac{h^2}{4}\right\rfloor.
\]

Every edge incident with the exceptional set is charged pessimistically at maximum possible `F`-degree `k`. Therefore

> \[
> \boxed{
> e(F)\le
> \left\lfloor\frac{h^2}{4}\right\rfloor
> +(5-2\lambda)k,
> \qquad
> h\le\left\lfloor\frac{r}{k-1}\right\rfloor.
> }
> \tag{6.4}
> \]

---

## 7. Eventual exclusion above M(n)

The two possible near-balanced layers are as follows.

### 7.1 `lambda=0`: `a=2k-1`

Here

\[
r=k^2,
\qquad
h\le k+1,
\]

and therefore

\[
e(F)\le
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor+5k. \tag{7.1}
\]

The required second-extremal defect is

\[
\delta\ge2k-1.
\]

The bound (7.1) gives this for every

\[
k\ge10. \tag{7.2}
\]

### 7.2 `lambda=-1`: `a=2k`

Here

\[
r=k(k+1),
\qquad
h\le k+2,
\]

and

\[
e(F)\le
\left\lfloor\frac{(k+2)^2}{4}\right\rfloor+7k. \tag{7.3}
\]

Again the required defect is `2k-1`. The bound (7.3) supplies it for every

\[
k\ge12. \tag{7.4}
\]

We obtain:

> **ISOLATED-STAR TWO-DEFECT SWITCHING EXCLUSION — internal candidate.**
>
> In the full tight-antipode Boolean branch, if the switching class contains
>
> \[
> K_1\dot\cup K_{1,k-2}
> \]
>
> and `k>=12`, then
>
> \[
> \boxed{m\le M(n).}
> \]

This closes the apparent extremal member of the first genuinely two-defect family.

---

## 8. Relation to the broader two-defect problem

The structural reduction in Section 2 shows that the complete two-defect regime is no longer an arbitrary signing problem: it is the explicit family

\[
(p,q,t,\epsilon),\qquad
p+q+2t=k-2,
\]

with exceptional degrees `p+epsilon` and `q+epsilon` not equal to one.

Exploratory exact computations on this canonical family for small and medium `k` consistently show

\[
\tau(\Omega_\sigma)\ge2k-1,
\]

with equality only in the isolated-star cases `(0,k-2,0,0)` and its symmetric copy. This broader statement is **not proved here** and is not promoted. It is the next compact target.

If proved, it would show that every two-defect switching class already forces the stronger near-balanced window `a>=2k-1`, reducing the entire two-defect branch to the same two `lambda` layers treated above. The present exact normal form identifies the equality mechanism which such a theorem would have to preserve.

---

## 9. Negative control and trust boundary

The twelve-vertex hostile control remains untouched. It is the `k=4,r=0` perfect-matching/factorization mechanism, not a two-defect isolated-star state.

No all-order second-extremal statement is claimed. The theorem above is internal hand mathematics with exact finite replay; external review and novelty assessment remain open.
