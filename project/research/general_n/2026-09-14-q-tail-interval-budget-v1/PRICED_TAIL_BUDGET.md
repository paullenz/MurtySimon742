# Priced high-q tails: a selected-excess obstruction beyond Hall deficiency

14 September 2026. **Hand derivation under explicit canonical selected-incidence and endpoint hypotheses, with finite independent arithmetic checks. External mathematical review and novelty assessment remain open. No whole-state or unrestricted Murty–Simon claim.**

This extends the [interval-tail budget](README.md) and incorporates the concurrent [localized selected-excess cap](../2026-09-14-localized-excess-v1/README.md) (commit 449a268f and successors). A tail can be Hall-feasible but too expensive in selected excess. We therefore do not need every relevant profile to have a deficient high-q tail.

## 1. Canonical charge budget, with zero demands retained

Use x_i=s_i+e_i, e_i>=0, E=Esel=sum e_i, z=#{i:s_i=0}, and smax=max_i s_i. Every source u selects q_u distinct labels. A selected positive-demand label i obeys the canonical endpoint consequence

```text
p_u <= rho_u-1+e_i.
```

It follows from d_i<=rho_u+q_u-1, R_i+x_i>=q_u+p_u and d_i=R_i+s_i; the last equality is used only when s_i>0.

Define

```text
v_u=(q_u-z)_+,
d_u=(p_u-rho_u+1)_+.
```

At least v_u of the selected labels at u are positive-demand labels. On each of them d_u<=e_i. Summing over source-label incidences yields

```text
sum_u v_u d_u
  <= sum_{i:s_i>0} e_i x_i
  <= sum_i e_i(s_i+e_i)
  <= E(E+smax).                                      (1)
```

The last step uses sum e_i^2<=E^2 and sum s_i e_i<=smax E. This is a shared selected-excess budget, not independently reusable allowances at each target. Zero-demand labels have been explicitly excluded by v_u; no assumption z<=E is made.

The graph-to-incidence and endpoint implications inherit the external-review status of the canonical bridge. The displayed algebra is valid whenever those hypotheses hold. The bound may be sharpened by retaining sum e_i(s_i+e_i) or another proved envelope rather than replacing it by E(E+smax).

The two-defect decomposition is retained without relabelling:

```text
Esel=Q-r-2t-D0 >=0.
```

Thus the right side of (1) is also (Q-r-2t-D0)(Q-r-2t-D0+smax). Structural surplus is t; q thresholds below are tau.

## 2. A priced-tail necessary inequality

Fix T_tau={u:q_u>=tau}, with demand Q_tau=sum_{u in T_tau}q_u. Take any legitimate incoming cap P_w, including P_w^loc. Put

```text
J_w(tau)=#{u!=w:tau<=q_u<=c_w+1},
A_w=min(P_w,J_w(tau)),
f_w=min(A_w,rho_w-1),
g_w=A_w-f_w.
```

Positive residual activity makes rho_w-1>=0. The interval bound drops only reverse compatibility; replacing J_w by the exact compatible count gives another valid, stronger formulation.

In a genuinely graph-derived orientation the tail sends ell_w incoming units to target w, with 0<=ell_w<=A_w and sum ell_w=Q_tau. Since ell_w<=p_w, equation (1) bounds sum_w v_w(ell_w-rho_w+1)_+.

For every price theta>=0,

```text
v_w(ell_w-rho_w+1)_+
 >= theta*ell_w-theta*f_w-(theta-v_w)_+*g_w.
```

Indeed at most f_w units are free; each further unit has cost v_w and there are at most g_w such units. The maximum of theta*ell minus its cost is theta*f_w+(theta-v_w)_+g_w. This covers theta=0 and v_w=0.

Summing gives the hand-proved necessary inequality:

> ```text
> theta*(Q_tau-sum_w f_w)
>   -sum_w(theta-v_w)_+ g_w
>   <= Esel(Esel+smax),                              (2)
> ```
>
> for every tau>=1 and theta>=0.

A strict violation contradicts the selected-incidence/endpoint bridge, without requiring a deficient Hall tail or equality between arbitrary Hall minima and tail minima. This is a scalar price certificate for an excess-cost lower bound; no universal exact representation of the graph problem by this relaxation is asserted.

## 3. How Hall and tight-tail cost fit together

For theta>=max_w v_w, the left side of (2) is

```text
theta*(Q_tau-sum_w A_w)+sum_w v_w g_w.               (3)
```

If Q_tau>sum A_w, a sufficiently large price recovers the interval Hall contradiction. If Q_tau=sum A_w, every available tail slot must be filled and the forced excess cost is sum v_w g_w. This can violate the bridge even when the tail is not Hall-deficient.

For a fixed receiver relaxation with feasible demand, optimizing the left side over theta in {0,v_1,...,v_b} gives the minimum free/paid allocation cost. This elementary receiver optimization is not full directed or graph realization; the independent verifier compares it against exhaustive integer allocations.

## 4. A concrete tight-tail certificate: 80 > 77

The only profile not rejected by the localized interval reconstruction of the old exported pilot stream is associated with scalar state 4073:

```text
a=15, b=18, t=1, D0=0, Esel=7,
q   =[0,0,0,0,0,1,2,2,2,2,7,7,7,7,7,7,7,7],
rho =[1,1,1,1,1,3,4,4,4,4,4,4,4,4,4,4,4,4],
s   =[2,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
P_loc=[3,3,3,3,3,5,6,6,6,6,4,4,4,4,4,4,4,4].
```

Here r=56, S=58, Q=65, z=0, smax=4. At tau=3, eight q=7 sources demand 56 units. The only interval-capacity slots are four targets with six slots each and eight targets with four slots each: total 56. Exact target-Hall tails are nondeficient, with this tail tight.

Each of the twelve receivers has rho=4, hence three free slots. The four q=2 receivers must each use three paid slots, costing 4*3*2=24. The eight q=7 receivers must each use one paid slot, costing 8*1*7=56. Thus every realization costs at least 80, whereas (1) permits at most

```text
Esel(Esel+smax)=7*(7+4)=77.
```

Equivalently choose theta=7 in (2): 7*(56-36)-(7-2)*12=80>77. The strict gap is three.

This profile was already rejected by the old pipeline's excess-cost screen. The new result is a short explicit priced-tail certificate explaining that rejection, not a new scalar-state exclusion. We do not claim to have calculated an exact minimum cost of 80 in the full graph realization problem.

## 5. Stronger localized caps change the fixed-weight question

The old capacity model has a preserved exact three-profile certificate ruling out one common strictly detecting nonnegative weighting on all 812 difficult profiles. That result is NOT transferred to a stronger cap model.

An independent reconstruction of localized caps finds that the single threshold tau=3 detects every one of the 812 difficult profiles. Its interval bound is exact at that threshold, with deficiency 1 to 15. Cap vectors change on 748 profiles; uniform weights detect 773; first deficient thresholds are 1:630, 2:117, 3:65. The common exact weight vector is (0,0,1,0,0,0,0,0). No optimization solver is needed for verification.

This is not a universal tau=3 theorem. The cap hypotheses genuinely changed, and the old obstruction remains a required old-model regression case.

## 6. Completed reconstruction on all old exported rows

The old frozen pilot exported 205,931 profiles reaching its target-flow stage: 205,919 Hall failures and 12 Hall passes. The original generation and early-stopping rules were retained for the interval replay. The localized experiment is a reconstruction on that EXISTING stream, not regenerated state enumeration after changing the caps.

```text
old exported profiles:                         205,931
cap vectors tightened:                          43,113
localized interval failures at fixed tau=3:     205,930
remaining tight profile:                             1
that profile rejected by priced tail 80>77:           1
uniform weighted-tail detections:              200,892
```

Thus a fixed tau=3 Hall-or-priced-tail explanation covers all 205,931 exported rows. Profile TSV SHA256: `4b183b899127f4f9e05faed0cb23a11c6962c854f077d0e3ad209d09b386fb67`.

These counts close no whole scalar state. The old scanner stopped early at two witness profiles; rejecting them requires resuming omitted continuations before claiming exhaustive state coverage. Shared generation with independent arithmetic is not independent graph generation or external reproduction.

## 7. Red-team boundary remains real

The original three hostile non-tail examples remain in the old-model regression suite. The a=4,b=7 cap-only example violates selected-incidence demand forcing; its all-zero-demand version violates S>=r+2t. Neither is hidden by imposing z<=E.

The priced-tail inequality was checked on 1,329 receiver profiles comprising 5,109 feasible integer demand values, and on 9,293 exhaustive selected-incidence configurations with zero demands. These verify algebra and charge accounting, not graph realizability.

Rechecking the earlier 713 sampled scalar/incidence/pair-flow relaxations with localized caps and priced tails rejects 652 but leaves **61 not rejected**. These are preserved, including an explicit example. Passing is not graph realizability, but the 61 block an unsupported claim of universal contradiction from the tested relaxation. No additional priced-only rejection occurred in this sample.

## 8. Reproduction and next proof obligation

`python3 verify_priced_tail.py` uses only the standard library and the existing interval verifier. It checks the selected-incidence charge, exhaustive receiver allocations, localized-cap reconstruction and exact 4073 fixture. Frozen output: `PRICED_TAIL_VERIFICATION.json`.

With inputs unpacked as in [REPRODUCE.md](REPRODUCE.md):

```sh
python3 verify_localized_fixed_tail.py
python3 replay_localized_export.py
python3 recheck_synthetic_priced.py
```

The middle command requires NumPy and the existing INTERVAL_PROFILES.tsv. Outputs preserve the 812 reconstruction, full exported-row counts and synthetic non-rejections. The optional discovery script `extend_localized_caps.py` is in the evidence bundle; the fixed-threshold certificate is integer-only.

The all-order goal is now a violating pair (tau,theta) from full canonical structure, perhaps using localized excess, exact pair losses and sharper excess envelopes. This broadens the target beyond requiring a Hall-deficient tail everywhere. Exact q-layer and crossing-wall routes remain fallbacks. The frontier remains 1,971 exclusions / 3,607 survivors with 977 closures; the separate 2,655-candidate relational audit remains unpromoted.
