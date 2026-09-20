# Exact rooted ledger for the maximal-selection m=1 survivor

Date: 2026-09-20

Status: internal conditional synthesis. It assumes the maximal-witness normalization in `MAXIMAL_SELECTION_GENERIC.md`, the independently audited first-strict setup, the all-R closure, and the surviving all-F structural theorems.

## 1. Literal U geometry

Maximal selection gives `m=1 => T=0`, hence

`u=k+2`, `U_o={z}`.

The all-R polarization is empty, so the surviving case is all-F. The all-F isolation theorem gives

- `G[U_-]` empty for `U_-=W_0 dotcup {b}`;
- `zW_0` empty;
- `bz in E`.

There are no other U-vertices. Therefore

> `G[U]` has exactly the single edge `bz`,
>
> `q=e(G[U])=1`.                                        `(M1-Q1)`

This is exact, not an upper bound.

## 2. Exact U-score

The exact common-core identity is

`epsilon_w=p+k-1+h_w`

for each core vertex `w in W_0`, where `h_w` is its number of missing U_o edges. Since `U_o={z}` and every core misses z,

> `epsilon_w=p+k` for every `w in W_0`.

The first-strict layer has exactly

> `epsilon_b=p-g+1`.

The isolated all-F witness has

> `epsilon_z=p+u-2=p+k`.

Hence the entire U-score is known exactly:

> `E_U=(k+1)(p+k)+(p-g+1)`.                             `(M1-EU)`

No score allocation or pair relaxation enters this identity.

## 3. Exact rooted unused-slot count

Use the exact rooted identity

`r=(p-lambda)(p+u)+q+E_U`.

With `T=0`,

`lambda=2p-g-y+1`, `u=k+2`, `q=1`.

Substitution gives

> `r = k^2+k y+g k+g p+g-p^2+p y-p+2y`.               `(M1-R-EXACT)`

Thus the surviving maximal-selection one-witness branch has no residual freedom in q or E_U: r is an explicit polynomial in `(p,k,g,y)`.

## 4. Hamming compatibility

The all-F Hamming lower bound remains

`r >= x+y[p-1-floor((p-2)/x)]`, `x=k+g`.

Therefore every maximal-selection m=1 survivor must satisfy the explicit integer inequality

> `k^2+k y+g k+g p+g-p^2+p y-p+2y`
> `>= k+g+y[p-1-floor((p-2)/(k+g))]`.                  `(M1-HAM-EXACT)`

For `y>=2`, head saturation further restricts `g in {0,1}`. The pair-local `Ccap_P/(ONE-P)/(CROWD)` gate remains additional; it is not absorbed into `(M1-HAM-EXACT)`.

## 5. Interpretation

The old one-witness residual optimization had an apparent outside-reservoir degree of freedom. Under maximal representative selection that degree of freedom disappears completely: the branch has one outside vertex, one U-edge, exact U-score and exact rooted r. Any surviving asymptotic family must therefore scale through `(p,k,y)` subject to the explicit polynomial/Hamming compatibility, not through an uncontrolled U_o reservoir.
