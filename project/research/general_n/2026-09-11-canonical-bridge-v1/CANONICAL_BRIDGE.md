# Canonical parameterized selected/residual bridge

11 September 2026. Research directed by Paul Lenz; mathematical development and hostile consolidation by ChatGPT/Geeps.

**Status: candidate universal lemma package. Independent expert review remains OPEN.** This note consolidates the common graph-to-demand machinery used throughout the fixed-order programme into one parameterized proof. It is not a proof of the unrestricted Murty-Simon conjecture and does not silently replace the historical fixed-order proofs; it is a canonical review surface intended to reduce duplicated hand arguments.

## 1. Setup

Let `G` be a finite simple diameter-two edge-critical graph on `n` vertices. Put

```text
H = complement(G).
```

Choose a minimum-degree vertex `v` of H and write

```text
A = N_H(v),
a = |A| = delta(H) = n-1-Delta(G),
B = V(H) \ N_H[v],
b = |B| = Delta(G).
```

Thus

```text
n=a+b+1.
```

Let

```text
C=H[A],
F=complement(C) on A.
```

For `i in A`, let `d_i=d_F(i)`.

Write `m=e(G)` and define the surplus over the complete bipartite benchmark determined by B as

```text
t = m-b(n-b) = m-b(a+1).
```

The strongest conclusions below assume `t>0`. The quasi-edge construction and exact ledger do not.

## 2. Complement form of diameter-two edge-criticality

Take an edge `uw` of G, equivalently a missing pair `uw` of H. Deleting `uw` from G is the same as adding `uw` to H.

Because G is diameter-two edge-critical, in `G-uw` some pair `x,y` has distance greater than two. Equivalently, in `H+uw`, the pair `x,y` is adjacent and its open neighbourhoods together contain every vertex: it is an adjacent total-dominating pair.

No adjacent total-dominating pair existed already in H, because that would correspond to a pair at distance greater than two in G. Hence the newly total-dominating pair must use `u` or `w`, the only vertices whose H-neighbourhoods changed.

Now suppose `u,w in B`. The new total-dominating pair cannot be `{u,w}`, because both miss `v`. Hence, after interchanging u and w if necessary, there is an existing cross-edge `ui` with `i in A` such that

```text
N_H(u) union N_H(i) = V(H) \ {w}.        (2.1)
```

Write

```text
ui -> w.
```

The vertex w is the unique exception of the adjacent pair `{u,i}` in H.

## 3. One selected representative per missing unordered B-pair

For every missing **unordered** pair `{u,w}` of `H[B]`, choose exactly one cross-edge supplied by Section 2, after orienting the pair if necessary.

Call these chosen A-B edges **selected**. Call every other existing A-B edge **residual**.

A selected edge `ui->w` determines:

- its B-source u;
- its A-label i;
- its unique B-exception w.

Therefore the selected cross-edge recovers the missing unordered B-pair `{u,w}`. Consequently:

1. distinct missing unordered B-pairs cannot choose the same selected cross-edge;
2. the two orientations of one missing B-pair cannot both be selected;
3. at a fixed source u, selected labels are distinct and their supplements/exceptions are distinct.

For `u in B` define

```text
rho_u = residual degree of u into A,
q_u   = number of selected edges with source u,
p_u   = number of selected missing B-pairs whose exception is u.
```

For `i in A` define

```text
R_i = residual degree of i into B,
x_i = selected degree of i into B.
```

Let

```text
r = sum_{u in B} rho_u = sum_{i in A} R_i.
```

## 4. Exact ledger

Every unordered pair of B is exactly one of:

- an edge of `H[B]`; or
- a missing pair of `H[B]`, carrying exactly one selected representative.

Hence

```text
#selected cross-edges + e(H[B]) = C(b,2).  (4.1)
```

Also

```text
e(H)=C(n,2)-m
    = a + e(C) + r + #selected + e(H[B]).
```

Using (4.1), `n=a+b+1`, and `t=m-b(a+1)`, this rearranges exactly to

```text
e(C)+r = C(a,2)-t.                         (4.2)
```

Since F is the complement of C on A,

```text
e(F)=r+t,                                  (4.3)
sum_i d_i = 2(r+t).                        (4.4)
```

No inequality has been used here.

## 5. Label demand

Because v has minimum H-degree a, every `i in A` satisfies `d_H(i)>=a`. Its H-neighbours consist of:

- v;
- `a-1-d_i` neighbours inside A;
- `R_i+x_i` neighbours in B.

Thus

```text
1+(a-1-d_i)+R_i+x_i >= a,
```

so

```text
x_i >= d_i-R_i.
```

Define

```text
s_i=max(0,d_i-R_i),
S=sum_i s_i.
```

Then

```text
x_i>=s_i.                                  (5.1)
```

Summing the weaker inequalities `s_i>=d_i-R_i` and using (4.4) gives

```text
S >= 2(r+t)-r = r+2t.                      (5.2)
```

A positive demand `s_i` therefore corresponds to at least `s_i` distinct selected A-B incidences, hence `s_i` distinct B-sources.

## 6. Pointwise forcing from a selected edge

Fix a selected edge

```text
ui -> w.
```

### 6.1 Label residual forcing

Let j be an F-neighbour of i, so `ij` is absent from H[A]. Since j is an A-vertex and w is the unique exception in (2.1), `uj` must be an H-edge.

If `uj` is residual, charge j to a residual source incidence at u.

Otherwise `uj` is selected, say `uj->z`. The supplement z differs from w because the missing unordered pair `{u,w}` already has its unique selected orientation. Since `ui->w` must dominate z and `uz` is missing in H[B], `iz` is an H-edge.

Moreover `iz` is residual. Indeed, `ij` is absent, and because z is the exception of `uj->z`, `jz` is absent. Thus both endpoints of `iz` miss the A-vertex j. A selected A-B edge has its unique exception in B and must dominate every A-vertex, so `iz` cannot be selected.

Distinct selected j at u have distinct supplements z. Therefore the F-neighbours of i inject into at most `rho_u` residual source incidences and `R_i` residual label incidences:

```text
d_i <= rho_u+R_i.                          (6.1)
```

In particular, at every selected incidence of label i,

```text
s_i <= rho_u.                              (6.2)
```

### 6.2 Supplement residual forcing

For the same F-neighbour j, again `uj` is an H-edge. If it is residual, charge it at u. Otherwise write `uj->z`.

The supplements z and w are distinct. The selected pair `{u,j}` must therefore dominate w. Since `uw` is missing, `jw` is an H-edge.

This edge is residual: `ij` is absent and `iw` is absent because w is the exception of `ui->w`, so both endpoints j and w miss the A-vertex i. Distinct j give distinct residual edges at w. Hence

```text
d_i <= rho_u+rho_w.                        (6.3)
```

### 6.3 Source selected-degree forcing

Every F-neighbour j of i is a cross-neighbour of u. Source u has exactly `rho_u+q_u` A-neighbours, one of which is i. Therefore

```text
d_i <= rho_u+q_u-1.                       (6.4)
```

### 6.4 Supplement forcing

For every other selected edge `uj->z` at u, its exception z differs from w. Thus `{u,j}` must dominate w. Since `uw` is missing, `jw` is an H-edge.

The `q_u-1` other selected labels j are distinct. They therefore give `q_u-1` distinct A-neighbours of w, each either residual or selected from source w. Hence

```text
rho_w+q_w >= q_u-1.                       (6.5)
```

## 7. Exact missing degree in B and source capacities

Every missing unordered B-pair incident with u is selected in exactly one orientation: outward from u or inward to u. Therefore

```text
q_u+p_u = missing degree of u in H[B].    (7.1)
```

The H-degree of u is

```text
d_H(u)
 = (rho_u+q_u) + [(b-1)-(q_u+p_u)]
 = rho_u+b-1-p_u.
```

Minimum H-degree gives

```text
p_u <= rho_u+b-a-1.                       (7.2)
```

Also

```text
q_u+p_u <= b-1,                           (7.3)
q_u+rho_u <= a.                           (7.4)
```

Equation (7.4) is simply the A-side capacity at source u.

## 8. Endpoint load

Again fix `ui->w`.

The following are distinct B-neighbours of label i:

1. u itself;
2. the `q_u-1` supplements of the other selected edges from source u;
3. the `p_u` sources of selected missing B-pairs oriented into u.

For family 2, if `uj->z` is another selected edge at u, then z differs from w and `ui->w` must dominate z; because `uz` is missing, `iz` is an H-edge.

For family 3, let a missing pair be oriented `y->u`. The source y cannot equal w, because `ui->w` already orients the missing pair `{u,w}` as `u->w`. Since `uy` is missing and `ui->w` dominates y, `iy` is an H-edge.

Families 2 and 3 cannot collide: a collision would orient the same missing unordered pair `{u,z}` both as `u->z` and `z->u`.

Therefore label i has at least

```text
1+(q_u-1)+p_u=q_u+p_u
```

B-neighbours, giving

```text
R_i+x_i >= q_u+p_u.                       (8.1)
```

## 9. Residual activity for positive surplus

Assume from now on

```text
t>0.
```

We prove

```text
rho_u>=1 for every u in B.                (9.1)
```

Suppose instead `rho_u=0`. Put

```text
U=N_A(u),
T=A\U.
```

Every A-B edge incident with u is selected.

There is no F-edge between U and T. Indeed, if `i in U`, `j in T`, and `ij in F`, then the selected edge at `ui` has its unique exception in B and must dominate j. Since `ij` is absent, this forces `uj` in H, contradicting `j in T`.

Now count residual cross-edges forced by F.

Take an F-edge `ij` inside U. The selected edges from u to i and j have distinct supplements, say `ui->w_i` and `uj->w_j`. Because `w_i!=w_j`, the selected pair `{u,j}` must dominate `w_i`; since `uw_i` is missing, `jw_i` is an H-edge. Similarly `iw_j` is an H-edge. Both are residual: `jw_i` has endpoints that jointly miss the A-vertex i, and `iw_j` has endpoints that jointly miss j. Distinct ordered F-edge endpoints give distinct residual cross-edges. Thus F[U] forces `2e(F[U])` residual edges with A-endpoint in U.

Now take an F-edge `ij` inside T. Adding ij to H creates a new adjacent total-dominating pair using i or j. It cannot be `{i,j}` because both miss u. Its auxiliary cannot be v: v already neighbours both i and j, so adding ij cannot repair a failure at the opposite endpoint. It cannot be u because u is adjacent to neither endpoint.

If the auxiliary z lay in A, domination of u would force `z in U`. But the unique exception before adding ij is the other endpoint in T, so z would miss that T-vertex, creating an F-edge between U and T, impossible. Hence the auxiliary lies in B.

The resulting cross quasi-edge has its unique exception in A. Selected representatives have their unique exception in B, so this cross-edge is residual. The cross-edge together with its unique A-exception recovers the original F[T]-edge, giving an injection from F[T] to residual edges with A-endpoint in T.

The U- and T-families are disjoint. Therefore

```text
r >= 2e(F[U])+e(F[T])
  >= e(F[U])+e(F[T])
  = e(F)
  = r+t,
```

contradicting `t>0`.

Thus (9.1) holds, and

```text
r>=b.                                      (9.2)
```

## 10. Charging inequality

For every label i choose exactly `s_i` of its selected incidences, possible by (5.1).

If source u is chosen for label i, (6.2) gives

```text
rho_u>=s_i.
```

Also (7.4) gives

```text
q_u<=a-rho_u.
```

A chosen source has `q_u>=1`, hence `rho_u<=a-1`. Assign to every chosen incidence from u the charge

```text
(rho_u-1)/(a-rho_u).
```

Source u appears in at most `q_u<=a-rho_u` chosen incidences, so its total charge is at most `rho_u-1`. Residual activity makes these budgets nonnegative. Summing over B gives total charge at most

```text
sum_u(rho_u-1)=r-b.
```

The function

```text
(rho-1)/(a-rho)
```

is increasing for `1<=rho<a`. Therefore a label of demand `s_i` receives charge at least

```text
s_i(s_i-1)/(a-s_i).
```

Hence

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i).          (10.1)
```

Combining with `S>=r+2t` gives

```text
sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t.      (10.2)
```

Every positive demand participating here satisfies `s_i<=a-1`; `s_i=0` contributes zero.

## 11. Threshold-capacity inequality

Fix an integer `h>=1` and define

```text
I_h={i:s_i>=h},
W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h},
z_h=|Z_h|.
```

Choose `s_i` actual selected incidences for every `i in I_h`. By (6.2), every chosen source lies in Z_h.

Call an actual selected incidence **heavy** if its label lies in I_h. Let `ell_u` be the number of heavy selected incidences from source u. Then

```text
W_h <= sum_{u in Z_h} ell_u.              (11.1)
```

Let

```text
J={u in Z_h:ell_u>h},
j=|J|.
```

Fix `u in J` and a heavy selected edge `ui->w`. For each other heavy selected label k at u, `{u,k}` must dominate w; since `uw` is missing, `kw` is an H-edge. There are `ell_u-1>=h` such distinct heavy labels.

We claim `w in Z_h`. If none of those forced edges `kw` is selected from source w, all are residual and `rho_w>=h`. If at least one is selected from w, its heavy label k has `s_k>=h`, and (6.2) applied to that selected incidence gives `rho_w>=s_k>=h`.

Thus every supplement of a heavy selected edge from J lies in Z_h. By injectivity on missing unordered B-pairs, the number of heavy selected arcs from J is at most the number of unordered pairs inside Z_h incident with J:

```text
j(z_h-j)+C(j,2)=j z_h-j(j+1)/2.           (11.2)
```

Every source in `Z_h\J` contributes at most h heavy incidences. Therefore

```text
W_h <= (z_h-j)h + j z_h-j(j+1)/2.         (11.3)
```

If `W_h>0`, some label needs at least h distinct selected sources in Z_h, so `z_h>=h`. Put

```text
q=z_h-h.
```

Then

```text
[h z_h+C(q,2)] - RHS(11.3)
 = (q-j)(q-j-1)/2
 >=0,                                     (11.4)
```

because `q-j` is an integer and the product of consecutive integers is nonnegative. Hence

```text
W_h <= h z_h+C(z_h-h,2),
```

or equivalently

```text
2W_h <= z_h^2-z_h+h(h+1).                 (11.5)
```

This is a necessary capacity bound; sufficiency is not claimed.

Residual activity also gives, for `h>=2`,

```text
r >= b+z_h(h-1).                           (11.6)
```

Thus any valid upper bound `r<=r_max` implies

```text
z_h <= floor((r_max-b)/(h-1)).             (11.7)
```

## 12. Isolated-C lemma

Assume `t>0` and suppose `C=H[A]` has an isolated vertex x. Put

```text
X=A\{x}.
```

Because x is C-isolated, `e(C)=e(C[X])`. The number P0 of missing H-pairs inside X is

```text
P0=C(a-1,2)-e(C)
  =r-(a-1-t),                              (12.1)
```

using (4.2).

Take a missing pair ij inside X. Adding ij to H creates a new adjacent total-dominating pair using i or j. It cannot be `{i,j}`, because both miss x. Suppose it is `iz->j`.

The auxiliary z cannot be v: v already neighbours j, so adding ij cannot newly make `{i,v}` total dominating. It cannot lie in A: every candidate A-auxiliary would still fail to dominate x (and z=x is not adjacent to i). Hence `z in B`.

Thus every missing X-pair forces a cross quasi-edge whose unique exception is in A. Such an edge cannot be selected, because selected representatives have their unique exception in B. It is residual. Distinct missing X-pairs give distinct residual cross-edges because the cross-edge and its unique exception recover the missing pair. Let P be this residual family. Then

```text
|P|=r-(a-1-t).                             (12.2)
```

Let Z be the set of B-endpoints used by P. For every `z in Z`, choose a member `iz->j` of P ending at z. The pair `{i,z}` must dominate x, and i misses x, so `xz` is an H-edge. It is residual: z misses j because j is the exception of `iz->j`, while x misses j because x is isolated in C; hence xz cannot be selected. These xz edges lie outside P because their A-endpoint is x.

For every `z in B\Z`, residual activity supplies at least one residual edge incident with z. It lies outside P because no P-edge has B-endpoint z.

Thus there are at least b residual edges outside P, so

```text
r>=|P|+b.
```

Using (12.2),

```text
b <= a-1-t.                               (12.3)
```

Therefore, whenever

```text
b>a-1-t,
```

C has no isolated vertex. In that case

```text
delta(C)>=1,
d_i<=a-2,
e(C)>=ceil(a/2),                          (12.4)
```

and (4.2) gives

```text
r <= C(a,2)-t-ceil(a/2).                  (12.5)
```

## 13. Residual h-index corollary

Let h be the largest integer such that at least h residual rows have degree at least h.

A label of demand `s_i` requires `s_i` distinct selected sources, and every such source has residual degree at least `s_i` by (6.2). Therefore

```text
s_i<=h for every i,
S<=a h.                                   (13.1)
```

Residual activity gives every B-row degree at least one. At least h rows have degree at least h, so

```text
r>=h^2+(b-h)=b+h(h-1).                    (13.2)
```

Combining (13.1), (13.2), and `S>=r+2t` yields

```text
b+2t <= (a+1)h-h^2
     <= floor((a+1)^2/4).                 (13.3)
```

This is the residual h-index exclusion used in several fixed-order assemblies.

## 14. Trust boundary and scope

The canonical bridge consists of the implications proved above:

```text
critical diameter two
 -> complement quasi-edge representatives
 -> selected/residual injection
 -> exact ledger
 -> demand
 -> selected-edge forcing and endpoint load
 -> [if t>0] residual activity
 -> charging
 -> threshold capacity
 -> isolated-C exclusion
 -> residual h-index corollary.
```

No finite LP, numerical solver, fixed-order enumeration, published density theorem, or later RX-Hall potential is used in these proofs.

A counterexample to any universal implication above overrides every downstream fixed-order or general argument that invokes it. The highest-value external attacks are therefore Sections 2-3, 6, 8-12.

This note is a consolidation, not an assertion of external acceptance. Same-assistant rederivation does not replace independent mathematical review.
