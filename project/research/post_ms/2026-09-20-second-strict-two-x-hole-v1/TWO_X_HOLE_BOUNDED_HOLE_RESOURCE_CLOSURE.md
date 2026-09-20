# Two-X-hole branch — analytic large-x closure of the bounded hole-resource arm

Date: 2026-09-20

Status: **same-session internal analytic closure** inside the core-saturated exact second-strict two-X-hole branch (`y>=2`, `x>=4`). This reuses the exact positive-combination calculation from `TWO_X_HOLE_NO_HOLE_CODE_CLOSURE.md` and the physical localization `e(G[X]),e(G[U_o])<=M_H`. No finite scan is used as proof.

## 1. Setup

Retain the core-saturated two-X-hole notation:

- `omega=|U_o|`;
- certificate-incidence load `L`;
- `M=M_H=m_{H_0}+m_{H_1}`;
- `e_X=e(G[X])<=M`;
- `e_o=e(G[U_o])<=M`;
- `u=x+1+omega`, `lambda=2p+omega-y`;
- `P=[omega(p-x)+2L]_+`.

The no-hole-code closure defined score and rooted margins `A_0,B_0` by setting `e_X=e_o=0` and proved the exact identity

> `A_0+3B_0=-F`,                                         `(B-COMB0)`

where

`F=8L+P-2eps`
`  +3p^2+2p omega-3py-8p`
`  +omega^2-4omega x+omega y-8omega`
`  +5x^2-3xy-10x+2y^2+4y+20`,                           `(B-F)`

with `eps in {0,1}` the parity remainder.

The same note proves `F>=3` everywhere in the branch.

## 2. The distinguished resource can improve the two margins by at most 2M and 3M

The exact X-slack ledger is

`L_X>=x(p+x-y)-(x-2)+L-2e_X`.

Relative to the `e_X=0` baseline, allowing `e_X<=M` can lower the score floor by at most `2M`. Therefore the best possible score margin in a geometry with distinguished resource M satisfies

> **`A<=A_0+2M`.**                                        `(B-A)`

For the rooted margin, two rebates are possible relative to the zero-resource baseline:

1. `e_o<=M` can increase the rooted U-edge ceiling q by at most M;
2. lowering `L_A` through `e_X<=M` can increase the available U-slack cap by at most `2M`.

Hence

> **`B<=B_0+3M`.**                                        `(B-B)`

The forward-routing surcharge from `TWO_X_HOLE_HOLE_CLASS_FORWARD_SURCHARGE.md` only makes these bounds stricter, so it is safe to omit it here.

If a graph survives, its actual margins satisfy `A>=0` and `B>=0`. Thus necessarily

> `0<=A+3B`
> ` <=A_0+3B_0+11M`
> ` =-F+11M`.                                             `(B-NEC)`

Therefore every survivor must obey

> **`F<=11M`.**                                           `(B-FCAP)`

This converts the two physical density rebates into a fixed budget against the exact positive-combination obstruction.

## 3. A uniform large-x lower bound: F>=96 for x>=14

We now strengthen the predecessor's `F>=3` only in the range `x>=14`.

As in `TWO_X_HOLE_NO_HOLE_CODE_CLOSURE.md`, use

- `P>=0`;
- `eps<=1`;
- `L>=max(x-2,omega)`.

This gives the lower relaxation `F>=F_0`. Completing the square in y there gives

> `F_0=2(y-y_*)^2+N/8`,                                  `(B-SQY)`

where

`N=64 max(x-2,omega)`
`  +15p^2+22p omega-18px-40p`
`  +7omega^2-26omega x-72omega`
`  +31x^2-56x+128`.

The predecessor minimizes N in p using

`p_*=(9x+20-11omega)/15`.

For `x>=14`, its four relevant lower bounds are:

1. if `p_*<=1` and `omega>=x-2`,

   `N/8 >= 6(x^2-7x+14)/7`;

2. if `p_*<=1` and `omega<=x-2`,

   `N/8 >= (12x^2-36x+103)/8`;

3. if `p_*>1`, `omega<=x-2`, and the `omega=x-2` endpoint is active,

   `N/8 >= 2(11x^2-27x+51)/15`;

4. if the `p_*>1` boundary `omega=(9x+5)/11` is active,

   `N/8 >= 2(109x^2-435x-350)/121`.

The remaining predecessor subcase `p_*>1, omega>=x-2` can occur only for `x<=13`, so it is absent here.

Each of the four displayed lower bounds is increasing for `x>=14`. At `x=14` they are respectively

- `96`;
- `243.875`;
- `243.866...`;
- `246.677...`.

Since the square term in `(B-SQY)` is nonnegative,

> **`F>=96` for every integer parameter row with `x>=14`.** `(B-F96)`

This is an analytic bound inherited from the predecessor's completed-square proof, not a finite-box extrapolation.

## 4. Closure when M<=8

`TWO_X_HOLE_MATCHED_ROUTING_CAPACITY.md` proves that if every represented physical hole code has agreement size at least two, then each distinguished witness class has size at most four. Therefore

> `M<=8`.                                                  `(B-M8)`

If also `x>=14`, then `(B-FCAP)` and `(B-F96)` would require simultaneously

`96<=F<=11M<=88`,

impossible.

Hence:

> **BOUNDED-RESOURCE LARGE-X CLOSURE.** In the core-saturated exact second-strict two-X-hole branch, if every represented hole code has `|I_C|>=2`, then
>
> **`x<=13`.**                                            `(2X-BOUNDED-X13)`

Equivalently, every survivor with

> **`x>=14`**

must contain a represented physical hole code C with

> **`|I_C|=1`, equivalently `d_H(C,d)=p-1`.**             `(2X-EXTREME-NEC)`

Thus the large-x two-X-hole problem has now collapsed completely to the extreme-radius arm.

## 5. Interaction with the new forward surcharge

The proof above deliberately ignored the new `F_H` surcharge, so `(2X-BOUNDED-X13)` is conservative.

Whenever a represented hole class approaches its routing-capacity maximum, the forward-surcharge theorem additionally gives

- `E_core>=x(p+x-1)+L+F_H`;
- `L_X>=x(p+x-y)-(x-2)+L+F_H-2e_X`;
- `q<=(x+1)omega-L-F_H+M`;
- `E(U_o)>=[omega(p-x)+2L+2F_H]_+`.

All four changes move against feasibility. They can be used later to shrink the explicit `4<=x<=13` structural tail, but they are not needed for the eventual large-x conclusion.

## 6. Strategic consequence

The large-x two-X-hole branch no longer has two arms. For `x>=14`, the bounded distinguished-resource arm is analytically empty. Every survivor must lie in the radius-`p-1` represented-hole-code geometry, where the local Hamming-slot theorem supplies

`r>=x+y[1+ceil(N_ext(p-2)/x)]`

and every witness beyond the first two in an extreme hole class produces the forward physical surcharge.

The next proof target is therefore precise:

> **close or classify the extreme-radius hole-code arm, keeping its class populations `(n_C,m_C,L_C)` and forward surcharge explicit.**

A bounded scan of `x<=13` may be useful as a diagnostic later, but it is no longer relevant to the eventual large-x theorem.

## 7. Audit notes

The load-bearing new point is only `(B-A)/(B-B)`: the same distinguished physical resource M can improve the score margin by at most `2M` and the rooted margin by at most `3M`. The completed-square lower bounds are copied algebraically from the already-preserved no-hole-code proof and specialized to `x>=14`.

Independent arithmetic spot-checks over positive integers `(m,s)` and broad parameter boxes were used only to look for sign mistakes; the closure itself is analytic.