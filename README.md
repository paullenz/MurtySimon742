# Murty–Simon / Erdős Problem #742

**n=25 and n=27 candidate proofs; active general-order research.**

**Status updated: 7 September 2026.** The complete order-25 and order-27 arguments remain **candidate proofs awaiting independent mathematical review**. The general-order programme has additional candidate inequalities and profile exclusions, but **no complete order above 27 is claimed resolved**. Internal arithmetic reproduction, preservation of evidence and independent review are separate status questions. This repository does not announce the conjecture as settled.

## Current position

| Workstream | Preserved position | Remaining obligation |
|---|---|---|
| n=25 | Complete candidate bound of 156 edges, with equality only for K₁₂,₁₃ | Independent mathematical review and external computational reproduction OPEN |
| n=27 | Complete candidate bound of 182 edges, with equality only for K₁₃,₁₄ | Independent mathematical review and external computational reproduction OPEN |
| General order | Candidate high-degree theorem, coupled resource inequalities and an infinite family of excluded numerical profiles | Middle-degree region remains open; no full general proof |
| n=28, Δ=15 | At m=196, 13,196 numerical rows in 1,119 demand patterns remain after the v4 tests | Individual degree/residual-column and shared-adjacency analysis; higher-edge-count coverage for the new tests |

For the active research, start with the [general-order overview below](#general-order-research) and the [latest preserved label-tail v4 checkpoint](project/research/general_n/2026-09-07-label-tail-v4/README.md). For external review of the frozen n=25 candidate, use the following reviewer entry points.

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

**Candidate mathematics; exact internal arithmetic REPRODUCED; independent review OPEN.** The latest preserved research checkpoint is [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md), committed at `a96711534b47e12c597d826dcf23896cf396f9e6`. The directory includes the recovery program and lossless storage for the original proof, code, certificates, reports, exact survivor lists and unfinished work.

### General maximum-degree result

The [coupled-resource v2 derivation](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md) gives the candidate implication, for diameter-two edge-critical graphs and n≥4,

```text
Delta(G) >= beta*n  ==>  e(G) < floor(n^2/4),
beta = (10 - sqrt(2))/14 = 0.6132704598...
```

This improves the earlier project's coefficient `0.630601937...` from the [residual h-index checkpoint](project/research/general_n/2026-09-07-residual-hindex-v1/README.md). It is a general mathematical argument conditional on its stated graph-theoretic inputs, not an extrapolation from finite tests. The v3 and v4 checkpoints do **not** improve this coefficient. The middle-degree region above the near-half-degree reduction remains open.

### Fixed-degree exclusions, not complete new orders

The [demand-support v3 proof](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md) proposes the following exclusions at and above the equality edge counts. The [demand-stability v3 checkpoint](project/research/general_n/2026-09-07-demand-stability-v3/README.md) covers the same three degree cases through alternative arguments and internally reproduced calculations; these are **not counted twice**.

| Order n | Excluded maximum degree | Edge-count scope | Remaining dense non-bipartite degree after the inherited reductions |
|---|---|---|---|
| 28 | 16 | m≥196 | 15 |
| 30 | 17 | m≥225 | 16 |
| 33 | 19 | m≥272 | 18 |

The proof explicitly justifies higher-edge-count coverage for these v3 exclusions through monotonicity of the necessary conditions. That coverage is not automatically inherited by new tests.

### What label-tail v4 adds

The new label-tail inequality couples each label's actual neighbourhood capacity to one global budget for extra selected incidences. It gives a hand contradiction for the previously retained **(n, Δ, m)=(64,33,1025) numerical profile**, and extends to an infinite two-parameter family of excluded profiles. **Neither that one profile nor the infinite family constitutes a proof for every graph at the corresponding orders.** The [pair-budgets v2 work](project/research/general_n/2026-09-07-pair-budgets-v2/README.md) records the earlier inequalities and the stress-test profile from which this continuation developed.

At **n=28, Δ=15, m=196**, v4 reproduces the initial 18,645-demand screen, leaving 1,976 demand patterns for full residual-row expansion. That specified expansion covers **17,669,896 numerical rows**, retains **24,411**, and then leaves **13,196 rows in 1,119 demand patterns** after the additional projected tests. The survivors are saved explicitly. These are necessary-condition rows, **not constructed graphs**.

The next target is to lift those rows to consistent individual degree and residual-column assignments, apply the stronger label-capacity and pair constraints, and enforce shared adjacency where needed. The degree case and order 28 remain **OPEN**. This v4 numerical scope is at **196 edges only**; the new tests do not claim coverage of 197 edges or every larger edge count. The bound and equality characterization remain separate proof obligations.

### Recovery, replay and limits

Follow the [v4 recovery and replay instructions](project/research/general_n/2026-09-07-label-tail-v4/README.md). Recovery restores **40 original payload files plus their manifest**, reusing four hash-checked dependencies from the already preserved demand-support v3 package. The original ZIP is **566,681 bytes**, SHA-256 `3944e786fb0ea5322ae3e18dd177ef8b01046d903076a4ca61caf89fdc5ae184`. The publication record reports byte-exact recovery of every original file and the original ZIP. In the recovered package, read `PROOF.md` and `REVIEW_AND_HANDOFF.md`; full arithmetic replay uses Python and a C++17 compiler, with no optimisation solver required for verification.

Separate checker implementations are software cross-checks by the same assistant, not independent researchers. Actual-graph tests in these checkpoints found **no positive-surplus examples**; finite tests do not establish the universal dense-case contradiction. The mathematical necessity of the lemmas still requires review.

**Arithmetic checks through n=1,000 are not proofs of every order through 1,000. No complete new order above 27, complete shared-adjacency search, improved v4 degree coefficient, novelty determination, or formal-kernel verification is claimed.** Committing a checkpoint preserves evidence; it does not promote its mathematical status.

## Historical work and governed status

The earlier Audit v5, parked Delta=15 proof and legacy SAT/reproduction work remain preserved. The new candidate supplies replacement arguments where documented; it does not retrospectively certify unresolved historical steps. The [earlier README](project/reviews/history/README_before_reviewer_v1.md) is retained verbatim.

- [Project standing orders](project/N25_PROJECT_STANDING_ORDERS.md)
- [Canonical review and dated updates](project/CANONICAL_N25_REVIEW_2026-09-06.md)
- [Governed theorem ledger](repro-v1/ledger/theorem_ledger.json)
- [Historical task backlog](project/CANONICAL_TASKS.json)
- [Evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json)

The governed theorem ledger is unchanged by the reviewer editions and research-checkpoint publication. Under the standing orders, promotion requires an explicit audited argument or replayable proof evidence; packaging alone does not change mathematical status. The legacy `repro-v1/scripts/reproduce_all.sh` is not the entry point for the candidate's numerical replay; each checkpoint documents its own entry point.

## Preservation

Keep code, inputs, exact outputs, provenance, corrections and review reports. Preserve each reviewer version and research checkpoint, and make later corrections through a new dated version. Computation, mathematical justification, evidence availability and external review are recorded separately.
