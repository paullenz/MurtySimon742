# One-defect support-cap / residual pinch

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

Assume `E=1` in the Hamming-defect notation. There is one radius-two defect head and all remaining X-code classes have radius one.

Put

`d_0:=g-A`.

For `k>1`, the predecessor proved `d_0 in {0,1}`; for `k=1`, `0<=d_0<=2`.

Let J be the total number of A-neighbour incidences over the `g+1` selected outside witnesses. Selected outside witnesses are nonadjacent to the head(s) they serve, so J counts only wrong-head incidences.

## 3. Unit I — exact support-channel cap on selected-witness incidences

The predecessor support-intersection theorem says that a selected outside witness for head code `c_s` can be adjacent to a wrong X-head h only if

`S(c_s) cap S(c(h)) != emptyset`.

In `E=1`, every wrong-head adjacency is therefore incident with the unique radius-two defect class. Its support has exactly two coordinates.

If `k>1`, the defect lies in `H_M`. Each of its two support coordinates can contain at most one radius-one code class. If one is the repeated core class, the defect witness can meet at most k core heads and the core witness can meet the defect once; the other support coordinate can contribute at most the two directed incidences of one singleton class. If the core support is not used, there are at most two singleton classes and hence at most four directed incidences.

Thus, writing

`c_0=(k+1)d_0`,

and

`J_0=4+(k-1)d_0` for `k>1`,

while for `k=1` put

`c_0=2d_0`, `J_0=4`,

we have the absolute support cap

> **`J<=J_0`.**                                           `(J-SUP)`

The predecessor density tradeoff independently gave

> `J<=c_0+2Delta`.

Combining the two gives the exact safe envelope

> **`J<=min(c_0+2Delta,J_0)`.**                           `(J-CAP)`

For `k>1` this is especially transparent:

- `d_0=0`: `J<=min(2Delta,4)`;
- `d_0=1`: `J<=k+1+min(2Delta,2)`.

So a one-defect state has only two support channels. Missing more and more X-edges cannot buy unbounded selected-witness adjacency.

## 4. Unit II — two-way adjacency is locally compatible; the factor two is not removable from singleton criticality alone

The hoped-for immediate contradiction from using both directed witness adjacencies on one defect/radius-one support pair does **not** follow from the two singleton certificates alone.

Let the defect support contain coordinate i and let a radius-one class use support `{i}`. Write `h_D,h_i` for the heads, `z_D,z_i` for their selected outside witnesses, and `q_i^d` for the matched d-endpoint at coordinate i. The support-intersection proof forces both wrong-head critical edges, if present, through this same coordinate:

- `z_D~h_i` can use `q_i^d~z_D`, `q_i^d!~h_i`;
- `z_i~h_D` can use `q_i^d~z_i`, `q_i^d!~h_D`.

The two original buffer singleton certificates force `h_D h_i` to be absent if either directed adjacency is used. With that head nonedge present, the local relations

`N(h_i) cap N(q_i^d)={z_D}` and

`N(h_D) cap N(q_i^d)={z_i}`

are mutually compatible provided the cross adjacencies are chosen in the evident way (`h_i!~z_i`, `h_D!~z_D`, `z_D!~z_i`, and `b!~q_i^d`). This is a **local hostile incidence gadget**, not a claim that the gadget extends to a D2C graph.

Consequently one missing defect/radius-one head edge can genuinely support two directed selected-witness incidences at the level of the currently used singleton relations. The coefficient `2Delta` in `(J-CAP)` cannot be improved merely by asserting that the two directions are incompatible. Any further improvement must use additional global code, Hall, rooted-slot, or D2C structure.

This negative result is preserved because it prevents a false strengthening of the current proof line.

## 5. Unit III — exact support-capped pair bill after eliminating X-density

The selected outside witnesses contribute

`sum epsilon_w >= p(g+1)+k+M-J`,

while the exact Hall identity gives

`L_X >= [D(A,M)+2Delta]_+`.

Therefore

`S-S_P >= p(g+1)+k+M + [D+2Delta]_+ - J`.

Use `(J-CAP)`. Because `J_0-c_0` is an even nonnegative integer in every allowed one-defect case, the following integer minimization is exact:

> `min_{Delta>=0} { [D+2Delta]_+ - min(c_0+2Delta,J_0) }`
>
> `=max(D-c_0,-J_0)`.                                    `(MIN)`

Hence every one-defect survivor satisfies the strengthened density-free bill

> **`S-S_P >= p(g+1)+k+M+max(D(A,M)-c_0,-J_0)`.**        `(E1-CAP-BILL)`

With exact crossing capacity `S_P>=sigma_P`, the new pair-local gate is

> **`p(g+1)+k+M+max(D(A,M)-c_0,-J_0)<=C0-sigma_P`.**     `(E1-CAP-PAIR)`

The predecessor `(E1-LIN)` is the first affine branch of this formula. The new second branch records that the two defect-support channels eventually saturate: making X still sparser cannot keep buying witness adjacency.

## 6. Unit IV — the one-defect pair-admissible M-set is an explicit interval

Fix `d_0` and hence `A=g-d_0`. Write

`D(A,M)=D_0-kM`,

`K_0=p(g+1)+k`,

`T=C0-sigma_P`.

Then `(E1-CAP-PAIR)` is exactly

> `max( K_0+D_0-c_0-(k-1)M,  K_0-J_0+M ) <= T`.          `(V)`

Thus the external pair bill is V-shaped in M: the old affine branch decreases with M when `k>1`, but after support-channel saturation the bill increases one-for-one with M.

For `k>1`, the pair-admissible set is therefore the explicit integer interval

> **`M in [M_-,M_+] cap [0,N]`,**                        `(M-INT)`

where

`M_- = ceil((K_0+D_0-c_0-T)/(k-1))`

and

`M_+ = T-K_0+J_0`.

The lower endpoint is clipped at zero and the upper endpoint at N. If the clipped lower endpoint exceeds the clipped upper endpoint, the E=1 row is closed.

For `k=1`, the decreasing branch is constant: one first requires

`K_0+D_0-c_0<=T`,

and then

`0<=M<=min(N,T-K_0+J_0)`.

This is stronger structurally than the predecessor monotone E1 gate: the support cap supplies a genuine **upper** bound on the outside-U defect M.

## 7. Unit V — exact intersection with the rooted residual optimizer

The rooted residual theorem remains

`G(M)=E_*+M+ceil([R_0-(k+1)M]_+/2)`,

with free minimizer

`M_Q=ceil([R_0]_+/(k+1))`.

Because the new E1 pair-admissible M-set is an interval, the exact best rooted lower bound compatible with the sharpened one-defect pair geometry is again obtained by projection:

> **`M_hat=clamp(M_Q,M_-,M_+)`,**
>
> **`q+E_U>=G(M_hat)`.**                                 `(E1-QE-CLAMP)`

For any concrete row there is also the independent physical upper bound

`q+E_U <= binom(u,2)-binom(k+1,2)-k-M + C0-Y_0-[D(A,M)]_+`.

So an actual row must contain an integer M in the explicit pair interval for which the rooted lower bound does not exceed this physical upper bound.

The companion checker applies this pointwise test on the bounded diagnostic box. It produces **no additional bounded-box E1 exclusions** after `(E1-CAP-PAIR)`. This is useful negative information: at the present abstraction level the rooted sum constraint is not the bottleneck on that box. Future progress should therefore come from more geometry, not another relaxation of the same q/E_U sum.

## 8. Unit VI — exact t=1 width / imbalance cap

Now specialize to the difficult layer `t=1`, so `g=p-1`. Let

`tau_P:=sigma_P-P_0>=0`

be the excess pair budget above the compulsory pair floor. Since `(E1-CAP-BILL)` is always at least `p^2+M-3`, every E=1 survivor obeys

`p^2+M-3+sigma_P<=C0`.

Using

`P_0=k(p+k)+1+y(p+2)`,

`y=p+u-lambda-k`,

and writing `epsilon_lambda` for the parity bit of lambda (`0` if lambda is even, `1` if odd), exact simplification gives

> **`(a+2)^2 <= u^2+2pu+2u+6p-2k^2+4k-3`**
> **`             -epsilon_lambda-2(M+tau_P)`.**          `(WIDTH)`

Equivalently,

> `lambda >= 2p+u+1-floor(sqrt(RHS))`,

whenever the right-hand side under the square root is nonnegative.

Thus an E=1 `t=1` survivor is forced into a quantitatively imbalanced / narrow-A regime even before using the finer D-dependent branch of `(E1-CAP-PAIR)`. The exact local pair threshold only strengthens this through `tau_P`.

## 9. Unit VII — independent bounded diagnostic

A companion checker starts from the predecessor's exact bounded box and changes only the E=1 pair gate from `(E1-LIN)` to `(E1-CAP-PAIR)`.

The result is deliberately reported at the branch level, not as a graph count:

- old E=1-feasible abstract states: `53,435`;
- new E=1-feasible abstract states: `48,674`;
- **4,761 abstract states lose their E=1 route**;
- old E=1-feasible rows: `1,212,749`;
- new E=1-feasible rows: `1,093,262`.

In the difficult `t=1` slice:

- old E=1-feasible states: `5,164`;
- new E=1-feasible states: `4,471`;
- **693 t=1 states lose their E=1 route**;
- rows fall from `128,750` to `111,046`.

The full union count remains `64,457`, and the t=1 union remains `5,404`, because every newly E=1-closed abstract state on this finite box still has either an `E>=2` noncheap route or the separately retained cheap-sphere route. These are arithmetic parameter states, not realizable D2C graphs.

The pointwise rooted `q/E_U` lower/upper intersection records zero failures on all `1,093,262` new E=1 rows. Again, this is bounded diagnostic evidence only.

## 10. Consequence and next move

The proposed immediate two-way-witness contradiction is false at the current local-singleton level, but that failure exposed the correct replacement theorem: only two defect-support channels exist, so the apparent `2Delta` witness saving saturates after O(k) incidences. This turns the E=1 pair gate from a monotone escape in M into an explicit V-shaped interval.

The next coherent move is still inside `m=g+1`, `t=1`:

1. classify equality / near-equality in `(J-CAP)` and `(E1-CAP-BILL)`, especially the `d_0=0` four-incidence pattern and the `d_0=1` `k+3` pattern;
2. exploit the forced head nonedges in those equality patterns inside the rooted local-slot/Hamming ledger, rather than only through `Delta`;
3. use `(WIDTH)` to separate large-imbalance from small-width regimes;
4. only after exhausting those equality patterns open the exact E=2 support types among the t=1 rows that no longer admit E=1.

`X_3` remains outside the hypotheses (`u=0`, no active rigid complete cut) and is untouched.