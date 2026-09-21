# Second hostile replay of the repaired half-ray equality face

Date: 2026-09-21

Status: independent audit of `HALF_RAY_EQUALITY_FACE_INDEPENDENT_REPLAY.md`. Result: **passes at its stated conditional scope**. This is now strategically subordinate because the raw boundary-population theorem closes the entire half-ray before the H--U equality analysis is needed.

## 1. Algebraic gate

From the corrected residual-slot theorem,

`a+c0>=binom(N,2)`,

`Delta=a+(h-N)+c0>=h-N+binom(N,2)`.

On `Delta=h`, one has exactly

`a+c0=N`.

Combining with the slot inequality gives `binom(N,2)<=N`, hence `N<=3`. The replay therefore has exactly the four faces `N=0,1,2,3`; no equality face is omitted.

## 2. Physical checks

I rechecked the load-bearing points rather than merely the scalar arithmetic.

- **N=0.** `a=c0=0` gives exact shared saturation and forces `R_q=2M_H`. Endpoint-indexed resources are H-anticomplete, so comparing the mechanism partition with the H--U physical edge count gives `M_H=0`; H is complete. B1 resources touching two distinct H-rows would destroy the two private-foot orientations of their connecting H-edge, so all B1 resources concentrate on one row. The exact local H-degree identity then caps that row at three U-neighbours, contradicting `t-1` resources for `t>=5`.

- **N=3.** The repaired proof correctly retains all allocations of `a+c0=3`; it does not silently assume `(0,3)`. A D=0 saturated carrier costs two units of a, while a D=2 carrier consumes a nonshared physical slot. This eliminates `(2,1),(1,2),(3,0)`. In `(0,3)`, the three distinct D=2 carriers exhaust the three nonshared slots and have H-degree one; no B1 shared resource can then survive, contradicting positive S.

- **N=2.** All three allocations `(0,2),(1,1),(2,0)` are covered. The key physical point is sound: a D=0 saturated carrier's unique H--U edge is already assigned to the residual `R_j` mechanism and cannot simultaneously be counted as its B1 shared mechanism. D=2 carriers consume the nonshared allowance. Each allocation therefore leaves fewer usable shared resources than exact saturation requires.

- **N=1.** Both allocations are covered. For `(1,0)`, the D=0 saturated carrier is physically unavailable to the shared mechanism despite `c0=0`. For `(0,1)`, all remaining used shared resources must be B1; only H-rows nonadjacent to the saturated source are eligible, at most two such rows exist under `a=0`, and each can host at most one B1 without destroying a required reverse-private slot. Hence `S<=2`, contradicting `S=t-2` for `t>=5`.

## 3. Potential double-counting challenge

The repaired proof's recurring use of “this physical vertex/edge is already consumed by `R_j` and cannot also be a B1 shared resource” is legitimate because the mechanism partition is a partition of actual H--U edges, not merely a count of abstract witness incidences. No step in the four-face argument requires assigning the same physical H--U edge to two mechanisms.

Similarly, the D=2 nonshared-slot count is physical: distinct saturated sources have distinct carriers in the cases where the proof needs distinctness, because each carrier's required H-hole pattern distinguishes it from the other saturated carrier.

## 4. Audit conclusion

The repaired equality-face theorem survives this second hostile replay:

> `Delta>=h+1=2t`, hence `L_H>=5t-1`, for `t>=5`,

conditional on the corrected half-ray interface and residual-slot-collapse lemmas.

However, this theorem is no longer load-bearing for the eventual programme. The same session's raw boundary-population obstruction proves that the half-ray has **no literal realization at all** for `t>=4`, using only boundary criticality and U-code-class population. Therefore the equality-face result should be retained as an internally useful audit/check, not as the main route forward.
