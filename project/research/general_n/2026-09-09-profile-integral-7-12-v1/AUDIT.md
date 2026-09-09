# Hostile audit — profile-integral 7/12 strengthening

9 September 2026.

**Current status: audit in progress. Do not promote the 7/12 implication until both exact workflows are green and the checks below have been reconciled.**

## Claim under audit

The proposed strengthening is

```text
t < 5a^2/128 + a/8,
```

and consequently

```text
n>=6 and Delta(G)>=(7/12)n  ==>  e(G)<floor(n^2/4).
```

The graph-to-demand, threshold-capacity and shifted-midpoint ingredients are inherited unchanged from the earlier 293/500 candidate. The new attack surface is therefore concentrated in the scalar `5/64` estimate and the new degree assembly.

## Scalar red-team checklist

1. **Domain shrink:** verify that `u=y^2/(2x)` really satisfies `u<=1/2`. Since the profile integral has `0<=y<=x<=1`, indeed `u<=x/2<=1/2`. This is essential; the new cubic minorant is not asserted on `[0,1]`.
2. **Minorant sign:** verify `B(u)>=0` before taking square roots. `B` is decreasing and `B(1/2)=181/256>0`.
3. **Square gap:** exact expansion must give

   ```text
   1-u-B(u)^2 = u^3(64-112u-24u^2-9u^3)/1024.
   ```

   The cubic factor is decreasing and equals `7/8` at `u=1/2`.
4. **Integrated coefficients:** independently recheck `x^2/12`, `x^3/160`, `3x^4/1792`.
5. **q substitution:** independently recheck

   ```text
   P(q)=2q^2-4q^3+(2/3)q^5+(1/10)q^7+(3/56)q^9.
   ```
6. **Three interval cover:** `[0,1/3]`, `[1/3,7/20]`, `[7/20,1/sqrt(2)]` cover the full domain with no gap.
7. **Low interval:** `P'>=0` follows because `Q>=4-12q>=0`.
8. **Middle interval:** the base `2q^2-4q^3` decreases, the positive tail increases, and the exact rational tail at `7/20` is below `1/250`.
9. **High interval:** `Q'<=-365/64<0` on the entire interval and `Q(7/20)<0`, hence `P` decreases.
10. **Strictness:** the middle rational margin `11/216000` is strictly positive, so the resulting surplus bound is strict.

## Profile-integral inheritance checklist

1. Recheck that the Cauchy--Schwarz direction in the pointwise threshold estimate is unchanged.
2. Recheck the indispensable lower bound `z_h>=H0>=h`.
3. Recheck the nested budget `sum_h z_h<=r`.
4. Recheck the shifted-midpoint inequality and the endpoint loss `<=a/4`.
5. Confirm `s_i/a in [0,1]` including `s_i=0`.

Any failure here affects the previous 293/500 candidate as well and overrides this strengthening.

## Degree-assembly red-team checklist

1. From `b>=7n/12` and `n=a+b+1`, verify `5b>=7(a+1)` and `(b-a-1)/2 >= (a+1)/5`.
2. Verify the parity identity

   ```text
   floor(n^2/4)-b(n-b)=floor((b-a-1)^2/4).
   ```
3. Verify the floor loss is at most `1/4`.
4. Large-a difference:

   ```text
   D(a)=(a+1)^2/25-1/4-5a^2/128-a/8.
   ```

   Check coefficient `3/3200`, `D(53)=123/3200`, and first forward difference `177/3200`.
5. For `2<=a<=52`, verify the least eligible degree is `ceil(7(a+1)/5)` and required surplus is nondecreasing thereafter.
6. Reconstruct the direct-bound exception list from scratch. Expected:

   ```text
   4,6,9,11,14,19,24,29,34,39,44.
   ```
7. For each exception, rederive the `K_h,w_h,L_h` threshold certificate and verify its maximum `S-r` upper bound is strictly below `2T0`.
8. Check `a=0` star and `a=1` edgeless-F cases separately.

## Independence / evidence policy

`src/check_7_12.py` and `src/audit_7_12_independent.py` share no code. They intentionally use different data flow and least-threshold implementations. Both remain same-assistant implementations and therefore are **not external independent reproduction**.

A green finite checker cannot validate the graph-to-demand bridge by itself. Promotion requires preserving both reports, documenting any discrepancy, and then building a reviewer manuscript/verification companion under the repository review-readiness policy.
