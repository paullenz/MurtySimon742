# One-code rigid cut — near-equality matched/U slot price

Date: 2026-09-20

Status: **same-session structural strengthening** in the audit-authorized one-code rigid branch. This note uses not only `M_X=E_X=0`, but the stronger provenance of a discrete Hall near-equality event:

> `J_X+kappa_X<1`.

Since both terms are nonnegative, in particular

> `J_X<1`.                                                `(NR-0)`

The result couples the corrected private-coordinate normal form to the exact direct/Hamming credit `J_X`, producing a new local score floor before another total-score relaxation.

## 1. One-code setup and the minimum U count per source

Assume Y has one tight code d. For each source `s in Y`, let `k_s` be the number of its x selected crossing witnesses that lie in U. Put

> `k_*:=min_{s in Y} k_s`.                                `(NR-1)`

Let P={d,bar d} and retain the pair-local gamma count `g_P`. Since at most `g_P` matched endpoints have gamma d,

> `k_*>=k_P:=[x-g_P]_+`.                                  `(NR-2)`

Every source uses at least k_* U-witnesses. The standard one-code incidence/slack proof therefore strengthens verbatim with k_* in place of k_P:

> `Z_X>=k_*(x-1)`,                                        `(NR-ZX)`
> `Z_Y>=y k_*`,                                           `(NR-ZY)`
> `E_U>=k_*(p-1)` when `g0=p-y>=1`.                       `(NR-EU)`

Now choose a source s attaining the minimum k_*. Its remaining

> `m:=x-k_*`

crossing heads are selected through matched singleton witnesses and therefore carry the private-coordinate system of `RIGID_PRIVATE_COORDINATE_NORMAL_FORM.md`.

## 2. If at least three heads are matched-covered, none of their pairs is complementary

Assume `m>=3` and let H be the matched-covered head set for s.

Take distinct `h1,h2 in H`. Suppose their codes were complementary. Choose a third `h3 in H`. The private coordinate of h3 is a coordinate at which **every other H-head**, in particular h1 and h2, agrees with d. But two complementary binary codes cannot both agree with d at the same coordinate. Contradiction.

Hence:

> **if `m>=3`, no two heads in H have complementary codes.** `(NR-NODIR)`

Every internal edge of G[H] is therefore a non-direct A-edge. By private coordinates,

> `d_H(c(h),c(h'))>=2`

for every distinct pair in H.

## 3. Near-equality forces the matched-covered subgraph to be sparse

Sum the local rooted Hamming inequality over all vertices of A_X. If `D_X` is the number of direct internal A_X edges and `N_X` the non-direct ones, then

`R_X:=sum_{z in A_X} r_z d_A(z)`
` >= 2p D_X + 2 sum_{e in N_X} d_H(e)`.

Since

`J_X=R_X/p-2D_X`,

we obtain

> `J_X >= (2/p) sum_{e in N_X} d_H(e)`.                  `(NR-J)`

All internal H-edges are non-direct and have Hamming distance at least two, so

> `J_X >= 4e(H)/p`.                                       `(NR-JH)`

Together with `(NR-0)`:

> **`e(H)<p/4`.**                                         `(NR-SPARSE)`

Equivalently, because e(H) is integral,

> `e(H)<=ceil(p/4)-1`.

This is a new structural consequence of the *near-equality provenance* of the rigid cut; it need not hold for an arbitrary complete cut with `M_X=E_X=0` that was not produced by the discrete Hall stability theorem.

## 4. Convert H-sparsity into an X-slack bill

Let `e_X=e(G[A_X])`. Removing the k_* U-certified heads can delete at most

`k_* x-k_*(k_*+1)/2`

internal X-edges. Hence

`e(H)>=e_X-k_*x+k_*(k_*+1)/2`.

The exact rigid degree identity is

`2e_X=xg0-L_X+Z_X`,

where `g0=x-T0=p-y`.

Using `Z_X>=k_*(x-1)` gives

`2e(H) >= xg0-L_X-k_*(x-k_*)`.                            `(NR-EHLOW)`

When `m=x-k_*>=3`, combine this with `e(H)<p/4`:

> **`L_X > xg0-k_*(x-k_*)-p/2`.**                        `(NR-LX)`

Since L_X is a nonnegative integer, define

> `ell(k):=max(0, floor(xg0-k(x-k)-p/2)+1)`.              `(NR-ELL)`

Then every actual value `k_*=k<=x-3` satisfies

> `L_X>=ell(k)`.                                          `(NR-LXINT)`

## 5. A new one-dimensional near-rigid score floor

For `g0>=1`, `(NR-EU)` and `(NR-LXINT)` give, for `k<=x-3`,

> `S=L_A+E_U >= ell(k)+k(p-1)`.                           `(NR-SK)`

For `k>=x-2`, the private-coordinate third-head argument no longer applies, but the safe U-slack floor remains

> `S>=k(p-1)`.                                            `(NR-SK2)`

Because `k_*>=k_P`, define the exact finite floor

> `Theta(p,x,g0,k_P)`
> ` := min_{k_P<=k<=x} F(k)`,                             `(NR-THETA)`

where

`F(k)=k(p-1)+ell(k)` for `k<=x-3`,

and

`F(k)=k(p-1)` for `k>=x-2`.

Then every near-rigid one-code cut with `g0>=1` satisfies

> **`S>=Theta(p,x,g0,k_P)`.**                             `(NR-SCORE)`

This floor is independent of the gamma-collision score `phi(g_P)`. Since both `ell(k)` and `phi(g_P)` are lower bounds on portions of L_A, they must be combined by a **maximum**, not by addition. A safe pair-local strengthened floor is therefore

> `S >= k_*(p-1)+max{ell(k_*), phi(g_P)}`                 `(NR-GAMMA)`

for `k_*<=x-3`, with the analogous `phi`-only form when `k_*>=x-2`.

## 6. Easy exact subcases

If `k_*=0` (all x heads matched-covered for a minimum-U source), then x>=3 and

> `L_X > xg0-p/2`,
> `S>=max{floor(xg0-p/2)+1, phi(g_P)}`.                   `(NR-K0)`

If `k_*=1` and x>=4,

> `L_X > xg0-(x-1)-p/2`,
> `S >= (p-1)+max{ell(1),phi(g_P)}`.                      `(NR-K1)`

These are precisely the cases in which the old gamma/U tradeoff is most tempted to make matched certification cheap.

## 7. Strategic consequence

The existing `Psi_p(x)` obstruction prices **how many** matched fibres share the source gamma code versus how many U-witnesses are needed. `(NR-SCORE)` prices a different fact: if the near-equality rigid cut actually uses many of those matched channels simultaneously, their private coordinates force Hamming load, and `J_X<1` can only survive if the matched-covered part of A_X is extremely sparse. The exact A_X degree identity then converts that sparsity into A-slack.

The correct next diagnostic is therefore not another broad state count. It is an independent comparison of

- `Psi_p(x)`;
- `(ONE-P)` and `(CHAN-P)`;
- `(CROWD)`;
- the new `Theta` / `(NR-GAMMA)` floor;

while retaining `g_P`, `k_*`, `L_Y`, `E_bar`, `u_bar`, and the rooted residual identity. Any new finite scan remains diagnostic only; the hand theorem above is the promoted content.