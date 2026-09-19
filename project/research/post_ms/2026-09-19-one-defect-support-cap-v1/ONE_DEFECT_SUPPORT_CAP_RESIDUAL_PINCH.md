# One-defect support-channel / residual pinch

Date: 2026-09-19

Status: internal structural theorem package for the eventual / sufficiently-large dense diameter-2-critical programme around `M(n)=floor((n-1)^2/4)+1`. Everything below remains conditional on the rigid one-code complete-cut / minimal-reservoir hypotheses. It is not graph-realizability evidence and does not assert the false all-order 2019 Dailly–Foucaud–Hansberg conjecture.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, root `README.md`, the newest commits, the 19 September daily red-team audit, the repaired source-premise note, and the graph-level regression handoff. The audit boundary is unchanged: `X_3` remains mandatory; the finite source-tuple theorem is not promoted beyond its selected-system interface; the actual-graph regression remains the independent premise check; exact pair-local `S_P/Ccap_P` remains live; and the four-exception gate stays subordinate. No audit-weakened line is resumed.

The predecessor requested first: (i) intersect the `E=1` pair bill with the exact rooted `q/E_U` allocation, and (ii) test whether both directed selected-witness adjacencies across one defect/radius-one support pair can coexist. Those are the first two tasks below.

## 2. Retained one-defect setup

Stay in the positive-buffer unloaded common-buffer rigid one-code branch at minimal outside reservoir `m=g+1`.

Use the predecessor notation:

- `X--Y` complete, `x>=3`, `y>0`, `a=x+y`;
- Y code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `X=H_M dotcup H_0`, `|H_M|=g`, `|H_0|=k`;
- `H_0` has one common code and one common selected outside witness;
- `A=g-d_{H_M}(z_*)`, `M=(u_o-1)-d_{U_o\{z_*}}(z_*)`, `N=u-k-2`;
- `D(A,M)=Q_H-(2k-1)A-kM`;
- `E_max(A)=binom(g,2)+kA`;
- `Delta=E_max(A)-e(X)>=0`;
- exact crossing capacity gives `S_P>=sigma_P`.

Assume `E=1` in the Hamming-defect notation. There is one radius-two defect head and all remaining X-code classes have radius one. Put `d_0:=g-A`. For `k>1`, the predecessor proved `d_0 in {0,1}`; for `k=1`, `0<=d_0<=2`.

Let J be the total number of A-neighbour incidences over the `g+1` selected outside witnesses. Selected outside witnesses are nonadjacent to the head(s) they serve, so J counts only wrong-head incidences.

## 3. Unit I — support-channel localization and the correct incidence envelope

The predecessor support-intersection theorem says that a selected outside witness for head code `c_s` can be adjacent to a wrong X-head h only if

`S(c_s) cap S(c(h)) != emptyset`.

In `E=1`, every wrong-head adjacency is therefore incident with the unique radius-two defect class and uses one of its two support coordinates.

### 3.1 `k>1`, `d_0=1`

The common core witness is adjacent to the defect head, so the repeated core radius-one support is one of the two defect coordinates. Star separation already forbids all k defect--core head edges. The core channel can therefore carry at most `k+1` selected-witness incidences without additional `Delta` cost: one from the common core witness to the defect and at most k from the defect witness to the k core heads. The second defect coordinate can contribute at most one singleton radius-one class, and one missing head edge can support at most the two directed incidences on that class.

Hence

> **`J<=k+1+min(2Delta,2)`.**                             `(J1)`

### 3.2 `k>1`, `d_0=0`

There is no free core reverse incidence. There are two support layouts.

- If neither defect coordinate is the repeated core support, there are at most two singleton channels, hence `J<=min(2Delta,4)`.
- If one defect coordinate is the repeated core support, that channel is one-way: each defect-witness adjacency to one of the k core heads forces a distinct missing defect--core head edge. The other coordinate can be one singleton bidirected channel. For `Delta>=1` this gives at most `2+min(k,Delta-1)=min(k+2,Delta+1)` incidences.

Maximizing over the two layouts gives the exact safe envelope

> **`J<=F_k(Delta)`,**                                    `(J0)`

where

`F_k(0)=0`, `F_k(1)=2`, `F_k(2)=4`,

and, for `Delta>=3`,

`F_k(Delta)=min(k+2,Delta+1)`.

This corrects an over-strong intermediate simplification made and caught during this same run: `d_0=0` does **not** globally imply `J<=4`, because a defect coordinate may equal the repeated core support and the defect witness may then meet several core heads, one missing head edge per incidence.

### 3.3 `k=1`

Every code class is singleton. The predecessor allows `0<=d_0<=2`, and the density tradeoff and two-support cap combine as

> **`J<=min(2d_0+2Delta,4)`.**                            `(Jk1)`

These three formulas are the support-channel incidence theorem used below.

## 4. Unit II — two-way singleton-channel adjacency is locally compatible

The hoped-for immediate contradiction from using both directed witness adjacencies on one defect/radius-one singleton support pair does **not** follow from the two singleton certificates alone.

Let the defect support contain coordinate i and let a singleton radius-one class use support `{i}`. Write `h_D,h_i` for the heads, `z_D,z_i` for their selected outside witnesses, and `q_i^d` for the matched d-endpoint at coordinate i. If both wrong-head edges are present, the support-intersection proof can route both through this same coordinate:

- `z_D~h_i` with `q_i^d~z_D`, `q_i^d!~h_i`;
- `z_i~h_D` with `q_i^d~z_i`, `q_i^d!~h_D`.

The original buffer singleton certificates force `h_D h_i` to be absent if either directed adjacency is used. With that head nonedge present, the local relations

`N(h_i) cap N(q_i^d)={z_D}` and

`N(h_D) cap N(q_i^d)={z_i}`

are mutually compatible with the selected-witness own-head nonedges, `z_D z_i` absent, and `b q_i^d` absent. This is a **local hostile incidence gadget**, not a claim that the gadget extends to a D2C graph.

Consequently one missing singleton defect/radius-one head edge can genuinely support two directed selected-witness incidences at the level of the currently used singleton relations. Any further improvement must use additional global code, Hall, rooted-slot, or D2C structure.

This negative result is preserved because it blocks a false local strengthening.

## 5. Unit III — density elimination with the support-channel cap

The selected outside witnesses contribute

`sum epsilon_w >= p(g+1)+k+M-J`,

while the exact Hall identity gives

`L_X >= [D(A,M)+2Delta]_+`.

Therefore

> `S-S_P >= p(g+1)+k+M + Psi_{k,d_0}(D)`,               `(BILL)`

where `Psi` is the minimum over nonnegative integer `Delta` of the Hall payment minus the appropriate support-channel incidence envelope.

For two cases there is a closed form:

### `k>1`, `d_0=1`

> **`Psi_{k,1}(D)=max(D-(k+1),-(k+3))`.**                `(PSI1)`

### `k=1`

> **`Psi_{1,d_0}(D)=max(D-2d_0,-4)`.**                   `(PSIk1)`

### `k>1`, `d_0=0`

Use `(J0)` and define

> **`Psi_{k,0}(D)=min_{Delta>=0}{[D+2Delta]_+-F_k(Delta)}`.** `(PSI0)`

No unbounded search is required. Since `F_k` is affine between its breakpoints and constant after `Delta=k+1`, a minimum is attained among at most six candidate integers:

`Delta in {0,1,2,k+1, clamp(floor(-D/2),3,k+1), clamp(ceil(-D/2),3,k+1)}`.

With exact crossing capacity `S_P>=sigma_P`, every one-defect row must satisfy

> **`p(g+1)+k+M+Psi_{k,d_0}(D(A,M))<=C0-sigma_P`.**      `(E1-SUPPORT-PAIR)`

The predecessor affine `(E1-LIN)` is recovered in the unsaturated range. The new term records that the two defect-support channels eventually saturate: making X still sparser cannot buy witness adjacency indefinitely.

## 6. Unit IV — explicit M interval in the main endpoint cases

Fix `d_0` and write `D(A,M)=D_0-kM`, `K_0=p(g+1)+k`, `T=C0-sigma_P`.

For `k>1,d_0=1`, `(E1-SUPPORT-PAIR)` is exactly

`max(K_0+D_0-(k+1)-(k-1)M, K_0-(k+3)+M)<=T`.

Hence its M-set is the explicit interval

> **`ceil((K_0+D_0-(k+1)-T)/(k-1)) <= M <= T-K_0+k+3`,** `(M1)`

clipped to `0<=M<=N`.

For `k=1`, the first affine term is M-independent and the second gives an upper endpoint:

`K_0+D_0-2d_0<=T`,

`0<=M<=min(N,T-K_0+4)`.

For `k>1,d_0=0`, retain the exact finite formula `(PSI0)` rather than replacing its repeated-core geometry by a coarser scalar interval. Once the repeated-core channel saturates, however, additional M again raises the outside bill instead of providing an unlimited monotone escape.

## 7. Unit V — exact rooted `q/E_U` intersection

The rooted residual theorem remains

`G(M)=E_*+M+ceil([R_0-(k+1)M]_+/2)`

with free optimizer

`M_Q=ceil([R_0]_+/(k+1))`.

For the explicit interval cases (`d_0=1` when `k>1`, and all `k=1` cases), the exact best rooted lower bound compatible with the sharpened E1 pair geometry is again obtained by projection:

> `M_hat=clamp(M_Q,M_-,M_+)`,
>
> **`q+E_U>=G(M_hat)`.**                                 `(E1-QE-CLAMP)`

For `k>1,d_0=0`, retain the exact support gate pointwise. Every row also has the physical upper bound

`q+E_U <= binom(u,2)-binom(k+1,2)-k-M + C0-Y_0-[D(A,M)]_+`.

The companion bounded checker records **zero** pointwise rooted lower/upper failures after the corrected support-channel pair gate. This is useful negative information: on the tested box, another relaxation of the same `q/E_U` sum is not the bottleneck.

## 8. Unit VI — exact `t=1` width / imbalance cap

Specialize to `t=1`, so `g=p-1`, and put `tau_P=sigma_P-P_0>=0`.

Every support pattern above satisfies the common consequence

`S-S_P>=p^2+M-3`.

Using `P_0=k(p+k)+1+y(p+2)`, `y=p+u-lambda-k`, and the parity bit `epsilon_lambda` (`0` for even lambda, `1` for odd), exact simplification gives

> **`(a+2)^2 <= u^2+2pu+2u+6p-2k^2+4k-3`**
> **`             -epsilon_lambda-2(M+tau_P)`.**          `(WIDTH)`

Equivalently,

`lambda >= 2p+u+1-floor(sqrt(RHS))`

whenever the radicand is nonnegative.

Thus every `t=1,E=1` survivor lies in an explicit imbalance / narrow-A regime even before the finer D-dependent support gate is used. Exact pair capacity only strengthens this via `tau_P`.

## 9. Unit VII — equality geometry feeds back into the rooted Hamming ledger

The support-channel caps identify a concrete equality pattern where the previous generic `E1-SLOT` bound can be sharpened.

### `k>1,d_0=1`, support saturation

If `J=k+3`, then all `k+1` core-channel incidences and both singleton-channel directions are present. Therefore:

- `z_*` is adjacent to the defect head (already encoded by `d_0=1`);
- the defect witness is adjacent to all k core heads;
- all k defect--core head edges are absent by star separation;
- the second defect coordinate is occupied by one singleton radius-one class and both directed selected-witness adjacencies on that channel are present;
- the corresponding defect--singleton head edge is absent.

These `k+1` missing head edges are precisely **all** possible zero-Hamming-excess internal edges in the E=1 code geometry. Hence every actual edge of `G[X]` has positive Hamming excess.

If `q_X` radius-one X-vertices have positive internal Hamming surcharge, every internal X-edge lies in the set consisting of the defect plus those `q_X` vertices, so `e(X)<=binom(q_X+1,2)`. With `eta(j)` the least q satisfying `binom(q+1,2)>=j`, the local slot theorem strengthens to

> **`r>=a+y+1+eta(e(X))`.**                              `(SAT-SLOT)`

The same conclusion holds in the `k>1,d_0=0,Delta=2,J=4` equality pattern: saturation then requires two singleton bidirected channels (the repeated-core layout can supply at most three incidences at `Delta=2`), so both zero-excess defect--singleton edges are absent and every surviving X-edge again has positive Hamming excess.

This is the first direct feedback from support-channel equality to the rooted local-Hamming ledger, rather than pricing the forced head nonedges only through `Delta`.

## 10. Unit VIII — bounded diagnostic

The companion checker starts from the predecessor's exact bounded box and changes only the E=1 pair theorem to `(E1-SUPPORT-PAIR)`.

The corrected support-envelope replay gives:

- old E=1-feasible abstract states: `53,435`;
- new E=1-feasible abstract states: `48,677`;
- **4,758 abstract states lose their E=1 route**;
- old E=1-feasible rows: `1,212,749`;
- new E=1-feasible rows: `1,094,326`.

In the difficult `t=1` slice:

- old E=1-feasible states: `5,164`;
- new E=1-feasible states: `4,471`;
- **693 t=1 states lose their E=1 route**;
- rows fall from `128,750` to `111,204`.

The full union count remains `64,457`, and the t=1 union remains `5,404`, because every newly E=1-closed abstract state on this finite box still has either an `E>=2` noncheap route or the separately retained cheap-sphere route. These are arithmetic parameter states, not realizable D2C graphs.

The pointwise rooted `q/E_U` lower/upper intersection records zero failures on all `1,094,326` new E=1 rows. Again, this is bounded diagnostic evidence only.

## 11. Consequence and next move

The proposed immediate two-way-witness contradiction is false at the current local-singleton level, but the failed attack exposed the correct replacement theorem: only two defect-support coordinates exist, and the repeated-core channel has a different one-way price from a singleton bidirected channel. This stops the predecessor's apparent unlimited `2Delta` witness saving.

The next coherent move remains inside `m=g+1`, `t=1`:

1. exploit `(SAT-SLOT)` in the pair-budget equality / near-equality rows, especially the `d_0=1` `k+3` pattern;
2. classify the `d_0=0` transition from two singleton bidirected channels to the one-way repeated-core channel;
3. use `(WIDTH)` and the exact `d_0=1` M interval to separate large-imbalance from small-width regimes;
4. only after these E1 equality geometries are exhausted, split the t=1 states with no E1 route into exact E=2 support types.

`X_3` remains outside the hypotheses (`u=0`, no active rigid complete cut) and is untouched.