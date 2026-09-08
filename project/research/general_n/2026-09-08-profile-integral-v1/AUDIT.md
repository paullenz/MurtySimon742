# Adversarial audit and handoff

8 September 2026. Internal reconstruction and testing by the same assistant that developed the candidate. This is not independent specialist peer review.

## Verdict

The previously unfinished 0.586 route now has a complete written derivation and a fresh exact audit. No blocking defect was found in this pass. The constant remains exactly 293/500; this session does not chase a further improvement. The full statement is still candidate mathematics, with internal computation REPRODUCED and independent review OPEN.

## What was challenged

**Pointwise Cauchy-Schwarz.** The square-root sum uses actual demands at least h, not a substitution of minimum demand for actual selected degree. The proof isolates p=|I_h|/a and the nonnegative gap (1-p)(z_h^2-p*h^2). The step 2W_h<=z_h^2+h^2 uses z_h>=h. A concrete illegal model with a=4, demands [0,0,0,3], h=3 and z_h=0 satisfies the quadratic threshold inequality alone but violates the proposed pointwise bound. This confirms the source floor is a genuine premise.

**Quadrature direction.** A decreasing right-endpoint sum is below its unshifted integral, so simply dropping a correction would be wrong. No such step is retained. The proof instead uses midpoint concavity on [h-1/2,h+1/2] and bounds the lost endpoint integrals by a/4 per demand. The conditions s integer, s>=1 and s<=a-1 explicitly guarantee a real radicand up to s+1/2 and f(s+1/2)>=s. The zero-demand case is treated separately. The exact regression checks 833,250 symmetric midpoint identities with rational offsets; it does not substitute numerical integration for this reasoning.

**Jensen.** Re-differentiation gives Phi''(x)=(3/2-x)/sqrt(x(2-x))>0 for 0<x<=1, with continuity at zero. Equal-weight finite Jensen is therefore applicable. More importantly, it is unnecessary for the stated constant: the scalar bound x-Phi(x)<1/12 is valid pointwise and can be summed directly. A primary Mathlib documentation check confirms the required finite Jensen hypothesis direction, but is not a Lean execution of our function.

**Scalar minorant.** Both sides are nonnegative before squaring sqrt(1-u)>=1-u/2-u^2/2. The square gap factors as u^2(1-u)(u+3)/4. Integrating gives the explicitly displayed degree-seven polynomial P(q). On the two intervals split at q=1/2, exact cubic envelopes leave positive rational margins 4049/2506188 and 7/240 below 1/12. No unverified root location, rounding or floating optimiser is used.

**Small cases and dependency reduction.** The large-a margin is positive at a=31, with positive increasing forward differences. The new surplus estimate alone leaves a=6 and a=11 in the finite degree table. A new 640-case (H0,S) certificate closes both using only the threshold family. This removes reliance on both the old 4/81 cubic and the much larger all-profile enumeration for the theorem's finite assembly. The full profile audit independently agrees with its upper bounds S-r<=2 and S-r<=8.

**Do not infer the new bound from the old cubic.** The integer family a=27k, S=216k^2, r=144k^2, t=36k^2 satisfies the old scalar cubic and S=r+2t, but violates the new profile bound for k>=1. These are abstract scalar tuples, not graphs. The new argument must retain the threshold structure, and does.

**Scope.** K(2,3) remains a counterexample to an overbroad strict n>=4 version. The n=29, Delta=17 consequence is a degree-case exclusion, not a complete n=29 result. The 5,000-order arithmetic loop is likewise not proof of all graphs through n=5,000.

## Evidence and limitations

The deterministic audit exited zero on Python 3.13.5. All finite checks use integers or exact rational arithmetic. Full output, source, count domains and command environment are preserved. The demand-profile digest is `4d31d2ca7ef631caad3554a3fc145684d6ad15f2bea046ebeb23c41fce2a4ad0`.

The new profile audit is abstract: 1,306 tested profiles have positive S-R_lower, but none is claimed graph-realisable. It therefore stresses positive abstract surplus without producing a positive-surplus actual critical graph. No new actual-graph enumeration was run for this checkpoint. The graph-to-threshold premises remain hand arguments with earlier separate computational and local Lean support; those tests are not silently promoted into a full formal proof.

The initial exploratory script `history/explore_exception.py` is preserved with a fresh replay output. It was used to find the smaller certificate. SymPy was used once in scratch exploration to simplify derivatives and inspect the polynomial, but no SymPy output, floating stationary point or numerical approximation is a proof dependency. The final standard-library checker and hand factorisations replace that exploration. No failed checker execution occurred in this session's saved full run. Historical failures and unreferenced weighted-spare-source v10 blobs remain distinct unresolved historical obligations; this checkpoint does not claim to recover them.

## Next priority

Freeze the 293/500 coefficient for review. The most useful next assurance work is a proof-assistant treatment of the newly isolated pointwise/shifted-midpoint/scalar chain or a genuinely independent specialist reconstruction of the graph-to-threshold premises. Do not expand the theorem ledger or announce unrestricted n=29 or general-conjecture resolution on the strength of this checkpoint.
