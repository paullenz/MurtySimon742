# Constraint-respecting cross-neighbourhood pilot — plan

13 September 2026. Exploratory continuation of the fixed-neighbourhood routing-flow work. External mathematical review remains OPEN.

## Motivation

The preceding arc-realisation pilot constructed fixed cross patterns and then applied the exact routing-flow test. All twelve deterministic probes failed, but every probe already violated a minimum endpoint-load inequality and some selected incidences had no compatible destination. Those failures therefore supplied no evidence beyond the earlier load framework.

The next experiment should reverse that order: do not ask a routing question until the cross pattern has already passed the logically prior checks that made the earlier probes trivial.

## Frozen sample

Reuse the same six states frozen before the previous pilot:

- N34 m289 states 60, 7896 and 13537;
- N35 m306 states 17, 246 and 454.

This is deliberately not a resampling exercise. The purpose is to compare a corrected construction method on the same heterogeneous sample.

## Construction stage

For a fixed selected-incidence pattern `S_u`, search for residual sets `R_u` satisfying:

1. `|R_u|=rho_u` exactly;
2. `S_u` and `R_u` are disjoint;
3. the selected-label demand/source eligibility rules used by the canonical bridge;
4. the minimum endpoint-load condition `R_i+x_i >= q_u` for every selected incidence `(u,i)`;
5. every selected incidence has at least one destination `v` satisfying the exact fixed-neighbourhood compatibility conditions

       S_u \ N_v = {i},    S_v subset N_u,

   where `N_u=S_u union R_u`.

Only a pattern passing these conditions is eligible for the next routing-flow stage. The actual incoming term `p_u` is not known before routing; successful exact routing supplies the stronger endpoint statement in the fixed-neighbourhood theorem.

## Selected-pattern search

Start with exact-demand patterns (`x_i=s_i`) because they are the smallest chosen-incidence realisations and make the obstruction easiest to interpret. Sample randomized load-balanced placements while preserving source eligibility and capacity. For N34 state 60 also sample patterns with modest extra selected incidences above the demand lower bounds.

A failure for a fixed `S` is only a failure of that fixed selected pattern. Even an exhaustive residual search for one `S` does not exclude the whole state. A solver infeasibility status is not a proof certificate under the project standing orders.

## Positive and negative evidence

- A **positive cross pattern** is useful evidence and can be checked directly from its `S_u,R_u` sets.
- A solver-reported infeasible fixed-`S` residual problem is preserved as exploratory negative evidence only.
- A time limit or absence of an incumbent is OPEN, not infeasible.
- No whole-state exclusion is permitted without a complete quantified search over all admissible selected and residual patterns, with proof-producing/checkable evidence.

## Follow-through

If compatible cross patterns are found, apply the exact integer-flow/Hall criterion from the preceding package and inspect either the successful routing or a genuine Hall-deficient obligation set.

If many varied selected patterns fail before routing, use their structure to seek a profile-level or overlap-level necessary inequality. The target is a hand lemma that removes cross-neighbourhood variables, not a larger solver budget.
