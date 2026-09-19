# Rigid one-code cut: local unused-slot surcharge

Date: 2026-09-19

Status: structural bridge from the preserved local witness-slot/Hamming theorem into the active rigid one-code branch. This is conditional on the rigid complete-cut hypotheses and does not assert an eventual theorem.

The 19 September audit boundary remains unchanged. `X_3` remains a mandatory hostile control and does not enter the present hypotheses.

## 1. Preserved local theorem

For every A-vertex `z`, let `r_z` be the number of unused rooted B-edge witness slots attached to z. The preserved local slot/Hamming theorem says

> `sum_{w in N_A(z)} d_H(c(w),c(z)) <= r_z d_A(z)`.      `(LH)`

Also

> `sum_{z in A} r_z=r`.                                   `(R)`

The active rigid one-code cut has `X--Y` complete, every vertex of Y has code d, and no vertex of X has code d.

---

## 2. Unit XI — every A-vertex pays at least one unused rooted slot

### Theorem 2.1 — rigid-cut slot surcharge

Every vertex of `A=X dotcup Y` satisfies

> **`r_z>=1`.**                                           `(SLOT1)`

Consequently

> **`r>=a`.**                                             `(SLOT-A)`

### Proof

Take `x in X`. Since `y>0`, x has a neighbour in Y, and that neighbour has code d different from `c(x)`. Hence the left side of `(LH)` is positive. Therefore `r_x>0`, so integrality gives `r_x>=1`.

Take `y0 in Y`. Since `x>0`, y0 has a neighbour in X, and every X-code differs from d. Again `(LH)` has positive left side, so `r_{y0}>=1`.

Summing over all A-vertices gives `(SLOT-A)`. `square`

This statement applies to the whole rigid one-code complete-cut branch, not merely to `m=g+1`. It is exactly the local information lost by a global direct/Hamming scalarization.

Using the preserved rooted identity `r=f+delta`, it also yields

> `f+delta>=a`.                                           `(SLOT-FD)`

No sign assumption on delta is needed for `(SLOT-A)` itself.

---

## 3. Unit XII — weighted surcharge in the minimal-reservoir geometry

Return to `m=g+1`. Let the common core code be `c_*` and put

> `h_*:=d_H(c_*,d)>=1`.

For the g matched-head vertices `h_i in H_M`, put

> `h_i^M:=d_H(c(h_i),d)>=1`,

and define

> `H_X:=k h_*+sum_{i=1}^g h_i^M`.                        `(HX)`

Thus `H_X>=k h_*+g>=x`.

### Y-side local bill

In the active branch `e(Y)=0` and `X--Y` is complete, so every `y0 in Y` has

`d_A(y0)=x`.

Its incident crossing edges have total Hamming length exactly `H_X`. Hence `(LH)` gives

> **`r_{y0}>=ceil(H_X/x)`** for every `y0 in Y`.          `(RY)`

Therefore

> `sum_{y0 in Y} r_{y0}>=y ceil(H_X/x)`.                 `(RY-SUM)`

### Core-side local bill

Star separation says every H_M vertex adjacent to `z_*` is anticomplete to H_0. Exactly A of the g H_M vertices are nonadjacent to `z_*`. Since H_0 itself is independent, every core head `x0 in H_0` has at most A neighbours in X. Thus

> `d_A(x0)<=y+A`.

The y crossing neighbours in Y alone contribute Hamming length `y h_*`. Therefore

> **`r_{x0}>=ceil(y h_*/(y+A))`** for every `x0 in H_0`. `(RCORE)`

Summing,

> `sum_{x0 in H_0} r_{x0}`
> ` >=k ceil(y h_*/(y+A))`.                              `(RCORE-SUM)`

Every H_M vertex still has at least one unused slot by Theorem 2.1. Combining the three disjoint vertex sets gives the structural floor

> **`r >= y ceil(H_X/x)`**
> ` **+ k ceil(y h_*/(y+A)) + g.**`                      `(R-WEIGHT)`

This dominates the bare `r>=a` whenever either the average X-to-d Hamming distance or the core distance `h_*` is forced above one strongly enough.

---

## 4. Equality layer `A=0`

When `A=0`, `z_*` is complete to H_M and star separation makes H_0 isolated inside `G[X]`. Hence every core head has

`d_A(x0)=y`.

The local inequality becomes exact at the denominator level:

> **`r_{x0}>=h_*`** for every `x0 in H_0`.                `(RCORE0)`

Thus

> **`r >= y ceil(H_X/x)+k h_*+g`.**                      `(R0-WEIGHT)`

In particular `h_*=1` and all H_M-to-d distances one is the unique Hamming-cheapest possibility compatible with the universal `r>=a` floor. Any larger code distance creates an immediate local-slot surcharge.

This gives a new interpretation of the earlier `A=0` equality geometry: H_0 isolation is not free. It converts code distance from d directly into unused rooted witness slots, one-for-one at every core head.

---

## 5. Interaction with the pair/residual pinch

The pair/Hall optimizer can prefer `A>0` because an A-defect relieves `2k-1` units of X-Hall demand. The local-slot theorem now shows a second effect of the same defect: increasing A raises the possible core A-degree from y to at most `y+A`, which can lower

`ceil(y h_*/(y+A))`.

So A-defects have **two** structural benefits which must both be paid for by their explicit unmatched-slack cost:

1. Hall relief in `H(A,M)`;
2. local-slot relief in `(RCORE)`.

By contrast M-defects do not alter this core local-Hamming denominator. This sharpens the distinction between the two currencies exposed in the pair/residual theorem.

The next calculation should therefore intersect `(R-WEIGHT)` with `r=f+delta` and the explicit clamped allocation `(M_hat,A_hat)`, rather than price A only through the scorecard.

---

## 6. Negative control and trust boundary

`X_3` has an independent A-layer at its canonical root and no active rigid complete A-cut of the present type. The theorem does not apply to it.

The result uses only the already-audited local slot/Hamming theorem plus the current rigid complete-cut geometry. It does not use the finite source-tuple theorem or the four-exception gate.
