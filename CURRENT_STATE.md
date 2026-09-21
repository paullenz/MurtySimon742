# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-21  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `VERIFIED_INTERNAL_Q3_AT_LEAST_THREE_STAR_CENTRES`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `03590dd66568c793605647febc749f6dd075385f`; opposite-centre obstruction and independent raw necessary-code checker.

LAST VERIFIED RESULT: a uniform raw-criticality proof excludes all one- and two-centre star supports under the Q3 antipodal-transversal hypothesis, regardless of multiplicity. All 28 two-centre supports pass independent finite-type replay. Nonempty support needs at least three distinct centres; external review remains open.

UNPRESERVED WORK: None. Mathematical status unchanged at entry; hourly continuity correction and 14:00 slot ledger are preserved with this handoff.

DEFERRED ADMIN: README top-level status still needs a compact pointer to the completed Q3 odd-halfcube classification, star certificate table and new minimal two-star-class exact-M closure. Defer the larger README rewrite to the next safe preservation window rather than risk overlap.

NEXT ACTION: classify three-centre supports by cube symmetry and test whether mandatory spoke witnesses force diameter-incompatible coordinate populations.
<!-- CURRENT-STATUS:END -->

## Current Q3 graph-level results

The 16 antipodal transversals are exactly eight odd affine halfcubes plus eight stars `S_c=N_Q[c]`. The complete local certificate table, star fan and no-singleton theorem are preserved under `project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/`.

### Star-side structure

- Every star must bridge its unique undominated antipode.
- Coordinate-halfcube bridging forces at least one additional star nonneighbour; opposite-parity bridging forces three distinct star nonneighbours.
- An incident A-edge at star `S_c` can be certified on the star side only by: direct opposite-centre endpoint; the unique B-target `bar c` (capacity one); or a third-A target of code `S_bar(c)` creating an explicit opposite-centre nonedge.
- Hence `E_nonopp <= |S|+2M_opp` for the star-star subgraph.

Files: `Q3_STAR_BRIDGE_PROPAGATION_AND_NONNEIGHBOR_BILL.md`, `Q3_STAR_INCIDENT_A_EDGE_CERTIFICATE_CLASSIFICATION.md`, `Q3_STAR_STAR_EDGE_ORIENTATION_CHARGE.md`.

### Two opposite star centres

If star codes use only one antipodal centre pair X,Z, every same-centre edge injects into a missing X-Z pair, giving

`e(G[X∪Z]) <= |X||Z| <= floor(|S|^2/4)`.

File: `Q3_TWO_OPPOSITE_STAR_CLASSES_MANTEL_BOUND.md`.

### Exact minimal-face closure

If the A-code population consists exactly of p vertices of `S_c`, q vertices of `S_bar(c)`, and exactly one vertex in each of the six coordinate-halfcube codes, with no parity / third star centre / extra coordinate multiplicity, then with `s=p+q`, `a=s+6`:

`e(S)<=floor(s^2/4)`, `e(W,S)<=3s`, `e(W)<=6`.

Therefore

`e(A)<=floor(a^2/4)-3`,

and since `e(G)=20+4a+e(A)` while `M(n)=floor(a^2/4)+4a+17`,

`e(G)<=M(n)`.

This closure survived same-session hostile replay. Files: `Q3_TWO_STAR_CLASSES_SIX_COORDINATE_WITNESS_TAX.md`, `Q3_MINIMAL_TWO_STAR_CLASS_FACE_EXACT_M_BOUND.md`, `Q3_MINIMAL_TWO_STAR_CLASS_FACE_HOSTILE_REPLAY.md`.

### Arbitrary coordinate multiplicity: preserved inputs

- `E_noncomp(C)<=2M_comp(C)`;
- within each fixed coordinate direction, `e(C_i^0∪C_i^1)<=|C_i^0||C_i^1|`;
- with only star centres c and bar(c), all six coordinate classes are nonempty and `missing(S,T)>=3s`, equivalently `e(S,T)<=s(t-3)`.

Files: `Q3_COORDINATE_CODE_GLOBAL_SUBSTITUTION_CHARGE.md`, `Q3_TWO_STAR_CLASSES_ARBITRARY_COORDINATE_MIXED_TAX.md`.

Remaining uncontrolled pieces: cross-direction coordinate density, parity/star-parity interactions, and the third-star-centre branch.

## Latest adversarial audit

`project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

The audit verified raw same-code criticality and ordered witness injection at stated scope, retained corrected H-U machinery only under its rigid one-code hypotheses, kept the old H-U private-foot route invalidated, and elevated graph-level realizability/non-realizability as the dominant risk. The Q3 programme is the active response.

## Latest invocation telemetry

Full record: `project/research/session_logs/2026-09-21/2026-09-21T13-30-18+01-00-a.md`.

- actual start: **2026-09-21 13:30:18 BST**;
- preservation cutoff: **2026-09-21 13:55:38 BST**;
- forward-research stop: **2026-09-21 13:49:16 BST**;
- preservation complete: **2026-09-21 13:51:15 BST**;
- wall-clock span: **22m52s (22.8667 min)**;
- forward-research span: **18m58s (18.9667 min)**;
- substantive units: **9**;
- stop reason: forward exploration stopped for preservation with 6m22s remaining before cutoff after a late start;
- >=50-minute target: **not applicable**, because only 25m20s existed from actual start to preservation cutoff.

## Mandatory constraints

- Preserve `X_3` as mandatory hostile control.
- Do not promote the minimal two-star-class theorem beyond its explicit code-population scope.
- Independently audit any extension using extra coordinate multiplicity / parity / third star centres before treating it as graph-level closure.
- Do not revive invalidated H-U private-foot arguments, uncorrected superconstant formulas, superseded residual-one wedges or repeated-code reverse-gamma branches.
- Treat all 0.53-wedge results as conditional on the rigid complete one-code interface.
- Finite scans are diagnostics, not substitutes for structural proof.
- Every run must finalize one telemetry record with measured timestamps and no inferred duration.

## Hourly continuity correction — effective 21 September

The scheduled trigger is the accounting unit; re-entry never resets the start, target or cutoff. No eight-minute early-stop permission exists. All prior late-segment target exemptions must be reconciled at slot level. Preserve missing historical timing as UNVERIFIED. Full correction and the 09:00 regression: `project/research/session_logs/2026-09-21/HOURLY_CONTINUITY_CORRECTION.md`.

Current slot: actual start 14:01:25 BST, cutoff 14:55:38 BST, research stop/preservation completion pending, units 0, status IN_PROGRESS. Ledger: `project/research/session_logs/2026-09-21/2026-09-21T14-01-25+01-00.json`.

## New star-support obstruction

`project/research/post_ms/2026-09-21-q3-star-support-v1/TWO_ANTIPODAL_CENTRES_IMPOSSIBLE.md` proves a stronger candidate than the prior minimal-face bound: arbitrary coordinate/parity multiplicities do not rescue one antipodal pair of star centres. All coordinate vertices become A-isolated; both opposite star types force incompatible opposite coordinate classes. Older narrower statements remain preserved. Unit 1 completed 2026-09-21T14:08:16+01:00.

Independent replay: `project/research/post_ms/2026-09-21-q3-star-support-v1/STAR_SUPPORT_CHECK_RESULTS.json`. Exploratory necessary-relation outputs also narrow distance-one and distance-two star pairs; their full exclusion remains the next hand-proof task. Unit 2 completed 2026-09-21T14:11:22+01:00.

## Two-centre closure

`project/research/post_ms/2026-09-21-q3-star-support-v1/AT_LEAST_THREE_STAR_CENTRES.md` gives a uniform separating-coordinate proof for any two distinct centres. This closes the arbitrary multiplicity/parity extension requested by the predecessor. Unit 3 completed 2026-09-21T14:13:22+01:00.
