# Universal selected/residual bridge for diameter-two-critical graphs

11 September 2026. Research directed by Paul Lenz; mathematical development and audit by ChatGPT/Geeps.

**Status: candidate hand mathematics. Independent expert review remains open.** This note consolidates the common graph-to-demand machinery used across the fixed-order programme into one parameterised statement. It is deliberately written before any finite LP or certificate layer.

## 1. Setup

Let `G` be a finite simple diameter-two edge-critical graph on `n` vertices. Put

```text
H = complement(G).
```

Choose a minimum-degree vertex `v` of `H`, and write

```text
a = d_H(v) = n-1-Delta(G),
A = N_H(v),                    |A|=a,
B = V(H) \ N_H[v],             |B|=b=Delta(G).
```

Thus

```text
n=a+b+1.
```

Let `C=H[A]`, let `F` be the complement of `C` on A, and write

```text
d_i=d_F(i)  (i in A).
```

For `m=e(G)` define the surplus

```text
t = m-b(n-b) = m-b(a+1).
```

The strongest consequences below that use residual activity assume `t>0`.

## 2. Quasi-edge representatives

Take a missing unordered pair `{u,w}` of `H[B]`. Adding `uw` to H corresponds to deleting the critical edge `uw` from G. In `H+uw`, a new adjacent total-dominating pair must appear.

That pair must use u or w because no other adjacency changes. It cannot be `{u,w}`, since both u and w miss v. Hence, after interchanging u and w if necessary, there is an existing cross-edge `ui`, with `i in A`, such that

```text
N_H(u) union N_H(i) = V(H) \ {w}.
```

Write

```text
ui -> w.
```

For every missing **unordered** pair of `H[B]`, choose exactly one such representative. Call the chosen A-B edges **selected** and all other existing A-B edges **residual**.

A selected edge determines both its B-source u and its unique exception w. Hence it recovers its indexing missing unordered B-pair. In particular:

1. two different missing unordered B-pairs cannot choose the same selected edge;
2. opposite orientations of one unordered pair cannot both be selected;
3. at one source, selected labels and supplements are distinct.

For `u in B` define

```text
rho_u = residual degree of u into A,
q_u   = selected outdegree of u,
p_u   = selected indegree of u as a supplement/exception.
```

For `i in A` define

```text
R_i = residual degree of i into B,
x_i = selected degree of i into B.
```

Finally put

```text
r = sum_{u in B} rho_u = sum_{i in A} R_i.
```

## 3. Exact ledger and demand

Selected cross-edges and existing edges of `H[B]` partition the unordered pairs of B. Direct edge counting therefore gives the exact identity

```text
e(F)=r+t,                                      (3.1)
sum_i d_i=2(r+t).                              (3.2)
```

Because v has minimum degree a in H, every `i in A` has `d_H(i)>=a`. Since

```text
d_H(i)=1+(a-1-d_i)+R_i+x_i,
```

we obtain

```text
x_i>=d_i-R_i.
```

Define

```text
s_i=max(0,d_i-R_i),
S=sum_i s_i.
```

Then

```text
x_i>=s_i,                                      (3.3)
S>=r+2t.                                       (3.4)
```

Thus a label of demand `s_i` genuinely requires at least `s_i` distinct selected source incidences.

## 4. Pointwise forcing from a selected edge

Fix a selected edge `ui->w`.

### 4.1 First residual injection

Let j be an F-neighbour of i. Since `{u,i}` dominates every vertex except w, `uj` is an H-edge.

If `uj` is residual, charge j to a residual slot at u. Otherwise write `uj->z`. Distinct selected labels at u have distinct supplements z. Since `ui->w` must dominate z and `uz` is missing, `iz` is an H-edge.

Moreover `iz` is residual: the endpoints i and z jointly miss the A-vertex j, whereas every selected A-B edge has its unique exception in B and therefore must dominate every A-vertex. Distinct j give distinct residual edges at label i. Hence

```text
d_i<=rho_u+R_i.                                (4.1)
```

Consequently every selected incidence satisfies

```text
s_i<=rho_u.                                    (4.2)
```

### 4.2 Second residual injection

For the same F-neighbour j, if `uj` is selected then `{u,j}` must dominate w. Since `uw` is missing, `jw` is an H-edge. It cannot be selected from source w, because j and w jointly miss the A-vertex i. Distinct j give distinct residual edges at w. Therefore

```text
d_i<=rho_u+rho_w.                              (4.3)
```

### 4.3 Source and supplement constraints

Every F-neighbour of i is a cross-neighbour of u. Source u has exactly `rho_u+q_u` cross-neighbours, one of which is i itself. Thus

```text
d_i<=rho_u+q_u-1.                             (4.4)
```

For every other selected `uj->z` at source u, the pair `{u,j}` must dominate w, so `jw` is an H-edge. The `q_u-1` other selected labels are distinct and all give cross-neighbours of w. Hence

```text
rho_w+q_w>=q_u-1.                             (4.5)
```

## 5. B-side degree identities and endpoint load

Every missing unordered B-pair incident with u is oriented exactly once, outward or inward. Hence

```text
q_u+p_u = missing degree of u in H[B].        (5.1)
```

Since

```text
d_H(u)=rho_u+(b-1)-(q_u+p_u)>=a,
```

we obtain

```text
p_u<=rho_u+(b-a-1),                           (5.2)
q_u+p_u<=b-1,                                 (5.3)
q_u+rho_u<=a.                                 (5.4)
```

For selected `ui->w`, label i is adjacent in B to:

- u;
- the `q_u-1` supplements of the other selected edges from u;
- the `p_u` sources of selected pairs oriented into u.

These vertices are distinct; a collision between the last two families would orient the same missing unordered B-pair both ways. Therefore

```text
R_i+x_i>=q_u+p_u.                             (5.5)
```

## 6. Residual activity for positive surplus

Assume `t>0`. Then

```text
rho_u>=1 for every u in B.                    (6.1)
```

Proof. Suppose `rho_u=0`. Put

```text
U=N_A(u),
T=A\U.
```

Every A-B edge incident with u is selected. There is no F-edge between U and T: if `i in U`, `j in T` and `ij in F`, the selected edge at ui would have to dominate j, forcing `uj in H`, contradiction.

Each F-edge inside U forces two distinct residual cross-edges through the supplements of its two endpoints. The forced edges are residual because their endpoints jointly miss an A-vertex.

Each F-edge inside T is a missing H-pair in A. Its quasi-edge auxiliary cannot be v or u. If its auxiliary lay in A, domination of u would force that auxiliary into U, while the quasi-edge exception in T would force a missing U-T edge, contradicting `F(U,T)=empty`. Hence the auxiliary lies in B. The resulting cross quasi-edge has its unique exception in A, so it cannot be one of the selected representatives (whose exception lies in B), and is therefore residual. Distinct F[T]-edges give distinct residual cross-edges.

The U-family and T-family are disjoint. Therefore

```text
r>=2e(F[U])+e(F[T])
 >=e(F[U])+e(F[T])
 =e(F)
 =r+t,
```

contradicting `t>0`. This proves (6.1), and therefore

```text
r>=b.                                          (6.2)
```

## 7. Charging inequality

Assume `t>0`. For every label i choose exactly `s_i` actual selected incidences, possible by (3.3). By (4.2), if source u is chosen for i then

```text
rho_u>=s_i.
```

A chosen source has `q_u>=1`, and (5.4) therefore gives `rho_u<=a-1`; all charging denominators below are positive.

Charge each chosen incidence from source u by

```text
(rho_u-1)/(a-rho_u).
```

Source u is used on at most `q_u<=a-rho_u` chosen incidences, so its total charge is at most `rho_u-1`. Summing over B gives total charge at most `r-b`.

The charge function is increasing for integer `1<=rho<a`. Thus a label of demand `s_i>0` receives at least

```text
s_i(s_i-1)/(a-s_i).
```

(The term is zero for `s_i=0`.) Hence

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i).             (7.1)
```

Combining (7.1) with `S>=r+2t` gives

```text
sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t.         (7.2)
```

## 8. Threshold-capacity inequality

Fix integer `h>=1`. Define

```text
I_h={i:s_i>=h},
W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h},
z_h=|Z_h|.
```

For each heavy label choose `s_i` actual selected incidences. By (4.2), all chosen sources lie in `Z_h`.

Let `ell_u` be the number of heavy selected incidences from source u and put

```text
J={u in Z_h:ell_u>h},
j=|J|.
```

Fix a heavy selected edge `ui->w` from `u in J`. Each of the other `ell_u-1>=h` heavy selected labels k at u forces an edge `kw`.

If none of these forced edges is selected from w, they are all residual and `rho_w>=h`. If at least one is selected from w, then its label k is heavy and (4.2) gives `rho_w>=s_k>=h`. Hence every supplement of a heavy arc from J lies in `Z_h`.

Selected-pair injectivity therefore bounds heavy arcs from J by the unordered B-pairs inside `Z_h` incident with J:

```text
j(z_h-j)+C(j,2)=j*z_h-j(j+1)/2.
```

Every source in `Z_h\J` contributes at most h heavy arcs. Thus

```text
W_h <= (z_h-j)h + j*z_h - j(j+1)/2.          (8.1)
```

If `W_h>0`, then at least one label needs h distinct sources in `Z_h`, so `z_h>=h`. Put `q=z_h-h`. Then

```text
[h*z_h+C(q,2)] - RHS(8.1)
  = (q-j)(q-j-1)/2
  >=0,                                         (8.2)
```

because `q-j` is an integer. Therefore

```text
W_h<=h*z_h+C(z_h-h,2),
```

or equivalently

```text
2W_h<=z_h^2-z_h+h(h+1).                       (8.3)
```

Useful consequences:

- if `H0=max_i s_i>0`, then `z_H0>=H0`;
- for `h>=2`, residual activity gives

```text
r>=b+z_h(h-1).                                (8.4)
```

Thus any independent upper bound `r<=r_max` yields

```text
z_h<=floor((r_max-b)/(h-1)).                  (8.5)
```

## 9. Isolated-C lemma

Assume `t>0` and `a>=2`. If `C=H[A]` has an isolated vertex x, then

```text
b<=a-1-t.                                     (9.1)
```

Proof. Put `X=A\{x}`. Since x is isolated in C,

```text
e(C)=e(C[X]).
```

From `e(C)+r=C(a,2)-t`, the number P0 of missing H-edges inside X is

```text
P0=C(a-1,2)-e(C[X])
   =r-(a-1-t).                                (9.2)
```

Each missing X-pair produces a cross quasi-edge with auxiliary in B and exception in A. It is therefore residual, and the unique exception makes these residual edges distinct. Let P be this family, so `|P|=P0`.

Let Z be the B-endpoints used by P. Every `z in Z` forces a further residual edge `xz` outside P. Every `z in B\Z` has some residual edge by residual activity, also outside P. These b extra edges are distinct because they have distinct B-endpoints. Hence

```text
r>=|P|+b.
```

Using (9.2) gives (9.1).

Consequently, whenever

```text
b>a-1-t,
```

we have

```text
delta(C)>=1,                                 (9.3)
d_i<=a-2,                                    (9.4)
e(C)>=ceil(a/2),                             (9.5)
r<=C(a,2)-t-ceil(a/2).                      (9.6)
```

## 10. Safe finite-relaxation interface

Any actual graph in the scope above induces integer data satisfying Sections 3--9. A finite verifier may therefore enumerate a **superset** of such data and reject every state using only necessary consequences.

Safe proof architecture:

```text
actual graph
 -> quasi-edge selected/residual construction
 -> exact ledger and demand
 -> pointwise selected-edge constraints
 -> residual activity (when t>0)
 -> charging / threshold capacity / isolated-C
 -> finite relaxation(s)
 -> exact terminal certificates.
```

A numerical or LP state is not itself a graph. Conversely, rejecting a relaxation is proof-relevant only if every graph maps into that relaxation and every pruning rule is necessary.

## 11. Specialisations used in the current fixed-order programme

### n=29, Delta=16

```text
a=12, b=16,
t=m-208.
```

The isolated-C consequence gives

```text
r<=66-t-6=60-t.
```

### n=30, Delta=16

```text
a=13, b=16,
t=m-224.
```

The isolated-C consequence gives

```text
r<=78-t-7=71-t.
```

Thus at `m=225,226` (`t=1,2`) respectively,

```text
r<=70,69.
```

## 12. Trust boundary

The highest-value independent attacks are:

1. the complement/quasi-edge construction;
2. uniqueness and injection of selected representatives;
3. the claim that forced cross-edges used in Sections 4, 6 and 9 are genuinely residual;
4. residual activity;
5. the charging source budget;
6. threshold-capacity supplement forcing and unordered-pair count;
7. isolated-C disjointness;
8. any later actual-graph-to-averaged-variable embedding.

This note intentionally does not claim that a downstream LP is exact or sufficient. It records only universal necessary consequences of an actual diameter-two edge-critical graph under the stated setup.
