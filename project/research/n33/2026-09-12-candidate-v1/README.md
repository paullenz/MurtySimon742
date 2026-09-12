# N33 candidate-v1 checkpoint

12 September 2026.

**Candidate statement**

```text
e(G) <= 272 = floor(33^2/4),
with equality exactly K(16,17).
```

This is AI-assisted candidate mathematics. Independent specialist review, novelty assessment and independent computational reproduction remain OPEN.

## Start here

- [Complete candidate proof](PROOF.md)
- [Frozen 21-profile equality frontier](N33_T2_FRONTIER.csv)
- [Independent 20,058,300-multiset frontier checker](check_n33_t2_frontier.cpp)
- [Exact 25-state shifted-potential verifier](n33_t2_shifted_potential_exact.py)
- [One-command replay](run_replay.sh)

## Proof architecture

At `m>=272`, average degree gives `Delta>=17`.

- `Delta=17`: hand witness-deficit proof; `m>=273` impossible and equality `m=272` forces `K(17,16)`.
- `Delta=18`: `m>=273` is scalar-impossible from `Q<=23` versus `Q>=18+2t`; equality has `(a,b,t)=(14,18,2)`.
- `Delta=19`: thirteen-label theorem excludes the target range.
- `Delta>=20`: twelve-label source-independent theorem puts the graph below 272; the universal-vertex case is a star.

The only new finite frontier is therefore `Delta=18,m=272`.

The fourteen-label score checker finds exactly 21 demand profiles (`18` with `Q=22`, `3` with `Q=23`). Monotone residual-tail closure and all allowed slack increments produce exactly 29 positive-demand `(s,rho)` states.

A fixed nine-term potential, obtained by shifting the N32 `t=2` `v=b-h` thresholds while retaining the same graph-level `h` cutoffs, excludes 25/29 states with exact integer acceptance. The four potential failures are all excluded by hand in the proof:

```text
(3,4,5^12) / (1^6,3,4,5^10)
(3,5^13)   / (1^6,3,5^11)
(4^2,5^12) / (1^6,4^2,5^10)
(4,5^13)   / (1^6,4,5^11)
```

No full RX/Hall Farkas stage is needed in the final N33 route.

## Replay

From repository root:

```sh
bash project/research/n33/2026-09-12-candidate-v1/run_replay.sh
```

Expected checker output begins with

```text
OK: 20,058,300 multisets; Q22=18 Q23=3; 21 total; all positive; max demand=5
```

and the Python verifier must report

```text
status: PASS
expanded_states: 29
exact_potential_exclusions: 25
hand_states: 4
failures: 0
```

Floating LP is used only to propose scalar envelope coefficients. Every accepted finite exclusion is rechecked in integer arithmetic after one-sided envelope repair.

## Trust boundary

The candidate remains conditional on the universal selected/residual bridge, the twelve-/thirteen-/fourteen-label tail theorems, threshold-capacity and its equality case, endpoint load/source forcing, and correct finite-frontier reconstruction. Same-assistant replay is not external mathematical validation.
