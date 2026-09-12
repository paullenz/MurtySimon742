# Hostile internal audit — N32 reviewer-v1

12 September 2026. Same-assistant hostile audit. **This is not independent external mathematical review.**

## Verdict

**NO BLOCKING FLAW FOUND in the assembled N32 candidate route.**

The proof remains conditional on the universal selected/residual bridge and on the correctness of the exact finite necessary-condition replays. Those are the highest-value external review targets.

## 1. Coverage audit

At `m>=256`, average degree gives `Delta>=16`. The proof covers every possible maximum degree:

- `Delta=16`: handshaking gives `m<=256`; equality is treated separately.
- `Delta=17`: all levels `m>=256` are covered (`>=259` scalar, 258 hand, 257 exact/hand, 256 exact/hand).
- `Delta=18`: thirteen-label bound gives an immediate contradiction in the target range.
- `19<=Delta<=30`: twelve-label source-independent theorem bounds the graph below 256.
- `Delta=31`: universal-vertex D2C graph is a star.

No maximum-degree branch is missing.

## 2. Delta=17 parameter arithmetic

For `Delta=17`, `(a,b)=(14,17)` and the benchmark is `17*15=255`, so:

```text
m=256 -> t=1,
m=257 -> t=2,
m=258 -> t=3,
m>=259 -> t>=4.
```

The bridge lower bound `Q>=b+2t` therefore gives respectively `19,21,23,>=25`, consistent with the fourteen-label hand upper bound `Q<=23`.

## 3. dmax=12 dependency

The finite `Delta=17` models use `d_i<=12`. This is valid uniformly for every positive `t` in the N32 branch, not only for zero-demand rows.

The isolated-C lemma is parameteric: if `C` has an isolated vertex then

```text
b <= a-1-t.
```

Here `a=14`, `b=17`, and `t>=1`, so the right side is at most 12. Contradiction. Hence `delta(C)>=1`, and because `F` is the complement of `C` on 14 vertices,

```text
d_i<=12.
```

The first draft of the assembled proof stated this explicitly only in the zero-demand subsection. That is a **documentation hardening point, not a mathematical defect**; reviewer-v1 should be read with this uniform dependency in mind, and it should be made explicit in the next text revision.

## 4. t=1 frontier completeness

An independent C++ recursion enumerates exactly

```text
C(27,14)=20,058,300
```

nondecreasing fourteen-demand multisets in `{0,...,13}` and reproduces the complete score histogram above the required threshold:

```text
Q19=206, Q20=104, Q21=50, Q22=18, Q23=3.
```

No `Q>23` vector occurs.

Residual tail counts must be nonincreasing. Taking the monotone closure of the lower bounds `gamma_h(W_h)` is necessary. It exposes one arithmetic impossibility `3^11,5^3`, because `z_5=5` forces `z_4>=5`, raising `r_min` to 47 while `S-2=46`.

Starting from the monotone-minimal residual degree multiset and distributing every allowed unit of total tail slack by single degree increments is complete for residual-degree **multisets**: raising a residual degree by one raises exactly one tail count, and every dominating tail vector can be obtained by such increments. Duplicate sorting changes representation only, not coverage.

The resulting 1,984 positive and 61 zero-demand states deliberately form a superset of graph images. Over-enumeration is safe for an exclusion proof.

## 5. Positive-demand exactness

The first-stage lifted potential does not use numerical infeasibility as acceptance. For every one of its 1,369 excluded states, the proposed scalar envelope is rounded and repaired, then all local envelope inequalities and the final strict gap are checked in integer arithmetic. A fresh preservation replay reproduced all 1,369 at denominator 10,000 with zero failures.

The 615 survivors enter the generic full RX/Hall model. The model is a necessary-condition relaxation: omitted graph constraints can create false survivors but cannot create false exclusions, provided every retained inequality is valid.

The exact Farkas layer adds explicit unit-density bounds and accepts only when the integer coefficient combination has every variable coefficient nonnegative and strictly negative right-hand side. This is the same semantics previously audited in the N29/N30 RX-Hall programme.

The completed session ledger was 614 exact rejects plus one primal survivor, zero unresolved. The preservation implementation was spot-checked after packaging on the first 30 states and reproduced 29 exact certificates plus the same unique survivor. The committed shard replay regenerates the full ledger; saved floating duals are not premises.

## 6. Hand survivor audit

For

```text
s=1^2,2^12,
rho=1^10,2^7,
```

one has `W_2=24` and `z_2=7`, while `C_2(7)=24`. Therefore **both** inequalities in the threshold-capacity chain are equalities:

```text
W_2 <= sum ell_u <= capacity <= 24.
```

This point is essential: it forces the total number of actual heavy incidences to be exactly 24, not merely the chosen demand incidences. Hence every demand-two label has actual selected degree exactly two, and equality in the source decomposition makes every high source heavy-active.

The equality-gap formula forces `j=4` or `5`; high-source heavy arcs therefore send at least 18 supplements into the seven-source high set. Endpoint load plus `d_i=R_i+2`, `x_i=2`, and source forcing at a high source gives `p_u<=1`. Thus the contradiction `18<=sum p_u<=7` is valid.

No solver claim is used in this final state.

## 7. Zero-demand model audit

The positive-demand identity `d=R+s` is correctly *not* used when `s=0`. The strengthened model retains `(d,R,x)` and enforces exactly

```text
s=max(0,d-R),
sum R=r,
sum d=2(r+t).
```

Its selected-incidence constraints `s<=rho`, `d<=rho+q-1`, and `R+x>=q+p` are direct necessary consequences of the bridge. Omitting stronger pointwise conditions would only weaken the model and is therefore safe for exclusion.

The cap `d<=12` is justified by the isolated-C lemma as in Section 3. The completed session ledger rejects all 61 states by exact integer Farkas certificates.

## 8. Delta=16 equality audit

With `Delta=16`, handshaking immediately gives `m<=256`. Equality makes the graph 16-regular.

At 256 edges a non-bipartite graph with a dominating edge is excluded by the published dominating-edge theorem, so the relevant non-bipartite graph has no dominating edge. The witness lemma used already at N29/N31 gives `d(x)+d(y)<=n-1=31` for every direct/two-step witness pair. Every critical edge has such a witness. A 16-regular graph would give degree sum 32, contradiction.

Thus equality is bipartite; diameter two makes it complete bipartite, and 32 vertices/256 edges force `K(16,16)`.

## 9. Main remaining risks / external review priorities

1. **Universal bridge correctness.** Recheck selection on one representative per missing unordered B-pair, residual activity, source forcing, endpoint load, and threshold capacity from the graph definitions.
2. **Threshold-capacity equality case.** The N32 hand survivor depends on equality throughout that chain, not merely on the final numerical bound.
3. **Finite-domain completeness.** Independently reproduce the monotone tail closure and residual multiset expansion.
4. **Zero-demand finite model.** Independently derive the `(d,R,x)` state space and exact degree-mass identity.
5. **Exact replay.** Run the committed sharded replay in a clean environment and compare aggregate counts. This is implementation reproduction, not a substitute for items 1-4.
6. **Literature/novelty.** No claim of novelty or publication priority should be made without specialist literature review.

## 10. Bottom line

The audit found no missing maximum-degree case, no accepted floating infeasibility, no obvious sign reversal, and no contradiction between the finite ledgers and the hand assembly.

**Candidate status is justified internally; external validation remains open.**
