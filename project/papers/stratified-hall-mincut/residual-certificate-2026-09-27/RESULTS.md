# Executed exact comparison

Each exhaustive regime has every labelled loopless n=3 relation, one block, and every quota vector in the displayed domain. The regimes overlap in 4,096 instances; do not add their counts as distinct coverage.

| Quotas P,d | Instances | Old accepted | Path accepted | Block accepted | Greatest tight exists but block fails |
|---|---:|---:|---:|---:|---:|
| {0,1,2} | 46,656 | 33,309 | 33,609 | 33,609 | 552 |
| {0,1/2,1} | 46,656 | 32,292 | 32,292 | 32,430 | 126 |

Each regime independently calculates all 373,248 source subsets and all 2,985,984 complete network cuts. Cut minimality agrees with residual forward closure, and the minimum-cut source projections are exactly the F-minima. Every reachable deletion choice is explored (canonical shortest residual paths, all receiver/strict-row witnesses). Every tested move is also checked on every exact-minimum restriction retaining its removed source block. Every accepted terminal equals the independent oracle's greatest tight minimum. Every deletion graph has one terminal, including failures. Zero discrepancies.

There are 300 integer path gains and 138 rational block gains. A further deterministic 500-instance sample of n=4,5,6 with one or two receiver blocks and mixed rational quotas accepts 192/198/199 instances under old/path/block rules; it is a sample, not exhaustive coverage. It has seven instances with a greatest tight minimum but no block certificate.

Focused checks enumerate 4,112 source subsets across four constructions, including all 16 states and 32 transitions for four disjoint frozen path obstructions. All 24 corrupt certificates are rejected. The complete source, exact result files, examples and corrupt inputs are preserved; finite checks do not prove the hand theorems.

EVIDENCE.json.gz contains filename-to-exact-UTF-8-content strings for INTEGER_RESULTS.json, RATIONAL_RESULTS.json, SAMPLE_RESULTS.json and FOCUSED_RESULTS.json. Each exhaustive result includes a digest of ordered per-instance records and full subset/cut tables for representative gains and remaining failures. The sample records its seed. Test provenance is same-programme, not external review.

The structural diagnosis adds five explicit cases: strict SCC gain, SCC incompleteness, unsafe omission of the low safeguard, neutrality-only failure, and two disjoint two-source SCC deletions (four states/four transitions). It rejects three further complete certificates with partial/invented SCCs and the unsafe low-guard step. PROOF.md Sections 7–9 diagnose them. The forced-count alternative is proved sufficient on paper, with a separate example trace, but is not part of the implemented acceptance totals.
