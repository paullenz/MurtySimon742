# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-21  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

CHECKPOINT CLASS: `FORWARD_2026_09_21_Q3_HALFCUBE_PALETTE_CLASSIFICATION`

WORK MODE: graph-level hostile reconstruction / negative-control classification, chosen in direct response to the 21 September audit's dominant rigid-realizability risk.

INSPECTED PREDECESSOR: 21 September daily red-team audit; README; prior live state; recent commits through `ed6b9efcc12fb0745f0b6e93d50f7a67b2255a62`; prior 11:00 session telemetry and its X3 extension/blow-up handoff.

LAST VERIFIED RESULT: the explicit X3/Q3 A-layer blow-up theorem survived same-session hostile replay. A stronger graph-level candidate now classifies the entire branch in which every A-to-B neighbourhood is one of the eight odd affine halfcubes of Q3; the complete classification is preserved but should receive an independent hostile replay before being treated as audit-verified.

UNPRESERVED WORK: none of the mathematical results listed below; all theorem notes are committed. Final telemetry fields are completed at session close.

DEFERRED ADMIN: README top-level status still needs a compact pointer to the new Q3 palette classification/dense parity-bridge family; deferred rather than risking a large README rewrite during the preservation cutoff.

NEXT ACTION: independently replay `Q3_HALFCUBE_PALETTE_COMPLETE_CLASSIFICATION.md` edge-deletion case by case; if it survives, use its exact linear-gap maximum as a graph-level control for the triangle-containing eventual problem, then attack the first raw-criticality mechanism allowing a Q3-root A-to-B neighbourhood outside the odd-halfcube palette. Do not spend the next hour merely sharpening the conditional 0.53 scalar wedge unless the graph-level route stalls.

## Current mathematical checkpoint

The previous conditional rigid one-code theorem remains available:

`(r+g0+d)/p >= 0.53-o(1)`

inside the repeated rigid complete one-code interface, with the same caveat that bounded actual-D2C regression has no positive rigid complete Hall-cut fixture with `x>=3`. That theorem is not promoted to graph-level closure.

The new graph-level work instead reconstructs the mandatory X3 control around a root whose neighbourhood is Q3.

### 1. Independent-A Q3 branch is completely classified

If `B=N(v)=Q3` and `A` is independent, raw diameter-two and edge-criticality force every A-to-B neighbourhood to be one of the eight affine halfcubes defined by odd linear forms `100,010,001,111`; opposite orientations cannot coexist; all three coordinate directions are mandatory; the parity direction is optional. Hence this branch is exactly the sparse X3 blow-up family with

`n=9+a`, `m=4n-16`,

and

`M(n)-m=floor((n-9)^2/4)-3`.

Thus only n=12 exceeds M in this branch, and that graph is X3 up to cube automorphism. The proof was hostile-replayed in-session; a real alternative root-A singleton certificate was caught and repaired by ordering the diameter-two domination lemma before the antipodal root-edge argument.

File: `project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/X3_Q3_ROOT_INDEPENDENT_A_CLASSIFICATION.md`.

### 2. A-edge criticality is paid for by opposite halfcube pairs

Within the odd-halfcube palette, every critical A-edge must be certified by an opposite-side A-pair. A fixed physical opposite pair certifies at most two A-edges, giving

`f=e(A) <= 2 P_opp`.

More exactly, if `E_opp` counts opposite-side A-edges and `P_1` opposite-side A-nonedges with exactly one common A-neighbour, then

`f <= E_opp + 2P_1 <= 2P_opp`.

Near M this forces macroscopic opposite-orientation mass; at least half of A asymptotically lies in one linear direction inside this palette branch.

File: `project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/Q3_HALFCUBE_OPPOSITE_PAIR_EDGE_CAPACITY.md`.

### 3. Dense parity-bridge family: an infinite triangle-containing graph-level control

There is an explicit D2C family with one positive coordinate halfcube class in each cube direction, both parity halfcube sides, and a complete bipartite `K_{p,q}` between the two parity A-classes. It has

`m=20+4a+pq`, `Q=12`, `f=pq`, `delta=4a-12-pq`, `r=4a-12`.

Thus quadratic A-density is genuinely realizable while the physical residual count r stays linear. For fixed a, the densest members take exactly three coordinate witnesses and balance the remaining `a-3` vertices across parity sides:

`m_dense=20+4a+floor((a-3)^2/4)`.

The exact gap from M is

- `3a/2-5` for even a;
- `(3a-11)/2` for odd a.

So this infinite triangle-containing family is below M by an asymptotically linear `3a/2` tax, while passing through X3 at n=12.

File: `project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/X3_PARITY_BRIDGE_DENSE_BLOWUP_FAMILY.md`.

### 4. Same-session complete odd-halfcube palette classification — CANDIDATE PENDING INDEPENDENT REPLAY

Raw A-B edge criticality gives two local rules:

- a coordinate halfcube A-vertex can only have A-neighbours of its exact same coordinate halfcube;
- a parity halfcube A-vertex can only have A-neighbours on the opposite parity side.

A-edge criticality then forces every coordinate A-vertex to be A-isolated. Hence opposite coordinate orientations cannot coexist; cube-edge criticality forces one positive orientation in each coordinate direction; and if both parity sides occur, diameter two forces the complete bipartite graph between them.

Therefore the dense parity-bridge family appears to be the **entire D2C branch inside the Q3 odd-halfcube palette**, and the linear-gap formula above is the exact maximum in that branch.

File: `project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/Q3_HALFCUBE_PALETTE_COMPLETE_CLASSIFICATION.md`.

## Latest adversarial audit — 21 September 2026

Full report: `project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

The audit verified raw same-code criticality and ordered `(source,witness)` injection at stated scope, retained the corrected H-U B-layer/capacity machinery under rigid one-code hypotheses, kept the old H-U private-foot coordinate-slice chain invalidated, and identified the unexercised rigid-cut realizability interface as the dominant graph-level risk. The present Q3 work follows that priority by reconstructing actual-D2C negative/control geometry rather than stacking another conditional scalar inequality.

## Latest invocation telemetry

Full record: `project/research/session_logs/2026-09-21/2026-09-21T11-28-31+01-00-a.md`.

- actual start: **2026-09-21 11:28:31 BST**;
- preservation cutoff: **2026-09-21 11:55:38 BST**;
- forward-research stop: **2026-09-21 11:48:30 BST**;
- preservation complete: **PENDING final telemetry close**;
- wall-clock span: **PENDING final telemetry close**;
- forward-research span: **19m59s (19.983 min)**;
- substantive units: **9**;
- stop reason: mandatory preservation phase began with <8 minutes to cutoff at a clean theorem checkpoint;
- >=50-minute target: **not applicable**, because this invocation began late and supplied only 27m07s before the preservation cutoff.

## Mandatory constraints

- Independently hostile-replay the complete Q3 palette classification before promoting it beyond same-session candidate status.
- Preserve `X_3` as mandatory hostile control; the new dense parity-bridge family is an additional infinite triangle-containing control, not a replacement.
- Do not revive invalidated H-U private-foot arguments, uncorrected superconstant formulas, superseded residual-one wedges, or repeated-code reverse-gamma branches.
- Treat all 0.53-wedge results as conditional on the rigid complete one-code interface.
- Finite scans are diagnostics, not substitutes for structural proof.
- Every run must finalize one telemetry record under `project/research/session_logs/` with measured timestamps and no inferred historical duration.
