# Saturated receiver barrier and joint forced-core cuts

15 September 2026. **Internal necessary-condition derivation; external review OPEN.**

## Result and scope

The saturated-receiver barrier below rejects **24 of the 124 preserved fixed-q rescue witnesses**. All 124 first pass the old independent scanner's full acceptance conditions. A separately coded direct r=1 capacity check reproduces exactly the same 24 rejections. These are not 24 whole-state exclusions: changed q can rescue a state, so the canonical ledger remains **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The prior audited forced-core reduction to 782 remains separately unpromoted.

Rejected witness IDs (N34-derived):
3349,4629,4687,5694,5993,6139,6273,6848,7079,7225,7327,7728,7932,8254,8358,9107,9340,9573,9851,10068,10276,10509,10510,10845.

## 1. A saturated selected set cannot receive its own labels

Use the canonical eligibility implication i in S_v => s_i <= rho_v. Define
A_r={i:s_i<=r}, h_r=|A_r|. If q_v=h_{rho_v}, eligibility and cardinality force
S_v=A_{rho_v}. Call this vertex saturated.

The fixed-neighbourhood routing rule for (u,i) -> v requires i not in N_v,
and S_v is a subset of N_v. Hence a saturated v cannot receive any obligation
whose label satisfies s_i<=rho_v. This is a forced membership obstruction,
not a numerical capacity estimate.

This applies even when v is saturated at a different residual level from the
source core. Excluding only the sources of the current core misses it.

## 2. General prefix-capacity inequality

Fix an active core r:
U_r={u:rho_u=r,q_u=h_r}, m_r=|U_r|>0.

Every u in U_r has S_u=A_r. Retain the deliberately relaxed receiver superset
D_r={v not in U_r:q_v<=h_r+r-1, q_v+rho_v>=h_r-1, c_v>0},
where c_v=rho_v+b-a-1.

For every demand value d<=r, any realization necessarily satisfies

    m_r h_d <= sum_{v in D_r:
                    q_v < h_{rho_v} OR rho_v < d} min(c_v,m_r).       (P)

Proof: there are m_r obligations for each of the h_d labels in A_d. A receiver
can serve only one label of A_r, since A_r minus N_v must be a singleton.
It therefore receives at most m_r of these obligations and at most c_v overall.
If saturated and rho_v>=d, it contains every label of A_d in S_v and cannot
receive any of them. Summing the remaining upper capacities proves (P).
The q_v<h_{rho_v} alternative uses the standing eligibility bound q_v<=h_{rho_v}.

For a label subset with largest demand d, including all of A_d only increases
its demand without adding a receiver to this relaxed union. Thus prefixes
suffice for this particular single-core saturated-membership Hall test.

## 3. Small explicit contradiction: state 3349's saved witness

Here a=15,b=18 and s=(1,3,3,4,4,4,4,4,4,4,4,4,4,4,4).
At r=1 there is one core label, and four forced sources, indices 1,2,3,4.
Only vertex 0 (q=0,rho=1) remains a possible receiver under (P), with capacity
rho+b-a-1=3. Vertex 5 has q=1,rho=2; since h_2=1 it is saturated and already
contains the sole core label, so it cannot receive that label.
All later vertices have q>=2 and fail the q<=1 receiver requirement.
Thus **4<=3 is necessary and false**, excluding this saved witness.

The previous relaxation counted vertex 5 as an available destination.
The theorem explains exactly why that apparent spare capacity is unavailable.

## 4. Simultaneous nested-core extension

Distinct residual levels have disjoint forced source sets. Their cores A_r
are nested. A receiver serving two such cores must serve the same label:
if A_r subset A_R and A_r minus N_v={i}, then A_R minus N_v={j}
forces i=j.

For a chosen set J of active cores and a set I of labels define

    demand(I,J)=sum_{r in J} m_r |I intersect A_r|,
    W_vi(J)=sum_{r in J: i in A_r, v in D_r} m_r.

Delete a label i as a possible choice for saturated v when s_i<=rho_v.
Then the common-label/shared-capacity restriction gives

    demand(I,J) <= sum_v max_{allowed i in I} min(c_v,W_vi(J)).        (J)

An empty maximum is zero. Every receiver's actual contribution is bounded
by the term for its one actual label; summing proves (J).
The implementation tests subsets of equal-demand label groups, retaining the
full multiplicity on the left. The 24 rejections already have single-core
certificates; no extra gain from multiple cores is claimed here.

## 5. Other directions tested, including non-improvements

A shared-capacity core/tail screen without saturated label restrictions made
602 checks and rejected **zero** of the 124 saved witnesses.

A nonnegative weighted-threshold fractional-cover screen made 6,481 checks
and also rejected **zero**. Its necessary inequality is valid: one actual
receiver selection must obey all threshold loss budgets simultaneously, so
any nonnegative weighted sum is bounded by the correspondingly weighted
available slack. The tested price family is finite and not complete.

Adding saturated label restrictions made 1,040 checks and rejected 24.
All controls and non-rejections remain in JOINT_CORE_RESULTS.json.

## 6. Evidence and exact replay

RESCUE_PROFILES.json reconstructs all 124 inputs from the frozen compatible
catalogue and the committed CERTIFIED_RESCUES.tsv at predecessor 61ef5f1.
The catalogue's encoded Git blob is
329c3ad8657dceac58fa6da5704ce027d53814cc; decoded SHA256 is
2c6bb11ec3c6dfb45a07b511c1e85c8c44898201c0f045630e0f622ee93647eb.
The local frozen copy's Git blob was checked against current main's tree.

The Python exploration and C++ replay are independently structured but are
both internal work, not external verification. The C++ baseline contains the
preserved old type-multiplicity scanner and replays each exact q rather than
re-enumerating a state.

    python3 project/research/general_n/2026-09-15-saturated-receiver-barrier-v1/run_replay.py

This uses a temporary directory, recomputes Python output exactly, compiles
the C++ replay, verifies all 124 old passes and the exact 24 new failures,
and preserves the frozen outputs unchanged.

An initial comparison used a C++ check restricted to h=1 and therefore found
only 22 of the 24; the two h=2 certificates were outside that harness's scope.
Extending the direct r=1 check to h>=1 recovered both and produced exact
agreement. No mathematical acceptance condition was weakened.

Two attempts to download earlier full-run artifacts into this session returned
HTTP 403. Those artifacts were not used to manufacture promotion or input
coverage. This package uses the already committed witness list and hash-matched
frozen catalogue. Full artifact preservation/promotion remains a separate task.

## Next mathematical step

Insert (P) into the exact q enumeration for the 24 affected states, preserve
every replacement witness, and distinguish full exhausted exclusions from
fixed-q rejections. Then test the stronger joint inequality (J) if the simpler
prefix bound leaves relevant cases. Keep every negative result and all ledger
changes behind the existing separate reviewed promotion gate.

