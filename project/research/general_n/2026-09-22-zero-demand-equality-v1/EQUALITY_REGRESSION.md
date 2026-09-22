# Equality and Boolean-orientation graph regression
22 September 2026. Finite internal regression, not an all-order enumeration or independent external review.

Run: `python check_equality_boundary.py` from this package (Python standard library).
Inputs and imported reconstruction helpers are in the sibling raw-profile-bridge package.

PASS on 1,396 graph fixtures, including all prior labelled n<=6 D2C fixtures, X_3/X_4/X_5, 600 seeded greedy D2C fixtures of orders 7–26, and balanced controls at every order 3–41. Fixture counts include repeated or isomorphic graphs; they are not counts of isomorphism classes.

- 2,783 maximum-degree root cases.
- All legal assignments exhausted at 2,727 roots; 56 roots were sampled (up to 32 assignments).
- 68,741 selection assignments checked.
- 647,582 exact degree-identity checks and 523,327 robust selected-arc checks.
- 922 exact Boolean arcs at zero residual.
- 384 selection/root occurrences with nonempty zero-residual orientation; these all have 2b-n>=2.
- 863 zero-demand equality occurrences: 588 even and 275 odd.
- Separate BFS verifies 39,846 edge-deletion checks.
- A five-vertex six-edge near-equality impostor is correctly rejected because edge (0,3) is deletable. Thus the proof's root-criticality hypothesis is non-vacuous and necessary.
- Final source SHA256: 565b392d707d87c1effd0e0db066caeb8ca8721156fb31f2683e4ff1d2af18f4.
- Measured checker duration: 50.912727069007815 seconds.

The extra robust identities checked on every selected ui->w are:
L_u minus {i} subset M_w; L_w subset M_u; M_w minus M_u subset residual-labels(w);
M_u minus M_w subset {i} union residual-labels(u);
deg_G(u)=a+1+indegree(u)-rho_u.

The machine ledger preserves the root, selection-space size, tested assignments and distinct (S,r,f,t,Q,lambda) profiles for every fixture. It does not upgrade sampled roots to exhaustive coverage.

The low-residual diagnostic found r=0,f=0 controls, r=2,f=1 examples, and no r=1 examples. This is a search observation only. Follow-on analysis will prove or refute the r<=2 obstruction from raw criticality; the absence of a finite fixture is not a proof.
