# Explicit scalar escape family versus exact pair-local gates

Date: 2026-09-20

Status: same-session method diagnostic, conditional on the rigid one-code interface. This is **not** a graph construction.

## Family

Use the infinite family preserved in `ONE_CODE_NEAR_RIGID_SCALAR_ESCAPE_FAMILY.md`:

- `c=2t`, `p=3t`, `y=t`, `g0=2t`,
- `lambda=4t-1`, `u=4t`, `x=5t`,
- minimum-source U-witness count `k=3t`, escape count `d=t`, matched-covered head count `m=2t`,
- `t>=2`.

For the pair-local test take the natural scalar assignment

- `g_P=m=2t`,
- `k_P=x-g_P=3t=k`,
- `rho=2t`.

This is a parameter-level assignment only; no graph realization is asserted.

The witness-class slack floor, which is actually located in the complementary `U_bar d` class and therefore in `S_P`, is

> `E_pair=9t^2+5t-2`.

Separately, the A_X collision/Hamming floor is outside the pair P and contributes at least

> `L_X=floor(4t^2-3t/2)+1`.

Thus the total scalar floor is `E_pair+L_X`, while the pair-local tests below deliberately use only

> `S_P=E_pair`.

This corrects an intermediate same-session draft that substituted the total scalar floor for `S_P`; that substitution was too generous to the pair capacity. The corrected smaller pair slack still leaves a large margin.

## Exact Ccap_P test

The preserved one-code pair capacity is

`Ccap_P = R_code(S_P)[g_P+2S_P/(lambda+1)]`,

with crossing feasibility requiring

`2xy <= Ccap_P`,

and

`R_code(s)=floor((D0+sqrt(D0^2+12s))/3)`,

`D0=5p+5u-3lambda-2`.

On this family,

`D0=23t+1`, `lambda+1=4t`, and `2xy=10t^2`.

Since `sqrt(D0^2+12S_P)>=D0`,

`R_code(S_P)>=floor(2D0/3)>=15t+1` for `t>=2`.

Also

`g_P+2S_P/(lambda+1)`
`=2t+(9t^2+5t-2)/(2t)`
`=(13/2)t+5/2-1/t`.

Therefore

`Ccap_P >= (15t+1)((13/2)t+5/2-1/t)`.

For every `t>=2` this is strictly larger than `10t^2=2xy`; the leading coefficient is `97.5`, versus `10`. Hence:

> **exact Ccap_P does not eliminate the scalar escape family even when only the pair-located witness-class slack is supplied to it.**

## Exact ONE-P test

The purified one-code theorem gives

`R_code(S_P)[g_P+2S_P/(lambda+1)] + L_Y`
`>= y(p+x+k_P)`.

On this family the right-hand side is

`y(p+x+k_P)=t(3t+5t+3t)=11t^2`.

The first term on the left is exactly `Ccap_P`, already bounded below by a quantity with leading coefficient `97.5t^2`. Therefore, even after setting the nonnegative `L_Y` term to zero,

> `Ccap_P > 11t^2`

for every `t>=2`.

Thus:

> **the exact purified `(ONE-P)` inequality also has a very large positive margin on this parameter ray.**

This is a method diagnostic only: it says the scalar inequality does not rule out the ray, not that the pair geometry is physically realizable.

## Exact CROWD scalar floor

The preserved pair-crowding floor is

`S_P >= s_crowd=[y(3y-D0)]_+`.

Here

`3y-D0=3t-(23t+1)=-20t-1`,

so

> `s_crowd=0`

for every `t>=1`.

Thus the scalar `(CROWD)` floor is identically vacuous on this direction.

## Consequence

All three audit-mandated **aggregate pair-local scalar gates** have now been tested on the explicit ray:

- exact `Ccap_P` has a large quadratic margin;
- purified `(ONE-P)` has a large quadratic margin even with `L_Y=0`;
- scalar `(CROWD)` is identically zero.

Therefore another aggregation of those same inequalities cannot close this ray. The next load-bearing mechanisms are the pieces that retain physical distribution and location: whether `rho=2t` can actually coexist with the required singleton matched-head geometry, the exact per-vertex witness reuse and located X--U/Y--U nonedges, rooted residual/defect feedback, and ultimately graph-level realizability of the rigid interface itself.

No claim is made that the family survives those stronger tests. Bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, and `X_3` remains the mandatory negative control.
