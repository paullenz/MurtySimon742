# Internal audit, corrections and limitations

12 September 2026. Same-assistant adversarial review and independently
structured arithmetic replay. No blocking flaw found in the stated candidate
lemma or accepted applications. External mathematical review, novelty and
external reproduction remain OPEN.

## Challenges to the proof

1. **Does H mean all selected degree?** No: H counts only heavy incidences.
   The proof uses H<=q, the decreasing ramp, and the necessary cap H+p<=b-1.
   Replacing q by H enlarges the local cost; it never asserts their equality.
2. **Are sources with no heavy arcs omitted from receiving capacity?** No.
   Every source in Z is retained, including H=0. Such a source can receive j
   arcs from J, not j-1. The latter incorrect extension has an explicit small
   counterexample in `routing_verification.json`.
3. **Can both orientations consume the same internal pair?** No. K_j counts
   each unordered internal pair once. The per-destination caps alone would
   not enforce this; the separate K_j constraint and specified-j capacity
   screen are retained. An invalid two-orientation example is recorded.
4. **Are the correction signs right?** D<=incoming and D<=K_j give
   lambda(incoming-D)+mu(K_j-D)>=0. W<=sum H gives
   eta(sum H-W)>=0. Adding these quantities produces an upper bound on the
   source sum. All three multipliers must be nonnegative.
5. **Can a different j be chosen for each source?** No. One actual j is fixed
   globally. Exactly j sources have H>h. Discovery sorts the j largest local
   differences; verification uses a separate cardinality dynamic program.
6. **Does ruling out one j suffice?** No. Each positive state witness covers
   every j=0,...,number of capacities above h. Some j values fail the existing
   source-capacity condition; every remaining one has a strict integer gap.
7. **Do zero demands require a deficit convention?** Not here. The lemma only
   uses heavy labels with s>=h>=1, total residual budget r and x>=s. It does
   not set d=R at zero-demand labels or assume every demand is positive.
8. **Do local maxima assert graph realizability?** No. They are upper bounds
   in a relaxation. Independent local choices and even the combined caps need
   not correspond to an actual routing or graph.
9. **Is the new inequality a finite-order observation?** The hand proof has
   arbitrary a,b,h,T and nonnegative rational multipliers. The measured 729
   exclusions use finite certificates and a fixed template catalogue. The
   latter count does not prove a new all-order density theorem.

The independent checker verified 2,645,388 cached local options and 1,234,969
integer envelopes, including every positive witness and every recorded
blocking case for all 20 templates. Its 915 complete state witnesses count
both ablation variants and the pilot, not 915 distinct states. Combinatorial
routing is also exhaustively checked on all partial orientations of up to
five vertices and every subset J. These finite checks corroborate the hand
proof; they do not replace its general implication.

## Correction to the comparison pool

The previous recommendation identified 6,499 historically envelope-certified
states surviving the heavy-load search. This was not yet the union of all
hand-rule survivors. In the original N34 run, the source-capacity rule ran
only after both fixed envelope attempts failed. Consequently, 192 states
already excluded by that hand rule had historical fixed-envelope labels:
83 fixed9 and 109 fixed13.

Reapplying all existing hand rules removes those states, leaving 6,307.
Every removed ID and arithmetic reason is preserved in `pilot_inputs.json`.
The 729 new exclusions are measured against this corrected pool. The 192
rediscovered old-rule exclusions are not credited to the new lemma. This is
a correction to the comparison pool, not to the canonical fixed-order proof
counts or the earlier heavy-load results.

The first sample-selection recipe included all zero-demand survivors and
produced 396 cases. Before any solver run, it was narrowed to three evenly
spaced zero-demand cases, giving 27 in total. `selection_initial.log` preserves
the initial recipe and count; `selection.log`, the final code and full inputs
preserve the completed bounded pilot. No 396-case solver experiment occurred.

## Negative results and scope of the ablations

In the pilot, the local and pair-only variants excluded zero of 27 cases;
the aggregate variant excluded eight, and the joint variant twelve. Fifteen
survive all tested variants. All attempted thresholds, first blocking j
values, solver statuses, objectives and exact multiplier proposals remain
in the original pilot stream. Numerical solver failure would never count as
an exclusion; this run's exclusions are decided by strict integer gaps.

The pilot searched T=4h and 0<=lambda,mu,eta<=16h, with denominator repair
choices 1,2,10,100,1000. It stops a threshold when one possible j cannot be
excluded; it stops a variant after a complete state witness is found. No
optimality over all multipliers, cutoffs or routing models is claimed.

Twenty distinct ratios (lambda/h,mu/h,eta/h) were frozen from successful
pilot certificates, then applied without a solver to all 6,307 cases.
The full-domain aggregate comparison uses the *same* catalogue and permits
its pair multiplier mu; it changes only min(p,j-e) back to p. It is therefore
stronger in this respect than the pilot's aggregate variant, which fixes
mu=0. Counts from those two experiments should not be conflated.

The frozen catalogue yields 166 exclusions with both variants, 563 with the
joint variant alone, and 5,578 surviving both. A surviving case has no
witness in this catalogue. It is not a feasible routing, a graph, or a
counterexample to Murty–Simon. The canonical N34/N35 envelopes already exclude
these states and remain the recorded fixed-order proof chain.

The next structural question is whether the successful destination cap can
be expressed using demand and residual tails without retaining all j cases
and local options. Actual arc allocation, stronger q-dependent supplement
eligibility and cross-threshold compatibility remain omitted information.
No improvement to the 7/12 theorem or the unrestricted conjecture is claimed.
