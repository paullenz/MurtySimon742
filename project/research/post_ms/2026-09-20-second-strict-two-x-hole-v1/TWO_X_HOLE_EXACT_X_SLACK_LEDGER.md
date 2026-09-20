# Two-X-hole branch — exact aggregate X-slack ledger

Date: 2026-09-20

Status: **same-session internal physical accounting theorem**. This combines the core-head bijection, certificate-incidence graph and complete localization of internal X-edges. It keeps the internal-edge variable explicit rather than replacing it immediately by a coarse bound.

## 1. Setup

Assume the core-saturated exact second-strict two-X-hole branch (`y>=2`, `x>=4`). Keep

- `omega=|U_o|`;
- certificate-incidence load `L=|E(J)|`;
- `e_X=e(G[X])`.

The preceding notes prove:

1. every X-vertex has exactly one common-core neighbour;
2. the buffer b is adjacent to exactly `x-2` vertices of X;
3. every X-vertex is adjacent to all y vertices of Y;
4. the L certificate incidences are L distinct X--U_o nonedges;
5. `G[R]` is edgeless and every internal X-edge touches one of the two holes;
6. the tight matched degree of every X-vertex is exactly p.

## 2. Exact aggregate degree ceiling on X

If every X--U_o pair not forced absent were present, the X-layer degree sum would be at most

> tight matched contribution: `xp`;
>
> X--Y contribution: `xy`;
>
> common-core contribution: `x`;
>
> buffer contribution: `x-2`;
>
> X--U_o contribution: `x omega-L`;
>
> internal-X contribution: `2e_X`.

There are no other possible neighbours of an A-vertex in the rooted partition. Therefore

`sum_{v in X} d(v)`
` <= xp+xy+x+(x-2)+(x omega-L)+2e_X`.

The root degree is

`b_root=2p+u=2p+x+1+omega`

because `u=x+1+omega` in the core-saturated branch. Hence

### Theorem 2.1 — exact aggregate X-slack floor

> **`L_X=sum_{v in X} epsilon_v`
> ` >=x(p+x-y)-(x-2)+L-2e_X`.**                         `(2X-LX)`

Equivalently,

> `L_X>=x(p+x-y-1)+2+L-2e_X`.

Every term is a physical incidence count. The `+L` and `-2e_X` terms should be kept together: each additional internal X-edge can buy at most two units of X-degree, while certificate traffic simultaneously removes X--U_o degree.

## 3. Exact Y-side price

The unloaded setup has

- `G[Y]=emptyset`;
- Y complete to X;
- Y anticomplete to `U_-=W_0 dotcup {b}` and to U_o;
- each Y-vertex has exactly p tight matched neighbours.

Therefore every Y-vertex has degree exactly `p+x`, so

> **`epsilon_y=p+1+omega` for every `y in Y`,**          `(2X-YPAY)`
>
> **`L_Y=y(p+1+omega)`.**                                `(2X-LY)`

Thus the full A-side floor is

> **`L_A>=x(p+x-y)-(x-2)+L-2e_X`
> `       +y(p+1+omega)`.**                              `(2X-LA)`

## 4. Internal-edge localization can be substituted without losing its class meaning

Let the two physical hole codes be `H_0=c(a_0)` and `H_1=c(a_1)`. The internal-X localization theorem gives

> `e_X<=m_{H_0}+m_{H_1}`,                                `(2X-EX-HOLE)`

with `m_H=|U_o cap V_{bar H}|` and absent classes interpreted as zero.

Therefore

> `L_A>=x(p+x-y)-(x-2)+L`
> `       -2(m_{H_0}+m_{H_1})+y(p+1+omega)`.             `(2X-LA-HOLE)`

This is intentionally **not** simplified to a function of omega: only witness populations complementary to the two physical hole codes can buy back the `-2e_X` term. All other outside classes increase L / outside slack without supporting X-density.

## 5. Full physical score ingredients before pair capacity

The unmatched-side pieces now sit in the following exact/necessary ledger:

- common core:
  `E_core>=x(p+x-1)+L`;
- buffer:
  `epsilon_b=p+2`;
- outside layer:
  `E(U_o)>=sum_z[p-x+2r_z]_+ >=[omega(p-x)+2L]_+`;
- A-side:
  `(2X-LA)` above;
- rooted U-edge ceiling:
  `q<=binom(omega,2)+(x+1)omega-L`.

Thus any future scalar score floor may use

> `S>=x(p+x-1)+L+(p+2)`
> `   +[omega(p-x)+2L]_+`
> `   +x(p+x-y)-(x-2)+L-2e_X`
> `   +y(p+1+omega)`.                                    `(2X-SCORE)`

But `(2X-EX-HOLE)` shows why flattening `e_X` to an anonymous integer is lossy: the only score rebate is tied to two distinguished complementary witness classes.

## 6. Strategic consequence

The branch now has a useful “no free density” principle:

> every unit of internal X-density must be purchased by one of at most two distinguished outside code classes, while **all** outside certificate traffic contributes to L and therefore to common-core holes, X--U_o holes, outside slack, and the q deficit.

The next pair-local attack should isolate the two hole-code pairs and ask whether their available `S_P/Ccap_P` resources can simultaneously support

1. the ordinary buffer-certificate load of those classes, and
2. the internal-X certificate load needed to realize a significant `e_X` rebate.

Unrelated outside classes cannot pay `(2X-EX-HOLE)` and should not be allowed to subsidize that local demand in a global scalar relaxation.