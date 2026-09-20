# Residual-one k=2 one-sided reservoir conservation

Date: 2026-09-20

Status: **same-session candidate consequence** of the residual-one hub theorem and `ONE_CODE_R1_LOW_K_ESCAPE_AND_MIXING_DICHOTOMY.md`. Conditional on rigid-interface reachability. No finite scan is used as proof.

## 1. Exact K and W_s slack in terms of escape incidences

Assume the residual-one branch with `k=2`, and write

`K={a,b}`, `W_s={z_a,z_b}`, `E=U\W_s`, `|E|=c-1`.

Put

`A=sum_{w in E}|N(w) cap K|`,

`B=sum_{w in E}|N(w) cap W_s|`.

The beta map is the transposition, so `ab` is a nonedge and each K-head is adjacent to exactly its own selected witness in W_s. The exact K degree formula from the physical-reprice note is

`epsilon_h=g0+u-e_K(h)-d_U(h)`.

Here `e_K(h)=0`, `u=c+1`, and `d_U(h)=1+d_E(h)`. Hence

> `epsilon_a+epsilon_b=2(lambda+1)-A`,                   `(KC-K)`

using `g0+c=lambda+1`.

For a used witness z, the exact U-side degree identity is

`p+u-1-epsilon_z=d_{A union U}(z)`.

Each `z_h` has exactly one A-neighbour, no Y-neighbour, no W_s-neighbour, and its remaining A/U neighbours are precisely its B-neighbours in E. Therefore

> `epsilon_{z_a}+epsilon_{z_b}=2(p+c-1)-B`.              `(KC-W)`

## 2. Beta cross holes give an exact four-vertex capacity

The two beta singleton equations imply, for every escape w,

`1_{wa}+1_{wz_b}<=1`,

`1_{wb}+1_{wz_a}<=1`.

Adding them gives

> `|N(w) cap (K union W_s)|<=2`.                          `(KC-CAP)`

Summing over `|E|=c-1`,

> `A+B<=2(c-1)`.                                         `(KC-AB)`

Combining `(KC-K)`, `(KC-W)` and `(KC-AB)` yields the source-local conservation law

> **`E_K+E_Ws >= 2(p+lambda+1)`.**                       `(KC-KW)`

This is independent of how the escape reservoir is split between serving K and serving W_s.

For `p>=4`, orientation covering already gives `epsilon_w>=2` for every escape. Hence

> **`E_K+E_Ws+E_E >= 2p+2lambda+2c`.**                  `(KC-TOT)`

On the exact low-k ray `p=lambda=c=t`, this is simply

> `E_K+E_Ws+E_E>=6t`.                                    `(KC-RAY)`

## 3. Mixed escapes add a linear-in-p penalty

Let `r_mix` be the number of escape vertices adjacent to at least one K-head and at least one used witness. The mixing theorem gives `epsilon_w>=p+1` on those vertices, while every other escape still pays at least 2. Therefore

> `E_E>=2(c-1)+r_mix(p-1)`.                              `(KC-EMIX)`

Together with `(KC-KW)`,

> **`E_K+E_Ws+E_E >= 2p+2lambda+2c+r_mix(p-1)`.**        `(KC-MIXTOT)`

Thus any near-minimal realization of the low-k ray must have very few mixed escape vertices; the cheap geometry is genuinely one-sided rather than a bookkeeping artifact.

## 4. Radius-two heads price every K-serving escape

Let `j2=|J2|`, and let `r_K` be the number of escape vertices having at least one neighbour in K.

Every such vertex is not J2-bad, because `(OM-BAD0)` would make it anticomplete to K. Hence it misses all `j2` vertices `q_i`, `i in J2`. Independently, the beta cross equations already force two missing pairs into `K union W_s`. Therefore

> `epsilon_w>=2+j2` for every K-serving escape w.         `(KC-J2V)`

Consequently

> **`E_E>=2(c-1)+j2*r_K`.**                              `(KC-J2)`

If `A` is the total number of K--E incidences, then each escape supplies at most two, so `r_K>=ceil(A/2)` and

> **`E_E>=2(c-1)+j2*ceil(A/2)`.**                        `(KC-J2A)`

Together with `(KC-K)`, this explicitly exposes the tradeoff between reducing K-slack by adding K--E edges and paying radius-two matched-fibre holes on the serving escape vertices.

## 5. Exact cheap endpoint and method boundary

The lower bound `(KC-TOT)` is itself physically sharp at the level of the current incidence constraints. If every escape is one-sided, has exactly two neighbours in `K union W_s`, and has slack exactly two, then each escape is of one of two saturated types:

- **K-heavy:** complete to `{a,b}` and anticomplete to `{z_a,z_b}`;
- **W-heavy:** complete to `{z_a,z_b}` and anticomplete to `{a,b}`.

If `r` escapes are K-heavy and the remaining `c-1-r` are W-heavy, then `(KC-AB)` is tight and the sum `E_K+E_Ws` is independent of r. On the exact ray `p=lambda=c=t`, the present degree equations permit the scalar equality value `6t` for `E_K+E_Ws+E_E`.

This is an important stop/pivot fact: **degree conservation plus the one-sided mixing theorem alone does not close the low-k ray.** The next theorem must attack the realizability of the saturated K-heavy/W-heavy types themselves (or price their matched-coordinate/rooted-Q consequences), rather than aggregate their degree slack again.

In particular, a K-heavy escape is automatically J2-clean and therefore pays the `j2` matched-endpoint holes. A W-heavy escape avoids that conclusion and is the most permissive endpoint. The highest-value next raw-criticality target is consequently a W-heavy escape adjacent to both same-code used witnesses `z_a,z_b` while anticomplete to K.
