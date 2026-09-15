# Canonical forced-core completed discovery and full independent-audit staging

This package freezes the completed output of GitHub Actions run `34950746007` and prepares the promotion-quality independent closure audit. It is research/audit evidence only until the independently structured scanner has reproduced all 170 candidate exclusions.

## Completed primary discovery

- Promoted relational survivor base entering this route: **952** states.
- Stored witnesses retained by forced core: **646**.
- Stored-witness failures exhaustively rescanned: **306**.
- Rescanned survivors: **136**.
- Candidate forced-core exclusions: **170**, all in N34; **0** in N35.
- Therefore **782/952** states are now explicitly known to survive this route, while **170/952** are promotion candidates.
- Canonical public totals remain **4,626 exclusions / 952 survivors / 3,632 whole-state closures** until promotion review.

The completed run agrees with all earlier preserved evidence: all 124 locally certified replacement witnesses occur among the 136 survivors, and all 24 previously independently enumerated closure cases occur among the 170 candidate exclusions. The exhaustive remote run supplied 12 additional N34 survivor witnesses: `2454, 3145, 4453, 4618, 5163, 5672, 5972, 7664, 7851, 7927, 9014, 9849`.

## Promotion gate

The audit workflow reconstructs `CANDIDATE_INPUT.txt` exactly by filtering the frozen 306-state plan to the completed primary exclusions. It runs the independently structured equal-rho type-multiplicity scanner from `forced-core-canonical-audit-v1` on all 170 states and compares 17 proof-relevant fields exactly: profile total, every successive fail/pass stage, forced-core rejection split, and terminal status.

The workflow preserves both successful and failed audit evidence on the research branch. No closure is to be promoted unless the full comparison is exact and the resulting ledger is reviewed. External mathematical review remains OPEN.
