# Scope audit and failed attempts

13 September 2026. Same-assistant internal review. External mathematical
review, novelty and independent computational reproduction remain OPEN.

## Graph-to-model obligations

The hand derivation was checked against the canonical bridge: selected
representatives are injective on missing unordered B-pairs; sum p=sum q;
endpoint load uses the same residual label degree at every incident source;
incoming/source capacities give h. The balanced-cover corollary uses only
these implications and nonnegative residual degrees. Its concentration
alternative follows by an integer augmenting-path cut.

The optional residual upper bounds require C=H[A] to have no isolated vertex
and s to be the actual canonical demand, not an arbitrary reduced vector.
The preserved N34/N35 source proof defines s_i=max(0,d_i-R_i); all applied
states satisfy t>0 and b>a-1-t. Zero-demand labels need the additional excess
E=sum s-r-2t. The proof retains that excess rather than assuming R_i<=a-2.
No universal bridge implication receives external endorsement here.

The combined inequality was checked with arbitrary signed residual prices
and incoming multiplier. Only pair weights and endpoint weights must be
nonnegative. Each source maximum ranges over every residual set of the
prescribed size disjoint from its fixed selected set. The shared support
function ranges over a larger box-and-total domain, so it is a safe upper
bound. No independence assumption between actual rows is needed.

## Attribution controls

A preliminary diagnostic found that all 4,584 original stored p vectors
fail total endpoint accounting. Those p vectors were constructed only as
scalar transport witnesses in the predecessor. This is not an error in
that predecessor's stated scope. The new endpoint control therefore allows
p to vary rather than fixing an unsuitable old vector.

The endpoint stage excludes 4,449 frozen selected patterns. All 26 old local
residual-cover failures are in that set, so none is credited as a new pair
effect. Of 135 remaining patterns, 13 fail the stronger residual-placement
control. All other 122 have exact rational control witnesses. Adding pair
constraints rejects 25 and leaves 97 with exact rational joint witnesses.

Among those 25, a separate weighted pair-only LP has 3 exact obstructions
and 22 exact fractional witnesses. The latter 22 also have exact witnesses
for the endpoint-placement control, while their conjunction is excluded.
This validates the claimed interaction between pair geometry and shared
endpoint budgets. It does not establish integer feasibility of either
separate control or a whole scalar-state exclusion.

## Numerical discovery and exact acceptance

SciPy/HiGHS proposes weights and fractional witnesses. All accepted
exclusions are evaluated again with rational or scaled integer arithmetic.
The standard-library verifier independently reconstructs pair deficits,
enumerates all residual choices for local maxima, checks box-budget support
and verifies each strict gap. It also checks every positive rational witness
directly, including row normalization, residual capacities, endpoint loads,
incoming total and pair coverage where relevant.

The first discovery pass stored certificates and solver statuses but did
not retain positive fractional witnesses. That original script and output
remain in `history/`. A subsequent witness-retention pass found that
rounding each floating coordinate to a rational with denominator at most
one million can fail exact row normalization. That pass stopped on an
assertion; no invalid witness was accepted. Its partial output and failure
log are preserved.

An attempted exact reconstruction used an unavailable optional SymPy
dependency and stopped. The final implementation uses standard-library
fraction-free elimination on the proposed active linear system, followed by
direct exact checks of every original constraint. Of the 219 control/joint
witnesses, 159 are recovered by scalar fractions and 60 require this exact
active-system reconstruction. The missing-dependency log is preserved.

The original rational weights can have large denominators. A separate
integer-weight compression verifies all 38 additional certificates with
scales no larger than 10,000; it changes no exclusion count. Original
outputs remain available for audit.

## Coverage and explicit limits

Every one of the 4,584 frozen selected patterns is accounted for exactly
once in the staged study: 4,449 endpoint exclusions, 13 placement-control
exclusions, 25 pair-stage exclusions and 97 joint fractional witnesses.
The 1,871 balanced-cover exclusions are a subset of the endpoint exclusions,
not an additional count. Concentration witnesses are structural alternatives,
not exclusions.

This study does not enumerate alternative selected sets, source selected
degrees q, additional incidences x>s, simultaneous integer residual choices,
the full heavy-H catalogue, exact compatible destinations, Hall routings,
H[A] or D2C graphs. Whole-state exclusions added: **0**. The generalisation
frontier remains 994 exclusions / 4,584 survivors. Fixed-order packages,
theorem ledger, 7/12 threshold and forecasts are unchanged.

The tiny checks include signed prices, signed incoming multipliers and
positive pair deficits on abstract cross data. They challenge the algebra,
not the universal graph-to-constraint bridge. The shared foundations remain
the main correlated correctness risk for external review.
