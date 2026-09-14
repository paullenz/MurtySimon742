# Localized selected excess: a stronger canonical incoming cap

14 September 2026. **Candidate universal hand consequence of the canonical bridge, with independent-implementation finite checks. External mathematical review remains OPEN. No whole-state exclusion or unrestricted Murty-Simon proof is promoted.**

This checkpoint continues the two-defect and weighted-tail programme. It incorporates, rather than duplicates, the concurrent [selected-excess tail-loss identity](../2026-09-14-type-compressed-orientation-hall-v1/SELECTED_EXCESS_TAIL_LOSS_BUDGET.md) and [interval-tail budget](../2026-09-14-q-tail-interval-budget-v1/README.md). Those identities rewrite the existing capacities. The result here **strengthens the capacities themselves** by locating excess already forced into a particular demand block.

The old target-Hall and selected-incidence relaxations can each be feasible while their shared selected-excess requirements are inconsistent. This note supplies an explicit coupling between them.

## 1. Canonical hypotheses

Use the [canonical selected/residual bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md). There are a labels and b B-vertices; structural surplus is t>0. Write

```text
x_i=s_i+e_i,  e_i>=0,  Esel=sum_i e_i,
r=sum_u rho_u,  S=sum_i s_i,  Q=sum_u q_u,
D0=S-r-2t>=0,
Q=r+2t+D0+Esel,
c_u=q_u+rho_u<=a,  rho_u>=1.
```

Each source u selects q_u DISTINCT labels, and a selected incidence ui implies s_i<=rho_u. For every selected positive-demand label i at u, the bridge also gives

```text
d_i<=rho_u+q_u-1,
R_i+x_i>=q_u+p_u,
d_i=R_i+s_i.
```

Combining these yields the endpoint-excess inequality

```text
p_u<=rho_u-1+e_i.                                    (1)
```

The last equality d_i=R_i+s_i is used ONLY for s_i>0. Zero-demand labels must not be treated as positive ones. The theorem below carefully places all zero-demand labels inside its low-demand block.

## 2. Localizing the excess budget

For an integer residual threshold eta>=0 define

```text
U_eta={u:rho_u<=eta},
L_eta={i:s_i<=eta},
m_eta=|L_eta|,
S_eta=sum_{i in L_eta}s_i,
Q_eta=sum_{u in U_eta}q_u,
C_eta=Esel+S_eta-Q_eta.                               (2)
```

Eta is a residual/demand-block threshold; tau remains the q-tail threshold. Neither is the structural surplus t.

All selections from U_eta land in L_eta, so x(L_eta)>=Q_eta. Consequently

```text
C_eta>=0                                             (3)
```

is necessary. A negative C_eta rejects selected-incidence feasibility; it must not be rounded up.

Fix a source w OUTSIDE U_eta, with q_w>0, and let k be the number of its selected labels lying in L_eta. These are additional incidences, disjoint from the source incidences already counted in Q_eta. Therefore

```text
x(L_eta)>=Q_eta+k,
e(L_eta)>=Q_eta+k-S_eta.                             (4)
```

The q_w-k selected labels outside L_eta have positive demand. If p_w>=rho_w, put d=p_w-rho_w+1>=1. Equation (1) forces e_i>=d on each of these DISTINCT labels. Add their excess to (4):

> **Localized excess inequality**
>
> ```text
> C_eta >= k+(q_w-k)d,
> d=p_w-rho_w+1>=1.                                  (5)
> ```

The lower bound in (4) need not itself be nonnegative. Adding a valid lower bound to the positive-demand excess lower bound is legitimate regardless. The restriction rho_w>eta is essential: without it, (4) could count w twice.

## 3. Explicit cap without knowing the selected labels

Let

```text
kstar=min(m_eta,q_w,C_eta).
```

If q_w>kstar, then

> ```text
> p_w <= rho_w-1 + floor((C_eta-kstar)/(q_w-kstar)).   (6)
> ```

If q_w=kstar, this threshold supplies no cap. All quantities are integers.

**Proof.** If p_w<=rho_w-1 there is nothing to prove. Otherwise (5) implies k<=C_eta as well as k<=m_eta,q_w. If C_eta<q_w, the right side of (5) is at least q_w for d>=1, a contradiction; the displayed floor is zero. If C_eta>=q_w and q_w>kstar, then m_eta<q_w. The ratio (C_eta-k)/(q_w-k) is nondecreasing in k, so its maximum is attained at kstar=m_eta. This proves (6).

Take the minimum of (6), over valid thresholds with rho_w>eta, and ALL previously legitimate target caps. Denote the result by P_w^loc. Keep the residual/incoming, simple-degree, exact potential-pair and existing selected-excess caps. A negative cap is infeasibility.

The finite implementations evaluate eta=0 and all distinct rho values. These are a stated finite subset of the valid thresholds, not a claim that every possible positive threshold must be examined to justify the theorem.

### Exact recovery of the existing zero-demand cap

At eta=0, positive residual activity gives U_eta empty. L_eta consists exactly of the z zero-demand labels, S_eta=0 and C_eta=Esel. Thus kstar=min(z,q_w,Esel), and (6) is precisely the existing zero-demand-corrected selected-excess cap. There is NO assumption z<=Esel.

The new content is eta>0: selected excess forced into low-positive-demand labels can no longer be spent again at every other target.

## 4. Coupling to the two-defect budget

Substituting Esel=Q-r-2t-D0 into (2) gives

```text
C_eta = sum_{rho_u>eta}q_u-r-2t-D0+S_eta.             (7)
```

Thus this localization is directly coupled to the exact bridge, not an extra freely chosen scalar parameter.

A particularly clean corollary is

```text
q_w>C_eta and rho_w>eta  =>  p_w<=rho_w-1.            (8)
```

Let Z consist of sources for which some tested eta certifies (8), counting each source once. Write delta=b-a. The old incoming cap is rho_w+delta-1, so each source in Z loses at least delta units of incoming capacity. Summing, using sum p=Q and the two-defect identity, yields

> ```text
> 2t+D0+Esel+delta*|Z| <= b(delta-1).                  (9)
> ```

The full non-double-counted loss inequality is stronger:

```text
2t+D0+Esel+sum_w(rho_w+delta-1-P_w^loc)
 <= b(delta-1).                                     (10)
```

Unlike a rewriting of the old sum-P test, (10) can newly exclude profiles because P^loc is smaller.

For adaptive high-q tails, simply substitute P^loc into the existing interval budget. With h_w=rho_w+delta-1,

```text
Lambda_loc=sum_w(h_w-P_w^loc),
J_w(tau)=#{u!=w:tau<=q_u<=c_w+1},
Omega_loc(tau)=sum_w(P_w^loc-J_w(tau))_+,
G=b(delta-1)-(2t+D0+Esel),
```

we obtain the valid sufficient inequality

```text
Lambda_loc+Omega_loc(tau)>sum_{q_u<tau}q_u+G
 => a deficient high-q tail.                        (11)
```

The exact reverse-compatibility correction from the interval package remains available. No equality between the arbitrary Hall minimum and a tail minimum is assumed.

## 5. Two old surviving PROFILE witnesses now fail

Both examples below have a=15, b=18, t=1 and D0=0. They are specific profiles associated with scalar states 1626 and 2984, NOT complete enumerations of those states.

### Profile associated with state 1626

```text
s=[1,2,2,3,3,3,3,3,3,4,4,4,4,4,4]
rho=[1,1,1,1,1,1,1,1,3,3,3,3,4,4,4,4,4,5]
q=[0,0,0,1,1,1,1,1,3,3,6,7,2,3,6,6,7,3]
r=45, S=47, Q=51, Esel=4.
```

An independent augmenting-path implementation verifies old target flow 51 and a feasible selected-incidence system. At eta=1, all five selections of the low-residual sources must use the sole demand-one label. Thus Q_eta=5, S_eta=1 and C_eta=4+1-5=0. Every one of the ten positive-q sources outside U_eta has p_w<=rho_w-1.

After retaining the exact potential-pair caps as well,

```text
P^loc=[3,3,3,3,3,3,3,3,2,2,2,2,3,3,3,3,2,4],
sum P^loc=50 < Q=51.
```

This profile is excluded. The simple exposed-source inequality (9) is only an equality here: 6+3*10=36. The potential-pair cap supplies the additional loss needed for strict contradiction. Dropping that cap would miss this full-source contradiction.

### Profile associated with state 2984

```text
s=[1,3,3,3,4,4,4,4,4,4,4,4,4,4,4]
rho=[1,1,1,1,1,1,3,3,4,4,4,4,4,4,4,4,4,4]
q=[0,0,1,1,1,1,3,3,1,1,3,6,6,6,6,6,6,6]
r=52, S=54, Q=57, Esel=3.
```

The old target flow is 57 and selected-incidence feasibility also passes. Now Q_eta=4, S_eta=1, C_eta=3+1-4=0 at eta=1. There are twelve exposed positive-q sources. Equation (9) fails by five:

```text
5+3*12=41 > 36.
```

Equivalently, sum P^loc=52<57. The old high-q tail margins were all nonnegative; the new tau=1 margin is -5.

The old scalar/incidence relaxation therefore cannot be used as evidence against this stronger bridge inequality. Conversely, these two exclusions do NOT show that all remaining profiles or either complete scalar state is excluded.

## 6. Independent implementation and frozen reconnaissance

`verify_localized_excess.py` uses Python's standard library and a separately structured dense-residual Edmonds-Karp implementation, with no imports from either production C++ scanner. `LOCALIZED_EXCESS_VERIFICATION.json` freezes its results:

```text
exhaustive selected-incidence configurations: 133,586
integer floor-optimization cases:                6,880
seeded ledger-preserving incidence mutations:    3,000
preserved hostile examples rechecked:                3
old surviving witness profiles newly excluded:       2
```

The exhaustive domain includes binary selected-incidence matrices with 1<=a<=3 and 1<=b<=4, all allowed demands, positive residuals, selected-label forcing and source caps. The mutations preserve the selected column degrees, positive-surplus scalar identity, source capacities and incidence forcing. They are NOT jointly realized F-graphs, residual matrices or quasi-edge systems. Same-assistant independent implementation is not external reproduction.

On all 812 frozen difficult profiles:

| Check | Old caps | Localized caps |
|---|---:|---:|
| Uniform weighted-tail pressure detects | 476 | 773 |
| Activation-only receiver bound detects | 794 | 808 |
| Some exact high-q tail is deficient | 812 | 812 |
| Tau=1 tail is deficient | 0 | 630 |

Cap vectors tighten on 748 profiles. The first deficient threshold changes from 2:426, 3:191, 4:195 to 1:630, 2:117, 3:65. These are reconstructions of the frozen diagnostic, not a new all-order theorem. The remaining 39 uniform-weight misses show that uniform weights are still not enough.

The old exact fixed-weight obstruction belongs to the OLD capacity model; do not automatically transfer it to P^loc. Adaptive thresholds and the exact q-layer fallback remain appropriate.

## 7. Hostile examples and trust boundary

All three examples in `MURTY_Q_TAIL_HALL_CONJECTURE.md` retain target-Hall failure without a deficient old high-q tail. The verifier reproduces this rather than hiding them.

For the one-(1,1), six-(3,1), a=4,b=7 cap-only example with Esel=5,z=2, Q=19 forces S=14. Selected-incidence forcing at rho=1 allows at most two units of total positive demand. It is rejected for that explicit reason, not by changing the zero-demand quantifier.

The Esel=19,z=4 all-zero-demand example admits selected incidence but has S=0<r+2t. It violates the positive-surplus bridge ledger. The arbitrary-monotone-cap example supplies no full canonical bridge; its r=8 already exceeds choose(4,2), inconsistent with r+t=e(F) for t>0.

The hand proof depends on the canonical selected-label and endpoint-forcing implications. External review should particularly attack the derivation of (1), the source-disjoint count in (4), treatment of zero demands, and integer optimization in (6).

A bounded instrumented full-pilot experiment timed out before producing a complete durable table. It is explicitly NOT accepted as a complete replay or new whole-state exclusion. See `EXPERIMENT_LOG.md`.

The canonical frontier remains **1,971 exclusions / 3,607 survivors, with 977 whole-state closures**. The 2,655-candidate relational audit and separate promotion gate remain logically independent of this new cap. High-q-tail sufficiency and the unrestricted Murty-Simon conjecture remain open.
