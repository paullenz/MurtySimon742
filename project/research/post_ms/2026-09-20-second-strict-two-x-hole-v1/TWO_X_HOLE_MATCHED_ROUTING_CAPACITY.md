# Two-X-hole branch — physical matched-routing capacity per code class

Date: 2026-09-20

Status: **same-session internal structural theorem** inside the core-saturated exact second-strict two-X-hole branch. The key point is to count physical matched edges `zq_i`, not head-certificate incidences: if one outside witness serves several same-code buffer heads, the rooted matched obligation is still one physical edge per witness and coordinate.

## 1. Setup

Let C be a represented buffer-head code in

`R=X\{a_0,a_1}`.

Put

- `I_C={i:C_i=d_i}` and `s_C=|I_C|>=1`;
- `M_C=U_o cap V_{bar C}` and `m_C=|M_C|>=1`.

Every physical `z in M_C` certifies at least one buffer head of code C, since every outside vertex is a buffer certificate and code complementation identifies its head class.

For every `i in I_C`, z selects the bar-d endpoint `q_i`, so `zq_i` is a rooted B-edge. The two-foot routing theorem says its raw singleton certificate must use one of the two physical buffer holes `a_0,a_1`.

Thus there are exactly

> `m_C s_C`

distinct physical matched-edge obligations `(z,i)` in this class.

## 2. Global two-foot capacity for one code class

For an obligation `(z,i)`, a foot can be used in one of two ways.

### Reverse routing

A reverse certificate through `a_j` has

`N(q_i) cap N(a_j)={z}`.

For a fixed ordered physical pair `(q_i,a_j)`, the singleton head z is graph-fixed. Therefore at most one physical witness z can use this reverse route.

There are only `2s_C` possible pairs `(q_i,a_j)`. Hence reverse routes cover at most

> `2s_C`

of the class obligations.

### Forward routing

A forward certificate through `a_j` has

`N(z) cap N(a_j)={q_i}`.

For a fixed ordered pair `(z,a_j)`, the singleton matched head q_i is graph-fixed. Therefore each witness z can forward-route at most one coordinate through each foot.

There are `2m_C` such source-foot pairs. Hence forward routes cover at most

> `2m_C`

obligations.

Combining the two channels yields the exact necessary capacity inequality

> **`m_C s_C <=2m_C+2s_C`.**                            `(2X-CLASS-ROUTE)`

Equivalently

> **`(m_C-2)(s_C-2)<=4`.**                              `(2X-CLASS-HYPERBOLA)`

No selected-representative uniqueness is used here beyond graph-fixed ordered singleton pairs. The count is over physical vertices and physical matched edges.

## 3. Stronger capacity when C is a physical hole code

Suppose

> `C=c(a_0)`.

A forward route through `a_0` is impossible. Indeed forward routing requires

`d_H(C,c(a_0))=1`

by the exact tight-singleton condition, whereas the two codes are equal.

Thus only the other foot can contribute forward routes. Reverse capacity remains at most `2s_C`. Hence

> **`m_C s_C<=m_C+2s_C`.**                              `(2X-HOLE-ROUTE)`

Equivalently

> `m_C(s_C-1)<=2s_C`.                                    `(2X-HOLE-ROUTE2)`

Consequences:

- if `s_C=1`, this inequality imposes no bound on `m_C`;
- if `s_C=2`, then `m_C<=4`;
- if `s_C=3`, then `m_C<=3`;
- if `s_C>=4`, then `m_C<=2`.

So an unbounded distinguished hole-code witness population is possible only in the extreme-radius case

> **`|I_C|=1`, equivalently `d_H(C,d)=p-1`.**            `(2X-HOLE-EXTREME)`

## 4. If both holes have the same represented code

If

`c(a_0)=c(a_1)=C`,

then forward routing through **either** foot is impossible for a C-head. All `m_Cs_C` obligations must use reverse routes, of which there are at most `2s_C`. Since `s_C>=1`,

> **`m_C<=2`.**                                          `(2X-SAME-HOLES-MCAP)`

Thus two identical hole codes cannot support a large distinguished outside population at all, even in the `s_C=1` extreme-radius case.

## 5. Structural dichotomy for the remaining branch

`TWO_X_HOLE_NO_HOLE_CODE_CLOSURE.md` proves that every surviving large two-X-hole geometry must represent at least one hole code in R.

The present theorem then gives a sharp dichotomy.

### Bounded distinguished-resource arm

If every represented hole code has `s_C>=2`, then each distinguished physical witness class has size at most four (and usually at most two or three). Hence

`M_H=m_{H_0}+m_{H_1}`

is an absolute constant at most eight, with further improvement when the holes share a code.

Since both `e(G[X])` and `e(G[U_o])` are at most `M_H`, all possible density rebates are then bounded by an absolute constant while the core/certificate bills scale with x and omega.

### Extreme-radius arm

Any unbounded distinguished witness population forces a represented hole code C with

`|I_C|=1`,

so every X-vertex of that code is at Hamming radius `p-1` from the Y-code d. This is exactly the regime where the local Hamming-slot ledger becomes strongest.

Thus the remaining two-X-hole programme should split on

> **bounded `M_H` versus radius-`p-1` hole-code heads**,

rather than continuing to optimize an unconstrained outside reservoir.

## 6. Next move

1. In the bounded arm, insert `M_H<=8` into the exact X-slack/rooted ledger and seek an analytic large-x closure, leaving only a finite structural tail.
2. In the extreme-radius arm, combine the large Hamming distance `p-1` across the complete X--Y cut with the two-foot routing and the fact that R is independent. The objective is to force rooted unused-slot mass growing like `n_C(p-1)` and defeat the only route by which `M_H` can remain unbounded.

The two arms are structurally distinct and should not be flattened into a single scalar parameter scan.