# Residual-one asymptotic boundary wedge — superseded same-session calculation

Date: 2026-09-21

Status: **SUPERSEDED / DO NOT USE AS LIVE GEOMETRY.** This file records a same-session analytic branch that was derived before the stronger repeated-code reverse-exclusion was noticed. The algebra below was based on treating X-reverse boundary certificates as potentially realizable for an outside one-code block with `y>=2`. That physical premise is false: source `q_i^{d_i}` and every X witness share the entire same-code block `Y_d`, so the required singleton common-neighbour condition cannot hold when `|Y_d|>=2`.

The live replacement is `RESIDUAL_ONE_BOUNDARY_POPULATION_OBSTRUCTION.md` together with `ONE_CODE_FULL_BOUNDARY_EXPOSURE_THEOREM.md`.

## Historical calculation preserved for audit

Before the reverse-arm correction, normalize

`alpha=u/p`, `beta=y/p`, `gamma=c/p`.

The then-used residual-gamma/U tradeoff led to the provisional score floor

`Phi(alpha)=1-alpha+alpha^2` for `alpha<=1/2`,

`Phi(alpha)=3/4` for `alpha>=1/2`,

and combining it with the score ceiling gave the provisional wedge

`Phi(alpha)+2beta^2 <= (1+alpha)^2/2`.

This implied, in that obsolete model,

`alpha>=2-sqrt(3)`

for the small-U branch.

The arithmetic is retained because it may be useful if an analogous reverse-capable **singleton** outside-code branch arises. It is not a valid live description of repeated one-code geometry.

## Stronger corrected statement

For a residual-one one-code branch with `p>=4` and `y>=2`, raw boundary criticality instead gives

- full boundary exposure `I=[p]`;
- no X-reverse mechanism at any coordinate;
- escape U-forward reservoir `e=c-1`;
- at most two matched-forward heads globally.

Hence

> **`c>=p-1`.**

If the residual K class is nonempty, then the residual coordinate is nonuniversal, `C=empty`, matched-forward support vanishes, and the stronger bound is

> **`c>=p+1`.**

These exact physical inequalities supersede the normalized wedge above. The corrected intermediate half-ray violates them outright and is unrealizable for all its stated parameters.

## Preservation reason

This file is intentionally not deleted. It records a plausible but physically incomplete intermediate optimization and the exact reason it was superseded. Future audits should not revive the reverse-capacity interpretation for `y>=2`.
