# State 226 — unique staircase-band false negative

14 September 2026. **Reconnaissance / theorem-design diagnostic only. No whole-state promotion follows from this note. External review remains OPEN.**

## Provenance

The unique false negative from [`STAIRCASE_BAND_REACH_PILOT.md`](STAIRCASE_BAND_REACH_PILOT.md) was isolated by GitHub Actions run `34838612503` at head `2e0080d0c19318709a93a0130620e634e022e905`. The run completed successfully and asserted that there was exactly one band false negative and that it was N34-derived state `226`.

Preserved raw block: [`STATE_226_BAND_EXCEPTION_DIAGNOSTIC.txt`](STATE_226_BAND_EXCEPTION_DIAGNOSTIC.txt).

Preserved provenance: [`STATE_226_BAND_EXCEPTION_DIAGNOSTIC_PROVENANCE.json`](STATE_226_BAND_EXCEPTION_DIAGNOSTIC_PROVENANCE.json).

Original Actions artifact:

```text
artifact id:      10344904119
artifact name:    staircase-band-exception-diagnostic
artifact digest:  sha256:7912587b4de8387107c8cd1c323fa38bc07dd8df2a9252a960240670123531fb
```

The raw diagnostic block frozen in the repository has

```text
sha256:c41e8eeaa4c00b13c25eb64ea698bb5e56afc7596090b0b977a9d9a44e2ec428
```

## Exact exceptional profile

The discrepancy occurs at

```text
state = 226
E     = 6
Q     = 47
```

with

```text
exact quotient target flow = 46
exact deficit              = 1
coarse band flow           = 39
coarse band demand         = 39
coarse band slack          = 0
canonical generators       = 2
```

So exact target Hall fails by one unit, while the deliberately relaxed staircase-band network is exactly saturated.

The six `(q,c,rho,P,n)` types are

```text
0: (0,1,1,3,7)   unselected
1: (2,4,2,4,1)   unselected
2: (2,5,3,5,3)   unselected
3: (4,6,2,2,1)   selected, band 0, generator
4: (5,9,4,4,1)   selected, band 1, generator
5: (6,9,3,3,5)   selected, band 1, non-generator
```

The staircase bands are therefore

```text
band 0: M=1, D=4,  generator type 3 = (q,c)=(4,6)
band 1: M=6, D=35, generator type 4 = (q,c)=(5,9)
```

## Where the coarse band relaxation loses information

For a selected source type `x` and target type `y`, exact directed compatibility requires

```text
q_x <= c_y + 1
q_y <= c_x.
```

Inside band 1, generator type 4 has `q=5,c=9`, whereas the five copies of non-generator type 5 have `q=6,c=9`.

Target type 1 has

```text
(q,c,P,n)=(2,4,4,1).
```

The generator is compatible with that target because

```text
5 <= 4+1.
```

But type 5 is not compatible because

```text
6 > 4+1.
```

Thus the coarse band model incorrectly gives all six band-1 source copies access to target type 1, although only the single generator copy actually has that access.

The diagnostic target table shows that this is the **only** capacity overestimate:

```text
target type   exact incoming   coarse-band incoming   overestimate
0                  0                    0                  0
1                  2                    7                  5
2                 21                   21                  0
3                  6                    6                  0
4                  6                    6                  0
5                 30                   30                  0
```

The five-unit error is exactly the five copies of type 5 which are represented by the easier band-1 generator when the coarse band network is built.

## Immediate refined-band consequence

This identifies a strictly stronger but still theorem-safe aggregation.

For each source band `i` and target type `sigma`, instead of giving the edge capacity implied by *all* source copies in band `i` whenever the generator is compatible with `sigma`, use the **actual number of selected source copies in that band which are individually compatible with `sigma`**, with the same self-deletion correction.

Exact target-flow feasibility still implies feasibility of this refined network: it is obtained by aggregating exact compatible source copies, not by inventing additional adjacencies.

For the state-226 exception, this changes only the band-1 to target-1 capacity, reducing it from `6` to `1`. Including the band-0 contribution, target type 1 then has at most `2` incoming incidences rather than `7`.

The resulting target-side effective capacities are bounded by

```text
target 1: min(4,  2) =  2
target 2: min(15,21) = 15
target 3: min(2,  6) =  2
target 4: min(4,  6) =  4
target 5: min(15,30) = 15
                           --
total                      38
```

against selected band demand

```text
D_0+D_1 = 4+35 = 39.
```

Hence this refined compatible-copy band relaxation rejects the unique exception by at least one unit.

Because the refined network only removes capacity from the already-verified coarse band relaxation, every one of the earlier `205,918` coarse-band failures remains a failure. Combining that monotonicity with this exact diagnostic gives the **derived frozen-pilot conclusion**:

```text
205,919 / 205,919 exact target-Hall failures
are detected by the refined compatible-copy band relaxation
on the same 15-state pilot.
```

This is an empirical/derived pilot result, **not yet an independently CI-audited all-profile theorem package**. The next required step is to formalize the compatible-copy band lemma, build an independent verifier, and replay it on the frozen pilot before elevating its status.

## Interpretation

The sole coarse-band miss does not require restoring full source-type identity. In this pilot it is explained entirely by one within-band demand-threshold distinction: a higher-`q` non-generator source loses a low-`c` target that its easier generator can still reach.

That materially strengthens the case for staircase-band theory. The next symbolic object should be a band flow whose edge capacities count genuinely compatible source copies, rather than the coarser generator-neighborhood multiplicity.

## Trust boundary

- No whole-state ledger count changes here.
- The canonical frontier remains `1,971 exclusions / 3,607 survivors` until the separate discovery/recovery/two-implementation promotion pipeline says otherwise.
- The `205,919/205,919` statement is about target-Hall-failing profiles in the frozen 15-state pilot only.
- External mathematical review and novelty assessment remain open.
