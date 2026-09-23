# Exact assigned-witness row screen: n=14, Delta=8

Status: exhaustive at the abstract assigned-witness MILP interface.

The screen enumerated all integer partitions of demand 15 and all deletion-minimal demand-16 partitions, all witness counts x_i compatible with h_i=2x_i-d_i, h_i<=Delta, at most a=n-1-Delta labels, physical-edge capacity, and symmetry among equal demand parts.

- symmetry-reduced patterns tested: 5,334;
- patterns passing the multiplicity-compressed scalar inequality: 878;
- patterns passing the exact aggregated-incidence MILP with D<=12: zero.

The closest abstract pattern has d=(8,7), x=(8,7), h=(8,7). Its exact minimum total degree deficit is 13, one above the strict-counterexample budget Dmax=12.

Therefore the first scalar-survivor row is eliminated at this interface. The result remains conditional on the audited bridge into the exact-H assigned-witness setup and is not a free-standing graph-realizability theorem.

Timing note: the computation's start boundary was not authoritatively captured after the preceding preservation operation, so its elapsed time is not credited to the session's verified research duration.
