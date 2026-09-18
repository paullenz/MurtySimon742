# Pair residual demand with local A--U cross deficit

Date: 2026-09-18

Status: strengthening of `COMPLEMENT_PAIR_RESIDUAL_DEMAND.md`.

The first pair-demand theorem deliberately used only coded-layer outside capacity. Retaining the actual A--U degree split gives an extra nonnegative term which is globally explicit in `q` and `E_U`. This creates a direct interface between the source/Hall unmatched machinery and the complementary-pair residual demand.

## 1. Local cross deficit

For an unordered complementary tight-code pair `P={c,bar c}`, keep

`A_P=A_c union A_bar c`, `a_P=|A_P|`, `L_P=L_c+L_bar c`.

Put

> `s_P=e_G(A_P,U)=sum_{z in A_P} d_U(z)`,                `(Z0)`

and define the pair A--U nonedge deficit

> `Z_P=a_P u-s_P`.                                       `(Z1)`

Thus `Z_P>=0` and, because the complementary pairs partition A,

> `sum_P Z_P=au-s`.                                      `(Z2)`

Using

`E_U=u(p+u-1)-2q-s`

and

`a=2p+u-lambda-1`,

the total cross deficit is exactly

> `Z:=sum_P Z_P`
> ` =u(p-lambda)+2q+E_U`.                                `(Z3)`

So `q` and unmatched slack do not merely raise the global forced A-edge mass through the residual split; they also create a **separate local crowding resource** distributed over complementary A-pairs.

## 2. Exact strengthened pair crowding

For `z in A_P`,

> `d_A(z)=p+u-epsilon_z-d_U(z)`.                         `(Z4)`

There are at most `a-a_P` A-vertices outside `A_P`, hence

`d_{A_P}(z)>=d_A(z)-(a-a_P)`.

Summing over `A_P` gives

> `2e(G[A_P])`
> ` >=a_P(p+u)-L_P-s_P-a_P(a-a_P)`
> ` =a_P(a_P+lambda+1-p)-L_P-s_P`.

Since `T=p+u-lambda-1` and `Z_P=a_Pu-s_P`, this is

### Lemma 2.1 — cross-deficit pair crowding

> `2e(G[A_P])`
> ` >=a_P(a_P-T)-L_P+Z_P`.                               `(ZPC)`

This strictly strengthens the previous pair crowding bound by the exact nonnegative term `Z_P`.

## 3. Strengthened non-direct demand

Let `R_P=sum_{z in A_P} r_z d_A(z)` be the local rooted-slot Hamming resource. The local direct-edge theorem gives

> `2pD_P<=R_P`.                                          `(ZPD)`

Writing `N_P=e(G[A_P])-D_P` for internal non-direct A-edges, combine `(ZPC)` and `(ZPD)`:

### Theorem 3.1 — cross-deficit pair residual demand

> `2N_P`
> ` >=[a_P(a_P-T)-L_P+Z_P-R_P/p]_+`.                    `(ZPRD)`

Every such `N_P` is forced to use a matched-B or A/U certificate whose source remains in pair `P`. Therefore the preserved local capacities give

### Theorem 3.2 — strengthened complementary-pair feasibility

> `[a_P(a_P-T)-L_P+Z_P-R_P/p]_+`
> ` <=R_code(S_P)[g_P+2S_P/(lambda+1)]`
> `   +2h_P`.                                             `(ZCPRF)`

Here:

- `g_P` is the number of tight fibres whose gamma pair is `P`;
- `h_P=sum_{i in I_P}min(t_i^0,t_i^1)` is the pair's two-sided matched-foot traffic;
- `sum_P g_P=p`;
- `(lambda+1)sum_P h_P<=R_A(L_A)L_A`;
- `sum_P R_P<=rK_A`;
- `sum_P Z_P=u(p-lambda)+2q+E_U`.

Thus `q` and `E_U` now enter the pair-local feasibility problem twice but through genuinely different mechanisms:

1. the exact residual split raises the total required A-edge mass;
2. `(Z3)` distributes A--U missing-incidence mass that locally raises internal pair crowding.

## 4. Aggregate positive-part consequence

Summing `(ZPRD)` and using `sum [x_P]_+ >= [sum x_P]_+` yields

> `2 sum_P N_P`
> ` >=[sum_P a_P^2-T a-L_A+Z-(1/p)sum_P R_P]_+`.

Since `sum_P R_P<=rK_A`, a coarser consequence is

> `2 sum_P N_P`
> ` >=[sum_P a_P^2-T a-L_A`
> `      +u(p-lambda)+2q+E_U-rK_A/p]_+.                  `(ZAGG)`

This is not expected to close the branch after replacing `sum a_P^2` by a crude distribution-free minimum; the value is that the exact pair form `(ZCPRF)` retains the allocation of all resources.

## 5. Strategic consequence

The live pair-resource system now contains a positive local input `Z_P` whose global total is fixed by `q,E_U`. This is the missing direct bridge from the unmatched/source-Hall side into the local complementary-pair demand.

The next natural target is to constrain how `Z_P` can be anti-correlated with `a_P` and `S_P`. In particular, a pair that tries to avoid internal crowding by keeping `a_P` small can still be forced into `(ZCPRF)` if it carries a large share of the A--U nonedge deficit. This is more promising than another global scalar cap because unrelated pair slack still cannot pay the local positive-part demand.

The `X_3` hostile control has `u=q=E_U=0`, hence `Z_P=0` for every pair, and remains untouched.