# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
**15 September 2026 — checkpoint `singleton-destination-trap-v1`.** Inspected predecessor: `00c872dd6321aa4d7c99ada4a703644329733af7`. The row471 branch work through `e_L=43` is preserved, including remote-success run34909572352. A stronger selected-label/destination consequence now excludes **whole original synthetic profiles347,471,586**: every `(q,rho)=(1,1)` source can point only to a `q<=1` destination, and opposite arcs turn these destinations into capacity-one unordered pair slots. Exact matching gives deficiencies on all three profiles; a broader all-source cardinality-compatible pair-slot flow independently rejects the same three. **Original sample improves from708/713 to711/713, leaving only160 and338. Canonical finite frontier remains4,626 exclusions / 952 survivors /3,632 whole-state closures. Fresh sample remains708/715 in its separate namespace.** External review remains OPEN.
<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [`AGENTS.md`](AGENTS.md), [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — unchanged by the singleton result

```text
whole-state closures:             3,632
canonical exclusions:             4,626
canonical survivors:                952
  N34-derived survivors:             949
  N35-derived survivors:               3
recovered relational candidates:  2,655 — AUDITED AND PROMOTED
```

The reviewed relational promotion remains the current canonical finite frontier. Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

## Original synthetic boundary sample — now 711/713

After the row108 exact source-sharing exclusion, the five original non-rejections were160,338,347,471,586. The new [`singleton-destination-trap-v1`](project/research/general_n/2026-09-15-singleton-destination-trap-v1/README.md) excludes347,471,586 as whole synthetic profiles. Exactly **160 and338 remain not rejected** in this original namespace.

The proof uses the retained canonical arc coupling. If `q_u=rho_u=1`, then `|S_u|=1` and

```text
1 <= |S_u minus S_w|,
|S_w minus S_u| <= rho_u=1
```

force `S_u` disjoint from `S_w` and hence `q_w=|S_w|<=1`. Thus every such source needs its one outgoing arc to a different `q<=1` vertex. Because opposite arcs are forbidden, the outgoing choices must match these sources into distinct unordered pair slots.

Exact results on the five current profiles:

```text
row160: singleton matching 2/2; full cardinality pair flow 81/81 — retained
row338: singleton matching 1/1; full cardinality pair flow 101/101 — retained
row347: singleton matching 0/1; full cardinality pair flow 127/129 — EXCLUDED
row471: singleton matching 1/2; full cardinality pair flow 95/96 — EXCLUDED
row586: singleton matching 0/1; full cardinality pair flow 108/109 — EXCLUDED
```

For row347, source16 is `(1,1)` and is itself the only `q<=1` vertex, so it has no legal destination. Row586 is identical in form at source8. Row471 has exactly two `(1,1)` sources,3 and4, and they are the only `q<=1` vertices; both would have to use the same unordered pair in opposite directions, forbidden by the simple orientation.

The broader cardinality flow is a deliberately relaxed independent cross-check. For direction `u->w`, if `I=|S_u intersect S_w|`, local coupling requires

```text
max(0,q_u+q_w-a,q_u-rho_w-1,q_w-rho_u)
<= I <=
min(q_u,q_w,q_u-1).
```

The verifier creates one capacity-one node per unordered pair for which at least one direction can satisfy this interval and asks whether all source outdegrees `q_u` fit. Failure is a valid necessary-condition exclusion; success for160/338 is only a non-rejection.

Frozen parsed result SHA256:

```text
9a89c420f82a0bd89eb8e99a34dd3109ace9c1829879e62e819d452f408313f7
```

Local standard-library replay passed. Dedicated remote workflow is newly installed by this checkpoint and **must not be called successful until inspected**.

## Row471 branch history — preserved but superseded for exclusion

Earlier exact work remains useful independent evidence:

- `e_L=39,40`: conditioned rigidity closure, remote run34906169745 SUCCESS.
- `e_L=41`: independent high-block/common-pressure contradiction.
- `e_L=42,43`: exact source-group split with `214<222` and `215<222`; remote run **34909572352 SUCCESS**. Its independent `e_L=41` regression gives `213<222`.

Before the singleton theorem, only `e_L=47` remained. That branch is now unnecessary because the destination obstruction excludes row471 before any excess split. Do not delete the branch packages: they are preserved proof-development and cross-check evidence.

## Exact row108 finish — remotely reproduced

Row108 remains excluded by its separate selected-incidence/source-sharing route. Its standard-library verifier enumerates46,662 excess histograms, leaves1,201 row/type-incidence-feasible histograms, disposes of1,124 by exact incidence-charge flow below211, and sends77 to exact common-pressure branch-and-bound.57,867 branch nodes are visited; none attains211. Remote workflow34906766833/job104185160249 completed SUCCESS.

## Fresh namespace — deliberately separate

The fresh seed sample remains **708/715 rejected** with seven retained profiles in its own namespace. The new singleton package intentionally scans only the five current ORIGINAL rows and makes no fresh-seed claim. Scan fresh profiles separately before changing those counts.

## Immediate next target

Rows160 and338 pass both the singleton matching and the all-source cardinality-compatible pair-slot flow. Cardinality-only orientation constraints have therefore reached their natural limit on the original sample.

The next attack should impose **one actual selected-label family** across all arcs together with destination compatibility and the shared residual-neighbourhood condition

```text
| (union_{w:u->w} S_w) minus S_u | <= rho_u.
```

The previously preserved uncoupled witnesses for rows160 and338 already violate these stronger coupling tests. The task is to exclude every allowed realization, not only those particular witnesses. A useful implementation target is an exact set-family/orientation feasibility checker or a proof-producing relaxation that shares residual labels globally per source.

In parallel, scan the seven fresh-seed profiles with the singleton/cardinality theorem **without mixing row namespaces**. Preserve all non-rejections.
<!-- CURRENT-STATUS:END -->

## Preservation, failures and audit gates

The complete pre-row108 handoff is preserved byte-for-byte in [`CURRENT_STATE_PRE_ROW108_2026-09-14.md`](CURRENT_STATE_PRE_ROW108_2026-09-14.md); earlier archives, reviewer packages, counterexamples and negative experiments remain intact.

Historical failures remain failures: source-price transfer run34904353492, N30 navigation run34906766832, the red-team-history guard failure34908428824, and standalone row471 process commit `2667a909...` are not repainted by later repairs. The branch-specific charge route did not itself finish row471; the singleton-destination theorem is a distinct stronger structural argument.

The 2,655 relational candidates have cleared complete coverage, dual agreement, zero unresolved cases, successful aggregate and the separate reviewed-ledger step. Their promotion changes the canonical finite frontier. Synthetic sample exclusions such as rows108,347,471,586 do **not** change it.

Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge and the selected-label/destination coupling used by the singleton theorem.