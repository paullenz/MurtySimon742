# High-q interval capacity and the two-defect budget

**Status:** exact identities and a sufficient inequality in the stated target-capacity model, with finite reconnaissance and independently implemented arithmetic checks. No universal tail-existence theorem, graph-realizability claim, whole-state promotion or external acceptance is asserted.

This checkpoint continues `0e6546e8947b43896d0c8f5eebde8335b8d95f11` and the newer summed-tail note at `2f535a2e016da53a2b5bbfa36637363023e67917`. It deliberately replaces the search for one fixed quadratic potential with an adaptive threshold and an explicit receiver-loss budget. Structural surplus is `t`; thresholds are always `tau`.

## 1. Domain and notation

Let B contain b labelled vertices with nonnegative integer q_u, rho_u, c_u=q_u+rho_u, and integer target caps P_u>=0. Directed compatibility is

```text
D(u,w) iff u!=w, q_u<=c_w+1, q_w<=c_u.
```

For the bridge application assume c_u<=a, rho_u>=1, t>0 and

```text
r=sum rho_u,  S=sum s_i,  Q=sum q_u,
D0=S-r-2t>=0,  Esel=Q-S>=0,
Q=r+2t+D0+Esel.
```

Write delta=b-a and

```text
Bload=2t+D0+Esel=Q-r,
h_w=rho_w+delta-1,
G=b(delta-1)-Bload>=0.
```

Here G is the unused aggregate incoming headroom, not a graph. Assume P_w<=h_w. The canonical origin of these assumptions inherits the external-review status of the [two-defect bridge decomposition](../2026-09-14-type-compressed-orientation-hall-v1/BRIDGE_TWO_DEFECT_DECOMPOSITION.md) and [canonical bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md). The identities below do not certify those graph-to-profile implications independently.

For T_tau={u:q_u>=tau}, set

```text
Q_tau=sum_{u in T_tau}q_u,
Q_<tau=sum_{q_u<tau}q_u,
y_w(tau)=#{u in T_tau:D(u,w)},
H_tau=sum_w min(P_w,y_w(tau)),
Delta_tau=Q_tau-H_tau=-F_tau.
```

A positive Delta_tau is a deficient high-q tail.

## 2. A one-sided interval reduction

Define the q-tail counts N_j=#{u:q_u>=j}. Drop only the reverse-compatibility condition q_w<=c_u, retaining the upper incoming threshold and exclusion of the target's own source copy:

```text
J_w(tau)
 = #{u!=w:tau<=q_u<=c_w+1}
 = max(0,N_tau-N_{c_w+2})-1_{q_w>=tau}.              (1)
```

The subtraction is legitimate because c_w>=q_w. In particular J_w>=0, even when tau>c_w+1. We have y_w<=J_w and therefore

```text
H_tau <= U_tau := sum_w min(P_w,J_w(tau)).           (2)
```

This upper bound needs the source q histogram and the receiver (q,c,P) data, but no arbitrary source-subset search or target max-flow.

**It is an upper bound, not a universal exactness theorem.** Section 7 preserves both abstract and frozen-profile strict gaps.

## 3. Receiver losses against the two-defect budget

Separate two losses:

```text
Lambda=sum_w(h_w-P_w),
Omega_tau=sum_w(P_w-J_w(tau))_+.
```

Lambda is capacity removed by the full target-cap formula. Omega_tau is capacity that remains nominally available but cannot be filled even by the relaxed interval incoming sources.

Since sum h=r+b(delta-1),

```text
sum P=r+b(delta-1)-Lambda,
U_tau=sum P-Omega_tau.
```

Also Q_tau=Q-Q_<tau=r+Bload-Q_<tau. Substitution gives the exact interval deficit and the promised sufficient inequality:

> ```text
> Delta_tau >= Q_tau-U_tau
>           = Lambda+Omega_tau-Q_<tau-G.              (3)
> ```

Consequently,

> ```text
> Lambda+Omega_tau > Q_<tau+G                         (4)
> ```
>
> forces a deficient high-q tail.

The four terms have distinct roles: full-cap loss, interval-unfillable capacity, source demand omitted below the threshold, and unused two-defect headroom. No equality of a Hall minimum with a tail minimum is required.

Equation (3) is a proved implication under the stated hypotheses. The claim that every relevant canonical Murty profile has a threshold satisfying (4) remains OPEN; it is not hidden inside this statement.

## 4. Exact correction and its location

The reverse-incompatible interval sources at w are simply

```text
I_w(tau)=#{u:q_u>=tau and c_u<q_w}.                  (5)
```

There is no need to repeat u!=w or q_u<=c_w+1 in (5): c_u<q_w implies u!=w and q_u<=c_u<q_w<=c_w+1. Therefore y_w=J_w-I_w.

For arbitrary integers 0<=I<=J and P>=0,

```text
min(P,J)-min(P,J-I)=[I-(J-P)_+]_+.
```

Define

```text
Xi_tau=sum_w[I_w(tau)-(J_w(tau)-P_w)_+]_+.
```

Then

> ```text
> Xi_tau=U_tau-H_tau>=0,
> Delta_tau=Lambda+Omega_tau+Xi_tau-Q_<tau-G.          (6)
> ```

Reverse deletions matter only after using up the target's excess interval incoming count. This retains exactly the correlation discarded in (2).

There is also a useful localization. If rho_u>=h for every source, then q_w<=tau+h implies I_w(tau)=0. Hence Xi_tau can be supported only on targets with q_w>=tau+h+1. In particular, when tau>=max(q)-h, the interval bound is exact. Positive-surplus residual activity supplies h>=1. This localization is a hand consequence, not an empirical fit.

## 5. Retain every target-cap term

Let dK_w be the exact degree in the undirected potential-pair graph, where a pair is potential when at least one orientation is directed-compatible. Let z=#{i:s_i=0} and k_w=min(z,q_w,Esel). The current cap formula is

```text
P_w=min(
  rho_w+delta-1,
  b-1-q_w,
  dK_w-q_w,
  rho_w-1+floor((Esel-k_w)/(q_w-k_w)) if q_w>k_w
).
```

A negative cap is infeasibility; it must not be clipped silently to zero. The selected-excess term is absent when its denominator is zero. In particular z is NOT assumed bounded by Esel.

Since c_w<=a, the simple-degree cap is no smaller than the residual cap, but it remains present in the implementation. The per-target loss has the exact compact expression

```text
h_w-P_w=max(
  0,
  c_w+delta-1-dK_w,
  delta-floor((Esel-k_w)/(q_w-k_w)) if q_w>k_w
).                                                       (7)
```

Thus (3) retains potential-pair scarcity and selected-excess scarcity, while D0, Esel and t enter separately through G. Neither D0 nor the count z may be substituted for Esel.

## 6. Weighted consequences, and a rigorous obstruction to fixed weights

For any nonnegative weights lambda_tau with finite support, summing (6) gives

```text
sum_tau lambda_tau Delta_tau
 = (sum_tau lambda_tau)(Lambda-G)
   +sum_tau lambda_tau(Omega_tau+Xi_tau-Q_<tau).       (8)
```

Dropping Xi gives a sufficient weighted pressure. With Phi(j)=sum_{tau<=j}lambda_tau, the source side is sum q_u Phi(q_u), as in the existing [summed-tail identity](../2026-09-14-type-compressed-orientation-hall-v1/SUMMED_Q_TAIL_PRESSURE.md). Choosing lambda concentrated at one threshold recovers (3).

One fixed profile-independent weighting cannot cover all 812 difficult profiles. This is now certified by exact integers, not merely a numerical optimization report. Three preserved profiles, zero-based diagnostic rows 199, 209 and 768, have deficiency vectors at tau=1,...,8:

```text
A=(-4, 0, 2, 2,-2,-2,-2,0),
B=(-5, 3, 3,-2,-2,-2,-2,0),
C=(-5,-7,-5, 1, 1, 1,-5,0).

7A+12B+10C=(-138,-34,0,0,-28,-28,-88,0)<=0.
```

All later threshold deficiencies are zero. If a common lambda>=0 gave strictly positive weighted pressure to all three profiles, the same positive combination would be strictly positive, contradicting the displayed coordinatewise inequality. Each profile individually has a deficient tail.

Complete arrays and coefficients are in `FIXED_WEIGHT_OBSTRUCTION.json`; the standard-library verifier checks the certificate without an optimization solver. All three have scalar state 1626; A and B have Esel=3, whereas C has Esel=4. Thus this certificate does NOT rule out weights depending on Esel or on the actual profile. Adaptive threshold choice remains viable.

## 7. Frozen experiments and preserved strict gaps

The original 15-state q-stratified pilot is run [34859094097](https://github.com/paullenz/MurtySimon742/actions/runs/34859094097), artifact 10356424619. Its source generator and original stopping rules were retained. The interval replay exactly matches every original logical summary column; runtime seconds are excluded from that comparison.

```text
original generated profiles:                  201,493,148
original target-Hall failures:                    205,919
Hall failures detected by interval inequality:    205,919
first deficient threshold agrees with exact:      205,919
all thresholds interval-exact:                    205,887
some reverse-correction gap:                           32
maximum interval/exact deficiency agrees:         205,895
uniform-weight detections:                        199,634
```

The independently written NumPy audit checked every exported profile: 205,919 failures plus 12 target-Hall passes, totaling 205,931. This is independent arithmetic on SHARED profile generation, not independently generated exhaustive evidence or external reproduction. The original pilot is only 15 scalar states, with its existing early stopping; this is not a scan of the entire frontier. The q-stratified artifact also records C_q=0 on all 205,919 failures, a separate finite observation.

For the difficult residue from run [34850187436](https://github.com/paullenz/MurtySimon742/actions/runs/34850187436), all 812 profiles and all 6,667 tested threshold rows satisfy U_tau=H_tau. The interval inequality detects 812/812; uniform weights detect only 476/812. First deficient thresholds are 2:426, 3:191, 4:195. Earliest maximum-deficiency thresholds are 2:220, 3:170, 4:422. Detailed outputs retain D0, Esel, t, r, Q, delta, headroom, losses and q/rho histograms.

**Frozen strict-gap example.** State 226 has a=15, b=18, t=1, D0=Esel=0, r=39, Q=41, G=34 and

```text
q  =0,0,0,0,0,0,0,3,4,3,3,3,3,3,3,7,7,2
rho=1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,3,3,4
P  =3,3,3,3,3,3,3,1,1,2,2,2,2,2,2,2,2,3.
```

At tau=1, H=26, U=28, Xi=2. Exact deficiency is 15; the interval lower bound is 13. Therefore universal interval exactness is false even on this frozen relaxation. The example does not defeat the one-sided theorem or the observed detection result.

The independent small verifier also preserves abstract interval-detection misses: for q=(0,1,2), rho=(1,0,0), P=(1,1,1), the tau=1 exact deficiency is 1 but the interval bound is 0, and no interval tail is deficient. This example is outside positive-surplus residual activity; it refutes only an unrestricted abstract strengthening.

## 8. Hostile examples and synthetic domain boundaries

All three examples in [MURTY_Q_TAIL_HALL_CONJECTURE.md](../2026-09-14-type-compressed-orientation-hall-v1/MURTY_Q_TAIL_HALL_CONJECTURE.md) are retained and rechecked. They have Hall minimum -1 but no deficient high-q tail. The new lower bound never falsely certifies one.

For a=4,b=7 with one (q,rho)=(1,1) and six (3,1), Esel=5,z=2 is ruled out by selected-incidence demand forcing, not by silently modifying z. Esel=19,z=4,s=0 violates S>=r+2t. The arbitrary-monotone-cap example never supplied a full canonical bridge.

A seeded synthetic search performed 100,000 trials. Its EXPLICIT domain comprises the scalar two-defect identities, positive residual activity, source caps, r+t<=choose(a,2), full deterministic target caps, selected-incidence feasibility and potential-pair Hall feasibility. It does NOT construct the F-graph, residual column realization or full quasi-edge representative forcing.

```text
formal scalar-domain trials:              44,234
full cap checks passed:                    5,582
selected incidence passed:                 1,467
potential-pair Hall passed:                  713
  with zero-demand labels:                    46
  with D0>0:                                  30
target-Hall failures among the 713:           474
failures detected by interval tails:          474
target-Hall passes:                           239
```

A separately written BFS augmenting-path implementation checked all 713 selected-incidence, potential-pair and target-flow instances, along with caps and interval identities. Representative selected-label and target-flow certificates are retained. They are separate feasible relaxations, not a joint graph realization.

The 239 target-Hall passes are a genuine warning: the listed scalar/incidence relaxations ALONE cannot force a deficient tail for every profile. This does not refute a theorem using the full canonical bridge. The original frozen replay likewise has 12 target-Hall passes, of which the old cost test rejects 10 and two pass that additional test. No graph is asserted to exist.

## 9. Verification and next proof obligation

The standard-library identity verifier passes 7,314 exhaustive multiset profiles and 5,000 seeded random profiles. It deliberately finds positive reverse gaps and abstract interval-detection misses; those are expected negative tests, not suppressed cases. It also rechecks the exact three-profile fixed-weight certificate.

The strongest clean new target is now

```text
find tau such that Lambda+Omega_tau > Q_<tau+G,
```

or, where reverse incompatibility is essential, use the exact Xi_tau correction in (6). A universal proof must derive this from additional canonical structure; finite success does not supply that implication. Selected-label endpoint forcing and joint residual/selected realization are natural remaining sources of information. The exact q-layer normal form and crossing-wall route remain valid fallbacks, not discarded work.

The promoted frontier remains 1,971 exclusions / 3,607 survivors, with 977 whole-state closures. The independent 2,655-candidate relational audit remains a separate gate. This checkpoint promotes no state and proves neither unrestricted Murty-Simon nor universal high-q-tail sufficiency.
