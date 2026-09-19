# Exact E=2 support-channel geometry in the minimal reservoir

Date: 2026-09-19

Status: internal conditional theorem package for the eventual / sufficiently-large dense diameter-2-critical programme around

`M(n)=floor((n-1)^2/4)+1`.

This package stays inside the rigid one-code complete-cut, positive-buffer unloaded common-buffer, minimal outside-reservoir branch `m=g+1`. It is not graph-realizability evidence and does not assert the false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3. The published order-12 graph `X_3` remains the mandatory negative control.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, the root `README.md`, the latest commits through `b5be3a06e7d197cdf9931883a714ca9d4e25c599`, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, and `RIGID_GRAPH_LEVEL_REGRESSION.md`.

The audit boundary is unchanged:

- distinct physical beta-source identity is proved from raw singleton criticality;
- `(source,coordinate)` uniqueness is selected-representative uniqueness, not raw-witness uniqueness;
- the finite source-tuple capacity theorem is not promoted to unconditional graph-level closure;
- the actual-D2C regression retains `X_3`, records zero graph/formula mismatches, but has no positive fixture realizing the full rigid complete-cut hypotheses;
- exact pair-local `S_P/Ccap_P` remains mandatory; the previously proved stronger physical bills continue to dominate `(ONE-P)` and `(CROWD)` only in the sublayers where that domination was already established;
- the four-exception gate remains subordinate.

There is no departure from the audit's proposed priorities. The predecessor explicitly identified exact `E=2`, first for `k>=3`, as the next live frontier.

## 2. Retained notation

Use the established minimal-reservoir notation:

- `X--Y` complete, `x>=3`, `y>0`, `a=x+y`;
- every Y-code is `d`;
- `X=H_M dotcup H_0`, with `|H_M|=g`, `|H_0|=k=x-g>0`;
- `H_0` is one repeated radius-one code class of size `k`; the `H_M` classes are singleton;
- there are `g+1` selected outside witnesses: one common witness `z_*` for `H_0` and one for each singleton `H_M` class;
- `A=g-d_{H_M}(z_*)`, and put `d_0=g-A`;
- `M=(u_o-1)-d_{U_o\{z_*}}(z_*)`, `N=u-k-2`;
- `D=D(A,M)=Q_H-(2k-1)A-kM`;
- `E_max(A)=binom(g,2)+kA`, `Delta=E_max(A)-e(X)`;
- `sigma_P` is the least pair-local score meeting the exact `Ccap_P>=2xy` requirement.

For `k>=3`, total Hamming excess `E=2` has exactly two block types:

1. `R3`: one singleton `H_M` head has radius three from `d`; every other X-code has radius one;
2. `R2+R2`: two singleton `H_M` heads have radius two from `d`; every other X-code has radius one.

The repeated core cannot carry positive excess because one excess unit on its code would already contribute at least `k>=3` to total `E`.

For a code `c`, write `S(c)` for its support relative to `d`.

## 3. Unit I — unified E=2 support-channel ledger

The preserved support-intersection theorem says that a selected outside witness serving code `c_s` can be adjacent to a wrong X-head of code `c_h` only if

`S(c_s) cap S(c_h) != emptyset`.

In the two `E=2` types, every possible wrong-head incidence therefore lies on a finite list of support channels.

Define:

- `s`: total defect-support incidences, so `s=3` for `R3` and `s=4` for `R2+R2`;
- `q`: number of defect-defect intersecting pairs, so `q=0` for `R3`, while for `R2+R2`, `q=h=|S_1 cap S_2| in {0,1}`;
- `c`: number of defect supports containing the repeated-core coordinate;
- `d_0`: number of those defects actually adjacent to the common core witness `z_*`; hence `0<=d_0<=c`;
- `B=s-c+q`;
- `K=k(c-d_0)`.

Interpretation:

- each active core channel (`z_*` adjacent to that defect) contributes at most `k+1` wrong-head incidences: one core-witness-to-defect incidence plus at most `k` reverse defect-witness-to-core incidences. Star separation has already removed the corresponding `k` defect-core head edges, and the loss is already present in `E_max(A)` through `A=g-d_0`;
- each non-core defect-support incidence is a singleton bidirected channel and gives at most two wrong-head incidences for one missing X-head edge;
- each intersecting defect pair gives one further singleton-type bidirected channel and likewise gives at most two incidences for one missing defect-defect head edge;
- each core support whose defect is *not* adjacent to `z_*` is a one-way repeated-core channel: every reverse incidence consumes a distinct missing defect-core head edge, at most `k` per inactive core channel.

The relevant missing head edges are distinct across these channel types. Therefore, if `J` is the total wrong-head incidence count over the `g+1` selected outside witnesses,

> **E2 CHANNEL LEDGER**
>
> `J <= d_0(k+1) + 2 min(Delta,B) + min(K,[Delta-B]_+)`.      `(E2-J)`

This is a safe graph upper bound. It is the sharp resource envelope if all support-eligible singleton classes are present.

For `R3`, `c in {0,1}` and `d_0<=c`.

For `R2+R2`:

- if `h=0`, the defect supports are disjoint and `c in {0,1}`;
- if `h=1`, the supports meet in one coordinate and `c in {0,1,2}`;
- `c=2` occurs exactly when the shared coordinate is the repeated-core coordinate.

Coincident radius-two supports are impossible because the two defects are distinct A-code classes.

## 4. Unit II — closed pair correction for every support topology

The selected outside witnesses contribute

`sum epsilon_w >= p(g+1)+k+M-J`,

while exact Hall accounting gives

`L_X >= [D+2Delta]_+`.

For fixed `(B,K,d_0)`, define

`Phi_{B,K}(D)=min_{Delta>=0} {[D+2Delta]_+ - 2min(Delta,B) - min(K,[Delta-B]_+)}`.

The minimization closes exactly:

### If `K=0`

> `Phi_{B,0}(D)=max(D,-2B)`.                              `(PHI0)`

### If `K>0`

> `Phi_{B,K}(D)=max(D,-2B)` for `D>=-2B-1`,              `(PHI-A)`
>
> `Phi_{B,K}(D)=max(ceil(D/2)-B,-(2B+K))` for `D<=-2B-2`. `(PHI-B)`

Hence every fixed E=2 support topology satisfies the exact pair-local gate

> `p(g+1)+k+M - d_0(k+1) + Phi_{B,K}(D) <= C0-sigma_P`.  `(E2-PAIR)`

This retains the actual support topology instead of prematurely collapsing it to total score slack.

The proof is the same finite V-shape mechanism exposed in the repaired E=1 analysis. Up to `Delta=B`, each missing edge can buy two incidences and exactly cancels the Hall slope two. For the next `K` units, each missing edge buys only one incidence, producing the integer V-minimum `ceil(D/2)-B`. Beyond `B+K`, the channel saving is saturated.

The companion checker brute-replays `(PHI0/A/B)` against direct integer minimization over a broad box.

## 5. Unit III — R3 has automatic positive-Hamming X-density

In `R3`, every X-code has support size one or three relative to `d`. Distinct X-code classes therefore have even Hamming distance. Because distinct classes have different codes, that distance is at least two. The repeated core `H_0` is already independent.

Therefore:

> **R3 PARITY LEMMA. Every actual edge of `G[X]` has positive Hamming excess `rho=d_H-1>=1`.**

This does not require support-channel saturation.

Let `eta(j)` be the least nonnegative integer `q` with `binom(q+1,2)>=j`. The local rooted slot theorem then gives

> **`r >= a+y+1+eta(e(X))`.**                            `(R3-SLOT)`

Reason: the radius-three defect contributes the mandatory positive local slot term; if `q` additional X-vertices meet positive-Hamming internal edges, all internal X-edges lie on at most `q+1` relevant vertices, so `e(X)<=binom(q+1,2)`.

Thus `R3` is intrinsically more expensive in the rooted residual ledger than the coarse distribution-sensitive `E=2` relaxation records.

## 6. Unit IV — exact R3 pair geometries

For `R3`, the unified ledger gives three topologies.

### `c=0,d_0=0`

`B=3,K=0`, so

`Phi=max(D,-6)`.

### `c=1,d_0=0`

`B=2,K=k`, so

`Phi=max(D,-4)` for `D>=-5`,

and

`Phi=max(ceil(D/2)-2,-(k+4))` for `D<=-6`.

### `c=1,d_0=1`

`B=2,K=0`, and the active repeated-core channel contributes `k+1`, hence

> `Psi_R3=max(D-(k+1),-(k+5))`.                          `(R3-ACTIVE)`

On its right arm `D<=-4`, exact pair equality forces both remaining singleton channels active and Hall payment zero. At `t=1`, where `g=p-1`, the right-arm pair bill is simply

> **`p^2+M-5 <= C0-sigma_P`.**                           `(R3-T1-RIGHT)`

If `s_P` is slack above this pair minimum, then

`Delta <= floor((s_P-D)/2)`

on the right arm. Combining this with `(R3-SLOT)` and `e(X)=E_max(A)-Delta` gives

> `r >= a+y+1+eta([E_max(A)-floor((s_P-D)/2)]_+)`.       `(R3-PINCH-SLOT)`

In particular, pair equality gives the same formula with `s_P=0`.

## 7. Unit V — R2+R2 zero-Hamming edges are completely classified

Let the two radius-two defects have supports `S_1,S_2`.

- two distinct radius-one classes have Hamming distance two;
- the two radius-two defects have Hamming distance two if `h=1` and four if `h=0`;
- a radius-two defect and a radius-one class have Hamming distance one **iff** the radius-one support is one of that defect's two support coordinates; otherwise the distance is three;
- `H_0` is independent.

Therefore:

> **R2+R2 ZERO-EDGE CLASSIFICATION.** The only possible zero-Hamming-excess X-edges are defect-to-radius-one head edges lying on a defect support coordinate.

Every defect-defect edge and every radius-one/radius-one edge has positive Hamming excess.

Let `j_+` be the number of positive-Hamming X-edges and let `eta_2(j)` be the least `q>=0` with

`binom(q+2,2)>=j`.

Because both radius-two defects already carry one unit of Hamming excess, the local rooted theorem gives

> **`r >= a+y+2+eta_2(j_+)`.**                           `(R22-SLOT)`

This is a strict one-unit improvement over the generic concentrated-`E=2` baseline whenever the `R2+R2` type is known.

## 8. Unit VI — deep support saturation removes every zero-Hamming edge

The maximum channel saving for fixed `(B,K,d_0)` is

`J_max=d_0(k+1)+2B+K`.

Equivalently, using `B=s-c+q` and `K=k(c-d_0)`,

> **`J_max = 2s+2q+c(k-2)+d_0`.**                        `(JMAX)`

The fully saturated constant arm of `(E2-PAIR)` occurs when

`D<=-2(B+K)`.

At exact pair minimum on that arm, all channel resources must be saturated:

- every bidirected singleton-type channel uses its missing head edge;
- every inactive repeated-core channel uses all its defect-core missing head edges;
- every active repeated-core channel already has all its defect-core head edges absent by star separation;
- the Hall term is zero.

For `R2+R2`, the zero-Hamming classification in Section 7 says those are **all** possible zero-Hamming head edges. Hence:

> **DEEP-SATURATION SLOT THEOREM.** At exact pair minimum on the fully saturated arm of any fixed `R2+R2` topology, every actual X-edge has positive Hamming excess, so
>
> `r >= a+y+2+eta_2(e(X))`.

Moreover exact saturation has `Delta<=floor(-D/2)`, hence

> `r >= a+y+2+eta_2([E_max(A)-floor(-D/2)]_+)`.          `(R22-DEEP-SLOT)`

This directly converts the pair-local equality escape into a rooted-residual charge.

## 9. Unit VII — the cheapest deep R2+R2 escape is uniquely shared-core / double-active

For `R2+R2`, `s=4`, so

`J_max=8+2h+c(k-2)+d_0`.

For `k>=3` this is maximized by

`h=1, c=2, d_0=2`:

- the two radius-two defects share exactly the repeated-core coordinate;
- the common core witness is adjacent to both defect heads;
- both repeated-core channels are active;
- the remaining two defect coordinates are private singleton channels;
- the defect-defect overlap itself is the third bidirected channel.

Then

`B=3`, `K=0`, `J_max=2k+8`.

At `t=1`, the exact deep pair bill becomes

> **`p^2+M-k-8 <= C0-sigma_P`.**                         `(R22-CHEAP)`

This is the most permissive deep pair geometry among all `R2+R2` topologies, so it is the correct next load-bearing equality family to attack rather than another global scalar relaxation.

Its compensating rooted structure is unusually rigid:

- star separation deletes all `2k` defect-core zero-Hamming edges;
- exact support saturation deletes the two private defect-singleton zero-Hamming edges;
- the defect-defect channel also deletes the positive-Hamming defect-defect edge;
- every surviving X-edge is therefore positive-Hamming;
- `A=g-2`, so
  `E_max=binom(g,2)+k(g-2)`;
- exact deep pair equality has `Delta<=floor(-D/2)` and therefore obeys `(R22-DEEP-SLOT)`.

This identifies a concrete pair-cheap / rooted-expensive pinch geometry.

## 10. Arithmetic audit

`check_e2_support_channels.py` independently verifies:

1. the channel resource formula `(E2-J)` against direct finite allocation of bidirected and one-way channel costs;
2. the closed `Phi_{B,K}` formula against brute integer minimization;
3. the three R3 specializations;
4. the allowed `R2+R2` topology table and `J_max` simplification;
5. that `h=1,c=2,d_0=2` uniquely maximizes `J_max` for every `k>=3` among the allowed `R2+R2` topology classes.

This checker is an arithmetic/topology audit only. It does not enumerate D2C graphs and makes no realizability claim.

## 11. Consequence and next move

The `E=2,k>=3` frontier is no longer one undifferentiated relaxation.

- `R3` has automatic all-positive X-edge Hamming density, with a closed exact pair correction and a particularly simple `t=1` right-arm bill `p^2+M-5`.
- `R2+R2` has a complete zero-Hamming edge classification and an exact support topology ledger. Its most permissive deep pair escape is uniquely the shared-core / double-active geometry `(h,c,d_0)=(1,2,2)`, but exact pair saturation there simultaneously forces every surviving X-edge positive-Hamming.

The next run should stay on `m=g+1,t=1,k>=3` and attack this single shared-core / double-active `R2+R2` family first, intersecting `(R22-CHEAP)` and `(R22-DEEP-SLOT)` with the exact rooted identity `r=(p-lambda)(p+u)+q+E_U` and the already preserved physical `q/E_U` allocation. Only if that family survives should the non-deep `R2+R2` arms or the `R3` near-equality strip be expanded. Do not open `k=2`, `k=1`, `m=g+2`, loaded buffer, `z=2`, or the four-exception gate yet.
