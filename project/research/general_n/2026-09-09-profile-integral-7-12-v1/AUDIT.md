# Hostile audit — profile-integral 7/12 strengthening

9 September 2026.

**Current status: internal hostile audit PASS for the new scalar and degree-assembly layers. Candidate theorem promoted for reviewer packaging; independent mathematical review, novelty assessment and external computational reproduction remain OPEN.**

## Claim under audit

The strengthening is

```text
t < 5a^2/128 + a/8,
```

and consequently

```text
n>=6 and Delta(G)>=(7/12)n  ==>  e(G)<floor(n^2/4).
```

The graph-to-demand, threshold-capacity and shifted-midpoint ingredients are inherited unchanged from the earlier 293/500 candidate. The new attack surface is therefore concentrated in the scalar `5/64` estimate and the new degree assembly.

## Audit outcome

Workflow `General profile-integral 7/12 candidate audit`, run `34355073705`, completed green.

Two separately written standard-library implementations agree exactly:

- `src/check_7_12.py`;
- `src/audit_7_12_independent.py`.

Durable evidence is preserved in `evidence/run-34355073705/` with SHA-256 receipt. The primary checker regressed 5,207,079 eligible `(n,b)` pairs through `n=5000`; the independently structured audit regressed 1,874,246 eligible pairs through `n=3000`. These regressions are consistency checks, not proof by extrapolation.

Both implementations reconstruct the same eleven direct-assembly exceptions and the same threshold caps:

| a | least b | required t | exact upper bound on S-r |
|---:|---:|---:|---:|
| 4 | 7 | 1 | 1 |
| 6 | 10 | 2 | 2 |
| 9 | 14 | 4 | 5 |
| 11 | 17 | 6 | 8 |
| 14 | 21 | 9 | 13 |
| 19 | 28 | 16 | 26 |
| 24 | 35 | 25 | 43 |
| 29 | 42 | 36 | 64 |
| 34 | 49 | 49 | 90 |
| 39 | 56 | 64 | 121 |
| 44 | 63 | 81 | 155 |

Every final column is strictly less than `2t_required`.

## Scalar red-team checklist

1. **Domain shrink — PASS.** `u=y^2/(2x)` satisfies `u<=1/2` because `0<=y<=x<=1`. The cubic minorant is used only on this restricted interval.
2. **Minorant sign — PASS.** `B(u)=1-u/2-u^2/8-3u^3/32` is decreasing and `B(1/2)=181/256>0`.
3. **Square gap — PASS.** Both checkers reconstruct

   ```text
   1-u-B(u)^2 = u^3(64-112u-24u^2-9u^3)/1024.
   ```

   The cubic factor is decreasing and equals `7/8` at `u=1/2`.
4. **Integrated coefficients — PASS.** Independent hand re-expansion gives `x^2/12`, `x^3/160`, `3x^4/1792`.
5. **q substitution — PASS.** Both derivations give

   ```text
   P(q)=2q^2-4q^3+(2/3)q^5+(1/10)q^7+(3/56)q^9.
   ```
6. **Three interval cover — PASS.** `[0,1/3]`, `[1/3,7/20]`, `[7/20,1/sqrt(2)]` cover the complete q-domain.
7. **Low interval — PASS.** `P'>=0` because `Q>=4-12q>=0`.
8. **Middle interval — PASS.** The cubic base decreases, the positive tail increases, and exact arithmetic gives the tail at `7/20` below `1/250`.
9. **High interval — PASS.** `Q'<=-365/64<0` and `Q(7/20)=-1631127391/30720000000<0`.
10. **Strictness — PASS.** The final scalar margin is exactly `11/216000>0`.

## Profile-integral inheritance checklist

1. Cauchy–Schwarz direction — rechecked; unchanged from the 293/500 proof.
2. Lower bound `z_h>=H0>=h` — rechecked and still explicitly required.
3. Nested budget `sum_h z_h<=r` — unchanged.
4. Shifted-midpoint argument and endpoint loss `<=a/4` — re-expanded; unchanged.
5. Domain `s_i/a in [0,1]` — valid, including `s_i=0` separately.

**Trust boundary:** these inherited points remain same-assistant candidate mathematics. A later flaw in the shared graph-to-demand or exact threshold-capacity lemma would affect both this 7/12 result and the earlier 293/500 result.

## Degree-assembly red-team checklist

1. From `b>=7n/12`, exact algebra gives `5b>=7(a+1)` and `(b-a-1)/2 >= (a+1)/5` — PASS.
2. Parity identity `floor(n^2/4)-b(n-b)=floor((b-a-1)^2/4)` — exact regression PASS.
3. Floor loss at most `1/4` — PASS.
4. Large-a difference

   ```text
   D(a)=(a+1)^2/25-1/4-5a^2/128-a/8
   ```

   has coefficient `3/3200`, `D(53)=123/3200`, and first forward difference `177/3200` — PASS in both implementations.
5. Least eligible degree `ceil(7(a+1)/5)` and monotone required surplus — PASS.
6. Direct-bound exception list reconstructed independently as

   ```text
   4,6,9,11,14,19,24,29,34,39,44.
   ```
7. Every exception is closed by the `K_h,w_h,L_h` threshold certificate — PASS, exact table above.
8. `a=0` star and `a=1` edgeless-F cases remain separate — PASS.

## Independence / evidence policy

The two checker implementations share no code, but both were produced within the same AI-assisted project. They are therefore **not external independent reproduction**. The green checks promote the result only to the repository's candidate-theorem status.

The next required steps are reviewer manuscript/verification companion generation, top-level README synchronization, and external specialist review.
