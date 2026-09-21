# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-21  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `FORWARD_2026_09_21_Q3_STAR_MINIMAL_FACE_CLOSURE`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: 21 September daily red-team audit; README; prior CURRENT_STATE; recent Q3 commits through `59aa405325a547835ad30bbc1ac302332283f503`; current-session telemetry and all nine new theorem/audit units.

LAST VERIFIED RESULT: inside the raw Q3 antipodal-transversal branch, the minimal face with exactly two opposite star-centre classes plus exactly one vertex in each of the six coordinate-halfcube codes satisfies `e(G)<=M(n)`. The closure survived an independent same-session hostile replay by fresh 16-code enumeration, domination/disjointness checks, physical injection replay and floor arithmetic. This result is graph-level within its explicit code-population scope and uses no conditional rigid-cut/Hall machinery.

UNPRESERVED WORK: none. All nine substantive units, the hostile replay, telemetry and this handoff are committed.

DEFERRED ADMIN: README top-level status still needs a compact pointer to the completed Q3 odd-halfcube classification, star certificate table and new minimal two-star-class exact-M closure. Defer the larger README rewrite to the next safe preservation window rather than risk overlap.

NEXT ACTION: extend the minimal two-star-class closure to arbitrary coordinate multiplicity using the preserved exact inputs `e(S)<=pq`, `missing(S,T)>=3s`, `E_noncomp(C)<=2M_comp(C)` and the fixed-direction coordinate product bounds. The uncontrolled terms are cross-direction coordinate density plus parity/star-parity interactions. In parallel, treat a third star-centre class as the other principal escape. Do not return to conditional 0.53-wedge sharpening unless the graph-level Q3 route stalls.
<!-- CURRENT-STATUS:END -->

## Current graph-level Q3 checkpoint

The Q3 programme is the active response to the latest red-team priority: attack actual D2C realizability/non-realizability directly rather than stack further conditional scalar inequalities.

### Odd-halfcube / X3 controls

The Q3 odd-affine-halfcube palette and explicit dense parity-bridge family remain preserved as graph-level controls. `X_3` remains mandatory. The complete odd-halfcube palette classification should still receive independent external/daily-audit replay before public promotion.

### Full antipodal-transversal universe

The 16 antipodal transversals are exactly the eight odd affine halfcubes plus the eight stars `S_c=N_Q[c]`. The complete local A-B certificate table and star fan are preserved in:

- `project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/Q3_TRANSVERSAL_LOCAL_CERTIFICATE_TABLE.md`;
- `Q3_ANTIPODAL_TRANSVERSAL_STAR_FAN.md`;
- `Q3_NO_SINGLETON_STAR_THEOREM.md`.

### New star-side structure

Current-session raw-criticality results:

- every star must bridge its unique undominated antipode;
- coordinate-halfcube bridging forces at least one additional star nonneighbour;
- opposite-parity bridging forces three distinct star nonneighbours;
- star-star bridging can only use a centre at Hamming distance 2 or 3;
- for an incident A-edge at star `S_c`, x-side certification is exactly: direct to opposite-centre star; the unique B-target `bar c` (capacity one); or a third-A target of code `S_bar(c)` creating an explicit opposite-centre nonedge.

Files:

- `Q3_STAR_BRIDGE_PROPAGATION_AND_NONNEIGHBOR_BILL.md`;
- `Q3_STAR_INCIDENT_A_EDGE_CERTIFICATE_CLASSIFICATION.md`.

### Star-star edge charge / two-centre Mantel theorem

If `M_opp` counts missing opposite-centre star pairs and `E_nonopp` non-antipodal-centre star edges, then

`E_nonopp <= |S| + 2 M_opp`.

If the star population uses only one antipodal centre pair X,Z, every same-centre edge injects into a missing X-Z pair, so

`e(G[X∪Z]) <= |X||Z| <= floor(|S|^2/4)`.

Files:

- `Q3_STAR_STAR_EDGE_ORIENTATION_CHARGE.md`;
- `Q3_TWO_OPPOSITE_STAR_CLASSES_MANTEL_BOUND.md`.

### Exact closure of the minimal two-star-class face

Assume the A-code population consists exactly of p vertices of `S_c`, q vertices of `S_bar(c)`, exactly one vertex in each of the six coordinate-halfcube codes, and no parity / third star centre / extra coordinate multiplicity. Put `s=p+q`, `a=s+6`.

Raw certificate geometry gives

`e(S)<=floor(s^2/4)`,

`e(W,S)<=3s`,

`e(W)<=6`.

Hence

`e(A)<=floor(s^2/4)+3s+6 = floor(a^2/4)-3`.

Since `e(G)=20+4a+e(A)` and `M(n)=floor(a^2/4)+4a+17` for `n=a+9`,

`e(G)<=M(n)`.

This closure survived same-session hostile replay. Files:

- `Q3_TWO_STAR_CLASSES_SIX_COORDINATE_WITNESS_TAX.md`;
- `Q3_MINIMAL_TWO_STAR_CLASS_FACE_EXACT_M_BOUND.md`;
- `Q3_MINIMAL_TWO_STAR_CLASS_FACE_HOSTILE_REPLAY.md`.

### First extension beyond the minimal face

With arbitrary coordinate multiplicity:

- `E_noncomp(C)<=2M_comp(C)`;
- within each fixed coordinate direction, `e(C_i^0∪C_i^1)<=|C_i^0||C_i^1|`;
- if star centres remain only c and bar(c), all six coordinate classes are nonempty and `missing(S,T)>=3s`, equivalently `e(S,T)<=s(t-3)`.

Files:

- `Q3_COORDINATE_CODE_GLOBAL_SUBSTITUTION_CHARGE.md`;
- `Q3_TWO_STAR_CLASSES_ARBITRARY_COORDINATE_MIXED_TAX.md`.

Remaining uncontrolled pieces: cross-direction coordinate density, parity/star-parity interactions, and the third-star-centre branch.

## Latest adversarial audit — 21 September 2026

Full report: `project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

The audit verified raw same-code criticality and ordered `(source,witness)` injection at stated scope, retained the corrected H-U B-layer/capacity machinery under rigid one-code hypotheses, kept the old H-U private-foot coordinate-slice chain invalidated, and identified the unexercised rigid-cut realizability interface as the dominant graph-level risk.

## Latest invocation telemetry

Full record: `project/research/session_logs/2026-09-21/2026-09-21T13-30-18+01-00-a.md`.

- actual start: **2026-09-21 13:30:18 BST**;
- preservation cutoff: **2026-09-21 13:55:38 BST**;
- forward-research stop: **2026-09-21 13:49:16 BST**;
- preservation complete: **2026-09-21 13:51:15 BST**;
- wall-clock span: **21m41s (21.6833 min)**;
- forward-research span: **18m58s (18.9667 min)**;
- substantive units: **9**;
- stop reason: forward exploration stopped for preservation with 6m22s remaining before cutoff after a late start;
- >=50-minute target: **not applicable**, because only 25m20s existed from actual start to preservation cutoff.

## Mandatory constraints

- Preserve `X_3` as mandatory hostile control.
- Do not promote the minimal two-star-class theorem beyond its explicit code-population scope.
- Independently audit any extension using extra coordinate multiplicity / parity / third star centres before treating it as graph-level closure.
- Do not revive invalidated H-U private-foot arguments, uncorrected superconstant formulas, superseded residual-one wedges, or repeated-code reverse-gamma branches.
- Treat all 0.53-wedge results as conditional on the rigid complete one-code interface.
- Finite scans are diagnostics, not substitutes for structural proof.
- Every run must finalize one telemetry record under `project/research/session_logs/` with measured timestamps and no inferred historical duration.
