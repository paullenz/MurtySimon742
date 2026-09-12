# Audit, unsuccessful approaches and exact scope

12 September 2026. Internal review by the same assistant. External mathematical
review, novelty and independent reproduction remain OPEN.

## General implication review

The pair criterion requires both S_u minus N_v={i} and S_v contained in N_u.
The first condition records the one exception and the other selected labels
at u. The second records the labels selected at the destination whose own
exceptions cannot be u. Dropping the subset condition could permit both
orientations: S_0=N_0={0}, S_1=N_1={1} has singleton differences both ways,
but neither direction dominates the incoming source's selected label.

For fixed cross sets, different labels at u cannot share a destination,
and opposite arcs cannot both be eligible. These facts are proved before
using a flow model; ordinary bipartite flow without them would omit pair
conflicts. A successful flow therefore respects one representative per
missing unordered pair automatically. The receiving capacity alone suffices
because q+p<=b-1 then follows from pair injectivity.

The Hall certificate recomputes the complete eligible-neighbour union of its
obligation subset, not just destinations used by one attempted assignment.
It therefore excludes every rerouting of the fixed cross pattern. It does
not quantify over other cross patterns. The Q+1 edge capacity ensures that
a residual minimum cut supplies the claimed Hall set, even when Q=0 is
handled separately by the empty routing.

The label-compatibility conditions imply endpoint load and all heavy
destination thresholds. Source eligibility and label demand assumptions
remain explicit. No conclusion about H[A], its degree ledger or full graph
criticality is inferred from B-side sufficiency.

## Frozen pilot: all twelve attempts unresolved

The first/middle/last rule was applied to the preceding 4,584 survivors before
any new solver work. Six inputs and two modes were frozen, with 20 seconds
per solver call and a separate 45-second wall guard. All twelve calls ended
with solver status 1 and no primal vector. Total original solver time was
243.7047776969921 seconds; subprocess wall time was 249.0517963139937 seconds.
No guard fired, no retry or sample replacement occurred, and no infeasibility
certificate or candidate witness was returned. Every case remains OPEN.

The original logs include HiGHS version, presolve and termination output.
The exact twelve input models are stored losslessly; their 109,035 rows and
46,744 variables are regenerated exactly by the archive checker. No claim
that a deterministic time-limited run must reproduce its timing, node count
or status on another machine is made.

## Post-pilot fixed-pattern probes: deliberately limited value

The [follow-up plan](FLOW_PLAN.md) was saved after the first four time-limited
attempts, while the unchanged pilot continued. It constructs one selected
incidence pattern per case, then two prescribed residual placements. Exactly
s_i selected incidences per label are used only for constructing these probes;
this is not imposed as a universal property of actual graph representatives.

All twelve constructed cross patterns have an exact deficient Hall set. In
every case the flow deficit equals the number of obligations with no eligible
destination: there is no additional collective-capacity obstruction beyond
those empty sets. Across the twelve patterns only nine obligations have a
nonempty eligibility set, and all nine can be routed.

Further audit checks show that **all twelve probes already violate some
minimum endpoint-load inequalities R_i+x_i>=q_u**, before incoming degrees
are added. Those violations are listed separately in verification.json.
Consequently these probes do not demonstrate extra strength over the earlier
load framework. They are reproducible tests of fixed-pattern checking and
expose the inadequacy of the deterministic construction as a search seed.
No exclusion is added to the 4,584-state frontier.

## Meaningful controls and exhaustive challenges

- The flow criterion agrees with direct exhaustive assignment checking on
  all 729 three-state cross matrices for a=2,b=3: 4,096 assignments are tested,
  with 154 routable patterns and 575 independently checked Hall obstructions.
- Every one of 343 labelled oriented graphs for a=b=3 is considered. After
  distinct-source-label filtering and all compatible residual placements,
  5,024 cross patterns check pair compatibility, receiver conflicts, coarse
  degree eligibility and endpoint load. There are 10,292 admissible demand
  vectors and 5,304 heavy threshold checks.
- The sparse integer row encoding agrees with direct combinatorial checking
  on 8,192 tiny model/assignment combinations. A positive-demand control
  actually triggers H>h heavy forcing and passes both models.
- The [preserved counterexample](shortcut_counterexample.json) changes one
  residual incidence in that control. It passes the degree-routing model
  but an exception label is present at its destination. This refutes the
  sufficiency of coarse constraints for that particular assignment; it is
  not a whole-profile nonrealizability proof.

These finite controls are abstract structures, not positive-surplus D2C
graphs. They test the stated reductions and implementations, not existence
of graph examples under the conjecture's counterexample hypotheses.

## Research decision

The bounded direct MILP formulation supplied no usable frontier evidence.
The general flow reduction separates a tractable routing check from the
hard search over cross-neighbourhoods. The next experiment should construct
cross sets that already satisfy minimum endpoint loads and provide at least
one compatible exception for every selected incidence, then apply checked
Hall cuts. Only a fully quantified/certified search over cross patterns could
exclude a whole state. This direction is motivated, not yet successful.

No fixed-order ledger, 7/12 threshold, forecast or unrestricted theorem claim
is changed. Earlier material is preserved, with current navigation and its
dependent manifest hashes refreshed.

## Publication check

The unfiltered Git whitespace check flagged one trailing-space table header
in each of the twelve original HiGHS logs. Those historical bytes and their
hashes are preserved. The exact warnings and twelve path-specific exemptions
are recorded in publication_whitespace_check.json; every other staged path
passes the whitespace check. No solver output was reformatted.
