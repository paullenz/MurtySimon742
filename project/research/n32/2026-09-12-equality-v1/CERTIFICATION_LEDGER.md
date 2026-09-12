# N32 equality certification ledger

12 September 2026. Research direction: Paul Lenz. Mathematical development, implementation and internal checking: ChatGPT/Geeps.

**Status: exact finite evidence inside the candidate selected/residual bridge. Independent mathematical review remains OPEN.**

## Scope

This directory handles the last equality branch for order 32:

```text
n=32,
Delta=17,
a=14,
b=17,
m=256,
t=1.
```

The fourteen-label score theorem gives `Q<=23`; the bridge gives `Q>=19`.

## Frontier reconstruction

`check_n32_t1_frontier.cpp` independently enumerates all 20,058,300 nondecreasing fourteen-demand multisets in `{0,...,13}` and verifies:

```text
Q=19 : 206 profiles
Q=20 : 104 profiles
Q=21 :  50 profiles
Q=22 :  18 profiles
Q=23 :   3 profiles
------------------
total : 381 profiles
```

Exactly 36 frontier profiles contain a zero demand.

The residual-tail lower bounds must themselves be monotone. Applying the monotone closure to `z_h>=gamma_h(W_h)` removes one apparent positive-demand profile before any RX/Hall modelling:

```text
s = 3^11,5^3.
```

For this row the raw score is `Q=19`, but monotonicity requires `z_4>=z_5=5` rather than the raw `gamma_4=4`, so `r_min=47` while `S-2=46`. It is arithmetically impossible.

After monotone closure and all allowed residual-tail slack increments, the intentionally conservative finite domain is:

```text
positive-demand states : 1,984
zero-demand states     :    61
pre-model impossibles  :     1 profile
```

The positive domain deliberately includes states with `S>r+2`; for an actual all-positive graph the exact ledger gives `S=r+2`. This is safe over-enumeration. It is retained here because it is the domain actually exact-certified during the 12 September audit. A later proof-size reduction may restrict to exact-ledger states, but must not silently change the frozen evidence ledger.

## Exact stage A: lifted N30 t=1 potential

`n32_t1_lifted_potential_exact.py` uses the natural `b=17` lift of the exact N30 13-term 3-D potential. The global weights are fixed; only profile-specific scalar envelope coefficients vary.

Floating LP is proposal only. The script rounds the scalar proposal, repairs only the one-sided `ell/sigma` envelope variables, and accepts a state only after checking every local row and the strict contradiction gap in integer arithmetic.

Fresh preservation replay reproduced:

```text
positive states tested       : 1,984
exact rational exclusions    : 1,369
survivors passed to stage B  :   615
exactification failures      :     0
accepted denominator         : 10,000 for all 1,369
strict gap numerators        : -10,003 ... -9,827
```

## Exact stage B: full positive-demand RX/Hall model

`n32_t1_full_rx_exact.py` imports the already preserved generic positive-demand RX/Hall model and exact integer Farkas layer from

```text
project/research/general_n/2026-09-09-rx-hall-v1/
```

It is designed to run in shards. Every rejected row is accepted only after `verify_certificate` checks the integer Farkas combination. A state with no exact certificate is re-solved as a primal feasibility problem and surfaced explicitly.

The completed 12 September exactification ledger is:

```text
stage-B input states          : 615
exact integer Farkas rejects  : 614
primal survivors              :   1
unresolved                    :   0
```

The unique survivor is

```text
s   = 1^2,2^12,
rho = 1^10,2^7.
```

It is excluded without computation in `HAND_EXCEPTION.md`.

As a preservation spot-check, the regenerated exactifier was rerun after packaging on the first 30 stage-B states. It returned 29 exact integer Farkas certificates, the same unique primal survivor, and zero unresolved rows. The committed shard driver regenerates the full 614-certificate ledger rather than treating saved dual coefficients as proof premises.

## Exact stage C: zero-demand states

When `s=0`, the positive-demand compression `d=R+s` is invalid. `n32_t1_zero_exact.py` therefore keeps `d` and `R` separately and enforces

```text
s=max(0,d-R),
sum R = r,
sum d = 2(r+t).
```

The cap `d<=12` is justified by the isolated-C lemma. In the present parameters an isolated vertex of `C` would imply

```text
b <= a-1-t,
17 <= 12,
```

which is impossible; hence `delta(C)>=1` and `d_F(i)<=a-2=12`.

The completed exactification ledger is:

```text
zero-demand states            : 61
exact integer Farkas rejects  : 61
unresolved                    :  0
```

The preservation implementation was independently rerun on the first zero-demand shard after packaging and reproduced exact integer rejection; the committed sharded replay regenerates all 61.

## Aggregate proof accounting

The equality branch is therefore partitioned as follows:

```text
one monotone-tail arithmetic impossibility                 1 profile
lifted-potential exact rational certificates            1,369 states
full RX/Hall exact integer Farkas certificates            614 states
hand threshold-equality contradiction                        1 state
strengthened zero-demand exact integer Farkas certificates  61 states
```

No floating-point infeasibility is a proof event. Floating solvers only propose coefficients or distinguish the unique stage-B primal survivor; every computational exclusion used in the candidate proof is checked exactly in integer/rational arithmetic.

## Replay

From the repository root:

```sh
bash project/research/n32/2026-09-12-equality-v1/run_replay.sh
```

The default uses 32 shards for the two heavier exact stages. The shard count can be changed, without changing the mathematical model, by setting for example

```sh
N32_SHARDS=64 bash project/research/n32/2026-09-12-equality-v1/run_replay.sh
```

The final aggregate file must report `status: PASS` and the counts above.

## Trust boundary

The finite arithmetic and exact certificate semantics are reproducible, but they remain conditional on the universal graph-to-selected/residual bridge, the threshold-capacity lemma, and the correctness of the finite necessary-condition models. Same-assistant replay is not independent external mathematical validation.
