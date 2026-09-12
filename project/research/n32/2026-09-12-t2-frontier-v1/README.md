# N32, Delta=17, m=257 (t=2): frontier checkpoint

12 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: OPEN reconnaissance checkpoint. No N32 theorem is claimed here. Independent mathematical review remains open.**

## Target

For `n=32`, `Delta=17`, put

```text
a = 14,
b = 17,
t = m - b(a+1) = m-255.
```

The fourteen-label hand theorem already closes every `m>=259`. The `m=258` (`t=3`) equality frontier reduces to the three score-maximising demand profiles and all three have separate hand contradictions preserved in `project/research/n32/2026-09-11-hand-route-v1/`.

Thus the only currently unresolved above-Turan branch is

```text
n=32, Delta=17, m=257, t=2.
```

## Score frontier

The canonical bridge gives

```text
Q(s) >= b+2t = 21,
```

while the fourteen-label theorem gives `Q(s)<=23`.

A preliminary exact score scan in the current research session found that the raw demand frontier is finite and small (working count: 71 multisets with `Q>=21`). This count is reconnaissance only until a standalone replay is committed; it is not used as a proof premise.

The key structural point is that the `Q=21` sector has zero threshold-tail slack: the lower bounds on residual threshold counts are then forced to equality. The `Q=22,23` sectors have only one or two units of aggregate slack. Hence the raw number of demand profiles substantially overstates the remaining freedom.

## Negative tests already performed

### 1. Fourteen-label score alone

The scalar inequality `Q<=23` does not close `t=2`: the required lower bound is only `Q>=21`.

### 2. Immediate Hall-core consequences

The direct graph-level Hall/source inequalities (selected-incidence forcing, pointwise source cap, threshold supplement transport, one/two-rectangle Hall counting, and total selected-incidence balance) do not immediately collapse the entire `t=2` frontier by the same short equality argument that closes `t=3`.

This is not evidence against the RX/Hall route; it shows that a stronger weighted/combined inequality is needed.

### 3. Witness-deficit shortcut

Because `n=32`, `Delta=17` and there is no dominating edge in the dense non-bipartite target range, a witness pair has degree sum at most 31, so relative to degree 17 its total degree deficit is at least 3. This is one unit stronger than the odd-order balanced witness calculation used at N29/N31.

However an extremal capacity check shows that this extra deficit budget alone does not force the witness-capacity upper bound below 257 for every admissible deficit distribution. Therefore the simple witness-deficit inequality is insufficient by itself and should not be promoted as an N32 closure.

## Most promising next route

Return to the preserved `t=2` RX/Hall compression, but keep the proof target combinatorial and small. In particular, the N29 `t=2` work established that the difficult Hall geometry can be expressed using a small family of cumulative BC rectangles plus diagonal slack thresholds. The graph-level forms of these inequalities are already preserved in

- `project/research/general_n/2026-09-09-rx-hall-v1/HALL_CORE_SYMBOLIC_LEMMAS.md`,
- `.../T2_RECTANGLE_DIAGONAL_COMPRESSION.md`, and
- `.../DIAGONAL_SLACK_THRESHOLD.md`.

The immediate N32 objective is to determine whether the 14-label `Q>=21` frontier is eliminated by a small fixed rectangle/diagonal potential. Any positive computational result must then be exactified and translated into an explicit hand inequality before theorem use.

## Trust boundary

- N32 `m>=258` remains hand-closed in the current candidate framework.
- N32 `m=257`, `Delta=17` remains OPEN.
- No claim should be made that the N32 Turan upper bound is proved until this case is removed.
- If `m=257` is removed, the equality-level `m=256`, `Delta=17` branch must still be addressed separately to obtain uniqueness of `K_{16,16}`.
