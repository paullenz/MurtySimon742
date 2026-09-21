# CURRENT_STATE.md

Canonical repository: `paullenz/MurtySimon742`. Date: 21 September 2026.

Active target: the eventual / sufficiently-large second-extremal problem around M(n)=floor((n-1)^2/4)+1. The general theorem and a uniform threshold remain open. X3 (12 vertices,32 edges,M(12)=31) remains mandatory. Do not revive the false all-order conjecture or the closed mixed {4,5} ladder.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `FIVE_CENTRE_QUADRATIC_FAMILY_CANDIDATE`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `0dc97e3c4447c7474fa56042fe8b66ada75d69d3`.

LAST VERIFIED RESULT: The entire exactly-four-star-centre Q3 antipodal-transversal branch is density-closed and hostile-replayed. Five-centre supports have three cube orbits. In the one-copy slice only the complement-{2,2,2} orbit is feasible, with a unique minimum n=21,m=77 model. Its P1-twin extension is proved for every q>=1. A complete P0--P1 two-parameter extension passes all 400 direct D2C checks for 1<=r,q<=20 and has n=20+r+q, m=rq+4(r+q)+73, but arbitrary-parameter criticality is not yet proved.

UNPRESERVED WORK: None after this invalidation/repair checkpoint.

DEFERRED ADMIN: Broad historical cleanup; it does not block the raw matching-one attack.

NEXT ACTION: Prove the two-parameter five-centre complete P0--P1 candidate by a uniform twin-extension witness invariant. Its balanced gap below M(n) is positive linear. Do not infer arbitrary multiplicity from the 8-by-8 scan, and do not generalize either negative one-copy orbit to larger populations.
<!-- CURRENT-STATUS:END -->

## Reviewable current package

`project/research/post_ms/2026-09-21-q3-star-support-v1/THEOREM_AND_REVIEW_INDEX.md` is the compact theorem/proof/dependency map.

- One, two and three star centres are impossible at the stated scope; the 56 nonplane four-centre supports are impossible for arbitrary multiplicities.
- The 14 remaining four-centre supports are six coordinate faces, six opposite-edge planes and two parity planes. Their symmetry coverage was independently rechecked. The sharp order minimum 19 holds for exactly four centres, not for all larger supports.
- The parity-plane construction at order 19 has 66 edges and all explicit deletion witnesses. Its balanced extension has gap floor((9n-139)/2). The earlier six-coordinate family has gap 5n-82. The former is denser only for n>=26, ties at 24,25 and is less dense at 20 through 23. Exact formulas were unchanged; overbroad prose was corrected.
- `OPPOSITE_EDGE_PARITY_FACTOR_REDUCTION.md` gives the latest reduction. For a fixed collapsed core of order n0, the balanced parity-expansion gap increases by exactly n0-11 for each two added vertices. Existence of that core remains open.
- Coordinate-face support forces its outward coordinate code and excludes the inward one; n>=20. Multiple outward-code copies matter. The bounded 1200-trial search supplies no nonexistence theorem.

## Actual-graph evidence and audit alignment

Latest mandatory audit: `project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

This session followed its priority on raw criticality and actual graph realizability. It did not extend the conditional 0.53 rigid-Hall machinery or substitute scalar feasibility for graph existence. The raw local certificate calculus now has a soundness induction for type pruning and exact agreement with 28,934 independent edge-deletion reachability checks across 916 populations. Arbitrary generated populations are not asserted to be D2C.

The actual five-coordinate and six-coordinate families supply 30 and 22 direct D2C controls respectively. The prior independent Hall verifier passes 108 root-policy runs including X3, but all 105 new fixture runs have p=0 at maximum-degree roots. No positive rigid cut was added. `MAXIMUM_ROOT_RESIDUAL_LEDGER.md` proves this for the whole balanced five-coordinate family and gives Q=13 with exact positive linear residual defect. Its Q3 construction root is not maximum-degree and has negative lambda.

The finite source-tuple capacity theorem remains conditional on distinct physical-source identity and global selected (source,coordinate) uniqueness at the required interface. Local certificate validation does not establish those global premises. Keep exact pair-local Ccap_P, (ONE) and (CROWD) conditional; keep the four-exception gate subordinate.

## Preserved earlier work and trust limits

Earlier Q3 code classification, star fan, bridge charges and odd-halfcube results remain under `project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/`. Opposite-star-pair density bounds are now superseded operationally by the stronger nonrealizability theorem; their historical proofs remain intact. The old H-U private-foot route and repeated-code reverse orientation remain invalidated. No theorem for five through eight centres, nontransversal codes, general sufficiently-large graphs or uniform n0 is claimed.

## Hourly continuity correction and telemetry

The scheduled slot is the accounting unit. Re-entry and compaction do not reset its start, target or cutoff. No eight-minute stopping permission exists. Missing historical boundaries remain UNVERIFIED; do not fabricate them from unit or commit counts. The 09:00/09:28/09:57 regression and exact correction are preserved in `project/research/session_logs/2026-09-21/HOURLY_CONTINUITY_CORRECTION.md`. The old 13:30 report's 'target not applicable' language is also superseded operationally: short/late segments must be reconciled at slot level.

Current slot ledger: `project/research/session_logs/2026-09-21/2026-09-21T14-01-25+01-00.json`.

- Earliest actual start: 14:01:25 BST; research start recorded at 14:05:42.
- Same-slot re-entry: 14:33:47 BST; post-compaction clock check: 14:37:59. Neither resets the slot.
- Preservation cutoff: 14:55:38 BST; measured forward-research stop: 14:55:57 BST (19 seconds after cutoff; deadline was not advanced).
- Verified continuation research span: 22m10s (22.1666666667 min). Full-slot forward-research span: UNVERIFIED because the preceding segment has no recorded stop. The 50m15s outer research envelope is not credited as a verified union.
- Substantive units: 15. >=50-minute target: UNVERIFIABLE. Telemetry compliance: NONCOMPLIANT because the full-slot research duration cannot be verified; this does not imply that the earlier segment did no work or identify a cause of re-entry.
- Preservation complete: 14:57:52 BST; recorded final-report time: 2026-09-21T14:58:42+01:00; wall-clock session span: 57m17s (57.2833333333 min). Preservation span: 1m55s. Full-slot forward-research span remains UNVERIFIED; verified continuation is 22m10s.
- Stop reason: reached the valid preservation cutoff; stopped exploration and handed off the reduced opposite-edge-plane core.


### Current 15:00 slot

Full telemetry: `project/research/session_logs/2026-09-21/2026-09-21T15-02-03+01-00.json`.

- Actual start: 15:02:03 BST; preservation cutoff: 15:55:38 BST.
- Forward research: 15:02:46--15:55:44 BST = 52m58s (52.9666666667 min), continuously documented across same-slot context re-entry.
- Preservation complete after late-segment reconciliation: 15:59:30 BST; wall-clock slot span 57m27s (57.45 min); verified preservation intervals total 1m33s (1.55 min).
- Substantive units: 26.
- Stop reason: reached the valid cutoff after the last bounded hostile-core replay; stopped exploration for preservation.
- Late same-slot segment: 15:58:54 BST, after cutoff; zero forward research, preservation/reconciliation only. Earlier verified research total and target result remain unchanged.
- >=50-minute target: MET.

### Current 17:00 slot

Full telemetry: `project/research/session_logs/2026-09-21/2026-09-21T17-03-31+01-00.json`.

- Actual start: 17:03:31 BST; preservation cutoff: 17:55:38 BST.
- Same-slot context re-entry: 17:36:13 BST; it did not reset the start, ledger, cutoff or target.
- Forward research: 17:04:05--17:52:05 BST = 48m00s (48.0 min).
- Preservation complete: 17:53:22 BST; wall-clock span through preservation 49m51s (49.85 min); preservation span 1m17s (1.2833333333 min).
- Substantive units: 10.
- Stop reason: stopped forward exploration at 17:52:05 for end-of-slot preservation after using the shortened window through the final minutes before the valid cutoff.
- >=50-minute target: NOT MET. Actual entry left 52m07s before cutoff, below the normal 55-minute allocation; the verified research span is reported without adding undocumented time. This is a shortened-window shortfall, not the strict normal-window early-stop classification.

### Current 18:00 slot

Full telemetry: `project/research/session_logs/2026-09-21/2026-09-21T18-00-38+01-00.json`.

- Actual start: 18:00:38 BST; preservation cutoff: 18:55:38 BST.
- Same-slot context re-entries: 18:08:49 and 18:43:07 BST; neither reset the start, ledger, cutoff or target.
- Forward research: 18:01:41--18:51:50 BST = 50m09s (50.15 min).
- Substantive units: 15.
- Stop reason: reached and slightly exceeded the 50-minute target, then stopped at a natural verified five-centre family checkpoint for preservation.
- >=50-minute target: MET.
