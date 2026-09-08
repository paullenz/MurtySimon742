# Adversarial audit of the threshold source-supplement capacity lemma

8 September 2026. Internal assurance by ChatGPT/Geeps. **The full 13/22 result remains CANDIDATE; independent mathematical review remains OPEN.**

## Verdict

No blocking defect has been found in the threshold source-supplement pair-capacity lemma. The audit sharpened the proof by replacing the phrase “maximising the integer quadratic” with an exact nonnegative-gap identity, isolated the two indispensable structural premises, constructed negative controls when either premise is removed, and independently enumerated the complete abstract partial-orientation domain through five vertices.

The audited inequality is, for h>=1,

    W_h <= h z_h + binom(z_h-h,2)

when W_h>0 (and then z_h>=h), equivalently

    2 W_h <= z_h^2-z_h+h(h+1).

If z_h<h then W_h=0.

## 1. Reduction to actual heavy selections

Let I_h={i:s_i>=h} and Z_h={u:rho_u>=h}. Source demand says every selected edge carrying a label i in I_h has source in Z_h. Since x_i>=s_i,

    W_h=sum_{i in I_h}s_i <= sum_{i in I_h}x_i = sum_{u in Z_h} ell_u,

where ell_u is the number of actual selected heavy labels at source u.

This uses actual selections rather than pretending x_i=s_i. At a fixed label, selected cross-edges have distinct B endpoints because the graph is simple, so if W_h>0 some label has at least h selected sources. Source demand puts all of them in Z_h, proving z_h>=h.

## 2. Heavy-source confinement

Suppose ell_u>h and ui->w is one of the heavy selections at u. Supplement adjacency makes w adjacent in H to every other selected heavy label at u, giving ell_u-1>=h distinct heavy-label neighbours.

If w were outside Z_h then rho_w<h. Source demand also says w cannot itself select a heavy label. Therefore every one of those heavy cross-edges at w is residual, forcing rho_w>=h, contradiction. Hence every heavy selection from a source with ell_u>h has its supplement in Z_h.

This step was checked for the possible loopholes that an edge at w could be selected in the opposite direction, that labels might repeat, or that the supplement could itself be a label. None is possible: a cross-edge has only one B endpoint/source, selected labels at one source are distinct, and A and B are disjoint.

## 3. Unordered-pair injection

Every selected heavy arc u i -> w is attached to the missing unordered B-pair {u,w} which generated it. The graph-to-selected-system construction chooses one cross-edge for each missing B-pair, so no unordered B-pair supports two selected orientations.

Let J be the j sources in Z_h with ell_u>h. By the preceding confinement, every heavy arc sourced in J uses an unordered pair wholly inside Z_h and incident with J. The number of such pairs is exactly

    j(z_h-j)+binom(j,2)
      = j z_h-j(j+1)/2.

The remaining z_h-j sources have at most h heavy selections apiece. Consequently

    W_h <= (z_h-j)h + j z_h-j(j+1)/2.              (A)

There is harmless overcounting here: a low-source selection may use an unordered pair that would otherwise be available to a high source, but adding the two separate maxima can only increase the right side. Thus no disjointness assumption beyond the one-orientation-per-unordered-pair rule is being smuggled in.

## 4. Exact extremal identity

Set z=z_h and q=z-h>=0. Instead of maximising (A), subtract its right side from the claimed bound. Direct algebra gives

    h z + binom(q,2)
      - [(z-j)h + j z-j(j+1)/2]
      = (q-j)(q-j-1)/2.

For every integer d, d(d-1)>=0, since either d>=1 or d<=0. Therefore the gap is nonnegative for every integer j. This proves the threshold bound without calculus, rounding or an unproved maximisation claim.

Equality in this arithmetic step occurs only for

    j=q    or    j=q-1,

that is, j=z-h or j=z-h-1. Any equality in the full graph inequality would additionally require equality in W_h<=sum ell_u, saturation of all low-source capacities, and saturation of the relevant unordered pairs. This rigidity may be useful later, but is not needed for the 13/22 proof.

## 5. Independent abstract enumeration

A new checker, `src/check_threshold_adversarial.py`, was written separately from the inherited threshold script. It enumerates every partial orientation of every unordered pair through n=5, marks each initial segment as a candidate Z, checks every h<=|Z|, and admits exactly those states satisfying the abstract high-source confinement rule. It then verifies both the direct j-source bound and the exact extremal bound.

Fresh local and clean-runner result for committed v3 logic:

    orientation states: 59,809
    marked (Z,h) checks: 1,191,446
    admitted states: 783,955
    minimum bound gap: 0
    equality hits: 60,251

The separate exact arithmetic sweep checked 5,302,626 triples (z,h,j) with z<=250 and found 63,001 equality instances, all at j=z-h or j=z-h-1.

GitHub Actions run `34200648279` on Ubuntu 24.04 / Python 3.12.3 completed successfully. The checked threshold source SHA-256 was

    cedadf5b0f7cde4f10d54525fd28ca0bfbb906cc0bfdcba5d9a361b09bf6418e

and the workflow artifact containing the construction, residual-injection and threshold reports had SHA-256

    749a0260e995f373f4b78de1f8b9b27edaf5060e4a686be441cb9e431b6b4521.

These computations are evidence against implementation/arithmetic mistakes, not a universal proof; the displayed identity and graph reduction carry the universal claim.

## 6. Negative controls

Two deliberately illegal abstract systems violate the capacity bound.

1. **Allow both orientations of one unordered pair.** A sufficiently dense bidirected source graph exceeds the bound. This confirms that unordered-pair injection is essential rather than decorative.
2. **Allow a source with load >h to use supplements outside Z_h.** A single high source can then spend arbitrarily many outside pairs, exceeding the bound. This confirms that heavy-source confinement is essential.

The real graph construction supplies both premises: one selected orientation per missing B-pair, and supplement confinement from source demand plus supplement adjacency.

## 7. Remaining risk

The arithmetic/combinatorial core of the threshold lemma is now simple and strongly checked. The remaining universal risk is not the extremal maximisation; it is whether the graph-to-model premises have been derived with exactly the needed scope in every case. The quasi-edge construction and residual/source-demand machinery have separate audits and a local Lean slice, but the global finite-cardinality threshold reduction is not itself formalised.

**Research decision:** treat the threshold capacity lemma as internally strengthened but still candidate mathematics. The next highest-value assurance target is the layer-sum aggregation from the family of threshold inequalities to `3 S^3 <= a^2 r(2r+1)`, unless an external reviewer challenges one of the two structural premises above.
