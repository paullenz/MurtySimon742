# Focused foundations audit and external review checklist

12 September 2026. Baseline: `8f55e0c763baff8de27897ea86cfca4bd45cb00b` in
`paullenz/MurtySimon742`. Same-assistant internal audit; **not external review**.

## Verdict and scope

No blocking implication flaw was found in the canonical selected/residual
bridge, the balanced-degree witness-capacity argument, the joint-clipping
recurrence, or the N34 upper-layer transfer reviewed here. This is a focused
dependency audit, not a new replay of every historical fixed-order certificate
or a novelty determination.

Two textual corrections are made visibly in current source:

1. The sixteen-label paper incorrectly inferred actual clipping failure from
   an inconclusive independent-interval bound at a=17. The actual joint
   minimum net gain there is +2. The a=16 theorem is unaffected.
2. The potential-certificate lemma unnecessarily stated `mu>=0`, although
   the implementations use `mu=mu+ - mu-`. The balance term is identically
   zero, so any real mu is valid. The new N34 certificates include 19 negative
   balance multipliers among 111 certificates. The proof now explicitly
   permits that sign; all other required nonnegativity conditions remain.

No frozen PDF, archived certificate, or governed theorem-ledger entry is
modified. The corrections and new packages are linked from the reviewer
entry points.

The publication link sweep also found a pre-existing N31 regression filename
mismatch in the top-level README and the N31 release entry point. Both now
link to the existing `check_n31_arithmetic.py`; no proof or regression code
was changed by that repair.

## Primary-source check

The primary text inspected was Dailly, Foucaud and Hansberg,
[*Strengthening the Murty-Simon conjecture on diameter 2 critical graphs*](https://arxiv.org/pdf/1812.08420v1),
Theorem 4, PDF page 4. It gives `m<=floor(n^2/4)-2` for non-bipartite D2C
graphs with a dominating edge, except H5. H5 has six vertices and eight edges,
as specified on PDF page 2 and in Figure 2. Thus n>=7 excludes the exception.
The [arXiv record](https://arxiv.org/abs/1812.08420) identifies the publication
as *Discrete Mathematics* 342(11), 2019, 3142–3159,
[DOI 10.1016/j.disc.2019.06.023](https://doi.org/10.1016/j.disc.2019.06.023).
The theorem numbering was verified in the preprint, not separately against
the typeset publisher edition.

This input disposes of dense non-bipartite dominating-edge graphs. It does
not prove the witness-capacity injection or the selected/residual bridge;
those require their own arguments below.

## Dependency-by-dependency checks

| Dependency | Check performed and potential failure point | Current finding |
|---|---|---|
| Critical-edge witnesses | Removing an edge can destroy all paths of length at most two only for its endpoints, or a pair whose unique two-step path contains it. A nonedge witness has one common neighbour. | Complete direct/two-step coverage. |
| Witness degree sum | For a nonedge witness, the neighbourhood union has at most n-2 vertices and intersection size one. For a direct witness, the intersection is empty; no dominating edge leaves at least one vertex outside the union. | Both give degree sum at most n-1 in the required branch. |
| Witness capacity | A missing pair meeting L and covering an edge outside L has exactly one endpoint in L. Its unique path covers at most one outside edge. Actual L-X edges and missing L-X pairs partition the same pair set. | No omitted or double-counted L-X capacity. |
| Balanced-degree equality | Convexity reduces the relaxed count to endpoints. At equality the low-deficit set is empty, the deficit-one set is independent, and its degrees exhaust all cross edges. | The equality argument is explicit and order-independent. |
| Complement quasi-edge existence | Adding a missing B-pair cannot use that pair as the new total-dominating pair because both endpoints miss v; an existing cross-edge has the opposite endpoint as its unique exception. | The adjacent-pair and unique-exception requirements are retained. |
| Selected injection and ledger | A selected cross-edge recovers its unique missing unordered B-pair; selecting exactly one orientation prevents collisions. Counting all B-pairs gives e(F)=r+t. | No duplicated orientation or multiplicity. |
| Pointwise forcing | Distinct selected labels at one source have distinct exceptions. Forced cross-edges jointly missing an A-vertex cannot be selected, whose exception lies in B. | Residual charges used in Sections 6.1–6.4 are injective in the stated families. |
| Source and endpoint bounds | A B-pair is outward, inward or present; q+p is its missing degree. Outgoing exceptions and incoming sources cannot collide without selecting both orientations. | Correct source identity includes q before cancellation; endpoint load is q+p. |
| Residual activity | At a residual-zero source, there are no F-edges between its A-neighbours and non-neighbours. Internal edges force disjoint residual families with their A-endpoints in the two parts. | Gives r>=e(F)=r+t, contradiction for t>0. |
| Threshold capacity | Every heavy arc from a source with more than h heavy labels has its exception in the high-residual set. Such arcs inject into unordered pairs incident with J. | Slack is the nonnegative integer product (z-h-j)(z-h-j-1)/2. |
| Isolated-C exclusion | Missing pairs away from an isolated C vertex force residual quasi-edges with A-exceptions, plus one extra residual incidence per B-source. | Gives b<=a-1-t; hence dmax=a-2 in the N34 domain. |
| Tail score | S=p+sum N_h and r=b+sum z_h; threshold capacity bounds each z_h below by gamma_h(W_h). Residual-tail monotonicity can only increase those minima. | Correct sign: b+2t<=Q; monotone closure is conservative. |
| Potential transfer | At positive demand d=R+s. Selected edges give d<=rho+q-1 and R+x>=q+p. The potential increases in d and decreases in the second coordinate. | Every label contribution is bounded by its source contribution. |
| Supplement transport | Every arc from a source with q>=j+1 ends where rho+q>=j by supplement forcing. | T_j<=0, so nonnegative tau_j has the required sign. |
| Scalar envelopes | Sum of the local inequalities cancels both incidence and orientation balances. The potential and transport sums are nonpositive. | Free mu is valid; strict integer gap supplies contradiction. |

The canonical bridge was reviewed in its entirety, including residual
activity, isolated-C and h-index arguments, rather than only the lemmas
used by the two new N34 layers.

## New arithmetic and complete-domain checks

- Joint clipping: all 46 rows requiring joint repair were compared with a
  direct enumeration of 156,721 lower multisets. Terminal domains were
  rechecked using tail counts rather than multiplicity recursion.
- N34 demand frontier: a complete C++ scan covers all 77,558,760 sorted
  15-demand multisets. The resulting 1,296-row union frontier is checked
  by direct Python tail formulas and fully expanded to residual states.
- N34 292-edge layer: two exact integer envelope certificates.
- N34 291-edge layer: 109 exact integer envelope certificates and one hand
  application of the tight total-demand threshold lemma.
- The standalone envelope verifier imports no LP builder or SciPy; it
  regenerates all local label/source inequalities and verifies 40,239
  integer inequalities, strict gaps, and complete coverage of those layers.

These checks reduce implementation risk. They do not turn finite necessary
states into graphs or replace a specialist audit of the universal implications.

## Concrete external review sequence

1. Read the [balanced-degree theorem](../../../research/general_n/2026-09-12-balanced-degree-v1/BALANCED_DEGREE_THEOREM.md)
   together with its [capacity hardening](../../../research/general_n/2026-09-12-balanced-degree-v1/WITNESS_CAPACITY_HARDENING.md).
   Check the missing-pair injection before its endpoint algebra.
2. Audit the [canonical bridge](../../../research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md),
   particularly unique exceptions, residual activity, endpoint load and threshold capacity.
3. Check the [tight-threshold lemma](../../../research/general_n/2026-09-12-joint-clipping-v1/TIGHT_THRESHOLD_LEMMA.md),
   especially why every high source is active in its equality argument.
4. Review the [joint recurrence](../../../research/general_n/2026-09-12-joint-clipping-v1/JOINT_CLIPPING.md)
   and run its independent finite verifier.
5. Review the [N34 partial route](../../../research/n34/2026-09-12-frontier-v1/README.md)
   and run its solver-free upper-layer verifier.

No request for review has been sent to another person in this work session.
External review, independent reproduction and novelty remain OPEN.
