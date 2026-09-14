# Layered receiver capacity — frozen internal audit

14 September 2026.

## Status

The identities and theorem-safe upper bounds in [`LAYERED_RECEIVER_CAPACITY.md`](LAYERED_RECEIVER_CAPACITY.md) have passed an independent finite arithmetic verifier.

Internally audited statements include:

- the exact layer-cake identity `sum_w min(P_w,y_w)=sum_k |A_k cap B_k|`;
- the comonotone marginal upper bound `H<=sum_k min(alpha_k,beta_k)`;
- equivalence with independently sorting the `P` and `y` multisets;
- the Murty-specific capacity-layer implications from the universal `P` caps;
- the residual-budget bound on high-`rho` receiver layers;
- the resulting scalar layered upper bound on exact Hall receiving capacity.

No whole-state frontier count changes here.

## GitHub Actions record

```text
workflow:        verify layered receiver capacity
run id:          34848254327
head sha:        a9cee9e5362211e9192727c185bdee5266b4c959
conclusion:      success
artifact id:     10349011436
artifact name:   layered-receiver-capacity-verification
artifact digest: sha256:dc9fb9d8c7a473cdbe109f16e20ecea03d19e80393d9b5ea4f7f8a7af3187fd4
```

## Verification totals

```text
arbitrary sequence trials:          5,000
synthetic Murty-like trials:       10,000
strict comonotone information loss: 4,675
```

The nonzero strict-loss count is useful: the comonotone projection is genuinely weaker than exact target identity on many profiles, so its reach must be measured empirically rather than assumed.

## Trust boundary

This is internal finite verification, not external mathematical review. The Murty-specific scalar layer bound inherits residual activity and the universal target-capacity bounds from the canonical bridge. Passing the layered test does not imply Hall feasibility; failure is a valid Hall certificate.
