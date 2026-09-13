# Alternative attacks v1 — quantifier correction and whole-state threshold programme

13 September 2026. **Research checkpoint. Candidate hand lemmas and exact finite reductions; external review, novelty assessment and independent reproduction remain OPEN. The unrestricted Murty–Simon conjecture is not proved.**

## Why this programme exists

The shared-residual-budget continuation rejects 4,487 of 4,584 stored selected patterns, but a fixed-pattern rejection does not exclude a scalar state because another selected geometry may exist. This programme therefore attacks the missing quantifiers directly.

The main line quantifies alternative selected sets, source margins and selected excess. A separate maximum-cut line is retained as an independent proof architecture. The quantified line has now produced **three whole-state exclusions: N34 states 227, 279 and 588**.

## Core selected-excess mechanism

See [`SELECTION_FREE.md`](SELECTION_FREE.md). For every selected positive-demand incidence,

```text
p_u-rho_u+1 <= e_i := x_i-s_i.                       (1)
```

In exact demand `x=s`, every active source therefore has `p_u<=rho_u-1`. More generally, put

```text
h_l=#{i:e_i>=l}.
```

If `p_u-rho_u+1>=l`, every one of the source's `q_u` selected labels has excess at least `l`; hence

```text
q_u<=h_l,
```

or equivalently

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

The `l=2` member is already strong enough to close most or all of the high-excess tails in all three quantified examples.

## Whole-state exclusion 1: N34 state 227

Full proof: [`STATE_227_WHOLE_STATE.md`](STATE_227_WHOLE_STATE.md).  
Machine summary: [`STATE_227_WHOLE_STATE_VERIFICATION.json`](STATE_227_WHOLE_STATE_VERIFICATION.json).  
Replay: [`STATE_227_REPLAY.md`](STATE_227_REPLAY.md).

State data:

```text
a=15, b=18, t=1,
s=2^4,3^11,
rho=1^7,2,3^10,
r=39, S=41.
```

Exact integer enumeration covers every excess profile through `E=20`; two equality profiles are removed by explicit hand rigidity. The relaxed `h_2` threshold/top-k argument closes `E=21,...,34`; total incoming capacity makes `E>=35` impossible. This moved the frozen frontier from `994 / 4,584` to `995 / 4,583`.

## Whole-state exclusion 2: N34 state 279

Full proof: [`STATE_279_WHOLE_STATE.md`](STATE_279_WHOLE_STATE.md).  
Machine summary: [`STATE_279_WHOLE_STATE_VERIFICATION.json`](STATE_279_WHOLE_STATE_VERIFICATION.json).  
Replay: [`STATE_279_REPLAY.md`](STATE_279_REPLAY.md).

State data:

```text
a=15, b=18, t=1,
s=2^3,3^12,
rho=1^7,3^11,
r=40, S=42.
```

The exact low-excess verifier covers `E=0,...,15`; three non-strict profiles are removed by explicit hand rigidity. The `h_2` tail closes every `E=16,...,34`, with minimum strict tail gap 2, and total incoming capacity excludes `E>=35`. This moved the frontier to `996 / 4,582`.

State 279 exposed a reusable **zero-excess availability** mechanism: a zero-excess label can use only sources with `p_u<=rho_u-1`, but the global incoming ledger can force the cheapest-q sources to carry too much `p`, pushing those labels onto larger endpoint loads and breaking the `C_i` budget.

## Whole-state exclusion 3: N34 state 588

Full proof: [`STATE_588_WHOLE_STATE.md`](STATE_588_WHOLE_STATE.md).  
Machine summary: [`STATE_588_WHOLE_STATE_VERIFICATION.json`](STATE_588_WHOLE_STATE_VERIFICATION.json).  
Replay: [`STATE_588_REPLAY.md`](STATE_588_REPLAY.md).

State data:

```text
a=15, b=18, t=1,
s=3^15,
rho=1^5,2,3^12,
r=43, S=45.
```

All selected labels have base demand three, so only the twelve `rho=3` sources can be active. The exact low-excess scan covers `E=0,...,15`; it has one coarse equality, at

```text
E=9, e=0^12,3^3, q=3^6,6^6,
```

which is excluded by an incidence-rigidity argument: equality forces the six `q=3` sources to have `p=5`, forcing all high-excess labels there and all 36 `q=6` incidences onto the zero-excess labels. Endpoint load then gives `sum C_i>=106`, contradicting the exact ledger `sum C_i=97`.

A cheap relaxed `h_2` tail screen makes every `E=16,...,34` layer strict except `E=16` and `E=24`. Exact profile replay then closes those two exception layers:

```text
E=16: 200/200 profiles strictly excluded;
E=24: 793 strict + 216 source-infeasible = 1,009/1,009 profiles.
```

The incoming-capacity ceiling is `sum p<=79`, while `Q=45+E`, so `E>=35` is impossible. State 588 therefore advances the frozen frontier to

```text
997 exclusions / 4,581 survivors,
```

split as

```text
4,503 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are scalar states in a frozen generalisation experiment, not surviving graphs. The separate fixed-order N34/N35 candidate proofs were already closed and are unchanged.

## New screening strategy

State 588 suggests a more efficient family-level workflow than exact-enumerating every state from scratch:

1. compute the cheap `h_2` relaxed tail gaps across the entire allowed excess range;
2. rank states by the number and severity of non-strict layers;
3. exact-enumerate only those exceptional layers;
4. if a low-excess equality survives, extract its equality conditions and seek a hand incidence-rigidity contradiction;
5. only after quantified pruning return to the stronger shared-residual/pair geometry.

This is now the primary threshold-family scan strategy.

The frozen survivor extraction utility [`extract_frozen_survivors.py`](extract_frozen_survivors.py) and [`.github/workflows/threshold-survivor-extract.yml`](../../../../.github/workflows/threshold-survivor-extract.yml) are transport/replay infrastructure only; they do not themselves apply a theorem.

## Raw candidate capacity

For a raw candidate quasi-edge `ui->w`, the selection-free package also gives

```text
d_i<=c_u-1,
C_i>=mu_u.
```

These define candidate-label sets `K_u` and the subset capacity inequality

```text
e(overline{H[B]}[U]) <= sum_(u in U) |K_u|,
```

with a positive-surplus sharpening by residual activity. This remains a secondary route for projecting graph-level candidate availability without choosing representatives.

## Independent maximum-cut route

[`MAXCUT_ROUTE.md`](MAXCUT_ROUTE.md) records

```text
e(G)=|X||Y|+I-M,
```

for any cut, where `I` is the number of internal edges and `M` the missing cross-pairs. Thus `I<=M` for some cut would prove Murty–Simon.

Reconnaissance found no violations among the preserved finite test sets and there is a hand proof for positive independent-set blow-ups of `C5`. A direct one-edge/one-nonedge matching proof is false and remains preserved as a failed route; any viable maximum-cut proof must use aggregate charging or stability.

## Audit boundaries and current priority

[`AUDIT.md`](AUDIT.md) records invalidated shortcuts and proof-status boundaries. None of the three whole-state closures uses numerical solver infeasibility: the proof-critical computations are exact integer enumerations, with explicit hand arguments where the coarse envelope is non-strict.

External mathematical review of the canonical bridge, the selected-excess/threshold lemmas, and the hand-rigidity arguments remains open; independent computational reproduction remains open.

**Current priority:** run the cheap threshold screen across the remaining **4,581** frozen states, rank the most tractable families by non-strict excess layers, and seek a symbolic theorem explaining the common state-227/state-279/state-588 mechanism before returning to fixed-pattern refinements.
