# Follow-up to blind external-AI red-team of n=29

11 September 2026. The user supplied a hostile review produced by a separate ChatGPT instance without the project background. This file records the review's substantive findings and the current project's independent follow-up. It is not human peer review.

## Overall disposition

The blind reviewer reported no fatal flaw and upgraded its assessment of the n=29 work from an interesting computational claim to a serious candidate proof. Its principal attacks were directed at exactly the right trust boundaries: selected/residual injections, residual activity, threshold capacity, isolated-C, the corrected late LP normalization, exact Farkas semantics, and the hand assembly.

Our follow-up agrees with that overall disposition. No candidate status is promoted to theorem status.

## Findings that survived hostile review

The reviewer independently reconstructed and failed to break:

- the complement/quasi-edge construction;
- one selected representative per missing unordered B-pair;
- `s_i<=rho_u`;
- `d_i<=rho_u+rho_w`;
- supplement forcing;
- endpoint load;
- residual activity;
- the expanded threshold-capacity lemma;
- the isolated-C exclusion;
- the corrected v2 grouped late model;
- exact integer Farkas verification;
- the Delta=15 witness/equality argument;
- the Delta=17 pointwise exclusion;
- the Delta=18..27 residual h-index argument;
- the cited non-bipartite dominating-edge dependency.

The review specifically identified the unique-B-exception property as the mechanism preventing several apparent selected/residual collisions. This matches the current bridge audit.

## Independent charging-domain census

The reviewer independently enumerated the nondecreasing integer charging profiles for `a=12,b=16` and obtained

```text
t=2: 9251
t=3: 4867
t=4: 2032
t=5:  586
t=6:   79
t=7:    1
t=8:    0
```

We independently regenerated the same census from scratch on 11 September and obtained exactly the same seven values. This is independent confirmation of the front end of the n=29 Delta=16 finite calculation.

Reproduction script: [`charging_domain_census.py`](charging_domain_census.py). It uses only the Python standard library and exact `Fraction` arithmetic.

## Independent graph-atlas bridge regression

The reviewer reported an exhaustive NetworkX graph-atlas check through order 7. We independently reproduced it.

Results:

```text
unlabeled diameter-two-edge-critical isomorphism types through order 7: 21
maximum-degree rooted cases:                                           50
admissible selected-quasi-edge configurations:                         58
bridge failures found:                                                  0
```

For every configuration we checked:

- exact ledger `e(F)=r+t` and `sum d_i=2(r+t)`;
- label demand and `S>=r+2t`;
- selected-edge injection;
- `d_i<=rho_u+R_i`;
- `d_i<=rho_u+rho_w`;
- `d_i<=rho_u+q_u-1`;
- supplement forcing `rho_w+q_w>=q_u-1`;
- source capacities;
- endpoint load `R_i+x_i>=q_u+p_u`;
- selected-source demand `s_i<=rho_u`.

All 58 configurations passed.

The surplus values occurring in these small examples are only

```text
t in {-3,-2,-1,0}.
```

Therefore this regression does **not** independently exercise residual activity, charging, or threshold capacity, all of which rely on the positive-surplus dense regime. It is evidence for the base bridge only.

Reproduction script: [`atlas_bridge_regression.py`](atlas_bridge_regression.py). It requires NetworkX and uses only `graph_atlas_g()`; no project verifier is imported.

## New analytic simplification supplied by the reviewer

For integer `0<=s<=11`,

```text
s(13-2s)/(12-s) <= 5/2,
```

with equality only at `s=4`, because

```text
5/2 - s(13-2s)/(12-s)
  = (s-4)(4s-15)/(2(12-s)) >= 0.
```

For n=29, Delta=16 this bounds the charging sum by `12*(5/2)=30`. Since the bridge requires

```text
16+2t <= sum_i s_i(13-2s_i)/(12-s_i),
```

we get `t<=7`, hence `m<=215`. This removes the old `m=216..232` generic scan from the logical dependency chain.

At `m=215`, `t=7`, equality forces all twelve demands to equal four. Then

```text
S=48,
r>=16+12*(4*3/8)=34,
S>=r+14 -> r<=34,
```

so `r=34`. Residual activity gives

```text
z_4<=floor((34-16)/3)=6,
```

but threshold capacity requires

```text
96=2W_4<=z_4^2-z_4+20<=50,
```

contradiction. Thus `m=215` is also a hand case.

The full cross-order propagation is recorded in

`project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md`.

It also removes computation from the logical chain for:

- n=28, Delta=15, `m>=203`;
- n=30, Delta=17, `m>=228`;
- n=30, Delta=16, `m>=234`.

Historical workflows remain preserved as corroborating evidence only.

## Threshold-capacity presentation

The blind reviewer agreed that the compressed threshold paragraph in the original standalone bridge was not self-contained enough, even though the companion expanded lemma repairs it. The current project follow-up therefore treats self-contained expansion in the reviewer-facing bridge as a worthwhile editorial hardening step.

That hardening is now implemented in [`../2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`](../2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md).

A separate 11 September cross-order re-audit also found and corrected a non-blocking sign/order typo in the explanatory algebra of the expanded threshold lemma. The corrected sign proves the same final inequality; no numerical result changed.

## Remaining risk ranking

The blind reviewer's risk ranking is consistent with the project's own:

1. graph-to-late-LP representation / averaging normalization;
2. residual activity;
3. threshold capacity and its presentation;
4. independent reconstruction of the exact finite verifier.

No theorem status is asserted. The value of the blind pass is that it attacked the proof at its genuine failure modes and found a simplification rather than a counterexample.
