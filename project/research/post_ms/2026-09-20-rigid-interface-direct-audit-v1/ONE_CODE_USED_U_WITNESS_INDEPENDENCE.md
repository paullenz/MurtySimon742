# Used complementary-U witnesses are independent in the rigid one-code branch

Date: 2026-09-20

Status: same-session structural theorem, conditional on the rigid one-code interface. This generalizes the mechanism that closed the explicit scalar escape ray. Independent hostile replay is still required before promotion.

## 1. Setup

Use the preserved rigid one-code notation:

- `A_X--Y` is complete, `x=|A_X|>=3`, `y=|Y|`;
- every vertex of Y has code d;
- `P={d,bar d}` and `A_bar d=emptyset`, `A_d=Y`;
- `g_P` is the number of pair-local matched gamma fibres;
- `k_P=(x-g_P)_+`;
- every outside source `y in Y` uses at least `k_P` distinct witnesses in `U_bar d`.

Let W be the union of the selected `U_bar d` witnesses across all sources and put `w=|W|`.

Then

> `w>=k_P`,                                               `(1.1)`

and there are at least

> `yk_P`                                                   `(1.2)`

distinct selected `(source,witness)` incidences, each a Y--W nonedge.

## 2. Every used witness has one X-head

Fix `z in W`. It is selected as a crossing witness for some source `s in Y` and some head `h in A_X`, so

> `N(s) cap N(z)={h}`.

Because the rigid A-cut is complete, s is adjacent to every vertex of `A_X`. Hence z cannot have a second neighbour in `A_X`; otherwise that vertex would be a second common neighbour with s. Since z is adjacent to h,

> **`N(z) cap A_X={h(z)}`**                                `(2.1)`

for a unique head `h(z)`.

This conclusion depends only on z being used at least once; it does not require the same witness set for every source.

## 3. Independence theorem

### Theorem 3.1

> **`G[W]` is independent.**                              `(3.1)`

### Proof

Suppose `zz'` is an edge of `G[W]`. Both endpoints have code `bar d`. Apply the independently repaired raw same-code criticality theorem to this U--U edge. After orienting the edge, say with source z, there is a unique-common-neighbour witness q satisfying

`N(z) cap N(q)={z'}`.

Because the source z lies in U, the raw theorem puts q in A; because z has code `bar d`, q has complementary code d. Pair purity gives

`q in A_d=Y`.

But z is a used crossing witness, so by `(2.1)` it has the unique X-neighbour `h(z)`. Since the rigid cut `A_X--Y` is complete,

`q h(z) in E`.

Therefore

`h(z) in N(z) cap N(q)`.

This is impossible because `h(z) in A_X` whereas the required unique common neighbour `z'` lies in U. Thus no edge `zz'` exists. `square`

The theorem is a direct composition of two already-audited raw interfaces: selected crossing witness singleton-head geometry and raw same-code U--U criticality.

## 4. General physical slack bill

Let `E_W=sum_{z in W} epsilon_z`. Every selected incidence is a Y--W nonedge, so

> `Z_Y(W)>=yk_P`.                                         `(4.1)`

By `(2.1)`, the total W--X edge count is exactly w. Hence the number of W--Y edges is at most `wy-yk_P`. By Theorem 3.1 there are no W--W edges, and edges from W to `U\W` contribute at most `w(u-w)` incidences.

For every U-vertex the preserved degree identity is

`d_{A union U}(z)=p+u-1-epsilon_z`.

Summing over W gives

`w(p+u-1)-E_W`
`<= w + (wy-yk_P) + w(u-w)`.

Therefore

> `E_W >= w(p-y+w-2)+yk_P`                                `(4.2)`
>
> `      = w(g0+w-2)+yk_P`.

When `g0>=1`, the right side is increasing for integer `w>=1`. Since `w>=k_P`,

> **`E_W >= k_P(p+k_P-2)`.**                              `(4.3)`

This strictly strengthens the predecessor one-code U-slack floor

`E_bar d>=k_P(p-1)`

whenever `k_P>=2`.

## 5. Strengthened gamma/U tradeoff

Retain the predecessor gamma-collision price

`L_A>=phi(g_P)`,

where `phi(g)=g(g-1)` for `g>=3` and zero for `g<=2`.

For `g0>=1`, disjoint score components now give

> **`S >= phi(g_P)+k_P(p+k_P-2)`,**                       `(5.1)`

with `k_P=(x-g_P)_+`.

Define the strengthened one-code obstruction

> `Psi_phys(p,x)=min_{0<=g<=p}`
> ` {phi(g)+(x-g)_+(p+(x-g)_+-2)}`.                       `(5.2)`

Every above-M rigid one-code candidate with `g0>=1` must satisfy

> `Psi_phys(p,x)<=C0`.                                    `(5.3)`

This replaces the predecessor linear unmatched-witness price by a quadratic physical witness price. It is the natural next object for the large-gap analysis.

## 6. Check on the explicit escape ray

For

`p=3t, x=5t, g_P=2t, k_P=3t`,

`(4.3)` gives

`E_W>=3t(6t-2)=18t^2-6t`,

which, together with the preserved Hamming floor, closes that ray for `t>=9` as recorded separately.

## 7. Trust boundary and next step

This theorem is still conditional on reaching the rigid one-code interface. Bounded actual-D2C regression contains zero positive rigid complete Hall-cut fixtures with `x>=3`, and `X_3` remains the mandatory negative control.

The highest-value next move is to hostile-replay Theorem 3.1 from the raw certificate orientation and then substitute `Psi_phys` into the predecessor `(c,p,u,n)` large-gap argument. The key question is whether the new quadratic `k_P` price converts the previous linear rooted-gap necessity into a genuine finite-order bound.
