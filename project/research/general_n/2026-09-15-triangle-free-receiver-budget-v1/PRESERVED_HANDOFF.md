# Murty–Simon / Erdős #742 — live current state

> Operational source of truth. Read this file first on resumption. README's current-status overview and tables are now first; routine WIP results may be newer here.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_PROOF_NOT_PROMOTED`. One bounded mathematical unit after the user-requested README repair: extend the extra-selection budget to |M|<3d using the triangle-free auxiliary graph.

**WORK MODE:** `MATH`. README repair was published at 03aba3e5070661052b591450a6c924b132fee305 and remotely checked before mathematics resumed. No further README changes, download repairs, workflow launches or polling in this mathematical unit.

**INSPECTED PREDECESSOR:** `03aba3e5070661052b591450a6c924b132fee305` on main, checked immediately before this write. Its layout repair and preservation links remain intact.

**LAST VERIFIED RESULT:** internally derived conditional corollary: under the full canonical tight-block assumptions |T|=|H|=d, if |M|<3d then the disjoint-receiver auxiliary graph Gamma is triangle-free and E=sum_H(|S_u|-d)<=floor(d^2/4). Thus the previous |M|=2d extra-selection budget extends to 2d<|M|<3d. The elementary triangle-free inequality is standard, proved below; no novelty is claimed for that inequality. The application inherits the previously recorded disjoint-destination lemma. A five-set example at d=5, |M|=13 gives Gamma=C5, demonstrating that the auxiliary graph need not remain bipartite. It is not a graph-realization counterexample.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. Prior 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. Equality catalogue replay remains NOT_RUN in this session. No new state IDs or catalogue exclusions. External mathematical review remains OPEN; this is the same assistant's internal reasoning.

**CHECKS:** local elementary auxiliary-graph checks passed for all 6,228 triangle-free labelled graphs on 1 through 6 vertices, with the explicit five-cycle set-family control. These are not enumerations of original diameter-two edge-critical graphs, nor catalogue replay. Full code and exact result counts are below.

**ACTIVE / PENDING:** catalogue application and original equality replay remain pending; state 3349 enumeration remains unresolved. Triangle-freeness alone gives an edge budget, not high-source rigidity or bipartiteness. At |M|=3d the present triangle-free argument need not apply.

**UNPRESERVED WORK:** `None` after publication: the complete conditional proof, negative control, runnable finite-check code and results are recorded below. Earlier mathematical evidence and README history remain preserved at stable paths and immutable commits.

**DEFERRED ADMIN:** large-input transfer, automatic workflow-completion reporting and unrelated CI/maintenance. Do not retry the previously failed direct-download route. Keep the README's current-status overview and tables before dated notes.

**NEXT ACTION:** one bounded symbolic unit connecting the extra-selection budget E to forced residual-label demand when high sources may have extra selections. Seek a necessary inequality rather than assuming the rigid-case residual-union argument remains valid. Preserve the first result or failure before further work; keep catalogue scanning separate.

**PROCESS RULE:** RESEARCH_EXECUTION_POLICY_V3. Bounded work, immediate preservation and one remote confirmation. Pause/stop overrides further work or housekeeping. No work is claimed to continue after a response ends.
<!-- CURRENT-STATUS:END -->

## Sources and preserved work

- [Disjoint-destination lemma D1-D3 and |M|=2d boundary proof](../2026-09-15-disjoint-receiver-boundary-v1/PRESERVED_HANDOFF.md).
- [Multi-spare rigidity and residual-union proof](../2026-09-15-spare-receiver-rigidity-v1/PRESERVED_HANDOFF.md).
- [Canonical selected/residual bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
- [README layout checkpoint and preservation record](https://github.com/paullenz/MurtySimon742/blob/03aba3e5070661052b591450a6c924b132fee305/CURRENT_STATE.md).
- [Complete original README before layout repair](../../../../archive/status-snapshots/2026-09-15/README_before_status_first.md).
- [One-spare review](https://github.com/paullenz/MurtySimon742/blob/43dc689300eb20efa30e2b848a5326f3c5dcbd6f/CURRENT_STATE.md).
- [Original candidate and transport history](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/CURRENT_STATE.md).

## Triangle-free disjoint-receiver budget — internal conditional proof

### Hypotheses and inherited restriction

Use the actual full selected-representative system, not demand-thinned subsets or independently chosen numerical routings. At each B-vertex u, N_u is the disjoint union of S_u and R_u with |R_u|=rho_u. Every label i is selected at at least s_i distinct sources; selecting i at u requires s_i<=rho_u. Each selected label has a distinct destination at its source; opposite orientations cannot represent the same unordered missing B-pair. For an actual selected obligation (u,i)->v, i is absent from N_v, S_u minus {i} is contained in N_v, and S_v is contained in N_u. The last containment is justified by quasi-edge domination and unique selected orientation in the preceding review.

Let d>=1, T={i:s_i=d}, H={u:rho_u>=d}, M={v:rho_v=d-1}; assume |T|=|H|=d. All high sources select T. Each has d distinct T-destinations D_u contained in M, so every realizable system has |M|>=d. A used receiver's residual set is exactly T minus its received label.

Define Gamma on the d distinct vertices of H by uw being an edge precisely when D_u and D_w are disjoint. Repeated destination-set types are allowed. Put E=sum_{u in H}(|S_u|-d).

The preserved disjoint-destination proof establishes E<=e(Gamma). Briefly, an extra label j at u cannot go outside H because its receiver would need all d T-labels residually despite fewer than d residual slots. If its high destination w shared a T-receiver v with u, then j would be selected at v (its residual set is within T), and reverse containment from w to v would force j into N_w, contrary to j being absent at its destination. Thus extra obligations use disjoint high pairs. Distinct destinations and unique orientations inject them into unordered Gamma edges. In an actual underlying graph G, the full representative property also gives E=e(G[H]) and G[H] contained in Gamma.

### Claim

If |M|<3d, then

    E <= floor(d^2/4),
    sum_{u in H} q_u <= d^2+floor(d^2/4).

For an actual G, G[H] is triangle-free. Bipartiteness is not asserted in the range 2d<|M|<3d.

### Proof

A triangle u,w,z in Gamma would give three pairwise disjoint d-element sets D_u,D_w,D_z inside M. Their union has 3d elements, contradicting |M|<3d. Hence Gamma is triangle-free.

Write e=e(Gamma) and a_u=deg_Gamma(u). For each edge uw, its endpoints have no common neighbour, so their open neighbourhoods are disjoint and a_u+a_w<=d. Summing over edges gives

    sum_u a_u^2 = sum_{uw in E(Gamma)}(a_u+a_w) <= d e.

Also sum_u a_u=2e and the nonnegativity of the sum of squared deviations from the mean yields

    (2e)^2 <= d sum_u a_u^2 <= d^2 e.

If e=0 the conclusion is immediate. Otherwise divide by e to obtain e<=d^2/4. Since e is an integer, E<=e<=floor(d^2/4). Adding the d tight selections at each of d high sources gives the claimed q sum. The statement about G[H] follows from containment in Gamma.

For |M|<2d the stronger already-proved result is E=0. At |M|=2d the complement-pair argument additionally proves bipartiteness. The present corollary preserves the same numerical upper bound beyond that boundary without claiming that stronger structure survives.

### Negative control: triangle-free does not mean bipartite

Take d=5, M={0,...,12} and the five sets

    D0={0,1,2,8,9}
    D1={3,4,5,10,11}
    D2={0,1,2,6,7}
    D3={3,4,5,8,9}
    D4={6,7,10,11,12}.

Each has size 5 and 10<|M|=13<15. Their disjointness edges are exactly 01,12,23,34,40, forming an odd cycle C5. Thus Gamma need not be bipartite in the extended range. This is an abstract set-family counterexample to an overstrong intermediate assertion, NOT a claimed realization of the canonical selected system or a counterexample to Murty–Simon. Its five edges satisfy the bound floor(25/4)=6.

### Scope

The proof is conditional on the existing canonical bridge and actual selected representatives. The classical triangle-free edge inequality is not a new theorem. The contribution of this unit is its explicit application to the saved disjoint-receiver reduction and the corrected structural limit. No catalogue input has been fetched, no baseline replay has run, and no new canonical closure is inferred.

## Runnable elementary checks

This exact Python program was run locally. Source SHA256: a756dc0734f48f5d72d80d746c8cb291569fc6064dc28b7e4f81231585eb413d.

```python
#!/usr/bin/env python3
"""Check the elementary triangle-free edge bound and a non-bipartite set control.
Not a catalogue replay or an enumeration of original Murty-Simon graphs.
"""
from itertools import combinations
import json

rows = []
for n in range(1, 7):
    pairs = list(combinations(range(n), 2))
    checked = maximum = 0
    for mask in range(1 << len(pairs)):
        adj = [0] * n
        edges = []
        for bit, (u, v) in enumerate(pairs):
            if (mask >> bit) & 1:
                edges.append((u, v))
                adj[u] |= 1 << v
                adj[v] |= 1 << u
        if any(adj[u] & adj[v] for u, v in edges):
            continue
        deg = [a.bit_count() for a in adj]
        e = len(edges)
        assert sum(x*x for x in deg) <= n*e
        assert (2*e)**2 <= n*sum(x*x for x in deg)
        assert e <= n*n//4
        maximum = max(maximum, e)
        checked += 1
    assert maximum == n*n//4
    rows.append(dict(n=n, triangle_free_auxiliary_graphs=checked, max_edges=maximum))

sets = [{0,1,2,8,9}, {3,4,5,10,11}, {0,1,2,6,7},
        {3,4,5,8,9}, {6,7,10,11,12}]
assert all(len(x)==5 for x in sets)
assert len(set().union(*sets)) == 13
edges = [(u,v) for u,v in combinations(range(5),2)
         if sets[u].isdisjoint(sets[v])]
assert edges == [(0,1),(0,4),(1,2),(2,3),(3,4)]
print(json.dumps(dict(status="PASS_ELEMENTARY_AUXILIARY_CHECKS_ONLY",
    rows=rows, total_triangle_free_auxiliary_graphs=sum(
        r["triangle_free_auxiliary_graphs"] for r in rows),
    odd_cycle_control={"d":5,"receiver_count":13,"edges":edges},
    catalogue_replay="NOT_RUN",
    original_graph_realizability="NOT_ASSERTED"), indent=2))
```

Recorded result: PASS_ELEMENTARY_AUXILIARY_CHECKS_ONLY. Exact rows (n, triangle-free auxiliary graphs, maximum edges) are (1,1,0), (2,2,1), (3,7,2), (4,41,4), (5,388,6), (6,5789,9), total 6,228. The five-cycle control passed with d=5, receiver_count=13 and edges [(0,1),(0,4),(1,2),(2,3),(3,4)]. Catalogue replay: NOT_RUN. Original graph realizability: NOT_ASSERTED.
