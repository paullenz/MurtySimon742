# Parameter-only score obstruction after reverse collapse

Date: 2026-09-19

Status: direct consequence of `ZERO_BUFFER_REVERSE_COLLAPSE.md` plus the preserved above-`M(n)` score ceiling. This is a hand derivation, not a finite scan.

## 1. Input

In the reverse-collapsed zero-buffer branch:

- `x=p+k`, `k>0`;
- `a=2p+u-lambda-1=x+y`, hence

  `y=p+u-lambda-1-k`;

- every buffer--X edge uses an outside-U certificate;
- at least one distinct outside witness exists, so `m>=1`;
- the distinguished pair-local slack satisfies

  `S_P>=k(p+k)+y(1+m)`.

Therefore, without using the aligned-code cap at all,

> `S>=S_P>=k(p+k)+2y`.                                   `(1.1)`

For an above-`M(n)` candidate the preserved scorecard gives

> `S<=C0`,                                                `(1.2)`

with

`C0=2(D_M-1)+lambda(p+u)-p`.

The balanced-product defect threshold has the compact parity-unified form

> `D_M=2p+u-floor((lambda+1)^2/4)-1`.                     `(1.3)`

Put

> `H_lambda=floor((lambda+1)^2/4)`.                       `(1.4)`

Then

> `C0=(lambda+3)p+(lambda+2)u-2H_lambda-4`.               `(1.5)`

## 2. Unit IX: explicit necessary inequality

Substitute `y=p+u-lambda-1-k` into `(1.1)` and compare with `(1.5)`.

The lower side is

`k(p+k)+2y`
` =kp+k^2+2p+2u-2lambda-2-2k`.

Thus every reverse-collapsed zero-buffer above-threshold candidate must satisfy

> `(lambda+1-k)p + lambda u`
> ` -k^2+2k+2lambda-2H_lambda-2 >= 0`.                    `(2.1)`

Equivalently,

> `(k-lambda-1)p`
> ` <= lambda u-k^2+2k+2lambda-2H_lambda-2`.              `(2.2)`

This is a parameter-only necessary condition. It uses only the weakest fact `m>=1`; the actual witness floor `m>=ceil(x/R_A)` and exact `Ccap_P/(CROWD)` constraints can only strengthen it.

## 3. Unit X: the balanced lambda=0 zero-buffer branch is impossible

Set `lambda=0`. Then `H_lambda=0`, and `(2.1)` becomes

> `(1-k)p-k^2+2k-2 >= 0`.                                 `(3.1)`

For every integer `k>=1`:

- if `k=1`, the left side is `-1`;
- if `k>=2`, `(1-k)p<=-(k-1)` because `p>=1`, while
  `-k^2+2k-2=-(k-1)^2-1<=-1`.

Hence the left side is strictly negative for every `k>=1`.

Therefore:

> **BALANCED ZERO-BUFFER EXCLUSION.** No above-`M(n)` rigid one-code `z=1` common-buffer candidate with zero buffer slack can have `lambda=0`. `(ZB0)`

This is an unconditional closure **inside the stated rigid zero-buffer hypotheses**. It is not an all-order theorem and does not touch branches outside those hypotheses.

## 4. First off-balance slices

The same inequality gives useful exact restrictions before invoking any more local machinery.

### lambda=1

Here `H_lambda=1`, so

> `(2-k)p+u-k^2+2k-2>=0`.                                 `(4.1)`

In particular:

- `k=1` requires only `p+u>=1` and is not closed by this coarse score comparison;
- `k=2` requires `u>=2`;
- `k>=3` requires

  `u >= (k-2)p + (k^2-2k+2)`.                            `(4.2)`

Thus any lambda=1 survivor with `k>=3` is forced into an increasingly unmatched-heavy regime.

### general fixed lambda

When `k>=lambda+2`, `(2.2)` has a positive left coefficient. Therefore

> `u >= ((k-lambda-1)p+k^2-2k-2lambda+2H_lambda+2)/lambda` `(4.3)`

for `lambda>0`.

So excess `k` beyond `lambda+1` cannot coexist with a balanced tight-fibre population: it forces a quantitatively large unmatched reservoir. That is precisely the regime in which the source-tuple / beta and rooted residual constraints should next be strongest.

## 5. Why this matters for the eventual problem

The previous scalar picture incorrectly suggested that the zero-buffer branch was cheapest at reverse saturation `d=0`. The physical reverse collapse instead forces maximal reverse deficit `d=p`, and the resulting compulsory outside load makes even the weakest pair-local score floor strong enough to eliminate the perfectly balanced `lambda=0` slice outright.

The remaining zero-buffer branch therefore has `lambda>=1` and, once `k>lambda+1`, must be unmatched-heavy according to `(4.3)`. This reduces the next attack to a sharply described off-balance regime rather than the full `(p,u,lambda,k)` box.

## 6. Next use

Do not replace the sharper local inequalities by `(2.1)`. Use `(2.1)` only as a first structural gate. For the surviving `lambda>=1` regime, retain

- `m>=ceil(x/R_A)`;
- `S_P>=k(p+k)+y(1+m)`;
- exact `2xy<=Ccap_P`;
- `(ONE-P)` and `(CROWD)`;
- `Z>=ka+p+y(1+m)`;
- the exact rooted `q+E_U` minimization.

The next target is the lambda=1 / small-k strip first, because `(4.1)` shows exactly where the coarse score floor stops closing the branch.