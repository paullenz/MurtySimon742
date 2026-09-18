# Minimum-defect twin package collapses the large switching window

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal structural theorem candidate. The unbounded reductions are hand arguments. Small `d=7,8` boundary certificates are recorded separately and remain pending external review. No all-order D2C theorem is claimed.**

The active target is the sufficiently-large/eventual second-extremal diameter-2-critical problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The published order-12, size-32 graph is the separately certified `X_3` negative control at `k=4,r=0`; nothing below suppresses it.

## 1. Entry point: choose a minimum-defect switched state

Work in the preserved full tight-antipode Boolean branch. Let

\[
d=d_*:=\min_c\phi(c)
\]

and choose a switched graph `L` attaining `d`. It has

\[
\ell=k-d
\]

leaf coordinates.

The universal degree bound already excludes

\[
2d>k+1.
\]

Therefore the only unresolved minimum-defect range satisfies

\[
\boxed{\ell=k-d\ge d-1.} \tag{1}
\]

As in the general leaf-package theorem, the leaves of `L` decompose into:

- `g` nonempty pendant groups `P_1,...,P_g`, attached to distinct exceptional coordinates, with sizes `p_1,...,p_g>=1`;
- `t` isolated leaf-leaf `K_2` components.

Put

\[
S=\sum_{j=1}^g p_j,
\qquad
\ell=S+2t.
\]

Let `E` be the `d` exceptional coordinates, let `J` be the `g` pendant parents, and let

\[
Q=E\setminus J,
\qquad q=|Q|=d-g.
\]

The coordinates in `Q` carry no ordinary pendant leaves.

## 2. New twin-package lemma

Partition `Q` into classes

\[
T_1,\ldots,T_h
\]

according to equality of their open neighbourhoods in `L`:

\[
x\sim y\iff N_L(x)=N_L(y).
\]

Write `m_s=|T_s|`.

Because a coordinate in `Q` has no pendant leaf of its own, its degree in `L` is just its exceptional-core degree. Since it is exceptional, that degree is not one.

For each twin class `T_s`, the forced orientation-code formula produces the following mutually vertex-disjoint subgraphs of `Omega` in addition to the preserved leaf-only package.

### 2.1 Twin-class core cliques

Vertices in one open-neighbourhood twin class are pairwise nonadjacent. If their common neighbourhood is `N_s`, then pairs inside `T_s` generate two complementary cliques

\[
2K_{m_s},
\]

with cover contribution

\[
2(m_s-1). \tag{2}
\]

### 2.2 Twin class against an ordinary pendant group

For a pendant parent `j` and a leaf `lambda in P_j`, every `x in T_s` is nonadjacent to `lambda`. The two complementary code halves give

\[
2K_{m_s,p_j},
\]

with cover contribution

\[
2\min(m_s,p_j). \tag{3}
\]

### 2.3 Twin class against isolated leaf-pairs

For each of the `2t` leaves lying in isolated leaf-leaf pairs, the same calculation gives two complementary `K_{m_s,1}` stars. Their total contribution for one twin class is

\[
4t. \tag{4}
\]

### 2.4 Disjointness

These packages are vertex-disjoint from the existing leaf-only package and from one another.

The small-code forms are useful for checking this directly:

- pendant-star centres have form `{j,x}`;
- isolated-pair star centres have form `{mu,x}`, where `mu` is a leaf;
- star leaves have form `N_s triangle {lambda}`;
- twin-clique vertices have form `N_s triangle {x}`.

A collision between a star centre and a twin-clique vertex would force `|N_s|=1`, impossible for an exceptional zero-parent coordinate. Star leaves from different twin classes can coincide only when the neighbourhoods coincide. Twin-clique vertices from two distinct nontrivial open-twin classes cannot coincide: such an equality would make representatives adjacent true twins, contradicting the existence of a second member in either open-twin class. The remaining possible collisions are separated by their leaf coordinates. This is the same code-level disjointness mechanism used in the earlier leaf-package/residual split.

Therefore, if `L_d` denotes the exact leaf-only cover from the general leaf-package theorem,

\[
\boxed{
\tau(\Omega)\ge
L_d+
2\sum_{s=1}^h
\left[
(m_s-1)+\sum_{j=1}^g\min(m_s,p_j)+2t
\right].
} \tag{5}
\]

This is the new **twin-package lower bound**.

## 3. Every nonlopsided minimum-defect state is support-impossible for d >= 7

Assume (1).

### 3.1 At least two ordinary pendant groups: g >= 2

Write `p_j=1+a_j`. For every twin-class size `m<=q`,

\[
\sum_j a_j+2t
=\ell-g
\ge d-1-g=q-1\ge m-1.
\]

Hence

\[
\sum_j\min(m,p_j)+2t
=g+\sum_j\min(m-1,a_j)+2t
\ge g+m-1.
\]

So the bracket in (5) is at least

\[
2m+g-2. \tag{6}
\]

If `g=2`, summing (6) gives an additional twin-package contribution at least

\[
4q=4(d-2).
\]

The leaf package has

\[
B_d\ge2S-2
\]

before its positive isolated-pair correction. For `t=0`,

\[
L_d+4q-2k\ge2d-10>0
\]

for `d>=6`; for `t>=1` the isolated-pair terms make the margin still larger.

If `g>=3` and `q>0`, summing (6), using `h>=1`, gives at least

\[
4q+2(g-2)=4d-2g-4.
\]

Also

\[
B_d\ge2S+g^2-3g.
\]

At `t=0` the margin over `2k` is at least

\[
2d+g^2-5g-4,
\]

which is positive for `d>=7,g>=3`. The isolated-pair terms again only improve the margin. The case `q=0` is even easier directly from the leaf-only bound.

Thus

\[
\boxed{g\ge2\implies\tau(\Omega)>2k\quad(d\ge7).} \tag{7}
\]

### 3.2 One ordinary pendant group and at least one isolated pair

Let `g=1,t>=1`, so `q=d-1`. For every twin class,

\[
(m-1)+\min(m,p_1)+2t\ge m+2t,
\]

because `p_1>=1`. Hence the extra contribution in (5) is at least

\[
2q+4t.
\]

The leaf-only package is

\[
L_d=2p_1+2t^2+2t-1.
\]

Therefore

\[
L_d+(2q+4t)-2k
\ge2t^2+2t-3>0
\]

for every `t>=1`.

So

\[
\boxed{g=1,t\ge1\implies\tau(\Omega)>2k.} \tag{8}
\]

### 3.3 No ordinary pendant group

If `g=0`, all leaves lie in isolated pairs, so (1) gives `2t>=d-1`. The twin-package term is at least

\[
2d+4t-2,
\]

while the leaf-only package is `2t(t-1)+1`. Thus

\[
\tau(\Omega)-2k
\ge2t(t-1)-1>0
\]

in the present range (`d>=7` forces `t>=3`).

Hence

\[
\boxed{g=0\implies\tau(\Omega)>2k.} \tag{9}
\]

### 3.4 Consequence

Combining (7)--(9):

> **PURE-LOPSIDED REDUCTION.** If `d=d_*>=7` lies in the unresolved degree-bound window and `tau(Omega)<=2k`, then the minimum-defect switched state must have
>
> \[
> \boxed{t=0,\quad g=1.}
> \]
>
> In other words all `k-d` leaves are attached to one exceptional root.

This removes every multiparent and isolated-pair geometry at once, for arbitrary `d`.

## 4. Pure lopsided states: a uniform residual count

Now suppose all

\[
z=k-d
\]

leaves attach to one exceptional root `r`. Put

\[
Q=E\setminus\{r\},\qquad q=d-1.
\]

In the unresolved window,

\[
z\ge q. \tag{10}
\]

### 4.1 Leaf and Q-leaf packages cost 2k-4

The leaf-leaf pairs give two `K_z` cliques, contribution

\[
2(z-1).
\]

Partition `Q` into open-neighbourhood twin classes of sizes `m_s`. For each class, its edges to the `z` leaves give two `K_{m_s,z}`. By (10), `z>=m_s`, so these cost exactly `2m_s`. Summing gives

\[
2q.
\]

Thus these vertex-disjoint packages already force

\[
2(z-1)+2q
=2k-4. \tag{11}
\]

Only five more residual cover vertices are needed to force strict excess over `2k`.

### 4.2 Which Q-Q pairs are already absorbed by the star centres?

The exceptional-only star-centre codes are

\[
\{r,u\},\qquad u\in Q,
\]

and their complements.

For distinct `x,y in Q`, the directed exceptional code is

\[
N_L(x)\triangle\{y\}.
\]

Because `x` has no pendant leaves, this can equal a star centre only if

\[
N_L(x)=\{r,u,y\}.
\]

The alternative nonedge case would force degree one and is forbidden. Therefore a directed endpoint is absorbed by the star package exactly when:

- `x` is adjacent to `r`;
- `x` has exactly two neighbours in `Q`;
- `y` is one of those two neighbours.

Let `S_2` be the set of such `x`. In the graph induced by `Q`, every vertex of `S_2` has degree two. If `s=|S_2|`, the number `b` of unordered `Q`-pairs with at least one absorbed endpoint is

\[
b=2s-e_Q(S_2). \tag{12}
\]

For `q>=5`,

\[
\boxed{b\le2q-4.} \tag{13}
\]

Indeed, if `s<=q-2` this is immediate. If `s=q-1`, the single outside vertex can supply at most one of the two required neighbours of each `S_2` vertex, forcing enough edges inside `S_2`; if `s=q`, the induced graph is 2-regular and `b=q`.

Hence at least

\[
\binom q2-(2q-4)
=\frac{q^2-5q+8}{2} \tag{14}
\]

`Q-Q` pairs survive outside the packages in (11).

Each surviving pair gives two complementary orientation-code edges. In either complementary half, a fixed code can arise from at most one target `y` for each source `x`, so the residual maximum degree is at most `q`. Therefore

\[
\boxed{
\tau(R_Q)\ge
\left\lceil\frac{q^2-5q+8}{q}\right\rceil
=
\left\lceil q-5+\frac8q\right\rceil.
} \tag{15}
\]

For

\[
q\ge9\quad(d\ge10),
\]

the right side is at least five. Together with (11),

\[
\boxed{d_*\ge10\implies\tau(\Omega)>2k} \tag{16}
\]

throughout the previously unresolved minimum-defect window.

Combining with the elementary large-minimum-defect degree bound, (16) is unconditional for minimum defect at least ten: if `z<d-1`, the degree bound closes; if `z>=d-1`, the twin/lopsided argument closes.

## 5. d*=9 closes analytically too

For `d=9`, `q=8`. Use the full twin-class package from (5), not merely (11). Let `h` be the number of open-neighbourhood classes in `Q`.

In the pure lopsided state the package margin relative to `2k` is

\[
2(q-h-2). \tag{17}
\]

Thus `h<=5` is already strict.

If `h=6`, the package reaches `2k` exactly. The general bound (13) leaves at least 16 good quotient `Q-Q` edges; deleting at most three within-class edges still leaves a residual edge, giving strict excess.

If `h=7`, there is exactly one twin pair. The package is two below `2k`. At least 16 good quotient edges remain; after removing the one twin-pair edge, at least 15 remain. Quotient maximum degree is at most eight, so its cover number is at least two; the complementary half doubles this to at least four, more than the required three.

If `h=8`, all eight `Q`-neighbourhoods are distinct. Equality in (13), namely `b=12`, would require six vertices of `S_2` to be independent and adjacent to the same two outside vertices. Those six vertices would then all have neighbourhood `{r}` plus the same two `Q` vertices, contradicting `h=8`. Hence `b<=11`, so at least 17 quotient edges survive. Maximum degree eight gives quotient cover at least three, hence full residual cover at least six.

Therefore

\[
\boxed{d_*=9\implies\tau(\Omega)>2k.} \tag{18}
\]

No finite core enumeration is needed for `d=9`.

## 6. New global switching frontier

Before this note, the full-tight branch for `k>=19` had the minimum-defect window

\[
7\le d_*\le\left\lfloor\frac{k+1}{2}\right\rfloor.
\]

The twin-package theorem collapses every nonlopsided state in that entire interval. The lopsided residual count then closes `d_*>=10`, and the refinement above closes `d_*=9`.

Thus the only minimum-defect values not settled by hand structure at this point are

\[
\boxed{d_*\in\{7,8\}.} \tag{19}
\]

Both are finite exceptional-core problems. The `d=7` lopsided layer is independently closed by the companion rooted graph-atlas audit, leaving only the `d=8` all-distinct-neighbourhood boundary as the final finite switching certificate. That certificate is also recorded separately.

Once those two finite boundary audits are accepted internally, the entire full-tight Boolean switching branch is eliminated above `M(n)` for `k>=19`.

## 7. Trust boundary

The structural content through (18) is hand mathematics: forced-code packages, elementary inequalities, and a residual edge/degree count. The remaining `d=7,8` boundary checks are finite certificates rather than hand classifications and are intentionally kept separate.

This note concerns only the full tight-antipode Boolean branch. It does not yet close near-full, unmatched, or errorful antipodes. It does not assert the false 2019 all-order strengthening, and it leaves the certified `k=4` `X_3` graph untouched.
