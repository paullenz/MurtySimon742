# Maximal-selection one-witness branch is empty for y>=2

Date: 2026-09-20

Status: internal conditional structural closure inside the audited first-strict unloaded branch. It combines the maximal representative normalization, all-R closure, all-F head saturation, exact U ledger, and the new internal-X collapse. The zero-positive-fixture rigid-cut caveat remains unchanged.

## 1. Setup reduced to two cases

Choose the outside certificates maximally as in `MAXIMAL_SELECTION_GENERIC.md`. If `m=1`, then `T=0`, `u=k+2` and `U_o={z}`. The all-R polarization is empty, so the graph is all-F.

Assume `y>=2`. Head saturation gives

`g in {0,1}`, `x=k+g`.

`MAXIMAL_M1_X_COLLAPSE.md` gives `e(X)=t<=g`, with t=0 forced when g=0. The exact U ledger gives

`E_U=(k+1)(p+k)+(p-g+1)` and `q=1`.

Every Y vertex is anticomplete to U and complete to X, so exactly

`epsilon_y=p-g+2`.

The exact X-score calculation is

`E_X=(x-1)(p+k-y)+p+k+1+g-y-2t`.

To obtain the weakest total score floor, put `t=g`.

The total available excess is

`C0=(lambda+3)p+(lambda+2)u-2 floor((lambda+1)^2/4)-4`,

with `lambda=2p-g-y+1`.

Write `d=p-y>=1`.

## 2. Score feasibility when g=0

Let `eta in {0,1}` record the parity of `lambda+1`. Direct substitution of the weakest exact degree ledger into `E_A+E_U<=C0` gives the necessary inequality

> `4k^2-4k-4p+(y+2)^2 <= eta <=1`.                    `(S0)`

Replacing `p=y+d`,

> `4d >= 4k^2-4k+y^2+3`.

Since `y>=2` and `k=x>=3`,

> `d >= k^2-k+2`.                                      `(D0)`

But the exact rooted identity from `MAXIMAL_M1_EXACT_LEDGER.md` is

`r=k^2+ky-p^2+py-p+2y`

and therefore

> `r=k^2+ky+y-d(d+y+1)`.                               `(R0)`

Using `(D0)`,

`d(d+y+1) >= (k^2-k+2)(k^2-k+y+3)`.

Subtracting the positive part in `(R0)`, the excess is at least

`k^4-2k^3 + y(k-1)^2 +5k^2-5k+6`,

which is strictly positive for `k>=3`, `y>=2`. Hence `r<0`, impossible because r counts unused rooted slots.

Thus g=0 is empty.

## 3. Score feasibility when g=1

Now `x=k+1>=3`, so `k>=2`. The weakest total score inequality simplifies exactly to

> `4k^2-4p+(y+1)^2 <= eta <=1`.                        `(S1)`

With `p=y+d`,

`4d >=4k^2+y^2-2y`.

For `y>=2`, this gives

> `d>=k^2`.                                             `(D1)`

The exact rooted identity is

> `r=k^2+k(y+1)+2y+1-d(d+y)`.                          `(R1)`

Using `d>=k^2`,

`d(d+y) >= k^2(k^2+y)`.

The difference between this lower bound and the positive terms in `(R1)` is

`k^4-k^2-k-1 + y(k^2-k-2)`,

which is strictly positive for `k>=2`, `y>=2` (the second term is nonnegative and the first is already positive at k=2). Hence again `r<0`, impossible.

Thus g=1 is empty.

## 4. Closure theorem

> **THEOREM. Under maximal valid outside-witness selection, no first-strict unloaded graph with m=1 and y>=2 exists.**

The proof is analytic and uses no finite parameter scan. It is stronger than the former all-F residual gate: the entire y>=2 one-witness branch closes by combining exact physical degrees with the nonnegativity of the rooted unused-slot count.

## 5. Remaining one-witness slice

The only maximal-selection m=1 possibility left is

> `y=1`, `T=0`, `U_o={z}`,

in the all-F polarization. The y=1 case was deliberately excluded from head saturation because a differing-fibre matched endpoint may certify an X--Y edge. It now becomes the unique live one-witness slice and should be attacked directly before moving to maximal `m>=2`.

All previous positive-T m=1 diagnostics are now historical conditional calculations for non-maximal representative choices; they are not live graph branches under the maximal-selection convention.
