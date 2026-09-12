# Compatible lower tails and adaptive clipping

12 September 2026. Research direction: Paul Lenz. Development, implementation
and internal checking: ChatGPT/Geeps.

**Candidate exact structural bounds. Independent mathematical review and
novelty assessment remain OPEN. The finite arithmetic is proof-critical.**
This is not an unrestricted Murty-Simon proof.

## 1. What has changed

The independent-interval clipping estimate first becomes inconclusive at
`(a,M,k)=(17,6,11)`. It does **not** exhibit a clipping counterexample there.
Keeping all lower tails compatible repairs every clipping step down to five
for `17<=a<=22`. At `a=23`, clipping six to five genuinely fails, but clipping
all higher levels down to six still works. Retaining a six-level terminal
domain therefore repairs this boundary without asserting false monotonicity.

The resulting sharp scalar bounds are:

| labels a | terminal maximum demand | terminal states | maximum D | maximum Q |
|---:|---:|---:|---:|---:|
| 17 | 5 | 5,985 | 15 | 32 |
| 18 | 5 | 7,315 | 17 | 35 |
| 19 | 5 | 8,855 | 20 | 39 |
| 20 | 5 | 10,626 | 22 | 42 |
| 21 | 5 | 12,650 | 25 | 46 |
| 22 | 5 | 14,950 | 27 | 49 |
| 23 | 6 | 98,280 | 31 | 54 |

The table proves bounds over **all** original vectors `0<=s_i<=a-1`, not
merely vectors initially having small demand. Witnesses attaining the maxima
are, respectively, `4^17`, `4^18`, `4,5^18`, `5^20`, `5^21`, `5^22`, `6^23`.
Full equality classification before clipping is not claimed; the saved
terminal equality lists concern the terminal domain only.

## 2. Definitions and the exact clipping identity

For `h>=2`, define `C_h(z)=[z(z-1)+h(h+1)]/2`. Let `gamma_h(W)` be the
least integer `z>=h` for which `W<=C_h(z)`, with `gamma_h(0)=0`.
For a demand vector s, let

`N_h=#{i:s_i>=h}`, `W_h=sum_{s_i>=h}s_i`, `p=#{i:s_i>=1}`,

`D(s)=sum_{h>=2}(N_h-gamma_h(W_h))`, `Q(s)=p+D(s)`.

Suppose the current maximum demand is M and exactly k entries equal M.
Replace all those entries by `M-1`. For `2<=h<M`, the tail count is unchanged
and its weight decreases by k. Level M disappears, with contribution

`L=k-gamma_M(Mk)`.

Hence the **exact** change is

`D(after)-D(before) = sum_{h=2}^{M-1}[gamma_h(W_h)-gamma_h(W_h-k)] - L`. (1)

Each lower-level drop is nonnegative. Thus `L<=0` is automatically safe.
When `L>0`, the previous method minimizes each summand on its own interval.
Those independently minimizing weights need not be simultaneously realizable.

## 3. A parameterized joint minimization lemma

Fix a, M, k. Let `c_h` be the number of lower demands equal to h, for
`2<=h<M`. They satisfy `c_h>=0` and `sum c_h<=a-k`; unused slots are zeros
or ones and do not affect D. The compatible tails are exactly

`W_h=Mk+sum_{j=h}^{M-1} j c_j`.

Put `delta_h(W)=gamma_h(W)-gamma_h(W-k)`. Define a recursion for an already
fixed higher-tail mass T and c available lower-label slots:

`F(1,c,T)=0`,

`F(h,c,T)=min_{0<=u<=c} [delta_h(T+h*u)+F(h-1,c-u,T+h*u)]`.           (2)

Then the exact minimum lower-level gain in (1) is

`F(M-1,a-k,Mk)`.                                                (3)

**Proof.** Partition all feasible lower-count vectors by the count u at
their highest remaining level h. That choice fixes the h-tail weight to
`T+h*u`, leaves `c-u` slots, and increases the mass inherited by every lower
level by `h*u`. The classes are disjoint and exhaustive. Induction on h
therefore proves (2)-(3). Filling unused slots with zeros realizes every
terminal choice. QED.

This recurrence is valid for all finite integer parameters in the stated
domain; it does not assert that the resulting gain is always at least L.
It supplies an exact compatibility test and a minimizing demand vector.

## 4. Finite assembly and verification

For each `17<=a<=23`, the verifier considers every `6<=M<=a-1` and every
`1<=k<=a`. Rows with `L<=0` are safe. Otherwise it first uses the valid
independent interval lower bound on `Mk<=W_h<=Mk+(M-1)(a-k)`.
Exactly 46 rows are not settled by that bound across the stated parameter
range. The joint recursion evaluates all 46 and reconstructs a minimizer.

The independent verifier does not use that recursion, its cache, or its
square-root capacity inverse. It directly checks all **156,721** compatible
lower multisets across these exceptional rows using a linear integer inverse.
Every exact minimum agrees. Its separate nonincreasing-tail enumeration also
checks all terminal bounds in the table.

All exceptional rows at a<=22 have nonnegative net gain. At a=23 every row
with M>=7 has nonnegative net gain. Consequently repeated clipping proves
the advertised terminal reductions.

At `(17,6,11)`, the old guaranteed gain is zero while the exact joint gain
is three. The disappearing contribution is one, so the true minimum net
change is **+2**. At a=23 the vector `6^23` has `D=31` and its clipped vector
`5^23` has `D=30`; retaining maximum demand six is essential for this route.

After clipping to c, only the counts of demands `2,...,c` matter for D.
There are `binomial(a+c-1,c-1)` such count vectors. Since `p<=a`, the terminal
D maxima imply the displayed Q maxima. The explicit positive witnesses
above attain them, so the bounds are sharp as scalar demand inequalities.

## 5. Graph transfer and limits

For an actual positive-surplus image of the canonical bridge,

`b+2t <= Q(s)`.

Thus each scalar bound applies to every graph in its corresponding band
`a=n-1-Delta`, with arbitrary b for which the bridge assumptions hold. These
are fixed-a structural families. They do not settle all orders in those
bands, and the bounds need not exclude every possible positive surplus.

The bounds for a=17..23 were not needed to reduce n=34, whose remaining
degree branch has a=15. N34 separately tests the shared incidence machinery
and yields the new [tight-threshold lemma](TIGHT_THRESHOLD_LEMMA.md).

Nothing here proves that maximum demand six suffices at a=24 or above.
The next generalization is an adaptive terminal-cap rule, or an analytic
upper bound extracted from the joint recurrence, with its range proved.

## 6. Replay and status

From the repository root:

```sh
python project/research/general_n/2026-09-12-joint-clipping-v1/verify_joint_clipping.py
```

This solver-free audit reads the preserved results and independently checks
the proof-critical arithmetic. `joint_clipping.py` preserves the discovery
recurrence and minimizers. `adaptive_cap_23.json` preserves the six-level
boundary. All computations are integer arithmetic; the verifier does not
use an external solver. Same-assistant separate implementations are internal
evidence, not external independent mathematical review.
