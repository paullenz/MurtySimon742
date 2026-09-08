# n=29 restarted red-team: inherited source and certificate audit

8 September 2026. Additive continuation of `N29_RED_TEAM_RESTART.md`. The candidate proof itself is deliberately unchanged.

**Status:** same-assistant red-team only. No blocking mathematical defect found in this continuation. This is not independent peer review, formal verification, or a theorem-ledger promotion.

## 1. Hash-pinned inherited source recovered for direct audit

The n=29 Delta=16 wrapper depends on the preserved n=28 direct197 archive

`project/research/general_n/2026-09-07-direct-197-v8/MurtySimon_N28_197_Direct_v8.zip`

with SHA-256

`b753076ffc755066a0c57756be91cc5b265c163d869244d3aa65e3943799347b`.

A read-only workflow `.github/workflows/n29-redteam-extract.yml` was added solely to verify that hash on a clean Ubuntu runner, extract the archive, and expose its source for inspection. Run `34234312834` completed successfully. The extracted artifact was then inspected directly in this restarted audit.

The following load-bearing source families were line-audited against independently rederived mathematics:

- demand discovery/checking: `dependencies/v3_discover.py`, `dependencies/v3_check.py`;
- joint propagation/checking: `exploration/joint.py`, `exploration/check_joint.py`;
- row-support feasibility/checking: `exploration/row_support.cpp`, `exploration/check_row_support.cpp`, `exploration/row_interface.py`;
- shared LP and Farkas mechanism: `dependencies/common_lp.py`, `dependencies/check_constraints.py`;
- degree-type refinement: `dependencies/degree_types.py` and its independent rebuild;
- source-local/conditional ledgers: `src/local_incidence.py`, `src/check_local.py`, `src/conditional_ledger.py`, `src/check_ledger.py`;
- endpoint/total-degree refinement: `src/total_degree.py`, `src/check_total.py`.

## 2. Fresh independent domain checks

The restarted audit did not rely only on agreement between the two committed residual scanners.

Starting from the rederived charging condition, an independent enumerator regenerated every nondecreasing length-12 demand tuple with `0<=s_i<=10`:

- `t=3` (`m=211`): **4,867** tuples;
- `t=2` (`m=210`): **9,251** tuples.

For the retained demand intervals, a separate integer-partition dynamic program independently counted all sorted length-16 residual rows with entries in `1,...,12`. It reproduced every per-demand raw band count and the full totals:

- `t=3`: **1,848,957** residual rows;
- `t=2`: **5,765,218** residual rows.

The grouped row-survivor totals also reproduced exactly: **206** and **2,087**.

A further independent projected-stage implementation used a cardinality dynamic program for forced high-degree labels and a direct unordered-pair count, rather than the wrapper's shortcut. It reproduced the saved survivor sets exactly, not merely their cardinalities:

- `m=211`: 206 -> **118**;
- `m=210`: 2,087 -> **1,225**.

This closes three important exhaustiveness boundaries without depending on common source lineage.

## 3. Parameter-adaptation audit

Several inherited n=28 routines have defaults appropriate to their original scope. The n=29 production wrapper was therefore checked specifically for a silent old-parameter leak.

The proof run explicitly supplies the current surplus `t` to:

- `joint.propagate`;
- `check_joint.verify_row`;
- every shared, typed and endpoint LP builder;
- every independent named-system rebuilder;
- demand enumeration/bounds/checking;
- projected-stage degree totals and slack equations.

It also explicitly passes `dmax=10` / `maxd=10` at the joint stage. The mathematical justification for that cap and for `r<=60-t` is the valid `k>=1` bridge recorded as finding `RT-N29-001` in the main restart report.

**Verdict:** no inherited `t=1` default leak was found in the n=29 proof run.

## 4. Row-support model audit

For one B-source of residual degree `rho_u` and candidate selected degree `q_u`, the row-support model asks only whether the A-labels can be partitioned into selected, residual and missing incidences while preserving the exact column totals and already-proved local inequalities. It does not assert that a graph exists.

The strongest-looking selected-incidence cut was rederived independently. If `ui` is selected, every F-neighbour of label `i` must be an H-neighbour of `u`. At most `rho_u` of those cross-edges are residual. Hence at least `d_i-rho_u` are selected in addition to `ui` itself, giving

`q_u >= d_i-rho_u+1`.

The production row-support code and the independent checker implement the same necessary feasibility question using different generating-polynomial machinery. No unsafe strengthening was found.

## 5. Demand support and exact dual pruning

The high-demand support bound was rederived from residual activity, `q_u+rho_u<=a`, supplement forcing, and the injection of selected arcs into unordered B-pairs.

For threshold `h`, high-demand labels require sources with `rho>=h`. Residual activity gives an upper bound on the number `z` of such sources. Sources outside this set cannot select high-demand labels and have total A-degree below the large-source threshold. If `p` high-residual sources are large, every supplement of each large source must also be high-residual, while the selected-pair injection supplies only

`C(z,2)-C(z-p,2)`

available unordered pairs incident with those large sources. This yields the support-capacity inequality used by the code.

The demand dual cut is a Hall/capacity relaxation by residual-degree type. A source of residual degree `j` can supply at most `a-j` selected incidences and only labels with demand at most `j`. The exact checker verifies the proposed dual weights against every residual type using integer arithmetic. Floating-point LP status is only a source of candidate weights, never a proof event.

**Verdict:** no mathematical or one-way-certificate defect found.

## 6. Joint propagation and symmetrization audit

The joint state was checked against the underlying pointwise graph inequalities. In particular:

- selected incidence: `d_i<=rho_u+R_i` and `d_i<=rho_u+rho_w`;
- selected source/supplement forcing: `rho_w+q_w>=q_u-1`;
- source/column selected load: `R_i+x_i>=q_u+p_u`;
- source simplicity: `q_u+rho_u<=a`;
- supplement indegree: `p_u<=rho_u+(b-a-1)` and `q_u+p_u<=b-1`;
- exact global column totals and selected-demand lower bounds.

The apparent symmetry reductions do not assume graph automorphisms. Labels and sources are grouped only by identical already-fixed numerical data. The LP variables can be interpreted as averages of actual 0/1 indicators over permutations within those identical-data classes. Every retained constraint is linear and pointwise valid before averaging, so it remains valid afterward.

No unsafe quotienting assumption was found.

## 7. Shared, typed and endpoint LP models

The shared LP was checked constraint-family by constraint-family. Its variables encode averaged selected/residual/missing status, residual columns, F-edge incidences and selected-source/supplement arcs. Its constraints are relaxations of the independently rederived graph inequalities, including the source-local inequality

`sum_{i in S_u} d_i <= rho_u(2a-rho_u-3+q_u)-2t`

and the disjoint residual-column bound

`sum_{i in S_u} R_i <= r-rho_u`.

The degree-type refinement conditions on actual source selected degree `q_u`; pair-type flow enforces the supplement requirement `rho_w+q_w>=q_u-1`.

The endpoint refinement additionally conditions on exact column selected degree `x_i` and source supplement indegree `p_u`. Its joint selected-incidence variables only allow `(q,p,x)` combinations satisfying the pointwise endpoint load `R_i+x_i>=q+p`. The marginal equations recover the typed source and column distributions.

Every variable-name list was also checked for accidental collisions in the two deepest endpoint cases; all names were unique.

**Verdict:** no blocking modelling defect found.

## 8. Exact Farkas verification audit

The numerical solver is used only to propose a dual ray. The certificate routine rationalizes/scales it and, where necessary, adds nonnegative multiples of individual `x<=1` bounds to eliminate negative primal-variable coefficients. The exact verifier then requires:

1. nonnegative multipliers for inequalities;
2. unrestricted signed multipliers only for equalities;
3. the exact combined coefficient of every nonnegative primal variable to be nonnegative;
4. an exact combined right-hand side strictly below zero.

The independent named-system checker does not trust the discovery model object. It separately reconstructs the named equalities and inequalities, rejects unknown/duplicate names or invalid multipliers, and verifies the same contradiction exactly.

Thus an optimizer status of `infeasible` is never, by itself, counted as an exclusion.

## 9. The two deepest m=210 endpoint cases

The only two `m=210` rows that survive both the shared and degree-type LPs were regenerated and rechecked separately.

### Projected position 68

- residual total `r=24`;
- residual row: twelve 1s followed by four 3s;
- demand row: four 1s followed by eight 3s;
- shared model feasible;
- typed model feasible;
- endpoint model infeasible;
- exact independently named Farkas certificate right-hand side: **-830**.

### Projected position 801

- residual total `r=39`;
- residual row: seven 1s, four 3s, five 4s;
- demand row: five 3s followed by seven 4s;
- shared model feasible;
- typed model feasible;
- endpoint model infeasible;
- exact independently named Farkas certificate right-hand side: **-355**.

The two complete regenerated named certificate objects are preserved in `N29_ENDPOINT_CERTIFICATES.json.gz.b64`; recovery and hashes are documented below.

## 10. Finding RT-N29-002 — production certificate retention

**Severity:** low / auditability and evidence preservation.

**Mathematical impact found:** none.

The n=29 production wrapper does the right mathematical thing at runtime: for each LP rejection it obtains a candidate Farkas certificate, verifies it against the model, translates it into the named representation, independently rebuilds the named system, and verifies the named certificate exactly.

However, after verification the shard report increments only the phase counter (`shared`, `typed`, or `endpoint`) and discards the certificate object. The GitHub Actions artifacts therefore preserve the final phase counts and the fact that exact verification succeeded, but not the 629 exact certificate objects accepted in that original run.

A fresh replay deterministically regenerates and rechecks them, so this is not a proof failure. It is nevertheless a real preservation weakness for external auditing: an auditor wishing to inspect the originally accepted exact certificates must rerun the discovery/checking pipeline.

**Recommended repair for a future proof edition:** make the final harness save every named exact certificate, its projected position/state key, exact checker/system signature, and hash; publish a complete certificate bundle. Do not retroactively rewrite the currently audited candidate artifacts.

## 11. Endpoint certificate bundle recovery

`N29_ENDPOINT_CERTIFICATES.json.gz.b64` is base64 text containing a deterministic gzip stream (`mtime=0`) whose uncompressed payload is canonical compact JSON followed by a newline.

Expected hashes:

- uncompressed JSON SHA-256: `7f43ab2413700044e9d5753c7a65a2cb0654fec2bc1f0a4edb8958c342dda938`;
- gzip SHA-256: `e506de04c3f8f3e347721cecb934963e7300b5ca6f3a39b9fa894b1787ea85c4`;
- uncompressed bytes: 56,595;
- gzip bytes: 31,151.

Recovery example:

```sh
base64 -d N29_ENDPOINT_CERTIFICATES.json.gz.b64 > N29_ENDPOINT_CERTIFICATES.json.gz
printf '%s  %s\n' e506de04c3f8f3e347721cecb934963e7300b5ca6f3a39b9fa894b1787ea85c4 N29_ENDPOINT_CERTIFICATES.json.gz | sha256sum -c -
gzip -dc N29_ENDPOINT_CERTIFICATES.json.gz > N29_ENDPOINT_CERTIFICATES.json
printf '%s  %s\n' 7f43ab2413700044e9d5753c7a65a2cb0654fec2bc1f0a4edb8958c342dda938 N29_ENDPOINT_CERTIFICATES.json | sha256sum -c -
```

## 12. Updated restarted-audit verdict

At this checkpoint:

- the Delta=15 hand proof has survived a first-principles red team;
- the complement/quasi-edge ledger, residual activity, charging, Delta=17 pointwise bound and Delta>=18 h-index closure have survived rederivation;
- the Delta=16 demand domain, full residual-domain counts and projected survivor sets have independent fresh reconstructions;
- the inherited row-support, joint, shared, typed and endpoint source has been line-audited against the hand model;
- the two deepest endpoint contradictions have independent exact named certificates;
- `RT-N29-001` is a repairable proof-traceability gap, not a mathematical failure;
- `RT-N29-002` is a repairable certificate-preservation gap, not a mathematical failure.

**No blocking mathematical defect has been found. The n=29 candidate is materially stronger after this restarted red team, but it should remain labelled CANDIDATE until genuinely independent expert mathematical review and independent computational reproduction are obtained.**
