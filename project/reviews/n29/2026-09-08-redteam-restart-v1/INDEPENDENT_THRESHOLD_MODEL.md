# n=29 Delta=16 — independent cumulative-threshold verifier

8 September 2026. Built during the restarted red-team audit as a deliberately separate final-stage model for the n=29, Delta=16 cases.

**Status:** same-assistant independent reimplementation, not external peer review. The model imports none of the inherited `joint`, shared-LP, degree-type, local-incidence, conditional-ledger or endpoint-model code. Every exclusion is accepted only with an exact integer Farkas certificate. The original candidate proof remains unchanged.

## Purpose and independence boundary

The production n=29 route reduces the two dense Delta=16 scopes to 118 projected rows at `m=211` and 1,225 projected rows at `m=210`, then uses inherited n=28 joint/LP machinery.

This verifier deliberately starts at that **published projected frontier** and replaces the entire later machinery with a new relaxation derived directly from the hand inequalities. The clean workflow regenerates the projected frontier using the already-audited production early stages, but from that handoff onward the verifier is standalone.

The main new idea is to avoid the inherited exact endpoint-degree enumeration. For a label option `(d,R)`, let `x` be its actual selected column degree and introduce cumulative tails

`T_h = Pr(x >= h)`.

Then

`E[x] = sum_h T_h`,

and the selected-slot capacity among labels satisfying `x>=h` is

`E[x 1{x>=h}] = (h-1)T_h + sum_{j=h}^U T_j`,

where `U=16-R`. Nested Hall inequalities use these capacities to host selected incidences whose source endpoint type requires a minimum `x`.

## Variables and necessary constraints

Labels are grouped only by equal demand `s`; sources only by equal residual degree `rho`. This is relabelling/averaging, not an automorphism assumption.

For each label demand group the model chooses a fractional distribution over integer `(d,R)` options satisfying:

- `0<=d<=10`;
- `0<=R<=16`;
- if `s>0`, `d-R=s`;
- if `s=0`, `d<=R`;
- `x<=16-R`, represented through the cumulative tails;
- `x>=s` and `d<=R+x` through mandatory lower tails and the option range.

Globally it enforces

`sum d = 2(r+t)`,

`sum R = r`.

For each residual source group it chooses actual source types `(q,p)` satisfying

`0<=q<=12-rho`,

`0<=p<=rho+3`,

`q+p<=15`.

A separate source-to-supplement `q`-flow enforces:

- a source of actual selected degree `q` sends exactly `q` selected arcs;
- a target source type receives its expected supplement indegree `p`;
- an arc from source degree `q` to target degree `q2` is allowed only if `rho_target+q2>=q-1`;
- each unordered B-pair has total orientation capacity at most one.

Selected source/label incidence flow is allowed only when the pointwise necessary conditions hold:

- `s<=rho_source`;
- `d<=rho_source+R`;
- `d<=rho_source+q-1`;
- `R+x>=q+p`.

The last condition is encoded without enumerating `x`: a source type `(q,p)` meeting label option `(d,R)` requires

`x >= max(1,q+p-R)`.

For every threshold `h`, the total selected incidence flow requiring `x>=h` is bounded by the cumulative-tail selected-slot capacity above. These nested Hall cuts are valid for every actual graph and form the distinctive part of this independent relaxation.

## Exact proof event

SciPy/HiGHS is used only twice as a proposal mechanism: first to detect numerical infeasibility, then to propose a Farkas ray. The proposed multipliers are scaled to integers. The checker accepts an exclusion only after direct integer arithmetic verifies that:

1. every inequality multiplier is nonnegative;
2. equality multipliers are signed integers;
3. the combined coefficient of every nonnegative primal variable is nonnegative;
4. the exact combined right-hand side is strictly negative.

Solver status alone is never a proof event.

## Fresh local red-team result before repository replay

The standalone implementation was first tested outside the production source tree against the preserved projected inputs.

It rejected, with exact certificates:

- `m=211`, `t=3`: **118 / 118**, zero survivors; certificate RHS range **-999503 to -42**;
- `m=210`, `t=2`: **1,225 / 1,225**, zero survivors; certificate RHS range **-999874 to -2**.

The two production endpoint-only rows (projected positions 68 and 801 at `m=210`) are also rejected directly by this new model, with new exact certificate RHS values `-435` and `-454`. Thus the independent route does not rely on the old endpoint certificates `-830` and `-355`.

## Files

- `independent_threshold_model.py` — standalone mathematical model and exact certificate verifier.
- `run_independent_threshold.py` — shardable certificate-producing runner.
- `.github/workflows/n29-independent-threshold.yml` — clean replay, aggregation, exact re-verification and evidence preservation.

The workflow-generated combined certificate bundles and summary are preserved under this review directory after a successful clean replay.

## Audit interpretation

If the clean replay succeeds, Delta=16 will have two materially different final-stage contradictions:

1. the original inherited direct197 joint/shared/typed/endpoint route;
2. this cumulative-threshold/source-flow route, which has different variables, different endpoint abstraction and different exact certificates.

They still share the graph-to-demand/quasi-edge lemmas and the published projected frontier, and they are still authored by the same assistant. Therefore this materially reduces implementation/model risk but does **not** substitute for an independent mathematician or independent external reproduction.
