# n=29, Delta=16: standalone graph-to-model bridge

9 September 2026. Research directed by Paul Lenz; mathematical development and internal audit by ChatGPT/Geeps.

**Status: candidate mathematics.** This note isolates the hand graph-theoretic bridge used before the finite `Delta=16` calculation in the n=29 Murty–Simon candidate. It is intentionally independent of the old n=28 inherited LP/joint machinery. External mathematical review remains open.

## 1. Scope and notation

Let `G` be a simple diameter-two edge-critical graph on `n=29` vertices with `Delta(G)=16`. Let `m=e(G)` be either `211` or `210`.

Put `H = complement(G)`. Choose a minimum-degree vertex `v` of `H`. Since `Delta(G)=16`,

```text
d_H(v)=29-1-16=12.
```

Set

```text
A = N_H(v),                 |A| = a = 12,
B = V(H) \ N_H[v],          |B| = b = 16.
```

Let `C=H[A]` and let `F` be the complement of `C` on the vertex set `A`. For `i in A`, write `d_i=d_F(i)`.

Define

```text
t = m - b(n-b) = m - 16*13,
```

so

```text
m=211 -> t=3,
m=210 -> t=2.
```

The purpose of this note is to derive the exact necessary conditions passed to the finite trusted-kernel calculation.

## 2. Complement form of edge-criticality

For an edge `uw` of `G`, the pair `uw` is a missing pair of `H`. Deleting `uw` from `G` is the same as adding `uw` to `H`.

Because `G` is diameter-two edge-critical, after deleting `uw` there is a pair of vertices at distance greater than two. Equivalently, in `H+uw` there is a new adjacent pair whose open `H+uw`-neighbourhoods together contain every vertex. Call such a pair an **adjacent total-dominating pair**.

Now take a missing pair `uw` of `H[B]`.

The new total-dominating pair in `H+uw` must use at least one endpoint of the newly added edge, since no other adjacency changed. It cannot be `{u,w}`, because both `u` and `w` miss `v`. Hence, after interchanging `u,w` if necessary, there exists a vertex `i` such that

```text
ui is already an edge of H,
N_H(u) union N_H(i) = V(H) \ {w}.
```

The vertex `i` must lie in `A`, because the pair must dominate `v` and `u` does not neighbour `v`.

We write

```text
ui -> w.
```

Thus every missing unordered pair `{u,w}` in `H[B]` admits at least one selected cross-edge of this form.

## 3. Selected-edge injection

Choose exactly one such cross-edge for every missing unordered pair in `H[B]`.

A selected edge `ui -> w` determines both its source `u` and its unique exception `w`: by definition `w` is the unique vertex not covered by `N_H(u) union N_H(i)`. Therefore two different missing unordered `B`-pairs cannot select the same cross-edge.

Hence the choice gives an injection

```text
{missing unordered pairs of H[B]} -> E_H(A,B).
```

Call the chosen cross-edges **selected**. Call all other existing `A-B` edges of `H` **residual**.

For `u in B` define

```text
rho_u = residual degree of u into A,
q_u   = number of selected edges with source u,
p_u   = number of selected missing B-pairs whose supplement/exception is u.
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

## 4. Exact edge ledger

Every unordered pair of `B` is exactly one of:

1. an edge of `H[B]`; or
2. a missing pair of `H[B]`, and therefore corresponds injectively to one selected cross-edge.

Thus

```text
#selected cross-edges + e(H[B]) = C(b,2).
```

On the other hand, counting missing edges of `H` relative to the complete bipartite cut determined by `v,A,B` gives the standard surplus identity

```text
e(F)=r+t.
```

Therefore

```text
sum_i d_i = 2(r+t).                    (4.1)
```

This identity is exact, not an inequality.

## 5. Label demand

Since `v` has minimum degree `a=12` in `H`, every `i in A` has `d_H(i)>=12`.

The neighbours of `i` in `H` are:

- `v`;
- the `C`-neighbours of `i` inside `A`, of which there are `a-1-d_i`;
- `R_i` residual neighbours in `B`;
- `x_i` selected neighbours in `B`.

Hence

```text
1 + (a-1-d_i) + R_i + x_i >= a,
```

so

```text
x_i >= d_i-R_i.
```

Define

```text
s_i = max(0,d_i-R_i),
S   = sum_i s_i.
```

Then

```text
x_i >= s_i.                              (5.1)
```

Summing and using the selected-edge ledger gives

```text
S >= r+2t.                               (5.2)
```

Thus a label of demand `s_i` genuinely requires at least `s_i` distinct selected source incidences.

## 6. Forcing from a selected edge

Fix a selected edge

```text
ui -> w.
```

By definition,

```text
N_H(u) union N_H(i) = V(H) \ {w}.
```

We now derive the pointwise inequalities used later.

### 6.1 `d_i <= rho_u + R_i`

Let `j` be an `F`-neighbour of `i`, so `ij` is missing in `H[A]`.

Since `j != w`, the covering property forces `uj in E(H)`.

Among such `uj` edges, at most `rho_u` are residual. Every remaining one is selected from source `u`; its supplement is a `B`-vertex adjacent to `i`, and distinct selected edges at source `u` have distinct supplements. Those supplement incidences are residual at label `i`.

Hence the `d_i` different `F`-neighbours are accounted for by at most `rho_u` residual source incidences plus `R_i` residual label incidences:

```text
d_i <= rho_u + R_i.                     (6.1)
```

### 6.2 `d_i <= rho_u + rho_w`

For the same `F`-neighbour `j` of `i`, the covering property also forces the corresponding residual incidence at the supplement side unless `uj` itself is residual. Distinct `F`-neighbours give distinct incidences. Therefore

```text
d_i <= rho_u + rho_w.                    (6.2)
```

### 6.3 `d_i <= rho_u + q_u - 1`

Every `F`-neighbour `j` of `i` forces `uj in E(H)`. Source `u` has exactly `rho_u+q_u` cross-neighbours in `A`, one of which is `i` itself. Therefore

```text
d_i <= rho_u + q_u - 1.                  (6.3)
```

### 6.4 Supplement forcing

Consider any other selected edge `uj -> z` at the same source `u`. Since `ui -> w` covers every vertex except `w`, the supplement `w` must be adjacent in `H` to `j` unless `j` is already covered by `u`; tracking the distinct selected labels yields

```text
rho_w + q_w >= q_u - 1.                  (6.4)
```

In particular, a source with large `q_u` requires many compatible supplement incidences.

## 7. Exact missing-degree identity in B

For a fixed `u in B`, every missing pair of `H[B]` incident with `u` is oriented exactly one of two ways by our selected choice:

- outward from `u`, counted by `q_u`; or
- inward to `u`, counted by `p_u`.

Therefore

```text
q_u+p_u = missing degree of u in H[B].   (7.1)
```

Consequently

```text
d_H(u) = rho_u + (b-1) - (q_u+p_u).
```

Since `d_H(u)>=a`,

```text
p_u <= rho_u + (b-a-1) = rho_u+3.        (7.2)
```

Also trivially

```text
q_u+p_u <= b-1 = 15.                     (7.3)
```

And because source `u` has only `a` cross-neighbours available,

```text
q_u+rho_u <= a = 12.                     (7.4)
```

## 8. Endpoint load at a selected label

Again fix `ui -> w`.

The following are distinct `B`-neighbours of label `i` in `H`:

1. the source `u` itself;
2. the `q_u-1` supplements of the other selected edges from source `u`;
3. the `p_u` sources of selected pairs oriented into `u`.

The last two families cannot collide: such a collision would orient the same missing unordered `B`-pair in both directions.

Hence label `i` has at least

```text
q_u+p_u
```

cross-neighbours in total. Since its residual and selected cross-degrees are `R_i` and `x_i`,

```text
R_i+x_i >= q_u+p_u.                      (8.1)
```

## 9. Residual activity when `t>0`

We prove that every `B`-vertex has positive residual degree.

Suppose, for contradiction, that `rho_u=0` for some `u in B`.

Let

```text
U=N_A(u),
T=A\U.
```

Every cross-edge from `u` is then selected. There is no `F`-edge between `U` and `T`: if `i in U`, `j in T`, and `ij in F`, then the selected edge at `ui` would have to cover `j`, forcing `uj in H`, contradiction.

Now count residual cross-edges forced by `F`.

- Each `F`-edge inside `U` forces two distinct residual cross-edges through the distinct supplements of its endpoints.
- Each `F`-edge inside `T` is a missing pair of `H[A]`. Its quasi-edge auxiliary cannot be `v` or `u`; an auxiliary in `A` would contradict the absence of `F(U,T)`. Therefore it yields a distinct residual cross-edge with `A`-endpoint in `T`.

These families are disjoint. Hence

```text
r >= 2e(F[U]) + e(F[T]).
```

Since there are no `F`-edges between `U` and `T`,

```text
e(F)=e(F[U])+e(F[T]),
```

so

```text
r >= e(F)+e(F[U]) >= e(F)=r+t.
```

But `t>0`, contradiction.

Therefore

```text
rho_u >= 1 for every u in B,             (9.1)
r >= b = 16.                             (9.2)
```

## 10. Charging inequality

For each label `i`, choose exactly `s_i` of its selected source incidences; this is possible by (5.1).

If source `u` is chosen for label `i`, then (6.1) gives

```text
s_i <= d_i-R_i <= rho_u,
```

so

```text
rho_u >= s_i.                             (10.1)
```

Also `q_u<=a-rho_u` by (7.4).

Assign to each chosen incidence from source `u` the charge

```text
(rho_u-1)/(a-rho_u).
```

A source contributes to at most `q_u<=a-rho_u` chosen incidences, so its total charge is at most `rho_u-1`. Summing over all `B`-sources gives total charge at most

```text
sum_u (rho_u-1) = r-b.
```

For a label of demand `s_i`, every chosen source has `rho_u>=s_i`, and the function

```text
(rho-1)/(a-rho)
```

is increasing for `1<=rho<a`. Therefore that label receives charge at least

```text
s_i(s_i-1)/(a-s_i).
```

Hence

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i).         (10.2)
```

Combining (10.2) with `S>=r+2t` yields

```text
sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t.     (10.3)
```

For `a=12,b=16`,

```text
sum_i s_i(13-2s_i)/(12-s_i) >= 16+2t.
```

This is the principal demand-domain inequality.

## 11. Threshold-capacity inequality

For an integer `h>=1`, define

```text
I_h = {i in A : s_i>=h},
W_h = sum_{i in I_h} s_i,
Z_h = {u in B : rho_u>=h},
z_h = |Z_h|.
```

Every selected incidence used to satisfy the demand of a label in `I_h` must come from a source in `Z_h`, by (10.1).

A source in `Z_h` can contribute at most one selected orientation to any unordered `B`-pair. Counting the available oriented pair capacity among the high-residual sources, together with the unavoidable low-end contribution from the threshold itself, gives the necessary inequality

```text
2W_h <= z_h^2-z_h+h(h+1).                (11.1)
```

This is a necessary Hall-type capacity bound; it is not asserted to be sufficient.

Residual activity and an upper bound `r<=r_max` also give, for `h>=2`,

```text
z_h <= floor((r_max-b)/(h-1)).            (11.2)
```

Conversely, if `max_i s_i=H`, then necessarily

```text
z_H>=H.                                   (11.3)
```

These threshold bounds replace the older pair-capacity support formula in the minimal trusted kernel.

## 12. Excluding `delta(C)=0`

The finite calculation also requires an explicit upper bound on `F`-degrees. We now derive it directly.

Suppose `C` has an isolated vertex `x`. Let `X=A\{x}`.

Every missing pair of `H` inside `X` has a quasi-edge whose auxiliary must lie in `B`; otherwise the required covering of `x` fails. Distinct such pairs force distinct residual cross-edges with `A`-endpoint in `X`.

For each `B`-endpoint already used by one of these residual edges, the quasi-edge structure forces a further residual edge incident with `x`. For every unused `B`-endpoint, residual activity supplies at least one residual edge. Thus there are at least `b` additional residual edges disjoint from the first family.

Writing

```text
L = C(a,2)-t,
```

we obtain the necessary inequality

```text
b <= L - C(a-1,2).                        (12.1)
```

At `a=12,b=16`,

```text
L=66-t,
L-C(11,2)=11-t,
```

so (12.1) would require

```text
16 <= 11-t,
```

impossible for both `t=3` and `t=2`.

Therefore

```text
delta(C)>=1.                              (12.2)
```

Consequently every `F`-degree satisfies

```text
d_i<=10.                                  (12.3)
```

Also `e(C)>=6`. Since

```text
e(C)+r = C(a,2)-t = 66-t,
```

we get

```text
r<=60-t.                                  (12.4)
```

This is the previously implicit bridge behind the old scanner bounds; it is now explicit.

## 13. What is passed to the finite trusted kernel

A graph in either dense `Delta=16` scope must therefore induce integer data satisfying all of the following:

```text
a=12, b=16, t in {3,2};
1<=rho_u<=12;
0<=d_i<=10;
r=sum rho=sum R;
e(F)=r+t;
s_i=max(0,d_i-R_i);
S>=r+2t;
q_u+rho_u<=12;
p_u<=rho_u+3;
q_u+p_u<=15;
for selected ui->w:
  d_i<=rho_u+R_i,
  d_i<=rho_u+rho_w,
  d_i<=rho_u+q_u-1,
  rho_w+q_w>=q_u-1,
  R_i+x_i>=q_u+p_u;
charging inequality (10.3);
threshold-capacity inequalities (11.1)-(11.3);
r<=60-t.
```

The minimal finite pipeline deliberately enumerates a **superset** of graph-realizable data satisfying these necessary conditions. Rejecting every such arithmetic state is therefore sufficient to exclude an actual graph, provided every pruning step is itself a necessary relaxation and every final infeasibility certificate is checked exactly.

## 14. Trust boundary

This note does not claim to prove the finite LP/certificate stage. It isolates the graph-theoretic bridge that an external reviewer should attack first.

The highest-value possible falsifications are:

1. a missing `B`-pair for which the selected cross-edge construction fails;
2. a collision invalidating selected-edge injection;
3. a counterexample to residual activity;
4. a label demand `s_i` that cannot be tied to `s_i` distinct sources of residual degree at least `s_i`;
5. a charging-budget failure;
6. a counterexample to the threshold-capacity inequality;
7. a configuration with `delta(C)=0` escaping (12.1).

Until those points receive independent expert review, the n=29 result remains a candidate theorem.
