# Compatible destination routing — reviewer v1

12 September 2026. Candidate general inequalities and bounded exact pilot.
External mathematical review, novelty and independent reproduction OPEN.

Destination eligibility supplies 16 additional exclusions beyond retaining
selected degrees in a frozen 29-state sample. Including two exclusions from
extending the old multiplier search and one from selected-degree information,
19 states are excluded and ten survive. Mixed cuts add zero further whole-state
exclusions. The sample came from the preceding 5,578 general-routing survivors;
the full pool has not been replayed under these new rules.

Read in this order:

1. [Research overview and exact comparison](../../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/README.md).
2. [General implications and potential envelope](../../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/COMPATIBLE_ROUTING.md).
3. [Compact hand exclusion](../../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/COMPACT_EXAMPLE.md): required capacity 659, upper bounds 636 or 628.
4. [Audit, failed variants and scope](../../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/AUDIT.md).
5. [Pre-solver design](../../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/PLAN.md), [inputs](../../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/pilot_inputs.json), [exact verification](../../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/verification.json) and [envelope verification](../../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/envelope_verification.json).

The candidate proof uses the [canonical graph bridge](../../project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md),
[heavy-load family](../general-heavy-load-reviewer-v1/README.md) and
[joint-routing argument](../general-joint-routing-reviewer-v1/README.md).
The known selected-degree eligibility condition is not claimed newly discovered.
The new work combines it with heavy-load routing, extracts a general envelope
and measures its contribution separately from expanded numerical search.

## Reproduction and evidence

Run from the repository root:

```sh
python releases/general-compatible-routing-reviewer-v1/check_manifest.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/verify_selection.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/independent_verify.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/verify_envelopes.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/check_routing.py
python project/research/general_n/2026-09-12-compatible-routing-pilot-v1/check_compact.py
```

These exact checks require only Python's standard library. They cover all 648
attempted models, 321 integer certificates, 321 extracted envelopes, whole-state
coverage, the independent sample reconstruction and the finite corroborations.
Discovery additionally requires NumPy and SciPy; its versions and limits are
recorded in the research directory. The [release validator](validate_release.py)
copies tracked/staged files to a clean directory, reruns discovery, compares
every result field except measured elapsed time, then performs exact checks
using only the original encoded evidence. Numerical rediscovery agreement is
environment-sensitive; the integer archive checks do not require a solver.

The [validation report](VALIDATION.json) records what was actually reproduced.
The [manifest](MANIFEST.json) pins this package, direct inputs, current navigation
and preceding current manifests. Its full baseline commit pins unchanged
transitive dependencies. The manifest excludes itself and the publication
receipt to avoid circular hashes.

The original stream retains solver failures, proposals, rounding repairs and
timings losslessly. A dual infeasibility report is not an exact primal feasibility
certificate. Original outputs are not replaced by rediscovery outputs.
The audit and differently structured checks are internal, not external review.

## Next gate

Freeze a small catalogue of the successful compatible envelopes, beginning with
the simpler separate eligibility tails, then replay the full preserved pool
without fitting a new LP to each state. The pilot rate must not be extrapolated.
No new fixed-order theorem, improved 7/12 threshold or unrestricted solution is
claimed. Paul is conducting external review separately.
