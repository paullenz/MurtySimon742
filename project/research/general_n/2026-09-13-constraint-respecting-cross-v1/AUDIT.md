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

## Sampling limits

The randomized selected patterns are not uniform samples from all admissible selected-set families. They are generated label by label, hardest demand first, with a load-balancing random score. The extra-selected runs add an independently random number of incidences per label up to a small cap.

Consequently the absence of a positive complete cross pattern is not a probability estimate for existence, and the raw sample count is not a measure of distance to a whole-state exclusion. The result is best used to guide structural theory and better search design.

## Structural lesson retained

The directly validated partial witness shows that compatible-destination availability can change substantially while the scalar profile `(a,b,s,rho)` remains fixed. This reinforces the need to retain selected-set overlap information.

For any eligible ordered pair `u->v` the exact condition gives

    |S_u intersect N_v| = q_u-1

and identifies the unique missing selected label. In addition `S_v subset N_u`. These simultaneous near-containments are the natural next object to count. Any proposed profile-level inequality must be proved from the canonical graph bridge rather than inferred from sample frequency.

## Preservation check

This checkpoint preserves the plan, observed-run parameters and outcomes, the positive partial pattern, its direct validator and the exploratory sampler. It does not replace or modify the preceding fixed-neighbourhood flow proof, fixed-order ledgers, 7/12 candidate, forecast or reviewer packages.
