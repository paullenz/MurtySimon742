# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research, organised by graph order. **Updated 7 September 2026. Independent mathematical review remains OPEN.** Exact arithmetic reproduction and archive publication do not constitute independent acceptance or a proof of the general conjecture.

## n=25 — candidate proof

**Proposed result:** every simple diameter-two edge-critical graph on 25 vertices has at most **156 edges**, with equality only for **K(12,13)**.

Start with the [reviewer manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) and [review guide](releases/n25-reviewer-v1/REVIEW_GUIDE.md). The [frozen proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md), [exact results](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RESULTS.md) and [complete reviewer package](releases/n25-reviewer-v1/README.md) contain the argument, evidence and replay instructions.

The candidate includes degree-13 witness counting, degree-14/15/16 residual arguments, the published high-degree reduction for Delta>=17, and 1,959 checked final equality-column certificates. The [reconciliation](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RECONCILIATION.md) explains its relationship to earlier work; the [literature and attribution note](releases/n25-reviewer-v1/LITERATURE_AND_ATTRIBUTION.md) and [internal red-team report](project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Report_2026-09-06.md) record the review boundaries.

**Status:** complete candidate; internal arithmetic reproduced; independent mathematical review and external computational reproduction OPEN. The frozen edition and governed theorem ledger are unchanged. Paul [reported sending an invitation to Dr Florent Foucaud](project/reviews/n25/outreach/2026-09-07-foucaud-sent-user-report.md); no completed external assessment is asserted.

## n=27 — candidate proof

**Proposed result:** at most **182 edges**, with equality only for **K(13,14)**.

Read the [n=27 candidate proof and guide](project/reviews/n27/2026-09-07-candidate-v1/README.md), then the [complete evidence package](releases/n27-candidate-v1/README.md) for source code, ledgers, certificates and replay instructions.

**Status:** complete candidate; internal arithmetic reproduced; independent mathematical review and external computational reproduction OPEN. This extension does not alter the frozen n=25 proof.

## n=28 — candidate proof

**Proposed result:** at most **196 edges**, with equality only for **K(14,14)**. The direct route treats the 196-edge equality case and the 197-edge exclusion separately. Fan's cited strict bound of 197.2075 rules out 198 or more edges; it is an external theorem input, not a result of numerical extrapolation.

### Direct route: equality, then upper bound

At **196 edges**, the degree-15 chain passes from [v5 column propagation](project/research/general_n/2026-09-07-column-propagation-v5/README.md), through [v6 shared adjacency](project/research/general_n/2026-09-07-shared-adjacency-v6/README.md), to [v7 local incidence](project/research/general_n/2026-09-07-local-incidence-v7/README.md): 6,918 rows reduce to 388, then to zero in v7's 22/19/347 partition. Earlier degree and domain reductions remain explicit dependencies. These rows are necessary-condition data, not constructed graphs.

At **197 edges**, [direct197 v8](project/research/general_n/2026-09-07-direct-197-v8/README.md) generates a fresh t=2 domain: 12,012 charging tuples, 1,229 retained intervals and 8,216,928 residual rows. Successive screens leave 5,154, 2,959 and 1,584 rows; exact shared, source-type and endpoint-type certificates exclude 787+790+7, leaving zero. Other maximum degrees at 197 are covered explicitly. This route uses neither the old t=1 survivor list as a new domain nor a weak-core density reduction.

Read the [direct197 summary](project/research/general_n/2026-09-07-direct-197-v8/DIRECT_197_SUMMARY.md), [results](project/research/general_n/2026-09-07-direct-197-v8/RESULTS.json), [exact-check report](project/research/general_n/2026-09-07-direct-197-v8/EXACT_CHECK_REPORT.json) and [creation-session replay report](project/research/general_n/2026-09-07-direct-197-v8/FULL_REPLAY_REPORT.json). Full proof texts, source and certificates are in the linked original archives.

**Status:** complete candidate route; full internal replay and [red-team audit](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md) completed with **no blocking defect found**. Independent mathematical review remains OPEN. The audit reran the v3–v8 sequence, verified five handoffs and checked 8,983 final certificate leaves with an additional arithmetic/branch kernel. One standalone helper input-validation defect is non-blocking because the full driver rejects the malformed input; an additive guard patch reproduces all valid results. This is same-assistant checking, not independent certification. All v6, LocalIncidence-v7 and v8 archives are attached in their dated directories.

### Alternative degree-load-v7 route

The separate [degree-load-v7 candidate](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md) excludes the same final 388 equality rows in a different 173/215 partition and adds a weak-core density reduction. Its [proof](project/research/general_n/2026-09-07-degree-load-v7/PROOF.md) and [core-scope audit](project/research/general_n/2026-09-07-degree-load-v7/CORE_SCOPE_AUDIT.md) identify that extra review obligation.

This is not LocalIncidence v7. The routes share ancestors, methods and authorship: their exclusions must not be counted twice, their archives are not interchangeable, and agreement is not independent expert endorsement. The separate 21,975,757-byte degree-load audit bundle remains tracked by its own [publication-scope record](project/research/general_n/2026-09-07-degree-load-v7/PUBLICATION_SCOPE.json). That alternative bundle was not computationally audited in the direct-route red-team pass.

## General-order research

The [coupled-resource derivation](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md) gives the candidate implication, for n>=4:

```text
Delta(G) >= ((10-sqrt(2))/14)*n  ==>  e(G) < floor(n^2/4),
(10-sqrt(2))/14 = 0.6132704598...
```

The middle-degree region remains open in general; v8 does not improve this coefficient. Earlier stages are preserved: [residual h-index v1](project/research/general_n/2026-09-07-residual-hindex-v1/README.md), [pair budgets v2](project/research/general_n/2026-09-07-pair-budgets-v2/README.md), [demand-support v3](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md), [overlapping demand-stability v3](project/research/general_n/2026-09-07-demand-stability-v3/README.md), and [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md).

V3's degree-case exclusions at (n,Delta)=(30,17) and (33,19) do not complete those orders. Infinite excluded profile families are not whole-order theorems. Historical frontiers are preserved, not rewritten. **No complete order above 28, proof through n=1,000, full all-order conjecture, novelty or priority determination, or formal-kernel verification is claimed.**

## Evidence and replay index

| Checkpoint | Repository evidence | Main scope |
|---|---|---|
| [n=25 reviewer edition](releases/n25-reviewer-v1/README.md) | Manuscript, complete evidence and replay guide | Frozen order-25 candidate |
| [n=27 candidate](releases/n27-candidate-v1/README.md) | Complete evidence and replay guide | Frozen order-27 candidate |
| [v5 column propagation](project/research/general_n/2026-09-07-column-propagation-v5/README.md) | Original ZIP, readable proof and integrity helper | Equality frontier: 6,918 rows |
| [v6 shared adjacency](project/research/general_n/2026-09-07-shared-adjacency-v6/README.md) | Original ZIP: 88 payloads plus manifest | Equality frontier: 388 rows |
| [v7 local incidence](project/research/general_n/2026-09-07-local-incidence-v7/README.md) | Original ZIP: 87 payloads plus manifest | Final 388 equality rows excluded |
| [v8 direct197](project/research/general_n/2026-09-07-direct-197-v8/README.md) | Original ZIP: 90 payloads plus manifest; readable summary and reports | Fresh 197-edge scope excluded |
| [n=28 red-team audit](project/reviews/n28/2026-09-07-redteam-v1/README.md) | Readable report; all 76 audit payloads and manifest recoverable from checked storage | Full direct-route replay, new kernel, graph tests and helper guard |

The v6/v7/v8 ZIPs uploaded in commit `9698513eb20817ebfa9556e79b11d5f538280065` were relocated without recompression or content changes. Archive CRCs, safe paths, manifest coverage and every payload checksum pass. The earlier [intake record](project/research/general_n/2026-09-07-v6-v7-intake/README.md) records a historical missing-upload state; that state is now superseded, not an unresolved archive-location problem.

Extract each archive into a fresh directory and use its own README and replay wrapper. `--verify-only` checks integrity; `--check --output /absolute/new/path` runs the specified arithmetic route. V6/v7 checking uses standard-library Python; v5/v8 also require C++17 and Boost headers. Keep assertions enabled. Optimisation solvers propose evidence but are not required for these exact checks. V8's direct197 replay is self-contained; the equality chain has separately documented ancestors. The [audit recovery and replay guide](project/reviews/n28/2026-09-07-redteam-v1/README.md) runs the combined 13-job audit from the six pinned original archives; the full combined driver has been executed successfully.

## Audit, attribution and governance

Paul Lenz directed the project; ChatGPT/Geeps supplied mathematical development, code and internal checking. Both original implementations and the new red-team audit are by the same assistant. The additional audit kernel reuses the preserved model constructors: it is a separate arithmetic and branch check, not a third independent mathematical model. The [external review register](releases/n25-reviewer-v1/REVIEW_REGISTER.json) remains OPEN. Saved actual-graph samples, including the new 107-graph audit sample, contain no positive-surplus example; universal correctness depends on the structural proofs, graph-to-model lifting and complete finite-domain coverage, not extrapolation from those samples.

The [README before archive publication](project/reviews/history/README_before_n28_archive_publication_2026-09-07.md) and the [ascending-order README before audit completion](project/reviews/history/README_before_n28_redteam_2026-09-07.md) are preserved verbatim. Frozen proofs, original archives, historical reports and the governed theorem ledger are unchanged. Legacy Delta=15, Audit v5 and SAT/reproduction obligations are not retrospectively certified by replacement routes.

See the [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [commit-completion policy](project/REPO_SYNC_POLICY.md), [canonical n25 review](project/CANONICAL_N25_REVIEW_2026-09-06.md), [governed ledger](repro-v1/ledger/theorem_ledger.json), [task backlog](project/CANONICAL_TASKS.json) and [evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json). Preserve code, exact data, provenance, corrections and review reports. Publication preserves evidence; it does not promote mathematical status.
