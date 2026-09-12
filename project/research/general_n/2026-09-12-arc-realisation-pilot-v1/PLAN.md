# Simultaneous arc-realisation pilot: frozen plan

12 September 2026. Baseline main: `31b5e78d9f80bc9328973db03ab6f497025e5ddc`.
This plan and the six inputs are saved before running any new solver model.

Question: can locally admissible labelled source capacities coexist in one
oriented graph of selected missing B-pairs? Does retaining the actual cross
neighbourhood forced by each representative add strength?

Select first, middle (zero-based floor(length/2)), and last state ID in each
layer of the preceding 4,584 combined survivors. This gives six cases; no
selection on new outcomes. The input file pins the source archive and plan.
It is a diagnostic sample, not a statistical or full-frontier experiment.

Two models use binary selected/residual A-B incidences and labelled oriented
B-arcs. Both impose residual row counts, disjoint cross incidences, label
demands, eligibility s_i<=rho_u, source and receiving degree bounds, one
orientation per unordered B-pair, endpoint load, coarse destination
eligibility, and heavy destination forcing for every nonempty integer demand
threshold. They therefore retain simultaneous routing and residual placement.

The stronger model also requires each arc's label to be absent at its
destination and all other missing B-neighbours of its source to contain that
label. These are necessary B-side quasi-edge domination conditions. Neither
model constructs H[A] or verifies diameter-two edge-criticality of a graph.

Run the two models in the stated order (`degree_routing`, `label_compatible`)
for each case in layer/state order. Use scipy.optimize.milp, zero objective,
presolve enabled, a 20-second solver time limit and 100,000-node limit per
run. A separate process has a 45-second wall guard. No parameter tuning,
symmetry assumptions, sample replacement or longer retries in this frozen
pilot. Preserve exact model bytes (losslessly encoded if useful), hashes,
all solver logs, floating output, timings and verified integer witnesses.

A separate standard-library verifier reconstructs the combinatorial objects
without importing the model builder and checks integer witnesses directly.
It also checks the encoded linear rows against a witness, when present.
Abstract tiny-object enumeration will challenge the B-side implication and
the receiver-label conflict lemma, with explicit scope and counts.

Only exact checked witnesses establish feasibility of the tested relaxation.
A solver infeasibility status is an uncertified report, not an exclusion;
a limit/no incumbent is OPEN. No incumbent or solver status is a graph proof.
The combined exclusion count remains 994 unless a new independently checked
exact exclusion certificate is supplied. All unsuccessful approaches and
audit challenges remain visible. Any follow-up beyond this plan is labelled
post-pilot and frozen separately before its own computation.

Keep fixed-order proof ledgers and forecasts unchanged. Update README and
reviewer entry points if the outcome changes the research direction; publish
the complete checkpoint and verified receipt without further permission.
