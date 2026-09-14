# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
**14 September 2026 — checkpoint `conditioned-source-sharing-row108-v1`.** Inspected predecessor: `c3eb63dd354c7170a1f56ff774d771accb709858`. This preserves the successful exact source-price restoration receipt (run34905883642), conditioned-price work, the exact row471 rigidity closure of branches39,40 and successful remote replay34906169745, stronger witness work, all failures and reviewer material, and adds an exact selected-incidence exclusion of original synthetic row108. **Fixed-order, general7/12 and canonical-frontier mathematical status unchanged; one additional original synthetic profile is excluded.**

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [`AGENTS.md`](AGENTS.md), [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — unchanged

```text
whole-state closures:               977
canonical exclusions:             1,971
canonical survivors:              3,607
recovered relational candidates:  2,655 — UNPROMOTED
```

Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

## Boundary-profile status

The shared block-slack package had rejected707/713 original synthetic profiles and708/715 fresh profiles. Its six original non-rejections were108,160,338,347,471,586. The new [`conditioned-source-sharing-v1`](project/research/general_n/2026-09-14-conditioned-source-sharing-v1/README.md) excludes original row108 in the stated selected-incidence relaxation. Therefore the ORIGINAL sample is now **708/713 rejected**, with exactly **160,338,347,471,586** not rejected. This is sample-level evidence only. The fresh sample remains **708/715 rejected** in its separate namespace. No canonical whole-state closure or relational-candidate promotion follows.

Separately, the row471 rigidity step closes conditioned branches `e_L=39,40`. Run34906169745 completed SUCCESS and its job explicitly passed the exact conditioned scan, frozen-output digest check, and `Verify row-471 hand rigidity closures` step. Row471 itself is not excluded; conditioned branches `41,42,43,47` remain.

## Exact row108 finish

For row108, shared-slack gives cumulative ranges `e_{s<=1}=26..33` and `e_{s<=2}=33..37`, hence40 monotone exact block-total tuples. Replaying the preserved simultaneous-multiblock screen rejects8 and leaves32.

A single fixed signed source-price vector, with `-4` at zero-based source indices1,12,21 and zero elsewhere, strictly closes24 of those32. All three priced sources have `q_u=5`, so exact source row sums restore the signed Lagrange price exactly.

The final eight tuples are `(26,33),(26,35),(26,36),(26,37),(27,33),(27,36),(27,37),(28,37)`. Row108 has no zero-demand labels, so unit charge is exactly `C0=sum q_u d_u` for ONE common pressure `d_u=(p_u-rho_u+1)_+` per source. All eight require charge at least211.

The standard-library verifier enumerates **46,662** excess histograms up to equal-demand permutation. Exact row/type incidence flow leaves **1,201** feasible histograms. Exact incidence-charge flow disposes of **1,124** below211 even while relaxing common pressure. The remaining **77** undergo exact common-pressure branch-and-bound with flow feasibility at every branch; **57,867** branch nodes are visited and none can attain211. Therefore all32 previous row108 survivors are eliminated in this selected-incidence relaxation.

Complete verifier output canonical SHA256: `5ea860b79516d9a34e73a67fafdb7875cd3c9c99b01594b4bf3aab2c3e8a7629`. Local replay passed before publication. A dedicated remote workflow is installed by this checkpoint and **must not be called successful until its run is inspected**.

## Verification history preserved

- Original source-price run34904353492 **FAILED** on the data-transfer defect before mathematics and stays failed.
- Exact source-price restoration replay run34905883642 **SUCCESS**: restored the pre-existing result hash and passed the unchanged full harness. This validates only that original package.
- Conditioned-source-price run34905354792 **SUCCESS** for its frozen scan.
- Its successor run34906169745 also **SUCCESS**, including exact verification of row471 conditioned branch closures `e_L=39,40`; row471 remains open at `41,42,43,47`.
- The row108 package has local complete replay only at this checkpoint; its remote result is pending inspection.

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

The complete predecessor handoff is preserved byte-for-byte in [`CURRENT_STATE_PRE_ROW108_2026-09-14.md`](CURRENT_STATE_PRE_ROW108_2026-09-14.md); historical status remains available without cluttering the live handoff. Earlier archives, reviewer packages, counterexamples and negative experiments remain intact.

The2,655 recovered relational candidates require complete coverage, both implementations agreeing, zero unresolved cases, successful aggregate and a separate reviewed ledger step before promotion. Sample exclusions do not change that gate. Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge.
