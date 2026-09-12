# Constraint-respecting cross-neighbourhood pilot v1

13 September 2026. **Exploratory continuation plus candidate general hand lemmas.** External mathematical review and novelty assessment remain OPEN. No fixed-order ledger, 7/12 threshold or whole-state frontier count is changed by this checkpoint.

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

## General theory extracted from the failures

The [co-singleton trace and receiver-containment spill note](CONTAINMENT_SPILL.md) extracts two candidate hand lemmas from exact destination compatibility.

For each source `u`, the actual exceptions of its selected labels force the cross-neighbourhood traces on `S_u` to contain every co-singleton `S_u-{i}`. Consequently every `k`-subset `T` of `S_u` has at least `q_u-k+1` common B-neighbours. Double counting gives the moment hierarchy

```text
sum_(|T|=k) max({q_u-k+1:T subset S_u} union {0})
    <= sum_v binom(q_v+rho_v,k).
```

The `k=1` case is only endpoint-load information, while `k>=2` retains higher-order overlap. A five-label/seven-source abstract example passes every individual endpoint load but violates the pair moment (`16<18`), so the higher-order trace is genuinely additional information.

More importantly for projection, the exact receiver condition `S_v subset N_u` yields a **receiver-containment spill inequality** depending only on `(a,b,s,rho,q)`. It compares a lower bound on selected mass forced outside `N_u` with the maximum outside mass that can be packed into sources not needed as contained compatible receivers. For each source it also retains the scalar receiver requirements `q_v+rho_v>=q_u-1`, `q_v<=q_u+rho_u` and positive incoming capacity.

A standard-library deterministic reconnaissance check of 2,000 exact-demand selected patterns per frozen state finds violations in **173/2,000** patterns for N34 m289 state 13537 (183 source-level violations) and zero in the other five samples. This does not exclude state 13537; it demonstrates that the new projected inequality can remove selected-degree configurations before residual placement. See [`check_containment_spill.py`](check_containment_spill.py) and [`CONTAINMENT_SPILL_CHECK.json`](CONTAINMENT_SPILL_CHECK.json).

## Interpretation

The work sharpens the diagnosis in two directions:

1. The previous deterministic residual placement was not the only problem. Many substantially different selected patterns also fail to admit residual sets giving every selected incidence an exact compatible destination.
2. Selected-pattern changes can materially increase compatible-destination availability, so the obstruction is not captured by scalar source sizes alone.
3. Exact compatibility contains a higher-order co-singleton design condition.
4. Part of the receiver-containment condition can nevertheless be projected back to the scalar selected-degree profile through the spill inequality.

The next high-value test is therefore **complete**, not random: add the spill inequality to the preserved compatible-routing `q`/source-option domain and determine by exact arithmetic whether it removes any of the 4,584 generalisation survivors or strengthens the closed potential. If it does, inspect the first witnesses for a simpler demand/tail consequence; if it does not, preserve the limit.

## Reproduction

SciPy/NumPy are needed only for exploratory fixed-pattern search:

```sh
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/run_fixed_selected_search.py --quick --output QUICK_RESULTS.json
```

The full default sampling schedule mirrors the preserved observed-run parameters but may be slow and is not promoted as proof evidence. The positive partial witness and the new spill checker require only the Python standard library:

```sh
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/validate_partial.py
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/check_containment_spill.py
```

## Status

- whole-state exclusions added: **0**;
- compatible-routing/generalisation frontier: unchanged at **994 exclusions / 4,584 survivors**;
- fixed-order candidate proofs N34/N35: unchanged and already closed by their own packages;
- candidate new general mathematics: co-singleton trace/moment hierarchy and receiver-containment spill inequality;
- bounded evidence: broad non-proof negative sampling, a directly validated 19/37 partial pattern, and 173/2,000 spill violations in one frozen stratum;
- next target: exact full-domain application of the spill inequality.
