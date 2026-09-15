# Aggregate receiver-price necessary conditions — working lemma

Date: 15 September 2026. Status: **proved as a necessary condition; empirical coverage of the canonical forced-core rejections is still being tested.** This note does not promote any finite closure and does not claim the unrestricted conjecture.

Fix a forced core parameter `r`. Let

- `h = #{i : s_i <= r}`;
- `U = {u : rho_u=r, q_u=h}` and `m=|U|`;
- an eligible receiver `v` be a vertex outside `U` with `q_v <= h+r-1`, `q_v+rho_v >= h-1`, and `c_v^0=rho_v+b-a-1>0`;
- `c_v=min(c_v^0,m)`.

Every realization of the forced-core routing has `h` labelled core receivers/bins, each requiring total receiver capacity at least `m`, and every eligible receiver can be dedicated to at most one bin. Therefore

```math
\sum_v c_v \ge hm. \tag{1}
```

This is the scalar receiver-capacity inequality. It is weaker than the exact partition DP but contains no partition state.

For a threshold `tau>r`, put

```math
R_tau = \sum_{rho_v\ge tau} q_v,
\qquad
D_tau = \sum_{s_i\ge tau} s_i,
\qquad
\ell_v(tau)=\mathbf 1_{rho_v\ge tau}(q_v-r)_+.
```

Selecting receiver `v` for any core bin incurs threshold loss `ell_v(tau)`. Relax the dedicated integral receiver choice to variables `0<=x_v<=1` satisfying

```math
\sum_v c_v x_v \ge hm.
```

Let `F_tau` be the minimum of `sum_v ell_v(tau)x_v` over this fractional cover. Any integral dedicated routing has loss at least `F_tau`. The LP dual/Lagrangian bound gives, for every `mu>=0`,

```math
F_tau \ge \mu hm-\sum_v\max\{0,\mu c_v-\ell_v(tau)\}. \tag{2}
```

Since a realization must retain at least `D_tau` high-threshold incidence from raw supply `R_tau`, it is necessary that, for every `mu>=0`,

```math
D_tau+\mu hm
\le
R_tau+\sum_v\max\{0,\mu c_v-\ell_v(tau)\}. \tag{3}
```

Equivalently, if the reverse strict inequality holds for any `mu`, the profile is impossible. Because the dual objective is piecewise linear, it is enough computationally to test the finitely many breakpoints `mu=ell_v/c_v` (plus endpoints); equivalently the fractional cover can be solved by sorting receivers by `ell_v/c_v`.

For an integer contradiction one may use `ceil(F_tau)`: if

```math
R_tau-\lceil F_tau\rceil < D_tau,
```

then the profile is impossible.

## Current empirical stress test

An instrumented version of the independently structured type-multiplicity scanner distinguishes exact-partition failures from failures already witnessed by (1) or the fractional bound above. On the five newly audited closures `9858,10296,10507,10858,10898` and on three previously audited closures chosen to diversify the core shape, `10850 (r=1,h=1)`, `2812 (r=2,h=3)`, and `9634 (r=3,h=3)`, every forced-core rejection was already detected by the aggregate conditions:

- `partition_only_fail = 0`;
- `partition_high_only_fail = 0`.

This is encouraging evidence, not a completeness claim. Heavier `h=4,5` states still need stress testing, and the full canonical profile population has not been shown to be captured by (1)–(3).
