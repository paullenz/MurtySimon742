# Non-star one-defect switching class: exact orientation-code normal form and eventual exclusion

17 September 2026. Research directed by Paul Lenz; derivation and finite regression by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The active target is the sufficiently-large/eventual second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 Dailly--Foucaud--Hansberg Conjecture 3 is not assumed. The published order-12, size-32 D2C obstruction remains a mandatory hostile control.

This note continues `LEAF_RICH_SWITCHING_EXCLUSIONS.md`. That predecessor removes perfect-matching and full-star switched states from any above-`M(n)` full tight-antipode graph for sufficiently large fibre count. The next unresolved leaf-rich state is the non-star one-defect graph

\[
K_{1,k-3}\ \dot\cup\ K_2.
\]

Here the orientation-code graph can be determined exactly. It is the disjoint union of two cliques and three balanced double-stars. This proves the previously conjectured cover bound `tau(Omega_sigma)>=2k-2` with equality throughout this switching class. The same normal form then makes `F`-separation strong enough to exclude the entire class above `M(n)` for `k>=16`.

---

## 1. Full-tight setup

Assume a maximum-degree root `v` has a full tight-antipode cover

\[
B=P_1\dot\cup\cdots\dot\cup P_k,
\qquad |P_i|=2,
\qquad b=\Delta(G)=2k.
\]

Put

\[
A=V(G)\setminus N[v],\qquad a=|A|.
\]

Retain the exact full-tight identities

\[
Q=k(k-1),
\qquad
r=k(a-k+1),
\qquad
\delta=r-e(F).                                    \tag{1.1}
\]

Every `A`-vertex has exactly `k` neighbours in `B`, so

\[
d_F(x)\le k.                                      \tag{1.2}
\]

The preserved above-`M(n)` density window gives

\[
\boxed{a\le2k}.                                    \tag{1.3}
\]

Choose endpoint bits on the antipode fibres. For a Boolean code `c`, let `L_c` be the switched graph on `[k]`. The orientation-code graph `Omega_sigma` has one code vertex for every Boolean code and one edge for every physical rooted `B`-edge, joining its two possible orientation-witness codes. The distinct code support actually occurring in `A` is a vertex cover of `Omega_sigma`.

We assume the switching class contains a non-star one-defect state.

---

## 2. Gauge normal form

Gauge-switch so that the zero code itself gives the one-defect graph. Write

\[
[k]=\{a,b,c\}\dot\cup D,
\qquad |D|=k-3,
\]

and take the signing graph

\[
L_0=K_{1,k-3}\dot\cup K_2
\]

with edge set

\[
E(L_0)=\{ad:d\in D\}\cup\{bc\}.                   \tag{2.1}
\]

Thus `a` is the unique non-leaf vertex, the `D`-vertices are its star leaves, and `bc` is the isolated edge.

The two other one-defect states in this switching class are obtained by switching the cuts `{a,b}` and `{a,c}`. Their exceptional vertices are `b` and `c`, respectively. In code notation the six codes giving the three one-defect states are the complementary pairs

\[
z_a=\varnothing,\quad \bar z_a=[k],
\]

\[
z_b=[k]\setminus\{a,b\},\quad \bar z_b=\{a,b\},
\]

\[
z_c=[k]\setminus\{a,c\},\quad \bar z_c=\{a,c\}. \tag{2.2}
\]

For each `d in D`, define the near-star code

\[
x_d=\{a,d\},
\qquad
\bar x_d=[k]\setminus\{a,d\}.                     \tag{2.3}
\]

Switching by `x_d` gives a graph with exactly `k-4` leaves, namely `D\setminus\{d\}`. These codes will form the two clique components below.

---

## 3. Exact orientation-code decomposition

The forced orientation-witness formula from the full-tight Boolean normal form can be evaluated directly in the gauge (2.1). It is enough to use one of the two physical `B`-edges over each quotient pair; the other physical edge complements both endpoint codes.

The quotient pairs split into three types.

### 3.1 Pairs inside D

For distinct `d,e in D`, the two physical `B`-edges over `{d,e}` give the orientation-code edges

\[
x_dx_e
\qquad\text{and}\qquad
\bar x_d\bar x_e.                                  \tag{3.1}
\]

Therefore the `x_d` form a clique `K_{k-3}`, and their complements form a second disjoint clique `K_{k-3}`.

### 3.2 Pairs between {a,b,c} and D

For each `d in D`, the two physical edges over `{a,d}` attach one leaf to each of the complementary centres `z_a,\bar z_a`; similarly `{b,d}` attaches one leaf to each of `z_b,\bar z_b`, and `{c,d}` attaches one leaf to each of `z_c,\bar z_c`.

For a fixed letter, say `a`, the resulting component consists of

- centres `z_a,\bar z_a`;
- `k-3` pendant leaves at `z_a`;
- `k-3` pendant leaves at `\bar z_a`.

The same holds for `b` and `c`.

### 3.3 Pairs inside {a,b,c}

The two physical edges over `{b,c}` both join `z_a` to `\bar z_a`; the two physical edges over `{a,c}` both join `z_b` to `\bar z_b`; and the two physical edges over `{a,b}` both join `z_c` to `\bar z_c`.

Thus each of the three components above is a balanced double-star whose central edge has multiplicity two in the physical-edge multigraph. Multiplicity is irrelevant for vertex cover, but is part of the exact rooted-edge accounting.

We obtain:

> **THEOREM 3.1 (non-star one-defect orientation-code normal form — internal candidate).**  
> If the Boolean switching class contains `K_{1,k-3} dotcup K_2` and `k>=5`, then after deleting isolated code vertices the orientation-code graph is
>
> \[
> \boxed{
> \Omega_\sigma
> \cong
> K_{k-3}\ \dot\cup\ K_{k-3}
> \ \dot\cup\ T_a\ \dot\cup\ T_b\ \dot\cup\ T_c,
> }
> \tag{3.2}
>
> where every `T_*` is the balanced double-star with two adjacent centres and `k-3` leaves on each centre. In the physical-edge multigraph, each central double-star edge has multiplicity two.

The physical-edge count checks exactly:

\[
2\binom{k-3}{2}
+3\bigl(2(k-3)+2\bigr)
=k(k-1),                                             \tag{3.3}
\]

where the final `+2` counts the doubled central physical edge in each double-star.

---

## 4. Exact vertex-cover number

A clique `K_{k-3}` has vertex-cover number `k-4`. A balanced double-star with `k-3>=2` leaves on each side has vertex-cover number exactly two: choosing the two centres covers every edge, while omitting either centre forces all `k-3` leaves on that side together with the opposite centre.

Hence Theorem 3.1 gives

\[
\tau(\Omega_\sigma)
=2(k-4)+3\cdot2
=\boxed{2k-2}.                                      \tag{4.1}
\]

Therefore every actual distinct witness-code support satisfies

\[
\boxed{|C|\ge2k-2}.                                 \tag{4.2}
\]

This proves the previously conjectured `2k-2` cover bound exactly for the complete non-star one-defect switching class.

Combining with (1.3), any above-`M(n)` graph in this class has

\[
2k-2\le |C|\le a\le2k.                              \tag{4.3}
\]

Equivalently, with

\[
\lambda=2k-a-1,
\]

only

\[
\boxed{\lambda\in\{1,0,-1\}}                       \tag{4.4}
\]

remain.

There is also useful near-minimum stability. For `k>=7`, replacing the two centres of one double-star by a cover omitting one centre costs at least `k-4>=3` extra code vertices. Since an above-threshold graph has at most two vertices beyond the minimum `2k-2`, every one of the six centre codes in (2.2) is forced into `C`. Each clique contributes at least `k-4` of its `k-3` vertices, so at most one `x_d` and at most one `\bar x_d` can be absent.

---

## 5. F-separation on the two large clique layers

The two clique layers in (3.2) give a large clean subsystem on which the selected-incidence separation rule is nearly identical to the already closed full-star branch.

Call a clique-code label **clean** if its code is one of the `x_d` or `\bar x_d` and occurs exactly once among the `A`-labels.

Let

\[
q=a-(2k-2)=1-\lambda\in\{0,1,2\}.                  \tag{5.1}
\]

Choose a minimum canonical core consisting of all six double-star centres and `k-4` vertices from each clique. There are only `q` labels beyond that core. If a core clique code is duplicated, mark every label in that duplicated class exceptional; if a label lies outside the chosen canonical clique core, mark it exceptional as well. The number of exceptional non-centre labels is at most `2q`.

Now put all six forced centre-code labels into the exceptional set too. Thus

\[
\boxed{|E|\le6+2q=8-2\lambda.}                     \tag{5.2}
\]

Every non-exceptional label is a clean singleton clique code.

### 5.1 Same clique means F-independent

For `d!=e`, the orientation-code graph contains the edge `x_dx_e`. Since both corresponding labels are singleton classes, the rooted `B`-edge represented by this `Omega` edge must be selected at one of those two labels. The source coordinate is one of `d,e`, and the codes differ at both coordinates. The F-separation rule therefore forbids an F-edge between the two labels.

Thus the clean `x_d` labels form an independent set in `F`. The same holds for the clean `\bar x_d` labels.

### 5.2 A clean cross-edge forces almost total residuality

Take clean labels of codes `x_d` and `\bar x_e`.

If `d=e`, the codes are complements and disagree at all `k` coordinates. An F-edge therefore forces every coordinate to be residual at both endpoints.

If `d!=e`, the codes agree exactly at coordinates `d,e`. The switched graph `L_{x_d}` has leaf set `D\setminus\{d\}`. Hence among the two agreement coordinates only `e` can possibly be selected at the `x_d` endpoint. Therefore an F-edge forces its selected cross-degree to be at most one, i.e.

\[
R_x\ge k-1.
\]

Symmetrically the `\bar x_e` endpoint also has residual degree at least `k-1`.

Consequently every clean-clean F-edge is a cross-clique edge whose two endpoints both satisfy `R>=k-1`.

Let `h` be the number of clean labels with residual degree at least `k-1`. Since the total label residual degree is `r`,

\[
h(k-1)\le r.                                        \tag{5.3}
\]

The clean-clean part of `F` is bipartite between the two clique layers, so

\[
e_F(A\setminus E)
\le\left\lfloor\frac{h^2}{4}\right\rfloor.         \tag{5.4}
\]

All edges incident with `E` are charged conservatively using `d_F<=k`. Hence

> **Lemma 5.1 (non-star one-defect F bound).**
>
> \[
> \boxed{
> e(F)\le
> \left\lfloor\frac{h^2}{4}\right\rfloor
> +(8-2\lambda)k,
> \qquad
> h\le\left\lfloor\frac{r}{k-1}\right\rfloor.
> }
> \tag{5.5}

No attempt is made here to optimise the six centre labels; treating all of them at full `F`-degree makes the bound deliberately conservative and easy to audit.

---

## 6. Eventual exclusion of the non-star one-defect class

For the three possible imbalance values,

\[
a=2k-1-\lambda,
\qquad
r=k(k-\lambda),                                     \tag{6.1}
\]

and (5.3) gives

\[
h\le
\begin{cases}
k,&\lambda=1,\\
k+1,&\lambda=0,\\
k+2,&\lambda=-1.
\end{cases}                                         \tag{6.2}
\]

Therefore

\[
\delta=r-e(F)
\ge
\begin{cases}
 k(k-1)-\lfloor k^2/4\rfloor-6k,&\lambda=1,\\[2mm]
 k^2-\lfloor (k+1)^2/4\rfloor-8k,&\lambda=0,\\[2mm]
 k(k+1)-\lfloor (k+2)^2/4\rfloor-10k,&\lambda=-1.
\end{cases}                                         \tag{6.3}
\]

The defect needed for `m<=M(n)` is exactly

\[
D=b(n-b)-M(n)
=\begin{cases}
2k-2,&\lambda=1,\\
2k-1,&\lambda=0,\\
2k-1,&\lambda=-1.
\end{cases}                                         \tag{6.4}
\]

A direct parity check gives the closure thresholds

- `lambda=1`: (6.3) reaches (6.4) for every `k>=12`;
- `lambda=0`: closure for every `k>=14`;
- `lambda=-1`: closure for every `k>=16`.

Thus:

> **THEOREM 6.1 (non-star one-defect switching exclusion — internal candidate).**  
> Let a D2C graph admit a maximum-degree root with a full tight-antipode cover, with `b=2k`. If the associated Boolean switching class contains
>
> \[
> K_{1,k-3}\dot\cup K_2
> \]
>
> and `k>=16`, then
>
> \[
> \boxed{m\le M(n).}
> \]
>
> Therefore no above-`M(n)` counterexample in the full-tight branch can contain a non-star one-defect switched state once `k>=16`.

This is a full closure of the remaining one-defect switching class at sufficiently large fibre count.

---

## 7. Verification and trust boundary

Companion checker:

`check_nonstar_one_defect_switching_exclusion.py`.

Recorded summary:

`NONSTAR_ONE_DEFECT_SWITCHING_EXCLUSION_CHECK_SUMMARY.json`.

Finite regression checks:

- exact orientation-code construction for every `k=5,...,100`;
- in every case, after deleting isolated code vertices, exactly two `K_{k-3}` components and three balanced double-stars occur;
- exactly three simple central pairs have multiplicity two, accounting for the six physical `B`-edges among `{a,b,c}`;
- exact cover formula `tau(Omega_sigma)=2k-2` in every checked order;
- defect arithmetic through `k=5000`, reproducing the exact thresholds `12,14,16` for `lambda=1,0,-1`.

These computations are regression evidence only. The universal statements are the hand derivations above.

The mandatory order-12/32 negative control remains untouched: `X_3` has `k=4` and lies in the residual-zero perfect-matching/factorization mechanism, outside the range and switching type of Theorem 6.1.

No all-order second-extremal statement is claimed. External mathematical review and novelty assessment remain open.

---

## 8. Strategic consequence

The entire **one-defect switching regime** is now finite in the full-tight branch:

- full-star states are excluded above `M(n)` for `k>=8`;
- non-star one-defect `K_{1,k-3} dotcup K_2` states are excluded above `M(n)` for `k>=16`;
- perfect-matching states were already excluded for even `k>=8`.

Moreover the conjectured cover bound

\[
\tau(\Omega_\sigma)\ge2k-2
\]

is now proved with equality for both major one-defect normal forms: the full-star class and the non-star class treated here.

The next eventual-scale target should therefore move to switching classes in which **every switched state has at least two non-leaf coordinates**. The highest-value question is whether `tau(Omega_sigma)>=2k-2` holds universally once `k` is sufficiently large. A proof would force every above-threshold full-tight graph into the same three near-balanced layers `a>=2k-2`; failure should expose a new explicit switching obstruction worth classifying. Either outcome is structurally informative.
