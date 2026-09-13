# N34 state 283 — whole-state exclusion

13 September 2026. **Candidate exact finite exclusion using the endpoint class-packing lemma; external mathematical review and independent reproduction remain OPEN.**

The conclusion is a whole scalar-state exclusion:

```text
N34 state 283 has no selected/residual realization satisfying the canonical bridge.
```

This is the ninth quantified whole-state exclusion in the alternative-geometry programme.

## State data

```text
a=15, b=18, t=1,
s=2^3,3^12,
rho=1^5,2^4,3^9,
r=40,
S=42.
```

With `E=sum_i(x_i-s_i)` and `Q=42+E`, basic incoming capacity gives

```text
Q=sum p_u <= 5*3+4*4+9*5=76,
42+E<=76,
E<=34.                                                (1)
```

## Earlier extension scan

Run `34780310971` was strict on every `E=0,...,34` layer except `E=7`, where the gap was `-2`. A reporting-only replay isolated the extremal excess profile

```text
e_(demand 2)=(0,0,7),
e_(demand 3)=0^12,
q_(rho=2)=1,1,1,1,
q_(rho=3)=5^9.
```

Thus only one label carried positive excess while twelve demand-three labels were exact-demand. The old individual endpoint-order relaxation treated those twelve labels independently and therefore failed to retain their competition for the same nine rho-three sources.

## Class-packing correction

[`ENDPOINT_CLASS_PACKING.md`](ENDPOINT_CLASS_PACKING.md) replaces repeated individual endpoint minima with the threshold capacity inequality

```text
x k <= sum_(u in A_lambda) min(q_u,k),                (2)
```

for any `k` labels that would all have endpoint load below `lambda`. This keeps both row degree and the one-edge-per-source-per-label condition. For zero-excess demand-three labels the eligible set additionally requires `rho_u>=3`, `q_u>0` and `p_u<=2`.

In the original `q_3=5^9` witness every rho-three source has five selected incidences but there is only one positive-excess label, so every such source must meet exact-demand labels and is correspondingly forced into the low-p regime. Class packing converts that qualitative rigidity into an aggregate endpoint-mass lower bound.

## Full exact verification

Workflow `verify-class-packing-closures.yml`, run `34782832374`, head `04544934050e376ae6e6a6af73dce5d73898d9e9`, used the generated scanner hashes

```text
BASE_SHA256      c8e97519de066781256f83cf9dac71f79bcadd1b72880cd2c510272aeda18514
GENERATED_SHA256 474c4758ca2fa975c1e8a86caac4834de347fc282ce1c1f005c0315e04bbaac7
```

and replayed every `E=0,...,34` layer. Result:

```text
CLASS_PACKING_SUMMARY state=283 min_gap=1 nonpositive_count=0 nonpositive=[]
```

The complete gap vector is preserved in [`STATE_283_CLASS_PACKING_GAPS.tsv`](STATE_283_CLASS_PACKING_GAPS.tsv). The Actions artifact was `10325840615`, digest

```text
sha256:5580b59d6e4bbfdb8a40ac42c8030b7f90a7ea886268e2361d1d9ea6debcb3d2
```

Every layer is strict, with weakest gap +1. Equation (1) excludes all larger `E`, hence the entire state is excluded.

## Trust boundary

The computation is exact integer enumeration. The class-packing lemma is elementary finite bipartite counting, but its Murty–Simon application inherits the canonical-bridge obligations: selected-edge forcing, selected-excess, endpoint load, exact degree ledgers and endpoint-sum identity. External review and independent reproduction remain open.
