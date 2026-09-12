# Review and closed compatible-potential continuation

12 September 2026. Prepared before the new cutoff-family experiment.
Baseline: dfcfbc26da5c32b76b83c19de47e08cdc3ea4815.
Candidate mathematics; external review and novelty OPEN.

User instruction: review the most recent work and continue. The preceding
catalogue checkpoint is fully published: 990 catalogue exclusions plus four
retained pilot-only witnesses, leaving 4,584 combined survivors from 5,578.
The recurring potential at cutoff 2 suffices for 707 recorded winning
thresholds and has an exact q elimination and five-p-breakpoint reduction.

## Review scope

Review the latest graph-to-potential implication, local domains, sender-count
aggregation, coefficient selection, exact verification, original-evidence
preservation and survivor accounting. Retain all limitations and correction
history. Do not conflate internal reimplementation with external review.

## Mathematical target

Replace enumeration of heavy degree H by a constant number of explicit
linear/quadratic maxima. Generalize the ordinary eligibility cutoff from 2
to any nonnegative integer k, keeping the weights fixed:

    load=1, heavy demand=1, heavy receiving=2, ordinary cutoff-k tail=4.

The source potential is

    H(h+(4h-max(h,q+p))_+)+H-2eH
    +2 1[rho>=h] min(p,j-e)
    -4q 1[q>k]+4p 1[rho+q>=k], e=1[H>h].

The planned exact reduction has two q branches: q=H, and q=k-rho when that
value exceeds H and is locally feasible. In the first branch, the p endpoints
and breakpoints are affine functions of H, giving linear or concave quadratic
pieces. In the second branch, the potential increases with H inside a fixed
sender class, so one H endpoint suffices before checking the p breakpoints.
Prove all boundary and integer-rounding claims explicitly; preserve failures.

## Bounded experiment fixed in advance

Recover all 5,578 original survivor states. Compare:

1. the fixed cutoff k=2 potential, searching h=2..max(s), T=4h;
2. the same fixed weights with every integer k=0..a+1.

At each h, address every j allowed by the original heavy-source capacity.
For the expanded family, different j values may use different k values;
this is valid case analysis on the actual j, not one simultaneous choice
of k. Preserve all evaluated gaps, capacities and first blocking j. Stop
after the first successful h for a mode. No LP, new fitted coefficients or
outcome-based expansion of the cutoff range.

Compare a closed-form implementation with independent complete integer source
enumeration. Check the formula on an additional declared finite domain of
local parameters to challenge boundaries absent from N34/N35. The hand proof
supplies the general claim; finite checks are corroboration.

Keep every earlier catalogue/pilot exclusion when computing the combined
frontier. Report new exclusions over the preceding combined 994 separately.
An exact reformulation alone cannot strengthen the old cutoff-2 potential;
any new reach must come from the expanded cutoff family. Publish a complete
audited checkpoint with current navigation and a verified receipt.
