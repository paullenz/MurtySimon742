# Quadratic boundary slack forces a large complementary-U repair budget

Date: 2026-09-21

Status: exact score consequence inside the repeated rigid one-code near-equality face `e=u-k=p`. Conditional on reaching that rigid interface and on the standard above-threshold score ceiling; not a graph-level eventual theorem.

## 1. Inputs

From `ONE_CODE_BOUNDARY_W_INDEPENDENCE_AND_SLACK.md`, the exact boundary spectrum on `e=p` gives

> **`E_U >= p(2p-1)`.**                                `(1.1)`

The scorecard is `S=L_A+E_U`, hence

> `S>=p(2p-1)`.                                         `(1.2)`

For an above-`M(n)` candidate the preserved score ceiling is

> `S<=C0`,
>
> `C0=(lambda+2)(p+u)+p-A_lambda`,                      `(1.3)`

where

> `A_lambda=ceil((lambda^2+2lambda+8)/2)`.              `(1.4)`

On `e=u-k=p`,

> `u=p+k`.                                               `(1.5)`

## 2. Exact repair-budget inequality

Combining `(1.2)`--`(1.5)` gives

`p(2p-1) <= (lambda+2)(2p+k)+p-A_lambda`.

Rearranging yields the exact necessary condition

> **`k(lambda+2) >= A_lambda-2lambda p+2p^2-6p`.**       `(2.1)`

Using the parity-free lower bound

`A_lambda >= (lambda^2+2lambda+8)/2`,

we obtain

> **`2k(lambda+2) >= (lambda-2p+1)^2-8p+7`.**           `(2.2)`

Thus whenever the right side is positive, a near-equality boundary realization requires a quantitatively large complementary repair reservoir, not merely one extra U-vertex.

## 3. The former hostile spine

The exact scalar hostile family had

`g0=1`, `c=p`, `m=p`, `r=0`, `lambda=p`.

The first repaired near-equality family keeps the same `lambda=p` spine but has `u=p+k` with `k>=1`.

Substituting `lambda=p` into `(2.2)` gives

> **`2k(p+2) >= p^2-10p+8`.**                            `(3.1)`

Equivalently

> **`k >= ceil((p^2-10p+8)/(2(p+2)))`**                 `(3.2)`

whenever the numerator is positive.

Asymptotically,

> **`k >= p/2-6+o(1)`.**                                 `(3.3)`

So the complementary repair population must itself be linear in p on this spine.

## 4. Single-hub closure

For `k=1`, `(3.1)` requires

`2(p+2) >= p^2-10p+8`,

or

`p^2-12p+4 <=0`.

The positive root is `6+4sqrt(2) <12`. Therefore

> **on the `lambda=p`, `e=p` face, the single-repair-hub geometry is impossible for every integer `p>=12`.** `(4.1)`

This is a genuine structural closure of the large-p single-hub repair attempt. Local criticality alone allowed the reciprocal hub gadget, but the p pairwise-independent A-anticomplete boundary vertices force too much U-slack for the global score ceiling to absorb.

## 5. Interpretation

The sequence is now:

`full boundary equality -> unique A-anticomplete one-match witnesses -> W independent -> E_U>=p(2p-1) -> linear lower bound on k`.

This is materially stronger than repeated scalar rooted-Q optimization. It explains why the old `u=p` hostile tuple survived the coarse scalar inequalities: those inequalities did not encode the physical independence of the exact one-match boundary layer.

The next high-value question is whether the same independence bill persists when `e>p`, where more than one witness may occupy a coordinate class and Y-anticompleteness need not hold vertexwise for the whole class. A second route is to combine `(2.1)` with the exact occupancy relation `m=p-c+e` and residual-defect identity to bound the remaining `e=p` parameter space beyond the `lambda=p` spine.

## 6. Scope

The only non-raw input is the already preserved above-threshold score ceiling `(1.3)`. No source-tuple capacity theorem, global selected `(source,coordinate)` uniqueness, rooted-Q inequality, or H--U private-foot chain is used.
