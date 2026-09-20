# Residual-one k=2 weighted source-collapse optimization

Date: 2026-09-20

Status: **same-session exact asymptotic synthesis** of the new global H/Y polarization, hole/slack coupling, and `bar d` source-collapse theorem. No finite scan is used.

This note deliberately optimizes only the legitimate weighted currencies

`E_U+Z_X+Z_Y+2M_U`

and leaves `2L_A` unused. It does not compare an unweighted defect coefficient to the score ceiling.

## 1. Parameter

On the exact low-k ray let

`eta=|B_0|/p+o(1)`,

where

`B_0={w in U_{bar d}:d_H(w)=0}`.

The source-collapse theorem gives

`e(U)/p^2 <= eta(1-eta)+o(1)`.

Since `u=p+1`,

`binom(u,2)/p^2 -> 1/2`.

Therefore

> **`M_U/p^2 >= m(eta)-o(1)`,**
>
> `m(eta)=1/2-eta+eta^2`.                                `(WS-M)`

## 2. Global hole/slack coupling prices the same missing U-pairs in E_U

The escape hole/slack identity gives

`E_E >= 2M_U(E)+M_U(E,W_s)-O(p)`.

Because `|W_s|=2`, all missing pairs involving W_s contribute only O(p). Hence

> **`E_U/p^2 >= 2m(eta)-o(1)`.**                         `(WS-E1)`

This use is legitimate in the combined ledger: `E_U` and `2M_U` are separate weighted terms even though the same missing U-pair helps force the slack.

## 3. B_0 itself supplies a second slack floor

Every `w in B_0` is H-anticomplete and Y-anticomplete, so

`epsilon_w >= p-2+m_U(w)`.

Also `B_0` is independent, hence every w misses the other `|B_0|-1` vertices of B_0. Summing over B_0 gives

`E_U(B_0)`
` >= |B_0|(p-2)+|B_0|(|B_0|-1)`.

Thus

> **`E_U/p^2 >= eta+eta^2-o(1)`.**                       `(WS-E2)`

Combining `(WS-E1)` and `(WS-E2)`,

> `E_U/p^2 >= max{2m(eta),eta+eta^2}-o(1)`.              `(WS-E)`

## 4. Add the global A-hole block

The global escape H/Y polarization gives exactly

`Z_X+Z_Y >= (p-1)(p-2)`,

so

> **`Z/p^2 >= 1-o(1)`.**                                 `(WS-Z)`

Therefore the legitimate weighted subtotal satisfies

> `W(eta):=(E_U+Z+2M_U)/p^2`
>
> `>= 1+2m(eta)+max{2m(eta),eta+eta^2}-o(1)`.            `(WS-W)`

## 5. Exact minimization

The two E_U floors cross when

`2m(eta)=eta+eta^2`,

that is

`1-3eta+eta^2=0`.

The relevant root is

> `eta_0=(3-sqrt(5))/2=0.381966...`.                     `(WS-ETA)`

For `0<=eta<=eta_0`, the `2m` floor dominates, so

`W>=1+4m=3-4eta+4eta^2`,

which decreases throughout this interval.

For `eta_0<=eta<=1`, the B_0 slack floor dominates, so

`W>=2-eta+3eta^2`,

which increases throughout this interval because `eta_0>1/6`.

Hence the exact relaxed minimum occurs at eta_0.

Using `eta_0^2=3eta_0-1`,

> **`liminf (E_U+Z+2M_U)/p^2 >= 11-4sqrt(5)`**
>
> **`=2.055728090...`.**                                  `(WS-MAIN)`

This is a corrected weighted coefficient, not the invalid earlier comparison between physical defect and C0.

## 6. Equality geometry

At the relaxed minimizer,

- about `38.1966%` of the U-scale population lies in the H-free/Y-free code class B_0;
- the missing-U coefficient is
  `m(eta_0)=0.263932...`;
- the two independent U-slack lower bounds tie:
  `2m(eta_0)=eta_0+eta_0^2=0.527864...`;
- the global A-hole block contributes coefficient one.

Thus a near-minimizer must simultaneously saturate

1. the U-edge source-capacity bound;
2. B_0 independence;
3. the global H/Y hole floor;
4. the escape hole/slack identity.

That is a much more rigid hostile normal form than the invalid golden dual-witness endpoint which this session superseded.

## 7. Remaining gap and next move

The legitimate combined ceiling is

`E_U+Z+2M_U+2L_A <= p(p+1)+2C0`,

with leading coefficient four. `(WS-MAIN)` leaves a substantial gap and therefore is **not** a closure.

The next term to understand is A-side slack. The new global H/Y polarization places about p^2 holes specifically into H--U or Y--U. Low `L_A` can compensate these only through dense internal H or Y adjacency. The next raw-criticality attack should therefore classify the compensating internal H/Y edges:

- Y--Y edges are same-code and require physical `U_{bar d}` witnesses;
- H--H edges can use private matched endpoints and need a separate exact local analysis.

A proof that the required compensator density itself creates U-slack or additional A-holes would feed directly into the unused `2L_A` term.

Global caveat unchanged: this entire calculation is conditional downstream of a rigid complete Hall cut that has no positive bounded actual-D2C fixture with `x>=3`.