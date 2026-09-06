# Murty–Simon at n=25 / Erdős Problem #742

**Current status: complete candidate proof, awaiting independent mathematical review.**

The proposed result is that every simple diameter-2 edge-critical graph on 25 vertices has at most **156 edges**, with equality exactly for **K₁₂,₁₃**. The argument and finite calculations have been examined internally and reproduced. Independent mathematical review, independent reproduction by another researcher and formal verification remain outstanding. This repository does not announce the case as settled.

## Start here

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

## What the candidate contains

- Published reductions, including Fan's strict bound reducing a counterexample to exactly 157 edges.
- A witness-count argument for maximum degree 13, including the equality case.
- Residual-edge arguments for maximum degrees 14, 15 and 16.
- **Maximum degree Δ≥17:** [Section 2 of the proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md#2-published-reductions-and-their-exact-numerical-effect) applies Haynes–Henning–van der Merwe–Yeo Theorem 3.6(a) to the complement. At n=25 this gives **e(G)≤155** in the remaining non-bipartite case. Stars and complete bipartite graphs are handled separately.
- Explicit finite checks for both 157-edge exclusion and 156-edge equality. All **1,959** final numerical equality columns have checked rejection certificates.

The complete general Murty–Simon conjecture is outside this project's scope. The literature check did not locate a published full order-25 resolution, but it does not establish novelty or priority.

## Attribution and review status

Paul Lenz directed the project. ChatGPT/Codex supplied substantial mathematical development, code and internal checking. The initial two arithmetic implementations were produced with the same assistant; agreement between them is a software cross-check, not independent mathematical authorship or expert endorsement. Published inputs are cited in the manuscript.

A further [internal red-team audit](project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Report_2026-09-06.md) examines the lemmas and their assumptions and uses a third arithmetic checker to recalculate all stored numerical exclusions. It found no blocking failure in the audited candidate, but records a helper defect outside the parameter ranges used in this proof. This remains a same-assistant check; external review is still open.

The [external review register](releases/n25-reviewer-v1/REVIEW_REGISTER.json) currently records both mathematical and independent computational review as **OPEN**. The [review-request draft](releases/n25-reviewer-v1/REVIEW_REQUEST_DRAFT.md) has not been sent. No prospective reviewer is represented as having agreed to participate.

## Historical work and governed status

The earlier Audit v5, parked Delta=15 proof and legacy SAT/reproduction work remain preserved. The new candidate supplies replacement arguments where documented; it does not retrospectively certify unresolved historical steps. The [earlier README](project/reviews/history/README_before_reviewer_v1.md) is retained verbatim.

- [Project standing orders](project/N25_PROJECT_STANDING_ORDERS.md)
- [Canonical review and dated updates](project/CANONICAL_N25_REVIEW_2026-09-06.md)
- [Governed theorem ledger](repro-v1/ledger/theorem_ledger.json)
- [Historical task backlog](project/CANONICAL_TASKS.json)
- [Evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json)

The governed theorem ledger is unchanged by this reviewer edition. Under the standing orders, promotion requires an explicit audited argument or replayable proof evidence; packaging alone does not change mathematical status. The legacy `repro-v1/scripts/reproduce_all.sh` is not the entry point for this candidate's numerical replay.

## Preservation

Keep code, inputs, exact outputs, provenance, corrections and review reports. Preserve each reviewer version and make later corrections through a new dated version. Computation, mathematical justification, evidence availability and external review are recorded separately.
