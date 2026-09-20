# Physical witness-incidence repricing on the explicit escape ray

Date: 2026-09-20

Status: same-session structural theorem/diagnostic, conditional on the rigid one-code interface and the parameter ray already preserved. This is not a graph construction.

## 1. Setup

Use

`p=3t, y=t, u=4t, x=5t, g_P=2t, k_P=3t`, `t>=2`.

Let `W` be the union of distinct complementary-U witnesses actually selected across the y outside sources, and put `w=|W|`.

Every outside source needs at least `k_P=3t` distinct U witnesses, hence

> `3t<=w<=4t`.                                             `(1.1)`

Every selected witness has code `bar d`. Because the A-cut is complete, a selected U witness can have only one neighbour in `A_X`: any second X-neighbour would be a second common neighbour with the source. Thus every vertex `z in W` has exactly one X-neighbour, denote it `h(z)`.

Across all `y=t` sources there are at least

> `I>=yk_P=3t^2`                                          `(1.2)`

selected source-witness incidences. Each such incidence is a Y--W nonedge. Therefore, writing `Z_Y(W)` for the number of Y--W nonedges,

> `Z_Y(W)>=3t^2`.                                         `(1.3)`

## 2. Used complementary witnesses are independent

All vertices of W have code `bar d`.

Suppose `zz'` were an edge of `G[W]`. Raw same-code criticality for a U--U edge says that, after orienting the edge, its source may be taken as one endpoint, say z, and its unique-common-neighbour witness must lie in `A_d=Y`; call it y. The certificate would require

> `N(z) cap N(y)={z'}`.

But z is a selected crossing witness, so it has the unique X-neighbour `h(z)`. The rigid A-cut is complete, hence every `y in Y` is adjacent to every vertex of `A_X`, in particular to `h(z)`. Therefore

`h(z) in N(z) cap N(y)`.

Since `h(z) in A_X` whereas `z' in U`, this is a second common neighbour, contradicting the certificate.

Thus

> **`e(W)=0`.**                                            `(2.1)`

This is strictly stronger than the generic same-code capacity `e(W)<=wy`: the singleton X-head forced by the rigid crossing certificate blocks every possible Y-witness for a same-code W-edge.

No assumption is made that all complementary U vertices are used, and no assumption is made that the same witness set is used by every Y-source.

## 3. Exact degree repricing

For `z in U`, the preserved degree identity is

> `d_{A union U}(z)=p+u-1-epsilon_z=7t-1-epsilon_z`.

For W:

- its total X-degree is exactly w;
- its Y-edge count is at most `wt-3t^2` by `(1.3)`;
- `G[W]` is independent by `(2.1)`;
- its U-neighbours outside W contribute at most `w(4t-w)` incidences.

Hence

`w(7t-1)-E_W`
`<=w+(wt-3t^2)+w(4t-w)`.

Rearranging,

> `E_W >= w(2t+w-2)+3t^2`.                               `(3.1)`

Since `w>=3t` and `t>=2`, the right side is minimized at `w=3t`, so

> **`E_W >= 18t^2-6t`.**                                  `(3.2)`

This is a major strengthening of the earlier aggregate witness-class floor `9t^2+5t-2`. It is fully physical: it uses the actual selected witness incidences, their forced singleton X-neighbourhoods, their forced Y-nonedges, and raw same-code criticality.

## 4. The infinite ray collapses to a finite tail

The independent near-rigid Hamming-slot floor on `A_X` is

> `L_X>=floor(4t^2-3t/2)+1`.                              `(4.1)`

Thus

> `S>=18t^2-6t+floor(4t^2-3t/2)+1`.                       `(4.2)`

The above-M ceiling is

> `C0=20t^2+10t-4`.                                       `(4.3)`

Direct comparison gives

> `18t^2-6t+floor(4t^2-3t/2)+1 > C0`

for every

> **`t>=9`.**                                              `(4.4)`

Therefore the explicit infinite scalar escape family is **not** physically viable asymptotically:

> **the ray is closed for t>=9, leaving only the finite parameter tail `2<=t<=8` for any further realization test.**

Equivalently, on this ray the conditional order `n=16t+1` is at most 129.

This is exactly the kind of structural gain the scalar diagnostics were pointing toward: the aggregate `Ccap_P/(ONE-P)/(CROWD)` inequalities all had room, but the *location* of the selected U witnesses makes their same-code edges impossible and doubles the leading witness-slack price.

## 5. Trust boundary

This is still conditional on the rigid one-code interface and the preceding source/Hall machinery. No positive actual-D2C rigid complete Hall-cut fixture with `x>=3` is known in bounded regression, and `X_3` remains the mandatory negative control. The finite tail `2<=t<=8` is not declared realizable; it is simply not excluded by `(4.2)` alone.
