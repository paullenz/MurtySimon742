# Frozen-catalogue full-pool experiment

12 September 2026. Written before the full-pool replay.
Baseline: be45e9c540ece11290e6f07e3a31bd8dcc3da2d0.
Candidate mathematical work; external review and novelty OPEN.

The preceding compatibility pilot excluded 19 of 29 selected cases. Its
selected-degree eligibility gain was 16 cases; mixed cuts added no whole-state
exclusions. This experiment tests a compact catalogue on all 5,578 survivors
of the older general-routing catalogue. These arithmetic cases already have
other exclusions in the canonical N34/N35 candidate ledgers.

## Catalogue rule fixed before replay

Use successful extracted envelopes from the pilot's catalogue_free,
selected_balance and separate_transport modes. Exclude joint_transport.
Divide each vector of integer weights by its positive gcd, order terms
lexicographically, and deduplicate. Rank vectors by sum of absolute weights,
then number of terms, then the ordered vector. Retain the first 20 vectors.
Preserve their original pilot provenance and the full ranked candidate list.

Apply each vector at h=2..max(s), T=4h. Retain its numerical destination
cutoffs as written; do not rescale cutoffs with h. This is valid under the
parameterized lemma, but no scale-invariant optimality is asserted.

Construct three nested comparisons using deletions of terms:

1. heavy_only: delete selected-balance and all transport terms; use the
   earlier H+p load ramp and heavy-only source domains.
2. selected_degree: retain selected balance, delete transport terms, and
   include all heavy_only projections; use full q+p source domains.
3. eligible: include all selected_degree vectors and all 20 original vectors;
   use full source domains and their separate eligibility tails.

Normalize and deduplicate each set. No multiplier fitting, LP solver, new
templates, or outcome-based catalogue enlargement in this experiment.

## Coverage and evidence

Recover the entire pool from the original encoded heavy-family and
joint-routing records, checking their hashes and matching their survivor IDs.
For every state and mode search thresholds in increasing order. At each h,
address all possible heavy-sender counts j: existing source capacity can
exclude some j; otherwise evaluate every vector in that mode. Stop a threshold
at its first j with no positive exact gap; stop a mode at its first threshold
excluding every possible j. Preserve every evaluated gap and the stop point.

Use integer arithmetic throughout. Independently reconstruct source domains
and verify local maxima, exact-j aggregation and coverage. Compare measured
pilot retention and non-pilot exclusions; do not extrapolate the old 19/29 rate.
Keep all survivors and failures. A nonpositive catalogue gap is not a graph
existence certificate. Record runtime/environment and reproduce the complete
result stream from a clean checkout.

Extract the simplest structural explanation supported by the completed run.
Do not change the canonical fixed-order ledgers or 7/12 theorem status. Publish
the full evidence and update the README/reviewer navigation before proposing
another research expansion. Paul handles external review separately.
