# Alternative attacks v1 — quantifier correction and whole-state threshold programme

13 September 2026. **Research checkpoint. Candidate hand lemmas and exact finite reductions; external review, novelty assessment and independent reproduction remain OPEN. The unrestricted Murty–Simon conjecture is not proved.**

## Why this programme exists

The shared-residual-budget continuation rejects 4,487 of 4,584 stored selected patterns, but a fixed-pattern rejection does not exclude a scalar state because another selected geometry may exist. This programme attacks the missing quantifiers directly.

The main line quantifies alternative selected sets, source margins and selected excess. A separate maximum-cut line is retained as an independent architecture. The quantified line has now produced **five whole-state exclusions: N34 states 227, 279, 588, 526 and 382**.

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

The `l=2` member is already strong enough to close most or all of the high-excess tails in all five quantified examples.

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

State 279 exposed a reusable **zero-excess availability** mechanism: the global incoming ledger can force cheap-q sources to high p, making them unavailable to zero-excess labels and pushing those labels onto larger endpoint loads.

### 3. N34 state 588

[`STATE_588_WHOLE_STATE.md`](STATE_588_WHOLE_STATE.md) / [`STATE_588_REPLAY.md`](STATE_588_REPLAY.md).

```text
s=3^15,
rho=1^5,2,3^12,
r=43, S=45.
```

The exact low-excess scan has one coarse equality, excluded by `sum C_i>=106>97`. A cheap `h_2` screen leaves only `E=16` and `E=24`; exact replay closes both. Frontier: `996/4,582 -> 997/4,581`.

State 588 shows the mechanism is not tied to demand-two correction terms and motivates cheap tail triage before exact enumeration.

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

Equality forces every q=1 source to high p, so all fourteen zero-excess demand-three labels must use q=5/6, p=2 sources and each has `C_i>=7`; they alone give `sum C_i>=98>93`. The relaxed `h_2` tail is strict for `E=17,...,34`; its sole zero at `E=16` is already exactly excluded. Frontier: `997/4,581 -> 998/4,580`.

### 5. N34 state 382

[`STATE_382_WHOLE_STATE.md`](STATE_382_WHOLE_STATE.md) / [`STATE_382_REPLAY.md`](STATE_382_REPLAY.md).

```text
s=2^2,3^13,
rho=1^6,2,3^11,
r=41, S=43.
```

Every exact low-excess profile through `E=17` is strictly excluded; no hand-rigidity exception is needed. The decisive refinement is to retain the universal contribution from zero-excess demand-two labels. If

```text
z_0=#{i:s_i=2,e_i=0},
```

then the baseline identity gives the stronger necessary inequality

```text
T + 2 z_0 - P_+ <= 3(84+E).                          (3)
```

Combining (3) with the relaxed `h_2` source caps makes every `E=17,...,34` tail layer strict. Without the `2z_0` term, the old relaxation misses `E=17,21,22`; with it their gaps are `3,3,2`. `E=16` is already exactly excluded. Frontier: `998/4,580 -> 999/4,579`.

## Current frozen frontier

The five quantified whole-state closures give

```text
999 exclusions / 4,579 survivors,
```

split as

```text
4,501 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are scalar states in a frozen generalisation experiment, not surviving graphs. The fixed-order N34/N35 candidate proofs were already closed and are unchanged.

## Default family-screening strategy

The programme should now use the following order:

1. apply the refined `h_2` tail screen, **retaining elementary negative baseline terms such as `2z_0`** rather than discarding them;
2. rank states by the number and severity of non-strict excess layers;
3. exact-enumerate only the exceptional layers and the low-excess boundary;
4. if an equality survives, extract its source-capacity equality conditions and seek an incidence-rigidity contradiction;
5. after quantified pruning, return to the stronger shared-residual/pair geometry.

The frozen survivor extraction utility [`extract_frozen_survivors.py`](extract_frozen_survivors.py) is transport/replay infrastructure only; it does not itself apply a theorem.

## Raw candidate capacity and independent route

The selection-free package also gives raw candidate-label subset capacities; these remain a secondary graph-level projection route without choosing representatives.

[`MAXCUT_ROUTE.md`](MAXCUT_ROUTE.md) records the independent identity

```text
e(G)=|X||Y|+I-M.
```

A direct one-edge/one-nonedge matching proof is false and remains preserved as a failed route; any viable maximum-cut proof must use aggregate charging or stability.

## Audit boundaries and current priority

[`AUDIT.md`](AUDIT.md) records invalidated shortcuts and proof-status boundaries. None of the five whole-state closures uses numerical solver infeasibility: the proof-critical computations are exact integer enumerations, with explicit hand arguments where a coarse envelope is non-strict.

External mathematical review of the canonical bridge, selected-excess/threshold lemmas and hand-rigidity arguments remains open; independent computational reproduction remains open.

**Current priority:** rerun the adjacent low-demand N34 family with the **refined h2 + zero-label correction** before spending effort on exact enumeration. Seek a symbolic theorem explaining the common state-227/state-279/state-588/state-526/state-382 mechanism.
