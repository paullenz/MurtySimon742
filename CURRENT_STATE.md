# Murty–Simon / Erdős #742 — live current state

> **Operational source of truth.** Read this file first after every timeout, new chat, takeover, or resumed session. `README.md` is the lower-frequency reviewer-facing summary and may lag routine WIP/status checkpoints. The complete pre-transaction-protocol handoff remains at [`archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md`](archive/status-snapshots/2026-09-15/CURRENT_STATE_pre_transaction_protocol.md).

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_PROOF_REVIEW_NOT_PROMOTED`. First bounded unit: targeted review of the saved one-spare argument, with finite checks of its elementary set steps. This is the same assistant's internal review, not independent expert acceptance.

**WORK MODE:** `MATH`. The user requested selection and execution of the next priorities without further intervention. Proof review was explicitly separated from the pending numerical replay; no download repairs, workflow polling or unrelated maintenance were performed.

**INSPECTED PREDECESSOR:** `219ba7043c8a8b7152ba42715ab8767e667fb75d` on `main`, re-read immediately before this write. Its complete original candidate argument, transport diagnosis, seven-file manifest and downloader source remain verbatim at the immutable predecessor link below.

**LAST VERIFIED RESULT:** the internal review below found no gap in OS1/OS2 under the specified full selected-representative bridge hypotheses and d>=2. The reverse-containment dependency was re-derived from the quasi-edge definition and uniqueness of the selected orientation. Finite set-step checks passed for d=2 through 9: 380 receiver-set pair checks and 1,318 two-occurrence intersection checks, plus two negative controls. These are NOT graph enumeration or catalogue replay. The original equality package's 25 certificates and 4,588 Python/C++ agreement remain prior recorded evidence, not newly rerun here.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 canonical exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict-block/equality active certificates remain `NOT_PROMOTED`; the 170-candidate forced-core audit remains `AUDIT_COMPLETE_NOT_PROMOTED`. External review of the bridge and new argument remains OPEN. No new exclusion count is claimed.

**ACTIVE / PENDING:** the equality catalogue replay remains `NOT_RUN` in this session. State 3349 q-enumeration remains unresolved. The present proof review does not require catalogue downloads and does not substitute for the replay before a catalogue scan. There is a next structural question: replace one spare receiver by k spare receivers and test the overlap lower bound d-k; this is a proposed next unit, not a generalized theorem claimed by this checkpoint.

**UNPRESERVED WORK:** `None` after publication: the complete review, exact finite-check program and its results are included below. Earlier candidate and transfer work are preserved by the immutable predecessor, not discarded or silently reclassified.

**DEFERRED ADMIN:** large-input transfer, automatic workflow-completion reporting, reviewer README maintenance and unrelated CI work. Do not revisit the failed direct DNS/download route in an unchanged environment. No workflow was launched, cancelled or polled for this unit.

**NEXT ACTION:** perform one bounded hand-mathematics unit on |M|=d+k with 0<=k<d: determine whether pairwise receiver intersection and k+1 forced occurrences yield a valid generalization of OS1/OS2. State all hypotheses, audit boundary cases, preserve the result before any further unit. The numerical replay remains a separate prerequisite for new catalogue decisions, not a prerequisite for this symbolic proof attempt.

**PROCESS RULE NOW IN FORCE:** `RESEARCH_EXECUTION_POLICY_V3`. Exact-input reads, one bounded unit, immediate preservation, one publication verification. A user pause/stop instruction overrides further research or housekeeping.
<!-- CURRENT-STATUS:END -->

## Recovery procedure

1. Read this file first and record current `main` SHA.
2. Read `AGENTS.md`; inspect only the exact inputs required for the active unit.
3. When durable sources agree, do not reconstruct the project from chat history.
4. Preserve the first substantive result or failure before another unit.

## Immutable source and preservation links

- [Complete preceding handoff, original one-spare argument, transfer diagnosis, manifest and downloader source](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/CURRENT_STATE.md). This is the archival source for the preceding WIP and its failure history; its text is not overwritten at that commit.
- [Canonical bridge at the reviewed predecessor](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md), especially Sections 2, 3, 5, 6.1 and 6.4.
- [Strict tight-label theorem](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-15-tight-label-block-v1/README.md).
- [Equality theorem and its existing replay](https://github.com/paullenz/MurtySimon742/blob/219ba7043c8a8b7152ba42715ab8767e667fb75d/project/research/general_n/2026-09-15-tight-label-equality-v1/README.md).

## One-spare proof review — internal, not promoted

### Exact scope

Let d>=2, T={i:s_i=d}, H={u:rho_u>=d}, M={v:rho_v=d-1}, and L={v:rho_v<d-1}. Assume |T|=|H|=d and |M|=d+1. Label demands and residual sizes are nonnegative integers. At a B-vertex u the cross-neighbourhood N_u is the disjoint union S_u union R_u, with |R_u|=rho_u. Every selected label has its actual canonical destination. A label i is selected at at least s_i distinct sources; selecting it at u requires s_i<=rho_u.

The sets S_u must be the FULL selected sets of the canonical representative construction, not arbitrary demand-sized subfamilies or purely numerical q witnesses. A source's destinations are distinct; exactly one orientation represents an unordered missing B-pair. For (u,i)->v, i is absent from N_v and S_u minus {i} is contained in N_v.

This review checks the dependencies used by OS1/OS2. It is not a new audit of the entire canonical bridge, the whole repository, fixed-order results or any numerical catalogue.

### 1. Reverse containment is justified

Write J for the complement graph to avoid confusing it with the high-source set H. If (u,i)->v is selected, uv is missing in J[B]. For j in S_v, let (v,j)->z be its selected quasi-edge. The exception z cannot be u: that would give the opposite selected orientation of the already represented unordered pair {u,v}. The quasi-edge vj dominates every vertex except z, hence it dominates u. As vu is missing, ju must be present. Thus j belongs to N_u, proving

    S_v subset N_u whenever (u,i)->v is selected.          (RC)

No capacity bound, total-surplus inequality, q enumeration or independently chosen routing is used here.

### 2. Tight-label sources and destinations

Every i in T needs at least d selected sources; exactly d vertices are eligible. Therefore all vertices of H select all labels in T. This uses a lower demand bound, not an unjustified assumption that every label has exactly its demand in occurrences.

A T-obligation cannot end in H because every high vertex contains its label. Outside H no T-label can be selected. The receiver must contain the other d-1 T-labels residually; its residual degree is less than d. Therefore it lies in M and, if it receives label i, its residual set is exactly T minus {i}.

For u in H, let D_u be the set of its d distinct T-destinations. Then D_u is a d-element subset of M. Only receivers actually receiving a T-obligation are asserted to have these saturated residual sets. A receiver omitted by every source has not been silently assumed saturated.

### 3. The overlap step does not assume equal omissions

For u,w in H,

    |D_u intersect D_w| >= |D_u|+|D_w|-|M| = d-1 >= 1.

This works whether u and w omit the same receiver or different receivers. At d=2 the guaranteed intersection has size one, which is sufficient. No stronger intersection property is needed.

### 4. High-source rigidity OS1

Suppose j in S_u minus T. Each v in D_u contains j by forward containment, and j cannot be residual there because R_v is contained in T. Hence j in S_v for all v in D_u.

For every other w in H choose v in D_u intersect D_w. Since w sends a T-obligation to v, (RC) puts j in N_w. It already belongs to N_u. Thus j belongs to every high neighbourhood.

The obligation (u,j) consequently cannot terminate in H, since its destination must omit j. Nor can it terminate outside H: forward containment would place all d labels of T there, none selectable there, despite fewer than d residual slots. Every selected label has a destination, so this is a contradiction. Therefore

    S_u=T and q_u=d for every u in H.                     (OS1)

### 5. Two-occurrence residual-union bound OS2

For i outside T let

    e_L(i)=|{w in L:rho_w>=s_i}|,
    K_2={i outside T:s_i>e_L(i)+1}.

OS1 leaves no selected occurrence of i in H. Eligibility permits at most e_L(i) selected sources in L. Thus each i in K_2 is selected at at least two DISTINCT vertices in M. Since each u in H omits just one receiver from D_u, at least one selected occurrence is at a vertex in D_u. Applying (RC) gives i in N_u. By OS1, i is outside S_u and hence is in R_u. Consequently

    K_2 subset R_u for every u in H,
    |K_2| <= min_{u in H} rho_u.                          (OS2)

This is conditional on the complete stated bridge hypotheses. It does not assert those hypotheses sufficient to realize a graph.

### 6. Negative controls and limits

- A single forced occurrence can be at the omitted receiver. Reusing the equality case's one-occurrence K without further information would be unjustified. The set example D={0,1}, P={2} exposes that inference failure; it is not a claimed graph counterexample.
- At d=1 two singleton receiver sets can be disjoint. The displayed intersection argument does not prove that boundary case. This is NOT a claim that OS1 is false at d=1; the present statement deliberately retains d>=2.
- Every quasi-edge needed in the proof is an actual selected representative, not an arbitrary arc in a scalar relaxation.
- No pass/fail result for a finite set check is called a proof of the graph-to-selected bridge.

**Review conclusion:** no gap found in OS1/OS2 under the explicit hypotheses above. This is internal reasoning by the same assistant, not independent review, catalogue certification or ledger promotion.

## Exact finite set-step check

The following program was run locally with Python 3. It needs no downloads or external packages. It checks elementary steps used in the proof, not complete graph realizations.

```python
#!/usr/bin/env python3
"""Finite checks of two set-theoretic steps, not a graph or catalogue replay."""
import itertools
import json

out = []
for d in range(2, 10):
    universe = set(range(d + 1))
    receivers = [universe - {o} for o in universe]
    pair_checks = 0
    for x in receivers:
        for y in receivers:
            assert len(x & y) >= d - 1 >= 1
            pair_checks += 1
    occurrence_checks = 0
    for dset in receivers:
        for pair in itertools.combinations(universe, 2):
            assert dset.intersection(pair)
            occurrence_checks += 1
    out.append({'d': d, 'receiver_pair_checks': pair_checks,
                'two_occurrence_checks': occurrence_checks})
assert not ({0, 1} & {2})
assert not ({0} & {1})
print(json.dumps({'status': 'PASS_FINITE_SET_STEPS_ONLY', 'rows': out,
    'receiver_pair_checks': sum(x['receiver_pair_checks'] for x in out),
    'two_occurrence_checks': sum(x['two_occurrence_checks'] for x in out),
    'negative_controls': ['one occurrence can miss D_u', 'd=1 overlap step can fail'],
    'catalogue_replay': 'NOT_RUN', 'graph_enumeration': 'NOT_RUN'}, indent=2))
```

Recorded result: `PASS_FINITE_SET_STEPS_ONLY`. Per-d counts `(d, receiver pairs, two-occurrence checks)` were `(2,9,9), (3,16,24), (4,25,50), (5,36,90), (6,49,147), (7,64,224), (8,81,324), (9,100,450)`. Totals: **380** and **1,318** respectively. Both negative controls passed. Catalogue replay and graph enumeration: `NOT_RUN`.
