# Physical witness-incidence repricing on the explicit escape ray

Date: 2026-09-20

Status: same-session structural diagnostic, conditional on the rigid one-code interface and the parameter ray already preserved. This is not a graph construction.

## 1. Setup

Use

`p=3t, y=t, u=4t, x=5t, g_P=2t, k_P=3t`, `t>=2`.

Let `W` be the union of distinct complementary-U witnesses actually selected across the y outside sources, and put `w=|W|`.

Every outside source needs at least `k_P=3t` distinct U witnesses, hence

> `3t<=w<=4t`.                                             `(1.1)`

Every selected witness has code `bar d`. Because the A-cut is complete, a selected U witness can have only one neighbour in `A_X`: any second X-neighbour would be a second common neighbour with the source. Thus every vertex of W has exactly one X-neighbour.

Across all y=t sources there are at least

> `I>=yk_P=3t^2`                                          `(1.2)`

selected source-witness incidences. Each such incidence is a Y--W nonedge. Therefore, writing `Z_Y(W)` for the number of Y--W nonedges,

> `Z_Y(W)>=3t^2`.                                         `(1.3)`

## 2. Same-code W-edge capacity

All vertices of W have code `bar d`. For every same-code edge inside W, raw same-code criticality orients the edge with its source in W and a witness in `A_d=Y`. The usual ordered `(source,witness)` injection therefore applies to this restricted edge family and gives

> `e(W)<=w y = wt`.                                       `(2.1)`

No assumption is made that all complementary U vertices are used, and no assumption is made that the same witness set is used by every Y-source.

## 3. Exact degree repricing

For `z in U`, the preserved degree identity is

> `d_{A union U}(z)=p+u-1-epsilon_z=7t-1-epsilon_z`.

For W:

- its total X-degree is exactly w;
- its Y-edge count is at most `wt-3t^2` by `(1.3)`;
- its U-edge incidence count is at most `2e(W)+w(4t-w)`.

Hence

`w(7t-1)-E_W`
`<=w+(wt-3t^2)+2e(W)+w(4t-w)`.

Rearranging,

> `E_W >= w(2t+w-2)+3t^2-2e(W)`.                         `(3.1)`

Using `(2.1)`,

> `E_W >= w(w-2)+3t^2`.                                   `(3.2)`

Since `w>=3t` and `t>=2`, the right side is minimized at `w=3t`, so

> **`E_W >= 12t^2-6t`.**                                  `(3.3)`

This is a strictly stronger physical price than the earlier aggregate witness-class floor `9t^2+5t-2` for all sufficiently large t. It does not assume witness-population saturation `w=k_P`; it allows the selected witness union to range all the way up to u=4t.

## 4. The ray still survives total score

The independent near-rigid Hamming-slot floor on `A_X` is

> `L_X>=floor(4t^2-3t/2)+1`.                              `(4.1)`

Thus the strengthened physical total-score floor is

> `S>=12t^2-6t+floor(4t^2-3t/2)+1`.                       `(4.2)`

The above-M ceiling remains

> `C0=20t^2+10t-4`.                                       `(4.3)`

Their difference is positive for every `t>=2` and grows quadratically; asymptotically the lower floor has leading coefficient 16 while C0 has leading coefficient 20.

Therefore:

> **even after charging the actual selected witness incidences, their forced Y-nonedges, exact singleton X-neighbourhoods, and restricted same-code W-edge capacity, the explicit ray remains scalar-feasible.**

This materially narrows the missing mechanism. Another score-only aggregation is not the right next step. The next attack must use the *location* of those nonedges/edges in the rooted residual identity, stronger per-vertex reuse structure, or prove that the rigid complete-cut event itself is not graph-realizable.

## 5. Trust boundary

No D2C graph realizing this pattern is known. Bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, and `X_3` remains the mandatory negative control. This note is a conditional structural/method diagnostic only.
