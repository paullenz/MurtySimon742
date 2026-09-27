# Current state — residual path and block Hall certificates, 27 September 2026

Canonical repository: `paullenz/MurtySimon742`. User-requested in-chat mathematics. Old research/recovery/audit schedules remain PAUSED; the local subscription worker is NOT DEPLOYED. Financial and health alerts are untouched. No services, paid computation or model/API execution lane were enabled.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: FORCED_COUNT_V3_EXHAUSTIVE_INTERNAL_INCOMPLETE
WORK MODE: MATH
INSPECTED PREDECESSOR: ce53dee6d3d898fa2c6073a9207fb88208169c4e; first read at fc5d692113f62a55c91dacbca3a5b1a499f65cb1.
LAST VERIFIED RESULT: Schema-3 forced-count guard has internal soundness/persistence/confluence proofs and exact verification. Two overlapping exhaustive n=3 regimes of 46,656 instances each check all source subsets, full cuts, reachable moves and retaining minimum restrictions. Path/block acceptances: 33657/33657 integer, 32418/32556 half-integer; gains over schema 2: 48 and 126 respectively for each mode. Zero discrepancies. Block-rule misses with a greatest tight minimum: 504 integer, zero in this bounded half-integer domain. Seeded sample n=4..6 accepts 198/200, still misses six greatest-tight instances in block mode. Focused rejection evidence preserved. Completeness is FALSE.
EVIDENCE: project/papers/stratified-hall-mincut/forced-count-2026-09-27/PROOF.md, verify_forced.py, test_forced.py and EVIDENCE.json.gz. Version 2 and earlier evidence remain unchanged; predecessor handoff archived at archive/status/2026-09-27-pre-forced-count-CURRENT_STATE.md.
UNPRESERVED WORK: None after publication of this checkpoint.
DEFERRED ADMIN: Reviewer-facing summary until exhaustive result; unrelated administration and literature comparison.
NEXT ACTION: Diagnose P=(0,2,0), d=(1,0,1), R={0->1,1->0,2->0}: its only tight minimum is {0,2}; mandatory source 2 compensates the high-only incoming row that defeats row containment. Investigate a residual-closure certificate for that signed incoming-count difference.
TRUST BOUNDARY: Internal proofs and checks only; not external/formal verification, novelty clearance or a general Murty–Simon proof. No completeness claim. Chen full main condition remains uninspected.
CONTROLS: X3, audit34854911792, equality and certification controls unchanged. No schedules, deployments, spending, paid execution, alert changes, background promises or research-hour credit.
<!-- CURRENT-STATUS:END -->

## Preservation and inherited status

[Current residual evidence](project/papers/stratified-hall-mincut/residual-certificate-2026-09-27/README.md) · [Predecessor local evidence](project/papers/stratified-hall-mincut/local-certificate-2026-09-27/README.md) · [Complete predecessor handoff](archive/status/2026-09-27-pre-local-certificate-CURRENT_STATE.md) · [Canonical WCD/RD closure](project/papers/stratified-hall-mincut/2026-09-27-closure/CANONICAL_CLOSURE.md) · [Fixed-support reductions](project/papers/stratified-hall-mincut/reduction-2026-09-27/REPORT.md).

The preceding Anstee-separation response was saved in a coordinating-chat ZIP/patch, not a remote commit. This checkpoint does not claim to have published that entire bundle; its exact frozen six-vertex certificate is carried in EVIDENCE.json.gz, and the new ordering proofs are self-contained. The complete prior bundle remains included in the downloadable continuation package.

No inherited mathematical status is promoted: n16,Delta9 and n19,Delta10 remain conditional internal exclusions; n18,Delta10 full-row certification remains suspended; n19,Delta11 remains locally checked with the full row open. R9/R11 reconstructions, the candidate threshold250/429, S<=14 internal computer-assisted edge bound and equality only through S<=8 retain the predecessor's qualifications. PR #2 remains a changes-required draft. Read the archived handoff and 24 September substantive review for the full evidence map; those dependencies were not rederived here.
