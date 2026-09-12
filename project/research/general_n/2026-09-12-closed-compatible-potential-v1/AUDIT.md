# Review of the latest work and audit of the closed continuation

12 September 2026. Same-assistant mathematical review and separately structured
implementations. External mathematical review, novelty and reproduction OPEN.

## Preceding checkpoint reviewed

The review baseline is dfcfbc26da5c32b76b83c19de47e08cdc3ea4815. The complete
catalogue publication and receipt were verified before starting this work:
55 research changed paths, 559 current-manifest artifact checks, 16 recovered
original streams and 293 committed links. The present prior-manifest check
records the baseline before navigation is updated again.

The reviewed mathematical chain is: canonical source domains; heavy-label
load inequality; strict source cutoff q>k and weak destination cutoff
rho+q>=k; receiving cap min(p,j-e); nonnegative inequality weights; exact
sender-count aggregation; coverage of every possible j; and strict integer
gap acceptance. The 20 seed vectors were frozen before the old full replay,
whereas the 11-vector compression was explicitly selected afterwards.

The old failed control modes, lost pilot cases, original input-preparation
failure, compiler warnings, timings and complete survivor flags remain
preserved. No old proof, certificate, source stream or governed ledger is
modified in this continuation. The earlier analytic reduction was reviewed
including its residual-one exception and its integer p breakpoints.

All 28,591 recorded gaps for the recurring old potential were recomputed using
the new closed formula, including failed gaps and sender counts not reached
by the new search's different stop points. All agree. The old 707 statement
was restricted to recorded winning thresholds. The newly observed 708th
cutoff-2 case is N35 m307 state 18 at a later threshold; this is not a prior
error or a new state exclusion.

No blocking flaw was found in the preceding stated claims or accounting.
That verdict is an internal review, not external mathematical acceptance.

## Closed-form proof audit

- Fixing H,p makes the potential nonincreasing in q on either side of the
  destination-indicator jump. The jump itself must be retained. Its q=D branch
  is present only when all source constraints permit D=k-rho.
- q=H is feasible without light labels. The second branch explicitly retains
  H>=D-v and H<=D, as well as D+rho<=a and p<=b-1-D. Ignoring those restrictions
  would no longer give the stated exact maximum.
- The heavy-sender class is fixed before setting J=j-e. An empty class, or
  the high class with j=0, is omitted. No negative receiving capacity is used.
- The upper p endpoint is split into p=R and p=B-H. Along all six p branches,
  feasibility is an integer interval in H. Source and destination indicators
  are split at k+1 and D; ramp and receiving breakpoints are also explicit.
- On each interval the quadratic coefficient is exactly 0 or -1. Mathematical
  floor and clipping give the integer maximum even at an interval boundary.
  The proof does not discard interior quadratic maxima.
- In the q=D branch, rho>=1 gives D<k and removes the source penalty. Its H
  coefficient is at least h-1>0, justifying the largest feasible H. At most
  five p values then suffice.
- The 59-value bound counts at most 27 quadratic/linear pieces with two
  candidates each, plus five second-branch candidates. It is a conservative
  bound per local sender class, not a bound on total graph verification work.
- Local maxima need not coexist in a graph. Exactly j sources are high and
  every possible j is covered. Choosing different k in different j cases is
  legitimate case analysis, not a claim that one k must work for every j.

## Independent checks and their limits

The closed implementation uses unbounded Python integers. The reference C++
program imports none of it: it enumerates the full Cartesian source domain,
evaluates the ramp as a sum of indicators, and aggregates by cardinality
dynamic programming. Their 6,846,352-byte original result streams agree
exactly, covering 42,193 thresholds, 52,491 attempted sender counts,
476,427 integer gaps and 179,823 capacity bypasses. The C++ parameter assertions
restrict its finite replay to a=15, b=18 or 19; its small costs are safely
within signed 64-bit range. The general formula itself uses Python integers.

The local challenge exhausts its declared small grid and adds 512 deterministic
larger cases. All 39,902 cases agree with complete enumeration. The largest
observed candidate count is 18 there and 22 in the full replay; the proved
upper bound is 59. Finite success corroborates the proof and is not extrapolated
into an unbounded theorem. No solver feasibility status is used anywhere.

## Invalid shortcuts and negative result

Two concrete failures are preserved in shortcut_counterexamples.json:

1. With (a,b,h,k,j,rho,u,v)=(15,18,4,2,5,1,0,1), the low-class maximum is 12,
   attained by q=1, H=0, p=3. Forcing q=H gives zero and underestimates the
   local maximum. The eligibility-jump branch is essential.
2. With (15,18,4,2,5,4,10,2), the high-class H interval is 5..10. Its endpoint
   maximum is 54, while the true maximum is 56 at an interior H. A quadratic
   vertex cannot be discarded.

These are counterexamples to shortcuts in abstract local optimization, not
assertions that the parameters occur in a diameter-two critical graph.
No blocking implementation failure arose during this continuation.

The expanded cutoff family excludes 832 cases, versus 708 for cutoff 2 alone.
It adds **zero** exclusions beyond the preceding combined 994. All four
pilot-only cases remain outside this new family and are still retained in the
combined record. The explicit new-exclusion list is empty; the 4,584 combined
survivors are fully preserved. The formula is an exact reformulation, so it
cannot by itself strengthen its fixed-cutoff inequality.

## Next gate and scope

The new general result is an exact constant-size local formula with explicit
hypotheses and case distinctions. Its finite applications give simpler
explanations of already excluded arithmetic cases. No stronger 7/12 threshold,
new fixed-order theorem, actual graph construction or unrestricted proof is
claimed. The latest outcome forecasts are not changed by this simplification.

The next bounded experiment should add actual arc-allocation constraints to
a small survivor sample, testing whether locally permitted capacities can
coexist. That is a research decision motivated by the measured zero frontier
gain, not a claim that every survivor fails for that reason. Paul continues
external review separately; no external review request was sent here.
