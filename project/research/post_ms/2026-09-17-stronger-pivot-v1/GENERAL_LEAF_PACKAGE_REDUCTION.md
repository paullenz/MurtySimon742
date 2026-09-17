# General leaf-package reduction and the four-defect finite-width frontier

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal structural lemma; not promoted. External mathematical review open.**

This note extracts the part of the orientation-code graph which depends only on the leaf coordinates of a switched state.  The three-defect leaf-package formula was not special to three exceptional coordinates: once there are at least three exceptional coordinates, the same package decomposition is exact for every defect count.  The first application is a sharp finite-width reduction of the complete four-defect switching problem.

The active target remains the sufficiently-large/eventual second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The order-12/32 `X_3` obstruction is the separate `k=4` residual-zero perfect-matching mechanism and remains a mandatory negative control.

---

## 1. General switched-state notation

Let `L` be one switched graph on the `k` antipode fibres.  Suppose exactly `d>=3` coordinates are **non-leaves** (degree different from one).  Call this exceptional set

\[
E=\{e_1,\ldots,e_d\}.
\]

Every remaining coordinate is a leaf.  A leaf has a unique neighbour, so the leaves split canonically into

1. pendant groups `D_i` attached to `e_i`, with
   \[
   p_i=|D_i|;
   \]
2. isolated leaf-leaf `K_2` components.

Write

\[
S=\sum_{i=1}^d p_i,
\qquad
t=\#\{\text{isolated leaf pairs}\},
\qquad
g=|\{i:p_i>0\}|.
\]

Then

\[
\boxed{k=d+S+2t.} \tag{1.1}
\]

The graph induced on `E` is arbitrary subject only to the requirement that the coordinates in `E` really are non-leaves.  The calculation below does **not** depend on that exceptional-core graph.

---

## 2. Forced code of a leaf source

If `x` is a leaf with unique neighbour `p(x)`, the zero-state row of `x` contains a single one at `p(x)`.  The forced witness-code formula therefore gives, modulo complement, the projective code class

\[
\boxed{c(x\to q)=\{p(x),q\}.} \tag{2.1}
\]

Consequently a quotient pair of leaves `x,y` contributes an orientation-code edge

\[
\{p(x),y\}\;\{p(y),x\}, \tag{2.2}
\]

together with the complementary copy in the full code graph.

For `d>=3`, the code families arising from the distinct parent/target roles in (2.2) are disjoint except for the deliberate common code pair contributed by the internal edges of isolated leaf pairs.  This is the only collision needed below.

---

## 3. Exact pendant-group contribution

For leaves `x,y` in the same group `D_i`, equation (2.2) gives two complementary copies of a clique:

\[
2K_{p_i},
\]

with cover contribution

\[
2(p_i-1)_+.
\]

For `x in D_i`, `y in D_j`, `i!=j`, the package is

\[
2K_{p_i,p_j},
\]

with contribution

\[
2\min(p_i,p_j).
\]

Hence the exact pendant-pendant leaf package is

\[
\boxed{
B_d(p_1,\ldots,p_d)
 =2\sum_i(p_i-1)_+
 +2\sum_{i<j}\min(p_i,p_j).
} \tag{3.1}
\]

If the attachment counts are sorted

\[
p_{(1)}\le\cdots\le p_{(d)},
\]

then

\[
\boxed{
B_d
=2S-2g
 +2\sum_{i=1}^d(d-i)p_{(i)}.
} \tag{3.2}
\]

Indeed `sum_i(p_i-1)_+=S-g`, and in the sorted list `p_(i)` is the minimum in exactly `d-i` unordered pairs.

---

## 4. Exact isolated-pair contribution

Assume `t>=1`.

For one isolated leaf pair against one nonempty pendant group, the leaf-leaf quotient pairs give four complementary stars, contributing `4`.  Thus all such packages contribute

\[
4tg. \tag{4.1}
\]

Two distinct isolated leaf pairs contribute four disjoint `K_2` packages, hence

\[
4\binom t2=2t(t-1). \tag{4.2}
\]

Finally, the physical edges internal to all isolated pairs collapse to the same complementary code pair; their multiplicity does not change vertex-cover size.  This contributes

\[
1. \tag{4.3}
\]

Therefore the subgraph of `Omega_sigma` contributed by quotient pairs whose **two coordinates are leaves** has exact cover number

\[
\boxed{
L_d(\mathbf p,t)
=
B_d(\mathbf p)+4tg+2t(t-1)+1
\qquad(t>=1),
} \tag{4.4}
\]

and

\[
\boxed{L_d(\mathbf p,0)=B_d(\mathbf p).} \tag{4.5}
\]

Since this is a subgraph of the full orientation-code graph,

\[
\boxed{\tau(\Omega_\sigma)\ge L_d.} \tag{4.6}
\]

This is the reusable form of the leaf-package theorem.

---

## 5. Necessary density inequality

In the full tight-antipode branch, an above-`M(n)` graph satisfies

\[
a\le2k,
\]

while its distinct A-code support is a vertex cover of `Omega_sigma`.  Therefore every switched state occurring in an above-threshold graph must satisfy

\[
\boxed{L_d\le2k.} \tag{5.1}
\]

Substituting (1.1), (3.2), and (4.4) gives, for `t>=1`,

\[
\boxed{
2\sum_{i=1}^d(d-i)p_{(i)}
 +(4t-2)g
 +2t^2-6t+1-2d
\le0.
} \tag{5.2}
\]

For `t=0`, the condition is

\[
\boxed{
\sum_{i=1}^d(d-i)p_{(i)}\le d+g.
} \tag{5.3}
\]

Thus, for every fixed defect count `d`, all attachment counts except the largest are bounded independently of `k`.  The infinite switching problem collapses to finitely many narrow rays before the exceptional core is considered.

---

# 6. Four-defect corollary

Set `d=4` and write

\[
w\le x\le y\le z
\]

for the sorted attachment counts.  Then

\[
B_4=2S-2g+6w+4x+2y. \tag{6.1}
\]

### 6.1 No isolated leaf pairs

For `t=0`, condition (5.3) becomes

\[
\boxed{3w+2x+y\le4+g.} \tag{6.2}
\]

Apart from the fixed small `g=0` case, the only surviving rays are:

- `g=1`: `(0,0,0,z)` with `z` arbitrary;
- `g=2`: `(0,0,y,z)` with `1<=y<=6`;
- `g=3`: `(0,x,y,z)` with
  \[
  (x,y)\in\{(1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3)\};
  \]
- `g=4`: only
  \[
  (w,x,y)\in\{(1,1,1),(1,1,2),(1,1,3)\},
  \]
  with `z>=y` arbitrary.

### 6.2 One isolated leaf pair

For `t=1`, (5.2) becomes

\[
6w+4x+2y+2g\le11. \tag{6.3}
\]

Hence only

- `g=1`: `(0,0,0,z)`;
- `g=2`: `(0,0,y,z)` with `1<=y<=3`

can survive.

### 6.3 Two isolated leaf pairs

For `t=2`, (5.2) becomes

\[
6w+4x+2y+6g\le11. \tag{6.4}
\]

Thus only the lopsided ray

\[
(0,0,0,z)
\]

with `g=1` survives.

### 6.4 Three or more isolated pairs

For `t=3`, a nonempty pendant family would already contribute at least `10` on the left of (5.2), while the constant term is `-7`; hence `g>=1` is impossible.  The `g=0` case has the fixed order `k=10`.  For `t>=4` the left side is even larger.

Therefore every sufficiently-large four-defect switched state which can possibly occur above `M(n)` lies on the finite-width list in Sections 6.1--6.3.

---

## 7. Strategic consequence

The complete three-defect calculation no longer needs to be repeated from scratch at four defects.  The unbounded part of the four-defect parameter space is already removed by the leaf-only witness packages.

The highest-value next subproblem is the no-pair lopsided ray `(0,0,0,z)`: only the rooted exceptional four-vertex core remains to be classified.  There are finitely many rooted core types, so exact projective-code grouping can identify every low-cover normal form and then the established F-separation machinery can be applied only to those survivors.

The other bounded-width rays can be attacked afterwards with the same exceptional-core method.

---

## 8. Trust boundary

- Equations (3.1) and (4.4) are hand decompositions of the leaf-leaf orientation-code subgraph, not empirical fits.
- The theorem is asserted for `d>=3`; small `d=1,2` has accidental code collisions and is deliberately outside the statement.
- The four-defect ray list is a necessary support condition only.  It does not claim that any listed state is realizable in a D2C graph.
- The complete three-defect theorem remains separately auditable.
- The `k=4`, order-12/32 `X_3` negative control is outside this higher-defect regime and is unaffected.
- No all-order second-extremal theorem is claimed.
