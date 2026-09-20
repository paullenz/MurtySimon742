# Residual-one k=2: general H--U orientation capacity and H-slack

Date: 2026-09-20

Status: **same-session conditional theorem**, extending the corrected half-ray B-layer argument to the full residual-one `k=2`, `J2=empty`, `y>0` parameter domain. It is downstream of the unresolved rigid complete Hall-cut interface and does not establish graph-level reachability.

## 1. General residual-one identities

For `k=2`, residual dimension one and `J2=empty`, the exact identities are

- `x=p+1`,
- `u=c+1`,
- `|H|=h=p-1`,
- `lambda=c+p-y-1`,
- `c(h_i)=d xor e_i` for every private head,
- `E(K,H)=empty`.

Assume `p>=4` and `y>0`.

The root has degree `b=2p+u`. For `h_i in H`, let `m_i` be its number of missing H-neighbours. Then

`d_H(h_i)=p-2-m_i`,

and exact degree bookkeeping gives

`epsilon_i=2p+u-[p+y+d_H(h_i)+d_U(h_i)]`.

Hence

> **`d_U(h_i)=u-y+2+m_i-epsilon_i`.**                    `(GH-LOCAL)`

Summing,

> **`e(H,U)=2M_H+h(u-y+2)-L_H`,**                        `(GH-GLOBAL)`

where `M_H=binom(h,2)-e(H)`.

## 2. Orientation capacity is parameter-free

The corrected H--U classification from the half-ray uses only

- both U and all matched endpoints belonging to the rooted B-layer;
- the `J2=empty` A-code repertoire;
- `E(K,H)=empty`;
- `y>0` to rule out the matched endpoint opposite h_i in its own coordinate;
- the two selected `bar d` witnesses, which are H-free;
- fixed-pair singleton uniqueness.

Therefore it applies unchanged in the variable parameter domain.

Every H--U edge is accounted for by one of the following mutually capacity-controlled mechanisms:

1. reverse private-coordinate matched witness `q_l`, `l!=i`, which consumes a directed H-hole: total at most `2M_H`;
2. reverse residual matched witness `q_j`: at most one per H-source, total at most h;
3. triangle-free endpoint in `U_{bar d xor e_i}`;
4. reverse-U witness in `U_{bar d xor e_i}`;
5. U-sourced A_X witness from an endpoint-indexed class `U_{bar d xor e_l}`;
6. U-sourced Y witness from a `bar d` vertex of H-degree exactly one.

The last four uses live in disjoint-or-incompatible physical roles inside U. Because the two selected witnesses `W_s subseteq U_bar(d)` have H-degree zero and belong to none of these roles, their combined capacity is at most `u-2`.

Thus

> **`e(H,U) <= 2M_H+h+u-2`.**                            `(GH-CAP)`

## 3. Exact general H-slack theorem

Combine `(GH-GLOBAL)` and `(GH-CAP)`:

`2M_H+h(u-y+2)-L_H <= 2M_H+h+u-2`.

The missing-H currency cancels exactly. Therefore

> **`L_H >= h(u-y+1)-u+2`.**                             `(GH-SLACK)`

Using `h=p-1` and `u=c+1`,

> **`L_H >= (p-1)(c-y+2)-c+1`.**                        `(GH-SLACK2)`

Of course `L_H>=0`, so the useful statement is the maximum of the right side with zero.

On the corrected intermediate half-ray `c=y=t`, this specializes to

`L_H>=3t-1`,

exactly the replacement theorem already proved there.

## 4. New asymptotic score term

For a bounded-ratio sequence write

`kappa=c/p`, `theta=y/p`.

Whenever `kappa>theta`, `(GH-SLACK2)` gives

> **`L_H/p^2 >= kappa-theta-o(1)`.**                     `(GH-NORM)`

The existing off-ray score theorem used only the Y-side lower bound `L_A/p^2>=Y0-o(1)`. Since H- and Y-slack are disjoint parts of `L_A`, the corrected orientation theorem strengthens that to

> **`L_A/p^2 >= Y0+(kappa-theta)_+-o(1)`.**              `(GH-LA)`

Accordingly every bounded-ratio survivor of the `k=2`, `J2=empty`, `y>0` branch must satisfy the strengthened normalized score condition

> **`F_H := F+(kappa-theta)_+ <= S0`,**                  `(GH-SCORE)`

where the predecessor quantities are

`F=Z0+Y0+kappa(kappa-theta)-2q`,

`S0=((1+kappa)^2-theta^2)/2`.

This is a genuinely new leading-order restriction whenever `c-y` is linear in p. It does not affect the leading coefficient on the half-ray `kappa=theta=1/2`, where the exact theorem still supplies the lower-order linear term `3p/4+O(1)`.

## 5. Structural interpretation

The theorem explains why the H-density itself disappeared from the corrected half-ray attack. Missing H-edges create exactly two units of additional H--U degree in `(GH-GLOBAL)`, but the same directed H-holes create exactly two reverse `q_l` certificate slots in `(GH-CAP)`. Those terms cancel. What remains is a pure slack requirement controlled by the size mismatch between U and Y.

Thus trying merely to make H sparser cannot evade H--U criticality: every missing H-edge increases both the required H--U load and the available reverse matched capacity at the same rate. Any further improvement must come from showing that the apparent reverse slots cannot all be saturated simultaneously, or that their U-heads collide with the endpoint-indexed / H--H certificate geometry.

## 6. Trust boundary and next target

This theorem does not repair the upstream realizability gap: bounded actual-D2C regression still has zero positive rigid complete-cut fixtures with `x>=3`, and `X_3` remains mandatory.

Within the conditional interface, the next high-value question is now sharp: characterize equality or near-equality in `(GH-CAP)`. A near-minimizer must simultaneously saturate directed H-holes by private matched reverse certificates, use almost every residual-hub source slot, and exhaust almost every U-vertex outside the two selected witnesses in exactly one endpoint-indexed or H-degree-one role. That simultaneous saturation should be attacked directly rather than by another undifferentiated scalar inequality.