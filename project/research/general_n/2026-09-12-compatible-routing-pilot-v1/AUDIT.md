# Audit, challenges and negative results

12 September 2026. Same-assistant mathematical audit plus independently
structured code. External review, novelty and external reproduction OPEN.

## Graph-to-model implications

- H counts actual selected incidences to heavy labels. q counts all selected
  incidences; replacing one by the other is not an identity. The baseline
  weakens the decreasing ramp from q+p to H+p, while later modes retain q+p.
- A selected label must have s<=rho. Distinct selected labels give both
  H<=number of eligible heavy labels and q-H<=number of eligible light labels.
  A zero-demand label is eligible as a light label. No d=R convention for
  zero-demand labels is used.
- Every selected unordered source pair has one orientation. Therefore sum q
  equals sum p, and every heavy destination receives at most j-e forced arcs.
  Subtracting one at a destination outside the high-sender set is invalid.
- Destination score is rho+q. A source of selected degree q needs destination
  score at least q-1, not q. The strict source cutoff q>k in the transport
  tails corresponds exactly to the weak destination cutoff rho+q>=k.
- Forced heavy traffic F=H 1[H>h] and the other traffic O=q-F are disjoint.
  At destinations reached by ordinary traffic, their combined capacity is p.
  Only the remaining destinations have the smaller forced-traffic cap m.
  This proves the mixed cut without double-counting the shared capacity.
- High-sender count j is one global integer. Every j allowed by source
  capacity is addressed in a whole-state witness. The residual total r in
  the load bound includes all sources, including those below h.
- All variables count source types within a fixed rho group. Their upper
  bound is that group's size. These are valid bounds for exact rounding
  repair and are redundant with nonnegativity and the source-count equation.
- Farkas inequality multipliers are nonnegative; equality multipliers are
  free. Exact repair adds the needed count-bound rows and charges their
  actual right sides. Acceptance needs nonnegative coefficients in every
  column and a strictly negative integer right side.
- Removing normalization and count-bound rows requires replacing their
  effects by actual local maxima and exactly j high sources. The resulting
  envelope uses no LP normalization or count-bound assumption. The baseline
  envelopes retain their explicitly weaker H+p domain; later ones use q+p.

## Verification boundaries

The independent checker imports no discovery model or solver. It enumerates
source domains by Cartesian filtering, evaluates rows by semantic names and
implements the ramp as an indicator sum. All 648 complete model hashes agree
with the recorded discovery models. All 321 certificates and full positive
witness coverage pass. A separate envelope checker uses dynamic programming
instead of sorting high-class differences. These reduce implementation risk;
they do not provide external independence or validate the bridge by themselves.

The sampling verifier independently decodes the original heavy-family and
joint-routing evidence, checks their hashes, reconstructs all 5,578 IDs and
recreates the 29-record selection. The coloured-routing check corroborates
the general mixed cut on its stated finite domain. The hand proof supplies
the unbounded implication; no finite-check extrapolation is used.

The compact example was extracted after the solver pilot. Its weights
(load, demand, receiving, ordinary k=2 tail)=(1,1,2,4) were suggested by a
successful certificate. Direct maximization confirms them for both j=5,6;
the published hand proof uses slightly weaker uniform low-source bounds,
giving gaps 23 and 31. This is a new simplification with explicit provenance,
not the original discovery certificate or an actual graph realization.

## What did not work

The catalogue-free mode excludes only 2/29, selected balance 3/29, separate
eligibility 19/29, and mixed eligibility 19/29. Ten states remain without
whole-state witnesses in all tested variants. Every failed threshold's first
blocking j and its solver status are preserved. No timeout occurred in the
648 attempts; 321 dual proposals succeeded and 327 dual proposal problems
were reported infeasible. The latter are not exact primal feasibility
certificates and do not establish a realizable graph or routing.

All successful proposals were repaired to strict integer certificates. Six
of the 321 extracted envelopes have zero load weight; those contradict the
source/transport data independently of the load bound. Intermediate successes
at thresholds blocked by another j are not credited as whole-state exclusions.

The h=1 threshold, T other than 4h, label residual/degree compatibility,
actual arc allocation and additional cross-threshold consistency were not
searched. No optimality claim about unsearched variants is made.

The new mixed cuts are valid, but add zero whole-state exclusions beyond the
separate tails in this sample. Their more detailed mathematics is not credited
as extra frontier progress. The known all-arc eligibility inequality itself
is not claimed novel; it was present in earlier RX-Hall work.

## Verdict and next gate

No blocking flaw was found in the stated candidate inequalities, compact
example or exact pilot applications. This is a bounded success for retaining
selected-degree destination eligibility. It supports a frozen-catalogue replay
over the full prior pool, not extrapolation from 19/29 to an expected total.
Canonical fixed-order counts, the 7/12 theorem and all external-review labels
are unchanged. Paul is handling external review; no external message or
review request was sent in this work session.
