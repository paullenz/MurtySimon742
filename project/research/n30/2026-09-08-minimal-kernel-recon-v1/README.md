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

Thus the new n=30 computational frontier is sharply concentrated at

`Delta=16`,

with 2,596 early demand profiles at 226 edges and 5,386 at 225 edges.

No residual-row enumeration or corrected-v2 LP has yet been run for those scopes in this checkpoint.

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

Thus equality uniqueness at n=30 will reduce to excluding the remaining Delta=16, m=225 scope.

## What remains for n=30

A complete n=30 candidate now appears to require only:

1. exclude `Delta=16, m=226`;
2. exclude non-bipartite `Delta=16, m=225`.

The next research step should **parameterise the residual-row scanner and corrected-v2 cumulative-threshold LP to `(a,b)=(13,16)`**, not invent a new n=30-specific model.

The existing early survivors are small enough to make that a plausible direct continuation, but no completion is claimed here.

## Replay

Run:

```bash
python n30_recon.py
```

The script uses exact rational arithmetic for every saved mathematical inequality. SciPy/HiGHS is used only to propose source-capacity dual weights; a dual rejection is counted only after the rational/integer inequalities are checked directly.
