# Current structural review — 17 September 2026

**Start with [Pair-covered interfaces and critical-edge charging](project/research/general_n/2026-09-17-defect-six-v1/THEOREM.md).** The preceding graph-to-representative construction and exact accounting are included byte-for-byte as the [prerequisite treatment](project/research/general_n/2026-09-17-defect-six-v1/PREREQUISITE_STRUCTURAL_TREATMENT.md).

Under the whole-level exact-block hypothesis |T|=|H|=d, small intrinsic defect forces each tight pair to share an interface neighbour. The new necessary inequality is

    E_h(Q)<=L+floor(L/h)+beta.

It yields D>=ceil(d(d-1)/4) for all d>=3. At d=5, the separate hand corollary strengthens the current bound to **D>=8, W>=33, or W>=53 with extra high-source selections**. These results do not assume a single interface label adjacent to every tight vertex.

**Status:** internally checked candidate mathematics within an explicit exact-block scope. Unrestricted exact-block coverage, sharpness, novelty and independent mathematical acceptance remain open. No catalogue promotion or global Murty–Simon proof is claimed.

## Reproduce the new checks

In project/research/general_n/2026-09-17-defect-six-v1/, run:

    python3 verify_published.py

Python 3.10+ and a C++17 compiler suffice; no network or third-party Python package is needed. The [exact summary](project/research/general_n/2026-09-17-defect-six-v1/CHECK_SUMMARY.json) contains 121549 matching Python/C++ records, including 87685 local graphs and 33864 auxiliary tight graphs, plus row and support-charge arithmetic checks. The [source-only replay](project/research/general_n/2026-09-17-defect-six-v1/FRESH_REPLAY.json) reproduced the pinned streams. Both implementations were written by the same assistant; they are not external independent review.

These tests include pair-covered interfaces without an all-tight common label, failures of essential premises, and examples showing that a support threat is not sufficient for actual criticality. No original exact-block graph census is claimed. Older verification families were not rerun in this package. Full generated gzip evidence is in the separate download and is reproducible from the published sources.

## Review focus and next obligation

Review the full-pool protection argument, the necessity rather than sufficiency of the support-threat cover, and the loss charged to each support. Then review the pair-coverage counting and the quadratic and five-label corollaries. The next mathematical target is **d=5,D=8**, using the actual threat-cover equality conditions, not merely the passing scalar envelope.

Canonical counts remain 4626 exclusions / 952 survivors / 3632 whole-state closures. For the operational handoff read [CURRENT_STATE.md](CURRENT_STATE.md). The [preceding structural review entry](project/research/general_n/2026-09-17-defect-six-v1/PREVIOUS_STRUCTURAL_REVIEW.md) and all its earlier proof and verification links are retained for provenance; its D=6 next target is superseded here. No old proof, failed route or fixed-order reviewer package is removed.
