# Tight-block equality forces exact selected sets

15 September 2026. General structural lemma and internally checked scalar
whole-state certificates. External review OPEN; no ledger promotion.

## Result

The equality case of the [tight-label block theorem](../2026-09-15-tight-label-block-v1/README.md)
is rigid: the high vertices can select only the tight block, and all selected
labels at its receivers must fit inside every high vertex's residual set.
This excludes 25 of the current 952 states without enumerating q.

Python and independently structured C++ checks agree on all 4,588 frozen
inputs: 164 satisfy the equality hypotheses and all 164 violate the resulting
union bound. The other 4,424 are outside this lemma's scope, not excluded by it.
Of the 164, 25 are active N34-derived states and 139 are already ledger-closed.
Nine of the 25 overlap the earlier 170 forced-core candidates; 16 are additional.
Together with the preceding strict-block result, the two new lemmas certify
41 active states: 19 overlapping the previous 170 and 22 additional distinct
keys. No N35 active state is rejected. Canonical counts remain
4,626 exclusions / 952 survivors / 3,632 whole-state closures.

## 1. Equality hypotheses

Use the same canonical graph-to-selected/residual hypotheses as the preceding
package. Fix d>=1 and suppose

    T={i:s_i=d},        |T|=d,
    H={u:rho_u>=d},     |H|=d,
    M={v:rho_v=d-1},    |M|=d.

Let L be the other vertices, with rho<d-1. Tight demand forces T subset S_u
for every u in H. Every T obligation must go to M, by the preceding theorem.
Each u has d such obligations with distinct destinations; therefore each u
uses every vertex of M exactly once.

If v receives the T-label i, its residual set is exactly T minus {i}:
it cannot select T, it must contain the other d-1 labels, and rho_v=d-1.
In particular S_v is disjoint from T.

We also use the reverse containment S_v subset N_u for a selected arc u->v.
For completeness: any selected edge (v,j) has a destination different from u,
because the unordered pair {u,v} already has its chosen orientation u->v.
Its quasi-edge must dominate u. Since uv is missing, ju is present, proving
j in N_u. This follows directly from canonical representative uniqueness.

## 2. No high vertex has an extra selected label

Suppose j in S_u minus T for some u in H. For each v in M, the T obligation
from u to v forces j in N_v. Since R_v is contained in T, actually j in S_v.

Every w in H sends a T obligation to every v in M. Reverse containment then
forces S_v subset N_w, so j belongs to N_w for every w in H. Thus j cannot
be routed to a vertex of H, because its destination must omit j.

It cannot be routed outside H either: all d labels of T would need to belong
to that destination's neighbourhood. Outside H none of T can be selected,
and fewer than d residual slots are available. This is impossible.

Every selected label has a destination. Hence the supposed extra j cannot
exist, proving the exact structural identity

    S_u=T, and therefore q_u=d, for every u in H.                (E1)

This is stronger than merely bounding the number of extra selections by
the number of unordered pairs within H.

## 3. Residual union bound

Put Q=union_{v in M} S_v. Reverse containment places Q in N_u for every
u in H. Since Q is disjoint from T and S_u=T by E1, Q is contained in R_u.
Therefore

    |Q| <= min_{u in H} rho_u.                                  (E2)

For a label i outside T, high vertices supply no selected occurrences.
Vertices in L supply at most e_L(i)=|{w in L:rho_w>=s_i}| occurrences.
If s_i>e_L(i), its demand forces at least one selected occurrence in M.
Consequently the explicitly known set

    K={i outside T:s_i>|{w in L:rho_w>=s_i}|}

is contained in Q. Combining with E2 gives the scalar necessary inequality

    |K| <= min_{u in H} rho_u.                                  (E3)

This involves only s and rho and holds for every q and every selected/residual
realization. It does not require an exhaustive search or a solver status.

## 4. Hand example: state 5802

    s=(1,1,3,3,4,4,4,4,4,4,5,5,5,5,5)
    rho=(1,1,1,1,1,1,1,3,4,4,4,4,4,5,5,5,5,5)

Here d=5; H is the final five vertices, M the five residual-four vertices,
and L the seven residual-one vertices plus one residual-three vertex.
Both demand-three labels and all six demand-four labels require a selected
occurrence in M: L can supply at most one occurrence of each demand-three
label and none of a demand-four label. Thus |K|=8. But each high residual set
has only five slots, so E3 requires 8<=5, a contradiction.

State 5973 similarly forces nine labels into five residual slots.
The complete 25 active certificates are recorded in RESULTS.json.

## 5. Weaker preliminary argument, preserved

Before E1 was derived, the calculation used e_u=|S_u minus T|. All extra
selected obligations must stay inside H, so sum e_u<=d(d-1)/2. Forced union
membership gives e_u>=max(0,|K|-rho_u). Thus

    sum_{u in H} max(0,|K|-rho_u) <= d(d-1)/2.

This valid weaker inequality rejected 142 of the 164 applicable inputs and
23 of the 25 active ones. E1/E3 also reject active states 911 and 5915, which
the weaker inequality did not exclude. Both outcomes are retained in every
certificate; the initial 23-state observation is not the final result.

## Evidence, provenance and replay

The exact inputs and baseline active-state flags are frozen in the preceding
tight-label-block-v1 package at commit
1992778d461056d365cc0c3584b510134b2b93ed. They reconstruct the decoded catalogue
SHA256 2c6bb11ec3c6dfb45a07b511c1e85c8c44898201c0f045630e0f622ee93647eb
and the 952-state frontier at that checkpoint. RESULTS.json retains all164
applicable certificates, including the weaker argument's non-rejections;
INDEPENDENT_RESULTS.tsv records scope and decisions for all4,588 inputs.
FORCED_CORE_OVERLAP.json preserves the exact overlap with all170 earlier keys,
their job provenance, and the completed census totals. It is log-derived;
it does not replace the separately audited original discovery artifact.

Run from a repository checkout:

    python3 project/research/general_n/2026-09-15-tight-label-equality-v1/run_replay.py

This recomputes the Python evidence, compiles a separate C++ checker in a
temporary directory, and requires exact agreement for all4,588 rows. Local
replay passed. Both implementations are internal; external mathematical
acceptance, reviewed ledger promotion and third-party reproduction remain
separate. No fresh remote proof execution is claimed in this package.

## Next mathematical question

Study |M|=d+1. Each high source may omit one receiver, so exact residual
membership and source/receiver incidence can no longer be inferred for all
pairs. Quantify the omitted pairs and derive a bound on extra selected labels
before attempting any scalar exclusion. The full q enumeration of the earlier
saturated-barrier witnesses remains unresolved and must not be called complete.
