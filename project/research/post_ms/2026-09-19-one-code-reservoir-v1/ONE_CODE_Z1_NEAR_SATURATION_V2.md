# One-code `z=1` near-saturation — corrected v2

Date: 2026-09-19

Status: **load-bearing replacement** for `ONE_CODE_Z1_NEAR_SATURATION.md` on the full-support traffic accounting. The v1 file is preserved as an audit trail and must not be cited for the statement `H=e_++e_-<=rho` in the full-support branch.

## 1. Correction found by immediate hostile re-read

The v1 support dichotomy, common-buffer geometry, common-core slack, safe score gates, and full-support crossing-incidence degree calculation are sound in substance. One bookkeeping statement was too strong in the full-support branch.

V1 wrote

`H=e_++e_- = e(Y)+e(Y,U_d)+e(U_{bar d})`

and then asserted `H<=rho`, where `rho` is the number of crossing holes in `Y x U_{bar d}`.

That is not justified when the crossing layer has full support: an internal `Y` edge can still use a **matched-B** certificate rather than an A/U certificate, so not every unit of `e(Y)` consumes a physical crossing hole. The correct hole-consuming quantity counts only internal-Y edges whose selected certificate uses the A/U channel.

The correction below preserves the useful exact normal form and, importantly, the later residual cancellation.

---

## 2. Setup and support dichotomy

As before, `u_-=k+1`, `k=x-g>0`, and `W=U_{bar d}`. Every source in `Y` uses at least `k` distinct members of `W` as crossing witnesses. Therefore the union of crossing witnesses has size exactly `k` or `k+1`.

- **Common-buffer branch:** the union has size `k`; every source uses the same core `W_0`, and the unique `b in W\W_0` is unused by crossing certificates.
- **Full-support branch:** every member of `W` is used by at least one crossing source.

This dichotomy is unchanged.

---

## 3. Common-buffer branch remains as stated, with the missing matched-saturation justification made explicit

In the common-buffer branch each source uses exactly `k` U-witnesses on its `x=g+k` crossing edges. Hence it uses exactly `g` matched-B crossing witnesses. Summed over `Y`, the crossing layer already uses

`yg`

matched-B certificates sourced in code `d`.

But the purified matched-channel theorem gives the **global** bound

`P_P<=yg`.

Therefore the crossing layer saturates the entire matched channel, and **no internal edge of `Y` can be matched-certified**. Every internal-Y certificate must use the A/U channel.

Consequently every extra object in

`e(Y)+e(Y,U_d)+e(U_{bar d})`

does consume a physical `Y x {b}` pair. Thus the common-buffer conclusions from v1 are retained:

1. `W_0` is independent;
2. every `U_{bar d}` edge is incident with `b` and sourced at `b`;
3. every internal-Y A/U certificate, every `Y--U_d` same-code certificate, and every `U_{bar d}` same-code certificate uses a distinct `Y x {b}` pair;
4. with
   `H=e(Y)+e(Y,U_d)+e(U_{bar d})`, one has `H<=y`;
5. the core pays
   `E_core>=k(p+k-2)`;
6. each buffer use adds a new Y--U nonedge, so
   `Z>=k(a-1)+H`;
7. if `H>0`, the buffer has no X-neighbour and
   `epsilon_b>=[p-y+k+e_+]_+`,
   where `e_+=e(Y)+e(Y,U_d)`.

The common-buffer residual bridge is therefore unchanged.

---

## 4. Correct full-support accounting

Assume all `k+1` vertices of `W` are used by crossing certificates.

Let

- `rho` = number of crossing holes, i.e. sources using exactly `k` rather than `k+1` U-witnesses;
- `c_Y` = number of internal `Y` edges whose selected certificate uses the A/U channel;
- `m_Y=e(Y)-c_Y` = number of internal `Y` edges using the matched-B channel;
- `e_{YU}=e(Y,U_d)`;
- `e_-=e(G[W])`;
- `A=c_Y+e_{YU}+e_-` = number of **auxiliary physical-hole uses**.

The crossing U-incidence count is

`I=yk+(y-rho)`.

Hence the crossing matched-B count is

`xy-I = yg-y+rho`.

Since the total matched channel satisfies `P_P<=yg`, the internal matched traffic obeys

> `m_Y<=y-rho`.                                           `(MROOM)`

All `I` crossing A/U certificates occupy non-hole physical pairs in `Y x W`. The three auxiliary A/U/same-code families counted by `A` inject into the remaining physical holes. Therefore

> `A<=rho`.                                               `(AHOLE)`

These two inequalities together imply the old coarse reservoir consequence

`e(Y)+e_{YU}+e_- = m_Y+A <= y`,

but they do **not** imply that this whole quantity is at most `rho`.

---

## 5. Correct full-support slack and defect equations

For `w in W`, let

- `t_w` = number of crossing sources using `w`;
- `a_w` = number of auxiliary physical-hole uses involving `w`;
- `d_W(w)` = its degree in `G[W]`.

Every `w` is a crossing witness and hence has exactly one X-neighbour. Its Y-nonneighbours include the disjoint crossing-source and auxiliary-partner sets. Therefore

`epsilon_w>=p-y+k-1+t_w+a_w-d_W(w)`.

Summing gives

> `E_- >= (k+1)(p+k-1)-rho+A-2e_-`.                      `(FULL-E-v2)`

Likewise the X--U nonedges contribute `(k+1)(x-1)`, the crossing incidences contribute `yk+y-rho`, and the auxiliary hole uses contribute `A`, so

> `Z >= k(a-1)+(a-1)-rho+A`.                             `(FULL-Z-v2)`

Define the number of unused crossing holes

> `j:=rho-A>=0`.                                          `(J)`

Then the two exact inequalities become

> `E_- >= B-j-2e_-`,                                      `(J-E)`
>
> `Z >= Z0-j`,                                            `(J-Z)`

with

`B=(k+1)(p+k-1)`,

`Z0=(k+1)(a-1)`.

Moreover `A>=e_-` and `rho<=y`, so

> `j+e_-<=y`.                                             `(JROOM)`

This is exactly the normal form needed by the residual elimination; the v1 formula survives after replacing the incorrect `H` by the correct auxiliary-hole count `A`.

---

## 6. Safe full-support floors and exact residual elimination survive

From `j+e_-<=y`,

`E_- >= B-j-2e_- >= B-2y+j`.

Hence the safe pure floor remains

> `E_->=[B-2y]_+`.                                        `(FULL-E0-v2)`

Also `Z>=Z0-j` and `j<=y`, so the relaxed defect floor

> `Z>=k(a-1)+(x-1)`

is unchanged.

If `B>=2y`, put

`Ebase=B-2y`,

`D0=Z0-u(p-lambda)`.

Then

`E_U>=Ebase+j`,

`2q+E_U>=D0-j`.

The same integer cancellation gives the corrected, still-valid hole-free residual theorem

> `q+E_U >= Ebase+ceil([D0-Ebase]_+/2)`.                  `(FULL-EXACT-QE-v2)`

Thus the main structural advance of the exact-elimination note is **not** lost by the bookkeeping correction.

---

## 7. Diagnostic status

The v1 bounded score gates used only

- common-buffer `phi(g)+k(p+k-2)`; and
- full-support `phi(g)+[B-2y]_+`.

Both remain valid under the corrected accounting. Therefore the previously frozen diagnostic counts remain unchanged:

- older shared-floor `z=1` possibilities: `86,820`;
- common-buffer gate survivors: `76,463`;
- full-support gate survivors: `77,310`;
- either support type: `78,167`;
- newly rejected relative to the older `z=1` floor: `8,653`.

No graph-realizability meaning is attached to these counts.

## 8. Trust update

Use this v2 file, not the v1 full-support `H<=rho` statement, as the load-bearing `z=1` theorem. The correction is local and was found before the branch was used downstream beyond the residual formulas. The exact residual formulas survive with the repaired variable `A=c_Y+e(Y,U_d)+e_-`.

The next work remains: common-buffer loaded/equality classification and the full-support `B<2y` truncation strip, followed by comparison with `(ONE-P)/(CHAN-P)`.
