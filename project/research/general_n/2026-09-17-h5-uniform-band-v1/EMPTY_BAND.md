# The uniform demand-four h=5 band is empty after common-margin coupling

17 September 2026. Research directed by Paul Lenz; derivation and enumeration by ChatGPT/Geeps.

**Status: exact bounded auxiliary result; not a graph census, not promoted, external review open.** The purpose is to understand the general scope obstruction before returning to the canonical survivor catalogue.

## Bounded band

Fix the near-Turan scalar parameters

    a=20, b=23, t=2,

with all twenty A-labels satisfying

    s_i=x_i=4,

so selected excess is zero, total selected load is `Q=80`, and the exact residual/demand ledger forces

    r=sum_u rho_u=76.

Assume positive residual activity `rho_u>=1` on all 23 B-sources and residual h-index exactly five. No upper restriction smaller than the natural `rho_u<=a=20` is imposed.

A residual-degree histogram is therefore a vector

    c_r=#{u:rho_u=r}, 1<=r<=20,

with

    sum c_r=23,
    sum r c_r=76,
    #{rho>=5}>=5,
    #{rho>=6}<6.                                      (1)

There are exactly **127,885** such histograms.

## Heavy-load screen

For every histogram the verifier applies the already-published exact restricted heavy-load source capacity `C(h,T,P,c)` for every

    h in {1,2,3,4},
    h<=T<=60.

These are only a finite subset of the full heavy-load necessary family. That is enough for the logical conclusion below: any profile satisfying the full family must in particular satisfy this subset.

Exactly **one** of the 127,885 histograms survives all these finite necessary inequalities:

    rho=(5^5,4^11,1^7).                               (2)

This is precisely the scalar staircase obstruction already preserved in the repository.

## Common-margin closure

The preceding global endpoint-orientation theorem evaluates (2) using the compatible endpoint masses of that obstruction and obtains

    2Q=160 >149=sum_u B_u.                             (3)

Hence (2) cannot extend to the coupled canonical selected-incidence/orientation margins.

Therefore:

> **Empty-band conclusion.** No abstract profile in the bounded band (1) can satisfy both the full restricted heavy-load family and the global endpoint-orientation common-margin cut.

The proof is exact: a full-heavy-load survivor must pass the enumerated finite subset, so it must equal (2), but (3) excludes (2). Staircase inequalities or the newer excess-aware envelope can only shrink the intersection further and are not needed for this bounded conclusion.

## Reproducibility

`check_uniform_h5_band.py` enumerates all 127,885 histograms and applies the exact finite heavy-load subset. A separately structured C++ implementation performs the same histogram recursion and local-capacity calculations. Both return the same unique survivor count vector

    (c_1,...,c_20)=(7,0,0,11,5,0,...,0).

The result is about an aggregated parameter band, not graph realizability. It does not prove the unrestricted conjecture or show that all h=5 non-square profiles are impossible. It does show that the most symmetric zero-excess demand-four near-Turan band no longer contains an obstruction once common-margin orientation is restored.

## Strategic consequence

The next obstruction must change at least one ingredient that was frozen here: demand distribution, selected excess, edge surplus/degree parameters, or residual h-index geometry. The highest-value continuation is therefore to expand one coordinate at a time, beginning with small positive selected excess and mixed demand 4/5 profiles, while retaining the excess-aware source envelope from the preceding theorem. Broad canonical survivor scans remain premature.
