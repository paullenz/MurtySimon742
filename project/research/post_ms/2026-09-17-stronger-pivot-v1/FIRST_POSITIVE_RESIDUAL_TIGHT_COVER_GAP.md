# First positive-residual full-tight covers: a Boolean code-cover gap

17 September 2026. Research directed by Paul Lenz; derivation and finite regression by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The active target remains the sufficiently-large/eventual second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 strengthening is not assumed. The order-12, size-32 obstruction remains a mandatory negative control.

This note continues `ZERO_RESIDUAL_TIGHT_COVER_CLASSIFICATION.md`. That predecessor classifies the exact `r=0` full-tight Boolean boundary: apart from the six-vertex `H5` mechanism, the only nontrivial case is the `k=4` twelve-vertex `X_3` cube mechanism. The question here is whether the first positive residual layer

\[
a=k,\qquad r=k
\]

can occur for larger fibre count. It cannot. In fact the proof gives a purely switching-theoretic statement: for `k>=5`, any set of Boolean witness codes covering all rooted B-edges has at least `k+1` distinct codes.

---

## 1. Full-tight Boolean normal form

Assume the tight antipodes at a maximum-degree root `v` cover

\[
B=N_G(v)=P_1\dot\cup\cdots\dot\cup P_k,
\qquad |P_i|=2,
\qquad b=2k.
\]

Choose endpoint bits on every fibre. The B-layer is a 2-lift of `K_k` with signs `sigma_ij`, and every `A`-vertex `x` has a code

\[
c(x)=(c_1(x),\ldots,c_k(x))\in\{0,1\}^k.
\]

The exact full-cover identities are

\[
Q=e(G[B])=k(k-1),
\qquad
r=k(a-k+1).                                           \tag{1.1}
\]

For a code `c`, define its switched defect graph `L_c` on `[k]` by

\[
ij\in E(L_c)
\quad\Longleftrightarrow\quad
\sigma_{ij}\oplus c_i\oplus c_j=1.                 \tag{1.2}
\]

Let

\[
\ell(c)=\#\{j:d_{L_c}(j)=1\},
\qquad
\phi(c)=k-\ell(c).                                   \tag{1.3}
\]

Thus `phi(c)` is the number of non-leaf fibre coordinates in the switched graph.

---

## 2. Selected incidences are leaf incidences

Fix a label `x` of code `c` and a fibre `j`. The unique H-cross neighbour of `x` in `P_j` is

\[
q_j=(j,1-c_j).
\]

Suppose `q_jx` is selected and has B-exception in fibre `i`. The same direct 2-lift calculation used at residual zero gives:

- `ij in E(L_c)`;
- every other fibre coordinate `h!=i,j` is **not** adjacent to `j` in `L_c`.

Hence

\[
d_{L_c}(j)=1.                                       \tag{2.1}
\]

So every selected H-cross incidence uses a leaf coordinate of `L_c`.

There is an additional point which matters once code multiplicities are allowed. For fixed code `c` and fixed leaf coordinate `j`, the source `q_j` and the unique neighbour `i` of `j` in `L_c` determine one specific rooted B-edge. Therefore two different A-labels with the same code cannot both use that same leaf incidence: selected representatives are in bijection with rooted B-edges.

Consequently, if `C` is the **set of distinct A-codes**, the total number of selected incidences satisfies

\[
Q\le\sum_{c\in C}\ell(c).                            \tag{2.2}
\]

Equivalently,

\[
\sum_{c\in C}\phi(c)
\le k|C|-k(k-1).                                      \tag{2.3}
\]

This is stronger than summing the per-label leaf-deficiency inequality: duplicate labels do not create duplicate selected capacity.

### Orientation-code graph interpretation

Each physical B-edge has exactly two possible Boolean witness codes, one for each orientation. Form a graph `Omega_sigma` whose vertices are codes and whose edge corresponding to a physical B-edge joins those two orientation codes. Then `C` must be a vertex cover of `Omega_sigma`, and

\[
d_{Omega_sigma}(c)=\ell(c)
\]

(counting parallel physical edges where appropriate). The theorem below is therefore a lower bound on this witness-code cover number.

---

## 3. Two elementary switching lemmas

For codes `c,d`, let

\[
S=\{i:c_i\ne d_i\}.
\]

Then

\[
E(L_c)\triangle E(L_d)=\delta(S),                    \tag{3.1}
\]

the complete cut between `S` and its complement.

### 3.1 Switching away from a perfect matching

Assume `k>=6` is even and `L_c` is a perfect matching. If `L_d` is a genuinely different switched graph, then

\[
\boxed{\phi(d)\ge k-2.}                              \tag{3.2}
\]

Indeed, a vertex is a leaf in both graphs only if the incidence sets of its unique edges differ by `0` or `2` edges. Thus its degree in the cut `delta(S)` is `0` or `2`.

For a nontrivial cut, the cut degrees are `|S|` and `k-|S|`. Unless one side has size `2`, no vertex can remain a leaf. If, say, `|S|=2`, only vertices outside `S` can possibly remain leaves. Such a vertex remains a leaf only when its perfect-matching mate lies in `S`; there are at most two such vertices. Hence `ell(d)<=2`, proving (3.2). The complementary case is identical.

### 3.2 Two one-defect switching states

Call a switched graph **one-defect** when

\[
\phi=1,
\]

i.e. exactly one fibre coordinate is not a leaf.

Let `L,L'` be distinct one-defect switched graphs for `k>=5`, with exceptional vertices `a,b` respectively. Then `a!=b`, and the switching cut is exactly

\[
\delta(\{a,b\})                                      \tag{3.3}
\]

(up to taking the complementary side of the same cut).

To see this, the other `k-2` vertices are leaves in both graphs. Every such common leaf must have cut degree `2`; a nontrivial complete cut can give all `k-2` of them degree two only when its small side is exactly `{a,b}`.

Now inspect `L`. Every common leaf is adjacent to exactly one of `a,b`.

- If `ab in E(L)`, then `b`, being a leaf in `L`, has no other neighbour, so every common leaf is adjacent to `a`. Thus `L` is the full star centred at `a`.
- If `ab notin E(L)`, then `b` has exactly one common-leaf neighbour `c`; all other `k-3` common leaves are adjacent to `a`. Thus

\[
L=K_{1,k-3}\ \dot\cup\ K_2,                         \tag{3.4}
\]

with star centre `a` and isolated edge `bc`.

So two distinct one-defect states are related in only these two ways.

---

## 4. No `k` Boolean codes can cover all rooted B-edges when `k>=5`

Let `C` be a set of distinct codes which covers all rooted B-edges. We prove

\[
\boxed{|C|\ge k+1\qquad(k\ge5).}                    \tag{4.1}
\]

Suppose instead `|C|<=k`.

From (2.2),

\[
k(k-1)\le\sum_{c\in C}\ell(c)\le k|C|.
\]

Therefore `|C|` is either `k-1` or `k`.

### Case A: `|C|=k-1`

Equality is forced throughout, so every code has `ell(c)=k`: every `L_c` is a perfect matching.

For odd `k` this is impossible. For even `k>=6`, two genuinely different perfect matchings cannot lie in one switching class: the symmetric difference of two perfect matchings has vertex degrees `0` or `2`, while a nontrivial complete cut has positive degrees `|S|` and `k-|S|`; both can equal two only at `k=4`. A fixed switched graph has only the two complementary codes `c,bar(c)`. Since `k-1>2`, the required `k-1` distinct codes cannot all represent one matching either.

Thus Case A is impossible.

### Case B: `|C|=k`

Equation (2.3) gives

\[
\sum_{c\in C}\phi(c)\le k.                          \tag{4.2}
\]

For odd `k`, no perfect matching exists, so every `phi(c)>=1`; hence every code has `phi(c)=1`.

For even `k>=6`, suppose some code gives a perfect matching. At most two codes (a complementary pair) give that same switched graph. Every other code is a nontrivial switch and costs at least `k-2` by (3.2). Even in the most optimistic case of two zero-cost complementary codes, the remaining `k-2` codes contribute at least

\[
(k-2)^2>k,
\]

contradicting (4.2). Hence again every code has

\[
\phi(c)=1.                                            \tag{4.3}
\]

So all `k` codes give one-defect switched graphs.

---

## 5. One-defect families cannot cover the physical B-edges

A switched graph has at most two codes, a complementary pair. Therefore `k` distinct codes produce at least

\[
\left\lceil\frac{k}{2}\right\rceil\ge3
\]

distinct one-defect switched graphs.

### 5.1 Star family

If one pair of distinct states is in the star alternative of Section 3.2, then comparing every other state with that star shows that all distinct states are full stars, with distinct centres.

A code whose switched graph is the star centred at `i` is compatible only with one physical B-edge over each quotient pair `{i,j}`. Its complementary code is compatible with the *other* physical edge over each such pair.

Let `T` be the set of star centres represented by the distinct states.

- If at least two fibre vertices lie outside `T`, the quotient edge between them has no compatible code at all.
- If exactly one vertex lies outside `T`, then for every centre `i` both complementary star codes at `i` are needed to cover the two physical edges over the pair joining `i` to that lone noncentre. This requires more than `k` codes.
- If `T=[k]`, there is exactly one code per centre. Give each chosen representative a sign according to which member of its complementary pair was chosen. For a pair of centres `i,j`, their two star codes cover the two distinct physical B-edges over `{i,j}` only when their signs are opposite. Thus all pairs of centres would have to receive opposite binary signs, impossible for `k>=3`.

So a star family cannot cover all rooted B-edges.

### 5.2 The non-star three-state family

If no pair is in the star alternative, fix a state with exceptional vertex `a`. By (3.4), it has exactly two vertices outside its star: the endpoints `b,c` of the isolated `K_2`. Any distinct one-defect partner must have exceptional vertex `b` or `c`. Hence there are at most three distinct states.

When there are three, after relabelling their forms are

\[
L_a=\{ad:d\in D\}\cup\{bc\},
\]
\[
L_b=\{bd:d\in D\}\cup\{ac\},
\]
\[
L_c=\{cd:d\in D\}\cup\{ab\},
\]

where

\[
D=[k]\setminus\{a,b,c\}.
\]

For `k>=5`, `|D|>=2`. No one of these three switched graphs contains an edge between two vertices of `D`, so no code in the family is compatible with either physical B-edge lying over such a quotient pair. Coverage again fails.

This contradicts the assumption `|C|<=k` and proves (4.1).

---

## 6. First positive-residual layer is impossible

Return to the full-tight D2C graph. Its A-labels supply a set `C` of distinct Boolean codes covering all rooted B-edges. Hence, for `k>=5`,

\[
a\ge |C|\ge k+1.                                    \tag{6.1}
\]

Using the exact residual formula (1.1),

\[
\boxed{r=k(a-k+1)\ge2k.}                             \tag{6.2}
\]

Thus:

> **FIRST POSITIVE-RESIDUAL GAP THEOREM — internal candidate.**  
> In a full tight-antipode cover with `k>=5`, neither `r=0` nor `r=k` can occur. More precisely,
>
> \[
> \boxed{a\ge k+1,\qquad r\ge2k.}
> \]
>
> The exact residual-zero exceptions remain the already isolated `k=2` (`H5`) and `k=4` (`X_3`) mechanisms.

The theorem is about the full tight-antipode normal form. It is not an eventual second-extremal theorem and says nothing by itself about unmatched/errorful antipodes.

---

## 7. Why this is useful

The zero-residual classification showed that the twelve-vertex Boolean/cube obstruction cannot simply continue to larger `k`. The present theorem adds a genuine **gap**: for every `k>=5`, the full-tight branch cannot even move one residual layer away from that boundary.

The residual values are discrete:

\[
r=k(a-k+1).
\]

The first algebraically possible positive layer would be `r=k`; the Boolean witness-cover theorem removes it. The next possible full-tight layer is therefore

\[
r\ge2k.
\]

The proof also supplies a reusable object, the orientation-code graph `Omega_sigma`. Future work can seek stronger universal lower bounds on its vertex-cover number. Finite experiments suggest the true bound is often substantially larger than `k+1`; no stronger universal claim is made here.

The next bounded target should be the `a=k+1`, `r=2k` layer, coupling code-cover slack with the F-separation rule. For a selected coordinate `j` at label `x`, every F-neighbour of `x` agrees with `x` in coordinate `j`; hence an F-edge may differ only on residual coordinates at both endpoints. That should price `e(F)` rather than residual mass alone and is the natural bridge to the required defect `delta=r-e(F)`.
