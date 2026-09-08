# n=29 candidate — adversarial audit and handoff

8 September 2026. Same-assistant internal audit, not independent peer review.

## Verdict

No blocking defect was found in the assembled fixed-order argument. The new computational burden is confined to `Delta=16`; the other degree ranges have short hand arguments whose exact arithmetic is independently reproduced by `check_all_degrees.py`.

## Load-bearing checks

**Witness coverage at Delta=15.** For every critical edge, deleting it leaves some pair at distance greater than two. In the original graph that pair is either the edge itself with no common neighbour, or a nonedge with a unique common neighbour. With no dominating edge, every such witness pair has degree sum at most 28. Deficits from degree 15 therefore sum to at least two. The count

`m <= C(h,2)+h(29-h)+o(o-1)`

was rederived by assigning one witness to each edge outside the high-deficit set: a witness inside that set covers no outside-outside edge; a missing cross witness covers at most one; an O-O witness covers at most two. Existing cross edges cancel the number of missing cross pairs. No global injective assignment of witnesses is assumed.

At 211 edges the largest bound is 156. At 210, equality in the coarse table occurs only at `(h,o)=(0,15)`. The sharpened O-pair count forces `e(G[O])=0`; every O vertex then has all fourteen possible outside neighbours, yielding exactly `K(14,15)`.

**Delta=16 parameter transport.** The adapted direct calculation has `a=12`, as in n=28 direct197, but now `b=16`. The joint and LP code infers the current `a,b` from the demand and residual-vector lengths. The source bound `p_u <= rho_u+(b-a-1)` therefore becomes `rho_u+3`, rather than silently retaining the old `+2`. Both `t=3` and `t=2` are supplied explicitly. The successful remote aggregate checks every partition position and reports zero survivors.

**Exact versus floating arithmetic.** SciPy solver status is not a proof event. A row is counted as excluded only after integer Farkas multipliers are verified against an independently reconstructed named system, with nonnegative combined coefficients and a strictly negative combined right-hand side.

**Delta=17 factorisation.** For integer `0<=s<=10`,

`16/7 - s(12-2s)/(11-s) = 2(s-4)(7s-22)/(7(11-s)) >= 0`.

Thus eleven labels total at most `176/7`, whereas the two dense scopes require 29 and 31.

**Residual h-index.** Positive surplus gives residual activity. If `h` is the residual h-index, each demand is at most h, so `S<=a h`; activity gives `r>=b+h(h-1)` and the ledger gives `S>=r+2t`. Hence

`b+2t <= (a+1)h-h^2 <= floor((29-b)^2/4)`.

The supplied checker verifies that every `b=18..27` violates this at both 210 and 211 edges.

**Boundary graph.** The checker explicitly constructs `K(14,15)`, verifies 210 edges and diameter two, and deletes each cross edge to confirm its endpoints no longer have distance at most two.

## Failed executions preserved

Three hosted attempts failed before the successful Delta=16 replay. They are recorded in `FAILURE_HISTORY.json`; no failed job is counted as evidence. The fourth run, `34220977858`, is the clean-run execution record.

## Remaining trust boundaries

- Fan's strict bound and the Dailly–Foucaud–Hansberg dominating-edge theorem are external theorem inputs, not re-proved here.
- The quasi-edge, residual injection/activity, charging and h-index lemmas are hand proofs with earlier project audits and limited local Lean coverage, not a full formalisation of this theorem.
- The finite calculation exhausts a necessary-condition relaxation, not all labelled graphs.
- The discovery and checking code was developed by the same assistant. Separate implementations and clean-run execution improve assurance but do not constitute independent research reproduction.
- No positive-surplus actual critical graph appears in the project's saved graph samples, so empirical graph testing cannot establish the dense structural lifting.

**Recommended next assurance:** specialist reconstruction of the Delta=16 graph-to-model necessity, followed by a clean reviewer release. Do not use this audit to promote the theorem ledger without independent review.
