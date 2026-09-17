# Current structural review — 17 September 2026

**Current five-label result: [Five-label defect eleven is impossible](project/research/general_n/2026-09-17-d5-defect11-closure-v1/THEOREM.md).** Its immediate prerequisite is the checked [exact support-cover theorem](project/research/general_n/2026-09-17-d5-exact-cover-v1/THEOREM.md), which itself rests on the pair-covered critical-edge theorem.

Under the whole-level exact-block hypothesis |T|=|H|=5, the current internally checked conclusion is

    D >= 12,
    W >= 37,
    extras => W >= 57.

The preceding exact support cover gave D>=11. Equality at eleven would force every actual exception to attain its cheapest support price and therefore beta=0. Independent exact enumeration shows that every one of the 25 auxiliary D=11 minimizers requires a singleton tight support in every cheapest cover: three singleton supports for K5 minus one edge and one for the two-missing-edge matching family.

Such a singleton must be a positive-demand K-label. But beta=0 forces its selected source into a full receiver pool, whose residual set contains only tight labels. The residual-union implication then bounds its F-degree by 1+4=5, whereas five residual high incidences plus positive demand require F-degree at least 6. This contradiction eliminates D=11.

Python and C++ independently enumerate all 1024 labelled tight graphs and agree byte-for-byte on the lexicographic `(cover cost, singleton count)` row stream; SHA256 `858941a3e47b59631433e61bd8ced65f6a9e7cb302a0de0281201e6074e0df77`.

The parameter-wide predecessor remains valid: pair coverage for D<d(d-2), the critical-edge support charge, and the quadratic exact-block bound. **Status remains internal candidate mathematics:** exact-block coverage, D=12 attainability, sharpness, novelty and independent review are open. No catalogue promotion or unrestricted proof is claimed.

## Next target

Analyze D=12 while tracking the one unit of slack that can now appear outside the full receiver pools. The beta=0 shortcut used at eleven is no longer automatic. The correct next object is the joint support-cover / exact-row / selected-source feasibility problem, not a fresh survivor scan.

Canonical counts remain 4626 exclusions / 952 survivors / 3632 whole-state closures. Use [CURRENT_STATE.md](CURRENT_STATE.md) as the operational source of truth; all earlier proofs and failed routes remain preserved.
