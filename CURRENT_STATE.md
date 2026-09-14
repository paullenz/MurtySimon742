# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
**14 September 2026 — checkpoint `relational-ledger-promotion-v1`.** The separate reviewed-ledger gate has completed after full discovery run `34844403328` and independent audit run `34854911792`. The candidate key files are byte-identical; all 2,655 keys have dual agreement; unresolved count is zero; the reviewed base ledgers were non-overlapping; and the promoted ledgers reconcile exactly. **Canonical finite frontier is now 4,626 exclusions / 952 survivors / 3,632 whole-state closures.** Fixed-order/general candidate and boundary-profile mathematical status is otherwise unchanged; external review remains OPEN.
<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [`AGENTS.md`](AGENTS.md), [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — unchanged pending reviewed ledger promotion

```text
whole-state closures:             3,632
canonical exclusions:             4,626
canonical survivors:                952
  N34-derived survivors:             949
  N35-derived survivors:               3
recovered relational candidates:  2,655 — AUDITED AND PROMOTED
```

Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

## Relational validation lane — promoted

Discovery/recovery run `34844403328` and independent audit run `34854911792` cover the exact same 2,655-key set (SHA256 `67593252e0bc27766c24c8bf38060c8b0f98384a6f61fc02ac1e25fafb0ecfa2`), with zero unresolved states and successful two-implementation aggregate agreement. The separate reviewed ledger step confirmed zero overlap with the pre-existing ledgers and promoted 2,580 N34 plus 75 N35 closures. The remaining relational frontier is 952 states: 949 N34 and 3 N35. See the promotion audit in the alternative-attacks package. This remains finite evidence conditional on the canonical bridge, not an unrestricted proof.

## Boundary-profile status

The shared block-slack package had rejected707/713 original synthetic profiles and708/715 fresh profiles. The row108 [`conditioned-source-sharing-v1`](project/research/general_n/2026-09-14-conditioned-source-sharing-v1/README.md) exclusion raises the ORIGINAL sample to **708/713 rejected**, with exactly **160,338,347,471,586** not rejected. This is sample-level evidence only. The fresh sample remains **708/715 rejected** in its separate namespace. No canonical whole-state closure or relational-candidate promotion follows.

Separately, the row471 rigidity step closes conditioned branches `e_L=39,40`. Run34906169745 completed SUCCESS and explicitly passed the exact conditioned scan, frozen-output digest check and `Verify row-471 hand rigidity closures` step. Row471 itself is not excluded; conditioned branches `41,42,43,47` remain.

## Exact row108 finish — now remotely reproduced

For row108, shared-slack gives cumulative ranges `e_{s<=1}=26..33` and `e_{s<=2}=33..37`, hence40 monotone exact block-total tuples. Replaying the preserved simultaneous-multiblock screen rejects8 and leaves32. One fixed signed source-price vector closes24; the final eight require unit charge at least211 under one common source pressure.

The standard-library verifier enumerates **46,662** excess histograms, leaves **1,201** exact row/type-incidence-feasible histograms, disposes of **1,124** by exact incidence-charge flow below211, and sends the remaining **77** to exact common-pressure branch-and-bound. **57,867** branch nodes are visited; none attains211. Complete verifier output canonical SHA256: `5ea860b79516d9a34e73a67fafdb7875cd3c9c99b01594b4bf3aab2c3e8a7629`.

Local replay passed before publication. Remote workflow **34906766833**, job **104185160249**, completed **SUCCESS**; its `Exact conditioned row-108 replay` step also completed SUCCESS. Status-sync run34906766824 and reviewer-navigation run34906766838 likewise completed SUCCESS on the predecessor row108 commit.

## Failure preservation and documentation repair

N30 reviewer-v3 package run **34906766832** on predecessor `010ea199...` FAILED at `Check complete proof tables, current links and release hashes`. Its log shows the specific assertion `releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf`: the predecessor's condensed protected reviewer section had retained package README links but removed the explicit frozen PDF paths required by the N30 integrity checker. No N30 proof or release bytes were changed. This checkpoint restores the full n25–n30 manuscript/verification PDF navigation. The failed run remains failed and is not repainted green; the new workflow result triggered by this repair must be inspected separately.

## Immediate next target

Do not broaden blind price search. Prioritize one actual selected-incidence matrix together with destination-label compatibility and the bridge's ONE common residual-neighbourhood condition, especially original row471 at eta2/e_L41 first, then42,43,47; branches39,40 are now exactly closed. In parallel, carry the exact common-pressure/source-incidence mechanism across the five remaining original profiles. Preserve every non-rejection and keep the fresh namespace separate.

For a canonical arc `u->w` and selected-label sets `S_u,S_w`, retain

```text
1 <= |S_u minus S_w| <= rho_w+1,
|S_w minus S_u| <= rho_u,
| (union_{w:u->w} S_w) minus S_u | <= rho_u.
```

The last line enforces one shared residual neighbourhood at each source. Full multiresource shared slack, exact q-layer/mincut, crossing-wall/saturation and maximum-cut/stability remain preserved alternatives.
<!-- CURRENT-STATUS:END -->

## Preservation and audit gates

The complete pre-row108 handoff is preserved byte-for-byte in [`CURRENT_STATE_PRE_ROW108_2026-09-14.md`](CURRENT_STATE_PRE_ROW108_2026-09-14.md); earlier archives, reviewer packages, counterexamples and negative experiments remain intact.

The 2,655 recovered relational candidates have now cleared complete coverage, dual agreement, zero unresolved cases, successful aggregate and the separate reviewed-ledger step. Their ledger promotion changes only the canonical finite frontier. Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge.
