# Rooted-Q hostile scalar family on the repeated-code large-gap face

Date: 2026-09-21

Status: exact hostile scalar construction inside the rigid one-code parameter system. This is **not** a graph construction. Its purpose is to show that the aggregate rooted-Q inequality, even after the new repeated-code full-boundary theorem, does not by itself close the remaining head-heavy branch.

## 1. Family

For every integer `p>=3`, take

- `g0=1`, hence `y=p-1`;
- `c=p`;
- `u=p`;
- `lambda=g0+c-1=p`;
- `x=p+u-c=p`;
- selected U-witness count `k=0`;
- U-deficit `d=u-k=p`;
- selected matched-head count `m=x-k=p`;
- residual matched dimension `r=p-m=0`;
- order `n=4p+2u-lambda=5p`.

The exact occupancy identity is saturated:

`m=p-c+d=p`.

The no-collision inequality is also saturated:

`d=c=p`.

The repeated-code full-boundary theorem is consistent with the generic face:

`c=p+r=p`.

Thus none of the newly established scalar consequences of full boundary exposure excludes this ray.

## 2. Exact rooted-Q check

For `m=p>=3`,

`phi(m)=(p-1)(p-2)`.

Since `k=0`, the left side of the rooted-Q feasibility inequality is exactly

`L=(p-1)(p-2)`.

On the right side,

`u(p-lambda)=0`,

and

`2du-d(d+1)=2p^2-p(p+1)=p^2-p`.

Also

`C0=(lambda+2)(p+u)+p-A_lambda`

`   =(p+2)(2p)+p-A_p`

`   =2p^2+5p-A_p`,

where

`A_p=ceil((p^2+2p+8)/2)`.

Hence

`R=3p^2+4p-A_p`.

The margin is

`R-L = 2p^2+7p-2-A_p`.

Using

`A_p <= (p^2+2p+9)/2`,

we obtain

`R-L >= (3p^2+12p-13)/2 >0`

for every `p>=1`. In particular the exact rooted-Q inequality holds with quadratic margin for every member of the hostile family.

## 3. Consequence

The family simultaneously satisfies, at the scalar level,

- the exact one-code identities;
- the exact occupancy identity;
- the no-collision bound;
- the generic repeated-code full-boundary gap `c>=p+r` with equality;
- the old independent U-bound `u<4p+3c`;
- the exact rooted-Q feasibility inequality.

Therefore:

> **Aggregate rooted-Q feedback cannot by itself eliminate the repeated-code, head-heavy, near-maximal-gap face.**

Any closure of this face must use information discarded by the scalar rooted-Q compression: pair-local Hall/source geometry, physical source-coordinate uniqueness, residual-defect structure, or direct graph-level realizability constraints.

## 4. Scope and audit warning

This is deliberately a hostile **parameter** family, not evidence that actual D2C graphs realize the rigid complete Hall-cut interface. The latest direct graph regression still has no positive rigid complete fixture with `x>=3`; `X_3` remains the mandatory negative control. The value of this family is diagnostic: it prevents further time being spent trying to close the surviving face by repeatedly strengthening the same aggregate rooted-Q scalar inequality.
