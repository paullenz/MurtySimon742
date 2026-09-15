# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff remains at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_PROOF_NOT_PROMOTED`. Second bounded unit: a parameterized spare-receiver rigidity proof, unifying the equality and one-spare cases. Internal symbolic reasoning and finite set-step checks; no independent expert acceptance or catalogue application.

**WORK MODE:** `MATH`. User-authorized autonomous prioritization. The first unit was published and remotely confirmed before this one began. No download repairs, workflow polling or unrelated maintenance were performed.

**INSPECTED PREDECESSOR:** `43dc689300eb20efa30e2b848a5326f3c5dcbd6f` on `main`, re-read immediately before this write. The complete preceding one-spare review and its runnable finite checks are preserved at the immutable link below. All earlier WIP and transfer history remain linked separately.

**LAST VERIFIED RESULT:** under the explicit canonical selected/residual assumptions, |T|=|H|=d and |M|=d+k with 0<=k<d force S_u=T at every high source. Labels outside T demanding more than e_L(i)+k selected sources must lie in every high residual set, giving |K_(k+1)|<=min_H rho. The full proof is below. Finite set-step checks passed for 21 (d,k) cases, 1<=d<=6: 286,528 receiver-pair checks and 301,013 occurrence checks. Six boundary controls and fifteen omission controls passed. These counts are NOT graph enumeration or catalogue exclusions.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The prior 41 strict-block/equality active certificates remain `NOT_PROMOTED`; the 170-candidate forced-core audit remains `AUDIT_COMPLETE_NOT_PROMOTED`. The equality package's 4,588 Python/C++ agreement and 25 active certificates are prior recorded evidence, not newly rerun here. External review of the bridge and these proofs remains OPEN.

**ACTIVE / PENDING:** original equality catalogue replay remains `NOT_RUN` in this session; no new state IDs or counts are claimed. State 3349 q-enumeration is unresolved. The first untreated scalar boundary is |M|=2d: two high sources may then have disjoint T-destination sets, so the common-receiver argument alone does not force rigidity. This is a proof-method boundary, not a graph counterexample or a proof that rigidity is false there.

**UNPRESERVED WORK:** `None` after publication: full parameterized proof, exact finite-check source, results and limitations are included below. The earlier one-spare review and its checks remain in the immutable predecessor.

**DEFERRED ADMIN:** large-input transfer, automatic workflow-completion reporting, reviewer README maintenance and unrelated CI work. Do not retry the failed direct DNS route in an unchanged environment. No workflow was launched, cancelled or polled.

**NEXT ACTION:** one bounded hand-mathematics unit at |M|=2d: classify possible destinations of an additional high-source selection using disjointness of its source and destination T-receiver sets. Seek an exact restriction or counting bound; do not call the overlap counterexample a graph counterexample. Preserve the first result or failure before further work. Catalogue replay/application remains a separate computational task.

**PROCESS RULE NOW IN FORCE:** `RESEARCH_EXECUTION_POLICY_V3`. One bounded substantive unit, immediate preservation, one publication verification. A user pause/stop instruction overrides further research or housekeeping.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Read `AGENTS.md` and only the exact mathematical inputs for the current unit.
3. Do not reconstruct from chat history when durable sources agree.
4. Preserve each substantive result or failure before the next unit.

## Immutable evidence and preservation links

- [One-spare proof review, dependency audit, exact finite-check source and results](https://github.com/paullenz/MurtySimon742/blob/43dc689300eb20efa30e2b848a5326f3c5dcbd6f/CURRENT_STATE.md).
- [Original one-spare WIP, complete transport diagnosis, seven-file manifest and downloader source](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/CURRENT_STATE.md).
- [Canonical selected/residual bridge](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md), particularly Sections 2, 3, 5, 6.1 and 6.4.
- [Strict tight-label block theorem](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-15-tight-label-block-v1/README.md).
- [Equality proof and existing replay package](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-15-tight-label-equality-v1/README.md).

## Spare-receiver rigidity and residual union — internal conditional proof

### Hypotheses

Use the actual full selected/residual system of the canonical bridge. Labels i have nonnegative integer demands s_i and at least s_i distinct selected sources. At vertex u, N_u=S_u disjoint-union R_u with |R_u|=rho_u. Selection of i at u requires s_i<=rho_u. Every selected label has its actual destination, different selected labels at a source have different destinations, and an unordered missing B-pair is represented in only one orientation.

For every actual selected obligation (u,i)->v we use

    i not in N_v,
    S_u minus {i} subset N_v,
    S_v subset N_u.                                         (P)

The last containment is not a new axiom asserted without justification: if (v,j)->z is selected, then z!=u by uniqueness of the missing-pair orientation. Its quasi-edge dominates u; since uv is missing, uj is present. The preceding review derives this directly from the canonical graph construction. These conditions are necessary for graphs, not asserted sufficient for realizing one.

Fix integers d>=1 and k with 0<=k<d. Define

    T={i:s_i=d},       H={u:rho_u>=d},
    M={v:rho_v=d-1},   L={v:rho_v<d-1}.

Assume |T|=|H|=d and |M|=d+k. For i outside T define

    e_L(i)=|{w in L:rho_w>=s_i}|,
    K_(k+1)={i outside T:s_i>e_L(i)+k}.

### Statement

For every u in H,

    S_u=T, hence q_u=d,                                    (SR1)
    K_(k+1) subset R_u.                                    (SR2)

In particular the following scalar necessary condition is independent of q:

    |K_(k+1)| <= min_{u in H} rho_u.                        (SR3)

All assertions are conditional on the listed full selected-representative hypotheses. No unrestricted Murty–Simon theorem or new catalogue exclusion is being asserted.

### Proof: tight destinations

Every i in T has at least d selected sources and precisely d eligible vertices, namely H. Therefore T subset S_u for all u in H. A T-obligation cannot end in H, where its label is present. Outside H a T-label cannot be selected by eligibility. Its destination must still contain the other d-1 T-labels, so those are all residual. Its residual size is less than d and at least d-1, hence equals d-1. It lies in M, and when receiving i its residual set is exactly T minus {i}.

Let D_u be the d distinct T-destinations of u in H. Thus D_u subset M, |D_u|=d, and u omits exactly k vertices of M. Saturation is claimed only at a vertex actually receiving a T-obligation, not at every unused receiver.

### Proof: rigidity from forced intersection

For any u,w in H,

    |D_u intersect D_w| >= 2d-(d+k)=d-k>0.                 (I)

Suppose j in S_u minus T. For every v in D_u, (P) forces j in N_v. As R_v is contained in T, j must be selected at v. For any other w in H choose v in D_u intersect D_w. Reverse containment at the obligation from w to v yields S_v subset N_w, so j in N_w. The original selection already puts j in N_u. Thus j belongs to every high neighbourhood.

The destination of (u,j) cannot be high, because a destination must omit j. It cannot be outside H either: all d labels of T belong to S_u minus {j}, so (P) would put all of T there, none selectable there, in fewer than d residual slots. Every selected label must have a destination; this contradiction proves SR1.

For d=1,k=0 there is only one high source. The statement and proof still hold: the assertion concerning other high sources is vacuous. This does not claim the one-spare case d=1,k=1, which is outside 0<=k<d.

### Proof: k+1 occurrences cannot all be omitted

Let i in K_(k+1). By SR1 it has no selected source in H. It can have at most e_L(i) selected sources in L, so its demand forces at least k+1 distinct selected sources in M. Every D_u omits only k vertices of M; at least one of these sources lies in D_u. Reverse containment puts i in N_u. Since i is outside T=S_u, it lies in R_u. This holds for every u in H, proving SR2 and SR3.

### Recovered cases and precise limits

- k=0 recovers the equality-case one-occurrence union bound.
- k=1 (necessarily d>=2) recovers the reviewed one-spare two-occurrence bound.
- For example d=5 permits k=0,1,2,3,4, with 5 through 9 receivers. At k=2 a label needs at least three selected M-occurrences to be forced into every high residual set. This example illustrates the theorem, not a catalogue state or an exclusion count.
- If a label has only k forced occurrences, they can all be in M minus D_u. Thus one cannot replace k+1 by k using the hitting argument alone.
- At |M|=2d, the d-sets D and M minus D are disjoint. This invalidates a universal positive-intersection assertion at that boundary. It does NOT establish that SR1 fails for a genuine graph, nor that the theorem's global range is sharp.
- More input structure might extend the result beyond this sufficient scalar range. That remains research, not a conclusion of the finite checks.

## Exact finite set-step check

This program was run locally; no input downloads or external packages were needed. It exhausts the elementary intersection assertions for the stated small parameters, not graph realizations.

```python
#!/usr/bin/env python3
"""Exhaust the small set steps of the spare-receiver lemma, not graph models."""
from itertools import combinations
import json


def masks(n, size):
    return [sum(1 << x for x in xs) for xs in combinations(range(n), size)]


rows = []
for d in range(1, 7):
    for k in range(d):
        m = d + k
        destinations = masks(m, d)
        supports = masks(m, k + 1)
        pair_count = 0
        occurrence_count = 0
        for x in destinations:
            for y in destinations:
                assert (x & y).bit_count() >= d - k > 0
                pair_count += 1
            for selected_support in supports:
                assert x & selected_support
                occurrence_count += 1
        if k:
            first_d = (1 << d) - 1
            omitted_k = ((1 << m) - 1) ^ first_d
            assert omitted_k.bit_count() == k and not first_d & omitted_k
        rows.append(dict(d=d, k=k, m=m, receiver_pair_checks=pair_count,
                         occurrence_checks=occurrence_count))
for d in range(1, 7):
    left = (1 << d) - 1
    right = left << d
    assert left.bit_count() == right.bit_count() == d and not left & right
print(json.dumps(dict(status='PASS_FINITE_SET_STEPS_ONLY', parameter_cases=len(rows),
    receiver_pair_checks=sum(r['receiver_pair_checks'] for r in rows),
    occurrence_checks=sum(r['occurrence_checks'] for r in rows),
    rows=rows, boundary_controls=6, omission_controls=15,
    catalogue_replay='NOT_RUN', graph_counterexample_claimed=False), indent=2))
```

Recorded status: `PASS_FINITE_SET_STEPS_ONLY`. There were **21** parameter cases, **286,528** receiver-pair checks, **301,013** occurrence checks, **6** boundary controls and **15** omission controls. Catalogue replay: `NOT_RUN`. Graph counterexample claimed: `False`.

Exact rows `(d,k,|M|,receiver-pair checks,occurrence checks)`:

```text
1 0 1 1 1
2 0 2 1 2
2 1 3 9 9
3 0 3 1 3
3 1 4 16 24
3 2 5 100 100
4 0 4 1 4
4 1 5 25 50
4 2 6 225 300
4 3 7 1225 1225
5 0 5 1 5
5 1 6 36 90
5 2 7 441 735
5 3 8 3136 3920
5 4 9 15876 15876
6 0 6 1 6
6 1 7 49 147
6 2 8 784 1568
6 3 9 7056 10584
6 4 10 44100 52920
6 5 11 213444 213444
```
