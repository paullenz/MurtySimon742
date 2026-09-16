# Murty–Simon / Erdős #742 — live current state

> Read this first. The d=2 private witness forces a different edge to be redundant. The symbolic closure is preserved below before its verification unit; new finite checks have not yet run.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_D2_SINGLETON_CLOSURE_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Theorem-first priority. One bounded closure derivation, not a survivor scan.

**INSPECTED PREDECESSOR:** `81067c78adc18c1bb4c3792c289d168af20f0540`, tree `851199dec81cb2f134b19406fb041c6a819506aa`, CURRENT_STATE blob `27d883cdb89d192085c6c93e4e7b34004460b502`. Main was re-read immediately before this contents update. The complete preceding private-witness normal form remains at that immutable commit.

**LAST VERIFIED RESULT:** new internal symbolic closure; finite verification pending. In the d=2 defect-one normal form, each common label q has R_q=2, x_q=0, hence delta_q=2 and N_G(q)={t,s} union X union Y union O. For every x in X and y=f(x), selected-set equality makes x and y adjacent to the same Z-labels. Deleting qx preserves every previously short pair: the endpoints use t; exclusive neighbours of q use y or pivot p; exclusive neighbours of x use t, y, or a high vertex's actual s-destination. Thus every C-X edge is separately redundant, contradicting original criticality. No full-twin or injectivity assertion is used.

**CONSEQUENCE:** combined with the preserved zero-defect and d>=3 proofs, every actual exact block |T|=|H|=d>=2 has L+beta+2mu>=2, and W>=d+(d-1)m+2. The conditional quadratic clique bound remains unchanged. For d=2 the generic thresholds W>=6 and E>0=>W>=8 already followed by rounding older bounds because W is even; this unit closes a structural exception and strengthens the joint W,m bound, not those rounded scalar thresholds. No positive-surplus or pool-size restriction.

**CHECKS:** new finite checks NOT_RUN at this checkpoint. No prior replay, catalogue application, graph-realisation assertion, independent acceptance or literature novelty is claimed. External review OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Prior 203-key candidate union, 41 strict/equality certificates, 170-candidate audit and state3349 retain their previous boundaries. No workflow launch, q-enumeration or promotion.

**UNPRESERVED WORK:** no completed mathematical derivation remains only in session memory after remote confirmation. Full normal form is at the immutable predecessor; all new closure steps are below. Earlier raw-stream and attachment transfers remain pending.

**DEFERRED ADMIN:** older evidence transfers; root README/reviewer integration; unrelated CI/status work; independent review, novelty assessment and promotion.

**NEXT ACTION:** verify and package this d=2 closure with separately structured explicit-path checks, full representative noncritical controls, and negative controls for common-label saturation, Z-neighbour containment and the high-to-Y destination. Keep local completions separate from actual canonical systems. Preserve exact inputs and decisions. The subsequent mathematical target is one missing tight edge, not an unsupported export of the clique bound.

**PROCESS RULE:** one bounded unit then preservation and one remote confirmation; no background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Full new closure, with the preserved normal-form hypotheses

Use the canonical system and all-edge criticality of G. In the d=2 intrinsic-defect-one case, T={t,s}, the two high vertices form H, C has c>=2 common K-labels, k is the unique singleton K-label adjacent to s, X=V_t and Y=V_s have residual sets {s} and {t}, |X|=c, |Y|=c-1. Put O=B minus (H union X union Y), Z=A minus (T union C union {k}). The exact rows give

    N_G(t)={s} union C union X union O,
    N_G(s)={t,k} union C union Y union O.

The complete proof at predecessor81067c78 establishes that criticality of ts requires N_G(t) intersect N_G(k)={s}. It then forces R_o={k} for every o in O, N_F(k)={s}, N_G(k)={s} union Y, and a function f:X->Y with N_G(x) intersect Y={f(x)}. For x in X and y=f(x), forward and reverse selected containment give

    S_x={k} disjoint-union S_y,
    N_J(x) intersect A={s,k} disjoint-union S_y,
    N_J(y) intersect A={t} disjoint-union S_y.

Apart from k at x, these selected sets lie in Z. Hence for every z in Z, xz is a G-edge if and only if yz is a G-edge. The map f is not assumed injective; identical A-neighbourhoods are not claimed to imply identical B-neighbourhoods.

### Common-label saturation supplies the missing global restriction

Fix q in C. It is never selected: at a low source this would require both tight labels residually in at most one slot, and at H it is residual. Its only residual occurrences are the two high vertices. The full pools X and Y have tight residual labels, while every O-vertex has residual label k. Thus R_q=2 and x_q=0. The minimum-pivot demand inequality x_q>=s_q=max(0,delta_q-R_q) forces delta_q<=2. Its two tight neighbours already meet that bound. Consequently

    N_F(q)={t,s},
    N_G(q)={t,s} union X union Y union O.

There are no additional q-C or q-Z edges in F. This conclusion cannot be inferred from the earlier local private-witness control without the demand and complete residual accounting.

### Delete qx rather than the protected tight edge ts

Take any x in X, q in C and y=f(x). The edge qx exists by full-pool saturation. Its endpoints retain the path q-t-x after deletion.

For an exclusive neighbour w of q, its exact neighbourhood leaves only these cases: w=s has replacement x-y-s; w in X minus {x}, Y or O has x-p-w. The vertex t is already adjacent to x. All these paths avoid qx.

For an exclusive neighbour w of x, partition the whole graph. In A, t is already adjacent to q; another common label q' has q-t-q'; and z in Z adjacent to x has q-y-z by the selected-set equality. Neither s nor k is adjacent to x. In B, only H lies outside N_G(q). Each h in H has an actual selected s-obligation ending at some y_h in Y, so hy_h is a G-edge and q-y_h-h is a replacement. Every other B-neighbour of x is already adjacent to q. Finally the pivot p has q-y-p.

These cases exhaust the pivot, all A-labels and all B-vertices, including unrestricted Z and O. A path of length at most two destroyed by deleting qx must have endpoint q or x; its endpoint pair or one of these exclusive-neighbour cases is covered. Therefore deletion loses no previously short pair and in particular preserves diameter at most two. This contradicts all-edge criticality.

The d=2 one-defect case is therefore symbolically closed. Every C-X edge is individually redundant under its forced normal form; simultaneous deletion is not asserted. Combining with the preceding zero-defect and d>=3 treatments yields intrinsic defect at least two for every d>=2 exact block. Larger defects and absence of an exact block remain outside this closure.

### Abandoned shortcut retained

The initial attack noticed a fibre of f with at least two sources because |X|>|Y|. Shared selected sets alone do not prove full twins or an edge deletion result. The successful proof does not use that shortcut; it uses the common labels' exact residual degree and a complete affected-pair partition instead.
