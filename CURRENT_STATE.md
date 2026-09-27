# Current state — forced-count and signed-closure Hall certificates, 27 September 2026

Canonical repository: `paullenz/MurtySimon742`. User-requested in-chat mathematics. Old research/recovery/audit schedules remain PAUSED; the local subscription worker is NOT DEPLOYED. Financial and health alerts are untouched. No services, paid computation or model/API execution lane were enabled.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: FORCED_COUNT_AND_SIGNED_CLOSURE_INTERNAL_BRANCHING_BOUNDARY
WORK MODE: MATH
INSPECTED PREDECESSOR: 7a0edf9aea11ad5e002458c128a0ba5219424e87; first read at fc5d692113f62a55c91dacbca3a5b1a499f65cb1.
LAST VERIFIED RESULT: Implemented and internally proved schema-3 forced-count and schema-4 signed residual-closure certificates. V4 includes mandatory sources, certifies signed incoming differences by auxiliary feasible flows, and removes full predecessor cones. Same-flow persistence, confluence for overlapping removals and V3 subsumption are proved. On each of two overlapping 46,656-instance n=3 domains, accepted V3/V4 block counts are 33657/34149 integer and 32556/32556 half-integer; V4 still misses 12 integer cases with a greatest tight minimum, proving incompleteness. Seeded 500-instance n=4..6 sample accepts 200/206, with no V4 greatest-tight misses. Zero observed discrepancies; exact optimization/restriction checks and 24 corrupt-certificate rejections plus an unsafe step are saved. A three-vertex remaining obstruction needs different crossing pairs depending on source 0. Its two-case exclusion proof is hand/oracle checked; branching is NOT implemented.
EVIDENCE: project/papers/stratified-hall-mincut/forced-count-2026-09-27/README.md, PROOF.md, CLOSURE_PROOF.md, verify_forced.py, verify_closure.py, test_forced.py, test_closure.py, diagnose_closure.py, VERIFICATION.json, SOURCE_HASHES.json and EVIDENCE.json.gz (13 exact outputs). Version 2 and earlier evidence remain unchanged; predecessor handoff archived at archive/status/2026-09-27-pre-forced-count-CURRENT_STATE.md.
UNPRESERVED WORK: None after publication of this checkpoint.
DEFERRED ADMIN: Unrelated administration and literature/novelty comparison.
NEXT ACTION: Implement CLOSURE_PROOF.md Sections 6-7 as a two-leaf branching certificate: P=(2,1,0), d=(1,0,1), R={0->1,0->2,1->2,2->0}; exclude source 1 using pair (2,1) when source 0 is absent and pair (2,0) when present. Check branch coverage and conditional flow bounds, reprove persistence/confluence, then replay the identical bounded domains.
TRUST BOUNDARY: Internal proofs and checks only; not external/formal verification, novelty clearance or a general Murty–Simon proof. No completeness claim. Chen full main condition remains uninspected.
CONTROLS: X3, audit34854911792, equality and certification controls unchanged. No schedules, deployments, spending, paid execution, alert changes, background promises or research-hour credit.
<!-- CURRENT-STATUS:END -->

## Preservation and inherited status

[Current forced-count and signed-closure evidence](project/papers/stratified-hall-mincut/forced-count-2026-09-27/README.md) · [Predecessor residual evidence](project/papers/stratified-hall-mincut/residual-certificate-2026-09-27/README.md) · [Predecessor local evidence](project/papers/stratified-hall-mincut/local-certificate-2026-09-27/README.md) · [Complete predecessor handoff](archive/status/2026-09-27-pre-local-certificate-CURRENT_STATE.md) · [Canonical WCD/RD closure](project/papers/stratified-hall-mincut/2026-09-27-closure/CANONICAL_CLOSURE.md) · [Fixed-support reductions](project/papers/stratified-hall-mincut/reduction-2026-09-27/REPORT.md).

The preceding Anstee-separation response was saved in a coordinating-chat ZIP/patch, not a remote commit. This checkpoint does not claim to have published that entire bundle; its exact frozen six-vertex certificate is carried in EVIDENCE.json.gz, and the new ordering proofs are self-contained. The complete prior bundle remains included in the downloadable continuation package.

No inherited mathematical status is promoted: n16,Delta9 and n19,Delta10 remain conditional internal exclusions; n18,Delta10 full-row certification remains suspended; n19,Delta11 remains locally checked with the full row open. R9/R11 reconstructions, the candidate threshold250/429, S<=14 internal computer-assisted edge bound and equality only through S<=8 retain the predecessor's qualifications. PR #2 remains a changes-required draft. Read the archived handoff and 24 September substantive review for the full evidence map; those dependencies were not rederived here.
