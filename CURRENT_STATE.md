# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. Latest result: shared block-slack pressure; END-TO-END CI NOW PASSED.** Run34898768799 completed SUCCESS and its complete downloaded parent/shared/fresh/multiblock outputs were compared locally with exact equality. See [CI_AUDIT.md](project/research/general_n/2026-09-14-joint-blocks-v1/CI_AUDIT.md). This supersedes earlier queued-at-creation observations, not their historical record.

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. The complete preceding shared-slack handoff is archived byte-for-byte in [CURRENT_STATE_SHARED_SLACK_DETAILS_2026-09-14.md](CURRENT_STATE_SHARED_SLACK_DETAILS_2026-09-14.md). It contains all theorem details, verification domains and branch ranges. Read [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md), [the proof package](project/research/general_n/2026-09-14-joint-blocks-v1/README.md) and [the offline replay guide](project/research/general_n/2026-09-14-joint-blocks-v1/REPRODUCE.md), then inspect newer commits before continuing. Earlier root overviews and reviewer navigation remain retained.

## Canonical frontier and external-review boundary — unchanged

```text
whole-state closures:            977
canonical exclusions:          1,971
canonical survivors:           3,607
  N34-derived:                 3,529
  N35-derived:                    78
recovered relational candidates:2,655 — UNPROMOTED
```

The fixed-order n25/n27-through-n35 and general7/12 candidates are unchanged. No synthetic profile is an actual graph or a whole canonical scalar state. External mathematical review, novelty assessment and third-party reproduction remain OPEN. Promotion of2,655 candidates requires exact coverage, both implementations agreeing, zero unresolved, successful aggregate and a separate reviewed ledger step. Preserve N34/N35 provenance and the closure-ledger validator.

## Documented starting point and durable data

Plan commit `e8a64d4af782a17ceae368e6218a7aa37ce1db05` preceded the new experiments. Parent evidence publication was inspected as complete at `b6a15db114d7b4f3b71d73da816daec563f11824`: all16 raw/derived files and the checked manifest are committed. Publication-only run34895776658 passed. Original34894544147 passed its mathematics and hashes but failed its Git rebase on an unclean checkout; its overall failure is not relabeled green. The [publication audit](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md) preserves the exact distinction and repair.

The durable inputs include original713 corpus/scanner, pilot/812 inputs, parent full conditioned output and prior arrays, complete previous capped/block actual-expected pairs, historical capped outputs and full timestamped audit snapshots. Readable unsuccessful explorations and rejected transfer attempts remain recorded. No hash was weakened to accept an artifact.

## Main new theorem: one shared slack budget

Keep Q=r+2t+D0+Esel, with structural t, q-threshold tau and block threshold eta. All zero labels are explicit; never assume z<=Esel. Retain all legitimate caps and positive-label endpoint forcing d_u=(p_u-rho_u+1)_+<=e_i on selected positive label i.

Choose a label block L containing every zero-demand label. Source u is forced to choose at least f_u=(q_u-|eligible labels outside L|)_+ labels in L. Put M=sum f_u, S_L=sum_L s_i, fix ACTUAL e_L, and let H=Esel-e_L and J=S_L+e_L-M. Actual low selections k_u satisfy sum(k_u-f_u)=J. Distinct high selections imply k_u>=q_u-floor(H/d_u) for d_u>0. Therefore

```text
gamma_u(0;H)=0,
gamma_u(d;H)=(q_u-f_u-floor(H/d))_+ for d>0,
sum_u gamma_u(d_u;H)<=J,
H+sum_u gamma_u(d_u;H)<=Esel+S_L-M.
```

The eligibility ceiling on k_u remains mandatory. Negative J or an impossible exact block total rejects the branch; no clipping. Unlike the preceding individual caps, this prevents every source from independently spending the SAME spare selected places. J=0 recovers the row295 tight-block mechanism; a group-count inequality quantifies positive J.

An integer DP maximizes incoming pressure under this one shared resource, retaining exact receiver free capacity and the safe interval incoming bound. Its optimum is exact only for the stated pressure projection, not joint incidence or graph realization. No universal high-q-tail or Hall-minimum equality theorem is assumed. The preserved false shortcut sum(high incidence charge)<=H fails when sources share a positive label; the valid theorem charges low-block selected places instead.

## Results and explicit limitations

The previous original713 sample had704 rejections. New shared slack excludes240,258,342 with complete inherited/new branch coverage, yielding **707/713 rejected and six not rejected:108,160,338,347,471,586**. Row240's illustrative branch requires104 incoming units but permits at most28 free+74 zero-slack pressure+1 affordable extra=103. Complete exact excess branches, not merely that example, establish the profile exclusion.

New local checks:9293 exhaustive selected-incidence configurations,25391 arbitrary blocks including12305 positive-slack blocks,7839 valid random incidence systems from10000 attempts,3000 independent brute comparisons covering237067 pressure vectors, and all3 standing hostile q-tail examples. Incidence tests need not satisfy the positive-surplus scalar ledger; the separate fresh synthetic test does satisfy its stated ledger relaxation.

Fresh seed74220260919 was fixed before inspection; the same hash-pinned generator ran100000 trials and produced715 profiles passing its scalar/cap/incidence/pair-flow screens. Earlier tests reject705; shared slack rejects3 more, leaving **7/715 not rejected**. New shared fresh rows163,362,687; fresh non-rejections20,91,391,490,528,562,677. These are a DIFFERENT row namespace from the original713 sample. New seed is not independently designed generation or actual graphs.

The simultaneous multiblock extension tested597 consistent excess tuples across the six original survivors.25 failed total capacity,118 failed price,454 remained across all six: **no extra profile closure**. This does not exhaust the full multiresource shared-slack formulation. Rational separable slack pricing also left original row240 branches41 and45 uncovered; the integer DP is materially stronger there. Source and outputs of that historical exploration are retained.

## Exact end-to-end replay — completed

Unified harness `run_replay.py --outdir /tmp/shared-slack-replay` runs offline using Python standard library and g++17. It checks source blobs, reruns the parent conditioned proof, checks every new shared result, regenerates the fresh corpus and checks all fresh values, and reproduces the full negative multiblock result.

Run34898768799, job104159335270, completed SUCCESS on research/workflow commit `de4cdce81db75301b622874fdfe6f5c792e89b7a`. Artifact10369204132 was downloaded and checked; archive SHA256 `ba15a20a9affa7bec78f3d2d4c9d2104772d7b31b6f8027cb1c2e83143a9f9d7`. All four remote JSON objects equal local full outputs, and the remote fresh TSV matches local bytes exactly.

```text
parent full: 7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e
shared full: 35d4c3c05595102b2a568d986d8bab753059da4a2c59b31689a550aaddb23ce6
fresh full: 754774a0d4fdb23c8403efe4c5e41f2df950ebf933f903ca7e3d335d6ce370f9
multi full: d979d53bad1239b65442265b477594cffa05ec67750d8be6b3123add2b2b5127
fresh TSV: f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e
```

Both new shared/fresh complete result objects are committed. The larger multiblock output and fresh raw TSV are deterministically reconstructible from committed inputs/code and fixed hashes, and retained in the downloaded CI artifact and portable bundle. They are not falsely described as raw files already committed in this package.

Main new commits: proof/hardening `4ad8657beff74c3bc075f9d0fb1b71a7bb1ffd06`; executed verifier `bed3e780d48327e8d09897c222707e28912141a8`; full original result `7e92fc952a141a807b80c33f9a22b61f3663de7c`; fresh result `8622562f8c2d0fbb3e1d363273d8b366ee882db5`; successful CI receipt `66a2c2667d81a44c37655d4e0058aa8257722d6a`.

## Relational audit and next mathematical target

No fresh live shard count is asserted by this research checkpoint. Fetch EVERY job page or a newer complete diagnostic for audit34854911792. Historical128-shard snapshots are not current conclusions. Preserve completed work; retry at most one individually confirmed transient infrastructure failure, not queued/running/successful jobs or computational timeouts. Do not duplicate the256-shard audit, alter budgets/concurrency or promote the ledger. The existing hourly monitor retains these rules.

Next attack common selected-source usage across blocks, or the full multiresource shared-slack system. Independent best-source choices for individual labels can still be mutually incompatible. Use the six original and seven fresh retained examples as separate boundary laboratories. Retain exact q-layer/mincut, crossing-wall/saturation and maximum-cut/stability routes. External specialist review of the canonical graph-to-selected/residual bridge remains the principal correlated dependency. Internal proof, successful CI and durable publication do not substitute for that review.
