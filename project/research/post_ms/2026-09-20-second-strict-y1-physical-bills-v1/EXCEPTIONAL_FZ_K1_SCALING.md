# Exceptional Fz — exact unbounded scalar k=1 scaling family

Date: 2026-09-20

Status: **diagnostic-to-structural synthesis**, not a realizability result. This note explains why the current total-score plus rooted-ledger inequalities cannot close exceptional Fz by themselves and identifies the precise family that must be attacked with pair-local / criticality geometry.

After `EXCEPTIONAL_FZ_CROSS_CLASS_CLOSURE.md`, the large-head exceptional-Fz necessary system has

- `G[X]=emptyset`;
- `G[U_o]=emptyset`;
- `epsilon_{z_0}>=p+k+omega-2`;
- `E(U_o^*) >= (omega-1)[p-x+omega]_+`;
- `q <= (k+1)(omega-1)`;
- `r>=x+2`.

The broad diagnostic continues to have survivors for arbitrarily increasing parameter ranges. They are not a finite-box artefact. The simplest scaling arm is already visible at

> `k=1`, equivalently `g=x-1`.

Put

> `omega=x-p+t`,

so that the truncation argument is exactly

> `[p-x+omega]_+=t` for `t>=0`.

Then

`lambda=2p+omega-g-1=p+t`.

Let `A` denote the total-score margin `C0-S_min` and `B` the rooted margin `R_max-(x+2)` for the current exceptional-Fz floors. Writing `eps in {0,1}` for the parity term in `floor((n-1)^2/4)`, exact symbolic expansion gives

> `2A = eps - p^2 + 2pt - t^2 + 4t + 2x - 7`,          `(K1-A)`
>
> `2B = eps - p^2 - t^2 + 4t + 4x - 11`.                `(K1-B)`

Thus both present scalar necessary conditions are only **lower bounds on x**:

> `x >= (p^2-2pt+t^2-4t+7-eps)/2`,
>
> `x >= (p^2+t^2-4t+11-eps)/4`.

For every fixed admissible `(p,t)`, sufficiently large x satisfies both. Therefore:

> **No argument using only the current total-score floor and rooted q/E_U ceiling can close exceptional Fz.**

This is exactly the stop/pivot condition required by the daily red-team audit: an unbounded scaling family has been identified and must be characterized rather than attacked with another weak scalar inequality.

The computational diagnostics reflect the same family. For example the current necessary system contains k=1 rows at progressively larger `(p,x,omega)`; enlarging the box simply moves the tail outward rather than eliminating it.

## Consequence for the proof strategy

The next attack must use information discarded by `(K1-A)/(K1-B)`. The highest-value surviving sources are:

1. **exact pair-local `Ccap_P/(ONE-P)/(CROWD)`**, which has deliberately not been flattened into the total-score inequalities above;
2. the exact criticality structure of the `k=1` common core and the two outside witness code classes, now known to form an independent U_o;
3. the selected/residual Hall ledger before total-score aggregation;
4. the zero-positive-fixture rigid-cut question itself — if the k=1 scaling system cannot be realized by any actual D2C graph, proving that interface nonrealizability would close the family upstream.

Do **not** enlarge the finite parameter scan as the next move. The scalar survivor family is mathematically understood: it is genuinely unbounded under the inequalities currently being scanned.