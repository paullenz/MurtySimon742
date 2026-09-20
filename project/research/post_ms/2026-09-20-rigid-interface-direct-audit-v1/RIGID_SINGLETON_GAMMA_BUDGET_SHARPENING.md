# Rigid Hall cuts — distinct singleton-head support refinement

Date: 2026-09-20

Status: **same-session refinement / scope correction**. Commit `92d1808` / `RIGID_SINGLETON_GAMMA_BUDGET_REPAIR.md` had already established the sharp physical singleton-endpoint budget `sum mu_d<=p`, `u>=[hx-p]_+`, `hx<=u+p`, the rooted collapse `(h-1)x+g0<=lambda+1`, and the corresponding `Z` / `E_U` bills. Those results are predecessor mathematics and are not re-claimed here.

The new point in this note is narrower but real: **matched capacity for one source is controlled by the number of distinct singleton heads, not by the number of singleton endpoints.** Several private coordinates may belong to the same head and cannot certify several different crossing heads.

## 1. Distinct-head support

For a represented source code `d`, let

`M_d := {w : w is a tight matched endpoint, gamma(w)=d, |N(w) cap A_X|=1}`

and define

`mu_d:=|M_d|`,

`rho_d:=|{h(w):w in M_d}|`.

Then

> `rho_d<=mu_d`.

The predecessor theorem gives

> `sum_d mu_d<=p`,

hence also

> **`sum_d rho_d<=p`.**                                    `(DHS-1)`

## 2. Physical U demand uses rho_d

Fix one `d`-coded source. Its `x` crossing edges have different heads. Its selected matched singleton witnesses therefore also have different heads. Every matched-certified head must lie in the physical head-support set counted by `rho_d`.

Thus at most `rho_d` crossing heads can be matched-certified, and every `d`-coded source requires at least

> **`k_d:=[x-rho_d]_+`**                                  `(DHS-2)`

physical U witnesses.

This is at least as strong as the predecessor endpoint-count demand `[x-mu_d]_+`, and can be strictly stronger when several singleton matched endpoints share one A_X head.

Distinct source codes use disjoint complementary U-code classes, so with

`K:=sum_d k_d`

we have

> `u>=K`,
> `K>=[hx-p]_+`.                                           `(DHS-3)`

The global `hx<=u+p` bound is unchanged, but the code-specific lower bounds are sharpened.

## 3. Located deficits with distinct-head demand

Let `y_d=|Y_d|`. Using the same physical witness argument as the predecessor singleton repair,

> `Z_X >= (x-1)K`,
> `Z_Y >= sum_d y_d k_d`,
> `Z >= (x-1)K+sum_d y_d k_d`.                            `(DHS-Z)`

A multiplicity-sensitive corollary is

`sum_d y_d k_d >= xy-sum_d y_d rho_d`.

Since `max_d y_d<=y-h+1` and `sum_d rho_d<=p`,

> **`Z_Y >= [xy-p(y-h+1)]_+`.**                           `(DHS-ZY)`

For `g0=p-y>=1`, the same per-witness degree count gives

> **`E_U >= sum_d k_d(y_d+g0-1)`.**                       `(DHS-EU)`

The predecessor aggregate relaxations follow by replacing `rho_d` with the weaker endpoint budget.

## 4. Why this matters for the near-rigid one-code branch

In the one-code branch, write simply `rho=rho_d`. Then every source has U-witness count

> `k_s >= [x-rho]_+`,

so the minimum actual count `k_*` used in `ONE_CODE_NEAR_RIGID_SLOT_PRICE.md` obeys

> **`k_* >= [x-rho]_+ >= [x-g_P]_+`.**                    `(DHS-NR)`

Thus repeated private coordinates on one head do not provide fictitious matched relief. The exact near-rigid optimization should use the distinct-head support `rho`, while `g_P` remains separately relevant for pair-local collision pricing.

## 5. Audit note

The earlier same-session draft of this file duplicated the already-present `92d1808` global p-budget because that commit had not yet been inspected during the shortened invocation. This correction preserves the genuinely new `rho_d` refinement and explicitly restores attribution of `hx<=u+p` and the rooted collapse to the predecessor singleton-repair theorem.