# Closed compatible potential: review and continuation

12 September 2026. Candidate general formula and exact finite applications.
External mathematical review, novelty and external reproduction remain OPEN.

The review found no blocking flaw in the preceding catalogue's stated
mathematics or accounting. Its 994 combined exclusions and 4,584 survivors
remain unchanged. The continuation produces a **closed exact local-maxima
formula requiring at most 59 candidate values per residual and sender class**,
independently of graph order. It also generalizes the eligibility cutoff k.

| Fixed-weight family, full 5,578-state pool | Excluded |
|---|---:|
| Cutoff k=2, full threshold search | 708 |
| All k=0..a+1, with a cutoff chosen for each sender-count case | 832 |
| Additional exclusions beyond the preceding combined record | **0** |

The expanded cutoff family adds 124 exclusions over its own cutoff-2 baseline.
Every one was already in the preceding 990-case catalogue; the four pilot-only
exclusions remain separate. The combined frontier stays at **4,584 survivors**:
4,506 N34 m289 cases and 78 N35 m306 cases. The 832 cases are alternative
explanations within existing fixed-order candidates, not new graph theorems.

The earlier 707 count referred to template 13 at the old catalogue's recorded
winning thresholds. The new full cutoff-2 search also excludes N35 m307 state
18 at a later threshold, giving 708. That case was already excluded; the prior
qualified 707 claim remains correct.

## Mathematical development

The [hand derivation](CLOSED_POTENTIAL.md) proves that two selected-degree
branches suffice: q=H and the destination-eligibility boundary q=k-rho.
In the first branch, six affine incoming-degree choices split into at most
27 linear or concave quadratic pieces. Their integer maxima are explicit.
In the second branch, one heavy-degree endpoint and at most five incoming
degrees suffice. Together they give at most 59 candidate values per class.

This removes the remaining heavy-degree enumeration while retaining the exact
source relaxation. The formula has explicit case distinctions; it is not a
single polynomial or a constant-time algorithm for the whole graph problem.
The source count and global sender-count aggregation remain part of an
application. Additional reach can come from changing the cutoff, not from
an exact reformulation alone.

## Verification and review

The closed Python implementation and an independently written C++ program
enumerating all integer source options produce **byte-identical full streams**:
476,427 gaps over all 5,578 states, including every recorded failed attempt.
The reference uses per-source cardinality dynamic programming instead of
sorted class differences. A separate local challenge checks 39,902 parameter
tuples, including 39,390 exhaustive small cases and 512 deterministic larger
cases through a=32. The hand proof supplies the unbounded claim.

The review also recomputes all 28,591 recorded gaps for the preceding recurring
potential. It preserves counterexamples to two invalid shortcuts: always
replacing q by H across an eligibility jump, and checking only the endpoints
of a heavy-degree interval. Those are abstract source domains, not asserted
diameter-two edge-critical graphs.

Read the [review and audit](AUDIT.md), [frozen experiment](EXPERIMENT.json),
[pre-experiment plan](PLAN.md), [full verification](verification.json),
[local challenges](local_verification.json), [invalid shortcuts](shortcut_counterexamples.json)
and [reviewer package](../../../../releases/general-closed-compatible-reviewer-v1/README.md).
All earlier exclusions are retained in the combined survivor accounting.

## Reproduction and evidence

Python's standard library suffices for the archived-output checks:

```sh
python project/research/general_n/2026-09-12-closed-compatible-potential-v1/check_local.py
python project/research/general_n/2026-09-12-closed-compatible-potential-v1/verify.py
python project/research/general_n/2026-09-12-closed-compatible-potential-v1/check_shortcuts.py
```

For fresh reproduction, use a separate checkout. Run `prepare_inputs.py`,
`check_local.py`, `replay.py`, then `run_reference.py` (g++/C++17 required).
The release validator compares both newly generated result streams with the
original hashes before removing raw files and checking the archived originals.
Evidence readers prefer the archives when their storage catalogue exists.

Five logical streams are stored losslessly in the [evidence catalogue](EVIDENCE_STORAGE.json).
The byte-identical closed and independent result streams share one stored
copy; their separate original logs and runtime records remain preserved.
All negative gaps, stop points and combined survivors are retained.
The explicit new-exclusion list is empty and is preserved as such.

## Next decision

Changing the eligibility cutoff within this fixed-weight family does not
reduce the combined frontier. The next bounded experiment should test whether
the locally allowed source and destination capacities can coexist under one
assignment of arcs, on a small sample of the remaining 4,584 cases. Fuller
label-specific compatibility may also matter. These are hypotheses for the
next experiment, not a demonstrated explanation of every survivor.

The N34/N35 ledgers, 7/12 candidate and outcome forecasts remain unchanged.
No unrestricted Murty–Simon proof or new density threshold is claimed.
