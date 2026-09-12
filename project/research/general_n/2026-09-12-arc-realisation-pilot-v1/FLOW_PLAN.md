# Fixed-pattern flow follow-up plan

12 September 2026. Written after the first four frozen MILP attempts ended
without an incumbent; the original pilot continues with its unchanged budget.
The pair-compatibility/flow reduction was derived during that run.

Do not extend the MILP budget or replace the sample. For each of the same six
states, construct one selected-incidence pattern by integer flow: label i
supplies exactly s_i incidences, eligible sources satisfy rho_u>=s_i, each
label-source edge has capacity one, and source u has capacity a-rho_u.
Use deterministic ascending-index augmenting paths. A full selected flow
constructs one pattern; it is not an assertion that every realization has
x_i=s_i. If the construction fails, preserve its cut and stop that case.

For that selected pattern choose two residual patterns: at each source, the
first rho_u and last rho_u unused labels, respectively. Do not choose after
seeing routing outcomes. Run the new fixed-neighbourhood flow test on all
twelve resulting patterns, preserving assignments or exact deficient Hall
sets. Also test any verified cross patterns returned by the original pilot.

These are constructed probes, not representatives of all possible cross
patterns, and need not satisfy the earlier local endpoint-load constraints.
Record those constraints separately. A failed fixed-pattern test proves only
that pattern cannot be rerouted. No whole-state exclusion follows. Report
empty eligibility sets explicitly rather than presenting trivial failures
as evidence of a difficult collective obstruction.

Check the conditional criterion independently on all three-state cross
incidence matrices for a=2,b=3 (absent, selected, residual at each of six
positions): 729 patterns. Exhaustively assign every selected obligation to
one of its other two B-vertices, checking B-side conditions directly; compare
with the flow algorithm. Supplement this with direct exhaustive checks of
all labelled oriented graphs on b=3,a=3, all compatible residual placements,
and feasible demand vectors. Preserve exact counts and any failures.
