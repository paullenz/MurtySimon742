# Audit, negative results and scope

12 September 2026. Same-assistant adversarial mathematical review plus separately
structured exact replay. No blocking flaw found in the stated candidate lemmas
or accepted arithmetic. External mathematical review, novelty assessment and
external computational reproduction remain OPEN.

## Proof challenges

- **Positive surplus is essential to the budget baseline.** It supplies
  rho>=1 at every source. The identity r=b+sum_{l>=2}z_l cannot be used with
  inactive sources. The projected theorem explicitly assumes t>0. The separate
  equality-rigidity lemma only assumes the bridge and its stated incoming cap.
- **Lower tails must already be proved.** The application independently
  reconstructs ordinary capacity and the preceding heavy-load lower bounds,
  then closes them monotonically. It performs one pass from that input. It
  does not assume its own conclusions while proving them.
- **The cost of raising z_h is not uniform across lower levels.** Only levels
  with L_l<z must rise. The correct cost is the sum of positive parts beta_h.
  An explicit integer counterexample to charging (h-1)(z-L_h) is preserved.
- **One vertex already contributes to higher tails.** Bounding its residual
  degree requires subtracting (L_l-1)_+, not L_l. A counterexample to the
  overstrong subtraction is preserved in the budget check.
- **Restoring the residual penalty requires kappa>=0.** The actual sum of
  excess residual degrees is at most E_h(z). Multiplying this upper bound by
  a negative coefficient would reverse the relevant comparison. All four
  coefficients are checked as nonnegative integers after common scaling.
- **Both counts z and j are global.** Every candidate z below a proved new
  minimum is covered, and every possible j at an excluded z is covered. An
  isolated successful local inequality does not exclude a tail or profile.
- **Local class maxima may be negative.** This is harmless after subtracting
  the residual penalty. They are restored using the correct total budget.
  Only classes with nonzero populations contribute to the sum.
- **Zeros among label demands are allowed.** The argument uses x>=s on heavy
  labels and r<=S-2t; it never assumes a zero label has d=R or all labels have
  positive demand.
- **Equality rigidity needs p<=3h.** The local maximum classification is
  H=h, or H=2h with p=0. Allowing p>3h breaks the bound; a concrete local
  counterexample is recorded. At equality, every source must attain its
  maximum because all intervening deficits are nonnegative.
- **Local maximality and full equality are different hypotheses.** The
  local maximum classification permits j=0, but nontrivial full equality
  does not: G<=4W<=4h(z+j), combined with G=r+4hz and r>0, forces j>=1.
  The first draft overstated the j=0 branch as essential. This explanation
  was corrected before publication; the closed upper bound and all computed
  exclusions were already valid and remain unchanged.
- **Indegree zero is a structural restriction.** Equality makes every
  2h-sender have p=0. Its heavy arcs must therefore end among the other z-j
  sources, each with capacity at most P, and use distinct unordered pairs.
  This proves both z-j>=2h and 2hj<=P(z-j).

The new exact verifier uses tail-slack identities and indicator sums instead
of the discovery implementation's budget calculation and ramp. It checks
3,834,361 cached local options and 790,922 integer envelopes, including all
recorded blocking cases for the full catalogue. The separate scalar verifier
enumerates admissible j instead of using the closed Jmax formula. A third
checker exhausts small positive residual tuples and local equality cases.
These finite checks corroborate the hand proofs; they do not establish their
unbounded parameter scope by extrapolation.

### Preserved correction to the draft audit

The initial audit said: “The j=0 case cannot be discarded.” Its local example
H=(h,h), p=(0,0) shows only that local maximality does not force high senders.
It does not meet the global equality hypotheses and is not a counterexample
to a graph-level elimination of j=0. The global argument now explicitly gives
j>=ceil(r/(4h)) at nontrivial equality. The uniform Jmax formula remains a
valid upper bound, so no theorem statement, witness or count changed.

`check_budget_initial.py`, `budget_verification_initial.json` and
`budget_verification_initial.log` preserve the exact earlier checker and report.
Their third counterexample's interpretation is superseded by this correction;
they are historical evidence and are not the active replay command.

## What was tried and what failed

The 27-profile pilot was selected from the preceding routing pilot, retaining
the same demand/layer instances. Its projected variant with kappa=0 excludes
six; allowing the residual-budget penalty excludes nine. All numerical
proposals, statuses, objectives, variable vectors and rounding attempts are
preserved. Strict integer gaps, not solver statuses, decide acceptance.
The pilot searches T=4h, coefficients 0..16h, and rounding denominators
1,2,10,100,1000. It stops a threshold when one possible j blocks an exclusion.

Forty-four multiplier ratios were frozen before the full replay: successful
pilot ratios, their kappa=0 versions, and the preceding twenty routing ratios.
The full scan uses no numerical solver. Among 1,453 layer/profile instances,
45 already fail the preceding demand-only bounds. The projected family adds
114 profile exclusions: 112 at one threshold and two by combining new tails.
The same catalogue without a residual penalty adds 106; replacing the
sharper destination term by aggregate p adds 62. Thus the finite comparisons
attribute eight additional profile exclusions to the penalty and 52 to the
destination term. These are bounded-catalogue comparisons, not claims about
all possible coefficients.

The 114 new whole-profile exclusions have unallocated budget D=0 in 91 cases
and D=1 in 23. This shows where the present projection is effective; it does
not prove that larger-budget profiles can never benefit. Another 109 profiles
have increased minimum residual cost without being excluded at one threshold;
two of those fail after the increases are combined, while 107 survive.

**No additional state among the preceding 5,578 joint-routing survivors is
excluded.** This was checked against the complete preserved state list, both
for the full projection and the closed equality-rigidity rule. The results
compress existing exclusions into demand-level statements; they do not shrink
the remaining fixed-order frontier. The earlier canonical N34/N35 proof
ledgers and the 729-state joint-routing study are unchanged.

The scalar follow-up separates the ordinary load cap from the new strictness
rule. Relative to the preceding 45 profile exclusions, the ordinary cap adds
31 profiles; the strict version adds 40. Nine are additional because equality
is now ruled out, and six other surviving profiles receive a higher residual
lower bound. All 40 scalar exclusions are among the full projection's 114.
They must not be added to 114 as separate progress.

## Preservation and next decision

Original pilot, profile, scalar and state-comparison streams are stored
losslessly with both original and encoded hashes. Every profile and every
surviving state remains recoverable. The strictness corollary was derived
after the first full projection scan; its separate code, inputs, outputs and
verification keep that provenance visible. No result is described as a graph
construction or as externally reviewed.

The immediate next research target should retain stronger supplement
eligibility, notably rho_destination+q_destination>=q_origin-1, or actual
label/supplement compatibility. The zero additional-state result argues
against merely enlarging this scalar catalogue. No new all-order density
threshold, improvement to 7/12, or unrestricted conjecture proof is claimed.
