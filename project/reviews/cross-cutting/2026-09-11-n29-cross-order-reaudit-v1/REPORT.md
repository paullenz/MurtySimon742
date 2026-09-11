# n=29 fresh cross-order bridge re-audit

11 September 2026. Research directed by Paul Lenz; re-audit performed by ChatGPT/Geeps against the current `main` branch.

**Status:** same-assistant hostile re-derivation, not independent expert review. No fixed-order candidate is promoted by this report.

## Trigger and scope

This pass was triggered by a user-supplied blind external-AI red-team of the n=29 result. The body of the shared conversation was not retrievable by the tools available in this runtime, so this report does **not** claim to answer or dispose of any allegation that appears only in that inaccessible transcript. Instead, it deliberately re-attacks the current proof-critical n=29 bridge from the repository and traces the shared lemmas into the other fixed-order candidates.

The principal files checked were:

- `project/reviews/n29/2026-09-09-fan-free-v2/PROOF.md`;
- `project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md`;
- `project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md`;
- `project/reviews/n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md`;
- `project/reviews/n29/2026-09-09-bridge-standalone-v1/ISOLATED_C_LEMMA.md`;
- the n=29 minimal-kernel preparation, residual-row and corrected cumulative-threshold/Farkas code;
- current Fan-free reviewer proofs for n=25,27,28,30.

## Verdict

No blocking mathematical defect was found in the current n=29 bridge or minimal trusted kernel.

One **real but non-blocking proof-text defect** was found in the threshold-capacity lemma: an intermediate algebraic difference was written in the wrong order. The final inequality was nevertheless the correct one, and the corrected sign is exactly the direction needed for the deduction. The numerical code has always used the final inequality in the correct direction. The lemma text has been corrected and its supplement step expanded.

The n=29 and n=30 candidate statuses are therefore unchanged. Independent mathematical review remains open.

## 1. Selected-edge injection

For each missing **unordered** pair `{u,w}` in `H[B]`, exactly one cross quasi-edge is designated selected, after orienting the pair if necessary. A selected edge recovers its source and its unique exceptional B-vertex, so two different missing unordered pairs cannot select the same cross-edge and the two orientations of one unordered pair cannot both be designated selected.

Fresh verdict: survives.

This convention is stated explicitly in the current n=25, n=27, n=28, n=29 and n=30 reviewer proofs.

## 2. Forced selected/residual separation

For a selected edge `ui->w` and an F-neighbour `j` of `i`, the usual forced cross-edge cannot silently be another selected representative when both endpoints miss an A-vertex. A selected representative of a missing B-pair has its unique exception in B and must dominate every A-vertex. This prevents the residual family from colliding with the selected family in the key injections.

Fresh verdict: survives.

The same mechanism appears explicitly in the n=25, n=27 and n=28 reviewer proofs and in the n=29 standalone bridge; n=30 imports the common bridge.

## 3. Residual activity

Assume a B-source `u` has `rho_u=0`. Split A into its selected neighbourhood `U` and complement `T`. There is no F-edge between U and T. Internal F-edges of U force two distinct residual cross-edges; F-edges of T force distinct residual cross-edges with A-endpoint in T. The families are disjoint. Thus

```text
r >= 2 e(F[U]) + e(F[T]) >= e(F)=r+t,
```

contradicting `t>0`.

Fresh collision audit: survives.

This is a genuinely cross-order lemma. It is written explicitly in the current n=25, n=27 and n=28 proofs, rederived for n=29, and used parametrically at n=30.

## 4. Source-demand and charging inequalities

For selected `ui->w`, every F-neighbour of `i` either uses one residual slot at source u or injects into a distinct residual slot at label i. Hence

```text
d_i <= rho_u+R_i,
s_i=max(0,d_i-R_i) <= rho_u.
```

Choosing `s_i` selected incidences per label and charging source u by

```text
(rho_u-1)/(a-rho_u)
```

per chosen incidence gives

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i),
```

and therefore the standard demand inequality.

Fresh verdict: survives. Denominators are safe because any selected source has `q_u>=1`, hence `rho_u<=a-1`.

## 5. Threshold-capacity lemma — correction and re-proof

Define

```text
I_h={i:s_i>=h},
W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h},
z_h=|Z_h|.
```

Let `ell_u` be the number of actual heavy selected incidences from u and `J={u in Z_h:ell_u>h}`, `j=|J|`.

For `u in J` and a heavy selected edge `ui->w`, the other `ell_u-1>=h` heavy selected labels at u all force cross-edges to w. If none is selected from w, all are residual and `rho_w>=h`; if one is selected from w, its heavy label has demand at least h and the source-demand implication gives `rho_w>=h`. Thus every supplement of a heavy arc from J also lies in `Z_h`.

Injectivity on unordered B-pairs then gives

```text
W_h <= (z_h-j)h + j z_h - j(j+1)/2.       (1)
```

Put `q=z_h-h`. The earlier text accidentally described the following difference in the reverse order. The correct identity is

```text
[h z_h + C(q,2)] - RHS(1)
  = (q-j)(q-j-1)/2
  >= 0
```

for every integer `q-j`. Therefore

```text
W_h <= h z_h + C(z_h-h,2),
```

or equivalently

```text
2W_h <= z_h^2-z_h+h(h+1).
```

So the typo was in the explanatory sign, not in the claimed threshold inequality. In fact the corrected sign is precisely what makes the implication immediate.

**Impact:** no certificate or numerical frontier changes. `minimal_prepare.py` and the n=30 threshold screens use the final inequality in the correct direction. Candidate status unchanged.

## 6. Isolated-C exclusion

If x is isolated in `C=H[A]`, missing H-pairs inside `A\{x}` force a distinct residual family P with B auxiliaries. Every B-endpoint used by P supplies a further residual edge at x outside P; every unused B-endpoint supplies a residual edge by residual activity. Hence

```text
r >= |P|+b
```

and the exact ledger gives

```text
b <= a-1-t.
```

Fresh collision audit: survives.

Consequences used at the two most relevant orders remain:

```text
n=29, Delta=16, (a,b)=(12,16), t=2 or 3:
    delta(C)>=1, d_F<=10, r<=60-t.

n=30, Delta=16, (a,b)=(13,16), t=1 or 2:
    delta(C)>=1, d_F<=11, r<=70 or 69.
```

This remains one of the highest-value hand lemmas for independent human review.

## 7. Minimal n=29 kernel and exact certificates

The preferred n=29 Delta=16 route remains the minimal trusted kernel, not the historical projected/joint/typed stack.

Its committed report records:

```text
m=211 (t=3): 72 retained demands, 126 residual rows, 126 exact rejections, 0 survivors.
m=210 (t=2): 367 retained demands, 1467 residual rows, 1467 exact rejections, 0 survivors.
```

The late model is the corrected v2 cumulative-threshold/source-q-flow relaxation. The historical v1 normalization bug remains quarantined and is not proof evidence.

The Farkas verifier accepts a contradiction only after exact integer recombination: inequality multipliers are nonnegative, equality multipliers may be signed, the resulting variable coefficients are nonnegative, and the combined right-hand side is strictly negative. Numerical LP status is only a proposal mechanism.

Fresh code/semantics verdict: no new blocking defect found.

## 8. Cross-order impact ledger

- **n=25:** shares the unordered-pair selection convention, forced-residual separation, residual activity, and small-k/isolated-C style injection. No status change from this pass.
- **n=27:** shares the same structural bridge and residual activity, with its own finite column machinery. No status change.
- **n=28:** current reviewer proof states the selected-edge constraints and residual-activity lemma explicitly and has its own isolated-C reduction and direct197/equality computations. No status change.
- **n=29:** threshold-capacity proof text corrected as above; final inequality and minimal-kernel computation unchanged. No status change.
- **n=30:** directly imports the threshold-capacity and parameterized isolated-C machinery. The corrected threshold derivation therefore strengthens its reviewer traceability without changing any n=30 numerical result. No status change.

## 9. Review priorities after this pass

The highest-value external attacks remain:

1. the complement/quasi-edge construction and one-representative-per-unordered-pair convention;
2. collision-freeness in residual activity and selected-source demand;
3. the threshold-capacity lemma, now with its supplement dichotomy and algebra written out;
4. the isolated-C injection;
5. graph-to-relaxation normalization in the corrected cumulative-threshold model;
6. exact Farkas semantics and independent replay.

A genuine counterexample to any universal graph-to-model lemma overrides every green downstream computation. This report therefore preserves candidate, not theorem, status.
