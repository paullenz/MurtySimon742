# Quadratic boundary slack forces a large complementary-U repair budget

Date: 2026-09-21

Status: exact score consequence inside the repeated rigid one-code near-equality face `e=u-k=p`. Conditional on reaching that rigid interface and on the standard above-threshold score ceiling; not a graph-level eventual theorem.

## 1. Inputs

The exact near-equality spectrum now carries **two disjoint U-slack bills**:

- boundary layer `W`: `E_W>=p(2p-1)`;
- complementary repair set `K`: `E_K>=k(p-1)`.

Hence

> **`E_U >= p(2p-1)+k(p-1)`.**                         `(1.1)`

The scorecard is `S=L_A+E_U`, so the same expression lower-bounds S.

For an above-`M(n)` candidate the preserved score ceiling is

> `S<=C0`,
>
> `C0=(lambda+2)(p+u)+p-A_lambda`,                      `(1.2)`

where

> `A_lambda=ceil((lambda^2+2lambda+8)/2)`.              `(1.3)`

On `e=u-k=p`,

> `u=p+k`.                                               `(1.4)`

## 2. Exact repair-budget inequality

Combining `(1.1)`--`(1.4)` gives

`p(2p-1)+k(p-1) <= (lambda+2)(2p+k)+p-A_lambda`.

Rearranging yields the exact necessary condition

> **`k(lambda-p+3) >= A_lambda-2lambda p+2p^2-6p`.**    `(2.1)`

Using the parity-free lower bound

`A_lambda >= (lambda^2+2lambda+8)/2`,

we obtain

> **`2k(lambda-p+3) >= (lambda-2p+1)^2-8p+7`.**        `(2.2)`

This replaces the weaker same-session inequality with denominator `lambda+2`; that earlier formula omitted the independent K-slack contribution and is superseded by `(2.1)`--`(2.2)`.

## 3. The former hostile spine

The exact scalar hostile family had

`g0=1`, `c=p`, `m=p`, `r=0`, `lambda=p`.

The repaired near-equality face keeps `lambda=p` and has `u=p+k` with `k>=1`.

Substituting `lambda=p` into `(2.2)` gives

> **`6k >= p^2-10p+8`.**                                `(3.1)`

Thus

> **`k >= ceil((p^2-10p+8)/6)`**                        `(3.2)`

whenever the numerator is positive, and asymptotically

> **`k >= p^2/6-O(p)`.**                                `(3.3)`

So the complementary repair population must be quadratic in p on this spine if the score ceiling alone is to absorb the boundary layer.

## 4. Single-hub closure

For `k=1`, `(3.1)` requires

`6 >= p^2-10p+8`,

or

`p^2-10p+2 <=0`.

The positive root is `5+sqrt(23)<10`. Therefore

> **on the `lambda=p`, `e=p` face, the single-repair-hub geometry is impossible for every integer `p>=10`.** `(4.1)`

Local criticality allows the reciprocal hub gadget, but the global score cannot pay for the p independent boundary vertices plus even one complementary repair vertex once p is large enough.

## 5. Whole-spine closure with the independent U-bound

The independently preserved no-collision U-bound is

`u<4p+3c`.

On the hostile spine `c=p` and `u=p+k`, so

`k<6p`, hence for integers

> `k<=6p-1`.                                             `(5.1)`

Together with `(3.1)`, a survivor would require

`p^2-10p+8 <= 6(6p-1)=36p-6`,

or

> **`p^2-46p+14<=0`.**                                  `(5.2)`

The positive root is `(46+sqrt(2060))/2 <46`. Consequently

> **the entire repaired `lambda=p`, `e=p` hostile spine is impossible for every integer `p>=46`, regardless of k.** `(5.3)`

This closes the old rooted-Q hostile direction as an unbounded physical family inside the repeated rigid interface.

## 6. General `e=p` parameter wedge

On `e=p`, the occupancy identity gives

`m=p-c+e=2p-c`,

so with residual matched dimension `r=p-m`,

> **`c=p+r`.**                                          `(6.1)`

Also

`lambda=g0+c-1=p+r+g0-1`.

Put

`s:=r+g0`.

Then `(2.2)` becomes the compact exact-parity-free inequality

> **`2k(s+2) >= (p-s)^2-8p+7`.**                        `(6.2)`

The U-bound gives

`p+k=u<4p+3(p+r)=7p+3r`,

hence

> **`k<=6p+3r-1`.**                                     `(6.3)`

Therefore every `e=p` survivor must satisfy

> **`(p-s)^2-8p+7 <= 2(6p+3r-1)(s+2)`.**               `(6.4)`

In particular an unbounded family with `r/p->alpha`, `g0/p->beta`, and `sigma=alpha+beta` must satisfy

`(1-sigma)^2 <= 12sigma+6alpha sigma <= 12sigma+6sigma^2`.

Thus

> **`5sigma^2+14sigma-1>=0`,**                           `(6.5)`

so

> **`sigma >= (3sqrt(6)-7)/5 = 0.0696938...`.**          `(6.6)`

Equivalently,

> **on the exact boundary-population face `e=p`, every unbounded repeated-code survivor has `r+g0 >= ((3sqrt(6)-7)/5-o(1))p`.** `(6.7)`

The near-saturated regime `r+g0=o(p)` is therefore impossible.

## 7. Interpretation

The proof spine is now

`full boundary equality -> unique one-match witnesses -> W independent -> quadratic E_W -> K also pays k(p-1) -> score repair budget -> U-bound -> positive residual/outside-gap wedge`.

This is stronger than repeated scalar rooted-Q optimization and directly converts physical boundary geometry into a macroscopic restriction on the residual dimension plus outside-code deficit.

## 8. Scope

The non-raw inputs are the preserved above-threshold score ceiling and the independent U-bound. No source-tuple capacity theorem, global selected `(source,coordinate)` uniqueness, rooted-Q inequality, or H--U private-foot chain is used.
