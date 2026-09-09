# General-N RX-Hall / staircase-potential programme

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite evidence plus candidate structural reductions. Not an unrestricted theorem. Independent mathematical review remains OPEN.**

## 1. Current position

Mining the exact n=29 and n=30 Delta=16 certificates exposed a much smaller endpoint mechanism than the original cumulative-threshold LP. The project has now moved beyond profile-by-profile Farkas rejection into a search for reusable **BC/SH staircase potentials**.

In the positive-demand zero-slack sector,

```text
S=sum_i s_i=r+2t.
```

For a selected incidence from B-source `u` to A-label `i`, write

```text
rho_u  source residual degree
q_u    selected outdegree
p_u    supplement indegree
s_i>0  label demand
R_i    residual column degree
x_i    selected label degree.
```

The graph-to-model bridge gives

```text
s_i <= rho_u,                                      (RX1)
R_i+s_i <= rho_u+q_u-1,                           (RX2)
R_i+x_i >= q_u+p_u.                               (RX3)
```

The stripped RX-Hall model keeps source/supplement compatibility, endpoint Hall structure, selected incidence and residual bookkeeping while deleting the old cumulative-tail machinery and unordered-pair aggregate capacity.

## 2. Exact n=29 RX-Hall frontier

The n=29 hard frontiers are exact finite results:

```text
(a,b,t,dmax)=(12,16,3,10): 94/94 exact integer Farkas rejections;
(a,b,t,dmax)=(12,16,2,10): 902/902 exact integer Farkas rejections.
```

All 996 profile certificates were independently replayed with standard-library-only arithmetic. Numerical LP is proposal-only; integer coefficient dictionaries are the acceptance layer. This remains conditional on the graph-to-demand/RX-Hall bridge and the earlier exact frontier preparation.

The earlier t=3 Hall-core reduction also remains preserved: all 94 t=3 rows are rejected by a much weaker model retaining essentially RX1, RX3, selected-incidence balance, source/supplement threshold transport and Hall inequalities for unions of at most two compatibility rectangles. See [`HALL_CORE_SYMBOLIC_LEMMAS.md`](HALL_CORE_SYMBOLIC_LEMMAS.md).

## 3. Exact order-wide n=29 common potential

A major compression is now exact.

One fixed **9 BC + 7 SH** staircase support admits one common staircase-weight vector across **all 996 n=29 hard profiles simultaneously**: all 902 t=2 profiles and all 94 t=3 profiles. Scalar dual bookkeeping remains profile-specific.

The exactifier checked

```text
profiles: 996
rows:     364,805
variables:22,586
row violations:   0
bound violations: 0
```

with deterministic scaling/repair followed by integer-only verification. Canonical checkpoint:

`checkpoints/N29_ALL_T23_EXACT_RUN_34375129207.json`

The successful workflow artifact was manually republished after only its final Git push raced; publication commit: `704eeb0fb05ae31bc5e1d04607f826eb07d38631`.

This is an exact finite **order-wide n=29 potential**, not an unrestricted theorem.

## 4. Boundary specialization and the 38 difficult t=2 profiles

The original n=30 nine-shape dictionary separates 932 of the 996 n=29 profiles profile-by-profile. In the t=2 sector it separates 838/902. Specializing the two dmax-sensitive BC staircases from dmax=11 to dmax=10 separates 26 more, leaving exactly **38** difficult t=2 profiles.

Those 38 admit an exact common **8 BC + 6 SH** potential. The integer exactifier reports zero row and bound violations at scale 1,000,000.

Canonical checkpoint:

`checkpoints/N29_COMMON_14_EXACT_RUN_34369583832.json`

Thus 14 shapes are an exact finite **upper/existence** bound for this generated common-potential problem.

## 5. Support compression: computationally 14 in the canonical dictionary

The canonical generated n=29 staircase dictionary is now materialized explicitly as

```text
75 BC shapes + 12 SH shapes = 87 total shapes.
```

Canonical catalog:

`N29_CANONICAL_DICTIONARY.json`

It is the dmax=10 specialization of `N30_SHARED_MIN_SUPPORT_RUN_34361230390.json` plus every generated n=29 pairwise correction in `N29_PAIRWISE_CORRECTION_RUN_34365472773.json`. This provenance matters: an earlier diagnostic accidentally reconstructed an 84-shape dictionary and is retained only as superseded audit history.

### Demand 45

Demand 45 is the single-profile bottleneck:

```text
s   = (1,1,3,3,3,3,4,4,4,4,4,4)
rho = (1,1,1,1,1,1,1,1,1,3,3,3,4,4,4,4).
```

Across the full 75+12 dictionary its zero-gap minimum-support MILP is

```text
13 = 7 BC + 6 SH.
```

Checkpoint: `checkpoints/N29_DEMAND45_FULL_MIN_RUN_34374650328.json`.

Fixing those 13 shapes and allowing new common weights over all 38 profiles is LP-infeasible. Moreover, adding each of the other 74 generated shapes one at a time still gives no common 14-shape repair. Therefore the exact common 14-shape basis genuinely requires BC substitutions rather than simply “demand45 + one extra cut.”

### Demand 45 + demand 68

Demand 68 differs from demand 45 by a tiny smoothing move:

```text
label side:  1 + 4  ->  2 + 2
source side: one residual degree 3 -> 2.
```

In the full canonical 75+12 dictionary, the two-profile system `{45,68}` has zero-gap minimum common support **14** at both coefficient caps `M=200` and `M=1000`.

Checkpoint:

`checkpoints/N29_DEMAND45_PAIR_MIN_RUN_34379676403.json`

This is strong **computational** support-minimality evidence, not an exact mathematical support-exclusion certificate. Accordingly the safe description is:

> the 38-profile common support is computationally pinned to 14 in the canonical generated dictionary; the 14-shape existence side is exact, while the lower-bound side is zero-gap big-M MILP evidence.

The detailed checkpoint and trust distinction are summarized in [`N29_COMMON_POTENTIAL_COMPRESSION.md`](N29_COMMON_POTENTIAL_COMPRESSION.md).

## 6. Structural lesson inside n=29: SH stable, BC adaptive

The demand-45 optimum, the demand45+68 pair solutions and the exact 38-profile common solution all retain the same six SH correction shapes. The basis movement occurs in BC.

Across the pair and 38-profile solutions there is a substantial stable BC core, with two BC slots moving on a small face of alternatives. The very small demand45 -> demand68 majorization move is enough to force that BC switch while leaving the SH family unchanged.

This makes a **parameterized BC transport envelope** a much better symbolic target than fourteen unrelated inequalities.

## 7. Recovered exact n=30 nine-shape potential

The n=30 hard equality-frontier states also possess an exact common potential. An earlier workflow had succeeded mathematically but lost only its final Git push; the exact artifact has now been recovered and republished.

Exact n=30 support:

```text
6 BC + 3 SH = 9 shapes
profiles: 7
rows: 2,775
variables: 55
row violations: 0
bound violations: 0
integer-only acceptance: PASS
```

Every profile margin is approximately twice the required exact margin.

Canonical checkpoint:

`checkpoints/N30_SHARED_NINE_EXACT_RUN_34371786328.json`

Recovery commit: `dda9b36a68c24736709d928b6183e5c53ec9f1ea`.

This exact 6-BC basis is **not** the same as the earlier floating n=30 minimum-support basis. The exact checkpoint above is canonical for exact-support comparisons.

## 8. Cross-order falsification: fixed n=29 geometry does not extend literally

Several increasingly permissive cross-order hypotheses have now been falsified.

First, one identical 16-shape numerical weight vector across all 996 n=29 profiles plus all seven n=30 hard profiles is LP-infeasible:

`checkpoints/CROSS_ORDER_ALL1003_FIXED16_RUN_34375647941.json`.

Second, even when n=30 receives completely **fresh weights**, the raw exact n=29 9-BC + 7-SH shapes are still infeasible for the seven n=30 states:

`checkpoints/N30_REWEIGHT_N29_FIXED16_RUN_34380758859.json`.

Third, restoring `(11,-11)` to the two BC shapes known to change under dmax=10 -> 11 specialization is still insufficient:

`checkpoints/N30_BOUNDARY_LIFT_N29_FIXED16_RUN_34380884815.json`.

Finally, adding each n=30 hard profile separately to the all-996 n=29 common-weight cone makes the raw n=29 16-shape system infeasible in **all seven cases**, so there is no single exceptional n=30 row to patch:

`checkpoints/CROSS_ORDER_N30_SINGLE_OBSTRUCTION_MATRIX_RUN_34380314207.json`.

These are finite LP falsifications of the stated hypotheses, not graph-theoretic counterexamples.

## 9. Exact n=29 versus n=30 support geometry

The strongest structural comparison is now deterministic rather than impressionistic.

Each of the six exact n=30 BC shapes was specialized to dmax=10 and compared against **all 75 canonical n=29 BC shapes**. Each of the three exact n=30 SH shapes was compared literally against all 12 n=29 SH shapes.

Result:

```text
BC exact matches: 1 / 6
SH exact matches: 3 / 3
```

Canonical comparison:

`N30_EXACT_VS_N29_DICTIONARY.json`.

Only the BC staircase `((1,-3),)` survives literally across the exact supports. By contrast, all three exact n=30 SH staircases already occur in the n=29 SH dictionary:

```text
((1,-1),(2,-5),(3,-6))
((1,-1),(2,-7))
((1,-1),(2,-2),(3,-11)).
```

This is currently the clearest general-N signal in the RX-Hall programme:

> **SH correction geometry is strongly cross-order stable; BC geometry changes substantially with order/surplus parameters.**

The next general theorem should therefore not assume a fixed literal BC dictionary. It should seek a symbolic rule generating the BC envelope from `(a,b,dmax,t)` and/or the demand/source distributions.

## 10. Current analytic frontier

Subsequent work has compressed the finite potential mechanism substantially beyond the staircase-dictionary comparison.

For the complete regenerated n=29 `t=3` frontier (94 hard profiles), the full canonical BC family needs **no SH correction**. The resulting BC potential was first exactified as a pure staircase surface and then replaced by the analytic min-hinge family

```text
H_{D,V}(d,v)=min((d-D)_+,(v-V)_+).
```

A single exact rational potential using only nine hinges works across all 94 profiles. The exact support is

```text
(0,0), (0,2),
(1,7),(1,8),(1,9),(1,10),(1,11),
(2,0),(4,0).
```

See [`MIN_HINGE_ANALYTIC_REDUCTION.md`](MIN_HINGE_ANALYTIC_REDUCTION.md) and
[`checkpoints/N29_T3_MIN_HINGE_EXACT_RUN_34384549422.json`](checkpoints/N29_T3_MIN_HINGE_EXACT_RUN_34384549422.json).
The latter checks 30,646 inequalities by integer arithmetic, with no row or bound violations and worst profile margin nearly twice the required margin.

The hinge has the exact discrete Hall-chain identity

```text
H_{D,V}(d,v)=sum_{k>=1} 1[d>=D+k and v>=V+k],
```

so this analytic form is a weighted chain of nested Hall rectangles rather than an unrelated fitted nonlinearity.

On the difficult n=29 `t=2` post-specialization core, all 75 canonical BC staircases solve 37 of the 38 profiles individually without SH; demand 45 is the unique BC-only obstruction. With all BC shapes available, a common hard38 potential needs only three SH shapes in the current zero-gap support-minimization experiment. Those minimum-support statements are computational/MILP evidence; positive common potentials are exactified separately before being used as proof evidence.

The nine exact `t=3` hinge locations admit the parameter-only description

```text
(0,0),
(0,t-1),
(t-2,V) for V=a-t-2,...,a-1,
(t-1,0),
(t+1,0),
```

specialized at `(a,t)=(12,3)` (with duplicates/nonnegative boundary handling for small `t`). This is now the principal falsification target, not a theorem.

## 11. Highest-priority next steps

1. test the parameterized min-hinge template on the n=29 `t=2` hard38 core with and without the full SH correction dictionary;
2. if it survives, test the same template on all 902 `t=2` profiles and exactify any positive result;
3. isolate and symbolically explain the demand-45 correction rather than increasing the feature dictionary indiscriminately;
4. test the resulting parameter rule on the n=30 `t=1` laboratory and then on new synthetic/fixed-order falsification domains;
5. derive closed source/label envelopes for the min-hinges, exploiting the cancellation in `min(u,v) <= (u+v)/2`;
6. combine the analytic potential with charging/demand bounds to seek a maximum-degree theorem below `7/12`;
7. continue external review of the universal graph-to-demand/RX-Hall bridge, which remains the main mathematical trust boundary.

No complete order above 30, unrestricted solution, novelty determination, full formal verification or external endorsement is claimed here.
