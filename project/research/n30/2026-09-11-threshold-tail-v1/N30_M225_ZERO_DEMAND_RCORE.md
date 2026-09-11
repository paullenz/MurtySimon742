# Exact treatment of the four zero-demand m=225 rows

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite hardening, not a new hand proof. Independent mathematical review remains open.**

The threshold-slack reduction leaves 211 ledger-tight rows at `n=30, Delta=16, m=225`. Of these, 207 have all thirteen demands positive and are exactly the sector studied by the preserved residual-budget RX-Hall programme. Four rows contain one zero demand:

```text
s=(0,2,3^11), rho=(1^7,2,3^8), r=33;
s=(0,3^12),   rho=(1^7,3^9),   r=34;
s=(0,3,4^11), rho=(1^6,3,4^9), r=45;
s=(0,4^12),   rho=(1^6,4^10),  r=46.
```

These four are not an exceptional mathematical regime once ledger tightness is used correctly.

Let

```text
s_i=max(0,d_i-R_i).
```

In the `m=225,t=1` ledger-tight sector,

```text
S=sum_i s_i=r+2.
```

But

```text
sum_i(d_i-R_i)=2e(F)-r=r+2,
```

so

```text
sum_i max(0,d_i-R_i)=sum_i(d_i-R_i).
```

Equality is possible only when every `d_i-R_i>=0`. Hence for every label, including a zero-demand label,

```text
d_i-R_i=s_i,
```

or equivalently

```text
d_i=R_i+s_i.                                      (1)
```

Therefore the same `(s,R,y)` label-state relation used by the positive-demand residual-budget Hall core is valid for these four rows. Keeping the established source types, the correct local supplement bound `p<=rho+2`, nested source/supplement transport, exact residual-column budget, total selected-incidence balance, RX1/RX2/RX3 compatibility and Hall domains formed from one or two source neighborhoods gives an exact finite necessary-condition model for each row.

All four models are infeasible. The preserved integer Farkas rays are in

```text
N30_M225_ZERO_DEMAND_RCORE_CERTS.json
```

and the standard-library checker

```text
verify_m225_zero_demand_rcore_exact.py
```

reconstructs every integer coefficient row and verifies the certificates without an LP solver or floating point. Their exact certificate right-hand sides are

```text
-761,
-998782,
-450,
-997665.
```

This removes the four zero-demand rows as a separate unresolved endpoint nuisance. It does **not** remove the remaining finite/computational dependence of the `m=225` equality branch: the 207 positive tight rows still rely on the residual-budget Hall programme plus the later two-template treatment of its seven hard survivors until those steps are converted into a hand argument.
