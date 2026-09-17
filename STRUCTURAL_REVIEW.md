# Current structural review — 17 September 2026

**Current five-label result: [Five-label exact support cover forces defect at least eleven](project/research/general_n/2026-09-17-d5-exact-cover-v1/THEOREM.md).** Its prerequisite is the checked [pair-covered interface and critical-edge charging theorem](project/research/general_n/2026-09-17-defect-six-v1/THEOREM.md), which in turn includes the exact graph-to-representative scope and links to the preceding treatment.

Under the whole-level exact-block hypothesis |T|=|H|=5, criticality turns the actual exceptional supports into a weighted cover of the ten possible tight edges. Every K-support pays at least max(0,4-|S|) units of L and every off-pool residual support pays at least that much beta. Exact enumeration of all 1024 labelled tight graphs and all 31 nonempty supports gives

    D >= 11,
    W >= 36,
    extras => W >= 56.

The two independent implementations produce the same complete 1024-row stream, SHA256 `80aa3a20b985dab08080c5d645bdf44cadb9498ec3be636219a670e35e4943c9`. The only auxiliary minimum types are K5 minus one edge, and the degree sequence (3,3,3,3,4) with two missing edges. These are necessary tight-graph shapes, not original-graph realizations.

The parameter-wide predecessor remains valid: pair coverage for D<d(d-2), the critical-edge inequality `E_h(Q)<=L+floor(L/h)+beta`, and the quadratic exact-block bound `D>=ceil(d(d-1)/4)`. The previous five-label D>=8 bound is superseded by D>=11.

**Status:** internally checked candidate mathematics. Exact-block existence/coverage, attainability of D=11, sharpness, novelty and independent mathematical acceptance remain open. No catalogue promotion or unrestricted Murty-Simon proof is claimed.

## Review focus and next target

Review first the necessity of the support-threat cover in the predecessor, then the cheap support price `max(0,4-|S|)` and the exact finite union-cover calculation. The next mathematical unit is to impose the full exact-row identities, demand types and receiver-pool multiplicities on the two auxiliary D=11 minimum families; a minimum set cover is necessary but not sufficient for realization.

Canonical counts remain 4626 exclusions / 952 survivors / 3632 whole-state closures. The operational source of truth is [CURRENT_STATE.md](CURRENT_STATE.md); all earlier proofs and failed routes remain preserved.
