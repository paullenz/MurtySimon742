# Explicit scalar escape family versus exact pair capacity

Date: 2026-09-20

Status: same-session method diagnostic, conditional on the rigid one-code interface. This is **not** a graph construction.

## Family

Use the infinite family preserved in `ONE_CODE_NEAR_RIGID_SCALAR_ESCAPE_FAMILY.md`:

- `c=2t`, `p=3t`, `y=t`, `g0=2t`,
- `lambda=4t-1`, `u=4t`, `x=5t`,
- minimum-source U-witness count `k=3t`, escape count `d=t`, matched-covered head count `m=2t`,
- `t>=2`.

The previously computed exact scalar score floor is

`S_floor = 9t^2+5t-2 + floor(4t^2-3t/2)+1`,

and the above-M ceiling is

`C0=20t^2+10t-4`.

## Exact Ccap_P test

The preserved exact complementary-pair capacity is

`Ccap_P = R_code(S_P)[g_P+2S_P/(lambda+1)]`,

with crossing feasibility requiring

`2xy <= Ccap_P`,

and

`R_code(s)=floor((D0+sqrt(D0^2+12s))/3)`,

`D0=5p+5u-3lambda-2`.

On this family,

`D0=23t+1`, `lambda+1=4t`, and `2xy=10t^2`.

To make the capacity test deliberately hostile, set the nonnegative pair term `g_P` to zero and take only `S_P=S_floor`. Since `sqrt(D0^2+12S_P)>=D0`,

`R_code(S_floor)>=floor(2D0/3)>=15t+1` for `t>=2`.

Also

`S_floor > 13t^2+(7/2)t-2`,

so

`2S_floor/(lambda+1)=S_floor/(2t) > (13/2)t+7/4-1/t`.

Therefore, already at `g_P=0`,

`Ccap_P > (15t+1)((13/2)t+7/4-1/t)`.

For every `t>=2` this is strictly larger than `10t^2=2xy` (indeed the leading coefficient is `97.5`, versus `10`). Hence:

> **exact Ccap_P by itself does not eliminate the scalar escape family; it has a large quadratic margin even under the hostile choice g_P=0.**

This is stronger than merely observing that the coarse global score survives: one of the audit-mandated exact local gates has now been checked explicitly and is not the missing mechanism for this family.

## Exact CROWD scalar floor

The preserved pair-crowding scalar floor used in the exact local feasibility envelope is

`S_P >= s_crowd=[y(3y-D0)]_+`.

On this family,

`3y-D0 = 3t-(23t+1) = -20t-1`,

so

> `s_crowd=0`

for every `t>=1`.

Thus the aggregate `(CROWD)` floor also does not touch this family. This does **not** say that all distribution-sensitive consequences of the pair geometry are vacuous; only that the preserved scalar crowding floor is identically zero on this scaling direction.

## Consequence

Two audit-mandated local scalar gates can now be ruled out as the missing contradiction on this family:

- exact `Ccap_P` has very large positive margin even under `g_P=0`;
- the preserved scalar `CROWD` floor is identically zero.

The next load-bearing tests are therefore the parts that retain *distribution and physical location* rather than only local aggregate capacity: exact `(ONE-P)` with the pair halves kept separate, the distinct singleton-head parameter `rho` rather than only `m<=rho`, exact rooted residual / located U-nonedge feedback, and graph-level realizability of the rigid interface itself.

No claim is made that the family survives those stronger tests. Bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, and `X_3` remains the mandatory negative control.
