# Two-X-hole branch — hole-code forward-routing surcharge and extreme-radius slot price

Date: 2026-09-20

Status: **same-session internal structural strengthening** inside the core-saturated exact second-strict two-X-hole branch (`y>=2`, `x>=4`). This note builds on `TWO_X_HOLE_MATCHED_ROUTING_CAPACITY.md`, `TWO_X_HOLE_CERTIFICATE_INCIDENCE.md`, and `TWO_X_HOLE_EXACT_X_SLACK_LEDGER.md`. It remains conditional on the audited rigid-cut interface; the zero-positive-fixture caveat remains binding.

## 1. Setup

Let the two physical buffer holes be `a_0,a_1`, with codes

`H_j=c(a_j)`.

Let `C=H_0` be a represented buffer-head code in

`R=X\{a_0,a_1}`.

Put

- `I_C={i:C_i=d_i}`;
- `s=s_C=|I_C|>=1`;
- `M_C=U_o cap V_{bar C}`;
- `m=m_C=|M_C|>=1`.

For every `z in M_C` and every `i in I_C`, the physical rooted matched edge `zq_i` must route through one of the two feet `a_0,a_1`.

The predecessor routing theorem gives

`m s <= m+2s`                                            `(H-ROUTE)`

because forward routing through the same-code foot `a_0` is impossible, reverse routing has capacity at most `2s`, and each physical witness can forward-route at most one coordinate through the opposite foot `a_1`.

If `H_0=H_1`, both feet have code C, forward routing through either foot is impossible and the predecessor already gives `m<=2`. Hence the only new case is `H_0!=H_1`.

## 2. A quantitative forward-routing floor

There are `ms` physical matched-edge obligations `(z,i)` in the class.

At most `2s` of them can use reverse routing, one for each ordered pair `(q_i,a_j)`. Therefore at least

> **`F_C := [ms-2s]_+ = s[m-2]_+`**                     `(H-FWD)`

obligations must use forward routing through the opposite foot `a_1`.

A fixed witness `z` can forward-route through `a_1` at most one coordinate, because the ordered pair `(z,a_1)` has a graph-fixed singleton matched head. Thus the `F_C` forward obligations use `F_C` **distinct physical witnesses**.

The predecessor inequality `(H-ROUTE)` implies automatically

`F_C<=m`.

This was independently checked over all positive integer `(m,s)` in a broad finite box; there is no arithmetic exception. The proof itself is the exact inequality above, not the finite check.

## 3. Every forward-routed witness forces two new physical holes

Fix a forward-routed witness `z in M_C`, using coordinate `i` through `a_1`.

The raw singleton certificate is

`N(z) cap N(a_1)={q_i}`,

with `za_1 notin E` in the witness orientation.

Let `c_{a_1} in W_0` be the unique common-core vertex assigned to `a_1` by the core-head bijection. Since `c_{a_1}a_1 in E`, if `c_{a_1}z` were also an edge then `c_{a_1}` would be a second common neighbour of `z` and `a_1`, contradicting the singleton identity. Hence

> `za_1 notin E`,                                         `(H-XHOLE)`
>
> `zc_{a_1} notin E`.                                     `(H-COREHOLE)`

These holes are new relative to the certificate-incidence ledger J:

- J-heads lie in `R`, never at the physical hole `a_1`, so `(z,a_1)` is not one of the `L` incidence nonedges;
- J-core holes have the form `(z,c_x)` with `x in R`; the core-head bijection makes `c_x != c_{a_1}`.

Because the forward-routed witnesses are distinct, the class contributes at least `F_C` additional X--U_o holes and at least `F_C` additional W_0--U_o holes beyond those already counted by J.

The same argument applies symmetrically to a represented class `C=H_1`, routing forward through `a_0`.

## 4. Global forward surcharge over represented hole classes

Let `mathcal H` be the set of distinct represented physical hole codes. For each `C in mathcal H`, write `(m_C,s_C)` as above and define

> `F_C=s_C[m_C-2]_+`.

If the two holes have the same code, the predecessor bound `m_C<=2` gives `F_C=0`.

If the hole codes are distinct, their complementary witness classes are distinct, so all physical holes counted below are distinct. Put

> **`F_H=sum_{C in mathcal H} F_C`.**                     `(H-FSUM)`

Then the certificate-incidence ledger sharpens from

`H_core>=L`

to

> **`H_core>=L+F_H`,**                                    `(H-HCORE)`

and therefore

> **`E_core>=x(p+x-1)+L+F_H`.**                           `(H-ECORE)`

Likewise the aggregate X-side degree ledger gains the additional physical X--U_o holes:

> **`L_X>=x(p+x-y)-(x-2)+L+F_H-2e_X`.**                  `(H-LX)`

The rooted U-edge ceiling loses the additional core--outside edges:

> **`q<=(x+1)omega-L-F_H+e(G[U_o])`**                     `(H-Q0)`

and hence, using `e(G[U_o])<=M_H`,

> **`q<=(x+1)omega-L-F_H+M_H`.**                          `(H-Q)`

Thus forward routing is not merely a combinatorial capacity mechanism: every unit of forced forward traffic is charged simultaneously in common-core score, A-side slack, and rooted U-edge capacity.

## 5. Outside-witness slack also receives the same surcharge twice

For `z in U_o`, let `r_z=d_J(z)` and let `f_z in {0,1}` indicate whether z is one of the forward-routed hole-code witnesses counted in `F_H`.

The predecessor certificate-incidence theorem gives z at least

- `r_z` certified X-head nonneighbours;
- `r_z` corresponding common-core nonneighbours.

If `f_z=1`, Section 3 adds

- the opposite physical X-hole;
- that hole's distinct common-core vertex.

Therefore

> **`epsilon_z >= [p-x+2r_z+2f_z]_+`.**                  `(H-ZPAY)`

Summing and using `sum r_z=L`, `sum f_z=F_H`,

> **`E(U_o)>=sum_z[p-x+2r_z+2f_z]_+`
> `       >=[omega(p-x)+2L+2F_H]_+`.**                   `(H-UOPAY)`

This is a second, independent score charge for the same forward-routing population.

## 6. Extreme-radius represented hole classes force rooted slot mass

The only way a represented hole-code witness population can be unbounded under `(H-ROUTE)` is

`s_C=1`.

Then every R-head of that code has Hamming radius

`d_H(C,d)=p-1`.

Let

`N_ext=sum n_C`

over represented hole-code classes with `s_C=1`.

Every X-code is different from d, so each of the other `x-N_ext` X-vertices contributes Hamming distance at least one across the complete X--Y cut. Hence for every `y_0 in Y`,

> **`H_Y(y_0)>=x+N_ext(p-2)`.**                           `(H-HAM)`

The audited local Hamming-slot theorem therefore yields

> **`r_{y_0}>=1+ceil(N_ext(p-2)/x)`.**                    `(H-RY)`

Every X-vertex has a Y-neighbour of a different tight code, so each X-vertex contributes at least one unused rooted slot. Consequently

> **`r>=x+y[1+ceil(N_ext(p-2)/x)]`.**                     `(H-R)`

For `p>=3`, any nonzero extreme-radius represented population therefore forces at least the discrete jump

> `r>=x+2y` whenever `N_ext>0` and `N_ext(p-2)>0`.

The precise ceiling form `(H-R)` should be retained when `N_ext` is large.

## 7. New structural dichotomy

Every surviving hole-code represented two-X-hole geometry now falls into one of two genuinely priced regimes.

### Bounded witness-resource regime

If every represented hole code has `s_C>=2`, the predecessor route theorem bounds each `m_C` by at most four. Thus `M_H<=8`, with stronger bounds in most patterns. The new `F_H` surcharge further reduces any case near those maxima.

### Extreme-radius regime

If some distinguished witness population is unbounded, then its class has `s_C=1`. For such a class:

- its physical witness excess over two contributes
  `F_C=m_C-2`;
- each of those excess witnesses pays two new physical holes and the triple ledger surcharge `(H-ECORE)/(H-LX)/(H-Q)` plus the doubled outside-slack surcharge `(H-UOPAY)`;
- its head population contributes radius-`p-1` Hamming load through `(H-R)`.

Thus neither a large witness population nor a large extreme-radius head population is now free. The remaining optimization should keep `(n_C,m_C,L_C,F_C)` explicit rather than replacing the class by an anonymous `M_H`.

## 8. Audit boundary and next move

This theorem is same-session candidate mathematics. The load-bearing points for hostile replay are:

1. forward routing through a same-code physical foot is indeed impossible at the exact tight-singleton level;
2. the `2s_C` reverse-route capacity is over physical ordered pairs `(q_i,a_j)`;
3. the additional `(z,a_{1-j})` and `(z,c_{a_{1-j}})` holes are disjoint from the J-incidence holes;
4. the local Hamming-slot theorem is applied only after the physical radius-`p-1` class is identified.

If these survive replay, the next analytic attack should insert `F_H` and the exact extreme-radius slot floor into the score/rooted combination used in the no-hole-code closure. The objective is to close the bounded `M_H<=8` arm analytically and determine whether the extreme-radius arm still admits an unbounded scaling family once forward traffic is physically priced.
