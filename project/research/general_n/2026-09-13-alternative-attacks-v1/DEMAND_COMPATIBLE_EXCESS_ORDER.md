# Demand-compatible excess order-statistic source cap

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note sharpens the selected-excess threshold mechanism by retaining two pieces of information that the global `h_l` counts discard:

1. a source with `q` selected outgoing incidences needs `q` **distinct** compatible labels;
2. selected-edge forcing restricts compatibility by the source residual degree `rho`.

The result is a pointwise order-statistic upper bound on the incoming load `p_u`. It contains all threshold caps `h_1,h_2,h_3,...` simultaneously and is particularly strong when low-`rho` sources can use only a small demand class.

## 1. Setup

Use the canonical bridge notation. For every positive-demand label `i`, put

```text
e_i=x_i-s_i>=0.
```

For a selected positive-demand incidence `ui`, the established lemmas give

```text
s_i <= rho_u,                                         (1)
p_u-rho_u+1 <= e_i.                                  (2)
```

Let `S_u^+` be the set of positive-demand labels selected at source `u`, and write

```text
q_u^+=|S_u^+|.
```

The selected cross-edges at one source have distinct A-endpoints, so the labels in `S_u^+` are distinct.

For an integer `rho>=1`, define the demand-compatible label class

```text
I_rho={i : 0<s_i<=rho}.                               (3)
```

Order the excesses in this class nonincreasingly:

```text
eta_1^(rho) >= eta_2^(rho) >= ... >= eta_m^(rho),    (4)
```

where `m=|I_rho|`.

## 2. Order-statistic source-cap theorem

**Theorem.** Let `u` be a source with `q_u^+>0`. Then necessarily

```text
q_u^+ <= |I_(rho_u)|,                                 (5)
```

and

```text
p_u <= rho_u-1 + eta_(q_u^+)^(rho_u).                (6)
```

### Proof

By selected-edge forcing (1), every label in `S_u^+` lies in `I_(rho_u)`. Because the selected labels at one source are distinct,

```text
|S_u^+|=q_u^+<=|I_(rho_u)|,
```

which is (5).

By selected-excess (2), every `i in S_u^+` satisfies

```text
e_i >= p_u-rho_u+1.                                  (7)
```

Thus there are at least `q_u^+` distinct labels in the compatible class whose excess is at least `p_u-rho_u+1`. The `q_u^+`-th largest compatible excess therefore obeys

```text
eta_(q_u^+)^(rho_u) >= p_u-rho_u+1.
```

Rearranging gives (6). QED.

No identities of selected representatives are fixed. The theorem uses only the fact that a source must find enough distinct compatible labels above its required excess threshold.

## 3. Demand-compatible threshold form

For `l>=0`, define

```text
h_l^(rho)=#{i : 0<s_i<=rho, e_i>=l}.                 (8)
```

If

```text
q_u^+ > h_l^(rho_u),                                 (9)
```

then not all selected positive-demand labels at `u` can have excess at least `l`. Equation (2) therefore forces

```text
p_u-rho_u+1 <= l-1,
```

or

```text
p_u <= rho_u+l-2.                                    (10)
```

This is the demand-compatible version of the earlier global threshold cap. Equation (6) is the exact order-statistic form obtained by retaining all thresholds at once.

The global count

```text
h_l=#{i:e_i>=l}
```

is weaker because `h_l^(rho)<=h_l`. The difference can be large for low-`rho` sources.

## 4. Combined source cap

Whenever the bridge also supplies the basic incoming and endpoint caps

```text
p_u <= rho_u+b-a-1,
p_u <= b-1-q_u,                                       (11)
```

an active all-positive-demand source may be bounded by

```text
p_u <= min(
          rho_u+b-a-1,
          b-1-q_u,
          rho_u-1+eta_(q_u)^(rho_u)
        ).                                            (12)
```

In a family where every selected label has positive demand, `q_u^+=q_u`, so (12) applies directly.

If zero-demand selected labels are possible, (6) must use `q_u^+`, not the total selected count `q_u`, unless a separate argument identifies the two.

## 5. Adjacent N34 family

In the adjacent family currently under study,

```text
s_i in {2,3},
rho_u in {1,2,3},
```

and every label has positive demand. Hence:

- a `rho=2` source can select only demand-two labels, so its order statistic is taken **only among the demand-two excesses**;
- a `rho=3` source can select either demand class, so its order statistic is taken among all label excesses;
- `rho=1` sources have no compatible positive-demand label and therefore have `q=0`.

For example, if the demand-two excess multiset is

```text
{11,0}
```

then any `rho=2` source with `q=2` must select both demand-two labels. Equation (6) gives

```text
p_u <= 2-1+0 = 1,
```

regardless of how many positive-excess demand-three labels exist. A global `h_1` count misses this demand-class restriction.

## 6. Computational consequence

For a fixed excess profile, (12) gives an independent integral cap for every source before any incidence identities are chosen. Thus one can:

1. enumerate only excess profiles left by a cheaper scalar screen;
2. compute the compatible excess order statistics;
3. tighten every source incoming cap by (12);
4. minimize `sum q_u p_u` under those caps;
5. when zero-excess exact-demand labels occur, combine the profile cap with the endpoint-order source objective.

A profile whose total tightened incoming capacity is below the required `Q=sum p_u` is excluded immediately.

This creates a useful hierarchy:

```text
global h_2 screen
  -> capacity-order endpoint screen
  -> demand-compatible excess-order profile screen
  -> exact incidence rigidity only if still necessary.
```

The third stage is still selection-free with respect to representative identities.

## 7. Relation to the aggregate selected-excess inequality

The earlier aggregate inequality

```text
sum_u q_u^+ max(0,p_u-rho_u+1)
 <= sum_i x_i e_i
```

sums the same pointwise selected-excess constraints. The present theorem retains their **order structure at each source** instead of summing it away. Neither statement should be substituted for the other without checking the direction needed by the argument.

## Trust boundary

This theorem depends only on selected-edge forcing, selected-excess, and distinct selected A-endpoints at a fixed source inside the canonical selected/residual bridge. It does not use graph switching, does not assume a fixed global representative geometry, and does not assert that the resulting scalar conditions are sufficient for a graph to exist. External checking of the bridge and this derivation remains open.
