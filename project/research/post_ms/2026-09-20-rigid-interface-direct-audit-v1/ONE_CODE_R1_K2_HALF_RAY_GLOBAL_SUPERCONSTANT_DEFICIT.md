# Residual-one k=2 half-ray: global superconstant residual-slot deficit

Date: 2026-09-20

Status: **same-session conditional structural theorem, self-corrected before handoff and pending the midnight red-team audit.** It is downstream of the corrected rigid one-code residual-one interface, repaired H--U B-layer classification, independently replayed residual-slot collapse theorem, and H--H private-foot certificate split. It does **not** use the superseded H--U private-foot coordinate-slice chain. Bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.

## 1. Setup

On the corrected intermediate half-ray

- `p=2t`, `c=y=t`, `u=t+1`, `h=|H|=2t-1`,
- `k=2`, `J2=empty`,
- `Delta=a+b+c0`, where `a=2M_H-R_q`, `b=h-R_j`, `c0=(u-2)-S`,
- `N=R_j=h-b`,
- `P=U_j^-`, `g=|U\P|`.

The independently replayed predecessor gives

`a+c0 >= binom(N,2)`,

hence

`Delta >= h-N+binom(N,2)`.

Write `s=Delta-h`. Then

`a+c0=s+N`,                                                `(SC-1)`

and

`N <= R(s):=(3+sqrt(9+8s))/2`.                            `(SC-2)`

Put `D=s+R(s)`, so `a,c0<=D`.

## 2. Strict exclusion of the predecessor equality face

The session classified all `Delta=h` cases. By `(SC-2)`, `N<=3`.

- `N=3` forces `a=0,c0=3`, three distinct D=2 residual carriers, an independent saturated triple complete to the unsaturated H-rows, and then forces all three carriers to H-degree one. Physical-slot equality removes B1 and leaves endpoint-indexed resources H-free, so `S=0`, contradicting `S=t-4` for `t>=5`.
- `N=2` reduces to three `(a,c0)` allocations. The cheapest `a=0,c0=2` forces two H-degree-one D=2 carriers and at most one usable B1 shared edge; the other allocations have still less usable shared capacity. Thus `S=t-3` is impossible for `t>=5`.
- `N=1` has `a+c0=1`; either full shared saturation is broken by the residual carrier, or the D=2 carrier consumes the unique nonshared slot and B1 support is confined to at most two exceptional H-rows. This gives `S<=2`, contradicting `S=t-2` for `t>=5`.
- `N=0` gives `a=c0=0`, `R_j=0`, `R_q=2M_H`, `S=u-2`. Shared saturation forces every nonselected U-vertex to be B1 or endpoint-indexed. Endpoint-indexed vertices are H-anticomplete, so `e(H,U)<=u-2`, whereas the mechanism partition gives `e(H,U)=2M_H+u-2`. Hence H is complete and every nonselected U-vertex is B1. B1 vertices on two different H-rows would block both private-foot orientations of their H-edge, so all `t-1` B1 vertices attach to one row. The exact local identity gives `d_U<=3`, hence `t<=4`.

Therefore

> **for every `t>=5`, `Delta>=h+1=2t`, hence `L_H>=5t-1`.** `(SC-3)`

## 3. Same-session correction: a common U-vertex can itself be the singleton head once

An initial version of this note incorrectly said that if a U-vertex `w` is common to `(h_i,q_l)`, then the reverse-private slot is unavailable. The correct statement is subtler: the slot may still be used **if `w` itself is the singleton U-head**, but the physical edge `h_iw` can be assigned to at most one chosen H--U mechanism. Therefore, for a fixed source row and fixed common U-vertex, at most one otherwise-blocked reverse-private slot can be recovered.

The correction weakens the finite degree polynomials below by one linear term, but it does **not** change the `t^(2/3)` asymptotic exponent or leading asymptotic constant. This correction was found and installed before the session handoff.

## 4. B1 touched rows

Let `B1` be the H-positive `bar d` vertices of H-degree one, and let `T` be the set of H-rows touched by B1.

Two touched rows cannot be adjacent: a B1 neighbour at each endpoint blocks both private-foot orientations, while endpoint-indexed U-certificates for H--H edges are unavailable. Thus `T` is independent.

For `h_i in T`, every missing H-neighbour `h_l` makes a reverse-private pair `(h_i,q_l)` with every B1 neighbour of `h_i` as a common U-vertex. If there are at least two B1 neighbours, no such singleton is possible. If there is exactly one, that one physical H--U edge can be assigned to at most one reverse-private slot. Hence uniformly

`a_i >= m_i-1` for every touched row.                    `(SC-B1A)`

Therefore, with `r=|T|`,

`a >= r(r-2)`.                                             `(SC-B1B)`

Put

`tau(a)=1+sqrt(1+a)`.

Then `r<=tau(a)`. The local identity `d_U(h_i)<=m_i+3` gives, writing `B_i` for the B1 multiplicity on row i,

- if `B_i=1`, its contribution is one;
- if `B_i>=2`, then no reverse-private slot from the row is usable and `B_i<=a_i+3`.

Summing safely gives

> **`|B1| <= a+3tau(a)`.**                                `(SC-B1)`

## 5. Exceptional residual-bar vertices

Take an H-positive `w in P` which is not B1. The raw private-spoke theorem gives a private D-set of size 0 or 2, and every H-neighbour index lies outside D, so w sees the corresponding private foot.

Its H-neighbourhood is independent: on an H-edge between two such neighbours, w blocks both private-foot orientations and U-certification is unavailable. If `d=d_H(w)`, there are `d(d-1)` ordered holes inside this neighbourhood. For each source row, at most one of the `d-1` corresponding reverse-private slots can use `w` itself as singleton head, because the physical edge from that row to w can be assigned only once. Therefore

> **`d(d-2)<=a`.**                                        `(SC-P)`

Hence `d_H(w)<=tau(a)`.

## 6. Outside-P matched-spoke lemma

Take an H-positive `w in U\P`. Let

`D(w)={r : w selects the d-endpoint p_r}`.

Because w is residual-plus, `j in D(w)`.

Suppose `h_i in N_H(w)` and `i in D(w)`, so `wp_i` is a rooted B-edge.

- Reverse orientation of `wp_i` is impossible: the only A-witness missing `p_i` is `h_i`, but every Y-vertex is a second common neighbour of `p_i` and `h_i`.
- In a forward orientation with singleton head `p_i`, the A-witness must have support relative to d exactly `D(w)\{i}`. The A repertoire has supports only `empty`, `{j}`, and `{l}`. Therefore `|D(w)\{i}|<=1`.

Since `j in D(w)`, two distinct H-neighbour indices cannot both belong to D(w). Thus at most one H-neighbour is a d-bit coordinate.

Let `r` be the number of remaining H-neighbours, all at bar-bit coordinates. They form an independent H-set and create `r(r-1)` ordered holes. Again, for each source row, at most one slot can use w itself as singleton head. Therefore

`r(r-2)<=a`.                                               `(SC-QA)`

Since `r>=d_H(w)-1`,

> **`(d_H(w)-1)(d_H(w)-3)<=a`.**                          `(SC-Q)`

Consequently

`d_H(w)<=2+sqrt(1+a)`.                                    `(SC-QB)`

Define

`kappa(a)=2+sqrt(1+a)`.

## 7. Global shared-resource count

The shared block has

`S=t-1-c0`.                                                `(SC-S1)`

Every used physical shared resource is either B1 or endpoint-indexed. Endpoint-indexed vertices are H-anticomplete. Of the `u-2` nonselected U-vertices, exactly `c0` are outside the used shared-resource set; therefore every H-positive non-B1 U-vertex lies among at most `c0` exceptional physical vertices.

Using `(SC-B1)`, `(SC-P)`, `(SC-QB)`,

> **`e(H,U) <= a+3tau(a)+c0 kappa(a)`.**                  `(SC-S2)`

Every shared mechanism is assigned to an H--U edge, so `S<=e(H,U)`. Hence

`t-1-c0 <= a+3tau(a)+c0 kappa(a)`.

Using `a,c0<=D` and monotonicity yields

> **`t <= 1+2D+3tau(D)+D kappa(D)`,**                     `(SC-FIN)`
>
> where `D=s+(3+sqrt(9+8s))/2`, `tau(D)=1+sqrt(1+D)`, and `kappa(D)=2+sqrt(1+D)`.

## 8. Superconstant consequence

As `s->infinity`,

`D=s+O(sqrt(s))`, `tau(D)=sqrt(D)+O(1)`, `kappa(D)=sqrt(D)+O(1)`.

Therefore `(SC-FIN)` gives

`t <= (1+o(1))s^(3/2)`.

Equivalently,

> **`s >= (1-o(1))t^(2/3)`.**                             `(SC-ASYM)`

Since `s=Delta-h` and `L_H=3t-1+Delta`,

> **`Delta >= h+(1-o(1))t^(2/3)`,**
>
> **`L_H >= 5t-2+(1-o(1))t^(2/3)`.**                     `(SC-H)`

Thus every fixed-excess saturation pattern is excluded and the corrected H--U capacity deficit grows polynomially. This remains a conditional downstream theorem, not a graph-level closure.

## 9. Hostile star and audit target

Before the matched-spoke lemma, the existing equations admitted an abstract `g=1,s=1` star in which one outside-P U-head appeared able to carry linearly many reverse-U roles through endpoint-indexed witnesses. It is not an actual D2C graph. The matched-spoke lemma kills that escape by forcing almost all of a high-degree outside-P head's H-neighbours onto bar-bit coordinates, where their mutual ordered holes charge `a` up to the one-self-head-per-source correction above.

The midnight audit should hostile-replay, in order:

1. the matched-spoke witness-location argument;
2. the one-self-head-per-source correction and the exact polynomials `(SC-P)` / `(SC-Q)`;
3. the B1 bound `(SC-B1)`;
4. the physical statement that every H-positive non-B1 U-vertex lies among the `c0` unused shared-resource slots;
5. `(SC-S2)` and the asymptotic conversion.

If these survive, feed the superconstant H-slack excess into the exact score/rooted ledger. The upstream rigid-interface reachability risk remains unchanged.