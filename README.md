# Murty–Simon / Erdős Problem #742

**n=25 and n=27 candidate proofs; active general-order research.**

**Status updated: 7 September 2026.** The complete order-25 and order-27 arguments remain **candidate proofs awaiting independent mathematical review**. The general-order programme has additional candidate inequalities and profile exclusions, but **no complete order above 27 is claimed resolved**. Internal arithmetic reproduction, preservation of evidence and independent review are separate status questions. This repository does not announce the conjecture as settled.

## Current position

| Workstream | Preserved position | Remaining obligation |
|---|---|---|
| n=25 | Complete candidate bound of 156 edges, with equality only for K₁₂,₁₃ | Independent mathematical review and external computational reproduction OPEN |
| n=27 | Complete candidate bound of 182 edges, with equality only for K₁₃,₁₄ | Independent mathematical review and external computational reproduction OPEN |
| General order | Candidate high-degree theorem, coupled resource and activation inequalities, and infinite families of excluded numerical profiles | Middle-degree region remains open; no full general proof |
| n=28, Δ=15 | At m=196, **6,918 numerical rows in 830 demand patterns** remain after the v5 tests | One common column assignment across multiple sources, shared adjacency, and higher-edge-count coverage for the new tests |

For the active research, start with the [general-order overview below](#general-order-research) and the [latest preserved column-propagation v5 checkpoint](project/research/general_n/2026-09-07-column-propagation-v5/README.md). For external review of the frozen n=25 candidate, use the following reviewer entry points.

## Start here: n=25 review

The proposed order-25 result is that every simple diameter-2 edge-critical graph has at most **156 edges**, with equality exactly for **K₁₂,₁₃**. The argument and finite calculations have been examined internally and reproduced. Independent mathematical review, independent reproduction by another researcher and formal verification remain outstanding.

1. Read the [reviewer manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf).
2. Follow the [review guide and complete replay instructions](releases/n25-reviewer-v1/REVIEW_GUIDE.md).
3. Inspect the [frozen candidate proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md) and [exact result tables](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RESULTS.md).
4. Read the [literature and attribution check](releases/n25-reviewer-v1/LITERATURE_AND_ATTRIBUTION.md) and [relationship to earlier project work](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RECONCILIATION.md).

## Reviewer edition 1

The [versioned reviewer package](releases/n25-reviewer-v1/README.md) includes a PDF manuscript, editable TeX and Markdown, the unchanged complete evidence archive, checksums, a wrapper covering the entire numerical route, and forms for reporting review findings. Package assembly instructions are provided alongside the archive parts. A GitHub Release page is a separate distribution step; its prepared instructions and text are in [RELEASE_UPLOAD_GUIDE.md](releases/n25-reviewer-v1/RELEASE_UPLOAD_GUIDE.md).

From the extracted reviewer package:

```sh
python3 -I -B review_package.py --verify-only
python3 -I -B review_package.py --replay --output /absolute/path/to/new-n25-replay
```

The first command checks manifests and all final equality certificates. The second also reruns the original Δ14/157-edge checks and all new numerical scopes. Python 3.10 or later and its standard library suffice. The largest replay needs several gigabytes of temporary memory and disk space. The expanded column JSON files are losslessly reconstructable from the compressed ledgers.

## What the n=25 candidate contains

- Published reductions, including Fan's strict bound reducing a counterexample to exactly 157 edges.
- A witness-count argument for maximum degree 13, including the equality case.
- Residual-edge arguments for maximum degrees 14, 15 and 16.
- **Maximum degree Δ≥17:** [Section 2 of the proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md#2-published-reductions-and-their-exact-numerical-effect) applies Haynes–Henning–van der Merwe–Yeo Theorem 3.6(a) to the complement. At n=25 this gives **e(G)≤155** in the remaining non-bipartite case. Stars and complete bipartite graphs are handled separately.
- Explicit finite checks for both 157-edge exclusion and 156-edge equality. All **1,959** final numerical equality columns have checked rejection certificates.

The complete general Murty–Simon conjecture is not proved by this repository. General-order research is now active, but it is not part of the frozen n=25 candidate's theorem claim. The literature check did not locate a published full order-25 resolution, but it does not establish novelty or priority.

## Attribution and review status

Paul Lenz directed the project. ChatGPT/Codex supplied substantial mathematical development, code and internal checking. The initial two arithmetic implementations were produced with the same assistant; agreement between them is a software cross-check, not independent mathematical authorship or expert endorsement. Published inputs are cited in the manuscript.

A further [internal red-team audit](project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Report_2026-09-06.md) examines the lemmas and their assumptions and uses a third arithmetic checker to recalculate all stored numerical exclusions. It found no blocking failure in the audited candidate, but records a helper defect outside the parameter ranges used in this proof. This remains a same-assistant check; external review is still open.

The [external review register](releases/n25-reviewer-v1/REVIEW_REGISTER.json) records both mathematical and independent computational review as **OPEN**. Paul [reported sending an n=25 review invitation to Dr Florent Foucaud](project/reviews/n25/outreach/2026-09-07-foucaud-sent-user-report.md) on 7 September 2026. No acceptance or completed external assessment has been reported.

## Larger-order extension: n=27

A separate [n=27 candidate proof and review package](project/reviews/n27/2026-09-07-candidate-v1/README.md) extends the residual method and proposes the bound **182 edges**, with equality only for **K₁₃,₁₄**. Its complete internal arithmetic checks leave no surviving configurations. The [full evidence archive](releases/n27-candidate-v1/README.md) includes source code, all ledgers, certificates and replay instructions. Independent mathematical review and external computational reproduction remain **OPEN**. This extension does not alter the frozen n=25 editions or the governed n=25 theorem ledger.

## General-order research

**Candidate mathematics; exact internal arithmetic REPRODUCED; independent review OPEN.** The latest preserved research checkpoint is [column propagation and supplement activation v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md). It contains the complete original ZIP plus readable proof, results, review notes and integrity/extraction instructions. Earlier [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md), committed at `a96711534b47e12c597d826dcf23896cf396f9e6`, remains unchanged.

### General maximum-degree result

The [coupled-resource v2 derivation](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md) gives the candidate implication, for diameter-two edge-critical graphs and n≥4,

```text
Delta(G) >= beta*n  ==>  e(G) < floor(n^2/4),
beta = (10 - sqrt(2))/14 = 0.6132704598...
```

This improves the earlier project's coefficient `0.630601937...` from the [residual h-index checkpoint](project/research/general_n/2026-09-07-residual-hindex-v1/README.md). It is a general mathematical argument conditional on its stated graph-theoretic inputs, not an extrapolation from finite tests. The v3, v4 and v5 checkpoints do **not** improve this coefficient. The middle-degree region above the near-half-degree reduction remains open.

### Fixed-degree exclusions, not complete new orders

The [demand-support v3 proof](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md) proposes the following exclusions at and above the equality edge counts. The [demand-stability v3 checkpoint](project/research/general_n/2026-09-07-demand-stability-v3/README.md) covers the same three degree cases through alternative arguments and internally reproduced calculations; these are **not counted twice**.

| Order n | Excluded maximum degree | Edge-count scope | Remaining dense non-bipartite degree after the inherited reductions |
|---|---|---|---|
| 28 | 16 | m≥196 | 15 |
| 30 | 17 | m≥225 | 16 |
| 33 | 19 | m≥272 | 18 |

The proof explicitly justifies higher-edge-count coverage for these v3 exclusions through monotonicity of the necessary conditions. That coverage is not automatically inherited by new tests.

### What label-tail v4 adds

The label-tail inequality couples each label's actual neighbourhood capacity to one global budget for extra selected incidences. It gives a hand contradiction for the previously retained **(n, Δ, m)=(64,33,1025) numerical profile**, and extends to an infinite two-parameter family of excluded profiles. **Neither that one profile nor the infinite family constitutes a proof for every graph at the corresponding orders.** The [pair-budgets v2 work](project/research/general_n/2026-09-07-pair-budgets-v2/README.md) records the earlier inequalities and the stress-test profile from which this continuation developed.

At **n=28, Δ=15, m=196**, v4 reproduces the initial 18,645-demand screen, leaving 1,976 demand patterns for full residual-row expansion. That specified expansion covers **17,669,896 numerical rows**, retains **24,411**, and then leaves **13,196 rows in 1,119 demand patterns** after the additional projected tests. These are the preserved historical v4 results and the input to v5, not the current frontier. The survivors are necessary-condition rows, **not constructed graphs**.

### What column propagation and activation v5 adds

The [v5 proof](project/research/general_n/2026-09-07-column-propagation-v5/PROOF.md) couples individual degree/residual-column options to one source row at a time, including the missing-neighbour restriction. Its general supplement-activation inequality charges the additional outgoing selections that mandatory connections force at their supplements, using incoming-capacity normalization to avoid double counting. A solver-free corollary gives **78 > 57** for one retained row and excludes a specified infinite family of demand/residual patterns at n=4p+4, p≥10. These are pattern exclusions, not whole-order theorems.

The [exact v5 results](project/research/general_n/2026-09-07-column-propagation-v5/RESULTS.json) are:

| Stage at n=28, Δ=15, m=196 | Rows remaining |
|---|---:|
| Preserved v4 input | 13,196 |
| Joint column, matching and one-source-row tests | 7,725 |
| After 663 activation-cost and 144 activation-cut certificates | **6,918** |

The 6,918 survivors occupy **830 demand patterns**. The 47 additional short block certificates overlap those exclusions and are not added to the totals. Every surviving row, individual option domain, source bound and forced-label set is preserved in `evidence/FINAL_SURVIVORS.json` inside the complete archive.

**The structural gap remains:** different source rows may be witnessed by different complete column assignments. The next target is one common assignment across multiple sources, then the individual-label tail and shared-neighbourhood restrictions. The degree case and order 28 remain **OPEN**. The v4/v5 finite tests cover **196 edges only**; they do not claim coverage of 197 edges or every larger edge count. The bound and equality characterization remain separate proof obligations.

### Recovery, replay and limits

Follow the [v5 archive verification and replay instructions](project/research/general_n/2026-09-07-column-propagation-v5/README.md). The original ZIP contains **54 payload files plus their manifest**, is **1,035,233 bytes**, and has SHA-256 `79bdbdf02b23b9eef38e964b54eb300921b24d539014f07b476655d1575e63b6`. Paul uploaded it in commit `ff96063742208920e14526546d178b5c2cef4a6b`; the same Git blob was relocated into the dated checkpoint directory without recompression. It does not depend on the previously unfinished multipart uploads. The readable proof, results and review notes match the archive byte-for-byte.

Publication checks verify integrity and extraction, not mathematical validity. The original creation-session discovery and separate-checker reports remain unchanged in the archive. From the extracted package, `replay.py --verify-only` checks hashes, `--check` runs the full separate checking route, and `--replay` additionally regenerates discovery results. Full arithmetic checking needs Python and g++ with C++17 and Boost headers; no optimisation solver or network is required. A 100-row smoke test is not a full-domain check.

The [v4 recovery instructions](project/research/general_n/2026-09-07-label-tail-v4/README.md) remain available for the previous checkpoint. Its original ZIP SHA-256 is `3944e786fb0ea5322ae3e18dd177ef8b01046d903076a4ca61caf89fdc5ae184`.

Separate checker implementations are software cross-checks by the same assistant, not independent researchers. Actual-graph tests in these checkpoints found **no positive-surplus examples**; v5's saved actual-graph sample also has no positive activation-cost example. Finite tests do not establish the universal dense-case contradiction. The mathematical necessity of the lemmas still requires review.

**Arithmetic checks through n=1,000 are not proofs of every order through 1,000. No complete new order above 27, complete shared-adjacency search, improved v5 degree coefficient, novelty determination, or formal-kernel verification is claimed.** Committing a checkpoint preserves evidence; it does not promote its mathematical status.

## Historical work and governed status

The earlier Audit v5, parked Delta=15 proof and legacy SAT/reproduction work remain preserved. The new candidate supplies replacement arguments where documented; it does not retrospectively certify unresolved historical steps. The [earlier README](project/reviews/history/README_before_reviewer_v1.md) is retained verbatim.

- [Project standing orders](project/N25_PROJECT_STANDING_ORDERS.md)
- [Repository synchronization and commit-completion policy](project/REPO_SYNC_POLICY.md)
- [Canonical review and dated updates](project/CANONICAL_N25_REVIEW_2026-09-06.md)
- [Governed theorem ledger](repro-v1/ledger/theorem_ledger.json)
- [Historical task backlog](project/CANONICAL_TASKS.json)
- [Evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json)

The governed theorem ledger is unchanged by the reviewer editions and research-checkpoint publication. Under the standing orders, promotion requires an explicit audited argument or replayable proof evidence; packaging alone does not change mathematical status. The legacy `repro-v1/scripts/reproduce_all.sh` is not the entry point for the candidate's numerical replay; each checkpoint documents its own entry point.

## Preservation

Keep code, inputs, exact outputs, provenance, corrections and review reports. Preserve each reviewer version and research checkpoint, and make later corrections through a new dated version. Computation, mathematical justification, evidence availability and external review are recorded separately. The [commit-completion policy](project/REPO_SYNC_POLICY.md) requires branch attachment and read-back verification before publication is reported as complete.
