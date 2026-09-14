# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
**14 September 2026 — checkpoint `relational-ledger-validation-v1`.** Inspected predecessor: `13d62aeb7abb1c84acb483610c0667c905709025`. The 2,655-key relational audit is confirmed complete: exact discovery/audit key sets are byte-identical, all 256 audit shards plus aggregate succeeded, both implementations agree, and unresolved count is zero. This commit installs the hash-gated separate reviewed-ledger promotion step and updates target reconstruction to respect both N34 and N35 ledgers. **Mathematical status unchanged in this preparatory commit; canonical counts remain unchanged until that promotion workflow succeeds.**
<!-- RELATIONAL-FULL-PROMOTION:PENDING -->

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [`AGENTS.md`](AGENTS.md), [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — unchanged pending reviewed ledger promotion

```text
whole-state closures:               977
canonical exclusions:             1,971
canonical survivors:              3,607
recovered relational candidates:  2,655 — AUDIT COMPLETE / LEDGER REVIEW PENDING
```

Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

## Relational validation lane — audit complete, promotion pending

Run `34854911792` completed successfully after auditing all 2,655 recovered keys with two independent implementations over 256 shards and a successful aggregate requiring complete agreement. The discovery and audit key TSVs are byte-identical (SHA256 `67593252e0bc27766c24c8bf38060c8b0f98384a6f61fc02ac1e25fafb0ecfa2`), and both report zero unresolved states. The separate reviewed-ledger step is installed by this checkpoint but has not yet run; therefore no canonical count changes are claimed here.

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

The2,655 recovered relational candidates have now cleared complete coverage, both implementations agreeing, zero unresolved cases and a successful aggregate in run34854911792. The final separate reviewed-ledger step is installed by this checkpoint and remains the only promotion gate. Sample exclusions do not change that gate. Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge.
