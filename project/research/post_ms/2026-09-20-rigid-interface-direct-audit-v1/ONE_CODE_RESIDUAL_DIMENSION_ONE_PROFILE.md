# One-code rigid cut — residual-dimension-one structural profile

Date: 2026-09-20

Status: **same-session structural theorem**, conditional on the rigid one-code near-equality interface and the private-coordinate exhaustion theorem. It is intended as the next exact normal form after the scalar large-gap optimization. Independent hostile replay is still required before promotion.

## 1. Setup

Fix a minimum-source `s in Y=A_d` in the rigid one-code branch. Use the notation

- `k` = number of selected U-witnesses for s;
- `m=x-k` = number of selected matched singleton witnesses;
- `I subseteq [p]`, `|I|=m`, their private coordinates;
- `R=[p]\I`, `r=|R|=p-m`;
- `d_U=u-k`;
- `c=lambda+1-g0`.

The private-coordinate exhaustion theorem gives

`r=c-d_U`.

This note treats the first nontrivial residual case

> **`r=1`.**

Write `R={j}`.

## 2. All U-certified heads have one code

Every U-certified head agrees with d on every private coordinate in I and must differ from d somewhere. Since the only residual coordinate is j,

> **every U-certified head has code**
>
> `C=d xor e_j`.                                         `(R1-1)`

Thus the entire U-certified head set K is a single A_X code class

> `K=A_C cap {the selected U-certified heads}`,
>
> `|K|=k`.

In particular all of the apparent Boolean freedom among those k heads has disappeared.

## 3. Codes of the matched heads

For every matched-covered head `h_i` with private coordinate `i in I`, private-coordinate normal form gives

- `c(h_i)_i != d_i`;
- `c(h_i)_ell=d_ell` for every other private coordinate `ell in I\{i}`.

Hence

> `supp(c(h_i) xor d) subseteq {i,j}`
>
> and contains i.                                       `(R1-2)`

So a matched head has exactly one of the two forms

`d xor e_i`,

or

`d xor e_i xor e_j`.

This reduces all X-codes in the r=1 branch to a radius-one/radius-two star around d.

## 4. The complement of C is absent from A when p>=3

The complement of C is

`̅C = ̅d xor e_j`.

Relative to d, `̅C` differs on every private coordinate in I and agrees only at j.

If `p>=3`, then in the r=1 branch `m=p-1>=2`. A matched head `h_i` agrees with d on every coordinate of `I\{i}`, so by `(R1-2)` it cannot have code `̅C`. A U-certified head has code C, and every Y-vertex has code d.

Therefore

> **`A_̅C=emptyset` for r=1 and p>=3.**                  `(R1-3)`

This is a genuine complement-code localization, not merely a score statement.

## 5. Location of U_̅C

Every selected U-witness for the source has code `̅d`. Since `̅C=̅d xor e_j != ̅d`, no selected witness in `W_s` lies in `U_̅C`.

Therefore

> **`U_̅C subseteq U\W_s`, hence `|U_̅C|<=d_U=c-1`.** `(R1-4)`

The existing same-code complement-pair localization theorem can now be applied to the large class `A_C`: any internal `C-C` edge must use a complementary witness in `U_̅C`, because `A_̅C` is empty.

Consequently the existing complement-capacity theorem yields

> `e(A_C) <= k |U_̅C| <= k(c-1)`.                    `(R1-5)`

This is an upper bound, not yet a contradiction.

## 6. Why the old crowding lower bound is vacuous here

The predecessor same-code crowding lower bound uses

`T=a-p=p+u-lambda-1`.

In the present minimum-source parameterization with r=1,

`k=u-c+1`,

while

`T=u+y-c`.

Hence

> `k-T=1-y<=0`.                                          `(R1-6)`

Thus the old generic crowding lower bound on `e(A_C)` supplies no positive density. This identifies a real methodological boundary: **the r=1 branch cannot be closed merely by feeding the large C-class into the old scalar crowding theorem.**

The next mechanism must use the special head-witness incidence itself, the unique residual coordinate j, or the rooted Q/deficit ledger.

## 7. Head-witness edge geometry to attack next

For every `h in K=A_C`, its selected U-witness `z_h` has code `̅d` and satisfies

`N(z_h) cap A_X={h}`.

Thus the used head-witness edge joins the near-complementary code pair

> `C=d xor e_j` in A,
>
> `̅d` in U.                                          `(R1-HW)`

The entire family shares the **same unique exceptional coordinate j**. Any criticality certificate for the k edges `h z_h` that is forced to record a code disagreement has only this one residual coordinate available outside the already-consumed private-coordinate set I.

This is now the preferred structural target. The scalar pair-local Ccap/ONE/CROWD package is too coarse in this regime, while the selected source-coordinate uniqueness machinery is naturally aligned with the single-coordinate bottleneck.

## 8. Summary

For r=1 and p>=3:

1. all k U-certified heads have one code `C=d xor e_j`;
2. every matched head has support `{i}` or `{i,j}` relative to d;
3. `A_̅C=emptyset`;
4. `|U_̅C|<=c-1`;
5. `e(A_C)<=k(c-1)`;
6. generic same-code crowding is vacuous because `k-T=1-y`;
7. all selected head-witness pairs share the unique residual coordinate j.

This profile is substantially narrower than the pre-exhaustion scalar boundary and is the correct object for the next raw-criticality attack.