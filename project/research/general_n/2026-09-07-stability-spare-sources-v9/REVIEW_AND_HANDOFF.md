# Review, limits and handoff — structural v9

**Candidate mathematics; internal checks pass; specialist external review is Paul's task.** No external message was sent. This continuation changes no frozen n25/n27/n28 proof, original evidence archive or governed theorem-ledger entry.

## What was accomplished

The inherited 0.613270459830... charging theorem was rederived with direct quasi-edge existence from edge-criticality. Its proof now has no need for the complement classification theorem, residual activity, Fan's estimate, the weak-core reduction, or the finite-order calculations. No blocking error was identified in the audited charging argument, including a=0, zero-residual sources, unused rho=a rows, and odd-order rounding.

A new exact deficit identity forces the minimum-demand distribution close to lambda a if t is close to ca^2. The good-label pair-capacity lemma prevents such concentration from attaining t >= (c-1/5000)a^2 at a>=25. Twenty-four explicit small-a inequalities extend the resulting 0.6131682474535585... maximum-degree threshold to all n>=4. This is a fixed quadratic improvement, not graph edit-distance stability. Constants were chosen for a short rational proof, not optimised.

The separate spare-source theorem gives h ell <= (2h-1)z for h<=z<=h^2+h. It includes two spare sources for every h>=2 and the earlier one-spare case. It needs no positive surplus. A bound attained by reduced incidence systems is not claimed sharp for actual critical graphs.

## Adversarial mathematical checks

1. Quasi-edge existence uses only an adjacent total dominating pair in H+uw, no such pair in H, and a third vertex missed by u,w. It is not assumed for arbitrary missing pairs without that third-vertex condition.
2. The residual injection charges distinct supplements, and each forced cross-edge has a common missed A-vertex. That prevents it from being a selected edge with unique B-exception. Minimum H-degree, not an arbitrary root, gives x_i>=s_i.
3. The charge uses exactly s_i chosen incidences but never assumes all actual selected incidences equal the demand. The later pair lemma uses P=sum x_i, not just S.
4. Good-label incidences must all originate among rho>=La. A low-residual source can select only bad labels. This is the premise confining busy-source supplements, not an assumption that every source is busy.
5. Busy arcs consume unordered pairs incident with the same busy set. Counting each direction separately would be wrong. Low sources are bounded by their selected outdegree, never charged the whole pair count again.
6. The deficit's three terms are nonnegative independently. The Cauchy bound is an upper bound on S and hence on r. The good-label fraction uses the squared deviation lower bound; it does not assume all demands lie near their mean.
7. Theorem A has a>=25 explicitly. The small-a table covers every b above its minimum by monotonicity and is not a claim to have enumerated every graph at 24 orders. No edge-deletion transfer is used.
8. For spare sources, exceptional labels have d=2h. Their supplements must have residual degree h and miss the selected label, forcing x<=z-1. Exceptional incoming/outgoing counts cancel only because these arcs stay inside Z.
9. A source with no labels in I still receives the compensation bound. The restriction z<=h^2+h is used both there and in the sign of the incoming coefficient. No claim for arbitrary k is made beyond k<=h^2.
10. The false shortcut L_u<=2h-1 for every source was deliberately challenged. Exceptional local overload occurs; the compensated bound is necessary. Reduced sharpness examples are not claimed realisable as graphs.

## Testing boundaries

Exact algebra checks, separate rational-interval checks, saved graph-system replays and reduced incidence/oriented-graph tests all pass. See the evidence JSONs and FULL_REPLAY_REPORT.json for actual counts and commands. The saved graph corpus contains 4,694 selected systems on 781 distinct labelled graphs. None has positive surplus, and no nonempty maximum-demand spare class falls in the theorem's range. Consequently it does not test the dense or spare contradiction nonvacuously. The separate 7,435 reduced systems include 3,555 with exceptional arcs; those are not critical graphs.

The graph checker shares Q(sqrt2) support code with the algebra checker, while the interval checker imports no project code. Both implementations and all derivations are by the same assistant. No claim of independent researcher reproduction follows.

## Formalisation: completed slice and remainder

Lean 4.19.0 checked five local implication/uniqueness lemmas without sorry, new axiom declarations or native_decide. Source hash and toolchain archive hash are in evidence. These assume explicit quasi-edge predicates. They do not prove graph-wide quasi-edge existence, finite cardinality injections, the charging sum, Theorem A, Theorem B, or the n28 theorem. Full formalisation remains OPEN.

## Corrections and unsuccessful steps preserved

The earlier literature comparison omitted arXiv:1610.00360. Its abstract uses 0.676; a related author-posted text's theorem uses 0.6756 and its PDF abstract 0.6755, with a different title-page date. We record rather than conceal this uncertainty, and claim no best-known result.

The initial exact algebra harness raised a Python TypeError on reversed Q2/rational comparisons. Reversed comparisons/division were implemented, after which the complete tests passed. No output from the failed execution was counted. The initial LaTeX build used hypersetup before hyperref and failed; the preamble ordering was corrected. A long unbreakable archive hash overflowed a reference paragraph; the hash remains in provenance and was replaced by a provenance pointer in the paper. The first build wrapper also assumed an unwrapped page-count log line; whitespace-tolerant parsing fixed it before any successful wrapper report. These were harness/editorial fixes, not changed mathematics. Exploratory floating-point optimisation is preserved but is not needed for any theorem or replay.

## Next research targets

First obtain external review of the minimal three-lemma graph core, the pair-capacity inequality, the explicit constants, and the compensated spare-source proof. Paul handles outreach. On the mathematical side, investigate mixed high-demand classes and a version of the source bound for z>h^2+h, or optimise the quantitative loss without replacing exact reasoning by floating-point extrapolation. On the formal side, add quasi-edge existence and the finite injections, then the charging sum. Do not resume a routine march through finite orders as the primary goal. Non-bipartite density-gap work remains a later application; it has not been advanced or solved in this checkpoint.
