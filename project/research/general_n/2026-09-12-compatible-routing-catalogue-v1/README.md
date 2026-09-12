# Compatible routing: frozen catalogue over the full prior pool

12 September 2026. Candidate general machinery and exact finite applications.
External mathematical review, novelty and external reproduction remain OPEN.

The frozen catalogue excludes **990 of all 5,578 preceding general-routing
survivors**. It retains 15 of the pilot's 19 exclusions; the other four pilot
certificates remain valid and are checked separately. Thus **994 cases are
excluded by the combined compatibility record, leaving 4,584 survivors**.
There are 975 new exclusions beyond the pilot.

| Frozen comparison | Excluded | Catalogue survivors |
|---|---:|---:|
| Heavy-only projections: H+p, without balance or transport terms | 0 | 5,578 |
| Retain selected degrees and balance; no transport terms | 0 | 5,578 |
| Add separate destination-eligibility tails | 990 | 4,588 |

These are comparisons of the **fixed catalogue**, not optimal bounds over
arbitrary multipliers. The pilot's unrestricted searches gave different
comparison counts. No per-state fitting or solver is used in this replay.

| Layer | Prior pool | Catalogue exclusions | Pilot-only retained | Combined survivors |
|---|---:|---:|---:|---:|
| N34 m289 | 5,415 | 905 | 4 | 4,506 |
| N35 m306 | 162 | 84 | 0 | 78 |
| N35 m307 | 1 | 1 | 0 | 0 |
| Total | 5,578 | 990 | 4 | 4,584 |

These are arithmetic necessary-condition cases that already had other proofs
in the canonical N34/N35 candidate ledgers. They are not actual graphs or new
fixed-order theorem closures.

## Theoretical result

The [recurring fixed potential](FIXED_POTENTIAL.md), with the same small weights
as the previous compact hand example, suffices for **707 cases** at their
recorded winning thresholds. A new hand reduction eliminates q from its exact
local maxima and leaves at most five p candidates per H. It applies under
explicit general bridge hypotheses, rather than being restricted to orders
34 and 35. The present applications still require exact local maxima and
complete heavy-sender-count coverage.

The same reduced formula matches all 28,591 recorded full-model gaps for that
template, including unsuccessful attempts. The hand proof establishes the
parameterized implication; finite checks corroborate its applications.

Post-replay analysis finds that 11 of the already frozen templates cover all
6,314 positive sender-count obligations at the recorded winning thresholds.
This is a greedy compression, not a smallest-catalogue claim. Ordinary tails
alone cover 989 of the 990 recorded winning thresholds. The remaining recorded
witness, N34 state 133, uses forced-heavy tails. That does not prove forced
tails necessary under every alternative threshold or potential. Six states
use more than one template across their sender counts at the recorded threshold.

## Selection, evidence and audit

The [pre-replay plan](PLAN.md) takes the 20 simplest primitive integer vectors
from the pilot's successful non-mixed envelopes. Ranking by total absolute
coefficient size, then term count and lexicographic order, selects 20 out of
155 vectors. Their control projections give 31 distinct templates: 15 in the
heavy-only mode, 16 with selected degrees, 31 with eligibility. Selection and
the catalogue hash were fixed before the full-pool run. Transport cutoffs stay
at their original integer values while h ranges from 2 to max(s), with T=4h.

Read the [audit and corrections](AUDIT.md), [full summary](frontier_summary.json),
[frozen catalogue](catalogue.json), [all ranked candidates](catalogue_candidates.json),
[exact verification](verification.json), [compression record](compression.json)
and [reviewer package](../../../../releases/general-compatible-catalogue-reviewer-v1/README.md).

The separately written Python checker verifies 1,564,007 catalogue gaps,
14,310,343 source-potential evaluations and full coverage of all 5,578 cases.
It checks the four inherited pilot witnesses over 46 sender-count cases.
All negative gaps and stop points remain in the original result stream.
The [storage catalogue](EVIDENCE_STORAGE.json) records original and encoded
hashes for five losslessly preserved streams. The survivor stream distinguishes
the 4,588 catalogue survivors from the 4,584 combined survivors.

## Reproduction

The exact checks need Python's standard library:

```sh
python project/research/general_n/2026-09-12-compatible-routing-catalogue-v1/independent_verify.py
python project/research/general_n/2026-09-12-compatible-routing-catalogue-v1/verify_catalogue_and_summary.py
python project/research/general_n/2026-09-12-compatible-routing-catalogue-v1/check_fixed_potential.py
```

To reproduce discovery in a separate checkout, run `freeze_catalogue.py`,
`prepare_inputs.py`, then `run_replay.py` (C++17/g++ required). Evidence readers
prefer the original archives when the storage catalogue exists. The release
validator compares fresh raw output with original hashes before removing it
and checking the originals; this avoids mistaking archive replay for rediscovery.
To archive a new experiment, regenerate its summaries from the new raw results
without an old storage catalogue, then run `pack_evidence.py`.

## Next question

The useful next mathematical step is to bound the remaining H maximum in the
recurring potential by a closed expression, and test which hypotheses make
that expression effective on the 4,584 combined survivors. Most of that pool
is still unresolved by these general rules. Actual arc allocation, fuller
label-degree compatibility and cross-threshold consistency remain omitted.
The fixed-order ledgers and 7/12 candidate are unchanged; no unrestricted
Murty–Simon proof is claimed.
