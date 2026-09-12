# General heavy-load and routing: research package

12 September 2026. Candidate structural theory; exact internal checks pass.
External mathematical review, novelty assessment and external reproduction OPEN.

Read the [hand proof](HEAVY_LOAD_FAMILY.md), [focused internal audit](AUDIT.md),
and [reviewer package](../../../../releases/general-heavy-load-reviewer-v1/README.md).

## New general statements

For every heavy threshold h, with k_h heavy labels, z_h high-residual sources
and residual budget r, the candidate family gives

`4h k_h <= r+4h z_h` when every source in Z_h has p<=3h.

The full version retains the weighted demand sum and an explicit penalty for
p>3h. Arbitrary integer cutoffs T>=h and individual source capacities have
exact elementary maxima. At h=2, the family strengthens the old N34 bound
to `8k<=r+8z` and permits p<=6.

For positive surplus, the penalty can be aggregated into demand-only
inequalities whenever delta=b-a<=2h+1. These give new residual-tail lower
bounds and can exclude profiles before residual enumeration. A useful
consequence is

`all demands <=2 and delta<=5 => 9t+4delta<=a`.

There is no residual-degree cap in this corollary. These statements apply
across graph orders under their stated hypotheses. They do not prove the
unrestricted conjecture or establish novelty.

## Measured reach and limits

| Preserved layer | State records | New family exclusions | Former envelope cases among them | Survive searched family after exact mass filter |
|---|---:|---:|---:|---:|
| N34, 289 edges | 13,546 | 790 | 543 | 7,988 |
| N35, 307 edges | 19 | 6 | 4 | 11 |
| N35, 306 edges | 466 | 75 | 48 | 281 |
| **Total** | **14,031** | **871** | **595** | **8,280** |

An additional 4,880 states fail the existing positive-demand exact budget and
are accounted for separately. The canonical fixed-order packages keep their
published ledgers; this package records the new alternative hand exclusions.

Joint use of the new tail bounds excludes 30/1,296 N34 equality profiles,
3/13 N35 307-edge profiles and 12/144 N35 306-edge profiles before residual
expansion. These are 45 layer/profile instances, not necessarily 45 distinct
demand tuples across layers. Survivors and complete original domains remain
available.

Every state witness uses T=4h. Searching integer T=h..4a with the uniform
and individually capped formulas adds no further exclusions on the residual
state set. That negative result, and explicit counterexamples to overstrong
local extensions, are part of the preserved result.

## Replay and evidence

From the repository root, using only the Python standard library:

```sh
python project/research/general_n/2026-09-12-heavy-load-family-v1/check_local.py
python project/research/general_n/2026-09-12-heavy-load-family-v1/verify_applications.py
python releases/general-heavy-load-reviewer-v1/check_manifest.py
```

The local checker evaluates indicator sums separately from the closed maxima.
The application verifier imports no discovery or bound-formula implementation.
It checks every recorded exclusion and the complete original domain. The
shared historical frontier input remains an explicitly pinned dependency.

[EVIDENCE_STORAGE.json](EVIDENCE_STORAGE.json) pins all original and encoded
bytes. The three large records are stored in gzip/base64 files and recovered
by `evidence_io.py`: `frontier_results.jsonl`, `profile_results.jsonl`, and
`remaining_states.json`. To recover a stream:

```sh
python project/research/general_n/2026-09-12-heavy-load-family-v1/evidence_io.py frontier_results.jsonl /tmp/heavy_frontier_results.jsonl
```

To reproduce the parameter scans in a separate checkout:

```sh
python project/research/general_n/2026-09-12-heavy-load-family-v1/probe_frontiers.py
python project/research/general_n/2026-09-12-heavy-load-family-v1/probe_profiles.py
python project/research/general_n/2026-09-12-heavy-load-family-v1/pack_evidence.py
python project/research/general_n/2026-09-12-heavy-load-family-v1/verify_applications.py
```

Packing is required after rediscovery because replay prefers the archived,
hash-checked bytes. Use the new run's logs and provenance rather than
overwriting the original discovery logs in the canonical checkout.

## Next question

The family controls each source locally and uses an aggregate incoming-routing
inequality. The surviving states indicate that this loses useful information
about which destinations receive the heavy arcs and whether extreme local
costs can occur simultaneously. The next target is a joint constraint on
those destinations and incoming degrees. The existing source-capped threshold
rule remains complementary: its 430 N34 exclusions all survive this searched
load family. More elaborate local caps alone did not close that gap here.
