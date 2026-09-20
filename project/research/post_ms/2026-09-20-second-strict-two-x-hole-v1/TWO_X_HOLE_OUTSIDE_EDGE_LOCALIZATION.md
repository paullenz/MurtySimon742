# Two-X-hole branch — all outside U_o edges localize to the two hole-code classes

Date: 2026-09-20

Status: **same-session internal structural theorem** inside the core-saturated two-X-hole branch (`y>=2`, `x>=4`). This is a raw rooted-edge criticality argument and does not assume the two outside endpoints have the same code.

## 1. Setup

Retain:

- every `z in U_o` is adjacent to b and certifies at least one buffer head `q in R`;
- hence `c(z)=bar c(q)`, with `c(q)` neither d nor bar d;
- `G[R]=emptyset`;
- the only X-vertices nonadjacent to b are the two holes `a_0,a_1`;
- U_o is Y-anticomplete;
- the root is adjacent to every U-vertex.

For a represented head code C, write

`M_C=U_o cap V_{bar C}`, `m_C=|M_C|`.

Let the two hole codes be

`H_j=c(a_j)`, `j=0,1`.

## 2. Raw witness localization for an arbitrary U_o--U_o edge

Take an arbitrary edge `zz'` inside U_o. Because both endpoints lie in the root neighbourhood, the edge lies in the triangle `vzz'` and raw triangle-edge criticality applies.

Choose an orientation with source z, head z', and witness w.

### Lemma 2.1 — the witness lies in A and has code complementary to the source

The witness cannot lie in U or in the tight matched layer: any such vertex lies in the root neighbourhood and therefore shares the root v with the U-source z, giving an extra common neighbour distinct from z'. The root itself is adjacent to z and cannot be the required non-neighbour witness.

Hence `w in A`.

If `c(w)` agreed with `c(z)` in any tight coordinate, z and w would share the corresponding matched endpoint, again an extra common neighbour. Thus

> **`c(w)=bar c(z)`.**                                   `(UO-EDGE-COMP)`

If z belongs to the outside witness class `M_C`, then `bar c(z)=C`. Therefore every certificate of an oriented U_o edge sourced from z must use an A-vertex of the **same code C as the buffer heads certified by z**.

## 3. Ordinary buffer heads of code C cannot witness

Let `x in R` have code C. Since x is a buffer neighbour and z is an outside vertex,

`bx,bz in E`.

Thus b is already a common neighbour of x and z. It is distinct from the U_o head z'. Hence no ordinary C-coded buffer head can be the singleton witness for an edge sourced from z.

A Y-witness would require C=d, excluded. Therefore:

> **an oriented U_o edge sourced from `z in M_C` can be witnessed only by one of the two physical holes whose code is C.** `(UO-HOLE-ONLY)`

In particular, if neither hole has code C, z cannot be the source orientation of any U_o edge.

## 4. Global U_o edge capacity

Put

> `h_C=#{j in {0,1}:H_j=C}`,

so `h_C in {0,1,2}` and `sum_C h_C=2` over distinct represented/unrepresented codes.

For a fixed source z in `M_C` and a fixed matching hole a_j, the ordered pair `(z,a_j)` has one graph-fixed common-neighbour set. It can therefore singleton-certify at most one U_o head.

Choose one valid orientation/certificate for every edge of `G[U_o]`. By `(UO-HOLE-ONLY)`, an edge assigned source z consumes one of at most `h_C` ordered source-hole pairs. Ordered-pair injectivity gives

> `d_source(z)<=h_C` in the chosen oriented certificate system.

Summing over sources yields the sharp global capacity

> **`e(G[U_o])<=sum_C h_C m_C`
> `                =m_{H_0}+m_{H_1}`**,                 `(2X-UO-EDGE-CAP)`

where a repeated hole code is counted twice and an unrepresented code has `m_H=0`.

This statement controls **all** outside edges, not only same-code edges.

## 5. The same distinguished resource pays X-density and U_o-density

The internal-X localization theorem already gives

> `e(G[X])<=m_{H_0}+m_{H_1}`.

Define the two-hole witness resource

> `M_H:=m_{H_0}+m_{H_1}`.                                `(MH)`

Then simultaneously

> **`e(G[X])<=M_H`,**                                     `(MH-X)`
>
> **`e(G[U_o])<=M_H`.**                                  `(MH-U)`

Thus the only physical outside classes capable of buying internal X-degree are exactly the same classes capable of buying internal U_o-degree. All other witness classes can contribute neither resource.

## 6. Linear rooted triangle ceiling

`U_-=W_0 dotcup {b}` is independent. There are at most `(x+1)omega-L` cross edges from `U_-` to U_o because the certificate incidence graph forces L distinct core--outside holes.

Using `(MH-U)` for the internal outside layer gives the much sharper bound

> **`q<= (x+1)omega-L+M_H`.**                            `(2X-Q-LIN)`

This replaces the predecessor quadratic allowance

`binom(omega,2)+(x+1)omega-L`.

The improvement is structural: an arbitrarily dense outside reservoir is impossible because every U_o edge must route its raw certificate through one of only two physical X-hole codes.

## 7. Combined score/rooted resource cone

The exact X-slack ledger has

`L_X>=x(p+x-y)-(x-2)+L-2e(G[X])`.

By `(MH-X)`,

> `L_X>=x(p+x-y)-(x-2)+L-2M_H`.                          `(MH-LX)`

Together with `(2X-Q-LIN)`, increasing the distinguished resource M_H has only a tightly controlled effect:

- it can recover at most `2M_H` units of X-slack;
- it can add at most `M_H` rooted U-edges;
- but all `m_C` contributing to M_H are already physical outside witnesses and therefore contribute to the incidence/core-hole and outside-slack ledgers.

This is the first reduction in the two-X-hole branch that couples the possible X-density rebate and q-density rebate to the **same two code classes**.

## 8. Next target

The natural next step is now to optimize only the distinguished hole-code populations, not arbitrary U_o density. Two cases should be separated:

1. neither hole code is represented in R: `M_H=0`, so both `G[X]` and `G[U_o]` are edgeless;
2. one or both hole codes are represented: use the two-foot support normal form and class self-pricing to bound `m_{H_j}` and the associated certificate loads.

The first case is now a purely linear rooted/score ledger and is a plausible candidate for immediate analytic closure. The second is a finite code-pattern problem rather than an unstructured reservoir.