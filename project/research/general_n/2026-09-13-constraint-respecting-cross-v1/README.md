# Constraint-respecting cross-neighbourhood pilot v1

13 September 2026. **Exploratory continuation plus candidate general hand lemmas and an exact full-domain negative application result.** External mathematical review and novelty assessment remain OPEN. No fixed-order ledger, 7/12 threshold or whole-state frontier count is changed by this checkpoint.

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

A standard-library deterministic reconnaissance check of 2,000 exact-demand selected patterns per frozen state found violations in **173/2,000** patterns for N34 m289 state 13537 (183 source-level violations) and zero in the other five samples. That was useful for discovering the inequality but was not evidence of a whole-state exclusion.

## Exact full-domain spill application: zero whole-state exclusions

The reconnaissance was followed by a complete positive-witness study over all **4,584 combined compatible-routing survivors**. The aim was deliberately constructive: a single directly checkable witness is enough to show that the spill inequality, together with the selected-degree/transport conditions checked here, does **not** eliminate that state.

[`assemble_exact_spill_witness.py`](assemble_exact_spill_witness.py) and the preserved [`FULL_DOMAIN_SPILL_EXACT.json`](FULL_DOMAIN_SPILL_EXACT.json) give one witness for every survivor with the stronger choice

```text
x_i = s_i  for every label i.
```

Each witness directly checks:

- exact selected label degrees `x=s`;
- source eligibility `rho_u>=s_i` for every selected incidence;
- source selected-degree capacity `q_u<=a-rho_u`;
- total selected/incoming balance;
- every preserved nested transport-tail inequality;
- the scalar candidate-receiver count;
- the receiver-containment spill inequality at every source.

The complete result is:

```text
combined survivors checked                    4,584
exact-demand witnesses found                  4,584
unresolved                                        0
whole-state exclusions added                      0
minimum candidate-receiver margin                 0
minimum spill slack                               0
```

The generation route was 4,484 first-pass exact witnesses, 98 deeper exact-demand search witnesses and two deterministic boundary exact-demand witnesses. All final witnesses are rechecked from their stored selected sets and degree data; no solver infeasibility result is used to establish the zero-gain conclusion.

This is an exact **limit result for the scalar spill projection**, not a feasibility result for the original graph problem. The witnesses do not construct residual sets, exact compatible destinations, heavy-H data or the final Hall routing. A state can therefore survive this projection and still fail much later set-level conditions.

The full-domain result also corrects the impression one might get from the `173/2,000` reconnaissance count: sampled selected-degree configurations can fail the spill inequality while every whole state still has another selected-degree configuration that passes it. Sample frequency must not be extrapolated into whole-state reach.

## Interpretation

The work now sharpens the diagnosis more decisively:

1. Exact compatibility contains genuinely higher-order information: the co-singleton trace hierarchy is not reducible to individual endpoint loads.
2. The receiver-containment spill inequality successfully projects part of that information to `(a,b,s,rho,q)` and can remove individual selected-degree configurations.
3. **That scalar projection is exhausted at the current whole-state frontier:** every one of the 4,584 survivors has an exact-demand witness passing it.
4. The remaining information therefore lies in the actual set geometry—simultaneous co-singleton traces, residual placements and exact receiver containment—not in this scalar spill bound alone.

The next high-value target is the first genuinely set-level projection. The natural starting point is the `k=2` co-singleton/pair-overlap condition: count how the `q_u` distinct exception rows must simultaneously realize `q_u-1` traces of every selected pair, and compare that requirement with the selected/residual pair capacity available across B. Any resulting inequality should be tested on complete preserved domains and separated carefully from raw solver infeasibility.

## Reproduction

SciPy/NumPy are needed only for exploratory fixed-pattern search:

```sh
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/run_fixed_selected_search.py --quick --output QUICK_RESULTS.json
```

The positive partial witness and the local spill reconnaissance require only the Python standard library:

```sh
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/validate_partial.py
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/check_containment_spill.py
```

The complete exact-demand witness assembly is also deterministic/checkable from the preserved catalogue evidence:

```sh
python project/research/general_n/2026-09-13-constraint-respecting-cross-v1/assemble_exact_spill_witness.py
```

## Status

- whole-state exclusions added by spill: **0**;
- compatible-routing/generalisation frontier: unchanged at **994 exclusions / 4,584 survivors**;
- fixed-order candidate proofs N34/N35: unchanged and already closed by their own packages;
- candidate new general mathematics: co-singleton trace/moment hierarchy and receiver-containment spill inequality;
- exact limit: **all 4,584 survivors admit exact-demand selected/transport/spill witnesses**;
- next target: pair/higher-order set-overlap projection and residual-compatible construction, not further scalar spill tuning.
