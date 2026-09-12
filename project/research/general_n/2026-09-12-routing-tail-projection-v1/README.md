# Demand/tail projection and equality rigidity

12 September 2026. Candidate general hand lemmas with exact internal checks.
External mathematical review, novelty assessment and external reproduction
OPEN. Read the [tail projection](TAIL_PROJECTION.md),
[closed equality lemma](EQUALITY_BOUNDARY.md), [audit](AUDIT.md), and
[reviewer package](../../../../releases/general-routing-tail-reviewer-v1/README.md).

## General theory extracted

Let L_l be proved residual-tail lower bounds, M=S-2t, and
D=M-b-sum_{l>=2}L_l. If d is the last positive lower-tail level, then

`rho_u<=d+D`.

Raising z_h to z costs beta_h(z)=sum_{l=2}^h(z-L_l)_+. This cost cannot
exceed D, and it lowers the residual cap to d+D-beta_h(z). A flat stretch
of m lower bounds ending at h gives the closed upper bound
`z_h<=L_h+floor(D/m)`. When D=0, all residual tails and the degree multiset
are forced.

Using this budget inside the joint-routing load inequality produces a
necessary inequality depending only on demands, lower tails, and scalar
parameters. It can exclude profiles before residual-degree enumeration.

A further hand simplification describes equality in G<=r+4hz when p<=P<=3h.
Every heavy source then has H=h or H=2h, and every 2h-sender has p=0. Thus,
with Jmax=max(0,min(z-2h,floor(Pz/(P+2h)))), equality forces

`W<=h(z+Jmax)`.

If this fails, the original load bound improves by one integer unit. This is
a closed all-parameter criterion with no local-type or multiplier search.

## Measured reach and limit

| Layer | Profiles | Prior profile exclusions | Further projected exclusions | Survive projection |
|---|---:|---:|---:|---:|
| N34, 289 edges | 1,296 | 30 | 79 | 1,187 |
| N35, 307 edges | 13 | 3 | 6 | 4 |
| N35, 306 edges | 144 | 12 | 29 | 103 |
| **Total** | **1,453** | **45** | **114** | **1,294** |

These are layer/profile instances, not necessarily distinct demand tuples
across layers. The comparison is with the previous demand-only profile test.
Within the frozen 44-template catalogue, the residual penalty accounts for
eight additional profile exclusions and the sharper destination term for 52.
Two of the 114 exclusions require combining new tails. All original domains,
witnesses and remaining profiles are preserved.

The closed scalar version excludes 40 additional profiles, compared with 31
for the ordinary load cap: nine extra whole profiles follow from equality
rigidity. Its 40 are already included in the projection's 114.

**All 5,578 states surviving the previous joint-routing catalogue still
survive these new tests.** This is a simplification into demand-level theory,
not a reduction of that remaining frontier. Fixed-order proofs, canonical
ledgers and the 7/12 maximum-degree result are unchanged.

## Reproduce and audit

From the repository root, the exact checks use standard-library Python:

```sh
python project/research/general_n/2026-09-12-routing-tail-projection-v1/check_budget.py
python project/research/general_n/2026-09-12-routing-tail-projection-v1/verify.py
python project/research/general_n/2026-09-12-routing-tail-projection-v1/verify_boundary.py
python releases/general-routing-tail-reviewer-v1/check_manifest.py
```

The main verifier imports no projection or discovery code. It independently
checks 790,922 integer envelopes and 3,834,361 cached local options, including
the full catalogue at every recorded blocking case. The scalar verifier uses
an independent enumeration of admissible sender counts. The budget checker
also preserves explicit counterexamples to invalid simplifications.

`EVIDENCE_STORAGE.json` pins the original and encoded bytes of five streams:
`pilot_results.jsonl`, `profile_results.jsonl`, `state_comparison.json`,
`boundary_results.jsonl`, and `boundary_state_comparison.json`.
The latter contains an object with a `records` array. Recover a stream with:

```sh
python project/research/general_n/2026-09-12-routing-tail-projection-v1/evidence_io.py profile_results.jsonl /tmp/routing_tail_profiles.jsonl
```

For fresh discovery and replay in a separate checkout:

```sh
python project/research/general_n/2026-09-12-routing-tail-projection-v1/probe.py
python project/research/general_n/2026-09-12-routing-tail-projection-v1/freeze_catalog.py
python project/research/general_n/2026-09-12-routing-tail-projection-v1/replay_profiles.py
python project/research/general_n/2026-09-12-routing-tail-projection-v1/boundary_profiles.py
python project/research/general_n/2026-09-12-routing-tail-projection-v1/pack_evidence.py
```

Only the pilot requires NumPy/SciPy. Pack regenerated evidence before exact
verification, because replay prefers the archived, hash-checked streams.
Keep fresh provenance for reruns; the original logs remain historical evidence.

The [audit](AUDIT.md) records the unsuccessful frontier reduction, all ablation
limits, hypotheses and next decision. The next structural target is stronger
supplement eligibility or label/supplement compatibility, which the current
projection still forgets.
