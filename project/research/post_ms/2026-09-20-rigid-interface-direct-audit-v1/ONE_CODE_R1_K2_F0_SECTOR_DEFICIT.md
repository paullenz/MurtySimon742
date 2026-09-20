# Residual-one k=2 fully-free exception sector deficit

Date: 2026-09-20

Status: **same-session candidate physical-ledger lemma**, conditional on the exact residual-one low-k identities. No criticality theorem and no finite scan are used in the main count.

The preceding exception-orientation conservation theorem shows that the only K-free U-vertices capable of repairing a K-heavy reservoir are the fully four-hole class

`F0={t in E=U\W_s : N_K(t)=empty, N_{W_s}(t)=empty}`.

This note shows that a large F0 class is itself physically expensive even before its incident edges are audited by D2C criticality.

## 1. Exact sector-deficit identity on the low-k ray

Specialize to the preserved exact low-k ray

`c=p=lambda`, `y=p-1`, `u=x=p+1`, `k=2`.

Then

- `|K|=2`;
- `|W_s|=2`;
- `|H|=x-k=p-1`;
- `|Y|=p-1`;
- `|E|=|U\W_s|=p-1`.

For `t in F0`, the exact U-degree identity is

`d_{A union U}(t)=p+u-1-epsilon_t=2p-epsilon_t`.          `(F0-DEG)`

Because t is anticomplete to K and W_s, every neighbour counted in `(F0-DEG)` lies in

`H union Y union (E\{t})`,

whose total size is

`(p-1)+(p-1)+(p-2)=3p-4`.

Define

`alpha_t=|H\N(t)|`,

`beta_t=|Y\N(t)|`,

`gamma_t=|(E\{t})\N(t)|`.

Then exact degree counting gives

> **`alpha_t+beta_t+gamma_t=p-4+epsilon_t`.**             `(F0-DEF)`

This is an identity, not an inequality. Since the universal escape floor gives `epsilon_t>=2`, every fully-free exception has at least `p-2` additional missing incidences across H, Y and the remaining escape reservoir, beyond its already-forced four holes to K and W_s.

## 2. Distinct physical holes

Let `F0` have size f and write

`E_F=sum_{t in F0} epsilon_t`.

Let

- `Z_H(F0)` be the number of missing H--F0 pairs;
- `Z_Y(F0)` be the number of missing Y--F0 pairs;
- `M_U(F0)` be the number of **distinct** missing U--U pairs with at least one endpoint in F0 and the other endpoint in E.

Summing `(F0-DEF)` gives

`Z_H(F0)+Z_Y(F0)+Gamma = f(p-4)+E_F`,                   `(F0-SUM)`

where

`Gamma=sum_{t in F0} gamma_t`.

A missing pair inside F0 is counted twice in Gamma, while a missing pair from F0 to `E\F0` is counted once. Therefore

`Gamma<=2 M_U(F0)`,

so

> **`M_U(F0)>=Gamma/2`.**                                  `(F0-U)`

Combining with `(F0-SUM)` yields the distinct-hole bill

> **`Z_H(F0)+Z_Y(F0)+M_U(F0)`**
> **`>= [f(p-4)+E_F]/2`.**                                `(F0-PHYS)`

The three currencies are physically separated: H--U holes feed the X-side rooted identity, Y--U holes feed the Y-side/rooted residual ledger, and missing U--U pairs reduce the rooted triangle reservoir `q=e(G[U])`.

In particular, using `E_F>=2f`,

> **`Z_H(F0)+Z_Y(F0)+M_U(F0) >= f(p-2)/2`.**              `(F0-COARSE)`

Thus a linear-size F0 reservoir already carries a quadratic physical defect on the low-k ray.

## 3. Consequence for the endpoint classification

The low-k escape reservoir has size `p-1`. The previous structural packages now price every obvious asymptotic endpoint in a genuinely physical currency:

- K-heavy vertices: exception-orientation conservation gives a quadratic bill on any linear K-heavy population;
- W-heavy vertices: Y-anticompleteness and the W-heavy internal-edge theorem give located Y--U and U-slack bills;
- mixed K/W vertices: each pays `epsilon>=p+1`;
- K-free vertices touching one selected witness: they are Y-anticomplete and anticomplete to the K-heavy reservoir;
- fully K/W-free vertices F0: `(F0-COARSE)` gives at least `f(p-2)/2` additional H/Y/U-sector holes.

This does not by itself establish the final score/rooted contradiction because these currencies must still be inserted without double counting into the exact rooted residual identities. It does remove the idea that a large F0 exceptional class can be treated as a cheap witness reservoir.

## 4. Next move

The next calculation should retain the partition sizes and the three located F0 sectors instead of collapsing them into total slack. Combine

- `(OC-PHYS)` for the K-heavy population;
- `(F0-PHYS)` for the fully-free exception population;
- W-heavy Y-holes / internal capacity;
- the `p+1` mixed-vertex slack price;

with the exact identities for `L_X`, `Z_X`, `Z_Y` and `q=e(U)`. If the resulting partition minimum is quadratic with coefficient exceeding the available low-k residual budget, the exact unbounded parameter ray becomes finite-order. If not, the minimizing partition will identify a much smaller literal geometry for raw-criticality attack.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; this remains conditional downstream mathematics pending independent hostile replay.