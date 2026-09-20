# One-code near-rigid cut — linear rooted-gap necessity

Date: 2026-09-20

Status: **same-session analytic structural theorem**, conditional on the exact rigid Hall interface, one-code outside layer and the repaired singleton-witness machinery. The theorem does not assert that the rigid interface is graph-realizable; the zero-positive-fixture caveat remains binding.

The previous two notes show that the rooted gap

`c=lambda+1-g0`, `g0=p-y`,

has a direct physical meaning: a minimum outside source can leave at most c U-vertices outside its selected complementary singleton-witness class. The new W-class same-code criticality bill is quadratic when that class becomes large.

This note turns that observation into a global dichotomy:

> **a large-order one-code rigid near-rigid survivor must have c linear in the graph order.**

Thus the zero-fixture problem is reduced further: bounded c is not an asymptotic escape direction.

## 1. Minimum-source parameterization

Fix a source `s in Y=A_d` with minimum selected U-witness count `k`. Put

`d:=u-k`.

The rooted one-code occupancy and distinct-head theorems give

> `0<=d<=c`.                                              `(LG-1)`

The selected matched-covered head count is

> `m=x-k=p-c+d`.                                          `(LG-2)`

The witness-class theorem gives

> `E_U>=max{`
> ` k(p-1),`
> ` k(g0+k-1)-2(y-1)(k-1)`
> `}`.                                                    `(LG-3)`

The selected matched heads force gamma-collision A-slack

> `L_A>=phi(m)`,                                          `(LG-4)`

where `phi(m)=m(m-1)` for `m>=3` and zero for `m<=2`.

## 2. Averaged branch lower bound

For the moment assume `m>=3`. Since `max(A,B)>=(A+B)/2`, every actual branch d satisfies

`2(E_U+L_A)`
` >= k(p-1)`
`    +k(g0+k-1)-2(y-1)(k-1)`
`    +2m(m-1)`.                                          `(LG-5)`

Write

`lambda=g0+c-1=p-y+c-1`.

The exact above-M score ceiling has the convenient parity-free form

> `C0=(lambda+2)(p+u)+p-A_lambda`,                        `(LG-6)`

where

> `A_lambda=floor(lambda^2/2)+lambda+4+(lambda mod 2)`,
>
> `2A_lambda>=lambda^2+2lambda+8`.                        `(LG-7)`

Substituting `k=u-d`, `m=p-c+d` into `(LG-5)` and subtracting `2C0`, then using `(LG-7)`, gives the lower quadratic

`D(u)`
`=u^2-u(y+2+2c+2d)`
` +3c^2-4cd-4cp-2cy+2c`
` +3d^2+2dp+3dy-2d`
` +p^2-6p+y^2+2y+5`.                                    `(LG-8)`

Any above-M survivor in this branch must have `D(u)<=0`.

## 3. Large p is impossible relative to c

Minimize `(LG-8)` over real u. Multiplying the resulting minimum by four gives

`N=`
` 8c^2-24cd-16cp-12cy`
` +8d^2+8dp+8dy-16d`
` +4p^2-24p+3y^2+4y+16`.                                `(LG-9)`

Use only `0<=d<=c`, dropping nonnegative `8d^2+8dp+8dy`, and minimize the remaining y-quadratic over the reals:

`3y^2+(4-12c)y >= -(12c-4)^2/12`.

This yields the safe lower bound

> `N >=`
> ` 4p^2-(16c+24)p-28c^2-8c+44/3`.                       `(LG-10)`

For `c>=1`, evaluate the right side at `p=6c+5`:

`4(15c^2+6c-4)/3>0`.

Its derivative in p is already positive there. Therefore `(LG-10)` is strictly positive for every

`p>=6c+5`.

In that range `(LG-2)` gives

`m>=p-c>=5c+5>=3`,

so the quadratic collision formula used above is valid. Hence:

> **`c>=1` and survival imply `p<=6c+4`.**                `(LG-P)`

This is analytic and uniform in u,y,d.

## 4. U cannot outrun p and c

A second bound needs no collision term.

If `u<=c`, there is nothing to prove. Otherwise put

`t:=u-c=x-p>0`.

The distinct-head theorem gives `k>=t`. Expanding the same-code W bill in `(LG-3)`,

`E_same(k)`
`=k^2+(3g0-2p+1)k+2y-2`
`>=k^2-(2p-4)k`,                                         `(LG-11)`

because `g0>=1` and `y>=1`.

If `t<=2p-4`, then immediately `t<4p+2c`.

If `t>2p-4`, the quadratic `z^2-(2p-4)z` is increasing for every integer `z>=t`, so

> `E_U>=t^2-(2p-4)t`.                                    `(LG-12)`

On the other hand `(LG-6)` and `lambda<=p+c-2` imply the generous ceiling

> `C0 <= (p+c)(p+u)+p`.                                  `(LG-13)`

Therefore a survivor in the second case must satisfy

`t^2-(3p+c-4)t-(p+c)^2-p <=0`.                           `(LG-14)`

At

`t=4p+2c`

the left side is exactly

`3p^2+4pc+c^2+15p+8c>0`.

Since the quadratic is negative at t=0 and opens upward, `(LG-14)` forces

> **`t<4p+2c`, hence `u<4p+3c`.**                         `(LG-U)`

This includes the first case as well.

## 5. Linear gap-versus-order theorem

Combine `(LG-P)` and `(LG-U)` for `c>=1`:

`p<=6c+4`,

`u<=27c+15` (integer form of `u<4p+3c`).

Also `lambda=g0+c-1>=c`. Since

`n=4p+2u-lambda`,

we obtain

> **`n<=77c+46`.**                                        `(LG-N)`

Equivalently, every one-code rigid near-rigid survivor of order n with c>=1 must satisfy

> **`c >= ceil((n-46)/77)`.**                             `(LG-LIN)`

Together with the separately proved c=0 bound `n<=18`, this has the structural interpretation:

> **bounded rooted gap cannot support an unbounded one-code rigid family. Any hypothetical large-order rigid fixture must drive `c=lambda+1-g0` to infinity at least linearly with n.**

The constants 77 and 46 are intentionally conservative. They come from transparent analytic relaxations, not numerical optimization.

## 6. Why this changes the next attack

The remaining asymptotic escape is no longer an arbitrary one-code family. It is a **large-gap** family in which

- the root imbalance contribution `lambda+1` substantially exceeds the local complete-cut offset `g0`;
- c itself is a linear-order resource;
- the minimum outside source still leaves at most c U vertices outside its complementary singleton-witness class;
- exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` must now be tested in a regime where c is macroscopic rather than treated as an unstructured slack parameter.

This suggests a sharper next dichotomy: compare c directly with x and y. If c is a small fraction of x, `(WC-8)` gives a strong quadratic W-class bill; if c is a large fraction of x, the imbalance lambda is itself large and should be fed into the exact rooted residual/defect expression before pair slack is aggregated.

## 7. Trust boundary

The only new graph-theoretic input is the W-class same-code crowding theorem proved in `ONE_CODE_NEAR_RIGID_WITNESS_CLASS_CROWDING.md`. Everything else here is exact substitution, the elementary inequality `max(A,B)>=(A+B)/2`, and deliberately generous relaxations of the standard above-M score ceiling.

No finite scan is used in `(LG-P)`, `(LG-U)` or `(LG-N)`. The actual-D2C positive-fixture gap remains unresolved, and `X_3` remains outside this rigid one-code interface.