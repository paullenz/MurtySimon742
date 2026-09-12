# General heavy-load and routing family: reviewer v1

12 September 2026. **Candidate structural inequalities across graph orders.**
External mathematical review, novelty assessment and external reproduction OPEN.

Start with the [hand proof](../../project/research/general_n/2026-09-12-heavy-load-family-v1/HEAVY_LOAD_FAMILY.md),
[focused hostile internal audit](../../project/research/general_n/2026-09-12-heavy-load-family-v1/AUDIT.md)
and [research/replay index](../../project/research/general_n/2026-09-12-heavy-load-family-v1/README.md).

## Candidate results

For a heavy threshold h>=1, define k_h as the number of labels with s>=h,
z_h as the number of sources with rho>=h, and r as the residual budget.

- If all those sources have p<=3h, then `4h k_h<=r+4h z_h`.
- With larger incoming degrees, the weighted version has the explicit penalty
  `sum_Z(p-3h)_+`. The canonical source caps turn this into a formula in
  the demand and residual profiles.
- Every integer cutoff T>=h has an exact source maximum
  `max(hT,h(h+P),floor(T^2/4))`. Individual source capacities admit an exact
  elementary refinement using at most five pieces.
- For positive surplus and delta=b-a<=2h+1, the family gives new residual-tail
  lower bounds and a demand-only inequality, avoiding residual enumeration.
- In particular, `all demands <=2, t>0, delta<=5 => 9t+4delta<=a`, with
  no residual-degree cap. This is a low-demand infinite-family restriction.

These statements follow from the canonical bridge, endpoint-load transport
and heavy-arc supplement routing. They require their stated hypotheses and
do not give an unrestricted solution or a new complete fixed order.

## Exact applications and negative results

Across 14,031 preserved N34/N35 state records, 4,880 fail the existing exact
positive-demand budget, 871 have new family witnesses, and 8,280 survive the
searched family. The 871 include **595 formerly envelope-certified states**.
The existing fixed-order reviewer packages retain their published ledgers.

The demand-only tail test excludes **45 layer/profile instances** before
residual expansion: 30 at N34 equality, three at N35 m=307 and 12 at N35 m=306.
The full profile domain has 1,453 records.

All state witnesses use T=4h. Wider integer cutoffs T=h..4a and individual
capacity refinements add no further exclusions in this experiment. Their
survivors, search parameters and negative results are preserved. Twenty-four
explicit local counterexamples show why two tempting extensions fail; the
earlier p=5 failure of the old N34 cutoff is also retained. None is a graph
counterexample to Murty–Simon.

## Replay and provenance

Python standard library only:

```sh
python project/research/general_n/2026-09-12-heavy-load-family-v1/check_local.py
python project/research/general_n/2026-09-12-heavy-load-family-v1/verify_applications.py
python releases/general-heavy-load-reviewer-v1/check_manifest.py
```

The local checker passes 15,201,197 source options and 2,556,945 label checks,
including 589,457 capped and 17,042 uniform exact maxima. The application
checker imports no new discovery or bound-formula code and checks 883,922
local source inequalities for the saved witnesses, full original domains,
strict gaps, all tail calculations and the complete surviving-state record.

[MANIFEST.json](MANIFEST.json) pins the artifacts and unchanged transitive
dependency baseline. [VALIDATION.json](VALIDATION.json) records clean replay,
reproduction of the search outputs, original-byte recovery and navigation
checks. Large records are stored losslessly with both original and encoded
hashes. Earlier proofs, failed approaches and correction histories remain
preserved, including the [original N34 hand argument](../../project/reviews/n34/2026-09-12-heavy-independent-v1/HAND_PROOF.md).

Paul Lenz directed the work. ChatGPT/Geeps developed the candidate arguments,
software and internal audit. Separate implementations remain internal checks;
external expert review and novelty assessment are still required.
