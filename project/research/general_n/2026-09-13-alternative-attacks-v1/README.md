# Alternative attacks v1 — quantifier correction and whole-state threshold programme

13 September 2026. **Research checkpoint. Candidate hand lemmas and exact finite reductions; external review, novelty assessment and independent reproduction remain OPEN. The unrestricted Murty–Simon conjecture is not proved.**

## Why this programme exists

The shared-residual-budget continuation rejects 4,487 of 4,584 stored selected patterns, but a fixed-pattern rejection does not exclude a scalar state because another selected geometry may exist. This programme therefore attacks the missing quantifiers directly.

The main line quantifies alternative selected sets, source margins and selected excess. A separate maximum-cut line is retained as an independent proof architecture. The quantified line has now produced **four whole-state exclusions: N34 states 227, 279, 588 and 526**.

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

The `l=2` member is already strong enough to close most or all of the high-excess tails in all four quantified examples.

## Whole-state exclusion 1: N34 state 227

Full proof: [`STATE_227_WHOLE_STATE.md`](STATE_227_WHOLE_STATE.md).  
Machine summary: [`STATE_227_WHOLE_STATE_VERIFICATION.json`](STATE_227_WHOLE_STATE_VERIFICATION.json).  
Replay: [`STATE_227_REPLAY.md`](STATE_227_REPLAY.md).

```text
a=15, b=18, t=1,
s=2^4,3^11,
rho=1^7,2,3^10,
r=39, S=41.
```

Exact integer enumeration covers every excess profile through `E=20`; two equality profiles are removed by explicit hand rigidity. The relaxed `h_2` threshold/top-k argument closes `E=21,...,34`; total incoming capacity makes `E>=35` impossible. Frontier: `994/4,584 -> 995/4,583`.

## Whole-state exclusion 2: N34 state 279

Full proof: [`STATE_279_WHOLE_STATE.md`](STATE_279_WHOLE_STATE.md).  
Machine summary: [`STATE_279_WHOLE_STATE_VERIFICATION.json`](STATE_279_WHOLE_STATE_VERIFICATION.json).  
Replay: [`STATE_279_REPLAY.md`](STATE_279_REPLAY.md).

```text
a=15, b=18, t=1,
s=2^3,3^12,
rho=1^7,3^11,
r=40, S=42.
```

The exact low-excess verifier covers `E=0,...,15`; three non-strict profiles are removed by explicit hand rigidity. The `h_2` tail closes every `E=16,...,34`, with minimum strict tail gap 2, and total incoming capacity excludes `E>=35`. Frontier: `995/4,583 -> 996/4,582`.

State 279 exposed a reusable **zero-excess availability** mechanism: a zero-excess label can use only sources with `p_u<=rho_u-1`, but the global incoming ledger can force the cheapest-q sources to carry too much `p`, pushing those labels onto larger endpoint loads and breaking the `C_i` budget.

## Whole-state exclusion 3: N34 state 588

Full proof: [`STATE_588_WHOLE_STATE.md`](STATE_588_WHOLE_STATE.md).  
Machine summary: [`STATE_588_WHOLE_STATE_VERIFICATION.json`](STATE_588_WHOLE_STATE_VERIFICATION.json).  
Replay: [`STATE_588_REPLAY.md`](STATE_588_REPLAY.md).

```text
a=15, b=18, t=1,
s=3^15,
rho=1^5,2,3^12,
r=43, S=45.
```

The exact low-excess scan covers `E=0,...,15`; its unique coarse equality is excluded by incidence rigidity, giving `sum C_i>=106>97`. A cheap relaxed `h_2` screen is strict on every `E=16,...,34` except `E=16` and `E=24`; exact profile replay closes those two layers. Incoming capacity excludes `E>=35`. Frontier: `996/4,582 -> 997/4,581`.

State 588 shows that the mechanism is not tied to demand-two correction terms and motivates cheap tail triage before exact enumeration.

## Whole-state exclusion 4: N34 state 526

Full proof: [`STATE_526_WHOLE_STATE.md`](STATE_526_WHOLE_STATE.md).  
Machine summary: [`STATE_526_WHOLE_STATE_VERIFICATION.json`](STATE_526_WHOLE_STATE_VERIFICATION.json).  
Replay: [`STATE_526_REPLAY.md`](STATE_526_REPLAY.md).

```text
a=15, b=18, t=1,
s=2,3^14,
rho=1^5,2^2,3^11,
r=42, S=44.
```

The exact low-excess scan covers `E=0,...,16`; it has one coarse equality,

```text
E=7, e_2=7, e_3=0^14,
q_(rho=2)=1^2,
q_(rho=3)=1^2,5^7,6^2.
```

The incoming ledger forces the two `rho=2,q=1` sources to `p=4`, the two `rho=3,q=1` sources to `p=5`, and all nine `q=5/6` sources to `p=2`. The four q=1 sources must select the unique high-excess label. Hence all fourteen zero-excess demand-three labels are selected only at q=5/6 sources, so each has `C_i>=7`. Those labels alone give `sum C_i>=98`, contradicting the exact total `sum C_i=93`.

The relaxed `h_2` tail has gap zero only at `E=16`, already strictly excluded by the exact scan with gap 23. Every `E=17,...,34` has positive relaxed gap; total incoming capacity `sum p<=78` excludes `E>=35`. Frontier: `997/4,581 -> 998/4,580`.

## Current frozen frontier

The four quantified whole-state closures give

```text
998 exclusions / 4,580 survivors,
```

split as

```text
4,502 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are scalar states in a frozen generalisation experiment, not surviving graphs. The separate fixed-order N34/N35 candidate proofs were already closed and are unchanged.

## New screening strategy

States 588 and 526 support a more efficient family-level workflow than exact-enumerating every state from scratch:

1. compute the cheap `h_2` relaxed tail gaps across the allowed excess range;
2. rank states by the number and severity of non-strict layers;
3. exact-enumerate only those exceptional layers plus the genuinely low-excess region;
4. if an equality survives, extract its source-capacity equality conditions and seek a hand incidence-rigidity contradiction;
5. only after quantified pruning return to the stronger shared-residual/pair geometry.

The frozen survivor extraction utility [`extract_frozen_survivors.py`](extract_frozen_survivors.py) is transport/replay infrastructure only; it does not itself apply a theorem.

## Raw candidate capacity

For a raw candidate quasi-edge `ui->w`, the selection-free package also gives

```text
d_i<=c_u-1,
C_i>=mu_u.
```

These define candidate-label sets `K_u` and a source-subset capacity inequality. This remains a secondary route for projecting graph-level candidate availability without choosing representatives.

## Independent maximum-cut route

[`MAXCUT_ROUTE.md`](MAXCUT_ROUTE.md) records

```text
e(G)=|X||Y|+I-M,
```

for any cut, where `I` is the number of internal edges and `M` the missing cross-pairs. Thus `I<=M` for some cut would prove Murty–Simon. A direct one-edge/one-nonedge matching proof is false and remains preserved as a failed route; any viable maximum-cut proof must use aggregate charging or stability.

## Audit boundaries and current priority

[`AUDIT.md`](AUDIT.md) records invalidated shortcuts and proof-status boundaries. None of the four whole-state closures uses numerical solver infeasibility: the proof-critical computations are exact integer enumerations, with explicit hand arguments where the coarse envelope is non-strict.

External mathematical review of the canonical bridge, selected-excess/threshold lemmas and hand-rigidity arguments remains open; independent computational reproduction remains open.

**Current priority:** run cheap threshold triage across the remaining **4,580** frozen states, especially the adjacent low-demand N34 family, and seek a symbolic theorem explaining the common state-227/state-279/state-588/state-526 mechanism before returning to fixed-pattern refinements.
