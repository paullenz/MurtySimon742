# N34 state 154 — whole-state exclusion

13 September 2026. **Candidate exact finite exclusion using the endpoint class-packing lemma; external mathematical review and independent reproduction remain OPEN.**

The conclusion is a whole scalar-state exclusion:

```text
N34 state 154 has no selected/residual realization satisfying the canonical bridge.
```

This is the tenth quantified whole-state exclusion in the alternative-geometry programme.

## State data

```text
a=15, b=18, t=1,
s=2^5,3^10,
rho=1^6,2^4,3^8,
r=38,
S=40.
```

With `Q=40+E`, the basic incoming cap is

```text
Q=sum p_u <= 6*3+4*4+8*5=74,
40+E<=74,
E<=34.                                                (1)
```

## Old scan and residual layers

The original low-demand extension matrix, run `34780310971`, was already strict on 32 of the 35 possible excess layers. Only

```text
E=0  gap=-1,
E=6  gap=-1,
E=7  gap=-3
```

remained nonpositive.

## Class-packing replay

The same exact p-allocation / endpoint class-packing fallback used for states 122 and 283 was applied without state-specific mathematical modifications. Workflow `test-class-packing-state154.yml`, run `34782876163`, head `a7886530f5f0f855573f63711267f554a2392aa0`, used

```text
BASE_SHA256      c8e97519de066781256f83cf9dac71f79bcadd1b72880cd2c510272aeda18514
GENERATED_SHA256 474c4758ca2fa975c1e8a86caac4834de347fc282ce1c1f005c0315e04bbaac7
```

and obtained

```text
E=0  gap=+1,
E=6  gap=+1,
E=7  gap=+1.
```

The exact comparison is preserved in [`STATE_154_CLASS_PACKING_RESIDUALS.tsv`](STATE_154_CLASS_PACKING_RESIDUALS.tsv).

The minimizing source vectors after strengthening were

```text
E=0: q2=0,0,1,2; q3=4,4,4,5,5,5,5,5
E=6: q2=0,1,1,1; q3=2,5,6,6,6,6,6,6
E=7: q2=0,0,2,2; q3=3,3,6,6,6,6,6,7
```

Thus all formerly weak layers are now strict. The unchanged old scanner had already excluded every other `E<=34`, and the class-packing fallback only strengthens nonpositive branches rather than replacing positive conclusions. Equation (1) excludes `E>=35`. Hence the whole state is excluded.

## General-theory significance

State 154 is important because it was not used to design the endpoint class-packing lemma. It is the first immediate out-of-sample propagation test after states 122 and 283: three unrelated residual layers all close at +1 under the same general strengthening. This is evidence that the mechanism is family-level rather than a bespoke repair, while not by itself establishing a universal theorem.

## Trust boundary

The residual computations are exact integer enumerations. The class-packing lemma itself is finite bipartite counting. Its use here depends on the canonical bridge and remains subject to external structural review and independent computational reproduction.
