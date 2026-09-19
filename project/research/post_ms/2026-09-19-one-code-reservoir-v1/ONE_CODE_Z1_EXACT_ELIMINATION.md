# `z=1` exact hole elimination and buffer surcharge

Date: 2026-09-19

Status: follow-on hand theorem to `ONE_CODE_Z1_NEAR_SATURATION.md`.

This note keeps the exact first-near-saturation variables instead of replacing them immediately by `y`.

## 1. Common-buffer branch: the buffer itself starts paying once it is used

Retain the common-buffer notation: `W=W_0 union {b}`, `|W_0|=k`, every source in `Y` uses every member of `W_0` as a crossing witness, and the buffer `b` is unused by crossing certificates.

Put

`H=e_++e_-`,

where every one of these `H` auxiliary selected objects is routed through a distinct physical pair in `Y x {b}`.

If `H>0`, every auxiliary head lies outside `X`:

- an internal-Y A/U certificate has its head in `Y`;
- a `Y--U_d` same-code certificate has its head in `U_d`;
- a `U_{bar d}` same-code certificate has its head in the core `W_0`.

Since every source in `Y` is adjacent to all of `X`, the existence of any such certificate forces

> `d_X(b)=0`.                                              `(B0)`

Let `e_+=e(Y)+e(Y,U_d)` as before. The buffer is nonadjacent to the `H` distinct Y-partners used by auxiliary certificates, has exactly `e_-` neighbours in the core (all `U_{bar d}` edges form a buffer star), and can have at most `u-k-1` unmatched neighbours outside `W`. Hence

`d_{A union U}(b)`
` <=(y-H)+e_-+(u-k-1)`.

Using `d_{A union U}(b)=p+u-1-epsilon_b` gives:

### Theorem 1.1 — used-buffer slack

If `H>0`, then

> `epsilon_b >= [p-y+k+H-e_-]_+`
> `            =[p-y+k+e_+]_+`.                           `(BUF-E)`

Together with the saturated core bill,

> `E_- >= k(p+k-2)+[p-y+k+e_+]_+`.                       `(BUF-E-TOT)`

Thus auxiliary use of the buffer is not only a residual-defect surcharge (`Z>=k(a-1)+H`); once the buffer is used at all, it loses every X-neighbour and acquires its own unmatched-slack cost.

### A useful aggregate source/buffer identity

The exact Y-degree identity and `Z_Y>=yk+H` give

`L_Y >= y(p-g)-e(Y)+e(Y,U_d)+e_-`.

Adding the untruncated right side of `(BUF-E)` cancels `e(Y)`:

> `L_Y+epsilon_b`
> ` >= y(p-g)+(p-y+k)+2e(Y,U_d)+e_-`,                    `(BUF-PAIR)`

whenever `p-y+k+e_+>=0` (otherwise retain the positive-part form separately).

So internal-Y traffic cannot buy arbitrary slack relief by moving load onto the buffer: the buffer degree loss cancels that escape in the combined A/U scorecard.

---

## 2. Full-support branch: replace `rho,H` by actual unused holes

Retain the full-support notation from `ONE_CODE_Z1_NEAR_SATURATION.md`:

- `rho` = number of crossing holes;
- `H=e_++e_-` = number of selected auxiliary hole uses;
- `H<=rho`;
- `e_-=e(G[U_{bar d}])`.

Define the number of **unused** crossing holes

> `j:=rho-H>=0`.                                          `(J)`

Because `H>=e_-` and `rho<=y`,

> `j+e_-<=y`.                                             `(JROOM)`

The previously proved exact inequalities become particularly transparent:

### Theorem 2.1 — hole-normal form

> `E_- >= B-j-2e_-`,                                      `(J-E)`
>
> `Z >= Z0-j`,                                            `(J-Z)`

where

> `B=(k+1)(p+k-1)`,
>
> `Z0=(k+1)(a-1)`.                                        `(BZ)`

### Proof

Substitute `rho=H+j` into

`E_- >= (k+1)(p+k-1)-rho+H-2e_-`

and

`Z>=k(a-1)+(a-1)-rho+H`. `square`

Interpretation: an **unused** crossing hole can reduce both the U-slack pressure and the A--U defect by one; a `U_{bar d}` edge can reduce the degree-based U-slack pressure by two but occupies one unit of the same total hole room. This is exactly the tradeoff which was hidden by replacing `rho,H,e_-` by `y` separately.

---

## 3. Full-support U-slack after exact edge/hole elimination

From `(JROOM)`, `e_-<=y-j`. Therefore `(J-E)` gives

> `E_- >= B-2y+j`.                                       `(JE)`

When

> `B>=2y`,                                                `(POS)`

put

> `Ebase:=B-2y>=0`.                                       `(EBASE)`

Then every full-support survivor satisfies

> `E_U>=E_- >= Ebase+j`,                                  `(EJ)`
>
> `Z-u(p-lambda) >= D0-j`,                               `(DJ)`

where

> `D0:=Z0-u(p-lambda)`.                                   `(D0)`

The same variable `j` moves these two lower bounds in opposite directions with slopes `+1` and `-1`.

---

## 4. Exact cancellation in the rooted residual ledger

Recall the exact constraints

`2q+E_U >= Z-u(p-lambda)`

and the quantity to be charged into the residual identity is `q+E_U`.

For fixed `j`, `(EJ)/(DJ)` imply

`q+E_U`
` >= Ebase+j`
`    +ceil([D0-j-(Ebase+j)]_+/2)`
` = Ebase+j+ceil([D0-Ebase-2j]_+/2)`.

Because `j` is an integer, the `+j` term cancels exactly against the `-2j` inside the half-defect until the defect gap closes; afterwards the expression only increases.

### Theorem 4.1 — full-support hole-free residual floor

Under `(POS)`, every `z=1` full-support survivor satisfies

> `q+E_U`
> ` >= Ebase+ceil([D0-Ebase]_+/2)`,                       `(FULL-EXACT-QE)`

where

`Ebase=(k+1)(p+k-1)-2y`,

`D0=(k+1)(a-1)-u(p-lambda)`.

### Proof

Let `A=D0-Ebase`. For every integer `j>=0`,

`j+ceil([A-2j]_+/2) >= ceil(A_+/2)`.

If `2j<A`, equality holds because `ceil((A-2j)/2)=ceil(A/2)-j`; once `2j>=A`, the left side is `j>=ceil(A/2)`. Add `Ebase`. `square`

This removes `rho,H,e_-` completely without paying the loss incurred by the separate coarse bounds `rho<=y`, `e_-<=y`.

### Corollary 4.2 — forced A-edge mass

Using

`f=(p-lambda)(p+u)+q+E_U-delta`,

every full-support survivor in the `(POS)` regime satisfies

> `f >= (p-lambda)(p+u)`
> `     +Ebase+ceil([D0-Ebase]_+/2)-delta`.               `(FULL-EXACT-F)`

For an above-`M(n)` candidate one may replace `delta` by `D_M-1` as in the preserved rigid residual theorem.

The important point is conceptual as well as numerical: the possible relief from unused crossing holes is already exactly accounted for. There is no need to optimize `rho,H,e_-` separately before feeding the full-support branch into the rooted residual ledger.

---

## 5. Next use

The two `z=1` support types now have clean residual inputs:

- **common buffer:** `E_core=k(p+k-2)`, `Z>=k(a-1)+H`, with the additional used-buffer surcharge `(BUF-E)` when `H>0`;
- **full support:** in `B>=2y`, the hole variables disappear completely in `(FULL-EXACT-QE)`.

The next calculation should compare these exact `q+E_U` floors with the available A-edge / direct-edge structure and `(ONE-P)/(CHAN-P)`. If they close the high-load regimes, only the low-`B<2y` full-support strip and the zero-auxiliary common-buffer equality model remain before moving to `z=2`.

No actual rigid-cut fixture is claimed, and `X_3` remains outside the branch.
