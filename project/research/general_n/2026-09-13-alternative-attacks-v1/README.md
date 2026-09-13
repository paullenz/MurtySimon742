# Alternative attacks v1 — quantifier correction and whole-state threshold programme

13 September 2026. **Research checkpoint. Candidate hand lemmas and exact finite reductions; external review, novelty assessment and independent reproduction remain OPEN. The unrestricted Murty–Simon conjecture is not proved.**

## Why this branch exists

The shared-residual-budget continuation rejects 4,487 of 4,584 stored selected patterns, but a fixed-pattern rejection does not exclude a scalar state because another selected geometry may exist. This branch therefore attacks the missing quantifiers directly.

The programme has two lines:

1. **geometry quantification / selection-free structure:** quantify alternative selected sets, source margins and selected excess;
2. **maximum-cut reformulation:** retain an independent proof architecture in case the canonical A/B model reaches a natural limit.

The first line has now produced **two whole-state exclusions**, N34 states **227 and 279**.

## Core selected-excess lemmas

See [`SELECTION_FREE.md`](SELECTION_FREE.md).

For every selected incidence `ui` on a positive-demand label,

```text
p_u-rho_u+1 <= x_i-s_i.                              (1)
```

In exact demand `x=s`, every active source therefore has

```text
p_u<=rho_u-1.
```

Moreover selected labels at source u satisfy

```text
q_u+p_u <= C_i <= rho_u+q_u-1.
```

### Threshold form

Put

```text
e_i=x_i-s_i,
h_l=#{i:e_i>=l}.
```

If `p_u-rho_u+1>=l`, every one of the source's q selected labels has excess at least l. Hence

```text
q_u<=h_l,
```

or equivalently

```text
q_u>h_l => p_u<=rho_u+l-2.                            (2)
```

This threshold family is general. The `l=2` member already closes the high-excess tails of both state 227 and state 279.

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

The closure climbs the quantifier hierarchy explicitly:

1. one saved exact-demand margin class, all selected geometries;
2. every q-vector at exact demand;
3. every excess profile through `E=20` by exact integer enumeration;
4. every `E=21,...,34` by the `h_2` threshold/top-k tail inequality;
5. `E>=35` by total incoming capacity.

The exact `E=0,...,20` stage covers **49,847 profiles**. The weakest tail contradiction is still +8. Therefore state 227 has no realization satisfying the canonical bridge.

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

This state is structurally cleaner than 227 because there is no `rho=2` source class.

- `verify_state279_low.cpp` exhausts every excess profile for `E=0,...,15`.
- All but three profiles are strictly excluded by the first endpoint/excess envelope.
- The remaining three have unique nonpositive q-vectors and are eliminated by hand rigidity of the three zero-excess demand-two labels.
- `verify_state279_tail.cpp` excludes every `E=16,...,34` using only the relaxed `h_2` threshold cap and top-k endpoint bounds. The weakest tail gap is +2.
- `E>=35` is impossible because total incoming capacity is 76 while `Q=42+E>=77`.

Thus state 279 is also a whole-state exclusion.

## New rigidity mechanism exposed by state 279

The state-279 exceptions reveal a second reusable mechanism complementary to (2).

A zero-excess label can be selected only by sources with

```text
p_u<=rho_u-1.
```

But the global incoming ledger may force the cheap-q sources to carry high p. If too many such sources become ineligible for the zero-excess labels, those labels must be supplied by larger-q sources, which raises their endpoint loads `C_i>=q_u+p_u` and breaks the endpoint budget.

So the emerging two-sided theory is:

1. **high-excess labels** restrict which large-p sources can have large q through the `h_l` threshold family;
2. **zero-excess labels** require enough low-p sources to remain available;
3. the same incoming ledger must satisfy both requirements.

This is now the primary generalisation target.

## Current frozen frontier

The compatible-routing/generalisation pool began this phase at

```text
994 exclusions / 4,584 survivors.
```

The two quantified whole-state closures change it to

```text
996 exclusions / 4,582 survivors,
```

split as

```text
4,504 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are scalar states in a frozen generalisation experiment, not surviving graphs. The separate fixed-order N34/N35 candidate proofs were already closed and are unchanged.

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

for any cut, where I is the number of internal edges and M the missing cross-pairs. Thus `I<=M` for some cut would prove Murty–Simon.

Reconnaissance found no violations among the preserved finite test sets and there is a hand proof for positive independent-set blow-ups of `C5`. A direct one-edge/one-nonedge matching proof is false and remains preserved as a failed route; any viable maximum-cut proof must use aggregate charging or stability.

## Audit boundaries

[`AUDIT.md`](AUDIT.md) records the invalid unrestricted switching interpretation, the failed naïve maximum-cut injection, solver-status limits and the dependency of all active excess lemmas on the canonical bridge.

Neither whole-state closure uses numerical solver infeasibility. The proof-critical computations are exact integer enumerations. External mathematical review and independent computational reproduction remain open.

## Current priority

Apply the **threshold + zero-excess availability** mechanism across the remaining 4,582 frozen states, beginning with the low-demand N34 family nearest states 227/279. Seek a parameterized theorem in `(s,rho,E,h_l)` before returning to fixed-pattern shared-budget refinements.
