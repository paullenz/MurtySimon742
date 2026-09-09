# Exact globally minimal nine-shape shared potential on the n=30 hard frontier

9 September 2026. Finite research checkpoint inside the pairwise staircase / monotone-coupling programme. **This is not a universal Murty–Simon theorem.**

## Result

On the seven preserved n=30 equality-frontier hard profiles at `(a,b,dmax,t)=(13,16,11,1)`, one common pairwise staircase potential of the form

\[
\Phi(s,d,h)=F(d,h)+G(s,h)
\]

separates all seven profiles simultaneously.

A mixed-integer support search over the full generated dictionary of **262 BC staircases + 4 SH staircases** found an optimum support cardinality of

\[
\boxed{9=6\text{ BC}+3\text{ SH}}.
\]

The MILP terminated optimal with zero MIP gap (`N30_SHARED_MIN_SUPPORT_RUN_34361230390.json`). Hence no support of at most eight shapes exists inside this complete generated dictionary for the stated shared-envelope model and big-M formulation.

The three selected SH shapes are exactly the unique minimum exceptional-state correction previously isolated:

\[
\{(1,-1),(2,-5),(3,-6)\},
\]
\[
\{(1,-1),(2,-7)\},
\]
\[
\{(1,-1),(2,-2),(3,-11)\}.
\]

The six globally selected BC staircases are recorded in the exact checkpoint `checkpoints/N30_GLOBAL_NINE_EXACT_RUN_34362935743.json`.

## Exactification

The selected support was rebuilt as a continuous shared envelope LP, using one common set of staircase/global coefficients and profile-specific envelope variables. Floating point was used only to propose the point.

All variables were scaled by `10^6` and rounded. Tiny positive residuals in tight homogeneous envelope rows were then repaired deterministically by lowering only the corresponding free `ell`/`sig` envelope variable. The repaired point was checked from scratch with Python integer arithmetic.

Exact checkpoint:

`checkpoints/N30_GLOBAL_NINE_EXACT_RUN_34362935743.json`

Results:

- support: 6 BC + 3 SH;
- variables: 55;
- exact rows checked: 2,775;
- bound violations: 0;
- row violations: 0;
- maximum zero-RHS row after repair: 0;
- repair variables: 14;
- maximum repair: 4 integer units at scale `10^6`;
- profile margins range from `-999957` to `-1000002`.

Thus the shared nine-shape potential is **exact finite evidence**, not merely a floating LP fit.

## Non-uniqueness

A separate minimum-support search restricted to the 31 shapes active in the earlier L1 shared solution also found an exact support minimum of 9 = 6 BC + 3 SH, but with a different six-BC basis. That alternate support also exactified successfully.

Therefore the compact shared mechanism is not tied to one brittle BC basis: multiple distinct six-BC bases can support a common nine-shape potential. The stable feature is the 6+3 architecture and, especially, the same three SH correction shapes.

## Research implication

The finite n=30 problem has now been compressed from a large incidence LP to one exact common potential built from nine monotone staircases. The next theorem-level target is not to reproduce these numerical thresholds verbatim, but to identify parameterised staircase families and analytic envelope bounds that play the same role for arbitrary `(a,b,t)` and improve the current `7/12` maximum-degree candidate.

A cross-order transfer scan against the independently regenerated n=29 Delta=16 hard frontiers is the immediate falsification test for whether the nine-shape dictionary reflects reusable structure rather than n=30 overfitting.
