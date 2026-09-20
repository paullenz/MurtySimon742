# Two-X-hole branch — analytic closure when neither hole code is represented

Date: 2026-09-20

Status: **same-session internal analytic closure** inside the core-saturated exact second-strict two-X-hole branch (`y>=2`, `x>=4`). This uses the physical incidence / edge-localization theorems preserved in the companion notes. No finite parameter scan is used as proof.

## 1. Structural arm

Let the two physical hole codes be

`H_j=c(a_j)`, `j=0,1`.

Assume neither hole code is represented among the actual buffer heads `R=X\{a_0,a_1}`. Equivalently

`m_{H_0}=m_{H_1}=0`,

because every physical outside vertex belongs to the complementary witness class of at least one represented R-head code.

Put

`M_H=m_{H_0}+m_{H_1}=0`.

The two localization theorems immediately give

> `G[X]=emptyset`,                                        `(NH-X0)`
>
> `G[U_o]=emptyset`.                                      `(NH-UO0)`

Thus this arm has no internal X-density and no internal outside-U density left to trade against the score/rooted ledgers.

Let

- `omega=|U_o|>=1`;
- `L=|E(J)|` be the certificate-incidence load.

Every R-head and every outside vertex is incident in J, so

> `L>=max(x-2,omega)`.                                    `(NH-L)`

The core/head bijection has `g=0`, `k=x`, hence

`u=x+1+omega`,

`lambda=2p+omega-y>=0`.

## 2. Physical score and rooted floors

From the incidence ledger:

> `E_core>=x(p+x-1)+L`,
>
> `epsilon_b=p+2`,
>
> `E(U_o)>=P:=[omega(p-x)+2L]_+`.                         `(NH-U)`

Because `G[X]=emptyset`, the exact aggregate X-slack ledger becomes

> `L_X>=x(p+x-y)-(x-2)+L`.                               `(NH-LX)`

The Y-price is exact:

> `L_Y=y(p+1+omega)`.                                    `(NH-LY)`

Hence, with the standard score cap `C0`, define the necessary score margin

> `A=C0-S_min`,                                          `(NH-A)`

where

`S_min=x(p+x-1)+L+(p+2)+P`
`      +x(p+x-y)-(x-2)+L+y(p+1+omega)`.

A survivor requires `A>=0`.

Since `G[U_o]=empty`, the rooted U-edge ceiling is linear:

> `q<=(x+1)omega-L`.                                     `(NH-Q)`

The complete X--Y cut joins unequal tight codes. With `G[X]=G[Y]=empty`, the local Hamming-slot theorem gives at least one unused rooted slot at every A-vertex:

> `r>=x+y`.                                               `(NH-RLOW)`

Using `E_U<=C0-L_A` in the exact rooted identity

`r=(p-lambda)(p+u)+q+E_U`,

define the necessary rooted margin

> `B=(p-lambda)(p+u)+(x+1)omega-L`
> `  +C0-[x(p+x-y)-(x-2)+L+y(p+1+omega)]-(x+y)`.          `(NH-B)`

A survivor requires `B>=0`.

## 3. A fixed positive combination is impossible

Write `eps in {0,1}` for the parity remainder in

`floor((n-1)^2/4)=((n-1)^2-eps)/4`.

Direct exact expansion gives

> **`A+3B=-F`**,                                          `(NH-COMB)`

where

`F=8L+P-2eps`
`  +3p^2+2p omega-3py-8p`
`  +omega^2-4omega x+omega y-8omega`
`  +5x^2-3xy-10x+2y^2+4y+20`.                           `(NH-F)`

We prove

> **`F>=3`.**                                             `(NH-FPOS)`

This contradicts `A>=0` and `B>=0` immediately.

## 4. Proof that F>=3

Since `P>=0`, `eps<=1`, and `L>=max(x-2,omega)`, it is enough to prove

`F_0:=8 max(x-2,omega)-2`
`     +3p^2+2p omega-3py-8p`
`     +omega^2-4omega x+omega y-8omega`
`     +5x^2-3xy-10x+2y^2+4y+20`

satisfies `F_0>=3` for integers `p>=1`, `x>=4`, `y>=2`, `omega>=1`.

Complete the square in y. Put

`y_*=(3p-omega+3x-4)/4`.

Then

> `F_0=2(y-y_*)^2+N/8`,                                 `(NH-SQY)`

with

`N=64 max(x-2,omega)`
`  +15p^2+22p omega-18px-40p`
`  +7omega^2-26omega x-72omega`
`  +31x^2-56x+128`.                                     `(NH-N)`

It therefore suffices to show `N>=24`, apart from any tiny integer cases where the real y-minimum lies between integers.

### 4.1 Minimize N in p

As a real quadratic in p, its unconstrained minimizer is

`p_*=(9x+20-11omega)/15`.

#### Case A: `p_*<=1`

The minimum over `p>=1` occurs at p=1.

If `omega>=x-2`, then

`N>=7omega^2-26omega x+14omega+31x^2-74x+103`.

Its unconstrained real minimum in omega is

`48(x^2-7x+14)/7`.

For `x>=5` this is already greater than 24. For `x=4`, direct integer inspection under `p_*<=1` leaves only the two real-y exceptions

`(p,x,omega)=(1,4,6),(1,4,7)`

with `N<24`.

If instead `omega<=x-2`, then `p_*<=1` can occur only once x is large enough for the intervals to overlap. The p=1 expression is decreasing in omega throughout `omega<=x-2`, so

`N>=N|_{omega=x-2}=12x^2-36x+103>24`.

#### Case B: `p_*>1`

Use the unconstrained real p-minimum. It equals

`N_min=(16/15)G`,

where

`G=60 max(x-2,omega)-omega^2-12omega x-40omega`
`  +24x^2-75x+95`.

If `omega<=x-2`, G is decreasing in omega. When the endpoint `x-2` lies below `p_*=1`,

`G>=11x^2-27x+51>22.5`.

When the condition `p_*>1` cuts off omega first, use the real boundary

`omega=(9x+5)/11`; there

`G=15(109x^2-435x-350)/121>22.5`

throughout the relevant `x>=14` range.

If `omega>=x-2`, the condition `p_*>1` forces `x<=13`. Here G is again decreasing in omega, so at the real boundary `omega=(9x+5)/11`,

`G=15(109x^2-523x+838)/121`.

This quadratic is increasing for `x>=4` and at x=4 already exceeds 22.5. Thus `N_min>24`.

### 4.2 The two integer exceptions

For `(p,x,omega)=(1,4,6)`, the allowed integers `y>=2` give minimum

`F_0=3` at `y=2`.

For `(1,4,7)`, the minimum is

`F_0=4` at `y=2`.

Therefore `(NH-FPOS)` holds in every case.

## 5. Closure

If a graph in this arm existed, its score and rooted ledgers would require

`A>=0`, `B>=0`,

hence

`A+3B>=0`.

But `(NH-COMB)` and `(NH-FPOS)` give

`A+3B=-F<=-3`.

Contradiction.

Therefore:

> **NO-HOLE-CODE CLOSURE.** In the core-saturated exact second-strict two-X-hole branch with `y>=2,x>=4`, at least one physical hole code must be represented among the actual buffer-head codes. `(2X-HOLE-CODE-NECESSARY)`

Equivalently every surviving geometry has

> **`M_H=m_{H_0}+m_{H_1}>=1`.**                          `(2X-MH-POS)`

This is a structural narrowing, not merely a score inequality: all surviving X- and U_o-density is now forced to route through a witness class complementary to an actual physical hole code.

## 6. Next target

The only large two-X-hole geometries left are the **hole-code represented** cases. The two-foot routing theorem should now be specialized to a head class C equal to `H_0` or `H_1`.

For such a class its complementary outside witnesses are exactly the distinguished resource that simultaneously pays

- all possible internal X-edges;
- all possible internal U_o-edges;
- the ordinary buffer certificate load;
- the located core--outside holes.

The next theorem should determine whether a witness of code `bar H_j` can serve a head of code `H_j` while also routing that head's agreement set through the two physical holes without creating an additional singleton collision.