# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The pair-coverage theorem, critical-edge charge, quadratic defect bound and five-label D>=8 corollary are assembled with complete reproducible source and checked evidence. The earlier special-case derivations remain as historical stages.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `VERIFIED_INTERNAL_PAIR_COVER_SUPPORT_CHARGE_NOT_PROMOTED`.

**WORK MODE:** `AUDIT`. Completed the bounded structural extension and source-only regeneration. No external job was launched.

**INSPECTED PREDECESSOR:** `d151af72e1fbd4a7fa2759347c045168cd868338`, tree `501dc4c8918b163c67bb9d01617053bb305f38ee`. Its pre-test pair-coverage and charge derivation is preserved unchanged. The special-case precursor remains at f047855b3d4f51f273fe1ba270284f6025134243.

**LAST VERIFIED RESULT:** under the actual whole exact-block hypothesis, D<d(d-2) forces a shared K-neighbour for every tight pair. Whenever this pair coverage holds, E_h(Q)<=L+floor(L/h)+beta for h>=1, where E_h counts edges with both tight degrees at least h+1. This gives D>=ceil(d(d-1)/4) for all d>=3. At d=5, a separate short hand corollary gives D>=8, W>=33, or W>=53 with extra high-source selections. No all-tight common label is required. These are internal candidate theorems with explicit graph scope; external mathematical acceptance, sharpness and novelty remain open.

**FRESH CHECKS:** Python bitset reachability and C++ explicit middle-vertex paths agree on all 121549 records: 87685 local graph records and 33864 tight-graph records. There are 71241 records meeting the sufficient deletion premises, with no lost short pair. Tests include pair-covered interfaces without a common all-tight label and five named controls. Exact checks cover 255632 support/weight/threshold cases, 5314440 row inequalities and 244420 floor/ceiling identities. These are local lemmas and auxiliary-graph checks, not a canonical exact-block graph census. Both implementations and proof are by the same assistant.

**REPLAY:** source-only regeneration reproduced the complete expected summary and pinned hashes; it was rerun successfully after the user's interruption. Input SHA256 c86c8d5580151753c75707ce7c93d16db83e00d52f0247c0ad3800126d089dc4; both decision SHA256 a3b0e95a3666e3deb3039b6d4e04278eead9c68740fc87873e656f97a14af581. Run python3 verify_published.py in the new package directory. Older 11357/324554/407741 replay families are not freshly rerun here.

**DIAGNOSTIC, NOT GRAPH REALIZATION:** the necessary-condition envelope has minima 8 and 13 over all labelled d=5 and d=6 tight graphs, with 40 and 60 attaining masks. The d=6 minimum is retained as diagnostic evidence, not an independently promoted strengthened theorem or an attainability claim.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Previous candidate unions, audits and state3349 keep their trust boundaries. No canonical catalogue scan, workflow launch, q-enumeration or promotion.

**PRESERVATION:** project/research/general_n/2026-09-17-defect-six-v1/ now contains THEOREM.md, a byte-identical prerequisite treatment, complete Python/C++ sources, replay driver, exact summary and replay report. STRUCTURAL_REVIEW.md is updated; its preceding version is preserved in the package. The download contains full compressed inputs/decisions and a checksum manifest. Those raw streams regenerate from source; their separate GitHub upload is not claimed.

**UNPRESERVED WORK:** None for this theorem, verification implementation or reported results after remote confirmation. Raw evidence copies are supplied in the download and regenerate deterministically from the published code. Historical archive work is not a hidden dependency of this package.

**DEFERRED ADMIN:** older archive transfers, PR #2 and unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: analyze d=5,D=8 using the actual support-threat cover and the equality conditions of the charge, rather than the scalar envelope alone. Determine whether the low-cost exceptional supports can protect every tight edge simultaneously. Exact-block coverage beyond this scoped theorem remains a separate essential obligation. Preserve the first result or obstruction before extending the unit.
<!-- CURRENT-STATUS:END -->
