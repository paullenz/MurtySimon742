# General joint heavy-routing: reviewer package v1

12 September 2026. Candidate general lemma and exact finite applications.
Internal arithmetic status **PROJECT_CERTIFIED**; external mathematical review,
novelty assessment and external reproduction **OPEN**. Publication is not
external acceptance. No unrestricted theorem or improvement to 7/12 is claimed.

Read the [hand lemma and worked example](../../project/research/general_n/2026-09-12-joint-routing-pilot-v1/JOINT_ROUTING_LEMMA.md),
[focused audit](../../project/research/general_n/2026-09-12-joint-routing-pilot-v1/AUDIT.md),
and [research package](../../project/research/general_n/2026-09-12-joint-routing-pilot-v1/README.md).

The new inequality conditions on the number j of sources sending more than
h heavy arcs. Each destination receives at most min(p,j), or min(p,j-1) if
it is also in that group. Combining this with heavy-destination eligibility,
one orientation per unordered pair, and the earlier load potential produces
a finite elementary upper bound for every possible j. Strict integer gaps
exclude a state only when every possible j is covered.

The pilot contains 27 states surviving all existing hand rules and the
preceding heavy-load family. Joint routing closes twelve; the aggregate
variant closes eight. Twenty multiplier ratios frozen from those witnesses
were replayed against the complete corrected pool:

- **6,307 eligible states**, after removing 192 previously hand-excluded
  cases from the historical envelope-labelled pool of 6,499.
- **729 further exact exclusions**: 687 at N34 m289, five at N35 m307, and
  37 at N35 m306.
- **563 exclusions beyond the aggregate variant using the same catalogue**.
- **5,578 survivors**, with complete IDs and recoverable original profiles.

The comparison correction, zero-success pilot variants, original search
outputs, invalid extensions and survivors are preserved. A catalogue survivor
is not a graph or proof of feasibility. Existing N34 reviewer-v2 and N35
reviewer-v1 proof ledgers remain unchanged.

From the repository root:

```sh
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/verify.py
python project/research/general_n/2026-09-12-joint-routing-pilot-v1/check_routing.py
python releases/general-joint-routing-reviewer-v1/check_manifest.py
```

The standard-library verifier imports no discovery code. It independently
uses step indicators and a cardinality recurrence, checking 1,234,969 integer
envelopes and 2,645,388 cached local options. The hand proof remains the
all-parameter justification. Finite orientation checks corroborate the pair
and destination bounds. Optional pilot rediscovery alone needs NumPy/SciPy.

`VALIDATION.json` records clean-checkout reproduction, archived-byte recovery,
exact replay and current navigation checks. `MANIFEST.json` pins this package
and its direct inputs; unchanged transitive evidence is at repository baseline
`e64091d771888fa68d60f0c8292fce9accf82d1a`. The manifest excludes itself and
`PUBLICATION_RECEIPT.json` to avoid circular hashes. The receipt records the
verified research publication; its subsequent receipt-only commit is checked
separately.

Current N34, N35 and heavy-load manifests receive updated navigation hashes
only. Historical proofs, logs, manifests and receipts retain their original
snapshot meaning. External reviewers should focus on the graph-to-routing
implication, the globally fixed j, the signs of all three corrections, and
the distinction between a general lemma and a finite coverage measurement.
