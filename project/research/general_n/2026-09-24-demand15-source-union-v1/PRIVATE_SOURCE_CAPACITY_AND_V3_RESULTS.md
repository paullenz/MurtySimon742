# Private-source capacity and right-budget diagnostics

24 September 2026. Status: proved internal graph-level lemma at the assigned-certificate interface, plus a corrected necessary-condition model. Neither is a complete realizability theorem.

## Private-source antichain lemma

Fix a right endpoint t of the assigned-witness graph and let I_t be its incident labels. Each incidence i--t uses a physical edge u_i t assigned to i, with N(i) intersect N(t)={u_i}. Since a physical edge is assigned only once, the sources u_i are distinct. If u_i belonged to C_j=N(j) intersect B for j different from i, then u_i and u_j would be two distinct common neighbours of j and t. Therefore

    u_i belongs to C_i minus union_{j in I_t, j!=i} C_j.

Consequently every C_i has a private point within the incident family. In particular, two labels sharing an assigned endpoint have incomparable B-neighbourhoods.

## Repeated common-endpoint capacity

For any label set J, let R_J be the assigned right endpoints incident with every i in J, and put

    P_i(J)=C_i minus union_{j in J, j!=i} C_j.

For fixed i and u in P_i(J), every t in R_J that uses u as i's source is adjacent to u. The vertex u is already adjacent to the root and to i, so it can source at most d(u)-2 such endpoints. Hence

    |R_J| <= min_{i in J} sum_{u in P_i(J)} (d(u)-2)
           <= (Delta-2) min_{i in J}|P_i(J)|.

This simultaneously generalizes the single-label source-capacity bound and records the neighbourhood-antichain obstruction lost by scalar profiles.

## Regression

A checker reconstructed every locally compatible common-endpoint family of up to eight labels on 575 independently edge-certified D2C graphs, 921 maximum-degree roots, including balanced complete-bipartite controls of both parities and X3.

- label subsets inspected: 2,685,701
- nonempty common-endpoint families: 6,245
- common endpoints: 6,944
- containment with a common endpoint: 0
- degree-capacity violations: 0
- coarse-capacity violations: 0
- exact degree-capacity equalities: 80
- maximum common endpoints for one label family: 5

The exact degree-capacity bound is sharp in the corpus; no +1 strengthening is asserted.

## Corrected right-vertex budget

The aggregated witness model was also corrected with the necessary constraint

    sum_{J,z} n_{J,z} <= Delta,

because each nonzero pattern copy is one physical endpoint in B. This changes some optimizer geometries but not the minimum deficits of the five audited leading n=18 profiles. The dense (8,7) and (5,5,5) survivors therefore remain open at this abstraction level.

With both the source-union floor and right-vertex budget, exact bounded replays found no survivors in n=16, Delta=9 scalar ranges 201--3,200. The initially attempted range 1--200 ended without a FINAL record, so no prefix-closure claim is made. The closest certified gaps within the later shards were at least +3 over the deficit allowance. Full row closure remains open.

## Handoff

The new antichain/private-source capacity is actual graph geometry not present in the scalar witness model. The next useful step is to add explicit C_i set-overlap/private-source variables to the demand-15/16 realizability model, or use incomparability directly on the leading dense survivor geometries. Merely extending scalar shards will not turn abstract feasibility into a graph theorem.
