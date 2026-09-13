# N34 state 122 — whole-state exclusion

13 September 2026. **Candidate exact finite exclusion using the endpoint class-packing lemma; external mathematical review and independent reproduction remain OPEN.**

The conclusion is a whole scalar-state exclusion:

```text
N34 state 122 has no selected/residual realization satisfying the canonical bridge.
```

This is the eighth quantified whole-state exclusion in the alternative-geometry programme.

## State data

```text
a=15, b=18, t=1,
s=2^6,3^9,
rho=1^7,2^3,3^8,
r=37,
S=39.
```

Put `e_i=x_i-s_i>=0`, `E=sum e_i`, and `Q=S+E=39+E`.

The basic incoming caps are 3 on each rho-one source, 4 on each rho-two source and 5 on each rho-three source. Hence

```text
Q=sum p_u <= 7*3+3*4+8*5=73,
39+E<=73,
E<=34.                                                (1)
```

So it suffices to exclude `E=0,...,34`.

## Earlier extension scan

GitHub Actions run `34780310971` used the audited low-demand extension scanner. It was strict on every layer except `E=0`; that sole layer had gap `-3`. Its minimizing branch had all labels at exact demand and exposed the missing issue: the old endpoint-order relaxation allowed many exact-demand labels to reuse the same cheapest eligible source pair/triple independently.

## Endpoint class packing

[`ENDPOINT_CLASS_PACKING.md`](ENDPOINT_CLASS_PACKING.md) retains the competition between labels for low-load sources. For a class of `z` labels of selected degree `x`, define

```text
A_lambda={u:q_u+p_u<lambda and u is compatible with the class}.
```

If `k` labels had endpoint load `C_i<lambda`, their `xk` selected incidences would all have to originate in `A_lambda`. Because the selected incidence graph is simple, a source `u` can meet at most one edge of each of those `k` labels and at most `q_u` edges overall. Thus necessarily

```text
x k <= sum_(u in A_lambda) min(q_u,k).                (2)
```

This yields a lower bound on the number of class labels with `C_i>=lambda`, and summing over thresholds yields a lower bound on the class's total endpoint mass. For zero-excess demand-`d` labels, compatibility also requires `rho_u>=d`, `q_u>0`, and `p_u<=rho_u-1`.

The class-packing fallback enumerates the incoming `p` allocation under the same pointwise source caps as the audited scanner. It may relax other constraints, so its minimum is conservative. Zero-q sources are filled first because they have zero `q p` cost and cannot serve positive-demand selected labels; this is an exchange argument, not an extra graph assumption.

## Full exact verification

Workflow `verify-class-packing-closures.yml`, run `34782832374`, head `04544934050e376ae6e6a6af73dce5d73898d9e9`, regenerated the scanner with

```text
BASE_SHA256      c8e97519de066781256f83cf9dac71f79bcadd1b72880cd2c510272aeda18514
GENERATED_SHA256 474c4758ca2fa975c1e8a86caac4834de347fc282ce1c1f005c0315e04bbaac7
```

and independently replayed all `E=0,...,34` layers. The result was

```text
CLASS_PACKING_SUMMARY state=122 min_gap=1 nonpositive_count=0 nonpositive=[]
```

The complete gap vector is preserved in [`STATE_122_CLASS_PACKING_GAPS.tsv`](STATE_122_CLASS_PACKING_GAPS.tsv). The GitHub Actions artifact was `10325940362`, digest

```text
sha256:de4e9dfda97644a80f01ec906188eedc20a284905925699bac5dbb6e66049c87
```

The minimum gap is +1 and every layer is strict. Together with (1), this excludes the entire state.

## Trust boundary

The finite arithmetic is exact and no timeout, floating infeasibility status or heuristic solver claim is used as proof. The endpoint class-packing inequality itself is elementary bipartite counting. Its application depends on the canonical bridge, especially selected-edge forcing, selected-excess, endpoint load, the exact incoming/selected ledger and `sum_i C_i=r+Q`. Independent computational reproduction and external checking of those structural implications remain open.
