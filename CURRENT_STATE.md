# CURRENT_STATE.md

Canonical repository: `paullenz/MurtySimon742`. Date: 21 September 2026.

Active target: a genuinely independent proof of Erdős #742 / the Murty–Simon inequality e(G)<=floor(n^2/4), preferably with the equality characterization. Forward priority is the project’s own complement / residual / Hall / profile / realizability route, not a reconstruction of the external e+disj+X proof. First live strip: n/2 < Delta(G) < 7n/12, using the elementary Delta<=n/2 bound on one side and the preserved internally checked candidate 7/12 theorem on the other. The 7/12 theorem remains candidate/internal-review mathematics. A 24-focused-session go/no-go gate now applies. Prior eventual-D2C work remains preserved but is no longer the active forward objective.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `INDEPENDENT_742_PIVOT`

WORK MODE: `MATH`

PIVOT COMMIT: `5825c203da78ecaefaa63568f0883de25518df9f`.

ACTIVE OBJECTIVE: Close the Murty–Simon inequality independently of the external `Erdos742/Erdos742` proof, preferably including equality uniqueness. The first attack is the maximum-degree strip
[
n/2 < \Delta(G) < 7n/12.
]

INHERITED BOUNDARY RESULTS:
- `Delta<=n/2` gives `e(G)<=n^2/4` immediately by degree sum.
- Preserved candidate theorem: `n>=6` and `Delta>=7n/12` imply `e(G)<floor(n^2/4)`; internal exact audits are green but independent/external review remains open.

FIRST ATTACK: Re-open the canonical 7/12 profile-integral proof, identify the exact first obstruction to lowering the threshold, sharpen toward `1/2`, and distinguish scalar/profile survivors from graph-realizable configurations. Use newer raw-criticality / realizability machinery against non-realizable survivor families. Treat balanced complete bipartite graphs as the expected equality boundary.

SUCCESS SIGNALS FOR FIRST 24 FOCUSED SESSIONS: (1) any strict threshold improvement below 7/12; (2) a new rigorous rigidity/realizability theorem materially shrinking the strip; or (3) a finite-dimensional obstruction with a credible closure path. If none occurs, explicitly reassess rather than continue by inertia.

HISTORICAL STATUS: The five-centre / eventual-D2C programme and all related audits, controls, failures and candidate results remain preserved and reusable, but are now subordinate to the independent-#742 target.
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
- Preservation complete: 18:52:55 BST; wall-clock span through preservation 52m17s (52.2833333333 min); preservation span 1m05s (1.0833333333 min).
- Substantive units: 15.
- Stop reason: reached and slightly exceeded the 50-minute target, then stopped at a natural verified five-centre family checkpoint for preservation.
- >=50-minute target: MET.


### Completed 19:00 D2C continuation (subordinate after independent-#742 pivot)

This slot completed and hostile-replayed the five-centre positive-control family package before discovering the newer concurrent pivot above. The results remain preserved as reusable structural work, but the next session must follow the independent-#742 objective rather than continue the subordinate D2C line by inertia.

Full telemetry: `project/research/session_logs/2026-09-21/2026-09-21T19-01-53+01-00.json`.

- Actual start: 19:01:53 BST; preservation cutoff: 19:55:38 BST.
- Forward research: 19:02:39--19:53:30 BST = 50m51s (50.85 min).
- Preservation complete: 19:54:27 BST; wall-clock span 52m34s (52.5666666667 min); preservation span 0m57s (0.95 min).
- Substantive units: 16; >=50-minute target: MET.
- Stop reason: reached the target and stopped at the completed family hostile-audit and bounded negative-orbit checkpoint for preservation.


## 20:00 independent-#742 focused session 1

Candidate/internal result: for every n>=6, Delta(G)>=250n/429 implies e(G)<floor(n^2/4). The proof uses the shared graph-to-profile spine, the sharpened exact scalar certificate f(x)<121/1569, a continuous assembly for a>=65, and exact threshold-capacity closure of the eight exceptional a-values. This strictly improves 7/12, but remains internally checked and not externally reviewed.

The exact first scalar/Hall obstruction is now isolated: an asymptotic uniform-demand plateau survives scalar capacity, full selected Hall, graphical margins, and simultaneous selected/residual incidence. Raw criticality nevertheless forces a new selected-signature union law. It implies a positive-density family of selected label pairs with F-codegree at least a/5. The next task is a raw-criticality upper bound or classification for that family; this is the first graph-realizability obstruction beyond the plateau.

Telemetry: actual start 2026-09-21T20:00:28+01:00; cutoff 2026-09-21T20:55:38+01:00; forward-research stop 2026-09-21T20:52:59+01:00; forward-research span 51.35 minutes; 12 substantive units. Full record: project/research/session_logs/2026-09-21/2026-09-21T20-00-28+01-00.json.
