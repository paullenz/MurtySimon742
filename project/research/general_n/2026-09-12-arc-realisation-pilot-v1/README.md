# Simultaneous routing: a fixed-neighbourhood flow reduction

12 September 2026. Candidate general reduction and bounded exploratory pilot.
External mathematical review, novelty and independent reproduction OPEN.

The useful general development is an exact **conditional routing criterion**.
Fix selected sets S_u and residual sets R_u, and write N_u=S_u union R_u.
A selected incidence (u,i) may have destination v exactly when

    S_u minus N_v={i}, and S_v is contained in N_u.

These conditions make the label and orientation unique for each usable pair.
Routing the fixed sets then reduces to integer flow with destination
capacities rho_v+b-a-1. A failed flow has an independently checkable Hall
obstruction for that fixed pattern. The [general hand proof](FIXED_NEIGHBOURHOOD_FLOW.md)
states the equivalence and proves a receiver-label conflict lemma.

This is B-side routing sufficiency only. Choosing cross sets, constructing
H[A], satisfying the full degree ledger and proving edge-criticality remain
outside the conditional criterion. Standard integer-flow theory is used;
no external novelty claim is made.

| Preserved experiment | Outcome |
|---|---|
| Six fixed survivors, two simultaneous MILP models | All 12 runs reached the time limit without a primal incumbent |
| Twelve deterministic fixed-cross probes | 12 exact pattern obstructions; all explained by empty destination sets |
| Audit of those probes | All already fail some minimum endpoint-load constraints; no measured gain over the old bounds |
| Whole-state exclusions added | **0** |
| Combined frontier retained | **994 exclusions / 4,584 survivors** |

The original six cases are N34 m289 states 60, 7896 and 13537, and N35 m306
states 17, 246 and 454. Selection and limits were frozen before model execution.
The later flow follow-up is explicitly dated and scoped as post-pilot analysis.
Neither timed-out searches nor fixed-pattern obstructions eliminate a state.

## Evidence and reproduction

Read the [audit and failed approaches](AUDIT.md), [model specification](MODEL.md),
[original plan](PLAN.md), [inputs](pilot_inputs.json), [flow follow-up plan](FLOW_PLAN.md),
[complete original results](runs/results.json), [model evidence catalogue](runs/EVIDENCE_STORAGE.json),
[flow probes and certificates](flow_probes.json), and [verification](verification.json).
The [reviewer package](../../../../releases/general-arc-realisation-reviewer-v1/README.md)
pins the complete checkpoint and its dependencies.

Python standard-library checks, from the repository root:

```sh
python project/research/general_n/2026-09-12-arc-realisation-pilot-v1/check_flow.py
python project/research/general_n/2026-09-12-arc-realisation-pilot-v1/check_model.py
python project/research/general_n/2026-09-12-arc-realisation-pilot-v1/verify.py
```

The first check compares the flow criterion with all assignments on 729 tiny
cross patterns and challenges 5,024 additional compatible tiny patterns.
The second checks 8,192 sparse-model/combinatorial cases and preserves a
counterexample to coarse sufficiency for one assignment. The third rebuilds
all twelve stored integer models, recovers their exact hashes, checks every
original result, reconstructs the fixed probes and checks their Hall deficits.

Fresh solver runs require SciPy/NumPy and can be written to a new directory:

```sh
python project/research/general_n/2026-09-12-arc-realisation-pilot-v1/run_pilot.py /tmp/murty-arc-fresh-run
```

The output directory must not exist. Time-limited solver outcomes may differ
across machines. The clean release validator reproduces deterministic checks
and all saved model bytes; it does not rerun or claim to reproduce the original
timings. Original logs, statuses and timing records remain unchanged.

The next bounded search should enforce minimum endpoint loads and a compatible
exception for every selected incidence while constructing cross-neighbourhoods,
then use the exact flow criterion. This study supplies that checker and its
general proof, but does not yet supply a successful search over cross sets.
