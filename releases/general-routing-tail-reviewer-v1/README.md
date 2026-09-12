# Demand/tail projection and equality rigidity: reviewer v1

12 September 2026. Candidate general hand lemmas and exact finite applications.
Internal arithmetic status **PROJECT_CERTIFIED**. External mathematical review,
novelty assessment and external reproduction **OPEN**. Publication is not
external acceptance; no unrestricted theorem or improvement to 7/12 is claimed.

Read the [tail projection and closed budget consequences](../../project/research/general_n/2026-09-12-routing-tail-projection-v1/TAIL_PROJECTION.md),
[equality-rigidity hand lemma](../../project/research/general_n/2026-09-12-routing-tail-projection-v1/EQUALITY_BOUNDARY.md),
[internal audit](../../project/research/general_n/2026-09-12-routing-tail-projection-v1/AUDIT.md),
and [research/evidence guide](../../project/research/general_n/2026-09-12-routing-tail-projection-v1/README.md).

The first mechanism pays for established residual-tail lower bounds, then uses
the remaining budget to bound both individual residual degrees and further
tail growth. Inserting this budget into joint routing gives inequalities
involving demands and scalar parameters, before residual enumeration.

The second mechanism characterizes equality in the earlier load inequality:
heavy source degree is h or 2h, and every 2h-sender has incoming degree zero.
The resulting destination-capacity restriction yields a closed criterion
making the load bound strict by one integer unit.

Measured scope:

- A 27-profile pilot gives nine profile exclusions with the residual penalty,
  compared with six when it is disabled.
- A frozen 44-template catalogue adds **114 whole layer/profile exclusions**
  beyond the preceding 45: 79 at N34 m289, six at N35 m307, and 29 at N35 m306.
  There are **1,294 profile survivors**.
- Within that catalogue, eight additional profile exclusions use the residual
  penalty and 52 use the sharper destination term. Two exclusions require
  combining new tails.
- The closed scalar rule adds 40 profiles over the preceding baseline, compared
  with 31 for the ordinary load-cap test. Its nine extra exclusions and all
  40 scalar exclusions are included in the projection's 114.
- **None of the 5,578 states surviving the previous joint-routing catalogue
  is newly excluded.** The new results simplify existing exclusions into
  demand-level theory. Canonical fixed-order proof ledgers remain unchanged.

Exact replay from the repository root:

```sh
python project/research/general_n/2026-09-12-routing-tail-projection-v1/check_budget.py
python project/research/general_n/2026-09-12-routing-tail-projection-v1/verify.py
python project/research/general_n/2026-09-12-routing-tail-projection-v1/verify_boundary.py
python releases/general-routing-tail-reviewer-v1/check_manifest.py
```

These checks use standard-library Python. The main verifier imports no
projection or discovery implementation; the scalar verifier enumerates sender
counts independently of the closed formula. Pilot rediscovery alone needs
NumPy/SciPy. Versions, original solver vectors and all rounding attempts are
preserved, along with negative results and invalid extensions.

`VALIDATION.json` records clean reproduction of the five original streams,
archive-only exact replay and navigation checks. `MANIFEST.json` pins the
new package and its direct inputs; unchanged transitive evidence remains at
repository baseline `fcdacbf32e79930977f7da77697f4b6f90b18ca0`. The manifest
excludes itself and `PUBLICATION_RECEIPT.json` to avoid circular hashes.

Current preceding manifests receive updated navigation and dependent-manifest
hashes. Historical proofs, logs and receipts retain their original snapshot
meaning. The publication receipt records the verified research commit; its
subsequent receipt-only commit is read back separately. Review should focus
on positive residual activity, the cost of changing several tails, correction
signs, global z/j coverage, and the equality classification.
