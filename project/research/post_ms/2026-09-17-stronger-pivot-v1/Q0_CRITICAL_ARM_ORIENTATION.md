# Q=0 critical-arm orientation and the saturated-source obstruction

17 September 2026. Research directed by Paul Lenz; derivation and finite diagnostics by ChatGPT/Geeps.

**Status: internal hand mathematics; not promoted. External mathematical and novelty review remain open.**

The active problem is the eventual / sufficiently-large second-extremal problem for diameter-2-critical graphs around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 strengthening is not assumed. The published order-12, size-32 D2C exception remains a mandatory hostile control.

This note continues `MAX_TRIANGLE_OR_TWIN_REDUCTION.md`. Its purpose is to make the peeled `Q=0` core structural rather than merely numerical.

---

## 1. Setup and exact defect ledger

Let `G` be D2C and choose a maximum-degree root `v`. Put

\[
B=N_G(v),\qquad A=V(G)\setminus N_G[v],\qquad b=|B|=\Delta(G),
\]

and assume

\[
Q=e(G[B])=0.
\]

Thus `B` is independent. Let

\[
F=G[A],\qquad f=e(F).
\]

For `x in A` write

\[
R_x=b-|N_G(x)\cap B|,
\qquad d_x=d_F(x),
\qquad e_x=R_x-d_x=b-d_G(x)\ge0.
\]

As established in `MAX_TRIANGLE_OR_TWIN_REDUCTION.md`, every missing `A-B` incidence is residual and

\[
\boxed{\delta:=b(n-b)-m=f+\sum_{x\in A}e_x.} \tag{1.1}
\]

Equivalently, if

\[
r=\sum_xR_x
\]

is the total number of missing `A-B` incidences, then

\[
\boxed{r=f+\delta.} \tag{1.2}
\]

The live target is

\[
\delta\ge b-1. \tag{IN}
\]

That target would close the entire independent-neighbourhood branch because

\[
m\le b(n-b)-(b-1)=b((n-1)-b)+1\le M(n).
\]

---

## 2. Critical arms for a triangular F-edge

Take an edge `xy in E(F)` which lies in a triangle of `G`.

Because deleting `xy` is critical but `x` and `y` remain at distance two through a common neighbour, the pair `(x,y)` itself cannot witness criticality. Any length-at-most-two path destroyed by deleting `xy` must therefore have one of the forms

\[
z-x-y\qquad\text{or}\qquad x-y-z.
\]

After orienting the edge if necessary, there is a vertex `z` such that

\[
z\sim x,\qquad z\not\sim y,
\qquad N_G(z)\cap N_G(y)=\{x\}. \tag{2.1}
\]

Call `(z,x,y)` a **critical arm** and write it schematically as

\[
z:x\to y.
\]

The arm vertex `z` cannot be the root `v`, since `v` has no neighbours in `A`. Thus `z` lies in `A` or `B`.

This is the direct `G`-language form of the standard complement quasi-edge observation: in `H=\bar G`, the edge `zy` dominates every vertex except `x`.

---

## 3. An A-side arm already overpays the target

> **Lemma 3.1 (A-arm payment).** If a triangular `F`-edge has a critical arm `(z,x,y)` with `z in A`, then
>
> \[
> \boxed{\delta\ge b.} \tag{3.1}
> \]

### Proof

From (2.1), `z` and `y` have no common neighbour in `B`. Hence their `B`-neighbourhoods are disjoint:

\[
(b-R_z)+(b-R_y)\le b,
\]

so

\[
R_z+R_y\ge b. \tag{3.2}
\]

Also `zy` is not an edge of `F`, so the sets of `F`-edges incident with `z` and `y` are disjoint. Therefore

\[
f\ge d_z+d_y. \tag{3.3}
\]

Using (1.1),

\[
\delta
\ge d_z+d_y+e_z+e_y
=R_z+R_y
\ge b.
\]

This proves the lemma. `square`

Thus any putative counterexample to `(IN)` with

\[
\delta\le b-2 \tag{3.4}
\]

has **no A-side arm at all** for a triangular `F`-edge.

The predecessor triangle-free-edge payment theorem already says that under (3.4) every `F`-edge is triangular. Consequently every `F`-edge has a `B`-side arm.

---

## 4. The exact B-arm orientation

Assume henceforth

\[
\delta\le b-2. \tag{4.1}
\]

For each edge `xy in E(F)`, choose one `B`-side critical arm. Orient the edge

\[
x\longrightarrow y
\]

when its chosen arm is

\[
u:x\to y,
\qquad u\in B. \tag{4.2}
\]

Equivalently,

\[
u\sim x,\qquad u\not\sim y,
\qquad N_G(u)\cap N_G(y)=\{x\}. \tag{4.3}
\]

Associate the oriented edge `x->y` with the missing cross incidence

\[
\psi(xy)=(u,y). \tag{4.4}
\]

### Injectivity

The incidence `(u,y)` determines its unique common neighbour with `y`, namely `x`, by (4.3). Hence it determines the `F`-edge `xy`. Therefore distinct `F`-edges cannot receive the same missing incidence:

\[
\boxed{\psi:E(F)\hookrightarrow \{(u,y)\in B\times A:u\not\sim y\}.} \tag{4.5}
\]

Since there are `r=f+delta` missing cross incidences and exactly `f` of them are used by `psi`, the number of unused incidences is **exactly**

\[
\boxed{r-f=\delta.} \tag{4.6}
\]

Call these unused incidences **free incidences**.

This is the main normalization of the present note: **the residual defect is exactly the number of free cross incidences after one critical arm is chosen for every `F`-edge.**

---

## 5. Endpoint formula and local nesting

For `x in A`, let

- `indeg(x)` and `outdeg(x)` be its indegree and outdegree in the chosen orientation of `F`;
- `phi_x` be the number of free incidences `(u,x)` with `u in B`.

Exactly `indeg(x)` of the `R_x` missing incidences at `x` are used by `psi`. Hence

\[
\phi_x=R_x-\operatorname{indeg}(x).
\]

Since

\[
R_x=d_x+e_x
=\operatorname{indeg}(x)+\operatorname{outdeg}(x)+e_x,
\]

we obtain the exact identity

> **Endpoint free-defect formula**
>
> \[
> \boxed{\phi_x=\operatorname{outdeg}(x)+e_x.} \tag{5.1}
> \]

Summing (5.1) gives

\[
\sum_x\phi_x=f+\sum_xe_x=\delta,
\]

recovering (4.6).

There is also a useful nesting statement. If `x->y` is labelled by `u`, then (4.3) implies that `u` misses `y` and every `F`-neighbour of `y` other than `x`. Thus

\[
|A\setminus N_A(u)|\ge d_y. \tag{5.2}
\]

Moreover, if a second source `w in B` lies in

\[
N_B(x)\setminus N_B(y)
\]

then `(w,y)` is free unless `w=u`: an incidence `(w,y)` could only represent the same `F`-edge `xy`, already represented by `(u,y)`. Similarly every source in

\[
N_B(y)\setminus N_B(x)
\]

gives a free incidence at `x`.

Hence

\[
\boxed{
\phi_x+\phi_y\ge
|N_B(x)\triangle N_B(y)|-1.
} \tag{5.3}
\]

Formula (5.3) is the direct analogue, in the present root coordinates, of the familiar quasi-edge nesting phenomenon: an oriented edge can have nearly nested opposite-side neighbourhoods only by spending free defect.

---

## 6. Saturated B-sources

It is useful to count free incidences by their `B`-endpoint as well.

For `u in B`, put

\[
\sigma_u=
|\{y\in A:u\not\sim y\text{ and }(u,y)\notin\operatorname{im}\psi\}|.
\]

Then

\[
\boxed{\delta=\sum_{u\in B}\sigma_u.} \tag{6.1}
\]

Call `u` **saturated** when

\[
\sigma_u=0.
\]

If every source but at most one is nonsaturated, then (6.1) immediately gives `delta>=b-1`. Therefore a counterexample satisfying (4.1) must have at least

\[
b-\delta\ge2 \tag{6.2}
\]

saturated sources.

For a saturated source `u`, define

\[
S_u=N_A(u),\qquad T_u=A\setminus S_u.
\]

Every missing incidence `(u,y)`, `y in T_u`, is used by `psi`. If it represents the edge `xy`, then (4.3) says

\[
N_F(y)\cap S_u=\{x\}. \tag{6.3}
\]

Consequently:

> **Lemma 6.1 (saturated cut).** For a saturated source `u`, every `y in T_u` has exactly one `F`-neighbour in `S_u`, and every edge of the cut
>
> \[
> E_F(S_u,T_u)
> \]
>
> is labelled by `u`. In particular
>
> \[
> \boxed{|E_F(S_u,T_u)|=|T_u|.} \tag{6.4}
> \]

Thus saturation is not merely a scalar state: `S_u` is a one-neighbour dominating side of the `F`-cut.

---

## 7. Two independent saturated sides are impossible

> **Lemma 7.1.** Suppose `F` is nonempty. Two distinct saturated sources `u,w` cannot both have `F[S_u]` and `F[S_w]` edgeless.

### Proof

By Lemma 6.1, every cut edge in `E_F(S_u,T_u)` is assigned to the label `u`, while every cut edge in `E_F(S_w,T_w)` is assigned to `w`. Since each `F`-edge has exactly one chosen arm, these two cut-edge sets are disjoint.                                   (7.1)

Assume first `S_u!=S_w`. Without loss of generality take

\[
x\in S_u\setminus S_w.
\]

Because `x` lies outside `S_w`, saturation of `w` gives a unique neighbour

\[
y\in S_w
\]

of `x` in `S_w`. Since `S_u` is independent, `y` cannot lie in `S_u`. Therefore

\[
x\in S_u\setminus S_w,
\qquad
y\in S_w\setminus S_u.
\]

The edge `xy` crosses **both** cuts, contradicting (7.1).

If `S_u=S_w=S`, then `S` is independent. Since `F` is nonempty, `T=A\setminus S` is nonempty. For `y in T`, Lemma 6.1 gives the same unique crossing edge `xy` for both sources. Saturation would require that single edge to be labelled simultaneously by `u` and `w`, again impossible.

This proves the lemma. `square`

Combining (6.2) with Lemma 7.1 gives the first sharp obstruction:

> **Corollary 7.2 (internal saturated side).** Any counterexample to `(IN)` with `delta<=b-2` admits, for every chosen full B-arm orientation, a saturated source `u` such that
>
> \[
> \boxed{e(F[S_u])>0.} \tag{7.2}
> \]

So the unresolved `Q=0` core is no longer “all triangular `F`-edges”. It must contain a source which simultaneously

1. spends **every** one of its missing cross incidences as a critical arm; and
2. sees both endpoints of an internal `F`-edge.

---

## 8. Internal saturated edges force private T-feet

The preceding obstruction can be sharpened using criticality of the cross edges from the saturated source.

Let `u` be saturated and assume `x in S_u` is incident with an edge of `F[S_u]`. Then the G-edge `ux` lies in a triangle. Delete `ux`. The endpoints remain at distance two, so criticality gives one of two arm types.

### Type I: an arm entering `x` through `u`

There is `z in N(u)\setminus{x}` with

\[
z\not\sim x,
\qquad N(z)\cap N(x)=\{u\}. \tag{8.1}
\]

Since `B` is independent,

\[
N(u)=\{v\}\cup S_u.
\]

If `z=v`, then `x` has exactly one `B`-neighbour, namely `u`, so `R_x=b-1`; from `delta=f+sum e` and `f>=d_x` we get

\[
\delta\ge d_x+e_x=R_x=b-1.
\]

If `z in S_u`, then `z` and `x` have exactly one common `B`-neighbour, `u`, so

\[
R_z+R_x\ge b-1.
\]

They are nonadjacent in `F`, hence their incident `F`-edge sets are disjoint and `f>=d_z+d_x`. Therefore again

\[
\delta\ge R_z+R_x\ge b-1.
\]

Thus Type I already proves `(IN)`.

### Type II: an arm leaving `x`

If `(IN)` is assumed false, Type I is impossible. Therefore there is a vertex `y` with

\[
y\sim x,\qquad y\not\sim u,
\qquad N(y)\cap N(u)=\{x\}. \tag{8.2}
\]

The vertex `y` cannot lie in `B`, because every two vertices of `B` have the root `v` as a common neighbour. Hence

\[
y\in T_u.
\]

Condition (8.2) says exactly

\[
N_F(y)\cap S_u=\{x\}. \tag{8.3}
\]

Distinct vertices `x` require distinct such feet, because every `y in T_u` has a unique neighbour in `S_u`.

Hence:

> **Lemma 8.1 (internal-foot injection).** If `delta<=b-2` and `u` is saturated, then every nonisolated vertex of `F[S_u]` has a distinct private foot in `T_u`. In particular
>
> \[
> \boxed{
> |\{x\in S_u:d_{F[S_u]}(x)>0\}|\le |T_u|.
> } \tag{8.4}
> \]

This is the exact remaining shape forced by a failed defect proof.

---

## 9. What has and has not been proved

The preceding results do **not** yet prove `delta>=b-1`.

They do prove that any counterexample with `delta<=b-2` must contain a highly constrained configuration:

- all `F`-edges are triangular;
- no triangular `F`-edge has an A-side critical arm;
- all `F`-edges can be injectively routed to missing `A-B` incidences;
- exactly `delta` cross incidences remain free;
- at least two `B`-sources are saturated;
- at least one saturated source `u` has `F[S_u]` nonempty;
- every nonisolated vertex of that internal graph `F[S_u]` has a distinct private foot in `T_u`.

A tempting attempted closure was to prove directly that every saturated `S_u` is independent. The graph-atlas diagnostic below supports that statement, but the present hand argument does **not** establish it. The internal-foot alternative in Section 8 is the genuine obstruction and is preserved explicitly rather than hidden.

The next high-value theorem should therefore attack exactly this obstruction: a saturated source with an internal edge and a private `T_u` foot for every internal-active `S_u` vertex. Possible routes are to price the criticality of the foot edges, or to combine two saturated-source cut systems before returning to broad Hall machinery.

---

## 10. Relation to the peeled core and mandatory controls

In the peeled twin core from `MAX_TRIANGLE_OR_TWIN_REDUCTION.md`, every `A`-vertex has positive degree slack `e_x>=1`. Equation (5.1) therefore says every `A`-vertex already carries at least one free incidence. The remaining difficulty is entirely on the `B`-source side: too many free incidences may concentrate on too few sources.

The published order-12/size-32 hostile control and the independent `X_3` reconstruction are unaffected. Their canonical maximum root has `Q=12`, not `Q=0`, so this theorem does not purport to exclude them.

The expanded-`C5` equality family is also consistent with the boundary. Its maximum-root `Q=0` profiles have

\[
\delta=b-1,
\]

so Section 4 is deliberately invoked only under the strict counterexample condition `delta<=b-2`.

---

## 11. Finite diagnostic

The companion checker `check_q0_critical_arm_orientation.py` performs exact graph-atlas regression through order 7. It verifies the exact defect identity, triangle-free-edge payment, critical-arm enumeration, A-arm payment, B-arm injectivity, free-incidence count, endpoint formula, and the saturated-cut lemmas whenever their hypotheses occur.

It also records two **diagnostic-only** observations, not promoted to theorem:

1. no atlas `Q=0` root admits a simultaneously saturated pair under a full B-arm choice;
2. no individually saturation-feasible source in the atlas has an internal edge in `F[S_u]`.

Those finite facts motivate the next attack but are not used as proof.

---

## Trust boundary

Everything through Lemma 8.1 is intended as a hand derivation from D2C criticality, maximum degree, and the exact `Q=0` ledger. It has not received external mathematical review or novelty review. The graph-atlas checks are regression evidence only.

**No eventual second-extremal theorem is claimed.**
