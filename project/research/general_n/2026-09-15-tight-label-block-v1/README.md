# Tight-label blocks: a scalar destination obstruction

15 September 2026. Internal general lemma and whole-state certificates;
external mathematical review OPEN. No canonical ledger promotion.

## Result

The inequality below rejects 108 of the 4,588 frozen catalogue rows, including
16 of the current 952 canonical survivors. Python and an independently
structured C++ implementation agree on all 4,588 decisions. All 16 active
certificates have five tight labels of demand five, five forced sources,
and only four possible destinations. This proof uses only s and rho; changing
the selected-degree witness q cannot repair it.

Active N34-derived state IDs:
5507,5573,5580,5586,5588,5591,5631,5644,5666,5667,5669,5672,5690,5691,5694,5710.
No N35 active state is rejected. These overlap earlier forced-core candidates;
ten overlap the earlier 170 candidates. The six additional IDs are
5586,5666,5667,5672,5694,5710; do not double-count the other ten.

## Canonical hypotheses

Use the [canonical selected/residual bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md),
Sections 3, 5, 6.2, 6.4 and 7: label i is selected at at least s_i distinct
sources; selection at u implies s_i<=rho_u; each source's selected labels have
distinct destinations; an obligation (u,i)->v has i absent from N_v and every
other selected label of u present in N_v; incoming capacity is at most
c_v=rho_v+b-a-1. Here N_v=S_v union R_v, with disjoint selected/residual sets
and |R_v|=rho_v. The argument does not assert these conditions sufficient for
a graph, and relies on the same bridge whose external review remains open.

## Theorem and proof

Fix an integer d>=1 with exactly d vertices satisfying rho_u>=d. Let

    H_d={u:rho_u>=d},   T_d={i:s_i=d},   k=|T_d|>0.

Each label in T_d needs at least d selected occurrences, all in the d eligible
vertices H_d. Therefore every vertex of H_d selects every label of T_d.

Consider one of its k obligations (u,i), with i in T_d. Its receiver v cannot
lie in H_d, since those vertices already select i, whereas i must be absent
from N_v. Thus rho_v<d. Eligibility prevents v from selecting any label in
T_d. The other k-1 labels must nevertheless belong to N_v, so all belong to
R_v. Necessarily rho_v>=k-1.

Hence all these destinations lie in

    M_d={v:k-1<=rho_v<d}.

Destinations at one source are distinct, proving the scalar inequality

    |M_d| >= k.                                               (TB1)

Moreover a receiver handling a T_d obligation is missing exactly one label
of T_d, so it can handle only that label, with at most one occurrence from
each of the d sources. Its contribution is at most min(d,c_v). Therefore

    d*k <= sum_{v in M_d} min(d,max(0,c_v)).                    (TB2)

The max with zero merely weakens the bound if an impossible negative receiver
capacity is supplied. In a graph every c_v is nonnegative. TB2 implies TB1
because each summand is at most d; both are retained for readable certificates.
The 16 active contradictions need only TB1, and do not depend on numerical
receiver capacities or any exhaustive search over q.

## Hand example: state 5666

Its label demands are

    s=(1,1,3,3,3,4,4,4,4,4,5,5,5,5,5)

and its residual degrees are

    rho=(1,1,1,1,1,1,1,3,3,4,4,4,4,5,5,5,5,5).

The five demand-five labels must all be selected at each of the final five
vertices. A receiver must be outside those five and have at least four
residual slots. Only vertices 9,10,11,12 qualify (zero-based indices).
Each source needs five distinct destinations among four vertices: impossible.
Equivalently TB2 reads 25<=20. The other 15 active certificates have the same
five-versus-four obstruction; their exact inputs are in CANDIDATE_STATES.json.

## Evidence and limits

The catalogue is the existing survivors.json.gz.b64 in
../2026-09-12-compatible-routing-catalogue-v1/. Decoded SHA256:
2c6bb11ec3c6dfb45a07b511c1e85c8c44898201c0f045630e0f622ee93647eb.
The 4,588 rows contain 4,584 combined survivors. Removing the current N34/N35
whole-state ledgers reconstructs exactly 952 active states (949 N34, 3 N35).
The replay pins this scope and fails if it changes.

RESULTS.json.gz.b64 preserves every check and non-rejection. The independently
structured C++ replay reconstructs forced membership and residual requirements
label by label rather than importing Python threshold certificates. The
integer comparison of all 4,588 decisions passed locally. No remote execution
or third-party reproduction of this new package is claimed at this checkpoint.

Canonical counts remain 4,626 exclusions / 952 survivors / 3,632 whole-state
closures. Internal whole-state certificates are distinct from the separate
reviewed promotion and external mathematical acceptance.

## Completed earlier census

CENSUS_COMPLETION.json preserves the exact aggregate summary read from GitHub
job 104561296194, run 34999206636, head
52ea9f1d787736a2c93451ef05886061085af27f. The run completed SUCCESS at
2026-09-15T20:54:48Z: all 170 state universes, 25,769,305,797 profiles,
15,307,737,127 aggregate rejections, zero partition-gap profiles. The aggregate
reports exact reconciliation with the authoritative primary core-failure count.
This is finite empirical equality, not a theorem of general equivalence.
Final artifact 10418246216 has ZIP SHA256
783f5c65d53fc84347e954c281cb688153bde81ad62b25b7e994fe0cb803fc68.
The artifact itself was not downloaded here; the preserved summary is log-derived.

## Preserved interrupted and exploratory work

The preceding saturated-prefix whole-state pilot for state 3349 was stopped
after eight seconds (exit 124), with no result. It is unresolved, not excluded.
Its scanner/input and the forced-label flow exploration are retained under
exploratory/. The flow results are fixed-witness exploratory output; no
independent flow-certificate validation is claimed. The scalar theorem above
has a separate direct proof and independent integer replay.

## Next mathematics

Reconcile the 16 states with the complete earlier 170 candidate keys. Then
study the equality case |M_d|=k: every source must use every available receiver,
forcing their residual sets and potentially constraining low-label selections.
Retain non-rejections and check any resulting bound without q assumptions
before calling it another whole-state certificate.
