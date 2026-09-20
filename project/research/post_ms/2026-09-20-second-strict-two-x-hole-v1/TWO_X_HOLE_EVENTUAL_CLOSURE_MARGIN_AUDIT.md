# Two-X-hole eventual closure — independent margin/slot audit

Date: 2026-09-20

Status: **same-session hostile audit** of the load-bearing accounting in `TWO_X_HOLE_BOUNDED_HOLE_RESOURCE_CLOSURE.md`, `TWO_X_HOLE_EVENTUAL_X16_CLOSURE.md`, and `TWO_X_HOLE_FINITE_ORDER_BOUND.md`. This note does not add a stronger theorem; it checks whether allowing internal X-density invalidates the rooted `r>=x+y` baseline or the `2M/3M` rebate accounting.

## 1. Potential failure mode

The no-hole-code proof stated `r>=x+y` in the edgeless-X arm. The later represented-hole-code closures reuse its zero-resource rooted margin `B_0` while allowing

`e_X=e(G[X])>0`.

A possible hidden error would be: internal X-edges might consume the local unused-slot budget and invalidate the baseline `r>=x+y`, in which case the later `B<=B_0+3M` estimate would be missing an additional rebate.

The local theorem in `LOCAL_SLOT_HAMMING_BUDGET.md` resolves this directly.

## 2. Local theorem

For every A-vertex z,

`sum_{w in N_A(z)} d_H(c(w),c(z)) <= r_z d_A(z)`.

All X--Y edges are present, and every X-code differs from the Y-code d. Therefore every vertex of `A=X dotcup Y` is incident with at least one A-edge of strictly positive Hamming length:

- for `x in X`, choose any `y in Y`;
- for `y in Y`, choose any `x in X`.

Hence the left side of the local inequality is strictly positive for every A-vertex. Since `d_A(z)>0` and `r_z` is a nonnegative integer,

> **`r_z>=1` for every `z in A`.**                        `(MA-R1)`

Summing gives

> **`r>=|A|=x+y`.**                                       `(MA-R)`

Crucially, this argument does **not** require `G[X]=emptyset`. Additional internal X-edges add nonnegative Hamming load and cannot make `(MA-R1)` fail.

Thus the rooted baseline used by the represented-resource closures survives unchanged when `e_X>0`.

## 3. Re-audit of the M rebates

Relative to the zero-resource baseline:

### Score margin

The exact aggregate X-slack ledger is

`L_X>=L_X^0-2e_X`.

Since `e_X<=M`, internal X-density can improve the score margin by at most `2M`:

> `A<=A_0+2M`.                                           `(MA-A)`

No rooted-slot rebate is hidden here.

### Rooted margin

The rooted upper side is

`(p-lambda)(p+u)+q+E_U`.

The distinguished resource can improve it in only two ways presently retained:

1. `e(G[U_o])<=M` raises q by at most M;
2. `L_A` can drop by at most `2M`, raising the score-derived cap on `E_U` by at most `2M`.

The lower requirement `r>=x+y` does not drop by Section 2. Therefore

> `B<=B_0+3M`.                                           `(MA-B)`

This validates the coefficient 11 in

`A+3B<=-Phi+11M`.

## 4. Re-audit with forward surcharge

For every forward-routed distinguished witness counted by `F_H`, the forward-surcharge theorem supplies

- one additional X--U_o hole;
- one additional core--U_o hole.

The first raises `L_A` by one, the second lowers q by one, and together the two physical holes raise the score floor by at least two. Therefore

> `A<=A_0+2M-2F_H`,
>
> `B<=B_0+3M-2F_H`,

and

> `A+3B<=-Phi+11M-8F_H`.

No extra assumption about internal-X slot usage is needed.

## 5. Result of the hostile check

The suspected missing rooted-slot rebate is **not present**. The local Hamming theorem gives `r_z>=1` at every A-vertex solely from the complete unequal-code X--Y cut. Internal X-density cannot erase that positive local load.

Therefore the `2M/3M` and `2M-2F_H / 3M-2F_H` margin accounting used in the new two-X-hole closures survives this hostile audit.

The remaining audit risks are upstream structural ones: the physical edge-localization theorems and the forward-route hole disjointness, plus the global zero-positive-rigid-cut interface already identified by the daily red team.