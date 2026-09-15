# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff remains at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_PROOF_NOT_PROMOTED`. Third bounded mathematical unit: a general disjoint-destination restriction for extra high-source selections, and a quadratic extra-selection budget at |M|=2d. Full proof and finite set-family checks are below; external review remains OPEN.

**WORK MODE:** `MATH`. User-authorized autonomous prioritization. The preceding mathematical checkpoint was published and remotely confirmed. No failed-download retries, CI polling, workflow launches/cancellations or unrelated repository maintenance were performed.

**INSPECTED PREDECESSOR:** `57a1a2b48637763a4b09ce857d1f29a25d649c75` on `main`, re-read immediately before this write. Its complete multi-spare proof and checks remain at the immutable link below; the original one-spare WIP, review and transport history also remain directly linked.

**LAST VERIFIED RESULT:** under the full canonical selected/residual assumptions and |T|=|H|=d, every extra selected label at a high source must be routed to another high source with a DISJOINT set of tight-label destinations. Hence E=sum_H(|S_u|-d) is at most the number of disjoint unordered high-source pairs. At |M|=2d, disjoint d-sets must be complements; their disjointness graph is a union of complete bipartite components and isolates. Therefore E<=floor(d^2/4), and sum_H q_u<=d^2+floor(d^2/4). For an actual underlying graph G, the same construction gives E=e(G[H]) and G[H] is bipartite at this boundary. Finite checks passed on 8,038 small receiver-set families, with extremal set controls and a larger-ground-set negative control. These are NOT enumerations of original graphs or catalogue states.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The prior 41 strict-block/equality active certificates remain `NOT_PROMOTED`; the 170-candidate forced-core audit remains `AUDIT_COMPLETE_NOT_PROMOTED`. Original equality replay remains `NOT_RUN` in this session; its 4,588 Python/C++ agreement and 25 active certificates are prior recorded evidence. No new state IDs or numerical exclusions are claimed. State 3349 q-enumeration is unresolved.

**ACTIVE / PENDING:** three bounded units are now preserved: one-spare review; the |M|=d+k,0<=k<d rigidity/union theorem; and this disjointness/boundary theorem. All new proof claims remain internally derived and not promoted. The boundary proof gives a useful restriction rather than complete rigidity. A new catalogue scan still requires exact inputs, the unchanged baseline replay, a tested scalar implementation and independent checks; none is silently inferred from the elementary tests below.

**UNPRESERVED WORK:** `None` after publication. Full current proof, runnable finite-check source and exact results are below. Previous complete proofs, checks and failed transport work are retained verbatim in the immutable predecessor links; the live handoff is not the sole copy of those materials.

**DEFERRED ADMIN:** large-input transfer, automatic workflow-completion reporting, reviewer README maintenance and unrelated CI work. Do not retry the failed direct DNS route in an unchanged environment. No workflow was launched, cancelled or polled during these units.

**NEXT ACTION:** one bounded symbolic unit extending the disjointness budget into 2d<|M|<3d. Start from the fact that three pairwise disjoint d-subsets would require at least 3d receivers; derive the resulting edge-count restriction directly before claiming an extra-selection bound. Do not assume bipartiteness merely from absence of triangles, and preserve the first result or failure before further work. Keep full-catalogue replay/application separate; no user intervention is required for sensible bounded continuation, but no work is claimed to run after the current response ends.

**PROCESS RULE NOW IN FORCE:** `RESEARCH_EXECUTION_POLICY_V3`. One bounded substantive unit, immediate preservation, one publication verification. A user pause/stop instruction overrides further research or housekeeping.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Read `AGENTS.md` and only the exact mathematical inputs needed.
3. Do not reconstruct from chat history when durable sources agree.
4. Preserve each substantive result or failure before the next unit.

## Immutable research and preservation links

- [Multi-spare rigidity and residual-union theorem, full proof, tests and limits](https://github.com/paullenz/MurtySimon742/blob/57a1a2b48637763a4b09ce857d1f29a25d649c75/CURRENT_STATE.md).
- [One-spare proof review, reverse-containment audit and finite checks](https://github.com/paullenz/MurtySimon742/blob/43dc689300eb20efa30e2b848a5326f3c5dcbd6f/CURRENT_STATE.md).
- [Original one-spare WIP, complete transport diagnosis, seven-file manifest and downloader](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/CURRENT_STATE.md).
- [Canonical selected/residual bridge](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md), especially Sections 2, 3, 5, 6.1 and 6.4.
- [Strict tight-label block theorem](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-15-tight-label-block-v1/README.md).
- [Original equality proof and replay package](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-15-tight-label-equality-v1/README.md).

## Extra selections require disjoint tight-destination sets

### Hypotheses and notation

Use the full canonical representative construction, not arbitrary demand-thinned selected sets or a freely chosen scalar routing. For each B-vertex u, N_u=S_u disjoint-union R_u and |R_u|=rho_u. Demands s_i are nonnegative integers, each label has at least s_i distinct selected sources, and selection of i at u requires s_i<=rho_u. Every selected label has an actual destination. Distinct labels at one source have distinct destinations, and opposite orientations cannot both represent the same unordered missing B-pair.

For an obligation (u,i)->v, the construction gives

    i not in N_v,
    S_u minus {i} subset N_v,
    S_v subset N_u.                                         (P)

The reverse containment follows directly from quasi-edge domination and the prohibition on opposite selected orientations; its full derivation is in the preceding review.

Fix d>=1 and set

    T={i:s_i=d}, H={u:rho_u>=d}, M={v:rho_v=d-1}.

Assume |T|=|H|=d. For this first lemma no upper bound on |M| is imposed. Any actual realization necessarily has |M|>=d. All high vertices select T. A tight-label destination lies in M and has residual set exactly T minus the label it receives, because it cannot select T and has fewer than d residual slots.

Let D_u be the d distinct tight-label destinations of u in H. Define a simple graph Gamma on the d high vertices by

    uw in E(Gamma) iff D_u intersect D_w is empty.

Repeated destination sets at different high vertices are allowed. Gamma has distinct source vertices, not merely distinct set types.

### Lemma 1: every extra obligation uses a disjoint high pair

Suppose j in S_u minus T and its selected destination is w.

First w must be high. Otherwise forward containment in (P) would place all d labels of T into N_w. None can be selected outside H, while rho_w<d, a contradiction.

Now suppose v belonged to D_u intersect D_w. The tight obligation from u to v forces j in N_v. Since R_v is contained in T, j is selected at v. The tight obligation from w to v and reverse containment then give j in N_w. But w is the destination of (u,j), so j must be absent from N_w. Contradiction.

Consequently

    (u,j)->w with j outside T implies u,w in H
    and D_u intersect D_w is empty.                         (D1)

This statement is valid for arbitrary |M| under the stated hypotheses. It does not say every disjoint pair supports a realizable obligation.

### Lemma 2: an exact combinatorial budget

Let

    E=sum_{u in H}|S_u minus T|=sum_{u in H}(|S_u|-d).

Every extra label has one destination, which by D1 is a neighbour of its source in Gamma. Different selected labels at a source have different destinations. Also opposite orientations of one unordered pair cannot both be selected. Thus extra obligations inject into unordered edges of Gamma, giving

    |S_u|-d <= deg_Gamma(u) for every u in H,
    E <= e(Gamma).                                         (D2)

For the actual original diameter-two edge-critical graph G, write J=complement(G). Every missing J-pair inside H has exactly one selected representative, whose source and destination are high. Its label cannot lie in T, since every high vertex already contains every T-label. Conversely every extra high obligation has both ends in H by D1. Therefore, for that actual graph,

    E=e(G[H]), and G[H] is a subgraph of Gamma.              (D3)

D3 uses the full missing-pair representation property. It is not an assertion of graph realization for a relaxation satisfying only some numerical conditions.

### Corollary: recover rigidity below 2d

If |M|<2d, no two d-element subsets of M are disjoint. Gamma is edgeless, so D2 gives E=0 and S_u=T for every high source. This recovers the rigidity step of the preceding multi-spare theorem by a shorter obstruction argument. For d=1 there is only one high source, so E=0 for any receiver pool; the earlier d>=2 restriction belonged to its particular overlap proof, not a counterexample at d=1.

## Boundary theorem at |M|=2d

When |M|=2d, disjoint d-subsets must be exact complements:

    D_u intersect D_w empty iff D_w=M minus D_u.            (B1)

Group high vertices by their destination set. Every set type X is paired with its unique complementary type M minus X. If the two groups have sizes p and q, the corresponding Gamma component is K_(p,q); a group whose complement is absent contributes isolated vertices. Since d>=1, a set cannot equal its disjoint complement, so there are no loops or exceptional self-pairs.

Thus Gamma is a disjoint union of complete bipartite components and isolates. Choose a bipartition of each component and combine them into two sides of sizes P and Q; place isolates arbitrarily. Then P+Q=d and

    e(Gamma) <= P Q <= floor(d^2/4).                       (B2)

The final inequality follows from (P-Q)^2>=0 and integrality. Combining D2 and B2 gives

    sum_{u in H}(|S_u|-d) <= floor(d^2/4),                  (B3)
    sum_{u in H}q_u <= d^2+floor(d^2/4).                    (B4)

For an actual G, D3 additionally shows that G[H] is bipartite at this boundary and e(G[H])<=floor(d^2/4). This is a LOCAL induced-subgraph statement under the tight-block hypotheses, not the unrestricted Murty–Simon inequality.

For example d=5, |M|=10 gives at most 6 extra high-source selections in total. This is an illustrative conditional bound, not a state rejection or an assertion that all six can occur in a genuine graph.

### Limits and failed overextensions preserved

- The previous common-receiver argument cannot simply be reused at |M|=2d. The replacement is a restriction on permitted extra obligations, not a claim that no extras exist.
- Extremal abstract set families attain floor(d^2/4) by splitting the d high vertices between a fixed d-set and its complement as evenly as possible. This proves sharpness of the SET-FAMILY edge budget only, not sharpness for realizable graphs.
- For larger M, disjoint d-sets need not be complements. The complete-bipartite-component argument must not be exported without proof.
- With d=3 and |M|=9, three disjoint triples give a triangle in Gamma with three edges, exceeding floor(3^2/4)=2. This is a counterexample to an UNRESTRICTED SET-FAMILY version of B2, not a counterexample graph to Murty–Simon or to the actual selected system.
- Neither the new budget nor the earlier union bound has been applied to the catalogue. A correct structural inequality may be weak or vacuous on some states; no reduction in the 952 survivors is inferred.

## Exact finite check of the boundary set-family graph

The following program was run locally. It checks all ordered families of d destination d-sets on a 2d-element ground set for d=1,2,3, including repeated set types. It also checks balanced complementary families for d=1 through 20 and the larger-ground-set triangle negative control. It does not enumerate original graphs or certify graph realizability.

```python
#!/usr/bin/env python3
"""Small exhaustive checks of the boundary set-family graph, not original graphs."""
from itertools import combinations, product
import json


def check_family(family, d):
    full = (1 << (2 * d)) - 1
    edges = []
    adjacency = [[] for _ in family]
    for u, v in combinations(range(len(family)), 2):
        if not family[u] & family[v]:
            assert family[v] == full ^ family[u]
            edges.append((u, v))
            adjacency[u].append(v)
            adjacency[v].append(u)
    colors = {}
    for start in range(len(family)):
        if start in colors:
            continue
        colors[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for v in adjacency[u]:
                if v in colors:
                    assert colors[v] != colors[u]
                else:
                    colors[v] = 1 - colors[u]
                    stack.append(v)
    assert len(edges) <= d * d // 4
    return len(edges)


rows = []
for d in range(1, 4):
    choices = [sum(1 << i for i in s) for s in combinations(range(2*d), d)]
    count, maximum = 0, 0
    for family in product(choices, repeat=d):
        maximum = max(maximum, check_family(family, d))
        count += 1
    assert maximum == d*d//4
    rows.append(dict(d=d, families=count, max_edges=maximum, bound=d*d//4))
for d in range(1, 21):
    left = (1 << d) - 1
    right = left << d
    family = [left]*(d//2) + [right]*(d-d//2)
    assert check_family(family, d) == d*d//4
# Disjointness need not be bipartite on a larger ground set.
family = [(1 << 3)-1, ((1 << 3)-1) << 3, ((1 << 3)-1) << 6]
assert all(not family[u] & family[v] for u, v in combinations(range(3), 2))
print(json.dumps(dict(status='PASS_BOUNDARY_SET_FAMILIES_ONLY', rows=rows,
    exhaustive_families=sum(x['families'] for x in rows),
    extremal_set_controls=20, larger_ground_set_triangle_control=True,
    catalogue_replay='NOT_RUN', original_graph_counterexample_claimed=False), indent=2))
```

Recorded status: `PASS_BOUNDARY_SET_FAMILIES_ONLY`. Exact rows `(d,families,maximum edges,bound)` were `(1,2,0,0)`, `(2,36,1,1)`, `(3,8000,2,2)`: **8,038** exhaustive set families in total. All **20** extremal set controls and the larger-ground-set triangle control passed. Catalogue replay: `NOT_RUN`; original graph counterexample claimed: `False`.
