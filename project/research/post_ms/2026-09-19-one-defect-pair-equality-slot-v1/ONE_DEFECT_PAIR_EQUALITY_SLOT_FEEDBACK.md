# One-defect pair-equality / rooted-slot feedback

Date: 2026-09-19

Status: internal structural theorem package for the eventual / sufficiently-large dense diameter-2-critical programme around

`M(n)=floor((n-1)^2/4)+1`.

Nothing below asserts the false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3. The published order-12 D2C graph `X_3` with 32 edges remains the mandatory hostile control.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, the root `README.md`, the latest commits through `71e2b3ee8f912c7bb5b882c5d13201c5a51fb716`, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, and the independent actual-graph Hall/pair regression.

The binding audit boundary is unchanged:

- distinct physical beta-source identity is established directly from raw singleton criticality;
- global `(source,coordinate)` uniqueness is a selected-representative statement, not raw-witness uniqueness;
- the finite source-tuple capacity theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression reconstructs the rooted/Hall/pair interface with `X_3` retained and zero recorded graph/formula mismatches;
- no bounded-corpus D2C graph realizes the full rigid complete-cut hypotheses, so this package is a conditional hand implication, not graph-realizability evidence;
- exact pair-local `S_P/Ccap_P` remains live. `(ONE-P)` and `(CROWD)` are used only where their domination by stronger physical bills was already proved;
- the four-exception gate remains subordinate.

There is no departure from the audit's proposed priority order. The predecessor explicitly asked to exhaust pair-budget equality / near-equality in the `E=1` minimal-reservoir geometry before opening `E=2`, and that is the line pursued here.

## 2. Retained one-defect geometry

Stay in the positive-buffer unloaded common-buffer rigid one-code branch at minimal outside reservoir `m=g+1` and Hamming excess `E=1`.

Use the established notation:

- `X--Y` complete, `x>=3`, `y>0`, `a=x+y`;
- every Y-vertex has code `d`;
- `X=H_M dotcup H_0`, with `|H_M|=g`, `|H_0|=k=x-g>0`;
- `H_0` has one common radius-one code; the `H_M` code classes are singleton;
- there is one unique radius-two defect head; every other X-code has radius one from `d`;
- `A=g-d_{H_M}(z_*)`, `d_0=g-A`, `M=(u_o-1)-d_{U_o\{z_*}}(z_*)`;
- for `k>1`, `d_0 in {0,1}`;
- `D=D(A,M)=Q_H-(2k-1)A-kM`;
- `E_max(A)=binom(g,2)+kA`;
- `Delta=E_max(A)-e(X)`;
- `sigma_P` is the least pair-local score meeting exact `Ccap_P>=2xy`.

The corrected support envelopes from the predecessor remain:

- `k>1,d_0=1`: `J<=k+1+min(2Delta,2)`;
- `k>1,d_0=0`: `J<=F_k(Delta)`, where
  `F_k(0)=0,F_k(1)=2,F_k(2)=4`,
  and `F_k(Delta)=min(k+2,Delta+1)` for `Delta>=3`;
- `k=1`: `J<=min(2d_0+2Delta,4)`.

The local two-way singleton-channel hostile gadget remains valid. No factor-two improvement is assumed.

---

## 3. Unit I — `d_0=1` leaves at most one zero-Hamming-excess X-edge

This is stronger than the generic `E=1` zero-excess cap used by the preceding arithmetic relaxation.

Let the radius-two defect support be `{i,j}`. When `d_0=1`, the repeated `H_0` radius-one support is one of these coordinates. The fact `d_0=1` means the common core witness is adjacent to the defect head. The previously proved star-separation theorem therefore forbids **all k defect--core head edges**.

Among radius-one X-code classes, every other support is a distinct singleton. Hence the only other radius-one class whose code can be Hamming distance one from the radius-two defect is the possible singleton class on the second defect coordinate.

All other pairs of distinct radius-one codes have Hamming distance two, and `H_0` itself is independent.

Therefore:

> **ONE-ZERO-EDGE LEMMA.** In the `E=1,d_0=1` branch, `G[X]` has at most one internal edge of Hamming excess zero.

If `e=e(X)`, at least `[e-1]_+` internal edges have positive Hamming excess. The unique defect vertex already pays the universal `E=1` extra X-slot. If `eta(j)` is the least nonnegative integer q with

`binom(q+1,2)>=j`,

the local rooted Hamming theorem consequently strengthens to

> **`r>=a+y+1+eta([e(X)-1]_+)`.**                       `(D1-UNIV-SLOT)`

This applies to every `d_0=1` row, without pair-budget equality.

There is a sharper trigger. The core support channel supplies at most `k+1` wrong-head witness incidences. Thus if

`J>k+1`,

the second singleton support channel is active. Either direction on that channel forces its defect--singleton head edge absent by the preserved singleton criticality argument. The one remaining possible zero-excess X-edge is then gone, and

> **`r>=a+y+1+eta(e(X))`.**                              `(D1-ACTIVE-SLOT)`

This recovers the predecessor's saturated theorem but shows that full `J=k+3` is not needed: `J>=k+2` already suffices.

---

## 4. Unit II — exact right-arm pair pinch in `d_0=1`

For fixed `D`, the `d_0=1` pair correction before the constant outside bill is

`[D+2Delta]_+ - (k+1+min(2Delta,2))`.

Its exact minimum is

`Psi_{k,1}(D)=max(D-(k+1),-(k+3))`.

The minimizers have a useful physical classification.

### 4.1 Right arm: `D<=-2`

Here `Psi=-(k+3)`. For an actual geometry define its excess above the pair minimum by

`xi=[D+2Delta]_+ + (k+3-J)`.

Both summands are nonnegative integers. If the available pair slack over the minimum is `s`, then `xi<=s`.

Hence, for `s<=1`,

- `J>=k+2`, so the second singleton channel is active and **every actual X-edge has positive Hamming excess**;
- `[D+2Delta]_+<=s`, so
  `Delta<=floor((s-D)/2)`.

In particular:

- exact pair equality (`s=0`) gives
  `J=k+3` and `Delta<=floor(-D/2)`;
- one unit above equality (`s=1`) gives
  `J>=k+2` and `Delta<=floor((1-D)/2)`.

### 4.2 Boundary `D=-1`

Exact equality has `Delta=1` and `J=k+3`; again every actual X-edge has positive Hamming excess.

### 4.3 Left arm `D>=0`

At exact equality there are precisely the two density possibilities relevant here:

- `Delta=0`, with the core channel only;
- `Delta=1`, with the second singleton channel saturated.

Both imply the positive-edge lower bound in the next section.

### 4.4 `t=1` endpoint becomes literal pair slack

When `t=1`, `g=p-1`, and the constant part is

`K_0=p(g+1)+k=p^2+k`.

On the right arm `D<=-2`, the exact pair-local bill is therefore simply

> **`p^2+M-3<=T`,**                                      `(D1-RIGHT)`
>
> where `T=C0-sigma_P`.

Thus the right endpoint is

> **`M_+=T-p^2+3`.**                                     `(D1-MPLUS)`

For any right-arm row the pair slack is exactly `M_+-M`. Consequently `M=M_+` is support-saturated, while `M=M_+-1` already forces the active-singleton conclusion above.

This is the requested direct conversion of the exact M interval into a graph-structural pinch regime.

---

## 5. Unit III — pair equality forces many positive-Hamming X-edges

For `d_0=1`,

`E_max=binom(g,2)+k(g-1)`.

At exact pair equality:

- if `D<=-2`, all zero-excess X-edges are absent and
  `Delta<=floor(-D/2)`;
- if `D=-1`, `Delta=1` and all zero-excess X-edges are absent;
- if `D>=0`, the only exact minimizers are `Delta=0` or `1`, and the universal one-zero-edge lemma applies.

Therefore the number `j_+` of actual internal X-edges with positive Hamming excess obeys

> **`j_+ >= [E_max-max(1,floor(-D/2))]_+`.**             `(D1-JPLUS)`

and hence

> **`r>=a+y+1+eta([E_max-max(1,floor(-D/2))]_+)`.**      `(D1-EQ-SLOT)`

On the right arm with one unit of pair slack,

> **`j_+ >= [E_max-floor((1-D)/2)]_+`,**                 `(D1-NEAR-JPLUS)`

so the same `eta` conversion gives the corresponding near-equality rooted-slot floor.

The important point is conceptual: pair-local score tightness now determines not merely an allowed `(A,M)` row but a lower bound on the number of **physically positive-Hamming edges** in `G[X]`, which is then charged through the rooted residual slots.

---

## 6. Unit IV — closed form for the `d_0=0` pair correction

The predecessor deliberately retained a six-candidate formula for

`Psi_{k,0}(D)=min_{Delta>=0}{[D+2Delta]_+-F_k(Delta)}`

because the repeated-core channel made the geometry piecewise.

For every `k>1` this minimization has the compact closed form

> **`Psi_{k,0}(D)=max(D,-4)` for `D>=-7`;**              `(PSI0-A)`
>
> **`Psi_{k,0}(D)=max(ceil(D/2)-1,-(k+2))` for `D<=-8`.** `(PSI0-B)`

### Proof

For `Delta=0,1,2`, `F_k(Delta)=2Delta`, so the minimum over these three values is exactly `max(D,-4)`.

For `3<=Delta<=k+1`, `F_k(Delta)=Delta+1`. Thus

`[D+2Delta]_+-(Delta+1)`

decreases while `D+2Delta<=0` and increases once it is positive. Its integer minimum is `ceil(D/2)-1`, unless the support envelope has already saturated.

For `Delta>=k+1`, `F_k(Delta)=k+2`, so this branch cannot go below `-(k+2)`.

Comparing the small-Delta value `-4` with the repeated-core V minimum shows that the latter becomes strictly better exactly from `D=-8` onward. This proves `(PSI0-A/B)`.

The companion checker brute-replays this identity for `k=2,...,29` and `D=-120,...,120` against both the direct Delta minimization and the predecessor finite-candidate formula.

This replaces a diagnostic minimization by a short reviewer-facing piecewise theorem.

---

## 7. Unit V — exact `d_0=0` equality geometry and rooted-slot feedback

The closed form exposes the support transition directly.

### 7.1 Small / transition regime

At exact pair equality:

- `D>=0`: `Delta in {0,1,2}`;
- `D=-1,-2`: `Delta in {1,2}`;
- `D=-3,-4,-5`: **uniquely `Delta=2,J=4`**;
- `D=-6,-7`: the two-singleton and repeated-core mechanisms tie.

For `D=-3,-4,-5`, the repeated-core layout can supply at most three incidences at `Delta=2`, whereas equality requires `J=4`. Therefore equality uses **two singleton bidirected channels**. Both zero-excess defect--singleton head edges are absent, every actual X-edge has positive Hamming excess, and

> **`j_+=E_max-2`,**
>
> where now `E_max=binom(g,2)+kg`.

### 7.2 Deep repeated-core regime

For `D<=-8` and `k>=3`, the value of `Psi` is below the two-singleton floor `-4`, so every exact minimizer uses the repeated-core support channel.

In that layout:

- the singleton bidirected channel is used first;
- every further core incidence is one-way and costs its own missing defect--core head edge.

If `Delta<=k+1`, the `Delta` missing edges can all be the possible zero-excess defect/support edges, leaving exactly `E_max-(k+1)` positive-Hamming edges.

If `Delta>=k+1`, all `k+1` possible zero-excess edges are already absent and every further deficit removes a positive-Hamming edge, leaving `E_max-Delta`.

Every exact minimizer satisfies

`Delta<=max(k+1,floor(-D/2))`.

Thus, uniformly over the entire exact-equality `d_0=0` branch,

> **`j_+ >= [E_max-max(k+1,floor(-D/2))]_+`.**          `(D0-JPLUS)`

and

> **`r>=a+y+1+eta([E_max-max(k+1,floor(-D/2))]_+)`.**   `(D0-EQ-SLOT)`

In the sharper `-5<=D<=-3` zone replace the bracketed term by `E_max-2`.

When the repeated-core envelope itself has saturated, `D<=-2k-2`, `Psi=-(k+2)`. In the `t=1` slice the pair bill then becomes

> **`p^2+M-2<=T`.**                                      `(D0-DEEP)`

So the deep repeated-core right endpoint is one unit tighter than the `d_0=1` right endpoint.

---

## 8. Unit VI — bounded replay: real E1 tightening, no union closure

The companion arithmetic checker starts from exactly the predecessor's support-capped E1 rows and changes only the rooted-slot floors proved above.

On the same bounded abstract box:

- support-capped E1 rows: `1,094,326`;
- sharpened E1 rows: `1,094,065`;
- **261 E1 rows are removed**;
- E1-feasible states: `48,677 -> 48,672`;
- **5 abstract states lose their E1 route**.

The 261 row removals split as:

- 199 from the universal `d_0=1` one-zero-edge lemma;
- 28 additional removals from exact `d_0=1` pair equality;
- 1 additional removal from the one-unit right-arm pinch;
- 33 from exact `d_0=0` equality.

The five E1-route state closures occur at:

- `t=4`: 2;
- `t=8`: 1;
- `t=9`: 1;
- `t=11`: 1.

In the difficult `t=1` slice:

- E1 rows fall `111,204 -> 111,197`;
- E1-feasible states remain `4,471`.

The full abstract union remains **64,457**, and the `t=1` union remains **5,404**, because every newly E1-closed state still has a retained `E>=2` or Hamming-cheapest sphere route.

These are abstract arithmetic parameter states, not realizable D2C graph counts. The absence of a `t=1` state closure is useful negative information: the equality feedback is structurally correct, but another scalar relaxation of the same E1 branch is unlikely to close the present t=1 bottleneck.

---

## 9. Unit VII — the `t=1` no-E1 frontier is exactly an E=2 frontier

The same replay isolates the `t=1` states that survive the current union but have **no** support-capped E1 route.

There are exactly

> **933**

such abstract states on the bounded box, and **all 933 already have an `E=2` route** under the retained distribution-sensitive `R_N` relaxation. None first requires `E>=3`.

Their k-distribution is:

| k | states |
|---:|---:|
| 1 | 223 |
| 2 | 201 |
| 3 | 146 |
| 4 | 104 |
| 5 | 82 |
| 6 | 60 |
| 7 | 53 |
| 8 | 47 |
| 9 | 17 |

This identifies the correct next mathematical frontier rather than merely suggesting it.

Moreover the `E=2` Hamming-excess block types are exactly:

### `k>=3`

The repeated core cannot carry positive excess, because one unit on the common core code would contribute at least k units. Therefore there are only two types:

1. **R3:** one singleton `H_M` head has excess 2 (radius three), all other X-code classes have radius one;
2. **R2+R2:** two singleton `H_M` heads each have excess 1 (two radius-two defects), all others have radius one.

### `k=2`

The two types above remain, plus:

3. **Core-R2:** the common `H_0` code has excess 1, contributing both units at once.

### `k=1`

All classes are singleton-sized at the multiplicity level, but the designated core channel remains structurally special. The exact possibilities are:

1. one matched R3 defect;
2. two matched R2 defects;
3. one core R2 plus one matched R2;
4. one core R3 defect.

This is an exact combinatorial classification of the next branch, not a realizability statement.

---

## 10. Consequence and next move

The E1 equality line has now yielded two compact structural outputs suitable for external review:

1. pair-budget saturation / near-saturation forces a large positive-Hamming subgraph in `G[X]`, which converts directly to unused rooted slots;
2. the previously awkward `d_0=0` pair minimization has an explicit closed form and a clear two-singleton-to-repeated-core phase transition.

The bounded replay says where to stop squeezing this same scalar layer: the difficult `t=1` union does not move, and every no-E1 survivor already has an E=2 escape.

The next session should therefore remain in `m=g+1,t=1` but open **exact E=2 support types**, in this order:

1. `k>=3`, R3: derive the three-support selected-witness envelope with the repeated-core channel separated from singleton bidirected channels, then minimize it against exact pair-local `Ccap_P`;
2. `k>=3`, R2+R2: classify overlap/disjointness of the two defect supports before any scalar relaxation;
3. `k=2`, add the Core-R2 type;
4. `k=1`, handle the four singleton/core placements separately.

Do not open `m=g+2`, loaded buffer, `z=2`, or the four-exception gate while this exact E=2 frontier remains live.

`X_3` remains outside these hypotheses (`u=0`, no active rigid complete cut) and is untouched.
