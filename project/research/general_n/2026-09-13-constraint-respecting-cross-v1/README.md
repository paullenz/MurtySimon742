# Constraint-respecting cross-neighbourhood pilot v1

13 September 2026. **Exploratory continuation, not a theorem package.** External mathematical review remains OPEN. No fixed-order ledger, general theorem, 7/12 threshold or whole-state frontier count is changed by this checkpoint.

## Why this continuation exists

The preceding fixed-neighbourhood flow package gave an exact conditional routing criterion once selected/residual cross-neighbourhoods are fixed. Its first deterministic probes were uninformative because they already failed minimum endpoint loads and some selected incidences had no compatible destination.

This continuation therefore tests the logically prior construction problem: can one choose cross-neighbourhoods that already satisfy the minimum load and exact destination-compatibility conditions before asking whether all obligations can be routed simultaneously?

The [plan](PLAN.md) reuses the same six frozen states from the previous pilot rather than selecting friendlier cases.

## Construction condition

For a fixed selected pattern `S_u`, the search chooses residual sets `R_u`, writes `N_u=S_u union R_u`, and requires:

- `|R_u|=rho_u` exactly and `S_u intersect R_u` empty;
- the selected pattern respects the canonical source eligibility/capacity rules used to construct it;
- for every selected incidence `(u,i)`, the minimum endpoint load `R_i+x_i>=q_u`;
- for every selected incidence `(u,i)`, at least one destination `v` with

      S_u \ N_v = {i},    S_v subset N_u.

A pattern passing these tests would then be sent to the exact flow/Hall checker from the preceding package. None of the bounded hard-compatibility samples below reached that stage.

## Observed bounded search

The preserved [observed-results record](OBSERVED_RESULTS.json) contains the exact sampling parameters and the evidential label used here.

Across exact-demand selected patterns (`x_i=s_i`):

| frozen state | randomized selected patterns | positive cross patterns found |
|---|---:|---:|
| N34 m289 state 60 | 1,000 | 0 |
| N34 m289 state 7896 | 100 | 0 |
| N34 m289 state 13537 | 100 | 0 |
| N35 m306 state 17 | 100 | 0 |
| N35 m306 state 246 | 100 | 0 |
| N35 m306 state 454 | 100 | 0 |

For N34 state 60, additional samples allowed each label a random small number of selected incidences above its demand lower bound. No positive pattern was found in 500 samples with at most one extra per label, 300 with at most two, or 200 with at most three.

**Important evidential limit:** the negative entries are solver-reported infeasibility of the residual/compatibility problem for each *fixed sampled selected pattern*. Under the project standing orders, an integer-solver infeasibility status is not a proof certificate. These runs do not exclude a sampled state, much less the whole 4,584-state frontier.

The all-at-once corrected state-60 MILP also reached its 30-second bound without an incumbent. That is recorded as OPEN, not negative evidence.

## Directly checkable positive information

A soft compatibility search produced the preserved [partial pattern](BEST_PARTIAL_PATTERN.json) for N34 state 60. It has all 37 exact-demand selected incidences, exact residual source degrees and no minimum endpoint-load violation. Direct checking finds:

- 19 of 37 selected obligations have a nonempty exact compatible-destination set;
- 18 remain empty;
- those 19 obligations have 20 eligible ordered pairs in total.

[`validate_partial.py`](validate_partial.py) recomputes these statements directly, without trusting the optimisation that found the pattern. The stored [validation output](PARTIAL_VALIDATION.json) lists every nonempty and empty obligation.

The number 19 is **not proved optimal**. Its value is diagnostic: compatibility responds materially to the selected-incidence geometry. A short local search moved from patterns with only a handful of compatible obligations to this 19/37 pattern, so the obstruction is not captured by the already-known scalar source sizes alone.

## Interpretation

This experiment improves the diagnosis of the next difficulty:

1. The previous deterministic residual placement was not the only problem. Many substantially different selected patterns also fail to admit residual sets giving every selected incidence an exact compatible destination.
2. On the other hand, selected-pattern changes can more than double the number of obligations with compatible destinations. This argues against treating the negative samples as evidence of a simple universal scalar contradiction.
3. The useful next object is therefore the **overlap geometry** of selected sets and cross-neighbourhoods: an eligible pair `u->v` requires the near-containment `|S_u intersect N_v|=q_u-1` together with `S_v subset N_u`.

The next theoretical step is to count or bound how many such near-containments can coexist given the label degrees `x_i`, residual degrees `R_i`, source sizes `q_u,rho_u` and the receiver capacities. A profile-level bound on the union of compatible destination sets could turn the fixed-neighbourhood Hall theorem into a genuine parameter-uniform exclusion.

## Reproduction

SciPy/NumPy are needed only for exploratory search:

```sh
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/run_fixed_selected_search.py --quick --output QUICK_RESULTS.json
```

The full default sampling schedule mirrors the preserved observed-run parameters but may be slow and is not promoted as proof evidence. The positive partial witness requires only the Python standard library:

```sh
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/validate_partial.py
```

## Status

- whole-state exclusions added: **0**;
- compatible-routing/generalisation frontier: unchanged at **994 exclusions / 4,584 survivors**;
- fixed-order candidate proofs N34/N35: unchanged and already closed by their own packages;
- useful new evidence: a corrected construction model, broad but non-proof negative sampling, and a directly validated 19/37 partial compatibility pattern;
- next target: a hand/profile inequality for compatible-destination overlap or a genuinely compatible complete cross pattern to feed into the exact Hall flow.
