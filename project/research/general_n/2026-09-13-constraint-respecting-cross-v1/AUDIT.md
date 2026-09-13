# Audit and scope limits — constraint-respecting cross pilot v1

13 September 2026. Internal same-assistant audit. External mathematical review and independent reproduction remain OPEN.

## What changed from the previous pilot

The earlier deterministic fixed-cross probes were rejected for reasons that preceded the new flow theorem: some selected incidences had no compatible destination and every probe violated a minimum endpoint-load inequality. This continuation moves those requirements into the construction stage.

For fixed selected sets `S_u`, a witness destination for `(u,i)` is permitted only when the exact theorem-level conditions hold:

    S_u \ N_v = {i},    S_v subset N_u.

The residual search additionally fixes every source residual degree and enforces `R_i+x_i>=q_u` on every selected incidence. Thus a positive pattern cannot reproduce the specific trivial defects of the previous deterministic probes.

## Encoding review

For a witness binary variable `w_(u,i,v)`:

- if label `i` is selected at `v`, `w` is forced to zero;
- otherwise `w=1` forces residual absence of `i` at `v`;
- for every `j in S_u-{i}` not already selected at `v`, `w=1` forces residual presence of `j` at `v`;
- for every `j in S_v` not already selected at `u`, `w=1` forces residual presence of `j` at `u`.

These clauses are exactly the two set conditions above after `S` is fixed. The direct positive-pattern decoder rechecks them as sets rather than trusting the linear rows.

The minimum endpoint row is deliberately only `R_i+x_i>=q_u`, because the incoming selected-pair count `p_u` is not known before routing. A successful exact fixed-neighbourhood routing would imply the stronger endpoint-load statement with `p_u` by the preceding theorem. The construction search does not claim otherwise.

## Negative evidence is not proof

The fixed-`S` residual problem is a binary integer feasibility problem. The observed negative samples returned the solver's infeasible status. The project standing orders explicitly prohibit treating an UNSAT/infeasible exit status as a proof certificate.

Therefore:

- no individual negative sample is promoted to theorem evidence;
- no selected pattern is declared mathematically impossible solely from the stored solver status;
- no state is excluded;
- the 4,584-state generalisation frontier is unchanged.

A time-limited all-at-once corrected MILP for N34 state 60 returned no incumbent. It remains OPEN and is recorded separately rather than mixed with the solver-infeasible fixed-pattern counts.

## Positive evidence is directly checkable

`BEST_PARTIAL_PATTERN.json` does not depend on trusting the optimiser for its stated properties. `validate_partial.py` reconstructs `S_u,R_u,N_u`, label selected and residual degrees, minimum endpoint loads and every exact destination set.

It confirms 19 obligations with a nonempty compatible-destination set, 18 with an empty set and 20 eligible ordered pairs. It also confirms the exact-demand vector and source residual sequence. The search that found this pattern does not prove that 19 is maximal.

## Sampling limits and the later correction

The randomized selected patterns are not uniform samples from all admissible selected-set families. They are generated label by label, hardest demand first, with a load-balancing random score. The extra-selected runs add an independently random number of incidences per label up to a small cap.

The reconnaissance spill checker later found 173/2,000 selected patterns failing the scalar spill inequality in one frozen N34 stratum. This was useful discovery evidence but never a whole-state exclusion. The complete positive-witness study now makes that distinction concrete: **all 4,584 combined survivors possess another exact-demand selected configuration that passes the spill and transport conditions.**

Thus the sampled failure rate is not a probability estimate for whole-state failure and must not be extrapolated. This correction is intentionally preserved because it is a useful example of why the project distinguishes configuration-level reconnaissance from complete state coverage.

## Exact full-domain positive-witness check

`assemble_exact_spill_witness.py` reads the preserved combined survivor set and constructs one selected-pattern witness for every survivor with `x_i=s_i` exactly. `FULL_DOMAIN_SPILL_EXACT.json` stores all 4,584 final witnesses.

For each witness the checker independently reconstructs and verifies:

1. the selected sets and source selected degrees `q_u`;
2. exact label selected degrees `x_i=s_i`;
3. source eligibility `rho_u>=s_i` for every selected incidence;
4. source capacity `q_u<=a-rho_u`;
5. the incoming-degree vector `p`, total balance and every nested transport-tail inequality;
6. candidate receiver counts required by the scalar containment projection;
7. the receiver-containment spill inequality source by source.

The final complete counts are:

```text
witnessed                   4,584
unresolved                      0
all exact-demand             true
whole-state exclusions added    0
minimum receiver margin          0
minimum spill slack              0
```

The final witness generation used 4,484 first-pass witnesses, 98 deeper search witnesses and two deterministic boundary exact-demand constructions. The search route is not proof-critical to the zero-gain claim because every saved final witness is checked directly.

The two deterministic boundary constructions were added after randomized/local search had difficulty with highly nonuniform selected-source degrees. This corrects an intermediate exploratory impression that extra selected incidences might be required. They are not: the final full-domain record has `x=s` for every state.

## Scope of the full-domain zero-gain result

A positive spill witness proves only that the following conjunction of necessary conditions does not exclude the state:

- exact demand selected degrees;
- selected-source eligibility/capacity;
- selected/incoming balance;
- the preserved nested transport inequalities;
- scalar candidate-receiver counts;
- receiver-containment spill.

It does **not** construct residual sets, verify the exact set equalities `S_u\N_v={i}`, realize `S_v subset N_u` for every actual exception, impose the full heavy-H catalogue data, route selected obligations by Hall flow, construct `H[A]`, or build a diameter-two edge-critical graph. The result is therefore a limit of this scalar projection, not evidence that any of the 4,584 states is graph-feasible.

## Workflow/preservation correction

The first full-domain workflow piped the Python process through `tee` without `pipefail`, so a partial search exit code was masked and its explicitly scoped 4,484/100 partial JSON was committed. The file correctly labels the 100 unresolved states and makes no complete claim, so it remains valid historical evidence. The workflow was hardened before subsequent use.

A later refinement workflow generated additional evidence but its automatic push lost a race with another main-branch update. The output was recovered from the immutable workflow artifact and then superseded by the stronger complete exact-demand run. The final exact-demand workflow completed successfully and committed `FULL_DOMAIN_SPILL_EXACT.json` to `main`.

These operational events do not alter the mathematics but are retained because publication/preservation failures are part of the audit trail.

## Structural lesson retained

The directly validated partial witness shows that compatible-destination availability can change substantially while the scalar profile `(a,b,s,rho)` remains fixed. The complete spill result now goes further: scalar `(a,b,s,rho,q)` information is still insufficient to remove any of the 4,584 surviving states.

For any eligible ordered pair `u->v` the exact condition gives

    |S_u intersect N_v| = q_u-1

and identifies the unique missing selected label. In addition `S_v subset N_u`. Across the `q_u` distinct exceptions of one source, these force a complete family of co-singleton traces. The next useful constraint must therefore retain **which labels overlap**, not merely how many selected labels each source has.

The most natural next target is the pair (`k=2`) member of the co-singleton hierarchy, followed by residual-compatible realization and exact Hall routing. Any proposed pair-overlap inequality must be proved from the canonical bridge and tested on complete preserved domains rather than inferred from sampled failure frequency.

## Preservation check

This checkpoint preserves the plan, observed-run parameters and outcomes, the positive partial pattern, its direct validator, the exploratory sampler, the co-singleton/spill hand derivation, deterministic reconnaissance, the complete exact-demand witness generator and all 4,584 final witnesses. It does not replace or modify the preceding fixed-neighbourhood flow proof, fixed-order ledgers, 7/12 candidate, forecast or reviewer packages.
