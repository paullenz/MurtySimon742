# One-code rigid cut — post-exhaustion residual-dimension-one escape family

Date: 2026-09-20

Status: **same-session method diagnostic**, conditional on the rigid one-code interface. This is not a graph construction. Its purpose is to identify the first exact scaling direction that survives the new private-coordinate exhaustion theorem and the current aggregate score / rooted-Q / pair-local gates.

The predecessor scalar escape direction with `d_U=c`, `m=p`, `k>0` is impossible after private-coordinate exhaustion. The adjacent boundary `d_U=c-1`, i.e. residual Boolean dimension `r=1`, remains the correct structural stress test.

## 1. Exact family

For integer `t>=2`, set

- `c=2t`;
- `p=2t`;
- `y=1`;
- `g0=p-y=2t-1`;
- `lambda=g0+c-1=4t-2`;
- `u=3t`;
- `x=p+u-c=3t`.

For the minimum source take

- escape count `d_U=c-1=2t-1`;
- U-witness count `k=u-d_U=t+1`;
- matched singleton count `m=x-k=2t-1=p-1`;
- residual coordinate dimension `r=p-m=1`.

Thus the family satisfies the exact minimum-source identities and the private-coordinate exhaustion theorem. The r=1 profile forces all k U-certified heads to have the single code

`C=d xor e_j`

for the unique residual coordinate j.

The order is

> `n=4p+2u-lambda=10t+2`.                                `(EF-n)`

So this is genuinely unbounded as a parameter family.

## 2. Total physical-score test

Take the natural collision parameter

`g_P=m=2t-1`,

so

`k_P=x-g_P=t+1=k`.

The gamma-collision floor is

`phi(m)=(2t-1)(2t-2)=4t^2-6t+2`.

The hostile-replayed used-witness independence theorem gives the pair-located physical witness floor

`E_W>=k(p+k-2)`

`=(t+1)(3t-1)`

`=3t^2+2t-1`.

For this same source, the preserved Hamming-slot bound gives

`L_X>=floor[x g0-k(x-k)-p/2]+1`

`=4t^2-5t+2`.

This exceeds `phi(m)` by t. Therefore the strongest present non-overlapping A+U scalar floor is

> `E_W+L_X >= 7t^2-3t+1`.                                `(EF-score)`

Since `lambda=4t-2` is even,

`A_lambda=lambda^2/2+lambda+4=8t^2-4t+4`,

and the exact score ceiling is

> `C0=12t^2+6t-4`.                                       `(EF-C0)`

The margin is

> `C0-(E_W+L_X)=5t^2+9t-5>0`.                            `(EF-margin)`

Thus the present physical score package does not close this r=1 family.

## 3. Rooted-Q feedback test

Used-witness independence gives

`q<=d_U u-d_U(d_U+1)/2`

`=4t^2-2t`.

The exact rooted-Q feedback inequality has left side

`k(x+y-1)+phi(m)=7t^2-3t+2`

and right side

`u(p-lambda)+2d_Uu-d_U(d_U+1)+C0`

`=14t^2+8t-4`.

Hence the rooted-Q margin is

> `7t^2+11t-6>0`.                                        `(EF-Qmargin)`

So the new triangle-capacity feedback is informative but still does not eliminate this direction.

## 4. Audit-mandated pair-local scalar gates

The exact pair-capacity parameter is

`D0=5p+5u-3lambda-2=13t+4`,

with

`lambda+1=4t-1`,

`g_P=2t-1`,

and pair-located witness slack at least

`S_P=3t^2+2t-1`.

The crossing load is only

> `2xy=6t`.                                               `(EF-cross)`

The exact capacity expression

`Ccap_P=R_code(S_P)[g_P+2S_P/(lambda+1)]`

already has both factors linear in t, hence quadratic growth, while `(EF-cross)` is linear. In particular the exact gate has ample margin for large t; direct substitution at the small endpoint t=2 is already positive, so monotonic growth leaves no asymptotic obstruction.

Likewise purified `(ONE-P)` has right side

> `y(p+x+k_P)=6t+1`,

while its pair-capacity term is quadratic. Finally the scalar crowding floor is

`[y(3y-D0)]_+=[3-(13t+4)]_+=0`.

Therefore exact `Ccap_P`, purified `(ONE-P)` and scalar `(CROWD)` do not close this r=1 direction. This is only a method diagnostic: no graph realization is asserted.

## 5. What the family really says

Unlike the superseded pre-exhaustion ray, this family respects the private-coordinate geometry. It therefore identifies a real next structural bottleneck:

- `p-1` coordinates are consumed as distinct private matched coordinates;
- **one coordinate j remains**;
- all `t+1` U-certified X-heads have the same code `C=d xor e_j`;
- their selected U-witnesses have code `bar(d)` and form an independent set;
- `A_bar(C)=emptyset` and `|U_bar(C)|<=c-1` by the residual-one profile;
- all selected head-witness pairs share the same residual coordinate j.

The remaining freedom is therefore not a diffuse high-dimensional code problem. It is a one-coordinate physical routing problem.

## 6. Strategic conclusion

Another scalar minimization of the existing score, rooted-Q or pair-capacity inequalities cannot by itself remove the family. The next high-value theorem should attack the k head-witness edges

`A_C -- W_s subseteq U_bar(d)`

through raw criticality and the unique residual coordinate j, while preserving global selected `(source,coordinate)` uniqueness.

A plausible success criterion is a constant capacity on the number of such head-witness pairs sharing j. Any bound `k=O(1)` would immediately kill this scaling ray because `k=t+1`.

Until such a theorem is proved, this file is a **method obstruction**, not positive evidence that actual D2C graphs realize the family. Bounded graph-level regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, and X_3 remains the mandatory negative control.