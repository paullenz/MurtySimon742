# Source-union MILP diagnostic

24 September 2026. The graph-level source-union lemma was inserted into the existing demand-15/16 aggregated witness model. For every right-incidence type J, variables at endpoint deficit z are forbidden below

    g(J)=max(0,rho+|J|-min_{i in J} h_i).

This is exactly the profile-only consequence of the proved source-union charge. It is a necessary condition only.

## Audited n=18 profiles

The strengthened model was compared with the immediately preceding witness-deficit model on five audited profiles at n=18, Delta=10, rho=2:

- d=x=(8,7), h=(8,7): 17 before and after;
- d=(8,7), x=(8,8), h=(8,9): 16 before and after;
- d=x=(8,6,1): 17 before and after;
- d=x=(8,5,2): 18 before and after;
- d=x=(5,5,5): 16 before and after.

The floor is positive on some right types of the low-h three-label profiles, but their optima already pay at least that endpoint deficit. It is zero on every right type of the dense (8,7) and (5,5,5) leading cases. Thus this new graph-derived charge does not by itself close the known abstract survivors. This negative result is load-bearing: source-union geometry must be combined with source capacity or more exact neighbourhood overlap, not presented as a realizability solution.

## Bounded row checks

Using the same strengthened model:

- n=14, Delta=8: all 150 scalar-pass candidates completed; zero survivors; closest deficit 17 versus allowance 12.
- n=15, Delta=8: zero scalar-pass candidates.
- n=16, Delta=9, stable scalar range 201--400: 200 candidates completed; zero survivors; closest deficit 20 versus allowance 14.

An earlier n=16 prefix attempt printed progress through scalar 200 but ended without a FINAL record. It is deliberately not used for a prefix-closure claim.

The bounded checks validate the implementation and preserve a failed theorem-facing route. They do not enlarge the general finite edge theorem beyond the separately reproduced S<=14 result.
