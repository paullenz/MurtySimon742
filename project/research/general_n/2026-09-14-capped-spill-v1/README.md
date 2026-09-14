# Capped positive excess and all-source spill

14 September 2026. **Candidate universal consequences of the canonical bridge, independently structured local finite verification, external review OPEN. No whole-state promotion or unrestricted proof.**

This continues the [priced-tail argument](../2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md) and [localized cap](../2026-09-14-localized-excess-v1/README.md). Two new constraints improve the old 713-profile synthetic experiment from 652 to 694 rejections. The remaining 19 profiles are retained. The sample is a specified relaxation, not a set of realized graphs or a complete scalar-state enumeration.

## 1. Bridge notation and the missing clipping

Write

```text
x_i=s_i+e_i, Esel=sum_i e_i, z=#{i:s_i=0},
delta=b-a, v_u=(q_u-z)_+,
d_u=(p_u-rho_u+1)_+.
```

Structural surplus is t; q thresholds are tau and label-demand thresholds are eta. In the positive-surplus canonical regime,

```text
Q=r+2t+D0+Esel,
rho_u>=1, c_u=q_u+rho_u<=a,
p_u<=rho_u+delta-1.
```

Thus d_u<=delta. At every selected POSITIVE-demand label i, the canonical endpoint-excess inequality also gives d_u<=e_i. Each source chooses distinct labels and at least v_u of them have positive demand. Summing over the ACTUAL selected incidence matrix therefore proves

> **Capped positive-label charge theorem**
>
> ```text
> sum_u v_u d_u
> <= sum_{i:s_i>0} x_i min(e_i,delta)
>  = sum_{i:s_i>0}(s_i+e_i)min(e_i,delta).             (1)
> ```

The previous Esel(Esel+smax) bound omitted two useful facts: incoming pressure is capped at delta, and zero-demand label excess does not finance the POSITIVE-label charge on the left of (1). This is a bound on the same charge, not a claim that zero-demand labels impose no other graph constraints.

## 2. Charge already forced into zero-demand labels

A source u can select at most

```text
h_u^+ = #{i:0<s_i<=rho_u}
```

positive labels. At least f_u(0)=(q_u-h_u^+)_+ of its selections must use zero-demand labels. Define

```text
M0=sum_u f_u(0),  B=Esel-M0.
```

Zero-demand labels have x_i=e_i, so their total excess is at least M0. Consequently 0<=E_+:=sum_{s_i>0}e_i<=B. B<0 is selected-incidence infeasibility, not something to clip to zero.

Let smax=max_i s_i. Since min(e,delta)<=e and min(e,delta)<=min(E_+,delta), (1) gives

> **Linear capped envelope**
>
> ```text
> sum_u(q_u-z)_+(p_u-rho_u+1)_+
> <= B [smax+min(B,delta)],
> B=Esel-sum_u(q_u-#{i:0<s_i<=rho_u})_+.              (2)
> ```

When B>=delta this is linear in B, replacing the old quadratic dependence. Substituting Esel=Q-r-2t-D0 couples it directly to the two-defect ledger. Equation (2) needs the incoming cap d_u<=delta; dropping that hypothesis is not legitimate.

For tail T_tau, take any legitimate receiver caps P and the interval-compatible upper bound J_w(tau)=#{u!=w:tau<=q_u<=c_w+1}. Set

```text
A_w=min(P_w,J_w(tau)),
f_w=min(A_w,rho_w-1), g_w=A_w-f_w.
```

The earlier priced-receiver argument now gives the stronger necessary inequality, for every tau>=1 and theta>=0,

```text
theta(Q_tau-sum_w f_w)-sum_w(theta-v_w)_+g_w
<= B[smax+min(B,delta)].                              (3)
```

A strict violation excludes the profile even when all its tested Hall tails are nondeficient. No universal tail-minimum theorem is assumed.

## 3. All-source spill: stronger localized receiver caps

For eta>=0 let L_eta={i:s_i<=eta}, S_eta=sum_{i in L_eta}s_i, and

```text
f_u(eta)=(q_u-#{i:eta<s_i<=rho_u})_+,
M_eta=sum_u f_u(eta).
```

EVERY source contributes its unavoidable spill into L_eta. The earlier localized cap counted only sources with rho_u<=eta. Thus M_eta is a stronger selected-incidence lower bound.

Fix a source w, and let k count its ACTUAL selected labels in L_eta. Remove w's own lower bound before adding these k incidences:

```text
x(L_eta)>=M_eta-f_w(eta)+k,
C_{eta,w}=Esel+S_eta-M_eta+f_w(eta).
```

All selected labels outside L_eta are positive. For d_w>=1, combine their required excess with the displayed low-block lower bound:

> ```text
> C_{eta,w} >= k+(q_w-k)d_w.                          (4)
> ```

The +f_w(eta) term is essential; otherwise w is counted twice. No rho_w>eta restriction is needed, because w is removed explicitly.

Set m_{eta,w}=#{i:s_i<=min(eta,rho_w)} and kstar=min(m_{eta,w},q_w,C_{eta,w}). As in the earlier integer ratio proof, when q_w>kstar,

```text
p_w<=rho_w-1+floor((C_{eta,w}-kstar)/(q_w-kstar)).     (5)
```

If C<q, (4) rules out d>=1. If C>=q, the ratio (C-k)/(q-k) is nondecreasing in k, proving the formula at kstar. Retain the minimum with ALL old caps, including potential-pair degrees. Negative caps reject a branch.

The implementation tests eta=0 and each distinct demand value. The low-label set, its spill count, and every resulting formula are constant between these demand breakpoints. For a fixed profile, the all-source lower bound includes the earlier low-residual-source count; taking the minimum with earlier caps is nevertheless retained explicitly.

## 4. A sharper integer upper envelope, with an explicit trust boundary

Equation (1) can retain the distribution of label excess rather than just B. Sort labels by demand and let

```text
h_i=#{u:q_u>0 and rho_u>=s_i}-s_i.
```

Every actual e vector satisfies

```text
0<=e_i<=h_i,  sum_i e_i=Esel,
sum_{i:s_i<=eta}e_i>=max(0,M_eta-S_eta) for every demand breakpoint eta.
```

Let U_DP maximize sum_{s_i>0}(s_i+e_i)min(e_i,delta) over these INTEGER vectors. A prefix dynamic programme computes this maximum with state (number of processed labels, excess used). Each equal-demand prefix inequality is imposed only after the whole equal-demand block, not halfway through it. An empty feasible set rejects the necessary selected-incidence projection.

The actual vector is in this set. Hence

```text
sum_u v_u d_u <= U_DP <= B[smax+min(B,delta)].        (6)
```

The dynamic programme is exact for this explicitly stated projection, NOT for realizable selected matrices or graphs: row correlations and full quasi-edge/residual realization are still omitted. A budget violation is safe; passing proves no realization. Replace the right side of (3) by U_DP for a stronger test.

## 5. A former unrejected witness now has the hand certificate 57>48

The old synthetic survivor published in SYNTHETIC_PRICED_TAIL_RECHECK.json is zero-based row 4 of the regenerated corpus. It has

```text
a=24, b=27, delta=3, t=2, D0=0,
r=58, S=62, Q=96, Esel=34, z=2, smax=3.
```

All arrays are frozen in CAPPED_SPILL_VERIFICATION.json. Forced zero-label selections total M0=26, so B=8. Equation (2) gives the upper bound

```text
8(3+3)=48.
```

At tau=1 and theta=4, even the PREVIOUS localized capacities have sum f=31 and price-discount sum 203. Thus the priced lower bound is

```text
4(96-31)-203=57>48.                                  (7)
```

This is a nine-unit contradiction using a short integer formula, with no optimizer or max-flow required to verify it. The new all-source caps preserve the same lower bound. The sharper integer envelope is 46, but that extra improvement is not needed for the hand exclusion. No interval tail is deficient on this profile even after the spill cap: the priced route genuinely adds something beyond tail deficiency.

## 6. Completed finite experiments

The original fixed-seed C++ generator was regenerated from its committed source and frozen q-stratified scanner artifact. Its 100,000 trials reproduced all original totals: 44,234 scalar-domain inputs, 5,582 cap passes, 1,467 selected-incidence passes, 713 potential-pair-flow passes, 474 old Hall failures, and zero old tail-detection misses. It shares generation with the earlier experiment; this is not an independent generator.

The regenerated 713-row TSV has SHA256

```text
157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572
```

Separately implemented Python arithmetic gives:

| Necessary test | Rejected / 713 |
|---|---:|
| Prior localized/priced test | 652 |
| All-source spill, old quadratic envelope | 654 |
| Spill plus new closed-form capped envelope | 672 |
| Spill plus integer prefix envelope | 694 |

This newly rejects 42 of the former 61 sampled survivors; 19 remain. Their zero-based row IDs and all newly rejected row IDs are frozen. The raw corpus, detailed arrays, generation output, code and surviving examples are preserved in the portable bundle and reproducible from pinned inputs. This is NOT a 42-state frontier reduction.

On the frozen 812 difficult profiles, all-source spill tightens one further cap vector (row 811, scalar state 6085). Full-capacity rejections increase from 630 to 631; uniform interval detections stay 773 and adaptive interval detections stay 812. That residue was already excluded by other tails; this is a simpler explanation, not new whole-state closure.

## 7. Local verification and hostile boundaries

`verify_capped_spill.py` has no imports from production scanners. It checks 133,586 exhaustive selected-incidence configurations for delta=1,2,4, yielding 400,758 pressure/cap/envelope checks. The domain includes binary selected matrices, zero demands, positive residuals, selected-label forcing and q+rho<=a. These matrices are not claimed to be realized graphs; the new arithmetic implications need only the explicitly tested incidence and pressure hypotheses.

A second implementation brute-enumerates excess vectors and compares their exact maxima to the prefix dynamic programme on 3,000 seeded instances, including 1,821 empty projections. All values agree. The three standing hostile q-tail examples are rechecked by exhaustive source subsets: their old negative Hall minima and nondeficient tails remain intact. Their bridge rejections are stated, not silently added.

Two audit traps:

* Never charge zero-label excess as available positive-label excess; it is subtracted through M0.
* Never omit +f_w in C_{eta,w}. For s=(1,0,0), two identical selection rows (1,1,0), rho=(1,1), and delta=2, Esel=3 and eta=0 give M=2 and f_w=1. The valid bound has C=2. Omitting f_w gives C=1 and falsely rules out d_w=1, even though the positive label has e=1. This is an incidence-domain counterexample to double counting, not a positive-surplus graph.

The canonical bridge, endpoint-excess implication and incoming cap still require external specialist review. No q-layer theorem is automatically transferred to the newly modified caps without rechecking its hypotheses. The finite promoted frontier stays 1,971 exclusions / 3,607 survivors and 977 whole-state closures; the 2,655-candidate cross-audit remains a separate gate.
