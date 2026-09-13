# Alternative attacks v1 — quantifier correction and whole-state threshold programme

13 September 2026. **Research checkpoint. Candidate hand lemmas and exact finite reductions; external review, novelty assessment and independent reproduction remain OPEN. The unrestricted Murty–Simon conjecture is not proved.**

## Why this programme exists

The shared-residual-budget continuation rejects 4,487 of 4,584 stored selected patterns, but a fixed-pattern rejection does not exclude a scalar state because another selected geometry may exist. This programme attacks the missing quantifiers directly.

The main line quantifies alternative selected sets, source margins and selected excess. A separate maximum-cut line is retained as an independent architecture. The quantified line has now produced **six whole-state exclusions: N34 states 227, 279, 588, 526, 382 and 519**.

## Core selected-excess mechanism

See [`SELECTION_FREE.md`](SELECTION_FREE.md). For every selected positive-demand incidence,

```text
p_u-rho_u+1 <= e_i := x_i-s_i.                       (1)
```

If

```text
h_l=#{i:e_i>=l},
```

then

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

The `l=2` member closes most high-excess tails in the six quantified examples.

Two later refinements are now central:

1. [`REFINED_BASELINE3_LEMMA.md`](REFINED_BASELINE3_LEMMA.md) keeps the exact selected-source score `rho_u+q_u-1` and the negative baseline contribution of zero-excess demand-two labels.
2. [`ZERO_EXCESS_ENDPOINT_ORDER.md`](ZERO_EXCESS_ENDPOINT_ORDER.md) keeps the **low-p source availability and endpoint-load order statistic** of an exact-demand label. For a zero-excess demand-two label this replaces the universal endpoint lower bound 2 by a state-dependent second-smallest eligible `q_u+p_u`.

## Whole-state exclusions

### 1. N34 state 227

[`STATE_227_WHOLE_STATE.md`](STATE_227_WHOLE_STATE.md) / [`STATE_227_REPLAY.md`](STATE_227_REPLAY.md).

```text
s=2^4,3^11,
rho=1^7,2,3^10,
r=39, S=41.
```

Exact integer enumeration covers every excess profile through `E=20`; two equality profiles are removed by hand rigidity. The relaxed `h_2` tail closes `E=21,...,34`; incoming capacity excludes `E>=35`. Frontier: `994/4,584 -> 995/4,583`.

### 2. N34 state 279

[`STATE_279_WHOLE_STATE.md`](STATE_279_WHOLE_STATE.md) / [`STATE_279_REPLAY.md`](STATE_279_REPLAY.md).

```text
s=2^3,3^12,
rho=1^7,3^11,
r=40, S=42.
```

Exact low-excess replay covers `E=0,...,15`, with three hand-rigidity cases. The `h_2` tail closes `E=16,...,34`; incoming capacity excludes `E>=35`. Frontier: `995/4,583 -> 996/4,582`.

State 279 exposed the first reusable **zero-excess availability** mechanism: the incoming ledger can consume cheap-p sources, forcing zero-excess labels onto larger endpoint loads.

### 3. N34 state 588

[`STATE_588_WHOLE_STATE.md`](STATE_588_WHOLE_STATE.md) / [`STATE_588_REPLAY.md`](STATE_588_REPLAY.md).

```text
s=3^15,
rho=1^5,2,3^12,
r=43, S=45.
```

The exact low-excess scan has one coarse equality, excluded by `sum C_i>=106>97`. A cheap `h_2` screen leaves only `E=16` and `E=24`; exact replay closes both. Frontier: `996/4,582 -> 997/4,581`.

State 588 shows the mechanism is not tied to demand-two corrections and motivates cheap tail triage before exact enumeration.

### 4. N34 state 526

[`STATE_526_WHOLE_STATE.md`](STATE_526_WHOLE_STATE.md) / [`STATE_526_REPLAY.md`](STATE_526_REPLAY.md).

```text
s=2,3^14,
rho=1^5,2^2,3^11,
r=42, S=44.
```

The exact scan through `E=16` has one coarse equality,

```text
E=7, e_2=7, e_3=0^14,
q_(rho=2)=1^2,
q_(rho=3)=1^2,5^7,6^2.
```

Equality forces every q=1 source to high p, so all fourteen zero-excess demand-three labels must use q=5/6, p=2 sources and each has `C_i>=7`; they alone give `sum C_i>=98>93`. The relaxed `h_2` tail is strict for `E=17,...,34`. Frontier: `997/4,581 -> 998/4,580`.

### 5. N34 state 382

[`STATE_382_WHOLE_STATE.md`](STATE_382_WHOLE_STATE.md) / [`STATE_382_REPLAY.md`](STATE_382_REPLAY.md).

```text
s=2^2,3^13,
rho=1^6,2,3^11,
r=41, S=43.
```

Every exact low-excess profile through `E=17` is strictly excluded; no hand-rigidity exception is needed. If

```text
z_0=#{i:s_i=2,e_i=0},
```

then retaining the negative baseline-three contribution gives

```text
T + 2 z_0 - P_+ <= 3(84+E).                          (3)
```

The refined tail is strict for every `E=17,...,34`; `E=16` is already exactly excluded. Frontier: `998/4,580 -> 999/4,579`.

### 6. N34 state 519

[`STATE_519_WHOLE_STATE.md`](STATE_519_WHOLE_STATE.md) / [`STATE_519_REPLAY.md`](STATE_519_REPLAY.md).

```text
s=2,3^14,
rho=1^6,3^12,
r=42, S=44.
```

The generic adjacent-family scan ranked 519 as the best active companion. The exact profile replay covers `E=0,...,24`; every relaxed profile is strict or source-infeasible except one coarse nonpositive profile at each of `E=6,8,9`.

Those three layers are closed by the new exact-demand endpoint-order mechanism. When the unique demand-two label has zero excess, its two selected sources are distinct `rho=3` sources satisfying

```text
p_u<=2,
```

and the label endpoint obeys

```text
C_2>=max(q_u+p_u,q_v+p_v).
```

The dedicated exact replay minimizes this endpoint load jointly with `sum q_u p_u`; the minimum gaps are

```text
E=6 : 2
E=8 : 4
E=9 : 2.
```

A refined `h_2` tail is strict for every `E=25,...,34`, with minimum gaps

```text
4,5,12,2,1,2,5,10,21,20,
```

and incoming capacity excludes `E>=35`. GitHub Actions run `34773463128` is green on all proof-critical stages. Frontier: `999/4,579 -> 1,000/4,578`.

## Current frozen frontier

The six quantified whole-state closures give

```text
1,000 exclusions / 4,578 survivors,
```

split as

```text
4,500 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are scalar states in a frozen generalisation experiment, not surviving graphs. The fixed-order N34/N35 candidate proofs were already closed and are unchanged.

## Adjacent low-demand family

[`REFINED_H2_FAMILY_SCAN.md`](REFINED_H2_FAMILY_SCAN.md) records the generic scan of the narrow N34 family with demands only 2/3 and residual degrees only 1/2/3. At scan time it contained the five already-closed states plus four active companions:

```text
230, 282, 385, 519.
```

State 519 ranked first and has now been closed. The remaining active companions in this narrow family are therefore

```text
230, 282, 385.
```

The generic refined tail is already strict from `E=21` upward for states 282 and 385, and from `E=23` upward for state 230. The next scan should add the exact-demand endpoint-order correction from `ZERO_EXCESS_ENDPOINT_ORDER.md` before committing to large low-excess enumerations.

## Default family-screening strategy

The programme should now use the following order:

1. apply the refined `h_2` tail screen, retaining negative baseline terms rather than discarding them;
2. whenever zero-excess exact-demand labels occur, optimize their **eligible-source endpoint order statistic jointly with the incoming ledger**;
3. rank states by the number and severity of remaining non-strict excess layers;
4. exact-enumerate only the exceptional layers and low-excess boundary;
5. if equality survives, extract source-capacity equality conditions and seek incidence rigidity;
6. after quantified pruning, return to the stronger shared-residual/pair geometry.

The frozen survivor extraction utility [`extract_frozen_survivors.py`](extract_frozen_survivors.py) is transport/replay infrastructure only; it does not itself apply a theorem.

## General lesson from the six closures

The examples now support a reusable two-sided architecture:

- **high-excess scarcity:** threshold counts `h_l` cap the incoming load of large-q sources;
- **low-excess availability:** exact-demand labels require enough low-p selected sources;
- **endpoint upper order statistics:** `d_i<=rho_u+q_u-1` bounds `C_i` from above through the selected sources;
- **endpoint lower order statistics:** zero-excess labels force `C_i` from below through the eligible low-p sources;
- **negative baseline terms:** demand-two zero-excess labels help the baseline-three contradiction and should not be thrown away;
- **triage before exact enumeration:** cheap scalar relaxations identify the few layers where detailed profile work is worth the cost.

States 588, 526, 382 and 519 now exhibit four complementary manifestations: demand-three endpoint rigidity, source-availability rigidity, universal negative-baseline correction, and exact-demand endpoint-order availability.

## Raw candidate capacity and independent route

The selection-free package also gives raw candidate-label subset capacities; these remain a secondary graph-level projection route without choosing representatives.

[`MAXCUT_ROUTE.md`](MAXCUT_ROUTE.md) records the independent identity

```text
e(G)=|X||Y|+I-M.
```

A direct one-edge/one-nonedge matching proof is false and remains preserved as a failed route; any viable maximum-cut proof must use aggregate charging or stability.

## Audit boundaries and current priority

[`AUDIT.md`](AUDIT.md) records invalidated shortcuts and proof-status boundaries. None of the six whole-state closures uses numerical solver infeasibility: proof-critical computations are exact integer enumerations, with explicit structural arguments where coarse envelopes are non-strict.

External mathematical review of the canonical bridge, selected-excess/threshold lemmas, refined baseline/order-statistic lemmas and rigidity arguments remains open; independent computational reproduction remains open.

**Current priority:** generalize the state-519 endpoint-order correction across the adjacent family, then attack states 282/385 before 230 unless the strengthened scan changes that ranking. In parallel, continue seeking a symbolic theorem that explains all six closures rather than accumulating isolated finite cases.
