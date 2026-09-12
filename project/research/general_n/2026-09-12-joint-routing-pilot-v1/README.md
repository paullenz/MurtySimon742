# Joint heavy-routing: pilot and general lemma

12 September 2026. Candidate structural result; complete exact internal replay
PASS. External mathematical review, novelty assessment and external reproduction
OPEN. Read the [hand lemma](JOINT_ROUTING_LEMMA.md), [audit](AUDIT.md), and
[reviewer package](../../../../releases/general-joint-routing-reviewer-v1/README.md).

The useful new information is the number j of sources with more than h heavy
selected incidences. A destination outside that group can receive at most j
of their arcs; a destination inside it can receive at most j-1. Combining this
with its actual incoming cap, heavy-destination eligibility, the one-orientation
pair budget and endpoint loads gives a parameterized hand inequality. A
specified-cardinality maximum replaces independent source maxima.

## Results

The deterministic pilot selected 27 cases after all previous hand rules and
the previous heavy-load family. The new joint variant excludes twelve; eight
also have an aggregate-routing witness. Its four additional pilot exclusions
justify extracting and replaying the general lemma.

Twenty multiplier ratios were then frozen from pilot witnesses and applied
to the complete corrected pool, with no numerical solver in this replay:

| Layer | Eligible states | Excluded by both variants | Additional joint exclusions | Survive catalogue |
|---|---:|---:|---:|---:|
| N34, 289 edges | 6,102 | 144 | 543 | 5,415 |
| N35, 307 edges | 6 | 4 | 1 | 1 |
| N35, 306 edges | 199 | 18 | 19 | 162 |
| **Total** | **6,307** | **166** | **563** | **5,578** |

Thus the new lemma supplies **729 further exact exclusions beyond the union
of all previous hand rules and the prior heavy-load search**. The 563 figure
measures the destination cap's added reach within the same frozen catalogue;
it does not compare all conceivable aggregate potentials. The hand proof is
general; these numerical coverage claims are finite applications.

A comparison correction is preserved: 192 of the previously identified 6,499
historical envelope cases already fail an old hand rule skipped by their
original solver ordering. They were removed before pilot selection and are
not credited to the new result. All IDs and reasons are saved. Fixed-order
statements and canonical N34/N35 proof ledgers remain unchanged.

## Exact replay

From the repository root, standard-library Python suffices:

```sh
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/verify.py
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/check_routing.py
python releases/general-joint-routing-reviewer-v1/check_manifest.py
```

The verifier imports no discovery or bound implementation. It uses indicator
sums and a cardinality dynamic program, checks the full pool and every
accepted witness, and verifies all twenty templates fail at each recorded
blocking case. Its 1,234,969 integer envelopes and 2,645,388 cached local
options pass. Original logs and environment versions are preserved.

`EVIDENCE_STORAGE.json` pins original and encoded hashes for the two result
streams. `evidence_io.py` recovers either one losslessly:

```sh
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/evidence_io.py frontier_results.jsonl /tmp/joint_frontier_results.jsonl
```

`pilot_inputs.json` contains the complete pilot, selection rule and all 192
old-rule removals. `frontier_summary.json` contains every new exclusion ID and
all 5,578 survivor IDs. The complete underlying profiles are recovered from
the pinned preceding heavy-load stream. `pilot_results.jsonl` preserves all
attempted LP proposals; `frontier_results.jsonl` preserves every successful
witness and blocking threshold case in the frozen catalogue.

To reproduce discovery and the full application in a separate checkout:

```sh
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/select_pilot.py
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/probe.py
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/catalog.py
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/replay_frontier.py
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/pack_evidence.py
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/verify.py
```

Only `probe.py` needs NumPy/SciPy. Pack regenerated streams before verification:
replay prefers hash-checked archived evidence. Preserve fresh provenance for
new runs; do not overwrite historical logs with claimed original timings.

## Limits and next question

The local and pair-only pilot variants closed no cases. Fifteen pilot cases
and 5,578 full-pool cases survive the stated searches. Failed approaches,
comparison corrections, invalid extensions, exact survivors and audit
challenges are part of this package. Survival does not mean graph feasibility.

The next goal is a demand/tail consequence of the new destination cap, possibly
using stronger supplement eligibility where the current model loses it. No
new all-order density bound, improvement of 7/12 or unrestricted proof has
been established.
