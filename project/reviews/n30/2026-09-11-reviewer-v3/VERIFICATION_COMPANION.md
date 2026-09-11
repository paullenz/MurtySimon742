# N30 reviewer-v3: verification and review guide

**Claim under review:** every finite simple diameter-two edge-critical graph on thirty vertices has at most 225 edges, with equality exactly for K(15,15).

**Status:** complete candidate argument. Exact internal arithmetic is REPRODUCED. Independent specialist mathematical review and external computational reproduction remain OPEN. Separate implementations by ChatGPT/Geeps do not constitute external independence. No governed theorem-ledger promotion or unrestricted conjecture claim is made.

## What the reviewer receives

The manuscript includes the full proof and all proof-critical integer tables. Its appendices contain the universal bridge, the twelve-label lemma, the 100-profile classification, every five- and six-lift interval, the residual-tail reconstruction, all eight 226-edge source inequalities, the four 225-edge envelopes and every one of the 211 positive-gap rows. Review does not require following links to assemble missing mathematical premises.

The ZIP preserves the PDFs, Markdown, build source, exact original mathematical inputs, arithmetic audit source and saved outputs. Paths inside the ZIP mirror the repository so that the audit scripts run without alteration. Historical inputs appear as source evidence; their earlier status prose is not the current edition's dependency map. Read the reviewer-v3 manuscript for that map.

## The dependency change from reviewer-v2

| Branch | Reviewer-v3 argument | Remaining review obligation |
|---|---|---|
| Delta at most 14, m at least 225 | Degree sum | Elementary arithmetic |
| Delta=15, m=225 | Regularity, common-neighbor count, criticality, complete bipartite equality | Short graph argument |
| Delta=16, m at least 227 | Q at most 21, Q at least 16+2t | Bridge and hand classification |
| Delta=16, m=226 | Seven profiles, nine residual rows, one ledger contradiction and eight source inequalities | Complete finite reconstruction and eight tables |
| Delta=16, m=225 | 100 profiles, 272 rows, 61 ledger contradictions and 211 envelope contradictions | Complete finite reconstruction and all envelope tables |
| Delta=17 through 28, m at least 225 | Twelve-label Q at most 18 and zero-padding | Hand transfer and universal bridge |
| Delta=29 | A universal vertex forces a star | Elementary criticality argument |

The hand transfer proves the stronger m at most 221 at Delta=17. It also yields the candidate corollary `e(G)<=Delta(n-Delta)` whenever `1<=n-1-Delta<=12` and `Delta>=17`; no uniqueness or novelty claim for that corollary is made.

Reviewer-v3 needs neither Fan's density theorem nor the published dominating-edge reduction. The isolated-C strengthening, higher-degree charging scans, large historical profile/residual scans, grouped LPs and Farkas rays are no longer premises. They remain historical evidence. **Finite arithmetic has not disappeared:** the printed classification and endpoint tables remain proof-critical.

## What the internal audit established

The preceding assembly was preserved at commit `01d1fb03d5b68ea4494a4ff29cedd0b49cb5dc16`, with its receipt at `81f37b80f643dd12f371680e673a95f6de793df2`. All six relevant GitHub workflows passed. The new implementation's run was [34649839054](https://github.com/paullenz/MurtySimon742/actions/runs/34649839054).

| Internal check | Result |
|---|---|
| Thirteen-label full-domain regression | 5,200,300 multisets; maximum Q=21; exactly 100 high-score profiles |
| Thirteen-label clipping regression | 20,801,200 comparisons; no failure |
| Twelve-label unbounded-threshold regression | 1,352,078 multisets; maximum Q=18 |
| Twelve-label clipping regression | 5,371,184 comparisons; no failure; exceptional all-fives case handled directly |
| Independent 225-edge reconstruction | 272 total rows, 61 ledger exclusions, 211 tight rows |
| Independent envelope arithmetic | 12,772 local states; all 844 per-template row gaps match |
| Assigned envelope cover | B1:195, B2:13, B3:2, C1:1; minimum integer gap 1 |
| Independent 226-edge arithmetic | Nine rows, one ledger exclusion, eight source contradictions; 859 source states |

The C++ full-domain regressions corroborate the written clipping proofs. They are not logical premises. The Python checker imports neither predecessor acceptance code nor discovery code. It uses a separate residual reconstruction and literal potential formulas; no numerical solver or floating point is used. Its agreements are internal evidence, not a substitute for human review of the deductions and printed arithmetic.

## Reproduce from the ZIP or repository

After extracting the ZIP, change into its top directory, `N30_Reviewer_Package_v3`. Alternatively run from the repository root. Python 3.12 and a C++17 compiler suffice for the mathematical checks; no third-party Python packages or solver are required.

```bash
python3 -I -B project/reviews/n30/2026-09-11-reviewer-v3/replay_bundle.py
```

This command verifies all bundled file hashes, compiles the preserved C++ regression into a temporary directory, regenerates both profile sweeps, compares the regenerated JSON with its saved counterpart, and runs the exact endpoint audit and written twelve-label payment-table check. It leaves original evidence files unchanged and prints a compact PASS report. A mismatch fails the command. The endpoint auditor reads the saved profile JSON only after it has been reproduced exactly in this replay.

To regenerate the PDF source and PDFs in a full repository checkout, use Python, Pandoc, XeLaTeX, the DejaVu Serif/Sans/Mono fonts and the supplied build script:

```bash
python3 project/reviews/n30/2026-09-11-reviewer-v3/build_package.py
```

Rendering is editorial; exact PDF bytes can vary with toolchain metadata and font versions. The committed manifest pins the reviewed outputs. SHA checks and exact arithmetic do not depend on visual rendering. The manuscript's mathematical input hashes are in SOURCE_MAP.json; BUNDLE_CONTENTS.json pins the files inside the ZIP, and MANIFEST.json pins the release PDFs and ZIP without recursive self-hashing.

## Editorial corrections and preservation

The new manuscript uses the canonical bridge's correct source-degree identity `(rho+q)+(b-1-q-p)=rho+b-1-p`, giving `p<=rho+b-a-1`. It correctly identifies z as the unique exception of `uj->z` in the residual forcing argument. These repair wording/display issues already documented in older copies; the old copies remain preserved.

Positive demand alone implies `s_i=d_i-R_i`; ledger tightness is not an extra premise for excluding the positive-slack 226-edge row. The manuscript states this directly. At zero-demand labels, the different equality-of-sums argument is written explicitly before the envelope proof.

Local equation and section references are qualified by appendix. Source statements that an already completed later task was still open have been removed from the new exposition. Every mathematical source and table remains hash-pinned; the editorial record explains the selected sections and these clarifications. All prior reviewer-v2 files and the governed ledger are preserved unchanged.

## Highest-value external review

1. Check the complement equivalence, unique selected representatives, residual forcing and all-source activity. A flaw here overrides downstream arithmetic.
2. Check the threshold-capacity unordered-pair count and both clipping arguments, especially unbounded gamma, the all-fives exception and reverse lifts.
3. Check completeness of all 100 profiles and both residual frontiers from the printed rules, then the sign of each envelope/resource inequality and all finite minima.
4. Check the elementary equality branch and the final degree assembly. Record any counterexample, missing case or hidden premise with a precise location.

A useful report distinguishes a mathematical gap, an arithmetic mismatch, a rendering error and an expository improvement. The supplied review report template can be used without accepting any project status label. A clean internal run does not pre-judge the result of that review.
