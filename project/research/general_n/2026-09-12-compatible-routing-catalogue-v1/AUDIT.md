# Audit, unsuccessful approaches and corrections

12 September 2026. Same-assistant mathematical audit and separately structured
implementations. External specialist review, novelty and external reproduction
OPEN. Paul handles external review separately.

## Graph implications and exact acceptance

The candidate graph-to-source bridge and compatible-routing inequalities are
dependencies, not facts established by this finite replay. The selected arc
u->v requires rho_v+q_v>=q_u-1. Heavy arcs from senders H>h have destination
capacity 1[rho>=h] min(p,j-e), including destinations outside the sender set.
One orientation per unordered source pair gives the separate pair cap.

All template inequality weights are nonnegative integers; the selected-balance
equality weight is free. Dividing by the positive gcd does not change an
inequality. Deleting terms gives valid control potentials. Their maxima are
computed in domains that contain every actual source option under the bridge.
Exactly j sources must be high senders. Every possible j is addressed before
a whole state is excluded. A positive exact gap is required; zero is failure.

The nested catalogue comparison is justified, not presumed: selected_degree
contains every heavy-only weight projection in a tighter full-q domain;
eligible contains all selected_degree vectors with the same domain. The
observed exclusion sets are checked to be nested.

The C++ engine uses signed 64-bit integers and asserts small input and weight
domains. Its asserted bounds keep costs, sums and gaps far below overflow.
For example q,H,rho<=15, p<=18, h<=15, all weights<=1000 and at most 32 tails
of each type give local absolute costs below 3,000,000 and total source sums
below 60,000,000. The sentinel is -2^50 and is never added as a real maximum.
Python's unbounded integers independently verify every recorded gap.

The checker uses Cartesian domain filtering and semantic row costs rather
than the engine's ragged loops and direct potential formula. It uses per-source
dynamic programming rather than sorted high-minus-low differences. It checks
all 64,332 visited thresholds, 72,303 attempted sender counts, 1,564,007 gaps
and 267,696 source-capacity bypasses. It reconstructs the complete old pool
from the original heavy-family and joint-routing streams. Internal redundancy
reduces implementation risk; it is not external independence.

## What failed or remained incomplete

- The heavy-only and selected-degree control catalogues exclude zero cases.
  This does not contradict the pilot's 2 and 3 optimized exclusions: those
  used individually fitted weights beyond this frozen catalogue.
- Restricting the reusable catalogue loses four of the pilot's exclusions:
  N34 states 66, 184, 316 and 13530. Their original separate-transport witnesses
  remain preserved and are checked over 46 sender-count cases. They are counted
  once, as pilot-only exclusions, in the combined frontier.
- The full catalogue leaves 4,588 survivors. Including the four pilot-only
  certificates leaves 4,584: 4,506 N34 cases and 78 N35 m306 cases. A survivor
  means only that these rules did not exclude it, not that it is realizable.
- Mixed transport cuts were deliberately omitted after their zero added
  whole-state benefit in the pilot. This experiment does not test them anew.
- The 11-template compression was selected after replay. It introduces no
  new weights and proves no minimum catalogue size. Claims of ordinary-only
  coverage and multi-template need are restricted to the recorded winning
  thresholds. Alternative later thresholds were not searched after success.
- The cutoff integers were not scaled with h. No claim is made that this
  catalogue is the best choice for larger orders, other cutoffs or T other
  than 4h. No per-state fitting occurred during the full replay.

## Analytic reduction audit

The recurring potential's q dependence is nonincreasing only after fixing
H,p and ensuring rho>=2, so that the destination indicator is constant.
Residual-one sources need their own argument. If they have no eligible label
of demand at most one, their maximum is zero; otherwise q=1 attains
4 min(delta,b-2). Zero-demand labels count as eligible and are not assigned
an unjustified label-degree identity.

For rho>=2, replacing q by H gives a locally feasible option with the same
H,p and sender class; it does not assert a realizable graph after replacement.
The p formula is piecewise affine with integer breakpoints at h-H, 4h-H and
j-e, so the endpoints and interior breakpoints suffice. The reduction retains
the exact-j condition and all source multiplicities. It matches 28,591 recorded
gaps, including failures, and supports the 707 existing applications of that
template. Its parameterized hand proof supplies the general claim.

## Implementation corrections preserved

Initial input preparation used display-style layer identifiers such as
N34_m289; the original evidence uses n34-m289. It stopped with a ValueError
before any engine run. The initial script and failure record are preserved
as `prepare_inputs_initial.py` and `input_preparation_initial_failure.log`.
The corrected identifiers reproduce the exact 5,578 records.

The first C++ compilation reported four misleading-indentation warnings on
multiple statements written on one line. The initial source and warnings are
preserved as `replay_initial.cpp` and `compile_initial.log`. Formatting was
clarified without changing statements or arithmetic; clean reproduction checks
the full original result stream byte for byte. The original runtime in
environment.json belongs to that initial run and is not replaced by a fresh
timing. Future run_replay.py timings use reproduction_environment.json.

## Scope and next gate

The experiment demonstrates transfer of fixed eligible-routing potentials to
975 cases beyond the pilot and exposes a simpler exact local-maximization
rule. The combined compatibility record contains 994 exclusions. These are
alternative structural explanations within already candidate-closed fixed
orders, not 994 new graph theorems. The N34/N35 canonical ledgers, 7/12 threshold
and forecast assessment are unchanged.

The next target is a closed bound on the remaining H maximum, tested honestly
against the combined survivors. The preserved failures define the reach of
the present relaxation; they must not be hidden by later simplification.
