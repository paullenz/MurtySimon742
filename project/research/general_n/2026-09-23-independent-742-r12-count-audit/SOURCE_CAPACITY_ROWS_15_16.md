# Graph-source capacity and corrected witness screens for (15,8) and (16,9)

Status: internally verified necessary-condition screen; not external acceptance and not a substitute for graph realizability.

## Source-capacity lemma

For a maximum-degree root v and an assigned label i, let h_i be its height and x_i the number of assigned witnesses. The label has exactly Delta-h_i vertices in its B-source set. Every such source is already adjacent to v and to i, so its degree bound leaves at most Delta-2 incident assigned B-edges carrying label i. Hence

    h_i < Delta,     x_i <= (Delta-h_i)(Delta-2)

whenever x_i>0. This is a graph-level necessary condition missing from the initial abstract screen.

## Exact results

- n=15, Delta=8: 14,413 symmetry-reduced demand/witness patterns enumerated; zero pass the corrected compressed scalar filter.
- n=16, Delta=9: 14,413 patterns enumerated; 7,008 pass the corrected scalar filter; every one is infeasible in the exact aggregated incidence-pattern MILP with total deficit at most Dmax=14.
- Closest n=16 pattern: d=(7,7,1), x=(7,7,1), h=(7,7,1). Its exact minimum deficit is 15, one above Dmax.

The earlier apparent n=16 survivors with h_i=Delta or insufficient source capacity were artifacts of abstract profile feasibility and are not graph-realizable.

## Scope

The screen is exhaustive for the demand-15/16 normal-form interface and the encoded necessary conditions. It does not prove that every abstract feasible point comes from a D2C graph, and it does not widen equality beyond the existing S<=8 control.
