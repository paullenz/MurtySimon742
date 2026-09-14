# Frozen-state global ledger invariant

14 September 2026. **Exact invariant of the current N34/N35 frozen scalar-state construction. This note does not claim the same formula outside that construction without rederivation.**

The q-tail red-team exposed that target-cap and selected-incidence constraints alone admit hostile profiles which never occur in the actual frozen Murty frontier. The missing hypothesis is already present in the original fixed-order state generation and should be stated explicitly.

## 1. Notation

For a scalar state write

```text
a = size of the A-side source-label universe,
b = number of B-side sources,
t = fixed positive surplus parameter,
s=(s_i)_{i=1}^a,
rho=(rho_u)_{u=1}^b,
S=sum_i s_i,
r=sum_u rho_u.
```

The current frozen layers have

```text
a=15,
b=18  on N34 m=289,
b=19  on N35 m=306 or 307,
t>0,
rho_u>=1 for every u.                                  (1)
```

## 2. N34 reconstruction

[`../../n34/2026-09-12-frontier-v1/check_frontier.py`](../../n34/2026-09-12-frontier-v1/check_frontier.py) reconstructs a baseline residual sequence `rho0` from the demand tails and defines

```text
slack = S - 2t - sum(rho0).                             (2)
```

It then raises residual coordinates using at most this many units of slack. Every generated residual variant is explicitly required to satisfy

```text
sum(rho) <= S - 2t.                                     (3)
```

Therefore every N34 frozen scalar state satisfies

> **Global frozen-state ledger**
>
> ```text
> S >= r + 2t.                                          (4)
> ```

This statement includes zero-demand states; no positivity assumption on every `s_i` is needed for (4).

## 3. N35 independent reconstruction

[`../../n35/2026-09-12-candidate-v1/frontier.py`](../../n35/2026-09-12-candidate-v1/frontier.py) independently rebuilds the N35 residual frontier. It again defines

```text
slack = S - 2t - sum(base),                             (5)
```

asserts `slack>=0`, and recursively spends at most that budget while increasing residual coordinates. Consequently every generated N35 state also satisfies

```text
r <= S - 2t,                                            (6)
```

hence the same ledger (4).

Thus (4) is not an artefact of one implementation.

## 4. Positive-demand equality branch

The later general heavy-load replay makes a sharper distinction. In [`../2026-09-12-heavy-load-family-v1/probe_frontiers.py`](../2026-09-12-heavy-load-family-v1/probe_frontiers.py), whenever every demand is positive, a state with

```text
S != r + 2t                                             (7)
```

is already removed by the existing `positive_degree_mass` condition before the newer heavy-load family is searched.

Therefore every **positive-demand state which reaches the later frozen survivor pool** satisfies the equality

```text
S = r + 2t.                                             (8)
```

Zero-demand states may retain strict slack

```text
S > r + 2t,                                             (9)
```

but still obey the universal frozen-state inequality (4).

## 5. Immediate consequences

Because the current survivor stream also has

```text
rho_u>=1,
```

we have

```text
r>=b.                                                   (10)
```

Combining with (4):

```text
S >= b+2t > 0.                                         (11)
```

Hence an all-zero demand profile is impossible in the live frozen domain. This directly excludes the hostile q-tail counterexample with `s=(0,...,0)` which is feasible in the weaker target-cap + selected-incidence relaxation.

More generally, any future finite or symbolic red-team intended to model the current N34/N35 frontier must impose (4), not merely

```text
Q=S+E,
q_u+rho_u<=a,
selected-incidence feasibility,
target-cap feasibility.                                (12)
```

Omitting (4) enlarges the domain in a mathematically material way.

## 6. Relation to all-order work

Equation (4) is presently asserted here as an exact invariant of the frozen N34/N35 state construction. Its graph-theoretic origin should be rederived directly from the canonical bridge before it is used as a general-N theorem.

For current finite frontier work it is proof-critical input because the survivor stream itself was generated under this ledger. For an unrestricted all-order proof the correct sequence is:

```text
fixed-order ledger identity
 -> direct graph-theoretic derivation
 -> general-N statement with explicit hypotheses.       (13)
```

No later theorem should silently extrapolate (4) beyond its proved scope.

## 7. Verification target

The companion verifier reads the hash-pinned `survivors.json` stream from the compatible-routing package and checks every combined survivor state for:

```text
a=15,
b in {18,19},
t>0,
rho>=1,
S>=r+2t,
and S=r+2t whenever min(s)>0.                           (14)
```

This verifier checks preservation of the frozen ledger; it is not the proof of the underlying graph-theoretic bridge.

## Trust boundary

The state-generation implications above are exact arithmetic consequences of the preserved N34 and N35 reconstruction programs. The general-N interpretation remains open until the ledger is derived directly from the graph bridge rather than inherited from fixed-order frontier generation.
