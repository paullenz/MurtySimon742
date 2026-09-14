# Murty q-tail Hall conjecture — narrowed after red-team failures

14 September 2026. **Research conjecture / proof target only. NOT a promoted theorem.**

## 1. Surviving empirical phenomenon

For an integer `t>=1`, define the complete high-demand source tail

```text
S_t={u:q_u>=t}.
```

Let

```text
F(S)=H(S)-D(S)
```

be the exact directed target-Hall margin with the current post-pair target capacities.

On the frozen Murty pilot, every difficult exact target-Hall failure found so far has a deficient high-q tail. In particular, the 812 failures missed by the global receiver-layer relaxation are all detected by this one-parameter family:

```text
812 difficult profiles tested,
812 profiles with a deficient high-q tail,
0 misses.
```

The first deficient threshold is distributed as

```text
t=2 : 426
t=3 : 191
t=4 : 195.
```

The maximum-deficiency tail uses

```text
t=2 : 220
t=3 : 170
t=4 : 422.
```

This is strong reconnaissance, but the natural abstract conjecture turned out to be false under weaker hypotheses.

## 2. Exact tail formula

For a target `w`, incoming from `S_t` is

```text
y_w(t)
 = #{u != w :
       t<=q_u<=c_w+1,
       q_w<=c_u}.
```

With

```text
R(t,x;q)=#{u:t<=q_u<=x and c_u>=q},
```

we have

```text
y_w(t)=R(t,c_w+1;q_w)-1_{q_w>=t}.
```

Hence

```text
F_t
 = sum_w min(P_w,
             R(t,c_w+1;q_w)-1_{q_w>=t})
   - sum_{u:q_u>=t}q_u.
```

So if a ledger-current Murty theorem reducing the minimum to high-q tails is eventually proved, its proof-critical inequalities will be explicit histogram inequalities rather than max-flow statements.

## 3. First hostile boundary — arbitrary monotone capacities

Tail sufficiency is false for arbitrary fixed-q-monotone target capacities, even when several Murty-looking pointwise caps are respected.

Take `a=4`, `b=7` and seven labelled copies with `(q,c,P)`

```text
(0,2,2),
(1,2,1),
(3,4,3),
(3,4,3),
(1,2,1),
(3,4,3),
(2,3,0).
```

Here `rho=c-q>=1`, `c<=a`, the capacities are fixed-q monotone, and the listed `P` values respect the residual, simple-degree and potential-pair upper caps. Nevertheless the exact Hall minimum is `-1` on a non-tail source set, while every high-q tail has margin at least zero.

Therefore no proof may rely only on directed compatibility plus monotone target capacities or those three cap families.

## 4. Second hostile boundary — the current cap formula alone

A bookkeeping correction materially changed the finite red-team. In the selected-excess cap,

```text
z = #{i:s_i=0}
```

is the number of zero-demand labels. It is **not** constrained by `z<=E`. The correct implementation is

```text
k*=min(z,min(q,E)).
```

After restoring the correct quantifier range for `z`, the current deterministic post-pair cap formula itself admits a tail counterexample if the `A`-side demand ledger is not enforced.

One example has

```text
a=4,
b=7,
(q,rho)=(1,1) once,
(q,rho)=(3,1) six times,
E=5,
z=2.
```

The current cap formula gives `P=3` on all seven targets. The exact Hall minimum is `-1`, while every high-q tail has margin at least zero.

However, this profile is not compatible with a legal selected-demand system: `Q=19`, so `S=Q-E=14`; with two zero-demand labels the remaining positive labels would have to carry total demand 14, whereas selected-edge forcing requires every selected positive-demand label incident to these `rho=1` sources to have `s_i<=1`.

Thus the cap formula by itself is not the missing theorem. The source-demand coupling matters.

## 5. Third hostile boundary — selected-incidence feasibility is still insufficient

Even adding the exact selection-free source-label incidence feasibility condition is not enough if the global scalar state identities are omitted.

Take again

```text
a=4,
b=7,
(q,rho)=(1,1) once,
(q,rho)=(3,1) six times,
s=(0,0,0,0),
E=19,
z=4.
```

All selected labels have zero demand, so the source-label lower-bound circulation is feasible. The current cap formula again gives `P=3` throughout. The exact Hall minimum is `-1` on the singleton `q=1` source, while every high-q tail is nondeficient.

Therefore the implication

```text
current cap formula
+ selected-incidence feasibility
=> high-q-tail Hall sufficiency
```

is **false**.

This negative result is now a standing red-team obligation.

## 6. What survives on the actual frozen Murty states

The frozen N34/N35-derived scalar states satisfy additional global ledger identities inherited from the canonical graph-to-constraint bridge and the fixed-order state construction. Those identities are not present in the hostile profiles above.

The live proof target is therefore deliberately narrower:

> **Ledger-current q-tail question.** On scalar profiles satisfying the **full canonical Murty bridge and the actual frozen-state global ledger identities**, is every negative target-Hall minimum attained by a high-q tail `S_t`?

This is presently a question, not a theorem. Its exact hypotheses must be recovered from the original state-generation identities before further promotion.

## 7. Corrected finite-evidence status

Earlier broad random and small exhaustive tests of the cap formula found no tail discrepancy, but some exploratory runs incorrectly restricted the zero-demand parameter by `z<=E`. Those runs are therefore **not accepted as evidence for the narrowed conjecture**.

After enforcing demand-consistent `z` and selected-incidence feasibility, exhaustive small tests still showed no discrepancy through several low orders before the all-zero-demand `a=4,b=7` counterexample in Section 5 appeared. This is useful boundary information: the failure requires a branch absent from the observed frozen frontier, but the reason must be proved from the global ledger rather than guessed.

The robust empirical fact that remains fully valid is the frozen 812-profile statement in Section 1.

## 8. Relation to the exact q-layer reduction

[`Q_LAYER_THRESHOLD_NORMAL_FORM.md`](Q_LAYER_THRESHOLD_NORMAL_FORM.md) remains exact. It gives, for arbitrary `S`,

```text
U_q(S)
 = sum_q sum_k
     min(
       T_q(theta_{q,k}),
       T^O_q(r_{q,k}-1;S)
       +T^S_q(r_{q,k+1}-1;S)
     ).
```

Together with [`Q_STRATIFIED_MINCUT_EXACTNESS.md`](Q_STRATIFIED_MINCUT_EXACTNESS.md), the exact target-Hall minimum is already reduced to threshold histogram data without assuming any q-tail theorem.

Accordingly the project does **not** depend on the tail conjecture. If the narrowed ledger-current tail theorem fails, the q-layer threshold normal form remains the preferred exact all-order route.

## 9. Immediate research task

Before any further q-tail promotion:

1. recover the exact global identities defining the frozen scalar states, especially the relation among `sum s`, `sum rho`, `a`, `b`, fixed-order edge count and surplus;
2. add those identities to the hostile finite generator;
3. rerun the tail-minimum red-team under the **full** bridge domain;
4. only then attempt an uncrossing proof for high-q tails.

Any proof which does not exclude the counterexamples in Sections 3-5 by an explicitly stated hypothesis is incomplete.

## Trust boundary

High-q-tail sufficiency is unproved and false under several natural weakenings. The only theorem-safe statements here are the exact tail-margin formula and the reported frozen-pilot computations. The unrestricted Murty-Simon conjecture remains unproved.
