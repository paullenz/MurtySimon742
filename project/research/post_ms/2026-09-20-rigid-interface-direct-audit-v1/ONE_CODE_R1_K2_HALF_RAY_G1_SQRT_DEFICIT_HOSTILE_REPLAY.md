# Hostile replay: g=1 square-root deficit theorem

Date: 2026-09-20

Status: **same-session independent replay passed at stated conditional scope**. Target: `ONE_CODE_R1_K2_HALF_RAY_G1_SQRT_DEFICIT.md`.

## Replay checks

1. **Source-row count.** The predecessor concentration theorem gives `T>=t-1-d-2b`. With `g=1`, a saturated shared-source row has exactly one outside head, hence exactly one shared edge. The local row identity and residual-slot degree cap force `m_i=a_i`. Since `sum a_i=a`, at least `R0>=T-a` source rows have `m_i=0`.

2. **Algebra of the lower bound.**

`R0>=t-1-d-2b-a = t-1-2a-3b-c0`.

As `d=a+b+c0` and `c0>=g=1`,

`2a+3b+c0 = 3d-a-2c0 <= 3d-2`,

so `R0>=t+1-3d` is correct.

3. **No hidden P-reservoir.** With `g=1`, `|P|=t` and `|P\W_s|=t-2`. The R0 reverse witnesses are distinct physical vertices outside `W_s` and are H-anticomplete because `d_H(w)<=m_i=0`. Hence at most `t-2-R0` P-vertices can serve as H-positive carriers for the unique P-neighbour slots of the R0 rows. Using the lower bound on R0 gives `N_car<=3d-3`.

4. **Clique property.** Each R0 source row has `m_i=0`, so these rows form a clique in H. No approximation is used here.

5. **Carrier capacity.** The replayed private-spoke classification applies to every carrier because it is H-positive. Every R0 row touched by a carrier lies outside that carrier's possible two-coordinate private d-support; the carrier therefore sees the private foot of every touched row. For each pair of touched R0 rows, both private-foot H--H orientations are spoiled, so the preserved H--H split forces that edge to be U-certified. The proof uses only the per-carrier implication `binom(r,2)<=u`; it never adds U-certified counts across carriers.

6. **Cover inequality.** Since every R0 row needs a P-neighbour and H-anticomplete reverse witnesses cannot supply one,

`R0 <= N_car R(t) <= (3d-3)R(t)`,

where `R(t)=floor((1+sqrt(8t+9))/2)`. Combined with `R0>=t+1-3d`,

`t+1-3d <= (3d-3)R(t)`.

Rearranging gives exactly

`d >= ceil((t+1+3R(t))/(3(R(t)+1)))`.

7. **Asymptotics.** Since `R(t)~sqrt(2t)`, the bound is `(1/(3sqrt(2))+o(1))sqrt(t)`.

## Verdict

No resource overlap, parity, row-count, carrier-coverage or U-certified-edge double-counting issue was found.

> **Replay verdict:** the conditional `g=1` theorem `Delta=Omega(sqrt(t))`, with the explicit bound above, survives same-session hostile replay.

The theorem remains downstream of the unresolved rigid-interface reachability gate; bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, and `X_3` remains mandatory.