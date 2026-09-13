# Incidence-capacity closure of the adjacent N34 family

13 September 2026. **Research checkpoint. Exact integer necessary-condition replay plus candidate hand lemmas; external mathematical review and independent reproduction remain OPEN. The unrestricted Murty–Simon conjecture is not proved.**

This note records the closure of the three remaining active members of the narrow adjacent family,

```text
230, 282, 385,
```

following the earlier closure of state 519. Together, the four active companions identified by `REFINED_H2_FAMILY_SCAN.md` are now all excluded inside the frozen scalar generalisation experiment.

The final verifier is

```text
scan_incidence_capacity_family.cpp
```

and accepts

```text
scan_incidence_capacity_family STATE_ID E
```

for `STATE_ID` in `{230,282,385}` and `E=0,...,34`.

A local exhaustive replay of all 105 state/layer pairs gives a positive gap in every case. The minimum reported whole-layer gap is `+1` for each of the three states. The GitHub Actions workflow `scan-incidence-capacity-family.yml` independently recompiles the verifier and requires all 105 gaps to be positive.

## 1. New lemma chain

The closure is not obtained by simply extending the old `h_2` brute force. Four reusable refinements form a hierarchy.

### 1.1 Capacity-order endpoint lemma

[`CAPACITY_ORDER_ENDPOINT_LEMMA.md`](CAPACITY_ORDER_ENDPOINT_LEMMA.md) converts the requirement for `d` cheap eligible endpoints into the exact capacity loss needed to make the `d`-th endpoint load small inside an independent source-cap relaxation.

For demand two this gives a selection-free lower bound on the zero-excess endpoint statistic without enumerating source pairs.

### 1.2 Demand-compatible excess order

[`DEMAND_COMPATIBLE_EXCESS_ORDER.md`](DEMAND_COMPATIBLE_EXCESS_ORDER.md) sharpens the selected-excess cap source by source. If the excesses of labels compatible with residual degree `rho` are

```text
eta_1^(rho) >= eta_2^(rho) >= ...,
```

then an active source satisfies

```text
p_u <= rho_u-1 + eta_(q_u)^(rho_u).                  (1)
```

In this family a `rho=2` source can select only demand-two labels, while a `rho=3` source can select either demand class. Equation (1) therefore retains information discarded by global `h_l` counts.

### 1.3 Threshold incidence capacity

[`THRESHOLD_INCIDENCE_CAPACITY.md`](THRESHOLD_INCIDENCE_CAPACITY.md) keeps competition between sources for the finite selected-degree capacity of high-excess labels. For

```text
L_u=max(0,p_u-rho_u+1),
```

and every excess threshold `ell` and residual-degree cutoff `R`,

```text
sum_{u:q_u>0, rho_u<=R, L_u>=ell} q_u
 <= sum_{i:0<s_i<=R, e_i>=ell} x_i.                 (2)
```

The final verifier enforces the `R=2` and `R=3` forms by an exact integer dynamic programme when a profile survives the cheaper screens.

### 1.4 Forced-incidence source score

[`FORCED_INCIDENCE_SCORE.md`](FORCED_INCIDENCE_SCORE.md) handles equality profiles in which a class of low-score sources cannot place all of its selected incidences on the other compatible labels. A target label is then forced to receive a low-score selected incidence, which sharpens

```text
d_i <= rho_u+q_u-1
```

for that particular label and reduces its positive baseline correction.

## 2. State 230

The state is

```text
s=2^4,3^11,
rho=1^6,2^3,3^9,
r=39, S=41.
```

The demand-compatible order-statistic scan reduces all possible excess layers to just three non-strict layers:

```text
E=0,3,6.
```

Before the incidence-capacity test these contain respectively

```text
13, 4, 1
```

nonpositive exact excess profiles.

Every one fails the `ell=0, R=2` instance of (2): the three `rho=2` sources emit more selected incidences than the four demand-two labels possess in total selected degree. Thus no threshold DP or hand equality case remains.

The final verifier is positive for every

```text
E=0,...,34,
```

with whole-layer minimum gap at least `+1`.

Therefore state 230 is excluded.

## 3. State 282

The state is

```text
s=2^3,3^12,
rho=1^6,2^2,3^10,
r=40, S=42.
```

Here the demand-compatible excess-order source cap is already sufficient after the earlier capacity-order refinement. The formerly difficult low/mid-excess layers become strict one by one; the exact replay ultimately gives a positive gap for every `E=0,...,20`, while the previously certified tail was already strict from `E=21` upward.

The final verifier independently replays all `E=0,...,34` and reports a positive gap throughout, with minimum `+1`.

Therefore state 282 is excluded.

## 4. State 385

The state is

```text
s=2^2,3^13,
rho=1^5,2^3,3^10,
r=41, S=43.
```

The demand-compatible order-statistic scan leaves only

```text
E=6,7,8,9,11
```

non-strict.

### 4.1 Layers E=6 and E=8

The old profile relaxation leaves 11 nonpositive profiles at `E=6` and one at `E=8`, all with no zero-excess demand-two label. The exact threshold-incidence DP enforces (2) jointly with the incoming total and the pointwise source caps.

The minimum refined gaps become

```text
E=6 : +9
E=8 : +9
```

on the formerly nonpositive profile set.

### 4.2 Layer E=7

There are seven old nonpositive profiles. Threshold-incidence capacity removes all six with `z_0=0`. The sole survivor is

```text
q_(rho=2)=(1,1,1),
q_(rho=3)=(1,5,5,5,5,5,5,5,5,6),
e_(s=2)=(0,7),
e_(s=3)=0^13.
```

Its old gap is `-1`.

The three `rho=2` sources emit three selected incidences into the two demand-two labels. The zero-excess label has selected degree two, so it can absorb at most two of those incidences. The excess-seven label is therefore forced to receive a `rho=2,q=1` selected incidence, giving

```text
d_i<=2,
C_i<=9
```

instead of the relaxed `C_i<=14`. Its correction coefficient is six, so the correction drops by 30 and the strengthened gap is at least

```text
-1+30=29.
```

### 4.3 Layer E=9

The unique remaining profile is

```text
q_(rho=2)=(2,2,2),
q_(rho=3)=(2,2,5,5,5,5,5,5,6,6),
e_(s=2)=(3,6),
e_(s=3)=0^13.
```

Its old gap is zero. Each `rho=2` source has outgoing degree two and there are exactly two demand-two labels, so both labels are forced to receive `rho=2,q=2` incidences. Hence both satisfy `d_i<=3`.

Their combined demand-two correction falls from

```text
2*10 + 5*13 = 85
```

to at most

```text
2*6 + 5*9 = 57.
```

The strengthened gap is at least `+28`.

### 4.4 Layer E=11

The unique remaining profile is

```text
q_(rho=2)=(2,2,2),
q_(rho=3)=(3,3,3,3,6,6,6,6,6,6),
e_(s=2)=(4,4),
e_(s=3)=0^12,3.
```

Again both demand-two labels are forced onto `rho=2,q=2` sources, so each has

```text
d_i<=3,
C_i<=7.
```

Their combined correction falls from 72 to at most 42. Keeping the demand-three excess-three correction at its old upper bound 33 reduces the total correction from 105 to at most 75. The old gap zero therefore becomes at least `+30`.

The final verifier is consequently positive for every `E=0,...,34`, with whole-layer minimum at least `+1`.

Therefore state 385 is excluded.

## 5. Exhaustive replay result

The final local replay executes

```text
3 states * 35 excess layers = 105 state/layer checks.
```

No nonpositive final layer remains:

```text
state 230 : min gap = +1
state 282 : min gap = +1
state 385 : min gap = +1
```

The high-excess layers are included in the same final replay rather than being trusted only through the older tail report.

## 6. Frontier update

Before these closures the frozen quantified frontier was

```text
1,000 exclusions / 4,578 survivors
```

with

```text
4,500 N34 survivors,
78 N35 survivors.
```

Closing states 230, 282 and 385 gives

```text
1,003 exclusions / 4,575 survivors,
```

split as

```text
4,497 N34 survivors,
78 N35 survivors.
```

The narrow adjacent family that originally left active companions

```text
230,282,385,519
```

is therefore fully closed.

These are scalar states in the frozen generalisation experiment, not individual surviving graphs. The fixed-order N34/N35 candidate proofs are unchanged.

## 7. What was learned

The main mathematical gain is more important than the three-state count. The progression is now

```text
high-excess threshold scarcity
 -> exact-demand endpoint availability
 -> demand-compatible excess order
 -> threshold selected-incidence capacity
 -> forced low-score incidence rigidity.
```

This is increasingly close to a genuine Hall/flow architecture for the selected source-label incidence graph. The next natural general step is to express the last two stages as a compact matching theorem rather than continue accumulating state-specific equality arguments.

## Trust boundary

The result depends on the canonical selected/residual bridge and the candidate lemmas linked above. Proof-critical computation uses exact integer enumeration and dynamic programming; no floating-point optimizer or numerical infeasibility certificate is used.

External mathematical review of the bridge and lemmas remains open. Independent reproduction of the final 105-layer replay remains open until a separate environment reruns the committed workflow/artifact.
