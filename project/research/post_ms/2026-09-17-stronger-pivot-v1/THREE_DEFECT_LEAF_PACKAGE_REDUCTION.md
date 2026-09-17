# Three-defect leaf-package reduction

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal structural lemma; not promoted. External mathematical review open.**

This note isolates the part of the three-defect orientation-code graph that comes only from quotient pairs whose two coordinates are leaves in the chosen switched state. It gives an exact cover formula for that subgraph and converts the complete three-defect problem from an unbounded parameter family into a finite list of narrow one-parameter rays.

The live target remains the sufficiently-large/eventual second-extremal D2C problem around `M(n)=floor((n-1)^2/4)+1`. The order-12/32 obstruction remains a mandatory hostile control.

---

## 1. Three-defect state and notation

Let `a,b,c` be the three non-leaf exceptional coordinates. Every other coordinate is a leaf, hence is either

- in a pendant group `D_i` attached to exceptional coordinate `i in {a,b,c}`; or
- one endpoint of an isolated leaf-leaf `K_2`.

Write

\[
p_i=|D_i|,
\qquad
S=p_1+p_2+p_3,
\qquad
t=\text{number of isolated leaf-pairs}.
\]

Then

\[
k=3+S+2t. \tag{1.1}
\]

Let

\[
g=|\{i:p_i>0\}|,
\]

and write the attachment counts in nondecreasing order

\[
x\le y\le z.
\]

The graph induced by `a,b,c` is arbitrary, subject only to those coordinates really being non-leaves. Importantly, the leaf-leaf calculation below is independent of that exceptional-core graph.

---

## 2. Leaf-source code formula

For a source leaf `d` with unique neighbour `p(d)`, the zero-state row of `d` has a single 1 at `p(d)`. In the forced witness-code formula, modulo complement, the code class for the orientation `d -> q` is therefore represented by the two-set

\[
\boxed{\{p(d),q\}.} \tag{2.1}
\]

Thus a quotient pair of leaves `d,e` contributes, modulo complement, the edge

\[
\{p(d),e\}\;\{p(e),d\}. \tag{2.2}
\]

Formula (2.2) makes the complete leaf-leaf subgraph explicit without reference to the exceptional-core signing.

---

## 3. Pendant-pendant packages

### Same pendant group

For `d,e in D_i`, (2.2) gives an edge between the vertices indexed by `d` and `e` in a clique. Including complementary codes, the package is

\[
2K_{p_i},
\]

with minimum-cover contribution

\[
2(p_i-1)_+.
\]

### Two different pendant groups

For `d in D_i`, `e in D_j`, `i!=j`, the package is

\[
2K_{p_i,p_j},
\]

with contribution

\[
2\min(p_i,p_j).
\]

All these leaf-source code families are disjoint for distinct ordered parent/target roles. Hence the exact pendant-pendant contribution is

\[
\boxed{
B(p_1,p_2,p_3)
=2\sum_i(p_i-1)_+
 +2\sum_{i<j}\min(p_i,p_j).
} \tag{3.1}
\]

Equivalently, with `x<=y<=z` and `g` positive attachment groups,

\[
\boxed{B=2S-2g+4x+2y.} \tag{3.2}
\]

---

## 4. Packages involving isolated leaf-pairs

Assume `t>=1`.

### One isolated pair against one pendant group

For each isolated pair and each nonempty `D_i`, the leaf-leaf quotient pairs give four complementary stars

\[
4K_{1,p_i}.
\]

Their cover contribution is `4`, independent of `p_i`. Across all isolated pairs and nonempty pendant groups this contributes

\[
4tg. \tag{4.1}
\]

### Two distinct isolated pairs

For each unordered pair of isolated `K_2` components, the four cross-pairs give four disjoint `K_2` components in the full orientation-code graph. This contributes

\[
4\binom{t}{2}=2t(t-1). \tag{4.2}
\]

### The internal edges of the isolated pairs

The quotient edges internal to all `t` isolated pairs collapse to the same complementary code pair. In the simple orientation-code graph this is one `K_2` (with physical multiplicity `2t`), hence contributes exactly

\[
1. \tag{4.3}
\]

Combining (3.1) and (4.1)--(4.3), the leaf-leaf subgraph has exact minimum cover

\[
\boxed{
L(p_1,p_2,p_3,t)
=
B(p_1,p_2,p_3)
+4tg+2t(t-1)+1
\qquad(t>=1).
} \tag{4.4}
\]

For `t=0`, of course,

\[
\boxed{L=B.} \tag{4.5}
\]

Since this is a subgraph of the full orientation-code graph,

\[
\boxed{\tau(\Omega_\sigma)\ge L.} \tag{4.6}
\]

This is a hand structural inequality, not an empirical fit.

---

## 5. Consequence of the density window `a<=2k`

Any above-`M(n)` full-tight graph has `a<=2k`, while its distinct A-code support is a vertex cover of `Omega_sigma`. Therefore a necessary condition for a three-defect switched state to occur above threshold is

\[
L\le2k. \tag{5.1}
\]

This already collapses the infinite parameter family.

### 5.1 No isolated leaf-pairs: `t=0`

Using (3.2) and `2k=6+2S`, condition (5.1) becomes

\[
4x+2y-2g-6\le0. \tag{5.2}
\]

Apart from the fixed tiny case `g=0,S=0,k=3`, only the following attachment patterns can survive the leaf-package test:

1. `g=1`: the lopsided ray `(0,0,z)`;
2. `g=2`: `(0,y,z)` with
   \[
   1\le y\le5;
   \]
3. `g=3`: only
   \[
   (x,y)\in\{(1,1),(1,2),(1,3),(1,4),(2,2)\},
   \]
   with the largest attachment `z` arbitrary subject to `z>=y`.

Thus every other nontrivial `t=0` three-defect state already satisfies `tau(Omega)>2k` before the exceptional-core edges are used.

### 5.2 At least one isolated leaf-pair: `t>=1`

From (3.2), (4.4), and (1.1),

\[
L-2k
=
(4t-2)g+4x+2y+2t^2-6t-5. \tag{5.3}
\]

Therefore `L<=2k` permits only:

- `t=1`: `g=0`, or `g=1`, or `g=2` with the smaller positive attachment at most `2`;
- `t=2`: only `g=0` or `g=1`;
- `t=3`: only `g=0`;
- `t>=4`: impossible from the leaf package alone.

For the eventual problem the `g=0` cases are fixed small orders (`k=5,7,9` for `t=1,2,3` respectively). Hence every sufficiently-large three-defect state with isolated leaf-pairs is reduced to

- `t=1`, one nonempty pendant group;
- `t=1`, two nonempty pendant groups with smaller size `1` or `2`;
- `t=2`, one nonempty pendant group.

This is a finite-width list of rays, not an arbitrary three-defect family.

---

## 6. Interaction with the two newly closed low-cover rays

For `t=0,g=1`, validity of the two zero-attachment exceptional coordinates leaves only two exceptional cores:

- the empty exceptional core, giving the empty-core star state with `tau=2k`;
- the triangle exceptional core, giving the triangle-star state with `tau=2k-1`.

The empty-core star is excluded above `M(n)` for `k>=14`; the triangle-star is excluded for `k>=15`. Hence

> **LOPSIDED NO-PAIR THREE-DEFECT RAY CLOSED — internal consequence.**  
> For `k>=15`, no above-`M(n)` full-tight graph can contain a `t=0,g=1` three-defect switched state.

The remaining complete-three-defect problem is therefore concentrated in the narrow rays listed in Section 5, together with closing the isolated-pair rays.

---

## 7. Why this is the next useful structural reduction

The previous strategy was to enumerate all attachment triples, pair counts, and 3-vertex exceptional cores. Formula (4.4) shows that most of that parameter space is irrelevant to an above-threshold graph: the leaf-leaf witness packages alone already demand more than `2k` distinct codes.

The next compact target is now finite-width:

1. close the surviving isolated-pair rays from Section 5.2 by adding a small exceptional-core matching/cover certificate;
2. for `t=0`, analyse only the bounded minor attachment values in Section 5.1;
3. combine those finite core certificates with the already closed lopsided empty-core and triangle-core rays.

This is more likely to yield a short externally reviewable complete three-defect theorem than a raw parameter-by-parameter census.

---

## 8. Trust boundary

- Formulae (3.1) and (4.4) concern only the leaf-leaf subgraph and are exact hand decompositions.
- They give a lower bound on the full `tau(Omega_sigma)`; no claim is made here that they determine the full cover number.
- The remaining narrow rays are not declared closed except where an independent structural theorem is already cited above.
- The fixed `g=0,t=0,k=3` case is explicitly outside the eventual argument.
- The order-12/32 hostile control lies in the residual-zero perfect-matching mechanism and is unaffected.