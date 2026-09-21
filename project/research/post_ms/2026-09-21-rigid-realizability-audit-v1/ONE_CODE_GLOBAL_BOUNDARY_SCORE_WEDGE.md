# Global repeated-code boundary score wedge

Date: 2026-09-21

Status: exact/asymptotic consequence inside the repeated rigid one-code `m>=2` branch. It combines the raw boundary-witness theorem with the preserved score ceiling and independent U-bound. It remains conditional on reaching the rigid complete one-code interface.

## 1. Boundary-excess coordinates

Let `ell=|L|<=2`. Define the nonnegative boundary-forward excess

> `d := e-(p-ell) >=0`,                                `(1.1)`

where `e=u-k=c-r`.

Then

`e=p-ell+d`,

`c=p+r-ell+d`,

`u=p-ell+d+k`.

Using `lambda=c+g0-1`, define

> `s := r+g0+d-ell`,                                    `(1.2)`

so that

> `lambda=p+s-1`.                                       `(1.3)`

The live branch has `s+2>0`.

## 2. Exact score lower bound

The global boundary-witness theorem gives

`E_U >= (p-ell)(2p-ell-1)+k(p-1)`.

Since `S=L_A+E_U>=E_U` and an above-threshold candidate obeys

`S<=C0=(lambda+2)(p+u)+p-A_lambda`,

we obtain after substituting `(1.1)`--`(1.3)`:

> **`k(s+2) >= B+A_lambda-(p+s+1)(2p-ell+d)-p`,**       `(2.1)`

where

`B=(p-ell)(2p-ell-1)`.

Using

`2A_lambda >= lambda^2+2lambda+8`,

this yields the parity-free necessary inequality

> **`2k(s+2) >=`**
>
> **`(p-s)^2-8p+7`**
>
> **`-2d(p+s+1)+2ell^2-4ell p+2ell s+4ell`.**          `(2.2)`

For `ell=d=0`, `(2.2)` reduces to the earlier exact-population expression.

## 3. Independent upper bound on k

The preserved no-collision U-bound is

`u<4p+3c`.

Substituting the boundary-excess coordinates gives

`p-ell+d+k < 7p+3r-3ell+3d`,

hence, for integer k,

> **`k <= 6p+3r-2ell+2d-1`.**                           `(3.1)`

Equations `(2.1)` and `(3.1)` are a finite exact compatibility test for every repeated-code `m>=2` survivor.

## 4. Asymptotic macroscopic wedge

Consider an unbounded family and normalize

`rho=r/p`, `beta=g0/p`, `delta=d/p`,

and

> `sigma=rho+beta+delta`.                                `(4.1)`

Because `ell<=2`, the ell-terms disappear after division by `p^2`. Also

`lambda/p -> 1+sigma`,

`u/p = 1+delta+k/p+o(1)`.

Writing `kappa=k/p`, the score inequality has the asymptotic necessary form

> `2+kappa <= (1+sigma)(2+delta+kappa)-(1+sigma)^2/2`.   `(4.2)`

Equivalently,

> **`kappa sigma >= 1/2-delta-sigma-delta sigma+sigma^2/2`.** `(4.3)`

The U-bound gives

`kappa <= 6+3rho+2delta+o(1) <= 6+3sigma+o(1)`.          `(4.4)`

For a fixed sigma the right side of `(4.3)` is minimized by the largest possible delta, namely `delta=sigma`. Combining that most permissive choice with `(4.4)` gives the necessary inequality

`1/2-2sigma-sigma^2/2 <= 6sigma+3sigma^2`.

Thus

> **`7sigma^2+16sigma-1 >=0`.**                          `(4.5)`

Therefore every unbounded repeated-code `m>=2` survivor satisfies

> **`sigma >= (sqrt(71)-8)/7 = 0.060878539...`.**        `(4.6)`

In original variables,

> **`(r+g0+d)/p >= (sqrt(71)-8)/7-o(1)`.**              `(4.7)`

Since `d=e-(p-ell)` is the excess boundary-forward population, an unbounded repeated-code survivor cannot simultaneously have

- small residual matched dimension r,
- a nearly full outside block (`g0=o(p)`), and
- nearly minimal U-forward population (`d=o(p)`).

At least one of those three quantities must consume about 6.09% of p asymptotically.

## 5. Interpretation

This is the first wedge in this line that applies to the **whole repeated-code `m>=2` branch**, rather than only the exact `e=p` face or the old residual-one diagnostic. Its source is physical: the U-forward boundary witnesses form an independent B-layer set and collectively carry every repeated-code boundary service.

The wedge does not by itself close the branch. The next useful question is which of the three escape directions in `(4.7)` can absorb the required mass without creating a second quadratic cost:

1. large r feeds directly into the residual matched ledger;
2. large g0 shrinks Y and changes the rooted triangle/order balance;
3. large d means many extra one-match U vertices and should be tested for additional same-class/source-service inefficiency.

## 6. Scope

No source-tuple capacity theorem, global selected `(source,coordinate)` uniqueness, rooted-Q inequality, or superseded H--U private-foot argument is used in deriving the boundary bill. The only downstream inputs are the preserved score ceiling and independent U-bound.
