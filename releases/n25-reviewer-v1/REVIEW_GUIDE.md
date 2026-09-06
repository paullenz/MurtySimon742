# Independent review guide

Version: n25-reviewer-v1, 6 September 2026. Status: complete candidate argument; independent mathematical and computational review OPEN.

Read `N25_Reviewer_Manuscript_v1.pdf` first. It presents the candidate bound e(G)≤156 and equality only for K₁₂,₁₃. The manuscript's section and equation numbers match the frozen proof. The nested evidence ZIP contains the original proof, code, exact integer outputs, certificate records and historical provenance.

## Requested mathematical review

An initial assessment of the central lemmas is useful before committing to a full review. Please identify the exact section, equation or parameter case for each concern.

| ID | Obligation | Where to inspect | External status |
|---|---|---|---|
| M1 | Fan's strict bound, complement correspondence and all exceptional cases apply at order 25. | Section 2 and cited original papers | OPEN |
| M2 | Every critical edge has a valid witness; the partition count and equality inference are exhaustive. | Section 3, especially (3.1) | OPEN |
| M3 | Selected-edge assignment is injective and the generalized residual ledger is correct. | Section 4 | OPEN |
| M4 | Each edge charged in the all-active lemma exists, is residual and is counted only once. | Section 5 | OPEN |
| M5 | Low-k residual injection is valid and all k-r domains are covered, including k=1 at 156 edges. | Section 6 | OPEN |
| M6 | Pair, column, closure, matching and supplement bounds are necessary conditions in the stated direction. | Sections 7–8 | OPEN |
| M7 | The subset-capacity inequality follows from the preceding lemmas for every labelled column. | Section 9, equation (9.1) | OPEN |
| M8 | All degree cases and both edge counts assemble into the claimed theorem, and equality is attained. | Section 10 | OPEN |

The claims were internally read and rederived, but the external-status column is intentionally open. A reviewer need not agree with any prior internal assessment.

## Requested computational review

Use Python 3.10 or later. The new wrapper and the mathematical verifiers use the standard library only. XeLaTeX is needed only to rebuild the PDF from its supplied TeX source.

From the extracted reviewer package:

```sh
python3 -I -B review_package.py --verify-only
python3 -I -B review_package.py --replay --output /absolute/path/to/new-n25-replay
```

The first command checks the top-level manifest, the frozen evidence ZIP and both internal manifests, then checks all 1,959 equality certificates and their coverage. The second performs those checks, reruns the original Δ14/e157 primary and second verifiers plus their original 12 tests, and then replays all four new scopes. It compares the expected outputs and reports `external_mathematical_review=false` throughout.

For a shorter first check, `--replay --scopes d15_157 d15_156` reruns the original Δ14/e157 stage and only those two new scopes. A partial replay must be labelled partial. The unrestricted command is the full numerical replay for the present route.

The largest scope is Δ14/e156/k1: 401,543 outer states and 3,252,212 labelled columns. Expect several gigabytes of transient memory and disk use. The redundant 2.4 GB column JSON can be reconstructed exactly from the roughly 15 MB compressed ledger; it is not a missing proof dependency.

Please inspect domain completeness, independent sorting of A and B, maximum-degree attainment, labelled treatment of repeated degrees, source matching and certificate coverage as well as running the code. A passing replay does not establish the graph-theoretic necessity of those bounds.

## Reporting a review

Use `REVIEW_REPORT_TEMPLATE.md`. Record the exact package SHA256, interpreter and operating system, commands, completed scopes, failures and the mathematical statements actually read. Retain full stdout/stderr logs. Do not describe a timeout, partial run or unexamined lemma as verified.

All findings belong in `REVIEW_REGISTER.json` through a dated revision after they are received. The present register contains no external verdicts. Corrections should create a new version and a change log while preserving this edition.
