# Small matched-head one-code branch — rooted-Q collapse

Date: 2026-09-21

Status: same-session analytic theorem inside the rigid complete one-code interface. It addresses the previously listed `m<=1` regime directly using the exact rooted-Q feedback inequality. It remains conditional on reaching the rigid interface.

## 1. Setup

Let `Y=A_d` be a repeated outside block, `y>=2`, and put `g0=p-y`, so `1<=g0<=p-2` in the large-gap regime. Use

`c=lambda+1-g0`,

`x=p+u-c`,

and for a minimum outside source let

`d:=u-k>=0`,

`m=x-k=p-c+d`.

This note treats `m in {0,1}`. Therefore

`c=p-m+d`,

`lambda=g0+p-m+d-1`.

The exact order identity is

`n=4p+2u-lambda`.

## 2. Start from the exact rooted-Q inequality

For `m<=1`, the matched collision term `phi(m)` vanishes. The preserved rooted-Q feedback inequality is

`(u-d)(x+y-1)`

`<= u(p-lambda)+2du-d(d+1)+C0`,                      `(2.1)`

where

`C0=(lambda+2)(p+u)+p-A_lambda`,

and

`2A_lambda >= lambda^2+2lambda+8`.

Substitute

`x=p+u-c`, `y=p-g0`, `c=p-m+d`, `lambda=g0+p-m+d-1`.

Moving the right side of `(2.1)` to the left gives

`D(u)=A_lambda-g0 p+g0 d-g0 u+mp-md+mu`

`     -p^2-2pd-2p+2d^2-4du+2d+u^2-3u <=0`.        `(2.2)`

Replacing `A_lambda` by its parity-free lower bound can only decrease `D`, so a necessary condition is

`D_0(u)<=0`, where `D_0` is a monic quadratic in u with linear coefficient

`-g0+m-4d-3`.

Its discriminant is

> `Delta_Q = -g0^2+2g0m+6g0-m^2-6m`
> `          +2p^2+4pd+8p+6d^2+16d-5`.              `(2.3)`

This algebra was derived twice from `(2.1)`: once by direct expansion and once by substituting the exact small-m identities before collecting powers of u.

## 3. Uniform discriminant bound

For `m in {0,1}`, the g0-dependent block satisfies

`-g0^2+(2m+6)g0-m^2-6m <=9`.

Hence

`Delta_Q <= 2p^2+4pd+8p+6d^2+16d+4`.                 `(3.1)`

Moreover

`(2p+3d+2)^2`

minus the right side of `(3.1)` equals

`2p^2+8pd+3d^2-4d >=0`

for `p>=1,d>=0`. Therefore

> **`sqrt(Delta_Q) <= 2p+3d+2`.**                      `(3.2)`

Because an actual survivor must lie between the roots of `D_0`,

`2u <= g0-m+4d+3+sqrt(Delta_Q)`.

Using `g0<=p-2` and `(3.2)` gives

> **`2u <= 3p+7d+3`.**                                 `(3.3)`

This is substantially stronger in the small-matched-head regime than the general no-collision bound `u<4p+3c`.

## 4. Order collapse

Since `g0>=1`,

`lambda=g0+c-1>=c`.

Using `(3.3)` in the exact order identity,

`n=4p+2u-lambda`

` <=4p+(3p+7d+3)-c`

` =6p+6d+m+3`.

But `p+d=c+m`, so

> **`n <= 6c+7m+3`.**                                  `(4.1)`

Consequently:

- if `m=0`, **`n<=6c+3`**;
- if `m=1`, **`n<=6c+10`**.

Thus the entire repeated-code small matched-head branch satisfies

> **`n<=6c+10`.**                                      `(4.2)`

Equivalently, an unbounded family in this branch requires

> **`c >= ceil((n-10)/6)`.**                            `(4.3)`

This is stronger than the general repeated-code bound `n<=17c+22` proved in the companion compression note.

## 5. Interpretation

The previously isolated `m<=1` regime is not a weakly constrained escape direction. Small matched-head count forces almost all selected heads into U; the same selected U-witness population both creates located A--U holes and deletes rooted U--U triangle capacity. The exact rooted-Q identity then forces the rooted gap to be at least about one sixth of the entire graph order.

What remains special about `m<=1` is certificate geometry, not scalar feasibility.

## 6. Audit boundary

No reverse-gamma argument, H--U private-foot argument, finite scan, or audit-sensitive source-tuple capacity theorem is used. The derivation depends on the previously preserved rooted-Q feedback identity and the rigid one-code order identities. It does **not** prove graph-level reachability of the rigid interface.
