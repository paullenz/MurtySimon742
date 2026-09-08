# n=30 reconnaissance from the reduced n=29 kernel

8 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: reconnaissance / candidate reduction, not a proof of n=30.** The purpose is to test how much of the stripped n=29 bridge generalises before building any new bespoke machinery.

## Result

For a 30-vertex diameter-two edge-critical graph, the Murty-Simon target is

`floor(30^2/4)=225`.

Fan's cited strict bound leaves only `m=226` as a possible upper-bound counterexample; equality at `m=225` must be handled separately.

The parameterised early kernel gives the following picture.

| Delta | m | a | t=m-Delta(30-Delta) | charging-admissible demand tuples | threshold/source-count rejects | exact source-capacity dual rejects | early survivors |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 16 | 226 | 13 | 2 | 48,046 | 40,615 | 4,835 | **2,596** |
| 16 | 225 | 13 | 1 | 67,050 | 54,843 plus 1 bounds contradiction | 6,820 | **5,386** |
| 17 | 226 | 12 | 5 | 250 | **250** | 0 | **0** |
| 17 | 225 | 12 | 4 | 1,155 | **1,137** | **18** | **0** |
| 18..28 | 225 or 226 | 11..1 | positive | **0 in every scope** | — | — | **0** |

For Delta=16 at `m=225`, the 54,843 figure consists of 47,098 source-count contradictions and 7,745 threshold contradictions; one additional profile has an empty exact residual interval. For Delta=16 at `m=226`, it consists of 30,780 source-count contradictions and 9,835 threshold contradictions.

Thus the n=30 frontier is sharply concentrated at `Delta=16`.

## Strengthened Delta=16 preparation and clean residual-row scan

The next checkpoint uses two further consequences already proved in the n=29 bridge rather than adding any new graph lemma.

First, the isolated-`C` contradiction gives

`b <= a-1-t`

if `C=H[A]` has an isolated vertex. For `(a,b)=(13,16)` this is impossible at both `t=1` and `t=2`. Hence `delta(C)>=1`, so

`d_i<=11`, `e(C)>=ceil(13/2)=7`,

and therefore

`r<=C(13,2)-t-7`.

Second, the existing threshold-capacity inequalities and exact source-capacity Hall duals can be used not only as rejection certificates but as **certified lower bounds on `r`**. The implementation uses floating point only to propose dual weights; every bound used to raise `r_min` is checked with exact rational arithmetic.

The strengthened preparation gives:

| m | t | charging domain | basic empty | threshold empty | dual empty | retained demands |
|---:|---:|---:|---:|---:|---:|---:|
| 226 | 2 | 48,046 | 50 | 40,607 | 4,799 | **2,590** |
| 225 | 1 | 67,050 | 167 | 54,854 | 6,650 | **5,379** |

The clean residual scanner then enumerates every sorted length-16 residual row within the certified total interval and uses only the same two necessary rules as the n=29 minimal scanner: source-capacity Hall and monotone supplement-cap refinement.

Clean GitHub Actions run `34286806474` completed both jobs successfully.

| m | raw residual states | initial Hall rejects | refinement rejects | residual-row survivors |
|---:|---:|---:|---:|---:|
| 226 | **50,690,620** | 50,561,364 | 93,726 | **35,530** |
| 225 | **158,314,695** | 157,894,303 | 269,496 | **150,896** |

The saved clean artifacts are:

- `m=226`: artifact `10079792637`, artifact-ZIP SHA-256 `0c5ada3ff72d18c4e4c0768e9648b5672157063d6ed91112b1bf112830afcd14`;
- `m=225`: artifact `10079799176`, artifact-ZIP SHA-256 `39d08ee88568f5944947e267b866d369503a96ff65461464af178bf1c348dfe4`.

These rows are necessary-condition states, not graphs.

## Delta=17 is already closed by the early kernel

At `Delta=17`, `a=12`.

- For `m=226`, `t=5`. Exactly 250 demand tuples satisfy the charging inequality, and every one is rejected by the exact threshold-capacity/source-count inequalities.
- For `m=225`, `t=4`. Exactly 1,155 tuples satisfy charging. Threshold/source-count cuts reject 1,137; the remaining 18 are all rejected by exact source-capacity Hall dual certificates.

This uses only the generic hand bridge already isolated for n=29: residual activity, charging, threshold capacity and the source-capacity relaxation. No n=29-specific final LP model is involved.

## Delta>=18 is already closed by charging

For every `Delta=18,...,28` at both `m=225` and `m=226`, the exact nondecreasing demand-domain enumeration is empty: no integer demand profile can satisfy

`sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t`.

Hence, conditional on the audited graph-to-demand bridge, these degree scopes are excluded before any row enumeration.

`Delta=29` is the universal-vertex case and edge-criticality forces a star.

## Delta=15 equality is a short hand case

At `m=225`, if `Delta=15`, degree sum forces every vertex to have degree exactly 15.

For a non-bipartite graph at this density, the published dominating-edge bound excludes a dominating edge. Every critical edge has either a direct witness (an adjacent pair with no common neighbour) or a two-step witness (a nonedge with exactly one common neighbour). In either case, absence of a dominating edge gives witness degree-sum at most

`n-1=29`.

But in a 15-regular graph every pair has degree sum 30, contradiction. Therefore the non-bipartite Delta=15 equality case is impossible.

A bipartite diameter-two graph is complete bipartite, and 225 edges on 30 vertices forces `K(15,15)`.

Thus equality uniqueness at n=30 will reduce to excluding the remaining Delta=16, `m=225` scope.

## Current next stage

A fresh n=30 version of the corrected cumulative-threshold/source-flow relaxation has now been written as `n30_threshold_model.py`. It is parameterised directly at `(a,b)=(13,16)` and does **not** import either historical n=29 threshold builder. In particular it retains the corrected per-label normalization

`sum_k n_k Z = sum_h T_h`

with no extra label-group multiplicity.

`n30_threshold_scan.py` provides shardable numerical reconnaissance and optional exact integer-Farkas certification.

The next step is to measure how strongly this model cuts the 35,530 / 150,896 residual-row frontiers, then run exact certificates only where the numerical pilot shows the route is effective. No Delta=16 exclusion is claimed at this checkpoint.

## What remains for n=30

A complete n=30 candidate now appears to require only:

1. exclude `Delta=16, m=226`;
2. exclude non-bipartite `Delta=16, m=225`.

No completion is claimed here.

## Replay

Early-kernel reconnaissance:

```bash
python n30_recon.py
```

Strengthened Delta=16 preparation and row scan are replayed by:

```text
.github/workflows/n30-d16-rows.yml
```

The scripts use exact rational arithmetic for every saved mathematical inequality. SciPy/HiGHS is used only to propose source-capacity dual weights or later Farkas rays; an exact rejection is counted only after the corresponding rational/integer inequalities are checked directly.
