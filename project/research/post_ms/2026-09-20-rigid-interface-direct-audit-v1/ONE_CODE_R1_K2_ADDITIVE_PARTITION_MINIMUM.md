# Residual-one k=2 additive partition minimum

Date: 2026-09-20

Status: **same-session analytic synthesis**, conditional on the preceding k=2 class theorems. No finite scan is used.

The earlier five-class theorem used only the maximum of five classwise lower bounds and therefore discarded additivity between physically disjoint currencies. Retaining the additive non-K-heavy bills raises the global asymptotic defect coefficient substantially and isolates the one-K-neighbour / W_s-free class as the only plausible cheap large population.

## 1. Partition and physical functional

On the exact low-k ray, partition the `p-1` escape vertices into

- R: K-heavy, size r;
- D: W_s-free but not K-heavy, size d;
- T: the union of F1 (K-free, exactly one W_s neighbour) and S (W-heavy), size `theta`;
- M: mixed, size m.

Thus

`r+d+theta+m=p-1`.                                       `(AP-PART)`

Use

`D_phys=E_U+Z_X+Z_Y+M_U`.

## 2. The non-R bills add

The D-sector theorem gives

`Z_H(D)+Z_Y(D)+M_U(D) >= d(p-2)/2`.                      `(AP-D)`

Every vertex of T is Y-anticomplete, so

`Z_Y(T)>=theta(p-1)`.                                    `(AP-TY)`

Moreover every T-vertex is anticomplete to every K-heavy vertex:

- for S this is the preserved K-heavy/W-heavy theorem;
- for F1 this is the general K-free selected-witness forward-orientation theorem.

Hence

`M_U(R,T)>=r theta`.                                      `(AP-RT)`

Every mixed vertex pays `epsilon>=p+1`, so

`E_U(M)>=m(p+1)`.                                        `(AP-M)`

The four quantities in `(AP-D)--(AP-M)` are pair-disjoint / currency-disjoint in the following sense:

- the D-sector U--U term has an endpoint in D, while `(AP-RT)` has endpoints in R and T;
- the Y--U holes in D and T have disjoint U endpoints;
- mixed slack lies in `E_U`, not in any located-hole term.

Therefore they may be added:

> **`D_phys >= d(p-2)/2 + theta(p-1+r) + m(p+1)`.**       `(AP-NONR)`

This is much stronger than taking the maximum of the individual class bounds.

## 3. Combine with the exception-independent K-heavy bill

The exception-orientation theorem independently gives

> `D_phys>=r(r-1)/3`.                                    `(AP-R)`

Normalize

`alpha=r/p`, `beta=d/p`, `vartheta=theta/p`, `mu=m/p`.

Asymptotically `alpha+beta+vartheta+mu=1`. Dividing `(AP-NONR)` by `p^2` gives

`liminf D_phys/p^2 >= beta/2 + vartheta(1+alpha)+mu`.     `(AP-NONR-LIM)`

For fixed alpha, the cheapest place to put all non-R mass is D, because

`1/2 < 1 <= 1+alpha`.

Hence every asymptotic configuration satisfies

> `liminf D_phys/p^2 >= max{alpha^2/3,(1-alpha)/2}`.      `(AP-MAX)`

The two terms balance when

`2alpha^2=3(1-alpha)`,

so

`alpha=(sqrt(33)-3)/4`.

At this point

> **`tau_add=(7-sqrt(33))/8 = 0.156929669...`.**           `(AP-TAU)`

Therefore

> **`liminf D_phys/p^2 >= (7-sqrt(33))/8`.**              `(AP-MAIN)`

This improves the previous five-class max coefficient from about `0.09387` to about **0.15693**.

## 4. The optimizer identifies the next literal geometry

Equality in the coarse additive relaxation requires asymptotically

- `r/p -> (sqrt(33)-3)/4 ≈0.68614`;
- `d/p -> 1-alpha ≈0.31386`;
- `theta/p ->0`;
- `m/p ->0`.

Thus any configuration approaching the current coarse minimum is overwhelmingly a mixture of

1. K-heavy escapes R, and
2. W_s-free non-K-heavy escapes D.

But the preceding coupled R/F0 theorem proves that if the D population is asymptotically fully free (`d_K=0`), then the coefficient is at least `1/4`, strictly above `tau_add`.

Consequently:

> **any sequence approaching the present `tau_add` lower envelope must contain a linear population of D1 vertices: W_s-free escapes with exactly one K-neighbour.** `(AP-D1)`

This is a much narrower structural endpoint than the original five-way partition.

## 5. Strategic consequence

The next raw-criticality target should be D1 itself. A D1 vertex t has

- no selected-witness neighbours;
- exactly one K-neighbour;
- exact sector deficit `p-3+epsilon_t` across H, Y and E;
- and lies in the same low-k residual hub geometry as the K-heavy source population.

A theorem forcing D1 to be Y-sparse, H-sparse, or anticomplete to a substantial fraction of R would immediately raise `(AP-TAU)` and may be enough, after exact rooted weighting, to make the low-k ray finite-order. Conversely, if D1 admits a cheap local normal form, that normal form is now the correct object to reconstruct rather than continuing broad partition algebra.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; this remains conditional downstream mathematics pending independent hostile replay.