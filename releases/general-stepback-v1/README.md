# General-theory step-back reviewer package v1

12 September 2026.

This package collects the structural results extracted after the fixed-order candidate frontier reached `n=33`.

**Status:** AI-assisted candidate mathematics. Independent specialist review, novelty assessment and independent computational reproduction remain OPEN. These results do **not** prove the unrestricted Murty-Simon conjecture.

## Main results

### 1. Balanced-degree branch theorem

For every D2C graph on `n>=7` vertices with

```text
Delta = ceil(n/2),
```

the Murty-Simon bound holds, with equality only for the balanced complete bipartite graph. Consequently any genuine counterexample must satisfy

```text
Delta >= ceil(n/2)+1.
```

- [Theorem](../../project/research/general_n/2026-09-12-balanced-degree-v1/BALANCED_DEGREE_THEOREM.md)
- [Witness-capacity hardening](../../project/research/general_n/2026-09-12-balanced-degree-v1/WITNESS_CAPACITY_HARDENING.md)
- [Exact algebra regression](../../project/research/general_n/2026-09-12-balanced-degree-v1/check_balanced_degree.py)

### 2. Fourteen-label high-b surplus theorem

In canonical bridge variables with `a=14`, `b=Delta` and `t=e-15b`:

```text
b>=17  =>  t<=1,
b>=20  =>  t<=0.
```

Thus for the infinite family `n>=35`, `Delta=n-15`,

```text
e(G) <= 15 Delta.
```

- [Theorem](../../project/research/general_n/2026-09-12-a14-high-b-v1/A14_HIGH_B_SURPLUS_THEOREM.md)
- [Exact new-boundary verifier](../../project/research/general_n/2026-09-12-a14-high-b-v1/check_a14_high_b.py)
- Prior boundary evidence is preserved in the N32/N33 packages cited by the theorem.

### 3. Fifteen-label tail theorem

```text
Q<=26,
```

with equality exactly `3^2 4^13` and `4^15`.

- [Theorem](../../project/research/general_n/2026-09-12-fifteen-label-tail-v1/FIFTEEN_LABEL_TAIL.md)
- [Proof-critical exact checker](../../project/research/general_n/2026-09-12-fifteen-label-tail-v1/check_fifteen_label_tail.py)
- [Independent exhaustive 77,558,760-profile regression](../../project/research/general_n/2026-09-12-fifteen-label-tail-v1/check_fifteen_label_full.cpp)

Graph transfer: every positive-surplus bridge image with `a=15` satisfies

```text
b+2t <= 26.
```

### 4. Sixteen-label tail theorem

```text
Q<=29,
```

with equality exactly `4^16` and `5^16`.

- [Theorem](../../project/research/general_n/2026-09-12-sixteen-label-tail-v1/SIXTEEN_LABEL_TAIL.md)
- [Exact checker](../../project/research/general_n/2026-09-12-sixteen-label-tail-v1/check_sixteen_label_tail.py)

Graph transfer: every positive-surplus bridge image with `a=16` satisfies

```text
b+2t <= 29.
```

## Internal hostile audit

- [General-theory hostile audit](../../project/reviews/general-theory/2026-09-12-stepback-v1/HOSTILE_AUDIT.md)

Verdict: **no blocking flaw found**, but this is same-assistant internal review, not independent validation.

The audit also records the methodological boundary: the original safe-interval clipping mechanism needs joint compatibility repair from `a=17`, and genuine `6->5` clipping counterexamples appear by `a=23`. No uniform all-a tail theorem is claimed.

## Highest-value external review targets

1. the order-independent witness-capacity injection;
2. the published dominating-edge input used by the balanced-degree theorem;
3. the canonical selected/residual bridge;
4. threshold capacity and its equality case;
5. the common potential-certificate semantics in the `a=14` family;
6. the finite clipping/terminal tables in the 15-/16-label theorems.
